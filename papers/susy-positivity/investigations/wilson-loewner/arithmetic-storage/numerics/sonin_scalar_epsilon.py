#!/usr/bin/env python3
"""Certified integrated Sonin error kernel for the exact A17 sources.

Prepared for Edward Baker with GPT-6 (Codex), 29 September 2026.
Serving variant and reasoning effort not exposed. Requires python-flint.
"""
import argparse, hashlib, json, math, sys, time
from fractions import Fraction as Q
from pathlib import Path
from flint import arb, arb_mat, arb_poly, fmpz_poly, ctx, fmpq


def require(condition, message):
    if not condition: raise ArithmeticError(message)


def ab(q):
    q=Q(q); return arb(fmpq(q.numerator,q.denominator))


def pack(v):
    return {'display':v.str(30),'rational_lower':str(v.lower().fmpq()),
            'rational_upper':str(v.upper().fmpq())}


def add_error(v,e):return v+arb(0,e.abs_upper())


def quantize(v,scale):
    if v.abs_upper()<arb(1)/(2*scale): return 0,v.abs_upper()
    q=Q(str(v.mid().fmpq()))*scale
    z=(2*q.numerator+q.denominator)//(2*q.denominator)
    return z,(v-ab(Q(z,scale))).abs_upper()


def exponential_model(prolate,K,bits,rho_max):
    certificate,C,R=prolate.certify(rank=32,precision_bits=bits)
    ctx.prec=bits
    n=C.nrows()
    L=arb_mat([[arb(0) for _ in range(n)] for _ in range(n)])
    for k in range(n):
        for i in range(k+1):
            c=Q((-1)**(k-i)*math.factorial(2*k+2*i),
                2**(2*k)*math.factorial(k-i)*math.factorial(k+i)*math.factorial(2*i))
            L[k,i]=arb(4*k+1).sqrt()*ab(c)
    T=L.transpose()*(C*R)*L
    positive=[];negative=[arb(0) for _ in range(n)]
    for k in range(K):
        ck=2*(-1)**k*(2*arb.pi())**(2*k)/math.factorial(2*k)
        ak=arb(0)
        for j in range(n):
            term=ck*sum((T[i,j]/((2*i+2*k+1)*(2*j+2*k+1)) for i in range(n)),arb(0))
            ak+=term;negative[j]+=term
        positive.append((Q(4*k+1,2),ak))
    terms=positive+[(Q(-4*j-1,2),-v) for j,v in enumerate(negative)]
    # The real cosine Lagrange remainder is bounded pointwise by z^(2K)/(2K)!.
    # The B-kernel occupies a subrectangle of the unit square, so this also
    # bounds its Hilbert-Schmidt norm, with its 2 sqrt(rho) prefactor.
    tau=ab('2.858');rn=prolate.frobenius(R)
    tnorm=(tau+ab("1.5e-40"))*rn
    kernel_tail=2*rho_max.sqrt()*(2*arb.pi()*rho_max)**(2*K)/math.factorial(2*K)
    remainder=tnorm*kernel_tail+ab('2.7e-31')
    gamma=ab('57/1000000')
    eps_sup=tau/gamma.sqrt()
    return terms,remainder,eps_sup,certificate,tnorm


def endpoint_corrections(q):
    require(abs(q)<1,'Endpoint series requires |lambda*h|<1')
    c0=arb(0);c1=arb(0)
    for n in range(1,82,2):
        term=2*q**n/math.factorial(n+4)
        c1+=term;c0+=(2**(n+4)-4)*term
    # Overbound all degrees n>=83, hence also the omitted odd terms.
    n=83;x=abs(q).abs_upper()
    rem1=2*x**n/math.factorial(n+4)/(1-x/(n+5))
    rem0=2*(2**(n+4)+4)*x**n/math.factorial(n+4)/(1-2*x/(n+5))
    return add_error(c0,rem0),add_error(c1,rem1)


def integrate_exponential_correlation(poly,a0,a1,h,lam,scale):
    q=ab(lam)*h
    K4=((q/2).sinh()/(q/2))**4
    c0,c1=endpoint_corrections(q)
    return h*h/(scale*scale)*(K4*(2*poly(q.exp())-a0)+a0*c0+2*a1*c1)


def run(numerics,N,K,bits):
    sys.path.insert(0,str(numerics))
    import source_norm_enclosures as source
    import prolate_certificate as prolate
    src_path=numerics/'records/source_norm_enclosures.json'
    src_record=json.loads(src_path.read_text())
    require(src_record['script_sha256']==hashlib.sha256((numerics/'source_norm_enclosures.py').read_bytes()).hexdigest(),'Source hash mismatch')
    ctx.prec=bits
    h=arb(2).log()/N;r=1/arb(2).sqrt();alpha=ab('3/2')
    radius=math.ceil(float(source.B)/float(h))+1
    require(radius*h>source.ball(source.B),'Source grid support guard failed')
    # Interpolants may extend one grid step past the exact source support.
    tmax=(2*radius+N+2)*h
    terms,kernel_error,eps_sup,pcert,tnorm=exponential_model(prolate,K,bits,tmax.exp())
    require(kernel_error<ab('1e-20'),'Cosine expansion tail too large')
    scale=2**80
    print(json.dumps({'stage':'kernel','terms':len(terms),'kernel_error':str(kernel_error),'epsilon_sup':str(eps_sup),'rho_max':str(tmax.exp())}),flush=True)
    outputs=[]
    for sid,row in enumerate(src_record['sources']):
        norm=source.record_ball(row['normalizer'])
        L1=source.record_ball(row['normalized_L1'])
        L1d2=source.record_ball(row['normalized_derivative_L1_cauchy_bounds'][2])
        values=[];qe=arb(0)
        for j in range(-radius,radius+1):
            z,e=quantize(source.source_value(sid,j*h,normalizer=norm),scale)
            values.append(z);qe=qe.max(e)
        require(values[0]==values[-1]==0,'Interpolation endpoints nonzero')
        interp_error=h*h*L1d2/8
        rounding_error=(2*radius+2)*h*qe
        eta=interp_error+rounding_error
        fp=fmpz_poly(values)
        conv=(fp*fmpz_poly(list(reversed(values)))).coeffs()
        mid=len(values)-1
        aa=[int(conv[mid+j]) if mid+j<len(conv) else 0 for j in range(mid+1)]
        def ac(m):return aa[abs(m)] if abs(m)<len(aa) else 0
        cross=[ac(m-N)+ac(m+N) for m in range(len(aa)+N)]
        p=arb_poly(aa);cp=arb_poly(cross)
        ebase=arb(0);ecross=arb(0)
        for lam,c in terms:
            ebase+=c*integrate_exponential_correlation(p,aa[0],aa[1],h,lam,scale)
            ecross+=c*integrate_exponential_correlation(cp,cross[0],cross[1],h,lam,scale)
        ef=ebase
        eh=alpha*ebase-r*ecross
        ef_interp=eps_sup*eta*(2*L1+eta)
        eh_interp=eps_sup*(1+r)**2*eta*(2*L1+eta)
        ef_kernel=kernel_error*(L1+eta)**2
        eh_kernel=kernel_error*(1+r)**2*(L1+eta)**2
        ef=add_error(ef,ef_interp+ef_kernel)
        eh=add_error(eh,eh_interp+eh_kernel)
        out={'source':sid,'E_F':pack(ef),'E_D2F':pack(eh),
             'computed_interpolant_E_F':pack(ebase),'computed_interpolant_E_D2F':pack(alpha*ebase-r*ecross),
             'L1_interpolation_error':pack(interp_error),'L1_rounding_error':pack(rounding_error),
             'E_F_interpolation_error':pack(ef_interp),'E_D2F_interpolation_error':pack(eh_interp),
             'E_F_kernel_error':pack(ef_kernel),'E_D2F_kernel_error':pack(eh_kernel),
             'nodal_coefficients_sha256':hashlib.sha256(json.dumps(values,separators=(',',':')).encode()).hexdigest()}
        outputs.append(out)
        print(json.dumps({'source':sid,'E_F':str(ef),'E_D2F':str(eh),'eta':str(eta)}),flush=True)
    return {'status':'CERTIFIED','date':'2026-09-29','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'Integrated archimedean Sonin epsilon correction only; no arithmetic residual sign.',
            'grid_N':N,'precision_bits':bits,'cosine_terms':K,'dyadic_coefficient_bits':80,
            'source_grid_radius':radius,'kernel_domain_rho_upper':pack(tmax.exp()),
            'kernel_uniform_error':pack(kernel_error),'epsilon_supnorm_bound':pack(eps_sup),
            'finite_smoothed_resolvent_trace_norm_upper':pack(tnorm),
            'source_record_sha256':hashlib.sha256(src_path.read_bytes()).hexdigest(),
            'script_hashes':{str(name):hashlib.sha256(path.read_bytes()).hexdigest() for name,path in
             [('sonin_scalar_epsilon.py',Path(__file__)),('source_norm_enclosures.py',numerics/'source_norm_enclosures.py'),('prolate_certificate.py',numerics/'prolate_certificate.py')]},
            'sources':outputs}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--grid',type=int,default=262144)
    parser.add_argument('--cosine-terms',type=int,default=80)
    parser.add_argument('--precision-bits',type=int,default=512)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'records/sonin_scalar_epsilon.json')
    args=parser.parse_args()
    require(args.grid>512 and args.cosine_terms>=64 and args.precision_bits>=384,'Insufficient certificate parameters')
    result=run(args.numerics,args.grid,args.cosine_terms,args.precision_bits)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
