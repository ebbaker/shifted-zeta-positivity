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
PAPER_GROUPS = {
    'shifted-zeta': ('psi-omega-margin', 'omega-string', 'defect-depth',
                     'first-slab-positivity', 'weil-depth', 'storage-depth'),
    'misc': ('rh-detector',),
}


def historical(path):
    parts = path.parts
    # Snapshot folders use both version numbers and dates. The drafts/
    # index itself remains current navigation and must still be checked.
    return 'drafts' in parts[:-2]


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
        for label, target in links:
            parsed = urlsplit(target.strip('<>'))
            if parsed.scheme or parsed.netloc:
                continue
            require((path.parent / unquote(parsed.path)).exists(),
                    f'Broken local link in {rel}: {target}')

    def require_index_links(index, destinations):
        require(index in tracked, f'Project index is not tracked: {index}')
        path = ROOT / index
        if not path.is_file():
            require(False, f'Missing project index: {index}')
            return
        targets = set()
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
            parsed = urlsplit(target.strip('<>'))
            if not parsed.scheme and not parsed.netloc:
                targets.add((path.parent / unquote(parsed.path)).resolve())
        for destination in destinations:
            require(destination in tracked, f'Paper/project README is not tracked: {destination}')
            require((ROOT / destination).resolve() in targets,
                    f'Index {index} omits {destination}')

    require_index_links(Path('papers/README.md'),
                        [Path('papers') / name / 'README.md'
                         for name in (*PAPER_GROUPS, 'susy-positivity')])
    for group, slugs in PAPER_GROUPS.items():
        base = Path('papers') / group
        require_index_links(base / 'README.md',
                            [base / slug / 'README.md' for slug in slugs])
        for slug in slugs:
            require(not (ROOT / 'papers' / slug).exists(),
                    f'Obsolete paper location remains: papers/{slug}')

    program = Path('papers/susy-positivity')
    attempt = program / 'investigations/positive-factorizations'
    require_index_links(program / 'README.md', [attempt / 'README.md'])
    for obsolete in ('manuscript.tex', 'manuscript.pdf', 'STATUS.md',
                     'RESEARCH_BRIEF.md', 'INVESTIGATION_round3.md',
                     'checks', 'manifest.json',
                     'archive/overview/rh-formulation-next-version/rh_background_section.tex',
                     'archive/overview/rh-formulation-next-version/rh_background_preview.tex'):
        require(not (ROOT / program / obsolete).exists(),
                f'Obsolete attempt location remains: {program / obsolete}')
    for wrapper, section in [('background.tex', 'background_section.tex')]:
        path = ROOT / program / wrapper
        require(path.is_file() and any('\\input{' + name + '}' in path.read_text()
                for name in (section, section.removesuffix('.tex'))),
                'Background wrapper must input the shared section')
    manifest = ROOT / attempt / 'manifest.json'
    require(manifest.is_file(), f'Missing attempt manifest: {attempt / "manifest.json"}')
    if manifest.is_file():
        current = json.loads(manifest.read_text())
        for name, want in current['sha256'].items():
            rel = attempt / name
            path = ROOT / rel
            require(rel in tracked, f'Attempt manifest names untracked file: {rel}')
            require(path.is_file() and digest(path) == want,
                    f'Attempt checksum mismatch: {rel}')

    for slug in ('storage-depth', 'weil-depth'):
        base = ROOT / 'papers' / 'shifted-zeta' / slug
        for line in (base / 'SHA256SUMS.txt').read_text().splitlines():
            want, name = line.split(None, 1)
            name = name.lstrip('*')
            rel = Path('papers') / 'shifted-zeta' / slug / name
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
          f'{readmes} current READMEs have valid local links; '
          f'{snapshots} historical README snapshots preserved; '
          'paper indexes cover all groups; current paper and attempt manifests match.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
