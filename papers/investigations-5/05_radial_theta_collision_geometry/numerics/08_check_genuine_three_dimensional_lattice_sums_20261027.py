#!/usr/bin/env python3
"""Exact finite shell checks and separate floating diagnostics for Note08.

27 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra, effort max. Standard-library only.
The infinite identities are proved analytically in Note08.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path


def chi4(n):
    assert n > 0 and n % 2
    return 1 if n % 4 == 1 else -1


limit = 625
bound = math.isqrt(limit)
signed = Counter()
unsigned = Counter()
for a in range(-bound, bound + 1):
    if a % 2 == 0:
        continue
    for b in range(-bound, bound + 1):
        if b % 2:
            continue
        for c in range(-bound, bound + 1):
            if c % 2:
                continue
            energy = a*a + b*b + c*c
            if energy <= limit:
                unsigned[energy] += 1
                signed[energy] += 1 if (c//2) % 2 == 0 else -1

weighted_coefficients = []
for energy in range(1, limit + 1):
    n = math.isqrt(energy)
    is_odd_square = n*n == energy and n % 2 == 1
    expected = 2*n*chi4(n) if is_odd_square else 0
    assert signed[energy] == expected
    if is_odd_square:
        # sin(pi*n/2)/(2*n) = chi4(n)/(2*n), exactly.
        coefficient = F(signed[energy]*chi4(n), 2*n)
        assert coefficient == 1
        weighted_coefficients.append({'radius': n, 'coefficient': str(coefficient)})

assert unsigned[5] == 8 and signed[5] == 0
assert unsigned[9] == 10 and signed[9] == -6
assert F(2*chi4(3), 2*3) == -F(1, 3)  # axes alone fail
assert F(signed[9]*chi4(3), 2*3) == 1

cube_bound = 8
cube_shells = Counter(max(abs(a), abs(b), abs(c))
                      for a,b,c in product(range(-cube_bound, cube_bound+1), repeat=3))
assert cube_shells[0] == 1
for n in range(1, cube_bound+1):
    assert cube_shells[n] == 24*n*n+2
    assert F(cube_shells[n], 12*n*n+1) == 2

# Exact analytic allowance for the omitted spatial box in P(r), r>=1/4.
# pi*r^2 > 3/16, exp(3/16)>19/16>7/6, hence q<6/7.
q = F(6, 7)
assert 1+F(3,16) > F(7,6)
box = 32
one_dim_total = 1 + 2*q/(1-q**3)
one_dim_tail = q**((box+1)**2)/(1-q**(2*box+3))
signed_box_tail = 3*one_dim_tail*one_dim_total**2
assert signed_box_tail < F(1,10**69)

# Exploratory direct sums: every point of the three-dimensional box is used.
points = []
for a in range(-box, box+1):
    if a % 2 == 0:
        continue
    for b in range(-box, box+1,2):
        for c in range(-box, box+1,2):
            energy = a*a+b*b+c*c
            radius = math.sqrt(energy)
            phase = 1 if (c//2) % 2 == 0 else -1
            weight = phase*math.sin(math.pi*radius/2)/(2*radius)
            points.append((energy,weight))


def lattice_p(r):
    return math.fsum(weight*math.exp(-math.pi*r*r*energy)
                     for energy,weight in points)


def odd_theta(r):
    return math.fsum(math.exp(-math.pi*r*r*n*n) for n in range(1,130,2))


def theta(r):
    return 1+2*math.fsum(math.exp(-math.pi*r*r*n*n) for n in range(1,130))


diagnostics = []
for r in (0.25, 0.5, 0.75, 1.0, 1.5, 2.0):
    value = lattice_p(r)
    target = odd_theta(r)
    assert abs(value-target) < 2e-14
    diagnostics.append({'r':r,'direct_3d_P':value,'odd_theta':target,
                        'absolute_difference':abs(value-target)})

reconstruction = []
for r in (0.5,0.75,1.0,1.5,2.0):
    value = 4*lattice_p(r)+2*lattice_p(1/(2*r))/r
    target = theta(r)
    assert abs(value-target)<8e-14
    reconstruction.append({'r':r,'reconstructed_Theta':value,'Theta':target,
                           'absolute_difference':abs(value-target)})

cube_points = [(max(a*a,b*b,c*c)) for a,b,c in product(range(-10,11),repeat=3)]
positive_diagnostics = []
for r in (0.5,1.0,2.0):
    value = math.fsum(math.exp(-math.pi*r*r*energy)/(1+12*energy)
                     for energy in cube_points)
    target = theta(r)
    assert abs(value-target)<5e-15
    positive_diagnostics.append({'r':r,'direct_3d_cube_resolvent':value,
                                 'Theta':target,'absolute_difference':abs(value-target)})

record = {
    'date':'2026-10-27','prepared_for':'Edward Baker','llm_assistance':'substantial',
    'model':'gpt-6-astra','effort':'max','status':'PASS',
    'scope':'Exact finite shell identities and rational Gaussian tail allowance; separate floating-point direct-sum diagnostics. Infinite identities follow from the written Jacobi/shell-count proofs. No collision certificate.',
    'exact_checks':{
        'signed_shells_checked_through_squared_radius':limit,
        'selected_shells':[{'squared_radius':j,'unsigned_count':unsigned[j],
                            'signed_count':signed[j]} for j in (1,5,9,13,17,25,49,81)],
        'weighted_odd_square_coefficients':weighted_coefficients,
        'axes_only_coefficient_at_squared_radius_9':'-1/3; full 3D coefficient is 1',
        'cube_shells_checked_through_radius':cube_bound,
        'cube_counts':{str(n):cube_shells[n] for n in range(cube_bound+1)},
        'signed_box_tail':{
            'box_coordinate_bound':box,'r_min':'1/4','q_upper':'6/7',
            'formula':'3*q^((B+1)^2)/(1-q^(2B+3))*(1+2*q/(1-q^3))^2',
            'strict_upper':'1e-69',
            'roundoff':'Not covered; this bounds truncation only'}
    },
    'floating_diagnostics':{'signed_P':diagnostics,'Theta_reconstruction':reconstruction,
                            'positive_cube_resolvent':positive_diagnostics,
                            'status':'Exploratory, not interval arithmetic'}
}
out = Path(__file__).with_name('08_GENUINE_THREE_DIMENSIONAL_LATTICE_CHECKS_20261027.json')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','record':str(out),'signed_shell_limit':limit,
                  'largest_floating_difference':max(d['absolute_difference'] for d in
                    diagnostics+reconstruction+positive_diagnostics)}))
