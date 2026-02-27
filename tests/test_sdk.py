"""Tests for the QRadar Python SDK."""

import pytest
import responses as rsps_lib

from qradar_sdk import QRadarClient, QRadarAPIError, QRadarAuthError, QRadarNotFoundError
from qradar_sdk._http import QRadarSession
from qradar_sdk.exceptions import QRadarRateLimitError


BASE_URL = "https://qradar.test/api"
SEC_TOKEN = "test-sec-token-1234"


# ---------------------------------------------------------------------------
# QRadarSession – authentication
# ---------------------------------------------------------------------------


class TestQRadarSessionAuth:
    def test_sec_token_sets_header(self):
        session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        assert session._session.headers["SEC"] == SEC_TOKEN
        assert "Authorization" not in session._session.headers
        session.close()

    def test_basic_auth_sets_auth(self):
        session = QRadarSession(host="qradar.test", username="admin", password="s3cr3t", verify_ssl=False)
        assert session._session.auth == ("admin", "s3cr3t")
        assert "SEC" not in session._session.headers
        session.close()

    def test_version_header_set(self):
        session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        assert session._session.headers["Version"] == "26.0"
        session.close()

    def test_custom_version(self):
        session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, version="25.0", verify_ssl=False)
        assert session._session.headers["Version"] == "25.0"
        session.close()

    def test_missing_auth_raises(self):
        with pytest.raises(QRadarAuthError):
            QRadarSession(host="qradar.test")

    def test_base_url_construction(self):
        session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        assert session.base_url == "https://qradar.test/api"
        session.close()

    def test_base_url_with_scheme(self):
        session = QRadarSession(host="https://qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        assert session.base_url == "https://qradar.test/api"
        session.close()

    def test_context_manager(self):
        with QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False) as s:
            assert s.base_url == "https://qradar.test/api"


# ---------------------------------------------------------------------------
# QRadarSession – HTTP methods (mocked)
# ---------------------------------------------------------------------------


@rsps_lib.activate
def test_get_request_parses_json():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses", json=[{"id": 1}], status=200)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    result = session.get("/siem/offenses")
    assert result == [{"id": 1}]
    session.close()


@rsps_lib.activate
def test_post_request_sends_json_body():
    rsps_lib.add(
        rsps_lib.POST,
        f"{BASE_URL}/ariel/searches",
        json={"search_id": "abc123", "status": "EXECUTE"},
        status=201,
    )
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    result = session.post("/ariel/searches", json_body={"query_expression": "SELECT * FROM events"})
    assert result["search_id"] == "abc123"
    session.close()


@rsps_lib.activate
def test_range_header_uses_items_prefix():
    def callback(request):
        assert request.headers.get("Range") == "items=0-49"
        return (200, {}, '[{"id": 1}]')

    rsps_lib.add_callback(rsps_lib.GET, f"{BASE_URL}/siem/offenses", callback)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    session.get("/siem/offenses", range_header="0-49")
    session.close()


@rsps_lib.activate
def test_filter_added_to_query_params():
    def callback(request):
        from urllib.parse import parse_qs, urlparse
        parsed = urlparse(request.url)
        qs = parse_qs(parsed.query)
        assert qs.get("filter") == ["status=OPEN"]
        return (200, {}, "[]")

    rsps_lib.add_callback(rsps_lib.GET, f"{BASE_URL}/siem/offenses", callback)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    session.get("/siem/offenses", filter_expr="status=OPEN")
    session.close()


@rsps_lib.activate
def test_404_raises_not_found():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses/9999",
                 json={"message": "Offense not found"}, status=404)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    with pytest.raises(QRadarNotFoundError) as exc_info:
        session.get("/siem/offenses/9999")
    assert exc_info.value.status_code == 404
    session.close()


@rsps_lib.activate
def test_401_raises_auth_error():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses",
                 json={"message": "Unauthorized"}, status=401)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    with pytest.raises(QRadarAuthError):
        session.get("/siem/offenses")
    session.close()


@rsps_lib.activate
def test_429_raises_rate_limit_error():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses",
                 json={"message": "Too many requests"}, status=429)
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    with pytest.raises(QRadarRateLimitError):
        session.get("/siem/offenses")
    session.close()


@rsps_lib.activate
def test_500_raises_api_error():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses",
                 json={"message": "Internal server error"}, status=500)
    # max_retries=0 prevents retry behaviour from masking the 500 in tests
    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False, max_retries=0)
    with pytest.raises(QRadarAPIError) as exc_info:
        session.get("/siem/offenses")
    assert exc_info.value.status_code == 500
    session.close()


@rsps_lib.activate
def test_paginate_yields_pages():
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses",
                 json=[{"id": 1}, {"id": 2}], status=200,
                 headers={"Content-Range": "items 0-1/10"})
    rsps_lib.add(rsps_lib.GET, f"{BASE_URL}/siem/offenses",
                 json=[{"id": 3}], status=200,
                 headers={"Content-Range": "items 2-2/10"})

    session = QRadarSession(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    pages = list(session.paginate("/siem/offenses", page_size=2))
    assert pages[0] == [{"id": 1}, {"id": 2}]
    assert pages[1] == [{"id": 3}]
    session.close()


# ---------------------------------------------------------------------------
# QRadarClient – structure
# ---------------------------------------------------------------------------


class TestQRadarClient:
    def test_all_api_tags_accessible(self):
        client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        expected_tags = [
            "access", "analytics", "ariel", "asset_model", "auth",
            "backup_and_restore", "bandwidth_manager", "config",
            "data_classification", "disaster_recovery", "dynamic_search",
            "forensics", "gui_app_framework", "health", "health_data",
            "help", "qni", "qrm", "qvm", "reference_data",
            "reference_data_collections", "scanner", "services", "siem",
            "staged_config", "system",
        ]
        for tag in expected_tags:
            assert hasattr(client, tag), f"Missing API tag: {tag}"
        client.close()

    def test_total_method_count(self):
        client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        count = sum(
            len([m for m in dir(getattr(client, tag)) if not m.startswith("_")])
            for tag in vars(client)
            if not tag.startswith("_")
        )
        assert count == 729
        client.close()

    def test_context_manager(self):
        with QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False) as client:
            assert hasattr(client, "siem")

    def test_sec_token_in_session(self):
        client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
        assert client._session._session.headers["SEC"] == SEC_TOKEN
        client.close()


# ---------------------------------------------------------------------------
# SIEM API – specific methods
# ---------------------------------------------------------------------------


@rsps_lib.activate
def test_siem_get_offenses():
    rsps_lib.add(
        rsps_lib.GET,
        f"{BASE_URL}/siem/offenses",
        json=[{"id": 42, "description": "Test offense", "status": "OPEN"}],
        status=200,
    )
    client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    offenses = client.siem.get_siem_offenses()
    assert len(offenses) == 1
    assert offenses[0]["id"] == 42
    client.close()


@rsps_lib.activate
def test_siem_get_offense_by_id():
    rsps_lib.add(
        rsps_lib.GET,
        f"{BASE_URL}/siem/offenses/42",
        json={"id": 42, "status": "OPEN"},
        status=200,
    )
    client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    offense = client.siem.get_siem_offenses_offense_id(offense_id=42)
    assert offense["id"] == 42
    client.close()


@rsps_lib.activate
def test_siem_get_offense_not_found():
    rsps_lib.add(
        rsps_lib.GET,
        f"{BASE_URL}/siem/offenses/9999",
        json={"message": "Not found"},
        status=404,
    )
    client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    with pytest.raises(QRadarNotFoundError):
        client.siem.get_siem_offenses_offense_id(offense_id=9999)
    client.close()


# ---------------------------------------------------------------------------
# Ariel API – specific methods
# ---------------------------------------------------------------------------


@rsps_lib.activate
def test_ariel_post_searches():
    rsps_lib.add(
        rsps_lib.POST,
        f"{BASE_URL}/ariel/searches",
        json={"search_id": "search-001", "status": "EXECUTE"},
        status=201,
    )
    client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    # Ariel AQL searches use query_expression as a query parameter, not a body
    result = client.ariel.post_ariel_searches(
        query_expression="SELECT * FROM events LAST 5 MINUTES"
    )
    assert result["search_id"] == "search-001"
    client.close()


@rsps_lib.activate
def test_ariel_get_search_status():
    rsps_lib.add(
        rsps_lib.GET,
        f"{BASE_URL}/ariel/searches/search-001",
        json={"search_id": "search-001", "status": "COMPLETED", "progress": 100},
        status=200,
    )
    client = QRadarClient(host="qradar.test", sec_token=SEC_TOKEN, verify_ssl=False)
    status = client.ariel.get_ariel_searches_search_id(search_id="search-001")
    assert status["status"] == "COMPLETED"
    client.close()
