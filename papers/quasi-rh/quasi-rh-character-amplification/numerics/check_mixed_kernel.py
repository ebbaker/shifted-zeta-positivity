#!/usr/bin/env python3
"""Exact local algebra and rational-margin checks for the mixed kernel note.

Prepared for Edward Baker, 2026-10-08, with GPT-6 (Codex) assistance.
Exact serving variant and configured reasoning effort are not exposed.
This verifies algebra on a finite exhaustive set, not the analytic moment.
The pair-counting proof is in the accompanying research note.
"""
from fractions import Fraction as F
from itertools import product
import json

norms = (7, 13)  # two formal distinct good prime ideals
vectors = list(product(range(9), repeat=2))
pairs = 0
sixth_pairs = 0
nontrivial_mask_pairs = 0
for left in vectors:
    for right in vectors:
        pairs += 1
        common = tuple(min(a,b) for a,b in zip(left,right))
        aa = tuple(a-g for a,g in zip(left,common))
        bb = tuple(b-g for b,g in zip(right,common))
        a0 = tuple(a%6 for a in aa)
        b0 = tuple(b%6 for b in bb)
        a6 = tuple(a//6 for a in aa)
        b6 = tuple(b//6 for b in bb)
        diff = tuple((a-b)%6 for a,b in zip(left,right))
        support = tuple(d != 0 for d in diff)
        extra = tuple((a+b>0) and d==0 for a,b,d in zip(left,right,diff))
        assert all(a == g+c+6*s for a,g,c,s in zip(left,common,a0,a6))
        assert all(b == g+c+6*s for b,g,c,s in zip(right,common,b0,b6))
        assert support == tuple(a+b>0 for a,b in zip(a0,b0))
        if not any(support):
            sixth_pairs += 1
        if any(extra):
            nontrivial_mask_pairs += 1
        def norm(v):
            result=1
            for p,e in zip(norms,v):
                result *= p**e
            return result
        assert norm(tuple(a+b for a,b in zip(a0,b0))) >= norm(support)
        A, B = norm(aa), norm(bb)
        assert max(A,B)**2 >= A*B
        # At every local unit, the sixth-root phase exponent agrees modulo 6;
        # at a nonunit, both original factors and the retained mask vanish.
        for a,b,d,e in zip(left,right,diff,extra):
            for phase in range(6):
                assert ((a-b)*phase)%6 == (d*phase)%6
            original_zero = (a+b>0)
            reduced_zero = (d!=0) or e
            assert original_zero == reduced_zero

baseline_margin = 1+F(9,25)**2-F(1,5000)-F(9,8)
count_margin = F(9,25)*(F(9,25)+F(23,20))-F(21,40)-F(1,5000)
assert baseline_margin == F(11,2500)
assert count_margin == F(23,1250)
# Additional exact constants for the combined source-dependent reduction.
row_conductor_gap = F(1,1000)
mixed_saving = F(1,5000)
row_margin = F(9,25)*row_conductor_gap-mixed_saving
plain_diagonal_margin = F(9,25)**2-mixed_saving
assert row_margin == F(1,6250)
assert plain_diagonal_margin == F(647,5000)
combined_margin = min(row_margin,plain_diagonal_margin,count_margin)
assert combined_margin == F(1,6250)
# Formal source-transfer widths, before the small strict decrement.
first_width = [-m for m in [F(9,25),F(1,2)]]
second_width = [2*r-1-2*m for r in [F(7,10),F(37,50)]
                for m in [F(9,25),F(1,2)]]
assert (min(first_width),max(first_width)) == (-F(1,2),-F(9,25))
assert (min(second_width),max(second_width)) == (-F(3,5),-F(6,25))
assert F(7,10)+F(9,25)>1
# The simplest lost-mask counterexample: p^6 against the unit ideal.
assert (6-0)%6 == 0 and (6+0>0)
result = {
    "status": "exact local algebra and rational margins passed; no mixed moment proved",
    "prime_ideal_norms": list(norms),
    "valuation_range": [0,8],
    "column_pairs_checked": pairs,
    "sixth_power_equivalent_pairs": sixth_pairs,
    "pairs_with_nontrivial_retained_mask": nontrivial_mask_pairs,
    "baseline_conductor_cutoff_exponent": "1/4",
    "baseline_margin": str(baseline_margin),
    "scalar_count_conductor_cutoff_exponent": "4/5",
    "scalar_count_margin": str(count_margin),
    "row_conductor_gap": str(row_conductor_gap),
    "row_conductor_margin": str(row_margin),
    "plain_diagonal_margin": str(plain_diagonal_margin),
    "combined_discarded_error_margin": str(combined_margin),
    "formal_transfer_widths_at_zero_decrement": {
        "first": [str(min(first_width)),str(max(first_width))],
        "second": [str(min(second_width)),str(max(second_width))],
    },
}
print(json.dumps(result,indent=2))
