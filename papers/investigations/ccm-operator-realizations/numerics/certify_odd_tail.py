#!/usr/bin/env python3
"""Exact-rational enclosures for a CCM odd Fourier tail and scalar Schur test.

Standard library only. Analytic inequalities are proved in the linked note.
No floating-point operations, zeta zeros, or unbounded matrix truncation enter
the certificate. This certifies the stated tail, not the whole odd-sector gap.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from math import isqrt
import json
from pathlib import Path

SCALE=10**40


def down(x):
    return F((x.numerator*SCALE)//x.denominator,SCALE)


def up(x):
    return -down(-x)


class Box:
    def __init__(self,lo,hi=None):
        if isinstance(lo,float) or isinstance(hi,float):
            raise TypeError('Floating-point input is forbidden in the certificate')
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        if self.lo>self.hi:
            raise ValueError('Reversed interval')

    @staticmethod
    def cast(x):
        return x if isinstance(x,Box) else Box(x)

    def __add__(self,other):
        b=self.cast(other)
        return Box(down(self.lo+b.lo),up(self.hi+b.hi))
    __radd__=__add__

    def __neg__(self):
        return Box(-self.hi,-self.lo)

    def __sub__(self,other):
        return self+-self.cast(other)

    def __rsub__(self,other):
        return self.cast(other)+-self

    def __mul__(self,other):
        b=self.cast(other)
        values=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return Box(down(min(values)),up(max(values)))
    __rmul__=__mul__

    def __truediv__(self,other):
        b=self.cast(other)
        if b.lo<=0<=b.hi:
            raise ZeroDivisionError('Interval denominator contains zero')
        return self*Box(down(1/b.hi),up(1/b.lo))

    def __rtruediv__(self,other):
        return self.cast(other)/self

    def __pow__(self,n):
        if not isinstance(n,int) or n<0:
            raise ValueError('Use nonnegative integer interval powers')
        if n==0:
            return Box(1)
        if n%2==0 and self.lo<=0<=self.hi:
            return Box(0,up(max(abs(self.lo),abs(self.hi))**n))
        values=[self.lo**n,self.hi**n]
        return Box(down(min(values)),up(max(values)))

    def inflate(self,error):
        if isinstance(error,float):
            raise TypeError('Floating-point remainder is forbidden')
        error=F(error)
        if error<0:
            raise ValueError('Negative error radius')
        return Box(down(self.lo-error),up(self.hi+error))


def sqrt_box(x):
    x=Box.cast(x)
    if x.lo<0:
        raise ValueError('Negative square root')
    lo=isqrt(x.lo.numerator*SCALE*SCALE//x.lo.denominator)
    hi=isqrt(x.hi.numerator*SCALE*SCALE//x.hi.denominator)+1
    return Box(F(lo,SCALE),F(hi,SCALE))


@lru_cache(None)
def log_unit(x):
    """log(x) for exact 1 <= x <= 2, via positive atanh series."""
    x=F(x)
    if not 1<=x<=2:
        raise ValueError('Log series argument outside [1,2]')
    u=(x-1)/(x+1)
    term=u; total=F(0); terms=60
    for k in range(terms):
        total+=2*term/(2*k+1)
        term*=u*u
    remainder=2*term/((2*terms+1)*(1-u*u))
    return Box(down(total),up(total+remainder))


def log_point(x):
    x=F(x)
    if x<=0:
        raise ValueError('Nonpositive logarithm')
    if x<1:
        return -log_point(1/x)
    exponent=0
    while x>=2:
        x/=2; exponent+=1
    return log_unit(x)+exponent*log_unit(F(2))


def log_box(x):
    x=Box.cast(x)
    return Box(log_point(x.lo).lo,log_point(x.hi).hi)


def atan_point(x):
    x=F(x)
    if x<0:
        return -atan_point(-x)
    if x>F(1,2):
        raise ValueError('Use the alternating atan series only at |x| <= 1/2')
    total=F(0); term=x; terms=80
    for k in range(terms):
        total+=(-1)**k*term/(2*k+1)
        term*=x*x
    # An even number of terms ends below the limit.
    return Box(down(total),up(total+term/(2*terms+1)))


def atan_box(x):
    return Box(atan_point(x.lo).lo,atan_point(x.hi).hi)


PI=16*atan_point(F(1,5))-4*atan_point(F(1,239))
L=log_box(13)


def sincos(angle):
    """Taylor enclosures after one exact interval argument reduction."""
    center=(angle.lo+angle.hi)/2
    period=(PI.lo+PI.hi)
    k=(center/period+F(1,2)).numerator//(center/period+F(1,2)).denominator
    x=angle-2*k*PI
    if max(abs(x.lo),abs(x.hi))>4:
        raise ValueError('Argument reduction failed')
    ss=Box(0); cc=Box(0); st=x; ct=Box(1)
    for j in range(40):
        ss+=st; cc+=ct
        st=-st*x*x/((2*j+2)*(2*j+3))
        ct=-ct*x*x/((2*j+1)*(2*j+2))
    # Taylor's real-variable remainder; next even/odd zero coefficients included.
    bound=max(abs(x.lo),abs(x.hi)); factorial=1
    for j in range(1,82):
        factorial*=j
    return ss.inflate(bound**81/factorial),cc.inflate(bound**80/(factorial//81))


def psi_box(y,shift=64):
    """Real and imaginary parts of psi(1/4+i*y), with a Binet bound."""
    a=F(1,4); r=a+shift; den=r*r+y*y
    real=log_box(den)/2-r/(2*den)
    if (y/r).hi<F(1,2):
        angle=atan_box(y/r)
    elif (r/y).hi<F(1,2):
        angle=PI/2-atan_box(r/y)
    else:
        raise ValueError('This certificate uses only small atan arguments')
    imag=angle+y/(2*den)
    for k in range(shift):
        u=a+k; denominator=u*u+y*y
        real-=u/denominator
        imag+=y/denominator
    error=1/(12*r*r)
    return real.inflate(error),imag.inflate(error)


POWERS=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11))


def b_coefficient(n):
    d=2*PI*n/L
    _,psi_im=psi_box(d/2)
    arch=psi_im/2
    exp_factor=1/sqrt_box(13); correction=Box(0); count=30
    for k in range(count):
        a=F(1,2)+2*k
        correction+=d*exp_factor/(a*a+d*d)
        exp_factor/=169
    correction=Box(correction.lo,
                   (correction+exp_factor/(d*(1-F(1,169)))).hi)
    arch-=correction
    cosh=(sqrt_box(13)+1/sqrt_box(13))/2
    pole=-2*d*(cosh-1)/(d*d+F(1,4))
    primes=Box(0)
    for n0,p in POWERS:
        ss,_=sincos(d*log_box(n0))
        primes+=log_box(p)/sqrt_box(n0)*ss
    return (arch+primes-pole)/PI


def odd_first_diagonal():
    """Independent closed formula for the n=1 odd Weil diagonal."""
    d=2*PI/L
    psi_re,_=psi_box(d/2)
    arch=psi_re-log_box(PI)
    summation=Box(0); count=64; exp_factor=1/sqrt_box(13)
    for k in range(count):
        a=F(1,2)+2*k
        summation+=(1-exp_factor)/(a*a+d*d)**2
        exp_factor/=169
    # Sum_{k>=count} (2k+1/2)^(-4) <= (1/count^4+1/(3count^3))/16.
    remainder=(F(1,count**4)+F(1,3*count**3))/16
    summation=Box(summation.lo,(summation+remainder).hi)
    arch-=4*d*d/L*summation
    sinh2=(sqrt_box(13)+1/sqrt_box(13)-2)/4
    pole=-16*sinh2*d*d/(L*(d*d+F(1,4))**2)
    primes=Box(0)
    for n,p in POWERS:
        delay=log_box(n); ss,cc=sincos(d*delay)
        correlation=2*(1-delay/L)*cc+2*ss/(L*d)
        primes+=log_box(p)/sqrt_box(n)*correlation
    return arch+pole-primes


def endpoints(x):
    return dict(lower_rational=str(x.lo),upper_rational=str(x.hi))


def certificate():
    if not __debug__:
        raise RuntimeError('Run without -O: certificate assertions must be enabled.')
    # Sanity controls exercise sign, zero-crossing powers, and outward rounding.
    assert (Box(-2,3)**2).lo==0 and (Box(-2,3)**2).hi==9
    assert (Box(1,2)*Box(-3,-1)).lo<=-6
    assert (Box(1,2)*Box(-3,-1)).hi>=-1
    assert sqrt_box(2).lo**2<=2<=sqrt_box(2).hi**2
    assert PI.lo>F(314159,100000) and PI.hi<F(3927,1250)
    assert log_box(PI).hi<F(23,20) and log_box(2).hi<F(7,10)
    assert L.lo>F(25649,10000) and L.hi<F(513,200)

    prime_bound=Box(0); prime_rows=[]
    for n,p in POWERS:
        chain=1
        while n**chain<13:
            chain+=1
        coefficient={2:Box(1),3:sqrt_box(2),4:(1+sqrt_box(5))/2}[chain]
        term=coefficient*log_box(p)/sqrt_box(n)
        prime_bound+=term
        prime_rows.append(dict(prime_power=n,prime=p,max_chain_vertices=chain,
                               norm_contribution=endpoints(term)))
    assert prime_bound.hi<F(483,100)
    M=4096; T=2700
    ratio=T*L/(2*PI*(M+1))
    eta=(L*T+1)/(PI**3*M*(1-ratio**2)**2)
    assert ratio.hi<1 and eta.hi<F(8,125)
    pole=L*(sqrt_box(13)+1/sqrt_box(13)-2)/(PI**2*M)
    assert pole.hi<F(1,5000)
    # From psi recurrence with four steps and |Binet remainder| <= 1/(12 r^2).
    arch_threshold=log_box(F(T,2)/PI)-F(73,8)/F(T,2)**2-F(1,12)/F(17,4)**2
    assert arch_threshold.lo>6
    # a(0)>-6 uses gamma<1, pi<22/7, log2<.7, logpi<1.15.
    arch_floor=-F(1)-F(11,7)-F(21,10)-F(23,20)
    assert arch_floor>-6
    simple_bound=F(6)-12*F(8,125)-F(483,100)-F(1,5000)
    assert simple_bound>F(2,5)
    actual_enclosure=6-12*eta-prime_bound-pole
    assert actual_enclosure.lo>F(2,5)
    bM=b_coefficient(M); bnext=b_coefficient(M+1)
    cross=2*((M+1)*bM-M*bnext)/(M*M-(M+1)**2)
    assert cross.hi<-F(1,20)
    diagonal=odd_first_diagonal()
    assert diagonal.hi<F(1,1000)
    scalar_schur_diagonal_upper=F(1,1000)-F(1,20)**2/F(2,5)
    assert scalar_schur_diagonal_upper<0
    weight_sum=sum((log_box(p)/sqrt_box(n) for n,p in POWERS),Box(0))
    cosh=(sqrt_box(13)+1/sqrt_box(13))/2
    uniform_b=F(1,4)+(2*cosh-1)*L/(2*PI**2)+weight_sum/PI
    assert uniform_b.hi<2
    # A slightly weakened Hilbert--Schmidt remainder bound avoids square roots.
    # |b_n|<=2, r<K, rho=r/(K+1); sqrt(r/K) and sqrt(4q+1)^{-1} <= 1.
    rank_bounds=[]
    for r,K,orders in ((64,4096,(0,4,8,12,16,20)),(4096,8192,(32,64,96,128))):
        for q in orders:
            error=4/(1-F(r,K+1)**2)*F(r,K)**(2*q)*(1+F(r,K))
            rank_bounds.append(dict(retained_modes=r,far_tail_after=K,series_terms=q,
                                    rank_at_most=2*q,operator_error_upper_rational=str(error)))
            if (r,q) in ((64,20),(4096,128)):
                assert error<F(1,10**70)
    return dict(date='2026-09-26',
        model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
        status='rigorous rational enclosures for the stated analytic tail and scalar-test obstruction',
        whole_odd_gap_certified=False,zero_data_used=False,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        arithmetic='Fraction with outward rounding to multiples of 10^-40; no floating point',
        pi=endpoints(PI),log13=endpoints(L),prime_rows=prime_rows,
        prime_translation_norm_upper=endpoints(prime_bound),
        Fourier_cutoff=M,continuous_frequency_split=T,
        low_frequency_leakage_upper=endpoints(eta),
        odd_pole_tail_norm_upper=endpoints(pole),
        archimedean_symbol_at_split_lower=endpoints(arch_threshold),
        archimedean_global_floor_proved=str(arch_floor),
        rounded_tail_lower_bound=str(simple_bound),
        certified_unshifted_odd_tail_lower_bound='2/5',
        sharper_evaluated_tail_bound=endpoints(actual_enclosure),
        boundary_cross_entry=endpoints(cross),odd_first_diagonal=endpoints(diagonal),
        scalar_schur_test_at_zero_diagonal_upper=str(scalar_schur_diagonal_upper),
        uniform_divided_difference_coefficient_bound=endpoints(uniform_b),
        far_coupling_finite_rank_error_bounds=rank_bounds,
        claim='Q_M W_- Q_M >= (2/5) Q_M on the odd Fourier complement of modes 1..4096. The scalar norm Schur test using this tail bound fails at every 0 <= s < 2/5.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).parent/'records'/'odd_tail_certificate_20260926.json')
    args=parser.parse_args()
    result=certificate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Certified: unshifted odd Fourier tail above mode 4096 is >= 2/5.')
    print('Certified: the scalar norm Schur test with that bound fails for 0 <= s < 2/5.')
    print('The whole odd-sector gap remains uncertified.')


if __name__=='__main__':
    main()
