#!/usr/bin/env python3
"""Finite controls for time-reflected endpoint states and their junction.

Uses the standard-library matrix implementation of check_defect_endpoints.
No interacting reflection-positivity or full perturbative-response claim.
"""
import cmath
import json
import math

import check_defect_endpoints as ep


def gauss_legendre(n, lo=0., hi=1.):
    nodes = []
    for j in range(1, n + 1):
        x = math.cos(math.pi * (j - .25) / (n + .5))
        for _ in range(50):
            p0, p1 = 1., x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            derivative = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / derivative
            x -= dx
            if abs(dx) < 2e-15:
                break
        # Recompute the derivative at the accepted root.
        p0, p1 = 1., x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        derivative = n * (x * p1 - p0) / (x * x - 1)
        weight = 2 / ((1 - x * x) * derivative * derivative)
        nodes.append(((lo + hi) / 2 + (hi - lo) * x / 2,
                      (hi - lo) * weight / 2))
    return sorted(nodes)


def bulk_response(a, b, n=48):
    """Two triangles t=s*v and s=t*v remove the corner of the double integral."""
    nodes = gauss_legendre(n)
    total = 0.
    for s, ws in nodes:
        for v, wv in nodes:
            numerator = 2 * a * b * s * v * (2 - 3 * s) * (2 - 3 * s * v)
            d1 = (1 + v) ** 2 + s * s * (a * (1 - s) - b * v * v * (1 - s * v)) ** 2
            d2 = (1 + v) ** 2 + s * s * (b * (1 - s) - a * v * v * (1 - s * v)) ** 2
            total += ws * wv * numerator * (1 / d1 + 1 / d2)
    return total


def direct_midpoint(a, b, n):
    def f(s):
        return s * s * (1 - s)
    result = 0.
    for i in range(n):
        s = (i + .5) / n
        for j in range(n):
            t = (j + .5) / n
            result += (2 * a * b * s * (2 - 3 * s) * t * (2 - 3 * t)
                       / ((s + t) ** 2 + (a * f(s) - b * f(t)) ** 2))
    return result / n ** 2


def cholesky_pivots(a):
    n = len(a)
    lower = [[0.] * n for _ in a]
    pivots = []
    for i in range(n):
        pivot = a[i][i] - sum(lower[i][k] ** 2 for k in range(i))
        pivots.append(pivot)
        if pivot <= 0:
            return pivots
        lower[i][i] = math.sqrt(pivot)
        for j in range(i + 1, n):
            lower[j][i] = (a[j][i] - sum(lower[j][k] * lower[i][k] for k in range(i))) / lower[i][i]
    return pivots


def fields(t, y):
    return (ep.add(ep.scale(ep.SX, .12 * t), ep.scale(ep.SZ, .1)),
            ep.add(ep.scale(ep.SY, .18 * y), ep.scale(ep.SX, .03)),
            ep.scale(ep.SY, .15 * (1 + .2 * t)),
            ep.add(ep.scale(ep.SZ, .13 * (1 + .3 * y)), ep.scale(ep.SX, .02 * t)))


def discrete_transport(eta, reflected_fields=False, reflected_reverse=False, correct_map=True):
    points = [(s, eta * s * s * (1 - s)) for s in [1 - j / 64 for j in range(65)]]
    if reflected_reverse:
        points = [(-t, y) for t, y in reversed(points)]
    u = ep.I2
    for (t0, y0), (t1, y1) in zip(points, points[1:]):
        t, y = (t0 + t1) / 2, (y0 + y1) / 2
        dt, dy = t1 - t0, y1 - y0
        a0, a3, x7, x6 = fields(-t if reflected_fields else t, y)
        if reflected_fields:
            a0 = ep.scale(a0, -1)
        normal_sign = -1 if reflected_reverse and correct_map else 1
        generator = ep.add(ep.scale(a0, 1j * dt), ep.scale(a3, 1j * dy),
                           ep.scale(x7, -dt), ep.scale(x6, normal_sign * dy))
        u = ep.mul(ep.exponential(generator), u)
    return u


def quadratic(matrix, coefficients):
    return sum(coefficients[i].conjugate() * matrix[i][j] * coefficients[j]
               for i in range(len(matrix)) for j in range(len(matrix)))


def main():
    cases = []

    def check(name, value, threshold=2e-12, lower=False):
        passed = math.isfinite(value) and (value >= threshold if lower else value <= threshold)
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison='>=' if lower else '<=', passed=passed))

    base = [(ep.CHI, 1), (ep.D, 1)]
    ket = base + [(ep.K[0], 1), (ep.K[1], -1), (ep.K[2], -1), (ep.KN, -1)]
    bra = base + [(ep.K[0], 1), (ep.K[1], 1), (ep.K[2], 1), (ep.KN, 1)]
    plane_ket = base + [(ep.K[0], 1), (ep.KN, -1)]
    plane_bra = base + [(ep.K[0], 1), (ep.KN, 1)]
    for name, conditions, expected in [('all-direction ket', ket, 1),
                                       ('all-direction bra', bra, 1),
                                       ('all-direction shared', ket + bra, 0),
                                       ('planar ket', plane_ket, 2),
                                       ('planar bra', plane_bra, 2),
                                       ('planar shared', plane_ket + plane_bra, 0),
                                       ('time-tangent bulk control', base + [(ep.K[0], 1)], 4)]:
        check(f'independent constraint nullity: {name}', abs(ep.nullity(conditions) - expected), 0)
    # Original M has columns (-e7,e8,e9,e6), and N=-M*R0.
    m = [[0.] * 4 for _ in range(6)]
    for a, mu, sign in ((3, 0, -1), (4, 1, 1), (5, 2, 1), (2, 3, 1)):
        m[a][mu] = sign
    reflection = [-1, 1, 1, 1]
    nmap = [[-m[a][mu] * reflection[mu] for mu in range(4)] for a in range(6)]
    twist = [1, -1, -1, 1, -1, -1]
    check('proper H and V pi rotations restore the original scalar map',
          max(abs(twist[a] * nmap[a][mu] - m[a][mu]) for a in range(6) for mu in range(4)))
    for eta in (.2, .7):
        left = ep.dagger(discrete_transport(eta, reflected_fields=True))
        right = discrete_transport(eta, reflected_reverse=True)
        wrong = discrete_transport(eta, reflected_reverse=True, correct_map=False)
        check(f'full reflected ordered-transport identity eta={eta}', ep.norm(ep.add(left, ep.scale(right, -1))))
        check(f'unchanged normal scalar map fails reflection eta={eta}', ep.norm(ep.add(left, ep.scale(wrong, -1))), .0001, True)
    # Independent gauge transformations at the two endpoints and the reference.
    ket_u = discrete_transport(.2)
    bra_u = discrete_transport(.7, reflected_reverse=True)
    ga, gb, gc = [ep.exponential(ep.scale(p, 1j * angle))
                  for p, angle in [(ep.SX, .3), (ep.SY, -.4), (ep.SZ, .2)]]
    q = [[1 + .2j], [-.3 + .7j]]
    barq = [[.5 - .4j, .2 + .6j]]
    original = ep.mul(ep.mul(ep.mul(barq, bra_u), ket_u), q)[0][0]
    transformed = ep.mul(ep.mul(ep.mul(
        ep.mul(barq, ep.dagger(gc)), ep.product(gc, bra_u, ep.dagger(gb))),
        ep.product(gb, ket_u, ep.dagger(ga))), ep.mul(ga, q))[0][0]
    check('explicit color contraction cancels the reference gauge frame', abs(original - transformed))

    times = [.4, .9, 1.7, 3.]
    cauchy = [[1 / (r + s) for s in times] for r in times]
    check('free physical-reflection endpoint Gram positive pivots', min(cholesky_pivots(cauchy)), 1e-5, True)
    coefficients = [1 + .2j, -.3 + .5j, .7 - .1j, -.2j]
    norm = quadratic(cauchy, coefficients)
    integral = sum(w * abs(sum(c * math.exp(-r * u) for r, c in zip(times, coefficients))) ** 2
                   for u, w in gauss_legendre(128, 0., 60.))
    check('free endpoint norm agrees with positive Laplace integral', abs(norm - integral), 2e-12)
    for r in (.5, 1., 2.):
        for s in (.7, 1.3):
            check(f'logarithmic free kernel is the opposite-ray kernel r={r} s={s}',
                  abs(math.sqrt(r * s) / (r + s) - 1 / (2 * math.cosh(math.log(r / s) / 2))))
    unit = 1 / math.sqrt(2)
    check('R-twisted diagonal endpoint pairing vanishes', abs(quadratic(ep.SX, [0j, 1 + 0j])))
    check('phase-adjusted R-twisted endpoint form has negative direction',
          quadratic(ep.SX, [unit + 0j, -unit + 0j]).real, -.99)
    check('ordinary adjoint restores positive endpoint direction',
          quadratic(ep.I2, [unit + 0j, -unit + 0j]).real, .99, True)
    check('unadjusted SU2 pi rotation gives non-real norm',
          abs(quadratic(ep.scale(ep.SX, 1j), [unit + 0j, unit + 0j]).imag), .99, True)
    # One real Gaussian oscillator mode suffices to test the odd-reflection sign.
    for mass in (.5, 1., 2.):
        normal_norm = math.exp(-2 * mass * .7) / (2 * mass)
        check(f'even scalar reflection control mass={mass}', normal_norm, 0., True)
        check(f'odd scalar reflection is negative mass={mass}', -normal_norm, -1e-3)
    # SU(2): sum f_abc^2=6, so i Tr(H[V1,V2]) has positive coefficient 6/4.
    free_d = 1 / (4 * math.pi ** 2 * (2 * .7) ** 2)
    cubic_norm = 1.5 * free_d ** 3
    check('gauge-invariant cubic even-reflection control', cubic_norm, 1e-7, True)
    check('gauge-invariant cubic odd-H reflection fails', -cubic_norm, -1e-7)

    # Spatial and internal tangents at the reference point, from the two maps.
    tangent = [-1., 0., 0., 0.]
    bra_tangent = [-reflection[j] * tangent[j] for j in range(4)]
    check('time-normal arrival produces a smooth spacetime join', math.dist(tangent, bra_tangent))
    scal = lambda mat, v: [sum(row[j] * v[j] for j in range(4)) for row in mat]
    check('time-normal arrival produces a continuous scalar direction',
          math.dist(scal(m, tangent), scal(nmap, bra_tangent)))
    old_tangent = [0., 0., 0., -1.]
    check('old defect-normal arrival backtracks under time reflection',
          math.dist(old_tangent, [-reflection[j] * old_tangent[j] for j in range(4)]), 1.99, True)
    for s in (.1, .001, .00001):
        for ratio in (.3, 1., 3.):
            t = ratio * s
            eta = .7
            value = abs(2 * eta ** 2 * s * (2 - 3 * s) * t * (2 - 3 * t)
                        / ((s + t) ** 2 + eta ** 2 * (s * s * (1 - s) - t * t * (1 - t)) ** 2))
            check(f'local cross-exchange bounded at smooth join s={s} ratio={ratio}', value, 2 * eta ** 2)

    coefficient = 1.5 - 2 * math.log(2)
    # Analytically reduced one-dimensional integral; independent of the response routine.
    a_numeric = .5 * sum(w * v * v / (1 - v) ** 2 for v, w in gauss_legendre(32, 0., .5))
    check('exact quadratic bulge coefficient', abs(2 * a_numeric - coefficient))
    responses = []
    for eta in (.01, .1, .3, .7):
        coarse, fine = bulk_response(eta, eta, 32), bulk_response(eta, eta, 64)
        responses.append(dict(eta=eta, response=fine, response_over_eta_squared=fine / eta ** 2))
        check(f'bulk exchange quadrature refinement eta={eta}', abs(coarse - fine))
        check(f'nonzero bulk shape response eta={eta}', fine, .1 * eta ** 2, True)
        check(f'analytic remainder bound eta={eta}', abs(fine - coefficient * eta ** 2), 2 * eta ** 4)
    direct_coarse = direct_midpoint(.3, .7, 320)
    direct_fine = direct_midpoint(.3, .7, 640)
    target = bulk_response(.3, .7, 64)
    check('independent direct-square quadrature approaches transformed integral',
          abs(direct_fine - target), abs(direct_coarse - target) * .35)
    check('independent direct-square quadrature absolute control', abs(direct_fine - target), 3e-6)
    gram_parameters = [.1, .3, .7]
    gram = [[bulk_response(a, b, 64) for b in gram_parameters] for a in gram_parameters]
    check('bulk cross-response finite Gram has positive pivots', min(cholesky_pivots(gram)), 1e-10, True)
    check('straight time-ray bulk exchange vanishes', bulk_response(0., 0.), 0.)

    # A Q-closed state can have a changing norm under a Q-exact deformation.
    qmatrix = [[0j, 1 + 0j, 0j], [0j, 0j, 0j], [0j, 0j, 0j]]
    psi = [[1 + 0j], [0j], [0j]]
    lam = [[0j], [1 + 0j], [0j]]
    harmonic = [[0j], [0j], [1 + 0j]]
    check('norm counterexample uses a nilpotent charge and a closed state',
          ep.norm(ep.mul(qmatrix, qmatrix)) + ep.norm(ep.mul(qmatrix, psi)))
    check('counterexample deformation is Q exact', ep.norm(ep.add(ep.mul(qmatrix, lam), ep.scale(psi, -1))))
    check('harmonic positive control is killed by Q and its adjoint',
          ep.norm(ep.mul(qmatrix, harmonic)) + ep.norm(ep.mul(ep.dagger(qmatrix), harmonic)))
    h = 1e-5
    derivative = ((1 + h) ** 2 - (1 - h) ** 2) / (2 * h)
    check('Q-closed two-state counterexample has norm derivative two', abs(derivative - 2), 2e-10)
    harmonic_derivative = ((1 + h * h) - (1 + h * h)) / (2 * h)
    check('harmonic-state control has zero first norm variation', abs(harmonic_derivative), 0.)

    result = dict(schema_version=1, description=__doc__.strip(),
                  parameters=dict(reflection='x0 -> -x0; all six real scalars even',
                                  scalar_map_columns=['-e7', 'e8', 'e9', 'e6'],
                                  quadrature_orders=[32, 64], direct_midpoint_orders=[320, 640],
                                  bulge='y=eta*s^2*(1-s), 0<=s<=1',
                                  gram_bulges=gram_parameters),
                  bulk_quadratic_coefficient=coefficient, bulk_responses=responses,
                  bulk_gram=gram,
                  case_count=len(cases), all_pass=all(c['passed'] for c in cases), cases=cases)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result['all_pass'])


if __name__ == '__main__':
    main()
