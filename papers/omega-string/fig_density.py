# Figure 1 of "The shifted zeta string": Poisson-smoothed zero spectral measure.
# Left: rho_{1/2}(u) on [0,60] vs the Riemann-von Mangoldt mean density.
# Right: the full closed-form density near gamma_1 for omega = 0.5, 0.25, 0.1.
# Requires mpmath, numpy, matplotlib. Runtime: a few minutes.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpmath import mp, mpc, zeta, digamma, log, pi, re, mpmathify

mp.dps = 15

def xilogd(s):
    """(xi'/xi)(s) via 1/s + 1/(s-1) - (log pi)/2 + psi(s/2)/2 + (zeta'/zeta)(s)."""
    s = mpmathify(s)
    return 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 + zeta(s, derivative=1)/zeta(s)

def rho(om, u):
    """rho_omega(u) = (1/pi) Re (xi'/xi)(1/2+omega+iu)."""
    return float(re(xilogd(mpc(0.5+om, u)))/pi)

# panel (a): omega = 1/2, u in (0, 60]
ua = np.linspace(0.02, 60.0, 1400)
ra = np.array([rho(0.5, u) for u in ua])
rvm = np.where(ua > 2*np.pi*np.e, np.log(ua/(2*np.pi))/(2*np.pi), np.nan)

# panel (b): zoom at gamma_1, omega = 0.5, 0.25, 0.1
g1 = 14.134725141734693
ub = np.linspace(12.6, 15.7, 900)
oms = [0.5, 0.25, 0.1]
rb = {om: np.array([rho(om, u) for u in ub]) for om in oms}

# colorblind-safe fixed-order hues
C = ['#0173B2', '#DE8F05', '#029E73']
ink, muted = '#1a1a1a', '#666666'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.6, 3.9), dpi=200,
                               gridspec_kw={'width_ratios': [1.55, 1]})
for ax in (ax1, ax2):
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_color(muted)
    ax.tick_params(colors=muted, labelsize=8.5)
    ax.grid(True, axis='y', color='#dddddd', lw=0.6, zorder=0)

ax1.plot(ua, ra, color=C[0], lw=1.4, zorder=3)
ax1.plot(ua, rvm, color=muted, lw=1.1, ls=(0, (5, 3)), zorder=2)
ax1.set_xlabel('$u$', fontsize=10, color=ink)
ax1.set_ylabel(r'$\rho_{1/2}(u)$', fontsize=10, color=ink)
ax1.set_xlim(0, 60); ax1.set_ylim(0, None)
rho0 = 0.0073515925
ax1.text(4.0, rho0+0.022, r'$\rho_{1/2}(0)=\pi^{-1}(\xi^{\prime}/\xi)(1)$',
         fontsize=8, color=ink)
ax1.annotate('', xy=(0.35, rho0+0.004), xytext=(3.8, rho0+0.021),
             arrowprops=dict(arrowstyle='-', lw=0.7, color=muted))
ax1.text(1.8, 0.545, 'Riemann–von Mangoldt\nmean density (dashed)',
         fontsize=8, color=muted, ha='left')
ax1.set_title(r'Poisson-smoothed zero spectral measure  ($\omega=\frac{1}{2}$)',
              fontsize=10.5, color=ink, pad=8)

for om, c in zip(oms, C):
    ax2.plot(ub, rb[om], color=c, lw=1.4, zorder=3)
ax2.axvline(g1, color='#bbbbbb', lw=0.8, ls=':', zorder=1)
ax2.set_xlabel('$u$', fontsize=10, color=ink)
ax2.set_xlim(ub[0], ub[-1]); ax2.set_ylim(0, None)
ax2.text(g1, ax2.get_ylim()[1]*0.02, r'$\gamma_1$', fontsize=9, color=muted,
         ha='left', va='bottom')
lab_pos = {0.5: (15.05, 0.70), 0.25: (14.75, 1.32), 0.1: (14.42, 3.05)}
for om, c in zip(oms, C):
    x, y = lab_pos[om]
    ax2.text(x, y, r'$\omega=%.2g$' % om, fontsize=8.5, color=c, va='bottom')
ax2.set_title(r'Full spectral density near $\gamma_1$ as $\omega\downarrow 0$',
              fontsize=10.5, color=ink, pad=8)

fig.tight_layout()
fig.savefig('fig_density.png', bbox_inches='tight', facecolor='white')
print('saved fig_density.png')
