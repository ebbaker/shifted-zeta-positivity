#!/usr/bin/env python3
"""The near-antiparallel, near-BPS corner of the generalized cusp in N=4 SYM.

Companion to N4SYM/notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md.
Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier
claude-opus-5-5 as reported by the runtime; reasoning effort not exposed).

Standard library only; prints one JSON object (or writes --output FILE).
Deterministic. No zeta function is evaluated except the constant zeta(3)
entering the two-loop cusp (a fixed number). Floating cases diagnose analytic
statements; they are not interval certificates.

Conventions: <W> ~ exp(-Gamma log(L/eps)); deflection phi, internal angle
theta; corner phi = pi - u, theta = pi - x u with u -> 0 (BPS at x = +-1).
Weak coupling: Gamma = sum_n (lambda/16 pi^2)^n V^(n)(phi, theta), planar,
V^(1), V^(2) as transcribed from Drukker-Forini arXiv:1105.5144 eqs (3.1),
(3.2) and validated here against three independent limits.
Strong coupling: planar classical string (Drukker-Gross-Ooguri ansatz),
Gamma = sqrt(lambda) gamma(phi, theta), parametrized by (zeta0, r1).

Groups
  W1-W5  weak coupling: small-angle Bremsstrahlung, near-BPS slope at every
         phi (CHMS), antiparallel two-loop logarithm, corner scaling
         Gamma -> (1 - x^2) Phi(lambda u) with Phi = (pi^2/2) B(2 lambda u/pi)
         through two loops;
  S1-S6  strong coupling: antiparallel-lines coefficient, small-angle B,
         exact BPS vanishing (on r1 = 1/zeta0^2), near-BPS slope versus
         CHMS at every phi, the corner scaling function
         Gamma = sqrt(lambda u) F(x) with parametric F, its value F(0) and
         its slope F'(1) = -(1/4) sqrt(2/pi) (the exact near-BPS value).
"""
from fractions import Fraction as Fr
import argparse
import json
import math

CASES = []
ZETA3 = 1.2020569031595942853997


def case(name, group, kind, value, threshold, comparison='<=', note=''):
    value = float(value)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, group=group, kind=kind, value=value,
                      threshold=threshold, comparison=comparison,
                      passed=bool(passed), note=note))


def gauss_legendre(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1.0)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        nodes.append(x)
        weights.append(2.0 / ((1.0 - x * x) * dp * dp))
    return nodes, weights


GL64 = gauss_legendre(64)


def quad(f, a, b, panels=8):
    nodes, weights = GL64
    h = (b - a) / panels
    total = 0.0
    for p in range(panels):
        lo = a + p * h
        for x, w in zip(nodes, weights):
            total += 0.5 * h * w * f(lo + 0.5 * h * (x + 1))
    return total


# ------------------------------------------------------------- Clausen functions
def bernoulli_even(nmax):
    """|B_2k| for k = 1..nmax from the standard recurrence (exact)."""
    B = [Fr(1)]
    for m in range(1, 2 * nmax + 1):
        B.append(-sum(math.comb(m + 1, k) * B[k] for k in range(m)) / (m + 1))
    return [abs(B[2 * k]) for k in range(1, nmax + 1)]


_B2K = bernoulli_even(30)
_C2 = [float(b) / (2 * k * (2 * k + 1) * math.factorial(2 * k)) for k, b in enumerate(_B2K, start=1)]


def cl2(x):
    """Clausen Cl_2(x) = sum sin(kx)/k^2 for 0 < x < 2 pi."""
    if x > math.pi:
        return -cl2(2 * math.pi - x)
    if x == 0:
        return 0.0
    s = x - x * math.log(x)
    for k, c in enumerate(_C2, start=1):
        s += c * x ** (2 * k + 1)
    return s


def cl3(x):
    """Cl_3(x) = sum cos(kx)/k^3 for 0 <= x <= 2 pi (d Cl_3/dx = -Cl_2)."""
    if x > math.pi:
        return cl3(2 * math.pi - x)
    if x == 0:
        return ZETA3
    s = ZETA3 - 0.75 * x * x + 0.5 * x * x * math.log(x)
    for k, c in enumerate(_C2, start=1):
        s -= c * x ** (2 * k + 2) / (2 * k + 2)
    return s


# ------------------------------------------------------------- weak coupling
def bracket(phi):
    """Li3(e^{2i phi}) - zeta3 - i phi (Li2(e^{2i phi}) + pi^2/6) + i phi^3/3 (real)."""
    return cl3(2 * phi) - ZETA3 + phi * cl2(2 * phi)


def cdiff(phi, th):
    """cos(theta) - cos(phi), written without cancellation."""
    return -2 * math.sin((th + phi) / 2) * math.sin((th - phi) / 2)


def V1(phi, th):
    return -2 * cdiff(phi, th) * phi / math.sin(phi)


def V2(phi, th):
    c = cdiff(phi, th)
    lad = -4 * c * c / math.sin(phi) ** 2 * bracket(phi)
    inter = (4.0 / 3.0) * c / math.sin(phi) * (math.pi - phi) * (math.pi + phi) * phi
    return lad + inter, lad, inter


def planar_B(lam):
    """B = sqrt(lam) I2(sqrt lam)/(4 pi^2 I1(sqrt lam)) by power series."""
    x = math.sqrt(lam)

    def I(nu):
        s, term, k = 0.0, (x / 2) ** nu / math.factorial(nu), 0
        while True:
            s += term
            k += 1
            term *= (x / 2) ** 2 / (k * (k + nu))
            if abs(term) < 1e-18 * abs(s):
                return s + term
    return x * I(2) / (4 * math.pi ** 2 * I(1))


def weak_checks():
    # Clausen implementation against direct sums
    worst = 0.0
    for x in (0.3, 1.7, 3.0, 5.1):
        d2 = sum(math.sin(k * x) / k ** 2 for k in range(1, 400001))
        d3 = sum(math.cos(k * x) / k ** 3 for k in range(1, 20001))
        worst = max(worst, abs(cl2(x) - d2), abs(cl3(x) - d3))
    case('W0 Clausen Cl2, Cl3 series agree with direct sums', 'W0', 'floating', worst, 1e-5)
    # W1 small angle: V2 -> (2 pi^2/3)(phi^2 - theta^2); planar B = lam/16pi^2 - lam^2/384pi^2
    lam = 1e-3
    b2 = (planar_B(lam) - lam / (16 * math.pi ** 2)) / lam ** 2
    case('W1 planar B: second-order coefficient -1/(384 pi^2)', 'W1', 'floating',
         abs(b2 * 384 * math.pi ** 2 + 1), 1e-3)
    for phi, th in ((0.02, 0.01), (0.01, 0.0)):
        v, _, _ = V2(phi, th)
        case(f'W1 small angle: V2/(phi^2 - theta^2) -> 2 pi^2/3 = -B^(2) at phi={phi}, theta={th}', 'W1',
             'floating', abs(v / (phi ** 2 - th ** 2) / (2 * math.pi ** 2 / 3) - 1), 1e-3)
    # W2 near-BPS slope at every phi: dV2/dtheta at theta = phi = -(4/3)(pi^2 - phi^2) phi (CHMS)
    for phi in (0.5, 1.5, 2.5, 3.0):
        h = 1e-5
        d = (V2(phi, phi + h)[0] - V2(phi, phi - h)[0]) / (2 * h)
        pred = -(4.0 / 3.0) * (math.pi ** 2 - phi ** 2) * phi
        case(f'W2 near-BPS slope of V2 equals CHMS 2 phi B^(2)(lambda~)/(1-phi^2/pi^2) at phi={phi}', 'W2',
             'floating', abs(d / pred - 1), 1e-6)
    # W3 antiparallel limit (theta = 0): u V_lad(pi - u, 0) -> -32 pi (log 2u - 1): lambda^2/(8 pi^3) log term
    for u in (1e-2, 1e-3):
        _, lad, _ = V2(math.pi - u, 0.0)
        case(f'W3 antiparallel two-loop log: u V_lad/(-32 pi) - (log 2u - 1) -> 0 at u={u}', 'W3', 'floating',
             abs(u * lad / (-32 * math.pi) - (math.log(2 * u) - 1)), 20 * u)
    # W4 corner: V1 -> pi (1 - x^2) u; V2 -> -(4 pi^2/3)(1 - x^2) u^2 + O(u^3 log u)
    for u in (1e-2, 1e-3):
        for x in (0.0, 0.5, 2.0):
            phi, th = math.pi - u, math.pi - x * u
            v1 = V1(phi, th)
            v2, lad, inter = V2(phi, th)
            case(f'W4 corner one loop: V1/((1-x^2) pi u) -> 1 at u={u}, x={x}', 'W4', 'floating',
                 abs(v1 / ((1 - x * x) * math.pi * u) - 1), 2 * u)
            case(f'W4 corner two loops: V2/((1-x^2) u^2) -> -4 pi^2/3 at u={u}, x={x}', 'W4', 'floating',
                 abs(v2 / ((1 - x * x) * u * u) / (-4 * math.pi ** 2 / 3) - 1), 10 * u * (1 + abs(math.log(u))) * (1 + x * x))
    # W5 corner function through two loops equals (pi^2/2) B(2 g/pi), g = lambda u
    lam, u = 0.3, 1e-4
    g = lam * u
    gam = (lam / (16 * math.pi ** 2)) * V1(math.pi - u, math.pi) \
        + (lam / (16 * math.pi ** 2)) ** 2 * V2(math.pi - u, math.pi)[0]
    phi_chms = (math.pi ** 2 / 2) * (2 * g / math.pi / (16 * math.pi ** 2) - (2 * g / math.pi) ** 2 / (384 * math.pi ** 2))
    case('W5 corner at theta = pi: two-loop Gamma equals (pi^2/2) B(2 lambda u/pi) through O(g^2)', 'W5',
         'floating', abs(gam / phi_chms - 1), 5 * u + 1e-9)
    # H = lim Gamma/u = lambda/(16 pi) at each order
    case('W5 H = lim Gamma(pi-u, pi)/u: one-loop coefficient pi (units lambda/16pi^2) and no two-loop term', 'W5',
         'floating', abs(V1(math.pi - 1e-6, math.pi) / 1e-6 - math.pi) + abs(V2(math.pi - 1e-6, math.pi)[0] / 1e-6),
         1e-4)


# ------------------------------------------------------------- strong coupling
def s_omega(z0, r1):
    return 2 * z0 * quad(lambda t: math.sin(t) ** 2 / (math.sqrt(1 + z0 * z0 * math.sin(t) ** 2)
                                                       * math.sqrt(math.sin(t) ** 2 + r1)), 0, math.pi / 2)


def s_theta(z0, r1):
    q = max(r1 - 1 + z0 * z0 * r1, 0.0)
    return 2 * math.sqrt(q) * quad(lambda t: 1 / (math.sqrt(1 + z0 * z0 * math.sin(t) ** 2)
                                                  * math.sqrt(math.sin(t) ** 2 + r1)), 0, math.pi / 2)


def s_gamma(z0, r1):
    """Gamma/sqrt(lambda) for the planar classical cusp string."""
    def f(t):
        st = math.sin(t)
        if t < 1e-4:
            return z0 * z0 / 2 - 1 / (2 * r1) + 0.5
        h = math.sqrt(r1) * math.sqrt(1 + z0 * z0 * st * st) / math.sqrt(st * st + r1)
        return (h - math.cos(t)) / (st * st)
    return (quad(f, 0, math.pi / 2) - 1) / (math.pi * z0)


def F_par(w):
    return 0.25 * (math.sqrt(w) - 4 / (math.pi ** 2 * w ** 1.5))


def x_par(w):
    return 3 / (math.pi * w) - math.pi * w / 4


def strong_checks():
    # S1 antiparallel lines: Gamma * Omega -> -4 pi^2/Gamma(1/4)^4 at theta = 0
    target = -4 * math.pi ** 2 / math.gamma(0.25) ** 4
    for z0 in (1e-2, 1e-3):
        r1 = 1 / (1 + z0 * z0)
        case(f'S1 antiparallel lines: Gamma Omega/sqrt(lambda) -> -4 pi^2/Gamma(1/4)^4 at zeta0={z0}', 'S1',
             'floating', abs(s_gamma(z0, r1) * s_omega(z0, r1) / target - 1), 20 * z0 * z0 + 1e-9)
    # S2 small angle: Gamma/phi^2 -> -1/(4 pi^2), i.e. B = sqrt(lambda)/(4 pi^2)
    for z0 in (100.0, 300.0):
        r1 = 1 / (1 + z0 * z0)
        phi = math.pi - s_omega(z0, r1)
        case(f'S2 small angle: Gamma/phi^2 -> -1/(4 pi^2) at phi={phi:.4g}', 'S2', 'floating',
             abs(s_gamma(z0, r1) / phi ** 2 * (-4 * math.pi ** 2) - 1), 0.2 * phi ** 2 + 1e-6)
    # S3 BPS curve r1 = 1/zeta0^2: theta + Omega = pi and Gamma = 0
    for z0 in (0.05, 0.3, 1.0, 3.0):
        r1 = 1 / z0 ** 2
        case(f'S3 BPS: theta + Omega = pi on r1 = 1/zeta0^2 at zeta0={z0}', 'S3', 'floating',
             abs(s_theta(z0, r1) + s_omega(z0, r1) - math.pi), 1e-12)
        case(f'S3 BPS: Gamma vanishes on r1 = 1/zeta0^2 at zeta0={z0}', 'S3', 'floating',
             abs(s_gamma(z0, r1)), 1e-10)
    # S4 near-BPS slope at fixed Omega versus CHMS with B -> sqrt(lambda~)/(4 pi^2)
    for z0 in (0.1, 0.5, 1.0, 2.0, 5.0):
        r1, h = 1 / z0 ** 2, 1e-5
        Oz = (s_omega(z0 * (1 + h), r1) - s_omega(z0 * (1 - h), r1)) / (2 * h * z0)
        Or = (s_omega(z0, r1 * (1 + h)) - s_omega(z0, r1 * (1 - h))) / (2 * h * r1)
        Tz = (s_theta(z0 * (1 + h), r1) - s_theta(z0 * (1 - h), r1)) / (2 * h * z0)
        Tr = (s_theta(z0, r1 * (1 + h)) - s_theta(z0, r1 * (1 - h))) / (2 * h * r1)
        Gz = (s_gamma(z0 * (1 + h), r1) - s_gamma(z0 * (1 - h), r1)) / (2 * h * z0)
        Gr = (s_gamma(z0, r1 * (1 + h)) - s_gamma(z0, r1 * (1 - h))) / (2 * h * r1)
        slope = (Gz * Or - Gr * Oz) / (Tz * Or - Tr * Oz)
        phi = math.pi - s_omega(z0, r1)
        pred = phi / (2 * math.pi ** 2 * math.sqrt(1 - phi ** 2 / math.pi ** 2))
        case(f'S4 near-BPS slope dGamma/dtheta equals CHMS strong-coupling value at phi={phi:.4g}', 'S4',
             'floating', abs(slope / pred - 1), 1e-5)
    # S5 corner scaling: exact integrals approach sqrt(Omega) F(x), x(w) parametric
    for w in (2 * math.sqrt(3) / math.pi, 0.5, 2.0):
        errs = []
        for Om_t in (1e-3, 1e-4):
            A = math.sqrt(w)
            Bc = 2 / (math.pi * A)
            z0, r1 = A * math.sqrt(Om_t), 1 / (Bc ** 2 * Om_t)
            Om, th, G = s_omega(z0, r1), s_theta(z0, r1), s_gamma(z0, r1)
            x = (math.pi - th) / Om
            errs.append((abs(x - x_par(w)), abs(G / math.sqrt(Om) - F_par(w))))
        case(f'S5 corner: x -> x(w) with O(Omega) error at w={w:.4g}', 'S5', 'floating',
             errs[1][0], 2e-3 * (1 + abs(x_par(w))))
        case(f'S5 corner: Gamma/sqrt(lambda Omega) -> F(w) with O(Omega) error at w={w:.4g}', 'S5', 'floating',
             errs[1][1], 1e-4)
        case(f'S5 corner: the x error falls about tenfold with Omega at w={w:.4g}', 'S5', 'floating',
             errs[1][0] / errs[0][0], 0.2,
             note=f'Gamma errors {errs[0][1]:.2e} -> {errs[1][1]:.2e}')
    # S6 corner function: BPS zero, F(0), F'(1) equals the exact near-BPS slope, and x -> -x asymmetry
    wb = 2 / math.pi
    case('S6 F vanishes at x = 1 (w = 2/pi)', 'S6', 'floating', abs(F_par(wb)) + abs(x_par(wb) - 1), 1e-14)
    w0 = 2 * math.sqrt(3) / math.pi
    case('S6 F(0) = 1/(sqrt(2 pi) 3^(3/4)) at w = 2 sqrt3/pi', 'S6', 'floating',
         abs(F_par(w0) - 1 / (math.sqrt(2 * math.pi) * 3 ** 0.75)) + abs(x_par(w0)), 1e-14)
    h = 1e-6
    dF = (F_par(wb + h) - F_par(wb - h)) / (x_par(wb + h) - x_par(wb - h))
    case('S6 F\'(1) = -(1/4) sqrt(2/pi): classical corner reproduces the exact near-BPS slope', 'S6', 'floating',
         abs(dF / (-0.25 * math.sqrt(2 / math.pi)) - 1), 1e-8)
    dF0 = (F_par(w0 + h) - F_par(w0 - h)) / (x_par(w0 + h) - x_par(w0 - h))
    case('S6 F\'(0) nonzero: minimal branch F(|x|) has a kink at theta = pi (antipodal S^5 moduli)', 'S6',
         'floating', abs(dF0), 0.1, '>=', note=f"F'(0) = {dF0:.6f}")
    # S7 byproduct: antiparallel lines near theta = pi at strong coupling,
    # Gamma Omega -> -v^(3/2)/(3^(3/2) sqrt(pi)) (non-analytic; weak coupling ~ v^2)
    for r1 in (100.0, 1000.0):
        z0 = 1e-5
        Om, th, G = s_omega(z0, r1), s_theta(z0, r1), s_gamma(z0, r1)
        v = math.pi - th
        pred = -v ** 1.5 / (3 ** 1.5 * math.sqrt(math.pi))
        case(f'S7 strong-coupling antiparallel lines near theta = pi: Gamma Omega -> -v^1.5/(3^1.5 sqrt pi) at v={v:.3g}',
             'S7', 'floating', abs(G * Om / pred - 1), 3.0 / r1 + 1e-6)
    return dict(F0=F_par(w0), Fprime1=dF, Fprime0=dF0)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output')
    args = parser.parse_args()
    weak_checks()
    derived = strong_checks()
    data = dict(
        program='check_near_bps_corner.py',
        prepared_by='Claude Opus 5.5 (Anthropic), model identifier claude-opus-5-5 as reported by the runtime; effort not exposed',
        prepared_for='Edward Baker',
        date='2026-09-24',
        parameters=dict(weak='planar two-loop generalized cusp, Drukker-Forini (3.1)-(3.2) transcription',
                        strong='planar classical string, Gauss-Legendre 8 x 64 on [0, pi/2]'),
        derived=derived,
        scope=('Diagnostics of the near-antiparallel, near-BPS corner of the generalized cusp at weak '
               'and strong coupling, and of the exact near-BPS slope; not interval arithmetic.'),
        case_count=len(CASES),
        all_pass=all(c['passed'] for c in CASES),
        cases=CASES)
    text = json.dumps(data, indent=1, sort_keys=True)
    if args.output:
        with open(args.output, 'w') as fh:
            fh.write(text + '\n')
    print(text)


if __name__ == '__main__':
    main()
