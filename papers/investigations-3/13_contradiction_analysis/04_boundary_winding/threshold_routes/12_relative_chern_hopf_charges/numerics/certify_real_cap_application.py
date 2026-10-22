#!/usr/bin/env python3
"""BW12 complete-source two-root real-cap application, 21 October 2026.
Prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6-astra (Codex), reasoning effort max.
Requires python-flint 0.9.0 and certify_relative_charge_pilot.py.
Analytic contract and payments: BW12 Note 06. No RH assumption.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import signal
import sys
import time
sys.dont_write_bytecode = True
import flint
from flint import arb, acb, ctx


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def A(value):
    q = Q(value)
    return arb(q.numerator) / q.denominator


def rec(value):
    return value.str(38, more=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_pilot(folder):
    path = folder / 'certify_relative_charge_pilot.py'
    spec = importlib.util.spec_from_file_location('pilot', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, digest(path)


class Source:
    def __init__(self, pilot):
        self.pilot = pilot
        self.pi = arb.pi()
        self.integrals = 0
        self.callbacks = 0
        self.max_radius = arb(0)
        self.max_tail = arb(0)

    def jet(self, j, t, z):
        self.integrals += 1
        require(self.integrals <= 5000, 'source acquisition budget')
        def integrand(u, analytic):
            self.callbacks += 1
            v = acb(0)
            q = (4*u).exp()
            for n in range(1, 5):
                lam = self.pi*n*n
                v += (2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
            phase = z*u
            trig = phase.cos() if j % 2 == 0 else phase.sin()
            if j % 4 in (1, 2):
                trig = -trig
            return (u+t*u*u).exp()*v*u**j*trig
        core = acb.integral(integrand, 0, 1, abs_tol=arb('1e-32'),
                            rel_tol=arb('1e-28'), eval_limit=100000,
                            depth_limit=30)
        require(core.is_finite(), 'finite source integral')
        rad = (core.real.rad()**2 + core.imag.rad()**2).sqrt().upper()
        require(rad < arb('1e-27'), 'source quadrature error budget')
        # A common envelope covers all anchors and both real time caps.
        omitted, exterior = self.pilot.tails(j, A('1/100'), arb(10), self.pi)
        tail = (omitted+exterior).upper()
        self.max_radius = max(self.max_radius, rad)
        self.max_tail = max(self.max_tail, tail)
        return core + acb(arb(0, tail), arb(0, tail))

    def moments(self):
        out, rows = {}, []
        for j in range(8, 18):
            value, row = self.pilot.acquire('moment', j, arb(0),
                                            A('1/100'), arb(10), self.pi)
            out[j] = value
            rows.append(row)
            self.integrals += 1
            self.callbacks += row['callbacks']
        return out, rows


def remainder(j, eta, h, moments):
    return sum((eta**k*h**(8-k)*moments[j+8+k]
                / (math.factorial(k)*math.factorial(8-k))
                for k in range(9)), arb(0)).upper()


def variation(coeff, eta, h, rem):
    value = rem
    for degree in range(1, 8):
        for k in range(degree+1):
            ell = degree-k
            value += (eta**k*h**ell*abs(coeff[2*k+ell]).upper()
                      / (math.factorial(k)*math.factorial(ell)))
    return value.upper()


def circle(source, radius, moments):
    n = 256
    eta = A('3/200')  # > sqrt(2)/100 on the whole time rectangle
    h = (2*source.pi*radius/n).upper()  # one full circular arc
    kappa = -A('3/10')
    remainders = [remainder(j, eta, h, moments) for j in (0, 1)]
    data = []
    for k in range(n//2+1):
        angle = 2*source.pi*k/n
        z = acb(A('71/2')) + radius*acb(0, angle).exp()
        jets = [source.jet(j, acb(0), z) for j in range(16)]
        data.append(jets)
    data += [[v.conjugate() for v in data[n-k]] for k in range(n//2+1, n)]
    require(len(data) == n, 'circle coverage')
    floor, raw_ratio, coupled_ratio, rho = [], [], [], []
    for jets in data:
        e0 = variation(jets, eta, h, remainders[0])
        e1 = variation(jets[1:], eta, h, remainders[1])
        denominator = (abs(jets[0]).lower()-e0).lower()
        require(denominator > 0, 'complete circle wall floor')
        coupled = [jets[j+1]-kappa*jets[j] for j in range(15)]
        en = variation(coupled, eta, h,
                       remainders[1]+abs(kappa)*remainders[0])
        floor.append(denominator)
        raw_ratio.append(((abs(jets[1]).upper()+e1)/denominator).upper())
        coupled_ratio.append(((abs(coupled[0]).upper()+en)/denominator).upper())
        rho.append((e0/abs(jets[0]).lower()).upper())
    # On each arc H(0,z) and its endpoint chord stay in one zero-free
    # disk centered at H(0,z_k). Thus this polygon has the exact winding.
    total_argument = arb(0)
    for k in range(n):
        ratio = data[(k+1) % n][0]/data[k][0]
        require(ratio.real > 0, 'unambiguous consecutive phase increment')
        total_argument += ratio.arg()
    winding = total_argument/(2*source.pi)
    require(winding.contains(2) and winding > A('3/2') and winding < A('5/2'),
            'integer spatial root count exactly two')
    serial = [[rec(v) for v in row] for row in data]
    return {
        'radius': radius, 'angular_subdivisions': n, 'acquired_anchors': n//2+1,
        'spatial_step_upper': rec(h), 'time_modulus_allowance': '3/200',
        'joint_taylor_order': 8, 'remainders_H_Hz': [rec(v) for v in remainders],
        'wall_floor_lower': rec(min(floor)), 'maximum_relative_variation': rec(max(rho)),
        'spatial_winding_enclosure': rec(winding), 'spatial_root_count': 2,
        'max_log_derivative_ratio_upper': rec(max(raw_ratio)),
        'mean_log_derivative_ratio_upper': rec((sum(raw_ratio, arb(0))/n).upper()),
        'max_coupled_ratio_upper': rec(max(coupled_ratio)),
        'mean_coupled_ratio_upper': rec((sum(coupled_ratio, arb(0))/n).upper()),
        'kappa': '-3/10',
        'regenerated_source_jets_sha256': hashlib.sha256(
            json.dumps(serial, separators=(',', ':')).encode()).hexdigest(),
    }, (sum(coupled_ratio, arb(0))/n).upper(), min(floor)


def controls():
    # The same wall/Taylor/winding consumer receives an exact quadratic
    # event, a real-root pair, and a nonreal-root pair on the declared box.
    # All moments used in the order-eight remainder are zero for them.
    class PolynomialSource:
        pi = arb.pi()
        def __init__(self, c):
            self.c = c
        def jet(self, j, t, z):
            w = z-acb(A('71/2'))
            return (w*w-2*t+self.c, 2*w, acb(2))[j] if j < 3 else acb(0)
    rows = []
    for c, charge in [(0, 1), (-1, 0), (1, 0)]:
        left, right = Q(-2,25)-4*c, Q(2,25)-4*c
        require(charge == ((1 if right > 0 else -1)-(1 if left > 0 else -1))//2,
                'quadratic real-cap charge control')
        src = PolynomialSource(c)
        inner, _, _ = circle(src, 8, {j: arb(0) for j in range(8,18)})
        outer, ratio, _ = circle(src, 10, {j: arb(0) for j in range(8,18)})
        paid_phase = (ratio/10).upper()
        require(paid_phase < src.pi/2, 'polynomial actual-consumer phase bound')
        rows.append({'H': f'(z-71/2)^2-2t+({c})',
                     'time_caps': ['-1/100', '1/100'],
                     'imaginary_half_width': '1/100', 'inner_radius': 8,
                     'outer_radius': 10, 'Delta_at_caps': [str(left), str(right)],
                     'A_exact': 0, 'charge': charge,
                     'same_consumer_spatial_counts': [inner['spatial_root_count'],
                                                      outer['spatial_root_count']],
                     'same_consumer_wall_floors': [inner['wall_floor_lower'],
                                                  outer['wall_floor_lower']],
                     'same_consumer_K_tau_upper': rec(paid_phase)})
    return rows


def run(folder):
    start = time.monotonic()
    pilot, pilot_hash = load_pilot(folder)
    source = Source(pilot)
    moments, moment_rows = source.moments()
    circles = []
    for radius in (8, 10):
        row, ratio, floor = circle(source, radius, moments)
        circles.append(row)
        print(json.dumps({'checkpoint': f'circle {radius}', 'floor': row['wall_floor_lower'],
                          'count': row['spatial_root_count'], 'coupled_ratio': rec(ratio),
                          'seconds': time.monotonic()-start}), flush=True)
        if radius == 10:
            K = (4*radius*ratio/(10-8)**2).upper()
            phase = (K/100).upper()
            require(phase < source.pi/2, 'paid complex-time phase bound')
    caps = []
    for t in (Q(-1,100), Q(1,100)):
        values = [source.jet(0, acb(A(t)), acb(x)) for x in (28, 29, 41, 43)]
        for v in values:
            require(v.imag.contains(0), 'real cap source')
        require(values[0].real > 0 and values[1].real < 0
                and values[2].real < 0 and values[3].real > 0,
                'two disjoint sign-changing real cap brackets')
        caps.append({'time': str(t), 'real_positions': [28,29,41,43],
                     'H_enclosures': [rec(v.real) for v in values],
                     'root_brackets': [[28,29],[41,43]],
                     'discriminant_lower_strict': 144, 'discriminant_sign': 1})
    require(source.integrals <= 5000, 'complete acquisition budget')
    return {
        'schema': 'rch12-complete-real-cap-application-v1', 'date': '2026-10-21',
        'timezone': 'America/New_York', 'prepared_for': 'Edward Baker',
        'authoring_model': 'gpt-6-astra', 'actual_effort': 'max',
        'LLM_assistance': 'substantial; derivation and review by the same assistant',
        'status': 'finite complete-source interval certificate; no global simplicity conclusion',
        'python': platform.python_version(), 'python_flint': flint.__version__,
        'precision_bits': ctx.prec, 'script_sha256': digest(Path(__file__)),
        'pilot_sha256': pilot_hash,
        'plan_sha256': digest(folder/'REAL_CAP_APPLICATION_PLAN_20261021.json'),
        'domain': {'Re_t': ['-1/100','1/100'], 'Im_t': ['-1/100','1/100'],
                   'spatial_center': '71/2', 'inner_radius': 8, 'outer_radius': 10,
                   'orientation': 'complex orientation; outward boundary orientation'},
        'complete_source_moments': moment_rows, 'circles': circles,
        'analytic_A_bound_upper': rec(K), 'K_tau_upper': rec(phase),
        'pi_over_two_minus_K_tau_lower': rec((source.pi/2-phase).lower()),
        'caps': caps, 'certified_charge': 0,
        'method': 'two spatial root counts + coupled wall coefficient + real-cap theorem',
        'controls': controls(),
        'cost': {'complete_integrals': source.integrals, 'callbacks': source.callbacks,
                 'elapsed_seconds': time.monotonic()-start,
                 'maximum_jet_quadrature_radius': rec(source.max_radius),
                 'maximum_complete_jet_tail_allowance': rec(source.max_tail),
                 'scope': 'application feasibility only; no direct-cost comparison'},
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent)
    args = p.parse_args()
    ctx.prec = 192
    signal.alarm(180)
    result = run(args.source_dir)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
          ('certified_charge','analytic_A_bound_upper','K_tau_upper','cost')}))


if __name__ == '__main__':
    main()
