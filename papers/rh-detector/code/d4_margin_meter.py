"""d4_margin_meter.py -- local De Bruijn--Newman margin via the CM pencil.

Feed a detected hidden configuration plus the nearest visible zeros into the
Calogero--Moser pencil X + tY and bisect on reality of the spectrum: the
threshold is the interaction-corrected local margin (the off-axis analogue of
the Lehmer-pair machinery).  Isolated benchmark: an off-axis quadruple
+-(tau +- i sigma) alone has threshold ~ sigma^2/2 for well-separated centres.
"""
import numpy as np
from mpmath import mp, zetazero

mp.dps = 25
G = np.array([float(zetazero(n).imag) for n in range(1, 81)])
I45, I46 = 44, 45
tau0 = 0.5 * (G[I45] + G[I46])
vis = np.delete(G, [I45, I46])


def cm_pair(roots):
    z = np.asarray(roots, dtype=complex)
    n = len(z)
    X = np.diag(z)
    Y = np.zeros((n, n), dtype=complex)
    for j in range(n):
        Y[j, j] = sum(2.0 / (z[j] - z[k]) for k in range(n) if k != j)
        for k in range(n):
            if j != k:
                Y[j, k] = 2.0 / (z[j] - z[k])
    return X, Y


def pencil_lambda(roots, hi=4.0, tol=1e-10):
    X, Y = cm_pair(roots)

    def isreal(t):
        return np.abs(np.linalg.eigvals(X + t * Y).imag).max() < 1e-8

    lo = 0.0
    assert isreal(hi) and not isreal(lo)
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if isreal(mid):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


print(f"{'sigma':>6} {'isolated quad':>14} {'with 2x6 local zeros':>21} "
      f"{'sigma^2/2':>10}")
for sigma in (0.8, 0.4, 0.2):
    quad_roots = [complex(tau0, sigma), complex(tau0, -sigma),
                  complex(-tau0, sigma), complex(-tau0, -sigma)]
    lam_iso = pencil_lambda(quad_roots)
    # nearest 6 visible zeros on each side of tau0, with mirrors
    order = np.argsort(np.abs(vis - tau0))
    near = vis[order[:6]]
    ctx = quad_roots + [complex(g, 0) for g in near] \
        + [complex(-g, 0) for g in near]
    lam_ctx = pencil_lambda(ctx)
    print(f"{sigma:>6} {lam_iso:>14.6f} {lam_ctx:>21.6f} {sigma**2/2:>10.6f}")
