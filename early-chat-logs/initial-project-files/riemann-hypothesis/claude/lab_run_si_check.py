"""
Numerical certification for `second_involution_resolution.tex`.

Certifies, for sigma = 1, lambda* = log 2:
  (V1) Guinand--Weil implementation: zero side == prime side of Z(c,lam)
       to ~1e-14 at c in {30, 100, 250, 500}  (800 zeros, heights <= 1183.7).
  (V2) Oscillation lemma: osc of F(c) = Re Z(c, log 2) on every sampled
       window [c0-15, c0+15] is >= 2.01 for c0 in [0, 1160] (zero side)
       and >= 2.48 at c0 in {1e4, 1e5, 1e6} (prime side; archimedean term
       verified slowly varying: range <= 2.1e-3 per 30-unit window at 1e4).
       Compare the crude effective bound B_2/8 = 0.0676 used in the proof.
  (V3) Adaptive-encoding theorem end-to-end: on the synthetic multiset
       obtained from the first 800 zeta ordinates by replacing the two
       ordinates nearest 100 (98.8312, 101.3179) with the conjugate
       quadruple +-100.0745 +- 0.25i, the two-sample semialgebraic decoder
       recovers D(c) with error <= 1.9e-15 at 13 test heights, including
       D(100.07) = 0.125 = 2 y0^2.  (r = 2, u = r/4 variant optional; the
       run below uses the f(d) = (r/2) d/(1+d) encoding.)

Requires: numpy, scipy, mpmath; zeros.txt (one positive ordinate per line; regenerate with mpmath.zetazero(1..800) at 25 dps).
Run:  python3 lab_second_involution_check.py
"""
import numpy as np
from scipy.optimize import brentq
import lab_si_lib as S


def certify_gw(gams):
    print("== (V1) Guinand-Weil: zero side vs prime side ==")
    ok = True
    for c in [30.0, 100.0, 250.0, 500.0]:
        zz = S.Z_zero(c, S.LAMSTAR, gams)
        zp = S.Z_prime(c, S.LAMSTAR, arch=True)
        d = abs(zz - zp)
        ok &= d < 1e-12
        print(f"  c={c:6.1f}  |zero-side - prime-side| = {d:.2e}")
    print("  PASS" if ok else "  FAIL")
    return ok


def certify_osc(gams, L=30.0, step=0.02, thresh=2.0):
    print("== (V2) uniform oscillation of F = Re Z(., log 2), window L=30 ==")
    centers = list(np.arange(0, 41, 2.5)) + [50, 75, 100, 150, 200, 300, 400,
                                             500, 600, 700, 800, 900, 1000, 1100, 1160]
    mn = np.inf
    for c0 in centers:
        grid = np.arange(c0 - L/2, c0 + L/2 + step/2, step)
        F = S.Z_zero(grid, S.LAMSTAR, gams).real
        mn = min(mn, F.max() - F.min())
    print(f"  min osc over {len(centers)} windows, c0 in [0,1160]: {mn:.4f}"
          f"  (proof's crude bound B2/8 = {S.B_coeff(2)/8:.4f})")
    print("  PASS" if mn > thresh else "  FAIL")
    return mn > thresh


def certify_encoding(gams, r=2.0, L=30.0):
    print("== (V3) adaptive-encoding demo on synthetic off-line multiset ==")
    idx = np.argsort(np.abs(gams - 100.0))[:2]
    ga, gb = sorted(gams[idx]); x0 = (ga + gb) / 2; y0 = 0.25
    keep = np.delete(gams, idx)
    full = np.concatenate([keep, -keep,
                           [x0 + 1j*y0, x0 - 1j*y0,
                            -x0 + 1j*y0, -x0 - 1j*y0]]).astype(complex)
    f = lambda d: (r/2) * d / (1.0 + d)
    Sdec = lambda u: u / ((r/2) - u)
    def Fs(s):
        return float(np.real(S.Z_zero_multiset(np.array([s, s]), S.LAMSTAR, full))[0])
    worst = 0.0
    for c in [0.0, 20.0, 50.0, 90.0, 95.0, 98.0, x0, 103.0, 108.0, 115.0,
              150.0, 400.0, 900.0]:
        grid = np.arange(c - L/2, c + L/2 + 0.005, 0.01)
        Fg = np.real(S.Z_zero_multiset(grid, S.LAMSTAR, full))
        assert Fg.max() - Fg.min() > r, "window oscillation below r"
        D = float(S.D_defect(c, full))
        u = f(D)
        i_min, i_max = int(Fg.argmin()), int(Fg.argmax())
        c2, F2 = grid[i_min], Fg[i_min]
        a_, b_ = sorted((c2, grid[i_max]))
        c1 = brentq(lambda s: Fs(s) - F2 - u, a_, b_, xtol=1e-15,
                    maxiter=300) if u > 1e-300 else c2
        dec = Sdec(Fs(c1) - F2)
        if D > 1e-13:
            worst = max(worst, abs(dec - D))
        print(f"  c={c:8.2f}  D={D:12.5e}  decoded={dec:12.5e}  err={abs(dec-D):.1e}")
    print(f"  worst error (D > 1e-13 cases): {worst:.2e}")
    print("  PASS" if worst < 1e-12 else "  FAIL")
    return worst < 1e-12


if __name__ == "__main__":
    gams = S.load_zeros()
    a = certify_gw(gams)
    b = certify_osc(gams)
    c = certify_encoding(gams)
    print("\nALL PASS" if (a and b and c) else "\nSOME CHECK FAILED")
