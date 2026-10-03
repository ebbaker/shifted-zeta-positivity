#!/usr/bin/env python3
"""Outward full-source Weil bound with signed or capped frequency integrals.

Prepared for Edward Baker, 2026-10-03, with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort not exposed.
All matrices are regenerated, not persisted. See this directory's README.
"""
import argparse
import hashlib
import json
import platform
import time
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, arb, arb_mat, ctx


def ball(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def pack(value):
    if not value.is_finite():
        raise ArithmeticError('Non-finite enclosure')
    return {'lower': str(value.lower().fmpq()), 'upper': str(value.upper().fmpq())}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ldl_positive(matrix):
    n = matrix.nrows()
    lower = arb_mat(n, n)
    pivots = []
    for j in range(n):
        pivot = matrix[j, j] - sum(
            (lower[j, k] ** 2 * pivots[k] for k in range(j)), arb(0))
        if not pivot > 0:
            raise ArithmeticError(f'Unproved positive LDL pivot {j}')
        pivots.append(pivot)
        lower[j, j] = 1
        for i in range(j + 1, n):
            lower[i, j] = (matrix[i, j] - sum(
                (lower[i, k] * lower[j, k] * pivots[k] for k in range(j)), arb(0))) / pivot
    return min(p.lower() for p in pivots)


def plane_tail(rank, z):
    denominator = 1
    for j in range(rank + 1):
        denominator *= 2 * j + 1
    ratio = z * z / ((2 * rank + 1) * (2 * rank + 3))
    if not ratio < 1:
        raise ArithmeticError('Unproved Legendre tail ratio')
    return ((2 * rank + 1) * z ** (2 * rank) /
            (denominator ** 2 * (1 - ratio))).sqrt()


def active_prime_powers(length):
    """Enumerate ALL active powers, proving each threshold comparison in Arb."""
    maximum = int(length.exp().upper().ceil().fmpq())
    primes = [p for p in range(2, maximum + 1)
              if all(p % d for d in range(2, int(p ** 0.5) + 1))]
    active = []
    for prime in primes:
        power, exponent = prime, 1
        while power <= maximum:
            delay = arb(power).log()
            if delay < length:
                active.append((prime, exponent, delay,
                               2 * arb(prime).log() / arb(power).sqrt()))
            elif not delay > length:
                raise ArithmeticError('Unresolved prime-power endpoint')
            power *= prime
            exponent += 1
    return active


def inherited_binding():
    record_path = Path(__file__).resolve().parent.parent / 'local_weil_gap_20261003/inherited_gap_replay.json'
    record = json.loads(record_path.read_text())
    root = next(p for p in Path(__file__).resolve().parents if (p / 'LARGE_FILES.md').is_file())
    generator = root / record['generator_repo_path']
    if (record['status'] != 'INHERITED_GAP_REBUILT' or
            record['gap'] != '57/1000000' or digest(generator) != record['generator_sha256']):
        raise ArithmeticError('Inherited prolate binding mismatch')
    return {'record_sha256': digest(record_path),
            'generator_repo_path': record['generator_repo_path'],
            'generator_sha256': record['generator_sha256'],
            'gap': record['gap'],
            'scope': 'Reuses earlier outward prolate proof; hash checks input identity only.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--length', default='6/5')
    parser.add_argument('--lambda', dest='level', default='1/2')
    parser.add_argument('--cutoff', default='100')
    parser.add_argument('--rank', type=int, default=100)
    parser.add_argument('--nodes', type=int, default=30000)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--matrix-cap', default='249/500')
    parser.add_argument('--error-cap', default='1/2000')
    parser.add_argument('--correction-cap', default='3458')
    parser.add_argument('--method', choices=['signed', 'capped'], default='signed')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.rank < 4 or args.rank % 2 or args.nodes <= 0 or args.bits < 96:
        parser.error('Require even rank >=4, positive nodes, and precision >=96')
    # Explicit session resource envelope; this program never expands it automatically.
    if (not 0 < Fraction(args.length) <= Fraction(6, 5) or args.rank > 192 or
            args.nodes > 80000 or not 0 < Fraction(args.cutoff) <= 200 or args.bits > 384):
        parser.error('Outside bounded experiment: L<=6/5, rank<=192, nodes<=80000, T<=200, bits<=384')
    ctx.prec = args.bits
    start = time.time()
    length, level, cutoff = map(ball, (args.length, args.level, args.cutoff))
    cap, error_cap, correction_cap = map(ball, (args.matrix_cap, args.error_cap, args.correction_cap))
    if not cap >= 0 or not error_cap > 0 or not level - cap - error_cap > 0 or not correction_cap > 0:
        parser.error('Require nonnegative matrix cap and positive error, gap, and correction caps')
    binding = inherited_binding()
    pi, rank, nodes = arb.pi(), args.rank, args.nodes
    step = cutoff / nodes
    active = active_prime_powers(length)
    amplitude = sum((row[3] for row in active), arb(0))
    gamma0 = acb(arb(1) / 4).digamma().real - pi.log()
    gammaT = acb(arb(1) / 4, cutoff / 2).digamma().real - pi.log()
    cutoff_margin = gammaT - level - amplitude
    if not cutoff_margin > 0:
        raise ArithmeticError('Frequency tail is not proved above lambda')
    # Fix {2,3} even on smaller windows; B and K depend on this representation.
    if any(row[0] not in (2, 3) for row in active):
        raise ArithmeticError('Fixed representation does not capture active primes')
    beta, z = length / 2, length / 4
    sh, ch = z.sinh(), z.cosh()
    mean = sh / z
    ns = beta.sinh() / length - arb(1) / 2
    nc = beta.sinh() / length + arb(1) / 2 - mean ** 2
    if not ns > 0 or not nc > 0:
        raise ArithmeticError('Moment norms unproved')
    fac, us, uc = [], [], []
    denominator = 1
    for j in range(rank):
        if j:
            denominator *= 2 * j + 1
        common = arb(2 * j + 1).sqrt() / denominator
        fac.append(common * (-1) ** (j // 2))
        moment = common * z ** j * (z * z / 4).hypgeom_0f1(arb(j) + arb(3) / 2)
        us.append(moment / ns.sqrt() if j % 2 else arb(0))
        uc.append(moment / nc.sqrt() if j > 0 and j % 2 == 0 else arb(0))
    mats = [arb_mat(rank // 2, rank // 2), arb_mat(rank // 2, rank // 2)]
    panels, weights = [[], []], []
    absolute_midpoint_mass = arb(0)
    used = 0

    def flush():
        nonlocal panels, weights
        if not weights:
            return
        for parity in (0, 1):
            left = arb_mat([[panels[parity][k][j] * weights[k] for k in range(len(weights))]
                            for j in range(rank // 2)])
            right = arb_mat([[panels[parity][k][j] for k in range(len(weights))]
                             for j in range(rank // 2)])
            mats[parity] += left * right.transpose()
        panels, weights = [[], []], []

    for cell in range(nodes):
        t = cutoff * (2 * cell + 1) / (2 * nodes)
        gamma = acb(arb(1) / 4, t / 2).digamma().real - pi.log()
        weight = level - gamma + sum((c * (a * t).cos() for _, _, a, c in active), arb(0))
        if args.method == 'capped':
            if weight.upper() <= 0:
                continue
            if weight.lower() < 0:
                upper = weight.upper()
                weight = arb(upper / 2, upper / 2)
        absolute_midpoint_mass += step * abs(weight)
        k = length * t
        v = k / 2
        sinc = v.sin() / v
        bs = 2 * (beta * ch * v.sin() - k * sh * v.cos()) / (beta ** 2 + k ** 2)
        bc = 2 * (beta * sh * v.cos() + k * ch * v.sin()) / (beta ** 2 + k ** 2)
        odd = bs / ns.sqrt()
        even = (bc - mean * sinc) / nc.sqrt()
        vals, power = [], arb(1)
        for j in range(rank):
            raw = fac[j] * power * (-v * v / 4).hypgeom_0f1(arb(j) + arb(3) / 2)
            vals.append(raw - us[j] * odd - uc[j] * even if j else arb(0))
            power *= v
        panels[0].append(vals[::2])
        panels[1].append(vals[1::2])
        weights.append(length * step * weight / pi)
        used += 1
        if len(weights) >= 128:
            flush()
        if (cell + 1) % 10000 == 0:
            print(json.dumps({'node': cell + 1, 'seconds': time.time() - start}), flush=True)
    flush()
    pivots = [ldl_positive(arb_mat([[cap * (i == j) - mat[i, j]
                                   for j in range(rank // 2)] for i in range(rank // 2)]))
              for mat in mats]
    variation1 = gammaT - gamma0 + cutoff * sum((c * a for _, _, a, c in active), arb(0))
    mass_bound = absolute_midpoint_mass + step * variation1 / 2
    variation2 = 15 * arb(3).sqrt() / 2 + cutoff * sum((c * a * a for _, _, a, c in active), arb(0))
    second_derivative_mass = (variation2 + 2 * length / arb(3).sqrt() * variation1 +
                              length ** 2 * (1 / arb(20).sqrt() + arb(1) / 6) * mass_bound)
    if args.method == 'signed':
        quadrature = length * step ** 2 / (8 * pi) * second_derivative_mass
    else:
        quadrature = length * step / (2 * pi) * (variation1 + length / arb(3).sqrt() * mass_bound)
    tail = (plane_tail(rank, length * cutoff / 2) + z.exp() * plane_tail(rank, z) *
            (1 / ns.sqrt() + 1 / nc.sqrt()))
    truncation = 2 * length * tail * mass_bound / pi
    error = quadrature + truncation
    if not error < error_cap:
        raise ArithmeticError(f'Remainder budget exceeded: {error}')
    g = ball(binding['gap'])
    for prime in (2, 3):
        rho = 1 / arb(prime).sqrt()
        g *= ((1 - rho) / (1 + rho)) ** 2
    correction = length * ((1 - g) / g).sqrt()
    if not correction < correction_cap:
        raise ArithmeticError('Correction cap unproved')
    delta = Fraction(args.level) - Fraction(args.matrix_cap) - Fraction(args.error_cap)
    theta = delta / (Fraction(args.correction_cap) + delta)
    payload = [[[pack(mat[i, j]) for j in range(rank // 2)] for i in range(rank // 2)] for mat in mats]
    result = {
        'status': 'CERTIFIED_FULL_SOURCE_WEIL_GAP', 'date': '2026-10-03',
        'model': 'GPT-6 (Codex)', 'serving_variant': 'not exposed', 'reasoning_effort': 'not exposed',
        'length': args.length, 'lambda': args.level, 'cutoff': args.cutoff,
        'rank': rank, 'nodes': nodes, 'bits': args.bits, 'method': args.method,
        'constraints': ['mean', 'exp(x/2)', 'exp(-x/2)'], 'representation_primes': [2, 3],
        'active_prime_powers': [{'prime': p, 'exponent': m} for p, m, _, _ in active],
        'matrix_cap': args.matrix_cap, 'error_cap': args.error_cap,
        'Q_norm_gap': str(delta), 'correction_norm_cap': args.correction_cap,
        'retained_B_fraction': str(theta), 'relative_K_upper_fraction': str(1 - theta),
        'parity_LDL_min_pivots': [pack(pivot) for pivot in pivots],
        'frequency_cutoff_margin': pack(cutoff_margin), 'absolute_amplitude': pack(amplitude),
        'absolute_midpoint_mass': pack(absolute_midpoint_mass), 'absolute_mass_bound': pack(mass_bound),
        'weight_variation_bound': pack(variation1), 'weight_second_derivative_mass_bound': pack(variation2),
        'integrand_second_derivative_mass_bound': pack(second_derivative_mass),
        'quadrature_error_bound': pack(quadrature), 'projected_plane_tail_bound': pack(tail),
        'truncation_error_bound': pack(truncation), 'total_error_bound': pack(error),
        'transported_boundary_gap': pack(g), 'correction_norm_evaluation': pack(correction),
        'inherited_prolate_binding': binding,
        'script_sha256': digest(Path(__file__)),
        'matrix_enclosure_sha256': hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'seconds': time.time() - start, 'used_nodes': used,
        'runtime': {'python': platform.python_version(), 'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__},
        'limitations': ['Only the stated bounded window and three moments are certified.',
                        'No all-window estimate or unweighted K_plus domination follows.',
                        'Relative B conclusion reuses the separately certified prolate gap.']}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ('status', 'Q_norm_gap', 'retained_B_fraction', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
