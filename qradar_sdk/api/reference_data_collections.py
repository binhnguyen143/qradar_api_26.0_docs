"""API methods for the ``reference_data_collections`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ReferenceDataCollectionsAPI:
    """Client for the QRadar ``reference_data_collections`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_reference_data_collections_set_bulk_update_tasks_task_status_id(self, task_status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the Bulk Update status"""
        url = f"/reference_data_collections/set_bulk_update_tasks/{task_status_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_reference_data_collections_set_bulk_update_tasks_task_status_id_results(self, task_status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the results of the Bulk Update task"""
        url = f"/reference_data_collections/set_bulk_update_tasks/{task_status_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_reference_data_collections_set_delete_tasks_task_status_id(self, task_status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get results of the asynchronous delete Set task"""
        url = f"/reference_data_collections/set_delete_tasks/{task_status_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_reference_data_collections_set_dependents_tasks_task_status_id(self, task_status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the status of the Get Dependents task"""
        url = f"/reference_data_collections/set_dependents_tasks/{task_status_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_reference_data_collections_set_dependents_tasks_task_status_id(self, task_status_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancel the Get Dependents request"""
        url = f"/reference_data_collections/set_dependents_tasks/{task_status_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_reference_data_collections_set_dependents_tasks_task_status_id_results(self, task_status_id, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the results of the Get Dependents task"""
        url = f"/reference_data_collections/set_dependents_tasks/{task_status_id}/results"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_reference_data_collections_set_entries(self, entry_type: Optional[Any] = None, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get a list of set entries which match a search criteria."""
        url = "/reference_data_collections/set_entries"
        params = {"entry_type": entry_type}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_reference_data_collections_set_entries(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create an entry within a set"""
        url = "/reference_data_collections/set_entries"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def patch_reference_data_collections_set_entries(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Perform asynchronous bulk update - series of add and updates"""
        url = "/reference_data_collections/set_entries"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, json_body=body, **kwargs)

    def get_reference_data_collections_set_entries_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get a set entry"""
        url = f"/reference_data_collections/set_entries/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_reference_data_collections_set_entries_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a Set Entry given the properties based in the body DTO. Only the notes field
 can be modified in an existing entry. The source and last_seen timestamp will be updated
 automatically."""
        url = f"/reference_data_collections/set_entries/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_reference_data_collections_set_entries_id(self, id, **kwargs: Any) -> Any:
        """Delete a set entry"""
        url = f"/reference_data_collections/set_entries/{id}"
        return self._s.delete(url, **kwargs)

    def get_reference_data_collections_sets(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get a list of set meta data information based on search criteria"""
        url = "/reference_data_collections/sets"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_reference_data_collections_sets(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create a set given the properties based in the body DTO"""
        url = "/reference_data_collections/sets"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_reference_data_collections_sets_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the meta data information for a specific set"""
        url = f"/reference_data_collections/sets/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_reference_data_collections_sets_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a Set given the properties based in the body DTO"""
        url = f"/reference_data_collections/sets/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_reference_data_collections_sets_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Delete a set by starting an asynchronous task"""
        url = f"/reference_data_collections/sets/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_reference_data_collections_sets_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create an asynchronous task to get the dependents of a Set"""
        url = f"/reference_data_collections/sets/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)
