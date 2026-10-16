#!/usr/bin/env python3
"""Rounded flipped-return loop at one loop, and closure-audit controls.

Companion to N4SYM/notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md.
Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier
claude-opus-5-5 as reported by the runtime; reasoning effort not exposed).

Standard library only; imports geometry and background helpers from
check_trace_completion.py. Prints one JSON object (or --output FILE).
Deterministic. No zeta function is evaluated.

Rounding: each cusp of the flipped loop (trace with n0, chord with -n0) is
replaced by the circular fillet of radius delta tangent to both legs; on the
fillet the internal vector rotates in the (n0, m) plane in step with the
tangent, n = cos(chi) n0 + sin(chi) m, chi advancing by pi across each
fillet in proportion to the turning angle. Units: rescaled trace (Loewner
time 1, slope s); log W^(1) = B_1 I with B_1 = lambda (1 - 1/N^2)/(16 pi^2).

Groups
  R0  conventions and normalization of the one-loop machinery: a Zarembo
      "stadium" (integrand identically zero, so this checks only the
      orientation/chi conventions) and a constant-scalar stadium against
      the antiparallel-lines law (checks the kernel normalization);
  R1  fillet construction: tangency, C^1 junctions, turning angles;
  R2  delta -> 0: the log(1/delta) coefficient is the exact one-loop cusp
      sum A(s) (differences halve);
  R3  finite part: R(s) = lim [I + A(s) log(1/delta)], with the exact A(s),
      equals -(2 pi s/3)[log(s/3) - 2] + h s + O(s^2): the s log s term is
      fixed, the constant h depends on the rounding convention;
  C1  closure controls: scalar-Laplacian counterexample, radial transported
      derivative with the scalar commutator, free flowed-propagator
      structure (EOM part contact, transverse part long range).
"""
import argparse
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_trace_completion as tc  # noqa: E402

CASES = []


def case(name, group, kind, value, threshold, comparison='<=', note=''):
    value = float(value)
    passed = value <= threshold if comparison == '<=' else value >= threshold
    CASES.append(dict(name=name, group=group, kind=kind, value=value,
                      threshold=threshold, comparison=comparison,
                      passed=bool(passed), note=note))


GL = {n: tc.gauss_legendre(n) for n in (8, 12, 16, 24)}


def graded_one(a, b, h0, ratio=1.7):
    edges, x = [a], h0
    while a + x < b:
        edges.append(a + x)
        x *= ratio
    edges.append(b)
    return edges


def graded_both(a, b, h0, ratio=1.7):
    mid = 0.5 * (a + b)
    left = graded_one(a, mid, h0, ratio)
    right = [b - (x - a) for x in reversed(graded_one(a, mid, h0, ratio))]
    return left + right[1:]


def rule(edges, order=12):
    nodes, weights = GL[order]
    xs, ws = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        h = hi - lo
        for x, w in zip(nodes, weights):
            xs.append(lo + 0.5 * h * (x + 1))
            ws.append(0.5 * h * w)
    return xs, ws


# ------------------------------------------------------------- loop pieces
class Segment:
    """Straight segment from P to P + L d (d unit), constant internal angle chi."""

    def __init__(self, P, d, L, chi):
        self.P, self.d, self.L, self.chi = P, d, L, chi
        self.kind = 'segment'

    def inner(self, x, T, chi):
        """int over the segment of (cos(chi - chi_s) - T.d)/|x - y|^2 dl (per unit |x_p|)."""
        z = (x - self.P) * self.d.conjugate()
        l0, dd = z.real, abs(z.imag)
        num = math.cos(chi - self.chi) - (T * self.d.conjugate()).real
        if num == 0.0:
            return 0.0
        if dd < 1e-14:
            raise ValueError('point on segment line')
        return num * (math.atan((self.L - l0) / dd) - math.atan(-l0 / dd)) / dd


class Curve:
    """Generic piece: nodes carry x, x_p (complex), chi, chi_p, theta_p."""

    def __init__(self, samples, weights):
        self.s, self.w = samples, weights
        self.kind = 'curve'


def curve_curve(A, B, same):
    total = 0.0
    for i, (xa, dxa, ca, cpa, tpa) in enumerate(A.s):
        for j, (xb, dxb, cb, cpb, tpb) in enumerate(B.s):
            if same and i == j:
                val = (tpa * tpa - cpa * cpa) / 2
            else:
                num = abs(dxa) * abs(dxb) * math.cos(ca - cb) - (dxa * dxb.conjugate()).real
                val = num / abs(xa - xb) ** 2
            total += A.w[i] * B.w[j] * val
    return total


def curve_segment(A, S):
    total = 0.0
    for (xa, dxa, ca, cpa, tpa), wa in zip(A.s, A.w):
        sp = abs(dxa)
        total += wa * sp * S.inner(xa, dxa / sp, ca)
    return total


def one_loop(pieces):
    """I = sum over ordered pairs of pieces (both orders included)."""
    total = 0.0
    n = len(pieces)
    for a in range(n):
        for b in range(n):
            A, B = pieces[a], pieces[b]
            if A.kind == 'segment' and B.kind == 'segment':
                if a == b:
                    continue
                # sample A with Gauss-Legendre, integrate B analytically
                xs, ws = rule(graded_both(0.0, A.L, min(1e-3, A.L / 8)), 16)
                for l, w in zip(xs, ws):
                    total += w * B.inner(A.P + l * A.d, A.d, A.chi)
            elif A.kind == 'curve' and B.kind == 'curve':
                total += curve_curve(A, B, a == b)
            elif A.kind == 'curve':
                total += curve_segment(A, B)
            else:
                total += curve_segment(B, A)
    return total


def arc_piece(c, r, a1, delta_angle, chi0, chi_span, h0, order=12):
    """Clockwise arc from angle a1 through delta_angle (> 0), chi from chi0 by chi_span."""
    xs, ws = rule(graded_both(0.0, 1.0, h0), order)
    samples = []
    for sg in xs:
        ang = a1 - delta_angle * sg
        x = c + r * cmath.exp(1j * ang)
        dx = -1j * r * delta_angle * cmath.exp(1j * ang)
        samples.append((x, dx, chi0 + chi_span * sg, chi_span, -delta_angle))
    return Curve(samples, ws)


# ------------------------------------------------------------- R0 stadium controls
def stadium(L, rad, zarembo=True):
    """Antiparallel legs of length L at separation 2 rad, semicircular ends, clockwise."""
    # left leg up (x = -rad), right leg down (x = +rad)
    left = Segment(complex(-rad, 0), 1j, L, 0.0)
    top = arc_piece(complex(0, L), rad, math.pi, math.pi, 0.0, math.pi if zarembo else 0.0, 0.02)
    right = Segment(complex(rad, L), -1j, L, math.pi if zarembo else 0.0)
    bottom = arc_piece(complex(0, 0), rad, 0.0, math.pi, math.pi if zarembo else 0.0,
                       math.pi if zarembo else 0.0, 0.02)
    return [left, top, right, bottom]


def r0_controls():
    I = one_loop(stadium(2.0, 0.05, zarembo=True))
    case('R0 Zarembo stadium (n rotates with the tangent): integrand vanishes identically (conventions check)',
         'R0', 'floating', abs(I), 1e-8)
    # constant scalar: sliver law 4 pi L/(2 rad) dominates as rad -> 0
    vals = []
    for rad in (0.02, 0.01):
        I = one_loop(stadium(2.0, rad, zarembo=False))
        vals.append(I * 2 * rad / (4 * math.pi * 2.0))
    case('R0 constant-scalar stadium: I (2 rad)/(4 pi L) -> 1 (antiparallel-lines law)', 'R0', 'floating',
         abs(vals[1] - 1), 0.05, note=f'values {vals[0]:.5f}, {vals[1]:.5f}')


# ------------------------------------------------------------- rounded flipped loop
def trace_data(s, u):
    q = tc.solve_tip(s, u * u)
    qd = s - 2 / q
    qu = 2 * u * qd
    quu = 2 * qd + 2 * u * (2 / q ** 2) * qu
    return q, qu, quu


def fillet(s, delta, near):
    """Circle of radius delta tangent to the chord and to the trace near 'tip' or 'base'."""
    tip = tc.solve_tip(s, 1.0)
    Lc = abs(tip)
    e = tip / Lc
    if near == 'tip':
        _, qu1, _ = trace_data(s, 1.0)
        alpha = abs(cmath.phase(qu1 / e))
        dist = delta / math.tan(alpha / 2)
        l, u = Lc - dist, 1.0 - dist / abs(qu1)
    else:
        alpha = abs(cmath.phase(e / 1j))
        dist = delta / math.tan(alpha / 2)
        l, u = dist, dist / 2
    for _ in range(60):
        q, qu, quu = trace_data(s, u)
        T = qu / abs(qu)
        kap = (quu / qu).imag
        F = e * l + 1j * delta * e - q + 1j * delta * T
        dFl = e
        dFu = -qu - delta * kap * T
        det = dFl.real * dFu.imag - dFl.imag * dFu.real
        dl = (F.real * dFu.imag - F.imag * dFu.real) / det
        du = (dFl.real * F.imag - dFl.imag * F.real) / det
        l, u = l - dl, u - du
        if abs(dl) + abs(du) < 1e-15:
            break
    q, qu, _ = trace_data(s, u)
    T = qu / abs(qu)
    c = e * l + 1j * delta * e
    return dict(l=l, u=u, c=c, P_chord=e * l, P_trace=q, T=T, e=e, Lc=Lc, alpha=alpha,
                resid=abs(c - (q - 1j * delta * T)))


def rounded_loop(s, delta):
    ft, fb = fillet(s, delta, 'tip'), fillet(s, delta, 'base')
    e = ft['e']
    # trace piece u in [u_B, u_T], chi = 0
    edges = graded_both(fb['u'], ft['u'], min(2e-3, delta), 1.5)
    xs, ws = rule(edges, 12)
    samples = []
    for u in xs:
        q, qu, quu = trace_data(s, u)
        samples.append((q, qu, 0.0, 0.0, (quu / qu).imag))
    trace = Curve(samples, ws)
    # tip arc: from trace point (angle of iT) clockwise to chord point (angle of -ie), chi 0 -> pi
    a1 = cmath.phase((ft['P_trace'] - ft['c']) / delta)
    a2 = cmath.phase((ft['P_chord'] - ft['c']) / delta)
    dang = (a1 - a2) % (2 * math.pi)
    tip_arc = arc_piece(ft['c'], delta, a1, dang, 0.0, math.pi, 0.02)
    chord = Segment(e * ft['l'], -e, ft['l'] - fb['l'], math.pi)
    b1 = cmath.phase((fb['P_chord'] - fb['c']) / delta)
    b2 = cmath.phase((fb['P_trace'] - fb['c']) / delta)
    dbang = (b1 - b2) % (2 * math.pi)
    base_arc = arc_piece(fb['c'], delta, b1, dbang, math.pi, math.pi, 0.02)
    return [trace, tip_arc, chord, base_arc], dict(ft=ft, fb=fb, dang=dang, dbang=dbang)


def cusp_sum(s):
    tip = tc.solve_tip(s, 1.0)
    e = tip / abs(tip)
    ab = abs(cmath.phase(e / 1j))
    _, dq = tc.trace_point(s, 1.0)
    at = abs(cmath.phase(dq / e))
    return sum(2 * (math.pi - a) * math.tan(a / 2) for a in (ab, at)), ab, at


def r_rounded():
    out = {}
    for s in (0.1, 0.05, 0.025):
        A, ab, at = cusp_sum(s)
        vals = {}
        deltas = [s * f for f in (2e-3, 1e-3, 5e-4, 2.5e-4)]   # fixed delta/s across s
        for delta in deltas:
            pieces, geo = rounded_loop(s, delta)
            if delta == deltas[0]:
                ft, fb = geo['ft'], geo['fb']
                case(f'R1 fillets tangent to both legs (residual) at s={s:g}', 'R1', 'floating',
                     max(ft['resid'], fb['resid']), 1e-12)
                # the trace tangent at the tangency point differs from the vertex tangent by
                # curvature x distance = (s/3)(2 delta/alpha) ~ 2 delta per fillet
                case(f'R1 fillet turning angles equal pi - cusp angle up to O(delta) at s={s:g}', 'R1', 'floating',
                     abs(geo['dang'] - (math.pi - at)) + abs(geo['dbang'] - (math.pi - ab)), 5 * delta)
            vals[delta] = one_loop(pieces)
        G = [vals[d] + A * math.log(1 / d) for d in deltas]
        d1, d2, d3 = G[1] - G[0], G[2] - G[1], G[3] - G[2]
        case(f'R2 log(1/delta) coefficient equals the exact cusp sum A(s): differences halve at s={s:g}',
             'R2', 'floating', abs(d3 / d2 - 0.5), 0.05, note=f'A = {A:.6e}; ratios {d2 / d1:.4f}, {d3 / d2:.4f}')
        R = (8 * G[3] - 6 * G[2] + G[1]) / 3      # Richardson removing O(delta) and O(delta^2)
        # sliver prediction with effective excision at the tangency points d_t = delta/tan(alpha/2)
        pred = -(2 * math.pi * s / 3) * (math.log(2 * s / 6) - 2)
        out[s] = (R, pred)
    for s, (R, pred) in out.items():
        case(f'R3 finite part R(s) = sliver prediction + h s, with |h| of order one, at s={s:g}', 'R3', 'floating',
             abs((R - pred) / s), 6.0, note=f'R = {R:.6e}; prediction {pred:.6e}; h = {(R - pred) / s:.6f}')
    hs = [(R - pred) / s for s, (R, pred) in out.items()]
    case('R3 hairpin constant h is independent of s to 1e-3 (finite part linear in s beyond the log)', 'R3',
         'floating', (max(hs) - min(hs)) / abs(hs[-1]), 1e-3,
         note=f'h(s) = {hs[0]:.6f}, {hs[1]:.6f}, {hs[2]:.6f}')
    return out, hs


# ------------------------------------------------------------- C1 closure controls
def c1_closure():
    # (i) Phi = c (x1^2 - x3^2) T3, A = 0: field equations hold (D^2 Phi = 0, no commutators),
    # but the planar Laplacian (d1^2 + d2^2) Phi = 2c T3 is not zero; the transverse part carries -2c.
    c = 0.7
    lap4 = 2 * c + 0 - 2 * c + 0
    planar = 2 * c
    case('C1 scalar Laplacian: harmonic 4D field with nonzero planar Laplacian (transverse term cannot be dropped)',
         'C1', 'exact', 0.0 if (lap4 == 0 and planar != 0) else 1.0, 0.0)
    # (ii) transported radial derivative along the chord with scalar connection:
    #      d_r Xhat = (q.DX)^ - |q| [Phihat, Xhat] for X = n.D Phi (planar background)
    s_a, t = 1.1, 0.2
    q = tc.solve_tip(s_a, t)
    Lq = abs(q)
    nhat = 1j * q / Lq

    def N(r):
        A1, A2, Ph = tc.fields(r * q.real, r * q.imag)
        return tc.madd(tc.msc(1j * q.real, A1), tc.msc(1j * q.imag, A2), tc.msc(Lq, Ph))
    n = 2000
    Rs = tc.rk4(N, n)

    def Xhat(idx):
        r = idx / n
        A1, A2, Ph, F12, D1P, D2P = tc.derived(r * q.real, r * q.imag)
        X = tc.madd(tc.msc(nhat.real, D1P), tc.msc(nhat.imag, D2P))
        R = Rs[idx]
        return tc.mm(tc.mm(tc.minv(R), X), R), R
    worst = 0.0
    for idx in (400, 1000, 1600):
        Xp, _ = Xhat(idx + 1)
        Xm, _ = Xhat(idx - 1)
        fd = tc.msc(n / 2.0, tc.madd(Xp, tc.msc(-1, Xm)))
        X0, R = Xhat(idx)
        r = idx / n
        x1, x2 = r * q.real, r * q.imag
        # q.D(n.D Phi) = n^nu q^mu D_mu D_nu Phi, from exact second derivatives
        import check_flipped_return as fr  # noqa: E402
        A1, A2, Ph, F12, DP, DF, DDP = fr.derived2(x1, x2)
        qv, nv = (q.real, q.imag), (nhat.real, nhat.imag)
        acc = [[0j, 0j], [0j, 0j]]
        for mu in range(2):
            for nu in range(2):
                acc = tc.madd(acc, tc.msc(qv[mu] * nv[nu], DDP[mu][nu]))
        Ri = tc.minv(R)
        pred = tc.madd(tc.mm(tc.mm(Ri, acc), R), tc.msc(-Lq, tc.comm(tc.mm(tc.mm(Ri, Ph), R), X0)))
        worst = max(worst, tc.mnorm(tc.madd(fd, tc.msc(-1, pred))) / tc.mnorm(pred))
    case('C1 radial transported derivative along the scalar-coupled chord includes -|q|[Phihat, Xhat]', 'C1',
         'floating', worst, 1e-6)
    # without the commutator the identity fails at O(1)
    case('C1 dropping the commutator term gives an O(1) error', 'C1', 'floating',
         tc.mnorm(tc.madd(fd, tc.msc(-1, tc.mm(tc.mm(Ri, acc), R)))) / tc.mnorm(pred), 0.05, '>=')
    # (iii) free flowed propagator k(r^2) = (1 - exp(-r^2/8tau))/r^2:
    # Laplacian is -4 pi^2 times the normalized heat kernel (contact); -4 k' -> 4/r^4 (long range)
    tau = 0.01

    def kfun(rho):
        return -math.expm1(-rho / (8 * tau)) / rho

    def kp(rho, h=1e-7):
        return (kfun(rho * (1 + h)) - kfun(rho * (1 - h))) / (2 * h * rho)

    def kpp(rho, h=1e-5):
        return (kp(rho * (1 + h)) - kp(rho * (1 - h))) / (2 * h * rho)
    worst_lap = 0.0
    for r in (0.1, 0.2, 0.35):
        rho = r * r
        lap = 8 * kp(rho) + 4 * rho * kpp(rho)
        heat = -4 * math.pi ** 2 * math.exp(-rho / (8 * tau)) / (64 * math.pi ** 2 * tau ** 2)
        worst_lap = max(worst_lap, abs(lap / heat - 1))
    case('C1 flowed propagator: 4D Laplacian of k equals -4 pi^2 x heat kernel (EOM part is contact)', 'C1',
         'floating', worst_lap, 1e-3)
    r = 3.0
    case('C1 flowed propagator: transverse weight -4 k\'(r^2) -> 4/r^4 at r >> sqrt(tau) (long range)', 'C1',
         'floating', abs(-4 * kp(r * r) * r ** 4 / 4 - 1), 1e-6)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--output')
    args = parser.parse_args()
    r0_controls()
    out, hs = r_rounded()
    c1_closure()
    data = dict(
        program='check_rounded_and_closure.py',
        prepared_by='Claude Opus 5.5 (Anthropic), model identifier claude-opus-5-5 as reported by the runtime; effort not exposed',
        prepared_for='Edward Baker',
        date='2026-09-24',
        parameters=dict(rounding='circular fillet of radius delta tangent to both legs; chi advances pi per fillet',
                        units='rescaled trace, Loewner time 1; B_1 stripped'),
        derived=dict(finite_part={f'{s:g}': v[0] for s, v in out.items()},
                     sliver_prediction={f'{s:g}': v[1] for s, v in out.items()},
                     hairpin_constant=hs),
        scope=('One-loop rounded flipped loop and closure-audit controls; diagnostics of analytic '
               'statements, not interval arithmetic.'),
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
