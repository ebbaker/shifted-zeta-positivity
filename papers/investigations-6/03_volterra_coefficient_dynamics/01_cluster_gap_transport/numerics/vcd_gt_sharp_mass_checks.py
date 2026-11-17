#!/usr/bin/env python3
"""Exact finite checks for E03 r6; no canonical source evaluations.

16 November 2026, for Edward Baker with OpenAI Codex assistance.
Actual model/effort unavailable. Analytical proofs remain in Notes27/28.
"""
from fractions import Fraction as F
from math import isqrt
import json


def sqrt_bounds(x, digits=24):
    scale = 10**digits
    n = isqrt(x.numerator * scale * scale // x.denominator)
    lo, hi = F(n, scale), F(n + 1, scale)
    assert lo * lo <= x < hi * hi
    return lo, hi


def bounds_record(lo, hi):
    return {"lower_exact": str(lo), "upper_exact": str(hi),
            "lower_float_display_only": float(lo), "upper_float_display_only": float(hi)}


def q(x, y, d):
    v = x*x - y*y - d
    return v / (v*v + 4*x*x*y*y)


def main():
    h, d, kappa, target = F(6, 5), F(1, 5), F(5000, 1962848636289), F(59, 100)
    slo, shi = sqrt_bounds(h)
    oldlo, oldhi = sqrt_bounds(h*(h+1))
    sharp = (1/(4*(1+shi)), 1/(4*(1+slo)))
    old = (1/(4*(h+1+oldhi)), 1/(4*(h+1+oldlo)))
    assert 9*old[1]+kappa < target
    assert 10*old[0]+kappa > target
    assert 4*sharp[1]+kappa < target
    assert 5*sharp[0]+kappa > target
    assert target - (9*old[1]+kappa) > F('0.00173512567')
    assert 4*sharp[1]+kappa < F('0.4772255776')
    example_sharp = min(q(x, F(1), z) for x in (F(8, 5), F(2)) for z in (-d, d))
    example_old = (F(8,5)**2-h)/((F(2)**2+h)**2+4*F(2)**2)
    assert example_sharp == F(425, 3778)
    assert example_old == F(17, 538)
    assert example_sharp/example_old == F(6725, 1889)

    atoms = [(F(0), F(5,12)), (F(1), F(1,4)), (F(-1), F(1,4)),
             (F(2), F(1,24)), (F(-2), F(1,24))]
    moments = {r: sum(w*x**r for x,w in atoms) for r in (2,4,6)}
    c0 = 5*sum(w*w*x**6 for x,w in atoms)
    total = sum(w*v*x*x*y*y*(3*x*x-4*x*y+3*y*y)/2
                for x,w in atoms for y,v in atoms)
    assert total == 3*moments[2]*moments[4]
    assert 2*c0-total == F(-10,9)
    # cos(n*pi)=(-1)^n: differentiate the original readout exactly.
    f2 = -sum(w*x*x*F(-1)**int(x) for x,w in atoms)
    f4 = sum(w*x**4*F(-1)**int(x) for x,w in atoms)
    assert f2 == F(1,6) and f4 == F(5,6)
    numerator = -3*f2*f4
    assert numerator == F(-5,12)
    # Same determinant computed by matrix entries and factored expression.
    p, r, wp, wr = F(1), F(2), F(1,4), F(1,24)
    def entry(x,y,wx,wy):
        return wx*wy*x*x*y*y*(3*x*x+4*x*y+3*y*y)/2
    determinant = entry(p,p,wp,wp)*entry(r,r,wr,wr)-entry(p,r,wp,wr)**2
    factored = -F(3,4)*wp**2*wr**2*p**4*r**4*(p-r)**2*(3*p*p+14*p*r+3*r*r)
    assert determinant == factored < 0
    return {
        "date_local": "2026-11-16 America/New_York",
        "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex",
        "model": None, "effort": None,
        "scope": "Exact rational checks of analytical thresholds and fixed atomic algebra; not a canonical-source certificate or a proof by sampling",
        "old_per_occurrence_cap": bounds_record(*old),
        "sharp_per_occurrence_cap": bounds_record(*sharp),
        "old_nine_plus_mirror": bounds_record(9*old[0]+kappa, 9*old[1]+kappa),
        "sharp_four_plus_mirror": bounds_record(4*sharp[0]+kappa, 4*sharp[1]+kappa),
        "necessary_counts": {"old": 10, "sharp": 5, "sufficient_canonical_counts": False},
        "abstract_rectangle_example": {"L": "8/5", "U": "2", "delta": "1", "d": "1/5", "old": str(example_old), "sharp": str(example_sharp), "ratio": str(example_sharp/example_old), "canonical_manifest": False},
        "five_atom": {"moments": {str(r):str(v) for r,v in moments.items()}, "constant": str(c0), "total_coefficients": str(total), "absolute_allowance": str(2*c0-total), "double_numerator": str(numerator), "natural_matrix_minor": str(determinant)},
        "checks_passed": True,
    }


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))
