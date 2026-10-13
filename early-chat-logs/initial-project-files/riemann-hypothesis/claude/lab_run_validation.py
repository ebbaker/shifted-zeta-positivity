"""Validation driver: certifies the claims of Appendix A.1.

(1) The cosine-transform Xi matches the mpmath xi(1/2+ix) at x in {0,5,20,30}
    and vanishes at the first zero ordinate to the quadrature floor.
(2) Xi_DH is real and even on the real axis (sampled), at 30-digit precision.
(3) Newton iteration on f_DH recovers the three classical off-line zeros
    (the zero spheres), starting from crude seeds.
(4) The DH on-line ordinates in [74,97] are recovered by sign-change
    bisection of Xi_DH.
"""
import numpy as np, mpmath as mp
from xi_lib import xi_int, xi_mp, Xi_DH, f_DH

mp.mp.dps = 30

# ---------------- (1) Xi validation ----------------
print("[V1] cosine transform vs mpmath xi:")
for x in (0.0, 5.0, 20.0, 30.0):
    a, b = xi_int(x), xi_mp(x).real
    print(f"    x={x}: Xi_int={a:.12g}  xi_mp={b:.12g}  rel.err={abs(a-b)/abs(b):.2e}")
z1 = float(mp.im(mp.zetazero(1)))
print(f"    first ordinate {z1:.12f}: Xi_int = {xi_int(z1):.2e} (quadrature floor)")

# ---------------- (2) DH reality/evenness ----------------
print("[V2] Xi_DH real and even on the axis (dps=30):")
worst_im, worst_ev = 0.0, 0.0
for x in (3.0, 17.5, 42.0, 85.7, 114.2):
    v, vm = Xi_DH(mp.mpf(str(x))), Xi_DH(mp.mpf(str(-x)))
    worst_im = max(worst_im, float(abs(mp.im(v))) / max(float(abs(v)), 1e-300))
    worst_ev = max(worst_ev, float(abs(v - vm)) / max(float(abs(v)), 1e-300))
print(f"    max relative |Im Xi_DH| = {worst_im:.1e};  max relative |Xi_DH(x)-Xi_DH(-x)| = {worst_ev:.1e}")

# ---------------- (3) DH off-line zeros by Newton ----------------
print("[V3] Newton on f_DH from crude seeds (the three classical off-line zeros):")
seeds = [0.8 + 85.7j, 0.65 + 114.2j, 0.57 + 166.5j]
for s0 in seeds:
    r = mp.findroot(f_DH, mp.mpc(s0))
    sig, tau = float(mp.re(r)), float(mp.im(r))
    print(f"    seed {s0} -> s = {sig:.9f} + {tau:.9f}i  "
          f"(sphere a={tau:.6f}, y0={sig-0.5:.6f});  |f_DH| = {float(abs(f_DH(r))):.1e}")

# ---------------- (4) DH on-line ordinates by bisection ----------------
print("[V4] DH on-line ordinates in [74,97] by sign change + bisection of Xi_DH:")
def XDH(x):
    return float(Xi_DH(mp.mpf(str(x))).real)
xs = np.arange(74.0, 97.0, 0.05)
vals = [XDH(x) for x in xs]
roots = []
for i in range(len(xs) - 1):
    if vals[i] * vals[i+1] < 0:
        lo, hi = xs[i], xs[i+1]
        for _ in range(40):
            midp = 0.5 * (lo + hi)
            if XDH(lo) * XDH(midp) <= 0:
                hi = midp
            else:
                lo = midp
        roots.append(0.5 * (lo + hi))
print("    " + ", ".join(f"{r:.3f}" for r in roots))
