#!/usr/bin/env python3
"""Exact rational check of a remote even polynomial heat-flow control.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Inherited model gpt-6.1-sol, reasoning effort ultra. Internal check only.
This concerns the named polynomial class, not the exact theta source.
"""
from fractions import Fraction as Q
import json
import argparse
import hashlib
from pathlib import Path
import platform

L = Q(2000)
q = Q(2, 5)  # Initial imaginary halfwidth squared.
T = Q(1, 5)
tau = Q(1, 100)
X = Q(1001)

def A(t): return L*L-q+6*t
def B(t): return (L*L+q)**2+4*t*(L*L-q)+12*t*t
def f(t): return 6*t*t+2*(L*L-q)*t-L*L*q
def field(t, x): return x**4-2*A(t)*x*x+B(t)
def jet(t, x):
    return field(t, x), 4*x**3-4*A(t)*x, 12*x*x-4*A(t)

# Coefficients in t, low degree first. These equalities verify the heat
# evolution and discriminant algebra identically, not at sampled times.
A_coeff = [L*L-q, Q(6)]
B_coeff = [(L*L+q)**2, 4*(L*L-q), Q(12)]
heat_constant_from_time = [B_coeff[1], 2*B_coeff[2]]
heat_constant_from_minus_second_z = [4*A_coeff[0], 4*A_coeff[1]]
assert heat_constant_from_time == heat_constant_from_minus_second_z
assert -2*A_coeff[1] == -12
discriminant_coeff = [A_coeff[0]**2-B_coeff[0],
                     2*A_coeff[0]*A_coeff[1]-B_coeff[1],
                     A_coeff[1]**2-B_coeff[2]]
assert discriminant_coeff == [-4*L*L*q, 8*(L*L-q), Q(24)]

# For c(t)=L^2+q+2t, c(t)^2-B(t)=8t(q-t). This proves the
# contracted strip while nonreal roots remain; subsequently all are real.
c_coeff = [L*L+q, Q(2)]
strip_identity = [c_coeff[0]**2-B_coeff[0],
                  2*c_coeff[0]*c_coeff[1]-B_coeff[1],
                  c_coeff[1]**2-B_coeff[2]]
assert strip_identity == [Q(0), 8*q, Q(-8)]
assert 0 < q <= 1 and 0 < T <= q and L*L > q

# f is strictly increasing for all t>=0. Its unique positive zero is
# the all-real threshold: discriminant negative before, nonnegative after.
assert 2*(L*L-q) > 0 and f(0) < 0
coarse_lo = q/2-1/(L*L)
coarse_hi = q/2
assert 0 < coarse_lo < coarse_hi == T
assert f(coarse_lo) < 0 < f(coarse_hi)
narrow_lo = T-1/(20*L*L)
narrow_hi = T-1/(40*L*L)
assert f(narrow_lo) < 0 < f(narrow_hi)
assert f(tau) < 0

# All roots stay beyond |Re z|>1400 on the entire interval [0,T].
# If D<0, their real parts squared are (sqrt(B)+A)/2 >= A_min/2.
# If D>=0, they are real and their squares are A +/- sqrt(D).
# Since D increases, D<=D(T)=8/25<1; inner square >=A_min-1.
A_min = A(0)
D_max = 4*f(T)
assert A_min > 0 and B(0) > 0 and all(v > 0 for v in B_coeff)
assert 0 < D_max == Q(8, 25) < 1
real_part_square_lower = min(A_min/2, A_min-1)
assert real_part_square_lower > Q(1400)**2 > X*X
assert 2*A_min > 0  # F(t,iy)=y^4+2A(t)y^2+B(t)>0 for every real y.

# The same remote roots all have |z|<3000 on [0,1/2]. Thus every
# exterior real-jet exclusion beyond exp(20/epsilon) is also true for
# this control; its obstruction is confined to the finite bridge.
T_outer = Q(1, 2)
assert B(T_outer) < Q(3000)**4
assert 4*f(T_outer) < Q(4000)**2
assert A(T_outer)+4000 < Q(3000)**2
assert 2**40 > 3000  # e^40>2^40, the smallest C20 threshold.

# It satisfies finite E exclusion but deliberately fails the stronger
# local signed theta inequality. This keeps the obstruction's scope clear.
v0, v1, v2 = jet(tau, Q(1000))
energy = v0*v0+v1*v1
laguerre = v1*v1-v0*v2
assert energy > 0 and laguerre-energy/100 < 0

out = {
    'status': 'PASS',
    'parameters': {'L':str(L), 'q':str(q), 'T':str(T), 'tau':str(tau), 'finite_X':str(X)},
    'heat_equation_coefficient_identity': True,
    'discriminant_coefficient_identity': True,
    'strip_coefficient_identity': True,
    'threshold_coarse_bracket': [str(coarse_lo), str(coarse_hi)],
    'threshold_narrow_bracket': [str(narrow_lo), str(narrow_hi)],
    'threshold_narrow_decimal_display_only': [float(narrow_lo), float(narrow_hi)],
    'threshold_bracket_signs': [str(f(narrow_lo)), str(f(narrow_hi))],
    'nonreal_at_tau_discriminant': str(4*f(tau)),
    'all_real_at_T': True,
    'entire_time_root_real_part_square_lower': str(real_part_square_lower),
    'wall_x1000_modulus_lower_strict': str(Q(400)**4),
    'finite_real_field_modulus_lower_strict': str(Q(399)**4),
    'positive_on_imaginary_axis': True,
    'all_roots_strictly_inside_modulus_3000_through_time': str(T_outer),
    'real_jet_exclusion_for_abs_x_at_least_3000': True,
    'fails_signed_D1_coefficient_1_over_100': True,
    'source_contract': 'even polynomial heat family; not the theta square-source/reflection contract',
    'scope': 'finite E coverage, vertical wall, unit strip, imaginary-axis positivity, evenness and known all-real time0.2 do not alone imply an improved global threshold',
}
parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path)
parser.add_argument('--execution-model',default='gpt-6.1-sol')
parser.add_argument('--execution-effort',default='ultra')
args=parser.parse_args()
out.update({'date':'2026-10-18','prepared_for':'Edward Baker',
            'actual_model':args.execution_model,'actual_effort':args.execution_effort,
            'llm_assistance':'substantial; same-model internal exact replay',
            'python':platform.python_version(),'arithmetic':'exact fractions.Fraction',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
serialized=json.dumps(out,indent=2)+'\n'
if args.output:
    args.output.write_text(serialized)
print(serialized,end='')
