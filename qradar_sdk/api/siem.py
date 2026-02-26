"""API methods for the ``siem`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class SiemAPI:
    """Client for the QRadar ``siem`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_siem_local_destination_addresses(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list offense local destination addresses currently in the system."""
        url = "/siem/local_destination_addresses"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_siem_local_destination_addresses_local_destination_address_id(self, local_destination_address_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an offense local destination address."""
        url = f"/siem/local_destination_addresses/{local_destination_address_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offense_closing_reasons(self, include_reserved: Optional[Any] = None, include_deleted: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of all offense closing reasons."""
        url = "/siem/offense_closing_reasons"
        params = {"include_reserved": include_reserved, "include_deleted": include_deleted}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_siem_offense_closing_reasons(self, reason: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create an offense closing reason."""
        url = "/siem/offense_closing_reasons"
        params = {"reason": reason}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_siem_offense_closing_reasons_closing_reason_id(self, closing_reason_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an offense closing reason."""
        url = f"/siem/offense_closing_reasons/{closing_reason_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offense_saved_search_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the delete the offense saved search task status."""
        url = f"/siem/offense_saved_search_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offense_saved_search_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent the offense saved search task status."""
        url = f"/siem/offense_saved_search_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_siem_offense_saved_search_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the dependent the offense saved search task."""
        url = f"/siem/offense_saved_search_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_siem_offense_saved_search_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the offense saved search dependent task results."""
        url = f"/siem/offense_saved_search_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offense_saved_search_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of offense saved search groups."""
        url = "/siem/offense_saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_siem_offense_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an offense saved search group."""
        url = f"/siem/offense_saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_siem_offense_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of an offense saved search group."""
        url = f"/siem/offense_saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_siem_offense_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes an offense saved search group."""
        url = f"/siem/offense_saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_siem_offense_saved_searches(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of offense saved searches."""
        url = "/siem/offense_saved_searches"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_siem_offense_saved_searches_id(self, id, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an offense saved search."""
        url = f"/siem/offense_saved_searches/{id}"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_siem_offense_saved_searches_id(self, id, body: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the offense saved search owner only."""
        url = f"/siem/offense_saved_searches/{id}"
        headers = {"filter": filter, "fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, range_header=range_header, json_body=body, **kwargs)

    def delete_siem_offense_saved_searches_id(self, id, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes an offense saved search. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/siem/offense_saved_searches/{id}"
        return self._s.delete(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_siem_offense_saved_searches_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on an offense saved search."""
        url = f"/siem/offense_saved_searches/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offense_types(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve all the Offense Types"""
        url = "/siem/offense_types"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_siem_offense_types_offense_type_id(self, offense_type_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an offense type structure that describes the properties of an offense type."""
        url = f"/siem/offense_types/{offense_type_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offenses(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of offenses currently in the system."""
        url = "/siem/offenses"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_siem_offenses_offense_id(self, offense_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an offense structure that describes  properties of an offense"""
        url = f"/siem/offenses/{offense_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_siem_offenses_offense_id(self, offense_id, protected: Optional[Any] = None, follow_up: Optional[Any] = None, status: Optional[Any] = None, closing_reason_id: Optional[Any] = None, assigned_to: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update an offense."""
        url = f"/siem/offenses/{offense_id}"
        params = {"protected": protected, "follow_up": follow_up, "status": status, "closing_reason_id": closing_reason_id, "assigned_to": assigned_to}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_siem_offenses_offense_id_assignable_actors(self, offense_id, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve assignable actors."""
        url = f"/siem/offenses/{offense_id}/assignable_actors"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_siem_offenses_offense_id_notes(self, offense_id, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of notes for an offense."""
        url = f"/siem/offenses/{offense_id}/notes"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_siem_offenses_offense_id_notes(self, offense_id, note_text: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create a note on an offense."""
        url = f"/siem/offenses/{offense_id}/notes"
        params = {"note_text": note_text}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_siem_offenses_offense_id_notes_note_id(self, offense_id, note_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a note for an offense."""
        url = f"/siem/offenses/{offense_id}/notes/{note_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_siem_offenses_ocsf(self, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of offenses currently in the system in OCSF format."""
        url = "/siem/offenses_ocsf"
        return self._s.get(url, range_header=range_header, **kwargs)

    def get_siem_source_addresses(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list offense source addresses currently in the system."""
        url = "/siem/source_addresses"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_siem_source_addresses_source_address_id(self, source_address_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an offense source address."""
        url = f"/siem/source_addresses/{source_address_id}"
        return self._s.get(url, fields=fields, **kwargs)
