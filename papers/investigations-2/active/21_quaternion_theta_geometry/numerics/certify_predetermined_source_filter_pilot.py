#!/usr/bin/env python3
"""Proper fixed-source filter pilot on both genuine stationary branches.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded inherited model gpt-6-astra, reasoning effort ultra.
Predeclared family: N in {1,2}, U in {1,3/2}, a=pi/16, b=1/4,
lambda=1/2, K_0=K_1=0; even slabs development, odd slabs holdout.
All four filters are retained irrespective of outcome.
"""
import argparse
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from math import factorial
from pathlib import Path
import platform
import time
import flint
from flint import arb,ctx


def require(ok,message):
    if not ok: raise RuntimeError(message)

def digest(path): return sha256(path.read_bytes()).hexdigest()
def rat(q):
    q=Q(q);return arb(q.numerator)/q.denominator

def decode(encoded):
    pts=[arb(int(m))*arb(2)**e for m,e in encoded]
    return (pts[0]+pts[1])/2+arb(0,((pts[1]-pts[0])/2).upper())

def enc(v):
    require(v.is_finite(),'finite output interval')
    def dy(z):
        m,e=z.man_exp();return [str(m),int(e)]
    return [dy(v.lower()),dy(v.upper())]

def sym(v):return arb(0,v.upper())
def ipow(v,n):
    q=arb(1)
    for _ in range(n):q*=v
    return q

def transport_poly(center,j,dx,dt,lx=12,lt=8):
    eta=sym(dx) if isinstance(dx,arb) else rat(dx)
    delta=sym(dt)
    value=arb(0)
    for ell in range(lt):
        value+=ipow(-delta,ell)/factorial(ell)*sum(ipow(eta,m)/factorial(m)*center[j+2*ell+m] for m in range(lx))
    return value

def remainder(row,kind,j):return decode(row['jet_'+kind+'_payments'][j]).upper()
def combined_remainder(row,kind,j,a,mu):
    return remainder(row,kind,j+2)+2*a*remainder(row,kind,j+1)+mu*remainder(row,kind,j)

def joint(a,b):
    lo=max(a.lower(),b.lower());hi=min(a.upper(),b.upper())
    require(lo<=hi,'nonempty intersection of valid stationary enclosures')
    return (lo+hi)/2+sym((hi-lo)/2)

def verdict(v):
    return 'CERTIFIED_POSITIVE' if v.lower()>0 else ('CERTIFIED_NEGATIVE' if v.upper()<0 else 'UNDECIDED')

def run(args):
    started=time.monotonic();ctx.prec=args.bits
    require(args.bits>=192,'precision at least 192')
    r=json.loads(args.record.read_text())
    require(r['status']=='PASS' and not r['failed_cells'],'input certificate passes')
    require(digest(args.original_driver)==r['script_sha256'],'input driver binding')
    require(digest(args.contour_source)==r['imported_source_sha256'],'input contour binding')
    require(r['N']==8 and r['U']=='3/2' and r['space_order']==12 and r['time_order']==8,'inherited full-moment support and orders')
    spec=importlib.util.spec_from_file_location('filter_pilot_contour',args.contour_source)
    source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
    a=arb.pi()/16;b=arb(1)/4;mu=a*a+b*b;lam=arb(1)/2
    c=arb.pi()/8;tol=arb(2)**(-(args.bits-64))
    family=[(1,Q(1)),(1,Q(3,2)),(2,Q(1)),(2,Q(3,2))]
    all_rows=[];branches=[];summary={}
    for j,xl in [(0,101),(1,103)]:
      cells=[row for row in r['cells'] if row['x']==[str(xl),str(xl+1)]]
      require(len(cells)==8,'eight cells per branch')
      for slab,row in enumerate(cells):
        tl,tr=map(Q,row['t']);tc=(tl+tr)/2;dt=rat((tr-tl)/2);X=arb(2*xl+1)/2;dx=arb(1)/2
        require((tl,tr)==(Q(slab,16),Q(slab+1,16)),'declared slab ordering')
        full=[decode(z) for z in row['center_jets']]
        Z=[decode(z) for z in row['whole_cell_jets']]
        endpoint=[]
        for side in (Q(-1,2),Q(1,2)):
            value=transport_poly(full,j+1,side,dt)+sym(remainder(row,'space',j+1)+remainder(row,'time',j+1))
            endpoint.append(value)
        if j==0:
            require(endpoint[0].lower()>0 and endpoint[1].upper()<0 and Z[2].upper()<0,'genuine unique h1 branch')
        else:
            require(endpoint[0].upper()<0 and endpoint[1].lower()>0 and Z[3].lower()>0,'genuine unique h2 branch')
        branches.append({'j':j,'x':row['x'],'t':row['t'],'left_stationary_derivative':enc(endpoint[0]),'right_stationary_derivative':enc(endpoint[1]),'monotonic_derivative':enc(Z[j+2]),'full_hj':enc(Z[j]),'nonempty_unique_stationary_branch':True})
        full_C=[-full[k+2]-2*a*full[k+1]-mu*full[k] for k in range(len(full)-2)]
        space=combined_remainder(row,'space',j,a,mu)
        temporal=combined_remainder(row,'time',j,a,mu)
        Cstat=-Z[j+2]-mu*Z[j]
        for N,U in family:
          key=f'N{N}_U{U}'
          scale=((c-a)*X).exp()
          partial=[scale*source.finite_integral(k,a,N,rat(U),rat(tc),X,tol) for k in range(29)]
          Gcenter=[-partial[k+2]-2*a*partial[k+1]-mu*partial[k] for k in range(27)]
          Rcenter=[full_C[k]-Gcenter[k] for k in range(27)]
          Bcenter=[full_C[k]-(1-lam)*Gcenter[k] for k in range(27)]
          # Each multiplier is bounded by 1 in absolute value on the
          # full horizontal source: G=chi_A C-source, R=(1-chi_A)C-source,
          # B=(1-(1-lambda)chi_A)C-source. Thus the inherited complete
          # absolute moment majorant pays EACH Taylor remainder separately.
          G=transport_poly(Gcenter,j,dx,dt)+sym(space+temporal)
          Rsource=transport_poly(Rcenter,j,dx,dt)+sym(space+temporal)
          Bsource=transport_poly(Bcenter,j,dx,dt)+sym(space+temporal)
          Rstat=joint(Rsource,Cstat-G)
          Bstat=joint(Bsource,Cstat-(1-lam)*G)
          favorable=Z[j]*G;absorption=Z[j]*Bstat;residual=Z[j]*Rstat
          vf,va,vr=verdict(favorable),verdict(absorption),verdict(residual)
          success=(vf=='CERTIFIED_POSITIVE' and va=='CERTIFIED_POSITIVE')
          label='holdout' if slab%2 else 'development'
          bucket=summary.setdefault(key,{'development':{},'holdout':{}})[label]
          tag=f'j{j}:favorable={vf},absorption={va},residual={vr}'
          bucket[tag]=bucket.get(tag,0)+1
          all_rows.append({'filter':key,'N':N,'U':str(U),'j':j,'slab':slab,'role':label,'x':row['x'],'t':row['t'],
            'normalization':row['normalization'],'partial_center_jets':list(map(enc,partial)),
            'whole_cell_G':enc(G),'whole_cell_R_source':enc(Rsource),'whole_cell_absorption_source':enc(Bsource),
            'stationary_full_C':enc(Cstat),'stationary_R':enc(Rstat),'stationary_absorption_factor':enc(Bstat),
            'full_hj':enc(Z[j]),'product_h_G':enc(favorable),'product_h_R':enc(residual),
            'product_h_R_plus_lambda_h_G':enc(absorption),
            'combined_space_payment':enc(space),'combined_time_payment':enc(temporal),
            'favorable_verdict':vf,'residual_product_verdict':vr,'absorption_verdict':va,
            'fixed_K_zero_criterion_passed':success,
            'display_only':{'hG':favorable.str(12),'hR':residual.str(12),'hR_plus_lambda_hG':absorption.str(12)}})
          print(key,'j',j,'slab',slab,label,vf,va,vr,'elapsed',round(time.monotonic()-started,2),flush=True)
    result={'schema':'inv21_predetermined_proper_source_filter_pilot_v1','date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra',
      'status':'COMPLETED_MIXED_RESULTS','script_sha256':digest(Path(__file__)),
      'input_record_name':args.record.name,'input_record_sha256':digest(args.record),
      'input_driver_name':args.original_driver.name,'input_driver_sha256':digest(args.original_driver),
      'input_contour_name':args.contour_source.name,'input_contour_sha256':digest(args.contour_source),
      'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'bits':args.bits},
      'predeclared_protocol':{'family':[{'N':n,'U':str(u)} for n,u in family],
        'a':'pi/16','b':'1/4','lambda':'1/2','K0':0,'K1':0,
        'development_slabs':[0,2,4,6],'holdout_slabs':[1,3,5,7],
        'family_changed_after_observing_results':False},
      'a':enc(a),'mu':enc(mu),
      'source_filter':'A={1<=n<=N, 0<=u<=U} on the fixed shifted horizontal contour z=u+ia; in common coordinates d_n<=v<=d_n+U.',
      'split':'G_j=e^(-a*x) Re sum_{n<=N} int_0^U (u^2-b^2)(i(u+ia))^j exp(t(u+ia)^2+i*x*u) Phi_n(u+ia) du; R_j=C_j-G_j.',
      'stationary_target':'h_j G_j>=0 and h_j(R_j+lambda G_j)>=0 imply h_j C_j>=(1-lambda)h_jG_j>=0, so L_j>=0 with fixed K_j=0.',
      'cross_terms':'Products multiply the full physical h_j by the exact filtered G_j or exact complementary absorption factor. They retain all source cross terms; no diagonal-only or phase-free replacement is made.',
      'tail_and_transport_accounting':'Partial G has only validated finite quadrature error. Full C center jets include the original complete index and integration tails. R=C-G retains those errors exactly. G,R,and R+lambda G each have a source multiplier of absolute value<=1, so the original complete absolute moment majorants dominate each transported remainder; spatial and temporal payments are added in full.',
      'branches':branches,'rows':all_rows,'summary':summary,'elapsed_seconds':time.monotonic()-started,
      'limitations':['Only the two existing bounded stationary branches are tested; no height extension or behavior near unknown collisions is inferred.',
        'Filters are fixed in t,x: no cutoff boundary derivative is omitted. No individual raw index is assumed to have a vanishing vertical contour segment.',
        'Development/holdout labels were predeclared; every filter is evaluated on both without selecting a winner and discarding failures.',
        'A negative enclosure disproves that specified product condition on its nonempty stationary branch; an enclosure crossing zero is only undecided.',
        'No loss is fitted using C/h or an energy lower bound. K0=K1=0 and lambda=1/2 were fixed before calculation.',
        'The analytic full-source contour and tail lemmas and original input quadrature remain trusted inputs; this run validates new partial quadrature and interval transport rather than formally verifying Arb or those lemmas.']}
    args.output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('SUMMARY',json.dumps(summary,indent=2),flush=True)
    print('OUTPUT',args.output,'elapsed',result['elapsed_seconds'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',type=Path,required=True);p.add_argument('--original-driver',type=Path,required=True);p.add_argument('--contour-source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--bits',type=int,default=192)
    run(p.parse_args())
