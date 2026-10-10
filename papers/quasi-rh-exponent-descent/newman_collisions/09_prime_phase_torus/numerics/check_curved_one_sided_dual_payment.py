#!/usr/bin/env python3
"""Certify sharp one-sided quadratic dual payments on s^2+|v|<=1.

Exact rational polynomial arithmetic and cubic root isolation. Controls
verify paid algebra; they are not actual huge-height collision states.
"""
import argparse
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

checks = 0
root_intervals = 0
WIDTH = F(1, 2**72)


def check(condition):
    global checks
    assert condition, f'Assertion {checks + 1} failed'
    checks += 1


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def peval(p, x):
    out = F(0)
    for a in reversed(p):
        out = out*x + a
    return out


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))])


def divide(p, q):
    p, q = trim(p), trim(q)
    assert q
    quot = [F(0)]*max(0, len(p) - len(q) + 1)
    while p and len(p) >= len(q):
        d, factor = len(p) - len(q), p[-1]/q[-1]
        quot[d] = factor
        for i, a in enumerate(q):
            p[d + i] -= factor*a
        p = trim(p)
    return trim(quot), p


def pgcd(p, q):
    while q:
        _, r = divide(p, q)
        p, q = q, r
    return [a/p[-1] for a in p] if p else []


def square_free(p):
    p = trim(p)
    if len(p) < 2:
        return p
    g = pgcd(p, derivative(p))
    quotient, remainder = divide(p, g)
    assert not remainder
    return quotient


def sturm(p):
    chain = [trim(p), derivative(p)]
    if not chain[1]:
        return chain[:1]
    while True:
        _, rem = divide(chain[-2], chain[-1])
        if not rem:
            return chain
        chain.append([-a for a in rem])


def variations(chain, x):
    signs = [(v > 0) - (v < 0) for p in chain if (v := peval(p, x))]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def isolate(p):
    """Exact enclosures of all distinct roots strictly in (-1,1)."""
    p = square_free(p)
    if len(p) < 2:
        return []
    for endpoint in [F(-1), F(1)]:
        if peval(p, endpoint) == 0:
            p, rem = divide(p, [-endpoint, F(1)])
            assert not rem
    if len(p) < 2:
        return []
    chain = sturm(p)
    tasks = [(F(-1), F(1))]
    out = []
    while tasks:
        left, right = tasks.pop()
        count = variations(chain, left) - variations(chain, right)
        if count == 0:
            continue
        assert count > 0
        if count == 1 and right - left <= WIDTH:
            out.append((left, right))
            continue
        mid = (left + right)/2
        if peval(p, mid) == 0:
            # Deflate exactly, then restart: avoids evaluating a sign
            # variation at a root or keeping duplicated root intervals.
            smaller, rem = divide(p, [-mid, F(1)])
            assert not rem
            return sorted([(mid, mid)] + isolate(smaller))
        tasks.extend([(left, mid), (mid, right)])
    return sorted(out)


def imul(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def interval_eval(p, interval):
    out = (F(0), F(0))
    for a in reversed(p):
        lo, hi = imul(out, interval)
        out = lo + a, hi + a
    return out


def objective(h, k, r, l, m, s, v):
    return h*s*s + 2*k*s*v + r*v*v + 2*l*s + 2*m*v


def boundary(h, k, r, l, m, tau):
    return [r + 2*tau*m, 2*tau*k + 2*l,
            h - 2*r - 2*tau*m, -2*tau*k, r]


def payment(coefficients):
    """Enclose max(-q) exactly by the complete finite critical set."""
    global root_intervals
    h, k, r, l, m = coefficients
    values = [(F(0), F(0))]
    for tau in [-1, 1]:
        p = boundary(h, k, r, l, m, tau)
        for endpoint in [F(-1), F(1)]:
            value = peval(p, endpoint)
            values.append((value, value))
        roots = isolate(derivative(p))
        root_intervals += len(roots)
        for bracket in roots:
            values.append(interval_eval(p, bracket))
    det = h*r - k*k
    if det:
        s, v = (k*m - r*l)/det, (k*l - h*m)/det
        if s*s + abs(v) <= 1:
            value = objective(h, k, r, l, m, s, v)
            values.append((value, value))
    min_lo = min(value[0] for value in values)
    min_hi = min(value[1] for value in values)
    return max(F(0), -min_hi), max(F(0), -min_lo)


def transform(eta, L, A, c, lam, b, u):
    D = [[eta/2, F(0)], [A*eta/(2*c), -L*eta/(2*c)]]
    H = [[sum(D[i][j]*lam[i][k]*D[k][v] for i in range(2) for k in range(2))
          for v in range(2)] for j in range(2)]
    g = [sum(D[i][j]*b[i][k]*u[k] for i in range(2) for k in range(3))
         for j in range(2)]
    return [H[0][0], H[0][1], H[1][1], g[0], g[1]], D


def null_term(e, lam, b, u):
    return sum(e[i]*lam[i][j]*e[j] for i in range(2) for j in range(2)) + 2*sum(
        e[i]*b[i][j]*u[j] for i in range(2) for j in range(3))


def old_payment(eta, L, A, c, lam, b, u):
    a0, a1 = eta/2, (L + abs(A))*eta/(2*c)
    return (abs(lam[0][0])*a0*a0 + 2*abs(lam[0][1])*a0*a1 + abs(lam[1][1])*a1*a1
            + 2*sum((a0*abs(b[0][j]) + a1*abs(b[1][j]))*abs(u[j]) for j in range(3)))


def exact_target(coeff, target):
    interval = payment(list(map(F, coeff)))
    check(interval[0] <= target <= interval[1])
    check(interval[1] - interval[0] < F(1, 10**18))
    return interval


# Known sharp classes, including constant boundary polynomials and ridges.
for a, b in [(1, 1), (2, 5), (F(1, 3), F(7, 8))]:
    exact_target([a, 0, b, 0, 0], F(0))
    exact_target([-a, 0, -b, 0, 0], max(a, b))
exact_target([1, 0, -1, 0, 0], F(1))
exact_target([1, 1, 1, F(1, 2), F(1, 2)], F(1, 4))
exact_target([2, 0, 0, 0, 1], F(2))
exact_target([2, 0, 3, F(1, 5), F(-1, 7)], F(1, 50) + F(1, 147))
for l, m in [(F(1, 3), F(5, 7)), (F(-2), F(1, 5)), (F(3, 5), F(0))]:
    aa, bb = abs(2*l), abs(2*m)
    support = bb + aa*aa/(4*bb) if bb and aa <= 2*bb else aa
    exact_target([0, 0, 0, l, m], support)
cross_intervals = []
for beta in [F(1), F(-2, 3), F(5, 7)]:
    interval = payment([F(0), beta, F(0), F(0), F(0)])
    check(interval[0] >= 0)
    check(interval[0]**2 <= 16*beta*beta/27 <= interval[1]**2)
    check(interval[1] - interval[0] < F(1, 10**18))
    cross_intervals.append([str(x) for x in interval])

# Root isolator checks: rational roots, repeated roots, endpoints, no roots,
# and three irrational roots in the critical range.
for p, expected in [([0, -1, 0, 1], 1), ([F(-1, 8), F(3, 4), F(-3, 2), 1], 1),
                    ([1, 0, 1], 0), ([0, -F(3, 4), 0, 1], 3),
                    ([F(1, 2), 1], 1)]:
    roots = isolate(list(map(F, p)))
    check(len(roots) == expected)
    check(all(b - a <= WIDTH for a, b in roots))
    check(all(roots[i][1] < roots[i + 1][0] for i in range(len(roots) - 1)))
    for interval in roots:
        lo, hi = interval_eval(p, interval)
        check(lo <= 0 <= hi)

# Drift-containing candidate transform and exact old/new paid comparisons.
eta, L, c, d, mu = F(1, 11), F(19), F(1, 2), F(1, 101), F(3)
A = -d*mu
payments = []
for seed in range(1, 13):
    lam = [[F(seed - 6, 7), F(4 - seed, 11)],
           [F(4 - seed, 11), F(seed - 9, 13)]]
    b = [[F(seed*(i + 1) - 5*j, 17 + j) for j in range(3)] for i in range(2)]
    u = [F(seed - 5, 3), F(2*seed - 17, 5), F(7 - seed, 7)]
    coeff, D = transform(eta, L, A, c, lam, b, u)
    new = payment(coeff)
    old = old_payment(eta, L, A, c, lam, b, u)
    check(new[1] <= old)
    check(new[1] - new[0] < F(1, 10**17))
    for i in range(-8, 9):
        s = F(i, 8)
        for j in range(-4, 5):
            v = F(j, 4)*(1 - s*s)
            e = [D[0][0]*s + D[0][1]*v, D[1][0]*s + D[1][1]*v]
            check((2*e[0]/eta)**2 + 2*abs(A*e[0] - c*e[1])/(L*eta) <= 1)
            check(null_term(e, lam, b, u) == objective(*coeff, s, v))
            check(-null_term(e, lam, b, u) <= new[1])
    payments.append({'seed': seed, 'sharp_interval': [str(x) for x in new],
                     'old_rectangular_absolute_payment': str(old)})

# Joint interval moment payment: a linear objective in u attains its
# extrema at a common corner; correlated e is optimized at each corner.
lam = [[F(2), F(-1, 3)], [F(-1, 3), F(-2)]]
b = [[F(1), F(-2), F(1, 3)], [F(-1, 2), F(3, 5), F(2)]]
box = [(F(-1), F(2)), (F(-2), F(3)), (F(1, 5), F(4, 3))]
corner_payments = [payment(transform(eta, L, A, c, lam, b, list(u))[0])
                   for u in product(*box)]
joint = max(x[0] for x in corner_payments), max(x[1] for x in corner_payments)
for s in [F(-1), F(-2, 3), F(0), F(1, 3), F(1)]:
    for v in [-(1 - s*s), F(0), 1 - s*s]:
        _, D = transform(eta, L, A, c, lam, b, [F(0)]*3)
        e = [D[0][0]*s, D[1][0]*s + D[1][1]*v]
        for fractions in product([F(0), F(1, 2), F(1)], repeat=3):
            u = [a + fraction*(z - a) for (a, z), fraction in zip(box, fractions)]
            check(-null_term(e, lam, b, u) <= joint[1])
            corner_max = max(-null_term(e, lam, b, list(corner)) for corner in product(*box))
            check(-null_term(e, lam, b, u) <= corner_max)

# Outward application to irrational physical data can use rational
# coefficient intervals. All five coefficients are affine in the
# objective, so their independent interval-box payment needs 32 corners.
coefficient_box = [(F(-1), F(2)), (F(-2, 3), F(1, 2)),
                   (F(-3), F(1)), (F(-1, 5), F(2, 7)),
                   (F(-4, 9), F(1, 3))]
coefficient_payments = [payment(corner) for corner in product(*coefficient_box)]
coefficient_joint = (max(x[0] for x in coefficient_payments),
                     max(x[1] for x in coefficient_payments))
for s in [F(-1), F(-1, 2), F(0), F(2, 3), F(1)]:
    for v in [-(1 - s*s), F(0), 1 - s*s]:
        for fractions in product([F(0), F(1, 2), F(1)], repeat=5):
            coeff = [a + fraction*(z - a) for (a, z), fraction in zip(coefficient_box, fractions)]
            check(-objective(*coeff, s, v) <= coefficient_joint[1])

# All four signed channels at one common phase generator, with the same
# dual parameters. No phase-sum or sine term is removed by the new payment.
def cmul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def quad(a, q, b):
    return sum(a[i]*q[i][j]*b[j] for i in range(5) for j in range(5))


gamma, epsilon = F(1, 11), d/c
qmatrix = [[lam[0][0], lam[0][1], *b[0]], [lam[1][0], lam[1][1], *b[1]],
           [b[0][0], b[1][0], -gamma, 0, F(3, 2)],
           [b[0][1], b[1][1], 0, 2, 0],
           [b[0][2], b[1][2], F(3, 2), 0, 0]]
phases = [(F(5, 13), F(12, 13))]
for _ in range(5):
    phases.append(cmul(phases[-1], (F(3, 5), F(4, 5))))
rho = [F(k, 3) - mu for k in range(6)]
weights = [F(1, k + 1) for k in range(6)]
features = []
for r, (co, si) in zip(rho, phases):
    features.append([co, r*(si + epsilon*co), r*r*co, r**3*si, r**4*co])
total = F(0)
for n, rn in enumerate(rho):
    for m, rm in enumerate(rho):
        r, s = [1, epsilon*rn, rn**2, 0, rn**4], [0, rn, 0, rn**3, 0]
        rr, ss = [1, epsilon*rm, rm**2, 0, rm**4], [0, rm, 0, rm**3, 0]
        R, S, C, Ct = quad(r, qmatrix, rr), quad(s, qmatrix, ss), quad(r, qmatrix, ss), quad(s, qmatrix, rr)
        cn, sn = phases[n]
        cm, sm = phases[m]
        channels = ((R + S)*(cn*cm + sn*sm) + (Ct - C)*(sn*cm - cn*sm)
                    + (R - S)*(cn*cm - sn*sm) + (C + Ct)*(sn*cm + cn*sm))/2
        check(channels == quad(features[n], qmatrix, features[m]))
        total += weights[n]*weights[m]*channels
moment = [sum(weights[n]*features[n][i] for n in range(6)) for i in range(5)]
check(total == quad(moment, qmatrix, moment))
check(total == (2*moment[3]**2 + 3*moment[2]*moment[4] - gamma*moment[2]**2
                + null_term(moment[:2], lam, b, moment[2:])))

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, help='Write the small record to this path instead of its retained default.')
args = parser.parse_args()
source = Path(__file__).resolve()
target = args.output or source.with_name('curved_one_sided_dual_payment_record_20261010.json')
record = {
    'date': '2026-10-10', 'checker': source.name,
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'assertions_passed': checks,
    'root_bracket_width': str(WIDTH),
    'critical_root_intervals_evaluated': root_intervals,
    'families': ['Sharp known quadratic, linear, cross, singular-ridge and constant-edge payments',
                 'Exact square-free cubic isolation and rational interval evaluations',
                 'Amplitude-drift curved candidate transform and one-sided paid inequalities',
                 'Sharp joint interval moment payment by eight common corners',
                 'Rational outward coefficient-box payment by 32 common corners',
                 'Complete common-frequency four sine/cosine dual channels'],
    'cross_only_payment_intervals': cross_intervals,
    'drift_controls': payments,
    'joint_interval_moment_payment': [str(x) for x in joint],
    'joint_interval_coefficient_payment': [str(x) for x in coefficient_joint],
    'scope': 'Exact rational critical-set payment certificates and formal common-phase algebra. No prescribed arithmetic pair sign, actual candidate, heat collision, or independent mathematical validation.',
}
target.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({'record': target.name, 'assertions_passed': checks,
                  'critical_root_intervals_evaluated': root_intervals}, sort_keys=True))
