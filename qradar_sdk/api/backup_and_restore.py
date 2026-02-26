"""API methods for the ``backup_and_restore`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class BackupAndRestoreAPI:
    """Client for the QRadar ``backup_and_restore`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_backup_and_restore_backups(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, sort: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of backups."""
        url = "/backup_and_restore/backups"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_backup_and_restore_backups(self, body: Optional[Any] = None, backup_type: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Submits a request to the Backup and Restore Engine to create a new backup."""
        url = "/backup_and_restore/backups"
        headers = {"backup_type": backup_type, "fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_backup_and_restore_backups_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an individual backup by ID."""
        url = f"/backup_and_restore/backups/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_backup_and_restore_backups_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing backup."""
        url = f"/backup_and_restore/backups/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_backup_and_restore_backups_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Sends a request to the Backup and Restore Engine to delete an existing backup."""
        url = f"/backup_and_restore/backups/{id}"
        return self._s.delete(url, fields=fields, **kwargs)

    def get_backup_and_restore_ha_action_flag(self, flag, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Done an individual HA Action as per passing flag."""
        url = f"/backup_and_restore/haAction/{flag}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_backup_and_restore_restores(self, range_header: Optional[Any] = None, fields: Optional[Any] = None, sort: Optional[Any] = None, filter: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a list of restores."""
        url = "/backup_and_restore/restores"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, sort=sort, **kwargs)

    def post_backup_and_restore_restores(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a restore object in the PENDING state."""
        url = "/backup_and_restore/restores"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def get_backup_and_restore_restores_id(self, id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves an individual restore by ID."""
        url = f"/backup_and_restore/restores/{id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_backup_and_restore_restores_id(self, id, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Updates an existing restore by ID."""
        url = f"/backup_and_restore/restores/{id}"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)

    def delete_backup_and_restore_restores_id(self, id, **kwargs: Any) -> Any:
        """Deletes an individual restore by ID."""
        url = f"/backup_and_restore/restores/{id}"
        return self._s.delete(url, **kwargs)

    def post_backup_and_restore_updateiptablesprefile(self, body: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Done an individual HA Action as per passing flag."""
        url = "/backup_and_restore/updateiptablesprefile"
        headers = {"fields": fields}
        headers = {k: v for k, v in headers.items() if v is not None}
        return self._s.post(url, headers=headers, json_body=body, **kwargs)
