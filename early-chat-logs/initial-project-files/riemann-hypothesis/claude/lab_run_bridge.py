"""Bridge experiments: (A) certify the explicit formula on the Gaussian family,
(B) rate experiment: limsup log|Z|/lambda reads off the largest sphere radius,
plus the bridge_results figure and the i_l Gegenbauer identity check."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import spherical_in
from explicit_formula import (zeta_zeros, zero_side, prime_side, arch_side,
                              pole_side, h_val)

SIG = 2.0

# ---------------- (A) EF certification ----------------
zs = zeta_zeros(250)
real_pairs = [(t, 0.0) for t in zs]
print("[A] EF certification (250 zeros, sigma=2):")
for (c, lam) in [(20,0.0),(20,1.0),(20,2.0),(20,3.0),(35,2.0)]:
    L = zero_side(real_pairs, c, lam, SIG)
    R = pole_side(c, lam, SIG) + arch_side(c, lam, SIG) + prime_side(c, lam, SIG)
    print(f"    (c,lam)=({c},{lam}): zero side = {L:.8f}, |Delta| = {abs(L-R):.2e}")

# ---------------- (B) rate experiment ----------------
DH_ONLINE = [74.325, 75.909, 77.226, 78.717, 80.328, 81.925, 83.109, 87.647,
             89.439, 90.725, 92.183, 93.781, 95.349, 96.292]
DH_SPHERE = (85.699348, 0.308517)

datasets = {
    'zeta (250 real), c=20':        ([(t,0.0) for t in zs], 20.0),
    'zeta + implant y0=0.1, c=20':  ([(t,0.0) for t in zs] + [(20.0, 0.1)], 20.0),
    'DH on-line only, c=85.7':      ([(t,0.0) for t in DH_ONLINE], 85.7),
    'DH with sphere, c=85.7':       ([(t,0.0) for t in DH_ONLINE] + [DH_SPHERE], 85.7),
}
lams = np.linspace(0.5, 25.0, 120)
fig, ax = plt.subplots(figsize=(7.2, 4.6))
styles = ['k-', 'tab:blue', 'tab:green', 'tab:red']
for (label, (zset, c)), st in zip(datasets.items(), styles):
    Z2 = np.array([abs(zero_side(zset, c, l, SIG))**2 for l in lams])
    mask = lams > 15.0
    slope = np.polyfit(lams[mask], 0.5*np.log(Z2[mask]), 1)[0]
    print(f"[B] {label}: fitted rate = {slope:.4f}, |Z|^2 at lam=25 = {Z2[-1]:.3g}")
    ax.semilogy(lams, Z2, st, lw=1.4, label=f"{label} (rate {slope:.3f})")
ax.set_xlabel(r'$\lambda$ (log prime scale)')
ax.set_ylabel(r'$|Z(c,\lambda)|^2$')
ax.set_title(r'Sphere anomaly: $\limsup_\lambda \log|Z|/\lambda = \sup_\rho y_\rho$')
ax.legend(fontsize=8)
plt.tight_layout()
plt.savefig('bridge_results.pdf')
plt.savefig('bridge_results.png', dpi=140)
print('figure saved')

# ---------------- (C) Gegenbauer identity check ----------------
print("[C] sinh(2z)/(2z) = sum (2l+1) i_l(z)^2:")
for z in (0.5, 1.0, 2.0, 4.0):
    s = sum((2*l+1)*spherical_in(l, z)**2 for l in range(80))
    ref = np.sinh(2*z)/(2*z)
    print(f"    z={z}: |Delta| = {abs(s-ref):.2e}")
