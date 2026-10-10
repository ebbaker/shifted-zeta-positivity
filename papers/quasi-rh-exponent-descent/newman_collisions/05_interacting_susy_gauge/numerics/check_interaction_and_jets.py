"""Exact coefficient and derivative algebra; no zero-free certificate."""
from fractions import Fraction as F

def add(*polys):
    n = max(map(len, polys))
    out = [F(0)] * n
    for p in polys:
        for k, v in enumerate(p):
            out[k] += v
    return trim(out)

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def scale(p, s):
    return trim([s*v for v in p])

def mul(p, q):
    out = [F(0)] * (len(p)+len(q)-1)
    for j, a in enumerate(p):
        for k, b in enumerate(q):
            out[j+k] += a*b
    return trim(out)

def power(p, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, p)
    return out

def derivative(p):
    return trim([F(k)*p[k] for k in range(1, len(p))] or [F(0)])

A = [F(1, 3), F(2, 5), F(-3, 7), F(1, 11), F(2, 13)]
d1 = derivative(A)
d2, d3 = derivative(d1), derivative(derivative(d1))
d4 = derivative(d3)
expected = [
    [F(1)], d1, add(d2, power(d1, 2)),
    add(d3, scale(mul(d1, d2), 3), power(d1, 3)),
    add(d4, scale(mul(d1, d3), 4), scale(power(d2, 2), 3),
        scale(mul(power(d1, 2), d2), 6), power(d1, 4)),
]
current = [F(1)]
for j in range(5):
    assert current == expected[j], j
    current = add(derivative(current), mul(d1, current))

cases = 0
for t in (F(1, 25), F(1, 20)):
    for l2, l3 in ((F(2, 3), F(7, 6)), (F(3, 4), F(5, 4))):
        sigma = F(3, 5)
        def log_weight(a, b):
            ell = a*l2+b*l3
            return t*ell*ell/4-sigma*ell
        for a in range(2):
            for b in range(2):
                mixed = (log_weight(a+1, b+1)+log_weight(a, b)
                         -log_weight(a+1, b)-log_weight(a, b+1))
                assert mixed == t*l2*l3/2
                cases += 1
print(f"PASS: 5 exponential jet polynomials and {cases} mixed-difference cases.")
