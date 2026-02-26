"""Custom exceptions for the QRadar SDK."""


class QRadarError(Exception):
    """Base exception for all QRadar SDK errors."""


class QRadarAPIError(QRadarError):
    """Raised when the QRadar API returns an unexpected HTTP status code."""

    def __init__(self, status_code: int, message: str, response=None):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(f"HTTP {status_code}: {message}")


class QRadarAuthError(QRadarError):
    """Raised when authentication fails."""


class QRadarNotFoundError(QRadarAPIError):
    """Raised when the requested resource is not found (HTTP 404)."""


class QRadarRateLimitError(QRadarAPIError):
    """Raised when the API rate limit is exceeded (HTTP 429)."""
