"""API methods for the ``health`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class HealthAPI:
    """Client for the QRadar ``health`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_health_metrics_qradar_metrics(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of QRadar component metrics"""
        url = "/health/metrics/qradar_metrics"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_health_metrics_qradar_metrics_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the QRadar health metric identified by ID."""
        url = f"/health/metrics/qradar_metrics/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_health_metrics_qradar_metrics_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the time_resolution and enable field of a QRadar metric identified by metric ID."""
        url = f"/health/metrics/qradar_metrics/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def post_health_metrics_qradar_metrics_global_config(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the frequency and enabled fields of all the qradar metrics."""
        url = "/health/metrics/qradar_metrics_global_config"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_health_metrics_system_metrics(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of system metrics."""
        url = "/health/metrics/system_metrics"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_health_metrics_system_metrics_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the system health metric identified by metric ID."""
        url = f"/health/metrics/system_metrics/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_health_metrics_system_metrics_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Enable or disable a system metric identified by metric ID"""
        url = f"/health/metrics/system_metrics/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def post_health_metrics_system_metrics_global_config(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the frequency and enabled value of all the qradar metrics identified by metric_id parameter."""
        url = "/health/metrics/system_metrics_global_config"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)
