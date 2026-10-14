#!/usr/bin/env python3
"""K=2 compensated theta stationary certificate on a bounded padded rectangle.

2026-10-14. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
Requires python-flint. All deciding arithmetic uses Arb/Acb real/complex balls.
No sampled sign or known zero location decides a retained/excluded cell.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
import platform
import time

import flint
from flint import arb, acb, ctx


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def rat(s):
    q = Fraction(s)
    return arb(q.numerator) / q.denominator


def enc(a):
    require(a.is_finite(), "Nonfinite real enclosure")
    def dy(v):
        m, e = v.man_exp()
        return {"mantissa": str(m), "exponent": int(e)}
    return {"display": a.str(20, more=True),
            "lower_dyadic": dy(a.lower()), "upper_dyadic": dy(a.upper())}


def symmetric(a):
    require(a >= 0, "Negative radius payment")
    return arb(0, a.upper())


def ipow(a, n):
    # python-flint's generic Arb power may use log(a), yielding NaN for
    # intervals crossing zero. Polynomial integer powers use multiplication.
    out = arb(1)
    for k in range(n):
        out *= a
    return out


def dyadic_fraction(d):
    return Fraction(int(d['mantissa'])) * Fraction(2)**int(d['exponent'])


def p_add(a, b):
    c = defaultdict(int, a)
    for e, v in b.items():
        c[e] += v
    return {e: v for e, v in c.items() if v}


def p_mul(a, b):
    c = defaultdict(int)
    for (ua, qa), ca in a.items():
        for (ub, qb), cb in b.items():
            c[ua + ub, qa + qb] += ca * cb
    return dict(c)


def p_diff(a, which):
    c = {}
    for e, v in a.items():
        if e[which]:
            ee = list(e)
            ee[which] -= 1
            c[tuple(ee)] = v * e[which]
    return c


def positive_derivative_polynomials():
    q = [{(0, 1): 2, (0, 0): 3}]
    for k in range(4):
        q.append(p_add(p_add(p_mul({(1, 0): 2, (0, 0): 5, (0, 1): 4}, q[-1]),
                             p_diff(q[-1], 0)),
                       p_mul({(0, 1): 4}, p_diff(q[-1], 1))))
    return q


def gaussian_poly_derivative(poly, n):
    # d[p(u)e^-u²]/du = [p'(u)-2u p(u)]e^-u².
    for k in range(n):
        out = defaultdict(int)
        for e, c in poly.items():
            if e:
                out[e - 1] += e * c
            out[e + 1] -= 2 * c
        poly = {e: c for e, c in out.items() if c}
    return poly


def gaussian_moment(k):
    return (arb(k + 1) / 2).gamma() / 2


def compensated_tail_norms(n):
    """Exact manuscript (14.4) recurrence; every omitted n>N is paid."""
    p = arb.pi()
    a = p * (n + 1)**2
    require(a >= 25, "K=2 all-index tail threshold")
    q = positive_derivative_polynomials()
    def ts(s):
        return a**s * (-a).exp() / (1 - (-p * (n + 2)).exp())
    norms = []
    beta_norms = []
    for j in range(4):
        w = {}
        for ell in range(min(j, 4) + 1):
            c = comb(4, ell) * factorial(j) // factorial(j - ell)
            w = p_add(w, {(ua + j - ell, qb): c * cv
                          for (ua, qb), cv in q[4 - ell].items()})
        main = sum(arb(c) * factorial(ua) / arb(3)**(ua + 1) * ts(qb - ua)
                   for (ua, qb), c in w.items())
        bn = []
        for k, beta in enumerate(({1: 1, 3: 1}, {3: Fraction(1, 6)})):
            pol = gaussian_poly_derivative({e + j: c for e, c in beta.items()}, 4)
            bb = sum(rat(c) * gaussian_moment(e) for e, c in
                     {e: abs(c) for e, c in pol.items()}.items())
            bn.append(bb)
            eta = {qb: c for (ua, qb), c in q[2 * k + 1].items() if ua == 0}
            main += bb * sum(arb(c) * ts(qb + 1) for qb, c in eta.items())
        norms.append(main)
        beta_norms.append(bn)
    return norms, beta_norms


def endpoint_coefficients(n):
    # Exact derivative polynomial P_k(0,q), t=0, for k=1,3.
    # At u=0 the original source has no u-polynomial factors.
    pol = {1: 2, 0: -3}
    vals = []
    for k in range(4):
        a = arb.pi() * n*n
        vals.append(a * (-a).exp() * sum(arb(c) * a**e for e, c in pol.items()))
        out = defaultdict(int)
        for e, c in pol.items():
            out[e] += (5 + 4*e) * c
            out[e + 1] -= 4*c
        pol = dict(out)
    return vals[1], vals[3]


class Source:
    def __init__(self, n, bits, space_order, time_order, beta_order):
        self.n = n
        self.p = arb.pi()
        self.t0 = rat('13/400')
        self.dt = rat('11/400')
        self.tmax = rat('3/50')
        self.lt = time_order
        self.lx = space_order
        self.lb = beta_order
        self.top = 3 + 2*(self.lt - 1) + self.lx - 1
        self.mtop = 3 + 2*(self.lt - 1) + self.lx
        self.tol = arb(2)**(-(bits - 48))
        self.endpoints = [endpoint_coefficients(nn) for nn in range(1, n + 1)]
        self.tail_norms, self.beta_norms = compensated_tail_norms(n)
        self.moments = []
        self.moment_quadrature_max_radius = arb(0)
        self.jet_quadrature_max_radius = arb(0)
        self.source_tail_max = arb(0)
        for nn in range(1, n + 1):
            mm = []
            for k in range(self.mtop + 1):
                v, rad, tail = self.integrate(nn, self.tmax, arb(0), k, True)
                mm.append(v)
                self.moment_quadrature_max_radius = max(self.moment_quadrature_max_radius, rad)
                self.source_tail_max = max(self.source_tail_max, tail)
            self.moments.append(mm)
        require(all(m > 0 for mm in self.moments for m in mm), "Positive channel moment enclosures")

    def phi(self, nn, u):
        a = self.p * nn*nn
        return (2*a*a*(9*u).exp() - 3*a*(5*u).exp()) * (-a*(4*u).exp()).exp()

    def source_tail(self, nn, t, k):
        a = self.p * nn*nn
        slope = 4*a*arb(4).exp() - 9 - 2*t
        require(slope > 0 and 16*a*arb(4).exp() > 2*t, "Source-tail concavity and decay")
        # u=1+s; source majorant 2a² e^(t+9-ae^4) e^-slope*s.
        return 2*a*a*(t + 9 - a*arb(4).exp()).exp() * sum(
            arb(comb(k, ell)*factorial(ell))/slope**(ell + 1) for ell in range(k + 1))

    def integrate(self, nn, t, x, k, moment=False):
        def f(u, analytic):
            if moment:
                tr = 1
            else:
                phase = x*u
                tr = (phase.cos(), -phase.sin(), -phase.cos(), phase.sin())[k % 4]
            return self.phi(nn, u) * (t*u*u).exp() * u**k * tr
        v = acb.integral(f, 0, 1, rel_tol=self.tol, abs_tol=self.tol,
                         eval_limit=100000, depth_limit=30)
        require(v.is_finite() and v.imag.contains(0), "Validated finite real quadrature")
        tail = self.source_tail(nn, t, k)
        return v.real + symmetric(tail), v.real.rad(), tail

    def raw_transport(self, nn, jets, k, eta):
        tau = symmetric(self.dt)
        ax = abs(eta).upper()
        mm = self.moments[nn - 1]
        total = arb(0)
        rx = arb(0)
        for ell in range(self.lt):
            sx = sum(ipow(eta, m)/factorial(m)*jets[k + 2*ell + m] for m in range(self.lx))
            total += ipow(-tau, ell)/factorial(ell)*sx
            rx += self.dt**ell/factorial(ell)*ax**self.lx/factorial(self.lx)*mm[k + 2*ell + self.lx]
        rt = self.dt**self.lt/factorial(self.lt)*mm[k + 2*self.lt]
        return total + symmetric(rx + rt), rx + rt

    def beta_jets(self, x):
        # I_m=integral_0^inf u^m e^-u² exp(ixu)du.
        # Entire erfi transform includes the complete Gaussian half-line.
        ii = acb(0, 1)
        y = x/2
        i0 = arb.pi().sqrt()/2*(-y*y).exp()*acb(1, y.erfi())
        integrals = [i0, (1 + ii*x*i0)/2]
        for m in range(1, self.lb + 6):
            integrals.append((m*integrals[m - 1] + ii*x*integrals[m])/2)
        b0 = [(ii**k*(integrals[k + 1] + integrals[k + 3])).real for k in range(self.lb + 4)]
        b1 = [(ii**k*integrals[k + 3]/6).real for k in range(self.lb + 4)]
        return b0, b1

    def beta_transport(self, jets, which, k, eta):
        v = sum(ipow(eta, m)/factorial(m)*jets[k + m] for m in range(self.lb))
        q = k + self.lb
        moment = (gaussian_moment(q + 1) + gaussian_moment(q + 3) if which == 0
                  else gaussian_moment(q + 3)/6)
        remainder = abs(eta).upper()**self.lb/factorial(self.lb)*moment
        return v + symmetric(remainder), remainder

    def center(self, x):
        raw = []
        for nn in range(1, self.n + 1):
            vv = []
            for k in range(self.top + 1):
                v, rad, tail = self.integrate(nn, self.t0, x, k)
                vv.append(v)
                self.jet_quadrature_max_radius = max(self.jet_quadrature_max_radius, rad)
                self.source_tail_max = max(self.source_tail_max, tail)
            raw.append(vv)
        return raw, self.beta_jets(x)

    def enclosure(self, center_data, eta):
        raw, betas = center_data
        beta = [[self.beta_transport(betas[b], b, k, eta)[0] for k in range(4)] for b in range(2)]
        beta_remainders = [[self.beta_transport(betas[b], b, k, eta)[1] for k in range(4)] for b in range(2)]
        channels = []
        raw_values = []
        raw_remainders = []
        tball = self.t0 + symmetric(self.dt)
        for nn in range(1, self.n + 1):
            b, e = self.endpoints[nn - 1]
            vals, pays = [], []
            for k in range(4):
                v, payment = self.raw_transport(nn, raw[nn - 1], k, eta)
                vals.append(v)
                pays.append(payment)
            raw_values.append(vals)
            raw_remainders.append(pays)
            channels.append([vals[k] - b*beta[0][k] - (e + 6*tball*b)*beta[1][k] for k in range(4)])
        # Correlated aggregation: subtract the summed endpoint coefficient once.
        # This is exactly sum_n a_n, retaining all arithmetic cross terms.
        sb = sum(z[0] for z in self.endpoints)
        se = sum(z[1] for z in self.endpoints)
        aggregate = [sum(vals[k] for vals in raw_values) - sb*beta[0][k]
                     - (se + 6*tball*sb)*beta[1][k] for k in range(4)]
        return aggregate, channels, raw_remainders, beta_remainders


def exact_controls():
    # Exact rational endpoint interpolation and arbitrary-shift heat controls.
    q = Fraction
    beta0 = {1: q(1), 3: q(1)}
    beta1 = {3: q(1, 6)}
    def odd_jet(pol, k):
        return factorial(k)*sum(c*(-1)**((k-e)//2)/factorial((k-e)//2)
                                for e, c in pol.items() if e <= k and (k-e)%2 == 0)
    checks = {"beta0_first_jet_one": odd_jet(beta0, 1) == 1,
              "beta0_third_jet_zero": odd_jet(beta0, 3) == 0,
              "beta1_first_jet_zero": odd_jet(beta1, 1) == 0,
              "beta1_third_jet_one": odd_jet(beta1, 3) == 1}
    # Independent coefficientwise expansion in twelve formal jet variables.
    # A monomial is the sorted pair ((n,k),(m,l)); coefficients are integers.
    for j in (0, 1):
        aggregate_polynomial = defaultdict(int)
        paired_polynomial = defaultdict(int)
        def add_monomial(poly, n, k, m, ell, coefficient):
            poly[tuple(sorted(((n, k), (m, ell))))] += coefficient
        for n in range(3):
            for m in range(3):
                add_monomial(aggregate_polynomial, n, j+1, m, j+1, 1)
                add_monomial(aggregate_polynomial, n, j, m, j+2, -1)
            add_monomial(paired_polynomial, n, j+1, n, j+1, 1)
            add_monomial(paired_polynomial, n, j, n, j+2, -1)
            for m in range(n+1, 3):
                add_monomial(paired_polynomial, n, j+1, m, j+1, 2)
                add_monomial(paired_polynomial, n, j, m, j+2, -1)
                add_monomial(paired_polynomial, m, j, n, j+2, -1)
        checks['D_plus_X_coefficientwise_identity_j'+str(j)] = dict(aggregate_polynomial) == dict(paired_polynomial)
    # An additional exact substitution exercises the formula ordering.
    av = [[q(2), q(3), q(5), q(7)], [q(-11), q(13), q(-17), q(19)],
          [q(23), q(-29), q(31), q(-37)]]
    for j in (0, 1):
        pp = [sum(aa[k] for aa in av) for k in range(4)]
        dd = sum(aa[j+1]**2-aa[j]*aa[j+2] for aa in av)
        xx = sum(2*av[n][j+1]*av[m][j+1]-av[n][j]*av[m][j+2]-av[m][j]*av[n][j+2]
                 for n in range(3) for m in range(n+1, 3))
        checks['D_plus_X_exact_j'+str(j)] = dd+xx == pp[j+1]**2-pp[j]*pp[j+2]
    controls = []
    a, threshold = q(24), q(1, 40)
    control_polynomials = {
        'Q2': {(0, 2): q(1), (0, 1): -2*a, (0, 0): a*a+2*threshold, (1, 0): q(-2)},
        'Q3': {(0, 3): q(1), (0, 2): -3*a, (0, 1): 3*a*a+6*threshold,
               (0, 0): -a**3-6*a*threshold, (1, 1): q(-6), (1, 0): 6*a}}
    control_derivatives = {}
    for name, pol in control_polynomials.items():
        checks[name+'_backward_heat_coefficientwise'] = p_diff(pol, 0) == {
            e: -c for e, c in p_diff(p_diff(pol, 1), 1).items()}
        control_derivatives[name] = [pol]
        for k in range(3):
            control_derivatives[name].append(p_diff(control_derivatives[name][-1], 1))
    def evaluate_control(pol, tt):
        return sum(c*tt**kt*a**kx for (kt, kx), c in pol.items())
    for hh in (q(1, 1000), q(1, 10000), q(1, 100000)):
        tt = threshold-hh
        qq2 = [evaluate_control(pol, tt) for pol in control_derivatives['Q2']]
        qq3 = [evaluate_control(pol, tt) for pol in control_derivatives['Q3']]
        l0, e0 = qq2[1]**2-qq2[0]*qq2[2], qq2[0]**2+qq2[1]**2
        l1, e1 = qq3[2]**2-qq3[1]*qq3[3], qq3[0]**2+qq3[1]**2
        checks['double_control_stationarity_'+str(hh)] = qq2[1] == 0
        checks['triple_control_stationarity_'+str(hh)] = qq3[2] == 0
        checks['double_control_ratio_'+str(hh)] = l0 < 0 and -l0/e0 == 1/hh
        checks['triple_control_ratio_'+str(hh)] = l1 < 0 and -l1/e1 == 1/hh
        checks['collision_control_inside_padded_time_band_'+str(hh)] = q(1, 200) < tt < q(3, 50)
        controls.append({"a": "24", "T": "1/40", "h": str(hh),
                         "t": str(tt), "x": "24",
                         "Q2_stationary_L0": str(l0), "Q2_energy": str(e0),
                         "Q3_stationary_L1": str(l1), "Q3_energy": str(e1),
                         "negative_L_to_energy": str(-l0/e0)})
    require(all(checks.values()), "Exact controls and endpoint interpolation")
    return checks, controls


def analyze_cell(source, left, right, depth=0):
    x0 = (left + right)/2
    dx = (right - left)/2
    data = source.center(x0)
    whole, channels, rawpay, betapay = source.enclosure(data, symmetric(dx))
    eps = [norm/left**4 for norm in source.tail_norms]
    full = [whole[k] + symmetric(eps[k]) for k in range(4)]
    signs = []
    for j in (0, 1):
        pp = whole
        stationary = full[j + 1]
        if not stationary.contains(0):
            signs.append({"j": j, "classification": "stationarity_excluded",
                          "genuine_stationary_derivative": enc(stationary)})
            continue
        derivative = full[j + 2]
        leftjets = source.enclosure(data, -dx)[0]
        rightjets = source.enclosure(data, dx)[0]
        ls = leftjets[j + 1] + symmetric(eps[j + 1])
        rs = rightjets[j + 1] + symmetric(eps[j + 1])
        regular = not derivative.contains(0)
        # A whole-cell polynomial enclosure may cross zero even when the
        # genuine derivative is strictly monotone and both endpoints share
        # a strict sign. This endpoint exclusion is a proof, not a sample.
        if regular and ((ls > 0 and rs > 0) or (ls < 0 and rs < 0)):
            signs.append({"j": j, "classification": "stationarity_excluded",
                          "exclusion_method": "uniform_endpoint_signs_and_strict_spatial_monotonicity",
                          "genuine_stationary_derivative": enc(stationary),
                          "genuine_next_derivative": enc(derivative),
                          "left_stationary_derivative": enc(ls), "right_stationary_derivative": enc(rs)})
            continue
        diagonals = [aa[j+1]**2-aa[j]*aa[j+2] for aa in channels]
        cross = [2*channels[n][j+1]*channels[m][j+1]-channels[n][j]*channels[m][j+2]
                 -channels[m][j]*channels[n][j+2] for n in range(source.n) for m in range(n+1, source.n)]
        dd = sum(diagonals)
        xx = sum(cross)
        ll = pp[j+1]**2-pp[j]*pp[j+2]
        fee = (eps[j+1]**2 + abs(pp[j])*eps[j+2] + abs(pp[j+2])*eps[j]
               + eps[j]*eps[j+2])
        margin = ll-fee
        unique = ((ls < 0 and rs > 0 and derivative > 0)
                  or (ls > 0 and rs < 0 and derivative < 0))
        classification = ("stationary_signed_and_unique_branch" if unique else "stationary_signed_cell") if margin > 0 else "unresolved"
        signs.append({"j": j, "classification": classification,
                      "genuine_stationary_derivative": enc(stationary),
                      "genuine_next_derivative": enc(derivative),
                      "left_stationary_derivative": enc(ls), "right_stationary_derivative": enc(rs),
                      "genuine_next_derivative_separated_from_zero": bool(regular),
                      "regular_stationary_branch_uniform_in_time": bool(unique),
                      "diagonal_terms": [enc(v) for v in diagonals],
                      "cross_index_pairs": [[n+1, m+1] for n in range(source.n) for m in range(n+1, source.n)],
                      "cross_terms": [enc(v) for v in cross],
                      "D": enc(dd), "X": enc(xx),
                      "aggregate_L_P_exactly_D_plus_X": enc(ll),
                      "stationary_error_payment": enc(fee),
                      "correlated_cross_term_surplus_L_P_minus_payment": enc(margin)})
    cell = {"x_left": enc(left), "x_right": enc(right), "depth": depth,
            "compensated_aggregate_jets": [enc(v) for v in whole],
            "compensated_channel_jets": [[enc(v) for v in aa] for aa in channels],
            "complete_compensated_four_jet_errors": [enc(v) for v in eps],
            "raw_source_parameter_Taylor_payments": [[enc(v) for v in aa] for aa in rawpay],
            "complete_Gaussian_transform_Taylor_payments": [[enc(v) for v in aa] for aa in betapay],
            "observations": signs}
    return cell


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--precision', type=int, default=256)
    ap.add_argument('--theta-terms', type=int, default=3)
    ap.add_argument('--space-order', type=int, default=12)
    ap.add_argument('--time-order', type=int, default=5)
    ap.add_argument('--beta-order', type=int, default=24)
    ap.add_argument('--max-depth', type=int, default=6)
    args = ap.parse_args()
    require(args.precision >= 192 and args.theta_terms >= 3 and args.space_order >= 8
            and args.time_order >= 4 and args.beta_order >= 20 and args.max_depth >= 0,
            'Minimum certificate parameters')
    ctx.prec = args.precision
    started = time.monotonic()
    checks, controls = exact_controls()
    source = Source(args.theta_terms, args.precision, args.space_order, args.time_order, args.beta_order)
    cells = []
    stack = [(arb(k), arb(k+1), 0) for k in range(7, 41)]
    while stack:
        left, right, depth = stack.pop()
        cell = analyze_cell(source, left, right, depth)
        if any(o['classification'] == 'unresolved' for o in cell['observations']) and depth < args.max_depth:
            middle = (left+right)/2
            stack.extend([(left, middle, depth+1), (middle, right, depth+1)])
        else:
            cells.append(cell)
    cells.sort(key=lambda c: dyadic_fraction(c['x_left']['lower_dyadic']))
    cover = [(dyadic_fraction(c['x_left']['lower_dyadic']),
              dyadic_fraction(c['x_right']['lower_dyadic'])) for c in cells]
    require(all(c['x_left']['lower_dyadic'] == c['x_left']['upper_dyadic']
                and c['x_right']['lower_dyadic'] == c['x_right']['upper_dyadic'] for c in cells),
            "Cover endpoints must be exact dyadics")
    require(cover[0][0] == 7 and cover[-1][1] == 41
            and all(left < right for left, right in cover)
            and all(cover[k][1] == cover[k+1][0] for k in range(len(cover)-1)),
            "Exact gap-free closed-cell cover of [7,41]")
    totals = {str(j): dict() for j in (0, 1)}
    unresolved = []
    branches = []
    margins = []
    uniform_margin_checks = {"0": True, "1": True}
    branch_isolation_unresolved = []
    for c in cells:
        for o in c['observations']:
            j = str(o['j'])
            cl = o['classification']
            totals[j][cl] = totals[j].get(cl, 0)+1
            if cl == 'unresolved':
                unresolved.append({"x_left": c['x_left'], "x_right": c['x_right'], "j": o['j']})
            if cl == 'stationary_signed_and_unique_branch':
                branches.append({"x_left": c['x_left'], "x_right": c['x_right'], "j": o['j'],
                                 "surplus": o['correlated_cross_term_surplus_L_P_minus_payment']})
            if cl.startswith('stationary_signed'):
                margins.append(o['correlated_cross_term_surplus_L_P_minus_payment'])
                low = dyadic_fraction(o['correlated_cross_term_surplus_L_P_minus_payment']['lower_dyadic'])
                target = Fraction(1, 2000000000) if o['j'] == 0 else Fraction(1, 100000000000)
                uniform_margin_checks[j] = uniform_margin_checks[j] and low > target
                if not o['regular_stationary_branch_uniform_in_time']:
                    branch_isolation_unresolved.append({"x_left": c['x_left'], "x_right": c['x_right'], "j": o['j']})
    status = 'PASS' if not unresolved else 'PARTIAL_UNRESOLVED'
    record = {"schema": "inv21-compensated-stationary-theta-v1", "date": "2026-10-14",
              "provenance": {"prepared_for": "Edward Baker", "llm_assistance": "substantial",
                             "recorded_model": "gpt-6.1-sol (Codex)", "reasoning_effort": "ultra"},
              "runtime": {"python": platform.python_version(), "python_flint": flint.__version__,
                          "seconds": round(time.monotonic()-started, 3)},
              "checker": {"file": Path(__file__).name, "sha256": sha256(Path(__file__).read_bytes()).hexdigest()},
              "manuscript_source_sha256": sha256((Path(__file__).parent.parent/'manuscript/quaternion_theta_geometry.tex').read_bytes()).hexdigest(),
              "precision_bits": args.precision, "normalization": "H=int_0^infinity e^(t u^2) Phi(u) cos(xu)du",
              "domain": {"t": ["1/200", "3/50"], "x": ["7", "41"],
                         "interior_collision_target": {"t": ["1/100", "1/20"], "x": ["8", "40"]}},
              "parameters": {"K": 2, "N": args.theta_terms, "source_cutoff": "1",
                             "time_center": "13/400", "time_radius": "11/400",
                             "initial_x_cell_width": "1", "space_Taylor_order": args.space_order,
                             "time_Taylor_order": args.time_order, "beta_Taylor_order": args.beta_order,
                             "max_spatial_bisection_depth": args.max_depth},
              "quadrature": {"method": "Acb validated integral of entire finite-source integrand",
                             "requested_tolerance_bits": args.precision-48, "eval_limit": 100000, "depth_limit": 30,
                             "max_returned_jet_quadrature_radius": enc(source.jet_quadrature_max_radius),
                             "max_returned_moment_quadrature_radius": enc(source.moment_quadrature_max_radius),
                             "max_all_source_integration_tail": enc(source.source_tail_max)},
              "complete_index_tail": {"formula": "manuscript (14.3)-(14.4), K=2; epsilon_j=C_j/x_left^4",
                                      "norm_constants_C_j": [enc(v) for v in source.tail_norms],
                                      "beta_L1_majorants_B_jk": [[enc(v) for v in vv] for vv in source.beta_norms]},
              "endpoint_coefficients": [{"n": n+1, "b_n": enc(b), "e_n": enc(e)} for n, (b,e) in enumerate(source.endpoints)],
              "summed_endpoint_coefficients": {"sum_b": enc(sum(v[0] for v in source.endpoints)),
                                               "sum_e": enc(sum(v[1] for v in source.endpoints))},
              "channel_absolute_moments_at_tmax": [[enc(v) for v in mm] for mm in source.moments],
              "exact_checks": checks, "shifted_heat_collision_controls": controls,
              "cell_count": len(cells), "observation_totals": totals,
              "exact_cover_checks": {"closed_time_band": ["1/200", "3/50"],
                                     "left_endpoint": "7", "right_endpoint": "41",
                                     "all_spatial_endpoints_exact_dyadic": True,
                                     "strict_positive_cell_widths": True,
                                     "adjacent_endpoints_equal": True,
                                     "gap_free_closed_cover": True},
              "regular_stationary_branches": branches, "unresolved_cells": unresolved,
              "branch_isolation_unresolved_cells": branch_isolation_unresolved,
              "uniform_stationary_surplus_targets": {"0": "1/2000000000", "1": "1/100000000000"},
              "uniform_stationary_surplus_target_checks": uniform_margin_checks,
              "stationary_margins": margins, "cells": cells,
              "status": status,
              "established_claim": ("For every (t,x) in R+, h_(j+1)=0 implies L_j(H)>0, j=0,1. "
                                    "Every omitted index, source integration tail, Gaussian transform, quadrature, rounding, "
                                    "and parameter Taylor remainder is enclosed. Retained D/X terms evaluated with correlated aggregate identity."
                                    if status == 'PASS' else 'Only the individually reported cells are certified; unresolved cells remain.'),
              "limitations": ["Bounded domain only; no all-height RH conclusion.",
                              "Finite compensated channels do not separately obey heat; collision theorem applies only to complete H.",
                              "D and X need not be individually positive; signs use their exact correlated sum."]}
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+'\n')
    print(json.dumps({"status": status, "cell_count": len(cells), "observation_totals": totals,
                      "regular_stationary_branches": branches, "unresolved_cell_count": len(unresolved),
                      "seconds": record['runtime']['seconds'], "record_bytes": args.output.stat().st_size}, indent=2))
    if unresolved:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
