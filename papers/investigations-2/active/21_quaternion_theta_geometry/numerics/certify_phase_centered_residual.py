#!/usr/bin/env python3
"""Complete-source closed-cell phase-centered residual pilot for inv21.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. Uses python-flint Arb/Acb.
This bounded rectangle certificate has no arbitrary-height implication.
The source contour, finite integrals, and two omitted-domain payments are
from the investigation's existing shifted-contour checker. Parameter
transport uses the exact heat equation with absolute complete-source
moment majorants, and includes both spatial and temporal remainders.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform
import sys
import time

import check_shifted_contour_payments as source
import flint
from flint import arb,acb,ctx


def require(ok,message):
    if not ok: raise RuntimeError(message)


def rat(q):
    q=Fraction(q)
    return arb(q.numerator)/q.denominator


def compact(v):
    require(v.is_finite(),'finite enclosure')
    def endpoint(z):
        m,e=z.man_exp();return [str(m),int(e)]
    return [endpoint(v.lower()),endpoint(v.upper())]


def symmetric(v):
    require(v>=0,'nonnegative error')
    return arb(0,v.upper())


def ipow(v,n):
    answer=arb(1)
    for _ in range(n): answer*=v
    return answer


def distance(v):
    if v.lower()>0: return v.lower()
    if v.upper()<0: return -v.upper()
    return arb(0)


def moment(k,a,n,u,tmax,tol):
    p=arb.pi();c=(4*a).cos()
    def f(v,analytic):
        majorant=acb(0)
        for nn in range(1,n+1):
            alpha=p*nn*nn
            majorant+=(2*alpha*alpha*(9*v).exp()+3*alpha*(5*v).exp())*(-alpha*c*(4*v).exp()).exp()
        return (v+a)**k*(tmax*v*v).exp()*majorant
    v=acb.integral(f,0,u,rel_tol=tol,abs_tol=tol,eval_limit=100000,depth_limit=35)
    require(v.is_finite() and v.imag.contains(0),'finite real positive-moment quadrature')
    nt=source.index_payment(k,a,n,tmax)[0]
    ut=source.integration_payment(k,a,u,tmax)[0]
    result=v.real+nt+ut
    require(result>0,'strict positive moment majorant')
    return result.upper()


def transport(center,moments,component,dx,dt,lx,lt):
    eta=symmetric(dx);delta=symmetric(dt)
    value=arb(0);space_payment=arb(0)
    for ell in range(lt):
        value+=ipow(-delta,ell)/factorial(ell)*sum(ipow(eta,m)/factorial(m)*center[component+2*ell+m] for m in range(lx))
        space_payment+=dt**ell/factorial(ell)*dx**lx/factorial(lx)*moments[component+2*ell+lx]
    time_payment=dt**lt/factorial(lt)*moments[component+2*lt]
    return value+symmetric(space_payment+time_payment),space_payment,time_payment


def run(args):
    started=time.monotonic();ctx.prec=args.bits
    require(args.bits>=192,'precision at least192')
    xl=Fraction(args.x_left);xr=Fraction(args.x_right);width=Fraction(args.width)
    require(xl>0 and xr>xl and width>0 and (xr-xl)/width==int((xr-xl)/width),'exact spatial partition')
    require(args.time_slabs>0,'positive time slabs')
    a=arb.pi()/16;c=arb.pi()/8;n=8;u=arb(3)/2;tmax=arb(1)/2;tol=arb(2)**(-(args.bits-64))
    lx=args.space_order;lt=args.time_order
    require(lx>=8 and lt>=6,'sufficient declared expansion orders')
    top=3+2*(lt-1)+lx-1
    mtop=max(3+2*(lt-1)+lx,3+2*lt)
    moments=[moment(k,a,n,u,tmax,tol) for k in range(mtop+1)]
    index_payments=[source.index_payment(k,a,n,tmax)[0] for k in range(mtop+1)]
    integration_payments=[source.integration_payment(k,a,u,tmax)[0] for k in range(mtop+1)]
    payments=[index_payments[k]+integration_payments[k] for k in range(top+1)]
    print('moments complete',round(time.monotonic()-started,2),flush=True)
    rows=[];max_B2=arb(0);max_K=arb(0);min_normalized_energy=None;min_physical_energy=None;min_mu=None;min_delta=None;failed=[]
    xleft=xl
    while xleft<xr:
      xright=xleft+width;xc=(xleft+xright)/2;dx=rat(width/2)
      for slab in range(args.time_slabs):
        tl=Fraction(slab,2*args.time_slabs);tr=Fraction(slab+1,2*args.time_slabs);tc=(tl+tr)/2;dt=rat((tr-tl)/2)
        X=rat(xc);time_center=rat(tc)
        scale=((c-a)*X).exp()
        center=[scale*(source.finite_integral(k,a,n,u,time_center,X,tol)+symmetric(payments[k])) for k in range(top+1)]
        # For every point in the cell, e^(c*xc-a*x) <= this factor.
        # e^(t*(u^2-a^2)) <= e^(tmax*u^2) for the nonnegative time range.
        uniform_scale=((c-a)*X+a*dx).exp()
        majorants=[uniform_scale*M for M in moments]
        b=((X+2*time_center*a)/(4*arb.pi()*(4*a).sin())).log()/4
        Lambda=a*a+b*b
        centered=[-center[k+2]-2*a*center[k+1]-Lambda*center[k] for k in range(top-1)]
        centered_majorants=[majorants[k+2]+2*a*majorants[k+1]+Lambda*majorants[k] for k in range(mtop-1)]
        jet_data=[transport(center,majorants,k,dx,dt,lx,lt) for k in range(4)]
        residual_data=[transport(centered,centered_majorants,k,dx,dt,lx,lt) for k in range(2)]
        jets=[v[0] for v in jet_data];C=[v[0] for v in residual_data]
        E_low=(distance(jets[0])**2+distance(jets[1])**2).lower()
        C2_upper=(abs(C[0]).upper()**2+abs(C[1]).upper()**2).upper()
        S=jets[0]*jets[2]+jets[1]*jets[3]
        norm_ok=bool(E_low>0)
        B2=C2_upper/E_low if norm_ok else arb('nan')
        K=max(arb(0),S.upper())/E_low if norm_ok else arb('nan')
        Delta=rat(args.B_squared)*E_low-C2_upper
        mu_ok=bool(Lambda>=arb(2)/5)
        residual_ok=bool(norm_ok and Delta>0 and mu_ok)
        if not residual_ok: failed.append({'x':[str(xleft),str(xright)],'t':[str(tl),str(tr)],'norm_ok':norm_ok})
        if norm_ok:
            physical_E=((-2*c*X).exp()*E_low).lower()
            min_physical_energy=physical_E if min_physical_energy is None else min(min_physical_energy,physical_E)
            min_mu=Lambda.lower() if min_mu is None else min(min_mu,Lambda.lower())
            min_delta=Delta.lower() if min_delta is None else min(min_delta,Delta.lower())
            max_B2=max(max_B2,B2.upper());max_K=max(max_K,K.upper())
            normalized_E=((-2*c*dx).exp()*E_low).lower() # optional uniform e^(cx) normalization lower bound
            min_normalized_energy=normalized_E if min_normalized_energy is None else min(min_normalized_energy,normalized_E)
        signs=[];sign_enclosures=[]
        for j in range(2):
            signed_form=Lambda*ipow(jets[j],2)+jets[j]*C[j]
            sign_enclosures.append(signed_form)
            if not jets[j+1].contains(0):
                signs.append('stationarity_excluded')
            elif signed_form.lower()>0:
                signs.append('stationary_sign_certified_by_centered_identity')
            else:
                signs.append('stationary_sign_not_decided_by_this_enclosure')
        row={'x':[str(xleft),str(xright)],'t':[str(tl),str(tr)],'normalization':'e^(pi*xc/8), constant across cell','center_jets':[compact(z) for z in center],'whole_cell_jets':[compact(z) for z in jets],'whole_cell_C':[compact(v) for v in C],'b':compact(b),'Lambda':compact(Lambda),'jet_space_payments':[compact(v[1]) for v in jet_data],'jet_time_payments':[compact(v[2]) for v in jet_data],'C_space_payments':[compact(v[1]) for v in residual_data],'C_time_payments':[compact(v[2]) for v in residual_data],'energy_lower':compact(E_low),'C2_upper':compact(C2_upper),'norm_positive':norm_ok,'residual_inequality_pass':residual_ok,'mu_at_least_two_fifths':mu_ok,'residual_cone_margin':compact(Delta),'stationary_classification':signs,'stationary_signed_form_enclosures':[compact(v) for v in sign_enclosures]}
        if norm_ok: row.update({'B2_upper':compact(B2.upper()),'radial_K_upper':compact(K.upper())})
        rows.append(row)
        print(str(xleft),str(tl),'B²',B2.str(7),'signs',','.join(signs),'elapsed',round(time.monotonic()-started,2),flush=True)
      xleft=xright
    record={'schema':'inv21_phase_centered_complete_source_pilot_v1','date':'2026-10-14','prepared_for':'Edward Baker','llm_assistance':'Substantial','recorded_model':'gpt-6-astra','recorded_effort':'ultra','runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'bits':args.bits},'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'imported_source_name':Path(source.__file__).name,'imported_source_sha256':sha256(Path(source.__file__).read_bytes()).hexdigest(),'status':'PASS' if not failed else 'INCOMPLETE','scope':'Bounded closed rectangle only; no arbitrary-height or collision-cusp conclusion','domain':{'x':[str(xl),str(xr)],'t':['0','1/2']},'a':compact(a),'N':n,'U':'3/2','space_order':lx,'time_order':lt,'time_slabs':args.time_slabs,'width':str(width),'cell_count':len(rows),'B_squared_claim':str(Fraction(args.B_squared)),'max_certified_B_squared_upper':source.enc(max_B2),'max_certified_radial_K_upper':source.enc(max_K),'normalized_energy_lower':source.enc(min_normalized_energy) if min_normalized_energy is not None else None,'physical_energy_lower':source.enc(min_physical_energy) if min_physical_energy is not None else None,'physical_norm_lower':source.enc(min_physical_energy.sqrt()) if min_physical_energy is not None else None,'minimum_mu':source.enc(min_mu),'minimum_residual_cone_margin':source.enc(min_delta),'all_stationary_observations_resolved':all('stationary_sign_not_decided_by_this_enclosure' not in row['stationary_classification'] for row in rows),'complete_unscaled_index_payments':[compact(v) for v in index_payments],'complete_unscaled_integration_payments':[compact(v) for v in integration_payments],'complete_unscaled_moment_majorants':[compact(v) for v in moments],'cells':rows,'failed_cells':failed,'elapsed_seconds':time.monotonic()-started,'identities':{'C':'C_j=-h_(j+2)-2*a*h_(j+1)-(a²+b²)*h_j; a,b frozen per cell','stationary':'h_(j+1)=0 implies L_j=(a²+b²)*h_j²+h_j*C_j','bounded_loss':'C0²+C1²<=B²E implies L_j>=-B²/(4(a²+b²))*E at stationarity'},'limitations':['The numerical source and tail lemmas are imported; this run is not independent formal verification.','The relative residual bound uses a certified finite-cell lower bound on E; it supplies no proof through a hypothetical unbounded-domain collision.','b is a documented saddle-based centering choice, not a proved optimal value.']}
    args.output.write_text(json.dumps(record,indent=2)+'\n')
    print('FINAL',record['status'],'cells',len(rows),'max_B²',max_B2,'max_K',max_K,'elapsed',record['elapsed_seconds'],flush=True)
    return 0 if not failed else 1


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',required=True,type=Path);ap.add_argument('--x-left',default='100');ap.add_argument('--x-right',default='104');ap.add_argument('--width',default='1');ap.add_argument('--time-slabs',type=int,default=8);ap.add_argument('--bits',type=int,default=192);ap.add_argument('--space-order',type=int,default=12);ap.add_argument('--time-order',type=int,default=8);ap.add_argument('--B-squared',default='1/9')
    return run(ap.parse_args())
if __name__=='__main__': raise SystemExit(main())
