#!/usr/bin/env python3
"""Finite checks of the defect projectors and endpoint polarization algebra.

Standard library only. Jordan--Wigner gamma matrices and independent row
reduction check the written complex-spinor calculation. Endpoint checks use
the SU(2) transformation tensors, not an interacting field-theory simulator.
"""
import cmath
import itertools
import json
import math


def eye(n):
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def scale(a, c):
    return [[c * z for z in row] for row in a]


def add(*arrays):
    return [[sum(a[i][j] for a in arrays) for j in range(len(arrays[0][0]))]
            for i in range(len(arrays[0]))]


def mul(a, b):
    out = [[0j] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, z in enumerate(row):
            if z:
                for j, w in enumerate(b[k]):
                    if w:
                        out[i][j] += z * w
    return out


def product(*arrays):
    out = eye(len(arrays[0]))
    for a in arrays:
        out = mul(out, a)
    return out


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def norm(a):
    return math.sqrt(sum(abs(z) ** 2 for row in a for z in row))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def exponential(a):
    """Convergent Taylor evaluation for the small two-by-two test matrices."""
    out = term = eye(len(a))
    for k in range(1, 40):
        term = scale(mul(term, a), 1 / k)
        out = add(out, term)
    return out


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a)) for l in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


def tensor(arrays):
    out = [[1]]
    for a in arrays:
        out = kron(out, a)
    return out


def rank(a, tolerance=1e-10):
    """Gaussian elimination, independent of the commuting-projector formula."""
    rows = [row[:] for row in a]
    pivot_row = 0
    for col in range(len(rows[0])):
        if pivot_row == len(rows):
            break
        pivot = max(range(pivot_row, len(rows)), key=lambda r: abs(rows[r][col]))
        if abs(rows[pivot][col]) <= tolerance:
            continue
        rows[pivot], rows[pivot_row] = rows[pivot_row], rows[pivot]
        divisor = rows[pivot_row][col]
        rows[pivot_row] = [z / divisor for z in rows[pivot_row]]
        for r in range(pivot_row + 1, len(rows)):
            factor = rows[r][col]
            if abs(factor) > tolerance:
                rows[r] = [z - factor * w for z, w in zip(rows[r], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


I2 = eye(2)
SX = [[0, 1], [1, 0]]
SY = [[0, -1j], [1j, 0]]
SZ = [[1, 0], [0, -1]]
G = [tensor([SZ] * j + [p] + [I2] * (4 - j))
     for j in range(5) for p in (SX, SY)]
I = eye(32)
CHI = scale(product(*G), -1j)
D = product(*G[3:7])
KN = scale(mul(G[6], G[3]), 1j)
K = [scale(mul(G[7 + mu], G[mu]), 1j) for mu in range(3)]
TH = scale(mul(G[4], G[5]), 1j)


def projector(conditions):
    return product(*(scale(add(I, scale(a, sign)), .5) for a, sign in conditions))


def nullity(conditions):
    return 32 - rank([row for a, sign in conditions for row in add(a, scale(I, -sign))])


def bilinear(v, w):
    return sum(z * t for z, t in zip(v, w))


def antisymmetric(v, w):
    return v[0] * w[1] - v[1] * w[0]


def main():
    cases = []

    def check(name, value, threshold=2e-12, lower=False):
        passed = math.isfinite(value) and (value >= threshold if lower else value <= threshold)
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison='>=' if lower else '<=', passed=passed))

    check('ten-dimensional Clifford relations', max(
        norm(add(mul(G[a], G[b]), mul(G[b], G[a]), scale(I, -2 * (a == b))))
        for a in range(10) for b in range(a, 10)))
    check('Euclidean chirality convention', norm(add(CHI, scale(tensor([SZ] * 5), -1))))
    operators = [('chirality', CHI), ('defect', D), ('normal', KN),
                 ('H Cartan', TH)] + [(f'tangent {mu}', k) for mu, k in enumerate(K)]
    for label, a in operators:
        check(f'involution and Hermiticity: {label}',
              max(norm(add(mul(a, a), scale(I, -1))), norm(add(a, scale(dagger(a), -1)))))
    check('all compatible involutions commute', max(
        norm(add(mul(a, b), scale(mul(b, a), -1)))
        for (_, a), (_, b) in itertools.combinations(operators, 2)))
    check('D equals Kn times H Cartan', norm(add(D, scale(mul(KN, TH), -1))))
    check('oriented tangent product equals chirality times defect',
          norm(add(product(*K), scale(mul(CHI, D), -1))))

    plane_conditions = [(CHI, 1), (D, 1), (KN, -1), (K[1], -1)]
    plane = projector(plane_conditions)
    check('planar projector idempotence', norm(add(mul(plane, plane), scale(plane, -1))))
    check('planar projector trace two', abs(trace(plane) - 2))
    check('planar nullity two by row reduction', abs(nullity(plane_conditions) - 2), 0)
    check('fixed H weight on planar charge', norm(mul(add(TH, I), plane)))
    for angle in (0., .3, 1.1, 2.7, 4.5, 5.8):
        tx, tn = math.cos(angle), math.sin(angle)
        bps = add(scale(G[1], 1j * tx), scale(G[8], tx),
                  scale(G[3], 1j * tn), scale(G[6], tn))
        check(f'full BPS equation for planar tangent {angle}', norm(mul(bps, plane)))

    for label, wrong in [('H scalar for defect tangent', scale(mul(G[4], G[1]), 1j)),
                         ('V scalar for normal', scale(mul(G[7], G[3]), 1j))]:
        check(f'wrong triplet anticommutes with D: {label}',
              norm(add(mul(D, wrong), mul(wrong, D))))
        check(f'wrong triplet simultaneous nullity zero: {label}',
              nullity([(CHI, 1), (D, 1), (wrong, -1)]), 0)
    for components in ((.2, -.3, .4), (.7, 0., 0.), (0., -.5, .1)):
        wrong_h = add(*(scale(G[4 + j], c) for j, c in enumerate(components)))
        check(f'nonzero real wrong-triplet vector is invertible {components}',
              norm(add(mul(wrong_h, wrong_h), scale(I, -sum(c * c for c in components)))))

    orientation_ranks = []
    for signs in itertools.product((-1, 1), repeat=3):
        conditions = [(CHI, 1), (D, 1), (KN, -1)] + [(K[j], -signs[j]) for j in range(3)]
        p = projector(conditions)
        determinant = math.prod(signs)
        expected = int(determinant == -1)
        direct = nullity(conditions)
        orientation_ranks.append(dict(signs=list(signs), determinant=determinant,
                                      expected_rank=expected, computed_rank=direct))
        check(f'all-direction projector rank signs={signs}', abs(trace(p) - expected))
        check(f'all-direction independent nullity signs={signs}', abs(direct - expected), 0)
    # This one common charge works for every tested direction and velocity,
    # rather than choosing a different charge separately for each direction.
    full = projector([(CHI, 1), (D, 1), (KN, -1), (K[0], 1), (K[1], -1), (K[2], -1)])
    for omega in ((1., 0., 0.), (0., 1., 0.), (0., 0., 1.), (.6, .8, 0.),
                  (1 / math.sqrt(3),) * 3):
        for theta in (.2, 1.7, 3.9):
            velocity = [math.cos(theta) * x for x in omega] + [math.sin(theta)]
            bps = add(*(scale(G[j], 1j * velocity[j]) for j in range(4)),
                      scale(G[7], -velocity[0]), scale(G[8], velocity[1]),
                      scale(G[9], velocity[2]), scale(G[6], velocity[3]))
            check(f'one charge across angular family {omega} theta={theta}', norm(mul(bps, full)))
    # Changing chirality or defect sign changes the required orientation.
    for c, d in ((-1, -1), (-1, 1), (1, -1)):
        signs = (-c * d, 1, 1)
        conditions = [(CHI, c), (D, d), (KN, -1)] + [(K[j], -signs[j]) for j in range(3)]
        check(f'orientation convention control c={c} d={d}', abs(nullity(conditions) - 1), 0)

    check('connection scalar generators neutral under residual H Cartan', max(
        norm(add(mul(TH, G[j]), scale(mul(G[j], TH), -1))) for j in (6, 7, 8, 9)))
    polarizations = [(0j, 1 + 0j), (1 + 0j, 0j), (1 + 0j, 1j),
                     (1 + 2j, -.4 + .7j), (-.8j, 2 + .3j)]
    for j, raw in enumerate(polarizations):
        length = math.sqrt(sum(abs(x) ** 2 for x in raw))
        a = tuple(x / length for x in raw)
        v = a
        w = (a[1], -a[0])  # epsilon*a; both endpoint actions vanish.
        physical_adjoint = tuple(x.conjugate() for x in v)
        check(f'fundamental endpoint killed by Q, basis control {j}', abs(antisymmetric(a, v)))
        check(f'antifundamental endpoint killed by Q, basis control {j}', abs(bilinear(a, w)))
        check(f'common-Q free contraction zero, basis control {j}', abs(bilinear(v, w)))
        check(f'physical adjoint contraction unit, basis control {j}',
              abs(bilinear(v, physical_adjoint) - 1))
        check(f'physical adjoint is not killed by same Q, basis control {j}',
              abs(bilinear(a, physical_adjoint)), .99, True)
    # q2 and bar q1 both have charge -1/2. The U(1)-neutral line cannot
    # compensate their total charge. This checks the phase, not a QFT Ward identity.
    for angle in (.3, 1., 2.4):
        endpoint_phase = cmath.exp(-.5j * angle) ** 2
        check(f'off-diagonal pair has H charge minus one angle={angle}',
              abs(endpoint_phase - cmath.exp(-1j * angle)))
        adjoint_phase = cmath.exp(-.5j * angle) * cmath.exp(.5j * angle)
        check(f'physical adjoint pair is neutral angle={angle}', abs(adjoint_phase - 1))

    # Piecewise constant Hermitian backgrounds with noncommuting segments.
    # The order and scalar sign are varied independently of taking the dagger.
    segments = [(scale(SX, .2), scale(SZ, .3)),
                (scale(SZ, -.15), scale(SY, .2)),
                (scale(SY, .12), scale(SX, -.1))]

    def transport(reverse=False, scalar_sign=1, no_scalar=False):
        u = I2
        for a, phi in reversed(segments) if reverse else segments:
            generator = add(scale(a, 1j), scale(phi, 0 if no_scalar else scalar_sign))
            if reverse:
                generator = scale(generator, -1)
            u = mul(exponential(generator), u)
        return u

    forward = transport()
    reversed_same = transport(reverse=True)
    reversed_opposite = transport(reverse=True, scalar_sign=-1)
    check('ordered adjoint equals reversed contour with opposite scalar map',
          norm(add(dagger(forward), scale(reversed_opposite, -1))))
    check('plain contour reversal gives inverse transport',
          norm(add(mul(reversed_same, forward), scale(I2, -1))))
    check('plain reversal differs from adjoint with scalar coupling',
          norm(add(dagger(forward), scale(reversed_same, -1))), .2, True)
    check('zero-scalar control: reversal equals adjoint',
          norm(add(dagger(transport(no_scalar=True)),
                   scale(transport(reverse=True, no_scalar=True), -1))))

    result = dict(schema_version=1, description=__doc__.strip(),
                  parameters=dict(gamma_dimension=32, gamma_convention='Jordan-Wigner, Euclidean 0..9',
                                  chirality='-i Gamma0...Gamma9', defect='Gamma3 Gamma4 Gamma5 Gamma6',
                                  rank_tolerance=1e-10, orientation_signs=[-1, 1],
                                  endpoint_basis_controls=len(polarizations),
                                  adjoint_control_segments=3, exponential_terms=40),
                  orientation_ranks=orientation_ranks,
                  case_count=len(cases), all_pass=all(c['passed'] for c in cases), cases=cases)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result['all_pass'])


if __name__ == '__main__':
    main()
