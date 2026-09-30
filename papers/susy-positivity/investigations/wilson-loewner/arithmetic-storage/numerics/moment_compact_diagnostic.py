#!/usr/bin/env python3
"""DIAGNOSTIC compact boundary correction for the actual Sonin first moment.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-29.
Exact serving variant/reasoning effort not exposed. Floating quadrature is
NOT a certificate. All integrals are compact by the accompanying derivation;
the infinite-dimensional prolate inverse is taken from its certified block.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.special import roots_legendre, eval_legendre, spherical_jn
from scipy.signal import fftconvolve
from scipy.interpolate import CubicSpline

def gauss(n,lo,hi):
    x,w=roots_legendre(n)
    return (hi+lo)/2+(hi-lo)*x/2,(hi-lo)*w/2


def basis(x,rank):
    return np.array([np.sqrt(4*j+1)*eval_legendre(2*j,x) for j in range(rank)]).T


def transformed_basis(x,rank):
    return np.array([2*(-1)**j*np.sqrt(4*j+1)*spherical_jn(2*j,2*np.pi*x)
                     for j in range(rank)]).T


def source(sid,x,norm,b=.45):
    x=np.asarray(x)
    result=np.zeros_like(x)
    idx=np.abs(x)<b
    xx=x[idx]
    z=1-(xx/b)**2
    phi=np.exp(-1/z)
    l1=-2*xx/b**2/z**2
    l2=-2/b**2/z**2-8*xx**2/b**4/z**3
    phi1=phi*l1
    phi2=phi*(l1*l1+l2)
    if sid==0: result[idx]=(-phi2+.25*phi)/norm
    else: result[idx]=(-xx*phi2-2*phi1+.25*xx*phi)/norm
    return result


def correlation(sid,normalizer,grid_power):
    n=2**grid_power
    xs=np.linspace(-.45,.45,n+1)
    dx=.9/n
    f=source(sid,xs,normalizer)
    corr=fftconvolve(f,f[::-1],mode='full')*dx
    ts=np.arange(-n,n+1)*dx
    spline=CubicSpline(ts,corr,extrapolate=False)
    def k(t):
        t=np.asarray(t)
        return np.where(np.abs(t)<.9,spline(np.clip(t,-.9,.9)),0.)
    return k,float(corr[n])


def correction(sid,n,correlation_power,rank,C,M,normalizer):
    started=time.time()
    p=2.;r=1/np.sqrt(p);a=np.log(p);c=1+r*r
    k,norm_check=correlation(sid,normalizer,correlation_power)
    def kg(t): return c*k(t)-r*(k(t-a)+k(t+a))
    def X(u,x): return kg(np.log(u[:,None]/x[None,:]))/np.sqrt(u[:,None]*x[None,:])
    # Source difference support is exactly [-.9,.9].
    umax=1.;umin=np.exp(-.9)/p;xmax=p*np.exp(.9)
    u,wu=gauss(n,umin,umax)
    v,wv=gauss(n,1/p,1.)
    x,wx=gauss(n,1.,xmax)
    y=p*v
    MR=M-np.eye(rank);S=C@M
    fx=transformed_basis(x,rank);fy=transformed_basis(y,rank)
    eu=basis(u,rank);ev=basis(v,rank)
    regularP=2*(np.sinc(2*(x[:,None]-y[None,:]))+
                np.sinc(2*(x[:,None]+y[None,:])))+fx@MR@fy.T
    PF=2*np.cos(2*np.pi*x[:,None]*y[None,:])+fx@S@fy.T
    xu=X(u,x)
    a0=X(u,y)-(xu*wx)@regularP
    a1=(xu*wx)@PF
    # The M identity term requires diagonal u=v and y=pv.
    xv=X(v,x)
    directdiag=kg(np.full(n,-a))/np.sqrt(v*y)
    a0diag=directdiag-np.einsum('vx,x,xv->v',xv,wx,regularP)
    t0=-2*np.dot(wv,a0diag)
    mkernel=ev@MR@eu.T
    skernel=ev@S@eu.T
    tM=-2*np.einsum('v,u,vu,uv->',wv,wu,mkernel,a0)
    tS=2*np.einsum('v,u,vu,uv->',wv,wu,skernel,a1)
    total=t0+tM+tS
    return {'source':sid,'gauss_order':n,'correlation_grid_power':correlation_power,
            'source_normalization_check':norm_check,
            'identity_contribution':float(t0),'M_minus_I_contribution':float(tM),
            'CM_contribution':float(tS),'compact_correction':float(total),
            'formula':'m1 = B_infinity[D2**2 F] - compact_correction',
            'elapsed_seconds':time.time()-started}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    ap.add_argument('--orders',nargs='+',type=int,default=[96,144,216,324])
    ap.add_argument('--correlation-power',type=int,default=17)
    ap.add_argument('--rank',type=int,default=32)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=ap.parse_args()
    NUM=args.numerics
    sys.path.insert(0,str(NUM))
    import prolate_certificate
    cert,cb,mb=prolate_certificate.certify(args.rank,256)
    C=np.array([[float(cb[i,j]) for j in range(args.rank)] for i in range(args.rank)])
    M=np.array([[float(mb[i,j]) for j in range(args.rank)] for i in range(args.rank)])
    src=json.loads((NUM/'records/source_norm_enclosures.json').read_text())
    norms=[float(Fraction(s['normalizer']['rational_lower'])) for s in src['sources']]
    results=[]
    for n in args.orders:
        for sid in range(2):
            row=correction(sid,n,args.correlation_power,args.rank,C,M,norms[sid])
            results.append(row)
            print(json.dumps(row),flush=True)
    record={'status':'DIAGNOSTIC_NOT_CERTIFIED','date':'2026-09-29',
            'generator':'moment_compact_diagnostic.py',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependency_sha256':{'inherited:'+name:hashlib.sha256((NUM/name).read_bytes()).hexdigest()
                                  for name in ['prolate_certificate.py','records/source_norm_enclosures.json']},
            'model':'GPT-6 (Codex); exact serving variant and effort not exposed',
            'scope':'Compact correction for first inverse-metric trace moment only; Gaussian and source quadrature errors not certified',
            'prolate_rank':args.rank,'results':results}
    args.output.write_text(json.dumps(record,indent=2)+'\n')

if __name__=='__main__': main()
