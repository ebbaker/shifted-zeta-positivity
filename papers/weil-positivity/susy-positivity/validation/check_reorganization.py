#!/usr/bin/env python3
"""Verify the delivered 20 September relocation snapshot against its fingerprints.

Unlike check_structure.py, this dated audit intentionally pins the current
files as delivered at reorganization. Later research may legitimately change
current files; historical files must remain unchanged.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RECORDS = Path(__file__).resolve().parent / 'reorganization-20260920'


def fingerprint(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    moves = json.loads((RECORDS / 'MOVES.json').read_text())
    audit = json.loads((RECORDS / 'HISTORICAL_HASH_AUDIT.json').read_text())
    errors = []
    for old, new in moves['directory_map'].items():
        if (ROOT / old).exists() or not (ROOT / new).is_dir():
            errors.append(f'Unexpected relocation layout: {old} -> {new}')
    for entry in moves['files']:
        path = ROOT / entry['new_path']
        if not path.is_file() or fingerprint(path) != entry['after']:
            errors.append(f'Relocated file differs: {entry["new_path"]}')
        if entry['preserved'] and entry['before'] != entry['after']:
            errors.append(f'Invalid preservation assertion: {entry["new_path"]}')
    for name, expected in audit['files'].items():
        path = ROOT / name
        if not path.is_file() or fingerprint(path) != expected:
            errors.append(f'Historical file differs: {name}')
    for name, expected in audit['wilson_loewner_files'].items():
        path = ROOT / name
        if not path.is_file() or fingerprint(path) != expected:
            errors.append(f'Wilson–Loewner preservation differs: {name}')
    print(json.dumps({'status': 'failed' if errors else 'passed',
                      'moved_packages': len(moves['directory_map']),
                      'relocated_files': len(moves['files']),
                      'historical_files': len(audit['files']),
                      'wilson_loewner_files': len(audit['wilson_loewner_files']),
                      'errors': errors,
                      'scope': 'Dated relocation identity; not proof verification.'}, indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
