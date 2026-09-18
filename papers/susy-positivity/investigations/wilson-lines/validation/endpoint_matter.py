#!/usr/bin/env python3
"""Separate registry/provenance for research notes beyond manuscript 0.8.

Does not alter BUILD_RECORD.json, archived snapshots, or legacy check records.
Model: OpenAI GPT-6 (Codex). Standard library only.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {'check_endpoint_matter.py': 'endpoint-matter-checks.json'}
RECORD = ROOT / 'ENDPOINT_MATTER_RECORD.json'
FILES = ['notes/ENDPOINT_MATTER_CONTINUATION_20260918.md',
         'notes/ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md',
         'validation/endpoint_matter.py',
         'numerics/records/endpoint-baseline-replay-audit.json']
for script, record in CHECKS.items():
    FILES += ['numerics/'+script, 'numerics/records/'+record]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['record', 'check'])
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    if args.command == 'record':
        payload = {'schema': 1, 'date': '2026-09-18',
                   'title': 'Endpoint-matter continuation', 'model': 'OpenAI GPT-6 (Codex)',
                   'manuscript_baseline': 'drafts/2026-09-18-v08-endpoint-baseline',
                   'sha256': {name: digest(ROOT/name) for name in FILES},
                   'scope': 'Research-note identity; no manuscript/PDF update or proof certification.'}
        RECORD.write_text(json.dumps(payload, indent=2)+'\n')
    record = json.loads(RECORD.read_text())
    assert set(record['sha256']) == set(FILES), 'Continuation file list drifted'
    for name, want in record['sha256'].items():
        assert digest(ROOT/name) == want, 'Changed continuation file: '+name
        assert (ROOT/name).stat().st_size < 1048576, 'File exceeds 1 MiB: '+name
    cases = 0
    if args.replay:
        for script, result in CHECKS.items():
            expected = json.loads((ROOT/'numerics/records'/result).read_text())
            actual = json.loads(subprocess.check_output(
                [sys.executable, str(ROOT/'numerics'/script)], text=True, cwd=ROOT))
            assert actual == expected, 'Continuation replay differs: '+script
            assert actual['pass'], 'Continuation check failed'
            cases += actual['total_checks']
    print(json.dumps({'status': 'passed', 'files': len(FILES),
                      'replayed_cases': cases, 'scope': record['scope']}, indent=2))


if __name__ == '__main__':
    main()
