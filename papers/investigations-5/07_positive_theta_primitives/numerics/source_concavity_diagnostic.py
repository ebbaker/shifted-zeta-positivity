"""Exact algebra for Note03's diagnostic, 2026-11-01.

Prepared for Edward Baker with substantial LLM assistance.
Actual recorded model gpt-6-astra; reasoning effort xhigh.
This verifies finite identities, not RH or the analytic Rouche argument.
"""
from collections import defaultdict
from fractions import Fraction as F
import json

def add(a, b):
    c = defaultdict(F, a)
    for k, v in b.items():
        c[k] += v
    return {k: v for k, v in c.items() if v}

def scale(a, factor):
    return {k: v * factor for k, v in a.items() if v * factor}

def mul(a, b):
    c = defaultdict(F)
    for (i, j), v in a.items():
        for (k, ell), w in b.items():
            c[i + k, j + ell] += v * w
    return {k: v for k, v in c.items() if v}

def derivative(a):
    return {(i - 1, j): i * v for (i, j), v in a.items() if i}

def laguerre(a):
    return add(mul(derivative(a), derivative(a)),
               scale(mul(a, derivative(derivative(a))), -1))

P = {(0, 0): F(17), (1, 0): F(6), (2, 0): F(1)}
Q = {(0, 0): F(1), (1, 0): F(6), (2, 0): F(1)}
eps = {(0, 1): F(1)}
one = {(0, 0): F(1)}
assert laguerre(P) == scale(Q, 2)
assert laguerre(Q) == scale(P, 2)
R = add(scale(Q, 2), scale(mul(eps, mul(P, P)), 2))
N = add(laguerre(R), scale(mul(eps, mul(R, R)), 4))
P2, eps2 = mul(P, P), mul(eps, eps)
expected = add(add(scale(P, 8), scale(mul(eps, P2), 24)),
               add(scale(mul(eps2, mul(P2, Q)), 48),
                   scale(mul(mul(eps2, eps), mul(P2, P2)), 16)))
assert N == expected
assert all(v > 0 for v in N.values())

# d^k/dz^k exp(-z^2/4) = exp(-z^2/4) g_k(z).
g = [one]
for k in range(4):
    g.append(add(derivative(g[-1]), mul({(1, 0): F(-1, 2)}, g[-1])))
fourier = add(add(scale(g[0], 17), scale(g[2], -6)), g[4])
assert fourier == {(0, 0): F(332, 16), (2, 0): F(-36, 16), (4, 0): F(1, 16)}
assert 36 ** 2 - 4 * 332 == -32

print(json.dumps(dict(date='2026-11-01', prepared_for='Edward Baker',
    model='gpt-6-astra', effort='xhigh', arithmetic='exact rational polynomial arithmetic',
    checks={'L_P_equals_2Q': True, 'L_Q_equals_2P': True,
            'Gaussian_Fourier_polynomial': True,
            'nonreal_quartic_roots_by_discriminant': True,
            'superGaussian_second_iterate_factorization': True},
    scope='Finite algebra only. The all-iterate Gaussian formula follows by induction; admissible small-epsilon nonreal zeros follow from local uniform convergence and Rouche as proved in Note03. No explicit epsilon threshold, all-iterate positive-epsilon claim, theta criterion, or RH evidence.'), indent=2))
