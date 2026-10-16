#!/usr/bin/env python3
"""Replay this attempt's four diagnostics without replacing historical records."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ABS_TOL = 5e-9
REL_TOL = 5e-8
METADATA = {'python', 'numpy', 'source_sha256'}
JOBS = [
    ('check_relative_and_delay_models.py', 'supplied-model-diagnostics.json'),
    ('check_finite_coupling.py', 'finite-coupling-diagnostics.json'),
    ('check_loop_evolution.py', 'loop-evolution-diagnostics.json'),
    ('check_field_mixing.py', 'field-mixing-diagnostics.json'),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(actual, expected, where='$', stats=None):
    if stats is None:
        stats = {'numeric_values_compared': 0, 'maximum_absolute_difference': 0.0,
                 'maximum_tolerance_fraction': 0.0}
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            raise ValueError(f'{where}: expected an object')
        ignore = METADATA if where == '$' else set()
        if set(actual) - ignore != set(expected) - ignore:
            raise ValueError(f'{where}: object keys differ')
        for key in expected.keys() - ignore:
            compare(actual[key], expected[key], f'{where}.{key}', stats)
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise ValueError(f'{where}: list lengths or types differ')
        for i, (a, b) in enumerate(zip(actual, expected)):
            compare(a, b, f'{where}[{i}]', stats)
    elif isinstance(expected, float):
        if isinstance(actual, bool) or not isinstance(actual, (int, float)):
            raise ValueError(f'{where}: expected a number')
        if not math.isfinite(actual) or not math.isfinite(expected):
            raise ValueError(f'{where}: non-finite number')
        error = abs(actual - expected)
        limit = ABS_TOL + REL_TOL * abs(expected)
        stats['numeric_values_compared'] += 1
        stats['maximum_absolute_difference'] = max(stats['maximum_absolute_difference'], error)
        stats['maximum_tolerance_fraction'] = max(stats['maximum_tolerance_fraction'], error / limit)
        if error > limit:
            raise ValueError(f'{where}: {actual!r} differs from {expected!r}, tolerance {limit:g}')
    elif type(actual) is not type(expected) or actual != expected:
        raise ValueError(f'{where}: exact value or type differs')
    return stats


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    if out.is_relative_to(HERE.parent):
        parser.error('Choose an output directory outside this attempt to preserve its records.')
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS']:
        env[key] = '1'
    env['PYTHONOPTIMIZE'] = '0'
    report = dict(status='running', python=platform.python_version(), numpy=np.__version__,
                  date=datetime.now(timezone.utc).date().isoformat(),
                  interpretation='Replay diagnostics, not interval certification.',
                  absolute_tolerance=ABS_TOL, relative_tolerance=REL_TOL, jobs=[])
    try:
        for script, record in JOBS:
            start = time.monotonic()
            generated = out / record
            command = [sys.executable, str(HERE / script), '--output', str(generated)]
            result = subprocess.run(command, env=env, capture_output=True, text=True)
            (out / (script + '.log')).write_text(result.stdout + result.stderr)
            require(result.returncode == 0, f'{script} exited with {result.returncode}; see its log')
            actual = json.loads(generated.read_text())
            expected = json.loads((HERE / 'records' / record).read_text())
            if 'source_sha256' in expected:
                require(digest(HERE / script) == expected['source_sha256'],
                        f'{script}: preserved source hash differs from historical record')
                require(actual.get('source_sha256') == expected['source_sha256'],
                        f'{script}: generated source hash differs')
            stats = compare(actual, expected)
            if script == 'check_loop_evolution.py':
                require(max(abs(x['error']) for x in actual['coefficient_controls']['single_prime']) < 1e-12,
                        'Prime coefficient control failed')
                require(max(abs(v['identity_error']) for r in actual['pairings'] for v in r['variants']) < 5e-8,
                        'Full pairing identity control failed')
                require(actual['analytic_controls']['evolution_integral_max_error'] < 1e-10,
                        'Evolution integral control failed')
            if script == 'check_field_mixing.py':
                require(max(abs(x['error']) for x in actual['bare_energy']['two_field']) < 1e-12,
                        'Independent bare-energy elimination control failed')
            report['jobs'].append(dict(script=script, status='passed',
                                       script_sha256=digest(HERE / script),
                                       reference_record=record,
                                       reference_sha256=digest(HERE / 'records' / record),
                                       generated_sha256=digest(generated),
                                       generated_bytes=generated.stat().st_size,
                                       elapsed_seconds=round(time.monotonic() - start, 3),
                                       comparison=stats))
            print(f'PASS {script}', flush=True)
        rejected = out / 'disabled-assertions-must-not-exist.json'
        require(not rejected.exists(), 'Negative-control output path already exists; choose a fresh output directory')
        result = subprocess.run([sys.executable, '-O', str(HERE / 'check_field_mixing.py'),
                                 '--output', str(rejected)], env=env, capture_output=True, text=True)
        require(result.returncode != 0 and 'Run without -O' in result.stderr and not rejected.exists(),
                'Disabled-assertion rejection control failed')
        report['disabled_assertions_control'] = 'passed: explicit refusal before output'
        report['status'] = 'passed'
    except Exception as error:
        report['status'] = 'failed'
        report['error'] = str(error)
    (out / 'replay-summary.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps(report, indent=2, allow_nan=False))
    return 0 if report['status'] == 'passed' else 1


if __name__ == '__main__':
    raise SystemExit(main())
