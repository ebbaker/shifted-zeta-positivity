#!/usr/bin/env python3
"""Exact diagnostic ledgers for Note 28's remaining form; no analytic proof.

Standard library only. Output is deterministic JSON. Serving model/effort are
not inferable from the process. Native arithmetic and analytic inputs remain
conditional. The finite character below is a formal monoid character only.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json

COUNTS = defaultdict(int)


def check(condition, group):
    COUNTS[group] += 1
    if not condition:
        raise AssertionError(group)


def fmt(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): fmt(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [fmt(v) for v in value]
    return value


D = (F(9, 25), F(21, 50))
R = (F(7, 10), F(73, 100))
M = (F(2, 5), F(207, 500))
Z = (F(0), F(2, 45))
V = F(1, 5000)
DELTA = F(3, 4) + 2 * V
CORNERS = list(product(D, R, M, Z))
SLOPES = (4, 10, 6, 9)


def cuts(d, r, m, z):
    l = r + z
    k1 = m + F(2, 3) * d * r - F(1, 750)
    ksf = F(1, 2) + (F(3, 5) * d - F(1, 2)) * r - z / 2 + F(9, 10) * m - F(3, 2500)
    return l, k1, ksf


def theta(alpha, l):
    return max(alpha, l, 5 * alpha / 6 + l / 3, alpha / 3 + 5 * l / 6)


def count_and_mass(k, lam, eta, l):
    alpha, physical = k - lam, k + 4 * lam - eta
    count = lam + (1 - physical) / 6
    return alpha, physical, count, count + theta(alpha, l)


def audit_frontier():
    witnesses = []
    for d, r, m, z in CORNERS:
        l, k1, ksf = cuts(d, r, m, z)
        check(k1 >= F(17, 30), "frontier_corners")
        check(ksf < l and ksf < 2 * m and ksf < 4 * m - F(1, 2), "frontier_corners")
        # The exact full-theta formula for alpha <= 1 < 2*l.
        for k in (k1, ksf, (k1 + ksf) / 2, F(4, 5), F(1)):
            for lam in (F(0), (1 - k) / 4, (1 - k) / 2, 1 - k):
                low = max(F(0), k + 4 * lam - 1)
                high = 3 * lam
                for eta in (low, (low + high) / 2, high):
                    alpha, phys, count, mass = count_and_mass(k, lam, eta, l)
                    check(0 <= alpha <= 1 and phys <= 1 and 0 <= eta <= 3 * lam, "full_theta_feasible")
                    formula = F(1, 6) + k / 6 + eta / 6 + max(l - alpha / 3, 5 * l / 6, alpha / 2 + l / 3)
                    check(mass == formula, "full_theta_identity")
                    # Every feasible aggregate has an exact type-2/type-5 realization.
                    g1, g2, g5 = alpha, eta / 3, lam - eta / 3
                    check(g1 >= 0 and g2 >= 0 and g5 >= 0, "all_gamma_reduction")
                    check(g1 + g2 + g5 == k and g1 + 2 * g2 + 5 * g5 == phys, "all_gamma_reduction")
                    rho = alpha + count
                    check(rho == k + (1 - phys) / 6 and rho >= k, "physical_support_count")
                    if k <= ksf:
                        penalty = max(F(0), l - 2 * alpha)
                        check(mass == F(1, 6) + k / 6 + 5 * l / 6 + (eta + penalty) / 6, "frontier_penalty")
                        nominal = mass + F(3, 2) * (k - m)
                        check(nominal == 1 + d * r - F(1, 500) + F(5, 3) * (k + (eta + penalty) / 10 - ksf), "frontier_cancellation")
                        if k + (eta + penalty) / 10 <= ksf:
                            check(nominal <= 1 + d * r - F(1, 500), "frontier_bound")
                            check(4 * V * (k - m) <= F(3, 12500), "frontier_contour")
    # Two concrete feasible rows omitted by Note28's eta<=.15 condition.
    d, r, m, z = F(39, 100), F(71, 100), F(81, 200), F(1, 50)
    l, k1, ksf = cuts(d, r, m, z)
    for k, lam, eta in ((F(3, 5), F(1, 10), F(1, 5)), (F(3, 5), F(49, 200), F(117, 200))):
        alpha, phys, count, mass = count_and_mass(k, lam, eta, l)
        frontier = k + (eta + max(F(0), l - 2 * alpha)) / 10
        check(k > k1 and eta > F(3, 20) and phys <= 1 and eta <= 3 * lam, "new_sector_witness")
        check(frontier < ksf, "new_sector_witness")
        witnesses.append(dict(kappa=k, radical_h=lam, defect=eta, alpha=alpha, physical=phys, frontier=frontier, kappa_sf=ksf))
    # Corrected low-radius example printed in Note29, including its physical w.
    d, r, m, z = F(21, 50), F(73, 100), F(2, 5), F(0)
    l, k1, ksf = cuts(d, r, m, z)
    k, lam, eta, alpha, theta_h, omega = F(151, 250), F(6, 25), F(18, 25), F(91, 250), F(12, 25), F(13, 500)
    a, physical, count, mass = count_and_mass(k, lam, eta, l)
    frontier = k + (eta + max(F(0), l - 2 * alpha)) / 10
    check(a == alpha and alpha < l / 2 and k > k1, "note29_corrected_low_radius_witness")
    check(5 * lam - eta == theta_h and alpha + theta_h + 6 * omega == 1, "note29_corrected_low_radius_witness")
    check(frontier == F(3381, 5000) and ksf == F(2118, 3125) and frontier < ksf, "note29_corrected_low_radius_witness")
    witnesses.append(dict(d=d, r=r, m=m, z=z, kappa=k, radical_h=lam, defect=eta, alpha=alpha, theta_h=theta_h,
                          physical=physical, physical_sixth_root_exponent=omega, frontier=frontier, kappa_sf=ksf))
    check(F(1, 500) - F(3, 12500) == F(11, 6250), "reserve")
    check(F(11, 6250) - F(1, 700) == F(29, 87500), "reserve")
    return dict(formula="kappa+(eta+(l-2alpha)_+)/10<=kappa_sf; alpha=kappa-lambda; no eta cap",
                physical_polytope="0<=lambda<=1-kappa; max(0,kappa+4lambda-1)<=eta<=3lambda",
                contour_cost_max=F(3, 12500), final_saving=F(11, 6250), target_reserve=F(29, 87500), witnesses=witnesses)


def audit_tail():
    native_reserves, scalar_reserves = [], []
    native_requirements, scalar_requirements = [], []
    native_branches, scalar_branches = [], []
    for d, r, m, z in CORNERS:
        l, k1, ksf = cuts(d, r, m, z)
        x, omega = r + 2 * m + z, (1 - k1) / 6
        bases = (F(1), x + omega, F(5, 6) + x / 3, F(1, 3) + 5 * x / 6)
        target = 1 + d * r - F(1, 500)
        scalar = 1 + DELTA * r
        for i, bfull in enumerate(bases):
            for j, (btail, slope) in enumerate(zip(bases, SLOPES)):
                gap = target - (bfull + btail - slope * F(1, 10)) / 2
                check(gap >= F(5519, 135000), "native_tail_16_branches")
                native_branches.append((gap, (d, r, m, z), i, j))
        for j, (btail, slope) in enumerate(zip(bases, SLOPES)):
            gap = target - (scalar + btail - slope * F(2, 25)) / 2
            check(gap >= F(84727, 6750000), "scalar_tail_4_branches")
            scalar_branches.append((gap, (d, r, m, z), j))
        b0 = max(bases)
        native_reserves.append(target - (b0 + max(b - s * F(1, 10) for b, s in zip(bases, SLOPES))) / 2)
        scalar_reserves.append(target - (scalar + max(b - s * F(2, 25) for b, s in zip(bases, SLOPES))) / 2)
        native_requirements.append(max((b0 + b - 2 * target) / s for b, s in zip(bases, SLOPES)))
        scalar_requirements.append(max((scalar + b - 2 * target) / s for b, s in zip(bases, SLOPES)))
    check(min(native_reserves) == F(5519, 135000), "native_tail_extrema")
    check(max(native_requirements) == F(55231, 607500), "native_tail_extrema")
    check(min(scalar_reserves) == F(84727, 6750000), "scalar_tail_extrema")
    check(max(scalar_requirements) == F(2345273, 30375000), "scalar_tail_extrema")
    return dict(x="r+2m+z", omega="(1-kappa1)/6", bases="1,x+omega,5/6+x/3,1/3+5x/6", slopes=SLOPES,
                native=dict(sigma=F(1, 10), minimum_sigma=F(55231, 607500), nominal_reserve=min(native_reserves), worst=min(native_branches)),
                scalar=dict(sigma=F(2, 25), minimum_sigma=F(2345273, 30375000), nominal_reserve=min(scalar_reserves), worst=min(scalar_branches),
                            extra_scope="Note27 Lemma18.1 coefficient class, original slot mesh, nonexceptional rows, and 2m+(9/2)z<1; not supplied by the coarse box"))


def audit_envelopes():
    worst = []
    count_deficits = []
    for d, r, m, z in CORNERS:
        l, k1, ksf = cuts(d, r, m, z)
        # Worst marked sieve for fixed k: achieved by pure valuation-2 physical cores.
        points = {k1, F(1), F(1, 2) + l / 4, F(1, 2) + l / 2, 2 * m}
        for k in sorted(p for p in points if k1 <= p <= 1):
            alpha, phys, count, mass = count_and_mass(k, 1 - k, 3 * (1 - k), l)
            if k <= F(1, 2) + l / 4:
                exact = 1 - k + l
            elif k <= F(1, 2) + l / 2:
                exact = F(2, 3) - k / 3 + 5 * l / 6
            else:
                exact = F(1, 6) + 2 * k / 3 + l / 3
            check(mass == exact, "worst_core_piecewise")
            plain = 2 * DELTA * min(m, k - m)
            correction = DELTA * (min(F(1, 4), k - F(1, 4)) + min(2 * m - F(1, 4), k - 2 * m + F(1, 4)))
            check(correction <= plain, "plain_branch_full_physical_range")
        # Pointwise inverse + trivial slots + sharper physical row count.
        target = 1 + d * r - F(1, 500)
        minimum_count_bound = k1 + F(3, 4) * r + z + F(3, 2) * (k1 - m)
        deficit = minimum_count_bound - target
        count_deficits.append(deficit)
        check(deficit >= F(11, 120), "count_route_obstruction")
        # A residual point where every independently available envelope fails.
        k, lam, eta = F(1), F(0), F(0)
        alpha, phys, count, mass = count_and_mass(k, lam, eta, l)
        plain = 2 * DELTA * m
        scalar = 1 + DELTA * r
        best = min(mass + plain, 1 + plain, 1 + DELTA * r + z + plain, scalar)
        check(best == scalar and k > k1 and k > ksf, "uniform_scalar_witness")
        worst.append((best, d, r, m, z))
    check(min(count_deficits) == F(11, 120), "count_route_obstruction")
    return dict(worst_marked_mass="1-kappa+l below .5+l/4; 2/3-kappa/3+5l/6 through .5+l/2; 1/6+2kappa/3+l/3 above",
                actual_count="rho=kappa+(1-physical_core_exponent)/6>=kappa",
                minimum_count_deficit=F(11, 120), best_uniform_scalar_exponent=max(worst)[0],
                obstruction="kappa=1, gamma1=1, other gamma_e=0: no available independent-envelope interpolation improves 1+delta_g*r; not a lower bound for the signed form")


# Exact Q(sqrt(-3)) complex arithmetic: a+b*sqrt(-3).
def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def mul(z, w):
    return (z[0] * w[0] - 3 * z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def conj(z):
    return (z[0], -z[1])


def scale(c, z):
    return (c * z[0], c * z[1])


def norm(z):
    return z[0] ** 2 + 3 * z[1] ** 2


ZERO, ONE = (F(0), F(0)), (F(1), F(0))
ROOTS = [ONE]
for _ in range(5):
    ROOTS.append(mul(ROOTS[-1], (F(1, 2), F(1, 2))))
PRIMES = (2, 3, 5)


def ideal_norm(exponents):
    n = 1
    for p, e in zip(PRIMES, exponents):
        n *= p ** e
    return n


def ideals(cap):
    return sorted((e for e in product(range(7), repeat=3) if ideal_norm(e) <= cap), key=lambda e: (ideal_norm(e), e))


def psi(u, k):
    if any(a and b for a, b in zip(u, k)):
        return ZERO
    mat = ((0, 1, 2), (3, 0, 1), (1, 2, 0))
    exponent = sum(u[i] * mat[i][j] * k[j] for i in range(3) for j in range(3))
    if len(u) == 4:
        exponent += u[3] * sum((j + 1) * k[j] for j in range(3))
    return ROOTS[exponent % 6]


def profile(t):
    if t <= F(1, 2) or t >= 2:
        return F(0)
    return 2 * t - 1 if t <= 1 else 2 - t


def audit_full_coefficient():
    # Actual original Mobius and equal-product centered rectangles, one original slot.
    d, n, y1, y2, pslot = 6, 12, 6, 24, 5
    x = d * n * n * pslot
    plain_ideals = ideals(48)
    inverse_ideals = [e for e in ideals(12) if max(e) <= 1]
    coefficients = defaultdict(F)
    tuples = []
    for inv, a, b in product(inverse_ideals, plain_ideals, plain_ideals):
        ai = (-1) ** sum(inv) * profile(F(ideal_norm(inv), d))
        center = profile(F(ideal_norm(a), n)) * profile(F(ideal_norm(b), n)) - profile(F(ideal_norm(a), y1)) * profile(F(ideal_norm(b), y2))
        coefficient = ai * center
        if coefficient:
            k = tuple(inv[i] + a[i] + b[i] + (i == 2) for i in range(3))
            coefficients[k] += coefficient
            tuples.append((inv, a, b, coefficient, k))
    coefficients = {k: a for k, a in coefficients.items() if a}
    rows = list(product(range(3), repeat=4)) + [(6, 0, 0, 0), (0, 6, 0, 0), (0, 0, 6, 0)]
    # A sharp arbitrary predicate with nonuniform nonnegative row weights.
    weights = {u: (1 + sum(u) % 3) if 15 <= ideal_norm(u[:3]) * 7 ** u[3] <= 300 and sum(e % 6 for e in u) else 0 for u in rows}
    full_energy = head_energy = tail_energy = F(0)
    full_tail = ZERO
    tail_columns = [k for k in coefficients if ideal_norm(tuple(e // 6 for e in k)) >= 2]
    physical_mask_witnesses = 0
    for u in rows:
        full = head = tail = ZERO
        unfolded = ZERO
        for inv, a, b, coefficient, k in tuples:
            raw = mul(mul(psi(u, inv), psi(u, a)), mul(psi(u, b), psi(u, (0, 0, 1))))
            unfolded = add(unfolded, scale(coefficient, raw))
        for k, coefficient in coefficients.items():
            term = scale(coefficient, psi(u, k))
            core, power = tuple(e % 6 for e in k), tuple(e // 6 for e in k)
            mask = int(not any(a and b for a, b in zip(u, power)))
            extracted = scale(mask, psi(u, core))
            check(extracted == psi(u, k), "full_sixth_extraction_mask")
            if not mask and norm(psi(u, core)):
                physical_mask_witnesses += 1
            full = add(full, term)
            if ideal_norm(power) >= 2:
                tail = add(tail, term)
            else:
                head = add(head, term)
        check(full == unfolded and full == add(head, tail), "coherent_original_coefficient")
        check(norm(full) - norm(head) == 2 * mul(full, conj(tail))[0] - norm(tail), "coherent_tail_cross_identity")
        w = weights[u]
        full_energy += w * norm(full) / x
        head_energy += w * norm(head) / x
        tail_energy += w * norm(tail) / x
        full_tail = add(full_tail, scale(F(w, x), mul(full, conj(tail))))
    check(full_energy - head_energy == 2 * full_tail[0] - tail_energy, "selected_tail_cross")
    check(norm(full_tail) <= full_energy * tail_energy, "selected_tail_cauchy")
    check(tail_columns and tail_energy > 0 and physical_mask_witnesses > 0, "tail_nonvacuous")
    # Actual common physical kernel and symmetric nested B/F pair selectors.
    kernel = {}
    active_rows = [u for u in rows if weights[u]]
    for k, kp in product(coefficients, repeat=2):
        value = ZERO
        for u in active_rows:
            value = add(value, scale(weights[u], mul(psi(u, k), conj(psi(u, kp)))))
        kernel[k, kp] = value
    pair_sums = defaultdict(lambda: ZERO)
    for k, kp in product(coefficients, repeat=2):
        check(kernel[kp, k] == conj(kernel[k, kp]), "common_kernel_hermitian")
        term = scale(coefficients[k] * coefficients[kp] / x, kernel[k, kp])
        a = tuple(e if not ep else 0 for e, ep in zip(k, kp))
        b = tuple(ep if not e else 0 for e, ep in zip(k, kp))
        f = tuple(int((e - ep) % 6 != 0) for e, ep in zip(k, kp))
        bsmall, fsmall = min(ideal_norm(a), ideal_norm(b)) <= 2, ideal_norm(f) <= 6
        kh, kph = k not in tail_columns, kp not in tail_columns
        pair_sums['full'] = add(pair_sums['full'], term)
        if kh and kph:
            pair_sums['head'] = add(pair_sums['head'], term)
        if not kh and not kph:
            pair_sums['tail'] = add(pair_sums['tail'], term)
        if kph is False:
            pair_sums['full_tail'] = add(pair_sums['full_tail'], term)
        label = 'B' if bsmall else ('F_after_B' if fsmall else 'remaining')
        pair_sums[label] = add(pair_sums[label], term)
        if not bsmall:
            pair_sums['after_B'] = add(pair_sums['after_B'], term)
    check(pair_sums['full'] == (full_energy, F(0)) and pair_sums['head'] == (head_energy, F(0)), "common_kernel_norm_identity")
    check(pair_sums['tail'] == (tail_energy, F(0)) and pair_sums['full_tail'] == full_tail, "common_kernel_norm_identity")
    check(pair_sums['full'] == add(pair_sums['B'], pair_sums['after_B']), "nested_B_F_exact_sets")
    check(pair_sums['after_B'] == add(pair_sums['F_after_B'], pair_sums['remaining']), "nested_B_F_exact_sets")
    check(all(pair_sums[label][1] == 0 for label in ('B', 'F_after_B', 'remaining')), "nested_B_F_reverse_real")
    return dict(scales=dict(D=d, N=n, Y1=y1, Y2=y2, slot_prime=pslot, X=x), tuples=len(tuples), columns=len(coefficients),
                tail_columns=len(tail_columns), rows=len(rows), selected_rows=sum(bool(w) for w in weights.values()),
                physical_mask_witnesses=physical_mask_witnesses, full_energy=full_energy, head_energy=head_energy,
                tail_energy=tail_energy, full_tail_cross=full_tail,
                common_kernel_pair_parts=dict(pair_sums), nested_cuts=dict(B=2, F=6),
                limitation="formal monoid Q(sqrt(-3)) character; no native conductor transfer or smooth decay is certified")


def audit_primitive_quotient():
    cap = 80
    domain = ideals(cap)
    counts = defaultdict(int)
    mismatches = 0
    nonunit_sixth_roots = 0
    for k, kp in product(domain, repeat=2):
        g = tuple(min(e, f) for e, f in zip(k, kp))
        a, b = tuple(e - f for e, f in zip(k, g)), tuple(e - f for e, f in zip(kp, g))
        a0, b0 = tuple(e % 6 for e in a), tuple(e % 6 for e in b)
        at, bt = tuple(e // 6 for e in a), tuple(e // 6 for e in b)
        f = tuple(int((e - ep) % 6 != 0) for e, ep in zip(k, kp))
        check(f == tuple(int(bool(e or ep)) for e, ep in zip(a0, b0)), "primitive_quotient_map")
        check(all(not (e and ep) for e, ep in zip(a, b)), "primitive_quotient_map")
        check(ideal_norm(a0) * ideal_norm(b0) >= ideal_norm(f), "primitive_quotient_count_inequality")
        # Squared form of Ng <= X/[sqrt(Na0 Nb0) (Nat Nbt)^3].
        check(ideal_norm(g) ** 2 * ideal_norm(a0) * ideal_norm(b0) * (ideal_norm(at) * ideal_norm(bt)) ** 6 <= cap ** 2, "primitive_quotient_count_inequality")
        nonunit_sixth_roots += bool(sum(at) or sum(bt))
        counts[ideal_norm(f)] += 1
        common = tuple(int(e and ep) for e, ep in zip(k, kp))
        mismatches += common != f
    check(sum(counts.values()) == len(domain) ** 2 and mismatches > 0, "primitive_quotient_coverage")
    check(nonunit_sixth_roots > 0, "primitive_quotient_nonunit_sixth_parts")
    check(2 * (F(63, 250) - F(1, 500)) == F(1, 2), "primitive_quotient_cutoff")
    return dict(domain_norm_cap=cap, columns=len(domain), ordered_pairs=len(domain) ** 2, quotient_radical_counts=dict(counts), nonunit_sixth_root_pairs=nonunit_sixth_roots,
                f="rad of ordinary-gcd quotients after deleting sixth powers; primes with unequal exponents modulo6",
                common_support_mismatches=mismatches, count_formula="X sum_{Nf<=V}10^omega(f)/sqrt(Nf) << X V^(1/2+epsilon)",
                removable_cut="Nf<=U^(2dr-1/250); intersect the exact remaining unmatched-support cut")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="explicit optional output path; default prints the deterministic record to stdout")
    args = parser.parse_args()
    results = dict(frontier=audit_frontier(), tail=audit_tail(), envelopes=audit_envelopes(),
                   finite_original_centered_tail=audit_full_coefficient(), primitive_quotient=audit_primitive_quotient())
    parameters = dict(d=D, r=R, m=M, z=Z, fresh_fixed_v_max=V, field="formal column prime monoid 2,3,5; rows also have an external7 coordinate; exact Q(sqrt(-3)) values")
    canonical_parameters = json.dumps(fmt(parameters), sort_keys=True, separators=(",", ":")).encode()
    record = dict(date="2026-10-09", checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  model="GPT-6 (Codex), inherited configuration; exact serving variant and reasoning effort are not exposed and are not inferred",
                  validation="same-model internal exact arithmetic audit; not formal verification or independent specialist validation",
                  parameters=parameters, parameters_sha256=hashlib.sha256(canonical_parameters).hexdigest(),
                  conditional_inputs=["native arbitrary-vector Theta6 transfer and zero extension", "good conductor comparable to good radical", "global beta*<=7/8 for the marked-plain contour frontier", "source scalar rectangle scope only for the optional .08 tail"],
                  coverage="16 coarse corners suffice for multi-affine power ledgers; 256 native full/tail branch-pair inequalities; exact interior type tests and finite coefficient/mask algebra are supplementary",
                  results=results, assertions=dict(sorted(COUNTS.items())), assertion_count=sum(COUNTS.values()))
    data = json.dumps(fmt(record), indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(data)
        print(json.dumps(dict(output=str(Path(args.output)), assertions=sum(COUNTS.values()), bytes=len(data.encode()), sha256=hashlib.sha256(data.encode()).hexdigest()), sort_keys=True))
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
