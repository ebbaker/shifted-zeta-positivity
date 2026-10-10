#!/usr/bin/env python3
"""Exact Gaussian derivative algebra and finite coherent-observation replay."""
from fractions import Fraction as F
import cmath
import json
import math


def add(p, q):
    out = p.copy()
    for k, value in q.items():
        out[k] = out.get(k, F(0))+value
    return {k: v for k, v in out.items() if v}


def derivative(p):
    return {k-1: k*v for k, v in p.items() if k}


def mul(p, q):
    out = {}
    for i, x in p.items():
        for j, y in q.items():
            out[i+j] = out.get(i+j, F(0))+x*y
    return {k: v for k, v in out.items() if v}


a_exact = F(3, 10)
p = {0: F(1)}
polynomials = [p]
for _ in range(4):
    p = add(derivative(p), mul({1: 2*a_exact}, p))
    polynomials.append(p)
assert polynomials[1] == {1: 2*a_exact}
assert polynomials[2] == {0: 2*a_exact, 2: 4*a_exact**2}
assert polynomials[3] == {1: 12*a_exact**2, 3: 8*a_exact**3}
assert polynomials[4] == {0: 12*a_exact**2, 2: 48*a_exact**3, 4: 16*a_exact**4}

a, b, c, time = 0.3, 1/(16*0.3), 1.3, 0.1


def husimi(u, p, t):
    kappa = c-t
    A = kappa/(1+4*a*kappa)
    B = 1/(kappa+4*b)
    value = math.exp(-A*u*u-B*p*p)/(math.sqrt(math.pi)
             * math.sqrt(1+4*a*kappa)*math.sqrt(kappa+4*b))
    return value, A, B


generator_errors = []
for u, p in ((0.0, 0.0), (0.2, -0.4), (1.0, 0.5), (-1.3, 1.2)):
    value, A, B = husimi(u, p, time)
    du = -2*A*u*value
    duu = (4*A*A*u*u-2*A)*value
    dpp = (4*B*B*p*p-2*B)*value
    generator = u*u*value+4*a*u*du+2*a*value+4*a*a*duu-dpp/4
    epsilon = 1e-6
    numerical = (husimi(u, p, time+epsilon)[0]
                 -husimi(u, p, time-epsilon)[0])/(2*epsilon)
    generator_errors.append(abs(generator-numerical))
assert max(generator_errors) < 2e-10

weights = [1.1, 0.7, 0.2]
phases = [0.3, -1.2, 2.1]
alpha = [-0.2, 0.1, 0.05]
beta = [0.5, -0.7, 1.3]
q = [w*cmath.exp(1j*p) for w, p in zip(weights, phases)]
v = q+[z.conjugate() for z in q]
l0 = [1.0]*len(v)
l1half = [A+1j*B for A, B in zip(alpha, beta)]
l1 = l1half+[z.conjugate() for z in l1half]
F0 = sum(z for z in q)*2
expected_value = F0.real
expected_derivative = 2*sum(z*k for z, k in zip(q, l1half)).real
actual_value = sum(z*k for z, k in zip(v, l0))
actual_derivative = sum(z*k for z, k in zip(v, l1))
assert abs(actual_value-expected_value) < 1e-14
assert abs(actual_derivative-expected_derivative) < 1e-14
density = [[x*y.conjugate() for y in v] for x in v]


def observed_square(row):
    return sum(row[i]*density[i][j]*row[j].conjugate()
               for i in range(len(v)) for j in range(len(v)))


assert abs(observed_square(l0)-expected_value**2) < 1e-13
assert abs(observed_square(l1)-expected_derivative**2) < 1e-13

# A generic coherent control: two equal contributions differing by pi.
control = [1.0+0j, -1.0+0j]
assert abs(sum(control)) == 0
print(json.dumps({
    "status": "PASS",
    "scope": "exact rational jet polynomial checks and floating-point Gaussian/coherent replay; not a theta sign certificate",
    "a": a, "b": b,
    "jet_polynomials": [{str(k): str(v) for k, v in p.items()} for p in polynomials],
    "husimi_generator_finite_difference_errors": generator_errors,
    "finite_doubled_value_error": abs(actual_value-expected_value),
    "finite_doubled_derivative_error": abs(actual_derivative-expected_derivative),
    "positive_density_observation_control": "nonzero rank-one positive matrix, zero coherent sum",
}, indent=2))
