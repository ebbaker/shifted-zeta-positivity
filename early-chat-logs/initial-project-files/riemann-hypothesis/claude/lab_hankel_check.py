"""
lab_hankel_check.py -- certification for memo4 (geometric reformulation), Aug 2026.

Certifies, at high precision:
  (1) Hermite's theorem: for a real polynomial with r distinct real roots and c
      conjugate pairs, the Hankel form of the power sums has signature (r+c, c),
      so #negative eigenvalues == number of "zero spheres", exactly.
  (2) The same form on Xi via the convergent reciprocal-square moments
      m_k = sum_n gamma_n^{-2k}, t_n = gamma_n^{-2}; full-rank Hankel; and the
      determinant identity det = prod t_i * prod_{i<j} (t_i - t_j)^2, so
      sign(det) = (-1)^c.
  (3) The sensitivity law: a sphere of radius y0 at height a enters through the
      single factor (t - tbar)^2 = -4 (Im t)^2 ~ -16 y0^2 / a^6, so the relative
      size of the violation is quadratic in y0 (log-log slope -> 2.000).
  (4) The resolution cost: log10|det| ~ -3.2 n^2 in the number of zeros carried,
      and a truncated K x K Hankel with K < #atoms is SILENT (not wrong) about an
      implanted sphere.

Run: python3 lab_hankel_check.py    (mpmath only; ~2 minutes)
"""

from mpmath import mp, mpf, mpc, matrix, det, zetazero, sqrt, log, fabs

mp.dps = 120


def hankel(moments, K, shift=0):
    """(m_{i+j+shift}) for i,j < K, moments indexed from 1."""
    return matrix([[moments[i + j + shift] for j in range(K)] for i in range(K)])


def minors(H):
    """Leading principal minors D_1..D_K."""
    K = H.rows
    out = []
    for k in range(1, K + 1):
        out.append(det(matrix([[H[i, j] for j in range(k)] for i in range(k)])))
    return out


def n_negative(H):
    """#negative eigenvalues via sign changes of 1, D_1, ..., D_K (Jacobi)."""
    seq = [mpf(1)] + minors(H)
    changes = 0
    for a, b in zip(seq, seq[1:]):
        if a == 0 or b == 0:
            return None  # degenerate; count undefined by this method
        if (a > 0) != (b > 0):
            changes += 1
    return changes


def power_sums(roots, kmax):
    """s_k = sum r^k, k = 0..kmax."""
    return [sum((r ** k for r in roots), mpc(0)) for k in range(kmax + 1)]


# ----------------------------------------------------------------------------
print("=" * 74)
print("TEST 1  Hermite: #negative eigenvalues of Hankel(power sums) = #conj pairs")
print("=" * 74)

cases = [
    ("(x-1)(x-2)                  ", [mpf(1), mpf(2)]),
    ("(x^2+1)                     ", [mpc(0, 1), mpc(0, -1)]),
    ("(x-1)(x-2)(x-3)(x-4)        ", [mpf(k) for k in (1, 2, 3, 4)]),
    ("(x-1)(x-2)(x^2+1)           ", [mpf(1), mpf(2), mpc(0, 1), mpc(0, -1)]),
    ("(x^2+1)(x^2+4)              ", [mpc(0, 1), mpc(0, -1), mpc(0, 2), mpc(0, -2)]),
    ("(x-1)(x-2)(x-3)((x-5)^2+.01)", [mpf(1), mpf(2), mpf(3),
                                      mpc(5, mpf("0.1")), mpc(5, mpf("-0.1"))]),
]
for name, roots in cases:
    n = len(roots)
    c = sum(1 for r in roots if abs(mp.im(r)) > mpf("1e-40")) // 2
    s = power_sums(roots, 2 * n - 2)
    H = matrix([[mp.re(s[i + j]) for j in range(n)] for i in range(n)])
    nn = n_negative(H)
    print(f"  {name}  deg={n}  conj pairs={c}   #neg eig={nn}   {'OK' if nn == c else 'MISMATCH'}")

# ----------------------------------------------------------------------------
print()
print("=" * 74)
print("TEST 2  the same form on Xi, from reciprocal-square moments")
print("=" * 74)

NZ = 40      # zeros used (one per +/- pair)
K = 6        # Hankel size

print(f"  computing first {NZ} Riemann zero ordinates ...")
gam = [mp.im(zetazero(n)) for n in range(1, NZ + 1)]
print(f"  gamma_1 = {mp.nstr(gam[0], 12)}   gamma_{NZ} = {mp.nstr(gam[-1], 12)}")


def moments_from_ordinates(ords, kmax):
    """m_k = sum t^k with t = gamma^{-2}, k = 1..kmax."""
    ts = [1 / (g ** 2) for g in ords]
    return [None] + [sum((t ** k for t in ts), mpc(0)) for k in range(1, kmax + 1)]


def report(label, ords):
    m = moments_from_ordinates(ords, 2 * K + 2)
    A = matrix([[mp.re(m[i + j + 1]) for j in range(K)] for i in range(K)])
    B = matrix([[mp.re(m[i + j + 2]) for j in range(K)] for i in range(K)])
    na, nb = n_negative(A), n_negative(B)
    print(f"  {label}")
    print(f"      Hankel(m_{{i+j+1}}) {K}x{K}: #neg eig = {na}")
    print(f"      Hankel(m_{{i+j+2}}) {K}x{K}: #neg eig = {nb}")
    return na, nb


print()
report("RH-true data (all ordinates real)", gam)

print()
print("  implanting an off-line quadruple in place of two real ordinates")
print("  (same device as lab_run_si_check.py: two ordinates near 100 -> +/-a +/- i*y0)")
idx = [i for i, g in enumerate(gam) if 95 < g < 105]
print(f"      replacing ordinates {[mp.nstr(gam[i], 10) for i in idx[:2]]}")

for y0 in ["0.25", "0.1", "0.03", "0.01", "0.003"]:
    y = mpf(y0)
    a = mpf("100.0745")
    pert = [g for i, g in enumerate(gam) if i not in idx[:2]]
    pert += [mpc(a, y), mpc(a, -y)]
    m = moments_from_ordinates(pert, 2 * K + 2)
    A = matrix([[mp.re(m[i + j + 1]) for j in range(K)] for i in range(K)])
    B = matrix([[mp.re(m[i + j + 2]) for j in range(K)] for i in range(K)])
    na, nb = n_negative(A), n_negative(B)
    # size of the violation: last leading minor, normalised by the RH-true one
    mref = moments_from_ordinates(gam, 2 * K + 2)
    Aref = matrix([[mp.re(mref[i + j + 1]) for j in range(K)] for i in range(K)])
    dA, dAref = minors(A)[-1], minors(Aref)[-1]
    ratio = dA / dAref
    print(f"      y0={y0:>6}:  #neg eig (A,B) = ({na},{nb});   "
          f"D_{K}(A)/D_{K}(A_RH) = {mp.nstr(ratio, 8)}")


# ============================================================================
# PART 2: full rank, sensitivity, resolution cost
# ============================================================================

from mpmath import mp, mpf, mpc, matrix, det, zetazero

mp.dps = 400


def minors(H):
    K = H.rows
    return [det(matrix([[H[i, j] for j in range(k)] for i in range(k)]))
            for k in range(1, K + 1)]


def n_negative(H):
    seq = [mpf(1)] + minors(H)
    ch = 0
    for a, b in zip(seq, seq[1:]):
        if a == 0 or b == 0:
            return None
        if (a > 0) != (b > 0):
            ch += 1
    return ch


def full_hankel(atoms):
    """Hankel of the weighted measure sum t*delta_t: entries m_{i+j+1}."""
    n = len(atoms)
    mom = [sum((t ** k for t in atoms), mpc(0)) for k in range(1, 2 * n + 1)]
    return matrix([[mp.re(mom[i + j]) for j in range(n)] for i in range(n)])


def vandermonde_form(atoms):
    """prod t_i * prod_{i<j} (t_i - t_j)^2  -- the closed form for det."""
    p = mpc(1)
    for t in atoms:
        p *= t
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            p *= (atoms[i] - atoms[j]) ** 2
    return mp.re(p)


N = 8
print(f"computing first {N} Riemann zero ordinates ...")
gam = [mp.im(zetazero(n)) for n in range(1, N + 1)]
print("  ", [mp.nstr(g, 10) for g in gam])

print()
print("=" * 78)
print("(i)-(ii)  full-rank Hankel: negative-eigenvalue count and det identity")
print("=" * 78)


def atoms_from(ords):
    return [1 / (g ** 2) for g in ords]


H = full_hankel(atoms_from(gam))
d, v = minors(H)[-1], vandermonde_form(atoms_from(gam))
print(f"  all real:            #neg eig = {n_negative(H)}   "
      f"det = {mp.nstr(d, 8)}   closed form = {mp.nstr(v, 8)}   "
      f"match = {mp.nstr(abs(d / v - 1), 3)}")

# implant c conjugate pairs by replacing real ordinates
for c, y0 in [(1, "0.25"), (1, "0.05"), (2, "0.25"), (3, "0.25")]:
    y = mpf(y0)
    ords = list(gam)
    for k in range(c):
        ords[2 * k] = mpc(mp.re(ords[2 * k]), y)
        ords[2 * k + 1] = mpc(mp.re(ords[2 * k]), -y)
    at = atoms_from(ords)
    H = full_hankel(at)
    nn = n_negative(H)
    d, v = minors(H)[-1], vandermonde_form(at)
    ok = "OK" if nn == c else "MISMATCH"
    print(f"  c={c} pairs, y0={y0:>5}:  #neg eig = {nn}  {ok}   "
          f"sign(det) = {'+' if d > 0 else '-'} (expect {'+' if c % 2 == 0 else '-'})   "
          f"det/closed-form-1 = {mp.nstr(abs(d / v - 1), 3)}")

print()
print("=" * 78)
print("(iii)  sensitivity: relative size of the violation vs sphere radius y0")
print("=" * 78)
print("      predicted   |det_pert/det_real| ~ 16 y0^2 / a^6  (relative to the")
print("      factor it replaces), so log-log slope in y0 should be 2")
print()
a = mp.re(gam[0])          # implant at the height of the first ordinate
base = atoms_from(gam)
Hb = full_hankel(base)
db = minors(Hb)[-1]
prev = None
for y0s in ["0.4", "0.2", "0.1", "0.05", "0.025", "0.0125"]:
    y = mpf(y0s)
    ords = list(gam)
    ords[0] = mpc(a, y)
    ords[1] = mpc(a, -y)
    at = atoms_from(ords)
    d = minors(full_hankel(at))[-1]
    t = 1 / (mpc(a, y) ** 2)
    pred = -4 * (mp.im(t)) ** 2
    r = abs(d)
    line = f"  y0={y0s:>7}:  |det| = {mp.nstr(r, 6)}   (t-tbar)^2 = {mp.nstr(pred, 6)}"
    if prev is not None:
        slope = mp.log(r / prev[0]) / mp.log(y / prev[1])
        line += f"   log-log slope = {mp.nstr(slope, 6)}"
    print(line)
    prev = (r, y)

print()
print("=" * 78)
print("(iv)  cost of resolution: det magnitude vs number of zeros carried")
print("=" * 78)
for n in range(3, 13):
    g = [mp.im(zetazero(k)) for k in range(1, n + 1)]
    at = atoms_from(g)
    d = vandermonde_form(at)
    print(f"  n={n:>3} zeros:  det(full Hankel) = {mp.nstr(d, 6)}"
          f"   log10 = {mp.nstr(mp.log(abs(d), 10), 6)}")
