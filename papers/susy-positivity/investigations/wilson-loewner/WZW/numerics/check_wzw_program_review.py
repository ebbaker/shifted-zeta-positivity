#!/usr/bin/env python3
"""Finite controls accompanying the 24 September 2026 review of the WZW branch.

Standard library only (fractions, math, json, hashlib, random, platform).
Written by Claude Fable 5.1 (Anthropic, model `claude-fable-5-1`) for Edward Baker.

Groups
  A  Independent re-derivation of the SU(2)_2 pilot's finite algebra
     (pilot note eqs. (7), (10)-(13), (16)-(21)) in exact arithmetic over Q(sqrt 3)
     where the statement is exact, floating otherwise.
  B  The archimedean tower and the free-fermion sector of SU(2)_2:
     unit two-point weights force h = 1/2; the two-spin-structure sum at
     cylinder scale 1 reproduces 2 n_gamma exactly; the scale-2 single tower
     has offset 1 (the collar note's "gap 1").
  C  Cross-identities the review asserts: the Bost--Connes coefficient is the
     Jordan totient J_{2 omega} of the fractional-dimension investigation;
     multiplicativity; the integer-d counting interpretation; the k = 2
     anomaly coincidence is unique to k = 2; a causal self-adjoint finite
     matrix is diagonal.
  D  Leading singularity of the prime-free kernel, A_omega u^(omega-1).

These are finite identities and floating diagnostics.  They are not a
positivity certificate, a realization, or a statement about the zeros.
Run from anywhere:  python3 -B check_wzw_program_review.py --output out.json
"""
import argparse
import hashlib
import json
import math
import platform
import random
from fractions import Fraction as Fr
from pathlib import Path

CASES = []


def check(name, value, threshold, kind="floating"):
    value = float(value)
    passed = math.isfinite(value) and value <= threshold
    CASES.append(dict(name=name, value=value, threshold=threshold,
                      passed=passed, kind=kind))


def exact(name, condition):
    CASES.append(dict(name=name, value=0 if condition else 1, threshold=0,
                      passed=bool(condition), kind="exact rational"))


# ---------------------------------------------------------------------------
# Exact arithmetic over Q(sqrt 3):  a + b*sqrt(3)
# ---------------------------------------------------------------------------
class Q3:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = _q3(o); return Q3(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __sub__(self, o):
        o = _q3(o); return Q3(self.a - o.a, self.b - o.b)

    def __rsub__(self, o):
        return _q3(o) - self

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __mul__(self, o):
        o = _q3(o)
        return Q3(self.a * o.a + 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def inv(self):
        n = self.a * self.a - 3 * self.b * self.b
        return Q3(self.a / n, -self.b / n)

    def __truediv__(self, o):
        return self * _q3(o).inv()

    def __eq__(self, o):
        o = _q3(o); return self.a == o.a and self.b == o.b

    def __float__(self):
        return float(self.a) + float(self.b) * math.sqrt(3.0)

    def __repr__(self):
        return f"Q3({self.a},{self.b})"


def _q3(x):
    return x if isinstance(x, Q3) else Q3(x)


S3 = Q3(0, 1)  # sqrt(3)


def mat(rows):
    return [[_q3(x) for x in r] for r in rows]


def mmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(2)), Q3(0)) for j in range(2)]
            for i in range(2)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def msc(c, A):
    c = _q3(c)
    return [[c * A[i][j] for j in range(2)] for i in range(2)]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))


I2 = mat([[1, 0], [0, 1]])
D = mat([[Fr(-3, 2), 0], [0, Fr(1, 2)]])                       # T_01
C = [[Q3(0), -S3 / 2], [-S3 / 2, Q3(-1)]]                     # T_02
B = [[Q3(0), S3 / 2], [S3 / 2, Q3(-1)]]                       # T_12
NU = Fr(1, 4)          # 1/(k+2) at k = 2
H = Fr(3, 16)          # h = C_{1/2}/(2K) = (3/2)/8


# ---------------------------------------------------------------------------
# Group A: the pilot's finite algebra
# ---------------------------------------------------------------------------
def group_a():
    # (7): D + C + B = -(3/2) I
    exact("A1 D+C+B = -3/2 I", meq(madd(madd(D, C), B), msc(Fr(-3, 2), I2)))
    # (17): D^2 = 3/4 I - D, C^2 = 3/4 I - C, DC + CD = B
    exact("A2 D^2 = 3/4 I - D", meq(mmul(D, D), madd(msc(Fr(3, 4), I2), msc(-1, D))))
    exact("A3 C^2 = 3/4 I - C", meq(mmul(C, C), madd(msc(Fr(3, 4), I2), msc(-1, C))))
    exact("A4 DC + CD = B", meq(madd(mmul(D, C), mmul(C, D)), B))

    def G_of(a, b, udot):
        a, b, udot = Fr(a), Fr(b), Fr(udot)
        t1 = msc(NU * (2 / a**2 - udot / a), D)
        t2 = msc(NU * (2 / b**2 - udot / b), C)
        t3 = msc(-NU * 2 / (a * b), B)
        t4 = msc(-2 * H * (1 / a**2 + 1 / b**2), I2)
        return madd(madd(madd(t1, t2), t3), t4)

    def Q_of(a, b):
        return madd(msc(1 / Fr(a), D), msc(1 / Fr(b), C))

    def reduced(a, b, udot):
        Q = Q_of(a, b)
        return msc(-NU, madd(msc(2, mmul(Q, Q)), msc(Fr(udot), Q)))

    # (19) and (21)
    G19 = mat([[Fr(-39, 32), 0], [0, Fr(-3, 32)]])
    G19[0][1] = G19[1][0] = -3 * S3 / 16
    exact("A5 G(a=1,b=2,udot=0) equals (19)", meq(G_of(1, 2, 0), G19))
    G21 = mat([[Fr(9, 32), 0], [0, Fr(-3, 32)]])
    G21[0][1] = G21[1][0] = S3 / 16
    exact("A6 G(a=1,b=2,udot=4) equals (21)", meq(G_of(1, 2, 4), G21))

    # (1) from (16)+(17): G = -nu (2 Q^2 + udot Q), several rational geometries
    for (a, b, u) in [(1, 2, 0), (1, 2, 4), (Fr(1, 3), Fr(5, 2), Fr(-7, 3)),
                      (3, 7, Fr(1, 2)), (Fr(2, 5), 1, 11)]:
        exact(f"A7 Ward/KZ reduction G = -nu(2Q^2+udot Q) at a={a},b={b},udot={u}",
              meq(G_of(a, b, u), reduced(a, b, u)))

    # det Q = -(3/4)(1/a - 1/b)^2
    for (a, b) in [(1, 2), (Fr(1, 3), Fr(5, 2)), (3, 7)]:
        Q = Q_of(a, b)
        det = Q[0][0] * Q[1][1] - Q[0][1] * Q[1][0]
        exact(f"A8 det Q = -(3/4)(1/a-1/b)^2 at a={a},b={b}",
              det == Q3(Fr(-3, 4) * (1 / Fr(a) - 1 / Fr(b))**2))

    # Blocks (10),(11) satisfy KZ (8):  f' = nu (D/r + B/(r-1)) f   (floating)
    Df, Bf = [[float(x) for x in r] for r in D], [[float(x) for x in r] for r in B]
    nu = float(NU)

    def f0(r):
        s = math.sqrt(1 - r); p = (r * (1 - r))**(-3 / 8)
        return [p / (2 * math.sqrt(2)) * (1 + s)**1.5,
                -p / (2 * math.sqrt(2)) * math.sqrt(3) * (1 - s) * math.sqrt(1 + s)]

    def f1(r):
        s = math.sqrt(1 - r); p = (r * (1 - r))**(-3 / 8)
        return [-p / math.sqrt(6) * (1 - s)**1.5,
                p / math.sqrt(6) * math.sqrt(3) * (1 + s) * math.sqrt(1 - s)]

    def kz_rhs(f, r):
        M = [[nu * (Df[i][j] / r + Bf[i][j] / (r - 1)) for j in range(2)] for i in range(2)]
        return [M[0][0] * f[0] + M[0][1] * f[1], M[1][0] * f[0] + M[1][1] * f[1]]

    def deriv(fun, r, h=1e-4):
        # 6th-order central stencil
        c = [(-1 / 60), (3 / 20), (-3 / 4), 0, (3 / 4), (-3 / 20), (1 / 60)]
        out = [0.0, 0.0]
        for k, ck in zip(range(-3, 4), c):
            v = fun(r + k * h)
            out[0] += ck * v[0]; out[1] += ck * v[1]
        return [out[0] / h, out[1] / h]

    worst = 0.0
    for r in [0.15, 0.3, 0.5, 0.7, 0.85]:
        for fun in (f0, f1):
            d = deriv(fun, r); rhs = kz_rhs(fun(r), r)
            worst = max(worst, abs(d[0] - rhs[0]), abs(d[1] - rhs[1]))
    check("A9 blocks (10),(11) satisfy KZ (8), max residual (6th-order FD)", worst, 1e-7)

    # Frobenius leading terms: f0 ~ r^(-3/8) e0, f1 ~ r^(1/8) e1
    r = 1e-8
    check("A10 f0 leading r^(-3/8) e0", abs(f0(r)[0] * r**0.375 - 1) + abs(f0(r)[1] * r**0.375), 1e-6)
    check("A11 f1 leading r^(1/8) e1", abs(f1(r)[0] * r**(-0.125)) + abs(f1(r)[1] * r**(-0.125) - 1), 1e-6)

    # (13): M0 = 2^(-3/8) f0(1/2); (21): initial norm growth for udot = 4 is
    # 2<M0, G M0> ~ 0.4363884954; for udot = 0 it is negative.
    M0 = [2**(-0.375) * v for v in f0(0.5)]
    check("A12 M0 matches (13)", abs(M0[0] - 1.02266239412001) + abs(M0[1] + 0.30390758736355), 1e-11)

    def quad(G, v):
        Gf = [[float(x) for x in r] for r in G]
        return 2 * sum(v[i] * Gf[i][j] * v[j] for i in range(2) for j in range(2))

    g4 = quad(G_of(1, 2, 4), M0)
    check("A13 d/dt |M|^2 at udot=4 equals 0.436388495438834", abs(g4 - 0.436388495438834), 1e-12)
    check("A14 d/dt |M|^2 at udot=4 is positive (moving driver grows)", -g4, -1e-3)
    g0 = quad(G_of(1, 2, 0), M0)
    check("A15 d/dt |M|^2 at udot=0 is negative", g0, -1e-3)
    # e0 growth 9/16 at udot=4 (pilot text)
    exact("A16 <e0, 2 G e0> = 9/16 at udot=4", G_of(1, 2, 4)[0][0] * 2 == Q3(Fr(9, 16)))


# ---------------------------------------------------------------------------
# Group B: archimedean tower and the free-fermion sector
# ---------------------------------------------------------------------------
def poch_over_fact(alpha, n):
    """(alpha)_n / n! as a Fraction."""
    v = Fr(1)
    for k in range(n):
        v *= (alpha + k) / (k + 1)
    return v


def group_b():
    # B1: two-point weights d_n = (2h)_n/n!  are all 1 iff 2h = 1
    exact("B1 h=1/2: (2h)_n/n! = 1 for n<=30",
          all(poch_over_fact(Fr(1), n) == 1 for n in range(31)))
    exact("B2 h=3/16: d_1=3/8, d_2=33/128, d_3=209/1024 (collar note)",
          poch_over_fact(Fr(3, 8), 1) == Fr(3, 8)
          and poch_over_fact(Fr(3, 8), 2) == Fr(33, 128)
          and poch_over_fact(Fr(3, 8), 3) == Fr(209, 1024))
    exact("B3 h=3/16 weights are not unit (d_1 != 1)", poch_over_fact(Fr(3, 8), 1) != 1)
    # For any h != 1/2 the first weight 2h != 1
    exact("B4 (2h)_1/1! = 2h, so unit weights force 2h = 1",
          all(poch_over_fact(Fr(a), 1) == Fr(a) for a in (Fr(3, 8), Fr(1), Fr(2), Fr(7, 5))))

    def tower(u, offset, spacing, N=4000):
        return sum(math.exp(-(spacing * n + offset) * u) for n in range(N))

    worst_sum = worst_ns = worst_l2 = 0.0
    for u in [0.05, 0.2, 0.7, 1.5, 3.0]:
        Gs = 1 / (2 * math.sinh(u / 2))          # NS-type fermion propagator, scale 1
        Go = 1 / (2 * math.cosh(u / 2))          # twisted ((-1)^n weighted) propagator
        two_ngamma = 2 * tower(u, 0.5, 2.0)      # 2 n_gamma = 2 sum e^{-(2n+1/2)u}
        worst_sum = max(worst_sum, abs(Gs + Go - two_ngamma))
        worst_ns = max(worst_ns, abs(Gs - tower(u, 0.5, 1.0)))
        # scale-2 single fermion tower: 1/sinh u = 2 sum e^{-(2n+1)u}  (offset 1)
        worst_l2 = max(worst_l2, abs(1 / math.sinh(u) - 2 * tower(u, 1.0, 2.0)))
    check("B5 G_s + G_o = 2 n_gamma (two spin structures at cylinder scale 1)", worst_sum, 1e-12)
    check("B6 G_s = sum e^{-(n+1/2)u} (fermion, scale 1: offset 1/2, spacing 1)", worst_ns, 1e-12)
    check("B7 scale-2 fermion tower 1/sinh u = 2 sum e^{-(2n+1)u} has offset 1", worst_l2, 1e-12)
    # G_o has the (-1)^n alternation: G_o = sum (-1)^n e^{-(n+1/2)u}
    u = 0.9
    alt = sum((-1)**n * math.exp(-(n + 0.5) * u) for n in range(4000))
    check("B8 G_o = sum (-1)^n e^{-(n+1/2)u}", abs(alt - 1 / (2 * math.cosh(u / 2))), 1e-12)
    # Collision order: 2 n_gamma ~ 1/u ; G_o regular at 0
    u = 1e-6
    check("B9 2 n_gamma(u) u -> 1 (1/u collision, as the form requires)",
          abs(2 * (math.exp(u / 2) / (2 * math.sinh(u))) * u - 1), 1e-5)
    check("B10 G_o(0) = 1/2 (regular)", abs(1 / (2 * math.cosh(0)) - 0.5), 1e-15)


# ---------------------------------------------------------------------------
# Group C: cross-identities asserted in the review
# ---------------------------------------------------------------------------
def prime_factors(n):
    ps, d = [], 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps.append(n)
    return ps


def c_coeff(n, omega):
    v = n ** (omega - 0.5)
    for l in prime_factors(n):
        v *= 1 - l ** (-2 * omega)
    return v


def jordan(n, d):
    v = n ** d
    for l in prime_factors(n):
        v *= 1 - l ** (-d)
    return v


def phi_exact(n):
    v = Fr(n)
    for l in prime_factors(n):
        v *= 1 - Fr(1, l)
    return v


def group_c():
    # C1: c_n(omega) = J_{2 omega}(n) / n^{omega + 1/2}  (fractional-dimension Prop 1.2, d = 2 omega)
    worst = 0.0
    for omega in (0.1, 0.25, 0.4, 0.5):
        for n in range(1, 61):
            worst = max(worst, abs(c_coeff(n, omega) - jordan(n, 2 * omega) / n ** (omega + 0.5)))
    check("C1 c_n(omega) = J_{2omega}(n)/n^{omega+1/2}, n<=60, four shifts", worst, 1e-13)
    # C2: at omega = 1/2, c_n = phi(n)/n exactly
    exact("C2 omega=1/2: n^{0} prod(1-l^{-1}) = phi(n)/n exactly, n<=200",
          all(Fr(1) * math.prod([1 - Fr(1, l) for l in prime_factors(n)] or [Fr(1)]) == phi_exact(n) / n
              for n in range(1, 201)))
    # C3: multiplicativity for coprime arguments
    worst = 0.0
    for omega in (0.1, 0.3, 0.5):
        for m, n in [(2, 3), (4, 9), (5, 12), (7, 20), (8, 27)]:
            worst = max(worst, abs(c_coeff(m * n, omega) - c_coeff(m, omega) * c_coeff(n, omega)))
    check("C3 c_{mn} = c_m c_n for coprime m,n", worst, 1e-13)
    # C4: integer d: J_d(n) counts tuples mod n with gcd(n, x) = 1
    ok = True
    for d in (1, 2, 3):
        for n in (1, 2, 3, 4, 6, 8, 12):
            cnt = 0
            for x in range(n ** d):
                digits = [(x // n ** i) % n for i in range(d)]
                if math.gcd(n, *digits) == 1:
                    cnt += 1
            ok = ok and cnt == round(jordan(n, d))
    exact("C4 J_d(n) counts primitive d-tuples mod n (d=1,2,3)", ok)
    # C5: anomaly coincidence: nu/4 = c/24 with nu = 1/(k+2), c = 3k/(k+2)  iff k = 2
    sols = [k for k in range(1, 13) if Fr(1, 4 * (k + 2)) == Fr(3 * k, 24 * (k + 2))]
    exact("C5 nu/4 = c/24 holds only at k = 2 among k = 1..12", sols == [2])
    exact("C6 at k=2: c = 3/2 and 6 nu = 3/2", Fr(3 * 2, 4) == Fr(3, 2) and 6 * Fr(1, 4) == Fr(3, 2))
    # C7: finite shadow of the collar theorem.  A causal operator on a filtered
    #     finite space is lower triangular; if it is also self-adjoint it must be
    #     diagonal, i.e. a multiplication operator.  Check: (i) a random
    #     lower-triangular matrix with any nonzero strictly-lower entry is not
    #     symmetric; (ii) forcing symmetry on a lower-triangular matrix leaves
    #     exactly its diagonal.
    rng = random.Random(20260924)
    ok = True
    for n in range(2, 9):
        L = [[Fr(rng.randint(1, 9), rng.randint(1, 9)) if j <= i else Fr(0)
              for j in range(n)] for i in range(n)]
        symmetric = all(L[i][j] == L[j][i] for i in range(n) for j in range(n))
        ok = ok and not symmetric                       # (i)
        S = [[L[i][j] if (i == j or (L[i][j] == L[j][i])) else Fr(0)
              for j in range(n)] for i in range(n)]      # (ii) keep only entries matching the mirror
        ok = ok and all(S[i][j] == (L[i][i] if i == j else 0) for i in range(n) for j in range(n))
    exact("C7 causal (triangular) + self-adjoint finite matrix is diagonal (multiplication)", ok)


# ---------------------------------------------------------------------------
# Group D: leading singularity of the prime-free kernel
# ---------------------------------------------------------------------------
def group_d():
    worst = 0.0
    for omega in (0.1, 0.25, 0.4):
        A = (2 * math.pi) ** omega / math.gamma(omega)
        for u in (1e-7, 1e-6):
            q = (2 * math.pi ** omega / math.gamma(omega)) * math.exp(-(2.5 - omega) * u) \
                * (1 - math.exp(-2 * u)) ** (omega - 1)
            worst = max(worst, abs(q / (A * u ** (omega - 1)) - 1))
    check("D1 q_omega(u) / (A_omega u^{omega-1}) -> 1, A_omega = (2pi)^omega/Gamma(omega)", worst, 1e-5)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    args = ap.parse_args()
    group_a(); group_b(); group_c(); group_d()
    here = Path(__file__).resolve()
    record = dict(
        program=here.name,
        program_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
        model="Claude Fable 5.1 (Anthropic, claude-fable-5-1)",
        date="2026-09-24",
        python=platform.python_version(),
        platform=platform.platform(),
        dependencies="standard library only",
        case_count=len(CASES),
        exact_rational_cases=sum(c["kind"] == "exact rational" for c in CASES),
        all_pass=all(c["passed"] for c in CASES),
        failed=[c["name"] for c in CASES if not c["passed"]],
        cases=CASES,
        scope=("Finite identities and floating diagnostics for the WZW program review. "
               "Not a positivity certificate, realization, or statement about zeros."),
    )
    if args.output:
        Path(args.output).write_text(json.dumps(record, indent=1))
    print(json.dumps({k: record[k] for k in ("case_count", "exact_rational_cases", "all_pass", "failed")}))


if __name__ == "__main__":
    main()
