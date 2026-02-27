#!/usr/bin/env python3
"""
Generate a Python SDK client from the QRadar OpenAPI 3.0 specification.

Usage:
    python3 generate_sdk.py [--spec openapi.yaml] [--output qradar_sdk]

Produces a ``qradar_sdk`` package that wraps every endpoint defined in the
spec.  Each OpenAPI tag becomes its own module inside ``qradar_sdk/api/``.
"""

import argparse
import keyword
import os
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _to_snake(name: str) -> str:
    """Convert camelCase / mixed strings to snake_case identifiers."""
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    s = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s)
    s = s.replace('-', '_').replace(' ', '_')
    s = re.sub(r'_+', '_', s).lower().strip('_')
    # Only avoid Python *keywords* (syntax errors), not builtins
    if keyword.iskeyword(s):
        s = s + '_'
    return s


def _sanitise_module_name(tag: str) -> str:
    """Turn an API tag into a valid Python module name."""
    name = _to_snake(tag)
    # Avoid clashing with stdlib/builtins
    if name in ('auth', 'help', 'type', 'input', 'filter', 'id', 'list',
                'set', 'map', 'hash', 'format', 'open', 'import'):
        name = name + '_api'
    return name


def _path_to_method_name(method: str, path: str) -> str:
    """Derive a readable snake_case method name from HTTP method + URL path."""
    parts = [method.lower()] + [
        re.sub(r'[{}]', '', p) for p in path.strip('/').split('/')
    ]
    joined = '_'.join(p for p in parts if p)
    return _to_snake(joined)


def _python_type(schema: dict) -> str:
    """Map an OpenAPI schema to a Python type hint string."""
    if not schema:
        return 'Any'
    t = schema.get('type', 'object')
    if t == 'integer':
        return 'int'
    if t == 'number':
        return 'float'
    if t == 'boolean':
        return 'bool'
    if t == 'array':
        items = schema.get('items', {})
        inner = _python_type(items) if items else 'Any'
        return f'List[{inner}]'
    if t == 'object':
        return 'Dict[str, Any]'
    return 'str'


def _collect_operations(spec: dict) -> dict:
    """
    Return a dict mapping tag -> list of operation dicts.

    Each operation dict has keys:
        method, path, operation_id, summary, parameters, request_body,
        response_type
    """
    ops_by_tag: dict = defaultdict(list)
    http_methods = ('get', 'post', 'put', 'patch', 'delete', 'head', 'options')

    for path, path_item in spec.get('paths', {}).items():
        # Collect path-level parameters
        path_params = path_item.get('parameters', [])
        for method in http_methods:
            operation = path_item.get(method)
            if not operation:
                continue
            tags = operation.get('tags', ['default'])
            tag = tags[0] if tags else 'default'

            # Merge path-level + operation-level parameters
            all_params = list(path_params) + list(operation.get('parameters', []))

            # Determine response type from 200/201 response schema
            resp_schema: dict = {}
            for code in ('200', '201'):
                resp = operation.get('responses', {}).get(code, {})
                content = resp.get('content', {})
                for _mime, media in content.items():
                    resp_schema = media.get('schema', {})
                    break
                if resp_schema:
                    break

            ops_by_tag[tag].append({
                'method': method,
                'path': path,
                'operation_id': operation.get('operationId', ''),
                'summary': operation.get('summary', ''),
                'parameters': all_params,
                'request_body': operation.get('requestBody'),
                'response_schema': resp_schema,
            })

    return dict(ops_by_tag)


# ---------------------------------------------------------------------------
# Code generators
# ---------------------------------------------------------------------------

_EXCEPTIONS_SRC = '''\
"""Custom exceptions for the QRadar SDK."""


class QRadarError(Exception):
    """Base exception for all QRadar SDK errors."""


class QRadarAPIError(QRadarError):
    """Raised when the QRadar API returns an unexpected HTTP status code."""

    def __init__(self, status_code: int, message: str, response=None):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"HTTP {status_code}: {message}")


class QRadarAuthError(QRadarError):
    """Raised when authentication fails."""


class QRadarNotFoundError(QRadarAPIError):
    """Raised when the requested resource is not found (HTTP 404)."""


class QRadarRateLimitError(QRadarAPIError):
    """Raised when the API rate limit is exceeded (HTTP 429)."""
'''


_HTTP_SRC = '''\
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
'''


def _generate_api_module(tag: str, operations: list) -> str:
    """Generate Python source for a single API tag module."""
    module_lines = [
        f'"""API methods for the ``{tag}`` tag."""',
        '',
        'from __future__ import annotations',
        '',
        'from typing import Any, Dict, List, Optional',
        '',
        'from .._http import QRadarSession',
        '',
        '',
        f'class {_class_name(tag)}:',
        f'    """Client for the QRadar ``{tag}`` API endpoints."""',
        '',
        '    def __init__(self, session: QRadarSession) -> None:',
        '        self._s = session',
        '',
    ]

    seen_names: set = set()

    for op in operations:
        method = op['method']
        path = op['path']
        summary = op.get('summary', '').strip()
        parameters = op.get('parameters', [])
        request_body = op.get('request_body')

        func_name = _path_to_method_name(method, path)
        # Deduplicate within the same tag module
        original = func_name
        counter = 2
        while func_name in seen_names:
            func_name = f'{original}_{counter}'
            counter += 1
        seen_names.add(func_name)

        # Collect path params (required positional), query/header params (optional keyword)
        path_params = [p for p in parameters if p.get('in') == 'path']
        optional_params = [p for p in parameters if p.get('in') in ('query', 'header')]

        # Build positional args for path params
        sig_parts = ['self']
        for p in path_params:
            sig_parts.append(_to_snake(p['name']))

        # Optional keyword arguments
        kw_args = []
        for p in optional_params:
            pname = _to_snake(p['name'])
            if pname in ('range',):
                pname = 'range_header'
            kw_args.append(f'{pname}: Optional[Any] = None')

        if request_body:
            kw_args.insert(0, 'body: Optional[Any] = None')

        # Extra generic kwargs forwarded to the session
        kw_args.append('**kwargs: Any')

        sig = ', '.join(sig_parts + kw_args)
        module_lines.append(f'    def {func_name}({sig}) -> Any:')

        # Docstring
        if summary:
            module_lines.append(f'        """{summary}"""')
        else:
            module_lines.append(f'        """Call {method.upper()} {path}"""')

        # Build URL (replace {param} with f-string values)
        url = path
        for p in path_params:
            pname = _to_snake(p['name'])
            url = url.replace('{' + p['name'] + '}', '{' + pname + '}')
        if path_params:
            module_lines.append(f'        url = f"{url}"')
        else:
            module_lines.append(f'        url = "{url}"')

        # Build params dict from optional query parameters
        query_params = [p for p in optional_params if p.get('in') == 'query'
                        and _to_snake(p['name']) not in ('fields', 'filter', 'sort')]
        hdr_params = [p for p in optional_params if p.get('in') == 'header'
                      and _to_snake(p['name']) not in ('range',)]

        if query_params:
            entries = ', '.join(
                f'"{p["name"]}": {_to_snake(p["name"])}'
                for p in query_params
            )
            module_lines.append(f'        params = {{{entries}}}')
            module_lines.append('        params = {k: v for k, v in params.items() if v is not None}')
            params_kwarg = ', params=params'
        else:
            params_kwarg = ''

        if hdr_params:
            entries = ', '.join(
                f'"{p["name"]}": {_to_snake(p["name"])}'
                for p in hdr_params
            )
            module_lines.append(f'        headers = {{{entries}}}')
            module_lines.append('        headers = {k: v for k, v in headers.items() if v is not None}')
            headers_kwarg = ', headers=headers'
        else:
            headers_kwarg = ''

        # Range header
        range_p = next((p for p in optional_params if _to_snake(p['name']) == 'range'), None)
        range_kwarg = ''
        if range_p:
            range_kwarg = ', range_header=range_header'

        # Handle special query params (fields, filter, sort)
        fields_kwarg = ''
        filter_kwarg = ''
        sort_kwarg = ''
        for p in optional_params:
            pname = _to_snake(p['name'])
            if p.get('in') == 'query':
                if pname == 'fields':
                    fields_kwarg = ', fields=fields'
                elif pname == 'filter':
                    filter_kwarg = ', filter_expr=filter'
                elif pname == 'sort':
                    sort_kwarg = ', sort=sort'

        # Body
        body_kwarg = ''
        if request_body:
            body_kwarg = ', json_body=body'

        call_args = f'url{params_kwarg}{headers_kwarg}{range_kwarg}{fields_kwarg}{filter_kwarg}{sort_kwarg}{body_kwarg}, **kwargs'
        module_lines.append(f'        return self._s.{method}({call_args})')
        module_lines.append('')

    return '\n'.join(module_lines)


def _class_name(tag: str) -> str:
    """Turn a tag name into a PascalCase class name."""
    return ''.join(w.capitalize() for w in re.split(r'[_\-\s]+', tag)) + 'API'


def _generate_client_src(tags_and_modules: list) -> str:
    """Generate the main QRadarClient source."""
    import_lines = []
    attr_lines = []
    doc_lines = []
    for tag, module_name, class_name in tags_and_modules:
        import_lines.append(f'from .api.{module_name} import {class_name}')
        attr_name = _to_snake(tag)
        attr_lines.append(
            f'        self.{attr_name}: {class_name} = {class_name}(session)'
        )
        doc_lines.append(f'    {attr_name}: :class:`~qradar_sdk.api.{module_name}.{class_name}`')

    imports = '\n'.join(import_lines)
    attrs = '\n'.join(attr_lines)
    doc_attrs = '\n'.join(doc_lines)

    return f'''\
"""
QRadar Python SDK – main client entry-point.

Usage::

    from qradar_sdk import QRadarClient

    client = QRadarClient(
        host="qradar.example.com",
        sec_token="<your-service-token>",
        verify_ssl=False,   # set to True (or a CA bundle path) in production
    )

    # List open offenses
    offenses = client.siem.get_siem_offenses(filter="status=OPEN", range_header="0-49")

    # Run an Ariel search
    search = client.ariel.post_ariel_searches(
        body={{"query_expression": "SELECT * FROM events LAST 5 MINUTES"}}
    )

Authentication
--------------
QRadar supports two authentication methods:

1. **SEC token** (recommended for service-to-service integration)::

    client = QRadarClient(host="...", sec_token="<token>")

2. **Basic auth** (username + password)::

    client = QRadarClient(host="...", username="admin", password="secret")

API reference
-------------
Each QRadar API tag is exposed as an attribute on :class:`QRadarClient`:

{doc_attrs}
"""

from __future__ import annotations

from typing import Optional, Union

from ._http import QRadarSession
{imports}


class QRadarClient:
    """Top-level client for the IBM QRadar REST API (version 26.0).

    :param host: Hostname or IP address of the QRadar console
        (e.g. ``"qradar.example.com"`` or ``"192.168.1.10"``).
    :param sec_token: QRadar service token (SEC header).  Either this *or*
        ``username``/``password`` must be provided.
    :param username: QRadar username for Basic auth.
    :param password: QRadar password for Basic auth.
    :param version: API version string (default: ``"26.0"``).
    :param verify_ssl: TLS certificate verification.  Accepts ``True``
        (verify with default CA bundle), ``False`` (disable – only for dev/test),
        or a path to a custom CA bundle.
    :param timeout: Per-request timeout in seconds (default: 30).
    :param max_retries: Maximum number of retries for failed requests (default: 3).
    """

    def __init__(
        self,
        host: str,
        *,
        sec_token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        version: str = "26.0",
        verify_ssl: Union[bool, str] = True,
        timeout: int = 30,
        max_retries: int = 3,
    ) -> None:
        session = QRadarSession(
            host=host,
            sec_token=sec_token,
            username=username,
            password=password,
            version=version,
            verify_ssl=verify_ssl,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._session = session
{attrs}

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()

    def __enter__(self) -> "QRadarClient":
        return self

    def __exit__(self, *_) -> None:
        self.close()
'''


def _generate_init_src(tags_and_modules: list) -> str:
    """Generate qradar_sdk/__init__.py."""
    class_imports = '\n'.join(
        f'from .api.{mod} import {cls}'
        for _, mod, cls in tags_and_modules
    )
    class_names = ', '.join(f'"{cls}"' for _, _, cls in tags_and_modules)
    return f'''\
"""
qradar_sdk – Python SDK for the IBM QRadar REST API (version 26.0).

Quick start::

    from qradar_sdk import QRadarClient

    client = QRadarClient(
        host="qradar.example.com",
        sec_token="<your-service-token>",
        verify_ssl=False,
    )
    offenses = client.siem.get_siem_offenses(filter="status=OPEN")
"""

from .client import QRadarClient
from ._http import QRadarSession
from .exceptions import (
    QRadarError,
    QRadarAPIError,
    QRadarAuthError,
    QRadarNotFoundError,
    QRadarRateLimitError,
)
{class_imports}

__all__ = [
    "QRadarClient",
    "QRadarSession",
    "QRadarError",
    "QRadarAPIError",
    "QRadarAuthError",
    "QRadarNotFoundError",
    "QRadarRateLimitError",
    {class_names},
]

__version__ = "26.0.0"
'''


def _generate_pyproject(output_dir: Path) -> str:
    return '''\
[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "qradar-sdk"
version = "26.0.0"
description = "Python SDK client for the IBM QRadar REST API v26.0"
readme = "README_SDK.md"
requires-python = ">=3.9"
license = {text = "Apache-2.0"}
dependencies = [
    "requests>=2.28",
    "urllib3>=1.26",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-mock",
    "responses",
]

[tool.setuptools.packages.find]
where = ["."]
include = ["qradar_sdk*"]
'''


def _generate_readme() -> str:
    return '''\
# QRadar Python SDK

A Python SDK client for the **IBM QRadar REST API version 26.0**, generated
from the [`openapi.yaml`](openapi.yaml) specification.

## Installation

```bash
pip install requests
# then place the qradar_sdk/ package on your Python path, or install it:
pip install -e .
```

## Quick start

### SEC token authentication (recommended)

```python
from qradar_sdk import QRadarClient

client = QRadarClient(
    host="qradar.example.com",
    sec_token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    verify_ssl=False,   # disable TLS verification for self-signed certs
)

# List the 50 most-recent open offenses
offenses = client.siem.get_siem_offenses(
    filter="status=OPEN",
    sort="-start_time",
    range_header="0-49",
)
for offense in offenses:
    print(offense["id"], offense["description"])
```

### Basic auth

```python
client = QRadarClient(
    host="qradar.example.com",
    username="admin",
    password="s3cr3t",
)
```

## Usage patterns

### Using as a context manager

```python
with QRadarClient(host="...", sec_token="...") as client:
    rules = client.analytics.get_analytics_rules()
```

### Pagination helper

```python
with QRadarClient(host="...", sec_token="...") as client:
    for page in client._session.paginate("/siem/offenses", page_size=100):
        for offense in page:
            process(offense)
```

### Running an Ariel (AQL) search

```python
# Submit the search
search = client.ariel.post_ariel_searches(
    body={"query_expression": "SELECT * FROM events LAST 5 MINUTES"}
)
search_id = search["search_id"]

# Poll until complete
import time
while True:
    status = client.ariel.get_ariel_searches_search_id(search_id=search_id)
    if status["status"] == "COMPLETED":
        break
    time.sleep(2)

# Fetch results
results = client.ariel.get_ariel_searches_search_id_results(search_id=search_id)
```

## API reference

The `QRadarClient` exposes one attribute per API tag:

| Attribute | Tag | Description |
|---|---|---|
| `client.access` | access | Login attempts and access management |
| `client.analytics` | analytics | Rules, building blocks, ADE rules |
| `client.ariel` | ariel | AQL searches, saved searches |
| `client.asset_model` | asset_model | Asset management |
| `client.auth` | auth | Authentication (logout) |
| `client.backup_and_restore` | backup_and_restore | Backup management |
| `client.bandwidth_manager` | bandwidth_manager | Bandwidth configurations |
| `client.config` | config | System configuration |
| `client.data_classification` | data_classification | QID records, categories |
| `client.disaster_recovery` | disaster_recovery | Ariel copy profiles |
| `client.dynamic_search` | dynamic_search | Dynamic search schemas |
| `client.forensics` | forensics | Packet capture and case management |
| `client.gui_app_framework` | gui_app_framework | App framework management |
| `client.health` | health | Health metrics |
| `client.health_data` | health_data | Security data counts |
| `client.help` | help | API endpoint documentation |
| `client.qni` | qni | QNI host configuration |
| `client.qrm` | qrm | Risk management |
| `client.qvm` | qvm | Vulnerability management |
| `client.reference_data` | reference_data | Reference sets, maps, tables |
| `client.reference_data_collections` | reference_data_collections | Reference data collections |
| `client.scanner` | scanner | Vulnerability scanner profiles |
| `client.services` | services | DNS, WHOIS, port scan services |
| `client.siem` | siem | Offenses, notes, closing reasons |
| `client.staged_config` | staged_config | Staged (pre-deploy) configuration |
| `client.system` | system | System information, servers |

## Error handling

```python
from qradar_sdk import QRadarClient, QRadarAPIError, QRadarNotFoundError

try:
    offense = client.siem.get_siem_offenses_offense_id(offense_id=9999)
except QRadarNotFoundError:
    print("Offense not found")
except QRadarAPIError as exc:
    print(f"API error {exc.status_code}: {exc.message}")
```

## Regenerating the SDK

If you update `openapi.yaml`, run:

```bash
python3 generate_sdk.py
```

to regenerate the `qradar_sdk/` package.
'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate(spec_path: Path, output_dir: Path) -> None:
    print(f'Reading spec: {spec_path}', file=sys.stderr)
    spec = yaml.safe_load(spec_path.read_text(encoding='utf-8'))

    ops_by_tag = _collect_operations(spec)
    print(f'Found {len(ops_by_tag)} tags', file=sys.stderr)

    # Prepare output directories
    api_dir = output_dir / 'api'
    api_dir.mkdir(parents=True, exist_ok=True)

    # Write static files
    (output_dir / 'exceptions.py').write_text(_EXCEPTIONS_SRC, encoding='utf-8')
    (output_dir / '_http.py').write_text(_HTTP_SRC, encoding='utf-8')
    (output_dir / 'py.typed').write_text('', encoding='utf-8')

    tags_and_modules = []
    api_init_imports = []

    for tag, operations in sorted(ops_by_tag.items()):
        module_name = _sanitise_module_name(tag)
        class_name = _class_name(tag)
        tags_and_modules.append((tag, module_name, class_name))

        src = _generate_api_module(tag, operations)
        module_path = api_dir / f'{module_name}.py'
        module_path.write_text(src, encoding='utf-8')
        api_init_imports.append(f'from .{module_name} import {class_name}')
        print(f'  wrote {module_path.name} ({len(operations)} ops)', file=sys.stderr)

    # api/__init__.py
    (api_dir / '__init__.py').write_text(
        '"""Auto-generated QRadar API modules."""\n\n'
        + '\n'.join(api_init_imports) + '\n',
        encoding='utf-8',
    )

    # client.py
    (output_dir / 'client.py').write_text(
        _generate_client_src(tags_and_modules), encoding='utf-8'
    )

    # __init__.py
    (output_dir / '__init__.py').write_text(
        _generate_init_src(tags_and_modules), encoding='utf-8'
    )

    # pyproject.toml (in parent directory)
    (output_dir.parent / 'pyproject.toml').write_text(
        _generate_pyproject(output_dir), encoding='utf-8'
    )

    # README_SDK.md (in parent directory)
    (output_dir.parent / 'README_SDK.md').write_text(
        _generate_readme(), encoding='utf-8'
    )

    total_ops = sum(len(v) for v in ops_by_tag.values())
    print(
        f'\nSDK written to {output_dir}/ '
        f'({len(ops_by_tag)} modules, {total_ops} operations)',
        file=sys.stderr,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Generate Python SDK from QRadar OpenAPI spec'
    )
    parser.add_argument(
        '--spec', '-s',
        default=str(Path(__file__).parent / 'openapi.yaml'),
        help='Path to openapi.yaml (default: openapi.yaml in script dir)',
    )
    parser.add_argument(
        '--output', '-o',
        default=str(Path(__file__).parent / 'qradar_sdk'),
        help='Output directory for the SDK package (default: qradar_sdk/)',
    )
    args = parser.parse_args()

    spec_path = Path(args.spec).resolve()
    if not spec_path.is_file():
        print(f'Error: spec not found: {spec_path}', file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output).resolve()
    generate(spec_path, output_dir)


if __name__ == '__main__':
    main()
