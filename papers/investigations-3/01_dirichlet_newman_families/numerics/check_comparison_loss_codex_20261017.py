#!/usr/bin/env python3
"""Bounded loss-sensitivity check supporting review 01, 17 October 2026.
Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort ultra.
Floating planning arithmetic, not a certificate or a character-family bound.
Uses the original programme's time-zero floor and independently integrates
its comparison ODE in closed form, retaining the same 801-point p grid.
Run from numerics: python3 -I check_comparison_loss_codex_20261017.py
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import sys

sys.dont_write_bytecode = True
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--contract-dir', type=Path, default=Path(__file__).resolve().parent)
args = parser.parse_args()
source = args.contract_dir / 'benchmark_family_contract_claude_20261017.py'
expected = '07ec4ac02e4ef73c90c4e621a688d8ac6296132501c9fa5ce8b353a7ed06fafc'
actual = hashlib.sha256(source.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit('Reviewed benchmark source hash does not match')
spec = importlib.util.spec_from_file_location('reviewed_contract', source)
contract = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contract)


def closed_form_time(C, p, a=1.0):
    """Integral_0^a (B-Q)/(2B+(kB-10)Q-kQ^2) dQ; k=4C/p, B=p^2.

    This rational integrand equals 1/g(Q). For k>0, g is concave, so
    positive endpoint values certify its positivity as a real algebraic
    statement when the parameters are exact. Here the checks are floating.
    """
    k, B = 4*C/p, p*p
    if C <= 0 or B < 5*a or 2+k*a-8*a/(B-a) <= 0:
        raise ValueError('Outside the positive comparison regime')
    v = k*B-10
    d = math.sqrt(v*v+8*k*B)
    def antiderivative(Q):
        N = 2*B+v*Q-k*Q*Q
        w = (2*k*Q-v)/d
        return math.log(N)/(2*k)+(B/2+5/k)*(2/d)*math.atanh(w)
    return antiderivative(a)-antiderivative(0.0)


rows = []
for q in (10**8, 10**12):
    for parity in (0, 1):
        candidates = []
        for i in range(801):
            p = math.sqrt(5.0)+0.01*i
            C = 0.75*contract.S_floor(math.log(q/math.pi), parity, p)
            candidates.append((closed_form_time(C, p), p, C))
        time, p, C = min(candidates)
        simpson = contract.comparison_time(C, p, 1.0, 0.0)
        if simpson is None or abs(time-simpson) > 1e-10:
            raise SystemExit('Closed form and Simpson cross-check disagree')
        rows.append({'q':q, 'parity':parity, 'delta_fraction_of_C':0.25,
                     'p':float(f'{p:.12g}'), 'planning_lambda':float(f'{time:.12g}'),
                     'below_conditional_baseline':time < 0.2811856084,
                     'closed_form_matches_simpson_within_1e-10':True})
record = {
    'date':'2026-10-17',
    'prepared_for':'Edward Baker',
    'model':'gpt-6.1-sol (Codex)',
    'reasoning_effort':'ultra',
    'assistance':'Substantial LLM assistance',
    'status':'floating planning diagnostic; assumes S >= 0.75 C on the comparison interval and H12; no bound is certified',
    'script':Path(__file__).name,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'reviewed_benchmark_sha256':actual,
    'runtime':{'python':platform.python_version(), 'system':platform.system(),
               'release':platform.release(), 'machine':platform.machine()},
    'domain':{'a':1, 'b':0, 'p_grid':'sqrt(5)+0.01*i, i=0,...,800'},
    'conditional_baseline':0.2811856084,
    'rows':rows,
}
print(json.dumps(record, indent=2, sort_keys=True))
