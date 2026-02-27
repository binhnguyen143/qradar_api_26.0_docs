"""API methods for the ``disaster_recovery`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class DisasterRecoveryAPI:
    """Client for the QRadar ``disaster_recovery`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_disaster_recovery_ariel_copy_profiles(self, fields: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of the Ariel Copy Profiles."""
        url = "/disaster_recovery/ariel_copy_profiles"
        return self._s.get(url, fields=fields, filter_expr=filter, **kwargs)

    def post_disaster_recovery_ariel_copy_profiles(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new Ariel Copy Profile."""
        url = "/disaster_recovery/ariel_copy_profiles"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_disaster_recovery_ariel_copy_profiles_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a Ariel Copy Profile by ID."""
        url = f"/disaster_recovery/ariel_copy_profiles/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_disaster_recovery_ariel_copy_profiles_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates a Ariel Copy Profile by ID."""
        url = f"/disaster_recovery/ariel_copy_profiles/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_disaster_recovery_ariel_copy_profiles_id(self, id, **kwargs: Any) -> Any:
        """Deletes a Ariel Copy Profile by ID."""
        url = f"/disaster_recovery/ariel_copy_profiles/{id}"
        return self._s.delete(url, **kwargs)
