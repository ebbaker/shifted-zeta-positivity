#!/usr/bin/env python3
"""Exact algebra for the nonsquarefree mu*mu discrete-moment test.

Prepared for Edward Baker, 23 October 2026, with substantial LLM assistance.
Recorded model: gpt-6-astra (Codex); reasoning effort: ultra.
Requires only Python 3 and SymPy; no local-data dependencies.

This checks symbolic Euler factors, complete shift derivatives, rational
transforms, and positive norm coefficients. Arithmetic asymptotics and the
normalized density argument are proved separately in the accompanying note.
The raw cross with the low-degree P0 is explicitly a formal check only.
"""
from __future__ import annotations
import argparse
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path
import sympy as S

s,t,a,b,c,theta,x = S.symbols('s t a b c theta x')
checks=[]

def check(condition,name):
    if not condition:
        raise AssertionError(name)
    checks.append({'name':name,'passed':True})

def equal(actual,expected,name):
    diff=S.cancel(actual-expected)
    if diff != 0:
        raise AssertionError(f'{name}: {diff}')
    checks.append({'name':name,'passed':True,'exact_difference':'0'})

def homogeneous(poly,max_degree):
    result={d:S.S.Zero for d in range(max_degree+1)}
    for monomial,coefficient in S.Poly(S.expand(poly),a,b,c).terms():
        d=sum(monomial)
        if d<=max_degree:
            result[d]+=coefficient*a**monomial[0]*b**monomial[1]*c**monomial[2]
    return result

def I(r,q):
    # F_rq=b(s+b)^r(t+a)^q(t+c)^q/[(a+b)(b+c)(s+t)^(rq)t^q].
    h=homogeneous(b*(s+b)**r*(t+a)**q*(t+c)**q,5)
    numerator=(a-c)*h[5]
    for k in range(5):
        numerator+=(b+c)*(-a-b)**k/S.factorial(k)*h[5-k].subs({a:-b,b:-a,c:c},simultaneous=True)
        numerator-=(a+b)*(-b-c)**k/S.factorial(k)*h[5-k].subs({a:a,b:-c,c:-b},simultaneous=True)
    quotient,remainder=S.div(S.Poly(S.expand(numerator),a,b,c,s,t),S.Poly((a+b)*(b+c)*(a-c),a,b,c,s,t))
    check(remainder.is_zero,f'I{r}{q}: exact shift-pole cancellation')
    return S.factor(S.Poly(quotient.as_expr(),a,b,c).coeff_monomial(a*b*c)/((s+t)**(r*q)*t**q))

def J(r,q):
    # G_rq=(s+b)^r(t+a)^q/[(a+b)(s+t)^(rq)].
    h=homogeneous((s+b)**r*(t+a)**q,3)
    numerator=h[3]-sum((-a-b)**k/S.factorial(k)*h[3-k].subs({a:-b,b:-a},simultaneous=True) for k in range(4))
    quotient,remainder=S.div(S.Poly(S.expand(numerator),a,b,s,t),S.Poly(a+b,a,b,s,t))
    check(remainder.is_zero,f'J{r}{q}: exact shift-pole cancellation')
    return S.factor(S.Poly(quotient.as_expr(),a,b).coeff_monomial(a*b)/((s+t)**(r*q)))

def K(r,q):
    return S.factor(I(r,q)+I(q,r).subs({s:t,t:s},simultaneous=True)+J(r,q))

def local_factor(r,q):
    # Exact p-adic triple sum at all shifts and Mellin variables zero;
    # h*k=0 is the local form of gcd(h,k)=1. Here x=1/p.
    answer=0
    for g in range(min(r,q)+1):
        for hh in range(r-g+1):
            for kk in range(q-g+1):
                if hh and kk:
                    continue
                left=(-1)**(g+hh)*S.binomial(r,g+hh)
                right=(-1)**(g+kk)*S.binomial(q,g+kk)
                answer+=left*right*x**(g+hh+kk)
    return S.expand(answer)

def inverse(expr):
    # Finite sum of exact double inverse-Laplace monomial transforms.
    # together(), rather than a multivariate gcd, avoids needless large
    # integer factorization for the degree-100 profile.
    numerator,denominator=S.fraction(S.together(expr))
    powers=S.factor(denominator).as_powers_dict()
    aa,bb,cc=(int(powers.get(v,0)) for v in (s,t,s+t))
    constant=S.cancel(denominator/(s**aa*t**bb*(s+t)**cc))
    if {s,t}&constant.free_symbols:
        raise ValueError('Unexpected denominator')
    answer=0
    for (i,j),coefficient in S.Poly(numerator,s,t).terms():
        A,B,C=aa-i,bb-j,cc
        if C==0:
            term=theta**(A+B-2)/(S.factorial(A-1)*S.factorial(B-1)) if A>0 and B>0 else S.S.Zero
        elif A>0 and B>0:
            term=theta**(A+B+C-2)*S.factorial(A+B-2)/(S.factorial(A-1)*S.factorial(B-1)*S.factorial(A+B+C-2))
        elif A+B>1:
            term=S.S.Zero
        else:
            raise ValueError(f'Unpaid boundary term: {A=}, {B=}, {C=}')
        answer+=coefficient/constant*term
    return S.factor(answer)

def exponential_residue(expr,pole):
    u=S.Symbol('u')
    shifted=S.cancel(expr.subs(s,u+pole))
    numerator,denominator=S.fraction(shifted)
    numerator_order=min(mon[0] for mon,coef in S.Poly(numerator,u).terms())
    denominator_order=min(mon[0] for mon,coef in S.Poly(denominator,u).terms())
    order=max(0,denominator_order-numerator_order)
    jet=sum((theta*u)**j/S.factorial(j) for j in range(order))
    return S.factor(S.residue(shifted*jet,u,0))

def D(B):
    return (
        B*(B-1)/(48*(2*B-1)*(2*B-3))
        +B*theta/(3*(2*B-1)*(2*B+1))
        +theta**2/((B+1)*(2*B+1))
        +(5*B+3)*theta**3/((B+1)**2*(2*B+1)*(2*B+3))
        +theta**4/((B+1)**2*(B+2)**2)
    )

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    started=time.monotonic()
    local={f'E{r}{q}':local_factor(r,q) for r,q in ((1,1),(1,2),(2,2))}
    equal(local['E11'],1-x,'ordinary Euler factor including prime powers')
    equal(local['E12'],1-x,'mixed Euler factor including prime powers')
    equal(local['E22'],1-x**2,'mu2 square Euler factor including prime powers')
    equal(local['E12']/(1-x),1,'mixed arithmetic factor at the origin')
    equal(local['E22']/(1-x)*(1-x),1-x**2,'square arithmetic factor after extracting one zeta pole')
    kernels={f'K{r}{q}':K(r,q) for r,q in ((1,1),(1,2),(2,2))}
    expected11=(s**2*t**2+4*s**2*t+6*s**2+4*s*t**2+12*s*t+12*s+6*t**2+12*t)/(12*s*t*(s+t))
    expected12=(s**2*t**4+8*s**2*t**3+24*s**2*t**2+24*s**2*t+12*s**2+4*s*t**4+24*s*t**3+48*s*t**2+24*s*t+6*t**4+24*t**3+12*t**2)/(12*s*t**2*(s+t)**2)
    expected22=(s**4*t**4+8*s**4*t**3+24*s**4*t**2+24*s**4*t+12*s**4+8*s**3*t**4+48*s**3*t**3+96*s**3*t**2+48*s**3*t+24*s**2*t**4+96*s**2*t**3+72*s**2*t**2+24*s*t**4+48*s*t**3+12*t**4)/(12*s**2*t**2*(s+t)**4)
    for label,expected in [('K11',expected11),('K12',expected12),('K22',expected22)]:
        equal(kernels[label],expected,f'{label}: complete kernel formula')
    M0=lambda z:(1+theta)/(theta*z**2)-2/(theta*z**3)
    inner=M0(s)*kernels['K12']
    r0=exponential_residue(inner,0)
    rm=exponential_residue(inner,-t)
    expected_r0=(1+theta)**3*(1+4/t+2/t**2)/(12*theta)
    expected_rm=-(theta*(theta+1)*t+(4*theta**2+7*theta+1)+(6*theta**2+14*theta+4)/t+(6*theta+2)/t**2)/(12*theta)
    equal(r0,expected_r0,'formal P0 cross: residue at zero')
    equal(rm,expected_rm,'formal P0 cross: residue at -t after removing exp(-theta*t)')

    # General norm identity for every integer B>=2, as a rational identity
    # in B. Factorial ratios are expressed by four elementary factors.
    B=S.Symbol('B',integer=True,positive=True)
    numerator=S.Poly(S.expand(kernels['K22']*12*s**2*t**2*(s+t)**4),s,t)
    def factorial_ratio(i):
        if i>=2:
            return S.prod(B-j for j in range(i-2))
        return 1/S.prod(B+j for j in range(1,3-i))
    general_norm=0
    for (i,j),coefficient in numerator.terms():
        common_ratio=1/S.prod(2*B+k-i-j for k in range(5,9))
        general_norm+=coefficient*S.Rational(1,12)*factorial_ratio(i)*factorial_ratio(j)*common_ratio*theta**(8-i-j)
    equal(general_norm,D(B),'general B>=2: complete norm integral equals positive D_B')

    cases=[]
    ctheta=6*theta/(1+theta)**3
    for degree in (2,5,100):
        n=S.Integer(degree)
        MB=lambda z:S.factorial(n)/(theta**n*z**(n+1))
        norm=inverse(kernels['K22']*MB(s)*MB(t))
        equal(norm,D(n),f'B={degree}: direct norm transform')
        check(all(coef>0 for coef in S.Poly(norm,theta).all_coeffs()),f'B={degree}: all norm polynomial coefficients positive')
        cross=inverse(kernels['K12']*M0(s)*MB(t))
        mean=S.Rational(1,2)+2*theta/(n+1)+theta**2/((n+1)*(n+2))
        equal(mean-ctheta*cross,0,f'B={degree}: formal raw P0 residual')
        tail=S.cancel(MB(t)*rm)
        num,den=S.fraction(tail)
        check(S.degree(den,t)-S.degree(num,t)>=2,f'B={degree}: formal residue tail has no boundary contribution')
        cases.append({'B':degree,'first_moment':str(mean),'formal_raw_P0_cross':str(cross),'formal_raw_residual':'0','D_B':str(norm),'D_B_at_half':str(norm.subs(theta,S.Rational(1,2)))})
    low_tail=S.cancel(rm/(theta*t**2))
    num,den=S.fraction(low_tail)
    check(S.degree(den,t)-S.degree(num,t)==1,'B=1: boundary obstruction retained explicitly')

    result={
        'status':'passed','scope':'exact symbolic algebra only; arithmetic limits and normalized Gram convergence are proved in the accompanying note',
        'prepared_for':'Edward Baker','research_date':'2026-10-23',
        'llm_assistance':{'model':'gpt-6-astra (Codex)','reasoning_effort':'ultra'},
        'run_utc':datetime.now(timezone.utc).isoformat(),'python_version':platform.python_version(),'sympy_version':S.__version__,
        'elapsed_seconds':round(time.monotonic()-started,6),
        'local_euler_factors':{k:str(v) for k,v in local.items()},
        'arithmetic_factors':{'mixed_mu_mu2':'1','mu2_square':'1/zeta(2)'},
        'logarithmic_normalization':{'general_pair_exponent':'(r-1)*(q-1)','mixed_mu_mu2':0,'mu2_square':1,'finite_norm_direction':'w_mu2/sqrt(log(T))'},
        'kernels':{k:str(v) for k,v in kernels.items()},
        'formal_raw_P0_residues':{'R0':str(r0),'Rtheta':str(expected_rm)},
        'general_positive_D_B':str(D(B)),
        'examples':cases,
        'actual_theorem_scope':'Use B=100. The note proves mean(v)->0, <w0,v>->0, norm(v)^2->D_100/zeta(2)>0. Raw <w0,w_mu2> asymptotics are not asserted.',
        'low_smoothing_warning':'For Q(u)=u the unexponentiated residue tail is only O(1/t); no low-smoothing raw cross conclusion is taken.',
        'assertion_count':len(checks),'checks':checks,
    }
    output=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(output,encoding='utf-8')
        print(f'PASS: {len(checks)} exact assertions; JSON written to {args.output}')
    else:print(output,end='')

if __name__=='__main__':main()
