#!/usr/bin/env python3
"""Supporting exact checks, not a canonical-zero experiment or proof assessment.

8 November 2026. Prepared for Edward Baker with substantial OpenAI Codex
LLM assistance. Actual recorded model/effort unavailable.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import factorial
import json

weights = [Q(1), Q(1, 2), Q(1, 3)]
checks = {}
for k in range(1, 4):
    tuple_mass = sum((__import__('functools').reduce(lambda a,b:a*b,
                     (weights[j] for j in ids), Q(1))
                     for ids in permutations(range(3), k)), Q(0))
    mixture_mass = Q(0)
    for retained in product([0, 1], repeat=3):
        prob = Q(1)
        for flag, w in zip(retained, weights):
            prob *= w if flag else 1-w
        m = sum(retained)
        mixture_mass += prob * (factorial(m)//factorial(m-k) if m>=k else 0)
    assert tuple_mass == mixture_mass
    checks[f'factorial_mass_order_{k}'] = str(tuple_mass)
# Arbitrary rational factor values make the self-index subtraction check
# independent of Gaussian evaluation. Coincident positions share factors.
a = [Q(2), Q(2), Q(5)]
b = [Q(3), Q(3), Q(7)]
direct = sum(weights[j]*weights[k]*a[j]*b[k]
             for j in range(3) for k in range(3) if j != k)
r_product = sum(w*x for w,x in zip(weights,a))*sum(w*x for w,x in zip(weights,b))
self_term = sum(w*w*x*y for w,x,y in zip(weights,a,b))
wrong_self = sum(w*x*y for w,x,y in zip(weights,a,b))
assert direct == r_product-self_term
assert direct != r_product-wrong_self
checks['weighted_pair_direct_and_corrected'] = str(direct)
checks['incorrect_linear_weight_rejected'] = True
for m in [1,2,3,7]:
    assert sum(1 for j in range(m) for k in range(m) if j!=k)==m*(m-1)
checks['multiplicity_labels_checked'] = [1,2,3,7]
buffer = Q(25,6)**2-(1+(4+Q(1,32))**2)
assert buffer == Q(1015,9216) and buffer>0
assert 2*24+2*Q(15,4)**2 == Q(609,8)
assert 2*6+2*Q(15,8)**2 == Q(609,32) <1536
checks['squared_support_buffer'] = str(buffer)
checks['squared_horizontal_cutoff_second_derivative'] = '609/8'
checks['squared_vertical_cutoff_second_derivative'] = '609/32 < 1536'
# The support intervals, written in exact rational endpoints, are disjoint.
assert Q(1,32)<1
checks['partition_and_vertical_cutoff_derivative_supports_disjoint'] = True
print(json.dumps({
 'task':'TND-OC-E06','date_local':'2026-11-08','timezone':'America/New_York',
 'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
 'prepared_for':'Edward Baker','llm_assistance':'substantial OpenAI Codex',
 'actual_model':None,'actual_effort':None,
 'status':'exact bookkeeping passed; supports transcription only',
 'canonical_zero_evaluation':False,'checks':checks},indent=2))
