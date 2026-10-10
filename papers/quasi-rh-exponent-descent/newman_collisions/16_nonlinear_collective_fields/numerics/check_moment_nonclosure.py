"""Exact positive-density perturbation invisible to four low moments.

P6 on [-1,1] is orthogonal to 1,u^2,u^4 and visible to u^6. This is a
finite integral witness, not a perturbation of the genuine theta state.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

p6 = {6: F(231, 16), 4: F(-315, 16), 2: F(105, 16), 0: F(-5, 16)}


def integral_monomial(power):
    return F(0) if power % 2 else F(2, power + 1)


def pairing(power):
    return sum((c * integral_monomial(power + k) for k, c in p6.items()), F(0))


assert [pairing(k) for k in (0, 2, 4)] == [0, 0, 0]
assert pairing(6) == F(32, 3003)
# Crude coefficient-sum bound guarantees 1 +/- epsilon*P6 >=1/2.
epsilon = F(1, 100)
assert epsilon * sum(abs(c) for c in p6.values()) < F(1, 2)
record = {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "pairings": {str(k): str(pairing(k)) for k in (0, 2, 4, 6)}, "epsilon": str(epsilon), "sixth_moment_separation_between_densities": str(epsilon * pairing(6)), "scope": "Exact low-moment nonclosure control on two positive compactly supported densities; no theta-specific exclusion."}
path = Path(__file__).with_name('moment_nonclosure_record_20261010.json')
path.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps({"passed": 5, "record": path.name}))
