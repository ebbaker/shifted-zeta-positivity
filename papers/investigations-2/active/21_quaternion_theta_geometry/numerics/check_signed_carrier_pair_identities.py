#!/usr/bin/env python3
"""Exact coefficient checks for the signed common-carrier pair formula.

Prepared for Edward Baker, 2026-10-14, with substantial LLM assistance.
Recorded parent configuration: gpt-6-astra, reasoning effort ultra.
This checks finite algebra, not an infinite-domain theta sign estimate.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import platform

DIM = 8
ZERO = (0,) * DIM


class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.c = dict(value.c)
        elif isinstance(value, dict):
            self.c = {m: F(v) for m, v in value.items() if v}
        else:
            self.c = {ZERO: F(value)} if value else {}

    def __add__(self, other):
        out = dict(self.c)
        for m, v in P(other).c.items():
            out[m] = out.get(m, F(0)) + v
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -v for m, v in self.c.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        out = {}
        for m, v in self.c.items():
            for n, w in P(other).c.items():
                k = tuple(i + j for i, j in zip(m, n))
                out[k] = out.get(k, F(0)) + v * w
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, k):
        out = P(1)
        for _ in range(k):
            out = out * self
        return out


class C:
    def __init__(self, real=0, imag=0):
        self.r, self.i = P(real), P(imag)

    def __add__(self, other):
        return C(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return C(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        if not isinstance(other, C):
            other = C(other)
        return C(self.r * other.r - self.i * other.i,
                 self.r * other.i + self.i * other.r)

    def __pow__(self, k):
        out = C(1)
        for _ in range(k):
            out = out * self
        return out

    def conj(self):
        return C(self.r, -self.i)


def var(i):
    m = list(ZERO)
    m[i] = 1
    return P({tuple(m): 1})


checks = []


def equal(name, left, right):
    residual = left - right
    if residual.c:
        raise AssertionError((name, residual.c))
    checks.append(name)


def main():
    a, y, z, wr, wi, vr, vi, b = [var(i) for i in range(DIM)]
    q, r, W, V = C(-a, y), C(-a, z), C(wr, wi), C(vr, vi)
    p = [(W * q**k).r for k in range(4)]
    s = [(V * r**k).r for k in range(4)]
    for k in range(4):
        equal(f'real-product polarization k={k}', p[k] * s[k],
              F(1, 2) * ((W * V.conj() * (q * r.conj())**k).r
                         + (W * V * (q * r)**k).r))
    for j in (0, 1):
        pair = p[j+1] * s[j+1] - F(1, 2) * (p[j] * s[j+2] + p[j+2] * s[j])
        formula = F(1, 4) * (
            (y+z)**2 * (W * V.conj() * (q * r.conj())**j).r
            + (y-z)**2 * (W * V * (q * r)**j).r)
        equal(f'full signed pair kernel j={j}', pair, formula)
        residual_pair = F(1, 2) * (y*y + z*z - 2*b*b) * p[j] * s[j]
        ideal = p[j+1] * s[j+1] + a * (p[j] * s[j+1] + p[j+1] * s[j])
        equal(f'centered stationary ideal j={j}',
              pair - (a*a+b*b) * p[j] * s[j] - residual_pair, ideal)
    # The pair frequencies lose the common horizontal drift exactly.
    equal('Hermitian frequency difference real', ((q-r.conj())**2).r, -(y+z)**2)
    equal('Hermitian frequency difference imaginary', ((q-r.conj())**2).i, P())
    equal('bilinear frequency difference real', ((q-r)**2).r, -(y-z)**2)
    equal('bilinear frequency difference imaginary', ((q-r)**2).i, P())
    equal('sum of pair frequency squares', (y+z)**2+(y-z)**2, 2*(y*y+z*z))
    # Expansion underlying the paid scalar tail bound; variables are renamed.
    p0, p1, p2, e0, e1, e2 = a, y, z, wr, wi, vr
    equal('complete quadratic error expansion',
          (p1+e1)**2 - (p0+e0)*(p2+e2) - (p1*p1-p0*p2),
          2*p1*e1+e1*e1-p0*e2-p2*e0-e0*e2)
    equal('direct pair-tail mass expansion',
          (p0+e0)*(p2+e2)-p0*p2, p0*e2+p2*e0+e0*e2)
    # Convexity and endpoint arithmetic in the threshold-three proof.
    def exponent1(beta, theta, delta=0):
        return F(1, 6) - theta*beta*(1-beta)*F(1, 4) + delta*beta

    def exponent2(beta, theta, delta=0):
        return -F(1, 6) + beta*F(1, 2) - theta*beta*(1-beta)*F(1, 4) + delta*beta

    for name, fn, expected in (
        ('first', exponent1, (F(0), F(-1, 48))),
        ('second', exponent2, (F(-1, 6), F(-5, 48))),
    ):
        for beta, target in zip((F(1, 3), F(1, 2)), expected):
            equal(f'{name} block endpoint beta={beta}', P(fn(beta, F(3))), P(target))
        chord = 6*(fn(F(1, 3), a, z)*(F(1, 2)-y)
                   + fn(F(1, 2), a, z)*(y-F(1, 3)))
        equal(f'{name} convex chord gap', chord-fn(y, a, z),
              a*F(1, 4)*(y-F(1, 3))*(F(1, 2)-y))
    equal('small-index exponent excess',
          F(1, 2)+(3+a*F(1, 2)+b)*F(1, 6)-a*F(1, 72)
          -(1+a*F(1, 24)+b*F(1, 6)), a*F(1, 36))
    equal('first high-index exponent margin',
          F(1, 6)-(3+a*F(1, 2)+b)*F(1, 18)+a*F(1, 144),
          -a*F(1, 48)-b*F(1, 18))
    # Per-index smooth recurrence: d=b, v=y+b, time=wr, lambda=q.
    for j in range(4):
        last = C(0, j)*q**(j-1) if j else C()
        left = q**j*(-2*wr*b)+last
        right = C(-2*wr*(y+b), -2*wr*a)*q**j+C(0, -2*wr)*q**(j+1)+last
        equal(f'smooth staircase recurrence real j={j}', left.r, right.r)
        equal(f'smooth staircase recurrence imaginary j={j}', left.i, right.i)
    # Complete entry phase: t(d+ia)^2 + ixd + td^2-2td(d+ia)-ixd.
    entry = C(b, a)**2*wr+C(0, z*b)+C(wr*b*b)-C(b, a)*(2*wr*b)-C(0, z*b)
    equal('entry exponent real cancellation', entry.r, -wr*a*a)
    equal('entry exponent imaginary cancellation', entry.i, P())
    # Two signed atoms: positive individual contributions, negative total.
    atoms = [(F(1), F(1)), (F(2), -F(1, 2))]
    # Compute this example with exact rational real jets.
    h0 = sum(w for u, w in atoms)
    h2 = -sum(w*u*u for u, w in atoms)
    total = -h0*h2
    diagonal = sum(w*w*u*u for u, w in atoms)
    if (total, diagonal, total-diagonal) != (F(-1, 2), F(2), F(-5, 2)):
        raise AssertionError('signed atom cross-term control')
    checks.append('signed two-atom control retains adverse cross terms')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    record = {
        'date': '2026-10-14', 'prepared_for': 'Edward Baker',
        'llm_assistance': 'Substantial', 'recorded_model': 'gpt-6-astra',
        'recorded_effort': 'ultra', 'status': 'PASS',
        'source_name': Path(__file__).name,
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'python': platform.python_version(),
        'arithmetic': 'exact rational sparse polynomial coefficients',
        'checks': len(checks), 'identities': checks,
        'signed_atom_control': {'total_L0': '-1/2', 'diagonal_L0': '2', 'cross_L0': '-5/2'},
        'scope': 'Finite polynomial identities and a non-theta signed-atom control; no theta sign certificate, no quadrature, no finite-height extension.'
    }
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'checks': len(checks), 'output': str(args.output)}))


if __name__ == '__main__':
    main()
