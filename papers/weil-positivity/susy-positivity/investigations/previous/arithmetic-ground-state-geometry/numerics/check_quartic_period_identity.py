#!/usr/bin/env python3
"""Exact elimination of quartic period moment identities, using Fraction only.

The integration-by-parts identities are proved in the note. This independently
checks their elimination and the obstruction to I(M)=1/M at fixed g.
"""
import argparse
from fractions import Fraction
import json
from math import factorial
from pathlib import Path


def add(*expressions):
    out = {}
    for expression in expressions:
        for key, coefficient in expression.items():
            out[key] = out.get(key, Fraction(0)) + coefficient
            if not out[key]:
                del out[key]
    return out


def times(expression, coefficient, m_power=0, g_power=0):
    return {(m + m_power, g + g_power, n): Fraction(coefficient) * value
            for (m, g, n), value in expression.items() if coefficient * value}


def derivative(expression):
    # A key (m,g,n) represents M**m * g**g * I^(n)(M), with g fixed.
    out = {}
    for (m, g, n), value in expression.items():
        if m:
            out = add(out, {(m - 1, g, n): m * value})
        out = add(out, {(m, g, n + 1): value})
    return out


def require_equal(a, b, name):
    if add(a, times(b, -1)):
        raise RuntimeError('Failed exact identity: ' + name)


def run():
    identity = {(0, 0, 0): Fraction(1)}
    # I'=-A/2; A'=-I/g+MA/(2g)-B/2.
    a = times(derivative(identity), -2)
    b = add(times(derivative(a), -2), times(identity, -2, g_power=-1),
            times(a, 1, m_power=1, g_power=-1))
    # B'=-A/(3g)+2MB/(3g).
    moment_residual = add(derivative(b), times(a, Fraction(1, 3), g_power=-1),
                          times(b, Fraction(-2, 3), m_power=1, g_power=-1))
    ode = times(moment_residual, Fraction(3, 2), g_power=2)
    expected = {(0, 2, 3): Fraction(6), (1, 1, 2): Fraction(-7),
                (2, 0, 1): Fraction(2), (0, 1, 1): Fraction(-7),
                (1, 0, 0): Fraction(2)}
    require_equal(ode, expected, 'third-order period equation')

    reciprocal_residual = {}
    for (m, g, n), value in ode.items():
        key = (m - n - 1, g, 0)
        reciprocal_residual = add(reciprocal_residual,
                                  {key: value * (-1) ** n * factorial(n)})
    require_equal(reciprocal_residual,
                  {(-4, 2, 0): Fraction(-36), (-2, 1, 0): Fraction(-7)},
                  'reciprocal Euler period residual')
    return {'status': 'passed', 'arithmetic': 'exact rational Laurent-polynomial coefficients',
            'checks': ['moment elimination', 'Euler reciprocal residual'],
            'period_equation': "6*g^2*I''' - 7*g*M*I'' + (2*M^2-7*g)*I' + 2*M*I = 0",
            'reciprocal_residual': '-g*(7*M^2+36*g)/M^4',
            'assumptions': ['g is fixed and nonzero', 'lambda=g/2',
                            'flat rapid-decay cycle; integration-by-parts boundary terms vanish'],
            'limitation': 'Checks algebra after the analytic moment identities; not cycle existence, a physical metric, or Weil positivity.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New small JSON record; an existing file is refused.')
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x') as handle:
            handle.write(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
