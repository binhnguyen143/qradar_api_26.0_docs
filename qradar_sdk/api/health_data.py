"""API methods for the ``health_data`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class HealthDataAPI:
    """Client for the QRadar ``health_data`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_health_data_security_data_count(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves count of security artifacts in QRadar"""
        url = "/health_data/security_data_count"
        return self._s.get(url, fields=fields, **kwargs)

    def get_health_data_top_offenses(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves Top Offenses in the system sorted by update count."""
        url = "/health_data/top_offenses"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_health_data_top_rules(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves Top Rules in the system sorted by response count."""
        url = "/health_data/top_rules"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)
