#!/usr/bin/env python3
"""Exact algebra checks for BW-01 Note 04; no theta computation.

Prepared for Edward Baker with substantial LLM assistance, 20 October 2026.
Model gpt-6-astra (Codex), reasoning effort ultra.
Uses only the Python standard library. Frequency powers are factored out;
the note proves lambda=acos(-q)/20 and the uniform pi/log inequalities.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def poly_add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else F(0)) +
                 (b[i] if i < len(b) else F(0)) for i in range(n)])


def poly_mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return trim(c)


def poly_scale(a, c):
    return trim([c * x for x in a])


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def evaluate(a, x):
    return sum(c * x ** i for i, c in enumerate(a))


def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_case(q):
    d, A = 1 - q*q, 1 / (1 + q)**2
    # Pairs (a,b) represent a+b*sqrt(d), permitting exact odd jets.
    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def scale(x, c):
        return (c*x[0], c*x[1])

    def square(x):
        return (x[0]**2 + d*x[1]**2, 2*x[0]*x[1])

    # cos(theta), -sin(theta), -cos(theta), sin(theta), then repeat.
    modes = [(F(1), 2*q, [(-q, F(0)), (F(0), F(-1)),
                          (q, F(0)), (F(0), F(1))]),
             (F(2), F(1, 2), [(2*q*q-1, F(0)), (F(0), 2*q),
                              (1-2*q*q, F(0)), (F(0), -2*q)])]
    h = []
    for j in range(7):
        value = (q*q+F(1, 2), F(0)) if j == 0 else (F(0), F(0))
        for node, weight, phases in modes:
            value = add(value, scale(phases[j % 4], weight * node**j))
        h.append(value)
    assert h[0] == h[1] == (F(0), F(0))
    assert h[2] == (2*d, F(0))
    assert h[3] == (F(0), -6*q)
    assert h[4] == (14*q*q-8, F(0))
    assert h[2][0] > 0
    assert A*(q*q+F(1, 2)+2*q+F(1, 2)) == 1
    # Each node independently has time derivative n^2 and spatial
    # second derivative -n^2; this is the complete source PDE.
    for node, weight, phases in modes:
        for j in range(4):
            assert add(scale(phases[j], weight * node**2),
                       scale(phases[(j+2) % 4], weight * node**2)) == (0, 0)
    h3sq = square(h[3])
    assert h3sq[1] == 0
    S = h3sq[0] / (9*h[2][0]**2) - h[4][0] / (6*h[2][0])
    curvature = h[4][0]/h[2][0] - h3sq[0]/h[2][0]**2
    assert S == (4-q*q)/(6*d)
    assert curvature == -(4+2*q*q)/d
    assert S >= F(5, 6)
    # ell(20)/lambda^2 < 3/8 is proved in the note. The stronger
    # endpoint L/lambda^2=3/8 already leaves Q strictly positive.
    Lhat = F(3, 8)
    Q = 2*h3sq[0] - 3*h[2][0]*h[4][0] - 18*Lhat*h[2][0]**2
    assert Q == 12*d*(4-q*q-6*Lhat*d) and Q > 0
    # Independent complete critical-value substitution in p_r(y).
    for r in [F(1), F(11, 10), F(2), F(1, 2)]:
        y = -q / r**3
        p = r**4*y*y+2*q*r*y+q*q+F(1, 2)-r**4/2
        value = q*q+F(1, 2)-r**4/2-q*q/r**2
        assert p == value
        assert 2*r**4*y+2*q*r == 0
    # Derivatives of V(alpha) with alpha=lambda^2(t-T).
    V1 = -F(1, 2)*4 - q*q*(-2)
    V2 = -F(1, 2)*16 - q*q*4
    assert V1 == -h[2][0]
    assert V2/h[2][0] == curvature
    return {"q": str(q), "h2_over_A_lambda2": str(h[2][0]),
            "h3_over_A_lambda3_sqrt_d": str(h[3][1]),
            "h4_over_A_lambda4": str(h[4][0]),
            "S_over_lambda2": str(S),
            "V_second_over_h2_lambda2": str(curvature),
            "Q_over_A2_lambda6_at_Lhat_3_8": str(Q)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name(
                            "EVENT_CONDITIONED_POSITIVE_SOURCE_20261020.json"))
    args = parser.parse_args()
    # Symbolic polynomial identities in rho=q^2.
    d = [F(1), F(-1)]
    h2 = poly_scale(d, F(2))
    h4 = [F(-8), F(14)]
    h3sq = poly_scale(poly_mul([F(0), F(1)], d), F(36))
    # 6*d*S=4-rho, after clearing the exact positive denominator.
    lhs = poly_add(poly_scale(h3sq, F(2)),
                   poly_scale(poly_mul(h2, h4), F(-3)))
    rhs = poly_scale(poly_mul(d, [F(4), F(-1)]), F(12))
    assert lhs == rhs
    # V''/h2=-(4+2rho)/(1-rho), again clearing denominators.
    lhs = poly_add(poly_mul(h2, h4), poly_scale(h3sq, F(-1)))
    rhs = poly_scale(poly_mul(d, [F(4), F(2)]), F(-4))
    assert lhs == rhs
    # Discriminant coefficients in v, symbolic in rho, matched separately.
    assert poly_mul([F(1), F(-1)], [F(1, 2), F(1, 2)]) == [F(1, 2), F(0), F(-1, 2)]
    assert poly_mul([F(1), F(-1)], [F(0), F(0), F(-1)]) == [F(0), F(0), F(-1), F(1)]
    # (1+v)/2-v^2=(1-v)(v+1/2) supports its full-interval sign.
    assert poly_mul([F(1), F(-1)], [F(1, 2), F(1)]) == [F(1, 2), F(1, 2), F(-1)]
    # Outward elementary constants, independent of floating transcendents.
    assert sum(F(2)**k / factorial(k) for k in range(6)) > 7
    assert sum(F(3, 5)**k / factorial(k) for k in range(4)) > F(7, 4)
    assert F(3, 5)/80-F(3, 800) == F(3, 800) < F(1, 120)
    # Adaptive b=40 observation, on the subfamily q>=99/100.
    cos3_lower = sum((-1)**k * F(3)**(2*k) / factorial(2*k)
                     for k in range(8))
    assert cos3_lower == F(-355168841, 358758400) > F(-99, 100)
    assert sum(F(6)**k / factorial(k) for k in range(9)) > 199
    # Machin: pi=16 atan(1/5)-4 atan(1/239). Alternating lower
    # atan(1/5) through its fourth term and upper atan(1/239)<=1/239.
    atan5_lower = sum((-1)**k * F(1, 5)**(2*k+1) / (2*k+1)
                      for k in range(4))
    pi_lower = 16*atan5_lower - F(4, 239)
    assert pi_lower > F(157, 50)
    assert sum(F(297, 250)**k / factorial(k) for k in range(6)) > F(1025, 314)
    L2_upper = F(1, 800) + F(297, 1000)/40 - F(1, 500)
    assert L2_upper == F(267, 40000) < F(1, 120)
    assert L2_upper / F(9, 400) < F(3, 8)
    cases = [check_case(q) for q in
             [F(1, 2), F(3, 4), F(9, 10), F(99, 100), F(999, 1000)]]
    own = Path(__file__).resolve()
    note = own.parent.parent / "notes" / "04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md"
    record = {
        "date": "2026-10-20", "prepared_for": "Edward Baker",
        "model": "gpt-6-astra (Codex)", "reasoning_effort": "ultra",
        "method": "Python standard-library exact Fraction algebra",
        "status": "exact control algebra checked; no theta computation",
        "parent_git_revision": "b39c6cc9b4756bc14c2e500e327169db88571d1f",
        "fixed_event_height": 20, "time_class": "any fixed 0<T<=1/2",
        "frequency_definition": "lambda=acos(-q)/20",
        "symbolic_identities": ["deflated jet numerator", "critical-value curvature numerator",
                                "future discriminant factorization", "bracket positivity factorization"],
        "checks": ["complete-source PDE", "exact H=Hx=0", "jets through order four",
                   "event mass normalization", "critical-value substitution", "V derivatives",
                   "Q positivity with L/lambda^2=3/8", "rational exponential lower bounds",
                   "adaptive b=40 floor at q>=99/100", "Machin pi lower bound",
                   "alternating cos(3) lower bound"],
        "limitations": ["positive atomic sources, not theta", "infinitely many simultaneous threshold events",
                        "selected b=20 and b=40 floors only, not the all-height profile", "no fixed symmetric radius as q tends to 1",
                        "control tables do not replace the analytic proof"],
        "cases": cases,
        "source_sha256": {"checker": hash_file(own), "result_note": hash_file(note)},
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"status": "passed", "record": str(args.output),
                      "cases": len(cases)}, indent=2))


def factorial(n):
    value = 1
    for k in range(2, n+1):
        value *= k
    return value


if __name__ == "__main__":
    main()
