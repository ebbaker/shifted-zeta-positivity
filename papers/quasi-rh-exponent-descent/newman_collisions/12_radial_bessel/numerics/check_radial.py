#!/usr/bin/env python3
"""Exact polynomial checks and exploratory theta replay; no interval certificate."""
from fractions import Fraction as F
import json
import math


def poly_add(p, q):
    n = max(len(p), len(q))
    return [(p[k] if k < len(p) else 0)+(q[k] if k < len(q) else 0)
            for k in range(n)]


def derivative(p):
    return [(k+1)*p[k+1] for k in range(len(p)-1)]


def exp_bounds(x, terms=80):
    """Rational Taylor enclosure, x>=0, subsequent term ratios geometric."""
    x = F(x)
    assert x >= 0 and terms+2 > x
    term, lower = F(1), F(1)
    for k in range(1, terms+1):
        term *= x/k
        lower += term
    next_term = term*x/(terms+1)
    upper = lower+next_term/(1-x/(terms+2))
    return lower, upper


def theta_derivative_polynomial(p):
    # d/dr [exp(r-a)*p(a)] with da/dr=4a.
    return poly_add(p, [0]+[4*x for x in poly_add(derivative(p), [-x for x in p])])


p0 = [0, -3, 2]
p1 = theta_derivative_polynomial(p0)
p2 = theta_derivative_polynomial(p1)
assert p1 == [0, -15, 30, -8]
assert p2 == [0, -75, 330, -224, 32]
q = lambda a: 32*a**3-224*a*a+330*a-75
qp = lambda a: 96*a*a-448*a+330
amin, amax = F(157, 50), F(82, 25)
assert q(amin) < -250
assert qp(amin) < 0 and qp(amax) < 0
a = F(2041, 625)  # 3.14*(1+0.04) exactly.
log_decay = (8*a*a-30*a+15)/(2*a-3)
assert log_decay > F(3, 5)
e3_lower, _ = exp_bounds(3)
e12_lower, _ = exp_bounds(12)
e15_lower, _ = exp_bounds(15)
_, e328_upper = exp_bounds(F(82, 25))
_, e004_upper = exp_bounds(F(1, 25))
assert e3_lower > 20
assert 1/e12_lower < F(123, 20000000)
ratio8_upper = F(3, 2)**8/e15_lower
ratio4_upper = F(3, 2)**4/e15_lower
assert ratio8_upper < F(8, 1000000)
assert ratio4_upper < F(2, 1000000)
assert e328_upper < 27
assert F(22, 7)*e004_upper < F(82, 25)
first_tail_upper = (32*(3*4)**4+330*(3*4)**2)/e12_lower
full_tail_upper = first_tail_upper/(1-ratio8_upper)
assert full_tail_upper < F(9, 2)
phi0_certified_upper = 2*F(22, 7)**2*(F(1, 20)+F(1, 10000)/(1-ratio4_upper))
assert phi0_certified_upper < 1
tail = sum((32*(3*n*n)**4+330*(3*n*n)**2)*math.exp(-3*n*n)
           for n in range(2, 20))
assert tail < 4.4
assert (1.5)**8*math.exp(-15) < 8e-6
phi0_upper = 2*(22/7)**2*sum(n**4*math.exp(-3*n*n) for n in range(1, 20))
assert phi0_upper < 1 and math.exp(3.28) < 27


def values(r):
    phi = phip = phipp = 0.0
    for n in range(1, 12):
        a = math.pi*n*n*math.exp(4*r)
        factor = math.exp(r-a)
        phi += factor*(2*a*a-3*a)
        phip += factor*(-8*a**3+30*a*a-15*a)
        phipp += factor*(32*a**4-224*a**3+330*a*a-75*a)
    return phi, phip, phipp


phi0, phip0, phipp0 = values(0)
assert abs(phip0) < 2e-14
center = -(phipp0+0.1*phi0)/(2*math.pi)
assert center > 0
positivity_samples = []
for r in (0.0001, 0.001, 0.01, 0.1, 0.25, 0.5, 0.75, 1.0):
    phi, phip, _ = values(r)
    decay_margin = -phip/phi-0.1*r
    assert decay_margin > 0
    positivity_samples.append({"r": r, "log_decay_margin_at_t_0.05": decay_margin})

print(json.dumps({
    "status": "PASS",
    "scope": "polynomial and Taylor/geometric certificate bounds exact rational; sampled theta values floating point",
    "p1": p1, "p2": p2,
    "rational_q_at_3.14": str(q(amin)),
    "rational_log_decay_lower": str(log_decay),
    "exact_transcendental_and_tail_bounds": "PASS: Taylor/geometric rational enclosures verify all constants in the small-radius positivity proof",
    "full_tail_rational_upper_float_display": float(full_tail_upper),
    "Phi0_rational_upper_float_display": float(phi0_certified_upper),
    "tail_first_18_terms": tail,
    "Phi0_crude_upper_partial_sum": phi0_upper,
    "Phi0_exploratory": phi0,
    "Phi_prime_0_exploratory": phip0,
    "Phi_second_0_exploratory": phipp0,
    "R_center_t_0.05_exploratory": center,
    "positivity_samples": positivity_samples,
}, indent=2))
