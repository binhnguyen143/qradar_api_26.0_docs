"""API methods for the ``config`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ConfigAPI:
    """Client for the QRadar ``config`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_config_access_authorized_services(self, current_authorized_service: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of authorized services. For security reasons, the token field will never be populated in this endpoint.
 To view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the list of authorized services that they've created. An authorized service can see itself and other authorized services that it created, but the Administrator Manager permission is needed to see the complete list of authorized services."""
        url = "/config/access/authorized_services"
        params = {"current_authorized_service": current_authorized_service}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_access_authorized_services(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates an authorized service. The response to this API invocation will contain the API token. This will be the only time the token value is available.
 Any user or authorized service can call this endpoint. To create an authorized service with any user role, security profile, or tenant, the caller must have the Administrator Manager permission. Callers who don't have the Administrator Manager permission can only create an authorized service with their own user role, security profile and tenant. An authorized service that is created by a caller who doesn't have the Administrator Manager permission expires no later than the default expiration time, even if the caller enters a later time. The default expiration time is also what is set as the expiration date for the authorized service if the expiration_date is not set in the request. This default expiration time can be configured using the Authentication Settings API found here: /api/system/authorization/settings.
 Only the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be set when creating an authorized service. All other fields are ignored."""
        url = "/config/access/authorized_services"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_access_authorized_services_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an authorized service.  For security reasons, the token field will never be populated in this endpoint.
 To view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the authorized services that they've created. An authorized service can see itself and other authorized services it created, but the Administrator Manager permission is needed to see the complete list of authorized services."""
        url = f"/config/access/authorized_services/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_access_authorized_services_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an authorized service. Only the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be updated.
 To view any authorized service, the caller must have the Administrator Manager permission. Callers without the Administrator Manager permission can only see the authorized services that they've created. An authorized service can see itself and other authorized services it created, but the Administrator Manager permission is needed to see the complete list of authorized services.
 Only the label, tenant_id, security_profile_id, user_role_id, and expiration_date fields can be set when creating an authorized service. All other fields are ignored."""
        url = f"/config/access/authorized_services/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_access_authorized_services_id(self, id, **kwargs: Any) -> Any:
        """Deletes an authorized service.
 Any user or authorized service can call this endpoint. If the caller has the Administrator Manager permission, then they can delete any authorized service. If the caller does not have the Administrator Manager permission, then they can only delete authorized services that they've created."""
        url = f"/config/access/authorized_services/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_access_security_profiles(self, tenant_id: Optional[Any] = None, current_security_profile: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the list of deployed security profiles available in the system."""
        url = "/config/access/security_profiles"
        params = {"tenant_id": tenant_id, "current_security_profile": current_security_profile}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_access_security_profiles_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get a deployed security profile by ID."""
        url = f"/config/access/security_profiles/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_access_tenant_management_tenants(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve the list of all tenants ordered by tenant id."""
        url = "/config/access/tenant_management/tenants"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_access_tenant_management_tenants(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create a new tenant."""
        url = "/config/access/tenant_management/tenants"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_access_tenant_management_tenants_tenant_id(self, tenant_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a tenant by tenant id."""
        url = f"/config/access/tenant_management/tenants/{tenant_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_access_tenant_management_tenants_tenant_id(self, tenant_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a tenant"""
        url = f"/config/access/tenant_management/tenants/{tenant_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_access_tenant_management_tenants_tenant_id(self, tenant_id, **kwargs: Any) -> Any:
        """Delete a tenant."""
        url = f"/config/access/tenant_management/tenants/{tenant_id}"
        return self._s.delete(url, **kwargs)

    def get_config_access_user_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent user task status."""
        url = f"/config/access/user_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_access_user_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels a dependent user task."""
        url = f"/config/access/user_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_access_user_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the user dependent task results."""
        url = f"/config/access/user_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_access_user_roles(self, current_user_role: Optional[Any] = None, contains: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the list of deployed user roles available in the system."""
        url = "/config/access/user_roles"
        params = {"current_user_role": current_user_role, "contains": contains}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_access_user_roles_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get a deployed user role by ID."""
        url = f"/config/access/user_roles/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_access_users(self, current_user: Optional[Any] = None, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve Deployed Users."""
        url = "/config/access/users"
        params = {"current_user": current_user}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_config_access_users_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a deployed user."""
        url = f"/config/access/users/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_access_users_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a deployed user."""
        url = f"/config/access/users/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_access_users_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the user."""
        url = f"/config/access/users/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_backup_and_restore_scheduled_backup_configurations(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of Backup Configurations."""
        url = "/config/backup_and_restore/scheduled_backup_configurations"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_backup_and_restore_scheduled_backup_configurations_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a Backup Configuration by ID."""
        url = f"/config/backup_and_restore/scheduled_backup_configurations/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_certificates_components(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, sort: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of registered components."""
        url = "/config/certificates/components"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_config_certificates_end_certificates(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of deployed certificates."""
        url = "/config/certificates/end_certificates"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_certificates_end_certificates_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets information about a specific deployed certificate, as specified the certificate ID."""
        url = f"/config/certificates/end_certificates/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_certificates_end_certificates_id_full_chain(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the full chain of the certificate. The chain hierarchy includes the content of the end certificate, and the content of the issuer chain certificates, up to and including the root certificate.
  This endpoint might not return the root certificate if it was uploaded in the last 24 hours"""
        url = f"/config/certificates/end_certificates/{id}/full_chain"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_certificates_root_certificates(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of all root certificates that have been uploaded and deployed.
You must have System Administrator or Security Administrator permissions to use this endpoint."""
        url = "/config/certificates/root_certificates"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_certificates_root_certificates_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets details of a deployed root certificate, as specified by the ID.
You must have System Administrator or Security Administrator permissions to use this endpoint."""
        url = f"/config/certificates/root_certificates/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_certificates_root_certificates_id_get_dependant_ids(self, id, **kwargs: Any) -> Any:
        """Gets a list of end certificate IDs that depend on the root certificate. This endpoint
might not return the dependent IDs of the certificates that were uploaded in the last 24 hours.You
must have System Administrator or Security Administrator permissions to use this
endpoint."""
        url = f"/config/certificates/root_certificates/{id}/get_dependant_ids"
        return self._s.get(url, **kwargs)

    def get_config_deployment_hosts(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of all deployed hosts."""
        url = "/config/deployment/hosts"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_deployment_hosts_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a deployed host by ID."""
        url = f"/config/deployment/hosts/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_deployment_hosts_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a host by ID and sends a JMS message to update the pipeline."""
        url = f"/config/deployment/hosts/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_deployment_hosts_id_tunnels(self, id, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of tunnels for the host."""
        url = f"/config/deployment/hosts/{id}/tunnels"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_deployment_license_pool(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the deployed license pool information."""
        url = "/config/deployment/license_pool"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_domain_management_domains(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of domains."""
        url = "/config/domain_management/domains"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_domain_management_domains(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new domain."""
        url = "/config/domain_management/domains"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_domain_management_domains_domain_id(self, domain_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual domain by ID"""
        url = f"/config/domain_management/domains/{domain_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_domain_management_domains_domain_id(self, domain_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing domain."""
        url = f"/config/domain_management/domains/{domain_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_domain_management_domains_domain_id(self, domain_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes a domain by domain id."""
        url = f"/config/domain_management/domains/{domain_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_config_event_retention_buckets(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of event retention buckets."""
        url = "/config/event_retention_buckets"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_retention_buckets_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an event retention bucket."""
        url = f"/config/event_retention_buckets/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_retention_buckets_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the event retention bucket owner or enabled/disabled only."""
        url = f"/config/event_retention_buckets/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_retention_buckets_id(self, id, **kwargs: Any) -> Any:
        """Deletes an event retention bucket."""
        url = f"/config/event_retention_buckets/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_calculated_properties(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of calculated event properties."""
        url = "/config/event_sources/custom_properties/calculated_properties"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_calculated_properties(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new calculated event property."""
        url = "/config/event_sources/custom_properties/calculated_properties"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a calculated event property based on the supplied calculated property identifier."""
        url = f"/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing calculated event property."""
        url = f"/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes the event calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_properties_calculated_property_id_dependents(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the event calculated property."""
        url = f"/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_properties_calculated_property_id_dependents_disable(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the event calculated property."""
        url = f"/config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_properties_dep_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a calculated event property based on the supplied calculated property ID."""
        url = f"/config/event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_calculated_property_name(self, calculated_property_name, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of event calculated properties."""
        url = f"/config/event_sources/custom_properties/calculated_property/{calculated_property_name}"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of the event calculated property delete task."""
        url = f"/config/event_sources/custom_properties/calculated_property_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the event calculated property dependent task status."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the calculated property dependent task."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the calculated property dependent task results."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of the event calculated property dependents task."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_calculated_property_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the event calculated property dependent task."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the calculated property dependent task results."""
        url = f"/config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_calculated_property_operands(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of available options for calculated event property operand."""
        url = "/config/event_sources/custom_properties/calculated_property_operands"
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)

    def get_config_event_sources_custom_properties_property_aql_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of Custom Property AQL Expressions. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = "/config/event_sources/custom_properties/property_aql_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_aql_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new Custom Property AQL expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = "/config/event_sources/custom_properties/property_aql_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_aql_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets a Custom Property AQL Expression by ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_aql_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_aql_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a Custom Property AQL expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_aql_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_aql_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a Custom Property AQL expression based on the supplied expression ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_aql_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_calculated_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of Custom Property Calculated Expressions. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = "/config/event_sources/custom_properties/property_calculated_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_calculated_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new Custom Property Calculated Expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = "/config/event_sources/custom_properties/property_calculated_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_calculated_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets a Custom Property Calculated Expression by ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_calculated_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a Custom Property Calculated Expression. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_calculated_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a Custom Property Calculated Expression based on the supplied expression ID. Requires the System Administrator, Security Admin or User Defined Event Properties permission."""
        url = f"/config/event_sources/custom_properties/property_calculated_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_cef_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of CEF expressions."""
        url = "/config/event_sources/custom_properties/property_cef_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_cef_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new CEF expression."""
        url = "/config/event_sources/custom_properties/property_cef_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_cef_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a CEF expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_cef_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_cef_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing CEF expression."""
        url = f"/config/event_sources/custom_properties/property_cef_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_cef_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a CEF expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_cef_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of event regex property expressions."""
        url = "/config/event_sources/custom_properties/property_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new event regex property expression."""
        url = "/config/event_sources/custom_properties/property_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a event regex property expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing event regex property expression."""
        url = f"/config/event_sources/custom_properties/property_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes an event regex property expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_genericlist_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of Generic List expressions."""
        url = "/config/event_sources/custom_properties/property_genericlist_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_genericlist_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new Generic List expression."""
        url = "/config/event_sources/custom_properties/property_genericlist_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_genericlist_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a Generic List expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_genericlist_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing Generic List expression."""
        url = f"/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_genericlist_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a Generic List expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_json_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of JSON expressions."""
        url = "/config/event_sources/custom_properties/property_json_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_json_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new JSON expression."""
        url = "/config/event_sources/custom_properties/property_json_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_json_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a JSON expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_json_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_json_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing JSON expression."""
        url = f"/config/event_sources/custom_properties/property_json_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_json_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a JSON expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_json_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_leef_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of LEEF Expressions."""
        url = "/config/event_sources/custom_properties/property_leef_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_leef_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new LEEF Expression."""
        url = "/config/event_sources/custom_properties/property_leef_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_leef_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a LEEF Expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_leef_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_leef_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing LEEF Expression."""
        url = f"/config/event_sources/custom_properties/property_leef_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_leef_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a LEEF Expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_leef_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_nvp_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of Name Value Pair expressions."""
        url = "/config/event_sources/custom_properties/property_nvp_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_nvp_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new Name Value Pair expression."""
        url = "/config/event_sources/custom_properties/property_nvp_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_nvp_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a Name Value Pair expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_nvp_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing Name Value Pair expression."""
        url = f"/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_nvp_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a Name Value Pair expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_nvp_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_property_xml_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of XML expressions."""
        url = "/config/event_sources/custom_properties/property_xml_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_property_xml_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new XML expression."""
        url = "/config/event_sources/custom_properties/property_xml_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_property_xml_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a XML expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_xml_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_property_xml_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing XML expression."""
        url = f"/config/event_sources/custom_properties/property_xml_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_property_xml_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes an XML expression based on the supplied identifier."""
        url = f"/config/event_sources/custom_properties/property_xml_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_custom_properties_regex_properties(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of event regex properties."""
        url = "/config/event_sources/custom_properties/regex_properties"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_custom_properties_regex_properties(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new event regex property."""
        url = "/config/event_sources/custom_properties/regex_properties"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a event regex property based on the supplied regex property ID."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing event regex property."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes an event regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_properties_regex_property_id_dependents(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the event regex property."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_properties_regex_property_id_dependents_change_field_type(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the event regex property for changing type of field for it."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_properties_regex_property_id_dependents_disable(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the event regex property for disabling it."""
        url = f"/config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the event regex property delete task status."""
        url = f"/config/event_sources/custom_properties/regex_property_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the event regex property dependent task status."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the regex property dependent task."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_disable_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the event regex property dependent task status."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_regex_property_dependent_tasks_disable_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the regex property dependent task."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_disable_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the event regex property dependent task status."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_custom_properties_regex_property_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the regex property dependent task."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_custom_properties_regex_property_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_disconnected_log_collectors(self, **kwargs: Any) -> Any:
        """Retrieves a list of disconnected log collectors."""
        url = "/config/event_sources/disconnected_log_collectors"
        return self._s.get(url, **kwargs)

    def post_config_event_sources_disconnected_log_collectors(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new disconnected log collector. A disconnected log collector contains the
following fields:"""
        url = "/config/event_sources/disconnected_log_collectors"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_disconnected_log_collectors_id(self, **kwargs: Any) -> Any:
        """Retrieves an disconnected log collector by ID.."""
        url = "/config/event_sources/disconnected_log_collectors/{id}"
        return self._s.get(url, **kwargs)

    def post_config_event_sources_disconnected_log_collectors_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a disconnected log collector by ID. A disconnected log collector contains the
following fields:"""
        url = f"/config/event_sources/disconnected_log_collectors/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_disconnected_log_collectors_id(self, id, **kwargs: Any) -> Any:
        """Deletes a Disconnected Log Collector by ID."""
        url = f"/config/event_sources/disconnected_log_collectors/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_event_collectors(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of event collectors.."""
        url = "/config/event_sources/event_collectors"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_event_collectors_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an event collector by ID.."""
        url = f"/config/event_sources/event_collectors/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_generated_regexes(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a regex pattern"""
        url = "/config/event_sources/generated_regexes"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_autodetection_config_records(self, sort: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of Autodetection Config Records."""
        url = "/config/event_sources/log_source_management/autodetection/config_records"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_config_event_sources_log_source_management_autodetection_config_records(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates an Autodetection Config Record."""
        url = "/config/event_sources/log_source_management/autodetection/config_records"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_autodetection_config_records_config_id(self, config_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual Autodetection Config Record by id."""
        url = f"/config/event_sources/log_source_management/autodetection/config_records/{config_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_autodetection_config_records_config_id(self, config_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an Autodetection Config Record."""
        url = f"/config/event_sources/log_source_management/autodetection/config_records/{config_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_bulk_tasks_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source bulk task by ID."""
        url = f"/config/event_sources/log_source_management/log_source_bulk_tasks/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_source_bulk_tasks_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a log source bulk task.
 
 The only field that can be updated is the 'status' field, and the only allowed value is 'CANCELLED'."""
        url = f"/config/event_sources/log_source_management/log_source_bulk_tasks/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_extensions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of log source extensions."""
        url = "/config/event_sources/log_source_management/log_source_extensions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_log_source_management_log_source_extensions_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source extension by ID."""
        url = f"/config/event_sources/log_source_management/log_source_extensions/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_log_source_management_log_source_groups(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of log source groups."""
        url = "/config/event_sources/log_source_management/log_source_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_log_source_management_log_source_groups(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new log source group. A log source group contains the following fields:"""
        url = "/config/event_sources/log_source_management/log_source_groups"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_groups_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source group by ID."""
        url = f"/config/event_sources/log_source_management/log_source_groups/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_log_source_management_log_source_languages(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of log source languages."""
        url = "/config/event_sources/log_source_management/log_source_languages"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_log_source_management_log_source_languages_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source language by ID."""
        url = f"/config/event_sources/log_source_management/log_source_languages/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_source_statistics(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates log source statistics Log source statistics contains the following fields:
LogSourceFieldValueStatistic contains the following fields:"""
        url = "/config/event_sources/log_source_management/log_source_statistics"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of log source types. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned in each log source type. If called by a less privileged client, only name and ID are returned in each log source type."""
        url = "/config/event_sources/log_source_management/log_source_types"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_log_source_management_log_source_types(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create a new custom log source type. Log source types do not need to be deployed. The
following fields can be provided in the body of this request, all other log source type fields will
be ignored:"""
        url = "/config/event_sources/log_source_management/log_source_types"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve dsm parameter allowed values."""
        url = "/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def patch_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(self, body: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create new dsm parameter allowed values or Update available dsm parameter allowed values.

 The following fields can be provided in the body of this request, all other dsm parameter allowed value fields will be ignored:
 >"""
        url = "/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values"
        headers = {"fields": fields, "filter": filter}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, range_header=range_header, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a dsm parameter allowed value by id."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a dsm parameter allowed value by id."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_id(self, id, **kwargs: Any) -> Any:
        """Deletes a dsm paramater allowed value by ID."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_definition(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve dsm parameter definitions."""
        url = "/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve dsm parameters."""
        url = "/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def patch_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, body: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Create new dsm parameters or Update available dsm parameters.

 The following fields can be provided in the body of this request, all other dsm parameter fields will be ignored:"""
        url = "/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters"
        headers = {"fields": fields, "filter": filter}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.patch(url, headers=headers, range_header=range_header, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a dsm parameter by id."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a dsm parameter by id."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_id(self, id, **kwargs: Any) -> Any:
        """Deletes a dsm paramater by ID."""
        url = f"/config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_log_source_management_log_source_types_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source type by ID. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned for the log source type. If called by a less privileged client, only name and ID are returned for the log source type."""
        url = f"/config/event_sources/log_source_management/log_source_types/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_source_types_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a log source type by ID. The following fields can be provided in the body of this
request, all other log source type fields will be ignored:"""
        url = f"/config/event_sources/log_source_management/log_source_types/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_log_source_management_log_source_types_id(self, id, **kwargs: Any) -> Any:
        """Deletes a custom log source type by ID."""
        url = f"/config/event_sources/log_source_management/log_source_types/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_log_source_management_log_sources(self, x_qrd_encryption_algorithm: Optional[Any] = None, x_qrd_encryption_password: Optional[Any] = None, sort: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of log sources."""
        url = "/config/event_sources/log_source_management/log_sources"
        headers = {"x-qrd-encryption-algorithm": x_qrd_encryption_algorithm, "x-qrd-encryption-password": x_qrd_encryption_password}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_config_event_sources_log_source_management_log_sources(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new log source.

 A log source contains the following fields:"""
        url = "/config/event_sources/log_source_management/log_sources"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def patch_config_event_sources_log_source_management_log_sources(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Patches an array of log sources. Capable of creating, updating and deleting multiple log sources in the same transaction."""
        url = "/config/event_sources/log_source_management/log_sources"
        return self._s.patch(url, json_body=body, **kwargs)

    def get_config_event_sources_log_source_management_log_sources_id(self, id, x_qrd_encryption_algorithm: Optional[Any] = None, x_qrd_encryption_password: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a log source by ID."""
        url = f"/config/event_sources/log_source_management/log_sources/{id}"
        headers = {"x-qrd-encryption-algorithm": x_qrd_encryption_algorithm, "x-qrd-encryption-password": x_qrd_encryption_password}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.get(url, headers=headers, fields=fields, **kwargs)

    def post_config_event_sources_log_source_management_log_sources_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a log source by ID."""
        url = f"/config/event_sources/log_source_management/log_sources/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_log_source_management_log_sources_id(self, id, **kwargs: Any) -> Any:
        """Deletes a log source by ID."""
        url = f"/config/event_sources/log_source_management/log_sources/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_log_source_management_protocol_types(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of protocol types. Requires the System Administrator, Security Admin, or Manage Log Sources permission."""
        url = "/config/event_sources/log_source_management/protocol_types"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_log_source_management_protocol_types_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a protocol type by ID. Requires the System Administrator, Security Admin, or Manage Log Sources permission."""
        url = f"/config/event_sources/log_source_management/protocol_types/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_property_discovery_profiles(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets all PropertyDiscoveryProfiles currently in the system."""
        url = "/config/event_sources/property_discovery_profiles"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_event_sources_property_discovery_profiles(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile JSON object."""
        url = "/config/event_sources/property_discovery_profiles"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_event_sources_property_discovery_profiles_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile corresponding to the supplied ID."""
        url = f"/config/event_sources/property_discovery_profiles/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_event_sources_property_discovery_profiles_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a PropertyDiscoveryProfile based on the information supplied via the property_discovery_profile JSON object."""
        url = f"/config/event_sources/property_discovery_profiles/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_event_sources_property_discovery_profiles_id(self, id, **kwargs: Any) -> Any:
        """Deletes the specified PropertyDiscoveryProfile."""
        url = f"/config/event_sources/property_discovery_profiles/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_event_sources_wincollect_wincollect_agents(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of WinCollect agents."""
        url = "/config/event_sources/wincollect/wincollect_agents"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_wincollect_wincollect_agents_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a WinCollect agent by ID."""
        url = f"/config/event_sources/wincollect/wincollect_agents/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_event_sources_wincollect_wincollect_destinations(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of WinCollect destinations."""
        url = "/config/event_sources/wincollect/wincollect_destinations"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_event_sources_wincollect_wincollect_destinations_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a WinCollect destination by ID."""
        url = f"/config/event_sources/wincollect/wincollect_destinations/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_extension_management_extension_export_tasks(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Exports an extension."""
        url = "/config/extension_management/extension_export_tasks"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_extension_management_extension_export_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the tasks status based on the task_id."""
        url = f"/config/extension_management/extension_export_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_extension_management_extension_export_tasks_task_id_extension_export(self, task_id, **kwargs: Any) -> Any:
        """Retrieves the exported extension based on the task_id."""
        url = f"/config/extension_management/extension_export_tasks/{task_id}/extension_export"
        return self._s.get(url, **kwargs)

    def get_config_extension_management_extension_export_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the tasks status results based on the task_id."""
        url = f"/config/extension_management/extension_export_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_extension_management_extensions(self, content_limit: Optional[Any] = None, sort: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of extensions."""
        url = "/config/extension_management/extensions"
        params = {"content_limit": content_limit}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_config_extension_management_extensions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Uploads the supplied extension file to the QRadar system."""
        url = "/config/extension_management/extensions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_extension_management_extensions_extension_id(self, extension_id, content_limit: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an extension based on the supplied extension_id."""
        url = f"/config/extension_management/extensions/{extension_id}"
        params = {"content_limit": content_limit}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.get(url, params=params, fields=fields, **kwargs)

    def post_config_extension_management_extensions_extension_id(self, extension_id, action_type: Optional[Any] = None, overwrite: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Install an extension based on the supplied extension_id. This is an asynchronous action."""
        url = f"/config/extension_management/extensions/{extension_id}"
        params = {"action_type": action_type, "overwrite": overwrite}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def delete_config_extension_management_extensions_extension_id(self, extension_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Uninstall an extension based on the supplied extension_id. This is an asynchronous action."""
        url = f"/config/extension_management/extensions/{extension_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.delete(url, headers=headers, json_body=body, **kwargs)

    def post_config_extension_management_extensions_extension_id_metadata(self, extension_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Adds metadata to the Extension corresponding to the supplied extension_id."""
        url = f"/config/extension_management/extensions/{extension_id}/metadata"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_extension_management_extensions_task_status_status_id(self, status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the tasks status based on the status_id."""
        url = f"/config/extension_management/extensions_task_status/{status_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_extension_management_extensions_task_status_status_id_results(self, status_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the tasks status results based on the status_id."""
        url = f"/config/extension_management/extensions_task_status/{status_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_applications_active_applications(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, sort: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of active flow applications."""
        url = "/config/flow/applications/active_applications"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_config_flow_applications_active_applications_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual active flow application that is currently deployed in the system, as specified by the application ID.
 
 Active applications are flow applications that are currently in-use by the system.
 Changes or modifications to a flow application should always be made to the active applications list. Do not update the default applications.
 
 You must have System Administrator or Security Administrator permissions to use this endpoint."""
        url = f"/config/flow/applications/active_applications/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_applications_default_applications(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, sort: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of default flow applications."""
        url = "/config/flow/applications/default_applications"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_config_flow_applications_default_applications_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual default flow application, as specified by an ID."""
        url = f"/config/flow/applications/default_applications/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_common_destination_ports_active_configurations(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, sort: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of active configurations for common destination ports."""
        url = "/config/flow/common_destination_ports/active_configurations"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_config_flow_common_destination_ports_active_configurations(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new active configuration."""
        url = "/config/flow/common_destination_ports/active_configurations"
        return self._s.post(url, json_body=body, **kwargs)

    def get_config_flow_common_destination_ports_active_configurations_id(self, id, **kwargs: Any) -> Any:
        """Gets the active configuration for a common destination port, as specified by an ID."""
        url = f"/config/flow/common_destination_ports/active_configurations/{id}"
        return self._s.get(url, **kwargs)

    def post_config_flow_common_destination_ports_active_configurations_id(self, id, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the active configuration for a common destination port, as specified by the ID."""
        url = f"/config/flow/common_destination_ports/active_configurations/{id}"
        return self._s.post(url, json_body=body, **kwargs)

    def delete_config_flow_common_destination_ports_active_configurations_id(self, id, **kwargs: Any) -> Any:
        """Removes the active configuration for the specified ID from the system."""
        url = f"/config/flow/common_destination_ports/active_configurations/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_flow_common_destination_ports_default_configurations(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, sort: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of default configurations for common destination ports."""
        url = "/config/flow/common_destination_ports/default_configurations"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def get_config_flow_common_destination_ports_default_configurations_id(self, id, **kwargs: Any) -> Any:
        """Gets the default configuration for a common destination port, as specified by an ID."""
        url = f"/config/flow/common_destination_ports/default_configurations/{id}"
        return self._s.get(url, **kwargs)

    def get_config_flow_retention_buckets(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of flow retention buckets."""
        url = "/config/flow_retention_buckets"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_flow_retention_buckets_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a flow retention bucket."""
        url = f"/config/flow_retention_buckets/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_retention_buckets_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the flow retention bucket owner, or enabled/disabled only."""
        url = f"/config/flow_retention_buckets/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_flow_retention_buckets_id(self, id, **kwargs: Any) -> Any:
        """Deletes a flow retention bucket."""
        url = f"/config/flow_retention_buckets/{id}"
        return self._s.delete(url, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_properties(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of calculated flow properties."""
        url = "/config/flow_sources/custom_properties/calculated_properties"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_flow_sources_custom_properties_calculated_properties(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new calculated flow property."""
        url = "/config/flow_sources/custom_properties/calculated_properties"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a calculated flow property based on the supplied calculated property ID."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing calculated flow property."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_flow_sources_custom_properties_calculated_properties_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes the flow calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_properties_calculated_property_id_dependents(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the flow calculated property."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_properties_calculated_property_id_dependents_disable(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the flow calculated property."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_properties_dep_calculated_property_id(self, calculated_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a calculated flow property based on the supplied calculated property ID."""
        url = f"/config/flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_calculated_property_name(self, calculated_property_name, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of flow calculated properties."""
        url = f"/config/flow_sources/custom_properties/calculated_property/{calculated_property_name}"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of the flow calculated property delete task."""
        url = f"/config/flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the flow calculated property dependent task status."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the calculated property dependent task."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the calculated property dependent task results."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the status of the flow calculated property dependents task."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_calculated_property_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the flow calculated property dependent task."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the calculated property dependent task results."""
        url = f"/config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_calculated_property_operands(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the list of available options for calculated flow property operand."""
        url = "/config/flow_sources/custom_properties/calculated_property_operands"
        return self._s.get(url, range_header=range_header, filter_expr=filter, **kwargs)

    def get_config_flow_sources_custom_properties_property_expressions(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieve a list of flow regex property expressions."""
        url = "/config/flow_sources/custom_properties/property_expressions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_flow_sources_custom_properties_property_expressions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new flow regex property expression."""
        url = "/config/flow_sources/custom_properties/property_expressions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_property_expressions_expression_id(self, expression_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a flow regex property expression based on the supplied expression ID."""
        url = f"/config/flow_sources/custom_properties/property_expressions/{expression_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_property_expressions_expression_id(self, expression_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing flow regex property expression."""
        url = f"/config/flow_sources/custom_properties/property_expressions/{expression_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_flow_sources_custom_properties_property_expressions_expression_id(self, expression_id, **kwargs: Any) -> Any:
        """Deletes a flow regex property expression based on the supplied expression ID."""
        url = f"/config/flow_sources/custom_properties/property_expressions/{expression_id}"
        return self._s.delete(url, **kwargs)

    def get_config_flow_sources_custom_properties_regex_properties(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of flow regex properties."""
        url = "/config/flow_sources/custom_properties/regex_properties"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_flow_sources_custom_properties_regex_properties(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new flow regex property."""
        url = "/config/flow_sources/custom_properties/regex_properties"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a flow regex property based on the supplied regex property ID."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing flow regex property."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_flow_sources_custom_properties_regex_properties_regex_property_id(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes a flow regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_properties_regex_property_id_dependents(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the flow regex property."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_properties_regex_property_id_dependents_change_field_type(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the flow regex property for changing type of field for it."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_properties_regex_property_id_disabling_dependents(self, regex_property_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the flow regex property."""
        url = f"/config/flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the flow regex property delete task status."""
        url = f"/config/flow_sources/custom_properties/regex_property_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the flow regex property dependent task status."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the regex property dependent task."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_disable_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the flow regex property dependent task status."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_regex_property_dependent_tasks_disable_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the regex property dependent task."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_disable_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the flow regex property dependent task status."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_flow_sources_custom_properties_regex_property_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the flow regex property dependent task."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_flow_sources_custom_properties_regex_property_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the regex property dependent task results."""
        url = f"/config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_flow_sources_flow_source_management_flow_sources(self, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets the list of flow sources that are available to the current user."""
        url = "/config/flow_sources/flow_source_management/flowSources"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_flow_sources_flow_source_management_flow_sources_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Gets an individual Flow Source as specified by the ID."""
        url = f"/config/flow_sources/flow_source_management/flowSources/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_network_hierarchy_networks(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the deployed network hierarchy."""
        url = "/config/network_hierarchy/networks"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_network_hierarchy_staged_networks(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the staged network hierarchy."""
        url = "/config/network_hierarchy/staged_networks"
        return self._s.get(url, fields=fields, **kwargs)

    def put_config_network_hierarchy_staged_networks(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Replaces the current network hierarchy with the input that is provided."""
        url = "/config/network_hierarchy/staged_networks"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def get_config_remote_networks(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of deployed remote networks."""
        url = "/config/remote_networks"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_remote_networks_network_id(self, network_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a deployed remote network by ID."""
        url = f"/config/remote_networks/{network_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_remote_services(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of deployed remote services."""
        url = "/config/remote_services"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_remote_services_service_id(self, service_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a deployed remote service by ID."""
        url = f"/config/remote_services/{service_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_resilient_test(self, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Perform asynchronous test Resilient connection"""
        url = "/config/resilient/test"
        return self._s.post(url, fields=fields, **kwargs)

    def post_config_resilient_test_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Test the Resilient connection by using the connection ID.
 You must have the System Administrator or Security Admin permission (ADMIN | SAASADMIN capability) to use this endpoint."""
        url = f"/config/resilient/test/{id}"
        return self._s.post(url, fields=fields, **kwargs)

    def get_config_resilient_test_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Get the test Resilient connection task status
 You must have the System Administrator or Security Admin permission (ADMIN | SAASADMIN capability) to use this endpoint."""
        url = f"/config/resilient/test/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_config_resource_restrictions(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of all resource restrictions."""
        url = "/config/resource_restrictions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_config_resource_restrictions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new resource restriction."""
        url = "/config/resource_restrictions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_config_resource_restrictions_resource_restriction_id(self, resource_restriction_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a resource restriction consumer by ID."""
        url = f"/config/resource_restrictions/{resource_restriction_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def put_config_resource_restrictions_resource_restriction_id(self, resource_restriction_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a resource restriction consumer by ID."""
        url = f"/config/resource_restrictions/{resource_restriction_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.put(url, headers=headers, json_body=body, **kwargs)

    def delete_config_resource_restrictions_resource_restriction_id(self, resource_restriction_id, **kwargs: Any) -> Any:
        """Deletes a resource restriction consumer by ID."""
        url = f"/config/resource_restrictions/{resource_restriction_id}"
        return self._s.delete(url, **kwargs)

    def get_config_store_and_forward_policies(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of store and forward policies."""
        url = "/config/store_and_forward/policies"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_config_store_and_forward_policies_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a store and forward policy."""
        url = f"/config/store_and_forward/policies/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_config_store_and_forward_policies_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the store and forward policy owner only."""
        url = f"/config/store_and_forward/policies/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_config_store_and_forward_policies_id(self, id, **kwargs: Any) -> Any:
        """Deletes a store and forward policy."""
        url = f"/config/store_and_forward/policies/{id}"
        return self._s.delete(url, **kwargs)
