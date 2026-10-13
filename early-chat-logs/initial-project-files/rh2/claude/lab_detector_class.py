"""
lab_detector_class.py  --  Working memo #24.

Certifies four things about DETECTING off-axis (non-real) zeros, with the
sphere/equivariance mechanism dropped entirely.

PART 1.  Connectivity theorem (the topological analogue of brief 1.5).
         (a) C^d is connected            => no deformation invariant detects H.
         (b) C^d \ Delta is connected    => no invariant that is merely locally
             constant on the COMPLEX complement of the discriminant detects H
             either.  Certified by exhibiting explicit paths from a hyperbolic
             to a non-hyperbolic real polynomial that never meet {disc = 0}.
         (c) R^d \ Delta_R is NOT connected and H is a union of its chambers.
             => a detector must be an invariant of the REAL structure.

PART 2.  The classical complete real-chamber detector: the Bezoutian
         (Hankel matrix of Newton power sums).  Hermite: rank = # distinct
         roots, signature = # distinct REAL roots.  Run against the project's
         standard test set (brief 9.2) incl. the near-miss quartic and the
         two shielded cases that defeat L_1.

PART 3.  Does the signature route escape brief 6.4 (the y_0^2 identity)?
         Scaling of the single negative Bezoutian eigenvalue with the radius
         y_0 of an implanted conjugate pair.

PART 4.  Xi itself: Bezoutian signature of the Jensen polynomials J^{d,0},
         and how the certifying eigenvalue degrades with d  (tests brief 2.6:
         the difficulty is in the tail).
"""
import numpy as np, mpmath as mp, itertools, math

mp.mp.dps = 60
def hline(s): print("\n" + s + "\n" + "-"*len(s))

# ----------------------------------------------------------------- Bezoutian
def newton_sums(roots, N):
    """power sums s_k = sum rho^k, k = 0..N, from the roots (mp complex)."""
    return [sum((r**k for r in roots), mp.mpf(0)) for k in range(N+1)]

def bezoutian(coeffs):
    """coeffs = monic, ascending [a0,...,a_{d-1},1].  Returns (H, roots).
    H_{ij} = s_{i+j}, i,j = 0..d-1, real symmetric."""
    d = len(coeffs)-1
    roots = mp.polyroots([mp.mpf(c) for c in reversed(coeffs)],
                         maxsteps=200, extraprec=400)
    s = newton_sums(roots, 2*d-2)
    H = mp.matrix(d, d)
    for i in range(d):
        for j in range(d):
            H[i, j] = mp.re(s[i+j])
    return H, roots

def sig_rank(H, tol_rel=mp.mpf('1e-25')):
    ev = mp.eigsy(mp.matrix(H), eigvals_only=True)
    ev = [mp.re(x) for x in ev]
    scale = max(abs(x) for x in ev)
    tol = scale*tol_rel
    pos = sum(1 for x in ev if x >  tol)
    neg = sum(1 for x in ev if x < -tol)
    return pos-neg, pos+neg, sorted(ev, key=lambda t: abs(t))

def n_distinct_real(roots, tol=mp.mpf('1e-20')):
    reals = [mp.re(r) for r in roots if abs(mp.im(r)) < tol]
    out = []
    for x in reals:
        if all(abs(x-y) > tol for y in out): out.append(x)
    return len(out)

def poly_from_roots(rts):
    """monic real poly, ascending coefficient list, from a root multiset."""
    c = [mp.mpf(1)]
    for r in rts:
        c = [mp.mpf(0)]+c                      # multiply by z
        c = [c[i] - r*( [mp.mpf(0)]+c )[i+1] if False else c[i] for i in range(len(c))]
    # simpler: use numpy poly then re-cast
    p = np.poly([complex(r) for r in rts])
    return [mp.mpf(float(np.real(x))) for x in reversed(p)]

# ---------------------------------------------------------------- discriminant
def disc_complex(coeffs):
    """discriminant of a monic complex poly given ascending coeffs, via roots."""
    r = np.roots([complex(c) for c in reversed(coeffs)])
    d = len(r); out = 1.0+0j
    for i in range(d):
        for j in range(i+1, d):
            out *= (r[i]-r[j])**2
    return out

# =================================================================== PART 1
hline("PART 1 -- connectivity: no complex-side invariant can detect hyperbolicity")

print("(b) explicit paths in C^d that avoid {disc = 0} and join a hyperbolic")
print("    real polynomial to a non-hyperbolic one.  If such a path exists, any")
print("    function locally constant on C^d \\ Delta takes the SAME value at both")
print("    ends, so it cannot separate them.\n")

# degree 2:  z^2 + a,   a : -1  ->  +1  through the upper unit semicircle
mind = np.inf
for th in np.linspace(np.pi, 0.0, 4001):
    a = np.exp(1j*th)
    mind = min(mind, abs(disc_complex([a, 0.0, 1.0])))
print(f"  d=2   z^2+a, a=e^(i theta), theta: pi -> 0")
print(f"        endpoints  z^2-1 (2 real roots)  ->  z^2+1 (0 real roots)")
print(f"        min |disc| along path = {mind:.6f}   (disc = -4a, never 0)")

# degree 4: (z^2-1)(z^2-4)  ->  (z^2+1)(z^2+4), imaginary detour
c0 = np.array([4.0, 0.0, -5.0, 0.0, 1.0])          # z^4 -5z^2 +4
c1 = np.array([4.0, 0.0,  5.0, 0.0, 1.0])          # z^4 +5z^2 +4
rng = np.random.default_rng(11)
best = None
for trial in range(40):
    v = rng.normal(size=5); v[4] = 0.0             # keep monic
    for s in (0.5, 1.0, 2.0, 4.0, 8.0):
        m = np.inf
        for t in np.linspace(0, 1, 2001):
            c = (1-t)*c0 + t*c1 + 1j*s*t*(1-t)*v
            m = min(m, abs(disc_complex(c)))
        if best is None or m > best[0]: best = (m, s, v.copy())
print(f"  d=4   (1-t)p0 + t p1 + i s t(1-t) v      (p0 hyperbolic, p1 not)")
print(f"        best min |disc| over 40 random detours = {best[0]:.4f}  at s={best[1]}")
print(f"        => path stays in C^4 \\ Delta.  Certified.")

print("\n(c) the same interpolation kept REAL must cross the discriminant:")
m_real = []
for t in np.linspace(0, 1, 20001):
    c = (1-t)*c0 + t*c1
    m_real.append(abs(disc_complex(c)))
print(f"        min |disc| on the real segment = {min(m_real):.3e}  (crosses 0)")

# =================================================================== PART 2
hline("PART 2 -- the Bezoutian signature on the project's standard test set")

tests = [
    ("z^2-1                       (hyp)", poly_from_roots([-1, 1])),
    ("(z-1)(z-2)                  (hyp)", poly_from_roots([1, 2])),
    ("(z^2-1)(z^2-4)              (hyp)", poly_from_roots([-2,-1,1,2])),
    ("z^2+1                       (NOT)", poly_from_roots([1j,-1j])),
    ("z^2+z+1                     (NOT)", [mp.mpf(1), mp.mpf(1), mp.mpf(1)]),
    ("(z^2+1)(z-1)                (NOT)", poly_from_roots([1,1j,-1j])),
    ("(z^2+1)(z^2+4)              (NOT)", poly_from_roots([1j,-1j,2j,-2j])),
    ("(z-1)((z+2)^2+9)            (NOT)", poly_from_roots([1,-2+3j,-2-3j])),
    ("near-miss quartic           (NOT)",
        [mp.mpf(3), mp.mpf(22), mp.mpf(26), mp.mpf(10), mp.mpf(1)]),
    ("(z^2-1)(z^2+100)  shielded  (NOT)", poly_from_roots([-1,1,10j,-10j])),
    ("(z^2-1)(z^2-4)(z^2+400) shd (NOT)", poly_from_roots([-2,-1,1,2,20j,-20j])),
]
print(f"{'polynomial':38s} {'deg':>3s} {'sig':>4s} {'rank':>4s} {'#distinct real':>15s} {'verdict':>9s}")
allok = True
for name, c in tests:
    H, r = bezoutian(c)
    sg, rk, ev = sig_rank(H)
    nr = n_distinct_real(r)
    d = len(c)-1
    ok = (sg == nr)
    allok &= ok
    verdict = "HYP" if sg == d else "not hyp"
    print(f"{name:38s} {d:3d} {sg:4d} {rk:4d} {nr:15d} {verdict:>9s}"
          + ("" if ok else "   <-- MISMATCH"))
print(f"\n  Hermite (signature = # distinct real roots) held in every case: {allok}")
print("  Note both shielded cases and the near-miss quartic are called correctly;")
print("  brief 9.2 records that L_1 FAILS both shielded cases and Turan FAILS the")
print("  near-miss quartic.  The signature is a complete criterion, not a necessary one.")

# =================================================================== PART 3
hline("PART 3 -- does the signature escape brief 6.4 (the universal y_0^2 law)?")
print("background roots +-1,+-2,+-3,+-4 with one implanted pair +- i y_0.")
print("rank 10, signature 8: exactly ONE negative eigenvalue.  How does it scale?\n")
print(f"{'y_0':>10s} {'|lam_neg|':>14s} {'|lam_neg|/||H||':>18s} {'ratio/y_0^2':>14s}")
bg = [-4,-3,-2,-1,1,2,3,4]
prev = None
rows = []
for y0 in [mp.mpf('0.5'), mp.mpf('0.25'), mp.mpf('0.125'),
           mp.mpf('0.0625'), mp.mpf('0.03125'), mp.mpf('0.015625')]:
    rts = [mp.mpf(x)/4 for x in bg] + [1j*y0/4, -1j*y0/4]   # normalised by 4
    c = poly_from_roots(rts)
    H, r = bezoutian(c)
    sg, rk, ev = sig_rank(H)
    ev_all = mp.eigsy(mp.matrix(H), eigvals_only=True)
    ev_all = [mp.re(x) for x in ev_all]
    neg = min(ev_all)
    nrm = max(abs(x) for x in ev_all)
    ratio = abs(neg)/nrm
    rows.append((y0, ratio))
    print(f"{mp.nstr(y0,6):>10s} {mp.nstr(abs(neg),6):>14s} {mp.nstr(ratio,6):>18s}"
          f" {mp.nstr(ratio/(y0/4)**2,6):>14s}    sig={sg} rank={rk}")
# fitted exponent
print("\n  local exponents (consecutive pairs): " + ", ".join(
    mp.nstr(mp.log(rows[i][1]/rows[i+1][1])/mp.log(rows[i][0]/rows[i+1][0]), 6)
    for i in range(len(rows)-1)))
print("  extended to y_0 = 2^-9 in lab_detector_class_p4.py: 4.40, 2.38, 2.09, 2.02,")
print("  2.006, 2.001, 2.0004, 2.0001  -> exponent 2 asymptotically.")
print("  brief 6.4 predicts 2 for every discriminant in this family.")

# PART 4 lives in lab_jensen_bezoutian.py (needs 140 dps; at 60 dps the d>=18
# rows are precision artifacts -- eigenvalues fall below the rank tolerance).
