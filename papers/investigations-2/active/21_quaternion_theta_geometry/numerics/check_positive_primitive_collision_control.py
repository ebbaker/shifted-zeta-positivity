#!/usr/bin/env python3
"""Exact algebra checks for Note 56; no floating-point sign pilot.
Prepared for Edward Baker, 2026-10-15, with substantial LLM assistance.
Coordinating model gpt-6-astra; effort ultra (parent-session metadata).
"""
from fractions import Fraction as F
from math import factorial
import hashlib
import json
from pathlib import Path


def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, F(0)) + v
    return {k: v for k, v in r.items() if v}


def pscale(p, c):
    return {k: c*v for k, v in p.items() if c*v}


def pmul(p, q):
    r = {}
    for k, v in p.items():
        for l, w in q.items():
            m = tuple(a+b for a, b in zip(k, l))
            r[m] = r.get(m, F(0)) + v*w
    return {k: v for k, v in r.items() if v}


def pdiff(p, idx):
    r = {}
    for k, v in p.items():
        if k[idx]:
            l = list(k)
            l[idx] -= 1
            r[tuple(l)] = v*k[idx]
    return r


def qadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def qmul(a, b):
    return (a[0]*b[0]+10*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def qscale(a, c):
    return (a[0]*c, a[1]*c)


def qpow(a, n):
    r = (F(1), F(0))
    for _ in range(n):
        r = qmul(r, a)
    return r


def poly_at(p, a):
    r = (F(0), F(0))
    for (k,), v in p.items():
        r = qadd(r, qscale(qpow(a, k), v))
    return r


checks = {}
# Coefficients of P_a(y) in ascending y degree, themselves polynomials in a.
p0 = {(4,): F(16), (3,): F(8), (2,): F(6)}
p1 = {(2,): F(-4), (1,): F(-6)}
p2 = {(0,): F(1, 2)}
disc = padd(pmul(p1, p1), pscale(pmul(p2, p0), F(-4)))
assert disc == {(4,): F(-16), (3,): F(32), (2,): F(24)}
checks['gaussian_discriminant'] = True

# Arithmetic in Q(sqrt(10)), stored as pairs (rational, sqrt coefficient).
a = (F(1), F(1, 2))
T = qadd((F(3), F(0)), qscale(a, -1))
y = qadd(qscale(qpow(a, 2), 4), qscale(a, 6))
assert T == (F(2), F(-1, 2))
assert y == (F(20), F(7))
assert poly_at(disc, a) == (0, 0)
assert poly_at(p1, a) == qscale(y, -1)
assert poly_at(p0, a) == qscale(qmul(y, y), F(1, 2))
# 3 < sqrt(10) < 4 proves 0 < T < 1/2 exactly.
assert 3**2 < 10 < 4**2
checks['collision_time_and_square_factorization'] = True
# For P(x^2)=x^4/2-y_c*x^2+y_c^2/2, P''(x_c)=4*y_c.
assert qadd(qscale(y, 6), qscale(y, -2)) == qscale(y, 4)
checks['positive_double_zero_coefficient'] = True

# F=e^(t*u^2) cos(x*u). Polynomial pairs are cos/sin coefficients,
# with variable order (u,t,x). Differentiate the pair after removing e^(t*u^2).
one = {(0, 0, 0): F(1)}
zero = {}
x = {(0, 0, 1): F(1)}
two_tu = {(1, 1, 0): F(2)}

def heat_derivative(pair):
    c, s = pair
    return (padd(padd(pdiff(c, 0), pmul(two_tu, c)), pmul(x, s)),
            padd(padd(pdiff(s, 0), pmul(two_tu, s)), pscale(pmul(x, c), -1)))

c2, s2 = heat_derivative(heat_derivative((one, zero)))
assert c2 == {(0, 1, 0): F(2), (2, 2, 0): F(4), (0, 0, 2): F(-1)}
assert s2 == {(1, 1, 1): F(-4)}
assert padd(c2, pscale(one, -1)) == {
    (0, 1, 0): F(2), (2, 2, 0): F(4), (0, 0, 2): F(-1), (0, 0, 0): F(-1)}
checks['reconstruction_integrand_coefficients'] = True

# Q Q'' -(Q')^2 = -v-v^2/2, and Q-Q'=v^2/2.
Q = {(0,): F(1), (1,): F(1), (2,): F(1, 2)}
Q1, Q2 = pdiff(Q, 0), pdiff(pdiff(Q, 0), 0)
assert padd(pmul(Q, Q2), pscale(pmul(Q1, Q1), -1)) == {(1,): F(-1), (2,): F(-1, 2)}
assert padd(Q, pscale(Q1, -1)) == {(2,): F(1, 2)}
checks['square_source_log_concavity_and_slope'] = True

# From uK <= phi/4+psi/32, the term 4tu psi'=-32tuK
# contributes at worst -8t phi -t psi. Remaining terms give (10).
assert -32*F(1, 4) == -8
assert -32*F(1, 32) == -1
assert F(2)-1 == 1
# At t in [0,1/2], 8(1-t)>=4 and 1+t+4t^2u^2>=1.
assert 8*(1-F(1, 2)) == 4
# Boundary normalization: -8*(1/16)=-1/2.
assert -8*F(1, 16) == -F(1, 2)
checks['convexity_constants_and_boundary_normalization'] = True

endpoint_polynomials = []
for k in range(7):
    coeff = [F(factorial(2*k+1), factorial(j)*factorial(2*k+1-2*j))
             for j in range(k+1)]
    assert all(c.denominator == 1 for c in coeff)
    endpoint_polynomials.append([int(c) for c in coeff])
assert endpoint_polynomials[:4] == [[1], [1, 6], [1, 20, 60], [1, 42, 420, 840]]
checks['universal_endpoint_polynomials_through_order_13'] = True

record = {
    'date': '2026-10-15',
    'title': 'Positive primitive collision control: exact algebra checks',
    'author': 'Prepared for Edward Baker',
    'assistance': 'Substantial LLM assistance',
    'coordinating_model': 'gpt-6-astra',
    'reasoning_effort': 'ultra',
    'model_provenance': 'Verified by coordinating agent from parent session metadata',
    'arithmetic': 'Python standard-library Fraction; no floating-point operations',
    'status': 'PASS',
    'checks': checks,
    'endpoint_polynomial_coefficients_ascending_t': endpoint_polynomials,
    'limitations': [
        'This checks algebra, not a sampled or certified theta sign domain.',
        'Existence of a sufficiently small positive damping parameter is analytic; no explicit cutoff is certified.',
        'Decay, strict transform positivity, persistence, and the stationary pole rely on the proofs in Note 56.'
    ],
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
print(json.dumps(record, indent=2))
