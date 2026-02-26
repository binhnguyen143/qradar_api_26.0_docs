"""API methods for the ``bandwidth_manager`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class BandwidthManagerAPI:
    """Client for the QRadar ``bandwidth_manager`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_bandwidth_manager_configurations(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of configurations."""
        url = "/bandwidth_manager/configurations"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_bandwidth_manager_configurations(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a bandwidth manager configuration"""
        url = "/bandwidth_manager/configurations"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_bandwidth_manager_configurations_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a configuration."""
        url = f"/bandwidth_manager/configurations/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_bandwidth_manager_configurations_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a bandwidth manager configuration by ID."""
        url = f"/bandwidth_manager/configurations/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_bandwidth_manager_configurations_id(self, id, **kwargs: Any) -> Any:
        """Delete a bandwidth manager configuration by ID."""
        url = f"/bandwidth_manager/configurations/{id}"
        return self._s.delete(url, **kwargs)

    def get_bandwidth_manager_filters(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of egress filters."""
        url = "/bandwidth_manager/filters"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_bandwidth_manager_filters(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a bandwidth manager filter"""
        url = "/bandwidth_manager/filters"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_bandwidth_manager_filters_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a filter."""
        url = f"/bandwidth_manager/filters/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_bandwidth_manager_filters_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Delete a filter by sequence ID."""
        url = f"/bandwidth_manager/filters/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_bandwidth_manager_filters_id(self, id, **kwargs: Any) -> Any:
        """Update a filter by ID."""
        url = f"/bandwidth_manager/filters/{id}"
        return self._s.delete(url, **kwargs)
