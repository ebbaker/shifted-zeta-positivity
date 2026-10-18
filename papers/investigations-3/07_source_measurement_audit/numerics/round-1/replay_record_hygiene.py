#!/usr/bin/env python3
"""Canonical mathematical-content identity for the fixed source replay.

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol, reasoning effort ultra. This identity covers
serialized enclosures, witnesses, scope and diagnostics, not their validity
or arithmetic portability. Stored-byte hashes remain separate provenance.
"""
import hashlib
import json


# These exact field names contain execution or stored-file provenance in
# the replay schemas. Apply recursively so per-case timings are omitted too.
# Do not discard arbitrary *_sha256 fields: mathematical content references
# (record_content_sha256) must remain bound by the summary's content hash.
EXCLUDED_KEYS = frozenset({
    'elapsed_seconds', 'wall_seconds', 'runtime_seconds',
    'largest_child_peak_rss_bytes', 'peak_resident_bytes',
    'python', 'python_version', 'python_flint_version', 'mpmath',
    'platform_system', 'input',
    'script_sha256', 'checker_sha256', 'generator_sha256',
    'source_code_sha256', 'evaluation_sha256', 'floating_witnesses_sha256',
    'input_sha256', 'evaluation_file_sha256', 'record_sha256',
    'code_sha256', 'original_record_sha256', 'mathematical_content_sha256',
})

CONTENT_HASH_POLICY = {
    'schema': 'source_measurement_math_content_v1',
    'algorithm': 'SHA-256',
    'serialization': 'UTF-8 JSON; sorted object keys; compact separators; '
                     'ensure_ascii=True; allow_nan=False; list order retained',
    'recursive_excluded_keys': sorted(EXCLUDED_KEYS),
    'meaning': 'Identity of serialized mathematical data and retained scope '
               'metadata in the tested environments; not proof validity '
               'or arithmetic portability.',
}


def mathematical_content(value):
    """Return the documented canonical projection of a parsed JSON value."""
    if isinstance(value, dict):
        return {key: mathematical_content(item) for key, item in value.items()
                if key not in EXCLUDED_KEYS}
    if isinstance(value, list):
        return [mathematical_content(item) for item in value]
    return value


def mathematical_content_digest(value):
    serialized = json.dumps(mathematical_content(value), sort_keys=True,
                            separators=(',', ':'), ensure_ascii=True,
                            allow_nan=False).encode('utf-8')
    return hashlib.sha256(serialized).hexdigest()


def peak_rss_bytes(value, system):
    """Convert resource.ru_maxrss on the two supported replay platforms."""
    if system == 'Linux':
        return int(value) * 1024  # Linux reports KiB.
    if system == 'Darwin':
        return int(value)  # macOS reports bytes.
    raise ValueError('Unknown ru_maxrss units on platform ' + repr(system))
