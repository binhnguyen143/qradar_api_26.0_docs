"""API methods for the ``qrm`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class QrmAPI:
    """Client for the QRadar ``qrm`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_qrm_model_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of model groups."""
        url = "/qrm/model_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qrm_model_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a model group."""
        url = f"/qrm/model_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qrm_model_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a model group."""
        url = f"/qrm/model_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qrm_model_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a model group."""
        url = f"/qrm/model_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_qrm_qrm_saved_search_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of QRM saved search groups."""
        url = "/qrm/qrm_saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qrm_qrm_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a QRM saved search group."""
        url = f"/qrm/qrm_saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qrm_qrm_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a QRM saved search group."""
        url = f"/qrm/qrm_saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qrm_qrm_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a QRM saved search group."""
        url = f"/qrm/qrm_saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_qrm_question_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of question groups."""
        url = "/qrm/question_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qrm_question_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a question group."""
        url = f"/qrm/question_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qrm_question_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a question group."""
        url = f"/qrm/question_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qrm_question_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a question group."""
        url = f"/qrm/question_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_qrm_simulation_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a of list the simulation groups."""
        url = "/qrm/simulation_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qrm_simulation_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a simulation group."""
        url = f"/qrm/simulation_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qrm_simulation_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a simulation group."""
        url = f"/qrm/simulation_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qrm_simulation_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a simulation group."""
        url = f"/qrm/simulation_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_qrm_topology_saved_search_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of topology saved search groups."""
        url = "/qrm/topology_saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_qrm_topology_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a topology saved search group."""
        url = f"/qrm/topology_saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qrm_topology_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of an topology saved search group."""
        url = f"/qrm/topology_saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qrm_topology_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a topology saved search group."""
        url = f"/qrm/topology_saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)
