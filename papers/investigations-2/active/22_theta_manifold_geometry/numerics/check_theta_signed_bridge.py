#!/usr/bin/env python3
"""Exact finite checks for Investigation 22's signed two-source bridge.

Standard library only. All coefficients use fractions.Fraction. The exponential
representation strips the common heat factor and records spectral phases;
source-jet checks use formal Laurent polynomials. No theta truncation is used.
This checks identities, not analytic convergence, signs, or collision exclusion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

# A term key is (phase_u, phase_v, deg_u, deg_v, deg_t, deg_x, i_power).
# i_power is 0 or 1; coefficients lie in Q. The represented expression is the
# coefficient after stripping e^{t(u^2+v^2)}, with phase e^{ix(su*u+sv*v)}.
Z = (0, 0, 0, 0, 0, 0, 0)
checks = []


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(p, c):
    return clean({k: F(c) * v for k, v in p.items()})


def mon(c=1, *, pu=0, pv=0, u=0, v=0, t=0, x=0, i=0):
    sign = -1 if (i // 2) % 2 else 1
    return {(pu, pv, u, v, t, x, i % 2): F(c) * sign} if c else {}


def mul(p, q):
    out = {}
    for a, av in p.items():
        for b, bv in q.items():
            k = tuple(a[j] + b[j] for j in range(7))
            sign = -1 if k[6] >= 2 else 1
            k = k[:6] + (k[6] % 2,)
            out[k] = out.get(k, F(0)) + sign * av * bv
    return clean(out)


def dd(p, axis):
    """Ordinary derivative, including the stripped heat and recorded phase."""
    out = {}
    di, si = (2, 0) if axis == 0 else (3, 1)
    for k, c in p.items():
        if k[di]:
            a = list(k)
            a[di] -= 1
            a = tuple(a)
            out[a] = out.get(a, F(0)) + k[di] * c
        # Derivative of heat: 2*t*u or 2*t*v.
        a = list(k)
        a[di] += 1
        a[4] += 1
        a = tuple(a)
        out[a] = out.get(a, F(0)) + 2 * c
        # Derivative of phase: i*phase*x.
        if k[si]:
            a = list(k)
            a[5] += 1
            a[6] += 1
            sign = -1 if a[6] == 2 else 1
            a[6] %= 2
            a = tuple(a)
            out[a] = out.get(a, F(0)) + sign * k[si] * c
    return clean(out)


def ll(p, axis):
    return add(dd(dd(p, axis), axis), scale(p, -1))


def restrict(p, axis):
    di, si = (2, 0) if axis == 0 else (3, 1)
    out = {}
    for k, c in p.items():
        if k[di]:
            continue
        a = list(k)
        a[si] = 0
        a = tuple(a)
        out[a] = out.get(a, F(0)) + c
    return clean(out)


def cj(j, axis):
    if axis == 0:
        return add(mon(F(1, 2), pu=1, u=j, i=j),
                   mon(F(1, 2), pu=-1, u=j, i=-j))
    return add(mon(F(1, 2), pv=1, v=j, i=j),
               mon(F(1, 2), pv=-1, v=j, i=-j))


def cosine(pu, pv):
    return add(mon(F(1, 2), pu=pu, pv=pv),
               mon(F(1, 2), pu=-pu, pv=-pv))


def check(name, actual, expected):
    if clean(actual) != clean(expected):
        raise AssertionError(f"{name}: {actual!r} != {expected!r}")
    checks.append(name)


c = [[cj(j, axis) for j in range(4)] for axis in range(2)]
r = [[ll(c[axis][j], axis) for j in range(4)] for axis in range(2)]
plus2 = add(mon(u=2), mon(2, u=1, v=1), mon(v=2))
minus2 = add(mon(u=2), mon(-2, u=1, v=1), mon(v=2))
kernels = []
for j in (0, 1):
    k_product = add(mul(c[0][j+1], c[1][j+1]),
                    scale(mul(c[0][j], c[1][j+2]), F(-1, 2)),
                    scale(mul(c[0][j+2], c[1][j]), F(-1, 2)))
    k_phase = scale(mul(mon(u=j, v=j),
                        add(mul(plus2, cosine(1, -1)),
                            scale(mul(minus2, cosine(1, 1)), (-1)**j))), F(1, 4))
    check(f"laguerre_phase_kernel_j{j}", k_product, k_phase)
    kernels.append(k_product)
    transferred = add(mul(r[0][j+1], r[1][j+1]),
                      scale(mul(r[0][j], r[1][j+2]), F(-1, 2)),
                      scale(mul(r[0][j+2], r[1][j]), F(-1, 2)))
    check(f"primitive_double_transfer_j{j}", ll(ll(k_product, 0), 1), transferred)
    for axis in (0, 1):
        check(f"primitive_lower_first_derivative_j{j}_axis{axis}",
              restrict(dd(k_product, axis), axis), {})
    check(f"laguerre_corner_j{j}", restrict(restrict(k_product, 0), 1), {})

check("branch0_lower_edge", restrict(kernels[0], 0),
      scale(mul(mon(v=2), cosine(0, 1)), F(1, 2)))
check("branch1_lower_edge", restrict(kernels[1], 0), {})
check("branch0_transferred_edge_equals_minus_half_R2", ll(restrict(kernels[0], 0), 1),
      scale(r[1][2], F(-1, 2)))

energy_product = add(mul(c[0][0], c[1][0]), mul(c[0][1], c[1][1]))
energy_phase = scale(add(mul(add(mon(), mon(u=1, v=1)), cosine(1, -1)),
                         mul(add(mon(), mon(-1, u=1, v=1)), cosine(1, 1))), F(1, 2))
check("physical_energy_phase_kernel", energy_product, energy_phase)
check("physical_energy_double_transfer", ll(ll(energy_product, 0), 1),
      add(mul(r[0][0], r[1][0]), mul(r[0][1], r[1][1])))
check("physical_energy_lower_edge", restrict(energy_product, 0), c[1][0])
check("physical_energy_transferred_edge", ll(restrict(energy_product, 0), 1), r[1][0])
check("physical_energy_corner_before_boundary_factor", restrict(restrict(energy_product, 0), 1), mon())
for axis in (0, 1):
    check(f"physical_energy_lower_first_derivative_axis{axis}",
          restrict(dd(energy_product, axis), axis), {})

for j in range(4):
    for axis in (0, 1):
        check(f"jet_lower_value_j{j}_axis{axis}", restrict(c[axis][j], axis), mon() if j == 0 else {})
        check(f"jet_lower_first_derivative_j{j}_axis{axis}", restrict(dd(c[axis][j], axis), axis), {})
    # Displayed general R_j formula, axis u.
    cosj = add(mon(F(1, 2), pu=1, i=j), mon(F(1, 2), pu=-1, i=-j))
    cosnext = add(mon(F(1, 2), pu=1, i=j+1), mon(F(1, 2), pu=-1, i=-j-1))
    a = add(mon(2*(2*j+1), u=j, t=1), mon(4, u=j+2, t=2),
            mon(-1, u=j, x=2), mon(-1, u=j))
    if j >= 2:
        a = add(a, mon(j*(j-1), u=j-2))
    b = mon(4, u=j+1, t=1, x=1)
    if j:
        b = add(b, mon(2*j, u=j-1, x=1))
    check(f"explicit_heat_retaining_R{j}", r[0][j], add(mul(a, cosj), mul(b, cosnext)))

# Formal jet polynomials: key (power of c=pi/q, ordinary theta derivative).
# Powers may be negative. Theta_r' = c^{-1}Theta_{r+2}; c'=-4c.
def jet(k):
    if k < 0:
        return {}
    return {(m, k-2*m): F(factorial(k), 2**m*factorial(m)*factorial(k-2*m))
            for m in range(k//2+1)}


def jshift(p, power):
    return {(m+power, k): a for (m, k), a in p.items()}


def jderivative(p):
    out = {}
    for (m, k), a in p.items():
        out[(m, k)] = out.get((m, k), F(0)) - 4*m*a
        out[(m-1, k+2)] = out.get((m-1, k+2), F(0)) + a
    return clean(out)


for k in range(11):
    check(f"covariant_jet_path_recurrence_k{k}", jderivative(jet(k)),
          add(jshift(jet(k+2), -1), scale(jet(k), -(2*k+1)),
              scale(jshift(jet(k-2), 1), -k*(k-1))))

# Independent theta-lattice mode check. Key (power a, power q), a=pi*n^2.
# J_{2r}/pi^r = sum_m k!/[2^m m! (k-2m)!] * (-4a)^(r-m)q^(-m).
def scaled_even_jet(k):
    assert k % 2 == 0
    out = {}
    for (m, derivative), a in jet(k).items():
        half = derivative//2
        out[(half, -m)] = a * (-4)**half
    return out


def aqshift(p, a=0, q=0):
    return {(ma+a, mq+q): v for (ma, mq), v in p.items()}


def mode_derivative(p):
    # d_u[e^u exp(-a*q)P(a,q)] / [e^u exp(-a*q)]
    # = P + 4q P_q - 4aq P.
    out = {(ma, mq): (1+4*mq)*v for (ma, mq), v in p.items()}
    return add(out, scale(aqshift(p, a=1, q=1), -4))


mode0 = {(2, 2): F(2), (1, 1): F(-3)}
mode1 = mode_derivative(mode0)
mode2 = mode_derivative(mode1)
source0 = scale(add(aqshift(scaled_even_jet(4), q=2), {(0, 0): F(-3)}), F(1, 8))
source1 = scale(add(aqshift(scaled_even_jet(6), q=3),
                    scale(aqshift(scaled_even_jet(2), q=1), -15)), F(1, 8))
source2 = scale(add(aqshift(scaled_even_jet(8), q=4),
                    scale(aqshift(scaled_even_jet(4), q=2), -45), {(0, 0): F(30)}), F(1, 8))
check("paired_lattice_mode_complete_source", source0, mode0)
check("paired_lattice_mode_source_first_derivative", source1, mode1)
check("paired_lattice_mode_source_second_derivative", source2, mode2)
check("ordinary_mode_first_derivative_coefficients", mode1,
      {(3, 3): F(-8), (2, 2): F(30), (1, 1): F(-15)})
check("ordinary_mode_second_derivative_coefficients", mode2,
      {(4, 4): F(32), (3, 3): F(-224), (2, 2): F(330), (1, 1): F(-75)})
for j, expression in enumerate((source0, source1, source2)):
    check(f"constant_theta_mode_cancels_source_derivative_{j}",
          {k: v for k, v in expression.items() if k[0] == 0}, {})

record = {
    "date": "2026-10-15",
    "prepared_for": "Edward Baker",
    "llm_assistance": "Substantial LLM assistance; independent exact finite algebra checks.",
    "model": "gpt-6-astra",
    "reasoning_effort": "ultra",
    "checker": Path(__file__).name,
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "python_version": platform.python_version(),
    "arithmetic": "Exact rational coefficients over Q[i]; formal spectral phases and Laurent polynomials.",
    "assertions_passed": len(checks),
    "checks": checks,
    "scope": [
        "Complete j=0,1 signed Laguerre kernels and physical energy kernel.",
        "Primitive transfer polynomial identities, lower-edge parity, and corner values.",
        "Heat-retaining transferred one-source test functions through spatial derivative three.",
        "Formal covariant-jet path recurrence through jet ten.",
        "Complete source and its first two u derivatives checked against an arbitrary paired theta lattice mode.",
        "Constant theta mode cancellation in all three source expressions."
    ],
    "does_not_establish": [
        "Analytic convergence, boundary decay, or differentiation of the infinite theta series.",
        "Any numerical sign, uniform source estimate, new theta sign domain, or collision exclusion.",
        "A favorable physical-energy comparison from ASD geometry alone."
    ],
}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
encoded = json.dumps(record, indent=2) + "\n"
if args.output:
    args.output.write_text(encoded)
    print(f"Passed {len(checks)} exact finite assertions; wrote {args.output}.")
else:
    print(encoded, end="")
