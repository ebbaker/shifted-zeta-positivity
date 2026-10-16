#!/usr/bin/env python3
"""Replay string transfer, determinant derivative, and Green identity."""
import cmath
import json
import math

c, ell = 1.0, 1.5


def transfer(length, lam):
    k = cmath.sqrt(c-lam)
    if abs(k) < 1e-14:
        return [[1+0j, length+0j], [0j, 1+0j]]
    C, S = cmath.cosh(k*length), cmath.sinh(k*length)
    return [[C, S/k], [k*S, C]]


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def determinant(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


maxdet, maxcomposition = 0.0, 0.0
for lam in (-2, 0, 1, 3, 1+2j):
    T = transfer(ell, lam)
    maxdet = max(maxdet, abs(determinant(T)-1))
    product = matmul(transfer(0.9, lam), transfer(0.6, lam))
    maxcomposition = max(maxcomposition,
                         max(abs(T[i][j]-product[i][j])
                             for i in range(2) for j in range(2)))
assert maxdet < 1e-12 and maxcomposition < 1e-12

lam = 0.2
k = math.sqrt(c-lam)
f0, f1 = 0.7, -0.3
v0p = k*(f1-f0*math.cosh(k*ell))/math.sinh(k*ell)
T = transfer(ell, lam)
v1p = (T[1][0]*f0+T[1][1]*v0p).real
boundary = f1*v1p-f0*v0p
panels = 400
energy = 0.0
for i in range(panels+1):
    y = ell*i/panels
    v = f0*math.cosh(k*y)+v0p*math.sinh(k*y)/k
    vp = f0*k*math.sinh(k*y)+v0p*math.cosh(k*y)
    weight = 1 if i in (0, panels) else (4 if i % 2 else 2)
    energy += weight*(vp*vp+(c-lam)*v*v)*ell/(3*panels)
green_error = abs(energy-boundary)
assert green_error < 1e-10 and boundary > 0

derivative_errors = []
for n in range(1, 5):
    eig = c+(n*math.pi/ell)**2
    epsilon = 1e-5
    numerical = (transfer(ell, eig+epsilon)[0][1]
                 -transfer(ell, eig-epsilon)[0][1])/(2*epsilon)
    formula = (-1)**n*ell/(2*(n*math.pi/ell)**2)
    derivative_errors.append(abs(numerical-formula))
assert max(derivative_errors) < 2e-9

alpha = math.tanh(math.sqrt(c)*ell/2)/math.sqrt(c)
print(json.dumps({
    "status": "PASS",
    "scope": "floating-point identities for a specified string, not a zeta realization",
    "c": c, "length": ell,
    "transfer_determinant_error": maxdet,
    "transfer_composition_error": maxcomposition,
    "green_identity_error": green_error,
    "boundary_energy": boundary,
    "determinant_derivative_errors": derivative_errors,
    "product_extension_inward_flux": alpha,
}, indent=2))
