#!/usr/bin/env python3
"""Exact geometry of paid coherent current tests; no arithmetic sign claim."""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

checks = 0


def check(condition):
    global checks
    assert condition, checks+1
    checks += 1


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def sign(x):
    return (x > 0)-(x < 0)


def cmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def cconj(a):
    return (a[0], -a[1])


# Sharp distance of determinant line to the paid error square.
for a in itertools.product((F(-3), F(-1, 2), F(0), F(2, 3)), repeat=2):
    if a == (0, 0):
        continue
    norm2 = dot(a, a)
    for eps in (F(0), F(1, 7), F(2)):
        support = eps*sum(abs(x) for x in a)
        for j in (F(-5), F(-1, 8), F(0), F(2, 9), F(7)):
            excess = max(abs(j)-support, F(0))
            if excess:
                delta = tuple(sign(j)*eps*sign(x) for x in a)
                residual = tuple(sign(j)*excess*x/norm2 for x in a)
                obs = tuple(x+y for x, y in zip(delta, residual))
            else:
                delta = tuple(j*sign(x)/sum(abs(v) for v in a) for x in a)
                residual = (F(0), F(0))
                obs = delta
            check(all(abs(x) <= eps for x in delta))
            check(dot(a, obs) == j)
            check(dot(residual, residual)*norm2 == excess**2)
            # Other compatible observable vectors and all square corners
            # cannot beat the attained lower norm.
            for tangent in (F(-2), F(0), F(3, 5)):
                other = (obs[0]+tangent*a[1], obs[1]-tangent*a[0])
                for corner in itertools.product((-eps, eps), repeat=2):
                    truehalf = tuple(x-y for x, y in zip(other, corner))
                    check(dot(truehalf, truehalf)*norm2 >= excess**2)


# Phase-invariant spectrum and exact minimum max-coordinate floor.
matrix_count = 0
for raw in itertools.product(range(-3, 4), repeat=4):
    u, v, p, q = map(F, raw)  # p=u'/L, q=v'/L.
    det = u*q-v*p
    if not det:
        continue
    matrix_count += 1
    trace = u*u+v*v+p*p+q*q
    rowdot = u*p+v*q
    discriminant = trace**2-4*det**2
    check(discriminant == (u*u+v*v-p*p-q*q)**2+4*rowdot**2)
    reflected = (u*u-v*v+p*p-q*q, 2*(u*v+p*q))
    check(trace**2-dot(reflected, reflected) == 4*det**2)
    check((trace+reflected[0])/2 == u*u+p*p)
    denominator = trace+2*abs(rowdot)
    floor2 = det**2/denominator
    # The maximizing inverse-Gram corner has opposite signs when rowdot>0.
    sigma = (F(1), F(-sign(rowdot) or 1))
    preimage = ((q*sigma[0]-v*sigma[1])/det,
                (-p*sigma[0]+u*sigma[1])/det)
    check(floor2*dot(preimage, preimage) == 1)
    # All rational carrier rotations satisfy the sharp floor.
    for a, b in ((1, 0), (1, 1), (2, 1), (-3, 2), (1, -4)):
        cosine, sine = F(a*a-b*b, a*a+b*b), F(2*a*b, a*a+b*b)
        first, second = u*cosine-v*sine, p*cosine-q*sine
        check(max(first**2, second**2) >= floor2)


# Exact centered arithmetic cross-feed, including real amplitude drift.
for k in range(1, 50):
    A, c, d = F(k-25, 11), F(k+1, 13), F(7-k, 17)
    m0, m1 = (F(k-9, 5), F(23-k, 7)), (F(2*k-31, 19), F(k+3, 23))
    sp = tuple(x+y for x, y in zip(cmul((A, 0), m0), cmul((-d, c), m1)))
    current = -cmul(sp, cconj(m0))[1]
    mixed = cmul(m1, cconj(m0))
    check(current == -c*mixed[0]+d*mixed[1])
    check(current == sp[0]*m0[1]-m0[0]*sp[1])


# Ordered-pair current kernel is purely the difference-phase channel.
for size in range(1, 12):
    phases = [(F(n*n-1, n*n+1), F(2*n, n*n+1)) for n in range(1, size+1)]
    weights = [F(1, n+1) for n in range(1, size+1)]
    rho = [F(n-7, 5) for n in range(1, size+1)]
    c, d = F(5, 7), F(2, 11)
    m0 = tuple(sum((w*z[j] for w, z in zip(weights, phases)), F(0)) for j in (0, 1))
    m1 = tuple(sum((w*r*z[j] for w, r, z in zip(weights, rho, phases)), F(0)) for j in (0, 1))
    mixed = cmul(m1, cconj(m0))
    current = -c*mixed[0]+d*mixed[1]
    pair = F(0)
    for n in range(size):
        for m in range(size):
            phase = cmul(phases[n], cconj(phases[m]))
            h, difference = rho[n]+rho[m], rho[n]-rho[m]
            pair += weights[n]*weights[m]*(-c*h*phase[0]/2+d*difference*phase[1]/2)
    check(pair == current)

source = Path(__file__)
print(json.dumps({
    'status': 'PASS',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'assertions_passed': checks,
    'nonsingular_integer_matrices_checked': matrix_count,
    'families': ['sharp paid determinant-line distance and attaining errors',
                 'phase-invariant discriminant and sharp square extremizer',
                 'rational constant carrier rotations',
                 'centered current with actual amplitude-drift algebra',
                 'complete ordered-pair difference-current kernel'],
    'scope': 'Exact finite geometry/algebra checks, no genuine current lower bound or independent mathematical validation.'
}, indent=2, sort_keys=True))
