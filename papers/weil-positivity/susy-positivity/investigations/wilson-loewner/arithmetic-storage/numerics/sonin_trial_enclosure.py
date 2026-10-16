#!/usr/bin/env python3
"""Actual-Sonin rank-two trial enclosures using compact spline proxies.

Prepared for Edward Baker, 2026-09-29, with GPT-6 (Codex) assistance.
Exact serving variant and reasoning effort are not exposed.
Arb and exact integer convolution decide bounds. No spatial tail is dropped.
Requires sibling source_norm_enclosures.py/.json and prolate_certificate.py.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, arb_mat, ctx, fmpq, fmpz_poly
import source_norm_enclosures as source
import prolate_certificate as prolate


def ab(q):
    q=Q(q)
    return arb(fmpq(q.numerator,q.denominator))


def require(test,message):
    if not test: raise ArithmeticError(message)


def interval(lo,hi):
    lo,hi=lo.lower(),hi.upper()
    return arb((lo+hi)/2,(hi-lo)/2)


def errball(v,e):
    return v+arb(0,e.abs_upper())


def pack(v):
    return {"display":v.str(24),"ball":prolate.pack(v)}


def export_matrix(a):
    return [[pack(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]


def quantize(v,scale):
    q=Q(str(v.mid().fmpq()))*scale
    integer=(2*q.numerator+q.denominator)//(2*q.denominator)
    return integer,(v-ab(Q(integer,scale))).abs_upper()


def legendre(n):
    # P_n(2x-3) with exact rational coefficients, in powers of x.
    p0,p1=[Q(1)],[Q(-3),Q(2)]
    if n==0:return p0
    for k in range(1,n):
        p2=source.scale(source.add(source.scale(source.mul(p1,[-3,2]),2*k+1),
                                  source.scale(p0,-k)),Q(1,k+1))
        p0,p1=p1,p2
    return p1


def integral_poly(p):
    return sum((v*Q(2**(k+1)-1,k+1) for k,v in enumerate(p)),Q(0))


def seed_averages(n,N,h,scale):
    p=legendre(n)
    # Integral b_log dt = sqrt(2n+1) sqrt(x) sum p_k x^k/(k+1/2).
    anti=[ab(c/Q(2*k+1,2)) for k,c in enumerate(p)]
    def primitive(x):
        y=arb(0)
        for c in reversed(anti):y=y*x+c
        return arb(2*n+1).sqrt()*x.sqrt()*y
    values=[]; maxerr=arb(0)
    prev=primitive(arb(1))
    for j in range(N):
        x=((j+1)*h).exp()
        now=primitive(x)
        value=(now-prev)/h
        z,e=quantize(value,scale)
        values.append(z);maxerr=maxerr.max(e)
        prev=now
    dp=source.deriv(p)
    derivative=source.add(source.scale(p,Q(1,2)),[Q(0)]+dp)
    derivative_sq=(2*n+1)*integral_poly(source.mul(derivative,derivative))
    return values,maxerr,ab(derivative_sq).sqrt()


def dotshift(x,y,shift):
    lo=max(0,shift);hi=min(len(x),len(y)+shift)
    return sum((x[k]*y[k-shift] for k in range(lo,hi)),0)


def spline_ip(x,y,m,N,h,scale):
    s=m*N
    numerator=(66*dotshift(x,y,s)
               +26*(dotshift(x,y,s-1)+dotshift(x,y,s+1))
               +dotshift(x,y,s-2)+dotshift(x,y,s+2))
    return h*h*h*ab(Q(numerator,120*scale**4))


def run(N=16384,indices=(20,24)):
    path=Path(__file__).resolve().parent
    src_path=path/'records'/'source_norm_enclosures.json'
    src_record=json.loads(src_path.read_text())
    require(src_record['script_sha256']==hashlib.sha256((path/'source_norm_enclosures.py').read_bytes()).hexdigest(),
            'Source norm record does not match its generating script; regenerate it.')
    prec=320
    prec_record,_,_=prolate.certify(rank=32,precision_bits=prec)
    ctx.prec=prec
    gamma=ab(prec_record['gamma_exact'])
    tau_data=prec_record['bounds']['cosine_trace_norm_bound']['ball']
    tau=arb((int(tau_data[0][0]),tau_data[0][1]),(int(tau_data[1][0]),tau_data[1][1]))
    a=arb(2).log();h=a/N;r=1/arb(2).sqrt();alpha=ab(Q(3,2));kappa=(1+r)*(1+r)
    scale=2**80
    cutoff=ab(Q(1,10**40))
    seed_data=[]
    for n in indices:
        coeffs,qe,derivative=seed_averages(n,N,h,scale)
        df=math.prod(range(1,2*n+2,2))
        leak=2*arb.pi()**n/df
        delta=leak/gamma.sqrt()
        smooth=(2*(2*n+1)*cutoff).sqrt()
        d=delta+smooth
        z=kappa*d+(alpha+2**n)*delta
        seed_data.append((coeffs,qe,derivative,d,z))
        print(json.dumps({'seed':n,'projection_error':str(d),'Aq_proxy_error':str(z)}),flush=True)
    dim=len(indices)
    # Exact sources and true trial vectors are both real.
    A=arb_mat([[errball(alpha if i==j else arb(0),kappa*(seed_data[i][3]+seed_data[j][3]))
                for j in range(dim)]for i in range(dim)])
    prolate.ldl_positive(A)
    Ai=A.inv()
    c_norm=(alpha*alpha+r*r).sqrt()
    K=arb_mat([[errball(c_norm*c_norm if i==j else arb(0),
                c_norm*(seed_data[i][4]+seed_data[j][4])+seed_data[i][4]*seed_data[j][4])
                for j in range(dim)]for i in range(dim)])
    outputs=[]
    for sid,row in enumerate(src_record['sources']):
        normalizer=source.record_ball(row['normalizer'])
        L1=source.record_ball(row['normalized_L1'])
        L1d1=source.record_ball(row['normalized_derivative_L1_cauchy_bounds'][1])
        L1d2=source.record_ball(row['normalized_derivative_L1_cauchy_bounds'][2])
        radius=int(math.ceil(float(source.B)/float(h)))+1
        require(radius*h > source.ball(source.B),'Grid must cover full source support')
        fv=[];fe=arb(0)
        for j in range(-radius,radius+1):
            value=source.source_value(sid,j*h,normalizer=normalizer)
            q,e=quantize(value,scale);fv.append(q);fe=fe.max(e)
        require(fv[0]==0 and fv[-1]==0,'Source grid endpoints must be outside support')
        source_rounding=(2*radius+2)*h*fe
        source_interp=h*h*L1d2/8
        fpoly=fmpz_poly(fv)
        convolutions=[];proxy_errors=[]
        for seed,qe,bd,d,z in seed_data:
            convolutions.append([int(v) for v in (fpoly*fmpz_poly(seed)).coeffs()])
            e=(h*h/(arb.pi()*arb.pi())*L1d1*bd+source_interp+source_rounding
               +(L1+source_interp+source_rounding)*a.sqrt()*qe)
            proxy_errors.append((1+r)*e)
        # Inner products of the base C_F b proxies at integer prime translations.
        def base(i,j,m):return spline_ip(convolutions[i],convolutions[j],m,N,h,scale)
        def response(i,j,m):
            return alpha*base(i,j,m)-r*(base(i,j,m+1)+base(i,j,m-1))
        Hhat=[[response(i,j,0) for j in range(dim)]for i in range(dim)]
        Jhat=[[alpha*Hhat[i][j]-r*response(i,j,1) for j in range(dim)]for i in range(dim)]
        y_norms=[Hhat[i][i].sqrt() for i in range(dim)]
        c_norms=[((alpha*alpha+r*r)*Hhat[i][i]-alpha*r*(response(i,i,1)+response(i,i,-1))).sqrt()
                 for i in range(dim)]
        mu=(1+r)*L1
        e_y=[proxy_errors[i]+mu*seed_data[i][3] for i in range(dim)]
        e_c=[(alpha+r)*proxy_errors[i]+mu*seed_data[i][4] for i in range(dim)]
        H=arb_mat([[errball(Hhat[i][j],e_y[i]*y_norms[j]+e_y[j]*y_norms[i]+e_y[i]*e_y[j])
                    for j in range(dim)]for i in range(dim)])
        J=arb_mat([[errball(Jhat[i][j],e_y[i]*c_norms[j]+e_c[j]*y_norms[i]+e_y[i]*e_c[j])
                    for j in range(dim)]for i in range(dim)])
        prolate.ldl_positive(H)
        BN=(Ai*H).trace()
        correction=-2*(Ai*J).trace()+(Ai*K*Ai*H).trace()
        gamma_upper=source.record_ball(row['gamma_upper_bound_D2F'])
        epscoef=source.record_ball(row['B_infinity_D2F_epsilon_supnorm_coefficient'])
        h0upper=gamma_upper+epscoef*tau
        # h0 >= ell² B_N follows from H>=0 and A>=ell² on the full space.
        ell2=(1-r)*(1-r)
        h0lower=ell2*BN.lower()
        h0=interval(h0lower,h0upper)
        residual_raw=h0+correction
        require(residual_raw.upper()>0,'Inconsistent residual upper bound')
        residual=interval(arb(0).max(residual_raw.lower()),residual_raw.upper())
        B2=interval(BN.lower(),(BN+residual/ell2).upper())
        output={'source':sid,'source_L1':pack(L1),'L_operator_norm_bound':pack(mu),
                'compact_response_L2_error':[pack(e) for e in proxy_errors],
                'actual_Lq_L2_error':[pack(e) for e in e_y],
                'actual_LAq_L2_error':[pack(e) for e in e_c],
                'A':export_matrix(A),'H':export_matrix(H),'J':export_matrix(J),'K':export_matrix(K),
                'B_N':pack(BN),'h0_enclosure':pack(h0),
                'finite_residual_correction':pack(correction),'full_HS_residual_squared':pack(residual),
                'B2_enclosure':pack(B2),
                'compact_proxy_response_norms':[pack(v) for v in y_norms]}
        outputs.append(output)
        print(json.dumps({'source':sid,'B_N':str(BN),'h0':str(h0),'residual_squared':str(residual),
                          'B2':str(B2),'response_errors':[str(v)for v in e_y]}),flush=True)
    record={'date':'2026-09-29','model':'GPT-6 (Codex)','serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'Certified actual-Sonin trial matrices and full but coarse residual bound; no arithmetic residual sign or evaluated return moments.',
            'precision_bits':prec,'N':N,'seed_degrees':list(indices),'smooth_cutoff_width':'1/10^40',
            'dyadic_coefficient_bits':80,'gamma_exact':prec_record['gamma_exact'],
            'source_record_sha256':hashlib.sha256(src_path.read_bytes()).hexdigest(),
            'script_hashes':{name:hashlib.sha256((path/name).read_bytes()).hexdigest() for name in
                            ('sonin_trial_enclosure.py','source_norm_enclosures.py','prolate_certificate.py')},
            'seed_bounds':[{'n':n,'q_minus_b_L2':pack(data[3]),'Aq_minus_c_L2':pack(data[4]),
                            'b_log_derivative_L2':pack(data[2])}for n,data in zip(indices,seed_data)],
            'sources':outputs}
    return record


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grid',type=int,default=16384)
    parser.add_argument('--seed-degrees',type=int,nargs='+',default=[20,24])
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent / 'records' / 'sonin_trial_enclosure.json')
    args=parser.parse_args()
    require(args.grid>0 and len(set(args.seed_degrees))==len(args.seed_degrees),
            'Use a positive grid and distinct seed degrees')
    record=run(args.grid,tuple(args.seed_degrees))
    args.output.write_text(json.dumps(record,indent=2)+'\n')
