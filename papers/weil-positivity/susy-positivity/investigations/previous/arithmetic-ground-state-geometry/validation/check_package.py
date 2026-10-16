#!/usr/bin/env python3
"""Validate this research package and optionally replay its small exact checks.

Integrity, source policy and algebra replay are not analytical proof checking.
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external-root', type=Path,
                        help='Intended installation directory for external relative links in a staged copy.')
    parser.add_argument('--replay', action='store_true', help='Replay all ten exact algebra programs.')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    known = {'manifest.json'}
    for entry in manifest['files']:
        rel = entry['path']
        path = (ROOT / rel).resolve()
        require(contained(path, ROOT), 'Path leaves package: ' + rel)
        require(path.is_file(), 'Missing file: ' + rel)
        require(path.stat().st_size == entry['bytes'], 'Size changed: ' + rel)
        require(digest(path) == entry['sha256'], 'Hash changed: ' + rel)
        require(entry['bytes'] < 1048576, 'Large file belongs in szp-archive: ' + rel)
        known.add(rel)
    present = set()
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if path.name == '.DS_Store' or '__pycache__' in path.parts:
            continue
        if rel.startswith(('build/', 'numerics/output/', 'numerics-archives/', 'validation/replay/')):
            continue
        present.add(rel)
    require(present == known, 'Unlisted or missing files: ' + repr(sorted(present ^ known)))

    build_records = 0
    snapshots = 0
    for rel in sorted(known):
        if not rel.endswith(('BUILD_RECORD.json', 'SNAPSHOT.json')):
            continue
        record_path = ROOT / rel
        record = json.loads(record_path.read_text())
        base = record_path.parent
        if record_path.name == 'BUILD_RECORD.json':
            entries = [record['pdf']] + record['sources']
            build_records += 1
        else:
            entries = record['files']
            snapshots += 1
        for entry in entries:
            artifact = (base / entry['path']).resolve()
            require(contained(artifact, base), 'Record path leaves snapshot: ' + rel)
            require(artifact.is_file(), 'Missing recorded artifact: ' + str(artifact))
            require(digest(artifact) == entry['sha256'],
                    'Build/snapshot hash changed: ' + str(artifact))
            if 'bytes' in entry:
                require(artifact.stat().st_size == entry['bytes'],
                        'Build/snapshot size changed: ' + str(artifact))

    links = 0
    for path in sorted(ROOT.rglob('*.md')):
        if path.relative_to(ROOT).as_posix() not in known:
            continue
        text = path.read_text()
        require(not any(ord(c) < 32 and c not in '\n\t' for c in text), 'Control character in ' + str(path))
        starts = re.findall(r'^\s*\\\[\s*$', text, re.M)
        ends = re.findall(r'^\s*\\\]\s*$', text, re.M)
        require(len(starts) == len(ends), 'Unbalanced display math in ' + path.name)
        require(text.count(r'\(') == text.count(r'\)'), 'Unbalanced inline math in ' + path.name)
        link_text = re.sub(r'^```.*?^```[^\n]*$', '', text, flags=re.M | re.S)
        link_text = re.sub(r'\\\[.*?\\\]', '', link_text, flags=re.S)
        link_text = re.sub(r'\\\(.*?\\\)', '', link_text, flags=re.S)
        for target in re.findall(r'\]\(([^\s)]+)\)', link_text):
            parsed = urlparse(target)
            if parsed.scheme or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not contained(linked, ROOT) and args.external_root:
                linked = (args.external_root.resolve() / path.relative_to(ROOT).parent / unquote(parsed.path)).resolve()
            require(linked.exists(), f'Broken link in {path.name}: {target}')
            links += 1

    replay_status = {}
    if args.replay:
        for name, program in [('supercharge-algebra', 'check_supercharge_algebra.py'),
                              ('quartic-period-identity', 'check_quartic_period_identity.py'),
                              ('shape-period', 'check_shape_period.py'),
                              ('shape-jacobi', 'check_shape_jacobi.py'),
                              ('boundary-pairing', 'check_boundary_pairing.py'),
                              ('coherent-delay', 'check_coherent_delay.py'),
                              ('prime-returns', 'check_prime_returns.py'),
                              ('collective-feedback', 'check_collective_feedback.py'),
                              ('joint-response', 'check_joint_response.py'),
                              ('arithmetic-sign', 'check_arithmetic_sign.py')]:
            script = ROOT / 'numerics' / program
            completed = subprocess.run([sys.executable, str(script)], check=True, text=True, capture_output=True)
            fresh = json.loads(completed.stdout)
            saved = json.loads((ROOT / 'numerics/records' / (name + '.json')).read_text())
            require(fresh == saved, 'Exact algebra record differs on replay: ' + name)
            require(fresh['status'] == 'passed', 'Exact algebra did not pass: ' + name)
            replay_status[name] = {'status': 'exact record reproduced', 'checks': len(fresh['checks'])}
    print(json.dumps({'status': 'passed', 'files_hashed': len(manifest['files']),
                      'local_links_checked': links, 'algebra_replays': replay_status,
                      'build_records_checked': build_records,
                      'draft_snapshots_checked': snapshots,
                      'large_external_data_required': False,
                      'limitation': 'Package integrity and labelled algebra only; not proof or RH verification.'}, indent=2))


if __name__ == '__main__':
    main()
