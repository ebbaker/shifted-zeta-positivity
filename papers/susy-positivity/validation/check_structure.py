#!/usr/bin/env python3
"""Check current program navigation and file identity without rewriting history.

Run the investigation check_package.py entry points for their complete package
checks. This check does not compile TeX, access the network, or verify proofs.
Historical Markdown is excluded only from link resolution, not JSON parsing
or the current manifests that cover it.
"""
import ast
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_NOTE = ('brainstorm/continuation-notes/'
                   'CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md')


def historical(path):
    rel = path.relative_to(ROOT)
    return (('archive' in rel.parts or 'drafts' in rel.parts
             or 'reviews' in rel.parts) and path.name != 'README.md'
            or 'drafts' in rel.parts
            or 'provenance' in rel.parts
            or rel.as_posix() == HISTORICAL_NOTE)


def ignored(path):
    return any(part in {'build', '__pycache__', 'output', 'replay-results'}
               for part in path.relative_to(ROOT).parts)


def main():
    errors = []
    counts = dict(local_links=0, tex_dependencies=0, json_files=0,
                  python_sources=0, recorded_files=0, historical_markdown=0)

    def require(ok, message):
        if not ok:
            errors.append(message)

    def check_link(path, target, kind):
        parsed = urlparse(target)
        if parsed.scheme or not parsed.path:
            return
        local = unquote(parsed.path)
        # Editor-style line suffixes are not part of a filesystem name.
        local = re.sub(r':\d+(?::\d+)?$', '', local)
        require(not Path(local).is_absolute(),
                f'Machine-specific current link in {path.relative_to(ROOT)}: {target}')
        require((path.parent / local).exists(),
                f'Broken {kind} in {path.relative_to(ROOT)}: {target}')
        counts[kind] += 1

    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or ignored(path):
            continue
        if path.suffix == '.json':
            try:
                json.loads(path.read_text())
                counts['json_files'] += 1
            except (ValueError, UnicodeError) as exc:
                errors.append(f'Invalid JSON: {path}: {exc}')
        elif path.suffix == '.py':
            try:
                ast.parse(path.read_text(), filename=str(path))
                counts['python_sources'] += 1
            except SyntaxError as exc:
                errors.append(str(exc))
        elif path.suffix == '.md':
            if historical(path):
                counts['historical_markdown'] += 1
                continue
            text = re.sub(r'```.*?```|\\\[.*?\\\]|\\\(.*?\\\)',
                          '', path.read_text(), flags=re.S)
            for target in re.findall(r'\]\(([^\s)]+)\)', text):
                check_link(path, target, 'local_links')
        elif path.suffix == '.tex' and not historical(path):
            text = re.sub(r'(?m)(?<!\\)%.*$', '', path.read_text())
            for target in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
                if not Path(target).suffix:
                    target += '.tex'
                check_link(path, target, 'tex_dependencies')
            for target in re.findall(r'\\href\{([^}]+)\}', text):
                check_link(path, target, 'tex_dependencies')

    def check_record(base, entries):
        for rel, expected in entries.items():
            path = base / rel
            require(path.is_file(), f'Missing recorded file: {path}')
            if not path.is_file():
                continue
            if isinstance(expected, str):
                expected = {'sha256': expected}
            require(hashlib.sha256(path.read_bytes()).hexdigest() == expected['sha256'],
                    f'Recorded hash differs: {path}')
            if 'bytes' in expected:
                require(path.stat().st_size == expected['bytes'],
                        f'Recorded size differs: {path}')
            counts['recorded_files'] += 1

    positive = ROOT / 'investigations/positive-factorizations'
    manifest = json.loads((positive / 'manifest.json').read_text())
    check_record(positive, manifest['sha256'])
    for key in ('record', 'summary'):
        require((positive / manifest['fresh_verification'][key]).is_file(),
                f'Positive-factorizations verification {key} is missing')
    candidate = ROOT / 'brainstorm/candidate-bulk-theories'
    record = json.loads((candidate / 'results/package-record.json').read_text())
    check_record(candidate, record['current_files'])
    paper = ROOT / 'manuscripts/finite-response-weil-positivity'
    record = json.loads((paper / 'VALIDATION.json').read_text())
    check_record(paper, {entry['path']: entry for entry in record['files']})
    check_record(paper, record['checks']['source_sha256'])
    for snapshot in paper.glob('drafts/*/SNAPSHOT.json'):
        record = json.loads(snapshot.read_text())
        check_record(snapshot.parent, {entry['path']: entry for entry in record['files']})
    # The first draft predates SNAPSHOT.json; its own validation pins its files.
    first = paper / 'drafts/2026-09-13-before-review-revisions'
    record = json.loads((first / 'VALIDATION.json').read_text())
    check_record(first, {entry['path']: entry for entry in record['files']})
    print(json.dumps({'status': 'failed' if errors else 'passed', **counts,
                      'errors': errors,
                      'scope': 'Current paths, source syntax and recorded file identity; '
                               'historical links retain their dated layouts. '
                               'No new TeX build or mathematical proof review.'}, indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
