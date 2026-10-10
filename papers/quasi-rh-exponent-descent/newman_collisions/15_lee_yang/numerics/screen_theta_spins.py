"""Theta moments and a ten-spin ferromagnetic screening experiment.

Standard-library Simpson quadrature is exploratory. With --enclose, a
separate outward Decimal midpoint enclosure bounds moments 0,2,4.
That enclosure proves only the identical independent-spin mismatch.
"""
import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


def phi(u):
    return math.fsum((2 * math.pi ** 2 * n ** 4 * math.exp(9 * u) - 3 * math.pi * n * n * math.exp(5 * u)) * math.exp(-math.pi * n * n * math.exp(4 * u)) for n in range(1, 9))


def moments(cells):
    h = 3 / cells
    samples = [(j * h, phi(j * h), 1 if j in (0, cells) else 4 if j % 2 else 2) for j in range(cells + 1)]
    raw = [h / 3 * math.fsum(w * u ** (2 * k) * f for u, f, w in samples) for k in range(5)]
    return [v / raw[0] for v in raw]


def spin_moments(coupling):
    weights = [math.comb(10, k) * math.exp(coupling * (2 * k - 10) ** 2 / 2) for k in range(11)]
    total = math.fsum(weights)
    return [math.fsum(weights[k] * (2 * k - 10) ** r for k in range(11)) / total for r in (2, 4, 6)]


class I:
    def __init__(self, lo, hi=None):
        self.lo = D(lo)
        self.hi = self.lo if hi is None else D(hi)

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I((self.lo + other.lo).next_minus(), (self.hi + other.hi).next_plus())

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = [x * y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(vals).next_minus(), max(vals).next_plus())

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert not other.lo <= 0 <= other.hi
        return self * I((1 / other.hi).next_minus(), (1 / other.lo).next_plus())

    def power(self, n):
        assert n >= 0
        result = I(1)
        for _ in range(n):
            result = result * self
        return result

    def exp(self):
        return I(self.lo.exp().next_minus(), self.hi.exp().next_plus())

    def data(self):
        return [str(self.lo), str(self.hi)]


def atan_bounds(q, terms=70):
    total = sum((Fraction((-1) ** k, (2 * k + 1) * q ** (2 * k + 1)) for k in range(terms)), Fraction(0))
    next_term = Fraction((-1) ** terms, (2 * terms + 1) * q ** (2 * terms + 1))
    return min(total, total + next_term), max(total, total + next_term)


def enclose(cells):
    with localcontext() as ctx:
        ctx.prec = 42
        ctx.Emin = -999999
        lo5, hi5 = atan_bounds(5)
        lo239, hi239 = atan_bounds(239)
        lower, upper = 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239
        pi = I((D(lower.numerator) / D(lower.denominator)).next_minus(), (D(upper.numerator) / D(upper.denominator)).next_plus())
        h = I(2) / cells
        totals = [I(0) for _ in range(3)]
        for j in range(cells):
            a = h * j
            b = h * (j + 1)
            u = I(a.lo, b.hi)
            midpoint = h * (D(j) + D('0.5'))
            e4, e5, e9, e13, e17 = [(u * k).exp() for k in (4, 5, 9, 13, 17)]
            m4, m5, m9 = [(midpoint * k).exp() for k in (4, 5, 9)]
            value, slope, curvature, midvalue = I(0), I(0), I(0), I(0)
            for n in (1, 2, 3):
                c = pi * n ** 2
                envelope = (-(c * e4)).exp()
                value = value + (c.power(2) * 2 * e9 - c * 3 * e5) * envelope
                slope = slope + (c.power(2) * 30 * e9 - c * 15 * e5 - c.power(3) * 8 * e13) * envelope
                curvature = curvature + (c.power(2) * 330 * e9 - c * 75 * e5 - c.power(3) * 224 * e13 + c.power(4) * 32 * e17) * envelope
                midvalue = midvalue + (c.power(2) * 2 * m9 - c * 3 * m5) * (-(c * m4)).exp()
            for k in range(3):
                degree = 2 * k
                second = u.power(degree) * curvature
                if degree:
                    second = second + u.power(degree - 1) * (2 * degree) * slope
                if degree >= 2:
                    second = second + u.power(degree - 2) * (degree * (degree - 1)) * value
                error = h.power(3) * max(abs(second.lo), abs(second.hi)) / 24
                totals[k] = totals[k] + midpoint.power(degree) * midvalue * h + I(-error.hi, error.hi)
        # n>=4 tail: n^4 <=256*3^(n-4), n^2>=16+9(n-4).
        # Integral bound <= C for moments through degree four, by Gaussian
        # integration after e^(4u)>=1+4u+8u^2. The u>2 full-kernel
        # contribution is <1e-39 via the envelope printed in the note.
        tail = pi.power(2) * 512 * (-(pi * 16)).exp() / (I(1) - (-(pi * 9)).exp() * 3)
        raw = [I(v.lo, ((v + I(0, tail.hi)) + I(0, '1e-39')).hi) for v in totals]
        mu2, mu4 = raw[1] / raw[0], raw[2] / raw[0]
        ratio = mu4 / mu2.power(2)
        effective_n = I(2) / (I(3) - ratio)
        assert I(Fraction(25, 9).numerator).lo / 9 < ratio.lo < ratio.hi < D('2.8')
        assert D(9) < effective_n.lo < effective_n.hi < D(10)
        return {"precision": ctx.prec, "cells": cells, "u_interval": [0, 2], "theta_terms": [1, 2, 3], "mu2": mu2.data(), "mu4": mu4.data(), "kurtosis": ratio.data(), "identical_independent_spin_effective_n": effective_n.data(), "scope": "Outward Decimal enclosure; excludes equal-weight independent Rademacher spins at t=0, not general ferromagnetic models."}


parser = argparse.ArgumentParser()
parser.add_argument('--enclose', action='store_true')
parser.add_argument('--cells', type=int, default=2048)
args = parser.parse_args()
low, high = moments(4096), moments(8192)
target_ratio = high[2] / high[1] ** 2
lo, hi = 0.0, 0.1
for _ in range(70):
    coupling = (lo + hi) / 2
    spin = spin_moments(coupling)
    if spin[1] / spin[0] ** 2 > target_ratio:
        lo = coupling
    else:
        hi = coupling
spin = spin_moments(coupling)
scale = math.sqrt(high[1] / spin[0])
predicted6 = scale ** 6 * spin[2]
record = {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "exploratory": {"moments_4096": low, "moments_8192": high, "ten_spin_coupling": coupling, "ten_spin_scale": scale, "sixth_moment_prediction": predicted6, "sixth_moment_relative_mismatch": predicted6 / high[3] - 1, "scope": "Floating-point screening, not a validated fit or zero certificate."}}
target = Path(__file__).with_name('theta_spin_screen_record_20261010.json')
if args.enclose:
    record['enclosure'] = enclose(args.cells)
elif target.exists():
    old = json.loads(target.read_text())
    if old.get('source_sha256') == record['source_sha256'] and 'enclosure' in old:
        record['enclosure'] = old['enclosure']
target.write_text(json.dumps(record, sort_keys=True, indent=2) + '\n')
print(json.dumps(record, sort_keys=True, indent=2))
