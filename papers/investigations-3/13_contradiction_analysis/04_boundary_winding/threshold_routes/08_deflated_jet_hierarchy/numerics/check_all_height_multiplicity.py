#!/usr/bin/env python3
"""Exact BW-08 all-height multiplicity controls; no acquired theta data.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-20.
Recorded model gpt-6-astra, effort ultra. Standard library only.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

BASE = Path('papers/investigations-3/13_contradiction_analysis/04_boundary_winding')
ROUTE = BASE / 'threshold_routes/08_deflated_jet_hierarchy'


def load_previous(root):
    path = root / ROUTE / 'numerics/check_imaginary_axis_bound.py'
    spec = importlib.util.spec_from_file_location('bw08_exact_previous', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def control(pv, a, m, b, others=(), scale=1):
    a, b = F(a), F(b)
    assert 0 < a <= b
    pairs = [(a, m)] + [(F(r), n) for r, n in others]
    polynomial = [F(scale)]
    for r, n in pairs:
        for _ in range(n):
            polynomial = pv.mul(polynomial, [-r*r, F(0), F(1)])
    jets = [pv.evaluate(pv.derivative(polynomial, j), a)
            for j in range(max(m+5, len(polynomial)))]
    assert all(j == 0 for j in jets[:m]) and jets[m] != 0
    hm, hp, hpp = jets[m:m+3]
    sj = hp*hp / ((m+1)**2*hm*hm) - 2*hpp / ((m+1)*(m+2)*hm)
    sr = F(m, 4)/(a*a) + sum((n*(1/(a-r)**2+1/(a+r)**2)
                               for r, n in pairs if r != a), F(0))
    assert sj == sr
    imaginary = [v*(-1)**(j//2) if j % 2 == 0 else F(0)
                 for j, v in enumerate(polynomial)]
    dp = pv.evaluate(pv.derivative(imaginary, 1), b)/pv.evaluate(imaginary, b)
    dr = sum((2*b*n/(r*r+b*b) for r, n in pairs), F(0))
    assert dp == dr
    gap = sj - (F(m, 4)/(a*a)+dp/b-2*m/(a*a+b*b))
    assert gap >= 0
    assert (gap == 0) == (len(others) == 0)
    curvature = hpp/hm - (hp/hm)**2
    rhs = -F(m, 2*(m+1))*(hp/hm)**2-F((m+1)*(m+2), 2)*sj
    assert curvature == rhs
    shifted_jets = jets[m-2:]
    series = pv.heat_critical_series(shifted_jets)
    assert series[0] == 0 and series[1] == -hm
    assert 2*series[2]/hm == curvature
    pi = pv.pi_bounds()
    loglo = pv.log_bounds((b+1)/(4*pi[1]))[0]
    loghi = pv.log_bounds((b+1)/(4*pi[0]))[1]
    dstatus = 'passes' if dp > loghi/4 else 'fails' if dp < loglo/4 else 'inconclusive'
    return {'a': str(a), 'm': m, 'b': str(b), 'degree': len(polynomial)-1,
            'scale': scale, 'extra_pairs': [[str(r), n] for r,n in others],
            'S_exact': str(sj), 'D_exact': str(dp), 'kernel_gap_exact': str(gap),
            'differentiated_critical_curvature_exact': str(curvature),
            'selected_D_floor': dstatus,
            'theta_source_assigned': False, 'event_excluded': False}


def coefficient(pv, a, m):
    a = F(a)
    b = max(a, F(20*m))
    pi = pv.pi_bounds()
    loglo = pv.log_bounds((b+1)/(4*pi[1]))[0]
    loghi = pv.log_bounds((b+1)/(4*pi[0]))[1]
    mirror = F(m, 4)/(a*a)
    ell = tuple(mirror+l/(4*b)-2*m/(a*a+b*b) for l in (loglo, loghi))
    assert ell[0] > mirror + 1/(40*b)
    return {'hypothetical_a': str(a), 'multiplicity': m, 'b': str(b),
            'mirror_exact': str(mirror), 'L_outward': pv.show_interval(ell),
            'increment_outward': pv.show_interval(tuple(v-mirror for v in ell)),
            'simple_increment_floor_exact': str(1/(40*b)),
            'ratio_to_mirror_outward': pv.show_interval(tuple(v/mirror for v in ell), 8)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=Path.cwd())
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    pv = load_previous(root)
    cases = []
    for m in (2,3,4,6):
        cases.append(control(pv, 1, m, 20*m))
        cases.append(control(pv, 20, m, 20*m, [(F(r), 1) for r in range(21, 41)], -1))
    cases.append(control(pv, 100, 3, 100, [(F(101), 1)]))
    assert any(c['selected_D_floor'] == 'passes' for c in cases)
    assert any(c['selected_D_floor'] == 'fails' for c in cases)
    coeffs = [coefficient(pv, a, m) for a,m in
              [(1,2),(20,2),(100,2),(1000,2),(1,3),(20,10),(1000,10)]]
    paths = [ROUTE/'notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md',
             ROUTE/'notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md',
             ROUTE/'numerics/check_imaginary_axis_bound.py',
             ROUTE/'numerics/check_all_height_multiplicity.py']
    hashes = {str(p): hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
    record = {'date': '2026-10-20', 'prepared_for': 'Edward Baker',
              'model': 'gpt-6-astra', 'reasoning_effort': 'ultra',
              'status': 'exact rational controls and outward analytic coefficients',
              'git_parent': subprocess.check_output(['git','rev-parse','HEAD'], cwd=root, text=True).strip(),
              'source_sha256': hashes, 'controls': cases, 'coefficients': coeffs,
              'theta_jet_acquisition': False, 'theta_event_location': None,
              'new_region': None, 'newman_bound_improved': False,
              'all_m_proof': 'written comparison in Note 04; finite controls audit formulas only'}
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'controls': len(cases), 'coefficient_rows': len(coeffs),
                      'output': str(args.output), 'all_exact_checks': 'passed'}))


if __name__ == '__main__':
    main()
