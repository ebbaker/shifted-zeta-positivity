#!/usr/bin/env python3
"""Exact rational control of the infinite probe tail above H=6063.

GPT-6 (Codex) assistance for Edward Baker, 25 September 2026.
Exact serving variant and reasoning effort unavailable. See the proof in
../reviews/PROBE_TAIL_CERTIFICATION_AUDIT_20260925.md. This checks the rational
inequalities in that proof, conditional on the cited proved zero-count bound.
It does NOT certify stored zero ordinates, quadrature, or the 48-factor replay.
Only Python's standard library is used; no zero file is read.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform


def exp_enclosure(x, degree=64):
    """Positive Taylor sum and a rational geometric majorant of its tail."""
    assert x >= 0 and x < degree + 2
    term = total = F(1)
    for k in range(1, degree + 1):
        term *= x / k
        total += term
    first_omitted = term * x / (degree + 1)
    return total, total + first_omitted / (1 - x / (degree + 2))


def encode(q):
    with localcontext() as ctx:
        ctx.prec = 24
        display = str(Decimal(q.numerator) / Decimal(q.denominator))
    return {"numerator": str(q.numerator), "denominator": str(q.denominator),
            "decimal_display_only": display}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    height = 6063
    checks = {
        "log_H_below_9": exp_enclosure(F(9))[0] > height,
        "exp_17_over_4_below_71": exp_enclosure(F(17, 4))[1] < 71,
        "exp_1_over_3_below_7_over_5": exp_enclosure(F(1, 3))[1] < F(7, 5),
        "polynomial_factor_below_1001_over_1000":
            (1 + F(1, 2 * height**2))**2 < F(1001, 1000),
        "first_12_product_inverse": sum(range(1, 13)) == 78,
    }
    # Both signs, integration by parts, and N_+(T) <= T log T:
    count_integral = 40 * F(1, height**19) * (F(9, 19) + F(1, 19**2))
    common = 2**156 * F(1001, 1000) * count_integral
    line, strip = F(7, 5) * common, 71 * common
    checks["full_strip_tail_below_1e_minus_21"] = strip < F(1, 10**21)
    checks["full_strip_tail_below_1_665e_minus_22"] = strip < F(1665, 10**25)
    assert all(checks.values()), checks
    result = {
        "status": "exact rational verification of the stated analytic post-cutoff bound only",
        "prepared_for": "Edward Baker",
        "assistant": "GPT-6 (Codex); exact serving variant and reasoning effort unavailable; LLM assisted",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "height": height, "t_max": 7, "product_factors_used_for_decay": 12,
        "infinite_product_tail": "included analytically using cosh(x) <= exp(x*x/2)",
        "zero_count_input": "N_+(T) <= T log T for T >= 6063, derived from Rosser's bound in the audit",
        "critical_line_tail": encode(line), "full_strip_tail": encode(strip),
        "checks": checks, "all_passed": all(checks.values()),
        "not_certified": ["finite block floating envelope", "stored zero ordinates or their completeness",
                          "48-factor transform evaluations", "quadrature and floating rounding"],
    }
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output)
    print(output)


if __name__ == "__main__":
    main()
