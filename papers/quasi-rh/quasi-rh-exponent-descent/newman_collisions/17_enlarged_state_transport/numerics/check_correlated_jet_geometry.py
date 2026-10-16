#!/usr/bin/env python3
"""Exact rational checks of project17 correlated disk-jet geometry.

This is an algebra/method control, not a theta computation or a domain
certificate. Every mathematical value and sign uses fractions.Fraction.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from math import factorial
from pathlib import Path


DEGREE = 3


def add(p, q):
    return [p[j] + q[j] for j in range(DEGREE + 1)]


def multiply(p, q):
    return [sum((p[k] * q[j-k] for k in range(j+1)), Q(0))
            for j in range(DEGREE + 1)]


def divide(p, q):
    assert q[0] != 0
    out = []
    for j in range(DEGREE + 1):
        out.append((p[j] - sum((q[k]*out[j-k] for k in range(1, j+1)), Q(0))) / q[0])
    return out


def inverse_schur(a, h):
    wh = [Q(0)] + h[:DEGREE]
    numerator = wh.copy()
    numerator[0] = a
    denominator = [a*v for v in wh]
    denominator[0] = Q(1)
    return divide(numerator, denominator)


def recursive_jet(a, b, c, d):
    h = [d, Q(0), Q(0), Q(0)]
    for p in [c, b, a]:
        h = inverse_schur(p, h)
    return h


def explicit_jet(a, b, c, d):
    D = 1 - a*a
    return [a,
            D*b,
            D*((1-b*b)*c-a*b*b),
            D*((1-b*b)*((1-c*c)*d-b*c*c-2*a*b*c)+a*a*b*b*b)]


def determinant(m):
    if len(m) == 1:
        return m[0][0]
    return sum(((-1)**j * m[0][j] * determinant([
        [row[k] for k in range(len(m)) if k != j] for row in m[1:]])
        for j in range(len(m))), Q(0))


def principal_minors_of_defect(u):
    T = [[u[i-j] if i >= j else Q(0) for j in range(4)] for i in range(4)]
    defect = [[Q(int(i == j)) - sum((T[i][k]*T[j][k] for k in range(4)), Q(0))
               for j in range(4)] for i in range(4)]
    return [determinant([[defect[i][j] for j in ix] for i in ix])
            for size in range(1, 5) for ix in combinations(range(4), size)]


def conditional_data(a, s, u):
    D = 1-a*a
    assert D > 0 and abs(s) <= D
    b = s/D
    M2 = -a*s*s/D
    R2 = D-s*s/D
    assert abs(u-M2) <= R2
    if R2 == 0:
        return M2, R2, D*a*a*b*b*b, Q(0)
    c = (u-M2)/R2
    M3 = D*((1-b*b)*(-b*c*c-2*a*b*c)+a*a*b*b*b)
    R3 = D*(1-b*b)*(1-c*c)
    return M2, R2, M3, R3


def mapped_physical_jet(f, u, eta, L, lam, lam1, lam2):
    m2 = lam*lam+lam1
    m3 = lam**3+3*lam*lam1+lam2
    return [f[0]+eta*u[0],
            f[1]+eta*(lam*u[0]+L*u[1]),
            f[2]+eta*(m2*u[0]+2*lam*L*u[1]+2*L*L*u[2]),
            f[3]+eta*(m3*u[0]+3*m2*L*u[1]+6*lam*L*L*u[2]+6*L**3*u[3])]


def product_physical_jet(f, u, eta, L, lam, lam1, lam2):
    A = [Q(1), lam, (lam*lam+lam1)/2,
         (lam**3+3*lam*lam1+lam2)/6]
    AF = [f[j]/factorial(j) for j in range(4)]
    F = divide(AF, A)
    error = [eta*L**j*u[j] for j in range(4)]
    physical = multiply(A, add(F, error))
    return [factorial(j)*physical[j] for j in range(4)]


def run():
    grid = [Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1)]
    series_checks = psd_checks = minor_checks = boundary_checks = 0
    interval_checks = physical_checks = elimination_checks = 0
    normalizers = [
        (Q(2), Q(1, 7), Q(0), Q(0), Q(0)),
        (Q(3, 2), Q(2, 11), Q(-2, 5), Q(1, 13), Q(-3, 17)),
        (Q(5), Q(3, 19), Q(1, 3), Q(-2, 7), Q(4, 9)),
    ]  # L, eta, lambda, lambda', lambda''
    for a, b, c, d in product(grid, repeat=4):
        u = explicit_jet(a, b, c, d)
        assert u == recursive_jet(a, b, c, d)
        series_checks += 1
        minors = principal_minors_of_defect(u)
        assert all(v >= 0 for v in minors)
        psd_checks += 1
        minor_checks += len(minors)
        if abs(a) == 1:
            assert u[1:] == [Q(0)]*3
            boundary_checks += 1
        elif abs(b) == 1:
            D = 1-a*a
            assert u[2] == -a*D and u[3] == D*a*a*b
            boundary_checks += 1
        else:
            M2, R2, M3, R3 = conditional_data(a, u[1], u[2])
            assert u[2] == M2+R2*c
            assert u[3] == M3+R3*d
            for sign in [Q(-1), Q(1)]:
                assert explicit_jet(a, b, c, sign)[3] == M3+R3*sign
                assert explicit_jet(a, b, sign, d)[2] == M2+R2*sign
            assert R2 >= 0 and R3 >= 0
            interval_checks += 1
        for L, eta, lam, lam1, lam2 in normalizers:
            m2 = lam*lam+lam1
            f = [Q(2, 7), Q(-3, 8),
                 -eta*(m2*u[0]+2*lam*L*u[1]+2*L*L*u[2]), Q(5, 9)]
            K = mapped_physical_jet(f, u, eta, L, lam, lam1, lam2)
            assert K == product_physical_jet(f, u, eta, L, lam, lam1, lam2)
            physical_checks += 1
            assert K[2] == 0
            eliminated = f[3]-3*lam*f[2]+eta*(
                (lam2-2*lam**3)*u[0]+3*(lam1-lam*lam)*L*u[1]+6*L**3*u[3])
            assert K[3] == eliminated
            elimination_checks += 1
    invalid = [Q(1, 2)]*4
    invalid_minors = principal_minors_of_defect(invalid)
    assert all(abs(v) <= 1 for v in invalid)
    assert any(v < 0 for v in invalid_minors)
    sharp = explicit_jet(Q(0), Q(0), Q(0), Q(1))
    assert sharp == [Q(0), Q(0), Q(0), Q(1)]
    blowup = []
    for k in [2, 4, 16, 64]:
        b = Q(1, k)
        u = explicit_jet(Q(0), b, Q(0), Q(1))
        assert u == [Q(0), b, Q(0), 1-b*b]
        ratio = 6*(1-b*b)/b  # L=eta=1
        assert ratio > 0
        blowup.append({'b': str(b), 'positive_stationary_ratio': str(ratio)})
    return {
        'status': 'PASS',
        'date': '2026-10-10',
        'prepared_for': 'Edward Baker',
        'model_family': 'GPT-6 (Codex)',
        'reasoning_effort': 'not exposed to this worker; not inferred',
        'acknowledgment': 'Prepared with substantial LLM assistance; internal exact arithmetic checks, not independent mathematical validation.',
        'scope': 'Exact rational algebra and method controls; no theta evaluation or domain certificate.',
        'arithmetic': 'fractions.Fraction throughout every mathematical identity and sign decision',
        'parameter_grid': [str(v) for v in grid],
        'formal_series_identity_checks': series_checks,
        'toeplitz_psd_cases': psd_checks,
        'exact_principal_minors_checked': minor_checks,
        'degenerate_boundary_cases': boundary_checks,
        'conditional_interval_cases': interval_checks,
        'physical_product_checks': physical_checks,
        'stationary_drift_elimination_checks': elimination_checks,
        'independent_cauchy_box_counterexample': {
            'coefficients': [str(v) for v in invalid],
            'smallest_principal_minor': str(min(invalid_minors))},
        'third_cauchy_saturator': [str(v) for v in sharp],
        'spatial_error_blowup_control': blowup,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'limitations': [
            'The general identities are proved in the companion note; finite checks alone do not prove them.',
            'No genuine theta source, stationary rectangle, or collision exclusion is evaluated.',
            'The blowup control samples different Schur functions, not one heat orbit.',
            'The local heat non-identifiability proposition is analytic and is not validated by these finite samples.'
        ]
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.record:
        args.record.write_text(payload)
    print(payload, end='')
