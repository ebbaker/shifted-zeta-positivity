#!/usr/bin/env python3
"""Exact finite controls for sharp anchored adjoint residuals.

Fraction arithmetic checks tree identities, disconnected sector payments,
the support geometry, and a common-zero control. These are finite algebra
checks, not verification of the imported heat-flow approximation theorem.
"""
import argparse
import hashlib
import json
import platform
from fractions import Fraction as F
from pathlib import Path

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
assertions = 0


def check(condition):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(f'Exact assertion {assertions} failed')


def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def conj(a):
    return (a[0], -a[1])


def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def scale(a, v):
    return (a[0]*v, a[1]*v)


def norm2(a):
    return a[0]*a[0]+a[1]*a[1]


def div(a, b):
    return scale(mul(a, conj(b)), 1/norm2(b))


def csum(values):
    total = ZERO
    for value in values:
        total = add(total, value)
    return total


def smallest_prime(n):
    for p in range(2, n+1):
        if n % p == 0:
            return p
    raise AssertionError('n must exceed one')


def parents(N, selected=None):
    result = {}
    for n in range(2, N+1):
        if selected is None:
            result[n] = n//smallest_prime(n)
        else:
            choices = [p for p in selected if n % p == 0]
            if choices:
                result[n] = n//min(choices)
    return result


def components(N, parent):
    groups = {}
    for n in range(1, N+1):
        m = n
        while m in parent:
            m = parent[m]
        groups.setdefault(m, []).append(n)
    return groups


def solve_tree(q, h, parent):
    """Solve B*lambda=h after the complex root balances have vanished."""
    N = len(q)-1
    accumulated = h.copy()
    lam = {}
    for n in range(N, 1, -1):
        if n not in parent:
            continue
        m = parent[n]
        lam[n] = accumulated[n]
        ratio = div(q[n], q[m])
        accumulated[m] = add(accumulated[m], mul(conj(ratio), lam[n]))
    for m in components(N, parent):
        check(accumulated[m] == ZERO)
    reconstructed = [ZERO for _ in q]
    for n, value in lam.items():
        m = parent[n]
        ratio = div(q[n], q[m])
        reconstructed[n] = add(reconstructed[n], value)
        reconstructed[m] = sub(reconstructed[m], mul(conj(ratio), value))
    for n in range(1, N+1):
        check(reconstructed[n] == h[n])
    return lam


def graph_controls():
    count_before = assertions
    for N in (2, 7, 24, 48):
        # Rational Pythagorean phases give exactly rational positive moduli.
        q = [ZERO]
        weights = [F(0)]
        for n in range(1, N+1):
            j = n % 5 + 1
            phase = (F(1-j*j, 1+j*j), F(2*j, 1+j*j))
            weight = F(1, n)
            q.append(scale(phase, weight))
            weights.append(weight)
            check(norm2(q[n]) == weight*weight)
        for selected in (None, (2, 3), (2,)):
            parent = parents(N, selected)
            groups = components(N, parent)
            for y1, y2 in ((F(0), F(0)), (F(2, 3), F(-4, 5)),
                           (F(-7, 4), F(3, 2)), (F(1), F(0))):
                gamma = [ZERO]
                for n in range(1, N+1):
                    ell, d, c, omega, L = F(n-1, 7), F(1, 37), F(1, 2), F(2, 5), F(3)
                    gamma.append((y1-d*ell*y2/L, (omega-c*ell)*y2/L))
                Z = {m: csum(mul(gamma[n], conj(q[n])) for n in nodes)
                     for m, nodes in groups.items()}
                z = -Z[1][1]
                r = [ZERO for _ in q]
                r[1] = scale(q[1], 1-Z[1][0])
                for m in groups:
                    if m != 1:
                        r[m] = div(neg(Z[m]), conj(q[m]))
                        check(weights[m]**2*norm2(r[m]) == norm2(Z[m]))
                b = [ZERO for _ in q]
                a = [ZERO for _ in q]
                b[1] = q[1]
                a[1] = mul((F(0), F(1)), q[1])
                h = [sub(sub(sub(b[n], gamma[n]), scale(a[n], z)), r[n])
                     for n in range(N+1)]
                solve_tree(q, h, parent)
                total_Z = csum(Z.values())
                observed = csum(mul(conj(gamma[n]), q[n]) for n in range(1, N+1))[0]
                check(observed == total_Z[0])
                check(weights[1]**2*norm2(r[1]) == (1-Z[1][0])**2)
                if selected is None:
                    check(len(groups) == 1)
                    check(weights[1]**2*norm2(r[1]) == (1-observed)**2)
                if selected == (2, 3):
                    check(all(m % 2 and m % 3 for m in groups))
    return assertions-count_before


def support(D, B):
    if D == 0 or B >= 2*D:
        return B
    return D+B*B/(4*D)


def geometry_controls():
    count_before = assertions
    for s in (F(-1), F(-3, 4), F(-1, 2), F(0), F(2, 3), F(1)):
        for sign in (-1, 1):
            v = sign*(1-s*s)
            normal = (2*s, F(sign) if v else F(0))
            h = support(abs(normal[1]), abs(normal[0]))
            check(h == 1+s*s)
            for gauge in (F(1, 4), F(1), F(3)):
                o = (gauge*s, gauge*v)
                # Squared equation defining the positive gauge, no float sqrt.
                check((2*gauge-abs(o[1]))**2 == o[1]**2+4*o[0]**2)
                y = (normal[0]/(gauge*h), normal[1]/(gauge*h))
                check(y[0]*o[0]+y[1]*o[1] == 1)
                check(support(abs(y[1]), abs(y[0])) == 1/gauge)
    # Each separate coordinate test permits this point; the curved body does not.
    s, v = F(4, 5), F(4, 5)
    check(abs(s) < 1 and abs(v) < 1)
    check(s*s+abs(v) > 1)
    return assertions-count_before


def failure_controls():
    count_before = assertions
    q = [ZERO, ONE, ONE, ONE]
    parent = parents(3)
    # Both observation rows annihilate this nonzero anchored state.
    C1 = [ZERO, ONE, neg(ONE), ZERO]
    C2 = [ZERO, ZERO, ONE, neg(ONE)]
    for y1, y2 in ((F(0), F(0)), (F(7), F(-3)), (F(-2), F(5))):
        gamma = [add(scale(C1[n], y1), scale(C2[n], y2)) for n in range(4)]
        check(csum(mul(gamma[n], conj(q[n])) for n in range(1, 4)) == ZERO)
        h = [neg(v) for v in gamma]
        solve_tree(q, h, parent)
        # Residual r=b has weighted cost exactly one; no strict witness exists.
        check(norm2(q[1]) == 1)
    # Disconnected-root costs cannot be dropped: positive real test state.
    N = 48
    groups = components(N, parents(N, (2, 3)))
    check(len(groups) > 1)
    for y in (F(-2), F(0), F(1, 20), F(3)):
        cost = abs(1-y*len(groups[1])) + abs(y)*(N-len(groups[1]))
        check(cost >= 1)
    return assertions-count_before


def main():
    global assertions
    assertions = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    counts = {'graph_and_forest': graph_controls(),
              'support_geometry': geometry_controls(),
              'failure_controls': failure_controls()}
    record = {'status': 'PASS', 'assertions': assertions, 'counts': counts,
              'date': '2026-10-10', 'prepared_for': 'Edward Baker',
              'model': 'GPT-6 (Codex)',
              'reasoning_effort': 'Active setting unavailable to this session; no level inferred',
              'acknowledgment': 'Substantial LLM assistance; internal finite algebra checks, not independent mathematical validation',
              'arithmetic': 'exact fractions; complex numbers are rational pairs',
              'scope': 'finite algebra, explicit tree reconstruction, disconnected root payments and candidate support controls; no heat-flow analytical input certified',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python_version': platform.python_version()}
    args.record.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()
