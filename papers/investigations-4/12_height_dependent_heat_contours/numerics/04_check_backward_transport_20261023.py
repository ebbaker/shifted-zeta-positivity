#!/usr/bin/env python3
"""Exact algebra diagnostics for HDC-09; no theta/source certificate."""
from fractions import Fraction as F
import json
from pathlib import Path

checks = {}
def check(group, actual, expected):
    assert actual == expected, (group, actual, expected)
    checks[group] = checks.get(group, 0) + 1

def repulsion(x):
    return [sum((1 / (xi - xj) for j, xj in enumerate(x) if j != i), F(0))
            for i, xi in enumerate(x)]

for n in range(2, 9):
    c = [F(i * i + 2 * i + 1) for i in range(n)]
    y = [ci + F((-1)**i * (i+1), 20*n) for i, ci in enumerate(c)]
    d = [yi-ci for yi,ci in zip(y,c)]
    sy, sc = repulsion(y), repulsion(c)
    kd = [sum(((d[i]-d[j])/((y[i]-y[j])*(c[i]-c[j]))
              for j in range(n) if j != i), F(0)) for i in range(n)]
    alpha, scale_velocity = F(7,3), F(2,11)
    b = lambda x: F(3,7)-F(5,13)*x+F(2,17)*x*x
    bs = lambda x: -F(1,19)+F(3,23)*x
    for i in range(n):
        check("mixed_laplacian_subtraction", sy[i]-sc[i], -kd[i])
        xi, star = y[i]/alpha, c[i]/alpha
        # Average of b_z along the segment, with no numerical quadrature.
        Di = -F(5,13) + F(2,17)*(xi+star)
        cdot = F(2*i-3, 29)
        eta = cdot-(2*alpha*alpha*sc[i]+scale_velocity*c[i]+2*alpha*bs(star))
        residual = 2*alpha*(b(star)-bs(star))-eta
        direct = 2*alpha*alpha*sy[i]+scale_velocity*y[i]+2*alpha*b(xi)-cdot
        matched = -2*alpha*alpha*kd[i]+scale_velocity*d[i]+2*Di*d[i]+residual
        check("normalized_complete_matched_motion", direct, matched)

for left, right in [(F(-3,2),F(2,3)),(F(1,5),F(11,7)),(F(-2),F(5))]:
    unit = lambda x: F(3,7)-F(2,11)*x+F(5,13)*x*x
    gap = right-left
    divided = (unit(right)-unit(left))/gap
    gap_velocity = 4/gap + 2*(unit(right)-unit(left))
    check("two_root_complete_force_sign", 2*gap*gap_velocity, 8+4*divided*gap*gap)

for t in [F(1,7),F(1),F(5,2)]:
    for T in [F(3),F(9),F(17,2)]:
        if T <= t:
            continue
        for s in [F(0),F(1,13),F(2),F(9)]:
            qT, qt = T/(2*T+s), t/(2*t+s)
            reconstructed = t*qT/(T+2*(t-T)*qT)
            check("quadratic_exact_backward_filter", reconstructed, qt)
            check("quadratic_endpoint_signature", F(1,2)-qT, s/(2*(2*T+s)))
            check("quadratic_stable_squared_gap", 8*(T+s)-8*T, 8*s)
        derivative_at_double = t*T/(T+2*(t-T)*F(1,2))**2
        check("quadratic_sharp_filter_amplification", derivative_at_double, T/t)
        for power in range(5):
            constant = F(7,3)
            hT = 8*T/F(power+1)+constant*T**(-power)
            ht = 8*t/F(power+1)+constant*t**(-power)
            amp = (T/t)**power
            integral = t**(-power)*(T**(power+1)-t**(power+1))/F(power+1)
            check("exact_power_compression_backward_integral", amp*hT-8*integral, ht)

for m in range(2, 13):
    hm = sum((F(1,k) for k in range(1,m+1)),F(0))
    hm2 = sum((F(1,k*k) for k in range(1,m+1)),F(0))
    check("hermite_birth_filter", sum((F(k,k+1) for k in range(1,m)),F(0)), m-hm)
    check("hermite_precision_coefficient", sum((F(k,(k+1)**2) for k in range(1,m)),F(0)), hm-hm2)
    T,s = F(17),F(3,5)
    qs = sum((k*T/((k+1)*T+s) for k in range(1,m)),F(0))
    diff = sum((k*s/((k+1)*((k+1)*T+s)) for k in range(1,m)),F(0))
    check("hermite_exact_terminal_difference", m-hm-qs, diff)

record = {
    "date": "2026-10-23",
    "prepared_for": "Edward Baker",
    "model": "gpt-6-astra",
    "reasoning_effort": "ultra",
    "llm_assistance": True,
    "arithmetic": "Python standard-library exact rational fractions",
    "status": "passed",
    "checks_by_group": checks,
    "total_assertions": sum(checks.values()),
    "scope": "Algebra diagnostics only; no source wall, onset, theta estimate, or simplicity certificate."
}
print(json.dumps(record, indent=2))
