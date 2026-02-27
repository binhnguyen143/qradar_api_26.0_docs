"""API methods for the ``forensics`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ForensicsAPI:
    """Client for the QRadar ``forensics`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_forensics_capture_recoveries(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of capture recoveries."""
        url = "/forensics/capture/recoveries"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_forensics_capture_recoveries(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new capture recovery."""
        url = "/forensics/capture/recoveries"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_forensics_capture_recoveries_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a recovery based on the supplied ID."""
        url = f"/forensics/capture/recoveries/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_forensics_capture_recovery_tasks(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of recovery tasks."""
        url = "/forensics/capture/recovery_tasks"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_forensics_capture_recovery_tasks_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a recovery task based on the supplied ID."""
        url = f"/forensics/capture/recovery_tasks/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_forensics_case_management_case_create_tasks_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a case create task based on the supplied id."""
        url = f"/forensics/case_management/case_create_tasks/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_forensics_case_management_cases(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of cases."""
        url = "/forensics/case_management/cases"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_forensics_case_management_cases(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new case."""
        url = "/forensics/case_management/cases"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_forensics_case_management_cases_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a case based on the supplied id."""
        url = f"/forensics/case_management/cases/{id}"
        return self._s.get(url, fields=fields, **kwargs)
