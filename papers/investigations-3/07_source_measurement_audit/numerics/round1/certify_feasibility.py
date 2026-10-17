#!/usr/bin/env python3
"""Outward-rounded feasibility, Farkas and equality-distance checks.

Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Recorded model gpt-6.1-sol, reasoning effort ultra. Uses certified jet balls
and independently produced rational decimal separating witnesses.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb,arb_mat,ctx

def bs(v):return v.str(65,more=True)
def dot(u,v):return sum((a*b for a,b in zip(u,v)),arb(0))

def certify(evaluation,candidates,output):
    ctx.prec=448
    raw=json.loads(evaluation.read_text()); cand=json.loads(candidates.read_text())
    cases={(c['t'],c['x']):c for c in raw['cases']}
    beta=[(4*arb.pi()*n*n-1)*(-arb.pi()*n*n).exp() for n in range(1,7)]
    result={'schema':'source_measurement_feasibility_ball_v1','date':'2026-10-17',
            'prepared_for':'Edward Baker','model':'gpt-6.1-sol','reasoning_effort':'ultra',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'evaluation_sha256':hashlib.sha256(evaluation.read_bytes()).hexdigest(),
            'floating_witnesses_sha256':hashlib.sha256(candidates.read_bytes()).hexdigest(),
            'precision_bits':448,'cases':[]}
    for c in cand['cases']:
        rawcase=cases[(c['t'],c['x'])];B=[[arb(v) for v in row] for row in rawcase['B']]
        h=[arb(v) for v in rawcase['h']];N=c['N'];anchor=c['anchor_a1'];theta=c['tail']=='theta'
        free=list(range(1 if anchor else 0,N)); k=len(free)
        tailbeta=arb(1)/2-sum(beta[:N],arb(0)) if theta else arb(0)
        tailjet=[h[j]-sum(B[j][:N],arb(0)) if theta else arb(0) for j in (0,1)]
        mass=arb(1)/2-tailbeta-(beta[0] if anchor else 0)
        target=[-tailjet[j]-(B[j][0] if anchor else 0) for j in (0,1)]
        assert mass>0
        pn=[[B[j][n]/beta[n] for j in (0,1)] for n in free]
        q=[v/mass for v in target]
        out={key:c[key] for key in ('point_id','t','x','N','tail','anchor_a1')}
        if k<3:
            spec=c['equality']['augmented_minor']; rr=spec['row_indices']
            cols=[p+[arb(1)] for p in pn]+[q+[arb(1)]]
            minor=arb_mat([[col[r] for col in cols] for r in rr]).det()
            assert not minor.contains(0),('unresolved equality minor',out)
            out['equality_status']='certified_infeasible'
            out['augmented_minor']=bs(minor)
        else:
            # Exact equality projection in delta coordinates. Its Gram inverse
            # identity proves stationarity; interval evaluation encloses the
            # corresponding real minimizer, without treating a residual as proof.
            E=arb_mat([[B[0][n] for n in free],[B[1][n] for n in free],[beta[n] for n in free]])
            rhs=arb_mat([[-h[0] if theta else -sum(B[0][:N],arb(0))],
                         [-h[1] if theta else -sum(B[1][:N],arb(0))],
                         [0 if theta else arb(1)/2-sum(beta[:N],arb(0))]])
            G=E*E.transpose();inv=G.inv();dual=inv*rhs;d=E.transpose()*dual
            delta=[arb(0) for _ in range(N)]
            for j,n in enumerate(free):delta[n]=d[j,0]
            coefficients=[1+v for v in delta]
            norm=dot(delta,delta).sqrt()
            weighted=dot(beta[:N],[abs(v) for v in delta])
            if not theta:weighted+=arb(1)/2-sum(beta[:N],arb(0))
            source_endpoint=arb(0)
            for n in range(1,N+1):
                lam=arb.pi()*n*n
                mode_endpoint=(-lam).exp()*(-8*lam**3+30*lam**2-15*lam)
                source_endpoint+=(delta[n-1] if theta else coefficients[n-1])*mode_endpoint
            out.update({'equality_status':'certified_feasible',
                        'a_first_N':[bs(v) for v in coefficients],
                        'first_N_euclidean_minimum':bs(norm),
                        'full_raw_l2_distance':bs(norm) if theta else 'infinity (fixed zero tail compared with theta)',
                        'full_beta_l1_at_euclidean_minimizer':bs(weighted),
                        'weighted_metric_optimized':False,
                        'source_first_odd_endpoint_at_euclidean_minimizer':bs(source_endpoint),
                        'stationarity_basis':'delta=E^T(EE^T)^-1 rhs with verified inverse',
                        'positive_equality_minimizer':all(v>0 for v in coefficients)})
        pos=c['positive']
        if 'strict_farkas_separator' in pos:
            y=[arb(s) for s in pos['strict_farkas_separator']['normalized_point_multiplier']]
            slacks=[dot(y,p+[arb(1)]) for p in pn]; target_value=dot(y,q+[arb(1)])
            assert all(s>0 for s in slacks) and target_value<0,('unresolved Farkas witness',out)
            out.update({'positive_status':'certified_infeasible',
                        'farkas_multiplier_decimal':[s for s in pos['strict_farkas_separator']['normalized_point_multiplier']],
                        'column_slacks':[bs(v) for v in slacks],
                        'target_value':bs(target_value)})
        else:
            assert out['equality_status']=='certified_feasible' and out['positive_equality_minimizer'],out
            out['positive_status']='certified_feasible_and_euclidean_optimal'
        result['cases'].append(out)
        print(c['t'],N,c['tail'],anchor,out['equality_status'],out['positive_status'],flush=True)
    result['totals']={
        'cases':len(result['cases']),
        'equality_feasible':sum(c['equality_status']=='certified_feasible' for c in result['cases']),
        'positive_feasible':sum(c['positive_status']=='certified_feasible_and_euclidean_optimal' for c in result['cases']),
        'positive_infeasible':sum(c['positive_status']=='certified_infeasible' for c in result['cases'])}
    output.write_text(json.dumps(result,indent=2)+'\n');print(result['totals'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--evaluation',type=Path,required=True)
    p.add_argument('--candidates',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();certify(a.evaluation,a.candidates,a.output)
