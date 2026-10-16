#!/usr/bin/env python3
"""Full-output cumulative storage on piecewise polynomial input spaces.

All output is integrated; only the input spaces are finite dimensional.
Coupling diagnostics alone never certify the unrestricted extension.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import mpmath as mp
from flint import arb as A, arb_mat as AM, arb_poly as P, ctx

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'cumulative-path-20260910'))
import certify_vector_storage as core
sys.path.insert(0,str(ROOT/'critical-path-20260910'))
import reference_certify_arb as ref

def mid(a):
    x,y=a.mid().man_exp()
    return mp.mpf(int(x))*mp.mpf(2)**int(y)

def tomp(a):
    return mp.matrix([[mid(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())])

def sub(a,r0,r1,c0,c1):
    return AM([[a[i,j] for j in range(c0,c1)] for i in range(r0,r1)])

def ident(n):
    return AM([[int(i==j) for j in range(n)] for i in range(n)])

def legendre(n,offset,scale,factor):
    p=P([(-1)**(n+k)*math.comb(n,k)*math.comb(n+k,k) for k in range(n+1)])
    return factor*A(2*n+1).sqrt()*p(P([offset,scale]))

def coefficient_matrix(polys,ncols):
    return AM([[p[j] for j in range(ncols)] for p in polys])

def input_coefficients(nold,nnew,L,a,h):
    cut=a/L
    main=[legendre(n,A(0),L/a,(L/a).sqrt()) for n in range(nold)]
    tail=[-p(P([cut,1])) for p in main]
    tail += [legendre(n,A(0),L/h,(L/h).sqrt()) for n in range(nnew)]
    main += [P([]) for _ in range(nnew)]
    k=max(nold,nnew)
    return coefficient_matrix(main,k),coefficient_matrix(tail,k)

def gamma_operator(n,L,w,degree):
    g=core.profile(w,degree)
    lp=[L**j for j in range(degree+1)]
    out=AM(n,n+degree)
    factor=(2*A.pi()*L)**w/(1+w).gamma()
    for k in range(n):
        if k: factor *= A(k)/(w+k)
        ratio=A(1)
        for j in range(degree+1):
            if j: ratio *= (w+j-1)/(w+k+j)
            out[k,k+j]=factor*g[j]*lp[j]*ratio
    return out

def shift(Q,d):
    n,k=Q.nrows(),Q.ncols()
    return coefficient_matrix([P([Q[i,j] for j in range(k)])(P([d,1])) for i in range(n)],k)

def moments(k,d,ell,w):
    if d is None:
        seq=[ell**(2*w+j+1)/(2*w+j+1) for j in range(2*k-1)]
    else:
        seq=core.mixed_moments(d,ell,w,2*k-2)
    return AM([[seq[i+j] for j in range(k)] for i in range(k)])

def gram(Q,ds,w,upper,tail=None,cut=None,label=''):
    """Q is the common base output; optional tail is added at cut=last delay."""
    n,k=Q.nrows(),Q.ncols()
    out=AM(n,n)
    for i,(di,bi,ni) in enumerate(ds):
        Qi=Q*bi
        if tail is not None and ni==7:
            Qi += tail
        ell=upper-di
        H=moments(k,None,ell,w)
        out += Qi*H*Qi.transpose()
        for dj,bj,nj in ds[i+1:]:
            Qj=Q*bj
            if tail is not None and nj==7:
                Qj += tail
            H=moments(k,dj-di,upper-dj,w)
            mixed=shift(Qi,dj-di)*H*Qj.transpose()
            out += mixed+mixed.transpose()
        print(f'{label}: integrated delay {ni}',flush=True)
    assert (out-out.transpose()).contains(AM(n,n))
    return (out+out.transpose())/2

def gamma_error(L,w,M):
    return ((2*A.pi()*L)**w/w.gamma()*32768*(L/3)**(M+1)
            /((M+1+w)*(1-L/3)))

def full_error(L,w,M,cut):
    ds=core.delays(cut,L,w)
    return sum((b for _,b,_ in ds),A(0))*gamma_error(L,w,M)

def diagnostics(E,F,W,nold,nnew):
    ee,ev=mp.eigsy(E)
    fe=mp.eigsy(F,eigvals_only=True)
    assert ee[0]>0 and fe[0]>0
    T=ev*mp.diag([1/mp.sqrt(x) for x in ee])
    H=T.T*W*T
    H=(H+H.T)/2
    ce,cv=mp.eigsy(H)
    c2=ce[-1,0]
    top=T*cv[:,-1]
    S=E-W
    se=mp.eigsy((S+S.T)/2,eigvals_only=True)
    return {'old_storage_min':mp.nstr(ee[0],28),'new_slab_storage_min':mp.nstr(fe[0],28),
            'relative_coupling_squared':mp.nstr(c2,35),
            'relative_schur_slack':mp.nstr(1-c2,35),
            'effective_old_schur_min':mp.nstr(se[0],28)},T,H

def run(args):
    if not __debug__: raise RuntimeError('Assertions must remain enabled')
    start=time.monotonic()
    ctx.prec=args.bits
    mp.mp.dps=args.digits
    L,a=A(8).log(),A(7).log()
    h=L-a
    w=core.rat(args.shift)
    assert 0<w<=A(1)/2 and 0<h<A(2).log() and L<3
    assert A(3).sin()>A(1)/8 and (A(3)/2).exp()<5
    assert 120+1440*A(3).exp()<32768
    no,nn=args.old,args.new
    n=no+nn
    ca,ct=input_coefficients(no,nn,L,a,h)
    G=gamma_operator(max(no,nn),L,w,args.degree)
    Q,tail=ca*G,ct*G
    ds=core.delays(8,L,w)
    # The cutoff is exactly log 7, so this is the only delayed tail term.
    full=gram(Q,ds,w,A(1),tail=tail,cut=a/L,label='extended output')
    old=gram(sub(Q,0,no,0,Q.ncols()),ds[:-1],w,a/L,label='old output')
    E=ident(no)-old
    D=ident(n)-full
    F=sub(D,no,n,no,n)
    R=sub(full,0,no,no,n)
    leakage=sub(full,0,no,0,no)-old
    W=leakage+R*F.solve(R.transpose())
    # Work with all forms divided by 2w to remove a harmless common scale.
    en,fn,wn=E/(2*w),F/(2*w),W/(2*w)
    print('Computing relative-coupling diagnostics',flush=True)
    vals,T,H=diagnostics(tomp(en),tomp(fn),tomp(wn),no,nn)
    # Enclose positivity for ALL inputs in this finite input space. The
    # complementary input spaces remain uncontrolled.
    delta=full_error(L,w,args.degree,8)
    trace=sum((full[i,i] for i in range(n)),A(0))
    eps=(2*delta*trace.sqrt()+delta*delta).upper()
    dn=(D-ident(n)*eps)/(2*w)
    ldl_result=ref.ldl(dn)
    finite_pass=ldl_result['positive']
    pivot_min=ldl_result.get('minimum_pivot_lower')
    data={'scope':'Finite INPUT spaces with full output and analytic remainder. No unrestricted coupling upper bound or all-operator extension.',
          'normalization':'Weil-depth v0.3, a566944dc1be2899e37fce3d0e857516ced33d8f',
          'old_horizon':'log 7','new_horizon':'log 8','new_slab':'log(8/7)',
          'old_input_modes':no,'new_input_modes':nn,'shift_rational':args.shift,
          'profile_degree':args.degree,'precision_bits':args.bits,'eigensolver_digits':args.digits,
          'storage_minima_are_scaled_by_2omega':True,'diagnostics':vals,
          'full_transfer_error_upper':delta.upper().str(40),
          'finite_input_defect_error_upper':eps.str(40),
          'finite_input_positivity_with_remainder_pass':finite_pass,
          'smallest_LDL_pivot_scaled_by_2omega':pivot_min,
          'seconds':time.monotonic()-start,
          'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in
              [Path(__file__).resolve(),Path(core.__file__),Path(ref.__file__)]}}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--old',type=int,default=32)
    p.add_argument('--new',type=int,default=8)
    p.add_argument('--shift',default='4e-15')
    p.add_argument('--degree',type=int,default=240)
    p.add_argument('--bits',type=int,default=6144)
    p.add_argument('--digits',type=int,default=100)
    p.add_argument('--output',required=True)
    run(p.parse_args())
