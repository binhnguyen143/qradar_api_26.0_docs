"""API methods for the ``auth`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class AuthAPI:
    """Client for the QRadar ``auth`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def post_auth_logout(self, **kwargs: Any) -> Any:
        """Invoke this method as an authorized user and your session will be invalidated."""
        url = "/auth/logout"
        return self._s.post(url, **kwargs)
