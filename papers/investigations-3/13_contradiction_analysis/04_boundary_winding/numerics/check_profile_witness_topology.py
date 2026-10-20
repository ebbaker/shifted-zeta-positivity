#!/usr/bin/env python3
"""Exact diagnostics for the boundary-winding brainstorm of 20 October 2026.

Prepared for Edward Baker with substantial LLM assistance.
Authoring model: gpt-6-astra (Codex), recorded reasoning effort max.
This checks a particular relaxed witness and algebraic fixtures, not RH.
"""

import argparse
import datetime
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def linear_interval(coefficients, intervals):
    lower = sum(c * (lo if c >= 0 else hi)
                for c, (lo, hi) in zip(coefficients, intervals))
    upper = sum(c * (hi if c >= 0 else lo)
                for c, (lo, hi) in zip(coefficients, intervals))
    return lower, upper


def strings(interval):
    return [str(x) for x in interval]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--wall-replay", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    bw = root / "papers/investigations-3/13_contradiction_analysis/04_boundary_winding"
    profile = bw / "threshold_routes/08_deflated_jet_hierarchy/notes/06_ACTUAL_PROFILE_OBSERVATIONS_AND_RELAXED_DUAL_FAILURE_20261020.md"
    text = profile.read_text()
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(message)

    # These are the source note's deliberately widened, uniform, full-source
    # enclosures, not fresh quadrature and not midpoint substitutions.
    decimal_profiles = [
        ("0.2041296865", "0.2041296928"),
        ("0.3336081998", "0.3336082066"),
        ("0.4849096493", "0.4849096549"),
    ]
    heights = [20, 40, 80]
    squared_heights = [b * b for b in heights]
    for b, (lo, hi) in zip(heights, decimal_profiles):
        check(f"| {b} | `[{lo}, {hi}]` |" in text,
              "readable profile enclosure must match pinned source")
    profiles = [(F(lo), F(hi)) for lo, hi in decimal_profiles]
    s = (F(1001) ** 2, F(1002) ** 2)
    neighbor = (s[0], (F(1002) + F(1, 2)) ** 2)
    slack_nodes = [900, 1600, 25000]
    inverse = [
        [F(231775, 30366), -F(34675, 2169), F(286525, 30366)],
        [-F(4064, 567), F(19000, 1053), -F(91688, 7371)],
        [F(20881, 39042), -F(522025, 253773), F(1524313, 507546)],
    ]
    matrix = [[F(y + 400, y + B) for y in slack_nodes]
              for B in squared_heights]
    for i in range(3):
        for j in range(3):
            check(sum(inverse[i][k] * matrix[k][j] for k in range(3))
                  == int(i == j), "exact observation matrix inverse")

    # Enlarge the correlated (a,d) domain to independent closed s,y intervals.
    # This includes d=0 only for bounding, while the source witness has d>0.
    observations = [
        (lo / b - F(4) / (s[0] + B) - F(2) / (neighbor[0] + B),
         hi / b - F(4) / (s[1] + B) - F(2) / (neighbor[1] + B))
        for (lo, hi), b, B in zip(profiles, heights, squared_heights)
    ]
    claimed_residue_bounds = [
        ("1.1429", "1.1433"),
        ("1.9438", "1.9444"),
        ("82.5224", "82.5235"),
    ]
    rows = []
    for y, row, claimed in zip(slack_nodes, inverse, claimed_residue_bounds):
        weights = linear_interval(row, observations)
        residues = tuple(value * F(y + 400, 2) for value in weights)
        lower, upper = map(F, claimed)
        check(weights[0] > F(1, 1000), "strict positive slack weight")
        check(lower < residues[0] <= residues[1] < upper,
              "outward rational displayed residue enclosure")
        integer_part = lower.numerator // lower.denominator
        check(F(integer_part) < lower < upper < integer_part + 1,
              "entire interval excludes every integer")
        rows.append({
            "squared_node": y,
            "weight_interval_exact": strings(weights),
            "logarithmic_derivative_residue_interval_exact": strings(residues),
            "displayed_strict_residue_bounds": list(claimed),
            "integers_in_interval": [],
        })

    # The Q identity and the critical-value identity have different coefficients.
    for h2 in [F(-3), F(-1, 5), F(2, 7), F(4)]:
        for h3 in [F(-2), F(0), F(3, 2)]:
            for h4 in [F(-5), F(0), F(7)]:
                for L in [F(1, 100), F(2, 3)]:
                    S = h3 * h3 / (9 * h2 * h2) - h4 / (6 * h2)
                    Q = 2 * h3 * h3 - 3 * h2 * h4 - 18 * L * h2 * h2
                    check(Q == 18 * h2 * h2 * (S - L),
                          "raw necessary polynomial identity")
                    vpp = h4 / h2 - (h3 / h2) ** 2
                    check(vpp == -(h3 / h2) ** 2 / 3 - 6 * S,
                          "critical-value curvature identity")

    # For a translated quadratic heat polynomial, the two-root discriminant
    # is 8*tau, independently of a and of a nonzero overall scalar.
    for a in [F(-3), F(0), F(1001)]:
        for tau in [F(-1), F(-1, 8), F(0), F(1, 8), F(1)]:
            p1 = 2 * a
            p2 = 2 * a * a + 4 * tau
            check(2 * p2 - p1 * p1 == 8 * tau,
                  "two-root contour-moment discriminant fixture")

    # For real roots outside the circle, the second boundary harmonic of
    # log|G| divided by pi is r^2 times the quadratic coefficient of log G.
    # Check both derivative and harmonic factors on exact finite products.
    harmonic_cases = 0
    for a in [F(1), F(20)]:
        for with_neighbor in [False, True]:
            distances = [-2 * a, -2 * a]
            if with_neighbor:
                distances += [F(1, 2), -(2 * a + F(1, 2))]
            coefficients = [F(1), F(0), F(0)]
            for distance in distances:
                old = coefficients[:]
                coefficients[1] = old[1] - old[0] / distance
                coefficients[2] = old[2] - old[1] / distance
            c1, c2 = coefficients[1:]
            root_sum = sum(F(1) / distance ** 2 for distance in distances)
            for radius in [F(1, 10), F(1, 7)]:
                harmonic_cases += 1
                harmonic_over_pi = radius ** 2 * (c2 - c1 ** 2 / 2)
                check(c1 ** 2 - 2 * c2 == root_sum,
                      "deflated derivative equals exact residual root sum")
                check(-2 * harmonic_over_pi / radius ** 2 == root_sum,
                      "signed boundary harmonic has correct factor and sign")

    wall_checker = root / "papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_spacetime_wall_flux.py"
    base_checker = wall_checker.with_name("check_spacetime_topology.py")
    wall = json.loads(args.wall_replay.read_text())
    check(wall["status"] == "PASS", "wall replay passed")
    check(wall["checker_sha256"] == digest(wall_checker),
          "wall replay matches current checker")
    check(wall["base_checker_sha256"] == digest(base_checker),
          "wall replay matches current base checker")
    check(wall["cases"] == 88 and wall["assertions"] == 2122,
          "expected inherited finite-control suite")
    narrow_quadratic = next(
        row for row in wall["cases_data"]
        if row["degree"] == 2 and row["overall_sign"] == 1
        and row["family"] == "narrow"
    )
    check(narrow_quadratic["endpoint_root_counts"] == [0, 0]
          and narrow_quadratic["signed_wall_terms_Q"] == [1, -1]
          and narrow_quadratic["direct_winding"] == -1,
          "equal endpoint counts do not remove wall flux")

    sources = [
        profile,
        bw / "threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md",
        bw / "threshold_routes/08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md",
        root / "papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/15_COMPLETE_FOURTH_ORDER_INTERFACE_20261020.md",
        wall_checker,
        base_checker,
        root / "papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md",
    ]
    record = {
        "date": "2026-10-20",
        "checked_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "prepared_for": "Edward Baker",
        "llm_assistance": "Substantial LLM assistance",
        "model": "gpt-6-astra",
        "reasoning_effort": "max",
        "status": "PASS",
        "review_scope": "Author self-check; exact rational arithmetic; no new theta acquisition",
        "question": "Do the three slack masses of the displayed actual-profile witness give integer logarithmic-derivative residues?",
        "answer": "No. All three residues lie strictly between consecutive integers throughout the declared parameter domain.",
        "limitation": "Rejects this explicit witness as an entire-function divisor; does not exclude other integer witnesses or a theta event.",
        "arithmetic": "Python standard-library Fraction; decimal inputs are exact rationals enclosing the source values",
        "source_profile_intervals": decimal_profiles,
        "time_domain": ["0.099999", "0.100001"],
        "event_height_domain": ["1001", "1002"],
        "neighbor_distance_domain": "0 < d <= 1/2",
        "residue_formula": "nu_j = (y_j+400)*w_j/2",
        "slack_residue_rows": rows,
        "new_exact_checks": checks,
        "boundary_harmonic_finite_product_cases": harmonic_cases,
        "inherited_wall_replay": {
            "status": wall["status"],
            "assertions": wall["assertions"],
            "cases": wall["cases"],
            "replay_file_sha256": digest(args.wall_replay),
            "inherited_header_date": wall["date"],
            "replayed_for_this_note_on": "2026-10-20",
            "replaying_model": "gpt-6-astra",
            "replaying_effort": "max",
            "quadratic_missing_flux_control": narrow_quadratic,
        },
        "source_sha256": {str(p.relative_to(root)): digest(p) for p in sources},
        "checker_sha256": digest(Path(__file__)),
        "git_parent": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({
        "status": record["status"],
        "new_exact_checks": checks,
        "residue_bounds": claimed_residue_bounds,
        "inherited_wall_cases": wall["cases"],
    }))


if __name__ == "__main__":
    main()
