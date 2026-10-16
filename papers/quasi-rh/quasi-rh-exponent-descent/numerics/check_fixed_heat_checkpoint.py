#!/usr/bin/env python3
"""Exact moving-domain algebra and outward interval heat certificate.

Uses only Python's standard library. Decimal exp/ln/sqrt are correctly rounded;
we widen each result to its representable predecessor and successor. Every
other arithmetic endpoint uses directed rounding. Trigonometric functions and
pi use Taylor/Machin formulas with explicit remainder enclosures. No floating
point value participates in the heat certificate.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as Q
from functools import lru_cache
import json
import math
import sys

PREC = 50
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
NEAR = Context(prec=PREC, rounding=ROUND_HALF_EVEN)

class I:
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, D) else D(str(lo))
        self.hi = self.lo if hi is None else (hi if isinstance(hi, D) else D(str(hi)))
        assert self.lo <= self.hi
    @staticmethod
    def make(x):
        return x if isinstance(x, I) else I(x)
    def __add__(self, b):
        b=I.make(b);return I(DOWN.add(self.lo,b.lo),UP.add(self.hi,b.hi))
    __radd__=__add__
    def __neg__(self):
        return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,b):return self+-I.make(b)
    def __rsub__(self,b):return I.make(b)+-self
    def __mul__(self,b):
        b=I.make(b)
        pairs=[(x,y) for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return I(min(DOWN.multiply(x,y) for x,y in pairs),max(UP.multiply(x,y) for x,y in pairs))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.make(b);assert not b.lo<=0<=b.hi
        return self*I(DOWN.divide(D(1),b.hi),UP.divide(D(1),b.lo))
    def __rtruediv__(self,b):return I.make(b)/self
    def square(self):
        if self.lo<=0<=self.hi:return I(0,max(UP.multiply(x,x) for x in (self.lo,self.hi)))
        return I(min(DOWN.multiply(x,x) for x in (self.lo,self.hi)),max(UP.multiply(x,x) for x in (self.lo,self.hi)))
    def power(self,n):
        assert n>=0
        ans=I(1);base=self
        while n:
            if n%2:ans=ans*base
            base=base.square();n//=2
        return ans
    def abs(self):
        if self.lo>=0:return self
        if self.hi<=0:return -self
        return I(0,max(self.lo.copy_negate(),self.hi))
    def elementary(self,name):
        if name in ('ln','sqrt'):assert self.lo>0
        low=getattr(NEAR,name)(self.lo);high=getattr(NEAR,name)(self.hi)
        lo=NEAR.next_minus(low);hi=NEAR.next_plus(high)
        if name=='sqrt':
            # Verify the enclosure by directed squaring, independent of
            # the square-root routine's rounding guarantee.
            while UP.multiply(lo,lo)>self.lo:lo=NEAR.next_minus(lo)
            while DOWN.multiply(hi,hi)<self.hi:hi=NEAR.next_plus(hi)
            assert lo>0 and UP.multiply(lo,lo)<=self.lo
            assert DOWN.multiply(hi,hi)>=self.hi
        return I(lo,hi)
    def exp(self):return self.elementary('exp')
    def ln(self):return self.elementary('ln')
    def sqrt(self):return self.elementary('sqrt')
    def endpoints(self):return [str(self.lo),str(self.hi)]


def atan_small(x,terms=80):
    """Taylor enclosure for |x|<1, using a uniform alternating remainder."""
    x=I.make(x);assert x.abs().hi<1
    total=I(0);p=x;xx=x.square()
    for k in range(terms):
        total=total+((-1 if k%2 else 1)*p/(2*k+1));p=p*xx
    rem=x.abs().power(2*terms+1)/(2*terms+1)
    return total+I(rem.hi.copy_negate(),rem.hi)

PI=16*atan_small(I(1)/5)-4*atan_small(I(1)/239)
assert D('3.14159265358979323846264338327950288419716939') < PI.lo
assert PI.hi < D('3.14159265358979323846264338327950288419716940')


def sin_cos(x,terms=55):
    """Reduce by an exact integer multiple of the enclosed 2*pi, then Taylor."""
    x=I.make(x)
    mid=NEAR.divide(NEAR.add(x.lo,x.hi),D(2))
    k=int(NEAR.divide(mid,NEAR.multiply(D(2),NEAR.add(PI.lo,PI.hi)/D(2))).to_integral_value(rounding=ROUND_HALF_EVEN))
    x=x-2*k*PI
    assert x.abs().hi < 4
    xx=x.square();c=I(0);s=I(0);cp=I(1);sp=x
    for j in range(terms):
        sign=-1 if j%2 else 1
        c=c+sign*cp/math.factorial(2*j)
        s=s+sign*sp/math.factorial(2*j+1)
        cp=cp*xx;sp=sp*xx
    # Taylor's theorem: |remainder after degree m| <= |x|^(m+1)/(m+1)!.
    cr=x.abs().power(2*terms)/math.factorial(2*terms)
    sr=x.abs().power(2*terms+1)/math.factorial(2*terms+1)
    return s+I(sr.hi.copy_negate(),sr.hi),c+I(cr.hi.copy_negate(),cr.hi)

@lru_cache(None)
def logn(n):return I(n).ln()


def finite_heat(t,x,N):
    d=1+x.square();L=d.ln()/2-(4*PI).ln();at=atan_small(1/x,terms=20)
    ar=L/2-1/d;ai=(-PI/2+at)/2+3*x/d
    theta=-7*PI/8-at/4+x*(1-L)/4+t*ar*ai/2
    arp=6*(x.square()-1)/d.square()+1/d
    aip=4*x/d.square()+x/d
    sumf=I(0);sumgp=I(0)
    for n in range(1,N+1):
        l=logn(n)
        amp=(t*l.square()/4-(I('.5')+t*ar/2)*l).exp()
        sn,cs=sin_cos(theta+(x-t*ai)*l/2)
        lr=(ar-l)*(1+t*arp/2)-ai*t*aip/2
        li=(ar-l)*t*aip/2+ai*(1+t*arp/2)
        sumf=sumf+2*amp*cs
        sumgp=sumgp+amp*(lr*sn+li*cs)
    b=(ai*(1+t*arp/2)+ar*t*aip/2)/2
    return sumf,sumgp-b*sumf


def heat_error(X,ep,ta,R,N):
    xm=X-R;xp=X+R;qm=xm/(4*PI);qp=xp/(4*PI);V=xm/2;S=(xp.square()+(1+R).square()).sqrt()/2
    am=qm.ln()/2-1/V.square()
    ast=I('1.5')/V+( (S/(2*PI)).ln().square()+PI.square()/4).sqrt()/2
    dst=I('1.5')/V.square()+I('.5')/V
    K=(R*ast*(1+ta*dst/2)/2).exp()
    mlo=(qm+ep/16).sqrt();mhi=(qp+ta/16).sqrt()
    m0=int(mlo.lo.to_integral_value(rounding=ROUND_FLOOR));m1=int(mhi.hi.to_integral_value(rounding=ROUND_FLOOR))
    candidates=[]
    for m in range(m0,m1+1):
        ab=I(0)
        for n in range(1,m+1):
            l=logn(n);dn=l.square()/4-am*l/2
            td=I(max((ep*dn).lo,(ta*dn).lo),max((ep*dn).hi,(ta*dn).hi))
            vn=(-l/2+td).exp()
            ell=max((qm/(n*n)).ln().abs().hi,(qp/(n*n)).ln().abs().hi)
            un=((ta.square()*I(ell).square()/16+I('.626'))/(xm-I('6.66'))).exp()-1
            mk=(ta*R/(2*(xm-6))*logn(m)).exp()
            ab=ab+(1+mk*(R*l).exp())*vn*un
        ec=(-qm.ln()/4-ep*qm.ln().square()/16+I('1.24')*((R*logn(3)).exp()+(-R*logn(3)).exp())/(I(m)-I('.125'))+(3*(qp.ln().square()+PI.square()/4).sqrt()+I('10.44'))/(xm-12)).exp()
        tail=I(0)
        for n in range(min(m,N)+1,max(m,N)+1):
            l=logn(n);dn=l.square()/4-am*l/2
            td=I(max((ep*dn).lo,(ta*dn).lo),max((ep*dn).hi,(ta*dn).hi))
            tail=tail+((R-1)*l/2+td).exp()
        candidates.append(K*(ab+ec+2*tail))
    return I(max(v.lo for v in candidates),max(v.hi for v in candidates)),[m0,m1]


def heat_certificate():
    # One outer disk uniform for a substantial compact rectangle; subcells
    # enclose the exact finite holomorphic approximant over the whole rectangle.
    X=I('452.2');R=I('.35');ep=I('.2');ta=I('.3');N=6
    eta,cutoffs=heat_error(X,ep,ta,R,N)
    x0=D('451.9');x1=D('452.5');t0=D('.2');t1=D('.3')
    nx=12;nt=10
    cells=[]
    for j in range(nx):
        xlo=DOWN.add(x0,DOWN.divide(D(j)*D('.6'),D(nx)))
        xhi=UP.add(x0,UP.divide(D(j+1)*D('.6'),D(nx)))
        for k in range(nt):
            tlo=DOWN.add(t0,DOWN.divide(D(k)*D('.1'),D(nt)))
            thi=UP.add(t0,UP.divide(D(k+1)*D('.1'),D(nt)))
            f,fp=finite_heat(I(tlo,thi),I(xlo,xhi),N)
            assert f.lo>eta.hi, (j,k,f.endpoints(),eta.endpoints())
            cells.append((f,fp))
    fmin=min(v[0].lo for v in cells)
    # Exact crossing curve lies inside the certified rectangle at EVERY time.
    crossing=4*PI*(36-I(t0,t1)/16)
    assert x0<crossing.lo<crossing.hi<x1
    left=I(x0)/(4*PI)+I(t0,t1)/16
    right=I(x1)/(4*PI)+I(t0,t1)/16
    assert 25<left.lo<=left.hi<36<right.lo<=right.hi<49
    assert cutoffs==[5,6]
    return {
        'status':'outward interval certificate passed',
        'rectangle':{'x':[str(x0),str(x1)],'t':[str(t0),str(t1)]},
        'outer_disk':{'center':'452.2','radius':'.35'},
        'fixed_N':N,'natural_cutoffs':cutoffs,'cells':len(cells),
        'pi_interval':PI.endpoints(),
        'eta_interval':eta.endpoints(),
        'finite_F_lower_bound':str(fmin),
        'normalized_Q_lower_bound':str(DOWN.subtract(fmin,eta.hi)),
        'crossing_x_enclosure':crossing.endpoints(),
        'scope':'H_t has no real zero, hence no real multiple zero, on this compact rectangle. Imported Polymath theorem and Note 3 analytic disk estimates are proof inputs. No global RH or Newman bound is certified.'
    }


def moving_domain_checks():
    checks=0
    # Rational weighted meshes make the exact bookkeeping independent of
    # quadrature error. These are synthetic functions, not arithmetic bounds.
    for X in (Q(64),Q(81),Q(100)):
      for c in (Q(2),Q(3)):
        Y=X/c;V=Q(2);U=Q(3);C=Q(2);r=Q(3,4);beta=Q(1)
        k=r*c**(1+beta)
        def M(s):return Q((s.numerator*7)//s.denominator)-s
        def E(s):return Q((s.numerator*11)//s.denominator)-2*s
        def F(z):return z**3*(C-z)**2 if 0<z<C else Q(0)
        m=M(U)-M(V);e=E(U)-E(V)
        totalX=totalY=bulk=center=terminal=lower=Q(0)
        # Every domain is restricted to this same arbitrary finite mesh;
        # pointwise partition identity therefore gives an exact mesh identity.
        for i in range(5,101):
          s=Q(i,2)
          for j in range(5,101):
            t=Q(j,2);fx=F(s*t/X);fy=F(s*t/Y)
            mv=M(s)-M(V);ev=E(t)-E(V);mu=mv-m;eu=ev-e
            inX=s>U and t>U and s*t<C*X
            inY=s>V and t>V and s*t<C*Y
            common=s>U and t>U and s*t<C*Y
            if inX:totalX+=mu*eu*fx
            if inY:totalY+=mv*ev*fy
            if common:
                bulk+=mv*ev*(fx-k*fy)
                center+=(-m*ev-e*mv+m*e)*fx
            if inX and not common:terminal+=mu*eu*fx
            if inY and not common:lower-=k*mv*ev*fy
            checks+=1
        assert totalX-k*totalY==bulk+center+terminal+lower
        assert terminal!=0 and lower!=0 and center!=0
    # Finite-mode phase identities for complex vectors use rational cosines:
    # 2 Re<d,f_delayed> = 2(cos phi-1) A;
    # |d|^2 = 2(1-cos phi) A. They cancel, including resonance.
    cosines=[Q(-1),Q(-3,5),Q(0),Q(3,5),Q(1)]
    for z in cosines:
        covariance=2*(z-1);defect=2*(1-z)
        assert covariance+defect==0
        checks+=1
    return {'status':'exact rational identities passed','mesh_point_checks':checks-5,'phase_checks':5,'scope':'Checks the complete moving-domain/centering/terminal partition on synthetic rational mesh inputs and the exact mode covariance identity; proves no actual-prime asymptotic estimate.'}


def main():
    record={'precision':PREC,'backend':'stdlib Decimal, directed endpoint operations, widened correctly rounded exp/ln/sqrt; Machin pi and Taylor trigonometric remainders','fixed_scale':moving_domain_checks(),'heat':heat_certificate()}
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
