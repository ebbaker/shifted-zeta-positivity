#!/usr/bin/env python3
"""Outward center-jet certificates and exact sine-jet algebra, stdlib only.

Decimal primitive arithmetic is widened one ulp in both directions.
Transcendentals use rational Machin bounds and positive Taylor/geometric
enclosures, not floating-point samples. The source note supplies the
analytic implications and the infinite theta-tail bound.
"""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = self.lo if hi is None else D(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I((self.lo + other.lo).next_minus(),
                 (self.hi + other.hi).next_plus())

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = [x * y for x in (self.lo, self.hi)
                for y in (other.lo, other.hi)]
        return I(min(vals).next_minus(), max(vals).next_plus())

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert not other.lo <= 0 <= other.hi
        return self * I((D(1) / other.hi).next_minus(),
                        (D(1) / other.lo).next_plus())

    def power(self, n):
        assert isinstance(n, int) and n >= 0
        ans = I(1)
        for _ in range(n):
            ans = ans * self
        return ans

    def data(self):
        return [str(self.lo), str(self.hi)]


def atan_bounds(q, terms=90):
    total = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), F(0))
    next_term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(total, total+next_term), max(total, total+next_term)


def rational_interval(lo, hi):
    return I((D(lo.numerator)/D(lo.denominator)).next_minus(),
             (D(hi.numerator)/D(hi.denominator)).next_plus())


def exp_positive(x, terms=300):
    """Enclose exp(x), x>=0, by Taylor and its geometric tail."""
    assert x.lo >= 0 and x.hi < terms+2
    term, total = I(1), I(1)
    for k in range(1, terms+1):
        term = term * x / k
        total = total + term
    next_term = term * x / (terms+1)
    tail = next_term / (I(1) - x / (terms+2))
    return I(total.lo, (total + I(0, tail.hi)).hi)


def exp_negative(x):
    return I(1) / exp_positive(x)


def next_poly(p):
    # P -> P+4a(P'-P), for d/dr exp(r-a)P(a), a'=4a.
    out = [0] * (len(p)+1)
    for k, coefficient in enumerate(p):
        out[k] += (1+4*k)*coefficient
        out[k+1] -= 4*coefficient
    return out


def eval_poly(p, a):
    ans = I(0)
    for c in reversed(p):
        ans = ans * a + c
    return ans


def poly_add(p, q):
    out = p.copy()
    for term, coefficient in q.items():
        out[term] = out.get(term, F(0)) + coefficient
        if not out[term]:
            del out[term]
    return out


def poly_scale(p, coefficient):
    return {k: v*coefficient for k, v in p.items() if v*coefficient}


def poly_mul(p, q):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            term = tuple(x+y for x, y in zip(a, b))
            out[term] = out.get(term, F(0)) + ca*cb
    return {k: v for k, v in out.items() if v}


def check_sine_dictionary():
    # Variables are S_m, S_{m+1}, S_{m+2}, z=1/x.
    sm = {(1, 0, 0, 0): F(1)}
    sn = {(0, 1, 0, 0): F(1)}
    so = {(0, 0, 1, 0): F(1)}
    z = {(0, 0, 0, 1): F(1)}
    z2 = poly_mul(z, z)
    for m in range(2, 7):
        hm = sm
        hn = poly_add(sn, poly_scale(poly_mul(z, sm), -(m+1)))
        ho = poly_add(so, poly_scale(poly_mul(z, sn), -(m+2)))
        ho = poly_add(ho, poly_scale(poly_mul(z2, sm), (m+1)*(m+2)))
        lhs = poly_scale(poly_mul(hn, hn), F(1, (m+1)**2))
        lhs = poly_add(lhs, poly_scale(poly_mul(hm, ho), -F(2, (m+1)*(m+2))))
        lhs = poly_add(lhs, poly_scale(poly_mul(z2, poly_mul(hm, hm)), -F(m, 4)))
        rhs = poly_scale(poly_mul(sn, sn), F(1, (m+1)**2))
        rhs = poly_add(rhs, poly_scale(poly_mul(sm, so), -F(2, (m+1)*(m+2))))
        rhs = poly_add(rhs, poly_scale(poly_mul(z2, poly_mul(sm, sm)), -F(m+4, 4)))
        assert lhs == rhs
        if m == 2:
            ordinary = poly_scale(lhs, 18)
            expected = poly_add(poly_scale(poly_mul(sn, sn), 2),
                                poly_scale(poly_mul(sm, so), -3))
            expected = poly_add(expected, poly_scale(poly_mul(z2, poly_mul(sm, sm)), -27))
            assert ordinary == expected
    return "PASS: symbolic polynomial identities for multiplicities 2 through 6"


def main():
    with localcontext() as ctx:
        ctx.prec = 60
        lo5, hi5 = atan_bounds(5)
        lo239, hi239 = atan_bounds(239)
        pi = rational_interval(16*lo5-4*hi239, 16*hi5-4*lo239)
        polys = [[0, -3, 2]]
        for _ in range(10):
            polys.append(next_poly(polys[-1]))
        assert polys[1] == [0, -15, 30, -8]
        assert polys[2] == [0, -75, 330, -224, 32]
        jets, tails = {}, {}
        for j in range(0, 11, 2):
            total = I(0)
            for n in range(1, 6):
                a = pi * (n*n)
                total = total + exp_negative(a) * eval_poly(polys[j], a)
            degree = j+2
            coefficient = sum(abs(c) for c in polys[j])
            ratio = (I(7)/6).power(2*degree) * exp_negative(pi*13)
            assert ratio.hi < 1
            tail = (pi.power(degree) * (coefficient*6**(2*degree))
                    * exp_negative(pi*36) / (I(1)-ratio))
            jets[j] = total + I(-tail.hi, tail.hi)
            tails[j] = tail.hi
        determinant = jets[0]*jets[4]/12 - jets[2].power(2)/4
        assert D('-38.050') < determinant.lo < determinant.hi < D('-38.048')
        t = I(0, '0.05')
        heat10 = jets[10] + jets[8]*90*t + jets[6]*2520*t.power(2)
        heat10 = heat10 + jets[4]*25200*t.power(3)
        heat10 = heat10 + jets[2]*75600*t.power(4) + jets[0]*30240*t.power(5)
        assert D('3.3580e11') < heat10.lo <= heat10.hi < D('3.3688e11')
        denominator = (pi*2).power(5) * 945  # 9!!
        inverse11 = -heat10/denominator
        assert D('-36403') < inverse11.lo <= inverse11.hi < D('-36287')
        record = {
            "status": "PASS",
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Outward Decimal arithmetic with rational Machin and Taylor/geometric bounds; exact polynomial identities. No collision exclusion.",
            "decimal_precision": ctx.prec,
            "pi": pi.data(),
            "center_even_theta_jets": {str(k): v.data() for k, v in jets.items()},
            "absolute_infinite_theta_tail_bounds_n_ge_6": {str(k): str(v) for k, v in tails.items()},
            "squared_radius_log_convexity_determinant": determinant.data(),
            "heat_tenth_center_jet_t_0_to_0.05": heat10.data(),
            "eleven_dimensional_radial_inverse_center_t_0_to_0.05": inverse11.data(),
            "sine_jet_algebra": check_sine_dictionary(),
        }
        print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
