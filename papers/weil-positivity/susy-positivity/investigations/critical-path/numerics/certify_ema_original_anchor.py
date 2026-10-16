#!/usr/bin/env python3
"""All-input prime-free anchor from the fixed arithmetic EMA tower.

Pure standard library. Every certificate comparison uses outward fixed-point
rational intervals; NumPy and floating eigenvalues are not used. See the
associated research note for the infinite-dimensional reduction and flow step.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path


class I:
    scale = 10**40

    def __init__(self, q=0):
        q = F(q)
        self.lo = q.numerator*self.scale//q.denominator
        self.hi = -((-q.numerator*self.scale)//q.denominator)

    @classmethod
    def raw(cls, lo, hi):
        assert lo <= hi
        x = object.__new__(cls)
        x.lo, x.hi = lo, hi
        return x

    def __add__(self, y):
        y = y if isinstance(y, I) else I(y)
        return I.raw(self.lo+y.lo, self.hi+y.hi)

    __radd__ = __add__

    def __neg__(self):
        return I.raw(-self.hi, -self.lo)

    def __sub__(self, y):
        return self+(-y if isinstance(y, I) else -I(y))

    def __rsub__(self, y):
        return I(y)+(-self)

    def __mul__(self, y):
        y = y if isinstance(y, I) else I(y)
        v = (self.lo*y.lo, self.lo*y.hi, self.hi*y.lo, self.hi*y.hi)
        return I.raw(min(v)//self.scale, -((-max(v))//self.scale))

    __rmul__ = __mul__

    def reciprocal(self):
        assert self.lo > 0 or self.hi < 0
        t = self.scale**2
        return I.raw(t//self.hi, -((-t)//self.lo))

    def __truediv__(self, y):
        y = y if isinstance(y, I) else I(y)
        return self*y.reciprocal()

    def __rtruediv__(self, y):
        return I(y)*self.reciprocal()

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = I(1)
        for _ in range(n):
            out = out*self
        return out

    def abs(self):
        lo = 0 if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi))
        return I.raw(lo, max(abs(self.lo), abs(self.hi)))

    def sqrt(self):
        assert self.lo >= 0
        a, b = isqrt(self.lo*self.scale), isqrt(self.hi*self.scale)
        return I.raw(a, b+(b*b < self.hi*self.scale))

    def lower(self):
        return F(self.lo, self.scale)

    def upper(self):
        return F(self.hi, self.scale)

    def record(self):
        return {'lower': str(self.lower()), 'upper': str(self.upper()),
                'decimal_display_only': [float(self.lower()), float(self.upper())]}


def atan_reciprocal(q, terms=64):
    z = F(1, q)
    s = sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    t = (-1)**terms*z**(2*terms+1)/F(2*terms+1)
    return I.raw(I(min(s, s+t)).lo, I(max(s, s+t)).hi)


def log_interval(q):
    q = q if isinstance(q, I) else I(q)
    assert q.lower() >= 1
    k = 0
    while q.lower() >= 2:
        q = q/2
        k += 1
    assert q.upper() < 2

    def atanh_series(z):
        s = I(0)
        power = z
        for j in range(64):
            s += 2*power/(2*j+1)
            power *= z*z
        tail = 2*power/(129*(1-z*z))
        return s+I.raw(0, tail.hi)

    return atanh_series((q-1)/(q+1))+k*atanh_series(I(F(1, 3)))


def exp_interval(q):
    q = q if isinstance(q, I) else I(q)
    assert q.lo >= 0
    count = 0
    while q.upper() > F(1, 2):
        q = q/2
        count += 1
    term, partial = I(1), I(1)
    for j in range(1, 49):
        term = term*q/j
        partial += term
    tail = (term*q/49)/(1-q/50)
    out = partial+I.raw(0, tail.hi)
    for _ in range(count):
        out *= out
    return out


def ldl_positive(A):
    """Enclose the exact no-pivot LDL recursion and prove every pivot positive."""
    n = len(A)
    unit = [[I(int(i == j)) for j in range(n)] for i in range(n)]
    pivots = []
    for j in range(n):
        d = A[j][j]-sum((unit[j][k]**2*pivots[k] for k in range(j)), I(0))
        assert d.lo > 0, ('unproved LDL pivot', j, d.record())
        pivots.append(d)
        for i in range(j+1, n):
            unit[i][j] = (A[i][j]-sum((unit[i][k]*unit[j][k]*pivots[k]
                                      for k in range(j)), I(0)))/d
    return pivots


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--digits', type=int, default=40)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert args.digits >= 24
    I.scale = 10**args.digits
    L, b, M, N, J = I(F(1, 2)), I(F(1, 2)), 32, 16, 128
    pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
    H = I(sum((F(1, j) for j in range(1, 1001)), F(0)))
    hn = H-log_interval(1000)
    gamma = I.raw((hn-F(1, 2000)).lo, (hn-F(1, 2002)).hi)
    w0 = -gamma-pi/2-3*log_interval(2)-log_interval(pi)
    a = [I(F(4*n+1, 2)) for n in range(M)]
    k2 = [(j*pi/L)**2 for j in range(J)]
    phi = [(1/L).sqrt()]+[(2/L).sqrt()]*(J-1)
    v = [[phi[j]/(aa*aa+k2[j]) for j in range(J)] for aa in a]
    e = [1/exp_interval(aa*L) for aa in a]
    coeff = [[2*aa*aa*(1-(-1)**parity*ee) for aa, ee in zip(a, e)]
             for parity in (0, 1)]
    ep = exp_interval(b*L/2)
    sh, ch = (ep-1/ep)/2, (ep+1/ep)/2
    c = [2*b*sh*phi[j]/(b*b+k2[j]) if j % 2 == 0 else I(0) for j in range(J)]
    s = [-2*b*ch*phi[j]/(b*b+k2[j]) if j % 2 else I(0) for j in range(J)]

    def diag(j):
        return w0+sum((2/aa*k2[j]/(aa*aa+k2[j]) for aa in a), I(0))

    def entry(i, j):
        if i % 2 != j % 2:
            return I(0)
        return sum((coeff[i % 2][n]*v[n][i]*v[n][j] for n in range(M)), I(0)) \
            +2*c[i]*c[j]-2*s[i]*s[j]

    A = [[entry(i, j)+(diag(i) if i == j else 0) for j in range(N)] for i in range(N)]
    head_floor, tail_floor, mixed_sq, target = F(11, 400), F(107, 50), F(49, 10000), F(1, 40)
    pivots = ldl_positive([[A[i][j]-(head_floor if i == j else 0)
                           for j in range(N)] for i in range(N)])
    # sum_{j>=r} j^-4 <= 1/[3(r-1)^3], r>=2; no parity saving used.
    def fourth_tail(r):
        return (2/L)*(L/pi)**4/(3*(r-1)**3)
    high_lower = diag(N)-2*(2*b*ch)**2*fourth_tail(N)
    assert high_lower.lower() >= tail_floor
    finite_hs = sum((entry(i, j).abs()**2 for i in range(N) for j in range(N, J)), I(0))
    env = [2*phi[i]*sum((aa*aa*(1+ee)/(aa*aa+k2[i]) for aa, ee in zip(a, e)), I(0))
           +4*b*(c[i].abs()*sh+s[i].abs()*ch) for i in range(N)]
    tail_hs = fourth_tail(J)*sum((t*t for t in env), I(0))
    mixed_upper = finite_hs+tail_hs
    assert mixed_upper.upper() <= mixed_sq
    schur_slack = (head_floor-target)*(tail_floor-target)-mixed_sq
    assert min(head_floor-target, tail_floor-target, schur_slack) > 0
    # Shift perturbation, after the exact lowest gamma-mode/pole cancellation.
    omega = F(1, 1000)
    ew = exp_interval(omega*L)
    factor = (ew+1/ew)/2*(L*L/4+exp_interval(L/2)*L**3/3)
    assert factor.upper() <= F(1, 8)
    shifted_floor = target-omega**2/8
    x = 2*shifted_floor*omega
    defect_floor = F(49998, 10**9)
    assert x-x*x/2 >= defect_floor
    out = {
        'schema': 1, 'date': '2026-09-20',
        'model': 'OpenAI GPT-6 (Codex; system identity)',
        'reasoning_effort': 'Not exposed in this reviewing session; no inference from the reviewed task setting',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'Outward fixed-point rational intervals; exact integer decisions; decimal displays are non-certifying',
        'digits': args.digits, 'parameters': {'L': '1/2', 'M': M, 'N': N, 'J': J, 'omega_max': str(omega)},
        'constants': {'pi': pi.record(), 'gamma': gamma.record(), 'w0': w0.record()},
        'head_ldl_pivots': [d.record() for d in pivots],
        'high_block_lower': high_lower.record(), 'finite_mixed_HS_squared': finite_hs.record(),
        'remaining_mixed_HS_squared_upper': tail_hs.record(), 'mixed_HS_squared_upper': mixed_upper.record(),
        'rounded_certificate': {'head_floor': str(head_floor), 'tail_floor': str(tail_floor),
                                'mixed_norm_squared_upper': str(mixed_sq), 'central_floor': str(target),
                                'schur_slack': str(schur_slack)},
        'shift_factor': factor.record(), 'shifted_floor_uniform': str(shifted_floor),
        'original_defect_floor_at_omega_max': str(defect_floor),
        'normalized_defect_floor_at_omega_max': str(defect_floor/(2*omega)),
        'scope': 'All L2 inputs, original complete prime-free transfer at L=1/2 and 0<omega<=1/1000, conditional only on the analytic reduction documented in the research note; no auxiliary output smoother, all-depth result, or physical realization.',
        'certificate_pass': True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'certificate_pass': True, 'rounded_certificate': out['rounded_certificate'],
                      'mixed_HS_upper_display': float(mixed_upper.upper()),
                      'original_defect_floor': str(defect_floor), 'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Certification requires assertions; do not use python -O.')
    main()
