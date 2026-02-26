"""API methods for the ``dynamic_search`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class DynamicSearchAPI:
    """Client for the QRadar ``dynamic_search`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_dynamic_search_saved_queries(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Returns a list of all queries to which the caller has access."""
        url = "/dynamic_search/saved_queries"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_dynamic_search_saved_queries(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a query to be saved for use in dynamic searches. A query represents a request for data. Queries are not the same as searches, which are the results of a request for data. The benefit of saving a query is that it may be referenced in dynamic searches and can be reused."""
        url = "/dynamic_search/saved_queries"
        return self._s.post(url, json_body=body, **kwargs)

    def get_dynamic_search_saved_queries_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Returns a single query with the specified ID. The caller must have access to the query."""
        url = f"/dynamic_search/saved_queries/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def delete_dynamic_search_saved_queries_id(self, id, **kwargs: Any) -> Any:
        """Removes the specified query from the system."""
        url = f"/dynamic_search/saved_queries/{id}"
        return self._s.delete(url, **kwargs)

    def get_dynamic_search_schemas(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all schemas available to the user."""
        url = "/dynamic_search/schemas"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_dynamic_search_schemas_name(self, name, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all schemas available to the user."""
        url = f"/dynamic_search/schemas/{name}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_dynamic_search_schemas_name_fields(self, name, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all available Fields"""
        url = f"/dynamic_search/schemas/{name}/fields"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_dynamic_search_schemas_name_functions(self, name, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all available Functions"""
        url = f"/dynamic_search/schemas/{name}/functions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_dynamic_search_schemas_name_operators(self, name, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all available relational Operators"""
        url = f"/dynamic_search/schemas/{name}/operators"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_dynamic_search_searches(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all searches performed by this user."""
        url = "/dynamic_search/searches"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_dynamic_search_searches(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Posts a search to be performed by the service."""
        url = "/dynamic_search/searches"
        return self._s.post(url, json_body=body, **kwargs)

    def get_dynamic_search_searches_handle(self, handle, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the specific search performed by this user."""
        url = f"/dynamic_search/searches/{handle}"
        return self._s.get(url, fields=fields, **kwargs)

    def delete_dynamic_search_searches_handle(self, handle, **kwargs: Any) -> Any:
        """Deletes a search and any stored results."""
        url = f"/dynamic_search/searches/{handle}"
        return self._s.delete(url, **kwargs)

    def get_dynamic_search_searches_handle_results(self, handle, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the specific search performed by this user."""
        url = f"/dynamic_search/searches/{handle}/results"
        return self._s.get(url, range_header=range_header, filter_expr=filter, sort=sort, **kwargs)
