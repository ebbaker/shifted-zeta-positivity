#!/usr/bin/env python3
"""Fixed Gaussian source filter on both genuine stationary branches.

Prepared for Edward Baker, 2026-10-14; substantial LLM assistance.
Recorded inherited model gpt-6-astra, effort ultra. Standard library only.
Protocol fixed before evaluation: delta=1/16, lambda=1/2, a=pi/16,
b=1/4, K0=K1=0, all 14 branch/slab cases for t in [1/16,1/2].
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform


def require(ok,message):
    if not ok: raise ValueError(message)
def digest(p): return sha256(p.read_bytes()).hexdigest()
def dy(v):return Q(int(v[0]))*Q(2)**v[1]
def iv(v):
    z=tuple(map(dy,v));require(z[0]<=z[1],'ordered dyadic interval');return z
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def scale(a,q):return mul(a,(Q(q),Q(q)))
def power(a,k):
    z=(Q(1),Q(1))
    for _ in range(k):z=mul(z,a)
    return z
def sym(q):return -q,q
def intersect(a,b):
    z=(max(a[0],b[0]),min(a[1],b[1]));require(z[0]<=z[1],'nonempty stationary intersection');return z
def encode(v):return [str(v[0]),str(v[1])]
def verdict(v):return 'CERTIFIED_POSITIVE' if v[0]>0 else ('CERTIFIED_NEGATIVE' if v[1]<0 else 'UNDECIDED')
def cjets(row,a,mu):
    z=list(map(iv,row['center_jets']))
    return [sub(sub(neg(z[k+2]),mul(scale(a,2),z[k+1])),mul(mu,z[k])) for k in range(len(z)-2)]
def polynomial(z,j,eta,delta):
    val=(Q(0),Q(0))
    for ell in range(8):
        space=(Q(0),Q(0))
        for m in range(12):
            space=add(space,scale(mul(power(eta,m),z[j+2*ell+m]),Q(1,factorial(m))))
        val=add(val,scale(mul(power(neg(delta),ell),space),Q(1,factorial(ell))))
    return val
def payment(row,j):
    return iv(row['jet_space_payments'][j])[1]+iv(row['jet_time_payments'][j])[1]
def cpayment(row,j,a,mu):
    return payment(row,j+2)+2*a[1]*payment(row,j+1)+mu[1]*payment(row,j)
def endpoint(row,j,side):
    z=list(map(iv,row['center_jets']))
    q=Q(side,2);val=polynomial(z,j,(q,q),sym(Q(1,32)))
    return add(val,sym(payment(row,j)))


def run(args):
    r=json.loads(args.record.read_text())
    require(r['status']=='PASS' and not r['failed_cells'],'source record passes')
    require(digest(args.original_driver)==r['script_sha256'],'original driver hash')
    require(digest(args.contour_source)==r['imported_source_sha256'],'contour source hash')
    require(r['space_order']==12 and r['time_order']==8 and r['time_slabs']==8,'fixed original orders')
    a=iv(r['a']);mu=add(power(a,2),(Q(1,16),Q(1,16)))
    delta_shift=Q(1,16);lam=Q(1,2);eta=sym(Q(1,2));dt=sym(Q(1,32))
    rows=[];summary=Counter()
    for j,xl in [(0,101),(1,103)]:
      cells=[row for row in r['cells'] if row['x']==[str(xl),str(xl+1)]]
      require(len(cells)==8,'eight cells on each branch')
      for k in range(1,8):
        row,prior=cells[k],cells[k-1]
        require(list(map(Q,row['t']))==[Q(k,16),Q(k+1,16)],'current time slab')
        require([Q(v)+delta_shift for v in prior['t']]==list(map(Q,row['t'])),'exact shifted time cell')
        Z=list(map(iv,row['whole_cell_jets']))
        left,right=endpoint(row,j+1,-1),endpoint(row,j+1,1)
        if j==0:require(left[0]>0 and right[1]<0 and Z[2][1]<0,'current unique genuine h1 branch')
        else:require(left[1]<0 and right[0]>0 and Z[3][0]>0,'current unique genuine h2 branch')
        Ccur,Cprev=cjets(row,a,mu),cjets(prior,a,mu)
        Rcenter=[sub(x,y) for x,y in zip(Ccur,Cprev)]
        Bcenter=[sub(x,scale(y,1-lam)) for x,y in zip(Ccur,Cprev)]
        Pcur,Pprev=cpayment(row,j,a,mu),cpayment(prior,j,a,mu)
        G=add(polynomial(Cprev,j,eta,dt),sym(Pprev))
        Rsource=add(polynomial(Rcenter,j,eta,dt),sym(Pcur+Pprev))
        Bsource=add(polynomial(Bcenter,j,eta,dt),sym(Pcur+(1-lam)*Pprev))
        Cstat=sub(neg(Z[j+2]),mul(mu,Z[j]))
        Rstat=intersect(Rsource,sub(Cstat,G))
        Bstat=intersect(Bsource,sub(Cstat,scale(G,1-lam)))
        favorable=mul(Z[j],G);residual=mul(Z[j],Rstat);absorption=mul(Z[j],Bstat)
        vf,vr,va=map(verdict,(favorable,residual,absorption))
        good=(vf=='CERTIFIED_POSITIVE' and va=='CERTIFIED_POSITIVE')
        label='holdout' if k%2 else 'development'
        summary[f'j{j}:{label}:favorable={vf},residual={vr},absorption={va}']+=1
        rows.append({'j':j,'slab':k,'role':label,'x':row['x'],'t':row['t'],'shifted_t':prior['t'],
            'normalization':row['normalization'],'current_left_stationary_derivative':encode(left),
            'current_right_stationary_derivative':encode(right),'current_monotonic_derivative':encode(Z[j+2]),
            'current_hj':encode(Z[j]),'stationary_full_C':encode(Cstat),'whole_cell_G':encode(G),
            'whole_cell_R_source':encode(Rsource),'whole_cell_absorption_source':encode(Bsource),
            'stationary_R':encode(Rstat),'stationary_absorption_factor':encode(Bstat),
            'h_G':encode(favorable),'h_R':encode(residual),'h_R_plus_lambda_h_G':encode(absorption),
            'current_C_payment':str(Pcur),'prior_C_payment':str(Pprev),
            'favorable_verdict':vf,'residual_verdict':vr,'absorption_verdict':va,
            'fixed_K_zero_criterion_passed':good,
            'display_only':{name:[float(v[0]),float(v[1])] for name,v in [('hG',favorable),('hR',residual),('absorption',absorption)]}})
    result={'schema':'inv21_fixed_gaussian_source_filter_pilot_v1','date':'2026-10-14','prepared_for':'Edward Baker',
      'llm_assistance':'Substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra','status':'COMPLETED',
      'script_sha256':digest(Path(__file__)),'python':platform.python_version(),
      'input_record_name':args.record.name,'input_record_sha256':digest(args.record),
      'input_driver_name':args.original_driver.name,'input_driver_sha256':digest(args.original_driver),
      'input_contour_name':args.contour_source.name,'input_contour_sha256':digest(args.contour_source),
      'protocol':{'delta':'1/16','lambda':'1/2','a':'pi/16','b':'1/4','K0':0,'K1':0,
        'tested_slabs':[1,2,3,4,5,6,7],'development_slabs':[2,4,6],'holdout_slabs':[1,3,5,7],
        'changed_after_observing_results':False},
      'a':encode(a),'mu':encode(mu),
      'exact_source_identity':'Multiplying the complete shifted source by q_delta(z)=exp(-delta*z^2) changes H(t,x) to H(t-delta,x). With fixed a,b, G_j=C_j(t-delta,x) and R_j=C_j(t,x)-G_j exactly.',
      'boundary_compatibility':'q_delta(iy)=exp(delta*y^2) is real; multiplying the complete theta source preserves its evenness and real values on the imaginary segment, so its complete-source contour identity remains valid.',
      'scope':'Both current genuine stationary branches, x in [101,102] for j0 and [103,104] for j1; t in [1/16,1/2].',
      'transport':'Current and preceding cell centers differ by exactly delta in time. Their Taylor polynomials use the same displacement. Center differences are formed before transport. R payment=current+prior; absorption payment=current+(1-lambda)*prior. Every original full-source center and transport tail is paid.',
      'product_criterion':'h_j G_j>=0 and h_j(R_j+lambda G_j)>=0 imply L_j>=0 on current h_(j+1)=0 with prescribed K_j=0.',
      'summary':dict(summary),'row_count':len(rows),'rows':rows,
      'limitations':['No new quadrature is performed; original full-source intervals and analytic tail lemmas remain trusted inputs.',
        'Gaussian filter is noncompact and fixed before evaluation; no filter or loss is fitted using physical jets or an energy floor.',
        'The earlier-time observation G is not assumed to be at an earlier-time stationary point; only current stationarity is imposed.',
        'Products retain the full integrated cross terms. These finite cells do not prove an all-height time-delay comparison or a bound near an unknown collision.',
        'A negative product enclosure disproves the specified condition on that nonempty current branch; an enclosure crossing zero is only undecided.']}
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'summary':dict(summary),'cases':len(rows),'output':str(args.output)},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',required=True,type=Path);p.add_argument('--original-driver',required=True,type=Path);p.add_argument('--contour-source',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    run(p.parse_args())
