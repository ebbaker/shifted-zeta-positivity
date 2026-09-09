"""d1_synthetic.py -- injection tests for the velocity-residual detector.

Protocol (Round 3): take the first 80 true zeta ordinates; remove zeros #45,#46
and replace them by a hidden configuration centred at their midpoint tau:
  - off-axis quadruple  +-(tau +- i sigma)   (contributes two "missing" ordinates)
  - on-axis pair        +-(tau +- a)         (two real zeros the list doesn't show)
  - empty control       (no replacement, complete list)
The detector sees only the visible real ordinates and the exact velocities
  V_j = sum over the TRUE multiset (both signs) of 2/(gamma_j - rho).
Residual: R_j = V_j - (sum over visible list, both signs).
Model fit (d2 part): compare the exact off-axis model
  F_off(x) = 2/(x-tau-i s) + 2/(x-tau+i s) + 2/(x+tau-i s) + 2/(x+tau+i s)
with the exact on-axis model (s -> a, poles at +-(tau+-a)), fit (tau, s) by
least squares on the residuals, report rms and model separation.
"""
import json
import numpy as np
from scipy.optimize import least_squares
from mpmath import mp, zetazero

mp.dps = 25
G = [float(zetazero(n).imag) for n in range(1, 81)]
G = np.array(G)

I45, I46 = 44, 45  # zeros #45, #46 (0-based)
tau0 = 0.5 * (G[I45] + G[I46])
visible_mask = np.ones(80, bool)
visible_mask[[I45, I46]] = False
VIS = G[visible_mask]


def field_at(x, rho_list):
    """sum of 2/(x - rho) over multiset rho_list (real x)."""
    return sum((2.0 / (x - r) for r in rho_list), 0j)


def true_multiset(hidden):
    rho = []
    for g in VIS:
        rho += [g, -g]
    rho += hidden
    return rho


def residuals(hidden):
    rho = true_multiset(hidden)
    out = []
    for j, g in enumerate(VIS):
        others = [r for r in rho if r != g]  # remove the zero itself once
        V = field_at(g, others).real
        vis_field = sum(2.0 / (g - h) for h in VIS if h != g) \
            + sum(2.0 / (g + h) for h in VIS)
        out.append(V - vis_field)
    return np.array(out)


def model_off(params, x):
    tau, s = params
    z = [complex(tau, s), complex(tau, -s), complex(-tau, s), complex(-tau, -s)]
    return np.array([sum(2.0 / (xx - r) for r in z).real for xx in x])


def model_on(params, x):
    tau, a = params
    z = [tau + a, tau - a, -tau - a, -tau + a]
    return np.array([sum(2.0 / (xx - r) for r in z).real for xx in x])


def fit(model, R, x, p0):
    sol = least_squares(lambda p: model(p, x) - R, p0, xtol=1e-15, ftol=1e-15)
    rms = np.sqrt(np.mean((model(sol.x, x) - R) ** 2))
    return sol.x, rms


cases = [
    ("off-axis sigma=0.8", [complex(tau0, 0.8), complex(tau0, -0.8),
                            complex(-tau0, 0.8), complex(-tau0, -0.8)], "off"),
    ("off-axis sigma=0.2", [complex(tau0, 0.2), complex(tau0, -0.2),
                            complex(-tau0, 0.2), complex(-tau0, -0.2)], "off"),
    ("on-axis a=0.3", [tau0 + 0.3, tau0 - 0.3, -tau0 - 0.3, -tau0 + 0.3], "on"),
    ("on-axis a=0.9", [tau0 + 0.9, tau0 - 0.9, -tau0 - 0.9, -tau0 + 0.9], "on"),
    ("empty (control)", [], "none"),
]

print(f"hidden centre tau0 = {tau0:.6f}  (midpoint of zeros #45,#46)")
print()
for name, hidden, kind in cases:
    R = residuals(hidden)
    if kind == "none":
        print(f"{name:>22}:  max|R_j| = {np.abs(R).max():.3e}  (should be ~0)")
        continue
    x = VIS
    p_off, rms_off = fit(model_off, R, x, [tau0 + 0.5, 0.5])
    p_on, rms_on = fit(model_on, R, x, [tau0 + 0.5, 0.5])
    sep = (rms_on / rms_off) if kind == "off" else (rms_off / rms_on)
    best = p_off if kind == "off" else p_on
    print(f"{name:>22}:  fitted (tau, par) = ({best[0]:.10f}, {abs(best[1]):.10f})"
          f"   rms(correct) = {min(rms_off, rms_on):.2e}"
          f"   separation = {sep:.2e}")
