"""Experiments: (1) Laguerre positivity for Xi, (2) Laguerre dips for DH at its
zero spheres, (3) l-graded sector-energy scaling in the sphere radius."""
import numpy as np, mpmath as mp, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from xi_lib import xi_int, Xi_DH, sector_energy, zeta_ordinates
mp.mp.dps = 40

results = {}

# ---------------- Exp 1: Laguerre for Xi on the axis --------------------
X1 = np.linspace(0.0, 60.0, 1201)
F, F1, F2 = xi_int(X1, 0), xi_int(X1, 1), xi_int(X1, 2)
L1_xi = F1**2 - F * F2
L1_rel = L1_xi / (F1**2 + np.abs(F*F2) + 1e-300)
mask52 = X1 <= 52.0
print(f"[1] Laguerre for Xi: min relative L1 on [0,52] = {L1_rel[mask52].min():.3f}; "
      f"on [0,60] the min ({L1_rel.min():.3e}) sits at the ~1e-34 float64 quadrature floor "
      f"beyond x~55 (raw min {L1_xi.min():.1e}) -- no verdict there without higher precision")

# ---------------- Exp 2: Laguerre for DH near its zero spheres ----------
spheres = [(85.6993484854, 0.30851718), (114.1633426857, 0.15083008), (166.4793059, 0.07435605)]
def W_grid(x0, x1, h):
    xs = np.arange(x0, x1 + h/2, h)
    vals = np.array([float(mp.e**(mp.pi*mp.mpf(str(x))/4) * Xi_DH(mp.mpf(str(x))).real) for x in xs])
    return xs, vals
def L1_from_grid(xs, vals):
    h = xs[1]-xs[0]
    d1 = (vals[2:]-vals[:-2])/(2*h); d2 = (vals[2:]-2*vals[1:-1]+vals[:-2])/h**2
    return xs[1:-1], d1**2 - vals[1:-1]*d2

panels = []
for (a, y0) in spheres[:2]:
    xs, vals = W_grid(a-4*y0, a+4*y0, y0/12)
    xm, L1 = L1_from_grid(xs, vals)
    neg = xm[L1 < 0]
    lo, hi = (neg.min(), neg.max()) if neg.size else (np.nan, np.nan)
    print(f"[2] DH sphere a={a:.4f} y0={y0:.4f}: min L1={L1.min():.3e}, "
          f"negative on [{lo:.3f},{hi:.3f}] (predicted [{a-y0:.3f},{a+y0:.3f}])")
    panels.append((a, y0, xm, L1))
# control stretch away from spheres (on-line zeros only)
xs, vals = W_grid(78.0, 82.0, 0.02)
xm_c, L1_c = L1_from_grid(xs, vals)
print(f"[2] DH control [78,82]: min L1 = {L1_c.min():.3e} (positive: {bool((L1_c>0).all())})")

# ---------------- Exp 3: sector-energy scaling in radius ----------------
tk = zeta_ordinates(20)
real_zeros = [(t, 0.0) for t in tk]
y0s = np.logspace(-3, -0.5, 9)
E = {ell: [] for ell in (1, 2, 3)}
for y0 in y0s:
    zs = real_zeros + [(28.0, float(y0))]
    for ell in E:
        E[ell].append(sector_energy(zs, ell))
slopes = {}
for ell in E:
    logy, logE = np.log(y0s), np.log(E[ell])
    slopes[ell] = np.polyfit(logy[:6], logE[:6], 1)[0]
    print(f"[3] sector l={ell}: log-log slope = {slopes[ell]:.3f} (predicted {2*ell})")
E1_real_only = sector_energy(real_zeros, 1)
print(f"[3] E_1 with real zeros only = {E1_real_only:.2e} (exact 0 up to roundoff)")
# per-sphere E_1 for the actual DH spheres (radius attenuation on real data)
for (a, y0) in spheres:
    print(f"[3] DH sphere y0={y0:.4f}: per-sphere E_1 = {sector_energy([(a,y0)],1):.3e}")

# ---------------- Figure --------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))
ax = axes[0]
ax.semilogy(X1, L1_xi, 'b-', lw=1)
ax.set_title(r'Riemann $\Xi$: Laguerre $L_1 > 0$ (no dips)')
ax.set_xlabel('x'); ax.set_ylabel(r'$L_1[\Xi](x)$')
ax = axes[1]
for (a, y0, xm, L1), c in zip(panels, ('tab:red', 'tab:orange')):
    ax.plot(xm - a, L1 / np.abs(L1).max(), c, lw=1.4, label=f'sphere $y_0$={y0:.3f}')
    ax.axvspan(-y0, y0, color=c, alpha=0.12)
ax.axhline(0, color='k', lw=0.6)
ax.set_title(r'Davenport--Heilbronn: $L_1<0$ inside $|x-a|<y_0$')
ax.set_xlabel(r'$x-a$'); ax.set_ylabel(r'$L_1$ (normalized)'); ax.legend(fontsize=8)
ax = axes[2]
for ell, mk in zip((1, 2, 3), ('o-', 's-', '^-')):
    ax.loglog(y0s, E[ell], mk, ms=4, label=fr'$\ell$={ell}: slope {slopes[ell]:.2f}')
ax.set_title(r'Sector energies: $\mathcal{E}_\ell \propto y_0^{2\ell}$')
ax.set_xlabel(r'sphere radius $y_0$'); ax.set_ylabel(r'$\mathcal{E}_\ell$'); ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig('lab_results.pdf')
plt.savefig('lab_results.png', dpi=140)
print('figure saved')
