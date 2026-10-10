#!/usr/bin/env python3
"""Exact finite checks for Short Note 29; no unbounded arithmetic estimates.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-09.
Model: GPT-6 (Codex), inherited variant/effort not exposed.
Only the standard library is used. Output is a small deterministic record.
"""
from fractions import Fraction as F
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path


COUNT = 0
CATEGORIES = {}


def check(condition, category):
    global COUNT
    if not condition:
        raise AssertionError(category)
    COUNT += 1
    CATEGORIES[category] = CATEGORIES.get(category, 0) + 1


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, x):
    return a[0] * x, a[1] * x


def norm2(a):
    return a[0] * a[0] + a[1] * a[1]


def csum(items):
    ans = F(0), F(0)
    for item in items:
        ans = add(ans, item)
    return ans


def prod(items):
    ans = F(1)
    for item in items:
        ans *= item
    return ans


def model(qs):
    cells = list(product((0, 1), repeat=len(qs)))
    rhos = [F(1, q) for q in qs]
    pi = {s: prod(r if z else 1-r for z, r in zip(s, rhos)) for s in cells}
    bases = {i: {s: prod(F(z)-r for j, (z, r) in enumerate(zip(s, rhos)) if i[j])
                 for s in cells} for i in cells}
    norms = {i: prod(r*(1-r) for j, r in enumerate(rhos) if i[j]) for i in cells}
    return cells, rhos, pi, bases, norms


def transform(values, cells, pi, bases, norms):
    return {i: scale(csum(scale(values[s], pi[s]*bases[i][s]) for s in cells),
                     1/norms[i]) for i in cells}


def tensor_checks():
    tuples = [(7,), (13,), (7, 7), (7, 13), (7, 13, 19),
              (7, 7, 13, 13), (7, 13, 19, 31), (7, 7, 13, 13, 19)]
    for qs in tuples:
        cells, rhos, pi, bases, norms = model(qs)
        check(sum(pi.values()) == 1, "cell_mass")
        for i in cells:
            for j in cells:
                inner = sum(pi[s]*bases[i][s]*bases[j][s] for s in cells)
                check(inner == (norms[i] if i == j else 0), "tensor_orthogonality")
        actual_packet = {s: (prod(1-F(1, q) for z, q in zip(s, qs) if not z), F(0))
                         for s in cells}
        coeffs = transform(actual_packet, cells, pi, bases, norms)
        means = [1-F(1, q)+F(1, q*q) for q in qs]
        s2 = [F(q-1, q**4) for q in qs]
        for i in cells:
            expected = prod(F(1, q) if marked else a for marked, q, a in zip(i, qs, means))
            check(coeffs[i] == (expected, 0), "packet_mode_coefficients")
            check(norms[i]*norm2(coeffs[i]) ==
                  prod(b if marked else a*a for marked, a, b in zip(i, means, s2)),
                  "normalized_packet_mode_squares")
        packet_mean = csum(scale(actual_packet[s], pi[s]) for s in cells)
        variance = sum(pi[s]*norm2(sub(actual_packet[s], packet_mean)) for s in cells)
        variance_expected = prod(a*a+b for a, b in zip(means, s2))-prod(a*a for a in means)
        check(variance == variance_expected and variance > 0, "positive_deletion_variance")
        for trial in range(1, 33):
            vals = {s: (F(((k+3)*trial)%29-14, trial+1),
                        F(((2*k+5)*trial)%31-15, trial+2)) for k, s in enumerate(cells)}
            fc = transform(vals, cells, pi, bases, norms)
            energy = sum(pi[s]*norm2(vals[s]) for s in cells)
            parseval = sum(norms[i]*norm2(fc[i]) for i in cells)
            check(energy == parseval, "complex_parseval")
            for s in cells:
                reconstruction = csum(scale(fc[i], bases[i][s]) for i in cells)
                check(reconstruction == vals[s], "complex_tensor_reconstruction")
            # A slightly nonproduct actual measure, compared to the model.
            perturb = {s: F((sum(s)+trial)%3-1, 20) for s in cells}
            unscaled = {s: pi[s]*(1+perturb[s]) for s in cells}
            mass = sum(unscaled.values())
            weights = {s: unscaled[s]/mass for s in cells}
            delta = max(abs(weights[s]/pi[s]-1) for s in cells)
            actual_energy = sum(weights[s]*norm2(vals[s]) for s in cells)
            check((1-delta)*parseval <= actual_energy <= (1+delta)*parseval,
                  "actual_measure_comparison")


def divisor_coefficient_checks():
    # Distinct ideal symbols; equal norms are legal. These finite parameters
    # test the original coefficient identity on z < Nn <= z^2, Y < z.
    # They do not model an asymptotic or assert a common adaptive L_u.
    for small in [(7,), (7, 7), (7, 13)]:
        norms = list(small)+[103, 109]
        z, y = 2000, 100
        for bits in product((0, 1), repeat=len(small)):
            selected = [i for i, b in enumerate(bits) if b]+[len(small), len(small)+1]
            subnorms = [norms[i] for i in selected]
            n_norm = int(prod(subnorms))
            check(z < n_norm <= z*z and y < z, "finite_original_annulus")
            prefix = sum(F((-2)**sum(d)) for d in product((0, 1), repeat=len(selected))
                         if prod(q for q, b in zip(subnorms, d) if b) <= y)
            mobius = (-1)**len(selected)
            expected = 2*(-1)**sum(bits)
            check(mobius+prefix == expected, "saturated_actual_prefix")
            # Compute the ORIGINAL truncated c_z(d) and tail, not only its
            # prefix reformulation. For a squarefree d, factorizations split
            # its distinct prime symbols between the two truncated factors.
            original_tail = F(0)
            for div in product((0, 1), repeat=len(selected)):
                dnorms = [q for q, b in zip(subnorms, div) if b]
                if prod(dnorms) <= y:
                    continue
                cz = 0
                for left in product((0, 1), repeat=len(dnorms)):
                    na = prod(q for q, b in zip(dnorms, left) if b)
                    nb = prod(q for q, b in zip(dnorms, left) if not b)
                    if na <= z and nb <= z:
                        cz += (-1)**len(dnorms)
                original_tail -= cz
            check(original_tail == expected, "original_truncated_tail")
        # Assign exact complex profile values to finite total-ideal columns;
        # ordered pair counts cancel the actual factor two in each cofactor.
        cells, _, pi, bases, bnorms = model(small)
        coeffs = {a: (F(3+sum((i+1)*b for i, b in enumerate(a)), 7),
                      F(2-sum(a), 11)) for a in cells}
        response = {s: csum(scale(coeffs[a], (-1)**sum(a)) for a in cells
                           if not any(a[i] and s[i] for i in range(len(small))))
                    for s in cells}
        # Fourier transform of arbitrary cross-shape cofactor coefficients.
        fc = transform(response, cells, pi, bases, bnorms)
        for i in cells:
            # E[1_(Z_A=0) h_I]/||h_I||^2 equals (-1)^|I|
            # times the free probability on A\I whenever I is contained in A.
            expected = csum(scale(coeffs[a], (-1)**(sum(a)+sum(i)) *
                                      prod(1-F(1, q) for j, q in enumerate(small)
                                           if a[j] and not i[j]))
                            for a in cells if all(not i[j] or a[j] for j in range(len(i))))
            check(fc[i] == expected, "general_cross_shape_deletion_transform")


def exact_full_response_checks():
    for q in [7, 13, 19, 31]:
        for trial in range(1, 65):
            groups = [[], []]
            for s in (0, 1):
                for k in range(1, 6):
                    weight = F(q+trial+k+s, (q+1)*(trial+3)*(k+2))
                    remainder = F((trial*k+3*s)%17-8, trial+1), F((trial+2*k+s)%19-9, k+1)
                    groups[s].append((weight, remainder))
            masses = [sum(w for w, _ in group) for group in groups]
            m = sum(masses)
            rho = masses[1]/m
            packets = [(F(q-1, q)*trial, F(trial, q+1)),
                       (F(trial), F(trial+1, q+1))]
            rmeans = [scale(csum(scale(r, w) for w, r in group), 1/masses[s])
                      for s, group in enumerate(groups)]
            variances = [sum(w*norm2(sub(r, rmeans[s])) for w, r in group)
                         for s, group in enumerate(groups)]
            outside = F(trial*trial+q, trial+5)
            direct = outside+sum(w*norm2(add(packets[s], r))
                                 for s, group in enumerate(groups) for w, r in group)
            mean_square = sum(masses[s]*norm2(add(packets[s], rmeans[s])) for s in (0, 1))
            check(direct == mean_square+sum(variances)+outside,
                  "full_response_cell_covariance_complement")
            total_mean = add(scale(add(packets[0], rmeans[0]), 1-rho),
                             scale(add(packets[1], rmeans[1]), rho))
            contrast = add(sub(packets[1], packets[0]), sub(rmeans[1], rmeans[0]))
            two_mode = m*norm2(total_mean)+m*rho*(1-rho)*norm2(contrast)
            check(mean_square == two_mode, "exact_single_prime_two_modes")
            best = add(scale(packets[0], 1-rho), scale(packets[1], rho))
            packet_var = sum(masses[s]*norm2(sub(packets[s], best)) for s in (0, 1))
            check(packet_var == m*rho*(1-rho)*norm2(sub(packets[1], packets[0])),
                  "exact_scalar_mean_subtraction")
            for scalar in [(F(0), F(0)), (F(trial), F(-trial, 7))]:
                residual = sum(masses[s]*norm2(sub(packets[s], scalar)) for s in (0, 1))
                check(residual == packet_var+m*norm2(sub(best, scalar)),
                      "arbitrary_scalar_least_squares")
            # The full remainder can cancel both cells exactly: a packet
            # lower bound is not a lower bound for the full signed response.
            check(sum(masses[s]*norm2(add(packets[s], scale(packets[s], -1)))
                      for s in (0, 1)) == 0, "full_response_cancellation_possible")


def exponent_checks():
    h, row_root = F(2, 5), F(1, 15)
    mass = row_root-1
    target = F(4, 5)
    check(h/6 == row_root, "rational_exponent_ledger")
    check(mass == -F(14, 15), "rational_exponent_ledger")
    check(2+mass == F(16, 15), "rational_exponent_ledger")
    check((target-mass)/2 == F(13, 15), "rational_exponent_ledger")
    check((target-mass)/2-1 == -F(2, 15), "rational_exponent_ledger")
    check(target-F(19, 24) == F(1, 120), "rational_exponent_ledger")
    check(row_root/2 == F(1, 30), "rational_exponent_ledger")


def full_column_covariance_checks():
    # Arbitrary real coefficient tables with physical p-deletion columns.
    # The adaptive-cutoff estimates remain unproved; no constant cutoff is
    # inserted here. These checks verify the literal whole-column forms.
    marked = {0, 3}
    for trial in range(1, 65):
        profiles = [(F((trial+j)%11-5, j+2), F((trial+3*j)%13-6, j+3))
                    for j in range(7)]
        weights = {s: [F(trial+k+s+1, k+2) for k in range(5)] for s in (0, 1)}
        mass = {s: sum(weights[s]) for s in (0, 1)}
        table = {s: [[F(0) if s == 1 and j in marked else
                      F((trial+2*k+3*j+s)%17-8, j+k+2) for j in range(7)]
                     for k in range(5)] for s in (0, 1)}
        beta = {s: [sum(weights[s][k]*table[s][k][j] for k in range(5))/mass[s]
                    for j in range(7)] for s in (0, 1)}
        means = {s: csum(scale(profiles[j], beta[s][j]) for j in range(7))
                 for s in (0, 1)}
        for s in (0, 1):
            direct_variance = sum(weights[s][k]*norm2(sub(
                csum(scale(profiles[j], table[s][k][j]) for j in range(7)), means[s]))
                                  for k in range(5))
            covariance = sum(
                (profiles[j][0]*profiles[l][0]+profiles[j][1]*profiles[l][1]) *
                sum(weights[s][k]*(table[s][k][j]-beta[s][j]) *
                    (table[s][k][l]-beta[s][l]) for k in range(5))
                for j in range(7) for l in range(7))
            check(direct_variance == covariance and covariance >= 0,
                  "whole_column_centered_covariance")
        actual_contrast = sub(means[1], means[0])
        expanded_contrast = sub(
            csum(scale(profiles[j], beta[1][j]-beta[0][j]) for j in range(7)
                 if j not in marked),
            csum(scale(profiles[j], beta[0][j]) for j in marked))
        check(actual_contrast == expanded_contrast, "complete_deletion_cutoff_contrast")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name(
        "deletion_mode_covariance_record_20261009.json"))
    args = parser.parse_args()
    tensor_checks()
    divisor_coefficient_checks()
    exact_full_response_checks()
    full_column_covariance_checks()
    exponent_checks()
    record = {
        "date": "2026-10-09",
        "prepared_for": "Edward Baker",
        "model": "GPT-6 (Codex), inherited configuration; exact variant and effort not exposed",
        "llm_acknowledgement": "Substantial LLM assistance; same-model internal validation only",
        "status": "passed",
        "assertions": COUNT,
        "categories": CATEGORIES,
        "arithmetic": "Python standard-library exact fractions; complex pairs of fractions",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Finite algebraic verification of Note 29's deletion transforms and energy ledgers",
        "not_certified": ["fixed-field prime ideal theorem", "unbounded weighted lattice asymptotic",
                          "actual full-response conditional mean estimates", "centered covariance bound",
                          "complementary squarefree energy", "RH or a new zero-free boundary"],
    }
    args.output.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"status": "passed", "assertions": COUNT,
                      "record": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
