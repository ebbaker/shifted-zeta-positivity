#!/usr/bin/env python3
"""Exact arithmetic certificate for MIXED_CONDUCTOR_REFINEMENT_20261008.md.

GPT-6 (Codex), inherited configuration, 8 October 2026. The exact serving
variant and reasoning effort are not exposed. No arithmetic moment or
external source theorem is verified here. Uses only the Python standard
library. Intervals cover boxes, rather than sample their endpoints.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    @staticmethod
    def make(value):
        return value if isinstance(value, Interval) else Interval(F(value), F(value))

    def __add__(self, other):
        other = self.make(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -self.make(other)

    def __rsub__(self, other):
        return self.make(other) - self

    def __mul__(self, other):
        other = self.make(other)
        corners = [a*b for a, b in product((self.lo, self.hi), (other.lo, other.hi))]
        return Interval(min(corners), max(corners))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0, "division interval contains zero"
        return Interval(1/self.hi, 1/self.lo)

    def __truediv__(self, other):
        return self * self.make(other).reciprocal()

    def __rtruediv__(self, other):
        return self.make(other) / self


@dataclass(frozen=True)
class Jet:
    value: Interval
    deriv: tuple

    @staticmethod
    def make(value):
        if isinstance(value, Jet):
            return value
        return Jet(Interval.make(value), (Interval.make(0), Interval.make(0)))

    def __add__(self, other):
        other = self.make(other)
        return Jet(self.value+other.value, tuple(a+b for a,b in zip(self.deriv,other.deriv)))

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, tuple(-a for a in self.deriv))

    def __sub__(self, other):
        return self + -self.make(other)

    def __rsub__(self, other):
        return self.make(other)-self

    def __mul__(self, other):
        other = self.make(other)
        return Jet(self.value*other.value, tuple(
            a*other.value+self.value*b for a,b in zip(self.deriv,other.deriv)))

    __rmul__ = __mul__

    def reciprocal(self):
        inverse = self.value.reciprocal()
        return Jet(inverse, tuple(-a*inverse*inverse for a in self.deriv))

    def __truediv__(self, other):
        return self*self.make(other).reciprocal()

    def __rtruediv__(self, other):
        return self.make(other)/self


ETA, GAMMA, ELL = F(1,5000), F(1,6250), F(1,10**6)
D0, D1, X0, X1 = F(9,25), F(21,50), F(49,100), F(1,2)


def quantities(d, x):
    aa = F(5,6)-d
    b = 2-F(8,9)*x
    dd = 3-F(17,9)*x
    p = b*(1-x)
    j = aa*dd+d*p
    factor = aa*b/j
    row = 1-d+aa*d*p/(2*j)
    coarse_gap = F(9,8)-F(23,20)*d-row
    width = ETA/(d*(1-x))
    rn = 1-factor/2-(1-factor)*width
    mn = F(1,2)-aa/j*((1-x)/2-ETA/d)
    anchor = 2*(1+d*mn-ETA-GAMMA-row)
    tau_low = anchor-2*x/(1-x)*(ETA+ELL)-2*d*ELL+2*ELL
    tau_high = anchor+2*ETA+4*ELL+2*ELL/b
    return locals()


def rec(v):
    return {"exact": str(v), "decimal": float(v)}


def certify_monotonicity():
    # Automatic differentiation with exact rational interval arithmetic.
    # Closed cells cover the entire rectangle. Dependency overestimation
    # can make a check fail, but cannot certify a false derivative sign.
    derivative_lowers = {name: [None, None] for name in
                         ("anchor", "tau_low", "tau_high", "coarse_gap")}
    subdivisions = 32
    zero, one = Interval.make(0), Interval.make(1)
    for i,k in product(range(subdivisions), repeat=2):
        di = Interval(D0+(D1-D0)*F(i,subdivisions), D0+(D1-D0)*F(i+1,subdivisions))
        xi = Interval(X0+(X1-X0)*F(k,subdivisions), X0+(X1-X0)*F(k+1,subdivisions))
        vals = quantities(Jet(di,(one,zero)), Jet(xi,(zero,one)))
        for name in derivative_lowers:
            for axis in range(2):
                derivative = vals[name].deriv[axis]
                # coarse_gap decreases with d; its x derivative is positive.
                lower = -derivative.hi if name == "coarse_gap" and axis == 0 else derivative.lo
                assert lower > 0, (name, axis, i, k, lower)
                old = derivative_lowers[name][axis]
                derivative_lowers[name][axis] = lower if old is None else min(old,lower)
    # Publish small rational lower certificates, checked against the full
    # interval result. Exact large internal fractions need not be saved.
    coarse = {}
    for name, lower in derivative_lowers.items():
        coarse[name] = []
        for bound in lower:
            rational_floor = F((10000*bound).numerator//(10000*bound).denominator,10000)
            assert 0 < rational_floor <= bound
            coarse[name].append(str(rational_floor))
    return {"closed_cells": subdivisions**2,
            "method": "exact rational interval automatic differentiation",
            "derivative_lower_bounds_d_then_x": coarse,
            "coarse_gap_first_axis_sign": "negative; listed bound is for minus d derivative"}


def main():
    certificate = certify_monotonicity()
    gamma_op = GAMMA-3*ELL
    assert gamma_op > 0
    slope_max = D1*(1-X0)
    assert slope_max*F(39,14) < 1
    smax = ETA+2*ELL
    assert D0/1000-smax-gamma_op == ELL
    tau_min = quantities(D0,X0)["tau_low"]
    tau_max = quantities(D1,X1)["tau_high"]
    gap_min = quantities(D1,X0)["coarse_gap"]
    gap_max = quantities(D0,X1)["coarse_gap"]
    # The operational wedge stays strictly inside the source length box.
    r_low = F(47749,67660)-F(39,14)*ELL
    r_high = F(10261670,14086891)+(ETA+ELL)/F(9,50)
    m_low = F(3470383,8566666)-(ETA+ELL)/F(9,50)-ELL
    m_high = F(28646,69475)+F(25,14)*ELL
    assert r_low > F(7,10) and r_high < F(37,50)
    assert m_low > F(2,5) and m_high < F(1,2)
    assert 2*(D0*F(2,5)-smax-gamma_op) > F(7,25)
    # The tapered cutoff's exact dependence on wedge coordinates.
    for d,x in product((D0,D1),(X0,X1)):
        vals = quantities(d,x)
        for ar in (-ELL, F(0), vals["width"]):
            for bm in (F(0), ar+ELL):
                r,m = vals["rn"]+ar, vals["mn"]-bm
                sop = ETA-d*(1-x)*ar+ELL
                tau = 2*(1+d*m-sop-gamma_op-vals["row"]-ELL)
                assert tau == vals["anchor"]+2*d*((1-x)*ar-bm)+2*ELL
                vplain = 2*(d*m-sop-gamma_op)
                assert 1+vplain/2 == 1+d*m-sop-gamma_op

    fmax = F(1988,3383)
    rnmin = F(47749,67660)
    mass_gain_lower = ((1-fmax)*ETA-D1*F(1,10000)/2
                       -D1*F(1,10000)*(1-rnmin)-ELL)
    mu = F(1,25000)
    assert mass_gain_lower > mu
    assert 2*mu == F(1,12500)
    # A concrete point inside the ideal triangle and the new subregion.
    d,x,ar,bm = D0,X1,F(1,20000),F(1,40000)
    vals = quantities(d,x)
    r,m,z = vals["rn"]+ar,vals["mn"]-bm,(1-vals["rn"]-ar)/2
    sop = ETA-d*(1-x)*ar+ELL
    actual_gain = 1-vals["row"]-ELL-d*(r+z)
    assert actual_gain > mu
    assert sop > actual_gain  # the new sector is not a complete-moment proof
    tau = 2*(1+d*m-sop-gamma_op-vals["row"]-ELL)
    vp = 2*(d*m-sop-gamma_op)
    result = {
        "status": "conditional cutoff and sector bookkeeping; residual moment remains unproved",
        "model": "GPT-6 (Codex), inherited; exact serving variant and reasoning effort not exposed",
        "continuous_certificate": certificate,
        "operational_loss_budget": rec(ELL),
        "operational_gamma": rec(gamma_op),
        "low_row_reserve_lower": rec(ELL),
        "total_cutoff_exponent": {"infimum":rec(tau_min), "supremum":rec(tau_max)},
        "full_bin_count_improvement": {"minimum":rec(gap_min),"maximum":rec(gap_max)},
        "total_cutoff_gain_over_coarse_lower":rec(2*gap_min),
        "buffered_length_enclosure": {"r_lower":rec(r_low),"r_upper":rec(r_high),
                                      "m_lower":rec(m_low),"m_upper":rec(m_high)},
        "mass_gain_subregion_lower": rec(mass_gain_lower),
        "chosen_mass_gain": rec(mu),
        "additional_plain_cutoff_exponent": rec(2*mu),
        "example": {"d":rec(d),"x":rec(x),"a_r":rec(ar),"b_m":rec(bm),
                    "s_op":rec(sop),"positive_inverse_mass_gain":rec(actual_gain),
                    "total_cutoff_exponent":rec(tau),"plain_cutoff_exponent":rec(vp),
                    "improved_plain_cutoff_exponent":rec(vp+2*mu)},
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
