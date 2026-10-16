#!/usr/bin/env python3
"""Exact Arb exponential integrals of an even cubic-spline correlation.

Prepared for Edward Baker with GPT-6 (Codex), 29 September 2026.
Serving variant and configured effort not exposed. The helper introduces
no quadrature or series truncation error. Caller must separately bound
replacement of the exact source correlation by this spline correlation.

For positive-index coefficients a[m] (a[-m]=a[m]), represent
    kappa(t) = h/scale**2 * sum_m a[m] beta3(t/h-m),
where beta3 is the centered cubic cardinal B-spline.
TruncatedCorrelation(a,h,N,scale).evaluate(lam) returns
    (integral_0^infinity kappa(t) exp(lam*t) dt,
     integral_0^(N*h) kappa(t) exp(lam*t) dt).
Coefficients may be exact integers or Arb balls, including a transported
correlation built by exact integer shifts. All polynomials are built once.
"""
from flint import arb, arb_poly


def _require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def _poly_at(coefficients, x):
    result = x*0
    for c in reversed(coefficients):
        result = result*x+c
    return result


def _poly_exponential(coefficients, lo, hi, q):
    """Integral_lo^hi p(v)exp(qv)dv by an exact cubic antiderivative."""
    if q == 0:
        return sum(c*(hi**(j+1)-lo**(j+1))/(j+1)
                   for j,c in enumerate(coefficients))
    _require(not q.contains(0), 'Nonzero exponent enclosure contains zero')
    derivative = list(coefficients)
    primitive = [arb(0)]*len(coefficients)
    factor = 1/q
    while derivative:
        for j,c in enumerate(derivative):
            primitive[j] += factor*c
        derivative = [(j+1)*derivative[j+1] for j in range(len(derivative)-1)]
        factor /= -q
    return (q*hi).exp()*_poly_at(primitive,hi)-(q*lo).exp()*_poly_at(primitive,lo)


def _boundary_integrals(q):
    """H(q)=int_0^2 beta3(v)e^(qv)dv; T(q)=int_1^2 ... ."""
    if q == 0:
        return arb(1)/2, arb(1)/24
    # beta3(v)=2/3-v²+v³/2 on [0,1], and (2-v)³/6 on [1,2].
    inner = [arb(2)/3, arb(0), arb(-1), arb(1)/2]
    outer = [arb(4)/3, arb(-2), arb(1), -arb(1)/6]
    tail = _poly_exponential(outer,arb(1),arb(2),q)
    return _poly_exponential(inner,arb(0),arb(1),q)+tail,tail


class TruncatedCorrelation:
    def __init__(self, positive_coefficients, h, N, scale):
        _require(N >= 4, 'N must be at least 4')
        _require(scale > 0, 'Scale must be positive')
        _require(len(positive_coefficients)>0, 'Empty coefficient list')
        self.h = arb(h)
        _require(self.h > 0, 'Spacing must be positive')
        self.N = N
        self.prefactor = self.h*self.h/(scale*scale)
        self.full = arb_poly(positive_coefficients)
        self.prefix = arb_poly(positive_coefficients[:N+1])
        def a(j):
            return arb(positive_coefficients[j]) if j<len(positive_coefficients) else arb(0)
        self.a0,self.a1 = a(0),a(1)
        self.aNm1,self.aN,self.aNp1 = a(N-1),a(N),a(N+1)

    def evaluate(self, lam):
        q = arb(lam)*self.h
        H,T = _boundary_integrals(q)
        Hminus,Tminus = _boundary_integrals(-q)
        z = q.exp()
        K4 = arb(1) if q == 0 else ((q/2).sinh()/(q/2))**4
        # Lower endpoint: add the piece from center -1, and remove pieces
        # below zero from centers 0 and 1. Coefficients are even.
        lower = -self.a0*Hminus+self.a1*((-q).exp()*T-z*Tminus)
        full_half = K4*self.full(z)+lower
        # Upper endpoint: remove outgoing pieces of centers N-1,N and
        # add the entering piece from N+1.
        upper = -(self.aNm1*(q*(self.N-1)).exp()*T
                  +self.aN*(q*self.N).exp()*H)
        upper += self.aNp1*(q*(self.N+1)).exp()*Tminus
        before_a = K4*self.prefix(z)+lower+upper
        full_half *= self.prefactor
        before_a *= self.prefactor
        _require(full_half.is_finite() and before_a.is_finite(), 'Nonfinite spline integral')
        return full_half,before_a

    def before(self, lam):
        return self.evaluate(lam)[1]
