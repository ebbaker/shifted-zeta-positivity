#!/usr/bin/env python3
"""Certified finite exponential model for compact first-moment correction.

Prepared for Edward Baker with GPT-6 (Codex) assistance, 2026-09-29.
Serving variant and effort not exposed. Model is a linear functional of the
autocorrelation of H=D2 F. Numerical integration belongs to the driver.
"""
from fractions import Fraction as Q
import math
from flint import arb, arb_mat, ctx, fmpq


def ab(x):
    q=Q(x)
    return arb(fmpq(q.numerator,q.denominator))


def build(K=120,bits=1024,L='901/1000'):
    import prolate_certificate as prolate
    cert,C,R=prolate.certify(32,bits)
    ctx.prec=bits
    n=32; p=arb(2);r=1/p.sqrt();a=p.log();gamma=ab('57/1000000')
    transform=arb_mat(n,n)
    for k in range(n):
        for i in range(k+1):
            coeff=Q((-1)**(k-i)*math.factorial(2*k+2*i),
                    2**(2*k)*math.factorial(k-i)*math.factorial(k+i)*math.factorial(2*i))
            transform[k,i]=arb(4*k+1).sqrt()*ab(coeff)
    RM=transform.transpose()*(R-prolate.identity(n))*transform
    S=C*R
    SM=transform.transpose()*S*transform
    V=arb_mat([[arb(1)/(2*i+2*j+1) for j in range(n)] for i in range(K)])
    D=arb_mat([[arb(1)/(2*i+2*j+1) for j in range(K)] for i in range(K)])
    tv=[2*(-1)**i*(2*arb.pi())**(2*i)/math.factorial(2*i) for i in range(K)]
    Ap=D+V*RM*V.transpose()
    Bp=V*SM*V.transpose()
    A=arb_mat(K,K);B=arb_mat(K,K)
    for i in range(K):
        for j in range(K):
            A[i,j]=tv[i]*tv[j]*Ap[i,j]
            B[i,j]=tv[i]*tv[j]*Bp[i,j]+(tv[i] if i==j else arb(0))
    strip=arb_mat([[p**(2*j)*(1-p**(-2*i-2*j-1))/(2*i+2*j+1)
                   for j in range(K)] for i in range(n)])
    cross=2*(RM.transpose()*strip*A.transpose()+SM.transpose()*strip*B.transpose())
    whole={Q(4*j+1,2):arb(0) for j in range(K)}
    whole.update({Q(-4*j-1,2):arb(0) for j in range(K)})
    before={lam:arb(0) for lam in whole}
    def jterm(i,j,w,kind):
        d=2*i+2*j+1;w=w/d
        lp=Q(4*j+1,2);ln=Q(-4*i-1,2)
        if kind=='full':
            whole[lp]+=w;whole[ln]-=w
        elif kind=='upper':
            whole[ln]+=w*(p**d-1)
            before[lp]+=w;before[ln]-=w*p**d
        else:
            whole[lp]+=w*(1-p**(-d))
            before[lp]+=w*p**(-d);before[ln]-=w
    for i in range(n):
        for j in range(K):jterm(i,j,cross[i,j],'full')
    for k in range(K):
        for ell in range(K):jterm(ell,k,2*A[k,ell]*p**(2*ell),'lower')
    for i in range(n):
        for j in range(n):jterm(j,i,-2*RM[i,j]*p**(-2*i-1),'upper')
    # Analytic replacement errors. X is nuclear with norm <= Gmax(a+L),
    # for a unit exact source, where its difference support is [-L,L].
    gb=(1+r)**2; z=a+ab(L); xmax=z.exp()
    xn=gb*z
    mn=prolate.frobenius(R);sn=prolate.frobenius(S)
    epsM=ab('9.2e-32');epsS=ab('2.7e-31')
    op_error=2*r*xn*(epsM*(1+mn)+epsS*(1+sn))
    def tay(arg):return 2*arg**(2*K)/math.factorial(2*K)
    dx=tay(2*arb.pi()*xmax);dy=tay(2*arb.pi()*p)
    dc=tay(2*arb.pi()*xmax*p)
    common=2*dx+2*dy+dx*dy
    ep=mn*common
    ej=dc+sn*common
    block=(xmax-1).sqrt()*(p-1).sqrt()
    cosine_error=2*r*xn*(mn*block*ep+sn*block*ej)
    # We integrated the approximating full kernels and keep all cancellations.
    # This error assumes a unit source; a driver may multiply by ||Fh||2^2.
    return {'whole':whole,'before':before,'contact':-2*a*r,
            'operator_error':op_error,'cosine_error':cosine_error,
            'L_upper':ab(L),'G_max':gb,'z_upper':z,
            'M_norm_bound':mn,'S_norm_bound':sn,'bits':bits,'K':K,
            'certificate':cert}


if __name__=='__main__':
    result=build()
    print({key:str(result[key]) for key in
           ['operator_error','cosine_error','M_norm_bound','S_norm_bound']})
