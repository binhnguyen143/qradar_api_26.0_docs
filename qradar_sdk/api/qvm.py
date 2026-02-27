"""API methods for the ``qvm`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class QvmAPI:
    """Client for the QRadar ``qvm`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_qvm_assets(self, saved_search_id: Optional[Any] = None, saved_search_name: Optional[Any] = None, filters: Optional[Any] = None, **kwargs: Any) -> Any:
        """List the assets with discovered vulnerabilities present in the asset model.  The response will contain all available RESTful resources"""
        url = "/qvm/assets"
        params = {"savedSearchId": saved_search_id, "savedSearchName": saved_search_name, "filters": filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)

    def get_qvm_filters(self, **kwargs: Any) -> Any:
        """Get a list of the allowable filters that can be used or applied against the:"""
        url = "/qvm/filters"
        return self._s.get(url, **kwargs)

    def get_qvm_network(self, saved_search_id: Optional[Any] = None, saved_search_name: Optional[Any] = None, filters: Optional[Any] = None, **kwargs: Any) -> Any:
        """List the networks present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources"""
        url = "/qvm/network"
        params = {"savedSearchId": saved_search_id, "savedSearchName": saved_search_name, "filters": filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)

    def get_qvm_openservices(self, saved_search_id: Optional[Any] = None, saved_search_name: Optional[Any] = None, filters: Optional[Any] = None, **kwargs: Any) -> Any:
        """List the openservices present in the asset model with vulnerabilities present.  The response will contain all available RESTful resources"""
        url = "/qvm/openservices"
        params = {"savedSearchId": saved_search_id, "savedSearchName": saved_search_name, "filters": filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)

    def get_qvm_saved_search_groups(self, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of vulnerability saved search groups."""
        url = "/qvm/saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a vulnerability saved search group."""
        url = f"/qvm/saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qvm_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of an vulnerability saved search group."""
        url = f"/qvm/saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qvm_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a vulnerability saved search group."""
        url = f"/qvm/saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_qvm_saved_searches(self, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of  vulnerability instance saved searches."""
        url = "/qvm/saved_searches"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_searches_saved_search_id(self, saved_search_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a vulnerability instance saved search."""
        url = f"/qvm/saved_searches/{saved_search_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qvm_saved_searches_saved_search_id(self, saved_search_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the vulnerability saved search owner only."""
        url = f"/qvm/saved_searches/{saved_search_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qvm_saved_searches_saved_search_id(self, saved_search_id, **kwargs: Any) -> Any:
        """Deletes a vulnerability saved search."""
        url = f"/qvm/saved_searches/{saved_search_id}"
        return self._s.delete(url, **kwargs)

    def get_qvm_saved_searches_saved_search_id_vuln_instances(self, saved_search_id, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates the Vulnerability Instances search. This search will return a maximum of 100,000 results."""
        url = f"/qvm/saved_searches/{saved_search_id}/vuln_instances"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_searches_vuln_instances_task_id_results_assets(self, task_id, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Lists the Vulnerability Instances assets that are returned from the vulnerability instance saved search."""
        url = f"/qvm/saved_searches/vuln_instances/{task_id}/results/assets"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_searches_vuln_instances_task_id_results_vuln_instances(self, task_id, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Lists the Vulnerability Instances returned from a vulnerability instance saved search."""
        url = f"/qvm/saved_searches/vuln_instances/{task_id}/results/vuln_instances"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_searches_vuln_instances_task_id_results_vulnerabilities(self, task_id, filter: Optional[Any] = None, fields: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """List the Vulnerability Instances vulnerabilities returned from the saved search."""
        url = f"/qvm/saved_searches/vuln_instances/{task_id}/results/vulnerabilities"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qvm_saved_searches_vuln_instances_task_id_status(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the current status of a vulnerability instance search that was initiated."""
        url = f"/qvm/saved_searches/vuln_instances/{task_id}/status"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qvm_saved_searches_vuln_instances_task_id_status(self, task_id, status: Optional[Any] = None, retention_period_in_days: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the status of a vulnerability instance saved search."""
        url = f"/qvm/saved_searches/vuln_instances/{task_id}/status"
        params = {"status": status, "retention_period_in_days": retention_period_in_days}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def post_qvm_tickets_assign(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update the remediation ticket for the assigned vulnerability"""
        url = "/qvm/tickets/assign"
        return self._s.post(url, json_body=body, **kwargs)

    def get_qvm_vulns(self, saved_search_id: Optional[Any] = None, saved_search_name: Optional[Any] = None, filters: Optional[Any] = None, **kwargs: Any) -> Any:
        """List the Vulnerabilities present in the asset model.  The response will contain all available RESTful resources"""
        url = "/qvm/vulns"
        params = {"savedSearchId": saved_search_id, "savedSearchName": saved_search_name, "filters": filters}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, **kwargs)
