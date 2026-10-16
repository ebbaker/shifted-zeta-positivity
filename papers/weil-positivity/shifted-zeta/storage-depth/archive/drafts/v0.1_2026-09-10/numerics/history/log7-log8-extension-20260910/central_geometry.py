#!/usr/bin/env python3
"""Central-limit cross-slab geometry; finite input diagnostics only."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from fractions import Fraction
import mpmath as mp
from flint import arb as A, arb_mat as AM, ctx
import extension_storage as ex
sys.path.insert(0,str(ex.ROOT/'critical-path-20260910'))
import explore_path as old
import reference_certify_arb as c

def legendre(n):
    return AM([[(-1)**(i+k)*math.comb(i,k)*math.comb(i+k,k) if k<=i else 0 for k in range(n)] for i in range(n)])

def gamma_head(n,L,M,g):
    P=legendre(n)
    U=AM(n,n+M)
    ell=A.const_euler()+(2*A.pi()*L).log()
    harmonic=Fraction(0)
    for k in range(n):
        if k: harmonic+=Fraction(1,k)
        U[k,k]=ell-c.rat(harmonic)
        beta=Fraction(1,k+1)
        for j in range(1,M+1):
            if j>1: beta*=Fraction(j-1,j+k)
            U[k,k+j]=c.rat(g[j]*beta)*L**j
    D=P*c.moment(n,n+M,'plain')*(P*U).transpose()+P*c.moment(n,n,'log')*P.transpose()
    return AM([[-(D[i,j]+D[j,i])*A((2*i+1)*(2*j+1)).sqrt()/2 for j in range(n)] for i in range(n)])

def rational_moments(c0,d,n):
    out=[((c0+d)/c0).log()/d]
    for k in range(1,n):
        out.append(1/(d*k)-c0/d*out[-1])
    assert all(x>0 for x in out)
    return out

def cross(no,nn,a,h,M,g):
    Po,Pn=legendre(no),legendre(nn)
    # Reflect the old variable: distance to the new point is a*u+h*v.
    iv=rational_moments(a,h,nn)
    iu=rational_moments(h,a,no)
    C=AM([[(iv[j]+iu[k])/(j+k+1) for k in range(no)] for j in range(nn)])
    H=AM(M,M)
    ap,hp=[a**r for r in range(M)],[h**s for s in range(M)]
    for r in range(M):
        for s in range(M-r):
            H[r,s]=-c.rat(g[r+s+1])*math.comb(r+s,r)*ap[r]*hp[s]/2
    raw=-Pn*C*Po.transpose()/2+(Pn*c.moment(nn,M,'plain'))*H.transpose()*(Po*c.moment(no,M,'plain')).transpose()
    gamma=AM([[raw[j,k]*(a*h).sqrt()*A((2*j+1)*(2*k+1)).sqrt()*(-1)**k for k in range(no)] for j in range(nn)])
    arithmetic=AM(nn,no)
    newest=None
    for n,p,_ in c.prime_powers(a+h,8):
        z=A(0) if n==7 else 1-A(n).log()/a
        r=h/a
        tr=AM([[math.comb(k,s)*z**(k-s)*r**s if s<=k else 0 for s in range(no)] for k in range(no)])
        raw=Pn*c.moment(nn,no,'plain')*(Po*tr).transpose()
        term=AM([[-(h/a).sqrt()*A(p).log()/A(n).sqrt()*raw[j,k]*A((2*j+1)*(2*k+1)).sqrt() for k in range(no)] for j in range(nn)])
        arithmetic+=term
        if n==7: newest=term
    return gamma+arithmetic,newest,gamma,arithmetic

def coupling(B,Aold,F):
    Lo,Lf=mp.cholesky(Aold),mp.cholesky(F)
    K=Lf**-1*B*(Lo.T**-1)
    KK=K*K.T
    es=mp.eigsy((KK+KK.T)/2,eigvals_only=True)
    return es[-1,0],K

def coupling_lower_witness(B,Aold,F,a,h,L,M):
    aa,ff,bb=ex.tomp(Aold),ex.tomp(F),ex.tomp(B)
    Lo,Lf=mp.cholesky(aa),mp.cholesky(ff)
    K=Lf**-1*bb*(Lo.T**-1)
    es,vs=mp.eigsy((K*K.T+(K*K.T).T)/2)
    u=vs[:,-1]
    x=Lo.T**-1*K.T*u/mp.sqrt(es[-1,0])
    y=Lf.T**-1*u
    xs=[mp.nstr(t,100) for t in x]
    ys=[mp.nstr(t,100) for t in y]
    vx,vy=AM([[c.rat(t)] for t in xs]),AM([[c.rat(t)] for t in ys])
    ea=(vx.transpose()*Aold*vx)[0,0]
    ef=(vy.transpose()*F*vy)[0,0]
    cross=(vy.transpose()*B*vx)[0,0]
    nx=(vx.transpose()*vx)[0,0]
    ny=(vy.transpose()*vy)[0,0]
    def eta(t): return 256*(t/3)**(M+1)/((M+1)*(1-t/3))
    lower_cross=cross-eta(L).upper()*(nx*ny).sqrt()
    assert lower_cross>0
    bound=(lower_cross**2/((ea+eta(a).upper()*nx)*(ef+eta(h).upper()*ny))).lower()
    assert bound>0
    return {'scope':'Lower bound for FULL central coupling, using v0.3 old-depth coercivity and small-slab coercivity. It is not an upper bound.',
            'central_coupling_squared_lower':bound.str(45),
            'central_relative_slack_upper':(1-bound).upper().str(45),
            'old_vector_rational_legendre_coefficients':xs,
            'new_vector_rational_legendre_coefficients':ys,
            'old_vector_L2_norm_squared':nx.str(30),'new_vector_L2_norm_squared':ny.str(30)}

def run(args):
    start=time.monotonic()
    ctx.prec=args.bits
    mp.mp.dps=args.digits
    a,L=A(7).log(),A(8).log()
    h=L-a
    no,nn,M=args.old,args.new,args.degree
    g=c.profile(M)
    Ao=old.head(c,7,no,M,return_balls=True)
    F=gamma_head(nn,h,M,g)
    B,B7,Bgamma,Barith=cross(no,nn,a,h,M,g)
    aa,ff=ex.tomp(Ao),ex.tomp(F)
    vals={}
    for name,bb in [('complete',B),('without_new_prime',B-B7),('new_prime_alone',B7),('gamma_alone',Bgamma),('arithmetic_alone',Barith)]:
        c2,_=coupling(ex.tomp(bb),aa,ff)
        vals[name]={'relative_coupling_squared':mp.nstr(c2,32),'relative_coupling':mp.nstr(mp.sqrt(c2),24)}
    slack=1-mp.mpf(vals['complete']['relative_coupling_squared'])
    joint=AM(no+nn,no+nn)
    for i in range(no+nn):
        for j in range(no+nn):
            joint[i,j]=Ao[i,j] if i<no and j<no else F[i-no,j-no] if i>=no and j>=no else B[i-no,j] if i>=no else B[j-no,i]
    eta=256*(L/3)**(M+1)/((M+1)*(1-L/3))
    result=c.ldl(joint-ex.ident(no+nn)*eta.upper())
    witness=coupling_lower_witness(B,Ao,F,a,h,L,M)
    data={'scope':'Central-limit finite-input geometry. Component norms quantify cancellation, not full-norm bounds.',
          'old_input_modes':no,'new_input_modes':nn,'profile_degree':M,'precision_bits':args.bits,
          'relative_schur_slack':mp.nstr(slack,32),'components':vals,
          'profile_operator_error_upper':eta.upper().str(35),
          'finite_input_central_positivity_with_remainder_pass':result['positive'],
          'full_central_coupling_lower_witness':witness,
          'source_sha256':{str(p.relative_to(ex.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(ex.__file__),Path(old.__file__),Path(c.__file__)]},
          'seconds':time.monotonic()-start}
    Path(args.output).write_text(json.dumps(data,indent=2)+'\n')
    display={k:v for k,v in data.items() if k not in ['source_sha256','full_central_coupling_lower_witness']}
    display['full_central_coupling_lower_witness']={k:v for k,v in witness.items() if 'coefficients' not in k}
    print(json.dumps(display,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--old',type=int,default=32)
    p.add_argument('--new',type=int,default=8)
    p.add_argument('--degree',type=int,default=240)
    p.add_argument('--bits',type=int,default=3072)
    p.add_argument('--digits',type=int,default=100)
    p.add_argument('--output',required=True)
    run(p.parse_args())
