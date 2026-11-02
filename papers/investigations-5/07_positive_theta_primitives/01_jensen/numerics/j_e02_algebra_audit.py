#!/usr/bin/env python3
"""Exact joint-numerator audit for J-E02 r1, 1 November 2026.

Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol (Codex), effort ultra. Standard library only.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys
import time


def main():
    start=time.monotonic()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    repo=parser.parse_args().repo.resolve()
    route=repo/'papers/investigations-5/07_positive_theta_primitives/jensen'
    helper=route/'numerics/j_e01_audit.py'
    assert sha256(helper.read_bytes()).hexdigest()=='5905598d1aba38d7e366df0b0fabf0b53a34f4ace21b4056a1a644e89d4f73e5'
    sys.dont_write_bytecode=True
    spec=importlib.util.spec_from_file_location('frozen_r1',helper)
    old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    add,scale,mul,der,prod,det=old.add,old.scale,old.mul,old.der,old.product,old.determinant3
    q=[{tuple(int(i==j) for i in range(8)):F(1)} for j in range(8)]

    def numerators(v):
        A=add(mul(v[0],v[3]),scale(mul(v[1],v[2]),-1))
        B=add(mul(v[0],v[4]),scale(mul(v[2],v[2]),-1))
        W=det([[v[0],v[1],v[2]],[v[2],v[3],v[4]],[v[4],v[5],v[6]]])
        W1=det([[v[0],v[1],v[3]],[v[2],v[3],v[5]],[v[4],v[5],v[7]]])
        N=add(prod(v[0],A,W1),scale(mul(add(mul(v[0],B),scale(mul(v[1],A),-1)),W),-3))
        return A,B,W,W1,N

    A,B,W,W1,N=numerators(q)
    def jet_derivative(p):
        assert all(e[7]==0 for e in p)
        return add(*(mul(der(p,j),q[j+1]) for j in range(7)))
    assert jet_derivative(A)==B
    assert jet_derivative(W)==W1
    raw=add(mul(A,add(mul(q[0],W1),scale(mul(q[1],W),-3))),
            scale(mul(W,add(mul(q[0],B),scale(mul(q[1],A),-2))),-3))
    assert raw==N
    assert all(sum(e)==6 and sum(j*v for j,v in enumerate(e))==13 for e in N)
    assert len(N)==29 and sum(abs(c) for c in N.values())==76

    # Same canonical Q polynomials as the frozen Q10 record; no new Q generation.
    prior=route/'numerics/J_E01_R2_EXACT_RECORD_20261101.json'
    assert sha256(prior.read_bytes()).hexdigest()=='9d2c6b008cebda9138537011295aa167d4c6e21d57edb491a89751e95452d5f4'
    r=json.loads(prior.read_text())
    Q=[{tuple(e):F(c) for e,c in p} for p in r['Q'][:8]]
    expected={tuple(e):F(c) for e,c in r['interior_K']['numerator']}
    powers=[]
    for p in Q:
        row=[{(0,0,0):F(1)}]
        for j in range(6):row.append(mul(row[-1],p))
        powers.append(row)
    substituted=add(*(scale(prod(*(powers[j][e[j]] for j in range(8))),c) for e,c in N.items()))
    assert substituted==expected

    # Gaussian normalized jets through order seven.
    a,u,unit={(1,0):F(1)},{(0,1):F(1)},{(0,0):F(1)}
    G=[unit]
    for j in range(7):G.append(add(der(G[-1],1),scale(prod(a,u,G[-1]),-2)))
    assert not numerators(G)[4]

    # Generic even source through u^10; verify all low coefficients exactly.
    source={tuple([2*j]+[int(i==j) for i in range(6)]):F(1) for j in range(6)}
    jets=[source]
    for j in range(7):jets.append(der(jets[-1],0))
    even_A,_,_,_,even_N=numerators(jets)
    assert all(e[0]%2==1 and e[0]>=1 for e in even_A)
    assert all(e[0]%2==1 and e[0]>=5 for e in even_N)

    print(json.dumps(dict(date='2026-11-01',prepared_for='Edward Baker',llm_assistance='substantial',
        model='gpt-6.1-sol',effort='ultra',task='J-E02',revision='r1',arithmetic='exact rational polynomials',
        code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        joint_N=old.serial(N),N_terms=29,N_coefficient_absolute_sum=76,
        checks=dict(A_derivative_B=True,W_derivative_W1=True,K_quotient_identity=True,
                    N_degree6_weight13=True,r2_K_state_numerator_identical=True,
                    Gaussian_N_zero=True,generic_even_A_u_and_N_u5=True),
        arithmetic_elapsed_seconds=time.monotonic()-start),indent=2)+'\n')


if __name__=='__main__':main()
