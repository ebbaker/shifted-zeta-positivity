# Ihara lab round 1 — experiment scripts (concatenated for the project record).
# Split on the "### FILE:" markers to re-run individually; all import lab_ihara_core as lab_core.

############ FILE: v1_validate.py ############
"""Validation of the Ihara-lab core machinery."""
import numpy as np
from mpmath import mp, mpf, mpc, sqrt as msqrt, fabs, cos as mcos, pi as mpi, mpmathify
from lab_core import *

mp.dps = 60
print("=== V1: K4 spectrum + Bass identity + closed-form zeta ===")
A4 = K(4)
G4 = analyze(A4, name="K4")
print("K4 eigs:", [(str(l)[:8], m) for l, m in G4.eigs])
print("Bass identity worst rel err:", bass_check(G4, A4))
# closed form: zeta^{-1} = (1-u^2)^2 (1-u)(1-2u)(1+u+2u^2)^3   [Terras]
u = mpc(0.137, 0.211)
lhs = (1-u**2)**(G4.m - G4.n)
c = charpoly_exact(A4)
x = (1 + G4.q*u**2)/u
lhs *= u**G4.n * sum(mpf(c[k])*x**k for k in range(G4.n+1))
lhs = 1/lhs   # zeta itself
rhs = 1/((1-u**2)**2 * (1-u)*(1-2*u)*(1+u+2*u**2)**3)
print("K4 closed-form zeta match:", fabs(lhs-rhs)/fabs(rhs))

print("\n=== V2: string CF round-trips ===")
# (a) hand 1-mass check: atoms [(t,w)] -> string [1/w, w/t]
ats = [(mpf(2), mpf(3))]
P, Q = poly_from_atoms(ats)
s = string_from_q(P, Q)
print("1-mass string:", [str(x)[:12] for x in s], " expect m=1/3, l=3/2")
# (b) random 4-atom Stieltjes round trip
rng = np.random.default_rng(7)
ats = [(mpf(str(t)), mpf(str(w))) for t, w in zip(sorted(rng.uniform(0.3, 9, 4)), rng.uniform(0.5, 2, 4))]
P, Q = poly_from_atoms(ats)
s = string_from_q(P, Q)
worst = mpf(0)
for _ in range(6):
    z = mpc(*(rng.uniform(-3, -0.5, 2)))
    q1 = sum(w/(t-z) for t, w in ats)
    q2 = q_from_string(s, z)
    worst = max(worst, fabs(q1-q2)/fabs(q1))
print("4-atom round-trip worst rel err:", worst)
print("positivity of CF coeffs:", all(mre(c) > 0 and abs(mim(c)) < 1e-30 for c in s))
print("q(0) = sum w/t =", str(sum(w/t for t, w in ats))[:20], " vs sum of lengths =",
      str(sum(mre(s[i]) for i in range(1, len(s), 2)))[:20])

print("\n=== V3: Petersen string ===")
GP = analyze(petersen(), name="Petersen")
print("Petersen eigs:", [(str(l)[:8], m) for l, m in GP.eigs], "Ramanujan:", GP.ramanujan)
P, Q = poly_from_atoms(atoms(GP))
sP = string_from_q(P, Q)
print("string coeffs (m,l alternating):", [str(mre(c))[:10] for c in sP])
rng = np.random.default_rng(3)
worst = mpf(0)
for _ in range(5):
    z = mpc(*(rng.uniform(-4, -0.5, 2)))
    worst = max(worst, fabs(q_of_z(GP, z) - q_from_string(sP, z))/fabs(q_of_z(GP, z)))
print("Petersen round-trip:", worst)

print("\n=== V4: q_omega at omega=0 equals atom form (all three kinds) ===")
for Gname, Ag in [("prism C9 (excN)", prism(9)), ("prism C17 (excP+excN)", prism(17))]:
    Gg = analyze(Ag, name=Gname)
    print(Gname, "tempered/excP/excN counts:",
          sum(m for _, m in Gg.tempered), sum(m for _, m in Gg.excP), sum(m for _, m in Gg.excN))
    worst = mpf(0)
    rng = np.random.default_rng(11)
    for _ in range(5):
        z = mpc(rng.uniform(-4, 4), rng.uniform(0.3, 3))
        q1 = q_of_z(Gg, z)
        q2 = q_omega(Gg, z, mpf(0))
        worst = max(worst, fabs(q1-q2)/fabs(q1))
    print("  omega=0 consistency:", worst)

print("\n=== V5: Psi checks ===")
GH = analyze(heawood(), name="Heawood")
t = mpf('3.7')
direct = sum(2*m*(1-mcos(tau*t))/tau**2 for tau, m in GH.tempered)
print("Heawood Psi(3.7) series vs closed:", fabs(Psi(GH, t) - direct))
# Siegel-type check: single synthetic real pair growth rate
g = mpc(0, 1)*mpf('0.4')   # delta = 0.4
om = mpf('0.1')
v1 = psi_pair(mpf(40), g, om); v2 = psi_pair(mpf(41), g, om)
print("synthetic real-pair growth rate:", str(mre((v2/v1)))[:12], "expect ~ e^{0.3} =", str(mexp(mpf('0.3')))[:12])
print("\nall validation done")

############ FILE: e2_census.py ############
"""E2: Ramanujan census + string tables for cubic graphs."""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, mpmathify
from lab_core import *

mp.dps = 90

def dumbbell():
    """Two K4-minus-an-edge blobs joined by two edges. 3-regular, n=8."""
    A = np.zeros((8, 8), dtype=object)
    def blob(off):
        for i in range(4):
            for j in range(i+1, 4):
                if (i, j) != (0, 1):
                    A[off+i][off+j] = A[off+j][off+i] = 1
    blob(0); blob(4)
    for (a, b) in [(0, 4), (1, 5)]:
        A[a][b] = A[b][a] = 1
    return A

def dumbbell_long(k):
    """Two K4-minus-edge blobs joined by a ladder of k rungs (prism segment). 3-regular n=8+2k."""
    n = 8 + 2*k
    A = np.zeros((n, n), dtype=object)
    def blob(off):
        for i in range(4):
            for j in range(i+1, 4):
                if (i, j) != (0, 1):
                    A[off+i][off+j] = A[off+j][off+i] = 1
    blob(0); blob(4)
    # ladder vertices 8..8+2k-1 as pairs (8+2i, 8+2i+1)
    prev = (0, 1)
    for i in range(k):
        a, b = 8+2*i, 8+2*i+1
        A[a][b] = A[b][a] = 1
        A[prev[0]][a] = A[a][prev[0]] = 1
        A[prev[1]][b] = A[b][prev[1]] = 1
        prev = (a, b)
    A[prev[0]][4] = A[4][prev[0]] = 1
    A[prev[1]][5] = A[5][prev[1]] = 1
    return A

graphs = [
    ("K4",         K(4)),
    ("K3,3",       Kbip(3, 3)),
    ("cube Q3",    cube()),
    ("crown(4)",   crown(4)),
    ("Petersen",   petersen()),
    ("Heawood",    heawood()),
    ("Desargues",  desargues()),
    ("prism C3",   prism(3)),
    ("prism C5",   prism(5)),
    ("prism C6",   prism(6)),
    ("prism C9",   prism(9)),
    ("prism C17",  prism(17)),
    ("moebius(4)", moebius(4)),
    ("moebius(7)", moebius(7)),
    ("dumbbell",   dumbbell()),
    ("dumbbell+2", dumbbell_long(2)),
    ("dumbbell+4", dumbbell_long(4)),
    ("rand12(s2)", random_cubic(12, 2)),
    ("rand16(s5)", random_cubic(16, 5)),
    ("rand24(s1)", random_cubic(24, 1)),
]

print(f"{'graph':<11} {'n':>3} {'chi':>4} {'b1':>3} {'bip':>3} {'gir':>3} {'Ram':>3} "
      f"{'#exc+':>5} {'#exc-':>5} {'N_at':>4} {'L=q(0)':>12} {'tau_min':>9} {'2w/t_min':>10} {'Stlj':>4}")
rows = {}
for name, A in graphs:
    G = analyze(A, dps=90, name=name)
    ats = atoms(G)
    L = sum(w/t for (t, w) in ats) if not (G.excP or G.excN) else None
    stj = "-"
    smin = None
    if G.ramanujan:
        P, Q = poly_from_atoms(ats)
        s = string_from_q(P, Q)
        stj = "yes" if all(mre(c) > 0 and abs(mim(c)) < mpf(10)**(-20) for c in s) else "NO"
        rows[name] = (G, s)
        taum = min(tau for tau, m in G.tempered)
        wm = [2*m for tau, m in G.tempered if fabs(tau - taum) < 1e-30][0]
        dom = wm/taum**2
        print(f"{name:<11} {G.n:>3} {G.chi:>4} {G.b1:>3} {str(G.bipartite)[0]:>3} {G.girth:>3} "
              f"{'yes':>3} {sum(m for _,m in G.excP):>5} {sum(m for _,m in G.excN):>5} "
              f"{len(ats):>4} {str(L)[:12]:>12} {str(taum)[:9]:>9} {str(dom)[:10]:>10} {stj:>4}")
    else:
        rows[name] = (G, None)
        print(f"{name:<11} {G.n:>3} {G.chi:>4} {G.b1:>3} {str(G.bipartite)[0]:>3} {G.girth:>3} "
              f"{'NO':>3} {sum(m for _,m in G.excP):>5} {sum(m for _,m in G.excN):>5} "
              f"{len(ats):>4} {'(not Stlj)':>12} {'-':>9} {'-':>10} {stj:>4}")

print("\n--- bead detail (Ramanujan members): [m1, l1, m2, l2, ...] first 8 coeffs ---")
for name, (G, s) in rows.items():
    if s:
        print(f"{name:<11}", [f"{float(mre(c)):.6g}" for c in s[:8]], f"(2N={len(s)})")

print("\n--- IR-dominance: last-gap fraction of total length vs spectral gap ---")
print(f"{'graph':<11} {'lam_2':>10} {'tau_min':>10} {'l_last/L':>10} {'2w/(t_min L)':>13}")
for name, (G, s) in rows.items():
    if s and len(s) >= 4:
        L = sum(mre(s[i]) for i in range(1, len(s), 2))
        lam2 = max(l for l, m in G.eigs if fabs(l - (G.q+1)) > 1e-20)
        taum = min(tau for tau, m in G.tempered)
        wm = [2*m for tau, m in G.tempered if fabs(tau - taum) < 1e-30][0]
        llast = mre(s[-1]) if len(s) % 2 == 0 else mre(s[-2])
        print(f"{name:<11} {float(lam2):>10.6f} {float(taum):>10.6f} {float(llast/L):>10.6f} "
          f"{float(wm/(taum**2*L)):>13.6f}")

############ FILE: e3_universality.py ############
"""E3: per-vertex bulk vs the universal-cover (Kesten-McKay) string, q=2 (cubic)."""
import numpy as np
from mpmath import mp, mpf, mpc, sqrt as msqrt, cos as mcos, sin as msin, acos as macos, \
    pi as mpi, fabs, mpmathify, matrix, eigsy
from lab_core import *

mp.dps = 60
q = 2

# ---- fixed Gauss-Legendre grid on tau in [0, pi] (integrand smooth) ----
NG = 500
import numpy.polynomial.legendre as leg
xs, ws = leg.leggauss(NG)
TAU = [(mpf(float(x))+1)/2*mpi for x in xs]
WTS = [mpf(float(w))/2*mpi for w in ws]

def km_weight(tau):
    lam = 2*msqrt(q)*mcos(tau)
    f = (q+1)/(2*mpi) * msqrt(4*q - lam**2) / ((q+1)**2 - lam**2)
    return 2 * f * 2*msqrt(q)*msin(tau)     # dmu_infty pushed to tau, total mass 2

def integ(fun):
    return sum(w*fun(t) for t, w in zip(TAU, WTS))

def Qinf(z):
    return integ(lambda t: km_weight(t)/(t**2 - z))

print("total KM mass (expect 2):", integ(km_weight))
ell_inf = Qinf(mpf(0))
print("per-vertex limit length  ell_inf = Qinf(0) =", str(ell_inf)[:20])

# ---- Gauss quadrature (K nodes) of dmu_infty in t = tau^2, via Stieltjes procedure ----
def km_string(Knodes):
    # orthonormal polynomial recurrence by quadrature
    tgrid = [t**2 for t in TAU]
    wgrid = [w*km_weight(t) for t, w in zip(TAU, WTS)]
    def ip(f, g):
        return sum(w*f[i]*g[i] for i, w in enumerate(wgrid))
    ones = [mpf(1)]*NG
    p_prev = [mpf(0)]*NG
    nrm0 = msqrt(ip(ones, ones))
    p_cur = [x/nrm0 for x in ones]
    alphas, betas = [], []
    for k in range(Knodes):
        tp = [tgrid[i]*p_cur[i] for i in range(NG)]
        a = ip(tp, p_cur)
        alphas.append(a)
        nxt = [tp[i] - a*p_cur[i] - (betas[-1]*p_prev[i] if betas else 0) for i in range(NG)]
        b = msqrt(ip(nxt, nxt))
        betas.append(b)
        p_prev, p_cur = p_cur, [x/b for x in nxt]
    # Jacobi matrix -> nodes/weights (Golub-Welsch)
    J = matrix(Knodes, Knodes)
    for i in range(Knodes):
        J[i, i] = alphas[i]
        if i+1 < Knodes:
            J[i, i+1] = J[i+1, i] = betas[i]
    E, V = eigsy(J)
    c0 = integ(km_weight)
    nodes = [E[i] for i in range(Knodes)]
    wts = [c0*V[0, i]**2 for i in range(Knodes)]
    ats = sorted(zip(nodes, wts))
    P, Qp = poly_from_atoms([(mpf(t), mpf(w)) for t, w in ats])
    return string_from_q(P, Qp), ats

sKM, atsKM = km_string(12)
print("\nKM string (K=12 Gauss atoms), first 8 coeffs [m,l,...]:",
      [f"{float(mre(c)):.6g}" for c in sKM[:8]])
print("KM string length:", str(sum(mre(sKM[i]) for i in range(1, len(sKM), 2)))[:14],
      "(vs ell_inf", str(ell_inf)[:14], ")")

# ---- graphs of growing size: per-vertex q at test points, and per-vertex beads ----
tests = [mpf(-1), mpc(-0.5, 0.8), mpc(1.5, 1.0)]
family = [
    ("K4", K(4)), ("cube", cube()), ("Petersen", petersen()), ("Heawood", heawood()),
    ("Desargues", desargues()), ("rand16(s5)", random_cubic(16, 5)),
    ("rand24(s1)", random_cubic(24, 1)), ("rand32(s3)", random_cubic(32, 3)),
    ("rand40(s4)", random_cubic(40, 4)),
]
print("\n--- per-vertex Stieltjes-transform distance to KM limit ---")
print(f"{'graph':<11} {'n':>3}  " + "  ".join(f"{'|q/n-Qinf| @z'+str(k):>16}" for k in range(3)))
results = {}
for name, A in family:
    G = analyze(A, dps=60, name=name)
    devs = [fabs(q_of_z(G, z)/G.n - Qinf(z)) for z in tests]
    results[name] = G
    print(f"{name:<11} {G.n:>3}  " + "  ".join(f"{float(d):>16.3e}" for d in devs))

print("\n--- per-vertex beads (m~_k = n m_k, l~_k = n l_k... rescale q->q/n: m x n, l / n) ---")
print("KM        ", [f"{float(mre(sKM[i])):.5g}" for i in range(8)])
for name, A in family:
    G = results[name]
    ats = [(t, w/G.n) for (t, w) in atoms(G)]     # per-vertex measure
    P, Qp = poly_from_atoms(ats)
    s = string_from_q(P, Qp)
    print(f"{name:<10}", [f"{float(mre(s[i])):.5g}" for i in range(min(8, len(s)))],
          f" L/n={float(sum(mre(s[i]) for i in range(1,len(s),2))):.5f}")
print("(KM row = universal-cover prediction; ell_inf =", str(ell_inf)[:10], ")")

############ FILE: e4_e5.py ############
"""E4: violation anatomy + Siegel-blindness split.  E5: omega-flow indices."""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, exp as mexp, log as mlog, sqrt as msqrt, acosh as macosh
from lab_core import *

def dumbbell_long(k):
    """Two K4-minus-edge blobs joined by a ladder of k rungs. 3-regular n=8+2k."""
    n = 8 + 2*k
    A = np.zeros((n, n), dtype=object)
    def blob(off):
        for i in range(4):
            for j in range(i+1, 4):
                if (i, j) != (0, 1):
                    A[off+i][off+j] = A[off+j][off+i] = 1
    blob(0); blob(4)
    prev = (0, 1)
    for i in range(k):
        a, b = 8+2*i, 8+2*i+1
        A[a][b] = A[b][a] = 1
        A[prev[0]][a] = A[a][prev[0]] = 1
        A[prev[1]][b] = A[b][prev[1]] = 1
        prev = (a, b)
    A[prev[0]][4] = A[4][prev[0]] = 1
    A[prev[1]][5] = A[5][prev[1]] = 1
    return A

mp.dps = 80
TWOSQ = 2*msqrt(2)

def report_graph(G):
    dP = [(macosh(l/TWOSQ), m) for l, m in G.eigs if l > TWOSQ and fabs(l-3) > 1e-20]
    dN = [(macosh(-l/TWOSQ), m) for l, m in G.eigs if -l > TWOSQ and (not G.bipartite or fabs(l+3) > 1e-20)]
    print(f"\n### {G.name}: n={G.n} excP deltas {[ (float(d),m) for d,m in dP ]} "
          f"excN deltas {[ (float(d),m) for d,m in dN ]}")
    return dP, dN

def cf_anatomy(G, dps=160):
    mp.dps = dps
    P, Q = poly_from_atoms(atoms(G))
    s = string_from_q(P, Q)
    bad = [(i, complex(c)) for i, c in enumerate(s)
           if mre(c) < 0 or abs(mim(c)) > mpf(10)**(-dps//3)]
    # round-trip verification
    z = mpc('-1.37', '0.41')
    q1 = q_of_z(G, z); q2 = q_from_string(s, z)
    rt = fabs(q1-q2)/fabs(q1)
    print(f"  CF: 2N={len(s)} coeffs; non-Stieltjes entries at indices "
          f"{[i for i,_ in bad]} (of {len(s)}); round-trip {float(rt):.1e}")
    for i, c in bad[:6]:
        print(f"    idx {i} ({'mass' if i%2==0 else 'len '} #{i//2+1}): {c:.6g}")
    mp.dps = 80
    return s, bad

def psi_scan(G, tmax=40, npts=2001):
    ts = [mpf(tmax)*k/(npts-1) for k in range(1, npts)]
    vals = [Psi(G, t) for t in ts]
    mn = min(vals); tmin = ts[vals.index(mn)]
    firstneg = next((float(t) for t, v in zip(ts, vals) if v < 0), None)
    print(f"  Psi on (0,{tmax}]: min = {float(mn):.6g} at t={float(tmin):.3f}; "
          f"first negative t = {firstneg}")
    return mn

def pick_points():
    return [mpc(*p) for p in [(-2, 1.5), (-0.5, 0.8), (0.2, 0.3), (1.5, 1.1),
                              (3.0, 0.9), (5.0, 2.0), (8.0, 3.0), (0.9, 0.5)]]

def kappa_of_omega(G, omegas):
    pts = pick_points()
    out = []
    for om in omegas:
        f = lambda z: q_omega(G, z, om)
        k, _ = pick_kappa(f, pts)
        out.append((float(om), k))
    return out

def support_leak(G, om, xs):
    """max |Im q_omega(x + i eps)| on negative axis: detects the exc+ pole at -(delta-om)^2."""
    eps = mpf('1e-6')
    return max(fabs(mim(q_omega(G, mpc(x, eps), om))) for x in xs)

# ------------------------------------------------------------------ specimens
specimens = [
    ("dumbbell+4  [pure exc+]", dumbbell_long(4)),
    ("prism C9    [pure exc-]", prism(9)),
    ("prism C17   [both]",      prism(17)),
    ("rand40(s4)  [random exc-]", random_cubic(40, 4)),
    ("Petersen    [control]",   petersen()),
]

print("=================== E4: anatomy ===================")
data = {}
for name, A in specimens:
    G = analyze(A, dps=80, name=name)
    dP, dN = report_graph(G)
    s, bad = cf_anatomy(G)
    mn = psi_scan(G)
    # Pick at omega=0
    k0, evs = pick_kappa(lambda z: q_of_z(G, z), pick_points())
    print(f"  Pick negative squares at omega=0: kappa = {k0}")
    data[name] = (G, dP, dN)

print("\n--- synthetic Siegel shielding (labelled synthetic) ---")
# C9's exc- ordinates + an artificial real pair with larger delta: Psi should turn positive
G9 = data["prism C9    [pure exc-]"][0]
dN9 = data["prism C9    [pure exc-]"][2][0][0]
class Synth: pass
S = Synth(); S.tempered = G9.tempered; S.excN = G9.excN; S.excP = [(dN9 + mpf('0.15'), 1)]
S.name = "C9 + synthetic real pair"
mnS = None
ts = [mpf(40)*k/2000 for k in range(1, 2001)]
vals = [Psi(S, t) for t in ts]
mnS = min(vals)
print(f"  delta_N(C9) = {float(dN9):.5f}; synthetic delta_P = {float(dN9)+0.15:.5f}")
print(f"  min Psi with shield on (0,40] = {float(mnS):.6g}  (was negative without shield)")

print("\n=================== E5: omega-flow indices ===================")
for name in ["prism C9    [pure exc-]", "dumbbell+4  [pure exc+]", "prism C17   [both]"]:
    G, dP, dN = data[name]
    deltas = sorted([float(d) for d, m in dP] + [float(d) for d, m in dN])
    print(f"\n### {name}: crossing predictions at omega = {[f'{d:.5f}' for d in deltas]}")
    # kappa staircase around each predicted crossing
    grid = sorted(set([mpf('0.001')] + [mpf(d) + s for d in deltas for s in
                      (mpf('-0.02'), mpf('-0.002'), mpf('0.002'), mpf('0.02'))] + [mpf('0.45')]))
    ks = kappa_of_omega(G, grid)
    print("  kappa_Pick(omega):", ks)
    if dP:
        dp = dP[0][0]
        xs = [-mpf(x)/50 for x in range(1, 120)]
        for om in [dp - mpf('0.05'), dp - mpf('0.005'), dp + mpf('0.005'), dp + mpf('0.05')]:
            print(f"  support-leak at omega={float(om):.5f}: max|Im q_omega| on (-2.4,0) = "
                  f"{float(support_leak(G, om, xs)):.4g}"
                  f"   (pole predicted at z={-float(dp-om)**2 if dp>om else None})")

############ FILE: e5_fix.py ############
"""E5 (fixed detectors): kappa(omega) with pole-tracking Pick points; support leak at pole."""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, sqrt as msqrt, acosh as macosh, pi as mpi
from lab_core import *

mp.dps = 80
TWOSQ = 2*msqrt(2)

def dumbbell_long(k):
    n = 8 + 2*k
    A = np.zeros((n, n), dtype=object)
    def blob(off):
        for i in range(4):
            for j in range(i+1, 4):
                if (i, j) != (0, 1):
                    A[off+i][off+j] = A[off+j][off+i] = 1
    blob(0); blob(4)
    prev = (0, 1)
    for i in range(k):
        a, b = 8+2*i, 8+2*i+1
        A[a][b] = A[b][a] = 1
        A[prev[0]][a] = A[a][prev[0]] = 1
        A[prev[1]][b] = A[b][prev[1]] = 1
        prev = (a, b)
    A[prev[0]][4] = A[4][prev[0]] = 1
    A[prev[1]][5] = A[5][prev[1]] = 1
    return A

def kappa_tracked(G, om, dNs):
    """Pick with generic points + points ringing each predicted C+ pole of q_omega.
    excN ordinate gamma = pi - i*delta -> h-pole w0 = (delta-om) + i*pi (RHP iff om<delta)
    -> q_omega pole z0 = -w0^2, conj-pole in C+ at conj(z0) if Im z0<0."""
    pts = [mpc(*p) for p in [(-2, 1.5), (-0.5, 0.8), (1.5, 1.1), (5.0, 2.0)]]
    for d in dNs:
        if om < d:
            w0 = (d - om) + mpc(0, 1)*mpi
            z0 = -w0**2
            zc = mpc(mre(z0), abs(mim(z0)))     # the C+ member of the conjugate pair
            for off in [mpc(0.05, 0.05), mpc(-0.07, 0.02), mpc(0.02, 0.11)]:
                pts.append(zc + off)
        else:
            # ring where the pole was last seen, as control
            pts.append(mpc(mpi**2 - (om-d)**2, 0.15))
    f = lambda z: q_omega(G, z, om)
    k, evs = pick_kappa(f, pts)
    return k, evs[0]

def leak_at_pole(G, om, dP):
    eps = mpf('1e-8')
    if om < dP:
        x = -(dP - om)**2
        return float(fabs(mim(q_omega(G, mpc(x, eps), om))))
    else:
        x = -(om - dP)**2 - mpf('1e-4')     # nearby control point
        return float(fabs(mim(q_omega(G, mpc(x, eps), om))))

print("=== prism C9 (excN delta=0.18954, mult 2): kappa staircase ===")
G9 = analyze(prism(9), dps=80, name="C9")
d9 = macosh(mpf('2.879385241571816768')/TWOSQ)  # recompute exactly below
d9 = [macosh(-l/TWOSQ) for l, m in G9.eigs if -l > TWOSQ][0]
for om in ['0.001', '0.05', '0.10', '0.15', '0.18', '0.187', '0.192', '0.21', '0.30', '0.45']:
    k, minev = kappa_tracked(G9, mpf(om), [d9])
    print(f"  omega={om:>6}: kappa={k}   min Pick eigenvalue = {float(minev):.3e}")
print(f"  predicted crossing at delta = {float(d9):.6f}")

print("\n=== dumbbell+4 (excP delta=0.098773): support-leak at predicted pole ===")
GD = analyze(dumbbell_long(4), dps=80, name="D4")
dp = [macosh(l/TWOSQ) for l, m in GD.eigs if l > TWOSQ and fabs(l-3) > 1e-20][0]
for om in ['0.001', '0.05', '0.09', '0.097', '0.101', '0.11', '0.15', '0.30']:
    print(f"  omega={om:>6}: |Im q_omega| at pole site = {leak_at_pole(GD, mpf(om), dp):.4e}")
print(f"  predicted crossing at delta = {float(dp):.6f}")
k, minev = kappa_tracked(GD, mpf('0.01'), [])
print(f"  control: kappa_Pick(0.01) for dumbbell+4 = {k} (exc+ never makes negative squares)")

print("\n=== prism C17 (excP 0.16052, excN 0.31058): both flows ===")
G17 = analyze(prism(17), dps=80, name="C17")
d17N = [macosh(-l/TWOSQ) for l, m in G17.eigs if -l > TWOSQ][0]
d17P = [macosh(l/TWOSQ) for l, m in G17.eigs if l > TWOSQ and fabs(l-3) > 1e-20][0]
for om in ['0.001', '0.15', '0.25', '0.305', '0.316', '0.40']:
    k, minev = kappa_tracked(G17, mpf(om), [d17N])
    print(f"  omega={om:>6}: kappa={k}  min-ev={float(minev):.2e}  "
          f"leak@pole={leak_at_pole(G17, mpf(om), d17P):.3e}")
print(f"  predicted: kappa drop at {float(d17N):.5f}; leak dies at {float(d17P):.5f}")

############ FILE: e6_covers.py ############
"""E6: bipartite double covers (Artin-like splitting in the bulk) + violation-position law."""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, sqrt as msqrt, acos as macos
from lab_core import *

mp.dps = 100
TWOSQ = 2*msqrt(2)

print("=== exact cover identities (integer charpoly equality) ===")
print("charpoly BD(K4) == charpoly(Q3):      ",
      charpoly_exact(bipartite_double(K(4))) == charpoly_exact(cube()))
print("charpoly BD(Petersen) == charpoly(Desargues):",
      charpoly_exact(bipartite_double(petersen())) == charpoly_exact(desargues()))

print("\n=== base vs cover: per-vertex strings and atom provenance ===")
for bname, bA, cname, cA in [("K4", K(4), "Q3=BD(K4)", cube()),
                             ("Petersen", petersen(), "Desargues=BD(Pet)", desargues())]:
    GB = analyze(bA, dps=100, name=bname)
    GC = analyze(cA, dps=100, name=cname)
    print(f"\n{bname} atoms (tau, w/n):", [(f"{float(t):.5f}", f"{float(2*m)/GB.n:.4f}")
                                           for t, m in GB.tempered])
    base_taus = {float(t) for t, m in GB.tempered}
    prov = []
    for t, m in GC.tempered:
        src = "base" if any(abs(float(t)-bt) < 1e-9 for bt in base_taus) else "TWISTED"
        prov.append((f"{float(t):.5f}", f"{float(2*m)/GC.n:.4f}", src))
    print(f"{cname} atoms (tau, w/n, origin):", prov)
    for G in (GB, GC):
        ats = [(t, w/G.n) for (t, w) in atoms(G)]
        P, Q = poly_from_atoms(ats)
        s = string_from_q(P, Q)
        print(f"  per-vertex string {G.name:<18}:",
              [f"{float(mre(c)):.5g}" for c in s], f" L/n={float(sum(mre(s[i]) for i in range(1,len(s),2))):.5f}")

print("\n=== violation-position law: where the CF anomaly lands ===")
def dumbbell_long(k):
    n = 8 + 2*k
    A = np.zeros((n, n), dtype=object)
    def blob(off):
        for i in range(4):
            for j in range(i+1, 4):
                if (i, j) != (0, 1):
                    A[off+i][off+j] = A[off+j][off+i] = 1
    blob(0); blob(4)
    prev = (0, 1)
    for i in range(k):
        a, b = 8+2*i, 8+2*i+1
        A[a][b] = A[b][a] = 1
        A[prev[0]][a] = A[a][prev[0]] = 1
        A[prev[1]][b] = A[b][prev[1]] = 1
        prev = (a, b)
    A[prev[0]][4] = A[4][prev[0]] = 1
    A[prev[1]][5] = A[5][prev[1]] = 1
    return A

cases = [("dumbbell+4", dumbbell_long(4)), ("dumbbell+6", dumbbell_long(6)),
         ("dumbbell+8", dumbbell_long(8)), ("prism C9", prism(9)),
         ("prism C17", prism(17)), ("rand40(s4)", random_cubic(40, 4)),
         ("moebius(9)", moebius(9)), ("prism C11", prism(11))]
print(f"{'graph':<12} {'type':<12} {'delta(s)':<24} {'anomaly idx / 2N':<20} {'first anomaly value'}")
for name, A in cases:
    G = analyze(A, dps=160, name=name)
    if G.ramanujan:
        print(f"{name:<12} {'Ramanujan':<12}")
        continue
    dP = [float(macosh(l/TWOSQ)) for l, m in G.eigs if l > TWOSQ and fabs(l-3) > 1e-20]
    dN = [float(macosh(-l/TWOSQ)) for l, m in G.eigs
          if -l > TWOSQ and (not G.bipartite or fabs(l+3) > 1e-20)]
    mp.dps = 160
    P, Q = poly_from_atoms(atoms(G))
    s = string_from_q(P, Q)
    bad = [(i, complex(c)) for i, c in enumerate(s)
           if mre(c) < 0 or abs(mim(c)) > mpf(10)**(-40)]
    typ = ("exc+" if dP else "") + ("exc-" if dN else "")
    ds = f"P:{[f'{d:.4f}' for d in dP]} N:{[f'{d:.4f}' for d in dN]}"
    print(f"{name:<12} {typ:<12} {ds:<24} {str([i for i,_ in bad])+' / '+str(len(s)):<20} "
          f"{bad[0][1]:.4g} ...")
    mp.dps = 100

############ FILE: r2a_full_structure.py ############
"""Round 2, Task A: restore the complete Ihara analytic structure.

Exact objects (round-1 natural units: V = log(q)*(s_true - 1/2); ell := log q):

  D(s)  := -u d/du log zeta_X(u),  u = q^{-s}
         =  2*chi*u^2/(1-u^2)  +  Sum_{ALL eigenvalues} u(2qu - lambda)/(1 - lambda u + q u^2)

  Per-eigenvalue block: 1 - lambda u + q u^2 = (1 - c1 u)(1 - c2 u), c = (lambda +/- sqrt(lambda^2-4q))/2,
  c1 c2 = q;  block(lambda, V) = Sum_c  (c/sqrt(q)) e^{-V} / (1 - (c/sqrt(q)) e^{-V}).
  Tempered lambda = 2 sqrt(q) cos(theta):  c/sqrt(q) = e^{+/- i theta}.

  Coth expansion per tempered eigenvalue (exact):
      block(theta, V) = [2V/(V^2+theta^2) + Sum_{k>=1} towers] - 1
  so with W0 := total nontrivial multiplicity,
      h_plus(V)  := Sum_nontriv block + W0        (the POSITIVE tower completion; odd, Herglotz)
      Gamma_X(V) := trivial blocks + Bass block   (the graph gamma factor; carries chi and bipartiteness)
      h_full(V)  =  h_plus(V) - W0 + Gamma_X(V)   (the honest log-derivative)

  Completed positive length:  L_plus = q_plus(0) = Sum_j 2 m_j / (4 sin^2(theta_j/2))
                                     = Sum_nontriv 2 sqrt(q) m_j / (2 sqrt(q) - lambda_j)
  (edge resolvent at the Ramanujan edge).
"""
import numpy as np
from mpmath import mp, mpf, mpc, sqrt as msqrt, log as mlog, exp as mexp, sin as msin, \
    cos as mcos, acos as macos, pi as mpi, fabs, mpmathify
from lab_core import *

mp.dps = 60
q = 2
ELL = mlog(q)
TWOSQ = 2*msqrt(q)

def blocks_all(G, V):
    """Exact h_full(V) via per-eigenvalue root blocks + Bass block. V complex."""
    tot = mpc(0)
    for lam, m in G.eigs:
        disc = msqrt(mpc(lam)**2 - 4*q)
        for c in ((lam + disc)/2, (lam - disc)/2):
            x = (c/msqrt(q))*mexp(-V)
            tot += m * x/(1 - x)
    y = mexp(-(2*V + ELL))
    tot += 2*G.chi * y/(1 - y)
    return tot

def D_rational(G, V):
    """Same object from the rational u-formula (independent evaluation)."""
    s = mpf(1)/2 + V/ELL
    u = mexp(-s*ELL)
    tot = 2*G.chi*u**2/(1 - u**2)
    for lam, m in G.eigs:
        tot += m * u*(2*q*u - lam)/(1 - lam*u + q*u**2)
    return tot

def h_plus_exact(G, V):
    """Positive tower completion = Sum_nontriv block + W0 (exact, no truncation)."""
    tot = mpc(0); W0 = 0
    for lam, m in G.eigs:
        if fabs(lam - (q+1)) < 1e-40 or (G.bipartite and fabs(lam + (q+1)) < 1e-40):
            continue
        W0 += m          # coth constant: -1/2 per factor, two factors per unit multiplicity
        disc = msqrt(mpc(lam)**2 - 4*q)
        for c in ((lam + disc)/2, (lam - disc)/2):
            x = (c/msqrt(q))*mexp(-V)
            tot += m * x/(1 - x)
    return tot + W0, W0

def Gamma_X(G, V):
    """Graph gamma factor: trivial eigenvalue blocks + Bass block."""
    tot = mpc(0)
    for lam, m in G.eigs:
        if fabs(lam - (q+1)) < 1e-40 or (G.bipartite and fabs(lam + (q+1)) < 1e-40):
            disc = msqrt(mpc(lam)**2 - 4*q)
            for c in ((lam + disc)/2, (lam - disc)/2):
                x = (c/msqrt(q))*mexp(-V)
                tot += m * x/(1 - x)
    y = mexp(-(2*V + ELL))
    tot += 2*G.chi * y/(1 - y)
    return tot

print("=== A1: exact identity  blocks == rational D  (no truncation) ===")
for name, A in [("Petersen", petersen()), ("prism C9", prism(9)), ("K3,3", Kbip(3, 3))]:
    G = analyze(A, dps=60, name=name)
    worst = mpf(0)
    rng = np.random.default_rng(5)
    for _ in range(5):
        V = mpc(*(rng.uniform(0.2, 1.5, 2)))
        worst = max(worst, fabs(blocks_all(G, V) - D_rational(G, V)))
    print(f"  {name:<10} identity error: {float(worst):.3e}")

print("\n=== A2: h_plus consistency: blocks+W0 == truncated tower pair-sum (K -> inf) ===")
GP = analyze(petersen(), dps=60, name="Petersen")
def h_plus_towers(G, V, K):
    tot = mpc(0)
    for tau, m in G.tempered:
        for gam in [tau + 2*mpi*k for k in range(0, K+1)] + [2*mpi*k - tau for k in range(1, K+1)]:
            tot += m * 2*V/(V**2 + gam**2)
    return tot
Vt = mpc('0.7', '0.3')
hex_, W0 = h_plus_exact(GP, Vt)
# NOTE: the constant is -m per FACTOR, i.e. -1 per eigenvalue *counted with mult*, TWO factors
# per eigenvalue each -1/2 => -m per eigenvalue => total -(n - #trivial). Recheck numerically:
for W0try_name, W0try in [("sum m (n-triv)", sum(m for t, m in GP.tempered)),
                          ("sum 2m", 2*sum(m for t, m in GP.tempered))]:
    hex2 = h_plus_towers(GP, Vt, 4000)
    base = blocks_all(GP, Vt) - Gamma_X(GP, Vt)   # = sum_nontriv blocks
    print(f"  constant candidate {W0try_name}: |(blocks_nontriv + W0) - towers(K=4000)| = "
          f"{float(fabs(base + W0try - hex2)):.3e}")

print("\n=== A3: completed positive length: closed form vs tower sum vs derivative ===")
for name, A in [("K4", K(4)), ("Petersen", petersen()), ("Heawood", heawood()),
                ("prism C6", prism(6)), ("rand16(s5)", random_cubic(16, 5))]:
    G = analyze(A, dps=60, name=name)
    Lres = sum(2*msqrt(q)*m/(TWOSQ - lam) for lam, m in G.eigs
               if fabs(lam-(q+1)) > 1e-40 and not (G.bipartite and fabs(lam+(q+1)) < 1e-40))
    Lsin = sum(2*m/(4*msin(tau/2)**2) for tau, m in G.tempered)
    Lder = mre((h_plus_exact(G, mpf('1e-8'))[0])/mpf('1e-8'))
    Lprin = sum(2*m/tau**2 for tau, m in G.tempered)
    extra = ""
    if name in ("K4", "Petersen"):
        Ktow = 30000
        Ltow = sum(2*m/gam**2 for tau, m in G.tempered
                   for gam in [tau + 2*mpi*k for k in range(0, Ktow)]
                   + [2*mpi*k - tau for k in range(1, Ktow)])
        extra = f", towers(K=3e4) diff {float(fabs(Lres-Ltow)):.1e}"
    print(f"  {name:<11} L+={str(Lres)[:14]}  (sin form diff {float(fabs(Lres-Lsin)):.1e}, "
          f"deriv diff {float(fabs(Lres-Lder)):.1e}{extra})  L_principal={str(Lprin)[:12]}")

print("\n=== A4: signed-defect structure on the critical axis: Re h_spec(iy) = -W0 exactly ===")
for y in ['0.9', '2.3']:
    base = blocks_all(GP, mpc(0, mpf(y))) - Gamma_X(GP, mpc(0, mpf(y)))
    print(f"  Petersen y={y}: Re Sum_nontriv blocks(iy) = {float(mre(base)):.12f}   "
          f"(-W0 = {-sum(m for t, m in GP.tempered)})")

print("\n=== A5: gamma-block Gamma_X: explicit chi content and a.c. density it adds ===")
for name, A in [("K4 (chi=-2)", K(4)), ("Petersen (chi=-5)", petersen()),
                ("Heawood (chi=-7, bip)", heawood())]:
    G = analyze(A, dps=60, name=name)
    om = mpf('0.1')
    # a.c. density added by Gamma at a few x on the cut:  (1/pi) Im [Gamma(om + w)/w], w = -i sqrt(x)
    dens = []
    for x in ['1.0', '4.0', '9.0']:
        w = -mpc(0, 1)*msqrt(mpf(x))
        dens.append(float(mim(Gamma_X(G, om + w)/w)/mpi))
    print(f"  {name:<22} Gamma(0.1) = {float(mre(Gamma_X(G, mpf('0.1')))):+.6f}   "
          f"gamma-density at x=1,4,9: {[f'{d:+.5f}' for d in dens]}")

print("\n=== A6: completed positive string: bead convergence in tower cutoff K (Petersen, per-vertex) ===")
for Kt in [4, 8, 16]:
    mp.dps = 220
    ats = []
    for tau, m in GP.tempered:
        for gam in [tau + 2*mpi*k for k in range(0, Kt+1)] + [2*mpi*k - tau for k in range(1, Kt+1)]:
            ats.append((gam**2, mpf(2*m)/GP.n))
    ats.sort(key=lambda p: mre(p[0]))
    P, Q = poly_from_atoms(ats)
    s = string_from_q(P, Q)
    ok = all(mre(c) > 0 for c in s)
    Ltot = sum(mre(s[i]) for i in range(1, len(s), 2))
    print(f"  K={Kt:>2} ({len(ats)} atoms): first beads "
          f"{[f'{float(mre(c)):.5g}' for c in s[:8]]}  all>0:{ok}  L={float(Ltot):.6f}")
    mp.dps = 60
Lplus_pv = float(sum(2*msqrt(q)*m/(TWOSQ - lam) for lam, m in GP.eigs
                 if fabs(lam-3) > 1e-40)/GP.n)
print(f"  exact per-vertex completed length L+/n = {Lplus_pv:.6f}")

############ FILE: r2c_hankel.py ############
"""Round 2, Task C: F8 as moment-detection depth. Synthetic defect scans + potential-theory law.

Background sigma_0 = tempered atoms of rand24(s1) (Ramanujan, 23 atoms, total mass 46).
Defects: exc+ analogue: atom at a = -delta^2, weight eps.
         exc- analogue: conjugate atoms at (pi -/+ i delta)^2, weight eps/2 each.
Measured: first n with det H_n < 0 (H = (mu_{i+j}));
          first n with det H1_n < 0 (H1 = (mu_{i+j+1}));
          first anomalous CF coefficient index.
Potential theory: g(a) = Green's function of C \ [0, pi^2] at a, g = acosh-type;
hypothesis n* ~ log(stuff/eps) / (2 g(a)).
"""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, sqrt as msqrt, pi as mpi, log as mlog, matrix, det, acosh as macosh
from lab_core import *

mp.dps = 400
G0 = analyze(random_cubic(24, 1), dps=60, name="rand24")
mp.dps = 400
BG = [(mpf(str(float(t)))**1, mpf(2*m)) for t, m in [(tau**2, m) for tau, m in G0.tempered]]
# recompute background at dps400 from high-precision taus
BG = [((tau**2), mpf(2*m)) for tau, m in G0.tempered]
WBG = sum(w for _, w in BG)
R = mpi**2

def green(a):
    """Green's function of C \ [0, R] with pole at infinity, at point a (complex ok)."""
    x = (2*mpc(a) - R)/R
    return mre(mlog(x + msqrt(x-1)*msqrt(x+1)))   # log|phi|, principal branches give |phi|>1 off [0,R]

def moments(atoms, N):
    out = []
    for k in range(N):
        out.append(sum(w * t**k for t, w in atoms))
    return [mre(x) for x in out]   # conj pairs keep them real

def first_neg_hankel(mus, shift, nmax):
    for n in range(1, nmax):
        M = matrix(n, n)
        for i in range(n):
            for j in range(n):
                M[i, j] = mus[i+j+shift]
        if mre(det(M)) < 0:
            return n
    return None

def cf_anomaly(atoms):
    P, Q = poly_from_atoms(atoms)
    s = string_from_q(P, Q)
    for i, c in enumerate(s):
        if mre(c) < 0 or abs(mim(c)) > mpf(10)**(-mp.dps//4):
            return i, len(s)
    return None, len(s)

def run_case(kind, delta, eps):
    if kind == 'P':
        defect = [(-mpf(delta)**2, mpf(eps))]
    else:
        th = mpi - mpc(0, 1)*mpf(delta)
        defect = [(th**2, mpf(eps)/2), ((th**2).conjugate(), mpf(eps)/2)]
    atoms = BG + defect
    nmax = 30
    mus = moments(atoms, 2*nmax + 2)
    nH = first_neg_hankel(mus, 0, nmax)
    nH1 = first_neg_hankel(mus, 1, nmax)
    idx, twoN = cf_anomaly(atoms)
    a_eff = defect[0][0]
    g = green(a_eff)
    return nH, nH1, idx, twoN, float(g)

print(f"background: rand24 tempered atoms, {len(BG)} atoms, mass {float(WBG)}, support ~ "
      f"[{float(min(t for t,_ in BG)):.3f}, {float(max(t for t,_ in BG)):.3f}], R = pi^2")
print(f"\n{'kind':<5} {'delta':>6} {'eps':>8} {'g(a)':>8} {'nH':>4} {'nH1':>4} {'CF idx':>7} "
      f"{'log(W/eps)/(2g)':>16}")
for kind in ['P', 'N']:
    for delta in ['0.05', '0.1', '0.2', '0.4', '0.8']:
        for eps in ['2', '0.001']:
            nH, nH1, idx, twoN, g = run_case(kind, delta, eps)
            pred = float(mlog(WBG/mpf(eps))/(2*g)) if g > 0 else float('inf')
            print(f"{kind:<5} {delta:>6} {eps:>8} {g:>8.4f} {str(nH):>4} {str(nH1):>4} "
                  f"{str(idx)+'/'+str(twoN):>7} {pred:>16.2f}")

print("\n--- actual graphs, for comparison (from round 1 / e6): ---")
TW = 2*msqrt(2)
for name, dP, dN, idxs in [("dumbbell+4", '0.098773', None, "17/26"),
                           ("prism C9", None, '0.189539', "6/20"),
                           ("prism C11", None, '0.252366', "5/24"),
                           ("rand40(s4)", None, '0.182187', "7/80")]:
    if dP:
        a = -mpf(dP)**2
    else:
        a = (mpi - mpc(0, 1)*mpf(dN))**2
    g = float(green(a))
    print(f"  {name:<12} g(a) = {g:.4f}   1/(2g) = {1/(2*g):.2f}   measured CF anomaly {idxs}")

############ FILE: r3b_zeta.py ############
"""Round 3, Workstream B: defect depth on a GENUINE zeta-zero background + time/depth duality.

Background: first N nontrivial zeta ordinates gamma_j (mpmath zetazero), atoms (gamma_j^2, 2).
Defect: hypothetical off-line zero pair rho = 1/2 + delta +/- i tau0 -> conjugate atoms at
        c = (tau0 -/+ i delta)^2, weight eps/2 each  (eps = 2 is a genuine zero's weight).
Scale invariance: detection orders n0, n1 are invariant under t -> t/beta (H -> D H D),
so we compute on t/beta in [0,1] at moderate dps.
Detection curve: exact rank-two lemma
  det H(eps)/det H = 1 + eps Re[K(c,c)] + (eps^2/4)(|K(c,c)|^2 - K(c,cbar)^2)          [shift 0]
  det H'(eps)/det H' = 1 + eps Re[c K'(c,c)] + (eps^2/4)|c|^2 (|K'(c,c)|^2 - K'(c,cbar)^2) [shift 1]
with K the bilinear CD kernel v_x^T H^{-1} v_y (scaled variables).
"""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, pi as mpi, log as mlog, sqrt as msqrt, matrix, det, \
    lu_solve, zetazero, cos as mcos, exp as mexp
from lab_core import psi_pair
from mpmath import re as mre, im as mim

mp.dps = 30
NZ = 60
print(f"computing first {NZ} zeta ordinates...")
GAMS = [mim(zetazero(j)) for j in range(1, NZ+1)]
print(f"gamma_1 = {float(GAMS[0]):.6f}, gamma_{NZ} = {float(GAMS[-1]):.6f}")

mp.dps = 160
GAMS = [mpf(str(g)) for g in GAMS]
BETA = GAMS[-1]**2 * mpf('1.0001')
ALPHA = GAMS[0]**2

def bg_atoms(N):
    return [((g/GAMS[-1])**2 / mpf('1.0001'), mpf(2)) for g in GAMS[:N]]

def hank(atoms, shift, n):
    mus = [sum(w*mpc(t)**k for t, w in atoms) for k in range(2*n + shift)]
    M = matrix(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = mus[i+j+shift]
    return M

def kernels(Hm, c, n):
    vc = matrix([mpc(c)**i for i in range(n)])
    vcb = matrix([mpc(c).conjugate()**i for i in range(n)])
    xc = lu_solve(Hm, vc)
    Kcc = sum(vc[i]*xc[i] for i in range(n))
    Kccb = sum(vcb[i]*xc[i] for i in range(n))
    return Kcc, Kccb

def detection_orders(N, tau0, delta, eps, nmax=26):
    ats = bg_atoms(N)
    c = ((tau0 - mpc(0,1)*delta)/GAMS[-1])**2 / mpf('1.0001')
    n0 = n1 = None
    for n in range(2, nmax):
        if n0 is None:
            H0 = hank(ats, 0, n)
            Kcc, Kccb = kernels(H0, c, n)
            r0 = 1 + eps*mre(Kcc) + (eps**2/4)*(abs(Kcc)**2 - Kccb**2)
            if mre(r0) < 0:
                n0 = n
        if n1 is None:
            H1 = hank(ats, 1, n)
            Kcc1, Kccb1 = kernels(H1, c, n)
            r1 = 1 + eps*mre(c*Kcc1) + (eps**2/4)*abs(c)**2*(abs(Kcc1)**2 - Kccb1**2)
            if mre(r1) < 0:
                n1 = n
        if n0 is not None and n1 is not None:
            break
    return n0, n1, c

def green_interval(c, a, b):
    x = (2*mpc(c) - a - b)/(b - a)
    return float(mre(mlog(x + msqrt(x-1)*msqrt(x+1))))

def tstar(tau0, delta, eps, N):
    """first t where Psi_bg + defect term < 0."""
    gam_def = tau0 - mpc(0,1)*delta
    for k in range(1, 40001):
        t = mpf(k)/200      # up to t = 200
        bg = sum(2*(1-mcos(g*t))/g**2 for g in GAMS[:N])
        d = (eps/2)*mre(psi_pair(t, gam_def, mpf(0)) + psi_pair(t, gam_def.conjugate(), mpf(0)))
        if bg + d < 0:
            return float(t)
    return None

print(f"\n{'tau0':>5} {'delta':>6} {'eps':>5} {'N':>3} {'n0':>4} {'n1':>4} "
      f"{'CFidx(law)':>10} {'g(c)':>8} {'log(2/eps)/2g+':>13} {'t*':>8} {'n1*delta':>8} {'t**delta':>8}")
rows = []
for tau0f, deltaf, epsf, N in [(20, '0.3', 2, 60), (20, '0.1', 2, 60), (20, '0.5', 2, 60),
                               (40, '0.3', 2, 60), (40, '0.1', 2, 60),
                               (20, '0.3', '0.02', 60), (20, '0.3', 2, 40)]:
    tau0 = mpf(tau0f); delta = mpf(deltaf); eps = mpf(str(epsf))
    n0, n1, c = detection_orders(N, tau0, delta, eps)
    a, b = float((GAMS[0]/GAMS[-1])**2/mpf('1.0001')), 1.0
    # use actual support ends of the truncated background
    scaled_ats = bg_atoms(N)
    a_supp = float(mre(scaled_ats[0][0])); b_supp = float(mre(scaled_ats[N-1][0]))
    g = green_interval(c, mpf(str(a_supp)), mpf(str(b_supp)))
    # index law -> CF index
    if n1 is not None and (n0 is None or n1 < n0):
        cfidx = f"{2*n1-1} (len)"
    elif n0 is not None:
        cfidx = f"{2*n0-2} (mass)"
    else:
        cfidx = ">cap"
    ts = tstar(tau0, delta, eps, N)
    nd = (n1 if (n1 is not None and (n0 is None or n1 <= n0)) else n0)
    print(f"{tau0f:>5} {deltaf:>6} {str(epsf):>5} {N:>3} {str(n0):>4} {str(n1):>4} "
          f"{cfidx:>10} {g:>8.4f} {float(mlog(2/eps)/(2*g)) if g>0 else 0:>13.2f} "
          f"{str(ts):>8} {float(nd*delta) if nd else 0:>8.3f} "
          f"{ts*float(delta) if ts else 0:>8.3f}")
    rows.append((tau0f, float(delta), float(eps), N, n0, n1, g, ts))

print("\n--- equilibrium-density prediction for g (local law): g ~ 2 tau0 delta * pi * rho_eq(tau0^2) ---")
for tau0f, deltaf in [(20, '0.3'), (40, '0.3')]:
    tau0 = mpf(tau0f); delta = mpf(deltaf)
    scaled_ats = bg_atoms(60)
    a_s = mre(scaled_ats[0][0]); b_s = mre(scaled_ats[-1][0])
    x0 = (tau0/GAMS[-1])**2/mpf('1.0001')
    rho = 1/(mpi*msqrt((x0 - a_s)*(b_s - x0)))
    scale = 1/GAMS[-1]**2
    gloc = float(2*tau0*delta*scale*mpi*rho)   # local: g ~ pi * rho_eq * dist,  dist = |Im c| = 2 tau0 delta (scaled)
    c = ((tau0 - mpc(0,1)*delta)/GAMS[-1])**2/mpf('1.0001')
    gex = green_interval(c, a_s, b_s)
    print(f"  tau0={tau0f}, delta={deltaf}: local-law g = {gloc:.5f}  exact interval g = {gex:.5f}")

############ FILE: r3_irregular.py ############
"""Round 3 §7: GM-switching pairs — A-cospectral, Ihara-zeta-distinct irregular graphs."""
import numpy as np
from lab_core import charpoly_exact, connected, girth
from mpmath import mp, mpf, mpc, fabs
mp.dps = 40

def gm_pair(n_rest=6, seed=0, ctype='C4'):
    """Base graph on 4+n_rest vertices; switching set C={0,1,2,3} inducing a regular subgraph;
    every rest vertex has 0, 2, or 4 neighbours in C. Returns (A, A_switched) or None."""
    rng = np.random.default_rng(seed)
    n = 4 + n_rest
    A = np.zeros((n, n), dtype=object)
    # C internal: regular subgraph on 4 vertices
    if ctype == 'C4':
        for (i, j) in [(0,1),(1,2),(2,3),(3,0)]:
            A[i][j] = A[j][i] = 1
    elif ctype == 'M':      # perfect matching
        for (i, j) in [(0,1),(2,3)]:
            A[i][j] = A[j][i] = 1
    elif ctype == 'K4':
        for i in range(4):
            for j in range(i+1,4):
                A[i][j] = A[j][i] = 1
    # rest internal: random
    for i in range(4, n):
        for j in range(i+1, n):
            if rng.random() < 0.45:
                A[i][j] = A[j][i] = 1
    # rest -> C: type 0, 2, or 4
    n2 = 0
    for v in range(4, n):
        ty = rng.choice([0, 2, 2, 4])
        if ty == 2:
            pair = rng.choice(4, size=2, replace=False)
            for c in pair:
                A[v][c] = A[c][v] = 1
            n2 += 1
        elif ty == 4:
            for c in range(4):
                A[v][c] = A[c][v] = 1
    if n2 == 0:
        return None
    # switched copy
    B = A.copy()
    for v in range(4, n):
        cnt = sum(int(A[v][c]) for c in range(4))
        if cnt == 2:
            for c in range(4):
                B[v][c] = B[c][v] = 1 - int(A[v][c])
    # sanity
    for M in (A, B):
        if not connected(M):
            return None
        if min(sum(int(x) for x in M[i]) for i in range(n)) < 2:
            return None
    return A, B

def hashimoto(A):
    n = A.shape[0]
    edges = [(i, j) for i in range(n) for j in range(n) if A[i][j]]
    idx = {e: k for k, e in enumerate(edges)}
    m2 = len(edges)
    H = np.zeros((m2, m2), dtype=object)
    for (i, j) in edges:
        for (k, l) in edges:
            if j == k and l != i:
                H[idx[(i,j)]][idx[(k,l)]] = 1
    return H

if __name__ != "__main__":
    import sys
    sys.exit = None  # imported for gm_pair/hashimoto only

found = 0
for seed in (range(400) if __name__ == "__main__" else []):
    for ctype in ['C4', 'M', 'K4']:
        out = gm_pair(6, seed, ctype)
        if out is None:
            continue
        A, B = out
        cA, cB = charpoly_exact(A), charpoly_exact(B)
        if cA != cB:
            continue   # would indicate an implementation bug for GM; skip
        hA, hB = charpoly_exact(hashimoto(A)), charpoly_exact(hashimoto(B))
        if hA != hB:
            n = A.shape[0]
            degA = sorted(sum(int(x) for x in A[i]) for i in range(n))
            degB = sorted(sum(int(x) for x in B[i]) for i in range(n))
            print(f"FOUND (seed={seed}, C-type={ctype}): n={n}, m={sum(degA)//2}")
            print(f"  degree sequences: {degA} | {degB}")
            print(f"  A-charpoly (equal): {cA}")
            diffs = [(k, hA[k], hB[k]) for k in range(len(hA)) if hA[k] != hB[k]]
            print(f"  Ihara (Hashimoto) charpolys DIFFER in {len(diffs)} coefficients; first few:")
            for k, x, y in diffs[:4]:
                print(f"    u^{k}: {x} vs {y}")
            # exact edge lists for the record
            EA = [(i,j) for i in range(n) for j in range(i+1,n) if A[i][j]]
            EB = [(i,j) for i in range(n) for j in range(i+1,n) if B[i][j]]
            print(f"  edges(G):  {EA}")
            print(f"  edges(G'): {EB}")
            # zeta-derived response differs: resolvent of Hashimoto spectrum at test points
            from mpmath import polyroots
            rA = polyroots([mpf(x) for x in reversed(hA)], maxsteps=500, extraprec=200)
            rB = polyroots([mpf(x) for x in reversed(hB)], maxsteps=500, extraprec=200)
            for zt in [mpc('0.3','0.4'), mpc('-0.2','0.7')]:
                qA = sum(1/(zt-r) for r in rA); qB = sum(1/(zt-r) for r in rB)
                print(f"  zeta-resolvent at z={zt}: {complex(qA):.6f} vs {complex(qB):.6f} "
                      f"(|diff| = {float(abs(qA-qB)):.4f})")
            found += 1
            break
    if found:
        break
if not found:
    print("no pair found in search budget")

############ FILE: r5_w1.py ############
"""Round 5, W1: compactified depth law on the genuine a.c. omega>0 measure (scaled model).

KEY LEMMA (exact): the compactified moments are a binomial transform of the Taylor
coefficients of the response at z = -s0:
    q(z) = sum_j c_j (z+s0)^j   =>   mu_hat_k = sum_{j<=k} C(k,j) (-s0)^j c_j .
(The compactification IS re-expansion of the Weyl function about an interior point.)
So moments are computed to ~90 digits by a Cauchy-circle DFT of q -- no quadrature of the
spiky density at all. Background = mock ordinates gamma_j/5 (j<=100) + smooth tail,
Poisson-broadened at shift omega; violating quartet enters q exactly through its pair terms.
"""
import numpy as np
from mpmath import mp, mpf, mpc, fabs, pi as mpi, log as mlog, sqrt as msqrt, matrix, det, \
    zetazero, exp as mexp, binomial
from mpmath import re as mre, im as mim
import numpy.polynomial.legendre as leg

mp.dps = 30
GRAW = [mim(zetazero(j)) for j in range(1, 101)]
mp.dps = 140
GS = [mpf(str(g))/5 for g in GRAW]
S0 = mpf(8)

# smooth-tail quadrature nodes (fixed once): ordinate density 5*log(5u/2pi)/(2pi), weight 2/zero
TT = GS[-1]
tail_nodes = []
for (a, b, npts) in [(TT, 5*TT, 80), (5*TT, 60*TT, 80)]:
    xs, ws = leg.leggauss(npts)
    for x, w in zip(xs, ws):
        u = (mpf(float(x))+1)/2*(b-a) + a
        wq = mpf(float(w))/2*(b-a)
        tail_nodes.append((u, wq * 2 * 5*mlog(5*u/(2*mpi))/(2*mpi)))

def q_full(z, omega, tau=None, delta=None):
    w = msqrt(-z)
    v = omega + w
    h = mpc(0)
    for g in GS:
        h += 2*v/(v**2 + g**2)
    for u, wt in tail_nodes:
        h += wt * 2*v/(v**2 + u**2)
    if tau is not None:
        for gv in (tau - mpc(0,1)*delta, tau + mpc(0,1)*delta):
            h += 2*v/(v**2 + gv**2)
    return h/w

def compact_moments(omega, tau, delta, kmax, M=1024, rfrac='0.7'):
    """mu_hat_k via Cauchy-circle DFT at -s0 + r e^{i theta} and binomial transform."""
    r = S0*mpf(rfrac)
    vals = []
    for m in range(M):
        th = 2*mpi*m/M
        z = -S0 + r*mexp(mpc(0,1)*th)
        vals.append(q_full(z, omega, tau, delta))
    chat = []   # c_j * r^j
    for j in range(kmax+1):
        s = mpc(0)
        for m in range(M):
            th = 2*mpi*m/M
            s += vals[m]*mexp(-mpc(0,1)*j*th)
        chat.append(mre(s)/M)
    mus = []
    for k in range(kmax+1):
        s = mpf(0)
        for j in range(k+1):
            s += binomial(k, j) * (-S0/r)**j * chat[j]
        mus.append(s)
    return mus

def first_fail(mus, shift, nmax):
    for n in range(2, nmax):
        Mx = matrix(n, n)
        for i in range(n):
            for j in range(n):
                Mx[i, j] = mus[i+j+shift]
        if mre(det(Mx)) < 0:
            return n
    return None

def green01(c):
    x = 2*mpc(c) - 1
    return float(mre(mlog(x + msqrt(x-1)*msqrt(x+1))))

print("=== sanity: moment lemma vs direct atom check on a toy rational q ===")
toy = [(mpf(2), mpf('0.7')), (mpf(11), mpf('1.3'))]
def q_toy(z):
    return sum(w/(t-z) for t, w in toy)
r = S0*mpf('0.7'); M = 512
vals = [q_toy(-S0 + r*mexp(mpc(0,1)*2*mpi*m/M)) for m in range(M)]
chat = [mre(sum(vals[m]*mexp(-mpc(0,1)*j*2*mpi*m/M) for m in range(M)))/M for j in range(31)]
worst = mpf(0)
for k in [0, 3, 10, 30]:
    lemma = sum(binomial(k, j)*(-S0/r)**j*chat[j] for j in range(k+1))
    direct = sum(w*(t/(S0+t))**k/(S0+t) for t, w in toy)
    worst = max(worst, fabs(lemma-direct))
print("  worst |lemma - direct| over k=0,3,10,30:", float(worst))

print("\n=== control: undefected omega-measure is Stieltjes-clean ===")
mus0 = compact_moments(mpf('0.3'), None, None, 60)
print("  mu_0 =", float(mus0[0]), "  first_fail H:", first_fail(mus0, 0, 28),
      "  H':", first_fail(mus0, 1, 28))

print("\n=== W1 main: detection depth on the a.c. omega>0 compactified measure ===")
print(f"{'tau':>4} {'delta':>6} {'omega':>6} {'d-w':>5} {'n0':>4} {'n1':>4} {'g(x_c)':>9} "
      f"{'|eps|':>8} {'pred':>6} {'ratio':>6}")
cases = [(4, 0.7, 0.3), (4, 0.5, 0.3), (4, 0.9, 0.3), (6, 0.7, 0.3), (6, 1.1, 0.3),
         (4, 0.45, 0.15), (4, 0.35, 0.15), (9, 1.5, 0.3)]
for tau_f, dl_f, om_f in cases:
    tau, dl, om = mpf(tau_f), mpf(str(dl_f)), mpf(str(om_f))
    mus = compact_moments(om, tau, dl, 100)
    n0 = first_fail(mus, 0, 48)
    n1 = first_fail(mus, 1, 48)
    w1 = (dl-om) + mpc(0,1)*tau
    z1 = -w1**2
    xc = z1/(S0+z1)
    g = green01(xc)
    eps = float(2/abs(S0+z1))
    pred = float(mlog(1/mpf(str(eps)))/(2*g))
    nd = n1 if (n1 is not None and (n0 is None or n1 <= n0)) else n0
    print(f"{tau_f:>4} {dl_f:>6} {om_f:>6} {dl_f-om_f:>5.2f} {str(n0):>4} {str(n1):>4} "
          f"{g:>9.5f} {eps:>8.4f} {pred:>6.1f} {(nd/pred if nd else 0):>6.2f}")
