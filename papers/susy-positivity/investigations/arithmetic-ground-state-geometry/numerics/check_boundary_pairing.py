#!/usr/bin/env python3
"""Check finite reflection, Gaussian-source and endpoint algebra exactly.

These are sign and matrix checks, not analytical Hodge or localization proofs.
"""
import argparse
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path


def cq(real=0, imag=0):
    """A Gaussian rational, represented without floating-point complex numbers."""
    return Q(real), Q(imag)


ZERO, ONE, IMAG = cq(), cq(1), cq(0, 1)


def cadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def cmul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def conj(a):
    return a[0], -a[1]


def fadd(*forms):
    out = {}
    for form in forms:
        for mask, coefficient in form.items():
            out[mask] = cadd(out.get(mask, ZERO), coefficient)
    return {mask: coefficient for mask, coefficient in out.items() if coefficient != ZERO}


def scale(form, coefficient):
    return {mask: value for mask, old in form.items()
            if (value := cmul(coefficient, old)) != ZERO}


def wedge_sign(left, right):
    return (-1) ** sum(1 for i in range(4) for j in range(4)
                      if left & (1 << i) and right & (1 << j) and i > j)


def wedge(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            if not a & b:
                value = cmul(cq(wedge_sign(a, b)), cmul(ca, cb))
                out = fadd(out, {a | b: value})
    return out


def star(form):
    return {15 ^ mask: cmul(cq(wedge_sign(mask, 15 ^ mask)), coefficient)
            for mask, coefficient in form.items()}


def conjugate(form):
    return {mask: conj(coefficient) for mask, coefficient in form.items()}


def fermion(form):
    # U dx_j = -i dy_j, U dy_j = i dx_j; extend by exterior multiplication.
    images = [{2: cq(0, -1)}, {1: IMAG}, {8: cq(0, -1)}, {4: IMAG}]
    out = {}
    for mask, coefficient in form.items():
        term = {0: coefficient}
        for j in range(4):
            if mask & (1 << j):
                term = wedge(term, images[j])
        out = fadd(out, term)
    return out


def reflection(form):
    return star(conjugate(fermion(form)))


def inner(left, right):
    value = ZERO
    for mask, coefficient in left.items():
        value = cadd(value, cmul(conj(coefficient), right.get(mask, ZERO)))
    return value


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def inverse(matrix):
    n = len(matrix)
    aug = [[Q(v) for v in row] + [Q(i == j) for j in range(n)]
           for i, row in enumerate(matrix)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        divisor = aug[i][i]
        aug[i] = [value / divisor for value in aug[i]]
        for j in range(n):
            if j != i:
                multiplier = aug[j][i]
                aug[j] = [a - multiplier * b for a, b in zip(aug[j], aug[i])]
    return [row[n:] for row in aug]


def ladd(*polynomials):
    out = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            out[exponent] = out.get(exponent, Q(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def lmul(a, b):
    return ladd(*[{i + j: x * y} for i, x in a.items() for j, y in b.items()])


def lmatmul(a, b):
    return [[ladd(*(lmul(x, y) for x, y in zip(row, col))) for col in zip(*b)] for row in a]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()

    masks = [sum(1 << j for j in pair) for pair in combinations(range(4), 2)]
    basis = [{mask: ONE} for mask in masks]
    scalar = cq(Q(2, 3), Q(5, 7))
    for a in basis:
        assert star(star(a)) == a
        assert fermion(fermion(a)) == a
        assert star(conjugate(fermion(a))) == fermion(star(conjugate(a)))
        assert reflection(reflection(a)) == a
        assert reflection(scale(a, scalar)) == scale(reflection(a), conj(scalar))
        for b in basis:
            assert inner(reflection(a), reflection(b)) == conj(inner(a, b))
    theta = [[reflection(column).get(mask, ZERO)[0] for column in basis] for mask in masks]
    assert all(value[1] == 0 for column in basis for value in reflection(column).values())

    plus, minus = [], []
    for j in range(2):
        dz = {1 << (2 * j): ONE, 1 << (2 * j + 1): IMAG}
        dzbar = conjugate(dz)
        assert fermion(dz) == scale(dz, cq(-1))
        assert fermion(dzbar) == dzbar
        plus.append(fadd(dz, scale(dzbar, cq(-1))))
        minus.append(fadd(dz, dzbar))
    assert wedge(plus[0], minus[0]) == {3: cq(0, -4)}
    alpha_plus = wedge(*plus)
    alpha_minus = wedge(*minus)
    assert wedge(alpha_plus, alpha_minus) == {15: cq(16)}
    assert inner(alpha_plus, alpha_plus) == cq(16)
    assert reflection(alpha_plus) == alpha_plus
    # Gaussian integral coefficients are pi/(2a) and pi^2/(4ab).
    one_pair = cmul(cq(Q(1, 2)), cq(0, -4))
    two_pair = cmul(cq(Q(1, 4)), cq(16))
    assert one_pair == cq(0, -2)
    assert two_pair == cmul(cq(-1), cmul(one_pair, one_pair)) == cq(4)
    # b=(E-1)/(az), E=exp(-a z zbar), a>0: check D_f b=alpha_plus-dz.
    # Monomials below are (power of E, power of z, power of a).
    primitive = {(1, -1, -1): Q(1), (0, -1, -1): Q(-1)}
    holomorphic = {(e, z + 1, a + 1): value for (e, z, a), value in primitive.items()}
    antiholomorphic = {(e, z + 1, a + 1): -e * value
                       for (e, z, a), value in primitive.items() if e}
    assert holomorphic == {(1, 0, 0): Q(1), (0, 0, 0): Q(-1)}
    assert antiholomorphic == {(1, 0, 0): Q(-1)}

    # Laurent polynomials in x=a0/lambda>0 check the entire residual family.
    zero, one, x, xinv = {}, {0: Q(1)}, {1: Q(1)}, {-1: Q(1)}
    g0 = [[x, zero, zero], [zero, one, zero], [zero, zero, xinv]]
    g0inv = [[xinv, zero, zero], [zero, one, zero], [zero, zero, x]]
    pairing = [[zero, zero, one], [zero, one, zero], [one, zero, zero]]
    identity = [[one if i == j else zero for j in range(3)] for i in range(3)]
    source_reflection = lmatmul(g0inv, pairing)
    assert lmatmul(source_reflection, source_reflection) == identity
    assert lmatmul(lmatmul(transpose(source_reflection), g0), source_reflection) == g0
    assert lmatmul(lmatmul(pairing, g0inv), transpose(pairing)) == g0
    assert source_reflection[1][1] == one
    assert source_reflection[0][2] == xinv
    assert source_reflection[2][0] == x

    values = [[Q(1), Q(0), Q(0)], [Q(1), Q(-1), Q(0)],
              [Q(1), Q(-4, 3), Q(4, 9)]]
    metric_orbit = [[Q(16), Q(0), Q(0)], [Q(0), Q(64), Q(0)], [Q(0), Q(0), Q(48)]]
    residue_orbit = [[Q(16), Q(0), Q(0)], [Q(0), Q(-64), Q(0)], [Q(0), Q(0), Q(48)]]
    metric = matmul(matmul(transpose(values), metric_orbit), values)
    residue = matmul(matmul(transpose(values), residue_orbit), values)
    assert metric == [[Q(128), Q(-128), Q(64, 3)],
                      [Q(-128), Q(448, 3), Q(-256, 9)],
                      [Q(64, 3), Q(-256, 9), Q(256, 27)]]
    assert matmul(matmul(residue, inverse(metric)), transpose(residue)) == metric
    assert metric[0][0] / metric_orbit[0][0] == 8

    record = {
        'status': 'passed',
        'arithmetic': 'exact integer, rational, Gaussian-rational and Laurent-polynomial algebra; Python standard library',
        'checks': [
            'degree-two Hodge and fermion reflection: involution, commutation and antiunitarity',
            'Gaussian source cohomology coefficients, product wedge sign and residue calibration prefactor',
            'pure-quartic reflected Gram identities for the full positive one-parameter endpoint family',
            'massive endpoint frame conversion, reflected Gram identity and eightfold Gaussian ratio'
        ],
        'real_one_form_order': ['dx1', 'dy1', 'dx2', 'dy2'],
        'degree_two_basis_masks': masks,
        'reflection_matrix': [[str(value) for value in row] for row in theta],
        'gaussian_pairing_coefficient_of_pi_squared_over_ab': '4',
        'massive_metric_divided_by_4pi_squared': [[str(value) for value in row] for row in metric],
        'limitation': 'Checks finite algebra and signs using the stated Gaussian integral formulas. It does not prove Hodge comparison, physical adjoint domains, cutoff decay, harmonic localization, endpoint continuity, radial uniqueness, arithmetic source closure or Weil positivity.'
    }
    output = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        with args.output.open('x') as destination:
            destination.write(output)
    print(output, end='')


if __name__ == '__main__':
    main()
