"""Exact explanatory checks for Edward Baker, 18 November 2026.

OpenAI Codex LLM assistance; actual recorded model and effort unavailable.
Finite algebra checks only; no canonical source certificate.
Run from any directory. The small JSON record is written beside this file.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def derivative(p):
    return [i * p[i] for i in range(1, len(p))]


def value(p, x):
    return sum(a * x**i for i, a in enumerate(p))


def pair_dprime(p, a, b):
    dp = derivative(p)
    ddp = derivative(dp)
    assert value(p, a) == value(p, b) == 0
    va = value(ddp, a) / value(dp, a)
    vb = value(ddp, b) / value(dp, b)
    return (b - a) * (vb - va) / 2


roots = list(map(F, [-7, -3, -1, 1, 4, 9]))
n = 2
a, b = roots[n:n + 2]
g = b - a
gaps = [y - x for x, y in zip(roots, roots[1:])]
left = [sum(gaps[n - m:n]) for m in range(1, n + 1)]
right = [sum(gaps[n + 1:n + 1 + m]) for m in range(1, len(roots) - n - 1)]
direct = sum(1 / ((r - a) * (r - b)) for r in roots if r not in (a, b))
chain = sum(1 / (d * (d + g)) for d in left + right)
dipole = sum((1 / (r - b) - 1 / (r - a)) / g for r in roots if r not in (a, b))
assert direct == chain == dipole == F(9, 40)
p = [F(1)]
for root in roots:
    p = mul(p, [-root, F(1)])
assert pair_dprime(p, a, b) == 2 - g * g * chain == F(11, 10)

q = [F(-1), F(0), F(1)]
h = mul(q, [F(-25), F(0), F(1)])
assert pair_dprime(q, F(-1), F(1)) == 2
assert pair_dprime(h, F(-1), F(1)) == F(5, 3)
assert sum(1 / (r * r - 1) for r in [F(-5), F(5)]) == F(1, 12)
assert sum(F(1, m * (m + 1)) for m in range(1, 41)) == F(40, 41)

record = {
    "date_local": "2026-11-18",
    "timezone": "America/New_York",
    "prepared_for": "Edward Baker",
    "assistance": "OpenAI Codex LLM",
    "actual_recorded_model": None,
    "actual_recorded_effort": None,
    "status": "same-assistant exact finite algebra checks; not a canonical certificate",
    "arithmetic": "Python standard-library fractions.Fraction",
    "finite_chain": {
        "zeros": list(map(str, roots)), "target": [str(a), str(b)],
        "left_cumulative_distances": list(map(str, left)),
        "right_cumulative_distances": list(map(str, right)),
        "M_direct_chain_and_dipole": str(chain),
        "Dprime_polynomial_and_gap_law": "11/10",
    },
    "local_factor_example": {
        "isolated_initial_polynomial": "z^2-1",
        "with_exterior_initial_polynomial": "(z^2-1)(z^2-25)",
        "target_D_at_zero": "1",
        "isolated_Dprime": "2",
        "with_exterior_M": "1/12",
        "with_exterior_Dprime": "5/3",
        "check": "direct Hzz/Hz at both target roots",
    },
    "uniform_chain": {
        "finite_telescoping_sum_m_1_to_40": "40/41",
        "infinite_limit": "1, by the displayed telescoping formula in manuscript section 4",
    },
    "collision_control": {
        "field": "H(t,z)=z^2-2(t-T)",
        "D": "2(t-T)", "M": "0", "Dprime": "2",
        "scope": "generic finite heat identity permits D=0; literal theta source absent",
    },
    "all_checks_passed": True,
}
dest = Path(__file__).with_name("02_GAP_CHAIN_FACTOR_EXACT_CHECKS_20261118.json")
dest.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "passed", "record": str(dest)}))
