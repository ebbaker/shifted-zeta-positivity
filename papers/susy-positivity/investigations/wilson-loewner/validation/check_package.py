#!/usr/bin/env python3
"""Inventory and replay the Wilson--Loewner manuscript and research package.

Hashes establish file identity. Numerical replay checks the same cases and
thresholds, allowing runtime differences in floating diagnostic values.
Neither operation checks mathematical proofs or physical existence claims.
"""
import argparse
import hashlib
import json
import math
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'PACKAGE_RECORD.json'
CHECKS = (
    ('numerics/check_smooth_variation.py', 'numerics/records/smooth-variation-checks.json'),
    ('numerics/check_defect_endpoints.py', 'numerics/records/defect-endpoint-checks.json'),
    ('numerics/check_reflected_junction.py', 'numerics/records/reflected-junction-checks.json'),
)
INHERITED = (
    '../wilson-lines/notes/ENDPOINT_TRANSPORT_AND_SHIFT_20260918.md',
    '../wilson-lines/notes/ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md',
    '../wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md',
    '../wilson-lines/reviews/review_codex_2026-09-18.md',
    '../loewner/sections/03_decomposition.tex',
    '../loewner/sections/04_realizations.tex',
    '../loewner/manuscript.tex',
    '../fractional-dimension/manuscript.tex',
    '../fractional-dimension/sections/06_pointcount.tex',
    '../wilson-lines/manuscript.tex',
    '../../background_section.tex',
    '../wilson-lines/sections/07_region.tex',
    '../../../shifted-zeta/storage-depth/archive/background/1-critical_path_research.md',
    '../../../shifted-zeta/storage-depth/archive/background/2-cumulative_storage_path.md',
    '../../../shifted-zeta/storage-depth/manuscript/storage_depth.tex',
)


def digest(path):
    data = path.read_bytes()
    return dict(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))


def inventory():
    return {p.relative_to(ROOT).as_posix(): digest(p)
            for p in sorted(ROOT.rglob('*')) if p.is_file()
            and p != RECORD and p.name != '.DS_Store'
            and not any(x in {'__pycache__', 'build', '.git'}
                        for x in p.relative_to(ROOT).parts)}


def validate_result(data):
    cases = data['cases']
    if data['case_count'] != len(cases) or not data['all_pass']:
        raise ValueError('Case count or all_pass is invalid')
    if len({c['name'] for c in cases}) != len(cases):
        raise ValueError('Duplicate numerical case names')
    for case in cases:
        value, threshold = case['value'], case['threshold']
        if not math.isfinite(value) or not math.isfinite(threshold):
            raise ValueError(f"Nonfinite diagnostic: {case['name']}")
        comparison = case['comparison']
        if comparison not in ('<=', '>='):
            raise ValueError(f'Unknown comparison: {comparison}')
        passed = value <= threshold if comparison == '<=' else value >= threshold
        if not passed or not case['passed']:
            raise ValueError(f"Failed diagnostic: {case['name']}")


def run_program(program):
    result = subprocess.run([sys.executable, str(ROOT / program)], cwd=ROOT,
                            capture_output=True, text=True, check=True, timeout=180)
    data = json.loads(result.stdout)
    validate_result(data)
    return result.stdout, data


def identity(data):
    return dict(parameters=data['parameters'], case_count=data['case_count'],
                cases=[(c['name'], c['threshold'], c['comparison']) for c in data['cases']])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('refresh', 'check'))
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    if args.command == 'refresh':
        completed = [(program, destination, *run_program(program))
                     for program, destination in CHECKS]
        for _, destination, output, _ in completed:
            (ROOT / destination).parent.mkdir(exist_ok=True)
            (ROOT / destination).write_text(output)
        record = dict(schema_version=1,
                      generated_utc=datetime.now(timezone.utc).isoformat(),
                      author='OpenAI GPT-6 (Codex), for Edward Baker',
                      status='Working exposition and supplementary information 0.3; '
                             'prescribed shift-evolution research program; no independent review',
                      python=platform.python_version(),
                      scope='File identity and finite classical, chiral-defect, endpoint, '
                            'reflection and Gaussian-response diagnostics; not a proof checker '
                            'or quantum positivity certification',
                      replay_policy='Same parameters, case identities and thresholds; '
                                    'all cases pass. Floating values may differ.',
                      checks=[dict(program=p, record=r, cases=d['case_count'])
                              for p, r, _, d in completed],
                      current_files=inventory(),
                      inherited_sources={p: digest(ROOT / p) for p in INHERITED})
        RECORD.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
        print(json.dumps(dict(status='refreshed', files=len(record['current_files']),
                              cases=sum(d['case_count'] for _, _, _, d in completed))))
        return

    record = json.loads(RECORD.read_text())
    actual = inventory()
    expected = record['current_files']
    errors = []
    for path in sorted(actual.keys() | expected.keys()):
        if actual.get(path) != expected.get(path):
            errors.append(f'Inventory mismatch: {path}')
    for path, expected_digest in record['inherited_sources'].items():
        if not (ROOT / path).is_file() or digest(ROOT / path) != expected_digest:
            errors.append(f'Inherited source changed or missing: {path}')
    if [(c['program'], c['record']) for c in record['checks']] != list(CHECKS):
        errors.append('Registered programs or outputs changed')
    case_count = 0
    for program, destination in CHECKS:
        saved = json.loads((ROOT / destination).read_text())
        validate_result(saved)
        case_count += saved['case_count']
        registered = next((c for c in record['checks'] if c['program'] == program), {})
        if registered.get('cases') != saved['case_count']:
            errors.append(f'Registered case count mismatch: {program}')
        if args.replay:
            _, fresh = run_program(program)
            if identity(fresh) != identity(saved):
                errors.append(f'Replay parameters, cases or thresholds changed: {program}')
    print(json.dumps(dict(status='failed' if errors else 'passed',
                          files=len(actual), inherited_sources=len(INHERITED),
                          cases=case_count, replayed=args.replay, errors=errors,
                          scope=record['scope']), indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    main()
