#!/usr/bin/env python3
"""Finite arithmetic checks for Note59; no source data or flow computation.

29 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model gpt-6-astra, effort max, Investigation05 chat0028.
Run with --write-record to save the small adjacent JSON record.
"""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json
import sys

coefficients = []
for k in range(5):
    total = 0
    for pairs in range(k // 2 + 1):
        singles = k - 2 * pairs
        count = factorial(k) // (factorial(singles) * factorial(pairs) * 2**pairs)
        total += count * factorial(singles + pairs) * 2**singles * 4**pairs
    coefficients.append(total)
v = [None] + [coefficients[k] + 2*k*coefficients[k-1] + (2 if k == 1 else 0)
              for k in range(1, 5)]
d = [None] + [2*v[k+1] for k in range(1, 4)]
c3 = 6 + 2*sum(comb(4, m+1)*(v[m]+d[m]) for m in range(1, 4))
assert coefficients == [1, 2, 12, 96, 1056]
assert v[1:] == [6, 20, 168, 1824] and d[1:] == [40, 336, 3648]
assert c3 == 11038
assert sum([F(1), F(3, 4), F(15, 16), F(105, 64)]) == F(277, 64)
# Finite examples test arithmetic only. The all-parameter proof is in Note59.
for g0, x, loss in [(F(1), F(5, 4), F(1, 10)),
                    (F(2, 3), F(4, 3), F(1, 20)),
                    (F(1, 10), F(3), F(1, 50))]:
    delta = 1-F(4, 3)*g0*(x-1)
    assert delta > 0
    y = g0*x/delta
    g1 = y-loss
    terminal = 1-F(4, 3)*g1*((1+F(3, 4)/g0)/x-1)
    assert terminal == loss/y
record = {
    'date': '2026-10-29', 'timezone': 'America/New_York',
    'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
    'model': 'gpt-6-astra', 'effort': 'max', 'chat': '0028',
    'status': 'exact arithmetic checks passed',
    'scalar_derivative_bounds': coefficients, 'v_derivative_bounds': v[1:],
    'd_derivative_bounds': d[1:], 'C3': c3, 'Gaussian_H3_cost': '277/64',
    'endpoint_checks': 'three exact-rational illustrative identities passed',
    'limits': 'No source acquisition, PDE computation, interval certificate, or proof of all parameters by testing. Analytical proof is in Note59.'
}
if '--write-record' in sys.argv:
    Path(__file__).with_name('25_DIFFUSION_VARIANCE_CONSTANT_CHECKS_20261029.json').write_text(
        json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
