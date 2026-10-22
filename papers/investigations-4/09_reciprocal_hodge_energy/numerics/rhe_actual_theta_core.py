"""Arb physical-cell core for H_0(z)=xi(1/2+iz/2)/8 on |z-35|<=8.

Canonical identity and source/Cauchy majorant are mathematical inputs of the
calling note. A passed root ball represents an exact real zero; this module
checks finiteness and disk inclusion but does not manufacture that premise.
All returned cell values are outward balls on the stated physical subset;
no floating coefficient is used. Prepared for Edward Baker with substantial
LLM assistance, 2026-10-22, gpt-6.1-sol, effort ultra. Requires python-flint0.9.
"""
from time import perf_counter
from flint import acb, arb, acb_series, ctx


def canonical_h0(z):
    z=acb(z)
    s=acb(arb(1)/2)+acb(0,arb(1)/2)*z
    return s*(s-1)/16*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()


def synthetic_divided_difference(coeff, a):
    """Coefficients of (P(x)-P(a))/(x-a), ascending order."""
    q=[arb(0)]*(len(coeff)-1)
    q[-1]=coeff[-1]
    for k in range(len(q)-2,-1,-1):
        q[k]=coeff[k+1]+a*q[k+1]
    return q


def polynomial_value(coeff, x):
    x=acb(x)
    y=acb(coeff[-1])
    for c in coeff[-2::-1]:
        y=y*x+c
    return y


class ActualThetaCore:
    def __init__(self, bits=160, terms=65, center=35, radius=8,
                 cauchy_radius=16):
        self.bits=int(bits);ctx.prec=self.bits
        self.N=int(terms);self.C=arb(center);self.r=arb(radius)
        self.R=arb(cauchy_radius)
        if not (self.R>self.r and self.r>0 and self.N>=3):
            raise ValueError('invalid disk or Taylor order')
        self.counts=dict(H=0,P=0,Vcell=0)
        self.timings=dict(setup=0,H=0,P=0,Vcell=0)
        started=perf_counter();old_cap=ctx.cap;ctx.cap=self.N
        try:
            s=acb_series([acb(arb(1)/2,self.C/2),acb(0,arb(1)/2)])
            h=s*(s-1)/16*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
            if not all(h[k].is_finite() and h[k].imag.contains(0)
                       for k in range(self.N)):
                raise ArithmeticError('non-real or nonfinite Taylor coefficients')
            # H_0 has real Taylor coefficients at real C by conjugate symmetry.
            self.coeff=[h[k].real for k in range(self.N)]
        finally:
            ctx.cap=old_cap
        majorant=canonical_h0(acb(0,self.R))
        if not (majorant.is_finite() and majorant.imag.contains(0)
                and majorant.real>0):
            raise ArithmeticError('Cauchy source majorant not acquired')
        self.M=majorant.real.abs_upper()
        q=self.r/self.R;d=1-q;N=self.N
        self.tail0=self.M*q**N/d
        self.tail1=self.M/self.R*q**(N-1)*(N/d+q/d**2)
        self.tail2half=self.M/(2*self.R**2)*q**(N-2)*(
            N*(N-1)/d+2*N*q/d**2+2*q*q/d**3)
        self.Vcoeff=None;self.alpha=None;self.beta=None
        self.timings['setup']=perf_counter()-started

    def _record(self, key, started):
        self.counts[key]+=1;self.timings[key]+=perf_counter()-started

    def H(self,z):
        t=perf_counter();v=canonical_h0(z);self._record('H',t);return v

    def P_centered(self,x):
        t=perf_counter();v=polynomial_value(self.coeff,x);self._record('P',t);return v

    def set_roots(self,alpha,beta):
        """Pass disjoint, certified, real zero balls in physical z coordinates."""
        alpha=arb(alpha);beta=arb(beta)
        if not (alpha.is_finite() and beta.is_finite() and alpha<beta
                and abs(alpha-self.C)<self.r and abs(beta-self.C)<self.r):
            raise ValueError('root disks not finite, disjoint, interior and ordered')
        self.alpha=alpha;self.beta=beta
        self.Vcoeff=synthetic_divided_difference(
            synthetic_divided_difference(self.coeff,alpha-self.C),beta-self.C)
        self.Vd1=[(k+1)*self.Vcoeff[k+1] for k in range(len(self.Vcoeff)-1)]
        self.Vd2=[(k+1)*self.Vd1[k+1] for k in range(len(self.Vd1)-1)]
        self.range_radius=arb(9)
        self.Vthird=sum((k*(k-1)*(k-2)*abs(self.Vcoeff[k])*self.range_radius**(k-3)
                         for k in range(3,len(self.Vcoeff))),arb(0))
        return self

    def V_cell_centered(self,x):
        """Range oracle on input rectangle intersected with physical |x|<=8.

        The rectangle must be contained in |x|<=9. The polynomial is enclosed
        over the whole rectangle; the source remainder is added only for
        physical points |x|<=8. This oracle MUST NOT be used as an analytic
        acb.integral callback on arbitrary complex neighborhoods.
        """
        if self.Vcoeff is None:
            raise RuntimeError('certified exact root balls must be supplied first')
        t=perf_counter();x=acb(x)
        if not (x.is_finite() and x.abs_upper()<=self.range_radius):
            value=acb('nan')
        else:
            mid=acb(x.real.mid(),x.imag.mid());delta=x-mid
            p0=polynomial_value(self.Vcoeff,mid)
            p1=polynomial_value(self.Vd1,mid)
            p2=polynomial_value(self.Vd2,mid)
            value=p0+delta*(p1+delta*p2/2)
            err=(self.Vthird*delta.abs_upper()**3/6+self.tail2half).abs_upper()
            value=acb(value.real+arb(0,err),value.imag+arb(0,err))
        self._record('Vcell',t);return value

    def V_cell(self,z):
        return self.V_cell_centered(acb(z)-self.C)

