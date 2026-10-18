#!/usr/bin/env python3
"""Exact rational scalar certificate, conditional on the analytic contract.

17 October 2026. Prepared for Edward Baker with LLM assistance.
Recorded model: gpt-6.1-sol; reasoning effort ultra.

This certifies scalar inequalities only. It does not certify the Burgers
characteristic contract or H12; these remain separate analytic premises.
All inequalities deciding the result use fractions.Fraction, never floats.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys


def log_interval(x, terms=40):
    """For rational x>=1, rigorous rational natural-log enclosure.

    Reduce x by a power of 2 to [1,2), then use
      log r = 2 sum_{k>=0} z^(2k+1)/(2k+1), z=(r-1)/(r+1).
    The positive remainder after `terms` is bounded by
      2 z^(2 terms+1)/((2 terms+1)(1-z^2)).
    Thus z<=1/3 for every series evaluated here.
    """
    x=F(x)
    if x < 1:
        lo,hi=log_interval(1/x,terms)
        return -hi,-lo
    def basic(r):
        z=(r-1)/(r+1)
        lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
        tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return lo,lo+tail
    k=0
    while x >= 2:
        x/=2
        k+=1
    lo,hi=basic(x)
    l2,h2=basic(F(2))
    return lo+k*l2,hi+k*h2


def exp_negative_interval(x, degree=30):
    """For 0<=x<=1, odd/even alternating partial sums bound exp(-x)."""
    x=F(x)
    assert 0 <= x <= 1 and degree%2==0
    term=F(1)
    total=term
    for k in range(1,degree+1):
        term *= -x/F(k)
        total += term
    # total is the even partial sum; subtract the next positive magnitude.
    return total-x**(degree+1)/F(factorial(degree+1)),total


def factorial(n):
    ans=1
    for k in range(2,n+1): ans*=k
    return ans


def cube_root_interval(x, steps=160):
    """Bisection invariant lo^3<=x<=hi^3, with rational endpoints."""
    x=F(x)
    lo,hi=F(0),max(F(1),x)
    for _ in range(steps):
        mid=(lo+hi)/2
        if mid**3 <= x: lo=mid
        else: hi=mid
    assert lo**3 <= x <= hi**3
    return lo,hi


def decimal_outward(lo,hi,places=18):
    scale=10**places
    low=(lo.numerator*scale)//lo.denominator
    high=-((-hi.numerator*scale)//hi.denominator)
    def fmt(n):
        return ('-' if n<0 else '')+str(abs(n)//scale)+'.'+str(abs(n)%scale).zfill(places)
    assert F(low,scale) <= lo <= hi <= F(high,scale)
    return [fmt(low),fmt(high)]


def primes_up_to(n):
    prime=[True]*(n+1)
    prime[0]=prime[1]=False
    for p in range(2,n+1):
        if prime[p]:
            for k in range(p*p,n+1,p):prime[k]=False
    return [p for p in range(2,n+1) if prime[p]]


def main():
    # At p=3: C_even=(log(q/pi)-gamma)/4 - (-zeta'/zeta)(2)/2.
    # For odd characters psi(3/2)>=psi(1)=-gamma, so the even bound suffices.
    # pi=4 int_0^1 1/(1+x^2) dx <4; log4<7/5 is checked below.
    log10lo,log10hi=log_interval(10)
    log4lo,log4hi=log_interval(4)
    assert log10lo > F(23,10)
    assert log4hi < F(7,5)

    # H_n-log n decreases to gamma, so gamma < H_1000-log1000.
    N=1000
    H=sum((F(1,n) for n in range(1,N+1)),F(0))
    gamma_upper=H-3*log10lo
    assert gamma_upper < F(29,50)

    # -zeta'/zeta(2)=sum_n Lambda(n)/n^2.
    # Prime powers <=N are enclosed explicitly. For n>N, Lambda(n)<=log n;
    # log(x)/x^2 decreases for x>=1000, hence the remainder is bounded by
    # int_N^infinity log(x)/x^2 dx = (log N+1)/N.
    partial_lo=partial_hi=F(0)
    prime_power_count=0
    for p in primes_up_to(N):
        lp,hp=log_interval(p)
        pk=p
        while pk<=N:
            partial_lo += lp/(pk*pk)
            partial_hi += hp/(pk*pk)
            prime_power_count+=1
            pk*=p
    tail=(3*log10hi+1)/N
    zeta_hi=partial_hi+tail
    assert zeta_hi < F(3,5)

    # q>=10^12: log(q/pi)>12*(23/10)-7/5.
    # All three preceding strict bounds imply C_even,C_odd>1221/200>6.
    C_lower=(12*F(23,10)-F(7,5)-F(29,50))/4-F(3,5)/2
    assert C_lower==F(1221,200) and C_lower>6

    # Scalar contract: Q'<=-2-(4m/3-1)Q, m=C exp(-t/2)/D,
    # D=1+2C(1-exp(-t/2)). Its integrating factor is exp(-t)*D^(4/3).
    # For C=6 and T=27/100,
    # J(T)=13/168*(D^(7/3)-1)-1/240*(D^(10/3)-1).
    # Starting with Q(0)<=1, J(T)>1/2 forces contact with Q=0 by T.
    C,T=F(6),F(27,100)
    exp_lo,exp_hi=exp_negative_interval(T/2)
    Dlo=1+2*C*(1-exp_hi)
    Dhi=1+2*C*(1-exp_lo)
    root_lo,_=cube_root_interval(Dlo)
    _,root_hi=cube_root_interval(Dhi)
    Jlo=F(13,168)*(Dlo**2*root_lo-1)-F(1,240)*(Dhi**3*root_hi-1)
    Jhi=F(13,168)*(Dhi**2*root_hi-1)-F(1,240)*(Dlo**3*root_lo-1)
    assert Jlo <= Jhi and Jlo>F(1,2)
    rec={
        'date':'2026-10-17',
        'prepared_for':'Edward Baker',
        'llm_assistance':'gpt-6.1-sol; reasoning effort ultra',
        'status':'exact rational scalar certificate; analytic contract and H12 assumed, not certified',
        'arithmetic':'Python fractions.Fraction; no floating-point decision',
        'parameters':{'C':'6','T':'27/100','p':'3','q_min':'1000000000000','log_series_terms':40,'exp_even_degree':30,'cube_root_bisections':160,'von_mangoldt_cutoff':N},
        'runtime':{'python':sys.version,'platform':platform.platform(),'machine':platform.machine()},
        'log10':decimal_outward(log10lo,log10hi),
        'log4':decimal_outward(log4lo,log4hi),
        'gamma_upper':decimal_outward(gamma_upper,gamma_upper),
        'zeta_log_derivative':{'prime_powers_at_most_N':prime_power_count,'partial_sum':decimal_outward(partial_lo,partial_hi),'tail_upper':decimal_outward(tail,tail),'full_upper':decimal_outward(zeta_hi,zeta_hi),'proved_less_than':'3/5'},
        'C_both_parities_strict_lower_bound':str(C_lower),
        'exp_minus_T_over_2':decimal_outward(exp_lo,exp_hi),
        'D':decimal_outward(Dlo,Dhi),
        'J':decimal_outward(Jlo,Jhi),
        'J_minus_half':decimal_outward(Jlo-F(1,2),Jhi-F(1,2)),
        'conditional_scalar_check':'PASS: J(T)>1/2; C_q,a(3)>6 for q>=10^12, a=0,1',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(rec,indent=2,sort_keys=True))


if __name__=='__main__':main()
