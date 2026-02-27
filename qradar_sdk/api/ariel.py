"""API methods for the ``ariel`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ArielAPI:
    """Client for the QRadar ``ariel`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_ariel_databases(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of available Ariel database names"""
        url = "/ariel/databases"
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)

    def get_ariel_databases_database_name(self, database_name, fields: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve the columns that are defined for a specific Ariel database."""
        url = f"/ariel/databases/{database_name}"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_ariel_event_saved_search_groups(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list the event Ariel saved search groups."""
        url = "/ariel/event_saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_ariel_event_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an event Ariel saved search group."""
        url = f"/ariel/event_saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_event_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of an event Ariel saved search group."""
        url = f"/ariel/event_saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_ariel_event_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes an event Ariel saved search group."""
        url = f"/ariel/event_saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_ariel_flow_saved_search_groups(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of flow Ariel saved search groups."""
        url = "/ariel/flow_saved_search_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_ariel_flow_saved_search_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a flow Ariel saved search group."""
        url = f"/ariel/flow_saved_search_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_flow_saved_search_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a flow Ariel saved search group."""
        url = f"/ariel/flow_saved_search_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_ariel_flow_saved_search_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a flow Ariel saved search group."""
        url = f"/ariel/flow_saved_search_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_ariel_flow_vlans(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of available flow VLAN IDs in the Ariel database."""
        url = "/ariel/flow_vlans"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_ariel_flow_vlans(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new flow VLAN field as specified by input parameters."""
        url = "/ariel/flow_vlans"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_ariel_flow_vlans_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a flow VLAN ID object by VLAN ID."""
        url = f"/ariel/flow_vlans/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def delete_ariel_flow_vlans_id(self, id, **kwargs: Any) -> Any:
        """Deletes a flow VLAN ID with specified enterprise and customer VLAN ID's and removes any associated domain mappings."""
        url = f"/ariel/flow_vlans/{id}"
        return self._s.delete(url, **kwargs)

    def get_ariel_functions(self, database: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves AQL Functions for given ."""
        url = "/ariel/functions"
        params = {"database": database}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)

    def get_ariel_functions_function_name(self, function_name, database: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves AQL Function with given name for a given database."""
        url = f"/ariel/functions/{function_name}"
        params = {"database": database}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)

    def get_ariel_lookups(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of all tagged field lookups."""
        url = "/ariel/lookups"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_lookups(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new tagged field lookup."""
        url = "/ariel/lookups"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_ariel_lookups_name(self, name, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a tagged field lookup by name."""
        url = f"/ariel/lookups/{name}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_lookups_name(self, name, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a tagged field lookup with particular name."""
        url = f"/ariel/lookups/{name}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_ariel_lookups_name(self, name, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes a tagged field lookup with particular name."""
        url = f"/ariel/lookups/{name}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_ariel_parser_keywords(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves keywords applicable to AQL Parser."""
        url = "/ariel/parser_keywords"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_processors_aql_metadata(self, query_expression: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Parses the AQL query expression and returns metadata for this query"""
        url = "/ariel/processors/aql_metadata"
        params = {"query_expression": query_expression}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_ariel_saved_search_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the delete the Ariel saved search task status."""
        url = f"/ariel/saved_search_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_ariel_saved_search_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent the Ariel saved search task status."""
        url = f"/ariel/saved_search_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_saved_search_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the dependent Ariel saved search task."""
        url = f"/ariel/saved_search_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_ariel_saved_search_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the Ariel saved search dependent task results."""
        url = f"/ariel/saved_search_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_ariel_saved_searches(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of Ariel saved searches."""
        url = "/ariel/saved_searches"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_ariel_saved_searches_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an Ariel saved search."""
        url = f"/ariel/saved_searches/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_saved_searches_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the Ariel saved search."""
        url = f"/ariel/saved_searches/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_ariel_saved_searches_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes an Ariel saved search. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check."""
        url = f"/ariel/saved_searches/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_ariel_saved_searches_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the Ariel saved search."""
        url = f"/ariel/saved_searches/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_ariel_searches(self, db_name: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of Ariel searches. Search IDs for completed and active searches are returned."""
        url = "/ariel/searches"
        params = {"db_name": db_name}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, filter_expr=filter, **kwargs)

    def post_ariel_searches(self, query_expression: Optional[Any] = None, saved_search_id: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create a new asynchronous Ariel search."""
        url = "/ariel/searches"
        params = {"query_expression": query_expression, "saved_search_id": saved_search_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)

    def get_ariel_searches_search_id(self, search_id, prefer: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves information about an Ariel search."""
        url = f"/ariel/searches/{search_id}"
        headers = {"Prefer": prefer}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, **kwargs)

    def post_ariel_searches_search_id(self, search_id, status: Optional[Any] = None, save_results: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an Ariel search."""
        url = f"/ariel/searches/{search_id}"
        params = {"status": status, "save_results": save_results}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)

    def delete_ariel_searches_search_id(self, search_id, **kwargs: Any) -> Any:
        """Deletes an Ariel search."""
        url = f"/ariel/searches/{search_id}"
        return self._s.delete(url, **kwargs)

    def get_ariel_searches_search_id_metadata(self, search_id, fields: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve the columns that are defined for a specific Ariel search id."""
        url = f"/ariel/searches/{search_id}/metadata"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_ariel_searches_search_id_results(self, search_id, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves search results in the requested format."""
        url = f"/ariel/searches/{search_id}/results"
        return self._s.get(url, range_header=range_header, **kwargs)

    def get_ariel_taggedfieldcategories(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of categories for tagged fields."""
        url = "/ariel/taggedfieldcategories"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_ariel_taggedfieldcategories(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new category for tagged fields. To use this endpoint, you must have System Administrator or Security Admin permissions."""
        url = "/ariel/taggedfieldcategories"
        return self._s.post(url, json_body=body, **kwargs)

    def get_ariel_taggedfieldcategories_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets a category for tagged fields."""
        url = f"/ariel/taggedfieldcategories/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_taggedfieldcategories_id(self, id, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a category for tagged fields. To use this endpoint, you must have System Administrator or Security Admin permissions."""
        url = f"/ariel/taggedfieldcategories/{id}"
        return self._s.post(url, json_body=body, **kwargs)

    def delete_ariel_taggedfieldcategories_id(self, id, **kwargs: Any) -> Any:
        """Removes the category for tagged fields from the system. To use this endpoint, you must have System Administrator or Security Admin permissions."""
        url = f"/ariel/taggedfieldcategories/{id}"
        return self._s.delete(url, **kwargs)

    def get_ariel_taggedfields(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of tagged fields."""
        url = "/ariel/taggedfields"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_ariel_taggedfields(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new tagged field. To use this endpoint, you must have System Administrator or Security Admin permissions."""
        url = "/ariel/taggedfields"
        return self._s.post(url, json_body=body, **kwargs)

    def get_ariel_taggedfields_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual tagged field."""
        url = f"/ariel/taggedfields/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_ariel_taggedfields_id(self, id, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a tagged field specified by an id. You must have the ADMIN | SAASADMIN capability to use this endpoint."""
        url = f"/ariel/taggedfields/{id}"
        return self._s.post(url, json_body=body, **kwargs)

    def delete_ariel_taggedfields_id(self, id, **kwargs: Any) -> Any:
        """Removes a tagged field from the system. To use this endpoint, you must have System Administrator or Security Admin permissions."""
        url = f"/ariel/taggedfields/{id}"
        return self._s.delete(url, **kwargs)

    def post_ariel_validators_aql(self, query_expression: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Validates the AQL query expression."""
        url = "/ariel/validators/aql"
        params = {"query_expression": query_expression}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)
