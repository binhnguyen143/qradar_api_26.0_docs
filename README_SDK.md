# QRadar Python SDK

A Python SDK client for the **IBM QRadar REST API version 26.0**, generated
from the [`openapi.yaml`](openapi.yaml) specification.

## Installation

```bash
pip install requests
# then place the qradar_sdk/ package on your Python path, or install it:
pip install -e .
```

## Quick start

### SEC token authentication (recommended)

```python
from qradar_sdk import QRadarClient

client = QRadarClient(
    host="qradar.example.com",
    sec_token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    verify_ssl=False,   # disable TLS verification for self-signed certs
)

# List the 50 most-recent open offenses
offenses = client.siem.get_siem_offenses(
    filter="status=OPEN",
    sort="-start_time",
    range_header="0-49",
)
for offense in offenses:
    print(offense["id"], offense["description"])
```

### Basic auth

```python
client = QRadarClient(
    host="qradar.example.com",
    username="admin",
    password="s3cr3t",
)
```

## Usage patterns

### Using as a context manager

```python
with QRadarClient(host="...", sec_token="...") as client:
    rules = client.analytics.get_analytics_rules()
```

### Pagination helper

```python
with QRadarClient(host="...", sec_token="...") as client:
    for page in client._session.paginate("/siem/offenses", page_size=100):
        for offense in page:
            process(offense)
```

### Running an Ariel (AQL) search

```python
# Submit the search
search = client.ariel.post_ariel_searches(
    body={"query_expression": "SELECT * FROM events LAST 5 MINUTES"}
)
search_id = search["search_id"]

# Poll until complete
import time
while True:
    status = client.ariel.get_ariel_searches_search_id(search_id=search_id)
    if status["status"] == "COMPLETED":
        break
    time.sleep(2)

# Fetch results
results = client.ariel.get_ariel_searches_search_id_results(search_id=search_id)
```

## API reference

The `QRadarClient` exposes one attribute per API tag:

| Attribute | Tag | Description |
|---|---|---|
| `client.access` | access | Login attempts and access management |
| `client.analytics` | analytics | Rules, building blocks, ADE rules |
| `client.ariel` | ariel | AQL searches, saved searches |
| `client.asset_model` | asset_model | Asset management |
| `client.auth` | auth | Authentication (logout) |
| `client.backup_and_restore` | backup_and_restore | Backup management |
| `client.bandwidth_manager` | bandwidth_manager | Bandwidth configurations |
| `client.config` | config | System configuration |
| `client.data_classification` | data_classification | QID records, categories |
| `client.disaster_recovery` | disaster_recovery | Ariel copy profiles |
| `client.dynamic_search` | dynamic_search | Dynamic search schemas |
| `client.forensics` | forensics | Packet capture and case management |
| `client.gui_app_framework` | gui_app_framework | App framework management |
| `client.health` | health | Health metrics |
| `client.health_data` | health_data | Security data counts |
| `client.help` | help | API endpoint documentation |
| `client.qni` | qni | QNI host configuration |
| `client.qrm` | qrm | Risk management |
| `client.qvm` | qvm | Vulnerability management |
| `client.reference_data` | reference_data | Reference sets, maps, tables |
| `client.reference_data_collections` | reference_data_collections | Reference data collections |
| `client.scanner` | scanner | Vulnerability scanner profiles |
| `client.services` | services | DNS, WHOIS, port scan services |
| `client.siem` | siem | Offenses, notes, closing reasons |
| `client.staged_config` | staged_config | Staged (pre-deploy) configuration |
| `client.system` | system | System information, servers |

## Error handling

```python
from qradar_sdk import QRadarClient, QRadarAPIError, QRadarNotFoundError

try:
    offense = client.siem.get_siem_offenses_offense_id(offense_id=9999)
except QRadarNotFoundError:
    print("Offense not found")
except QRadarAPIError as exc:
    print(f"API error {exc.status_code}: {exc.message}")
```

## Regenerating the SDK

If you update `openapi.yaml`, run:

```bash
python3 generate_sdk.py
```

to regenerate the `qradar_sdk/` package.
