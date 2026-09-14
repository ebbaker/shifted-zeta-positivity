#!/usr/bin/env python3
"""Replay exact conservative-coupler and prime-return algebra from note 16.

This checks polynomial identities, not graph scattering completeness, domains,
the contact bound, or full Weil positivity. No floating-point arithmetic is used.
"""
import argparse
import json
from math import comb
from pathlib import Path


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for power, coefficient in polynomial.items():
            out[power] = out.get(power, 0) + coefficient
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def scale(polynomial, coefficient):
    return {power: value * coefficient for power, value in polynomial.items()
            if value * coefficient}


def mul(*polynomials):
    # Monomials are r^a s^b z^c, reduced by s^2=1-r^2; q=r^2.
    out = {(0, 0, 0): 1}
    for polynomial in polynomials:
        terms = []
        for (a, b, c), x in out.items():
            for (d, e, f), y in polynomial.items():
                pairs, odd = divmod(b + e, 2)
                for j in range(pairs + 1):
                    terms.append({(a + d + 2 * j, odd, c + f):
                                  x * y * (-1) ** j * comb(pairs, j)})
        out = add(*terms)
    return out


def star(polynomial):
    # On the unit circle, r and s are real and z*=z^(-1).
    return {(a, b, -c): coefficient for (a, b, c), coefficient in polynomial.items()}


def derivative(polynomial):
    return {(a, b, c - 1): c * coefficient
            for (a, b, c), coefficient in polynomial.items() if c}


def matmul(left, right):
    return [[add(*(mul(x, y) for x, y in zip(row, col)))
             for col in zip(*right)] for row in left]


def adjoint(matrix):
    return [[star(value) for value in row] for row in zip(*matrix)]


def matrix_scale(matrix, polynomial):
    return [[mul(value, polynomial) for value in row] for row in matrix]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    zero, one = {}, {(0, 0, 0): 1}
    r, s, z = {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    q = mul(r, r)
    omq = add(one, scale(q, -1))
    opq = add(one, q)
    den = add(one, scale(mul(q, z), -1))
    denbar = star(den)
    denabs = mul(den, denbar)
    omz = add(one, scale(z, -1))
    identity3 = [[one if i == j else zero for j in range(3)] for i in range(3)]
    identity2 = [[one if i == j else zero for j in range(2)] for i in range(2)]
    coupler = [[omq, r, mul(r, s)], [r, zero, scale(s, -1)],
               [mul(r, s), scale(s, -1), q]]
    assert adjoint(coupler) == coupler
    assert matmul(coupler, coupler) == identity3

    direct = [row[:2] for row in coupler[:2]]
    coupling = [coupler[2][:2]]
    btb = matmul(adjoint(coupling), coupling)
    numerator = [[omq, mul(r, omz)], [mul(r, omz), mul(omq, z)]]
    feedback_numerator = [[add(mul(direct[i][j], den), mul(z, btb[i][j]))
                           for j in range(2)] for i in range(2)]
    assert numerator == feedback_numerator
    assert matmul(adjoint(numerator), numerator) == matrix_scale(identity2, denabs)
    determinant = add(mul(numerator[0][0], numerator[1][1]),
                      scale(mul(numerator[0][1], numerator[1][0]), -1))
    assert determinant == mul(add(z, scale(q, -1)), den)

    assert add(mul(q, omz, star(omz)), mul(omq, omq)) == denabs
    signed_returns = add(mul(q, z, denbar), mul(q, star(z), den))
    assert add(scale(mul(q, denabs), 2), scale(mul(omq, signed_returns), -1)) == \
        mul(q, opq, omz, star(omz))

    differentiated = [[add(mul(derivative(value), den), mul(q, value))
                       for value in row] for row in numerator]
    smith_numerator = matrix_scale(matmul(adjoint(numerator), differentiated), z)
    assert smith_numerator == matrix_scale(btb, den)
    assert add(btb[0][0], btb[1][1]) == add(one, scale(mul(q, q), -1))

    record = {
        'status': 'passed',
        'arithmetic': 'exact integer Laurent-polynomial algebra modulo s^2=1-r^2, q=r^2; Python standard library',
        'checks': [
            'real symmetric three-port coupler squares to the identity',
            'stub elimination yields the stated two-port transfer numerator',
            'external transfer matrix is unitary on the unit circle',
            'transfer determinant is the stated Blaschke factor',
            'observed and complementary output powers sum to one',
            'coherent source Gram has every signed return and contact 2dq/(1-q)',
            'Wigner-Smith matrix numerator and positive trace density identity'
        ],
        'parameterization': {'r': 'sqrt(q)', 's': 'sqrt(1-q)', 'z': 'unit-modulus return phase'},
        'prime_contact': '2 log(p)/(sqrt(p)-1)',
        'limitation': 'Polynomial identities only; not analytical source, graph, contact-bound or Weil-positivity certification.'
    }
    encoded = json.dumps(record, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
