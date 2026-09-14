#!/usr/bin/env python3
"""Exact common-core differential/Grassmann algebra checks; no third-party packages.

Coefficients are integer polynomials in the first and second jets of h.
Products normal-order spatial derivatives using the Leibniz rule. This checks
the proposed four-supercharge identities, not domains or an arithmetic norm.
"""
import argparse
import json
from pathlib import Path

ZERO = (0, 0, 0, 0, 0)
ONE = {ZERO: 1}


def variable(index):
    powers = list(ZERO)
    powers[index] = 1
    return {tuple(powers): 1}


def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
        if not out[key]:
            del out[key]
    return out


def scale(a, factor):
    return {k: factor * v for k, v in a.items() if factor * v}


def multiply(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(x + y for x, y in zip(ka, kb))
            out = add(out, {key: va * vb})
    return out


def derivative(poly, axis):
    # Jets: h_y, h_theta, h_yy, h_ytheta, h_thetatheta.
    destinations = (2, 3) if axis == 0 else (3, 4)
    out = {}
    for powers, coefficient in poly.items():
        if any(powers[2:]):
            raise ValueError('A third derivative was requested unexpectedly')
        for index in range(2):
            if powers[index]:
                new = list(powers)
                new[index] -= 1
                new[destinations[index]] += 1
                out = add(out, {tuple(new): coefficient * powers[index]})
    return out


def harmonic(poly):
    # Exact quotient by h_thetatheta = -h_yy.
    out = {}
    for powers, coefficient in poly.items():
        new = list(powers)
        new[2] += new[4]
        sign = (-1) ** new[4]
        new[4] = 0
        out = add(out, {tuple(new): coefficient * sign})
    return out


def add_term(op, key, poly):
    value = add(op.get(key, {}), poly)
    if value:
        op[key] = value
    else:
        op.pop(key, None)


def op_sum(*ops):
    out = {}
    for op in ops:
        for key, poly in op.items():
            add_term(out, key, poly)
    return out


def op_scale(op, factor):
    return {k: scale(v, factor) for k, v in op.items() if factor}


def compose(left, right):
    out = {}
    for (i, j, dx, dt), a in left.items():
        if dx + dt > 1:
            raise ValueError('This verifier only composes first-order factors')
        for (k, ell, ex, et), b in right.items():
            if j != k:
                continue
            add_term(out, (i, ell, dx + ex, dt + et), multiply(a, b))
            if dx + dt:
                db = derivative(b, 0 if dx else 1)
                add_term(out, (i, ell, ex, et), multiply(a, db))
    return out


def anticommutator(a, b):
    return op_sum(compose(a, b), compose(b, a))


BASIS = ((), (0,), (1,), (0, 1))


def wedge(axis):
    out = {}
    for col, labels in enumerate(BASIS):
        if axis not in labels:
            row = BASIS.index(tuple(sorted((axis,) + labels)))
            out[row, col] = (-1) ** sum(label < axis for label in labels)
    return out


def charge(terms, adjoint=False):
    out = {}
    for matrix, axis, potential_sign in terms:
        for (i, j), value in matrix.items():
            if adjoint:
                i, j = j, i
            dx, dt = (1, 0) if axis == 0 else (0, 1)
            add_term(out, (i, j, dx, dt), scale(ONE, -value if adjoint else value))
            add_term(out, (i, j, 0, 0), scale(variable(axis), value * potential_sign))
    return out


def op_harmonic(op):
    out = {}
    for key, value in op.items():
        add_term(out, key, harmonic(value))
    return out


def require_equal(actual, expected, label):
    if op_sum(actual, op_scale(expected, -1)):
        raise RuntimeError('Exact identity failed: ' + label)


def run():
    ey, et = wedge(0), wedge(1)
    terms1 = [(ey, 0, 1), (et, 1, 1)]
    terms2 = [(et, 0, -1), ({k: -v for k, v in ey.items()}, 1, -1)]
    q1, q1a = charge(terms1), charge(terms1, True)
    q2, q2a = charge(terms2), charge(terms2, True)
    lap_h = add(variable(2), variable(4))
    expected_mixed = {(3, 0, 0, 0): scale(lap_h, -2)}
    expected_difference = {(i, i, 0, 0): scale(lap_h, 2 * (len(labels) - 1))
                           for i, labels in enumerate(BASIS) if len(labels) != 1}
    h1, h2 = anticommutator(q1, q1a), anticommutator(q2, q2a)
    checks = []
    for q, name in [(q1, 'Q1'), (q1a, 'Q1_adjoint'), (q2, 'Q2'), (q2a, 'Q2_adjoint')]:
        require_equal(compose(q, q), {}, name + '_nilpotent')
        checks.append(name + '_nilpotent')
    require_equal(anticommutator(q1, q2), expected_mixed, 'mixed_equals_minus_2_Laplacian_h_wedge')
    checks.append('mixed_equals_minus_2_Laplacian_h_wedge')
    require_equal(anticommutator(q1, q2a), {}, 'mixed_adjoint_zero')
    checks.append('mixed_adjoint_zero')
    require_equal(op_sum(h1, op_scale(h2, -1)), expected_difference,
                  'Hamiltonian_difference_equals_2_Laplacian_h_times_degree_minus_one')
    checks.append('Hamiltonian_difference_equals_2_Laplacian_h_times_degree_minus_one')
    require_equal(op_harmonic(h1), op_harmonic(h2), 'equal_Hamiltonians_for_harmonic_h')
    require_equal(op_harmonic(anticommutator(q1, q2)), {}, 'harmonic_mixed_zero')
    checks.extend(['equal_Hamiltonians_for_harmonic_h', 'harmonic_mixed_zero'])
    return {'status': 'passed', 'arithmetic': 'integer polynomial and exact differential-operator algebra',
            'checks': checks, 'basis': ['1', 'dy', 'dtheta', 'dy_wedge_dtheta'],
            'limitation': 'Common-core algebra only; not domain, ground-state, positivity-of-Weil, or RH verification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New small JSON record; existing files are refused.')
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x') as handle:
            handle.write(rendered)
    print(rendered, end='')


if __name__ == '__main__':
    main()
