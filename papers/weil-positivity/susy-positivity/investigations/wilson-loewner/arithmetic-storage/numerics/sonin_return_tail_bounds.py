#!/usr/bin/env python3
"""Exact rational bounds for Sonin inverse-series truncation, not Sonin traces.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
Uses ||X(f,f)||_1 <= 4 B_infinity[f]; all targets are relative to B_infinity.
Standard library only. Prints a small JSON record; no matrix data are generated.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path


def decimal_up(value, digits=22):
    scale = 10**digits
    n = (value.numerator * scale + value.denominator - 1) // value.denominator
    return f"{n // scale}.{n % scale:0{digits}d}"


def degree_for(ratio, prefactor, target):
    degree, bound = 0, prefactor * ratio
    while bound > target:
        degree += 1
        bound *= ratio
    return degree, bound


def main():
    digits = 50
    scale = 10**digits
    root = isqrt(2 * scale**2)
    lo, hi = Q(root, scale), Q(root + 1, scale)
    assert lo**2 < 2 < hi**2
    # Neumann: (4 sqrt(2)/3)/(1-beta) beta^(M+1).
    # Chebyshev: (16 r)/(1-r) r^(M+1), using r^2=1/2 exactly.
    rows = []
    for exponent in (6, 8, 10):
        target = Q(1, 10**exponent)
        for name in ("neumann", "chebyshev"):
            if name == "neumann":
                rate_lo, rate_hi = 2 * lo / 3, 2 * hi / 3
                pre_lo = (4 * lo / 3) / (1 - rate_lo)
                pre_hi = (4 * hi / 3) / (1 - rate_hi)
            else:
                rate_lo, rate_hi = lo / 2, hi / 2
                pre_lo = 16 * rate_lo / (1 - rate_lo)
                pre_hi = 16 * rate_hi / (1 - rate_hi)
            degree, bound = degree_for(rate_hi, pre_hi, target)
            # Certify minimal degree for this analytic majorant, not for actual error.
            assert degree > 0 and pre_lo * rate_lo**degree > target
            rows.append({
                "series": name, "relative_target": f"1e-{exponent}",
                "degree_M": degree, "trace_terms": degree + 1,
                "relative_bound_upper": decimal_up(bound),
                "previous_degree_majorant_exceeds_target": True,
            })
    result = {
        "date": "2026-09-29", "model": "GPT-6 (Codex)",
        "serving_variant": "not exposed", "reasoning_effort": "not exposed",
        "scope": "Certified scalar series majorants only; no actual Sonin trace, projection approximation, source normalization, or Weil sign test.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sqrt2_bracket": {"denominator": str(scale), "lower_numerator": str(root), "upper_numerator": str(root + 1)},
        "rows": rows,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
