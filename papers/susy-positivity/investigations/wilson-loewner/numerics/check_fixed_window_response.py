#!/usr/bin/env python3
"""Finite diagnostics for the fixed-window Wilson response obstruction.

Standard library only. Reuses the existing smooth-junction quadrature.
These checks are not interval enclosures, operator bounds, or a physical
realization of the arithmetic transfer. Analytical proofs are in the note.
"""
import json
import math

from check_reflected_junction import bulk_response, gauss_legendre


W0 = -math.euler_gamma if hasattr(math, 'euler_gamma') else -0.5772156649015328606
W0 -= math.pi / 2 + 3 * math.log(2) + math.log(math.pi)
EULER = 0.5772156649015328606


def tower(u):
    return math.exp(-u / 2) / (-math.expm1(-2 * u))


def tail(epsilon):
    """Exactly 2 integral_epsilon^infinity n_Gamma(u) du."""
    v = math.exp(-epsilon / 2)
    return math.log((1 + v) / (-math.expm1(-epsilon / 2))) + 2 * math.atan(v)


def digamma_positive(z):
    """Recurrence plus Bernoulli asymptotics on the positive real axis."""
    correction = 0.
    while z < 24:
        correction -= 1 / z
        z += 1
    inv = 1 / z
    return (correction + math.log(z) - inv / 2 - inv**2 / 12
            + inv**4 / 120 - inv**6 / 252 + inv**8 / 240
            - inv**10 / 132)


def original_symbol(p):
    return (digamma_positive((p + .5) / 2) - math.log(math.pi)
            + 2 / (p + .5) + 2 / (p - .5))


def original_log_transfer(p, omega):
    return (omega * math.log(math.pi)
            + math.lgamma((p + .5 - omega) / 2)
            - math.lgamma((p + .5 + omega) / 2)
            + math.log((p + .5 - omega) / (p + .5 + omega))
            + math.log((p - .5 - omega) / (p - .5 + omega)))


def reduced_log_transfer(p, omega):
    return (omega * math.log(math.pi)
            + math.lgamma((p + 2.5 - omega) / 2)
            - math.lgamma((p + 2.5 + omega) / 2)
            + math.log((p - .5 - omega) / (p - .5 + omega)))


def bulge_pair(r, s, eta, order=48):
    """B_eta and its analytic eta derivative; two corner-resolving triangles."""
    value = derivative = 0.
    nodes = gauss_legendre(order)
    for v, wv in nodes:
        for z, wz in nodes:
            base = r * s * v * z * (2 - 3 * v) * (2 - 3 * v * z)
            a1, a2 = (r + s * z)**2, (r * z + s)**2
            b1 = v**2 * (r * (1 - v) - s * z*z * (1 - v*z))**2
            b2 = v**2 * (r * z*z * (1 - v*z) - s * (1 - v))**2
            d1, d2 = a1 + eta*eta*b1, a2 + eta*eta*b2
            value += wv*wz * 2*eta*eta * base * (1/d1 + 1/d2)
            derivative += wv*wz * 4*eta * base * (a1/d1**2 + a2/d2**2)
    return value, derivative


def main():
    cases = []

    def check(name, value, threshold):
        cases.append(dict(name=name, value=value, threshold=threshold,
                          comparison='<=', passed=math.isfinite(value) and value <= threshold))

    nodes = gauss_legendre(192, 0, 60)
    for p in (1.3, 2., 5.):
        integral = W0 + sum(w * 2*tower(u)*(-math.expm1(-p*u)) for u, w in nodes)
        integral += 2/(p+.5) + 2/(p-.5)
        check(f'original generator versus subtracted integral p={p}',
              abs(original_symbol(p) - integral), 3e-11)
        reduced = digamma_positive((p+2.5)/2) - math.log(math.pi) + 2/(p-.5)
        check(f'lowest-mode pole cancellation p={p}', abs(original_symbol(p)-reduced), 2e-13)
        delta = 1e-4
        derivative = -(original_log_transfer(p, delta)-original_log_transfer(p, -delta))/(2*delta)
        check(f'finite-shift derivative matches full generator p={p}',
              abs(derivative-original_symbol(p)), 3e-8)
        for omega in (.1, .4):
            check(f'finite-shift rational absorption p={p} omega={omega}',
                  abs(original_log_transfer(p, omega)-reduced_log_transfer(p, omega)), 5e-14)

    for epsilon in (1e-3, 1e-5, 1e-7):
        contact = -W0-tail(epsilon)
        check(f'fixed contact finite part epsilon={epsilon}',
              abs(contact-math.log(epsilon)-EULER-math.log(2*math.pi)), .501*epsilon)

    for u in (.01, .1, .3, .6):
        full = 2*tower(u)-4*math.cosh(u/2)
        reduced = 2*math.exp(-2*u)*tower(u)-2*math.exp(u/2)
        check(f'full off-diagonal response and cancelled tower u={u}', abs(full-reduced), 5e-13)
    lo, hi = 1., 2.
    for _ in range(60):
        midpoint = (lo+hi)/2
        if midpoint**3-midpoint-1 > 0:
            hi = midpoint
        else:
            lo = midpoint
    u_star = math.log((lo+hi)/2)
    check('off-diagonal sign-change root', abs(2*tower(u_star)-4*math.cosh(u_star/2)), 1e-13)
    check('pole-corrected response is negative at delay 0.6', 2*tower(.6)-4*math.cosh(.3), -1.)

    bulges = []
    eta = .3
    for r, s in ((1., 1.), (math.exp(-.25), math.exp(.25))):
        value, derivative = bulge_pair(r, s, eta, 64)
        coarse = bulge_pair(r, s, eta, 32)
        step = 1e-5
        finite_difference = (bulge_pair(r, s, eta+step)[0]-bulge_pair(r, s, eta-step)[0])/(2*step)
        check(f'Gaussian response quadrature refinement r={r} s={s}',
              max(abs(value-coarse[0]), abs(derivative-coarse[1])), 3e-12)
        check(f'Gaussian response analytic insertion versus finite difference r={r} s={s}',
              abs(derivative-finite_difference), 3e-10)
        check(f'Gaussian response derivative bound r={r} s={s}', abs(derivative), 4*eta)
        bulges.append(dict(r=r, s=s, eta=eta, response=value, derivative=derivative))
    check('equal-radius reduction to existing bulge calculation',
          abs(bulges[0]['response']-bulk_response(eta, eta, 64)), 1e-14)

    result = dict(schema_version=1, description=__doc__.strip(),
                  parameters=dict(window_length=.5, laplace_points=[1.3, 2., 5.],
                                  shifts=[.1, .4], bulge_height=eta,
                                  gaussian_quadrature_orders=[32, 64], arithmetic_quadrature_order=192,
                                  arithmetic_integral_cutoff=60,
                                  precision='Python binary64; diagnostics, not rigorous enclosures'),
                  local_constant=W0, contact_finite_part=EULER+math.log(2*math.pi),
                  off_diagonal_zero=u_star, bulge_responses=bulges,
                  case_count=len(cases), all_pass=all(c['passed'] for c in cases), cases=cases)
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(not result['all_pass'])


if __name__ == '__main__':
    main()
