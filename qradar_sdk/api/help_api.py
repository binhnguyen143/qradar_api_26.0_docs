"""API methods for the ``help`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class HelpAPI:
    """Client for the QRadar ``help`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_help_endpoints(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of endpoint documentation objects that are currently in the system."""
        url = "/help/endpoints"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_help_endpoints_endpoint_id(self, endpoint_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a single endpoint documentation object."""
        url = f"/help/endpoints/{endpoint_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_help_resources(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of resource documentation objects currently in the system."""
        url = "/help/resources"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_help_resources_resource_id(self, resource_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a single resource documentation object."""
        url = f"/help/resources/{resource_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_help_versions(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of version documentation objects currently in the system."""
        url = "/help/versions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_help_versions_version_id(self, version_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a single version documentation object."""
        url = f"/help/versions/{version_id}"
        return self._s.get(url, fields=fields, **kwargs)
