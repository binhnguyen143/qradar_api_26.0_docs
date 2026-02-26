"""
QRadar Python SDK – main client entry-point.

Usage::

    from qradar_sdk import QRadarClient

    client = QRadarClient(
        host="qradar.example.com",
        sec_token="<your-service-token>",
        verify_ssl=False,   # set to True (or a CA bundle path) in production
    )

    # List open offenses
    offenses = client.siem.get_siem_offenses(filter="status=OPEN", range_header="0-49")

    # Run an Ariel search
    search = client.ariel.post_ariel_searches(
        body={"query_expression": "SELECT * FROM events LAST 5 MINUTES"}
    )

Authentication
--------------
QRadar supports two authentication methods:

1. **SEC token** (recommended for service-to-service integration)::

    client = QRadarClient(host="...", sec_token="<token>")

2. **Basic auth** (username + password)::

    client = QRadarClient(host="...", username="admin", password="secret")

API reference
-------------
Each QRadar API tag is exposed as an attribute on :class:`QRadarClient`:

    access: :class:`~qradar_sdk.api.access.AccessAPI`
    analytics: :class:`~qradar_sdk.api.analytics.AnalyticsAPI`
    ariel: :class:`~qradar_sdk.api.ariel.ArielAPI`
    asset_model: :class:`~qradar_sdk.api.asset_model.AssetModelAPI`
    auth: :class:`~qradar_sdk.api.auth_api.AuthAPI`
    backup_and_restore: :class:`~qradar_sdk.api.backup_and_restore.BackupAndRestoreAPI`
    bandwidth_manager: :class:`~qradar_sdk.api.bandwidth_manager.BandwidthManagerAPI`
    config: :class:`~qradar_sdk.api.config.ConfigAPI`
    data_classification: :class:`~qradar_sdk.api.data_classification.DataClassificationAPI`
    disaster_recovery: :class:`~qradar_sdk.api.disaster_recovery.DisasterRecoveryAPI`
    dynamic_search: :class:`~qradar_sdk.api.dynamic_search.DynamicSearchAPI`
    forensics: :class:`~qradar_sdk.api.forensics.ForensicsAPI`
    gui_app_framework: :class:`~qradar_sdk.api.gui_app_framework.GuiAppFrameworkAPI`
    health: :class:`~qradar_sdk.api.health.HealthAPI`
    health_data: :class:`~qradar_sdk.api.health_data.HealthDataAPI`
    help: :class:`~qradar_sdk.api.help_api.HelpAPI`
    qni: :class:`~qradar_sdk.api.qni.QniAPI`
    qrm: :class:`~qradar_sdk.api.qrm.QrmAPI`
    qvm: :class:`~qradar_sdk.api.qvm.QvmAPI`
    reference_data: :class:`~qradar_sdk.api.reference_data.ReferenceDataAPI`
    reference_data_collections: :class:`~qradar_sdk.api.reference_data_collections.ReferenceDataCollectionsAPI`
    scanner: :class:`~qradar_sdk.api.scanner.ScannerAPI`
    services: :class:`~qradar_sdk.api.services.ServicesAPI`
    siem: :class:`~qradar_sdk.api.siem.SiemAPI`
    staged_config: :class:`~qradar_sdk.api.staged_config.StagedConfigAPI`
    system: :class:`~qradar_sdk.api.system.SystemAPI`
"""

from __future__ import annotations

from typing import Optional, Union

from ._http import QRadarSession
from .api.access import AccessAPI
from .api.analytics import AnalyticsAPI
from .api.ariel import ArielAPI
from .api.asset_model import AssetModelAPI
from .api.auth_api import AuthAPI
from .api.backup_and_restore import BackupAndRestoreAPI
from .api.bandwidth_manager import BandwidthManagerAPI
from .api.config import ConfigAPI
from .api.data_classification import DataClassificationAPI
from .api.disaster_recovery import DisasterRecoveryAPI
from .api.dynamic_search import DynamicSearchAPI
from .api.forensics import ForensicsAPI
from .api.gui_app_framework import GuiAppFrameworkAPI
from .api.health import HealthAPI
from .api.health_data import HealthDataAPI
from .api.help_api import HelpAPI
from .api.qni import QniAPI
from .api.qrm import QrmAPI
from .api.qvm import QvmAPI
from .api.reference_data import ReferenceDataAPI
from .api.reference_data_collections import ReferenceDataCollectionsAPI
from .api.scanner import ScannerAPI
from .api.services import ServicesAPI
from .api.siem import SiemAPI
from .api.staged_config import StagedConfigAPI
from .api.system import SystemAPI


class QRadarClient:
    """Top-level client for the IBM QRadar REST API (version 26.0).

    :param host: Hostname or IP address of the QRadar console
        (e.g. ``"qradar.example.com"`` or ``"192.168.1.10"``).
    :param sec_token: QRadar service token (SEC header).  Either this *or*
        ``username``/``password`` must be provided.
    :param username: QRadar username for Basic auth.
    :param password: QRadar password for Basic auth.
    :param version: API version string (default: ``"26.0"``).
    :param verify_ssl: TLS certificate verification.  Accepts ``True``
        (verify with default CA bundle), ``False`` (disable – only for dev/test),
        or a path to a custom CA bundle.
    :param timeout: Per-request timeout in seconds (default: 30).
    :param max_retries: Maximum number of retries for failed requests (default: 3).
    """

    def __init__(
        self,
        host: str,
        *,
        sec_token: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        version: str = "26.0",
        verify_ssl: Union[bool, str] = True,
        timeout: int = 30,
        max_retries: int = 3,
    ) -> None:
        session = QRadarSession(
            host=host,
            sec_token=sec_token,
            username=username,
            password=password,
            version=version,
            verify_ssl=verify_ssl,
            timeout=timeout,
            max_retries=max_retries,
        )
        self._session = session
        self.access: AccessAPI = AccessAPI(session)
        self.analytics: AnalyticsAPI = AnalyticsAPI(session)
        self.ariel: ArielAPI = ArielAPI(session)
        self.asset_model: AssetModelAPI = AssetModelAPI(session)
        self.auth: AuthAPI = AuthAPI(session)
        self.backup_and_restore: BackupAndRestoreAPI = BackupAndRestoreAPI(session)
        self.bandwidth_manager: BandwidthManagerAPI = BandwidthManagerAPI(session)
        self.config: ConfigAPI = ConfigAPI(session)
        self.data_classification: DataClassificationAPI = DataClassificationAPI(session)
        self.disaster_recovery: DisasterRecoveryAPI = DisasterRecoveryAPI(session)
        self.dynamic_search: DynamicSearchAPI = DynamicSearchAPI(session)
        self.forensics: ForensicsAPI = ForensicsAPI(session)
        self.gui_app_framework: GuiAppFrameworkAPI = GuiAppFrameworkAPI(session)
        self.health: HealthAPI = HealthAPI(session)
        self.health_data: HealthDataAPI = HealthDataAPI(session)
        self.help: HelpAPI = HelpAPI(session)
        self.qni: QniAPI = QniAPI(session)
        self.qrm: QrmAPI = QrmAPI(session)
        self.qvm: QvmAPI = QvmAPI(session)
        self.reference_data: ReferenceDataAPI = ReferenceDataAPI(session)
        self.reference_data_collections: ReferenceDataCollectionsAPI = ReferenceDataCollectionsAPI(session)
        self.scanner: ScannerAPI = ScannerAPI(session)
        self.services: ServicesAPI = ServicesAPI(session)
        self.siem: SiemAPI = SiemAPI(session)
        self.staged_config: StagedConfigAPI = StagedConfigAPI(session)
        self.system: SystemAPI = SystemAPI(session)

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()

    def __enter__(self) -> "QRadarClient":
        return self

    def __exit__(self, *_) -> None:
        self.close()
