#!/usr/bin/env python3
"""Exact heat-polynomial controls for exponential averaged chords.

Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance.
Recorded model gpt-6-astra, effort ultra. Rational intervals certify the
stationary roots, exponential factors and finite control signs. No theta
sign estimate is asserted. Requires only the Python standard library.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import platform


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi, -self.lo)
    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -Q(other))
    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(values), max(values))
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError('interval contains zero')
        return self * I(1/other.hi, 1/other.lo)
    def power(self, n):
        if n == 0:
            return I(1)
        if n % 2:
            return I(self.lo**n, self.hi**n)
        return I(0 if self.lo <= 0 <= self.hi else min(self.lo**n, self.hi**n),
                 max(self.lo**n, self.hi**n))
    def absmax(self):
        return max(abs(self.lo), abs(self.hi))


def heat(m, b, s, sign, derivative):
    result = {}
    for n, c in ((m, Q(sign)), (m+1, sign*b)):
        for p in range(n//2+1):
            degree = n-2*p-derivative
            if degree >= 0:
                value = c*Q(factorial(n), factorial(p)*factorial(degree))*s**p
                result[degree] = result.get(degree, Q(0))+value
    return {k:v for k,v in result.items() if v}


def value(poly, x):
    return sum((c*x**k for k,c in poly.items()), Q(0))


def enclosure(poly, x):
    return sum((c*x.power(k) for k,c in poly.items()), I(0))


def exponential(delta):
    # Alternating Taylor series: positive decreasing terms for 0<delta<=1/4.
    lo = sum(((-delta)**n / factorial(n) for n in range(42)), Q(0))
    hi = sum(((-delta)**n / factorial(n) for n in range(41)), Q(0))
    return I(lo, hi)


def compact_bounds(x):
    denominator = 2**80
    low = (x.lo.numerator*denominator)//x.lo.denominator
    high = -((-x.hi.numerator*denominator)//x.hi.denominator)
    return [str(Q(low, denominator)), str(Q(high, denominator))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    assertions = 0
    def check(ok, label):
        nonlocal assertions
        if not ok:
            raise AssertionError(label)
        assertions += 1

    witnesses = []
    root_count = window_count = 0
    worst_error_over_s = Q(0)
    for m in range(2, 8):
        j = m % 2
        n = m-j
        for b in (Q(0), Q(1,3), Q(-2,5)):
            asymmetry = b if j == 0 else b*Q(m+1,m)
            for sign in (1, -1):
                for exponent in (8, 16, 24):
                    s = Q(1, 2**exponent)
                    polynomials = [heat(m,b,s,sign,d) for d in range(4)]
                    root = I(-2*s, 2*s)
                    check(sign*value(polynomials[j+1], root.lo) < 0, 'left root sign')
                    check(sign*value(polynomials[j+1], root.hi) > 0, 'right root sign')
                    # The heat-polynomial inequality |P_(n-1)| <= (n-1)|x|P_(n-2)
                    # gives the strict sign of W_xx throughout this bracket.
                    check(1-abs(asymmetry)*(n+1)*2*s > 0, 'unique stationary root')
                    for _ in range(80):
                        mid = (root.lo+root.hi)/2
                        y = sign*value(polynomials[j+1], mid)
                        if y == 0:
                            root = I(mid)
                            break
                        root = I(mid, root.hi) if y < 0 else I(root.lo, mid)
                    check(root.hi-root.lo <= 4*s/Q(2**80), 'root enclosure width')
                    H = enclosure(polynomials[0], root)
                    W = enclosure(polynomials[j], root)
                    check(sign*W.lo > 0 if sign > 0 else sign*W.hi > 0, 'starting sign')
                    if j == 0:
                        factor = I(1)
                    else:
                        ratio_squared_upper = (H/W).absmax()**2
                        factor = I(1/(1+ratio_squared_upper/2), 1)
                    root_count += 1
                    for delta in (Q(1,8), Q(1,4)):
                        check(1-abs(asymmetry)*(n+1)*(2*s+delta) > 0,
                              'entire shifted interval is zero-free')
                        q = exponential(delta)
                        check(0 < q.lo <= q.hi < 1, 'exponential enclosure')
                        Wend = enclosure(polynomials[j], root+delta)
                        scaled = sign*(W-q*Wend)*factor
                        limit = -q*(sign*value(heat(m,b,Q(0),sign,j),delta))
                        check(limit.hi < 0, 'limiting negative amplitude')
                        check(scaled.hi < 0, 'finite negative averaged chord')
                        error = (scaled-limit).absmax()
                        check(error <= 10000*s, 'finite convergence bound')
                        worst_error_over_s = max(worst_error_over_s, error/s)
                        window_count += 1
                        if exponent == 24 and sign == 1 and b == Q(1,3):
                            witnesses.append({'multiplicity':m,'branch':j,'b':str(b),
                                's':str(s),'delta':str(delta),
                                'stationary_root':compact_bounds(root),
                                'A_over_sqrt_physical_E':compact_bounds(scaled),
                                'negative_limit':compact_bounds(limit)})
    record = {'date':'2026-10-15','timezone':'America/New_York',
        'prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra',
        'llm_assistance':'Substantial LLM assistance; internal exact rational controls.',
        'script':Path(__file__).name,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python_version':platform.python_version(),'status':'PASS',
        'exact_assertions':assertions,'heat_germs':36,
        'certified_stationary_roots':root_count,'certified_zero_free_windows':window_count,
        'observation':'A=W(start)^2-exp(-delta)W(start)W(start+delta)',
        'event_time':'arbitrary T, with s=T-t',
        's_values':['1/256','1/65536','1/16777216'],
        'delta_values':['1/8','1/4'],
        'error_bound':'|A/sqrt(E)-negative_limit| <= 10000*s on these finite controls',
        'observed_max_error_over_s_upper':compact_bounds(I(worst_error_over_s))[1],
        'scope':'Polynomial collision controls only. Whole-interval zero-freeness and stationary uniqueness use the stated analytic heat-polynomial inequalities plus rational checks. The general exponential-average identity and arbitrary-multiplicity theorem are analytic proofs in the accompanying note. No theta sign or numerical theta certificate.',
        'witnesses':witnesses}
    if args.output:
        args.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='witnesses'},indent=2))


if __name__ == '__main__':
    main()
