#!/usr/bin/env python3
"""Independent exact-rational interval LDL replay of the saved Gram rows.

This verifies the algebra after the saved entry enclosures; it does not
independently reconstruct the prime sums or validate the original integrals.
Prepared for Edward Baker with substantial LLM assistance, 2026-10-03.
Model: GPT-6 (Codex); exact serving variant and effort unavailable.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

SCALE = 1 << 128

def rnd(x):
    a, b = x
    return F((a * SCALE).__floor__(), SCALE), F((b * SCALE).__ceil__(), SCALE)

def add(x, y):
    return rnd((x[0] + y[0], x[1] + y[1]))

def sub(x, y):
    return rnd((x[0] - y[1], x[1] - y[0]))

def mul(x, y):
    products = [a * b for a in x for b in y]
    return rnd((min(products), max(products)))

def square(x):
    a, b = x[0] ** 2, x[1] ** 2
    return rnd((F(0) if x[0] <= 0 <= x[1] else min(a, b), max(a, b)))

def div(x, y):
    if y[0] <= 0:
        raise ArithmeticError('Nonpositive divisor enclosure')
    return mul(x, (1 / y[1], 1 / y[0]))

def sum_intervals(items):
    total = (F(0), F(0))
    for item in items:
        total = add(total, item)
    return total

def audit(path):
    record = json.loads(path.read_text())
    entries = [rnd((F(x['lower']), F(x['upper']))) for x in record['first_row']]
    n = len(entries)
    if n != 7 or any(x[0] > x[1] for x in entries):
        raise ArithmeticError('Invalid matrix dimensions or intervals')
    shift = F(record['certified_strict_lower_bound'])
    if shift != F(1, 20):
        raise ArithmeticError('Unexpected comparison shift')
    L = [[(F(0), F(0)) for _ in range(n)] for _ in range(n)]
    D = []
    for i in range(n):
        L[i][i] = (F(1), F(1))
        pivot = sub(sub(entries[0], (shift, shift)),
                    sum_intervals(mul(square(L[i][k]), D[k]) for k in range(i)))
        if pivot[0] <= 0:
            raise ArithmeticError('Shifted pivot not strictly positive')
        D.append(pivot)
        for j in range(i + 1, n):
            numerator = sub(entries[j - i], sum_intervals(
                mul(mul(L[j][k], L[i][k]), D[k]) for k in range(i)))
            L[j][i] = div(numerator, pivot)
    return {'record': path.name, 'record_sha256': sha256(path.read_bytes()).hexdigest(),
            'all_seven_shifted_pivots_strictly_positive': True,
            'pivot_enclosures': [{'lower': str(x[0]), 'upper': str(x[1])} for x in D],
            'minimum_lower_display': float(min(x[0] for x in D))}

root = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
result = {'status': 'PASSED_INDEPENDENT_RATIONAL_INTERVAL_LDL',
          'date': '2026-10-03', 'model': 'GPT-6 (Codex)',
          'serving_variant': 'not exposed', 'reasoning_effort': 'not exposed',
          'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'rounding_grid': '2^-128, directed after every arithmetic operation',
          'scope': 'Saved matrix entry enclosures only, not independently re-integrated arithmetic',
          'records': [audit(root / name) for name in ('joint_192.json', 'joint_256.json')]}
args.output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'minimum_lower_bounds': [
    x['minimum_lower_display'] for x in result['records']]}))
