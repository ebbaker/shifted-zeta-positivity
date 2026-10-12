#!/usr/bin/env python3
"""Certified independent replay of finite-lane Triangle rows of the pinned
Gomila de Bruijn--Newman package.  Standard-library Python; deterministic.

Audited package: judegomila/dbn-lambda-01787854-candidate-audit at commit
a74738deb6d5e0f76887cb36901da08b68dca705 (Lambda <= 893927/5000000 claim).
Row parameters: t0 = 129/800, y0^2 = 87677/2500000, finite rows N = 690988..3840000.

Quantity (package NATIVE_BINDING.md; src/lemma_sweep_p235711.c compiled with
TRIANGLE_WEIGHT; at the first row of a producer run the stored floor is this
value floored to 12 decimals, at later rows it is smaller):

    L_N  = (1 - g_N - S_N) / M_N  -  g_N C_N,
    S_N  = sum_{n=2}^{DN} (|B_{N,n}| + g_N |A_{N,n}|) n^(-sigma_N),
    B_{N,n} = sum_{d|D, d|n, n<=dN} lambda_d b_t(n/d),
    A_{N,n} = sum_{same d} lambda_d b_t(n/d) (n/d)^y,
    lambda_d = (-1)^omega(d) prod_{p|d} b_t(p),     b_t(m) = exp((t/4) log^2 m),
    q_N = N^2 - t/16,   x_N = 4 pi q_N,
    g_N = exp(y/50 - (y/2) log q_N),
    sigma_N = (1+y)/2 + (t/4) log q_N - t (1 - 3y + 4y(1+y)/x_N^2)_+ / (2 x_N^2),
    kappa_N = t y / (2 (x_N - 6)),
    M_N = sum_{d|D} |lambda_d| d^(-sigma_N),
    C_N = sum_{m=2}^{N} b_t(m) (m^kappa_N - 1) m^(y - sigma_N),
D = product of the leg's Euler primes: {2,3,5,7,11} for N <= 728999,
{2,3,5,7} for N <= 818999, {2,3,5} for N <= 1027999, {2,3} above.

Method (independent of the package's Arb producer and of its amortisation):

1. Enumeration.  Write n = G k with G = gcd(n, D).  Then gcd(k, D/G) = 1, the
   active divisors are d = G/e with e | G and e k <= N, and
   B_{N,n} = sum_{e|G, ek<=N} lambda_{G/e} b_t(ek), n^-sigma = G^-sigma k^-sigma.
   Every contributing n has k <= N, so the sum runs over about
   N prod_p (2 - 1/p) integers n and 2^|P| N (d, m) incidences, instead of the
   D N integers scanned by a direct loop.
2. Tables.  ln m, b_t(m), b_t(m) m^y and m^-sigma (m <= N) are computed with the
   decimal module at PREC = 45 significant digits.  +, -, *, / are correctly
   rounded; exp and ln are documented as correctly rounded (ROUND_HALF_EVEN);
   sqrt is correctly rounded by the General Decimal Arithmetic specification.
   Each table value is exp(z) with z formed by at most six such operations
   from ln m and the midpoints of rigorous enclosures of y and sigma; the
   function rho_bound() below bounds the resulting relative error and the
   programme asserts that it is at most RHO = 1e-40.
3. Fixed point.  Table values are rounded to integers at scale U = 2^110; the
   sum over n is accumulated exactly in Python integers, every shift is a
   floor, and an explicit a-priori bound E_S on all rounding errors (derived in
   error_bound_S below from the table maxima, the incidence bound 2^|P| and the
   number of n) is added in both directions.
4. Scalars.  g_N, sigma_N, kappa_N, M_N and C_N are enclosed by interval
   arithmetic with directed rounding (decimal contexts ROUND_FLOOR/CEILING;
   correctly rounded exp/ln/sqrt padded by a relative 10^-(PREC-2), i.e.
   20 half-ulps).  C_N is enclosed via
   kappa ln m <= m^kappa - 1 <= kappa ln m N^kappa.
5. Output: an interval [L_lo, L_hi] containing L_N at t = t0, y = y0, compared
   with the stored floor T_N: T_N <= L_lo certifies the stored row
   independently; T_N > L_hi would refute it.  For first-of-run singleton-t
   rows the 12-decimal floor of L_N is also compared exactly.

What this does NOT check: the analytic reductions (native binding, Dini
y-transfer, window freeze, tail lemma, error budget) and every stored row.
The package's later legs store t-box floors over [0.16125, 0.161250001]; this
programme evaluates only t = t0 = 0.16125, which is the time consumed by
Polymath Theorem 1.2 (ii); such floors are expected to lie below L_N(t0).

Usage:
    python3 check_finite_row_certified_replay.py                 # weakest row only
    python3 check_finite_row_certified_replay.py --set first-of-run --jobs 2
    python3 check_finite_row_certified_replay.py --rows 690988,729000 --output rec.json
    python3 check_finite_row_certified_replay.py --selftest       # brute-force cross-check
    python3 check_finite_row_certified_replay.py --package DIR    # re-read stored floors (hash-checked)

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
claude-opus-5-5), 12 October 2026.  Internal check, not independent review.
"""
import argparse
import decimal
import gzip
import hashlib
import json
import os
import platform
import re
import sys
import time
from decimal import (Context, Decimal as Dc, ROUND_CEILING, ROUND_FLOOR,
                     ROUND_HALF_EVEN)

PACKAGE = {
    "repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
    "commit": "a74738deb6d5e0f76887cb36901da08b68dca705",
}
T0 = Dc("0.16125")          # 129/800, exact in decimal
Y0SQ = Dc("0.0350708")      # 87677/2500000, exact in decimal
LEGS = [(690988, 728999, (2, 3, 5, 7, 11)), (729000, 818999, (2, 3, 5, 7)),
        (819000, 1027999, (2, 3, 5)), (1028000, 3840000, (2, 3))]

# Stored floors (12-decimal L12 field) of the rows used below, with their
# shard and whether the row is the first row of a producer run (TBOX line).
SHARD_SHA256 = {
    "p235711_690988_690995.log.gz": "d9a66e7904bcb258f008197fc1d70b9e7dab578cc55350cb829605a8271907db",
    "p235711_690996_691500.log.gz": "d3103aec577d4d500b5713dd0b1aada109602849d1fa31805db6c2f08053e719",
    "p235711_691501_697000.log.gz": "d602a19441b3f668cda7130d1001034a5b6fcf86bb80b045e2f8b749469e5fca",
    "p235711_697001_728999.log.gz": "4dcadd8b8de0e6bd419455421b37fa26a4ecfc4e3ac8765af1ce85b70fd8d95b",
    "p2357_729000_818999.log.gz": "fe89eb942ccb5a4b7e7b6ba91dcb93b8be45d82784eb2e366e67e0766bf8ab85",
    "p235_819000_1027999.log.gz": "6b7371b7c2953c8fb96225531607ac878f2eab402242b5f44f22760d803c2e85",
    "p23_1028000_1030000.log.gz": "adefc4bbebdd55c57e795d186e2063b183a7eb34a0ba3fd3dc770b01e7c2e585",
    "p23_1030001_1050000.log.gz": "f217b53e6e02a805e8ffbfc2b3ffec98a0902625fe75e286cb5f88362f760f67",
    "p23_1050001_1100000.log.gz": "9a55421582f9e8751e85f18a93b83dfebca4f16996a24cc15d2ad0130a0afc5e",
    "p23_1100001_1300000.log.gz": "6880b739d3d3446a332f6fa1b939033168a426151c174aeff48c06f0dc3c0198",
    "p23_1300001_1700000.log.gz": "de8618e213152bff26db51b12aa167ba693a17bdf52a9e60aadf28d1024b7295",
    "p23_1700001_2200000.log.gz": "8e97159496ead5e4f8e0697c44ca7a0e754c294e6f6122486a508f70939242c5",
    "p23_2200001_2800000.log.gz": "a5573508d1b24e4fd74d8ff30c9f5065f39921b4fc4eec7a7cd63976bf769751",
    "p23_2800001_3300000.log.gz": "1ec7f34e7ce51c8e618f2cb136a27fc90bba78f9da5b66fff513413d2b6db124",
    "p23_3300001_3840000.log.gz": "fdd2fc6e9dbe69d3edfa69b91e9298d53eba5c860bda6a9d1d3c20d5f77798a3",
}
STORED = {  # N: (L12, shard, first_of_run, t-box)
    690988: ("0.000000791366", "p235711_690988_690995.log.gz", True, "singleton"),
    690989: ("0.000000974062", "p235711_690988_690995.log.gz", True, "singleton"),
    690990: ("0.000001570095", "p235711_690988_690995.log.gz", False, "singleton"),
    690991: ("0.000001891132", "p235711_690988_690995.log.gz", True, "singleton"),
    690995: ("0.000003354765", "p235711_690988_690995.log.gz", False, "singleton"),
    690996: ("0.000004185565", "p235711_690996_691500.log.gz", True, "singleton"),
    691011: ("0.000010281698", "p235711_690996_691500.log.gz", True, "singleton"),
    691051: ("0.000026905674", "p235711_690996_691500.log.gz", True, "singleton"),
    691151: ("0.000068664152", "p235711_690996_691500.log.gz", True, "singleton"),
    691501: ("0.000214840069", "p235711_691501_697000.log.gz", True, "singleton"),
    693001: ("0.000839967549", "p235711_691501_697000.log.gz", True, "singleton"),
    697001: ("0.002498055377", "p235711_697001_728999.log.gz", True, "singleton"),
    707001: ("0.006586777077", "p235711_697001_728999.log.gz", True, "singleton"),
    718001: ("0.010993582868", "p235711_697001_728999.log.gz", True, "singleton"),
    728999: ("0.014771594320", "p235711_697001_728999.log.gz", False, "singleton"),
    729000: ("0.000315112459", "p2357_729000_818999.log.gz", True, "box"),
    818999: ("0.029586978955", "p2357_729000_818999.log.gz", False, "box"),
    819000: ("0.000305788807", "p235_819000_1027999.log.gz", True, "box"),
    1027999: ("0.057544045266", "p235_819000_1027999.log.gz", False, "box"),
    1028000: ("0.000309285478", "p23_1028000_1030000.log.gz", True, "box"),
    1030000: ("0.000822612862", "p23_1028000_1030000.log.gz", False, "box"),
    1030001: ("0.000889356157", "p23_1030001_1050000.log.gz", True, "box"),
    1050001: ("0.006602095978", "p23_1050001_1100000.log.gz", True, "box"),
    1100001: ("0.020238110009", "p23_1100001_1300000.log.gz", True, "box"),
    1300001: ("0.067117380094", "p23_1300001_1700000.log.gz", True, "box"),
    1700001: ("0.135884893359", "p23_1700001_2200000.log.gz", True, "box"),
    2000000: ("0.170256181382", "p23_1700001_2200000.log.gz", False, "box"),
    2200001: ("0.194954190481", "p23_2200001_2800000.log.gz", True, "box"),
    2800001: ("0.244508896569", "p23_2800001_3300000.log.gz", True, "box"),
    3000000: ("0.256532255230", "p23_2800001_3300000.log.gz", False, "box"),
    3300001: ("0.275369757891", "p23_3300001_3840000.log.gz", True, "box"),
    3840000: ("0.299655457299", "p23_3300001_3840000.log.gz", False, "box"),
}
# Package's certified error budget for the finite lane (verify_prop410_arb.c,
# logs/prop410_arb_256.log), used only for the final margin at the weakest row.
E_MAX_PACKAGE = Dc("0.000000233494905212337848893636565949")

SETS = {
    "weakest": [690988],
    "first-of-run": sorted(N for N, v in STORED.items() if v[2]),
    "all-stored": sorted(STORED),
}

# ----------------------------------------------------------------------------
# Decimal contexts and a minimal directed-rounding interval type
# ----------------------------------------------------------------------------
PREC = 45
CN = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
CF = Context(prec=PREC, rounding=ROUND_FLOOR)
CC = Context(prec=PREC, rounding=ROUND_CEILING)
EPS = Dc(5) * Dc(10) ** (-PREC)        # half-ulp relative bound of a correctly rounded result
ETA = Dc(10) ** (-(PREC - 2))          # padding used for exp/ln/sqrt = 20 x EPS
RHO = Dc("1e-40")                      # asserted relative error bound of every table value
K = 110
U = 1 << K
UD = Dc(U)
# Every implicit Decimal operation (e.g. an unparenthesised product) would use the
# thread's current context; make that the 45-digit context too.  Negation and
# absolute value below use the exact copy_negate()/copy_abs().
decimal.setcontext(Context(prec=PREC, rounding=ROUND_HALF_EVEN))


class Iv:
    """Closed interval [lo, hi] with Decimal endpoints, outward rounding."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = Dc(lo)
        hi = lo if hi is None else Dc(hi)
        if lo > hi:
            raise ValueError("empty interval")
        self.lo, self.hi = lo, hi

    @staticmethod
    def c(x):
        return x if isinstance(x, Iv) else Iv(x)

    def __add__(a, b):
        b = Iv.c(b)
        return Iv(CF.add(a.lo, b.lo), CC.add(a.hi, b.hi))

    __radd__ = __add__

    def __sub__(a, b):
        b = Iv.c(b)
        return Iv(CF.subtract(a.lo, b.hi), CC.subtract(a.hi, b.lo))

    def __rsub__(a, b):
        return Iv.c(b) - a

    def __neg__(a):
        return Iv(a.hi.copy_negate(), a.lo.copy_negate())

    def __mul__(a, b):
        b = Iv.c(b)
        lo = min(CF.multiply(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi))
        hi = max(CC.multiply(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi))
        return Iv(lo, hi)

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = Iv.c(b)
        if not (b.lo > 0 or b.hi < 0):
            raise ZeroDivisionError("interval contains 0")
        lo = min(CF.divide(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi))
        hi = max(CC.divide(x, y) for x in (a.lo, a.hi) for y in (b.lo, b.hi))
        return Iv(lo, hi)

    def __rtruediv__(a, b):
        return Iv.c(b) / a

    def mid(self):
        return CN.divide(CN.add(self.lo, self.hi), 2)

    def width(self):
        return CC.subtract(self.hi, self.lo)


def _pad(lo, hi):
    """Enclosure of [f(lo_arg), f(hi_arg)] from correctly rounded values lo, hi of an
    increasing f with positive range (relative error <= EPS < ETA)."""
    return Iv(CF.multiply(lo, CF.subtract(1, ETA)), CC.multiply(hi, CC.add(1, ETA)))


def iexp(a):
    return _pad(CN.exp(a.lo), CN.exp(a.hi))


def iln(a):
    if a.lo <= 0:
        raise ValueError("log of nonpositive interval")
    lo, hi = CN.ln(a.lo), CN.ln(a.hi)
    # ln can be negative or near zero; pad absolutely by ETA * max(1,|value|)
    plo = CC.multiply(ETA, max(Dc(1), lo.copy_abs()))
    phi = CC.multiply(ETA, max(Dc(1), hi.copy_abs()))
    return Iv(CF.subtract(lo, plo), CC.add(hi, phi))


def isqrt(a):
    return _pad(CN.sqrt(a.lo), CN.sqrt(a.hi))


def imax0(a):
    return Iv(max(a.lo, Dc(0)), max(a.hi, Dc(0)))


# pi to 50 digits (a published constant); the enclosure has width 1e-48.
PI = Iv(Dc("3.14159265358979323846264338327950288419716939937510"),
        Dc("3.14159265358979323846264338327950288419716939937511"))


def leg_primes(N):
    for a, b, P in LEGS:
        if a <= N <= b:
            return P
    raise ValueError("N outside the finite lane 690988..3840000")


# ----------------------------------------------------------------------------
# Scalars of the row
# ----------------------------------------------------------------------------
def row_scalars(N, t=T0, y2=Y0SQ, P=None):
    t = Iv(t)
    y = isqrt(Iv(y2))
    qN = Iv(N) * Iv(N) - t / 16
    xN = 4 * PI * qN
    lq = iln(qN)
    g = iexp(y / 50 - (y / 2) * lq)
    inner = 1 - 3 * y + 4 * y * (1 + y) / (xN * xN)
    sigma = (1 + y) / 2 + (t / 4) * lq - t * imax0(inner) / (2 * xN * xN)
    kappa = t * y / (2 * (xN - 6))
    bt_p = {p: iexp((t / 4) * iln(Iv(p)) * iln(Iv(p))) for p in P}
    lam = {}            # mask -> (sign, |lambda| interval, d)
    nP = len(P)
    for mask in range(1 << nP):
        mag = Iv(1)
        d = 1
        for i, p in enumerate(P):
            if mask >> i & 1:
                mag = mag * bt_p[p]
                d *= p
        lam[mask] = ((-1) ** bin(mask).count("1"), mag, d)
    M = Iv(0)
    for mask, (_, mag, d) in lam.items():
        M = M + mag * iexp(-(sigma * iln(Iv(d))))
    return dict(t=t, y=y, qN=qN, xN=xN, lq=lq, g=g, sigma=sigma, kappa=kappa,
                lam=lam, M=M, inner=inner)


def rho_bound(N, sc):
    """A-priori bound on the relative error of every table value.

    Each table value is exp(z~) where z~ approximates z in {(t/4) l^2,
    (t/4) l^2 + y l, -sigma l} with l = ln m (m <= N), computed from the
    correctly rounded l~ = ln m by <= 6 correctly rounded operations, using the
    midpoints of the enclosures of y and sigma.  With L = ln N, Z = (t/4) L^2:
      |l~ - l| <= EPS L,
      |z~ - z| <= 8 EPS (Z + y L + sigma L) + (w_y + w_sigma) L,
    and the correctly rounded exp adds a relative EPS.  Hence the relative
    error is at most exp(|z~ - z|) (1 + EPS) - 1 <= 2 |z~ - z| + 2 EPS."""
    L = CC.multiply(CC.ln(Dc(N)), CC.add(1, ETA))
    Z = CC.multiply(CC.divide(sc["t"].hi, 4), CC.multiply(L, L))
    big = CC.add(Z, CC.multiply(CC.add(sc["y"].hi, sc["sigma"].hi), L))
    dz = CC.add(CC.multiply(CC.multiply(8, EPS), big),
                CC.multiply(CC.add(sc["y"].width(), sc["sigma"].width()), L))
    return CC.add(CC.multiply(2, dz), CC.multiply(2, EPS))


# ----------------------------------------------------------------------------
# Tables and the main sum
# ----------------------------------------------------------------------------
def build_tables(N, sc):
    """BT[m] ~ b_t(m) U, AA[m] ~ b_t(m) m^y U, KS[m] ~ m^-sigma U (m = 1..N), and the
    Decimal sum CS = sum_{m=2}^N b_t(m) m^y m^-sigma ln m used for C_N."""
    t4 = CN.divide(sc["t"].mid(), 4)
    y = sc["y"].mid()
    sg = sc["sigma"].mid()
    ln, ex, mul, add, rnd = CN.ln, CN.exp, CN.multiply, CN.add, ROUND_HALF_EVEN
    BT = [0] * (N + 1)
    AA = [0] * (N + 1)
    KS = [0] * (N + 1)
    CS = Dc(0)
    for m in range(1, N + 1):
        l = ln(Dc(m))
        z = mul(t4, mul(l, l))
        bt = ex(z)
        aa = ex(add(z, mul(y, l)))
        ks = ex(mul(sg, l).copy_negate())
        BT[m] = int(mul(bt, UD).to_integral_value(rounding=rnd))
        AA[m] = int(mul(aa, UD).to_integral_value(rounding=rnd))
        KS[m] = int(mul(ks, UD).to_integral_value(rounding=rnd))
        if m >= 2:
            CS = add(CS, mul(mul(aa, ks), l))
    return BT, AA, KS, CS


def main_sum(N, P, sc, BT, AA, KS):
    nP = len(P)
    nmask = 1 << nP
    # fixed-point lambda (signed) and G^-sigma for every mask
    LAM = {}
    G0S = {}
    for mask, (sgn, mag, d) in sc["lam"].items():
        LAM[mask] = sgn * int(CN.multiply(mag.mid(), UD).to_integral_value(rounding=ROUND_HALF_EVEN))
    sg = sc["sigma"].mid()
    for mask, (_, _, d) in sc["lam"].items():
        G0S[mask] = int(CN.multiply(CN.exp(CN.multiply(sg, CN.ln(Dc(d))).copy_negate()), UD)
                        .to_integral_value(rounding=ROUND_HALF_EVEN))
    val = {mask: sc["lam"][mask][2] for mask in range(nmask)}
    # for each G: list of (e, lambda_{G/e}) over submasks e of G, sorted by e
    PAIRS = {}
    for G in range(nmask):
        lst = []
        sub = G
        while True:
            lst.append((val[sub], LAM[G & ~sub]))
            if sub == 0:
                break
            sub = (sub - 1) & G
        lst.sort()
        PAIRS[G] = lst
    # supersets of each mask, with their pair lists and G^-sigma
    SUP = []
    for Kk in range(nmask):
        SUP.append([(G, PAIRS[G], G0S[G]) for G in range(nmask) if G & Kk == Kk])
    # prime mask of k
    pm = bytearray(N + 1)
    for i, p in enumerate(P):
        bit = 1 << i
        for k in range(p, N + 1, p):
            pm[k] |= bit
    Gfix = int(CN.multiply(sc["g"].mid(), UD).to_integral_value(rounding=ROUND_HALF_EVEN))
    S = 0
    NSsum = 0
    NT = 0
    INC = 0
    for k in range(1, N + 1):
        emax = N // k
        ksk = KS[k]
        for G, pairs, g0s in SUP[pm[k]]:
            if k == 1 and G == 0:
                continue                     # n = 1 (G = 1, k = 1) is the leading term
            B2 = 0
            A2 = 0
            for e, lam in pairs:
                if e > emax:
                    break
                m = e * k
                B2 += lam * BT[m]
                A2 += lam * AA[m]
                INC += 1
            Bt = B2 >> K
            At = A2 >> K
            Wt = (Bt if Bt >= 0 else -Bt) + ((Gfix * (At if At >= 0 else -At)) >> K)
            NSt = (g0s * ksk) >> K
            S += (Wt * NSt) >> K
            NSsum += NSt
            NT += 1
    return dict(S=S, NSsum=NSsum, NT=NT, INC=INC, LAM=LAM, G0S=G0S, Gfix=Gfix)


def error_bound_S(N, P, sc, BT, AA, KS, ms, rho):
    """Rigorous bound E_S (units of 2^-K) with |S_fixed - S_N U| <= E_S, U = 2^K.

    Table errors (units): an entry V of a value v with relative error <= rho
    satisfies |V - vU| <= rho vU + 1/2 + 1e-6, so dT = ceil(rho (Vmax + 2)) + 1
    bounds it.  lambda and g come from rigorous intervals: |V - vU| <= width U + 1.
    With Lmax, Bmax, Amax the largest |LAM|, BT, AA entries and c = 2^|P| the
    largest number of incidences of one n:
      B2 = sum LAM BT is exact; |B2 - B U^2| <= c (Lmax dBT + (Bmax + dBT) dL)
      eB  = ceil(c (Lmax dBT + (Bmax + dBT) dL) / U) + 1  >= |Bt - B U|
      eA  = ceil(c (Lmax dAA + (Amax + dAA) dL) / U) + 1  >= |At - A U|
      |A| <= Ar = ceil(c (Lmax + dL)(Amax + dAA) / U^2)     (a real bound)
      eW  = eB + eA + dG Ar + ceil(dG eA / U) + 1          >= |Wt - w U|   (g <= 1)
      eNS = dKS + dG0 + ceil(dG0 dKS / U) + 1              >= |NSt - ns U| (both factors <= 1)
      w  <= Wr = ceil(c (Lmax + dL)(Bmax + dBT + Amax + dAA) / U^2)
      |Tt - w ns U| <= Wr eNS + ns eW + eW eNS / U + 1.
    Summing over the NT values of n and using sum ns <= (NSsum + NT eNS)/U:
      E_S = NT (Wr eNS + ceil(eW eNS / U) + 1) + ceil(eW (NSsum + NT eNS) / U)."""
    Lmax = max(abs(v) for v in ms["LAM"].values())
    Bmax = max(BT)
    Amax = max(AA)
    Kmax = max(KS)
    Gmax = max(ms["G0S"].values())

    def dT(vmax):
        return int(CC.multiply(rho, Dc(vmax + 2)).to_integral_value(rounding=ROUND_CEILING)) + 1

    def dW(iv):
        return int(CC.multiply(iv.width(), UD).to_integral_value(rounding=ROUND_CEILING)) + 1

    dBT, dAA, dKS, dG0 = dT(Bmax), dT(Amax), dT(Kmax), dT(Gmax)
    dL = max(dW(mag) for (_, mag, _) in sc["lam"].values())
    dG = dW(sc["g"])
    c = 1 << len(P)

    def cdiv(x, y):
        return -(-x // y)

    eB = cdiv(c * (Lmax * dBT + (Bmax + dBT) * dL), U) + 1
    eA = cdiv(c * (Lmax * dAA + (Amax + dAA) * dL), U) + 1
    Ar = cdiv(c * (Lmax + dL) * (Amax + dAA), U * U)
    eW = eB + eA + dG * Ar + cdiv(dG * eA, U) + 1
    eNS = dKS + dG0 + cdiv(dG0 * dKS, U) + 1
    Wr = cdiv(c * (Lmax + dL) * (Bmax + dBT + Amax + dAA), U * U)
    NT = ms["NT"]
    E = NT * (Wr * eNS + cdiv(eW * eNS, U) + 1) + cdiv(eW * (ms["NSsum"] + NT * eNS), U)
    return E, dict(dBT=dBT, dAA=dAA, dKS=dKS, dG0=dG0, dL=dL, dG=dG, eB=eB, eA=eA, eW=eW,
                   eNS=eNS, Ar=Ar, Wr=Wr, c=c)


def certify_row(N, verbose=False):
    t_start = time.time()
    P = leg_primes(N)
    sc = row_scalars(N, P=P)
    rho_needed = rho_bound(N, sc)
    assert rho_needed <= RHO, (rho_needed, RHO)
    BT, AA, KS, CS = build_tables(N, sc)
    t_tab = time.time() - t_start
    ms = main_sum(N, P, sc, BT, AA, KS)
    E, eparts = error_bound_S(N, P, sc, BT, AA, KS, ms, RHO)
    t_sum = time.time() - t_start - t_tab
    S = Iv(CF.divide(Dc(ms["S"] - E), UD), CC.divide(Dc(ms["S"] + E), UD))
    # corr: kappa ln m <= m^kappa - 1 <= kappa ln m N^kappa; CS relative error <= 1e-35
    lnN = iln(Iv(N))
    CSi = Iv(CF.multiply(CS, 1 - Dc("1e-35")), CC.multiply(CS, 1 + Dc("1e-35")))
    C_N = Iv(CF.multiply(sc["kappa"].lo, CSi.lo),
             CC.multiply(CC.multiply(sc["kappa"].hi, iexp(sc["kappa"] * lnN).hi), CSi.hi))
    g, M = sc["g"], sc["M"]
    Q = 1 - g - S
    if Q.lo <= 0:
        raise RuntimeError("numerator not certified positive")
    L = Q / M - g * C_N
    stored = STORED.get(N)
    rec = {
        "N": N, "primes": list(P), "D": eval("*".join(map(str, P))),
        "t": str(T0), "y_squared": str(Y0SQ),
        "g_N": [str(g.lo), str(g.hi)], "sigma_N": [str(sc["sigma"].lo), str(sc["sigma"].hi)],
        "kappa_N": [str(sc["kappa"].lo), str(sc["kappa"].hi)],
        "M_N": [str(M.lo), str(M.hi)],
        "S_N": [str(S.lo), str(S.hi)],
        "g_N_C_N_upper": str((g * C_N).hi),
        "L_N": [str(L.lo), str(L.hi)],
        "L_N_width": str(L.width()),
        "number_of_n": ms["NT"], "incidences": ms["INC"],
        "fixed_point_error_units": E, "fixed_point_scale_bits": K,
        "relative_table_error_bound_used": str(RHO), "relative_table_error_bound_needed": str(rho_needed),
        "error_parts": eparts,
        "seconds_tables": round(t_tab, 1), "seconds_sum": round(t_sum, 1),
    }
    if stored is not None:
        T = Dc(stored[0])
        rec["stored_floor"] = stored[0]
        rec["stored_shard"] = stored[1]
        rec["stored_first_of_run"] = stored[2]
        rec["stored_t_box"] = stored[3]
        rec["stored_le_certified_lower"] = bool(T <= L.lo)
        rec["stored_gt_certified_upper"] = bool(T > L.hi)
        rec["certified_lower_minus_stored"] = str(CF.subtract(L.lo, T))
        E12 = Dc(10) ** 12
        fl_lo = CF.multiply(L.lo, E12).to_integral_value(rounding=ROUND_FLOOR)
        fl_hi = CF.multiply(L.hi, E12).to_integral_value(rounding=ROUND_FLOOR)
        rec["floor12_of_L"] = [str(fl_lo), str(fl_hi)]
        rec["floor12_matches_stored"] = bool(fl_lo == fl_hi == CN.multiply(T, E12))
    if N == 690988:
        rec["certified_lower_minus_E_max_package"] = str(CF.subtract(L.lo, E_MAX_PACKAGE))
    if verbose:
        print(json.dumps(rec), file=sys.stderr)
    return rec


# ----------------------------------------------------------------------------
# Self-test: brute force over all n <= DN for small N, same formulas
# ----------------------------------------------------------------------------
def brute_force_L(N, P, sc):
    from decimal import localcontext
    with localcontext(CN):
        return _brute_force_L(N, P, sc)


def _brute_force_L(N, P, sc):
    t4 = CN.divide(sc["t"].mid(), 4)
    y = sc["y"].mid()
    sg = sc["sigma"].mid()
    g = sc["g"].mid()
    D = 1
    for p in P:
        D *= p
    lam = {}
    for mask, (sgn, mag, d) in sc["lam"].items():
        lam[d] = sgn * mag.mid()
    bt = lambda m: CN.exp(CN.multiply(t4, CN.multiply(CN.ln(Dc(m)), CN.ln(Dc(m)))))
    S = Dc(0)
    for n in range(2, D * N + 1):
        B = Dc(0)
        A = Dc(0)
        act = False
        for d, ld in lam.items():
            if n % d == 0 and n <= d * N:
                act = True
                m = n // d
                B += ld * bt(m)
                A += ld * bt(m) * CN.exp(CN.multiply(y, CN.ln(Dc(m))))
        if act:
            S += (B.copy_abs() + g * A.copy_abs()) * CN.exp(CN.multiply(sg, CN.ln(Dc(n))).copy_negate())
    M = sc["M"].mid()
    kap = sc["kappa"].mid()
    C = Dc(0)
    for m in range(2, N + 1):
        l = CN.ln(Dc(m))
        C += bt(m) * (CN.exp(kap * l) - 1) * CN.exp((y - sg) * l)
    return (1 - g - S) / M - g * C, S


def selftest():
    out = []
    for N, P in [(37, (2, 3, 5, 7, 11)), (61, (2, 3, 5, 7)), (150, (2, 3, 5)), (999, (2, 3))]:
        sc = row_scalars(N, P=P)
        BT, AA, KS, CS = build_tables(N, sc)
        ms = main_sum(N, P, sc, BT, AA, KS)
        E, _ = error_bound_S(N, P, sc, BT, AA, KS, ms, RHO)
        Lb, Sb = brute_force_L(N, P, sc)
        Sfix = CN.divide(Dc(ms["S"]), UD)
        diff_units = abs(CN.multiply(CN.subtract(Sfix, Sb), UD))
        ok = diff_units <= E + 10 ** 6   # 10^6 units ~ 8e-28 covers the brute force's own ~1e-40 error
        out.append({"N": N, "primes": list(P), "S_bruteforce": str(Sb), "S_fixed": str(Sfix),
                    "difference": str(CN.subtract(Sfix, Sb)), "error_bound": str(CN.divide(Dc(E), UD)), "agree": bool(ok)})
        if not ok:
            raise SystemExit("SELFTEST FAILED: %r" % out[-1])
    return out


def check_package(pkgdir, rows):
    """Re-read the stored floors from the pinned package's shards (hash-checked)."""
    seen = {}
    for shard in sorted({STORED[N][1] for N in rows if N in STORED}):
        path = os.path.join(pkgdir, "certificates", shard)
        h = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if h != SHARD_SHA256[shard]:
            raise SystemExit("hash mismatch for %s" % shard)
        first = False
        for line in gzip.open(path, "rt"):
            if line.startswith("TBOX"):
                first = True
                continue
            m = re.match(r"N (\d+) L12 (0\.\d{12}) ", line)
            if m:
                N = int(m.group(1))
                if N in rows:
                    seen[N] = (m.group(2), first)
                first = False
    for N in rows:
        if N in STORED and (seen[N][0] != STORED[N][0] or seen[N][1] != STORED[N][2]):
            raise SystemExit("embedded stored value differs from package for N=%d" % N)
    return {str(N): seen[N][0] for N in sorted(seen)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rows", default=None, help="comma-separated N values")
    ap.add_argument("--set", default="weakest", choices=sorted(SETS))
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--output", default=None)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--package", default=None, help="path to a clone of the pinned package")
    a = ap.parse_args()
    rows = [int(x) for x in a.rows.split(",")] if a.rows else SETS[a.set]
    rec = {
        "title": "Certified independent replay of finite-lane Triangle rows (Gomila package)",
        "date": "2026-10-12",
        "model": "Claude Opus 5.5 (claude-opus-5-5)",
        "source_package": PACKAGE,
        "method": "enumeration n = gcd(n,D) k; decimal tables at 45 digits (correctly rounded "
                  "exp/ln/sqrt); exact integer fixed point at scale 2^110 with an a-priori rounding "
                  "bound; directed-rounding intervals for g, sigma, kappa, M, C",
        "rows_requested": rows,
    }
    if a.selftest:
        rec["selftest"] = selftest()
    if a.package:
        rec["package_stored_values_checked"] = check_package(a.package, rows)
    if a.jobs > 1 and len(rows) > 1:
        import multiprocessing as mp
        # largest rows first for load balance
        order = sorted(rows, key=lambda N: -N * (1 << len(leg_primes(N))))
        with mp.Pool(a.jobs) as pool:
            res = dict(zip(order, pool.map(certify_row, order)))
        results = [res[N] for N in rows]
    else:
        results = [certify_row(N) for N in rows]
    rec["rows"] = results
    summary = {
        "all_stored_floors_below_certified_lower_bound": all(r.get("stored_le_certified_lower", True) for r in results),
        "any_stored_floor_above_certified_upper_bound": any(r.get("stored_gt_certified_upper", False) for r in results),
        "first_of_run_singleton_rows_reproduced_to_12_decimals": [
            r["N"] for r in results if r.get("stored_first_of_run") and r.get("stored_t_box") == "singleton"
            and r.get("floor12_matches_stored")],
    }
    rec["summary"] = summary
    rec["software"] = {"python": platform.python_version(), "implementation": platform.python_implementation()}
    with open(__file__, "rb") as fh:
        rec["checker_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rec, indent=1)
    if a.output:
        with open(a.output, "w") as fh:
            fh.write(out + "\n")
        print("wrote", a.output)
    else:
        print(out)
    if not summary["all_stored_floors_below_certified_lower_bound"] or summary["any_stored_floor_above_certified_upper_bound"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
