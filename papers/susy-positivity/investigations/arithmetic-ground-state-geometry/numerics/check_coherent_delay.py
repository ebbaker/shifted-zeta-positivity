#!/usr/bin/env python3
"""Replay coherent-delay signs and coefficients in exact Laurent algebra.

This does not verify the source-domain, Laurent uniqueness, or Hodge proofs.
"""
import argparse
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path


NAMES = ('a', 'tau', 'alpha', 't', 'c', 'z', 'E', 'X')
ZERO_EXP = (0,) * len(NAMES)


def const(real=0, imag=0):
    value = (Q(real), Q(imag))
    return {ZERO_EXP: value} if value != (0, 0) else {}


def var(name, power=1):
    exponents = list(ZERO_EXP)
    exponents[NAMES.index(name)] = power
    return {tuple(exponents): (Q(1), Q(0))}


def add(*polys):
    out = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            old = out.get(exponent, (Q(0), Q(0)))
            value = (old[0] + coefficient[0], old[1] + coefficient[1])
            if value == (0, 0):
                out.pop(exponent, None)
            else:
                out[exponent] = value
    return out


def mul(*polys):
    out = const(1)
    for poly in polys:
        terms = []
        for left, a in out.items():
            for right, b in poly.items():
                exponent = tuple(x + y for x, y in zip(left, right))
                coefficient = (a[0] * b[0] - a[1] * b[1],
                               a[0] * b[1] + a[1] * b[0])
                terms.append({exponent: coefficient})
        out = add(*terms)
    return out


def adjoint(poly):
    out = {}
    for exponent, coefficient in poly.items():
        flipped = list(exponent)
        flipped[NAMES.index('z')] *= -1
        out[tuple(flipped)] = (coefficient[0], -coefficient[1])
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    a, tau, alpha, t, c, z, E, X = [var(name) for name in NAMES]
    zinv, Einv, Xinv = var('z', -1), var('E', -1), var('X', -1)
    neg, imag = const(-1), const(0, 1)
    sym = add(z, zinv)
    anti = add(z, mul(neg, zinv))
    denominator = add(mul(a, a), mul(tau, tau))
    source = [mul(alpha, tau, tau), mul(imag, alpha, a, tau)]
    defect = [mul(neg, t, sym), mul(neg, t, anti)]
    defect_norm = add(*(mul(adjoint(b), b) for b in defect))
    assert defect_norm == mul(const(4), t, t)
    cross_numerator = add(*(add(mul(adjoint(v), b), mul(adjoint(b), v))
                            for v, b in zip(source, defect)))
    expected = add(mul(const(-2), alpha, t, sym, denominator),
                   mul(const(2), alpha, t, a, a, sym),
                   mul(const(2), imag, alpha, a, t, tau, anti))
    assert cross_numerator == expected

    # X=e^(a z), E=e^(a D), valid in the interior |z|<D.
    green_sym = mul(const(Q(1, 2)), var('a', -1), Einv, add(X, Xinv))
    derivative_anti = mul(const(Q(1, 2)), Einv, add(X, Xinv))
    interior_cross = add(mul(const(2), alpha, t, a, a, green_sym),
                         mul(const(2), alpha, a, t, derivative_anti))
    assert interior_cross == mul(const(2), alpha, a, t, Einv, add(X, Xinv))
    # Lowest mode alpha=2, a=1/2, t=E/2: coefficient of X+X^-1 is 1.
    assert Q(2) * Q(2) * Q(1, 2) * Q(1, 2) == 1
    assert Q(4) * Q(1, 2) ** 2 == 1  # contact is E^2=e^D

    # Four-channel Cauchy--Schwarz defect, separately for real/imaginary parts.
    variables = [a, tau, alpha, t]
    squared_sum = mul(add(*variables), add(*variables))
    four_norms = mul(const(4), add(*(mul(v, v) for v in variables)))
    distances = add(*(mul(add(x, mul(neg, y)), add(x, mul(neg, y)))
                      for x, y in combinations(variables, 2)))
    assert add(four_norms, mul(neg, squared_sum)) == distances

    prime_defect = mul(neg, c, var('alpha', -1), z)
    prime_cross = add(mul(adjoint(source[0]), prime_defect),
                      mul(adjoint(prime_defect), source[0]))
    assert prime_cross == add(mul(neg, c, sym, denominator), mul(c, a, a, sym))
    assert mul(adjoint(prime_defect), prime_defect) == mul(c, c, var('alpha', -2))

    record = {
        'status': 'passed',
        'arithmetic': 'exact rational and Gaussian-rational multivariable Laurent polynomials; Python standard library',
        'checks': [
            'two residual channels cancel all double-delay atoms in the defect norm',
            'coherent cross-term signs and denominator-cleared Fourier identity',
            'interior massive-kernel identity and exact lowest-mode pole/contact normalization',
            'four-channel contact lower bound by the exact pairwise-square identity',
            'single-prime atom, positive contact cost and shifted massive-kernel numerator'
        ],
        'remote_pole_coupling': 't=exp(D/2)/2, a=1/2, alpha=2, D>=L',
        'pole_kernel': '2*cosh((x-y)/2)',
        'contact': 'exp(D)',
        'limitation': 'Checks finite algebra and coefficients only; not Hodge preparation, closed-source domains, infinite-series uniqueness, or Weil positivity.'
    }
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        with args.output.open('x') as destination:
            destination.write(output)
    print(output, end='')


if __name__ == '__main__':
    main()
