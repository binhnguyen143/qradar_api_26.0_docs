"""API methods for the ``qni`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class QniAPI:
    """Client for the QRadar ``qni`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_qni_hosts_host_id_configs(self, host_id, fields: Optional[Any] = None, filter: Optional[Any] = None, range_header: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of QNI configurations. The list contains a single configuration."""
        url = f"/qni/hosts/{host_id}/configs"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_qni_hosts_host_id_configs_id(self, host_id, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates the configuration of a QNI host. You cannot use this endpoint to update a host that is a part of a QNI stack. Use the QNI Stacking API instead."""
        url = f"/qni/hosts/{host_id}/configs/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_qni_stacking_stacks(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of all QNI stacks in the system."""
        url = "/qni/stacking/stacks"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_qni_stacking_stacks(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a QNI stack."""
        url = "/qni/stacking/stacks"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_qni_stacking_stacks_stack_id(self, stack_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a QNI stack, as specified by the stack ID."""
        url = f"/qni/stacking/stacks/{stack_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_qni_stacking_stacks_stack_id(self, stack_id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a QNI stack, as specified by the stack ID."""
        url = f"/qni/stacking/stacks/{stack_id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_qni_stacking_stacks_stack_id(self, stack_id, **kwargs: Any) -> Any:
        """Deletes a QNI stack, as specified by the stack ID."""
        url = f"/qni/stacking/stacks/{stack_id}"
        return self._s.delete(url, **kwargs)

    def get_qni_stacking_standalone_hosts(self, filter: Optional[Any] = None, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of all standalone QNI hosts that can be added to a stack. (Not all QNI appliance types are stackable.)"""
        url = "/qni/stacking/standalone_hosts"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)
