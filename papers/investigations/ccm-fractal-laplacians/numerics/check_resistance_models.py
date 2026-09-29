#!/usr/bin/env python3
"""Exact controls for CCM/fractal proposals; no CCM or zeta-zero fitting.

Python standard library only. Graph algebra uses Fraction, counts use integers.
Decimal at 32/64 digits checks the sensitivity of displayed diagnostics only.
The accompanying note supplies the infinite-dimensional proofs.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform


def zeros(n, m):
    return [[Q(0) for _ in range(m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    bt = transpose(b)
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in bt] for row in a]


def add(a, b, factor=Q(1)):
    return [[x + factor*y for x, y in zip(ar, br)]
            for ar, br in zip(a, b)]


def scale(a, factor):
    return [[factor*x for x in row] for row in a]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    aug = [row[:] + eye for row, eye in zip(a, identity(n))]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        divisor = aug[k][k]
        aug[k] = [x/divisor for x in aug[k]]
        for i in range(n):
            if i != k:
                c = aug[i][k]
                aug[i] = [x-c*y for x, y in zip(aug[i], aug[k])]
    result = [row[n:] for row in aug]
    assert mul(a, result) == identity(n)
    return result


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def max_abs(a):
    return max(abs(x) for row in a for x in row)


def trace(a):
    return sum((row[i] for i, row in enumerate(a)), Q(0))


def gasket(level):
    anchors = ((Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1)))
    cells = [anchors]
    for _ in range(level):
        cells = [tuple(((p[0]+v[0])/2, (p[1]+v[1])/2) for p in cell)
                 for v in anchors for cell in cells]
    vertices = sorted({p for cell in cells for p in cell})
    indices = {p: i for i, p in enumerate(vertices)}
    edges = {tuple(sorted((indices[cell[i]], indices[cell[j]])))
             for cell in cells for i, j in ((0, 1), (0, 2), (1, 2))}
    k = zeros(len(vertices), len(vertices))
    conductance = Q(5, 3)**level
    for i, j in edges:
        k[i][i] += conductance
        k[j][j] += conductance
        k[i][j] -= conductance
        k[j][i] -= conductance
    return vertices, k, len(edges)


def schur(k, boundary):
    interior = [i for i in range(len(k)) if i not in boundary]
    a = block(k, boundary, boundary)
    b = block(k, boundary, interior)
    c = block(k, interior, interior)
    return add(a, mul(mul(b, inverse(c)), transpose(b)), Q(-1))


def graph_controls():
    levels = []
    for level in range(3):
        vertices, k, edges = gasket(level)
        free = [i for i, p in enumerate(vertices) if p != (Q(0), Q(0))]
        inv = inverse(block(k, free, free))
        # Unit total mass on ungrounded vertices, for this discrete control.
        tau = trace(inv)/len(free)
        maximum_resistance = max(inv[i][i] for i in range(len(free)))
        assert tau <= maximum_resistance
        levels.append(dict(level=level, vertices=len(vertices), edges=edges,
                           inverse_trace=str(tau),
                           maximum_ground_resistance=str(maximum_resistance)))
    compatibility = []
    for level in range(2):
        vc, kc, _ = gasket(level)
        vf, kf, _ = gasket(level+1)
        boundary = [vf.index(p) for p in vc]
        error = max_abs(add(schur(kf, boundary), kc, Q(-1)))
        assert error == 0
        compatibility.append(dict(coarse_level=level, fine_level=level+1,
                                  max_schur_error=str(error)))

    vc, _, _ = gasket(0)
    vf, k, _ = gasket(1)
    boundary = [vf.index(p) for p in vc]
    interior = [i for i in range(len(k)) if i not in boundary]
    a = block(k, boundary, boundary)
    b = block(k, boundary, interior)
    c = block(k, interior, interior)
    ci = inverse(c)
    mb = scale(identity(3), Q(1, 6))
    mi = scale(identity(3), Q(1, 6))
    effective_mass = add(mb, mul(mul(mul(mul(b, ci), mi), ci), transpose(b)))
    static = add(a, mul(mul(b, ci), transpose(b)), Q(-1))
    t = Q(1, 7)
    dynamic = add(add(a, mb, -t),
                  mul(mul(b, inverse(add(c, mi, -t))), transpose(b)), Q(-1))
    residual = add(add(dynamic, static, Q(-1)), effective_mass, t)
    assert max_abs(residual) > 0
    # Control: massless interior makes the dynamic reduction exactly linear.
    massless_dynamic = add(add(a, mb, -t), mul(mul(b, ci), transpose(b)), Q(-1))
    massless_residual = add(add(massless_dynamic, static, Q(-1)), mb, t)
    assert max_abs(massless_residual) == 0
    return dict(levels=levels, harmonic_compatibility=compatibility,
                dynamic_reduction=dict(t=str(t),
                    effective_mass=[[str(x) for x in row] for row in effective_mass],
                    max_nonlinear_remainder=str(max_abs(residual)),
                    massless_interior_remainder=str(max_abs(massless_residual))))


def divisor_count(x):
    """Number of positive integer pairs n*m <= x, by hyperbola symmetry."""
    m = isqrt(x)
    return 2*sum(x//j for j in range(1, m+1)) - m*m


def odd_count(x):
    return divisor_count(x) - divisor_count(x//2)


def arm_count(x, branches):
    """At frequency T=pi*x/2, count n*(2*k+1) <= x on retained arms."""
    return sum((x//n+1)//2 for n in range(1, min(x, branches)+1))


def counts_and_moments():
    # Independent direct count checks the fast divisor formula at every x.
    for x in range(1, 501):
        assert odd_count(x) == arm_count(x, x)
    counts = [dict(x=x, frequency="pi*x/2", full_count=odd_count(x),
                   branch_cutoffs={str(b): arm_count(x, b) for b in (4, 16, 64)})
              for x in (10, 100, 1000, 10000, 100000, 1000000)]
    moments = []
    for b in (1, 4, 16, 64, 256):
        tau = sum((Q(1, 2*n*n) for n in range(1, b+1)), Q(0))
        moments.append(dict(branches=b, inverse_trace=str(tau),
                            missing_trace_lower=str(Q(1, 2*(b+1))),
                            missing_trace_upper=str(Q(1, 2*b))))
    return counts, moments


def fourier_compression_controls():
    """Rational parity-diagonal surrogates, not actual Weil forms.

    Set d_n=n. In the normalized parity basis the square roots in J cancel
    from the mass Gram matrix because T_plus is diagonal.
    """
    def forms(wp, wm):
        epsilon = min(wp + wm)
        assert wp.count(epsilon) == 1 and epsilon not in wm
        n = len(wm)
        k = [[Q(wm[i]-epsilon) if i == j else Q(0)
              for j in range(n)] for i in range(n)]
        mass = [[Q(2*(wp[0]-epsilon), (i+1)*(j+1)) +
                 (Q(wp[i+1]-epsilon, (i+1)**2) if i == j else Q(0))
                 for j in range(n)] for i in range(n)]
        return epsilon, k, mass

    e0, k0, m0 = forms([-1, 3], [2])
    result = []
    for label, even in [('stable_ground', [-1, 3, 5]),
                        ('lower_added_even_mode', [-1, 3, -2])]:
        ef, kf, mf = forms(even, [2, 6])
        delta = Q(e0-ef)
        kd, md = kf[0][0]-k0[0][0], mf[0][0]-m0[0][0]
        # For one retained mode, J^*J = 1 + 2 = 3.
        assert kd == delta and md == 3*delta
        result.append(dict(case=label, epsilon_change=str(delta),
                           stiffness_compression_defect=str(kd),
                           mass_compression_defect=str(md)))
    return result


def displayed_diagnostics(counts, moments, digits):
    with localcontext() as ctx:
        ctx.prec = digits
        values = {}
        for row in counts:
            x = Decimal(row['x'])
            # N(T) / ((T/pi)*log(2*T/pi)) tends to one.
            values['count_ratio_x'+str(row['x'])] = Decimal(row['full_count'])/(x*x.ln()/2)
        for row in moments:
            q = Q(row['inverse_trace'])
            values['trace_B'+str(row['branches'])] = Decimal(q.numerator)/Decimal(q.denominator)
        return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    graphs = graph_controls()
    counts, moments = counts_and_moments()
    low = displayed_diagnostics(counts, moments, 32)
    high = displayed_diagnostics(counts, moments, 64)
    assert all(format(low[key], '.24g') == format(high[key], '.24g') for key in low)
    with localcontext() as ctx:
        ctx.prec = 70
        max_delta = max(abs(low[key]-high[key]) for key in low)
    record = dict(
        schema=1, date='2026-09-26',
        model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
        status='Exact finite controls; not a CCM embedding or an RH computation',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        python=platform.python_version(),
        dependencies='Python standard library only',
        arithmetic='Fraction/integer for all identities and counts; Decimal for display',
        zero_data_used=False, full_matrices_saved=False,
        gasket=graphs, shrinking_star_counts=counts, shrinking_star_traces=moments,
        fourier_compression_surrogates=fourier_compression_controls(),
        precision_check=dict(decimal_digits=[32, 64], retained_significant_digits=24,
                             observables=len(low), all_retained_digits_agree=True,
                             maximum_absolute_difference=str(max_delta)),
        diagnostics={key: format(value, '.24g') for key, value in high.items()})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(dict(record=str(args.output), exact_controls='passed',
                          decimal_checks=len(low), max_decimal_delta=str(max_delta))))


if __name__ == '__main__':
    main()
