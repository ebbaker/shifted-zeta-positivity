#!/usr/bin/env python3
"""Finite checks for the reflection-network note; standard library only.

Supports notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md.
Prints deterministic JSON and writes nothing. Zeta is evaluated nowhere.
Nothing here is a positivity certificate for the Weil form, a proof of
reflection positivity of the defect theory, or a count of physical
supercharges; the Clifford identities are finite matrix identities under the
displayed bulk BPS equation of the endpoint-transport note.
Model: Claude Fable 5.1 (Anthropic), claude-fable-5-1.
"""
import cmath
from fractions import Fraction as F
import json
import math

GROUPS = []


def group(name, checks, method, tolerance=None):
    passed = all(checks)
    row = {"name": name, "cases": len(checks), "method": method, "pass": passed}
    if tolerance is not None:
        row["tolerance"] = tolerance
    GROUPS.append(row)
    if not passed:
        raise AssertionError(name + ': failed cases ' + str(
            [i for i, ok in enumerate(checks) if not ok]))


def simpson(fn, end, n):
    step = end / n
    terms = [complex(fn(0.)), complex(fn(end))]
    terms.extend((4 if k % 2 else 2) * fn(k * step) for k in range(1, n))
    return step / 3 * complex(math.fsum(x.real for x in terms),
                              math.fsum(x.imag for x in terms))


# --- 2x2 complex matrix helpers (Clifford algebra of the (1,3,I) directions).
def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def norm(a):
    return max(abs(x) for row in a for x in row)


EYE = [[1, 0], [0, 1]]
G1 = [[0, 1], [1, 0]]
G3 = [[0, -1j], [1j, 0]]
GI = [[1, 0], [0, -1]]
J = scale(1j, mul(GI, G3))          # J = i Gamma_I Gamma_3, J^2 = 1


def bps_residual(c, radius, side, direction, scalar_sign, eps_c, eps_s, co, si):
    """Residual of [i xdot.Gamma + scalar_sign |xdot| Gamma_I][eps_s + x.Gamma eps_c].

    side=+1: upper half-plane semicircle, side=-1: lower.  direction=+1 traverses
    from the right endpoint c+R to the left endpoint c-R (the convention of the
    endpoint-transport note); direction=-1 the reverse.  (co, si) = (cos, sin) of
    the parameter angle."""
    x1, x3 = c + radius * co, side * radius * si
    t1, t3 = -radius * si, side * radius * co
    if direction < 0:
        t1, t3 = -t1, -t3
    tangent = add(scale(t1, G1), scale(t3, G3))
    point = add(scale(x1, G1), scale(x3, G3))
    left = add(scale(1j, tangent), scale(scalar_sign * radius, GI))
    right = add(eps_s, mul(point, eps_c))
    return norm(mul(left, right))


def bps_solution(c, radius, side, direction, scalar_sign, eps_c):
    """eps_s = -c Gamma_1 eps_c - sigma R J Gamma_1 eps_c with sigma the sign
    read off in the note: sigma = side * direction * scalar_sign."""
    sigma = side * direction * scalar_sign
    return scale(-1, add(scale(c, mul(G1, eps_c)),
                         scale(sigma * radius, mul(J, mul(G1, eps_c)))))


ANGLES = ((1., 0.), (0., 1.), (-1., 0.), (.6, .8), (-.6, .8), (.28, .96))


def main():
    # A. Tower identities: n_gamma = G_o + G_-, G_o alternating, exact rationals.
    checks = []
    for k in range(1, 20):
        t = F(k, 20)                       # t = exp(-u/2)
        g_s, g_o = t / (1 - t * t), t / (1 + t * t)
        n_gamma = t / (1 - t ** 4)
        g_minus = t ** 3 / (1 - t ** 4)
        checks += [n_gamma == (g_s + g_o) / 2,
                   n_gamma == g_o + g_minus,
                   g_s == n_gamma + g_minus]
        # alternating expansion of G_o truncated at 2M terms, remainder bound
        M = 40
        partial = sum((-1) ** n * t ** (2 * n + 1) for n in range(2 * M))
        checks.append(abs(g_o - partial) <= t ** (4 * M + 1))
    group('A. even tower = alternating tower + odd tower', checks,
          'exact rational identities in t = exp(-u/2)')

    # B. Fourier transforms: G_o -> pi / cosh(pi tau) (positive); the even tower
    #    and the odd tower have positive Lorentzian-sum transforms.
    checks = []
    for tau in (.2, .7, 1.5, 3.):
        val = simpson(lambda u: math.cos(tau * u) / math.cosh(u / 2), 60., 24000)
        checks.append(abs(val.real - math.pi / math.cosh(math.pi * tau)) < 1e-9)
        # The odd tower G_- ~ 1/(2u) on the diagonal, so only its difference
        # energy converges: 2 int (1-cos tau u) G_-(u) du = sum 2 tau^2/(a(a^2+tau^2)).
        count = 20000
        odd = 2 * math.fsum(tau * tau / ((2 * n + 1.5) * ((2 * n + 1.5) ** 2 + tau * tau))
                            for n in range(count))
        direct = 2 * simpson(lambda u: (1 - math.cos(tau * u)) * math.exp(-1.5 * u)
                             / (-math.expm1(-2 * u)) if u > 0 else 0., 60., 24000)
        a = 2 * count + 1.5
        checks.append(direct.real > 0 and odd > 0)
        checks.append(abs(direct.real - odd) < 2 * tau * tau / a ** 2 + 1e-8)
    group('B. transforms: G_o regular with positive transform; odd tower positive as a difference energy',
          checks, 'quadrature versus closed form and Lorentzian sum with tail bound', 1e-8)

    # C. Orientation table for the bulk BPS solution on upper and lower
    #    semicircles, both traversal directions, both scalar signs.
    checks = [mul(J, J) == EYE, mul(J, G1) == mul(G1, J)]
    eps_c_list = ([[1, 0], [0, 0]], [[0, 0], [1, 0]], [[1, 0], [1j, 0]])  # spinors as first columns
    for c, radius in ((0.5, 0.5), (1.5, 1.5), (-1., 1.), (2., 1.), (-1.5, 0.5)):
        for side in (1, -1):
            for direction in (1, -1):
                for scalar_sign in (1, -1):
                    for eps_c in eps_c_list:
                        eps_s = bps_solution(c, radius, side, direction, scalar_sign, eps_c)
                        for co, si in ANGLES:
                            checks.append(bps_residual(c, radius, side, direction,
                                                       scalar_sign, eps_c, eps_s,
                                                       co, si) < 1e-12)
    group('C. bulk BPS solution on upper and lower semicircles, both orientations',
          checks, 'finite Clifford identities; sigma = side*direction*scalar_sign', 1e-12)

    # D. Common supercharge for every upper semicircle ending at the origin,
    #    traversed into the origin: [0,r] right-to-left and [-r,0] left-to-right.
    #    Solution: eps_s = 0, J eps_c = -eps_c.
    minus = scale(.5, add(EYE, scale(-1, J)))      # projector onto J = -1
    plus = scale(.5, add(EYE, J))
    checks = []
    for r in (0.5, 1., 2., 3.5, 7.):
        for eps_c in eps_c_list:
            eta = mul(minus, eps_c)
            zero = [[0, 0], [0, 0]]
            for co, si in ANGLES:
                # [0,r], upper, traversed r -> 0 (right to left)
                checks.append(bps_residual(r / 2, r / 2, 1, 1, 1, eta, zero, co, si) < 1e-12)
                # [-r,0], upper, traversed -r -> 0 (left to right)
                checks.append(bps_residual(-r / 2, r / 2, 1, -1, 1, eta, zero, co, si) < 1e-12)
                # lower [0,r], traversed 0 -> r (left to right), same scalar sign
                checks.append(bps_residual(r / 2, r / 2, -1, -1, 1, eta, zero, co, si) < 1e-12)
                # lower [-r,0], traversed 0 -> -r (right to left), same scalar sign
                checks.append(bps_residual(-r / 2, r / 2, -1, 1, 1, eta, zero, co, si) < 1e-12)
    # and the J = +1 eigenspace does not work with eps_s = 0 unless trivial
    for r in (1., 2.):
        for eps_c in eps_c_list:
            eta = mul(plus, eps_c)
            if norm(eta) > 0:
                bad = max(bps_residual(r / 2, r / 2, 1, 1, 1, eta, [[0, 0], [0, 0]], co, si)
                          for co, si in ANGLES)
                checks.append(bad > 1e-3)
    group('D. one special supercharge for all circles through the origin', checks,
          'eps_s = 0, J eps_c = -eps_c annihilates every arc tangent to the x3 axis at 0 traversed downward', 1e-12)

    # E. The two reflection networks.  Theta_3 (through the defect): both halves
    #    of every pairing path share the supercharge of D when the scalar
    #    coupling is Theta_3-even; Theta_1 (within the defect) never does.
    checks = []
    for r1, r2 in ((3., 1.), (5., 2.), (7., 3.), (1., 1.)):
        # Theta_3 network with even coupling: upper [0,r2] r2->0, lower [0,r1] 0->r1
        # Theta_3 network with odd coupling flips scalar_sign on the lower half:
        # then the constant coefficients are -(r1/2)(1-J) and -(r2/2)(1+J);
        # a common eps_c needs (r1-r2)^2 = (r1+r2)^2.
        a = add(scale(r1 / 2, add(EYE, scale(-1, J))), scale(-r2 / 2, add(EYE, J)))
        b = add(scale(r1 / 2, add(EYE, scale(-1, J))), scale(r2 / 2, add(EYE, J)))
        det_a = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        det_b = b[0][0] * b[1][1] - b[0][1] * b[1][0]
        # eigenvalues on J = +1 and J = -1: a has (-r2, r1), b has (r2, r1)
        checks.append(abs(det_a + r1 * r2) < 1e-12)
        checks.append(abs(det_b - r1 * r2) < 1e-12)
        checks.append(abs(det_a) > 1e-9)          # odd coupling: no common solution
        checks.append(abs(det_b) > 1e-9)          # Theta_1 network: no common solution
        # Theta_3 with even coupling: coefficient matrix (r1-r2)(1+J)/2 has the
        # whole J = -1 eigenspace as kernel
        m = scale((r1 - r2) / 2, add(EYE, J))
        checks.append(norm(mul(m, minus)) < 1e-12)
    group('E. through-the-defect network shares the supercharge; within-defect network does not',
          checks, 'determinants of the two-circle constant coefficients', 1e-12)

    # The pi-cusp coefficient of the within-defect network is left as a hand
    # computation in the note; a crude fixed-grid quadrature of the cusp
    # exchange is not deterministic enough to register.

    print(json.dumps({"schema": 1, "date": "2026-09-18",
                      "model": "Claude Fable 5.1 (Anthropic), claude-fable-5-1",
                      "groups": GROUPS,
                      "total_checks": sum(g['cases'] for g in GROUPS),
                      "pass": all(g['pass'] for g in GROUPS),
                      "scope": "Finite identity checks for the reflection-network note; no reflection-positivity proof, no physical supercharge count, no positivity certificate."},
                     indent=2))


if __name__ == '__main__':
    main()
