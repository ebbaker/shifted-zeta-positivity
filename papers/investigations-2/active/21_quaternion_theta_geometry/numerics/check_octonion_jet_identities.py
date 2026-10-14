#!/usr/bin/env python3
"""Exact algebra checks for investigation 21's octonionic four-jet proposal.

Prepared for Edward Baker, 2026-10-14, with LLM assistance.
Recorded model: gpt-6-astra; effort: ultra (provided in this research run).

Only Python's standard library is required. All identities are expanded in a
sparse polynomial ring over the rationals; no floating-point tolerances occur.
This is a reproducible computational check, not a proof-assistant certificate,
an analytic estimate, or a proof of any theta-specific positivity assertion.

Convention: (a,b) denotes a + ell*b, and
  (a,b)*(c,d) = (a*c - d*conj(b), conj(a)*d + c*b).
The inner algebra is Hamilton's quaternions, with i*j=k and j*i=-k.
Consequently h_m + j*h_{m+1}, for h_m=a_m+i*b_m, has coordinates
  (a_m, b_m, a_{m+1}, -b_{m+1}).

Usage: python3 check_octonion_jet_identities.py --output small_record.json
The output is required; any failed check or unexpected exception gives a
nonzero exit status and a failing record. The source SHA256 binds the record
to the exact checker bytes. It does not validate mathematical conclusions.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
import sys


class Poly:
    """Sparse Q-polynomial; monomials are sorted tuples of variable names."""

    def __init__(self, terms=None):
        self.terms = {
            tuple(sorted(m)): Fraction(c)
            for m, c in (terms or {}).items()
            if c
        }

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({(): Fraction(value)})

    @staticmethod
    def variable(name):
        return Poly({(name,): Fraction(1)})

    def __add__(self, other):
        other = self.coerce(other)
        terms = self.terms.copy()
        for m, c in other.terms.items():
            terms[m] = terms.get(m, Fraction(0)) + c
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        other = self.coerce(other)
        terms = {}
        for m, c in self.terms.items():
            for n, d in other.terms.items():
                product = tuple(sorted(m + n))
                terms[product] = terms.get(product, Fraction(0)) + c * d
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("Only nonnegative integer powers are supported")
        result = self.coerce(1)
        for _ in range(power):
            result *= self
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def derivative(self, name):
        terms = {}
        for m, c in self.terms.items():
            degree = m.count(name)
            if degree:
                reduced = list(m)
                reduced.remove(name)
                reduced = tuple(reduced)
                terms[reduced] = terms.get(reduced, Fraction(0)) + degree * c
        return Poly(terms)

    def substitute(self, values):
        result = self.coerce(0)
        for m, c in self.terms.items():
            term = self.coerce(c)
            for name in m:
                term *= values.get(name, self.variable(name))
            result += term
        return result

    def evaluate(self, values):
        result = Fraction(0)
        for m, c in self.terms.items():
            term = c
            for name in m:
                term *= Fraction(values[name])
            result += term
        return result

    def __str__(self):
        if not self.terms:
            return "0"
        pieces = []
        for m, c in sorted(self.terms.items(), key=lambda item: (len(item[0]), item[0])):
            counts = Counter(m)
            monomial = "*".join(
                name if degree == 1 else f"{name}^{degree}"
                for name, degree in sorted(counts.items())
            )
            magnitude = abs(c)
            body = monomial if magnitude == 1 and monomial else str(magnitude)
            if monomial and magnitude != 1:
                body += "*" + monomial
            if pieces:
                pieces.append((" + " if c > 0 else " - ") + body)
            else:
                pieces.append(("" if c > 0 else "-") + body)
        return "".join(pieces)


ZERO = Poly.coerce(0)
ONE = Poly.coerce(1)
QZERO = (ZERO,) * 4
QONE = (ONE, ZERO, ZERO, ZERO)


def vector_add(a, b):
    return tuple(x + y for x, y in zip(a, b, strict=True))


def vector_neg(a):
    return tuple(-x for x in a)


def vector_sub(a, b):
    return vector_add(a, vector_neg(b))


def vector_scale(s, a):
    return tuple(s * x for x in a)


def qconj(a):
    return (a[0], -a[1], -a[2], -a[3])


def qmul(a, b):
    ar, ai, aj, ak = a
    br, bi, bj, bk = b
    return (
        ar * br - ai * bi - aj * bj - ak * bk,
        ar * bi + ai * br + aj * bk - ak * bj,
        ar * bj - ai * bk + aj * br + ak * bi,
        ar * bk + ai * bj - aj * bi + ak * br,
    )


def qnorm(a):
    return sum((x * x for x in a), ZERO)


def embed(a):
    return a + QZERO


def omul(a, b):
    aa, ab = a[:4], a[4:]
    ba, bb = b[:4], b[4:]
    return vector_sub(qmul(aa, ba), qmul(bb, qconj(ab))) + vector_add(
        qmul(qconj(aa), bb), qmul(ba, ab)
    )


def oconj(a):
    return qconj(a[:4]) + vector_neg(a[4:])


def onorm(a):
    return sum((x * x for x in a), ZERO)


def associator(a, b, c):
    return vector_sub(omul(omul(a, b), c), omul(a, omul(b, c)))


def commutator(a, b):
    return vector_sub(qmul(a, b), qmul(b, a))


def basis(n, index):
    return tuple(ONE if k == index else ZERO for k in range(n))


def generic(n, prefix):
    return tuple(Poly.variable(f"{prefix}{k}") for k in range(n))


def at(a, substitutions):
    return tuple(p.substitute(substitutions) for p in a)


def dvector(a, variable):
    return tuple(p.derivative(variable) for p in a)


def jet_derivative(poly, direction):
    """Derive using the stipulated Fueter-lift jet recurrence.

    x0: h_m -> h_(m+1); x1: h_m -> i*h_(m+1);
    x2 and t: h_m -> -h_(m+2); x3: h_m -> -i*h_(m+2).
    The coefficient variables r_mu are independent of these four directions.
    """
    result = ZERO
    names = {name for monomial in poly.terms for name in monomial}
    for name in names:
        if len(name) < 2 or name[0] not in "ab" or not name[1:].isdigit():
            continue
        index = int(name[1:])
        shift = 1 if direction in ("x0", "x1") else 2
        real_next = Poly.variable(f"a{index + shift}")
        imag_next = Poly.variable(f"b{index + shift}")
        if direction == "x0":
            coefficient = real_next if name[0] == "a" else imag_next
        elif direction == "x1":
            coefficient = -imag_next if name[0] == "a" else real_next
        elif direction in ("x2", "t"):
            coefficient = -real_next if name[0] == "a" else -imag_next
        elif direction == "x3":
            coefficient = imag_next if name[0] == "a" else -real_next
        else:
            raise ValueError(f"Unknown jet derivative direction {direction}")
        result += poly.derivative(name) * coefficient
    return result


def jet_dvector(a, direction):
    return tuple(jet_derivative(p, direction) for p in a)


def quaternion_dirac(a, conjugate=False):
    result = QZERO
    for mu in range(4):
        unit = basis(4, mu)
        if conjugate:
            unit = qconj(unit)
        result = vector_add(result, qmul(unit, jet_dvector(a, f"x{mu}")))
    return result


def octonion_dirac(o):
    """Standard left operator sum e_mu*d_mu in the declared basis."""
    a, b = o[:4], o[4:]
    first = quaternion_dirac(a)
    second = quaternion_dirac(b, conjugate=True)
    for mu in range(4):
        unit = basis(4, mu)
        first = vector_sub(first, qmul(dvector(b, f"r{mu}"), qconj(unit)))
        second = vector_add(second, qmul(dvector(a, f"r{mu}"), unit))
    return first + second


def octonion_dirac_direct(o):
    """Independently assemble sum e_mu*d_mu by octonion multiplication."""
    result = (ZERO,) * 8
    for mu in range(4):
        result = vector_add(result, omul(basis(8, mu), jet_dvector(o, f"x{mu}")))
        result = vector_add(result, omul(basis(8, mu + 4), dvector(o, f"r{mu}")))
    return result


class Checks:
    def __init__(self):
        self.counts = Counter()
        self.failures = []

    def check(self, group, name, condition):
        self.counts[group] += 1
        if not condition:
            self.failures.append({"group": group, "check": name})

    def equal(self, group, name, left, right):
        self.check(group, name, left == right)


def run_checks(checks):
    x, y, t, a, T, epsilon = (
        Poly.variable(name) for name in ("x", "y", "t", "a", "T", "epsilon")
    )
    checks.equal("arithmetic_kernel", "binomial expansion", (x + y) ** 3,
                 x ** 3 + 3 * x ** 2 * y + 3 * x * y ** 2 + y ** 3)
    checks.equal("arithmetic_kernel", "exact rational cancellation",
                 Fraction(1, 3) * x + Fraction(2, 3) * x, x)
    checks.equal("arithmetic_kernel", "partial derivative", (x ** 2 * y).derivative("x"), 2 * x * y)
    checks.equal("arithmetic_kernel", "polynomial substitution", (x * y).substitute({"x": y + 1}), y ** 2 + y)
    checks.equal("arithmetic_kernel", "rational evaluation", (Fraction(2, 3) * x ** 2 + y).evaluate({"x": Fraction(3, 2), "y": -1}), Fraction(1, 2))
    probe = Checks()
    probe.check("probe", "intentional failure", False)
    checks.check("arithmetic_kernel", "failed checks are recorded", len(probe.failures) == 1)

    qi, qj, qk = (basis(4, n) for n in (1, 2, 3))
    for n, unit in enumerate((qi, qj, qk), start=1):
        checks.equal("hamilton_convention", f"imaginary basis square {n}", qmul(unit, unit), vector_neg(QONE))
    for u, v, w, name in ((qi, qj, qk, "ij=k"), (qj, qk, qi, "jk=i"), (qk, qi, qj, "ki=j")):
        checks.equal("hamilton_convention", name, qmul(u, v), w)
        checks.equal("hamilton_convention", "reverse " + name, qmul(v, u), vector_neg(w))
    qa, qb = generic(4, "qa"), generic(4, "qb")
    checks.equal("hamilton_convention", "conjugation reverses product", qconj(qmul(qa, qb)), qmul(qconj(qb), qconj(qa)))
    checks.equal("hamilton_convention", "quaternion norm identity", qmul(qa, qconj(qa)), (qnorm(qa), ZERO, ZERO, ZERO))

    ounits = tuple(basis(8, n) for n in range(8))
    oone, oi, oj, ok, ell = ounits[:5]
    ozero = (ZERO,) * 8
    for n, unit in enumerate(ounits):
        checks.equal("octonion_algebra", f"left unit basis {n}", omul(oone, unit), unit)
        checks.equal("octonion_algebra", f"right unit basis {n}", omul(unit, oone), unit)
        if n:
            checks.equal("octonion_algebra", f"imaginary basis square {n}", omul(unit, unit), vector_neg(oone))
    checks.equal("octonion_algebra", "ell times embedded q", omul(ell, embed(qa)), QZERO + qa)
    checks.equal("octonion_algebra", "q times ell", omul(embed(qa), ell), QZERO + qconj(qa))
    oa, ob = generic(8, "oa"), generic(8, "ob")
    checks.equal("octonion_algebra", "symbolic conjugation reverses product", oconj(omul(oa, ob)), omul(oconj(ob), oconj(oa)))
    checks.equal("octonion_algebra", "symbolic conjugate norm product", omul(oa, oconj(oa)), (onorm(oa),) + (ZERO,) * 7)
    checks.equal("octonion_algebra", "symbolic norm multiplicativity (16 independent variables)", onorm(omul(oa, ob)), onorm(oa) * onorm(ob))
    checks.equal("octonion_algebra", "symbolic left alternativity", associator(oa, oa, ob), ozero)
    checks.equal("octonion_algebra", "symbolic right alternativity", associator(oa, ob, ob), ozero)
    checks.equal("octonion_algebra", "symbolic flexibility", associator(oa, ob, oa), ozero)
    checks.equal("octonion_algebra", "nonassociative basis sign [i,j,ell]=-2ell*k", associator(oi, oj, ell), vector_scale(-2, QZERO + qk))
    checks.check("octonion_algebra", "nonassociative witness is nonzero", associator(oi, oj, ell) != ozero)
    checks.equal("octonion_algebra", "arbitrary quaternion associator identity", associator(embed(qa), embed(qb), ell), QZERO + qconj(commutator(qa, qb)))

    # This is a separate rational evaluation exercise, in addition to the
    # complete polynomial identity above; the seed and sample count are fixed.
    rng = random.Random(20261014)
    for sample in range(24):
        rational_a = tuple(Poly.coerce(Fraction(rng.randint(-7, 7), rng.randint(1, 5))) for _ in range(8))
        rational_b = tuple(Poly.coerce(Fraction(rng.randint(-7, 7), rng.randint(1, 5))) for _ in range(8))
        checks.equal("rational_samples", f"norm product sample {sample}", onorm(omul(rational_a, rational_b)), onorm(rational_a) * onorm(rational_b))

    # The physically used four directions are closed and associative.
    physical_basis = (oone, oj, ell, QZERO + qj)
    physical_indices = {0, 2, 4, 6}
    for i, u in enumerate(physical_basis):
        for j, v in enumerate(physical_basis):
            uv = omul(u, v)
            checks.check("physical_subalgebra", f"closure {i},{j}", all(uv[k] == 0 for k in range(8) if k not in physical_indices))
            for k, w in enumerate(physical_basis):
                checks.equal("physical_subalgebra", f"associativity {i},{j},{k}", associator(u, v, w), ozero)

    avars = tuple(Poly.variable(f"a{k}") for k in range(7))
    bvars = tuple(Poly.variable(f"b{k}") for k in range(7))
    complex_jets = tuple((avars[k], bvars[k], ZERO, ZERO) for k in range(7))
    G = tuple(vector_add(complex_jets[k], qmul(qj, complex_jets[k + 1])) for k in range(6))
    for k in range(3):
        checks.equal("complex_jet_packaging", f"complex jet coordinates G{k}", G[k], (avars[k], bvars[k], avars[k + 1], -bvars[k + 1]))
    doubled = G[0] + G[2]
    checks.equal("complex_jet_packaging", "doubled norm retains all eight scalar squares", onorm(doubled), sum((avars[k] ** 2 + bvars[k] ** 2 for k in range(4)), ZERO))
    checks.equal("complex_jet_packaging", "projection retains collision norm", qnorm(doubled[:4]), qnorm(G[0]))
    jet_associator = associator(embed(G[0]), embed(G[1]), ell)
    checks.equal("complex_jet_packaging", "complex jet associator", jet_associator, QZERO + qconj(commutator(G[0], G[1])))
    expected_commutator = (
        ZERO,
        2 * (avars[2] * bvars[1] - avars[1] * bvars[2]),
        2 * (bvars[0] * bvars[2] - bvars[1] ** 2),
        2 * (bvars[0] * avars[2] - avars[1] * bvars[1]),
    )
    checks.equal("complex_jet_packaging", "expanded commutator coordinates", commutator(G[0], G[1]), expected_commutator)

    real_substitution = {f"b{k}": ZERO for k in range(7)}
    P = tuple(at(g, real_substitution) for g in G)
    h0, h1, h2, h3 = avars[:4]
    L0, L1 = h1 ** 2 - h0 * h2, h2 ** 2 - h1 * h3
    N = h0 ** 2 + h1 ** 2
    for j, laguerre in enumerate((L0, L1)):
        expected_real = avars[j] * avars[j + 1] + avars[j + 1] * avars[j + 2]
        checks.equal("physical_jet_identities", f"signed adjacent product {j}", qmul(qconj(P[j]), P[j + 1]), (expected_real, ZERO, -laguerre, ZERO))
    mixed = h0 * h3 - h1 * h2
    checks.equal("physical_jet_identities", "mixed signed product", qmul(qconj(P[0]), P[2]), (h0 * h2 + h1 * h3, ZERO, mixed, ZERO))
    energy_velocity = -2 * qmul(qconj(P[0]), P[2])[0]
    checks.equal("physical_jet_identities", "stationary H energy derivative", energy_velocity.substitute({"a1": ZERO}), (2 * L0).substitute({"a1": ZERO}))
    checks.equal("physical_jet_identities", "stationary H_x energy derivative", energy_velocity.substitute({"a2": ZERO}), (2 * L1).substitute({"a2": ZERO}))
    checks.equal("physical_jet_identities", "physical associator vanishes", at(jet_associator, real_substitution), ozero)
    checks.equal("physical_jet_identities", "physical doubled norm", onorm(P[0] + P[2]), sum((h * h for h in avars[:4]), ZERO))

    # Fixed right multipliers i and k move the plane-valued fields into
    # different quaternion directions before Cayley-Dickson multiplication.
    # These associators retain the collision detector and the signed minors.
    u = QZERO + qj
    for m in range(3):
        for n in range(3):
            wronskian = avars[m] * avars[n + 1] - avars[m + 1] * avars[n]
            sign_associator = associator(embed(qmul(P[m], qi)), embed(qmul(P[n], qi)), ell)
            checks.equal("signed_associators", f"oriented minor pair {m},{n}", sign_associator, vector_scale(-2 * wronskian, u))
            dot = avars[m] * avars[n] + avars[m + 1] * avars[n + 1]
            dot_associator = associator(embed(qmul(P[m], qi)), embed(qmul(P[n], qk)), ell)
            checks.equal("signed_associators", f"inner product pair {m},{n}", dot_associator, vector_scale(2 * dot, u))
    Aenergy = associator(embed(qmul(P[0], qi)), embed(qmul(P[0], qk)), ell)
    Atime = associator(embed(qmul(P[0], qi)), embed(qmul(vector_neg(P[2]), qk)), ell)
    Asign = tuple(associator(embed(qmul(P[m], qi)), embed(qmul(P[m + 1], qi)), ell) for m in (0, 1))
    checks.equal("signed_associators", "collision detector A_energy=2uE", Aenergy, vector_scale(2 * N, u))
    checks.equal("signed_associators", "time identity A_time=uE_t", Atime, vector_scale(energy_velocity, u))
    checks.equal("signed_associators", "stationary sign A_sign0=2uL0", Asign[0], vector_scale(2 * L0, u))
    checks.equal("signed_associators", "stationary sign A_sign1=2uL1", Asign[1], vector_scale(2 * L1, u))
    checks.equal("signed_associators", "first stationary time/sign equality", at(Atime, {"a1": ZERO}), at(Asign[0], {"a1": ZERO}))
    checks.equal("signed_associators", "second stationary time/sign equality", at(Atime, {"a2": ZERO}), at(Asign[1], {"a2": ZERO}))

    # Formal recurrence checks for a standard eight-dimensional left-monogenic
    # extension. These use the four quaternion derivatives stipulated above;
    # they do not establish convergence or domain conditions for any source.
    r = generic(4, "r")
    rbar = qconj(r)
    for m in range(4):
        checks.equal("differential_extension", f"x0 recurrence G{m}", jet_dvector(G[m], "x0"), G[m + 1])
        checks.equal("differential_extension", f"x1 recurrence G{m}", jet_dvector(G[m], "x1"), qmul(G[m + 1], qi))
        checks.equal("differential_extension", f"x2 recurrence G{m}", jet_dvector(G[m], "x2"), vector_neg(G[m + 2]))
        checks.equal("differential_extension", f"x3 recurrence G{m}", jet_dvector(G[m], "x3"), vector_neg(qmul(G[m + 2], qi)))
        checks.equal("differential_extension", f"D G{m}=0", quaternion_dirac(G[m]), QZERO)
        checks.equal("differential_extension", f"barD G{m}=2G{m+1}", quaternion_dirac(G[m], conjugate=True), vector_scale(2, G[m + 1]))
    naive_defect = octonion_dirac(G[0] + G[2])
    checks.equal("differential_extension", "naive doubled trace defect", naive_defect, QZERO + vector_scale(2, G[3]))
    lifts = tuple(vector_sub(G[m], vector_scale(Fraction(1, 2), qmul(G[m + 3], rbar))) + G[m + 2] for m in range(3))
    checks.equal("differential_extension", "corrected lift is left monogenic", octonion_dirac(lifts[0]), ozero)
    checks.equal("differential_extension", "corrected lift has prescribed r=0 trace", at(lifts[0], {f"r{mu}": ZERO for mu in range(4)}), doubled)
    checks.equal("differential_extension", "corrected lift spatial recurrence", jet_dvector(lifts[0], "x0"), lifts[1])
    checks.equal("differential_extension", "corrected lift heat recurrence", jet_dvector(lifts[0], "t"), vector_neg(lifts[2]))
    generic_field = tuple(avars[mu % 7] + bvars[(mu + 3) % 7] * r[mu % 4] + r[(mu + 1) % 4] ** 2 * avars[(mu + 1) % 7] for mu in range(8))
    checks.equal("differential_extension", "split D8 formula matches direct left multiplication", octonion_dirac(generic_field), octonion_dirac_direct(generic_field))
    checks.equal("differential_extension", "direct left D8 of naive trace", octonion_dirac_direct(doubled), naive_defect)
    checks.equal("differential_extension", "direct left D8 of corrected lift", octonion_dirac_direct(lifts[0]), ozero)

    # Holomorphic transverse derivative: h_k(x+iy)=a_k+i*y*a_{k+1}+O(y^2).
    # First-order substitutions suffice because only d/dy at y=0 is tested.
    holomorphic_first_order = {f"b{k}": y * avars[k + 1] for k in range(4)}
    transverse = at(dvector(at(jet_associator, holomorphic_first_order), "y"), {"y": ZERO})
    expected_transverse = QZERO + (ZERO, -2 * L1, ZERO, ZERO)
    checks.equal("transverse_identity", "d_y[G0,G1,ell] at real slice equals -2ell*i*L1", transverse, expected_transverse)
    checks.equal("transverse_identity", "squared transverse norm is 4 L1 squared", onorm(transverse), 4 * L1 ** 2)
    # A centered primitive supplies the neighboring identity for L0, but adds
    # data beyond the original four jets and has an arbitrary integration constant.
    primitive_value = Poly.variable("primitive_value")
    primitive_jet = (primitive_value, y * h0, h0, -y * h1)
    first_jet = (h0, y * h1, h1, -y * h2)
    primitive_associator = associator(embed(primitive_jet), embed(first_jet), ell)
    primitive_transverse = at(dvector(primitive_associator, "y"), {"y": ZERO})
    checks.equal("transverse_identity", "primitive extension derivative equals -2ell*i*L0", primitive_transverse, QZERO + (ZERO, -2 * L0, ZERO, ZERO))

    collision_records = []
    for name, H, index in (
        ("quadratic", (x - a) ** 2 - 2 * (t - T), 0),
        ("cubic", (x - a) ** 3 - 6 * (t - T) * (x - a), 1),
    ):
        jets = [H]
        for _ in range(3):
            jets.append(jets[-1].derivative("x"))
        checks.equal("heat_collision_examples", f"{name} backward heat equation", H.derivative("t"), -jets[2])
        collision = [jet.substitute({"x": a, "t": T}) for jet in jets]
        checks.equal("heat_collision_examples", f"{name} collision projection norm zero", collision[0] ** 2 + collision[1] ** 2, ZERO)
        doubled_collision_norm = sum((jet ** 2 for jet in collision), ZERO)
        checks.equal("heat_collision_examples", f"{name} full norm stays positive at collision", doubled_collision_norm, 4 if name == "quadratic" else 36)
        before = [jet.substitute({"x": a, "t": T - epsilon}) for jet in jets]
        stationary = before[index + 1]
        loss = before[index + 1] ** 2 - before[index] * before[index + 2]
        collision_norm = before[0] ** 2 + before[1] ** 2
        checks.equal("heat_collision_examples", f"{name} stationary condition before collision", stationary, ZERO)
        checks.equal("heat_collision_examples", f"{name} exact loss is minus norm divided by epsilon", epsilon * loss, -collision_norm)
        checks.check("heat_collision_examples", f"{name} loss strictly negative for example epsilon=1", loss.evaluate({"epsilon": 1}) < 0)
        collision_map = {f"a{k}": jet for k, jet in enumerate(collision)}
        before_map = {f"a{k}": jet for k, jet in enumerate(before)}
        checks.equal("heat_collision_examples", f"{name} octonionic energy detector vanishes at collision", at(Aenergy, collision_map), ozero)
        checks.equal("heat_collision_examples", f"{name} octonionic energy detector before collision", at(Aenergy, before_map), vector_scale(2 * collision_norm, u))
        checks.equal("heat_collision_examples", f"{name} octonionic sign retains the negative loss", at(Asign[index], before_map), vector_scale(2 * loss, u))
        checks.equal("heat_collision_examples", f"{name} stationary octonionic time/sign identity", at(Atime, before_map), at(Asign[index], before_map))
        collision_records.append({
            "family": name,
            "H": str(H),
            "collision_at": "t=T, x=a (T may be any positive constant)",
            "jet_at_collision": [str(jet) for jet in collision],
            "doubled_norm_at_collision": str(doubled_collision_norm),
            "stationary_test_index": index,
            "before_collision_parameter": "t=T-epsilon, x=a, epsilon>0",
            "stationary_L": str(loss),
            "collision_norm": str(collision_norm),
            "ratio": "L/N=-1/epsilon",
        })

    return {
        "convention": "(a,b)=a+ell*b; (a,b)(c,d)=(ac-d*conj(b),conj(a)*d+cb)",
        "basis_order": ["1", "i", "j", "k", "ell", "ell*i", "ell*j", "ell*k"],
        "complex_jet_coordinates": "G_m=(a_m,b_m,a_(m+1),-b_(m+1))",
        "complex_commutator_G0_G1": [str(p) for p in expected_commutator],
        "physical_subalgebra_indices": sorted(physical_indices),
        "transverse_associator_coordinates": [str(p) for p in transverse],
        "transverse_identity": "d_y[G0,G1,ell]|_(y=0)=-2*ell*i*L1, z=x+iy",
        "primitive_identity_scope": "L0 analogue requires G_-1 built from a holomorphic primitive; no additional four-jet constraint follows",
        "signed_associator_identities": {
            "u": "ell*j",
            "minor": "[G_m*i,G_n*i,ell]=-2*u*(h_m*h_(n+1)-h_(m+1)*h_n)",
            "dot_product": "[G_m*i,G_n*k,ell]=2*u*(h_m*h_n+h_(m+1)*h_(n+1))",
            "collision_detector": "[F*i,F*k,ell]=2*u*(H^2+H_x^2)",
            "stationary_sign": "[G_j*i,G_(j+1)*i,ell]=2*u*L_j",
            "time_velocity": "[F*i,F_t*k,ell]=u*partial_t(H^2+H_x^2)",
            "scope": "exact on the physical real slice; fixed multipliers and orientation are part of each identity",
        },
        "differential_extension": {
            "naive_defect": "D8(G_0,G_2)=(0,2G_3)",
            "corrected_lift": "O_m(q,r)=(G_m(q)-(1/2)*G_(m+3)(q)*conj(r),G_(m+2)(q))",
            "checked": ["D8 O_0=0", "O_0(q,0)=(G_0,G_2)", "partial_x0 O_0=O_1", "partial_t O_0=-O_2"],
            "scope": "formal algebra under stated Fueter/heat jet recurrences; correction uses additional jets",
        },
        "collision_examples": collision_records,
        "interpretation": [
            "The physical four-jet package lies in an associative quaternion subalgebra.",
            "The complex jet extension can have a nonzero octonionic associator.",
            "Its first transverse derivative recovers an existing signed Laguerre form.",
            "Associators with fixed i/k multipliers retain the collision norm and stationary signs exactly.",
            "The corrected standard left-monogenic extension needs jets beyond the four boundary values.",
            "Norms square that form and therefore do not determine its sign.",
            "Generic algebra and the backward heat equation also admit positive-time collisions.",
            "No theta-specific sign estimate, analytic continuation bound, or RH conclusion is checked.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path to the small JSON execution record")
    args = parser.parse_args()
    source = Path(__file__).resolve()
    checks = Checks()
    record = {
        "schema": "inv21_octonion_four_jet_exact_checks_v1",
        "research_date": "2026-10-14",
        "prepared_for": "Edward Baker",
        "llm_assistance": True,
        "recorded_model": "gpt-6-astra",
        "recorded_effort": "ultra",
        "checker_source_name": source.name,
        "checker_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "arithmetic": "exact rational sparse polynomial expansion; Python standard library",
        "python_version": sys.version.split()[0],
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "status": "ERROR",
        "scope": "computational algebra checks; not formal proof verification or theta-specific positivity",
    }
    try:
        record["results"] = run_checks(checks)
        record["status"] = "PASS" if not checks.failures else "FAIL"
    except Exception as exc:
        record["error"] = {"type": type(exc).__name__, "message": str(exc)}
    record["checks_by_group"] = dict(sorted(checks.counts.items()))
    record["checks_total"] = sum(checks.counts.values())
    record["checks_failed"] = len(checks.failures)
    record["failures"] = checks.failures
    record["completed_utc"] = datetime.now(timezone.utc).isoformat()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": record["status"],
        "checks_total": record["checks_total"],
        "checks_failed": record["checks_failed"],
        "output": str(args.output),
        "source_sha256": record["checker_source_sha256"],
        **({"error": record["error"]} if "error" in record else {}),
    }, sort_keys=True))
    return 0 if record["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
