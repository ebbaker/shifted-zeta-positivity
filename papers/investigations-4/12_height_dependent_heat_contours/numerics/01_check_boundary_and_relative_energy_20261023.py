#!/usr/bin/env python3
"""Exact finite algebra checks; not a canonical-theta certificate.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-23.
Recorded model gpt-6-astra (Codex), effort ultra. Python standard library.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json
import random
import sys


@dataclass(frozen=True)
class C:
    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other):
        if not isinstance(other, C):
            other = C(Q(other))
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if not isinstance(other, C):
            other = C(Q(other))
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, C):
            other = C(Q(other))
        n = other.re**2 + other.im**2
        assert n
        return self * C(other.re/n, -other.im/n)

    def __pow__(self, n):
        if n < 0:
            return (C(Q(1))/self)**(-n)
        out = C(Q(1))
        for _ in range(n):
            out = out*self
        return out

    def conj(self):
        return C(self.re, -self.im)


def det(columns):
    out = Q(0)
    for perm in permutations(range(4)):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        value = Q(sign)
        for col, row in enumerate(perm):
            value *= columns[col][row]
        out += value
    return out


def realvec(pair):
    return tuple(x for z in pair for x in (z.re, z.im))


def integrate_monomial_path(n, vertices):
    return sum(((b**(n+1)-a**(n+1))/(n+1)
                for a, b in zip(vertices, vertices[1:])), C())


def main(output):
    rng = random.Random(20261023)
    checks = {}
    checks['four_flux_determinants'] = 0
    ii = C(Q(0), Q(1))
    for _ in range(100):
        h0, h1, h2, h3 = [C(Q(rng.randrange(-7, 8)), Q(rng.randrange(-7, 8))) for _ in range(4)]
        g = realvec((h0, h1))
        gt = realvec((-h2, -h3))
        gs = realvec((-ii*h2, -ii*h3))
        gx = realvec((h1, h2))
        gy = realvec((ii*h1, ii*h2))
        ell = h1*h1-h0*h2
        nn = h2*h2-h1*h3
        mm = h1*h2-h0*h3
        expected = [(ell*nn.conj()).re, -(ell*nn.conj()).im,
                    (mm*nn.conj()).re, -(mm*nn.conj()).im]
        for cols, want in zip([(g, gs, gx, gy), (g, gt, gx, gy),
                               (g, gt, gs, gy), (g, gt, gs, gx)], expected):
            assert det(cols) == want
            checks['four_flux_determinants'] += 1
    checks['complex_reference_identity'] = 0
    for d in [C(Q(1,3), Q(1,5)), C(Q(-2), Q(1)), C(Q(4)), C(Q(0),Q(3))]:
        for r in [Q(1,2),Q(1),Q(7,3)]:
            u = d/r
            vv = u**(-2)-C(Q(1))+2*(u-C(Q(1)))
            assert d**(-2) == C(1/r**2)-2*(d-C(r))/(r**3)+vv/(r**2)
            checks['complex_reference_identity'] += 1
    checks['holomorphic_path_integral_identity'] = 0
    for eps, yy in [(Q(1,10000),Q(1,10000)),(Q(1,7),Q(1,13)),(Q(2),Q(3))]:
        gamma = [C(0,-yy),C(-eps,-yy),C(-eps,yy),C(0,yy)]
        direct = [C(0,-yy),C(0,yy)]
        for n in range(13):
            assert integrate_monomial_path(n,gamma) == integrate_monomial_path(n,direct)
            checks['holomorphic_path_integral_identity'] += 1
    coeff = {}
    binom = Q(1)
    for n in range(1,13):
        binom *= (Q(1,2)-(n-1))/n
        coeff[n] = 8*((-8)**n+2*binom*8**n)
    assert coeff[1] == 0
    assert [coeff[n] for n in (2,3,4)] == [384,-3584,30208]
    for n in range(4,13,2):
        assert 0 < coeff[n] < 8*8**n
    control_y = Q(1,100)
    error = 8*control_y*(8*control_y)**4/(5*(1-64*control_y**2))
    leading = -128*control_y**3
    assert leading+error < 0
    checks['relative_energy_coefficients'] = 12
    checks['relative_energy_negative_bound_at_Y_1_over_100'] = True
    checks['zero_event_radius_rejection'] = 0
    for dd, eps, yy in [(Q(1,10000),Q(1,10000),Q(1,10000)),
                        (Q(1,8),Q(1,100),Q(0))]:
        assert (dd+eps)**2+yy**2 > dd**2
        checks['zero_event_radius_rejection'] += 1
    checks['sine_material_derivative'] = 0
    for ell2 in [Q(1),Q(4),Q(9,4)]:
        for h1 in [Q(-3),Q(1),Q(7,5)]:
            h2,h3=Q(0),-ell2*h1
            assert (h2/h1)**2-h3/h1 == ell2
            checks['sine_material_derivative'] += 1
    rho = Q(1,100)
    kk = rho*rho/(1+rho*rho)
    assert kk == Q(1,10001)
    assert kk+(1-kk) == 1
    record = {
        'date':'2026-10-23','prepared_for':'Edward Baker',
        'llm_assistance':'substantial; gpt-6-astra (Codex), effort ultra',
        'status':'all exact finite algebra checks passed; not a theta certificate',
        'arithmetic':'Python integers and fractions.Fraction; no floating point',
        'checks':checks,
        'relative_energy_control':{
            'Y':str(control_y), 'leading':str(leading), 'remainder_bound':str(error),
            'upper_bound_at_Y_1_over_100':str(leading+error),
            'note':'The note proves the negative sign on the full interval 0<Y<=1/100'},
        'rho_fraction':str(kk),
        'scope':'No canonical source jets, wall floors, population counts, charts, physical cap integrals or theta comparison acquired.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(output).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':checks,'output':str(output)}))


if __name__=='__main__':
    main(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('01_BOUNDARY_AND_RELATIVE_ENERGY_CHECKS_20261023.json'))
