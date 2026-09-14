#!/usr/bin/env python3
"""Explicitly refresh current deliverable hashes after review; does not validate proofs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED = ('build/', 'numerics/output/', 'numerics-archives/', 'validation/replay/')


def main():
    path = ROOT / 'manifest.json'
    manifest = json.loads(path.read_text())
    files = []
    for item in sorted(ROOT.rglob('*')):
        if not item.is_file():
            continue
        rel = item.relative_to(ROOT).as_posix()
        if rel == 'manifest.json' or item.name == '.DS_Store' or '__pycache__' in item.parts:
            continue
        if rel.startswith(IGNORED):
            continue
        size = item.stat().st_size
        if size >= 1048576:
            raise RuntimeError('Large deliverable requires archive policy review: ' + rel)
        files.append({'path': rel, 'bytes': size,
                      'sha256': hashlib.sha256(item.read_bytes()).hexdigest()})
    manifest['files'] = files
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'status': 'refreshed', 'files': len(files)}))


if __name__ == '__main__':
    main()
