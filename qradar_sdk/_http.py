"""
Low-level HTTP session wrapper for the QRadar REST API.

Supports two authentication mechanisms that QRadar provides:
  1. **SEC token** – pass ``sec_token`` (generated in QRadar under
     Admin → Authorized Services).  Sent as the ``SEC`` request header.
  2. **Basic auth** – pass ``username`` and ``password``.

Example::

    from qradar_sdk._http import QRadarSession

    session = QRadarSession(
        host="qradar.example.com",
        sec_token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        verify_ssl=False,      # disable TLS verification for self-signed certs
    )
    resp = session.get("/siem/offenses", params={"filter": "status=OPEN"})
"""

from __future__ import annotations

import json
from typing import Any, Dict, Optional, Union
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import QRadarAPIError, QRadarAuthError, QRadarNotFoundError, QRadarRateLimitError

_DEFAULT_VERSION = "26.0"
_DEFAULT_TIMEOUT = 30


class QRadarSession:
    """Manages an HTTP session to a QRadar console."""

    def __init__(
        self,
        host: str,
        *,
        sec_token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        version: str = _DEFAULT_VERSION,
        verify_ssl: Union[bool, str] = True,
        timeout: int = _DEFAULT_TIMEOUT,
        max_retries: int = 3,
    ) -> None:
        if not sec_token and not (username and password):
            raise QRadarAuthError(
                "Provide either 'sec_token' or both 'username' and 'password'."
            )

        scheme = "https"
        base = host.rstrip("/")
        if not base.startswith(("http://", "https://")):
            base = f"{scheme}://{base}"
        self.base_url = base.rstrip("/") + "/api"

        self.version = version
        self.timeout = timeout
        self.verify_ssl = verify_ssl

        self._session = requests.Session()
        self._session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Version": version,
        })

        if sec_token:
            self._session.headers["SEC"] = sec_token
        else:
            self._session.auth = (username, password)

        retry = Retry(
            total=max_retries,
            backoff_factor=0.5,
            status_forcelist=[502, 503, 504],
            allowed_methods=["GET", "HEAD"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount("https://", adapter)
        self._session.mount("http://", adapter)

    # ------------------------------------------------------------------
    # Public helpers
    # ------------------------------------------------------------------

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_body: Any = None,
        data: Any = None,
        range_header: Optional[str] = None,
        fields: Optional[str] = None,
        filter_expr: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Any:
        """Execute an HTTP request and return the parsed JSON body (or raw text).

        :param method: HTTP verb (GET, POST, PUT, PATCH, DELETE, …).
        :param path: API path relative to ``/api``, e.g. ``/siem/offenses``.
        :param params: URL query string parameters.
        :param headers: Extra request headers.
        :param json_body: Request body serialised as JSON.
        :param data: Raw request body (bytes / str).
        :param range_header: Value for the ``Range`` header (e.g. ``0-49``).
        :param fields: Comma-separated list of fields to include in the response.
        :param filter_expr: AQL-style filter expression.
        :param sort: Sort expression.
        :returns: Parsed JSON as ``dict`` / ``list``, or raw ``str`` on failure.
        :raises QRadarAPIError: on HTTP 4xx / 5xx responses.
        """
        url = self.base_url + path

        merged_params: Dict[str, Any] = {}
        if params:
            merged_params.update({k: v for k, v in params.items() if v is not None})
        if fields is not None:
            merged_params["fields"] = fields
        if filter_expr is not None:
            merged_params["filter"] = filter_expr
        if sort is not None:
            merged_params["sort"] = sort

        merged_headers: Dict[str, str] = {}
        if headers:
            merged_headers.update(headers)
        if range_header is not None:
            merged_headers["Range"] = f"items={range_header}"

        resp = self._session.request(
            method=method.upper(),
            url=url,
            params=merged_params or None,
            headers=merged_headers or None,
            json=json_body,
            data=data,
            verify=self.verify_ssl,
            timeout=self.timeout,
        )

        self._raise_for_status(resp)

        if resp.content:
            try:
                return resp.json()
            except ValueError:
                return resp.text
        return None

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Any:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Any:
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Any:
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Any:
        return self.request("DELETE", path, **kwargs)

    def paginate(
        self,
        path: str,
        page_size: int = 50,
        max_items: Optional[int] = None,
        **kwargs: Any,
    ):
        """Iterate over all pages of a paginated list endpoint.

        Yields each page (a list of items) until all pages are consumed.

        :param path: API path.
        :param page_size: Number of items per page.
        :param max_items: Stop after this many items (``None`` = no limit).
        :param kwargs: Extra arguments forwarded to :meth:`get`.
        """
        start = 0
        fetched = 0
        while True:
            end = start + page_size - 1
            page = self.get(path, range_header=f"{start}-{end}", **kwargs)
            if not page:
                break
            yield page
            fetched += len(page)
            if max_items is not None and fetched >= max_items:
                break
            if len(page) < page_size:
                break
            start += page_size

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()

    def __enter__(self) -> "QRadarSession":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _raise_for_status(resp: requests.Response) -> None:
        if resp.ok:
            return
        try:
            detail = resp.json()
            message = detail.get("message") or detail.get("description") or str(detail)
        except ValueError:
            message = resp.text or resp.reason or "Unknown error"

        if resp.status_code == 401:
            raise QRadarAuthError(f"Authentication failed: {message}")
        if resp.status_code == 404:
            raise QRadarNotFoundError(resp.status_code, message, resp)
        if resp.status_code == 429:
            raise QRadarRateLimitError(resp.status_code, message, resp)
        raise QRadarAPIError(resp.status_code, message, resp)
