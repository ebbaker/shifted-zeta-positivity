#!/usr/bin/env python3
"""Exact fourth-order Schur error jets and conditional threshold geometry.

The controls are local real holomorphic jets, not prescribed arithmetic
states. General analytic proofs are in Heat Note 19. Only Fraction
arithmetic enters assertions; the program prints a small deterministic
record and does not write files.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json

DEGREE = 4
checks = 0


def check(condition):
    global checks
    assert condition, checks + 1
    checks += 1


def mul(a, b, order=DEGREE):
    out = [F(0)]*(order+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= order:
                out[i+j] += x*y
    return out


def divide(a, b, order=DEGREE):
    assert b[0]
    out = [F(0)]*(order+1)
    for i in range(order+1):
        value = a[i] if i < len(a) else F(0)
        value -= sum((b[j]*out[i-j] for j in range(1, min(i+1, len(b)))), F(0))
        out[i] = value/b[0]
    return out


def schur_series(parameters):
    """Independent truncated rational composition of disk maps."""
    h = [F(0)]*(DEGREE+1)
    for s in reversed(parameters):
        if abs(s) == 1:
            h = [s]+[F(0)]*DEGREE
        else:
            numerator = [s]+h[:DEGREE]
            denominator = [F(1)]+[s*x for x in h[:DEGREE]]
            h = divide(numerator, denominator)
    return h


def schur_closed(parameters):
    a, lam, mu, r, s = parameters
    D, E, H, J = (1-a*a), (1-lam*lam), (1-mu*mu), (1-r*r)
    b0 = lam
    b1 = E*mu
    b2 = E*(H*r-lam*mu*mu)
    b3 = E*(H*(J*s-mu*r*r)-2*lam*mu*H*r+lam*lam*mu**3)
    return [a, D*b0, D*(b1-a*b0*b0),
            D*(b2-2*a*b0*b1+a*a*b0**3),
            D*(b3-a*(2*b0*b2+b1*b1)+3*a*a*b0*b0*b1-a**3*b0**4)]


def recover_parameters(coefficients):
    """Invert finite real Schur steps, terminating at a constant boundary."""
    current = coefficients[:]
    out = []
    while current:
        s = current[0]
        assert abs(s) <= 1
        out.append(s)
        if abs(s) == 1:
            assert all(x == 0 for x in current[1:])
            break
        if len(current) == 1:
            break
        denominator = [1-s*s]+[-s*x for x in current[1:]]
        current = divide(current[1:], denominator, len(current)-2)
    return out


def cmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def cdivide(a, b):
    norm = b[0]*b[0]+b[1]*b[1]
    assert norm > 0
    numerator = cmul(a, (b[0], -b[1]))
    return (numerator[0]/norm, numerator[1]/norm)


def disk_map(parameters, z):
    h = (F(0), F(0))
    for s in reversed(parameters):
        if abs(s) == 1:
            h = (s, F(0))
        else:
            zh = cmul(z, h)
            h = cdivide((s+zh[0], zh[1]), (1+s*zh[0], s*zh[1]))
    return h


def jets(parameters, finite, L=F(1), eta=F(1)):
    alpha = schur_closed(parameters)
    return [finite[j]+factorial(j)*L**j*eta*alpha[j] for j in range(5)]


def threshold(q, gamma):
    return 2*q[3]**2-3*q[2]*q[4]-gamma*q[2]**2


def quadratic_max(c0, c1, c2):
    options = [(c0-c1+c2, F(-1)), (c0+c1+c2, F(1))]
    if c2 < 0:
        vertex = -c1/(2*c2)
        if abs(vertex) <= 1:
            options.append((c0+c1*vertex+c2*vertex*vertex, vertex))
    return max(options)


def threshold_r_max(a, lam, mu, finite, L, eta, gamma):
    """Exact maximization over the last two free Schur parameters."""
    qminus = jets((a, lam, mu, F(-1), F(0)), finite, L, eta)
    qzero = jets((a, lam, mu, F(0), F(0)), finite, L, eta)
    qplus = jets((a, lam, mu, F(1), F(0)), finite, L, eta)
    q2 = qzero[2]
    A3, B3 = qzero[3], (qplus[3]-qminus[3])/2
    A4 = qzero[4]
    B4 = (qplus[4]-qminus[4])/2
    C4 = (qplus[4]+qminus[4])/2-A4
    R = (1-a*a)*(1-lam*lam)*(1-mu*mu)
    K = 72*L**4*eta*R*abs(q2)
    c0 = 2*A3*A3-3*q2*A4-gamma*q2*q2+K
    c1 = 4*A3*B3-3*q2*B4
    c2 = 2*B3*B3-3*q2*C4-K
    maximum, r = quadratic_max(c0, c1, c2)
    s = -((q2 > 0)-(q2 < 0))
    return maximum, r, F(s), (c0, c1, c2)


def run():
    grid = (F(-1), F(-1, 2), F(0), F(1, 3), F(1))
    for params in product(grid, repeat=5):
        alpha = schur_closed(params)
        check(alpha == schur_series(params))
        recovered = recover_parameters(alpha)
        check(recovered == list(params[:len(recovered)]))
        check(all(abs(v) <= 1 for v in alpha))
        check(alpha[0]**2+abs(alpha[1]) <= 1)
        for z in ((F(0), F(0)), (F(1, 3), F(1, 4))):
            value = disk_map(params, z)
            check(value[0]**2+value[1]**2 <= 1)
        D = 1-params[0]**2
        if D:
            lam = params[1]
            check(abs(alpha[2]) <= D*(1-(1-abs(params[0]))*lam*lam))

    # General exact last-parameter elimination and quadratic maximization.
    tested_maxima = 0
    for a, lam, mu in product((F(-1), F(-1, 2), F(0), F(2, 3), F(1)), repeat=3):
        L, eta, gamma = F(3, 2), F(2, 7), F(-1, 11)
        finite = [-eta*a, -L*eta*(1-a*a)*lam, F(3, 5), F(-2, 3), F(7, 4)]
        maximum, rstar, sstar, coefficients = threshold_r_max(a, lam, mu, finite, L, eta, gamma)
        check(threshold(jets((a, lam, mu, rstar, sstar), finite, L, eta), gamma) == maximum)
        for r, s in product(grid, repeat=2):
            q = jets((a, lam, mu, r, s), finite, L, eta)
            check(q[0] == q[1] == 0)
            check(threshold(q, gamma) <= maximum)
            qend = jets((a, lam, mu, r, sstar), finite, L, eta)
            c0, c1, c2 = coefficients
            check(threshold(qend, gamma) == c0+c1*r+c2*r*r)
        tested_maxima += 1

    # A control where the sharp analytic error body changes exclusion sign.
    for mu, r, s in product((F(n, 8) for n in range(-8, 9)), repeat=3):
        finite = [F(0), F(0), F(3), F(0), F(25)]
        q = jets((F(0), F(0), mu, r, s), finite)
        check(threshold(q, F(0)) <= -3)
        for gamma in (F(-1, 10), F(1, 10)):
            check(threshold(q, gamma) <= F(-1, 2))
        qend = jets((F(0), F(0), mu, r, F(-1)), finite)
        expression = -3*(3+2*mu)*(1+24*mu*mu)+72*(1-mu*mu)*(1-mu)*(-2-mu)*r*r
        check(threshold(qend, F(0)) == expression)
    box_witness = [F(0), F(0), F(1), F(6), F(1)]
    check(threshold(box_witness, F(0)) == 69)
    independent_payment = 2*6**2+3*(3*24+25*2+2*24)
    check(threshold([0, 0, 3, 0, 25], F(0))+independent_payment == 357)

    # A compatible ordinary double zero with strictly positive threshold.
    positive = jets((F(0), F(0), F(1, 2), F(0), F(-1)), [F(0)]*5)
    check(positive == [0, 0, 1, 0, -18])
    check(threshold(positive, F(0)) == 54)
    # Sharp zero-finite-jet upper range and a rational lower-range identity.
    for mu, r, s in product(grid, repeat=3):
        q = jets((F(0), F(0), mu, r, s), [F(0)]*5)
        value = 72*(1-mu*mu)*((1+mu*mu)*r*r-2*mu*(1-r*r)*s)
        check(threshold(q, F(0)) == value)
        check(value <= 72)
        check(value >= -144*abs(mu)*(1-mu*mu))
    check(threshold(jets((F(0), F(0), F(0), F(1), F(0)), [F(0)]*5), F(0)) == 72)

    return {
        'status': 'PASS',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'assertions_passed': checks,
        'full_five_parameter_schur_controls': 5**5,
        'exact_last_two_parameter_maxima_checked': tested_maxima,
        'families': [
            'fourth-order explicit Schur coefficients versus rational composition and inverse recovery',
            'boundary termination, bounded rational disk maps and conditional second-error norm',
            'last Schur parameter support and exact quadratic next-parameter maximum',
            'strict negative finite-jet control admitted by independent Cauchy upper bounds',
            'ordinary-double positive control and sharp zero-finite-jet threshold range',
        ],
        'negative_control': {
            'finite_physical_jets_units_L_eta_1': [0, 0, 3, 0, 25],
            'gamma_0_schur_threshold_upper': '-3',
            'abs_gamma_at_most_1_over_10_threshold_upper': '-1/2',
            'independent_cauchy_box_admitted_threshold': '69',
            'previous_absolute_payment_upper': '357',
        },
        'positive_ordinary_double_control': {'schur_parameters': ['0', '0', '1/2', '0', '-1'], 'q2_q3_q4_units_L_eta_1': ['1', '0', '-18'], 'gamma_0_threshold': '54'},
        'zero_finite_jet_sharp_range_gamma_0': ['-32*sqrt(3)', '72'],
        'scope': 'Exact local bounded-holomorphic error geometry and formal finite-jet controls. No genuine prescribed-coefficient threshold sign, uniform collision exclusion, or RH assertion.',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
