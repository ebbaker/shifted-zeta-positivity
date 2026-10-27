"""Finite exact diagnostics for the rank-three lattice lift note.

27 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model gpt-6-astra, actual recorded effort max.
The infinite-rank obstruction and marginal identity are proved analytically
in the note; this program checks shell counts and rational error allowances.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import factorial, isqrt
from pathlib import Path
import json

maximum_squared_norm = 16
radius = isqrt(maximum_squared_norm)
one = Counter({0: 1})
for n in range(1, radius + 1):
    one[n*n] = 2

def convolution(left, right):
    out = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            if a+b <= maximum_squared_norm:
                out[a+b] += ca*cb
    return out

cube = Counter()
projected = Counter()
stretched = Counter()
for m in product(range(-radius, radius+1), repeat=3):
    k = sum(n*n for n in m)
    if k <= maximum_squared_norm:
        cube[k] += 1
        if m[1] == m[2] == 0:
            projected[k] += 1
    j = m[0]**2 + 9*m[1]**2 + 9*m[2]**2
    if j <= maximum_squared_norm:
        stretched[j] += 1
assert cube == convolution(convolution(one, one), one)
assert projected == one
assert [cube[k] for k in range(5)] == [1, 6, 12, 8, 6]
assert [stretched[k] for k in (1, 4, 9, 10)] == [2, 2, 6, 8]

# e^3 > sum_{j=0}^8 3^j/j! > 20; inherited pi > 3 then gives
# q=exp(-pi r^2) < 1/20 for every r>=1.
exp_lower = sum((F(3)**j/F(factorial(j)) for j in range(9)), F(0))
assert exp_lower > 20
q = F(1, 20)
delta1 = q/(1-q**3)
allowances = {}
for length in (2, 3, 4):
    qL = q**(length*length)
    deltaL = qL/(1-qL**3)
    theta_error = 4*deltaL + 4*deltaL**2
    A_error = (
        2*q**(length*length-1)/(1-q**(3*length*length))
        *(1+deltaL)*(1+2*delta1)
    )
    allowances[str(length)] = {
        "relative_complete_theta_upper": str(theta_error),
        "relative_A_upper": str(A_error),
    }
    if length == 3:
        assert theta_error < F(8, 10**12)
        assert A_error < F(9, 10**11)

record = {
    "date": "2026-10-27",
    "timezone": "America/New_York",
    "prepared_for": "Edward Baker",
    "llm_assistance": "substantial",
    "model": "gpt-6-astra",
    "effort": "max",
    "thread_id": "01a17ee9-ed08-7271-9f66-04ac5ee516b8",
    "status": "passed",
    "scope": "Finite exact lattice shell diagnostics and rational uniform profile allowances; no physical theta transform, collision exclusion, or independent review",
    "maximum_squared_norm": maximum_squared_norm,
    "rank_one_shell_counts": dict(sorted(one.items())),
    "cubic_shell_counts": dict(sorted(cube.items())),
    "transverse_zero_mode_counts": dict(sorted(projected.items())),
    "Z_times_3Z_times_3Z_shell_counts": dict(sorted(stretched.items())),
    "exp_3_rational_lower": str(exp_lower),
    "pi_input": "pi > 3, weaker than Note05's rational lower bound 157/50",
    "uniform_domain": "r >= 1",
    "allowances": allowances,
    "L3_simple_allowances": {
        "relative_complete_theta_upper": "8/10^12",
        "relative_A_upper": "9/10^11",
    },
    "analytic_proofs_not_verified_by_enumeration": [
        "rank-three small-radius asymptotic",
        "full-support positive-weight spectral obstruction",
        "infinite torus marginal and source-operator commutation",
        "periodic spatial radial-profile distinction",
    ],
}
if __name__ == "__main__":
    out = Path(__file__).with_name("06_RANK_THREE_LATTICE_CHECKS_20261027.json")
    out.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"status": "passed", "record": str(out),
                      "relative_A_L3_upper": "9/10^11", "domain": "r>=1"}))
