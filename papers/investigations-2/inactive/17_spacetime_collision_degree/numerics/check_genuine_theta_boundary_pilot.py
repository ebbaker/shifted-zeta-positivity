#!/usr/bin/env python3
"""Small full-theta boundary/interior comparison, using outward intervals.

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent configuration: gpt-6-astra (Codex), reasoning effort ultra.
This is an internal arithmetic certificate, not independent validation.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import platform
import sys
import time


ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'quasi-rh-exponent-descent/newman_collisions'
INTERVAL = BASE / '13_microlocal_phase_space/numerics'
SOURCES = {
    INTERVAL / 'check_block_current.py':
        '0cfca37632cfaaea522cce2a9514b81eaf9db0bf6213cd243de0f937679627a2',
    INTERVAL / 'check_complete_current_rectangle.py':
        'ac547ff45915d95369afc558f6ee3daa01fb6974ad1569e719dc3f0abcd4c522',
    BASE / '17_enlarged_state_transport/numerics/check_theta_stationary_low_height.py':
        '18058e4994ae1c93f7796b87a12537a519340ea56228b5eac20a8db3ca1fa704',
    BASE / '17_enlarged_state_transport/numerics/THETA_STATIONARY_LOW_HEIGHT_RECORD_20261010.json':
        'f9c8159a7564f85ee55bbf3d14c4e8923593a3b6e9080ace6d2e3ddbfdbcf48e',
}
for source, digest in SOURCES.items():
    if hashlib.sha256(source.read_bytes()).hexdigest() != digest:
        raise RuntimeError('Retained input mismatch: ' + str(source))
sys.path.insert(0, str(INTERVAL))
from check_complete_current_rectangle import I, UP, PRECISION, pi_interval, reduced_trig, absmax


def pad(value, error):
    return value + I(error.copy_negate(), error)


def clip_trig(value):
    return I(max(Decimal(-1), value.lo), min(Decimal(1), value.hi))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--u-cells', type=int, default=512)
    parser.add_argument('--record', type=Path)
    args = parser.parse_args()
    assert args.u_cells > 0 and args.u_cells & (args.u_cells - 1) == 0
    # Dyadic cells have exactly representable Decimal endpoints and widths.
    start = time.perf_counter()
    pi = pi_interval()
    width = I(1) / args.u_cells
    assert width.lo == width.hi
    density_cells = []
    for j in range(args.u_cells):
        left, right = width * j, width * (j + 1)
        assert left.lo == left.hi and right.lo == right.hi
        u = I(left.lo, right.hi)
        e4, e5, e9 = [(k * u).exp() for k in (4, 5, 9)]
        value = I(0)
        for n in (1, 2, 3):
            c = pi * n * n
            value += (2 * c**2 * e9 - 3 * c * e5) * (-c * e4).exp()
        def omitted(power):
            ratio = (I(5) / 4)**power * (-9 * pi * e4).exp()
            assert ratio.hi < 1
            return I(4)**power * (-16 * pi * e4).exp() / (1 - ratio)
        missing = 2 * pi**2 * e9 * omitted(4) + 3 * pi * e5 * omitted(2)
        phi = value + I(0, missing.hi)
        assert phi.lo > 0
        density_cells.append((u, phi, missing.hi))
    preparation_seconds = time.perf_counter() - start

    # Full-source Gaussian majorant on u>=0; proof is in the companion note.
    assert (16 * (-3 * pi).exp()).hi < Decimal('.5')
    assert (4 * pi).lo > 9
    C = 4 * pi**2 * (-pi).exp()
    a = 8 * pi - I('.05')
    factor = C * (-a).exp()
    tails = [factor / (2 * a), factor / (2 * a),
             factor * (1 / (2 * a) + 1 / (4 * a**2)),
             factor * (1 / (2 * a) + 1 / (2 * a**2))]

    class Evaluator:
        def __init__(self):
            self.weights = {}
            self.calls = 0
            self.omitted_payments = []
            self.absolute_moments = []

        def pair(self, t, x):
            self.calls += 1
            key = tuple(t.strings())
            if key not in self.weights:
                weights, omitted, moments = [], [I(0) for _ in range(4)], [I(0) for _ in range(4)]
                for u, phi, missing in density_cells:
                    heat = (t * u**2).exp()
                    row = [width * u**k * heat * phi for k in range(4)]
                    weights.append((u, row))
                    for k in range(4):
                        omitted[k] += width * u**k * heat * I(missing)
                        moments[k] += row[k]
                self.weights[key] = weights
                self.omitted_payments.append([str(v.hi) for v in omitted])
                self.absolute_moments.append([str((moments[k] + tails[k]).hi) for k in range(4)])
            centre = I(x.midpoint())
            sin_step, cos_step = reduced_trig(centre * width, pi)
            sin_phase, cos_phase = reduced_trig(centre * width / 2, pi)
            values = [I(0), I(0)]
            for j, (u, row) in enumerate(self.weights[key]):
                phase = centre * width * (I(j) + I('.5'))
                phase_error = absmax(x * u - phase)
                sine = clip_trig(pad(sin_phase, phase_error))
                cosine = clip_trig(pad(cos_phase, phase_error))
                values[0] += row[0] * cosine
                values[1] -= row[1] * sine
                sin_phase, cos_phase = (sin_phase * cos_step + cos_phase * sin_step,
                                        cos_phase * cos_step - sin_phase * sin_step)
            return [pad(values[k], tails[k].hi) for k in range(2)]

    # One complete interval enclosure per oriented boundary side.
    boundary = Evaluator()
    boundary_start = time.perf_counter()
    edges = [('bottom', I(0, '.05'), I(8), ['0', '8'], ['0.05', '8']),
             ('right', I('.05'), I(8, 12), ['0.05', '8'], ['0.05', '12']),
             ('top', I(0, '.05'), I(12), ['0.05', '12'], ['0', '12']),
             ('left', I(0), I(8, 12), ['0', '12'], ['0', '8'])]
    boundary_records = []
    for name, t, x, path_start, path_end in edges:
        pair = boundary.pair(t, x)
        assert pair[1].hi < 0, (name, [v.strings() for v in pair])
        boundary_records.append({'edge': name, 'time': t.strings(), 'space': x.strings(),
                                 'oriented_start_time_space': path_start,
                                 'oriented_end_time_space': path_end,
                                 'H_Hx': [v.strings() for v in pair],
                                 'norm_lower_bound': str(pair[1].hi.copy_negate())})
    boundary_seconds = time.perf_counter() - boundary_start
    # The complete boundary lies in the open lower half-plane. Straight
    # homotopy to -i stays there, so its winding is exactly zero.

    interior = Evaluator()
    interior_start = time.perf_counter()
    pair = interior.pair(I(0, '.05'), I(8, 12))
    assert pair[1].hi < 0, [v.strings() for v in pair]
    interior_seconds = time.perf_counter() - interior_start

    record = {
        'status': 'PASS', 'date': '2026-10-13', 'prepared_for': 'Edward Baker',
        'acknowledgment': 'Substantial LLM assistance; internal outward certificate, not independent validation.',
        'model': 'gpt-6-astra', 'reasoning_effort': 'ultra',
        'arithmetic': f'{PRECISION}-digit outward Decimal; patched repeated integer powers; rigorous trig Taylor and rotation',
        'python_version': platform.python_version(),
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'retained_inputs': {str(p.relative_to(ROOT)): h for p, h in SOURCES.items()},
        'domain': {'time': ['0', '0.05'], 'space': ['8', '12']},
        'source': 'Full half-line theta integral; n=1..3 plus positive geometric n>=4 enclosure in every u cell',
        'integration': {
            'u_radius': '1', 'u_cells': args.u_cells,
            'shared_density_interval_evaluations': args.u_cells,
            'explicit_finite_theta_terms': 3 * args.u_cells,
            'u_tail_bounds_j0_to_j3': [str(v.hi) for v in tails],
            'time_boxes_in_payment_order': [list(key) for key in boundary.weights],
            'n_tail_bounds_by_time_box_j0_to_j3': boundary.omitted_payments,
            'absolute_jet_bounds_by_time_box_j0_to_j3': boundary.absolute_moments,
            'quadrature': 'Interval Riemann integration over each closed u cell, no sampled-value quadrature assumption',
            'parameter_variation': 'Full time intervals in positive heat weights; full spatial intervals in rigorous trig Lipschitz pads',
            'cutoff_crossings': 'None: fixed source integration cutoff u=1; no height-dependent natural cutoff or complex carrier',
        },
        'boundary': {'winding': 0, 'homotopy': 'Every side has Hx<0; straight homotopy to -i',
                     'orientation': 'counterclockwise in (time,space)',
                     'pair_integrals': boundary.calls, 'heat_weight_builds': len(boundary.weights),
                     'segments': boundary_records, 'runtime_seconds': boundary_seconds},
        'interior': {'joint_zero_excluded': True, 'method': 'One complete physical value-and-slope interval box; Hx<0',
                     'pair_integrals': interior.calls, 'heat_weight_builds': len(interior.weights),
                     'H_Hx': [v.strings() for v in pair],
                     'norm_lower_bound': str(pair[1].hi.copy_negate()), 'runtime_seconds': interior_seconds},
        'shared_density_preparation_seconds': preparation_seconds,
        'gate': 'NO GO for expanded winding campaign on this evidence: four boundary pair integrals versus one interior pair integral, same arithmetic and tails',
        'limitations': ['Easy calibration rectangle selected from the existing unconditional low-height atlas.',
                        'This does not compare optimized implementations or asymptotic complexity.',
                        'The earlier 80-cell record certified stronger Hxx/Hxxx stationary information; its cell count is not a fair joint-zero cost baseline.',
                        'No difficult-cell improvement, global boundary identity, unbounded-height coverage, or RH consequence.'],
    }
    if args.record:
        args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: record[k] for k in ('status', 'boundary', 'interior', 'gate')}, indent=2))


if __name__ == '__main__':
    main()
