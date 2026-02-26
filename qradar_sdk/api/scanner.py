"""API methods for the ``scanner`` tag."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .._http import QRadarSession


class ScannerAPI:
    """Client for the QRadar ``scanner`` API endpoints."""

    def __init__(self, session: QRadarSession) -> None:
        self._s = session

    def get_scanner_profiles(self, **kwargs: Any) -> Any:
        """Retrieves all of the currently created scan profiles. No parameters are required and the following information 
 should be retrieved for each scan profile
 
  - scanProfileId
  - scanProfileName
  - description
  - scanType
  - scannerName"""
        url = "/scanner/profiles"
        return self._s.get(url, **kwargs)

    def post_scanner_profiles_create(self, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Initiates a request to create a new scanProfile. The request takes one parameter - createScanRequest, which is just a POJO.

 To create the scan, you will need to build up a JSON object that contains the Scan Profile name and ips to scan e.g.
 {'name':'New Scan Profile', 'ips':['10.100.85.135']}

 Note: Only IP addresses and ranges are accepted. CIDR ranges are not supported."""
        url = "/scanner/profiles/create"
        return self._s.post(url, json_body=body, **kwargs)

    def post_scanner_profiles_start(self, scan_profile_id: Optional[Any] = None, **kwargs: Any) -> Any:
        """Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId.
 
 To get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the
 scanner endpoint. The scanProfileId will be validated and an appropriate message returned."""
        url = "/scanner/profiles/start"
        params = {"scanProfileId": scan_profile_id}
        params = {k: v for k, v in params.items() if v is not None}
        return self._s.post(url, params=params, **kwargs)

    def get_scanner_scanprofiles(self, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves all of the currently created scan profiles. No parameters are required and the following information 
 should be retrieved for each scan profile
 
  - scanProfileId
  - name
  - description
  - scanType
  - scannerName
  - schedule
  - status
  - progress
  - endTime
  - duration"""
        url = "/scanner/scanprofiles"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def get_scanner_scanprofiles_profileid(self, profileid, range_header: Optional[Any] = None, filter: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Retrieves a scan profile for a given Scan Profile ID. The only parameter required is the Scan Profile ID. The following
 information about a scan profile will be returned  
 
  - scanProfileId
  - name
  - description
  - scanType
  - scannerName
  - schedule
  - status
  - progress
  - endTime
  - duration"""
        url = f"/scanner/scanprofiles/{profileid}"
        return self._s.get(url, range_header=range_header, fields=fields, filter_expr=filter, **kwargs)

    def post_scanner_scanprofiles_profileid(self, profileid, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Update a scan profile. The Scan Profile ID is required.
  The following information on a scan profile can be updated 
 
  - name
  - description
  - ips
      eg  {'name':'Updated Scan Profile', 'ips':['10.100.85.135']}"""
        url = f"/scanner/scanprofiles/{profileid}"
        return self._s.post(url, json_body=body, **kwargs)

    def delete_scanner_scanprofiles_profileid(self, profileid, **kwargs: Any) -> Any:
        """Initiates a request to delete a  scanProfile. The request takes one parameter - the Scan Profile ID."""
        url = f"/scanner/scanprofiles/{profileid}"
        return self._s.delete(url, **kwargs)

    def get_scanner_scanprofiles_profileid_runs(self, profileid, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Call GET /scanner/scanprofiles/{profileid}/runs"""
        url = f"/scanner/scanprofiles/{profileid}/runs"
        return self._s.get(url, range_header=range_header, fields=fields, **kwargs)

    def get_scanner_scanprofiles_profileid_runs_run_id(self, profileid, run_id, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Call GET /scanner/scanprofiles/{profileid}/runs/{run_id}"""
        url = f"/scanner/scanprofiles/{profileid}/runs/{run_id}"
        return self._s.get(url, fields=fields, **kwargs)

    def get_scanner_scanprofiles_profileid_runs_run_id_results(self, profileid, run_id, range_header: Optional[Any] = None, fields: Optional[Any] = None, **kwargs: Any) -> Any:
        """Call GET /scanner/scanprofiles/{profileid}/runs/{run_id}/results"""
        url = f"/scanner/scanprofiles/{profileid}/runs/{run_id}/results"
        return self._s.get(url, range_header=range_header, fields=fields, **kwargs)

    def post_scanner_scanprofiles_profileid_start(self, profileid, body: Optional[Any] = None, **kwargs: Any) -> Any:
        """Initiates a request to start an already created scanProfile. The request takes one parameter - scanProfileId, and one optional parameter - ips.
 
 To get a list of scanProfileIds, simply get a list of the current scan profiles by initiating a 'profiles' request on the
 scanner endpoint. The scanProfileId will be validated and an appropriate message returned."""
        url = f"/scanner/scanprofiles/{profileid}/start"
        return self._s.post(url, json_body=body, **kwargs)
