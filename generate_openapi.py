#!/usr/bin/env python3
"""
Generate an OpenAPI 3.0 specification from QRadar API HTML documentation files.

Usage:
    python3 generate_openapi.py [--output openapi.yaml]
"""

import argparse
import html
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# HTML Parsing helpers
# ---------------------------------------------------------------------------

class _TableParser(HTMLParser):
    """Extract tables (caption + rows) from an HTML document."""

    def __init__(self):
        super().__init__()
        self.tables = []
        self._current_table = None
        self._current_row = []
        self._cell_buf = ''
        self._in_cell = False
        self._in_caption = False
        self._caption_buf = ''
        self._skip_tag = None
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if self._skip_tag:
            self._skip_depth += 1
            return
        if tag in ('script', 'style'):
            self._skip_tag = tag
            self._skip_depth = 1
            return
        if tag == 'table':
            self._current_table = {'caption': '', 'rows': []}
        elif tag == 'caption':
            self._in_caption = True
            self._caption_buf = ''
        elif tag in ('td', 'th'):
            self._in_cell = True
            self._cell_buf = ''
        elif tag == 'tr':
            self._current_row = []

    def handle_endtag(self, tag):
        if self._skip_tag:
            self._skip_depth -= 1
            if self._skip_depth == 0:
                self._skip_tag = None
            return
        if tag == 'table' and self._current_table is not None:
            self.tables.append(self._current_table)
            self._current_table = None
        elif tag == 'caption':
            self._in_caption = False
            if self._current_table is not None:
                self._current_table['caption'] = self._caption_buf.strip()
        elif tag in ('td', 'th'):
            self._in_cell = False
            if self._current_table is not None:
                self._current_row.append(self._cell_buf.strip())
        elif tag == 'tr' and self._current_table is not None:
            if any(c.strip() for c in self._current_row):
                self._current_table['rows'].append(list(self._current_row))
            self._current_row = []

    def handle_data(self, data):
        if self._skip_tag:
            return
        if self._in_caption:
            self._caption_buf += data
        elif self._in_cell:
            self._cell_buf += data


class _TextExtractor(HTMLParser):
    """Extract plain text from an HTML document, preserving <pre> content."""

    def __init__(self):
        super().__init__()
        self._buf = []
        self._in_pre = False
        self._pre_buf = ''
        self.pre_blocks = []
        self._skip_tag = None
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if self._skip_tag:
            self._skip_depth += 1
            return
        if tag in ('script', 'style'):
            self._skip_tag = tag
            self._skip_depth = 1
        elif tag == 'pre':
            self._in_pre = True
            self._pre_buf = ''

    def handle_endtag(self, tag):
        if self._skip_tag:
            self._skip_depth -= 1
            if self._skip_depth == 0:
                self._skip_tag = None
            return
        if tag == 'pre':
            self._in_pre = False
            self.pre_blocks.append(self._pre_buf)
            self._buf.append('\n__PRE__\n')

    def handle_data(self, data):
        if self._skip_tag:
            return
        if self._in_pre:
            self._pre_buf += data
        else:
            self._buf.append(data)

    @property
    def text(self):
        return ''.join(self._buf)


def _parse_html_file(path: Path) -> dict:
    """
    Parse a single QRadar API HTML file and return a structured dict with:
      method, api_path, summary, description, parameters, request_body,
      responses, response_schema_sample
    """
    content = path.read_text(encoding='utf-8')

    # ---- title ---------------------------------------------------------
    title_m = re.search(
        r'<h1[^>]*>\s*(GET|POST|PUT|DELETE|PATCH)\s+(/[^\s<]+)',
        content, re.IGNORECASE
    )
    if not title_m:
        return {}
    method = title_m.group(1).upper()
    api_path = title_m.group(2).strip()

    # ---- short description ---------------------------------------------
    desc_m = re.search(
        r'<p class="shortdesc">(.*?)</p>', content, re.DOTALL
    )
    description = ''
    if desc_m:
        raw = desc_m.group(1)
        description = html.unescape(re.sub(r'<[^>]+>', '', raw)).strip()

    # ---- tables --------------------------------------------------------
    tp = _TableParser()
    tp.feed(content)

    params_rows = []
    body_rows = []
    response_rows = []

    for table in tp.tables:
        cap = table['caption'].lower()
        rows = table['rows']
        if 'request parameter details' in cap:
            # skip header row
            params_rows = rows[1:] if rows else []
        elif 'request body details' in cap:
            body_rows = rows[1:] if rows else []
        elif 'response codes' in cap:
            response_rows = rows[1:] if rows else []

    # ---- request parameters --------------------------------------------
    parameters = []
    for row in params_rows:
        if len(row) < 6:
            continue
        name, location, optionality, data_type, _mime, desc_text = (
            row[0], row[1], row[2], row[3], row[4], row[5]
        )
        name = name.strip()
        location = location.strip().lower()
        if location not in ('query', 'path', 'header'):
            continue
        required = optionality.strip().lower() == 'required'
        param = {
            'name': name,
            'in': location,
            'description': desc_text.strip(),
            'required': required or location == 'path',
            'schema': {'type': _map_type(data_type.strip())},
        }
        parameters.append(param)

    # ---- request body --------------------------------------------------
    request_body = None
    if body_rows:
        # Collect all body parameters into a single schema
        properties = {}
        required_fields = []
        for row in body_rows:
            if len(row) < 4:
                continue
            b_name, b_type, b_mime, b_desc = row[0], row[1], row[2], row[3]
            b_name = b_name.strip()
            if not b_name:
                continue
            prop = {'type': _map_type(b_type.strip()), 'description': b_desc.strip()}
            properties[b_name] = prop
            if 'required' in b_desc.lower() and b_desc.strip().lower().startswith('required'):
                required_fields.append(b_name)

        schema = {'type': 'object', 'properties': properties}
        if required_fields:
            schema['required'] = required_fields

        # Determine content type
        content_types = [row[2].strip() for row in body_rows if len(row) > 2]
        mime = content_types[0] if content_types else 'application/json'

        request_body = {
            'required': True,
            'content': {mime: {'schema': schema}},
        }

    # ---- response codes ------------------------------------------------
    responses = {}
    for row in response_rows:
        if not row:
            continue
        code = row[0].strip()
        desc_text = row[2].strip() if len(row) > 2 else (row[1].strip() if len(row) > 1 else '')
        if not code.isdigit():
            continue
        responses[code] = {'description': desc_text or 'No description'}

    if not responses:
        responses['200'] = {'description': 'Success'}

    # ---- response sample (JSON in <pre> block) -------------------------
    te = _TextExtractor()
    te.feed(content)
    response_sample = None
    for pre in te.pre_blocks:
        # Strip inner <code> tags
        clean = re.sub(r'<[^>]+>', '', pre).strip()
        clean = html.unescape(clean)
        # Remove trailing type hints like  "String <one of: X, Y>"
        clean = re.sub(r'"String <one of:[^"]*>"', '"String"', clean)
        try:
            response_sample = json.loads(clean)
            break
        except (json.JSONDecodeError, ValueError):
            pass

    # Add response schema to 200/201 responses
    ok_code = '201' if method == 'POST' and '201' in responses else '200'
    if ok_code in responses:
        if response_sample is not None:
            schema = _json_to_schema(response_sample)
            responses[ok_code]['content'] = {
                'application/json': {'schema': schema}
            }
        else:
            responses[ok_code]['content'] = {
                'application/json': {'schema': {'type': 'object'}}
            }

    return {
        'method': method,
        'api_path': api_path,
        'summary': description,
        'description': description,
        'parameters': parameters,
        'request_body': request_body,
        'responses': responses,
    }


# ---------------------------------------------------------------------------
# Type mapping helpers
# ---------------------------------------------------------------------------

_TYPE_MAP = {
    'string': 'string',
    'number': 'number',
    'number (integer)': 'integer',
    'integer': 'integer',
    'int': 'integer',
    'long': 'integer',
    'boolean': 'boolean',
    'bool': 'boolean',
    'array': 'array',
    'array<object>': 'array',
    'object': 'object',
}


def _map_type(raw: str) -> str:
    return _TYPE_MAP.get(raw.lower(), 'string')


def _json_to_schema(value) -> dict:
    """Derive a minimal OpenAPI schema from a JSON sample value."""
    if isinstance(value, bool):
        return {'type': 'boolean'}
    if isinstance(value, int):
        return {'type': 'integer'}
    if isinstance(value, float):
        return {'type': 'number'}
    if isinstance(value, str):
        return {'type': 'string'}
    if isinstance(value, list):
        if value:
            return {'type': 'array', 'items': _json_to_schema(value[0])}
        return {'type': 'array', 'items': {}}
    if isinstance(value, dict):
        props = {k: _json_to_schema(v) for k, v in value.items()}
        return {'type': 'object', 'properties': props}
    return {}


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build_openapi(repo_dir: Path) -> dict:
    """Parse all 26.0--*.html files and return an OpenAPI 3.0 dict."""
    spec = {
        'openapi': '3.0.0',
        'info': {
            'title': 'IBM QRadar REST API',
            'description': (
                'IBM QRadar REST API version 26.0. '
                'Generated from HTML documentation files.'
            ),
            'version': '26.0',
            'contact': {
                'name': 'IBM QRadar',
                'url': 'https://www.ibm.com/docs/en/qradar-common',
            },
        },
        'servers': [
            {'url': 'https://{host}/api', 'variables': {
                'host': {'default': 'localhost', 'description': 'QRadar console hostname'}
            }},
        ],
        'paths': {},
    }

    html_files = sorted(repo_dir.glob('26.0--*.html'))
    print(f'Found {len(html_files)} HTML endpoint files', file=sys.stderr)

    for html_path in html_files:
        data = _parse_html_file(html_path)
        if not data:
            print(f'  SKIP (no title found): {html_path.name}', file=sys.stderr)
            continue

        method = data['method'].lower()
        api_path = data['api_path']

        if api_path not in spec['paths']:
            spec['paths'][api_path] = {}

        operation = {
            'summary': data['summary'],
            'description': data['description'],
            'operationId': _make_operation_id(method, api_path),
            'tags': [_extract_tag(api_path)],
            'responses': {
                code: _serialize_response(resp)
                for code, resp in data['responses'].items()
            },
        }

        if data['parameters']:
            operation['parameters'] = data['parameters']

        if data['request_body']:
            operation['requestBody'] = data['request_body']

        spec['paths'][api_path][method] = operation

    return spec


def _serialize_response(resp: dict) -> dict:
    """Return a clean OpenAPI response object."""
    out = {'description': resp.get('description', 'No description')}
    if 'content' in resp:
        out['content'] = resp['content']
    return out


def _make_operation_id(method: str, api_path: str) -> str:
    """Create a camelCase operationId from method + path."""
    parts = [method] + [
        p.strip('{}') for p in api_path.strip('/').split('/')
    ]
    def _cap(s):
        return s[0].upper() + s[1:] if s else ''
    return parts[0] + ''.join(_cap(p) for p in parts[1:])


def _extract_tag(api_path: str) -> str:
    """Use the first path segment as the OpenAPI tag."""
    parts = api_path.strip('/').split('/')
    return parts[0] if parts else 'default'


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Generate OpenAPI 3.0 YAML from QRadar HTML docs'
    )
    parser.add_argument(
        '--output', '-o',
        default='openapi.yaml',
        help='Output file path (default: openapi.yaml)',
    )
    parser.add_argument(
        '--dir', '-d',
        default=str(Path(__file__).parent),
        help='Directory containing the HTML files (default: script directory)',
    )
    args = parser.parse_args()

    repo_dir = Path(args.dir).resolve()
    if not repo_dir.is_dir():
        print(f'Error: directory not found: {repo_dir}', file=sys.stderr)
        sys.exit(1)

    spec = build_openapi(repo_dir)

    output_path = Path(args.output)
    with output_path.open('w', encoding='utf-8') as fh:
        yaml.dump(
            spec,
            fh,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )

    path_count = len(spec['paths'])
    op_count = sum(len(v) for v in spec['paths'].values())
    print(
        f'OpenAPI spec written to {output_path} '
        f'({path_count} paths, {op_count} operations)',
        file=sys.stderr,
    )


if __name__ == '__main__':
    main()
