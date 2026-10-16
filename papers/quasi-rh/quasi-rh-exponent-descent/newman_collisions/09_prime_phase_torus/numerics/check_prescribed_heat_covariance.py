#!/usr/bin/env python3
"""Exact prescribed quadratic-weight Gaussian covariance and dual hierarchy.

Finite rational common-frequency controls verify algebra, not an actual
large-height signed estimate. No dependencies outside the standard library.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json

DEGREE = 12
checks = 0


def check(condition):
    global checks
    assert condition, f'Assertion {checks + 1} failed'
    checks += 1


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(a, c):
    return [c*x for x in a]


def mul(a, b):
    out = [F(0)]*(DEGREE + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b[:DEGREE + 1 - i]):
            out[i + j] += x*y
    return out


def shift(a, k):
    return [F(0)]*k + a[:DEGREE + 1 - k]


def exp_even(a):
    # exp(a*h^2), to h^12.
    return [a**(j//2)/factorial(j//2) if j % 2 == 0 else F(0)
            for j in range(DEGREE + 1)]


def exp_linear(a):
    return [a**j/factorial(j) for j in range(DEGREE + 1)]


def gaussian_moment(k):
    return F(0) if k % 2 else F(factorial(k), 2**(k//2)*factorial(k//2))


def cmul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def cpow(a, k):
    out = (F(1), F(0))
    for _ in range(k):
        out = cmul(out, a)
    return out


def matrix(gamma, lam, b):
    return [[lam[0], lam[1], *b[0]], [lam[1], lam[2], *b[1]],
            [b[0][0], b[1][0], -gamma, 0, F(3, 2)],
            [b[0][1], b[1][1], 0, 2, 0],
            [b[0][2], b[1][2], F(3, 2), 0, 0]]


def feature(rho, epsilon, phase):
    co, si = phase
    return [co, rho*(si + epsilon*co), rho**2*co,
            rho**3*si, rho**4*co]


def quad(a, q, b):
    return sum(a[i]*q[i][j]*b[j] for i in range(5) for j in range(5))


def quad_poly(a, q, b):
    out = [F(0)]*(DEGREE + 1)
    for i in range(5):
        for j in range(5):
            out = add(out, scale(mul(a[i], b[j]), q[i][j]))
    return out


# Gaussian moments and the exact heat expectation in formal h=sqrt(t/2).
for rho in [F(-3), F(-2, 3), F(0), F(5, 4)]:
    co = exp_linear(rho)
    check([co[j]*gaussian_moment(j) for j in range(DEGREE + 1)]
          == exp_even(rho*rho/2))
    for second in [F(-2), F(1, 3), F(0), F(7, 5)]:
        check(mul(exp_even(rho*rho/2), exp_even(second*second/2))
              == exp_even((rho*rho + second*second)/2))
        check(mul(exp_even((rho*rho + second*second)/2), exp_even(rho*second))
              == exp_even((rho + second)**2/2))

# Centering identity: t=2h^2, rho=ell-mu, and sigma held fixed.
for ell in [F(0), F(1, 3), F(7, 3)]:
    for mu in [F(2), F(-1, 4), F(4, 3)]:
        rho = ell - mu
        # b_n has heat exponent (ell^2-rho^2)/2 in h^2.
        check(mul(exp_even((ell*ell - rho*rho)/2), exp_even(rho*rho/2))
              == exp_even(ell*ell/2))

# Prescribed multiplicative cross term and the non-binomial three-node ratio.
for j in range(1, 5):
    for k in range(1, 5):
        ell, second = F(j, 3), F(k, 3)
        check(mul(mul(exp_even(ell*ell/2), exp_even(second*second/2)),
                  exp_even(ell*second)) == exp_even((ell + second)**2/2))
ell = F(1, 3)
check(mul(exp_even(ell*ell/2), exp_even(ell*ell/2))
      == mul(exp_even((2*ell)**2/2), exp_even(-ell*ell)))

kernel_checks = 0
for count in range(2, 9):
    mu, epsilon, gamma = F(3), F(1, 7), F(1, 11)
    q = matrix(gamma, [F(-2), F(1, 5), F(3)],
               [[F(1), F(-2, 3), F(1, 7)], [F(-3, 5), F(2), F(-1)]])
    logs = [F(k, 3) for k in range(count)]
    rhos = [ell - mu for ell in logs]
    phases = [cmul((F(5, 13), F(12, 13)), cpow((F(3, 5), F(4, 5)), k))
              for k in range(count)]
    features = [feature(rhos[k], epsilon, phases[k]) for k in range(count)]
    # Unheated base 2^-k; every actual coefficient has the prescribed
    # quadratic exponential exp(t*ell^2/4), not freely varied coefficients.
    weights = [scale(exp_even(ell*ell/2), F(1, 2**k))
               for k, ell in enumerate(logs)]
    tilted_bases = [scale(exp_even((logs[k]**2 - rhos[k]**2)/2), F(1, 2**k))
                    for k in range(count)]
    actual = [[F(0)]*(DEGREE + 1) for _ in range(5)]
    shifted = []
    for order in range(DEGREE//2 + 1):
        moment = [[F(0)]*(DEGREE + 1) for _ in range(5)]
        for n in range(count):
            for i in range(5):
                moment[i] = add(moment[i], scale(weights[n],
                                               features[n][i]*rhos[n]**order))
        shifted.append(moment)
    actual = shifted[0]
    expected_tilted_quad = [F(0)]*(DEGREE + 1)
    covariance = [F(0)]*(DEGREE + 1)
    channel_covariance = [F(0)]*(DEGREE + 1)
    partitions = [[F(0)]*(DEGREE + 1) for _ in range(4)]
    for n in range(count):
        for m in range(count):
            rn, rm = rhos[n], rhos[m]
            factor = quad(features[n], q, features[m])
            expected_tilted_quad = add(expected_tilted_quad, scale(
                mul(mul(tilted_bases[n], tilted_bases[m]),
                    exp_even((rn + rm)**2/2)), factor))
            pair_cov = mul(mul(weights[n], weights[m]),
                           add(exp_even(rn*rm), scale(exp_even(F(0)), -1)))
            covariance = add(covariance, scale(pair_cov, factor))
            r = [1, epsilon*rn, rn**2, 0, rn**4]
            s = [0, rn, 0, rn**3, 0]
            rr = [1, epsilon*rm, rm**2, 0, rm**4]
            ss = [0, rm, 0, rm**3, 0]
            R, S, C, Ct = quad(r, q, rr), quad(s, q, ss), quad(r, q, ss), quad(s, q, rr)
            cn, sn = phases[n]
            cm, sm = phases[m]
            four = [(R + S)*(cn*cm + sn*sm)/2,
                    (Ct - C)*(sn*cm - cn*sm)/2,
                    (R - S)*(cn*cm - sn*sm)/2,
                    (C + Ct)*(sn*cm + cn*sm)/2]
            check(sum(four) == factor)
            kernel_checks += 1
            channel_covariance = add(channel_covariance, scale(pair_cov, sum(four)))
            partitions[2*(n >= count//2) + (m >= count//2)] = add(
                partitions[2*(n >= count//2) + (m >= count//2)],
                scale(pair_cov, factor))
    check(expected_tilted_quad == add(quad_poly(actual, q, actual), covariance))
    check(channel_covariance == covariance)
    partition_total = [F(0)]*(DEGREE + 1)
    for part in partitions:
        partition_total = add(partition_total, part)
    check(partition_total == covariance)
    hierarchy = [F(0)]*(DEGREE + 1)
    for k in range(1, DEGREE//2 + 1):
        hierarchy = add(hierarchy, scale(shift(quad_poly(shifted[k], q, shifted[k]), 2*k),
                                         F(1, factorial(k))))
    check(hierarchy == covariance)
    first_shift = shifted[1]
    # Explicit leading covariance coefficient includes shifted candidates.
    lead = quad([entry[0] for entry in first_shift], q,
                [entry[0] for entry in first_shift])
    check(covariance[2] == lead)

# Exact exponent reserves and phase-independent feature lower bound.
for kappa in [F(1), F(9, 8), F(5, 4), F(11, 8), F(3, 2)]:
    a = kappa*(4 - kappa)/16
    b = kappa*(kappa + 4)/16
    check(F(1, 2) - kappa/4 >= F(1, 8))
    check(2*a > 0)
    check(2*a - kappa == -2*b)
for co, si in [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13))]:
    check(co*co + si*si == 1)
    for rho in [F(-1), F(-3, 2), F(-2)]:
        v = feature(rho, F(1, 7), (co, si))
        check(sum(x*x for x in v) >= co*co + si*si)

source = Path(__file__).resolve()
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, help='Write the small record to this path instead of its retained default.')
args = parser.parse_args()
target = args.output or source.with_name('prescribed_heat_covariance_record_20261010.json')
record = {
    'date': '2026-10-10',
    'checker': source.name,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'assertions_passed': checks,
    'common_frequency_ordered_pair_checks': kernel_checks,
    'formal_degree_in_sqrt_t_over_2': DEGREE,
    'families': [
        'Gaussian moments, prescribed quadratic log-weight centering and multiplicative cross term',
        'Exact finite common-frequency four sine/cosine covariance channels',
        'Complete four-way block/core covariance recombination',
        'Gaussian covariance equals full shifted signed-log dual hierarchy through formal degree 12',
        'Leading hierarchy includes both shifted candidate coordinates',
        'Uniform exponent reserves and phase-independent feature lower bound',
    ],
    'arithmetic': 'Python standard-library Fraction, truncated exact formal power series',
    'scope': 'Finite formal algebra checks; asymptotic estimates are proved in Note 4. No actual large-height covariance sign, paid threshold exclusion, or independent validation.',
}
target.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({'record': target.name, 'assertions_passed': checks}, sort_keys=True))
