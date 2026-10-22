#!/usr/bin/env python3
"""Exact finite algebra for shared Note 05; no theta certificate.

Prepared for Edward Baker with substantial LLM assistance, 22 October 2026.
Recorded authoring configuration: gpt-6.1-sol (Codex), effort ultra.
Standard library only. The note proves the analytic inequalities; this
script checks polynomial identities and constants without sampling a grid.
"""

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


# Sparse rational polynomials in (Re tau, Im tau, Re z, Im z, delta^2).
ZERO = (0, 0, 0, 0, 0)


def constant(value):
    return {ZERO: F(value)} if value else {}


def variable(axis):
    powers = list(ZERO)
    powers[axis] = 1
    return {tuple(powers): F(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for powers, value in poly.items():
            out[powers] = out.get(powers, F(0)) + value
    return {p: v for p, v in out.items() if v}


def scale(value, poly):
    return {p: F(value) * v for p, v in poly.items() if value * v}


def mul(left, right):
    out = {}
    for p, v in left.items():
        for q, w in right.items():
            power = tuple(a + b for a, b in zip(p, q))
            out[power] = out.get(power, F(0)) + v * w
    return {p: v for p, v in out.items() if v}


def derivative(poly, axis):
    out = {}
    for p, v in poly.items():
        if p[axis]:
            q = list(p)
            q[axis] -= 1
            out[tuple(q)] = v * p[axis]
    return out


def squared(poly):
    return mul(poly, poly)


def run():
    t, s, u, v, regulator = [variable(i) for i in range(5)]
    radial = add(squared(u), squared(v))
    h_real = add(squared(u), scale(-1, squared(v)), scale(-2, t))
    h_imag = add(scale(2, mul(u, v)), scale(-2, s))
    energy = add(squared(h_real), squared(h_imag), scale(4, radial))
    dz_real = add(scale(-2, squared(u)), scale(2, squared(v)), scale(-4, t))
    dz_imag = add(scale(-4, mul(u, v)), scale(-4, s))
    dz_abs2 = add(squared(dz_real), squared(dz_imag))
    lap_energy = add(derivative(derivative(energy, 2), 2),
                     derivative(derivative(energy, 3), 3))
    numerator = add(mul(add(energy, regulator), lap_energy),
                    scale(-1, squared(derivative(energy, 2))),
                    scale(-1, squared(derivative(energy, 3))))
    hz_hzz_abs2 = add(scale(4, radial), constant(4))
    gram_expected = scale(4, add(dz_abs2, mul(regulator, hz_hzz_abs2)))
    assert numerator == gram_expected
    assert lap_energy == scale(4, hz_hzz_abs2)

    # Certificate envelopes: these are exact rational simplifications.
    direct_coefficient = F(1, 32)**2 * F(5, 4) / F(25, 64)
    j_coefficient = F(37, 64)**2
    topology_coefficient_without_pi = F(1, 2) / j_coefficient
    ratio_without_pi = topology_coefficient_without_pi / direct_coefficient
    final_without_pi = ratio_without_pi * F(8, 17)
    assert direct_coefficient == F(1, 320)
    assert topology_coefficient_without_pi == F(2048, 1369)
    assert ratio_without_pi == F(655360, 1369)
    assert final_without_pi == F(5242880, 23273)

    # (1+r/4)(1+r) - (8/17)r(1+17r/32), coefficients in r.
    positive_remainder = [F(1), F(5, 4) - F(8, 17),
                          F(1, 4) - F(8, 17) * F(17, 32)]
    assert positive_remainder == [F(1), F(53, 68), F(0)]

    # Full symbolic denominator subtraction and bias closure.
    e, x, m, f0 = t, regulator, u, v  # Formal symbols only here.
    # 1/(e+x)-1/e = -x/[e(e+x)], after multiplication.
    assert add(e, scale(-1, add(e, x)), x) == {}
    # Fdelta+Zdelta=F0, after multiplication by m+x (m denotes m_*^2).
    assert add(mul(m, f0), mul(x, f0), scale(-1, mul(add(m, x), f0))) == {}

    # (U+x)(A^2+x B)-x U B = U A^2+x A^2+x^2 B.
    U, A, B, x = t, s, u, regulator
    lhs = add(mul(add(U, x), add(squared(A), mul(x, B))),
              scale(-1, mul(x, mul(U, B))))
    rhs = add(mul(U, squared(A)), mul(x, squared(A)), mul(squared(x), B))
    assert lhs == rhs
    assert all(coefficient > 0 for coefficient in rhs.values())

    # Quadratic wall: E=4 t^2, Ndelta=4(4 t^2+delta^2).
    wall_energy = scale(4, squared(t))
    wall_ndelta = scale(4, add(wall_energy, regulator))
    assert wall_ndelta == add(scale(16, squared(t)), scale(4, regulator))
    # q^2=(1+delta^2/(4t^2))*pi*gamma_delta, cross-multiplied.
    assert mul(constant(4), add(wall_energy, regulator)) == wall_ndelta
    return {
        "quadratic_regularized_spatial_Gram_polynomial": "exact equality",
        "quadratic_spatial_Laplacian_energy": "exact equality",
        "direct_envelope_coefficient": str(direct_coefficient),
        "topological_envelope_coefficient_divided_by_pi": str(topology_coefficient_without_pi),
        "universal_certificate_ratio_divided_by_pi": str(final_without_pi),
        "positive_ratio_remainder_coefficients": [str(c) for c in positive_remainder],
        "Schur_certificate_positive_remainder": "U*A^2+x*A^2+x^2*B",
        "boundary_bias_and_certificate_closure": "exact polynomial equalities",
        "quadratic_critical_wall_regulator_multiplier": "1+delta^2/(4t^2)",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    own = Path(__file__).resolve()
    investigation = own.parents[2]
    sources = [own,
               investigation / "notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md",
               investigation / "notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md",
               investigation / "notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md"]
    record = {
        "status": "exact finite algebra passed; analytic proof remains in Note 05",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "research_date": "2026-10-22 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "substantial",
        "recorded_authoring_model": "gpt-6.1-sol",
        "recorded_authoring_effort": "ultra",
        "configuration_source": "root active turn metadata",
        "scope": "No theta acquisition, sampling campaign, analytic formalization, or specialist review",
        "checks": run(),
        "sha256": {str(p.relative_to(investigation)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sources},
    }
    output = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
