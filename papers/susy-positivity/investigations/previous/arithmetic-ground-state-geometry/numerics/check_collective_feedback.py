#!/usr/bin/env python3
"""Check the collective-feedback rational identities exactly.

This checks algebra only, not domains, compactness, or Weil positivity.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path

NAMES = ('lam', 'kappa', 'mu', 'E', 'c', 'w')
ZERO = (0,) * len(NAMES)


def const(value):
    return {ZERO: Q(value)} if value else {}


def var(name):
    exponents = list(ZERO)
    exponents[NAMES.index(name)] = 1
    return {tuple(exponents): Q(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            value = out.get(exponent, Q(0)) + coefficient
            if value:
                out[exponent] = value
            else:
                out.pop(exponent, None)
    return out


def mul(*polys):
    out = const(1)
    for poly in polys:
        terms = []
        for left, a in out.items():
            for right, b in poly.items():
                terms.append({tuple(x + y for x, y in zip(left, right)): a * b})
        out = add(*terms)
    return out


def sub(left, right):
    return add(left, mul(const(-1), right))


def derivative(poly, name):
    position = NAMES.index(name)
    out = {}
    for exponent, coefficient in poly.items():
        if exponent[position]:
            reduced = list(exponent)
            reduced[position] -= 1
            out[tuple(reduced)] = coefficient * exponent[position]
    return out


def replace(poly, name, replacement):
    position = NAMES.index(name)
    terms = []
    for exponent, coefficient in poly.items():
        reduced = list(exponent)
        power = reduced[position]
        reduced[position] = 0
        terms.append(mul({tuple(reduced): coefficient},
                         *([replacement] * power)))
    return add(*terms)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    lam, kappa, mu, E, c, w = [var(name) for name in NAMES]
    two = const(2)
    den = add(lam, mu)
    den2 = mul(den, den)
    gain = sub(den, kappa)
    # Compare the directly squared readout with the asserted shifted form.
    squared_readout = mul(lam, gain, gain)
    shifted_source = mul(sub(lam, mul(two, kappa)), den2)
    residual = add(mul(two, kappa, mu, den), mul(kappa, kappa, lam))
    assert squared_readout == add(shifted_source, residual)

    matched = mul(const(Q(1, 2)), sub(add(E, c), w))
    contact = sub(add(E, c), mul(two, kappa))
    assert replace(contact, 'kappa', matched) == w

    # Quotient differentiation, clearing the fourth-power denominator.
    quotient_numerator = sub(mul(derivative(residual, 'mu'), den2),
                             mul(residual, derivative(den2, 'mu')))
    assert quotient_numerator == mul(two, kappa, lam, gain, den)

    # Positive numerator decompositions establish both parameter minima,
    # with lambda>=kappa used for the first sign, lambda<kappa for attainability.
    branch_one = sub(mul(lam, residual), mul(kappa, kappa, den2))
    positive_branch_one = mul(
        kappa, mu,
        add(mul(two, lam, sub(lam, kappa)),
            mul(mu, sub(mul(two, lam), kappa))))
    assert branch_one == positive_branch_one
    branch_two = sub(residual, mul(sub(mul(two, kappa), lam), den2))
    assert branch_two == squared_readout

    # At zero auxiliary mass, the residual remains kappa^2/lambda.
    assert mul(lam, replace(residual, 'mu', {})) == mul(
        kappa, kappa, replace(den2, 'mu', {}))

    record = {
        'status': 'passed',
        'arithmetic': 'exact rational multivariable polynomials; Python standard library',
        'checks': [
            'direct squared feedback readout equals shifted reference plus residual',
            'gamma-pole contact and complete prime contact match w0 exactly once',
            'residual parameter derivative after exact quotient differentiation',
            'both parameter-minimum formulas from exact nonnegative numerator decompositions',
            'zero auxiliary mass leaves the nonzero inverse-reference residual'
        ],
        'identity': '||Gamma f||^2 = Q_L[f] + <f,C f>',
        'residual': 'C=2*kappa*mu*(T0+mu)^(-1)+kappa^2*T0*(T0+mu)^(-2)',
        'matching': '2*kappa=exp(D)+sum_p 2*log(p)/(sqrt(p)-1)-w0',
        'limitation': 'Algebra only; not analytical domain, compactness, Schatten-class, physical uniqueness, or Weil positivity verification.'
    }
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        with args.output.open('x') as destination:
            destination.write(output)
    print(output, end='')


if __name__ == '__main__':
    main()
