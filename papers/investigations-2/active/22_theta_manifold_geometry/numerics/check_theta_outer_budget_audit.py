#!/usr/bin/env python3
"""Exact arithmetic for a refined Investigation 21 low-index budget.

Prepared for Edward Baker, 15 October 2026; substantial LLM assistance.
Recorded coordinating model gpt-6-astra, reasoning effort ultra.
This verifies finite arithmetic, not the imported exponent-pair package.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json

checks = []

def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def exp_lower(x, order=50):
    return sum((x**k / factorial(k) for k in range(order + 1)), F(0))

theta = F(61, 24)
rho = F(1, 100000)
theta0 = theta-rho/100
ell0 = 100001
old_A = F(36138917, 16)
cuts = [F(1,1024), F(1,64), F(1,10), F(1,5)]
epsilons = [F(2,15), F(1,8), F(1,14), F(1,121)]
for i, (b, epsilon) in enumerate(zip(cuts, epsilons)):
    check(f'piece {i} has claimed uniform real exponent',
          F(1,2)+theta0*(1-b)/4-rho/2 > 1+epsilon)
    check(f'piece {i} retains uniform theta envelope coefficient',
          (1-b)/4 >= F(1,5))
check('e exceeds five halves using four Taylor terms', exp_lower(F(1),3) > F(5,2))

d0 = F(15,2)
D1 = d0*d0+1
D2 = 2*d0**3+4
A_head = (theta*D2+2*D1)/4
A = A_head+1
check('smallest-index sum constant', A_head == F(217843,384))
check('complete refined low-index constant', A == F(218227,384))
check('improvement factor exceeds 3974', old_A > 3974*A)

tail_parameters = [(F(1,1024),8,F(3,4)),
                   (F(1,64),14,F(1,8)),
                   (F(1,10),121,F(1,8))]
for i, (b,d,budget) in enumerate(tail_parameters, 1):
    r = b*ell0
    P = theta*(d*r*r+2*d*d*r+2*d**3)+2*(d*r+d*d)
    check(f'tail {i} lower integral endpoint is in decreasing regime', r-1 > 2)
    check(f'tail {i} polynomial exponential is decreasing', ell0 > 2*d/b)
    check(f'tail {i} exact Taylor lower bound pays assigned share',
          P/2 < budget*exp_lower(r/d))
check('three tail shares sum to one', sum(t[2] for t in tail_parameters) == 1)

G0 = F(962773,671)
lam = F(21807,254720000)-F(63,50)*rho
check('retained exponential saving exceeds one over 14000', lam > F(1,14000))
equal_share_height = 48*1728*4*A
check('old fixed height is one integer', 48*1728*4*old_A == 749376582912)
check('improved equal-share fixed height', equal_share_height == 188548128)
check('equal-share EP logarithm coefficient unchanged', 48*1728*8 == 663552)

leading = 1728*4*A+409
check('low-index plus carrier coefficient', leading == 3928495)
check('simple improved fixed height pays leading allowance',
      leading/F(32000000) < F(63,512))
check('reallocated EP logarithm coefficient', 1024*1728*8 == 14155776)
check('reallocated shares total one eighth',
      F(63,512)+F(1,1024)+F(1,1024) == F(1,8))

# The three remaining errors are paid at Lambda >= 100001. These
# deliberately use the same elementary exponential estimates as Note 58.
V0 = ell0
check('ordinary tail below one over 3072',
      F(V0,40)**3/6 > 3072*1728*64)
check('first RS polynomial absorbed by exponential',
      F(V0,4)**3/6 >= V0**2)
check('first RS tail below one over 3072',
      F(V0**2,8) > 3072*1728*16)
check('second RS tail below one over 3072',
      F(2*V0**2,25) > 3072*1728*6)
check('three remaining shares total one over 1024', 3*F(1,3072) == F(1,1024))

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path)
args = parser.parse_args()
record = {
    'date': '2026-10-15',
    'prepared_for': 'Edward Baker',
    'llm_assistance': 'substantial LLM assistance',
    'recorded_coordinating_model': 'gpt-6-astra',
    'recorded_coordinating_effort': 'ultra',
    'metadata_provenance': 'Coordinating conversation configuration supplied to this task.',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'assertion_count': len(checks),
    'assertions': checks,
    'constants': {
        'old_A': str(old_A),
        'refined_A': str(A),
        'old_fixed_log_height': 749376582912,
        'refined_equal_share_fixed_log_height': 188548128,
        'reallocated_fixed_log_height': 32000000,
        'equal_share_EP_log_coefficient': 663552,
        'reallocated_EP_log_coefficient': 14155776,
        'G0': str(G0),
        'lambda': str(lam),
        'C_EP': 'unevaluated; not replaced by one',
        'T_EP': 'retain any imported validity threshold',
    },
    'scope': 'Exact finite arithmetic supporting the analytic low-index proof in the companion note. Imported exponent-pair theorem, analytic replacements and original carrier proof are retained, not independently proved here. No evaluated unconditional starting height, feasible finite bridge, new small-time domain, or RH conclusion.',
}
serialized = json.dumps(record, indent=2, sort_keys=True)+'\n'
if args.output:
    args.output.write_text(serialized)
print(serialized)
