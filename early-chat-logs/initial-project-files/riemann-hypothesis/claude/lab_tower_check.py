"""
lab_tower_check.py -- checking the obstruction flagged in memo5 §4(b)/§5.

PART 1.  The hyperkaehler Hodge-Riemann tower: which ranks are actually available?
  By Verbitsky, SH^{2k} = Sym^k H^2 for k <= n, and the harmonic (primitive)
  decomposition w.r.t. q_X gives  Sym^k V = sum_j q^j . H^{k-2j}  with
      dim H^m = C(b+m-1, m) - C(b+m-3, m-2),      b = b_2 .
  The Hodge-Riemann relations are DEFINITE exactly on these primitive pieces, so
  these are the ranks at which the tower supplies a definite form.
  Known deformation types: K3^[n] (b=23), Kum_n (b=7), OG6 (b=8), OG10 (b=24).

PART 2.  The trace form of the Jensen polynomials of Xi, computed honestly.
  Xi(z) = 4 int_0^inf Phi(u) cos(zu) du = sum_m a_m z^{2m},  so with
      b_m := (-1)^m a_m = 4 M_{2m} / (2m)!,   M_k := int_0^inf Phi(u) u^k du > 0,
  the function H(w) = Xi(sqrt(-w)) = sum_m b_m w^m has positive coefficients and
  only real negative zeros iff RH.  Jensen polynomials of gamma(m) := m! b_m:
      J^{d,n}(X) = sum_{j=0}^d C(d,j) gamma(n+j) X^j ,
  and RH <=> every J^{d,n} is hyperbolic (Polya).  We compute the trace form of
  R[X]/(J^{d,n}) and inspect its signature AND its entries.
"""
from math import comb
from mpmath import mp, mpf, matrix, det, quad, exp, pi, cos, sqrt, polyroots, factorial

mp.dps = 40

# ---------------------------------------------------------------- PART 1
print("=" * 78)
print("PART 1  hyperkaehler Hodge-Riemann tower: available definite ranks")
print("=" * 78)


def dimH(b, m):
    if m < 0:
        return 0
    return comb(b + m - 1, m) - (comb(b + m - 3, m - 2) if m >= 2 else 0)


types = {"Kum_n": 7, "OG6": 8, "K3^[n]": 23, "OG10": 24}
avail = set()
for name, b in types.items():
    ds = [dimH(b, m) for m in range(0, 10)]
    avail |= set(ds)
    print(f"  {name:>8} (b2={b:>2}): dim H^m for m=0..9 = {ds}")

print()
print("  ranks d = 1..40 that the tower supplies a definite form at:")
hit = sorted(d for d in range(1, 41) if d in avail)
print(f"    {hit}")
print(f"    -> {len(hit)} of the first 40 ranks are reachable.")
print("  (RH needs hyperbolicity of J^{d,n} for EVERY d, i.e. a definite form of")
print("   every rank d = 1, 2, 3, ...)")

# ---------------------------------------------------------------- PART 2
print()
print("=" * 78)
print("PART 2  trace forms of the Jensen polynomials of Xi")
print("=" * 78)


def Phi(u):
    """Riemann's kernel: Xi(z) = 4 int_0^inf Phi(u) cos(zu) du."""
    s = mpf(0)
    n = 1
    while True:
        t = (2 * pi ** 2 * n ** 4 * exp(mpf(9) * u / 2)
             - 3 * pi * n ** 2 * exp(mpf(5) * u / 2)) * exp(-pi * n ** 2 * exp(2 * u))
        s += t
        if n > 3 and abs(t) < mpf(10) ** (-mp.dps - 5):
            break
        n += 1
        if n > 60:
            break
    return s


NM = 26
print(f"  computing moments M_k = int Phi(u) u^k du for k = 0..{2*(NM-1)} ...")
M = [quad(lambda u: Phi(u) * u ** k, [0, 4]) for k in range(0, 2 * NM, 2)]
b = [4 * M[m] / factorial(2 * m) for m in range(NM)]

# sanity: 4*M_0 = Xi(0) = xi(1/2)
xi_half = mpf("0.4971207174")
print(f"  check  4*M_0 = {mp.nstr(4*M[0], 12)}   vs  xi(1/2) = {xi_half}"
      f"   rel err {mp.nstr(abs(4*M[0]/xi_half - 1), 3)}")
print(f"  b_0..b_4 = {[mp.nstr(x, 10) for x in b[:5]]}   (all > 0: {all(x > 0 for x in b)})")

gamma = [factorial(m) * b[m] for m in range(NM)]


def jensen(d, n):
    """coefficients ascending: J^{d,n}(X) = sum_j C(d,j) gamma(n+j) X^j"""
    return [comb(d, j) * gamma[n + j] for j in range(d + 1)]


def trace_form(coeffs_asc):
    """Gram matrix of Tr(x^2) on R[X]/(p), i.e. Hankel of power sums."""
    d = len(coeffs_asc) - 1
    desc = [c for c in reversed(coeffs_asc)]
    rts = polyroots(desc, maxsteps=400, extraprec=400)
    s = [sum((r ** k for r in rts), mp.mpc(0)) for k in range(2 * d)]
    G = matrix([[mp.re(s[i + j]) for j in range(d)] for i in range(d)])
    return G, rts


def n_neg(G):
    K = G.rows
    mins = [det(matrix([[G[i, j] for j in range(k)] for i in range(k)]))
            for k in range(1, K + 1)]
    seq = [mpf(1)] + mins
    ch = 0
    for x, y in zip(seq, seq[1:]):
        if x == 0 or y == 0:
            return None
        if (x > 0) != (y > 0):
            ch += 1
    return ch


print()
print(f"  {'(d,n)':>8} {'#neg eig':>9} {'nonreal roots':>14} {'hyperbolic':>11}")
for d in range(2, 7):
    for n in (0, 1, 3):
        c = jensen(d, n)
        G, rts = trace_form(c)
        nr = sum(1 for r in rts if abs(mp.im(r)) > mpf("1e-25"))
        nn = n_neg(G)
        print(f"  {str((d,n)):>8} {str(nn):>9} {nr:>14} {'yes' if nr == 0 else 'NO':>11}")

print()
print("=" * 78)
print("PART 3  what the trace form's entries actually are")
print("=" * 78)
G, _ = trace_form(jensen(3, 0))
print("  Gram matrix of Tr(x^2) on R[X]/(J^{3,0}), first rows:")
for i in range(G.rows):
    print("    [" + "  ".join(mp.nstr(G[i, j], 12).rjust(16) for j in range(G.cols)) + "]")
print()
print("  eigenvalue signs via leading minors:", n_neg(G), "negative")
print("  -> the form is positive definite, hence isometric OVER R to the identity.")
print("  The entries are power sums of roots of a polynomial whose coefficients are")
print("  gamma(m) = 4 m! M_{2m}/(2m)!  with M_k = int Phi(u)u^k du: transcendental-")
print("  looking reals carrying no known Q-structure.  Over R, signature is a")
print("  COMPLETE invariant of a quadratic form, so there is nothing for a")
print("  geometric realization to match.")
