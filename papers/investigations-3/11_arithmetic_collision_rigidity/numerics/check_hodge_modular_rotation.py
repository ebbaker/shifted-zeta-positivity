#!/usr/bin/env python3
"""Finite exact algebra for the Hodge/modular/rotation review.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model gpt-6-astra, actual effort max. Internal self-check only.
The analytic identities are proved in the linked note; these finite checks
are not a proof of infinite modularity or a theta sign estimate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform


def add(*polys):
    out = {}
    for p in polys:
        for degree, value in p.items():
            out[degree] = out.get(degree, 0) + value
    return {k: v for k, v in out.items() if v}


def scale(p, scalar, shift=0):
    return {k + shift: scalar * v for k, v in p.items() if scalar * v}


def derivative(p):
    return {k - 1: k * v for k, v in p.items() if k}


def hermite_mode(k):
    # d_xi^k exp(xi^2/2 + 2 i v xi) at zero, for even k.
    assert k % 2 == 0
    return {
        k - 2*j: F(factorial(k) * 2**(k - 2*j) * (-1)**((k - 2*j)//2),
                   2**j * factorial(j) * factorial(k - 2*j))
        for j in range(k//2 + 1)
    }


def source_derivative(p):
    # d_u[e^u exp(-v^2) p(v)] / [e^u exp(-v^2)], v'=2v.
    return add(p, scale(p, -4, 2), scale(derivative(p), 2, 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, left, right):
        if left != right:
            raise ArithmeticError(name)
        checks.append(name)

    for k in range(0, 22, 2):
        right = hermite_mode(k + 2)
        if k >= 2:
            right = add(right, scale(hermite_mode(k - 2), -k*(k - 1)))
        check(f'normalized ladder at even order {k}', source_derivative(hermite_mode(k)), right)

    p0, p2, p4, p6, p8 = [hermite_mode(k) for k in (0, 2, 4, 6, 8)]
    source = scale(add(p4, scale(p0, -3)), F(1, 16))
    first = scale(add(p6, scale(p2, -15)), F(1, 16))
    second = scale(add(p8, scale(p4, -45), scale(p0, 30)), F(1, 16))
    check('source mode normalization including both signed indices', scale(source, 2), {4:F(2), 2:F(-3)})
    check('first complete source derivative', source_derivative(source), first)
    check('second complete source derivative', source_derivative(first), second)
    for name, p in [('source',source),('first derivative',first),('second derivative',second)]:
        check(name+' cancels the zero lattice mode', p.get(0,0), 0)

    # R(f)=f+f_xx/omega^2-omega_x f_x/omega^3.
    # D_theta(Q-iD_theta Q)-i(Q-iD_theta Q)=-i R(Q).
    # Formal coefficients in (Q,Q_theta,Q_theta_theta).
    I = complex(0, 1)  # Only exact Gaussian integers are used here.
    w = [1, -I, 0]
    w_theta = [0, 1, -I]
    check('rotation defect formal coefficients', [w_theta[j]-I*w[j] for j in range(3)], [-I,0,-I])

    record = {
        'date':'2026-10-18', 'timezone':'America/New_York',
        'prepared_for':'Edward Baker', 'actual_model':'gpt-6-astra',
        'actual_effort':'max', 'llm_assistance':'substantial; internal self-check',
        'status':'pass', 'python':platform.python_version(),
        'arithmetic':'exact rational polynomials and Gaussian integers',
        'checks':checks, 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'finite mode ladder and complete source derivatives; formal rotation defect',
        'not_established':['infinite modularity from finite testing','theta collision exclusion','an arithmetic rotation-defect bound','improved error, cost, or height']
    }
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status':'pass','output':str(args.output),'scope':record['scope']}))


if __name__ == '__main__':
    main()
