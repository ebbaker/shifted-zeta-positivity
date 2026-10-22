#!/usr/bin/env python3
"""Exact finite algebra for shared Note 06; no theta numerical acquisition.

For Edward Baker with substantial LLM assistance, 22 October 2026.
Actual recorded authoring model gpt-6.1-sol (Codex), effort ultra.
The written note proves the analytic trace and endpoint inequalities.
"""

import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEPENDENCY = HERE / "check_chb_gauss_comparison.py"
spec = importlib.util.spec_from_file_location("chb_gauss_algebra", DEPENDENCY)
algebra = importlib.util.module_from_spec(spec)
spec.loader.exec_module(algebra)
add, scale, mul = algebra.add, algebra.scale, algebra.mul
derivative, squared = algebra.derivative, algebra.squared
constant, variable = algebra.constant, algebra.variable


def run():
    t, nu, z, radius, lam2 = [variable(i) for i in range(5)]
    # Exact heat polynomial, with nu formal: both signs are covered.
    heat4 = add(mul(squared(z), squared(z)), scale(-12, mul(t, squared(z))),
                scale(12, squared(t)))
    field = add(squared(z), scale(-2, t), mul(nu, heat4))
    assert add(derivative(field, 0), derivative(derivative(field, 2), 2)) == {}
    V = add(scale(-2, t), scale(12, mul(nu, squared(t))))
    B = add(constant(-2), scale(12, mul(nu, t)))
    Vp = derivative(V, 0)
    Bp = derivative(B, 0)
    assert V == mul(t, B)
    assert add(mul(t, Vp), scale(-1, V)) == mul(squared(t), Bp)

    r0 = scale(-6, nu)
    # q^2 - t^-2 - 2*r0/t, over the common denominator t^2 B^2.
    square_residual_numerator = add(squared(Vp), scale(-1, squared(B)),
                                     scale(-2, mul(r0, mul(t, squared(B)))))
    expected = scale(144, mul(squared(nu), mul(squared(t),
                          add(constant(-1), scale(12, mul(nu, t))))))
    assert square_residual_numerator == expected
    # The unrenormalized square difference has a nonzero term linear in t.
    difference = add(squared(Vp), scale(-1, squared(B)))
    assert difference == add(scale(-48, mul(nu, t)),
                              scale(432, mul(squared(nu), squared(t))))

    # Sharp trace radial primitive s^2/[2(1+a*s^2)]: quotient derivative.
    s, a = z, radius
    denominator = add(constant(1), mul(a, squared(s)))
    primitive_numerator = scale(F(1, 2), squared(s))
    derivative_numerator = add(mul(derivative(primitive_numerator, 2), denominator),
                 scale(-1, mul(primitive_numerator, derivative(denominator, 2))))
    assert derivative_numerator == s

    # Fixed and adaptive regulator derivative costs, cross-multiplied.
    fixed_energy = add(squared(V), lam2)
    assert derivative(fixed_energy, 0) == scale(2, mul(V, Vp))
    adaptive_energy = add(squared(V), mul(lam2, squared(t)))
    adaptive_extra = add(scale(F(1, 2), derivative(adaptive_energy, 0)),
                         scale(-1, mul(V, Vp)))
    assert adaptive_extra == mul(lam2, t)

    # Source event center and certificate comparison constants.
    # h2=2, h3=0, h4=24*nu => r0=-6*nu exactly.
    assert -F(24, 1) / (2 * F(2)) == -6
    ratio_square = F(48, 37)**2 * 2
    assert ratio_square == F(4608, 1369) and ratio_square > 1

    return {
        "quartic_heat_equation_for_formal_nu": "exact polynomial equality",
        "coupled_moment_cancellation": "t*V'-V=t^2*B'",
        "critical_value_factorization": "V=t*B; B=-2+12*nu*t",
        "signed_endpoint_center": "r0=-6*nu (either sign)",
        "square_residual_common_numerator": "144*nu^2*t^2*(-1+12*nu*t)",
        "unsubtracted_square_pole_common_numerator": "-48*nu*t+432*nu^2*t^2",
        "sharp_trace_radial_primitive": "exact quotient-derivative equality",
        "adaptive_regulator_missing_derivative_numerator": "lambda^2*t",
        "bulk_trace_vs_direct_ratio_lower_squared": str(ratio_square),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    investigation = HERE.parents[1]
    sources = [Path(__file__).resolve(), DEPENDENCY,
        investigation / "notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md",
        investigation / "notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md",
        investigation / "notes/06_CRITICAL_WALL_TRACES_AND_SIGNED_ENDPOINT_BUDGET_20261022.md"]
    record = {
        "status": "exact finite algebra passed; analytic proof remains in Note 06",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "research_date": "2026-10-22 America/New_York",
        "prepared_for": "Edward Baker",
        "llm_assistance": "substantial",
        "recorded_authoring_model": "gpt-6.1-sol",
        "recorded_authoring_effort": "ultra",
        "configuration_source": "root active turn metadata",
        "scope": "Exact finite algebra; no theta acquisition or analytic formalization",
        "checks": run(),
        "sha256": {str(p.relative_to(investigation)):
                   hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
    }
    output = json.dumps(record, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
