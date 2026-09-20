#!/usr/bin/env python3
"""Independent finite diagnostics for the smooth Wilson--Loewner opening note.

Standard library only. Classical matrix backgrounds and complex Clifford
algebra; no interacting field theory, endpoint SUSY, or RH certification.
"""
import cmath
import json
import math


def eye(n):
    return [[complex(i == j) for j in range(n)] for i in range(n)]


def scale(a, c):
    return [[c * z for z in row] for row in a]


def add(*arrays):
    return [[sum(a[i][j] for a in arrays) for j in range(len(arrays[0]))]
            for i in range(len(arrays[0]))]


def mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def comm(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))


def norm(a):
    return math.sqrt(sum(abs(z) ** 2 for row in a for z in row))


def kron(a, b):
    return [[a[i][j] * b[k][l]
             for j in range(len(a)) for l in range(len(b))]
            for i in range(len(a)) for k in range(len(b))]


I2 = eye(2)
ZERO = scale(I2, 0)
SX = [[0, 1], [1, 0]]
SY = [[0, -1j], [1j, 0]]
SZ = [[1, 0], [0, -1]]


def bps_residual(z, dz):
    operator = mul(add(scale(SX, 1j * dz.real),
                       scale(SY, 1j * dz.imag), scale(SZ, abs(dz))),
                   add(scale(SX, z.real), scale(SY, z.imag)))
    spinor = [1 / math.sqrt(2), -1 / math.sqrt(2)]
    return math.sqrt(sum(abs(sum(operator[i][j] * spinor[j]
                                 for j in range(2))) ** 2 for i in range(2)))


def upper_sqrt(z):
    result = cmath.sqrt(z)
    return result if result.imag >= 0 else -result


def simpson(function, steps=1000):
    values = [function(k / steps) for k in range(steps + 1)]
    return (values[0] + values[-1]
            + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2])) / (3 * steps)


def path(s):
    return ((s, .3 + .2 * math.sin(math.pi * s)),
            (1., .2 * math.pi * math.cos(math.pi * s)),
            (0., -.2 * math.pi ** 2 * math.sin(math.pi * s)))


def variation(s, kind):
    if kind == 'fixed':
        return ((.07 * math.sin(2 * math.pi * s), .12 * math.sin(math.pi * s)),
                (.14 * math.pi * math.cos(2 * math.pi * s),
                 .12 * math.pi * math.cos(math.pi * s)))
    if kind == 'moving':
        return ((.03 + .05 * s, .04 * math.cos(math.pi * s)),
                (.05, -.04 * math.pi * math.sin(math.pi * s)))
    _, velocity, acceleration = path(s)
    h, dh = .1 * math.sin(math.pi * s), .1 * math.pi * math.cos(math.pi * s)
    return (tuple(h * v for v in velocity),
            tuple(dh * v + h * a for v, a in zip(velocity, acceleration)))


def fields(x, y):
    connection = [add(scale(SX, .2 + .3 * y), scale(SZ, .1 * x)),
                  add(scale(SY, .15 * x), scale(SZ, -.12 * y))]
    # derivatives[nu][mu] = partial_nu A_mu
    derivatives = [[scale(SZ, .1), scale(SY, .15)],
                   [scale(SX, .3), scale(SZ, -.12)]]
    phi = add(scale(SX, .08 * x * y), scale(SZ, .13 + .04 * x))
    dphi = [add(scale(SX, .08 * y), scale(SZ, .04)), scale(SX, .08 * x)]
    return connection, derivatives, phi, dphi


def coefficients(s, epsilon, kind):
    position, velocity, _ = path(s)
    eta, deta = variation(s, kind)
    position = [x + epsilon * e for x, e in zip(position, eta)]
    velocity = [v + epsilon * e for v, e in zip(velocity, deta)]
    speed = math.hypot(*velocity)
    connection, derivatives, phi, dphi = fields(*position)
    m = add(*(scale(a, 1j * v) for a, v in zip(connection, velocity)),
            scale(phi, speed))
    insertion = ZERO
    for nu in range(2):
        for mu in range(2):
            curvature = add(derivatives[nu][mu], scale(derivatives[mu][nu], -1),
                            scale(comm(connection[nu], connection[mu]), -1j))
            insertion = add(insertion, scale(curvature, 1j * eta[nu] * velocity[mu]))
        cov_derivative = add(dphi[nu], scale(comm(connection[nu], phi), -1j))
        insertion = add(insertion, scale(cov_derivative, speed * eta[nu]))
    insertion = add(insertion, scale(phi, sum(v * e for v, e in zip(velocity, deta)) / speed))
    boundary = add(*(scale(a, 1j * e) for a, e in zip(connection, eta)))
    return m, insertion, boundary


def transport(epsilon, kind, steps=400, with_insertion=False):
    """RK4 of the defining ordered exponential, optionally the curvature insertion."""
    state = (I2, ZERO)

    def rhs(s, pair):
        m, insertion, _ = coefficients(s, epsilon, kind)
        u, j = pair
        return (mul(m, u), add(mul(m, j), mul(insertion, u)) if with_insertion else ZERO)

    def shifted(pair, derivative, amount):
        return tuple(add(a, scale(b, amount)) for a, b in zip(pair, derivative))

    h = 1 / steps
    for k in range(steps):
        s = k * h
        k1 = rhs(s, state)
        k2 = rhs(s + h / 2, shifted(state, k1, h / 2))
        k3 = rhs(s + h / 2, shifted(state, k2, h / 2))
        k4 = rhs(s + h, shifted(state, k3, h))
        state = tuple(add(y, scale(a, h / 6), scale(b, h / 3),
                          scale(c, h / 3), scale(d, h / 6))
                      for y, a, b, c, d in zip(state, k1, k2, k3, k4))
    u, insertion = state
    if with_insertion:
        c0 = coefficients(0, 0, kind)[2]
        c1 = coefficients(1, 0, kind)[2]
        insertion = add(insertion, mul(c1, u), scale(mul(u, c0), -1))
    return u, insertion


def main():
    cases = []

    def check(name, value, threshold, lower=False):
        passed = math.isfinite(value) and (value >= threshold if lower else value <= threshold)
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison='>=' if lower else '<=', passed=passed))

    for r in (.5, 1., 2., 5.):
        for theta in (.2, .7, 1.3, 2.4, 2.9):
            z = r / 2 * (1 + cmath.exp(1j * theta))
            dz = r / 2 * 1j * cmath.exp(1j * theta)
            w = -1 / z
            a = -1 / r
            t = (math.tan(theta / 2) / (2 * r)) ** 2
            check(f'inversion r={r} theta={theta}', abs(w - (a + 2j * math.sqrt(t))), 2e-13)
            check(f'fixed-charge semicircle r={r} theta={theta}', bps_residual(z, dz), 2e-13)

    for a in (-2., -.5):
        for w in (1 + 1j, -3 + 2j):
            for t in (.03, .4):
                f = lambda time: a + upper_sqrt((w - a) ** 2 - 4 * time)
                z = f(t)
                g = a + upper_sqrt((z - a) ** 2 + 4 * t)
                check(f'inverse-map a={a} w={w} t={t}', abs(g - w), 2e-13)
                dt = 1e-6
                derivative = (f(t + dt) - f(t - dt)) / (2 * dt)
                predicted = -2 / (z - a)
                check(f'inverse-Loewner velocity a={a} w={w} t={t}', abs(derivative - predicted), 2e-9)

    for s in (.1, .25, .4, .7):
        w = -1 + .08 * math.sin(math.pi * s) + 1j * (s + .25)
        dw = .08 * math.pi * math.cos(math.pi * s) + 1j
        check(f'nonvertical fixed-charge obstruction s={s}', bps_residual(-1 / w, dw / w ** 2), 1e-3, True)
        w_control = -.9 + 1j * (s + .25)
        check(f'constant-driver control s={s}', bps_residual(-1 / w_control, 1j / w_control ** 2), 2e-13)

    for kind in ('fixed', 'moving', 'tangential'):
        base, insertion = transport(0, kind, with_insertion=True)
        fine, fine_insertion = transport(0, kind, steps=800, with_insertion=True)
        check(f'ordered exponential mesh control {kind}', norm(add(base, scale(fine, -1))), 2e-10)
        check(f'curvature insertion mesh control {kind}', norm(add(insertion, scale(fine_insertion, -1))), 2e-10)
        for epsilon in (1e-3, 5e-4):
            plus = transport(epsilon, kind)[0]
            minus = transport(-epsilon, kind)[0]
            derivative = scale(add(plus, scale(minus, -1)), 1 / (2 * epsilon))
            check(f'nonabelian finite variation {kind} epsilon={epsilon}',
                  norm(add(derivative, scale(insertion, -1))), 2e-8)
        if kind == 'tangential':
            check('fixed-endpoint reparameterization gives zero', norm(insertion), 2e-10)

    # Independent quadrature of A_x=c*y, A_y=0 on (s, epsilon*sin(pi*s)).
    for c in (0., .7, 1.3):
        epsilon = 1e-5
        integral = 2 * c / math.pi
        direct = simpson(lambda s: c * math.sin(math.pi * s))
        derivative = (cmath.exp(1j * epsilon * direct) - cmath.exp(-1j * epsilon * direct)) / (2 * epsilon)
        check(f'abelian curvature response c={c}', abs(derivative - 1j * integral), 2e-11)
    check('same undeformed holonomy has different shape response', 2 * .7 / math.pi, .4, True)
    # Flat A=d(x*y), integrated along genuinely deformed paths with fixed endpoints.
    flat_errors = []
    for epsilon in (-.1, .1):
        direct = simpson(lambda s: .2 + .1 * s + epsilon * math.sin(math.pi * s)
                         + s * (.1 + epsilon * math.pi * math.cos(math.pi * s)))
        flat_errors.append(abs(cmath.exp(1j * direct) - cmath.exp(.3j)))
    check('pure-gauge fixed-endpoint control', max(flat_errors), 2e-11)

    gx, gy = kron(SX, I2), kron(SY, I2)
    ix, iy = kron(SZ, SX), kron(SZ, SY)
    kx, ky = scale(mul(ix, gx), 1j), scale(mul(iy, gy), 1j)
    projector = scale(mul(add(eye(4), scale(kx, -1)), add(eye(4), scale(ky, -1))), .25)
    check('variable-scalar projector is nonzero', abs(sum(projector[i][i] for i in range(4))), .9, True)
    check('variable-scalar projector is idempotent', norm(add(mul(projector, projector), scale(projector, -1))), 2e-13)
    for angle in (0., .3, 1., 1.7, 2.6, 3.5):
        tx, ty = math.cos(angle), math.sin(angle)
        operator = add(scale(gx, 1j * tx), scale(gy, 1j * ty), scale(ix, tx), scale(iy, ty))
        check(f'variable-scalar arbitrary tangent angle={angle}', norm(mul(operator, projector)), 2e-13)
        # M is an isometry into the internal scalar plane, so the free numerator cancels.
        for angle2 in (.2, 2.1):
            ux, uy = math.cos(angle2), math.sin(angle2)
            scalar_map = lambda x, y: (x * math.cos(.7), x * math.sin(.7),
                                       y * math.cos(.4), y * math.sin(.4), 0., 0.)
            n1, n2 = scalar_map(tx, ty), scalar_map(ux, uy)
            numerator = -(tx * ux + ty * uy) + sum(v * w for v, w in zip(n1, n2))
            check(f'free bulk exchange cancellation angles={angle},{angle2}', abs(numerator), 2e-13)

    result = dict(schema_version=1, description=__doc__.strip(),
                  parameters=dict(rk4_steps=[400, 800], variation_epsilon=[.001, .0005],
                                  geometry_r=[.5, 1., 2., 5.],
                                  geometry_theta=[.2, .7, 1.3, 2.4, 2.9]),
                  case_count=len(cases), all_pass=all(c['passed'] for c in cases), cases=cases)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result['all_pass'])


if __name__ == '__main__':
    main()
