#!/usr/bin/env python3
"""Five outward translated-probe checks, not an all-window certificate.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort not exposed.
Exact polynomial preparation, rational autocorrelation, Arb prime sums.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from math import comb, isqrt
from pathlib import Path
import json
import platform
import time

import flint
from flint import arb, acb, ctx


def ab(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def pack(q):
    if not q.is_finite():
        raise ArithmeticError('Non-finite enclosure')
    return {'lower': str(q.lower().fmpq()), 'upper': str(q.upper().fmpq())}


def polynomial(coefficients, x):
    out = x * 0
    for c in reversed(coefficients):
        out = out * x + c
    return out


def derivative(coefficients):
    return [i * coefficients[i] for i in range(1, len(coefficients))]


def correlation_coefficients():
    """Integral_-a^(a-u) g(x)g(x+u)dx, 0<=u<=2a, in exact rationals."""
    a = F(1, 4)
    h = [F(0)] * 17
    for j in range(9):
        h[2*j] = F(comb(8, j) * (-16) ** j)
    first = derivative(h)
    third = derivative(derivative(first))
    g = [x / 4 for x in first]
    for j, x in enumerate(third):
        g[j] -= x
    phi = [F(0)] * (2 * len(g))
    for i, gi in enumerate(g):
        if not gi:
            continue
        for j, gj in enumerate(g):
            if not gj:
                continue
            for k in range(j + 1):
                m = i + k + 1
                c = gi * gj * comb(j, k) / m
                for v in range(m + 1):
                    phi[j-k+v] += c * comb(m, v) * a ** (m-v) * (-1) ** v
                phi[j-k] -= c * (-a) ** m
    while phi[-1] == 0:
        phi.pop()
    norm2 = phi[0]
    if norm2 <= 0:
        raise ArithmeticError('Nonpositive exact source norm')
    phi = [c / norm2 for c in phi]
    # Independent exact norm integral and endpoint/mean checks.
    direct_norm = sum((gi*gj * (a**(i+j+1)-(-a)**(i+j+1)) / (i+j+1)
                       for i, gi in enumerate(g) for j, gj in enumerate(g)), F(0))
    if direct_norm != norm2 or polynomial(phi, F(1, 2)) != 0 or phi[0] != 1 or phi[1] != 0:
        raise ArithmeticError('Exact polynomial consistency check failed')
    for row in (h, first, derivative(first)):
        if polynomial(row, a) != 0 or polynomial(row, -a) != 0:
            raise ArithmeticError('Preparation endpoint check failed')
    if sum((c * (a**(i+1)-(-a)**(i+1))/(i+1) for i,c in enumerate(g)), F(0)) != 0:
        raise ArithmeticError('Mean moment check failed')
    return g, phi, norm2


def prime_power_rows(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00' * ((limit-p*p)//p+1)
    rows = []
    for p in range(2, limit + 1):
        if sieve[p]:
            n, m = p, 1
            while n <= limit:
                rows.append((n, p, m))
                n *= p
                m += 1
    return sorted(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bits', type=int, choices=(192, 256), default=192)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    start = time.time()
    ell = arb(1)/2
    separations = (4, 6, 8, 10, 12)
    g, exact_phi, exact_norm = correlation_coefficients()
    phi = [ab(c) for c in exact_phi]
    # (1-phi(u))/u, evaluated analytically at u=0 as well.
    divided = [-c for c in phi[1:]]
    def integrand(u, analytic):
        # Entire polynomial/exponential divided by entire sinh(u)/u:
        # meromorphic, so pole-containing balls fail naturally.
        return polynomial(divided, u) * (u/2).exp() / (2*(u*u/4).hypgeom_0f1(acb(3)/2))
    integral = acb.integral(integrand, 0, acb(ell),
                            abs_tol=arb(2)**-100, rel_tol=arb(2)**-100,
                            eval_limit=20000, depth_limit=40)
    if not integral.is_finite() or not integral.imag.contains(0):
        raise ArithmeticError('Validated diagonal integration failed')
    z = (-ell/2).exp()
    gamma0 = acb(arb(1)/4).digamma().real - arb.pi().log()
    diagonal = gamma0 + 2*integral.real + 2*(z.atanh()+z.atan())
    if not diagonal > 0:
        raise ArithmeticError('Diagonal sign not certified')
    limit = int((arb(max(separations))+ell).exp().upper().ceil().fmpq())
    if limit > 300000:
        raise ArithmeticError('Scalar experiment exceeds sieve budget')
    rows = prime_power_rows(limit)
    sums = {r: [arb(0), arb(0), 0] for r in separations}
    for n, p, exponent in rows:
        logn = arb(n).log()
        for r in separations:
            u = logn-r
            if abs(u) < ell:
                if not (u > 0 or u < 0):
                    raise ArithmeticError('Unresolved autocorrelation branch')
                value = polynomial(phi, abs(u))
                weight = arb(p).log()/arb(n).sqrt()
                sums[r][0] += weight*value
                sums[r][1] += weight*abs(value)
                sums[r][2] += 1
            elif not abs(u) > ell:
                raise ArithmeticError('Unresolved support threshold')
    results = []
    for r in separations:
        signed, absolute, count = sums[r]
        remainder = ell*(-arb(5)/2*(r-ell)).exp()/(1-(-2*(r-ell)).exp())
        cross_abs_upper = abs(signed)+remainder
        margin = diagonal-cross_abs_upper
        if not margin > 0:
            raise ArithmeticError(f'Two-source Gram sign unproved at r={r}')
        results.append({'separation': r, 'prime_power_terms': count,
                        'signed_prime_sum': pack(signed), 'absolute_prime_sum': pack(absolute),
                        'absolute_sum_scaled_by_exp_minus_r_over_2': pack(absolute*(-arb(r)/2).exp()),
                        'archimedean_remainder_bound': pack(remainder),
                        'cross_form_lower_bound': pack((-signed-remainder).lower()),
                        'cross_form_upper_bound': pack((-signed+remainder).upper()),
                        'two_source_Gram_minimum_lower_bound': pack(margin.lower())})
    record = {'status': 'CERTIFIED_FIVE_TWO_SOURCE_GRAMS_ONLY', 'date': '2026-10-03',
              'model': 'GPT-6 (Codex)', 'serving_variant': 'not exposed', 'reasoning_effort': 'not exposed',
              'bits': args.bits, 'source_width': '1/2',
              'source': '(-d^2/dx^2+1/4)d/dx [(1-16x^2)^8 on |x|<1/4], L2-normalized',
              'source_polynomial_coefficients_unnormalized': [str(c) for c in g],
              'source_exact_norm_squared_unnormalized': str(exact_norm),
              'autocorrelation_coefficients_for_nonnegative_shift': [str(c) for c in exact_phi],
              'autocorrelation_degree': len(exact_phi)-1,
              'Q_diagonal': pack(diagonal), 'archimedean_finite_integral': pack(integral.real),
              'sieve_limit': limit, 'all_prime_power_rows': len(rows), 'results': results,
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'seconds': time.time()-start,
              'runtime': {'python': platform.python_version(), 'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__},
              'limitations': ['Only five two-dimensional translated-source Gram matrices are checked.',
                              'No full-source larger-window bound or all-window positivity follows.',
                              'The exact polynomial source is in the logarithmic form closure; it is not C-infinity.',
                              'Asymptotic claims use a separate PNT argument, not extrapolation from these rows.']}
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'seconds': record['seconds'],
                      'sieve_limit': limit, 'Q_diagonal': str(diagonal)}), flush=True)


if __name__ == '__main__':
    main()
