#!/usr/bin/env python3
"""Exact finite controls for the analytic all-multiplicity remainder proof.

Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
reasoning effort ultra. The theorem for all m is in the note, not inferred
from this finite replay. Standard library only; no floating arithmetic.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json


def clean(p):
    return {ij: F(c) for ij, c in p.items() if c}


def add(p, q):
    out = dict(p)
    for ij, c in q.items():
        out[ij] = out.get(ij, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({ij: c*x for ij, x in p.items()})


def shift(p, i, j):
    return {(k+i, ell+j): c for (k, ell), c in p.items()}


def diff(p, axis):
    out = {}
    for ij, c in p.items():
        if ij[axis]:
            key = list(ij)
            key[axis] -= 1
            out[tuple(key)] = c*ij[axis]
    return clean(out)


def dy(p, order):
    for _ in range(order):
        p = diff(p, 1)
    return p


def P(n):
    return {(k, n-2*k): F((-1)**k, factorial(k)*factorial(n-2*k))
            for k in range(n//2+1)}


def b(n):
    return sum((abs(c) for c in P(n).values()), F(0))


def envelope(p, radius):
    # Valid on the complete rectangle |s|<=radius^2, |y|<=radius.
    return sum((abs(c)*radius**(2*i+j) for (i, j), c in p.items()), F(0))


def bounds(m, radius, k1, k2):
    d = F(1, factorial(m//2+1))
    e0 = b(m+1)*k1*radius + (d*k2*radius**2 if m % 2 == 0 else 0)
    e1 = b(m)*k1*radius + (d*k2*radius**2 if m % 2 else 0)
    return e0, e1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    assert b(2) == F(3, 2) and b(3) == F(7, 6) and b(4) == F(25, 24)
    controls = []
    outer = F(1, 8)
    for m in range(2, 13):
        for n in (m, m+1, m+2):
            assert not add(diff(P(n), 0), dy(P(n), 2))
            assert dy(P(n), 1) == P(n-1)
            recur = add(shift(P(n-1), 0, 1), scale(shift(P(n-2), 1, 0), -2))
            assert scale(P(n), n) == recur
        field = add(add(P(m), P(m+1)), P(m+2))
        first = field.get((0, 0), F(0))
        assert first == 0
        for j in range(m):
            assert dy(field, j).get((0, 0), F(0)) == 0
        assert dy(field, m).get((0, 0), F(0)) == 1
        k1 = envelope(dy(field, m+1), outer)
        k2 = envelope(dy(field, m+2), outer)
        assert k1 == 1+outer and k2 == 1
        ell = F(1, 2*(2*m*m*(m+2))**(m-1))
        d = F(1, factorial(m//2+1))
        # A rational sufficient subchoice of the note's radius; r<=1
        # lets r^2<=r control the quadratic term without a square root.
        certified = min(outer, F(1), ell/(8*(b(m)+b(m+1))*k1), ell/(8*d*k2))
        for sign in (1, -1):
            signed = scale(field, sign)
            for radius in (outer/2, certified):
                e0, e1 = bounds(m, radius, k1, k2)
                rem0 = add(signed, scale(P(m), -sign))
                rem1 = add(dy(signed, 1), scale(P(m-1), -sign))
                actual0 = envelope(rem0, radius)/radius**m
                actual1 = envelope(rem1, radius)/radius**(m-1)
                assert actual0 <= e0 and actual1 <= e1
                if radius == certified:
                    assert e0+e1 <= ell/4
                    assert e0*e0+e1*e1 < ell*ell
        e0, e1 = bounds(m, certified, k1, k2)
        controls.append({'m': m, 'field': 'P_m+P_(m+1)+P_(m+2), and its negative',
                         'outer_radius': str(outer), 'B_m_plus_1': str(k1), 'B_m_plus_2': str(k2),
                         'b_m': str(b(m)), 'b_m_plus_1': str(b(m+1)),
                         'coarse_boundary_margin': str(ell), 'certified_radius': str(certified),
                         'remainder_sum_over_margin': str((e0+e1)/ell),
                         'inherited_degree': -(m//2),
                         'outcome': 'parity remainder and complete-radius margin passed'})
    script = Path(__file__).resolve()
    note = script.parent.parent/'notes/02_ALL_MULTIPLICITY_REMAINDER_AUDIT_20261020.md'
    record = {'date': '2026-10-20', 'prepared_for': 'Edward Baker',
              'model': 'gpt-6-astra', 'reasoning_effort': 'ultra',
              'status': 'exact finite asymmetric polynomial controls passed',
              'arithmetic': 'Python standard-library exact fractions',
              'source_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
              'note_sha256': hashlib.sha256(note.read_bytes()).hexdigest(),
              'scope': 'm=2,...,12 controls check algebra and payments. The all-m theorem is proved analytically in the note.',
              'controls': controls,
              'limitations': ['No theta moment quadrature or event certificate.',
                              'No runtime comparison or uniform-in-m radius claim.',
                              'The inherited index is recorded, not reproved by this replay.']}
    serialized = json.dumps(record, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(serialized)
        print('Exact all-multiplicity remainder controls passed; receipt written to '+str(args.output))
    else:
        print(serialized, end='')


if __name__ == '__main__':
    main()
