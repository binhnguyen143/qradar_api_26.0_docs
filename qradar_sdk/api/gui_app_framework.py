"""API methods for the ``gui_app_framework`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class GuiAppFrameworkAPI:
    """Client for the QRadar ``gui_app_framework`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_gui_app_framework_application_creation_task(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of all application installs."""
        url = "/gui_app_framework/application_creation_task"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_gui_app_framework_application_creation_task(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Installs a new application."""
        url = "/gui_app_framework/application_creation_task"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_gui_app_framework_application_creation_task_application_id(self, application_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of an application install."""
        url = f"/gui_app_framework/application_creation_task/{application_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_gui_app_framework_application_creation_task_application_id(self, application_id, status: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels an application install."""
        url = f"/gui_app_framework/application_creation_task/{application_id}"
        params = {"status": status}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_gui_app_framework_application_creation_task_application_id_auth(self, application_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an authorisation request for an application install."""
        url = f"/gui_app_framework/application_creation_task/{application_id}/auth"
        return self._s.get(url, fields=fields, **kwargs)

    def post_gui_app_framework_application_creation_task_application_id_auth(self, application_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Responds to an authorisation request for an application install."""
        url = f"/gui_app_framework/application_creation_task/{application_id}/auth"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_gui_app_framework_application_definitions(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve list of application definitions."""
        url = "/gui_app_framework/application_definitions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_gui_app_framework_application_definitions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Installs a new application definition."""
        url = "/gui_app_framework/application_definitions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_gui_app_framework_application_definitions_application_definition_id(self, application_definition_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an application definition."""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_gui_app_framework_application_definitions_application_definition_id(self, application_definition_id, status: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the creation or upgrade of an application definition"""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}"
        params = {"status": status}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def put_gui_app_framework_application_definitions_application_definition_id(self, application_definition_id, body: Optional[Any] = None, include_stopped_application: Optional[Any] = None, use_local_zip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Upgrades an application definition."""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}"
        headers = {"include_stopped_application": include_stopped_application, "use_local_zip": use_local_zip, "fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def delete_gui_app_framework_application_definitions_application_definition_id(self, application_definition_id, **kwargs: Any) -> Any:
        """Deletes an application definition and its associated instances."""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}"
        return self._s.delete(url, **kwargs)

    def get_gui_app_framework_application_definitions_application_definition_id_user_role_id(self, application_definition_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve all user roles associated with an application definition."""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}/user_role_id"
        return self._s.get(url, fields=fields, **kwargs)

    def post_gui_app_framework_application_definitions_application_definition_id_user_role_id_user_role_id(self, application_definition_id, user_role_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Add a user role to the list associated with an application definition"""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}"
        return self._s.post(url, fields=fields, **kwargs)

    def delete_gui_app_framework_application_definitions_application_definition_id_user_role_id_user_role_id(self, application_definition_id, user_role_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Call DELETE /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}"""
        url = f"/gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_gui_app_framework_applications(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve list of applications."""
        url = "/gui_app_framework/applications"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_gui_app_framework_applications(self, application_definition_id: Optional[Any] = None, memory: Optional[Any] = None, security_profile_id: Optional[Any] = None, force_multitenancy_safe: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new application instance."""
        url = "/gui_app_framework/applications"
        params = {"application_definition_id": application_definition_id, "memory": memory, "security_profile_id": security_profile_id, "force_multitenancy_safe": force_multitenancy_safe}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_gui_app_framework_applications_application_id(self, application_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve an installed application."""
        url = f"/gui_app_framework/applications/{application_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_gui_app_framework_applications_application_id(self, application_id, status: Optional[Any] = None, memory: Optional[Any] = None, oauth_user_id: Optional[Any] = None, security_profile_id: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an application."""
        url = f"/gui_app_framework/applications/{application_id}"
        params = {"status": status, "memory": memory, "oauth_user_id": oauth_user_id, "security_profile_id": security_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def put_gui_app_framework_applications_application_id(self, application_id, body: Optional[Any] = None, use_local_zip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Upgrades an application."""
        url = f"/gui_app_framework/applications/{application_id}"
        headers = {"use_local_zip": use_local_zip, "fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def delete_gui_app_framework_applications_application_id(self, application_id, **kwargs: Any) -> Any:
        """Deletes an application instance."""
        url = f"/gui_app_framework/applications/{application_id}"
        return self._s.delete(url, **kwargs)

    def get_gui_app_framework_applications_application_id_host_type(self, application_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a host type."""
        url = f"/gui_app_framework/applications/{application_id}/host_type"
        return self._s.get(url, fields=fields, **kwargs)

    def get_gui_app_framework_named_services(self, **kwargs: Any) -> Any:
        """Retrieves all named services."""
        url = "/gui_app_framework/named_services"
        return self._s.get(url, **kwargs)

    def get_gui_app_framework_named_services_uuid(self, uuid, **kwargs: Any) -> Any:
        """Retrieves a named service."""
        url = f"/gui_app_framework/named_services/{uuid}"
        return self._s.get(url, **kwargs)
