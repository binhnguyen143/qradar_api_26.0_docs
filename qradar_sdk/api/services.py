"""API methods for the ``services`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ServicesAPI:
    """Client for the QRadar ``services`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def post_services_dig_lookups(self, ip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new DIG lookup. Lookup completes in the background."""
        url = "/services/dig_lookups"
        params = {"IP": ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_services_dig_lookups_dig_lookup_id(self, dig_lookup_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the DIG lookup status. The result is included if the lookup completed."""
        url = f"/services/dig_lookups/{dig_lookup_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_services_dns_lookups(self, ip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new DNS lookup. Lookup completes in the background."""
        url = "/services/dns_lookups"
        params = {"IP": ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_services_dns_lookups_dns_lookup_id(self, dns_lookup_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the DNS lookup status. The result is included if the lookup completes."""
        url = f"/services/dns_lookups/{dns_lookup_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_services_geolocations(self, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the MaxMind geoip data for the given IP address."""
        url = "/services/geolocations"
        return self._s.get(url, fields=fields, filter_expr=filter, **kwargs)

    def post_services_port_scans(self, ip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new PortScans lookup. Port scan completes in the background."""
        url = "/services/port_scans"
        params = {"IP": ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_services_port_scans_port_scan_id(self, port_scan_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the port scan status. The result is included if the port scan completes."""
        url = f"/services/port_scans/{port_scan_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def post_services_whois_lookups(self, ip: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Creates a new WHOIS lookup. Lookup completes in the background."""
        url = "/services/whois_lookups"
        params = {"IP": ip}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, fields=fields, **kwargs)

    def get_services_whois_lookups_whois_lookup_id(self, whois_lookup_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves the WHOIS lookup status. The result is included if the lookup completes."""
        url = f"/services/whois_lookups/{whois_lookup_id}"
        return self._s.get(url, fields=fields, **kwargs)
