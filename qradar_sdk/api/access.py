"""API methods for the ``access`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class AccessAPI:
    """Client for the QRadar ``access`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_access_login_attempts(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of login attempts."""
        url = "/access/login_attempts"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)
