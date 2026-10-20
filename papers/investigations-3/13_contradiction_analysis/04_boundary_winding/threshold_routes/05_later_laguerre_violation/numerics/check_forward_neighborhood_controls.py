#!/usr/bin/env python3
"""Exact rational controls for the 20 October local forward-neighborhood note.

Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
reasoning effort ultra. Standard library only. These polynomial controls
check the algebra and stated margins, not a theta event or arithmetic gain.
Run without arguments for stdout, or with --output PATH for a small receipt.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def clean(p):
    return {ij: F(c) for ij, c in p.items() if c}


def add(p, q):
    out = dict(p)
    for ij, c in q.items():
        out[ij] = out.get(ij, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({ij: c * x for ij, x in p.items()})


def mul(p, q):
    out = {}
    for (i, j), c in p.items():
        for (k, ell), d in q.items():
            ij = (i + k, j + ell)
            out[ij] = out.get(ij, F(0)) + c * d
    return clean(out)


def diff(p, axis):
    out = {}
    for ij, c in p.items():
        if ij[axis]:
            key = list(ij)
            key[axis] -= 1
            out[tuple(key)] = c * ij[axis]
    return clean(out)


def dy(p, k):
    for _ in range(k):
        p = diff(p, 1)
    return p


def at(p, s, y):
    return sum((c * s**i * y**j for (i, j), c in p.items()), F(0))


def envelope(p, sigma, r):
    # Triangle inequality on every complex |y|<=r and real 0<=s<=sigma.
    return sum((abs(c) * sigma**i * r**j for (i, j), c in p.items()), F(0))


def K(alpha, beta):
    return (4*alpha + F(3, 8)*beta + F(3, 4)*alpha**2
            + (alpha + beta/8)*(alpha + beta/4))


def C(alpha, beta):
    return F(5, 12)*alpha + beta/32


def examine(name, p, r, small_expected, scalar_expected, circle_expected):
    assert not add(diff(p, 0), dy(p, 2)), name + ': heat PDE'
    assert at(p, F(0), F(0)) == 0
    assert at(dy(p, 1), F(0), F(0)) == 0
    h = at(dy(p, 2), F(0), F(0))
    assert h != 0
    sigma = r*r/4
    m3 = envelope(dy(p, 3), sigma, r)
    m4 = envelope(dy(p, 4), sigma, r)
    alpha, beta = m3*r/abs(h), m4*r*r/abs(h)
    small = alpha <= F(1, 16) and beta <= F(1, 4)
    scalar, circle = K(alpha, beta) < 1, C(alpha, beta) < F(1, 4)
    assert (small, scalar, circle) == (small_expected, scalar_expected, circle_expected)
    q = {(0, 2): F(1, 2), (1, 0): F(-1)}
    remainders = [add(p, scale(q, -h)),
                  add(dy(p, 1), {(0, 1): -h}),
                  add(dy(p, 2), {(0, 0): -h})]
    budgets = [m3*(r**3/6 + sigma*r) + m4*sigma**2/2,
               m3*(r*r/2 + sigma), m3*r + m4*sigma]
    for rem, budget in zip(remainders, budgets):
        assert envelope(rem, sigma, r) <= budget
    laguerre = add(mul(dy(p, 1), dy(p, 1)), scale(mul(p, dy(p, 2)), -1))
    assert at(laguerre, 0, 0) == 0
    assert at(diff(laguerre, 0), 0, 0) == h*h
    if circle:
        assert at(p, sigma, 0)/h < 0
        assert at(p, sigma, r)/h > 0
        assert at(p, sigma, -r)/h > 0
    if small:
        assert K(alpha, beta) <= F(367, 1024)
        assert C(alpha, beta) <= F(13, 384)
    return {'name': name, 'radius': str(r), 'time_gap_upper': str(sigma),
            'h': str(h), 'M3_complex': str(m3), 'M4_complex': str(m4),
            'alpha': str(alpha), 'beta': str(beta),
            'K': str(K(alpha, beta)), 'scalar_margin_factor': str(1-K(alpha, beta)),
            'C': str(C(alpha, beta)), 'circle_margin_factor': str(F(1, 4)-C(alpha, beta)),
            'small_contract': small, 'scalar_contract': scalar,
            'complex_pair_contract': circle, 'outcome': 'matches declared expectation'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    assert K(F(1, 16), F(1, 4)) == F(367, 1024)
    assert 1-K(F(1, 16), F(1, 4)) == F(657, 1024)
    assert C(F(1, 16), F(1, 4)) == F(13, 384)
    assert F(1, 4)-C(F(1, 16), F(1, 4)) == F(83, 384)
    eta = F(1, 16) + F(1, 4)/8
    assert 2*(1-eta)/(1+eta) == F(58, 35)
    assert 2*(1+eta)/(1-eta) == F(70, 29)

    quadratic = {(0, 2): F(1, 2), (1, 0): F(-1)}
    # P(T+s,1+y), where P(T,z)=(z^2-1)^2 and T=1/4.
    quartic = {(0, 4): F(1), (0, 3): F(4), (0, 2): F(4),
               (1, 2): F(-12), (1, 1): F(-24), (1, 0): F(-8), (2, 0): F(12)}
    # e^(-s d_y^2)[y^2(1+y^2)/2], locally double with other nonreal zeros.
    mixed = {(0, 4): F(1, 2), (0, 2): F(1, 2), (1, 2): F(-6),
             (1, 0): F(-1), (2, 0): F(6)}
    controls = [examine('quadratic', quadratic, F(1, 8), True, True, True),
                examine('negative_quadratic', scale(quadratic, -1), F(1, 8), True, True, True),
                examine('threshold_quartic', quartic, F(1, 64), True, True, True),
                examine('negative_threshold_quartic', scale(quartic, -1), F(1, 64), True, True, True),
                examine('large_radius_quartic_scalar_inconclusive', quartic, F(1, 8), False, False, True),
                examine('mixed_zero_quartic_local_only', mixed, F(1, 16), True, True, True)]

    # Exact quadratic-in-y^2 sign check: product of the two y^2 roots is
    # negative, proving one real pair and one imaginary pair at this time.
    mixed_s = F(1, 16)**2/4
    mixed_constant = -mixed_s + 6*mixed_s**2
    assert mixed_constant < 0
    mixed_discriminant = (F(1, 2)-6*mixed_s)**2 - 2*mixed_constant
    assert mixed_discriminant > 0
    # The theorem places the real pair in the small disk, so the imaginary
    # pair must be outside it. No global all-real claim is permitted.
    cubic = {(0, 3): F(1), (1, 1): F(-6)}
    assert not add(diff(cubic, 0), dy(cubic, 2))
    assert at(dy(cubic, 2), 0, 0) == 0
    # Center event and backward time cannot pass a strictly-later contract.
    assert at(quadratic, 0, 0) == at(dy(quadratic, 1), 0, 0) == 0
    backward_s = -F(1, 100)
    assert backward_s < 0 and 2*backward_s < 0

    script = Path(__file__).resolve()
    route_root = script.parents[2]
    note_paths = sorted(route_root.glob('0[2345]_*/notes/02_*20261020.md'))
    assert len(note_paths) == 4, 'Expected the four route-specific source notes'
    note_hashes = {str(path.relative_to(route_root)): hashlib.sha256(path.read_bytes()).hexdigest()
                   for path in note_paths}
    record = {'date': '2026-10-20', 'prepared_for': 'Edward Baker',
              'model': 'gpt-6-astra', 'reasoning_effort': 'ultra',
              'arithmetic': 'Python standard-library exact fractions; no floating point',
              'status': 'exact polynomial control replay passed',
              'scope': 'Local double-event algebra and derivative-envelope margins only; no theta event or arithmetic sign certificate.',
              'source_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
              'source_notes_sha256': note_hashes,
              'constants': {'K_upper': '367/1024', 'Laguerre_lower_factor': '657/1024',
                            'circle_error_upper': '13/384', 'circle_margin_lower': '83/384',
                            'root_squared_lower_over_s': '58/35', 'root_squared_upper_over_s': '70/29'},
              'controls': controls,
              'rejections': ['h=0 cubic event outside exact-double contract',
                             's=0 center has no strict forward margin',
                             's<0 backward imaginary pair outside later-time contract'],
              'mixed_zero_control': {'time_gap': str(mixed_s), 'constant_in_y_squared': str(mixed_constant),
                                     'discriminant': str(mixed_discriminant),
                                     'conclusion': 'two real local roots and two imaginary roots outside the certified disk'},
              'limitations': ['The complex derivative bounds are own-polynomial bounds.',
                              'No numerical theta source tail or hypothetical event was evaluated.',
                              'Review remains internal LLM review; no specialist review.']}
    serialized = json.dumps(record, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(serialized)
        print('Exact local controls passed; receipt written to ' + str(args.output))
    else:
        print(serialized, end='')


if __name__ == '__main__':
    main()
