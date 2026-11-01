#!/usr/bin/env python3
"""Source-free exact bookkeeping for B03 R11; not a proof of Hardy's theorem.

No theta evaluation, quadrature, numerical amplitude, or failing height is
computed. The analytical proof and imported theorem remain separate inputs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

INV = Path("papers/investigations-5/05_radial_theta_collision_geometry")
NOTE = INV / "notes/fixed_coefficient_parameter_geometry/B03_R11_FIXED_GAUSSIAN_SOURCE_RELATIVE_OBSTRUCTION_20261030.md"
REF = INV / "references/18_HARDY_UNCERTAINTY_AND_FIXED_GAUSSIAN_SCOPE_20261030.md"
SELF = INV / "reviews/fixed_coefficient_parameter_geometry/B03_R11_FIXED_GAUSSIAN_SELF_REVIEW_20261030.md"
HERE = INV / "numerics/fixed_coefficient_parameter_geometry"
OUTPUT = HERE / "fcg_b03_r11_gaussian_obstruction_checks_20261030.json"


def rational(x: F) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def compute() -> dict:
    checks = {}

    def require(name, condition):
        if not condition:
            raise AssertionError(name)
        checks[name] = True

    t_lo, t_hi = F(31, 128), F(33, 128)
    kappa = 1 - 2 * t_hi
    b_lo, b_hi = 32 - t_hi, 32 - t_lo
    require("time_interval_and_weight_slack", 0 < t_lo < t_hi < F(1, 2) and kappa == F(31, 64))
    require("paired_gaussian_heat_width", b_lo == F(4063, 128) and b_hi == F(4065, 128) and b_hi < 32)

    # Exact finite exponential series proves e^3 > 20.
    exp3_lower = sum((F(3**k, factorial(k)) for k in range(9)), F(0))
    require("exp3_lower_above_20", exp3_lower > 20)
    require("complete_arithmetic_geometric_ratio", F(16, 20**3) == F(1, 500))
    prefactor_upper = 2 * F(22, 7)**2 / (1 - F(1, 500))
    require("complete_source_prefactor_below_20", prefactor_upper < 20)
    require("weighted_squared_source_exponent", 2 * 24 - 1 == 47)
    # e^(4u) has coefficients 1,4,8,32/3,32/3 through degree 4.
    exp4_coeffs = [F(4**k, factorial(k)) for k in range(5)]
    require("source_exponent_linear", 9 - 3 * exp4_coeffs[1] == -3)
    require("source_exponent_quadratic", -3 * exp4_coeffs[2] == -24)
    require("source_exponent_quartic", -3 * exp4_coeffs[4] == -32)
    # B*x - 32*x^2 = B^2/128 - 32*(x - B/64)^2.
    require("all_gaussian_source_square_completion", F(32, 64**2) == F(1, 128) and F(64, 64) == 1)

    require("source_lower_interval_exponential_argument", F(22, 7) * F(4, 3) == F(88, 21) < 5)
    require("source_lower_coefficient", 3 * (2 * 3 - 3) == 9)
    require("source_lower_after_exp_bound", F(9, 3**5) == F(1, 27))
    require("weighted_source_lower_interval", F(31, 16**2) < 1)
    c_lower = F(2, 16) * F(1, 27) * F(1, 3)
    require("projection_numerator_lower", c_lower == F(1, 648))
    require("gram_sqrt_upper", F(22, 7 * 63) < F(1, 16))
    require("gram_exponent_upper", F(64, 63) < 2)
    d_upper = F(1, 2) * F(1, 4) * (1 + 9)
    a_lower = c_lower / d_upper
    require("gram_denominator_upper", d_upper == F(5, 4))
    require("paired_coefficient_lower", a_lower == F(1, 810))
    require("leading_amplitude_sqrt_lower", F(3, 32) > F(1, 16))
    m_lower = a_lower / 8
    require("leading_amplitude_lower", m_lower == F(1, 6480))
    require("jet_amplitude_numerator_lower", 4 * m_lower == F(1, 1620))
    require("jet_amplitude_exponent", 1 / (4 * b_lo) == F(32, 4063))
    require("jet_amplitude_denominator", 32**2 + 16 == 1040)

    # Gaussian completion for exp(-b*u^2)*cosh(8u):
    # (8+iA)^2/(4b) = 16/b - A^2/(4b) + i*4A/b.
    require("wave_completion_constant", F(8**2, 4) == 16)
    require("wave_completion_phase", F(2 * 8, 4) == 4)
    # Weighted Gram of exp(-32u^2)cosh(8u):
    # cosh^2(8u)=(1+cosh(16u))/2, exponent 16^2/(4*63).
    require("gram_gaussian_exponent", 2 * 32 - 1 == 63)
    require("gram_completion_constant", F(16**2, 4 * 63) == F(64, 63))
    require("cauchy_schwarz_whole_line_heat_exponent", 2 * t_hi - 1 == -kappa)
    # Gamma(j+1/2)/sqrt(pi), j=0,1,2.
    gamma_factors = [F(1), F(1, 2), F(3, 4)]
    require("gaussian_moment_recurrence", gamma_factors[1] == F(1, 2) * gamma_factors[0] and gamma_factors[2] == F(3, 2) * gamma_factors[1])
    # Source convention in the imported theorem: a=1/beta^2,
    # d=4/alpha^2; alpha*beta<4 is exactly a*d>1/4.
    require("hardy_fourier_threshold_conversion", F(4, 4**2) == F(1, 4))

    return {
        "status": "exact source-free bookkeeping passed",
        "prepared_for": "Edward Baker",
        "llm_assistance": "substantial",
        "model": "gpt-6-astra",
        "effort": "max",
        "date": "2026-10-30",
        "timezone": "America/New_York",
        "chat": "0052",
        "scope": "Rational constants and normalization bookkeeping only; analytical source/Hardy/relative-error proofs require reading the note and primary theorem.",
        "source_evaluations": 0,
        "quadrature_calls": 0,
        "new_source_moments": 0,
        "height_or_degree_scan": False,
        "failing_height_located": False,
        "check_results": checks,
        "exact_values": {
            "time_lower": rational(t_lo),
            "time_upper": rational(t_hi),
            "weight_slack": rational(kappa),
            "exp3_finite_sum_lower": rational(exp3_lower),
            "source_prefactor_upper": rational(prefactor_upper),
            "paired_coefficient_lower": rational(a_lower),
            "leading_amplitude_lower": rational(m_lower),
            "model_jet_numerator_lower": rational(4 * m_lower),
            "model_jet_gaussian_exponent": rational(1 / (4 * b_lo)),
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[5])
    parser.add_argument("--write", action="store_true", help="Write the small record; default checks the existing record.")
    args = parser.parse_args()
    repo = args.repo.resolve()
    result = compute()
    sources = [NOTE, REF, SELF, HERE / Path(__file__).name,
               INV / "notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md",
               INV / "notes/fixed_coefficient_parameter_geometry/E02_R10_VERIFICATION_AND_MODEL_HANDOFF_20261030.md"]
    result["input_sha256"] = {str(p): hashlib.sha256((repo / p).read_bytes()).hexdigest() for p in sources}
    output = repo / OUTPUT
    if args.write:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print("Wrote", output)
    else:
        saved = json.loads(output.read_text())
        if result != saved:
            raise SystemExit("Mismatch: saved record or one of its inputs changed; no automatic rewrite.")
        print("Exact bookkeeping and all saved input hashes match. No theta acquisition or analytical proof replay.")


if __name__ == "__main__":
    main()
