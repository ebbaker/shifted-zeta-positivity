#!/usr/bin/env python3
"""Exact conditional jet algebra and outward theta-score shell bounds.

Imports the existing source-bound 15_lee_yang moment enclosure, then uses
fresh Decimal intervals for theta values/derivatives. No zero exclusion.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = self.lo if hi is None else D(hi)
    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I((self.lo+other.lo).next_minus(),
                 (self.hi+other.hi).next_plus())
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))
    def __rsub__(self, other):
        return I(other) + -self
    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = [a*b for a in (self.lo, self.hi)
                for b in (other.lo, other.hi)]
        return I(min(vals).next_minus(), max(vals).next_plus())
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert not other.lo <= 0 <= other.hi
        return self * I((1/other.hi).next_minus(),
                        (1/other.lo).next_plus())
    def power(self, n):
        out = I(1)
        for _ in range(n):
            out = out*self
        return out
    def exp(self):
        return I(self.lo.exp().next_minus(), self.hi.exp().next_plus())
    def data(self):
        return [str(self.lo), str(self.hi)]


def atan_bounds(q, terms=70):
    value = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), F(0))
    nxt = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(value, value+nxt), max(value, value+nxt)


def pi_interval():
    l5, h5 = atan_bounds(5)
    l239, h239 = atan_bounds(239)
    lo, hi = 16*l5-4*h239, 16*h5-4*l239
    return I((D(lo.numerator)/D(lo.denominator)).next_minus(),
             (D(hi.numerator)/D(hi.denominator)).next_plus())


def theta_phi_and_slope(u, pi):
    e4, e5, e9, e13 = [(u*k).exp() for k in (4, 5, 9, 13)]
    phi, slope = I(0), I(0)
    for n in (1, 2, 3):
        c = pi*n*n
        env = (-(c*e4)).exp()
        phi += (2*c.power(2)*e9-3*c*e5)*env
        slope += (30*c.power(2)*e9-15*c*e5
                  -8*c.power(3)*e13)*env
    # n^m <=4^m(5/4)^(m(n-4)), n^2>=16+9(n-4), n>=4.
    def omitted(m):
        ratio = I(5).power(m)/I(4).power(m)
        return (I(4).power(m)*(-(16*pi*e4)).exp()
                /(I(1)-ratio*(-(9*pi*e4)).exp()))
    tail_phi = 2*pi.power(2)*e9*omitted(4)+3*pi*e5*omitted(2)
    tail_slope = (30*pi.power(2)*e9*omitted(4)
                  +15*pi*e5*omitted(2)+8*pi.power(3)*e13*omitted(6))
    phi += I(0, tail_phi.hi)  # every omitted theta summand is positive
    slope += I(-tail_slope.hi, tail_slope.hi)
    return phi, slope


# Sparse exact polynomial ring for x,beta,C2,C3,C4.
class P:
    size = 5
    def __init__(self, data=0):
        if isinstance(data, P):
            self.a = dict(data.a)
        elif isinstance(data, dict):
            self.a = {k:F(v) for k,v in data.items() if v}
        else:
            self.a = {} if not data else {(0,)*self.size:F(data)}
    @classmethod
    def var(cls, i):
        key = [0]*cls.size
        key[i] = 1
        return cls({tuple(key):1})
    def __add__(self, other):
        out = dict(self.a)
        for k,v in P(other).a.items():
            out[k] = out.get(k,F(0))+v
        return P(out)
    __radd__ = __add__
    def __neg__(self):
        return P({k:-v for k,v in self.a.items()})
    def __sub__(self, other):
        return self+-P(other)
    def __mul__(self, other):
        out = {}
        for k,v in self.a.items():
            for l,w in P(other).a.items():
                key = tuple(a+b for a,b in zip(k,l))
                out[key] = out.get(key,F(0))+v*w
        return P(out)
    __rmul__ = __mul__
    def __pow__(self, n):
        out = P(1)
        for _ in range(n):
            out = out*self
        return out
    def __eq__(self, other):
        return self.a == P(other).a


x,beta,c2,c3,c4 = [P.var(j) for j in range(5)]
r1, r2, r3 = beta*c2, x*c2+beta*c3, 3*c2+x*c3+beta*c4
# Multiply by x^2 to keep the exact check polynomial.
original = beta**4*(2*x*x*c3*c3-3*x*x*c2*c4-9*c2*c2)
residual = (2*beta*beta*x*x*r2*r2-beta*x**3*r1*r2
            -3*beta*beta*x*x*r1*r3
            +(9*beta*x*x-x**4-9*beta*beta)*r1*r1)
assert original == residual
assert beta*beta*c3 == beta*r2-x*r1
assert beta**3*c4 == beta*beta*r3-3*beta*r1-beta*x*r2+x*x*r1


source = Path(__file__).resolve()
base = source.parents[2]
moment_record = base/'15_lee_yang/numerics/theta_spin_screen_record_20261010.json'
moment_source = moment_record.with_name('screen_theta_spins.py')
if not moment_record.exists():
    raise SystemExit("Missing moment record: run 15_lee_yang/numerics/screen_theta_spins.py --enclose.")
inputs = json.loads(moment_record.read_text())
assert inputs['source_sha256'] == hashlib.sha256(moment_source.read_bytes()).hexdigest()
enclosure = inputs['enclosure']

with localcontext() as ctx:
    ctx.prec = 42
    ctx.Emin = -999999
    pi = pi_interval()
    mu2 = I(*enclosure['mu2'])
    mu4 = I(*enclosure['mu4'])
    tmax = I('0.05')
    # Z_0>.002 below, so weighted omitted u>2 fourth moment / Z_0
    # is <5e-37. Var(u^2)<=mu4 bounds the growth of mu2.
    mu2_upper = (mu2 + tmax*((I('0.2')).exp()*mu4+I('5e-37'))).hi
    beta_range = I((I(1)/I(mu2_upper)).lo, (I(1)/I(mu2.lo)).hi)
    time = I(0,'0.05')
    small_phi,_ = theta_phi_and_slope(I(0,'0.01'), pi)
    assert small_phi.lo*D('0.01') > D('0.002')
    shells = {}
    for name, lo, hi in [('negative','0.1','0.1001'),
                         ('positive','0.3','0.301')]:
        u = I(lo,hi)
        phi,slope = theta_phi_and_slope(u,pi)
        score = -slope/phi
        residual = score-2*time*u-beta_range*u
        shells[name] = {'u':[lo,hi], 'phi':phi.data(),
                        'score_at_time_zero':score.data(),
                        'residual_full_time_range':residual.data()}
    assert D('86.39010') < beta_range.lo <= beta_range.hi < D('86.56254')
    assert D(shells['negative']['residual_full_time_range'][1]) < D('-0.72')
    assert D(shells['positive']['residual_full_time_range'][0]) > D('4.18')
    assert D(shells['positive']['phi'][0]) > D('0.0071135')
    # Z_t<1 and the symmetric pair of positive shells imply this bulk
    # score-defect lower bound; the time reweight is >=1.
    rl = D(shells['positive']['residual_full_time_range'][0])
    pl = D(shells['positive']['phi'][0])
    bulk_lower = (I(rl).power(2)*I(pl)*I('0.001')).lo
    assert bulk_lower > D('0.00012')
    # Elementary constants used for the Gaussian kernel tail budgets.
    assert sum((F(3)**k/F(math_k) for k,math_k in
                enumerate((1,1,2,6,24,120,720,5040,40320))),F(0)) > 20
    record = {
        'date':'2026-10-10',
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'input_moment_record_sha256':hashlib.sha256(moment_record.read_bytes()).hexdigest(),
        'input_moment_source_sha256':inputs['source_sha256'],
        'precision':ctx.prec,
        'time_interval':['0','0.05'],
        'beta_full_time_interval':beta_range.data(),
        'shells':shells,
        'optimized_fisher_defect_strict_lower_bound':str(bulk_lower),
        'exact_conditional_polynomial_assertions':3,
        'scope':'Actual theta score sign change and bulk defect; no candidate sign, collision exclusion, or independent review.',
    }
target = source.with_name('conditional_score_record_20261010.json')
target.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({'record':target.name,'beta':record['beta_full_time_interval'],
                  'bulk_defect_lower':record['optimized_fisher_defect_strict_lower_bound'],
                  'exact_checks':3},sort_keys=True))
