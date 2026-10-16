"""Exact finite Calogero--Moser determinant and quartic heat checks.

Uses only the Python standard library. This checks finite identities, not a
matrix realization of the genuine entire theta heat function.
"""
from fractions import Fraction as F
from itertools import permutations
import hashlib
import json
from pathlib import Path


def add(a, b):
    c = dict(a)
    for key, value in b.items():
        c[key] = c.get(key, F(0)) + value
    return {key: value for key, value in c.items() if value}


def mul(a, b):
    c = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            c[key] = c.get(key, F(0)) + x * y
    return {key: value for key, value in c.items() if value}


roots = list(map(F, [-3, -1, 1, 3]))
matrix = []
for i, ri in enumerate(roots):
    row = []
    for j, rj in enumerate(roots):
        cij = sum((1 / (ri - rk) for k, rk in enumerate(roots) if k != i), F(0)) if i == j else 1 / (ri - rj)
        entry = {(0, 1): -2 * cij}
        if i == j:
            entry = add(entry, {(1, 0): F(1), (0, 0): -ri})
        row.append(entry)
    matrix.append(row)
det = {}
for p in permutations(range(4)):
    sign = (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
    term = {(0, 0): F(sign)}
    for i in range(4):
        term = mul(term, matrix[i][p[i]])
    det = add(det, term)
expected = {(4, 0): F(1), (2, 0): F(-10), (0, 0): F(9), (2, 1): F(-12), (0, 1): F(20), (0, 2): F(12)}
assert det == expected

def evaluate(p, z, tau):
    return sum(c * z ** i * tau ** j for (i, j), c in p.items())


threshold = F(-2, 3)
assert evaluate(det, F(1), threshold) == 0
dz = {(i - 1, j): c * i for (i, j), c in det.items() if i}
assert evaluate(dz, F(1), threshold) == 0
d2 = {(i - 2, j): c * i * (i - 1) for (i, j), c in det.items() if i >= 2}
dt = {(i, j - 1): c * j for (i, j), c in det.items() if j}
assert add(dt, d2) == {}
assert evaluate(d2, F(1), threshold) == 8
source = Path(__file__)
record = {
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "checks": ["exact bivariate 4 by 4 determinant", "backward heat equation", "threshold value", "threshold derivative", "nonzero second derivative"],
    "determinant_coefficients_z_tau": {f"{i},{j}": str(c) for (i, j), c in sorted(det.items())},
    "threshold_relative_time": str(threshold),
    "scope": "Exact rational polynomial model; not theta collision exclusion.",
}
target = source.with_name("matrix_heat_record_20261010.json")
target.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({"passed": len(record["checks"]), "record": target.name}))
