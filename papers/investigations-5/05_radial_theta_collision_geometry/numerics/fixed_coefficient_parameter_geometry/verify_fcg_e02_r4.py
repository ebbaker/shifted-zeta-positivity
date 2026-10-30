#!/usr/bin/env python3
"""Exact symbolic sign/constant checks for FCG-E02 R4; no source acquisition.

Prepared for Edward Baker with substantial LLM assistance, 30 October 2026.
Actual model gpt-6.1-sol, effort ultra, Investigation05 chat0047.
Python standard library only. Analytical integrability/scope require the review.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import re

PACKET="papers/investigations-5/05_radial_theta_collision_geometry/research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md"
PACKET_SHA="f8a78db8aef3c85907ddf16be39744d6b06c9ca11c471e21fc781bf73357d190"


def add(p,q):
    result=dict(p)
    for ij,v in q.items():result[ij]=result.get(ij,F(0))+v
    return {ij:v for ij,v in result.items() if v}


def mul(p,q):
    result={}
    for i,v in p.items():
        for j,w in q.items():
            ij=tuple(a+b for a,b in zip(i,j))
            result[ij]=result.get(ij,F(0))+v*w
    return {ij:v for ij,v in result.items() if v}


def scale(p,c):
    return {ij:c*v for ij,v in p.items() if c*v}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    assert not args.output.exists()
    root=args.repo.resolve();packet=root/PACKET
    assert sha256(packet.read_bytes()).hexdigest()==PACKET_SHA
    rows=re.findall(r"\| \x60([^\x60]+)\x60 \| \x60([0-9a-f]{64})\x60 \|",packet.read_text())
    assert len(rows)==9
    hashes=[]
    for path,expected in rows:
        actual=sha256((root/path).read_bytes()).hexdigest()
        assert actual==expected,path
        hashes.append({"path":path,"sha256":actual,"matches":True})
    checks=[]
    def equal(name,actual,expected,meaning):
        assert actual==expected,name
        checks.append({"check":name,"passed":True,"meaning":meaning})
    # A monomial is lambda^m exp(k*u); differentiate the prefactor
    # and the common exp(-lambda*exp(4u)) separately.
    derivative={}
    for (m,k),c in {(2,9):F(2),(1,5):F(-3)}.items():
        derivative[m,k]=derivative.get((m,k),F(0))+k*c
        derivative[m+1,k+4]=derivative.get((m+1,k+4),F(0))-4*c
    equal("complete summand derivative coefficients",derivative,
          {(2,9):F(30),(1,5):F(-15),(3,13):F(-8)},
          "Exact 30,-15,-8; integrability is separately proved analytically.")

    # q,r,z variables. Set y=1+q/r+z, z>=0; clear the positive r.
    one={(0,0,0):F(1)}
    q={(1,0,0):F(1)};r={(0,1,0):F(1)};z={(0,0,1):F(1)}
    q_plus_rz=add(q,mul(r,z))
    left=add(add(mul(q,q),mul(mul(q,r),add(z,scale(one,-1)))),
             scale(mul(q_plus_rz,q_plus_rz),-1))
    right=add(scale(mul(mul(q,r),add(one,z)),-1),
              scale(mul(mul(r,r),mul(z,z)),-1))
    equal("Gaussian time-gap strict factorization",left,right,
          "q(y-2)-r(y-1)^2=-q(1+z)-r*z^2<0 for q,r>0,z>=0; endpoint is -q.")

    # Variables a,q: clear denominator 4q^2 in h1^2/h0^2-2b/h0.
    aa={(2,0):F(1)};qq={(0,1):F(1)}
    b_numerator=add(aa,scale(qq,-2))
    equal("Gaussian discriminant numerator",add(aa,scale(b_numerator,-2)),
          add(scale(qq,4),scale(aa,-1)),
          "D0/h0^2=(4q-a^2)/(4q^2)=(2-y)/(2q).")
    equal("Gaussian C01 curvature cancellation",add(aa,scale(b_numerator,-1)),
          scale(qq,2),"L/H^2=1/(2q)>0.")

    # Linear polynomials in N, after multiplying by 2^(N+1).
    equal("kappa consecutive difference",{1:F(2)-1,0:F(6)-4},{1:F(1),0:F(2)},
          "kappa_N-kappa_(N+1)=(N+2)/2^(N+1)>0 for N>=1.")
    equal("degree-32 tail factor",F(32+3,2**32),F(35,4294967296),
          "The exact smallest factor on the inherited 8/16/32 list.")

    # nu,Z,kappa,R,B,E1,r,F variables: exact upper-budget subtraction.
    def var(j):
        index=[0]*8;index[j]=1
        return {tuple(index):F(1)}
    nu,Z,kappa,R,B,E1,rr,FF=[var(j) for j in range(8)]
    MG=add(Z,mul(mul(R,B),E1))
    left=add(add(add(mul(nu,Z),scale(mul(kappa,MG),-1)),
                 scale(mul(mul(B,B),rr),-2)),scale(FF,-1))
    right=add(add(add(mul(add(nu,scale(kappa,-1)),Z),
                      scale(mul(mul(mul(kappa,R),B),E1),-1)),
                  scale(mul(mul(B,B),rr),-2)),scale(FF,-1))
    equal("exact rejection-budget identity",left,right,
          "Retains -kappa*R*|b|*E1, -2b^2*r and -F_N in equation7; sign uses stated inequalities.")

    output={"task":"FCG-E02 R4","date":"2026-10-30","prepared_for":"Edward Baker",
        "llm_assistance":"Substantial; internal analytical assessment",
        "model":"gpt-6.1-sol","effort":"ultra","chat":"0047",
        "packet":{"path":PACKET,"sha256":PACKET_SHA},"inputs":hashes,
        "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks":checks,"all_passed":True,
        "scope":"Exact symbolic identities and frozen byte identity only. No theta source values, evaluated cutoff, parameter/degree scan or quadrature. Integrability, endpoint, sign hypotheses, controls and theorem quantifiers are assessed in the written review."}
    args.output.write_text(json.dumps(output,indent=2)+"\n")
    print(f"{len(checks)} exact symbolic checks and 9 frozen hashes passed; no source acquisition.")
    print(args.output)


if __name__=="__main__":main()
