#!/usr/bin/env python3
"""Compare both precision records, verify bindings and exact pivot signs.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort not exposed.
The comparisons are supplementary checks; the validated LDL arithmetic
and analytic remainder bound establish the matrix inequality.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path


def interval(row):
    lo, hi = F(row['lower']), F(row['upper'])
    if lo > hi:
        raise ArithmeticError('Reversed interval')
    return lo, hi


def pack(q):
    return {'lower': str(q[0]), 'upper': str(q[1])}


def abs_interval(q):
    lo, hi = q
    return (F(0) if lo <= 0 <= hi else min(abs(lo), abs(hi)), max(abs(lo), abs(hi)))


def gershgorin(record):
    first = [interval(q) for q in record['first_row']]
    rows = []
    for i in range(len(first)):
        terms = [abs_interval(first[abs(j-i)]) for j in range(len(first)) if j != i]
        rows.append((first[0][0] - sum(t[1] for t in terms),
                     first[0][1] - sum(t[0] for t in terms)))
    minimum = (min(r[0] for r in rows), min(r[1] for r in rows))
    return {'row_bounds': [pack(q) for q in rows],
            'minimum_enclosure': pack(minimum),
            'minimum_upper_endpoint_negative': minimum[1] < 0,
            'minimum_display': [float(v) for v in minimum]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--first', type=Path, required=True)
    p.add_argument('--second', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    paths = [args.first, args.second]
    records = [json.loads(p.read_text()) for p in paths]
    script_hash = sha256(Path(__file__).with_name('certify_joint_gram.py').read_bytes()).hexdigest()
    invariant_fields = ('status', 'translations', 'matrix', 'source_width', 'total_support_width',
                        'certified_strict_lower_bound', 'source', 'source_polynomial_coefficients_unnormalized',
                        'source_exact_norm_squared_unnormalized',
                        'autocorrelation_coefficients_for_nonnegative_shift',
                        'sieve_limit', 'all_prime_power_rows', 'base_script_sha256', 'script_sha256')
    for field in invariant_fields:
        if records[0][field] != records[1][field]:
            raise ArithmeticError('Invariant mismatch: ' + field)
    if any(r['script_sha256'] != script_hash for r in records):
        raise ArithmeticError('Extension-script binding failed')
    if sorted(r['bits'] for r in records) != [192, 256]:
        raise ArithmeticError('Expected 192/256-bit records')
    overlaps = []
    minima = []
    for key in ('first_row', 'shifted_LDL_pivots'):
        a, b = records[0][key], records[1][key]
        if len(a) != 7 or len(b) != 7:
            raise ArithmeticError('Wrong matrix dimension')
        for i, (x, y) in enumerate(zip(a, b)):
            x, y = interval(x), interval(y)
            if max(x[0], y[0]) > min(x[1], y[1]):
                raise ArithmeticError(f'Nonoverlapping {key}, index {i}')
            overlaps.append({'field': key, 'index': i, 'overlap': True})
    for r in records:
        pivots = [interval(q) for q in r['shifted_LDL_pivots']]
        if not all(q[0] > 0 for q in pivots):
            raise ArithmeticError('Pivot sign failed')
        minima.append({'bits': r['bits'], 'minimum_pivot_enclosure': pack((
            min(q[0] for q in pivots), min(q[1] for q in pivots))),
            'minimum_pivot_lower_endpoint_display': float(min(q[0] for q in pivots))})
    result = {'status': 'PASSED_192_256_PRECISION_CONSISTENCY_AND_EXACT_PIVOT_SIGN_CHECKS',
              'date': '2026-10-03', 'model': 'GPT-6 (Codex)',
              'serving_variant': 'not exposed', 'reasoning_effort': 'not exposed',
              'certificate_hashes': {p.name: sha256(p.read_bytes()).hexdigest() for p in paths},
              'script_sha256': script_hash,
              'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'invariant_fields_agree': True, 'interval_overlap_checks': overlaps,
              'shift': records[0]['certified_strict_lower_bound'],
              'minimum_pivots': minima,
              'gershgorin_from_256_record': gershgorin(next(r for r in records if r['bits'] == 256)),
              'limitations': ['The Gershgorin lower bound is negative; this is failure of this row-sum test, not a negative matrix eigenvalue.',
                              'The seven positive shifted LDL pivots prove the joint matrix bound.',
                              'Precision overlap checks alone do not certify the arithmetic.',
                              'No complete-source-window or all-window positivity is claimed.']}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'gershgorin_interval_display': result['gershgorin_from_256_record']['minimum_display'],
                      'min_shifted_pivot_lower_display': minima[-1]['minimum_pivot_lower_endpoint_display']}))


if __name__ == '__main__':
    main()
