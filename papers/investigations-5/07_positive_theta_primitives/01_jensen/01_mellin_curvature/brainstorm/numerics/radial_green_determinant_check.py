#!/usr/bin/env python3
"""Exact rational checks of the Green boundary expansion; no theta sign tests.

Prepared for Edward Baker, 2026-11-04, with substantial LLM assistance.
Recorded model gpt-6-astra, effort xhigh. Python standard library only.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, comb
import argparse
import hashlib
import json
from pathlib import Path


def add_term(p, e, a):
    p[e] = p.get(e, F(0)) + a
    if not p[e]:
        del p[e]


def add(p, q):
    z = dict(p)
    for e, a in q.items():
        add_term(z, e, a)
    return z


def scale(p, a):
    return {e: c*a for e, c in p.items() if c*a}


def mul(p, q):
    z = {}
    for e, a in p.items():
        for f, b in q.items():
            add_term(z, tuple(x+y for x, y in zip(e, f)), a*b)
    return z


def sign(perm):
    return (-1)**sum(perm[i] > perm[j] for i in range(len(perm))
                     for j in range(i+1, len(perm)))


def probe(r, k):
    """Sym det[m_(k+j-i)(u_i)]; exponents store powers of u_i^2."""
    raw = {}
    ps = list(permutations(range(r)))
    for perm in ps:
        es = tuple(k+perm[i]-i for i in range(r))
        if min(es) < 0:
            continue
        a = F(sign(perm))
        for n in es:
            a /= factorial(2*n)
        add_term(raw, es, a)
    out = {}
    for es, a in raw.items():
        for perm in ps:
            add_term(out, tuple(es[perm[i]] for i in range(r)),
                     a/factorial(r))
    return out


def L(p, i):
    """Apply partial_(u_i)^2 - 1 in the even polynomial basis."""
    q = scale(p, F(-1))
    for es, a in p.items():
        n = es[i]
        if n:
            e = list(es)
            e[i] -= 1
            add_term(q, tuple(e), a*(2*n)*(2*n-1))
    return q


def face_probe(p, r, q):
    for i in range(q):
        p = L(p, i)
    out = {}
    for es, a in p.items():
        if any(es[q:]):
            continue
        add_term(out, es[:q], a)
    return out


def integrate(p, q, r, dim):
    """Return moment polynomial in b,d0,d1,... including face prefactor."""
    out = {}
    for es, a in p.items():
        e = [0]*dim
        e[0] = r-q
        a *= F(comb(r, q), 8**q)
        for n in es:
            e[n+1] += 1
            a *= factorial(2*n)
        add_term(out, tuple(e), a)
    return out


def entry(n, dim):
    if n < 0:
        return {}
    p = {}
    if n == 0:
        e = [0]*dim
        e[0] = 1
        add_term(p, tuple(e), F(1))
    e = [0]*dim
    e[n+1] = 1
    add_term(p, tuple(e), F(-1, 8))
    if n >= 1:
        e = [0]*dim
        e[n] = 1
        add_term(p, tuple(e), F(1, 8))
    return p


def direct_determinant(r, k, dim):
    out = {}
    for perm in permutations(range(r)):
        p = {(0,)*dim: F(sign(perm))}
        for i in range(r):
            p = mul(p, entry(k+perm[i]-i, dim))
        out = add(out, p)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = []
    for r in range(1, 6):
        for k in range(r+2):
            dim = k+r+1  # b and d0 through d_(k+r-1)
            t = probe(r, k)
            result = {}
            nonzero_faces = []
            for q in range(r+1):
                w = face_probe(t, r, q)
                if q < min(k, r):
                    assert not w, (r, k, q, 'unexpected boundary face')
                if k == 0:
                    assert w == {(0,)*q: F((-1)**q)}, (r, q)
                if w:
                    nonzero_faces.append(q)
                result = add(result, integrate(w, q, r, dim))
            assert result == direct_determinant(r, k, dim), (r, k)
            checks.append({'r': r, 'k': k,
                           'nonzero_face_dimensions': nonzero_faces,
                           'moment_polynomial_terms': len(result)})
    # Independent explicit r=2,k=1 probe formulas in powers of u^2,v^2.
    w1 = face_probe(probe(2, 1), 2, 1)
    assert w1 == {(1,): F(-1, 4), (2,): F(1, 48)}
    w2 = face_probe(probe(2, 1), 2, 2)
    assert w2 == {(0, 0): F(1), (1, 0): F(-1, 4),
                  (0, 1): F(-1, 4), (1, 1): F(1, 4),
                  (2, 0): F(-1, 48), (0, 2): F(-1, 48)}
    record = {
        'date': '2026-11-04', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker', 'llm_assistance': True,
        'model': 'gpt-6-astra', 'reasoning_effort': 'xhigh',
        'status': 'exact rational algebra checks passed',
        'scope': 'Polynomial identity and boundary factors only; no theta sign evidence',
        'coefficient_convention': 'c_n=b*delta_n0+(d_(n-1)-d_n)/8, d_negative=0; c_negative=0',
        'symbolic_boundary_constant': 'b; canonical theta b=1/16',
        'cases': checks, 'explicit_r2_k1_probes': 'passed',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.output:
        args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'status': record['status'], 'cases': len(checks),
                      'explicit_r2_k1_probes': 'passed'}))


if __name__ == '__main__':
    main()
