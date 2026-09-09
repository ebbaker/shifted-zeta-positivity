"""h4_beta.py -- portability test: Dirichlet beta (L(s, chi_4)).

Xi_beta(z) = (pi/4)^{-(s+1)/2} Gamma((s+1)/2) L(s, chi_4),  s = 1/2 + i z:
even, entire, real on R.  Uses the cached 70 zeros (beta_zeros.json) if
present, else finds them by sign scanning; then runs the smooth-density-tail
null test at gamma_11, gamma_21, gamma_31.
"""
import json
import os
from mpmath import mp, mpf, mpc, pi, gamma as G, zeta, quad, inf, diff, findroot, re

mp.dps = 25


def L4(s):
    return (zeta(s, mpf(1) / 4) - zeta(s, mpf(3) / 4)) / 4 ** s


def Xib(z):
    s = mpf('0.5') + mpc(0, 1) * z
    return re((pi / 4) ** (-(s + 1) / 2) * G((s + 1) / 2) * L4(s))


CACHE = "beta_zeros.json"
if os.path.exists(CACHE):
    zs = [mpf(x) for x in json.load(open(CACHE))]
else:
    zs, step, x = [], mpf('0.05'), mpf('0.5')
    prev = Xib(x)
    while len(zs) < 70:
        x2 = x + step
        cur = Xib(x2)
        if prev * cur < 0:
            zs.append(findroot(Xib, (x, x2), solver='bisect',
                               tol=mpf(10) ** -22))
        x, prev = x2, cur
    json.dump([mp.nstr(z, 25) for z in zs], open(CACHE, "w"))

K = len(zs)
zf = [float(z) for z in zs]
U = zs[-1] + (zs[-1] - zs[-2]) / 2
print(f"K = {K} zeros, first three: " + ", ".join(f"{z:.6f}" for z in zf[:3]))

# empirical density check at T = 75
count = sum(1 for z in zf if z <= 75)
smooth = quad(lambda u: mp.log(2 * u / pi) / (2 * pi), [mpf('0.01'), 75])
print(f"density check at T=75: measured N/T = {count/75:.4f}, "
      f"smooth = {float(smooth)/75:.4f}")

for j in (10, 20, 30):  # gamma_11, _21, _31
    g = zs[j]
    V = diff(Xib, g, 2) / diff(Xib, g, 1)
    vis = mpf(0)
    for k in range(K):
        if k != j:
            vis += 2 / (g - zs[k])
        vis += 2 / (g + zs[k])
    tail = quad(lambda u: 4 * g / (g ** 2 - u ** 2)
                * mp.log(2 * u / pi) / (2 * pi), [U, 2 * U, 10 * U, inf])
    R = V - vis - tail
    print(f"gamma_{j+1} = {float(g):9.4f}   residual {float(R):+.2e}")
