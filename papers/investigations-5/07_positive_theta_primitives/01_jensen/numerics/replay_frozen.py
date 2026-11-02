#!/usr/bin/env python3
"""Replay frozen Jensen checks after the 1 November 2026 folder renaming.

Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra / xhigh.
Only recorded navigation edits are reversed in a temporary historical tree.
Original program and evidence bytes, and every original integrity check, remain.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def digest(data):
    return sha256(data).hexdigest()


def safe_path(root, relative):
    p = Path(relative)
    if p.is_absolute() or '..' in p.parts:
        raise ValueError(f'Unsafe manifest path: {relative}')
    target = root / p
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes root: {relative}')
    return target


def restore(repo, destination, manifest):
    for entry in manifest['inputs']:
        source = safe_path(repo, entry['current_path'])
        data = source.read_bytes()
        if digest(data) != entry['current_sha256']:
            raise ValueError(f'Changed replay input: {source}')
        if entry.get('reverse_navigation_edits'):
            text = data.decode('utf-8')
            for edit in reversed(entry['reverse_navigation_edits']):
                text = text[:edit['start']] + edit['original'] + text[edit['end']:]
            data = text.encode('utf-8')
        if digest(data) != entry['original_sha256']:
            raise ValueError(f'Historical reconstruction failed: {source}')
        target = safe_path(destination, entry['original_path'])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def main():
    here = Path(__file__).resolve().parent
    repo = here.parents[4]
    manifest = json.loads((here / 'J_E07_REPLAY_PATHS_20261101.json').read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('program', nargs='?', choices=sorted(manifest['programs']))
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.verify_only and not args.program:
        parser.error('choose a program, or use --verify-only')
    if '--repo' in args.arguments:
        parser.error('--repo is supplied by this historical-path adapter')
    extra = args.arguments[:]
    for option in ('--record', '--replay'):
        if option in extra:
            index = extra.index(option) + 1
            if index == len(extra):
                parser.error(f'{option} needs a path')
            extra[index] = str(Path(extra[index]).resolve())
    with tempfile.TemporaryDirectory(prefix='jensen-frozen-replay-') as folder:
        historical = Path(folder)
        restore(repo, historical, manifest)
        if args.verify_only:
            print(json.dumps({'status': 'verified', 'inputs': len(manifest['inputs']),
                              'scope': 'original bytes reconstructed; no mathematics executed'}))
            return
        program = manifest['programs'][args.program]
        command = [sys.executable, '-B', str(safe_path(historical, program['path']))]
        if program['takes_repo']:
            command += ['--repo', str(historical)]
        command += extra
        result = subprocess.run(command, cwd=historical, check=False)
        raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
