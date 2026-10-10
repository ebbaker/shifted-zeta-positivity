"""Exact follow-up ledger checks; source analytic estimates remain assumptions.

Prints deterministic JSON. Uses only Python's standard library.
"""
from fractions import Fraction as F
import json

checks = 0


def require(condition):
    global checks
    assert condition
    checks += 1


ell, b = F(1001, 6000), F(1, 8)
lx, ly = (1-ell-b)/2, (1-ell+b)/2
h = 1-lx+ell
sigma0 = F(20999, 24000)
c = lx/2-1+h/6
require(c == -F(11, 16))
require(sigma0+c == lx/2+b/12)
require(1+2*sigma0 == F(32999, 12000))
require(ell+b+2*lx == 1)

# Equality of coefficients in the unspecialized high identity.
# Variable order: constant, R, delta, q. This is an exact polynomial
# comparison, not a grid justification for a continuous identity.
unspecialized = [(1-ly)/2-sigma0-h/6-ell/2,
                 h, (1-ly+h)/2, ell]
displayed = [h/2-1-7*b/12-ell,
             h, h-b/2-ell/2, ell]
for v, w in zip(unspecialized, displayed):
    require(v == w)

m0, zeta = F(1, 400000), F(1, 6400000)
require(2*zeta == m0/8)
require(ell/(h+zeta) > F(1, 5) > F(7, 37))
mw, mz = ly/20, h/600
require(min(mw, mz) > m0)
threshold = F(87, 200)*ell/m0
require(threshold == 29029)
normalizer_cases = []
for K in [2, 100, 10000, 29028, 29030, 1000000]:
    mp = F(87, 200)*ell/K
    m = min(m0, mw, mz, mp)/8
    require(0 < mp < F(87, 100)*ell/K)
    require((mp < m0) == (K > threshold))
    require(m <= min(m0, mw, mz, mp)/8)
    normalizer_cases.append({"K": K, "m_P": str(mp),
                             "retained_m": str(m), "final_sigma": str(m/2)})

# Stress height selection over orders, small ceilings, and negative/positive
# tail degrees. Each test uses exact rational arithmetic; no floats select N.
height_cases = 0
for K in [2, 29030, 1000000]:
    mp = F(87, 200)*ell/K
    m = min(m0, mw, mz, mp)/8
    for A in [0, 1, 10, 1000]:
        for B in [-3, 0, 1, 100]:
            for tau0 in [F(1, 100), F(1, 10**15)]:
                tau = min(tau0/2, m/(4*(A+1)))
                edge = sigma0+F(1, 48000)
                Cedge = edge+c
                ratio = max(F(0), (B-Cedge+m/2)/tau)
                N = ratio.numerator//ratio.denominator + 1
                require(0 < tau < tau0)
                require(A*tau <= m/4)
                require(B-N*tau < Cedge-m/2)
                require(Cedge-m+A*tau <= Cedge-3*m/4)
                height_cases += 1

gap_cases = 0
for gap in [F(1, 24000), F(1, 10**8), F(1, 10**20)]:
    for K in [2, 29030, 1000000]:
        m = min(m0, mw, mz, F(87, 200)*ell/K)/8
        epsilon = min(gap/2, m/2)
        require(0 < epsilon < gap)
        require(sigma0+gap-epsilon > sigma0)
        require(sigma0+c+gap/2 <= sigma0+gap+c-epsilon)
        require(sigma0+gap+c-m/2 <= sigma0+gap+c-epsilon)
        gap_cases += 1

print(json.dumps({
    "scope": "Exact allocation and exponent identities only; no source analytic theorem is certified.",
    "assertions": checks,
    "sigma0": str(sigma0),
    "high_identity_coefficient_order": ["constant", "R", "delta", "q"],
    "high_identity_coefficients": [str(v) for v in displayed],
    "normalizer_threshold_K": str(threshold),
    "normalizer_cases": normalizer_cases,
    "height_cases": height_cases,
    "contradiction_gap_cases": gap_cases,
}, indent=2, sort_keys=True))
