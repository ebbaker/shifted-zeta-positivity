#!/usr/bin/env python3
"""Check tracked sizes, current README navigation and current paper manifests.

Run from any directory. Standard library only; no external matrices are read.
Historical draft snapshots retain their original README text and manifests.
This checks package identity, not mathematical validity or PDF correspondence.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def historical(path):
    parts = path.parts
    return ('drafts' in parts and
            any(p.startswith('v') for p in parts[parts.index('drafts') + 1:-1]))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    paths = [Path(p) for p in subprocess.check_output(
        ['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0') if p]
    tracked = set(paths)
    errors = []
    readmes = 0
    snapshots = 0

    def require(ok, message):
        if not ok:
            errors.append(message)

    for rel in paths:
        path = ROOT / rel
        if not path.is_file():
            require(False, f'Missing tracked file: {rel}')
            continue
        require(path.stat().st_size <= 1048576, f'File exceeds 1 MiB: {rel}')
        require(not str(rel).endswith(('.json.gz', '.npy', '.npz', '.zip', '.pyc')),
                f'Derived archive/cache is tracked: {rel}')
        if rel.name.lower() != 'readme.md':
            continue
        if historical(rel):
            snapshots += 1
            continue
        readmes += 1
        text = path.read_text()
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
        storage_links = [(label, target) for label, target in links
                         if 'storage-depth' in (label + target).lower()]
        require(bool(storage_links), f'Current README omits storage-depth link: {rel}')
        for label, target in storage_links:
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            require((path.parent / unquote(parsed.path)).exists(),
                    f'Broken storage-depth link in {rel}: {target}')

    for slug in ('storage-depth', 'weil-depth'):
        base = ROOT / 'papers' / slug
        for line in (base / 'SHA256SUMS.txt').read_text().splitlines():
            want, name = line.split(None, 1)
            name = name.lstrip('*')
            rel = Path('papers') / slug / name
            require(rel in tracked, f'Manifest names untracked file: {rel}')
            path = base / name
            require(path.is_file() and digest(path) == want,
                    f'Checksum mismatch: {rel}')
        record = json.loads((base / 'BUILD_RECORD.json').read_text())
        if slug == 'storage-depth':
            for item in record['files']:
                path = base / item['path']
                require(path.is_file() and path.stat().st_size == item['bytes']
                        and digest(path) == item['sha256'],
                        f'Build record mismatch: {slug}/{item["path"]}')
        else:
            for group, prefix in [('source_sha256', 'numerics'),
                                  ('manuscript_sha256', 'manuscript'),
                                  ('documentation_sha256', '')]:
                for name, want in record[group].items():
                    path = base / prefix / name
                    require(path.is_file() and digest(path) == want,
                            f'Build record mismatch: {slug}/{prefix}/{name}')
            require(digest(base / record['pdf']) == record['pdf_sha256'],
                    'Weil-depth PDF hash mismatch')

    if errors:
        for message in errors:
            print('FAIL:', message, file=sys.stderr)
        return 1
    print(f'PASS: {len(paths)} tracked files within 1 MiB; '
          f'{readmes} current READMEs link storage-depth; '
          f'{snapshots} historical README snapshots preserved; '
          'both current paper manifests match.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
