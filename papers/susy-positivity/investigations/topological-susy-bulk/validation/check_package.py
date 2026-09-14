#!/usr/bin/env python3
"""Check snapshot integrity, preserved notes, active links, and source policy."""
from pathlib import Path
import argparse
import hashlib
import json
import re
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external-root', type=Path,
                        help='For a staged copy only: intended installation root for external relative links.')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    entries = manifest['files']
    for item in entries:
        path = ROOT / item['path']
        require(path.is_file(), f'Missing: {item["path"]}')
        require(path.stat().st_size == item['bytes'], f'Size changed: {item["path"]}')
        require(digest(path) == item['sha256'], f'Hash changed: {item["path"]}')
        require(item['bytes'] < 1048576, f'File exceeds repository size convention: {item["path"]}')
    known = {item['path'] for item in entries} | {'manifest.json'}
    present = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
               and p.name != '.DS_Store' and '__pycache__' not in p.parts
               and not p.is_relative_to(ROOT / 'validation/build')}
    require(present == known, f'Unexpected or unlisted package files: {sorted(present ^ known)}')
    relocation = json.loads((ROOT / 'REORGANIZATION_20260912.json').read_text())
    for item in relocation['moves']:
        preserved = ROOT / item['new_path']
        require(digest(preserved) == item['sha256'], f'Original bytes changed: {item["old_path"]}')
        require(preserved.stat().st_size == item['bytes'], f'Original size changed: {item["old_path"]}')
    notes = [item for item in relocation['moves'] if item['new_path'].startswith('archive/notes/')]
    require(len(notes) == 3, 'Expected three preserved working notes')
    tex = (ROOT / 'manuscript.tex').read_text()
    require('brainstorm' not in tex.lower(), 'Manuscript refers to exploratory folder')
    require(not re.search(r'\\(?:input|include|bibliography)\s*\{', tex), 'Manuscript has a source dependency')
    require(re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}', tex) == ['background'],
            'Background must be the sole bibliography entry')
    citations = re.findall(r'\\cite\w*(?:\[[^]]*\])*\{([^}]+)\}', tex)
    require(bool(citations) and all(c == 'background' for c in citations), 'Unexpected citation')
    targets = re.findall(r'\\href\{([^}]+)\}', tex)
    require(set(targets) == {'../../background.pdf', '../../background_section.tex'},
            'Unexpected manuscript hyperlink')
    active_markdown = ['README.md', 'STATUS.md', 'archive/README.md', 'numerics/README.md']
    links_checked = 0
    for filename in active_markdown:
        path = ROOT / filename
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            parsed = urlparse(target)
            if parsed.scheme or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(ROOT) and args.external_root:
                linked = (args.external_root.resolve() / Path(filename).parent / unquote(parsed.path)).resolve()
            require(linked.exists(), f'Broken active link in {filename}: {target}')
            links_checked += 1
    external_root = args.external_root.resolve() if args.external_root else ROOT
    for target in targets:
        require((external_root / target).resolve().is_file(), f'Missing background link: {target}')
    for item in entries:
        path = item['path']
        if Path(path).name.startswith('check_') and path.endswith('.py'):
            require(path.startswith('numerics/') or path == 'validation/check_package.py',
                    f'Numerical checker outside numerics: {path}')
        if 'diagnostics' in Path(path).name and path.endswith('.json'):
            require(path.startswith('numerics/'), f'Diagnostic record outside numerics: {path}')
    replay = json.loads((ROOT / 'numerics/records/manuscript-replay.json').read_text())
    require(replay['status'] == 'passed' and len(replay['jobs']) == 4, 'Delivered replay did not pass')
    for job in replay['jobs']:
        require(digest(ROOT / 'numerics' / job['script']) == job['script_sha256'],
                f'Replay source changed: {job["script"]}')
        require(digest(ROOT / 'numerics/records' / job['reference_record']) == job['reference_sha256'],
                f'Replay reference changed: {job["reference_record"]}')
    build = json.loads((ROOT / 'validation/BUILD_RECORD.json').read_text())
    require(digest(ROOT / 'manuscript.tex') == build['source_sha256'], 'Build source hash differs')
    require(digest(ROOT / 'manuscript.pdf') == build['pdf_sha256'], 'Build PDF hash differs')
    print(json.dumps(dict(status='passed', files_hashed=len(entries),
                          preserved_originals=len(relocation['moves']),
                          unchanged_notes=len(notes), active_links_checked=links_checked,
                          sole_manuscript_reference='main SUSY-positivity background',
                          limitation='Integrity and recorded replay checks; not a proof checker.'), indent=2))


if __name__ == '__main__':
    main()
