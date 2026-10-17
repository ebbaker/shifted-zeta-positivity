#!/usr/bin/env python3
"""Validate fixed-space constants and actual equality distances from jet balls.

16 October 2026, prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6.1-sol; effort ultra. The independent floating producer
uses QR/SVD; this secondary outward-rounded check uses exact Gram identities.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import flint
from flint import arb, arb_mat, ctx

def bs(x):return x.str(65,more=True)

def phi(n,u):
    q=arb.pi()*n*n*(4*u).exp()
    return (u-q).exp()*(2*q*q-3*q)

def rows(design):
    if design=='recurrence':
        return arb_mat([[sum(c for idx,c in ((k-1,1),(k,-2),(k+1,1)) if idx==n)
                         for n in range(1,7)] for k in range(1,8)])
    return arb_mat([[phi(n,arb(j)/20)-phi(n,-arb(j)/20) for n in range(1,7)]
                    for j in range(1,13)])

def basis(beta,anchor):
    pivot=1 if anchor else 0
    free=list(range(pivot+1,6))
    Q=arb_mat(6,len(free))
    for j,n in enumerate(free):Q[n,j]=1;Q[pivot,j]=-beta[n]/beta[pivot]
    return Q

def build(source,output):
    ctx.prec=448; raw=json.loads(source.read_text())
    beta=[(4*arb.pi()*n*n-1)*(-arb.pi()*n*n).exp() for n in range(1,7)]
    out={'schema':'source_measurement_constants_ball_v1','date':'2026-10-16',
         'prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
         'python_flint_version':flint.__version__,'precision_bits':448,
         'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'evaluation_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'method':'validated Gram identity secondary to independent QR/SVD floating producer',
         'rows':[]}
    for case in raw['cases']:
        B=arb_mat([[arb(v) for v in row] for row in case['B']]);h=arb_mat([[arb(v)] for v in case['h']])
        hnorm=(h[0,0]**2+h[1,0]**2).sqrt()
        for anchor in (False,True):
            Q=basis(beta,anchor); X=B*Q
            for design in ('recurrence','reflection'):
                M=rows(design);D=M*Q;G=D.transpose()*D
                Ginv=G.inv();S=X*Ginv*X.transpose()
                off=(S[0,1]+S[1,0])/2
                determinant=S[0,0]*S[1,1]-off**2
                assert S[0,0]>0 and determinant>0,('jet rank not certified',case['id'],anchor,design)
                eig=(S[0,0]+S[1,1]+((S[0,0]-S[1,1])**2+4*off**2).sqrt())/2
                C=eig.sqrt();eta=hnorm/C
                Sinv=S.inv();r=(h.transpose()*Sinv*h)[0,0].sqrt()
                delta=-(Q*Ginv*X.transpose()*Sinv*h)
                positive=all(1+delta[n,0]>0 for n in range(6))
                negative=any(1+delta[n,0]<0 for n in range(6))
                out['rows'].append({'id':case['id'],'t':case['t'],'x':case['x'],
                    'anchor':anchor,'design':design,'h_norm':bs(hnorm),'C':bs(C),'eta':bs(eta),
                    'actual_unconstrained_measurement_distance':bs(r),
                    'distance_over_sufficient_radius':bs(r/eta),
                    'measurement_gram_invertible':True,'two_jet_rank':2,
                    'delta_at_measurement_minimum':[bs(delta[n,0]) for n in range(6)],
                    'minimizer_positive':positive,'minimizer_has_negative_coefficient':negative,
                    'measurement_error_model':'absolute Euclidean norm of unscaled observation rows'})
                print(case['id'],anchor,design,'C',C.str(9),'eta',eta.str(9),'r/eta',(r/eta).str(9),'positive',positive,flush=True)
    output.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--evaluation',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();build(a.evaluation,a.output)
