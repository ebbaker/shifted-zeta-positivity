#!/usr/bin/env python3
"""Full new-slab residual for finite old central input spaces.

The residual is represented by polynomial + polynomial*log(v) +
polynomial*log(1-v), with an explicitly bounded analytic remainder.
No new-slab output modes are discarded in its Gram matrix.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import mpmath as mp
from flint import arb as A, arb_mat as AM, arb_poly as P, ctx

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'log7-log8-extension-20260910'))
import central_geometry as cg
ex,c=cg.ex,cg.c

def matrix(polys,k=None):
    if k is None:k=max(p.degree()+1 for p in polys)
    return AM([[p[j] for j in range(k)] for p in polys])

def rows(Q):
    return [P([Q[i,j] for j in range(Q.ncols())]) for i in range(Q.nrows())]

def pad(Q,k):return matrix(rows(Q),k)

def eta(L,M):return 256*(L/3)**(M+1)/((M+1)*(1-L/3))

def cross_output(no,a,h,M,g,T):
    r=h/a
    # F_i(1+r*v) has positive coefficients in this representation.
    cont=[P([A(2*i+1).sqrt()*math.comb(i,k)*math.comb(i+k,k)*r**k for k in range(i+1)]) for i in range(no)]
    oldpolys=[ex.legendre(i,A(0),A(1),A(1)) for i in range(no)]
    div=[]
    for i,phi in enumerate(oldpolys):
        hz=P([sum((phi[k]/(k-j) for k in range(j+1,i+1)),A(0)) for j in range(i)])
        div.append(hz(P([1,r])))
    logpoly=P([(a/h).log()]+[(-1)**(s+1)*r**s/s for s in range(1,T+1)])
    poly=[r.sqrt()/2*(div[i]-cont[i]*logpoly) for i in range(no)]
    # Exact reflected Legendre power moments, avoiding monomial cancellation.
    moments=AM(no,M)
    for i in range(no):
        value=Fraction(math.factorial(i)**2,math.factorial(2*i+1))
        for k in range(i,M):
            if k>i:value*=Fraction(k*k,(k-i)*(k+i+1))
            moments[i,k]=(-1)**i*A(2*i+1).sqrt()*c.rat(value)
    H=AM(M,M)
    ap,hp=[a**j for j in range(M)],[h**j for j in range(M)]
    for j in range(M):
        for k in range(M-j):
            H[j,k]=-c.rat(g[j+k+1])*math.comb(j+k,j)*ap[j]*hp[k]/2
    smooth=rows((a*h).sqrt()*moments*H)
    for i in range(no):poly[i]+=smooth[i]
    for n,p,_ in c.prime_powers(a+h,8):
        z=A(0) if n==7 else 1-A(n).log()/a
        coefficient=-r.sqrt()*A(p).log()/A(n).sqrt()
        for i in range(no):poly[i]+=coefficient*oldpolys[i](P([z,r]))
    logv=[r.sqrt()/2*p for p in cont]
    log_remainder=r**(T+1)/((T+1)*(1-r))
    cont_norm=sum((p(A(1))**2 for p in cont),A(0)).sqrt()
    error=eta(a+h,M)+r.sqrt()/2*cont_norm*log_remainder
    return matrix(poly),matrix(logv),error

def gamma_output(nn,h,M,g):
    U=AM(nn,nn+M)
    ell=A.const_euler()+(2*A.pi()*h).log()
    harmonic=Fraction(0)
    for k in range(nn):
        if k:harmonic+=Fraction(1,k)
        U[k,k]=ell-c.rat(harmonic)
        beta=Fraction(1,k+1)
        for j in range(1,M+1):
            if j>1:beta*=Fraction(j-1,j+k)
            U[k,k+j]=c.rat(g[j]*beta)*h**j
    phi=[ex.legendre(i,A(0),A(1),A(1)) for i in range(nn)]
    q=rows(matrix(phi,nn)*U)
    poly=[(A(-1)/2)*(q[i]+(-1)**i*q[i](P([1,-1]))) for i in range(nn)]
    logv=[(A(-1)/2)*p for p in phi]
    return matrix(poly),matrix(logv)

def gram(poly,left,right):
    n=poly.nrows()
    kp,kl,kr=poly.ncols(),left.ncols(),right.ncols()
    out=poly*c.moment(kp,kp,'plain')*poly.transpose()
    out+=left*c.moment(kl,kl,'log2')*left.transpose()
    # Reflection converts log(1-v)^2 to log(v)^2.
    reflected=matrix([p(P([1,-1])) for p in rows(right)],kr)
    out+=reflected*c.moment(kr,kr,'log2')*reflected.transpose()
    for a,b,kind in [(poly,left,'log'),(poly,right,'log1'),(left,right,'loglog')]:
        q=a*c.moment(a.ncols(),b.ncols(),kind)*b.transpose()
        out+=q+q.transpose()
    assert (out-out.transpose()).contains(AM(n,n))
    return (out+out.transpose())/2

def row_floor(h,M,g):
    variation=sum((abs(c.rat(g[j]))*h**j for j in range(1,M+1)),A(0))
    variation+=256*(h/3)**(M+1)/(1-h/3)
    assert variation<1  # off-diagonal gamma kernel is negative
    remainder=sum((abs(c.rat(g[j]))*h**j/j for j in range(2,M+1)),A(0))
    remainder+=256*(h/3)**(M+1)/((M+1)*(1-h/3))
    lower=-A.const_euler()-(2*A.pi()*h).log()+A(2).log()+A(7)*h/4-remainder/2
    assert lower>0
    return lower.lower()

def rational_matrix(Q,digits=100):
    strings=[[mp.nstr(ex.mid(Q[i,j]),digits) for j in range(Q.ncols())] for i in range(Q.nrows())]
    return AM([[c.rat(s) for s in row] for row in strings]),strings

def run(args):
    if not __debug__:raise RuntimeError('Assertions must remain enabled')
    start=time.monotonic()
    ctx.prec=args.bits
    mp.mp.dps=args.digits
    a=A(7).log();h=(A(8).log()-a)/4;L=a+h
    no,nn,M=args.old,args.new,args.degree
    assert 0<h<A(2).log() and L<3
    assert A(3).sin()>A(1)/8 and (A(3)/2).exp()<5
    assert 5*(24+12)<256
    g=c.profile(M)
    Ao=cg.old.head(c,7,no,M,return_balls=True)
    F=cg.gamma_head(nn,h,M,g)
    B,*_=cg.cross(no,nn,a,h,M,g)
    J,js=rational_matrix(-F.solve(B),args.digits)
    f0=row_floor(h,M,g)
    print('Building full new-slab residual outputs',flush=True)
    bp,bl,be=cross_output(no,a,h,M,g,args.log_degree)
    fp,fl=gamma_output(nn,h,M,g)
    k=max(bp.ncols(),fp.ncols())
    rp=pad(bp,k)+J.transpose()*pad(fp,k)
    rl=pad(bl,max(bl.ncols(),fl.ncols()))+J.transpose()*pad(fl,max(bl.ncols(),fl.ncols()))
    rr=J.transpose()*fl
    print('Integrating complete residual Gram',flush=True)
    RG=gram(rp,rl,rr)
    jnorm=sum((J[i,j]**2 for i in range(nn) for j in range(no)),A(0)).sqrt()
    error=(be+eta(h,M)*jnorm).upper()
    # Strong check against the independently constructed projected blocks.
    Pnew=matrix([ex.legendre(i,A(0),A(1),A(1)) for i in range(nn)],nn)
    Rhead=Pnew*c.moment(nn,k,'plain')*rp.transpose()
    Rhead+=Pnew*c.moment(nn,rl.ncols(),'log')*rl.transpose()
    Rhead+=Pnew*c.moment(nn,rr.ncols(),'log1')*rr.transpose()
    projected=B+F*J
    head_difference=Rhead-projected
    check_norm=sum((head_difference[i,j]**2 for i in range(nn) for j in range(no)),A(0)).sqrt()
    assert check_norm < A('1e-50')+be*10
    Hj=Ao+B.transpose()*J+J.transpose()*B+J.transpose()*F*J
    aa=ex.tomp(Ao);hh=ex.tomp(Hj);rg=ex.tomp(RG)
    C=mp.cholesky(aa);T=C.T**-1
    residual_relative=T.T*rg*T
    residual_relative=(residual_relative+residual_relative.T)/2
    re=mp.eigsy(residual_relative,eigvals_only=True)
    hjrel=T.T*hh*T;hjrel=(hjrel+hjrel.T)/2
    he=mp.eigsy(hjrel,eigvals_only=True)
    remainder_test=Hj-RG/f0
    # Conservative full Gram perturbation and quadratic-form profile budget.
    rgtrace=sum((RG[i,i] for i in range(no)),A(0))
    norm_error=2*error*rgtrace.sqrt()+error**2
    hjerror=eta(L,M)*(1+jnorm**2)
    guarded=remainder_test-ex.ident(no)*(norm_error/f0+hjerror).upper()
    check=c.ldl(guarded)
    # Measure the residual against the candidate continuation energy itself,
    # retaining orientation instead of comparing two unrelated extrema.
    Ch=mp.cholesky(hh);Th=Ch.T**-1
    hmetric=Th.T*rg*Th/ex.mid(f0)
    hmetric=(hmetric+hmetric.T)/2
    theta_diag=mp.eigsy(hmetric,eigvals_only=True)[-1,0]
    rounded=Fraction(int(mp.ceil(theta_diag*1000)),1000)
    theta=c.rat(rounded) if 0<rounded<1 else c.rat(mp.nstr((1+theta_diag)/2,40))
    relative_residual_pass=False
    if 0<theta<1:
        theta_test=theta*f0*(Hj-ex.ident(no)*hjerror.upper())-RG-ex.ident(no)*norm_error.upper()
        relative_residual_pass=c.ldl(theta_test)['positive']
    eta_old=c.rat(args.relative_floor)
    relative_test=guarded-eta_old*Ao-ex.ident(no)*(eta_old*eta(a,M)).upper()
    relative_floor_pass=c.ldl(relative_test)['positive']
    data={'scope':'Central quarter-step. Full new-input complement addressed by a residual bound, old inputs restricted to polynomials.',
          'old_modes':no,'new_continuation_modes':nn,'profile_degree':M,'log_series_degree':args.log_degree,
          'precision_bits':args.bits,'digits':args.digits,
          'full_new_gamma_coercivity_lower':f0.str(40),
          'projected_residual_independent_check_norm':check_norm.str(35),
          'residual_output_operator_error_upper':error.str(35),
          'diagnostics':{'candidate_relative_energy_min':mp.nstr(he[0],30),
              'full_residual_squared_relative_norm':mp.nstr(re[-1,0],30),
              'residual_penalty_relative_norm':mp.nstr(re[-1,0]/ex.mid(f0),30),
              'residual_penalty_relative_to_candidate_energy':mp.nstr(theta_diag,30)},
          'full_new_input_schur_certificate_pass':check['positive'],
          'candidate_energy_residual_factor_upper':theta.str(40),
          'candidate_energy_residual_factor_pass':relative_residual_pass,
          'relative_old_energy_floor':args.relative_floor,
          'relative_old_energy_floor_pass':relative_floor_pass,
          'schur_check':{k:v for k,v in check.items() if k not in ['pivots','pivot_ball']},
          'continuation_rational_coefficients':js,
          'seconds':time.monotonic()-start,
          'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(cg.__file__),Path(ex.__file__),Path(c.__file__),Path(cg.old.__file__)]}}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ['source_sha256','continuation_rational_coefficients']},indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--old',type=int,default=128)
    p.add_argument('--new',type=int,default=32)
    p.add_argument('--degree',type=int,default=320)
    p.add_argument('--log-degree',type=int,default=80)
    p.add_argument('--bits',type=int,default=6144)
    p.add_argument('--digits',type=int,default=100)
    p.add_argument('--relative-floor',default='1e-8')
    p.add_argument('--output',required=True)
    run(p.parse_args())
