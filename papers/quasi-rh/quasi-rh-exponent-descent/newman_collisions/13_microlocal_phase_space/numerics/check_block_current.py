#!/usr/bin/env python3
"""Outward Decimal enclosure of a genuine macroscopic-block phase current.

Only standard-library arithmetic is used.  Pi and trigonometric functions
use explicit Taylor bounds.  Decimal ln/exp are correctly rounded; adjacent
representable values give enclosing endpoints.  No ordinary float enters
the certificate.  This checks a block current, not a heat collision.
"""
import argparse
import hashlib
import json
import platform
from decimal import (Decimal, Context, ROUND_FLOOR, ROUND_CEILING,
                     ROUND_HALF_EVEN, getcontext)
from fractions import Fraction
from pathlib import Path

PRECISION = 60
getcontext().prec = PRECISION
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)
NEAR = Context(prec=PRECISION, rounding=ROUND_HALF_EVEN)


class I:
    """Closed Decimal interval; endpoints rounded out at every operation."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        assert self.lo <= self.hi

    @staticmethod
    def rational(value):
        value = Fraction(value)
        n, d = Decimal(value.numerator), Decimal(value.denominator)
        return I(DOWN.divide(n, d), UP.divide(n, d))

    @staticmethod
    def cast(other):
        return other if isinstance(other, I) else I(other)

    def __add__(self, other):
        other = I.cast(other)
        return I(DOWN.add(self.lo, other.lo), UP.add(self.hi, other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self+-I.cast(other)

    def __rsub__(self, other):
        return I.cast(other)+-self

    def __mul__(self, other):
        other = I.cast(other)
        pairs = [(x, y) for x in (self.lo, self.hi)
                 for y in (other.lo, other.hi)]
        return I(min(DOWN.multiply(x, y) for x, y in pairs),
                 max(UP.multiply(x, y) for x, y in pairs))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi
        return I(DOWN.divide(Decimal(1), self.hi),
                 UP.divide(Decimal(1), self.lo))

    def __truediv__(self, other):
        return self*I.cast(other).reciprocal()

    def __rtruediv__(self, other):
        return I.cast(other)*self.reciprocal()

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        if power == 0:
            return I(1)
        if power % 2 == 0 and self.lo <= 0 <= self.hi:
            upper = max(UP.power(self.lo, power), UP.power(self.hi, power))
            return I(0, upper)
        vals_down = [DOWN.power(self.lo, power), DOWN.power(self.hi, power)]
        vals_up = [UP.power(self.lo, power), UP.power(self.hi, power)]
        return I(min(vals_down), max(vals_up))

    def ln(self):
        assert self.lo > 0
        return I(NEAR.ln(self.lo).next_minus(NEAR),
                 NEAR.ln(self.hi).next_plus(NEAR))

    def exp(self):
        return I(NEAR.exp(self.lo).next_minus(NEAR),
                 NEAR.exp(self.hi).next_plus(NEAR))

    def midpoint(self):
        return NEAR.divide(NEAR.add(self.lo, self.hi), Decimal(2))

    def width(self):
        return UP.subtract(self.hi, self.lo)

    def strings(self):
        return [str(self.lo), str(self.hi)]


def atan_small(x, terms):
    """Alternating arctangent enclosure for an interval 0<=x<1."""
    x = I.cast(x)
    assert 0 <= x.lo and x.hi < 1
    total, term = I(0), x
    square = x*x
    for k in range(terms):
        total += ((-1)**k)*term/(2*k+1)
        term *= square
    bound = (term/(2*terms+1)).hi
    return total+I(bound.copy_negate(), bound)


def pi_interval():
    # tan(4 atan(1/5)-atan(1/239))=1, with the angle in (0,pi/2).
    z = Fraction(1, 5)
    twice = 2*z/(1-z*z)
    four = 2*twice/(1-twice*twice)
    assert (four-Fraction(1, 239))/(1+four/Fraction(239)) == 1
    return 16*atan_small(I.rational(Fraction(1, 5)), 100) \
        -4*atan_small(I.rational(Fraction(1, 239)), 100)


def trig_taylor(angle, terms=30):
    """Sin/cos on |angle|<=4; absolute Taylor remainder enclosed."""
    assert -4 <= angle.lo <= angle.hi <= 4
    square = angle*angle
    sin_total, cos_total = I(0), I(0)
    sin_term, cos_term = angle, I(1)
    for k in range(terms):
        sin_total += ((-1)**k)*sin_term
        cos_total += ((-1)**k)*cos_term
        sin_term = sin_term*square/((2*k+2)*(2*k+3))
        cos_term = cos_term*square/((2*k+1)*(2*k+2))
    # Taylor degree 2*terms-1 (sin) and 2*terms-2 (cos): all derivatives <=1.
    sin_bound = I.rational(Fraction(4)**(2*terms)/factorial(2*terms)).hi
    cos_bound = I.rational(Fraction(4)**(2*terms-1)/factorial(2*terms-1)).hi
    return (sin_total+I(sin_bound.copy_negate(), sin_bound),
            cos_total+I(cos_bound.copy_negate(), cos_bound))


def factorial(n):
    out = 1
    for k in range(2, n+1):
        out *= k
    return out


def reduced_trig(angle, pi):
    period = 2*pi
    turns = int(NEAR.divide(angle.midpoint(), period.midpoint())
                .to_integral_value(rounding=ROUND_HALF_EVEN))
    reduced = angle-turns*period
    return trig_taylor(reduced)


def product_real(a, b):
    return a[0]*b[0]+a[1]*b[1]


def product_imag(a, b):
    """Imaginary part of a*conjugate(b)."""
    return a[1]*b[0]-a[0]*b[1]


def enclose(M):
    assert M >= 22027
    pi = pi_interval()
    logM = I(M).ln()
    L, t = 2*logM, 1/(2*logM)
    assert t.hi < Decimal('0.05')
    x = 4*pi*M*M
    x2 = x*x
    atanx = pi/2-atan_small(1/x, 6)
    log_correction = (1+1/x2).ln()
    ar = L/2+log_correction/4-1/(1+x2)
    ai = 3*x/(1+x2)-atanx/2
    U = (7*x2-5)/((1+x2)**2)
    V = x*(x2+5)/((1+x2)**2)
    c = (1+t*U/2)/2
    Omega = (ar*(1+t*U/2)-ai*t*V/2)/2
    lamN = Omega-c*logM
    aN = I('0.5')+t*ar/2-t*logM/2
    aprime = t*V/4
    T = (x-t*ai)/2
    wN = (t*logM*logM/4-(I('0.5')+t*ar/2)*logM).exp()
    z0 = [I(0), I(0)]
    z1 = [I(0), I(0)]
    for n in range(M//2+1, M+1):
        delta = (I(M)/n).ln()
        amp = (aN*delta+t*delta*delta/4).exp()
        sine, cosine = reduced_trig(-T*delta, pi)
        qr, qi = amp*cosine, amp*sine
        z0[0] += qr
        z0[1] += qi
        z1[0] += delta*qr
        z1[1] += delta*qi
    z0norm = z0[0]**2+z0[1]**2
    mixed_real, mixed_imag = product_real(z1, z0), product_imag(z1, z0)
    current_over_w2 = lamN*z0norm+c*mixed_real-aprime*mixed_imag
    current = wN*wN*current_over_w2
    assert current_over_w2.hi < 0, current_over_w2.strings()
    assert current_over_w2.width() < Decimal('1e-30')
    # Carrier reduced analytically, removing the exact integer pi*M^2.
    carrier = pi*(M % 2)-pi+atanx/4-x*log_correction/8 \
        +t*ai*(ar-logM)/2
    sine, cosine = reduced_trig(carrier, pi)
    Sreal = wN*(cosine*z0[0]-sine*z0[1])
    Simag = wN*(cosine*z0[1]+sine*z0[0])
    # gamma_N=-tV logN/4-i lambda_N; g=aprime-i c.
    gamma_real = -aprime*logM
    Dreal = gamma_real*z0[0]+lamN*z0[1]+aprime*z1[0]+c*z1[1]
    Dimag = gamma_real*z0[1]-lamN*z0[0]+aprime*z1[1]-c*z1[0]
    Sprime_real = wN*(cosine*Dreal-sine*Dimag)
    Sprime_imag = wN*(cosine*Dimag+sine*Dreal)
    direct_current = -(Sprime_imag*Sreal-Sprime_real*Simag)
    assert direct_current.lo <= current.hi and current.lo <= direct_current.hi
    second_coordinate = 4*Sprime_real/L
    energy = Sreal**2+second_coordinate**2
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        'status': 'PASS',
        'scope': 'certified outward interval for an actual finite relative-block phase current; not a heat collision or complete-sum sign',
        'M': M, 'kappa': '1', 'N': M,
        'indices': [M//2+1, M], 'number_of_terms': M-M//2,
        'time_interval': t.strings(), 'height_interval': x.strings(),
        'decimal_precision': PRECISION, 'pi_atan_terms': 100, 'trig_terms': 30,
        'Z0_real_interval': z0[0].strings(), 'Z0_imag_interval': z0[1].strings(),
        'Z1_real_interval': z1[0].strings(), 'Z1_imag_interval': z1[1].strings(),
        'current_over_wN_squared_interval': current_over_w2.strings(),
        'current_interval': current.strings(),
        'value_coordinate_interval': Sreal.strings(),
        'derivative_coordinate_interval': second_coordinate.strings(),
        'joint_block_energy_interval': energy.strings(),
        'current_formula_overlap': True,
        'source_sha256': source_hash, 'python_version': platform.python_version(),
        'sources': ['https://docs.python.org/3/library/decimal.html'],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--M', type=int, default=22066)
    args = parser.parse_args()
    print(json.dumps(enclose(args.M), indent=2))
