#!/usr/bin/env python3
"""Exact controls for the moving-wall real-zero flux formula.

Run: python3 check_spacetime_wall_flux.py --output OUTPUT.json
Prepared for Edward Baker with substantial LLM assistance, 15 October 2026.
Recorded coordinating model gpt-6-astra, reasoning effort ultra; verified by the coordinating session.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--base-checker', type=Path, default=Path(__file__).with_name('check_spacetime_topology.py'))
args = parser.parse_args()
spec = importlib.util.spec_from_file_location('base', args.base_checker)
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for p in (a, b):
        for i, v in enumerate(p):
            out[i] += v
    return B.trim(out)

def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i+j] += av*bv
    return B.trim(out)

def wall_poly(p, wall):
    out = []
    for (pt, px), coefficient in p.items():
        q = [F(1)]
        for _ in range(px):
            q = mul(q, wall)
        out = add(out, [F(0)] * pt + [coefficient*v for v in q])
    return B.trim(out)

def refine_root(p, left, right):
    mid = (left + right) / 2
    denominator = 8
    while B.poly_eval(p, mid) == 0:
        mid = (left + right) / 2 + (right-left)/denominator
        denominator *= 2
    if B.poly_eval(p, left)*B.poly_eval(p, mid) < 0:
        return left, mid
    return mid, right

def signed_crossings(p, q, left, right):
    """Return (sign derivative of p, sign q) at each simple real p root."""
    ps = B.sturm_sequence(p)
    check(B.simple_roots(p, ps), 'boundary scalar polynomial squarefree')
    check(B.poly_eval(p, left)*B.poly_eval(p, right) != 0, 'no corner H zero')
    qs = B.sturm_sequence(q)
    rows = []
    for a, b in B.isolate_simple_roots(p, ps, left, right):
        for _ in range(1000):
            qa, qb = B.poly_eval(q, a), B.poly_eval(q, b)
            if qa and qb and B.root_count(qs, a, b) == 0:
                break
            a, b = refine_root(p, a, b)
        else:
            raise AssertionError('failed to separate the boundary jet')
        check(qa*qb > 0, 'q keeps sign on isolated scalar crossing')
        rows.append((B.sign(B.poly_eval(p, b)), B.sign(qa)))
    check(len(rows) == B.root_count(ps, left, right), 'all scalar crossings isolated')
    return rows

records = []
families = [
    ('narrow', [F(-1)], [F(1)]),
    ('outside', [F(1)], [F(2)]),
    ('moving_enclosing', [F(-1,2),F(1,5)], [F(1),F(1,3)]),
    ('moving_outside', [F(1,3),F(1,10)], [F(3,2),F(1,5)]),
]
for m in range(2, 13):
    for multiplier in (F(1), F(-1)):
        h = B.scale2(B.heat_polynomial(m), multiplier)
        hx = B.derivative2(h, 1)
        check(not B.add2(B.derivative2(h,0), B.derivative2(hx,1)), 'exact heat PDE')
        for name, a, b in families:
            check(all(B.poly_eval(a,t) < B.poly_eval(b,t) for t in (F(-1),F(1))), 'ordered walls')
            n = []
            face_rays = []
            for t in (F(-1),F(1)):
                rows = signed_crossings(B.restrict(h,0,t), B.restrict(hx,0,t),
                                        B.poly_eval(a,t), B.poly_eval(b,t))
                n.append(len(rows))
                check(all(dp == q for dp,q in rows), 'spatial derivative sign equals Hx')
                face_rays.append(sum(q > 0 for dp,q in rows))
            qs = []
            wall_rays = []
            wall_counts = []
            for w in (a,b):
                rows = signed_crossings(wall_poly(h,w), wall_poly(hx,w), F(-1),F(1))
                qs.append(sum(dp*q for dp,q in rows))
                wall_rays.append(sum(-dp for dp,q in rows if q > 0))
                wall_counts.append(len(rows))
            winding = face_rays[0] - face_rays[1] + wall_rays[0] - wall_rays[1]
            flux_winding = F(n[0]-n[1]-qs[0]+qs[1], 2)
            inside = B.poly_eval(a,F(0)) < 0 < B.poly_eval(b,F(0))
            expected = -(m//2) if inside else 0
            check(winding == flux_winding, 'direct ray crossing equals wall flux formula')
            check(winding == expected, 'exact expected local-index count')
            records.append({'degree':m,'overall_sign':int(multiplier),'family':name,
                            'walls':[[str(x) for x in w] for w in (a,b)],
                            'endpoint_root_counts':n,'wall_crossing_counts':wall_counts,
                            'signed_wall_terms_Q':qs,'direct_winding':winding,
                            'flux_winding':str(flux_winding),'expected_winding':expected})

# Nontransverse crossings are recorded by one-dimensional local degree.
# H=x has no first-jet zero.  A(t)=t^2 touches its simple root and returns:
# root counts at t=+-1 agree and the lower-wall local degree is zero.
# A(t)=t^3 crosses it, with lower-wall Hx=1 and local degree +1:
# the endpoint root count decreases by one, exactly balanced by Q_a=+1.
for power, expected_q, expected_n in [(2,0,[0,0]), (3,1,[1,0])]:
    wall = [F(0)]*power+[F(1)]
    q = (B.sign(B.poly_eval(wall,F(1)))-B.sign(B.poly_eval(wall,F(-1))))//2
    n = [int(B.poly_eval(wall,t) < 0 < 2) for t in (F(-1),F(1))]
    check(q == expected_q and n == expected_n, 'nontransverse local wall degree')
    check(F(n[0]-n[1]-q,2) == 0, 'tangent/odd wall-degree flux formula')

out={'date':'2026-10-15','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance','model':'gpt-6-astra','reasoning_effort':'ultra','checker':Path(__file__).name,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_checker_sha256':hashlib.sha256(args.base_checker.read_bytes()).hexdigest(),'status':'PASS','scope':'Finite exact heat-polynomial and moving-wall controls, not theta certification',
     'assertions':checks,'cases':len(records),'degree_range':[2,12],
     'arithmetic':'Fraction, Sturm counts, rational root separation; no sampled signs',
     'formula':'wind = (N_minus - N_plus - Q_left + Q_right)/2',
     'cases_data':records}
args.output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k != 'cases_data'}))
