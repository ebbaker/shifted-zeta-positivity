#!/usr/bin/env python3
"""Small exact/diagnostic checks for the 2026-10-13 elliptic transport note.

Prepared for Edward Baker with LLM assistance: gpt-6-astra, effort ultra,
as recorded in the parent session. Standard library only. The rational
origin sign and polynomial checks are exact; floating-point theta residuals
are diagnostics, not outward-rounded enclosures or a stationary sign proof.
"""

from __future__ import annotations

import argparse
import cmath
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import platform


def add(a, b):
    result = [Q(0)] * max(len(a), len(b))
    for j, c in enumerate(a):
        result[j] += c
    for j, c in enumerate(b):
        result[j] += c
    while len(result) > 1 and not result[-1]:
        result.pop()
    return result


def scale(a, factor):
    return [c * factor for c in a]


def mul_linear(a, constant):
    return add(scale(a, Q(constant)), [Q(0)] + a)


def angular_polynomial_check(maximum=12):
    previous, current = [Q(0)], [Q(1)]
    rows = []
    for m in range(maximum + 1):
        product, closed = [Q(1)], [Q(0)]
        for k in range(m + 1):
            denominator = 2 ** (m - k) * math.factorial(m - k) * math.factorial(2 * k)
            closed = add(closed, scale(product, Q(1, denominator)))
            product = mul_linear(product, -1 - 4 * k)
        assert current == closed, (m, current, closed)
        assert all(c == 0 for j, c in enumerate(current) if j % 2 != m % 2)
        rows.append({"m": m, "coefficients_ascending": [str(c) for c in current]})
        following = scale(add([Q(0)] + current, previous), Q(1, (2 * m + 2) * (2 * m + 1)))
        previous, current = current, following
    return rows


def theta_jet(u, z, kappa, nmax=24, perturb=False):
    """Direct fixed-z derivatives; no elliptic identity used here."""
    s = math.exp(2 * u)
    output = {key: 0j for key in ("F", "Fu", "Fzz", "M", "BF", "BFu", "B2F")}
    for n in range(-nmax, nmax + 1):
        coefficient = 1.1 if perturb and abs(n) == 1 else 1.0
        term = coefficient * cmath.exp(u + math.pi * z * z / 2 - math.pi * n * n * s * s + 2j * math.pi * n * s * z)
        lu = 1 - 4 * math.pi * n * n * s * s + 4j * math.pi * n * s * z
        luu = -16 * math.pi * n * n * s * s + 8j * math.pi * n * s * z
        dz = math.pi * z + 2j * math.pi * n * s
        cov = (math.pi - kappa) * z + 2j * math.pi * n * s
        output["F"] += term
        output["Fu"] += lu * term
        output["Fzz"] += (math.pi + dz * dz) * term
        output["M"] += (lu * lu + luu - 1) * term / 16
        output["BF"] += cov * term
        output["BFu"] += (4j * math.pi * n * s + cov * lu) * term
        output["B2F"] += (math.pi - kappa + cov * cov) * term
    return output


def floating_transport_checks():
    rows = []
    for u in (-0.5, 0.0, 0.5):
        for z in (0j, 0.2 + 0.1j, -0.3j):
            for kind in ("real", "imaginary"):
                lam, kappa = (-2, math.pi) if kind == "real" else (2, -math.pi)
                p = math.exp(-2 * u) if kind == "real" else 1j * math.exp(2 * u)
                jet = theta_jet(u, z, kappa)
                qp = kappa * (p * z + p * p / 2)
                qm = kappa * (-p * z + p * p / 2)
                lhs = cmath.exp(-qp) * theta_jet(u, z + p, kappa)["M"]
                opposite = cmath.exp(-qm) * theta_jet(u, z - p, kappa)["M"]
                rhs = jet["M"] + (-2 * lam * p * jet["BFu"] - lam * lam * p * jet["BF"] + lam * lam * p * p * jet["B2F"]) / 16
                symmetric_rhs = jet["M"] + p * p * jet["B2F"] / 4
                residual = abs(lhs - rhs) / (1 + abs(lhs) + abs(rhs))
                symmetric_residual = abs((lhs + opposite) / 2 - symmetric_rhs) / (1 + abs(symmetric_rhs))
                pde_residual = abs(jet["Fu"] - jet["Fzz"] / math.pi + math.pi * z * z * jet["F"]) / (1 + abs(jet["Fu"]))
                assert max(residual, symmetric_residual, pde_residual) < 1e-10
                rows.append({"u": u, "z": [z.real, z.imag], "period": kind,
                             "normalized_transport_residual": residual,
                             "symmetric_transport_residual": symmetric_residual,
                             "balanced_pde_residual": pde_residual})
    # A changed integer preparation obeys the same balanced PDE and real
    # period, but fails the imaginary quasiperiod. This tests independence
    # from the PDE, not independence from all genuine-theta data.
    u, z = 0.0, 0.2 + 0.1j
    jet = theta_jet(u, z, -math.pi, perturb=True)
    shifted = theta_jet(u, z + 1j, -math.pi, perturb=True)
    q = -math.pi * (1j * z - 0.5)
    defect = cmath.exp(-q) * shifted["F"] - jet["F"]
    pde_defect = jet["Fu"] - jet["Fzz"] / math.pi + math.pi * z * z * jet["F"]
    assert abs(defect) > 0.01 and abs(pde_defect) < 1e-12
    return rows, {"coefficient_change": "c_1=c_-1=1.1; all other c_n=1",
                  "u": u, "z": [z.real, z.imag],
                  "absolute_normalized_imaginary_period_defect": abs(defect),
                  "absolute_balanced_pde_residual": abs(pde_defect)}


def exact_origin_sign():
    # Elementary proof uses 3 < pi < 22/7, pi^2 < 10, e < 3,
    # and exp(3) > sum_{k=0}^8 3^k/k! > 20.
    exp3_lower = sum((Q(3 ** k, math.factorial(k)) for k in range(9)), Q(0))
    assert exp3_lower > 20
    # n=1 term is -3*pi*exp(-pi) < -9/81 = -1/9.
    # Positive remainder is bounded by sum_{n>=2}20*n^4/20^(n^2).
    first = Q(20 * 2 ** 4, 20 ** 4)
    ratio = Q(3, 2) ** 4 / 20 ** 5
    tail_upper = first / (1 - ratio)
    total_upper = -Q(1, 9) + tail_upper
    assert total_upper < -Q(1, 10)
    diagnostic = math.fsum((2 * math.pi ** 2 * n * n * (n * n - 1) - 3 * math.pi * n * n) * math.exp(-math.pi * n * n) for n in range(1, 25))
    return {"exact_exp3_lower": str(exp3_lower), "exact_tail_ratio_upper": str(ratio),
            "exact_positive_remainder_upper": str(tail_upper),
            "exact_shifted_density_upper": str(total_upper),
            "certified_statement": "symmetric normalized shifted density at (u,z)=(0,0) < -1/10",
            "floating_value_diagnostic": diagnostic,
            "not_certified": "the displayed floating value is not an interval enclosure"}


def tail_bound_diagnostic():
    # Exact expression and its hypotheses are proved in the note. The
    # floating evaluation here is a diagnostic, not rounded outward.
    T, X, Z, U = 1.0, 1.0, 1.0, 1.0
    cm = ((1 + 4 * math.pi + 4 * math.pi * Z) ** 2 + 16 * math.pi + 8 * math.pi * Z + 1) / 16
    cn = cm + math.pi + 3 * math.pi ** 2 + 2 * math.pi ** 2 * Z
    prefactor = 2 * cn * math.exp(math.pi * Z * Z / 2) / (1 - 16 * math.exp(-3 * math.pi / 2))
    slope = 2 * math.pi * math.exp(4 * U) - 2 * T * U - 9 - X
    assert math.exp(2 * U) >= 4 * Z and slope > 0 and 8 * math.pi * math.exp(4 * U) >= 2 * T
    bound = prefactor * math.exp(T * U * U + (9 + X) * U - math.pi * math.exp(4 * U) / 2) / slope
    return {"domain": {"abs_t_le": T, "abs_real_x_le": 20, "abs_imag_x_le": X, "abs_z_le": Z},
            "cutoff_U": U, "full_symmetric_transform_tail_upper_formula_value": bound,
            "status": "analytic bound; floating evaluation is not outward rounded"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("ELLIPTIC_TRANSPORT_RECORD_20261013.json"))
    args = parser.parse_args()
    polynomials = angular_polynomial_check()
    transport, preparation = floating_transport_checks()
    result = {
        "date": "2026-10-13", "generated_utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker", "llm_assistance": True,
        "recorded_model": "gpt-6-astra", "recorded_reasoning_effort": "ultra",
        "configuration_provenance": "parent actual rollout configuration; inherited subagent configuration",
        "python": platform.python_version(), "dependencies": "Python standard library only",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_angular_polynomials": polynomials,
        "floating_transport": {"nmax": 24, "status": "diagnostic only; no rounded enclosures", "rows": transport},
        "changed_preparation_control": preparation,
        "exact_origin_sign": exact_origin_sign(), "analytic_tail_bound": tail_bound_diagnostic(),
        "scope": "No heat-integral enclosure, stationary theta sign, value-and-slope lower bound, or RH claim."
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"record": str(args.output), "angular_polynomial_checks": len(polynomials),
                      "transport_points": len(transport),
                      "max_normalized_transport_residual": max(row["normalized_transport_residual"] for row in transport),
                      "origin_sign": result["exact_origin_sign"]["certified_statement"]}, indent=2))


if __name__ == "__main__":
    main()
