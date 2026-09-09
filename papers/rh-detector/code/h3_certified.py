"""h3_certified.py -- certified velocity-residual null test on Xi.

R_j = V_j - [visible field from gamma_1..gamma_K, both signs] - T_j,
V_j = Xi''(gamma_j)/Xi'(gamma_j),
T_j = int_U^inf f theta'/pi du - f(U) S(U) - int_U^inf f' S du,
f(u) = 4 gamma_j/(gamma_j^2 - u^2),
S(U) = K - theta(U)/pi - 1  (exact at a truncation point separating the zeros),
the last integral bounded by eps_j = int_U^inf f'(u) B(u) du with Trudgian's
unconditional |S(u)| <= B(u) = 0.111 log u + 0.275 log log u + 2.450 (u >= e).

Requires zeros1001.json from h1_zeros1000.py.
"""
import json
from mpmath import mp, mpf, pi, log, gamma as G, zeta, siegeltheta, quad, inf, diff

mp.dps = 30

with open("zeros1001.json") as f:
    Z = [mpf(s) for s in json.load(f)]
K = 1000
gam = Z[:K]
U = (Z[K - 1] + Z[K]) / 2
S_U = K - siegeltheta(U) / pi - 1
print(f"K = {K},  U = {mp.nstr(U, 10)},  exact S(U) = {mp.nstr(S_U, 6)}")


def xi(s):
    return s * (s - 1) / 2 * pi ** (-s / 2) * G(s / 2) * zeta(s)


def Xi(z):
    return xi(mpf('0.5') + 1j * z)


def V_at(g):
    d1 = diff(Xi, g, 1)
    d2 = diff(Xi, g, 2)
    return (d2 / d1).real


def visible_field(j):
    g = gam[j]
    s = mpf(0)
    for k in range(K):
        if k != j:
            s += 2 / (g - gam[k])
        s += 2 / (g + gam[k])
    return s


def tail_and_band(g):
    def f(u):
        return 4 * g / (g ** 2 - u ** 2)

    def fp(u):
        return 8 * g * u / (g ** 2 - u ** 2) ** 2

    t1 = quad(lambda u: f(u) * siegeltheta(u, derivative=1) / pi, [U, 10 * U, inf])
    t2 = -f(U) * S_U
    T = t1 + t2
    B = lambda u: mpf('0.111') * log(u) + mpf('0.275') * log(log(u)) + mpf('2.450')
    eps = quad(lambda u: fp(u) * B(u), [U, 10 * U, inf])
    return T, eps


targets = [103.7, 146.0, 202.5, 321.2, 544.3]
print(f"\n{'gamma_j':>10} {'R_j':>13} {'eps_j':>10} {'headroom':>9}")
results = []
for tv in targets:
    j = min(range(K), key=lambda k: abs(float(gam[k]) - tv))
    g = gam[j]
    V = V_at(g)
    vis = visible_field(j)
    T, eps = tail_and_band(g)
    R = V - vis - T
    hr = float(eps / abs(R)) if R != 0 else float('inf')
    results.append((float(g), float(R), float(eps), hr))
    print(f"{mp.nstr(g, 8):>10} {float(R):>13.2e} {float(eps):>10.1e} "
          f"{'10^%.1f' % (mp.log10(hr)):>9}")

# certified thresholds at gamma ~ 146
eps146 = [r[2] for r in results if abs(r[0] - 146) < 1][0]
print(f"\nthresholds at gamma ~ 146 (eps = {eps146:.2e}):")
print(f"  existence: 4/d > 2 eps  out to  d = {2/eps146:.3g}")
for d in (1, 2, 5):
    smin = (eps146 * d ** 3 / 2) ** 0.5
    print(f"  sign-discrimination at d = {d}:  sigma_min = {smin:.3f}")
