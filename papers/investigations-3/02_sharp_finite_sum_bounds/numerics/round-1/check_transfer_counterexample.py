#!/usr/bin/env python3
"""Exact rational coefficients of log(2) in a transfer counterexample.
Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Model gpt-6.1-sol (Codex), reasoning effort ultra. No theta counterexample.
At y=1/2 take n=16, g=4^-y, B=1, A=-1+3*4^y-16^y,
and sigma=sigma0+y/2. Derivative coefficients below factor out log(2).
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

def calculate():
    B, A, g, Ap, gp, half_log_n = F(1), F(1), F(1,2), F(-4), F(-1), F(2)
    vp = gp*A + g*Ap
    plain_gate = g*abs(Ap) + gp*abs(A) - half_log_n*(abs(B)+g*abs(A))
    branches=[]
    for e in (-1,1):
        z, d = B+e*g*A, 1+e*g
        dz = e*vp
        dabs = (1 if z>0 else -1)*dz if z else abs(dz)
        u = abs(z)/d
        weighted_derivative = dabs/d - e*gp*abs(z)/(d*d) - half_log_n*u
        branches.append(dict(branch=e, u=str(u), weighted_derivative_coefficient=str(weighted_derivative)))
    assert plain_gate == -2
    assert all(F(b['u'])==1 for b in branches)
    assert max(F(b['weighted_derivative_coefficient']) for b in branches)==2
    return dict(status='exact counterexample to generic inheritance only',
                prepared_for='Edward Baker', date='2026-10-17', model='gpt-6.1-sol', reasoning_effort='ultra',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                family='n=16; sigma=sigma0+y/2; g=4^(-y); B=1; A=-1+3*4^y-16^y',
                evaluation_y='1/2', A_at_zero='1',
                plain_sufficient_gate_over_log2=str(plain_gate),
                branches=branches,
                normalized_mass_right_derivative_over_n_to_minus_sigma_log2='2',
                limitation='signed finite-sum class; no assertion that theta Euler coefficients fail transfer')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); r=calculate(); a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
