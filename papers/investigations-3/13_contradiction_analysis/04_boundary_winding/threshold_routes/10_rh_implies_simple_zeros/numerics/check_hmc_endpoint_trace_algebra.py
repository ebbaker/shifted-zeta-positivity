#!/usr/bin/env python3
"""Frozen finite algebra for HMC-05's endpoint tube comparison / Note 22.

Prepared for Edward Baker, 2026-10-21, with gpt-6-astra / max assistance.
Arithmetic: standard-library Fraction, polynomial quotient rings.
Question: do the heat normalization and critical-point tube profiles agree
with the displayed formulas, retaining the full Hermite birth cluster?
Domain: fixed degrees 2 through 8; no adaptive or theta-root sampling.
Stop on a failed identity. No theta zero/floor certificate or analytic
asymptotic is established by these finite computations.
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import platform

import check_hmc_exact_algebra as algebra
from check_hmc_exact_algebra import trim, add, scale, mul, derivative, value


def divrem(p, q):
    p, q = trim(p), trim(q)
    assert q != [0]
    quotient = [F(0)]*max(1, len(p)-len(q)+1)
    while p != [0] and len(p) >= len(q):
        shift, coefficient = len(p)-len(q), p[-1]/q[-1]
        quotient[shift] += coefficient
        p = add(p, [0]*shift+scale(q, -coefficient))
    return trim(quotient), p


def mod(p, q):
    return divrem(p, q)[1]


def inverse_mod(p, q):
    r0, r1, s0, s1 = trim(q), mod(p, q), [F(0)], [F(1)]
    while r1 != [0]:
        quotient, remainder = divrem(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, add(s0, scale(mul(quotient, s1), -1))
    assert len(r0) == 1 and r0[0]
    out = mod(scale(s0, 1/r0[0]), q)
    assert mod(mul(p, out), q) == [1]
    return out


def hermite(m):
    p = [F(0)]*(m+1)
    for j in range(m//2+1):
        p[m-2*j] = F((-1)**j*factorial(m), 2**j*factorial(j)*factorial(m-2*j))
    return p


def laguerre_coefficient(p, n):
    jets = [p]
    for _ in range(2*n):
        jets.append(derivative(jets[-1]))
    out = [F(0)]
    for j in range(2*n+1):
        out = add(out, scale(mul(jets[j], jets[2*n-j]),
                             F((-1)**(n+j), factorial(j)*factorial(2*n-j))))
    return out


def root_power_sums(p, highest):
    p = scale(p, 1/p[-1])
    degree = len(p)-1
    sums = [F(degree)]
    # Newton sums for a monic polynomial, through the degrees needed below.
    for k in range(1, highest+1):
        if k <= degree:
            total = k*p[degree-k]
            total += sum((p[degree-j]*sums[k-j] for j in range(1, k)), F(0))
        else:
            total = sum((p[degree-j]*sums[k-j] for j in range(1, degree+1)), F(0))
        sums.append(-total)
    return sums


def check_degree(m):
    p, critical = hermite(m), hermite(m-1)
    p1, p2 = derivative(p), derivative(derivative(p))
    assert p1 == scale(critical, m)
    assert add(add(p2, scale(mul([0, 1], p1), -1)), scale(p, m)) == [0]
    inv = inverse_mod(scale(mul(p, p), m), critical)
    gamma = [mod(mul(scale(laguerre_coefficient(p, n), n), inv), critical)
             for n in range(1, m+1)]
    assert gamma[0] == [1]
    assert gamma[1] == mod([F(4*m-2, 6), F(0), F(-1, 6)], critical)
    sums = root_power_sums(critical, m-2)
    outer = [sum((coefficient*sums[j] for j, coefficient in enumerate(poly)), F(0))
             for poly in gamma]
    assert outer[0] == m-1
    assert outer[1] == F(m*(m-1), 2)
    assert all(coefficient > 0 for coefficient in outer)
    # Independently derived in the note by Gaussian quadrature/orthogonality.
    assert outer == [F(m-1)]+[F(comb(m, j+1), factorial(j)) for j in range(1, m)]
    if m == 2:
        assert gamma == [[F(1)], [F(1)]]
    if m == 3:
        assert gamma == [[F(1)], [F(3, 2)], [F(1, 4)]]
    # At t=tau^2/2 the homogeneous heat polynomial is tau^m He_m.
    for j in range(m//2+1):
        heat_coefficient = F((-1)**j*factorial(m), factorial(j)*factorial(m-2*j))
        assert heat_coefficient/2**j == p[m-2*j]
    return {'m': m,
            'individual_profile_coefficients_mod_He_m_minus_1': [[str(c) for c in poly] for poly in gamma],
            'outer_profile_coefficients_in_r_squared': [str(c) for c in outer]}


def check_phase_change():
    # Exact transformed density and amplitude ratio at rational sample jets.
    for p, p1, p2, averaged_q, tau in (
        (F(-2), F(1, 3), F(6), F(19), F(1, 4)),
        (F(3), F(-2), F(-4), F(21), F(1, 7)),
        (F(-1), F(0), F(2), F(2), F(1, 9)),
    ):
        lag = p1*p1-p*p2
        assert lag > 0
        s = p1/p
        minus_sp = lag/(p*p)
        measure = tau*lag/(p1*p1+tau*tau*p*p)
        assert measure == tau*minus_sp/(tau*tau+s*s)
        assert measure*averaged_q/lag == tau*averaged_q/(p1*p1+tau*tau*p*p)
    # Endpoint contribution 1/y^2+1/(d-y)^2 >= 8/d^2.
    for d in (F(1), F(2), F(7, 3)):
        for f in (F(1, 5), F(1, 2), F(4, 5)):
            y = d*f
            assert 1/(y*y)+1/(d-y)**2 >= 8/(d*d)
    return 'pass; fixed rational fixtures only'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    record = {
        'status': 'passed', 'date': '2026-10-21', 'prepared_for': 'Edward Baker',
        'model': 'gpt-6-astra', 'effort': 'max',
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'python': platform.python_version(),
        'arithmetic': 'Python standard-library Fraction; exact polynomial quotient rings',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'helper': 'check_hmc_exact_algebra.py',
        'helper_sha256': hashlib.sha256(Path(algebra.__file__).read_bytes()).hexdigest(),
        'profiles': [check_degree(m) for m in range(2, 9)],
        'phase_measure_change': check_phase_change(),
        'scope': 'Finite algebra only; no theta event, interval certificate or proof of asymptotic quantifiers.',
    }
    encoded = json.dumps(record, indent=2)+'\n'
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
