#!/usr/bin/env python3
"""J-E01 r1: bounded exact algebra, no source grid or theta acquisition.

1 November 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded authoring model gpt-6.1-sol (Codex), reasoning effort ultra.
Python standard library only. Run from any directory; stdout is a small JSON
record. The --repo argument identifies the actual input checkout.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path


def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for e, c in p.items():
            out[e] += c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: v*c for e, v in p.items() if v*c}


def mul(p, q):
    out = defaultdict(F)
    for e, c in p.items():
        for f, d in q.items():
            out[tuple(x+y for x, y in zip(e, f))] += c*d
    return {e: c for e, c in out.items() if c}


def der(p, j):
    out = {}
    for e, c in p.items():
        if e[j]:
            f = list(e)
            f[j] -= 1
            out[tuple(f)] = e[j]*c
    return out


def product(*ps):
    out = {(0,)*len(next(iter(ps[0]))): F(1)}
    for p in ps:
        out = mul(out, p)
    return out


def determinant3(p):
    a, b, c = p[0]
    d, e, f = p[1]
    g, h, i = p[2]
    return add(product(a, e, i), product(b, f, g), product(c, d, h),
               scale(product(c, e, g), -1),
               scale(product(b, d, i), -1),
               scale(product(a, f, h), -1))


def serial(p):
    return [[list(e), str(c)] for e, c in sorted(p.items())]


def coeffs(p):
    assert all(len(e) == 1 for e in p)
    return [str(p.get((j,), F(0))) for j in range(max(e[0] for e in p)+1)]


def translate(p, origin):
    out = defaultdict(F)
    for (n,), c in p.items():
        for j in range(n+1):
            out[(j,)] += c*comb(n, j)*origin**(n-j)
    return {e: c for e, c in out.items() if c}


def value(p, x):
    return sum(c*x**e[0] for e, c in p.items())


def atan_bounds(q, terms):
    partial = sum((-1)**j*q**(2*j+1)/F(2*j+1)
                  for j in range(terms))
    following = partial + (-1)**terms*q**(2*terms+1)/F(2*terms+1)
    return min(partial, following), max(partial, following)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    args = parser.parse_args()
    a = {(1, 0, 0): F(1)}
    z = {(0, 1, 0): F(1)}
    h = {(0, 0, 1): F(1)}
    one = {(0, 0, 0): F(1)}
    field = [scale(add(z, mul(a, a), scale(one, -1)), F(1, 2)),
             scale(mul(z, add(a, h)), 2), add(mul(a, h), scale(z, -1))]

    def D(p):
        return add(*(mul(field[j], der(p, j)) for j in range(3)))

    Q = [add(z, scale(add(mul(a, a), scale(one, -1)), F(3, 2)))]
    for j in range(8):
        Q.append(add(D(Q[-1]), scale(mul(a, Q[-1]), F(1, 4))))
    assert len(Q) == 9

    # Quotient derivatives with respect to L: Q_j'=Q_(j+1)-a Q_j/4.
    A = add(mul(Q[0], Q[3]), scale(mul(Q[1], Q[2]), -1))
    B = add(mul(Q[0], Q[5]), scale(mul(Q[1], Q[4]), -1))
    Dr = add(product(Q[0], Q[0], Q[4]),
             scale(product(Q[0], Q[2], Q[2]), -1),
             scale(product(Q[0], Q[1], Q[3]), -2),
             scale(product(Q[1], Q[1], Q[2]), 2))
    Dt = add(product(Q[0], Q[0], Q[6]),
             scale(product(Q[0], Q[2], Q[4]), -1),
             scale(product(Q[0], Q[1], Q[5]), -2),
             scale(product(Q[1], Q[1], Q[4]), 2))
    N = determinant3([[Q[0], Q[1], Q[2]],
                      [Q[2], Q[3], Q[4]],
                      [Q[4], Q[5], Q[6]]])
    assert add(mul(A, Dt), scale(mul(B, Dr), -1)) == product(Q[0], Q[0], N)
    assert add(mul(D(A), Q[0]), scale(mul(A, D(Q[0])), -2)) == Dr
    assert add(mul(D(B), Q[0]), scale(mul(B, D(Q[0])), -2)) == Dt

    # Endpoint jet p_j=4^j Q_j(0,z,0), only through p_8.
    p = [{(e[1],): c*4**j for e, c in q.items() if e[0] == e[2] == 0}
         for j, q in enumerate(Q)]
    assert all(not p[j] for j in [1, 3, 5, 7])
    p0, p2, p4, p6, p8 = (p[j] for j in [0, 2, 4, 6, 8])
    origin_A = add(mul(p0, p4), scale(mul(p2, p2), -1))
    origin_B = add(product(p0, p0, p6),
                   scale(product(p0, p2, p4), -7),
                   scale(product(p2, p2, p2), 6))
    origin_D = add(mul(p0, p6), scale(mul(p2, p4), -1))
    origin_E = add(product(p0, p0, p8),
                   scale(product(p0, p2, p6), -6),
                   scale(product(p2, p2, p4), 6),
                   scale(product(p0, p4, p4), -1))
    origin_N = determinant3([[p0, p2, p4], [p2, p4, p6], [p4, p6, p8]])
    assert add(mul(origin_A, origin_E), scale(mul(origin_D, origin_B), -1)) == product(p0, p0, origin_N)
    shifted_A = translate(origin_A, F(47, 10))
    shifted_N = translate(origin_N, F(47, 10))
    assert all(c > 0 for c in shifted_A.values())
    assert all(c < 0 for c in shifted_N.values())

    # A purely rational analytic bound, not optional theta acquisition.
    # Machin's identity and alternating-series bounds justify the coarse pi facts.
    lo5, hi5 = atan_bounds(F(1, 5), 20)
    lo239, hi239 = atan_bounds(F(1, 239), 20)
    pi_lo, pi_hi = 16*lo5-4*hi239, 16*hi5-4*lo239
    assert F(157, 50) < pi_lo < pi_hi < F(22, 7)
    q = F(22, 7)
    exp_upper = sum(q**j/F(factorial(j)) for j in range(21))
    exp_upper += q**21/F(factorial(21))/(1-q/F(22))
    assert exp_upper < F(70, 3)
    z_lower = F(157, 50)**2/F(4) * (1+2*F(3, 70))**8
    assert z_lower > F(47, 10)

    # First summand derivatives P_0..P_6 and its complete mixed tail numerator.
    t = {(1,): F(1)}
    unit = {(0,): F(1)}
    P = [add(scale(mul(t, t), 2), scale(t, -3))]
    for j in range(6):
        P.append(add(scale(mul(t, der(P[-1], 0)), 4),
                     mul(add(unit, scale(t, -4)), P[-1])))
    d = add(scale(t, 2), scale(unit, -3))
    At = {(e[0]-1,): c for e, c in P[2].items()}
    Bt = {(e[0]-1,): c for e, c in P[4].items()}
    r = add(mul(der(At, 0), d), scale(At, -2))
    s = add(mul(der(Bt, 0), d), scale(Bt, -2))
    mixed_tail = add(mul(r, der(s, 0)), scale(mul(s, der(r, 0)), -1))
    assert r[(3,)] == 128
    assert mixed_tail[(7,)] == 2**20

    # Classical factorial normalization, symbolic for all k>=1:
    # beta/alpha^2=(2k-1)/(2k+1), beta=(k-1)!(k+1)!/((2k-2)!(2k+2)!).
    # k=1 boundary retained as an additional exact normalization check.
    assert F(factorial(0)*factorial(2), factorial(0)*factorial(4))/F(factorial(1), factorial(2))**2 == F(1, 3)

    base = 'papers/investigations-5/07_positive_theta_primitives/'
    files = ['AGENTS.md', 'GPT_RESEARCH_MODEL_WORKFLOW.md', 'LARGE_FILES.md',
             'tools/CHAT_HISTORY.md',
             base+'jensen/notes/01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md',
             base+'jensen/notes/02_CONTINUATION_FOR_SOL_J_E01_20261101.md',
             base+'notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md',
             base+'notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md',
             base+'notes/04_CONTINUATION_FIRST_COEFFICIENT_INVESTIGATION_20261101.md']
    hashes = {f: sha256((args.repo/f).read_bytes()).hexdigest() for f in files}
    record = dict(date='2026-11-01', prepared_for='Edward Baker',
                  llm_assistance='substantial', model='gpt-6.1-sol', effort='ultra',
                  task='J-E01', request_revision='r1', arithmetic='exact rational polynomial arithmetic; standard library only',
                  code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256=hashes,
                  limits=dict(max_Q=8, tail_derivative_order=6,
                              evaluation_grid=False, coefficient_scan=False,
                              optional_theta_numerical_acquisition=False),
                  Q_variables=['a', 'U', 'chi'], Q=[serial(q) for q in Q],
                  quotient_numerators=dict(Rprime_A=serial(A), C_N=serial(N)),
                  origin=dict(p_even={str(j): coeffs(p[j]) for j in [0, 2, 4, 6, 8]},
                              A=coeffs(origin_A), N=coeffs(origin_N),
                              translated_at='47/10', shifted_A=coeffs(shifted_A), shifted_N=coeffs(shifted_N),
                              analytic_U_lower_bound=str(z_lower),
                              proof='U>47/10; all translated A coefficients positive and N coefficients negative',
                              Rhat_prime_sign='positive', H0_sign='negative',
                              Rhat_prime_formula='A/(2*(U-3/2)^2)', H0_formula='N/(24*(U-3/2)^3)'),
                  tail=dict(P=[coeffs(poly) for poly in P], r=coeffs(r), s=coeffs(s), mixed=coeffs(mixed_tail),
                            Rprime_leading='128*t^2', C_leading='4194304*t^6',
                            derivative_error='E_j=O(e^u*t^(j+2)*exp(-4t)), 0<=j<=6',
                            Rprime_sign='eventually positive', C_sign='eventually positive', effective_cutoff=False),
                  checks=dict(Q_recurrence=True, quotient_derivatives=True,
                              complete_mixed_C_identity=True, odd_endpoint_jets_zero=True,
                              endpoint_mixed_determinant=True, endpoint_coefficient_signs=True,
                              rational_U_lower_bound=True, k1_factor=True,
                              tail_leading_coefficients=True),
                  disposition='Complete bounded return; required C>=0 fails near origin; next [B] J-B01 — Astra')
    print(json.dumps(record, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
