#!/usr/bin/env python3
"""Preassigned proportional Gaussian full-source filter on genuine branches.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded parent-session model gpt-6.1-sol, reasoning effort ultra.
Standard library, exact Fraction arithmetic; no new quadrature.
Fixed protocol: delta(t)=t/2, lambda=1/2, a=pi/16, b=1/4,
K0=K1=0, all 16 branch/slab cases for t in the closed interval [0,1/2].
Even original slab indices develop; odd indices hold out. Nothing is fitted.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import platform

RECORD_SHA256='aee1f000150a90e1269faa9a8cfafa6251d581ec0f586f0b09d554ef8822741d'
LX,LT=12,8
ZERO=(Q(0),Q(0))

def require(ok,message):
    if not ok: raise ValueError(message)
def digest(p): return sha256(p.read_bytes()).hexdigest()
def dy(v):
    require(isinstance(v,list) and len(v)==2 and isinstance(v[1],int),'dyadic shape')
    require(abs(v[1])<10000,'bounded exponent')
    return Q(int(v[0]))*Q(2)**v[1]
def iv(v):
    require(isinstance(v,list) and len(v)==2,'interval shape')
    z=tuple(map(dy,v));require(z[0]<=z[1],'ordered interval');return z
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def scale(a,q):
    q=Q(q);return (q*a[0],q*a[1]) if q>=0 else (q*a[1],q*a[0])
def power(a,k):
    require(isinstance(k,int) and k>=0,'nonnegative integral power')
    if k==0:return Q(1),Q(1)
    if k%2:return a[0]**k,a[1]**k
    return (Q(0) if a[0]<=0<=a[1] else min(a[0]**k,a[1]**k),max(a[0]**k,a[1]**k))
def sym(q):
    require(q>=0,'nonnegative payment');return -q,q
def intersect(a,b):
    z=(max(a[0],b[0]),min(a[1],b[1]));require(z[0]<=z[1],'nonempty enclosure intersection');return z
def encode(v):return [str(v[0]),str(v[1])]
def verdict(v):return 'CERTIFIED_POSITIVE' if v[0]>0 else ('CERTIFIED_NEGATIVE' if v[1]<0 else 'UNDECIDED')
def cjets(z,a,mu):
    return [sub(sub(neg(z[k+2]),mul(scale(a,2),z[k+1])),mul(mu,z[k])) for k in range(len(z)-2)]
def tensor(z,j,alpha=Q(1),offset=Q(0)):
    """Exact binomial substitution dt_original=alpha*dt_current+offset.

    Row (p,m) multiplies dt_current**p * eta**m. Form source coefficient
    differences BEFORE ranging the common variables, retaining cross-time
    correlation in the finite polynomial. No higher jets are accessed.
    """
    require(j+2*(LT-1)+(LX-1)<len(z),'sufficient high jets')
    out=[[ZERO for _ in range(LX)] for _ in range(LT)]
    for ell in range(LT):
      for p in range(ell+1):
        factor=Q((-1)**ell*comb(ell,p),factorial(ell))*alpha**p*offset**(ell-p)
        for m in range(LX):
          out[p][m]=add(out[p][m],scale(z[j+2*ell+m],factor/factorial(m)))
    return out
def combine(cur,prior,weight):
    return [[sub(cur[p][m],scale(prior[p][m],weight)) for m in range(LX)] for p in range(LT)]
def evaluate(coeff,eta,dt):
    ep=[power(eta,m) for m in range(LX)];tp=[power(dt,p) for p in range(LT)]
    answer=ZERO
    for p in range(LT):
      for m in range(LX): answer=add(answer,mul(coeff[p][m],mul(tp[p],ep[m])))
    return answer
def payment(row,j):
    require(0<=j<len(row['jet_space_payments']) and j<len(row['jet_time_payments']),'payment index')
    s,t=iv(row['jet_space_payments'][j]),iv(row['jet_time_payments'][j])
    require(s[0]>=0 and t[0]>=0,'nonnegative source payments')
    return s[1]+t[1]
def cpayment(row,j,a,mu):
    return payment(row,j+2)+2*a[1]*payment(row,j+1)+mu[1]*payment(row,j)
def endpoint(row,z,j,side):
    eta=(Q(side,2),Q(side,2));dt=sym(Q(1,32))
    return add(evaluate(tensor(z,j),eta,dt),sym(payment(row,j)))

def run(args):
    require(digest(args.record)==RECORD_SHA256,'fixed original record hash')
    r=json.loads(args.record.read_text())
    require(r['schema']=='inv21_phase_centered_complete_source_pilot_v1','original schema')
    require(r['status']=='PASS' and r['failed_cells']==[],'original record passes')
    require(digest(args.original_driver)==r['script_sha256'],'original driver hash')
    require(args.contour_source.name==r['imported_source_name'],'original contour name')
    require(digest(args.contour_source)==r['imported_source_sha256'],'original contour hash')
    require(r['domain']=={'x':['100','104'],'t':['0','1/2']},'original domain')
    require(r['space_order']==LX and r['time_order']==LT and r['time_slabs']==8 and r['width']=='1','fixed original orders')
    cells=r['cells'];require(len(cells)==r['cell_count']==32,'32 original cells')
    expected={((str(x),str(x+1)),(str(Q(k,16)),str(Q(k+1,16)))) for x in range(100,104) for k in range(8)}
    actual=[(tuple(v['x']),tuple(v['t'])) for v in cells]
    require(len(set(actual))==32 and set(actual)==expected,'exact unique closed original partition')
    lookup={key:row for key,row in zip(actual,cells)}
    for row in cells:
      require(len(row['center_jets'])==29 and len(row['whole_cell_jets'])==4,'original jets through 28 and whole jets through 3')
      require(len(row['jet_space_payments'])==len(row['jet_time_payments'])==4,'original payments through 3')
      for key in ('center_jets','whole_cell_jets','jet_space_payments','jet_time_payments'):
        for val in row[key]:iv(val)
      require(row['normalization']=='e^(pi*xc/8), constant across cell','time independent normalization')
    a=iv(r['a']);require(a[0]>0,'positive a');mu=add(power(a,2),(Q(1,16),Q(1,16)))
    lam=Q(1,2);eta=sym(Q(1,2));dt=sym(Q(1,32));rows=[];summary=Counter()
    for j,xl in [(0,101),(1,103)]:
      for k in range(8):
        key=((str(xl),str(xl+1)),(str(Q(k,16)),str(Q(k+1,16))))
        row=lookup[key];pk=k//2
        pkey=(key[0],(str(Q(pk,16)),str(Q(pk+1,16))))
        prior=lookup[pkey];current_t=tuple(map(Q,row['t']));earlier_t=tuple(t/2 for t in current_t)
        prior_t=tuple(map(Q,prior['t']));tc=sum(current_t)/2;pc=sum(prior_t)/2
        offset=tc/2-pc
        require(offset==Q(-1 if k%2==0 else 1,64),'even/odd earlier-center offset')
        prior_dt=add(scale(dt,Q(1,2)),(offset,offset))
        require(prior_dt==(earlier_t[0]-pc,earlier_t[1]-pc),'exact affine time map')
        require(prior_t[0]<=earlier_t[0]<=earlier_t[1]<=prior_t[1] and max(map(abs,prior_dt))<=Q(1,32),'earlier half slab lies in paid prior cell')
        require(row['x']==prior['x'] and row['normalization']==prior['normalization'],'common positive normalization')
        zcur=list(map(iv,row['center_jets']));zprior=list(map(iv,prior['center_jets']));Z=list(map(iv,row['whole_cell_jets']))
        left,right=endpoint(row,zcur,j+1,-1),endpoint(row,zcur,j+1,1)
        if j==0:require(left[0]>0 and right[1]<0 and Z[j+2][1]<0,'genuine unique current h1 branch for every t')
        else:require(left[1]<0 and right[0]>0 and Z[j+2][0]>0,'genuine unique current h2 branch for every t')
        Ccur,Cprior=cjets(zcur,a,mu),cjets(zprior,a,mu)
        Tcur=tensor(Ccur,j);Tprior=tensor(Cprior,j,Q(1,2),offset)
        Pcur,Pprior=cpayment(row,j,a,mu),cpayment(prior,j,a,mu)
        G=add(evaluate(Tprior,eta,dt),sym(Pprior))
        Rsource=add(evaluate(combine(Tcur,Tprior,1),eta,dt),sym(Pcur+Pprior))
        Bsource=add(evaluate(combine(Tcur,Tprior,1-lam),eta,dt),sym(Pcur+(1-lam)*Pprior))
        Cstat=sub(neg(Z[j+2]),mul(mu,Z[j]))
        Rstat=intersect(Rsource,sub(Cstat,G));Bstat=intersect(Bsource,sub(Cstat,scale(G,1-lam)))
        favorable=mul(Z[j],G);residual=mul(Z[j],Rstat);absorption=mul(Z[j],Bstat)
        vf,vr,va=map(verdict,(favorable,residual,absorption))
        result=('CERTIFIED_PASS' if vf==va=='CERTIFIED_POSITIVE' else ('CERTIFIED_FAIL' if 'CERTIFIED_NEGATIVE' in (vf,va) else 'UNDECIDED'))
        role='holdout' if k%2 else 'development';summary[f'j{j}:{role}:{vf}:{vr}:{va}:{result}']+=1
        rows.append({'j':j,'slab':k,'role':role,'x':row['x'],'t':row['t'],'earlier_t':list(map(str,earlier_t)),
          'prior_original_slab':pk,'prior_original_t':prior['t'],'prior_center_displacement':encode(prior_dt),'affine_offset':str(offset),
          'normalization':row['normalization'],'current_left_stationary_derivative':encode(left),'current_right_stationary_derivative':encode(right),
          'current_monotonic_derivative':encode(Z[j+2]),'current_hj':encode(Z[j]),'stationary_full_C':encode(Cstat),'whole_cell_G':encode(G),
          'whole_cell_R_source':encode(Rsource),'whole_cell_absorption_source':encode(Bsource),'stationary_R':encode(Rstat),
          'stationary_absorption_factor':encode(Bstat),'h_G':encode(favorable),'h_R':encode(residual),'h_R_plus_lambda_h_G':encode(absorption),
          'current_C_payment':str(Pcur),'prior_C_payment':str(Pprior),'favorable_verdict':vf,'residual_verdict':vr,'absorption_verdict':va,
          'fixed_K_zero_criterion_verdict':result,'fixed_K_zero_criterion_passed':result=='CERTIFIED_PASS',
          'display_only':{name:[float(v[0]),float(v[1])] for name,v in [('hG',favorable),('hR',residual),('absorption',absorption)]}})
    require(len(rows)==16,'all 16 prescribed cases')
    result={'schema':'inv21_proportional_gaussian_source_filter_pilot_v1','date':'2026-10-14','prepared_for':'Edward Baker',
      'llm_assistance':'Substantial','recorded_model':'gpt-6.1-sol','recorded_effort':'ultra','status':'COMPLETED',
      'script_name':Path(__file__).name,'script_sha256':digest(Path(__file__)),'python':platform.python_version(),
      'arithmetic':'Exact fractions.Fraction endpoint arithmetic; floats occur only in display_only fields.',
      'input_record_name':args.record.name,'input_record_sha256':digest(args.record),
      'input_driver_name':args.original_driver.name,'input_driver_sha256':digest(args.original_driver),
      'input_contour_name':args.contour_source.name,'input_contour_sha256':digest(args.contour_source),
      'protocol':{'delta':'t/2','earlier_time':'t/2','lambda':'1/2','a':'pi/16','b':'1/4','K0':0,'K1':0,
        'tested_slabs':list(range(8)),'development_slabs':[0,2,4,6],'holdout_slabs':[1,3,5,7],
        'changed_after_observing_results':False},'a':encode(a),'mu':encode(mu),
      'exact_source_identity':'For each fixed t, multiplying the complete shifted source by q_t(z)=exp(-t*z^2/2) changes H(t,x) to H(t/2,x). With fixed a,b, G_j=C_j(t/2,x) and R_j=C_j(t,x)-G_j exactly.',
      'boundary_compatibility':'q_t(iy)=exp(t*y^2/2) is real and q_t is even; the complete-source contour identity is retained for each fixed t.',
      'scope':'Both current genuine stationary branches, j0 x in [101,102] and j1 x in [103,104], on all 8 original closed slabs covering t in [0,1/2].',
      'transport':'Prior original slab floor(k/2); prior displacement equals current displacement/2 plus (-1)^k*(-1/64). Exact binomial substitution forms common-variable coefficient differences before interval evaluation. Original full paid spatial and temporal source remainders retained separately for current and prior cells.',
      'product_criterion':'h_j G_j>=0 and h_j(R_j+lambda G_j)>=0 imply L_j>=0 on the current h_(j+1)=0 branch with prescribed K_j=0.',
      'summary':dict(summary),'row_count':len(rows),'rows':rows,
      'minimum_lower_endpoints':{name:str(min(Q(row[field][0]) for row in rows)) for name,field in [('hG','h_G'),('hR','h_R'),('absorption','h_R_plus_lambda_h_G')]},
      'limitations':['Original full-source center enclosures, whole-cell jets, quadrature and analytic tail lemmas are trusted inputs; no new quadrature or formal source verification is performed.',
        'Gaussian source filter is noncompact and preassigned; no filter, constant, physical jet, or energy floor is fitted.',
        'Only current stationarity is imposed; the earlier point is not assumed stationary.',
        'All integrated cross terms remain in the source identity. Finite cells establish no arbitrary-height comparison or behavior near an unknown collision.',
        'A certified negative required product refutes that specified product condition on a nonempty current branch. An interval crossing zero is undecided; it does not establish a zero or failure.',
        'At t=0 the exact source remainder is zero by identity; a slab enclosure containing t=0 need not isolate that endpoint equality.']}
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'summary':dict(summary),'cases':len(rows),'output':str(args.output),'display_only_rows':[{'j':v['j'],'slab':v['slab'],**v['display_only'],'criterion':v['fixed_K_zero_criterion_verdict']} for v in rows]},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',required=True,type=Path);p.add_argument('--original-driver',required=True,type=Path)
    p.add_argument('--contour-source',required=True,type=Path);p.add_argument('--output',required=True,type=Path)
    run(p.parse_args())
