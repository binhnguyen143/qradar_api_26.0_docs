"""API methods for the ``analytics`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class AnalyticsAPI:
    """Client for the QRadar ``analytics`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_analytics_ade_rules(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of ADE rules."""
        url = "/analytics/ade_rules"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_analytics_ade_rules_ade_rule_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the delete the ADE rule task status."""
        url = f"/analytics/ade_rules/ade_rule_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_ade_rules_ade_rule_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent the ADE rule task status."""
        url = f"/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_ade_rules_ade_rule_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels a dependent the ADE rule task."""
        url = f"/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_analytics_ade_rules_ade_rule_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the ADE rule dependent task results."""
        url = f"/analytics/ade_rules/ade_rule_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_ade_rules_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an ADE rule."""
        url = f"/analytics/ade_rules/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_ade_rules_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the ADE rule owner or enabled/disabled only."""
        url = f"/analytics/ade_rules/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_ade_rules_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes an ADE rule. To ensure safe deletion, a dependency check is carried out. The check might take some time. An asynchronous task is started to do this check."""
        url = f"/analytics/ade_rules/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_analytics_ade_rules_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the ADE rule."""
        url = f"/analytics/ade_rules/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_building_blocks(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of building block rules."""
        url = "/analytics/building_blocks"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_analytics_building_blocks_building_block_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the delete the building block rule task status."""
        url = f"/analytics/building_blocks/building_block_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_building_blocks_building_block_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent the building block rule task status."""
        url = f"/analytics/building_blocks/building_block_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_building_blocks_building_block_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the dependent the building block rule task."""
        url = f"/analytics/building_blocks/building_block_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_analytics_building_blocks_building_block_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the building block rule dependent task results."""
        url = f"/analytics/building_blocks/building_block_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_building_blocks_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a building block rule."""
        url = f"/analytics/building_blocks/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_building_blocks_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the building block rule owner or enabled/disabled only."""
        url = f"/analytics/building_blocks/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_building_blocks_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Deletes the building block rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/analytics/building_blocks/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_analytics_building_blocks_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the building block rule."""
        url = f"/analytics/building_blocks/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_custom_actions_actions(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of available custom actions."""
        url = "/analytics/custom_actions/actions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_analytics_custom_actions_actions(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new custom action with the supplied fields."""
        url = "/analytics/custom_actions/actions"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_analytics_custom_actions_actions_action_id(self, action_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a custom action based on the supplied action_id."""
        url = f"/analytics/custom_actions/actions/{action_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_custom_actions_actions_action_id(self, action_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing custom action."""
        url = f"/analytics/custom_actions/actions/{action_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_custom_actions_actions_action_id(self, action_id, **kwargs: Any) -> Any:
        """Deletes an existing custom action."""
        url = f"/analytics/custom_actions/actions/{action_id}"
        return self._s.delete(url, **kwargs)

    def get_analytics_custom_actions_interpreters(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of available custom action interpreters."""
        url = "/analytics/custom_actions/interpreters"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_analytics_custom_actions_interpreters_interpreter_id(self, interpreter_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a custom action interpreter based on supplied interpreter_id."""
        url = f"/analytics/custom_actions/interpreters/{interpreter_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_custom_actions_scripts(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of meta-data for available custom action script files."""
        url = "/analytics/custom_actions/scripts"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_analytics_custom_actions_scripts(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new custom action script file. Newly created custom action script files require a deployment before using."""
        url = "/analytics/custom_actions/scripts"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_analytics_custom_actions_scripts_script_id(self, script_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves meta-data of a custom action script file based on supplied script_id."""
        url = f"/analytics/custom_actions/scripts/{script_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_custom_actions_scripts_script_id(self, script_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing custom action script file. Updated custom action script files require a deployment before using."""
        url = f"/analytics/custom_actions/scripts/{script_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_custom_actions_scripts_script_id(self, script_id, **kwargs: Any) -> Any:
        """Deletes an existing custom action script file."""
        url = f"/analytics/custom_actions/scripts/{script_id}"
        return self._s.delete(url, **kwargs)

    def get_analytics_rule_groups(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of the rule groups."""
        url = "/analytics/rule_groups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_analytics_rule_groups_group_id(self, group_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a rule group."""
        url = f"/analytics/rule_groups/{group_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_rule_groups_group_id(self, group_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the owner of a rule group."""
        url = f"/analytics/rule_groups/{group_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_rule_groups_group_id(self, group_id, **kwargs: Any) -> Any:
        """Deletes a rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/analytics/rule_groups/{group_id}"
        return self._s.delete(url, **kwargs)

    def get_analytics_rules(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of rules."""
        url = "/analytics/rules"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_analytics_rules_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a rule."""
        url = f"/analytics/rules/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_rules_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the rule owner or enabled/disabled only."""
        url = f"/analytics/rules/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_analytics_rules_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Delete the rule. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check."""
        url = f"/analytics/rules/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_analytics_rules_id_dependents(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the objects that depend on the rule."""
        url = f"/analytics/rules/{id}/dependents"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_rules_rule_delete_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the delete the rule task status."""
        url = f"/analytics/rules/rule_delete_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_rules_rule_dependent_tasks_task_id(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the dependent rule task status."""
        url = f"/analytics/rules/rule_dependent_tasks/{task_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_analytics_rules_rule_dependent_tasks_task_id(self, task_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Cancels the dependent the rule task."""
        url = f"/analytics/rules/rule_dependent_tasks/{task_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_analytics_rules_rule_dependent_tasks_task_id_results(self, task_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the rule dependent task results."""
        url = f"/analytics/rules/rule_dependent_tasks/{task_id}/results"
        return self._s.get(url, fields=fields, **kwargs)

    def get_analytics_rules_offense_contributions(self, sort: Optional[Any] = None, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves Rule Offense contributions 
 
 Retieves Rule and Offense references in the system."""
        url = "/analytics/rules_offense_contributions"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)
