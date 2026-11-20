"""AGC-JH-E04 r1 exact checks, prepared for Edward Baker with OpenAI Codex.

19 November 2026, America/New_York. Helper dispatch gpt-6.2-sol/ultra.
Run with Python 3.10+ and no third-party packages.
"""

import argparse
from datetime import datetime
from fractions import Fraction
from hashlib import sha256
from itertools import zip_longest
from math import factorial, prod
from pathlib import Path
import json
import platform
from time import perf_counter_ns
from zoneinfo import ZoneInfo


BRANCH = Path(__file__).resolve().parents[1]
RECORD = Path(__file__).with_name("03_AGC_JH_EXACT_CHECKS_20261119.json")
Q = Fraction


class Checks:
    def __init__(self):
        self.residuals = {}
        self.sensitivity = {}

    def equal(self, label, left, right):
        self.residuals[label] = str(left - right)

    def require(self, label, condition):
        self.equal(label, int(condition), 1)

    def omit(self, label, residual):
        self.sensitivity[label] = str(residual)


def beta(j):
    return Q(j, j + 1)


def poly_add(left, right):
    return [a + b for a, b in zip_longest(left, right, fillvalue=0)]


def poly_mul(left, right):
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def characteristic(sites, first_edge=1):
    """Monic characteristic polynomial, coefficients in ascending order."""
    previous, current = [Q(1)], [Q(0), Q(1)]
    for edge in range(first_edge, first_edge + sites - 1):
        term = [-beta(edge) * value for value in previous]
        previous, current = current, poly_add([Q(0), *current], term)
    return current


def moment(sites, order):
    """Return walks, with edge weight beta on ascent and 1 on descent."""
    state = [Q(1)] + [Q(0)] * (sites - 1)
    for _ in range(order):
        next_state = [Q(0)] * sites
        for site in range(1, sites):
            next_state[site] += beta(site) * state[site - 1]
            next_state[site - 1] += state[site]
        state = next_state
    return state[0]


def finite_weyl_checks(checks):
    summaries = {}
    for n in (2, 3, 4):
        name = f"N={n}"
        p_old, p_new = characteristic(n), characteristic(n + 2)
        a_old, a_new = characteristic(n - 1, 2), characteristic(n + 1, 2)
        # The 00-resolvent numerator is the trailing principal minor.
        numerator = poly_add(poly_mul(a_new, p_old),
                             [-coefficient for coefficient in poly_mul(a_old, p_new)])
        h = prod(beta(edge) for edge in range(1, n + 1))
        expected = [Q(0), h] + [Q(0)] * (len(numerator) - 2)
        checks.require(f"{name}: Weyl cross multiplication", numerator == expected)

        combined = poly_mul(p_old, p_new)
        knots = 2 * n + 2
        node_square_sum = 2 * (sum(beta(edge) for edge in range(1, n))
                               + sum(beta(edge) for edge in range(1, n + 2)))
        checks.equal(f"{name}: combined knot sum", combined[-2], 0)
        # Newton's second identity, using zero combined knot sum.
        variance_from_polynomial = -2 * combined[-3] / (knots * (knots + 1))
        variance = node_square_sum / (knots * (knots + 1))
        checks.equal(f"{name}: simplex variance", variance_from_polynomial, variance)

        leading = (-1)**n * h / factorial(2 * n)
        following = -leading * variance * (Q(1, 2) + Q(1, 2 * n + 1))
        coefficients = {}
        for k, expected_coefficient in ((n, leading), (n + 1, following)):
            coefficient = ((-1)**k * (moment(n + 2, 2 * k) - moment(n, 2 * k))
                           / factorial(2 * k))
            checks.equal(f"{name}: Fourier coefficient z^{2*k}", coefficient,
                         expected_coefficient)
            coefficients[str(2 * k)] = str(coefficient)
        summaries[str(n)] = {"simplex_variance": str(variance),
                             "fourier_coefficients": coefficients}
    return summaries


def forced_checks(checks):
    c, s, e = Q(1), Q(1, 3), Q(3)
    c_dot, s_dot, e_dot = Q(1, 5), Q(3, 14), Q(1, 66)
    d, h = s*s, 2*s
    roots = (c+s, c-s, -c+s, -c-s, e, -e)
    velocities = (c_dot+s_dot, c_dot-s_dot, -c_dot+s_dot,
                  -c_dot-s_dot, e_dot, -e_dot)
    plus, minus = roots[:2]
    exterior = roots[2:]
    heat = tuple(2 * sum(1 / (root - other) for j, other in enumerate(roots) if i != j)
                 for i, root in enumerate(roots))
    f = tuple(free - actual for free, actual in zip(heat, velocities))
    gamma = -(f[0] + f[1]) / 2
    delta = -((plus-c)*f[0] + (minus-c)*f[1])
    v_plus, v_minus = gamma + delta/h, gamma - delta/h
    checks.require("moving polynomial: six simple roots", len(set(roots)) == 6)
    checks.require("moving polynomial: exact buffered target count",
                   all(abs(root-c) < Q(1, 2) for root in roots[:2])
                   and all(abs(root-c) > Q(1, 2) for root in exterior))
    checks.equal("moving polynomial: target plus forcing from residue", v_plus, -f[0])
    checks.equal("moving polynomial: target minus forcing from residue", v_minus, -f[1])

    w = [root - c for root in exterior]
    q = [value*value - d for value in w]

    def S(n):
        return sum(value**(-n) for value in q)

    def T(n):
        return sum(offset * value**(-n) for offset, value in zip(w, q))

    def split_weight(root, p, q):
        return (root-plus)**(-p) * (root-minus)**(-q)

    def P(p, q):
        return sum(split_weight(root, p, q) for root in exterior)

    def contour(kernel):
        # All kernel poles are inside, f = O(1/z), and the infinity residue vanishes.
        return -sum(value * kernel(i) for i, value in enumerate(f[2:]))

    def compare_row(label, direct, unforced, spatial, moving=Q(0)):
        free = direct(heat)
        actual = direct(velocities)
        checks.equal(f"{label}: unforced recurrence", unforced, free)
        checks.equal(f"{label}: isolated forcing", spatial + moving, actual - free)
        checks.equal(f"{label}: full recurrence", unforced + spatial + moving, actual)
        checks.omit(f"{label}: all forcing omitted", unforced - actual)
        checks.omit(f"{label}: moving kernel terms omitted", unforced + spatial - actual)

    compare_row("c", lambda v: (v[0]+v[1])/2,
                sum(1/(target-root) for target in roots[:2] for root in exterior), gamma)
    compare_row("D", lambda v: s*(v[0]-v[1]), 2 - 4*d*S(1), delta)
    checks.equal("moving polynomial: prescribed D derivative",
                 s*(velocities[0]-velocities[1]), Q(1, 7))

    def symmetric_derivative(n, odd, v):
        center_speed = (v[0] + v[1]) / 2
        d_speed = s * (v[0] - v[1])
        total = Q(0)
        for offset, denominator, exterior_speed in zip(w, q, v[2:]):
            relative_speed = exterior_speed - center_speed
            q_speed = 2*offset*relative_speed - d_speed
            inverse_speed = -n * denominator**(-n - 1) * q_speed
            if odd:
                total += offset*inverse_speed + relative_speed*denominator**(-n)
            else:
                total += inverse_speed
        return total

    compare_row("M", lambda v: symmetric_derivative(1, False, v),
                2*S(1)**2 - 12*S(2) - 16*d*S(3),
                contour(lambda i: -2*w[i]*q[i]**(-2)),
                2*gamma*T(2) + delta*S(2))
    compare_row("S2", lambda v: symmetric_derivative(2, False, v),
                8*S(1)*S(2) + 4*T(2)**2 + 4*d*S(2)**2 - 32*S(3) - 40*d*S(4),
                contour(lambda i: -4*w[i]*q[i]**(-3)),
                4*gamma*T(3) + 2*delta*S(3))
    compare_row("T2", lambda v: symmetric_derivative(2, True, v),
                (6*S(1)+8*d*S(2))*T(2) - 20*T(3) - 40*d*T(4),
                contour(lambda i: -3*q[i]**(-2) - 4*d*q[i]**(-3)),
                gamma*(3*S(2)+4*d*S(3)) + 2*delta*T(3))

    def C(m, n):
        if n == 0:
            return sum(P(i, 0) * P(m+1-i, 0) for i in range(2, m))
        if m == 0:
            return sum(P(0, j) * P(0, n+1-j) for j in range(2, n))
        return (sum(P(i, 0) * P(m+1-i, n) for i in range(2, m+1))
                + sum(P(m, j) * P(0, n+1-j) for j in range(1, n)))

    def split_heat(p, q):
        drift = 2/h - h*S(1)
        if q == 0:
            return p*(C(p+1, 0) - (p+3)*P(p+2, 0) - 2*P(p+1, 1) + 2*P(p+1, 0)/h)
        if p == 0:
            return q*(C(0, q+1) - 2*P(1, q+1) - (q+3)*P(0, q+2) - 2*P(0, q+1)/h)
        return (p*(C(p+1, q) - (p+3)*P(p+2, q) - (q+2)*P(p+1, q+1) + drift*P(p+1, q))
                + q*(C(p, q+1) - (p+2)*P(p+1, q+1) - (q+3)*P(p, q+2) - drift*P(p, q+1)))

    def split_derivative(p, q, v):
        # Differentiate split weights via their logarithmic derivative.
        return -sum(split_weight(root, p, q)
                    * (p*(speed-v[0])/(root-plus) + q*(speed-v[1])/(root-minus))
                    for root, speed in zip(exterior, v[2:]))

    for p, q_index in ((1, 1), (2, 1), (1, 2), (2, 0), (0, 2)):
        kernel_force = -p*contour(lambda i: split_weight(exterior[i], p+1, q_index))
        kernel_force -= q_index*contour(lambda i: split_weight(exterior[i], p, q_index+1))
        center_force = p*v_plus*P(p+1, q_index) + q_index*v_minus*P(p, q_index+1)
        compare_row(f"P({p},{q_index})", lambda v: split_derivative(p, q_index, v),
                    split_heat(p, q_index), kernel_force, center_force)

    checks.require("sensitivity: omission of all forcing detected",
                   any(Q(value) for label, value in checks.sensitivity.items()
                       if label.endswith("all forcing omitted")))
    checks.require("sensitivity: omission of moving-kernel forcing detected",
                   any(Q(value) for label, value in checks.sensitivity.items()
                       if label.endswith("moving kernel terms omitted")))
    return {"roots": list(map(str, roots)), "velocities": list(map(str, velocities)),
            "heat_velocities": list(map(str, heat)), "force_residues": list(map(str, f)),
            "gamma": str(gamma), "delta": str(delta)}


def first_variation_checks(checks):
    k, radius, buffer, eta = Q(1, 128), Q(1), Q(1, 2), Q(1, 20)
    # Both square roots have modulus 1/8 for either sign of h; Y has a double at zero.
    checks.require("first variation: outer count and root buffer",
                   k + Q(1, 8) < radius - buffer)
    allowance = (16*radius**2/9 - 2*radius*buffer/3) * eta**2
    checks.equal("first variation: quadratic allowance", allowance, Q(13, 3600))
    summaries = {}
    for h in (Q(1, 64), Q(-1, 64)):
        label = f"first variation h={h}"
        q1, q2 = -2*k, k*k - h
        inner_radius = Q(3, 4)
        envelope = abs(q1)/inner_radius + abs(q2)/inner_radius**2
        checks.require(f"{label}: collar bound", envelope <= Q(449, 9216) < eta)
        # Higher log powers have no coefficient in either of these Laurent orders.
        ell1, ell2 = q1, q2 - q1*q1/2
        center_change = -ell1/2
        gap_change = -ell2 - ell1*ell1/4
        linear_part = -q2
        remainder = gap_change - linear_part
        checks.equal(f"{label}: center", center_change, k)
        checks.equal(f"{label}: discriminant", gap_change, h)
        checks.equal(f"{label}: signed quadratic remainder", remainder, k*k)
        checks.require(f"{label}: informative allowance", abs(remainder) <= allowance < abs(linear_part))
        summaries[str(h)] = {"q_bound": str(envelope), "J": str(linear_part),
                             "D_change": str(gap_change), "remainder": str(remainder),
                             "allowance": str(allowance)}
    return summaries


def source_hashes():
    root = BRANCH.parents[3]
    files = [
        BRANCH / "research-progress/handoffs/AGC_JH_E04_REQUEST_R1_20261119.md",
        BRANCH / "research-progress/handoffs/AGC_JH_E03_REQUEST_R1_20261119.md",
        BRANCH / "notes/02_AGC_JH_FORCED_INTEGER_HIERARCHY_20261119.md",
        BRANCH / "notes/03_AGC_JH_DEGREE_TIME_INTERFACE_20261119.md",
        BRANCH / "notes/04_AGC_JH_SIGNED_GAP_REMAINDER_20261119.md",
        BRANCH.parent / "manuscript/sections/03_hierarchy.tex",
        BRANCH.parents[1] / "03_volterra_coefficient_dynamics/manuscript/sections/readouts.tex",
        BRANCH.parents[1] / "03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex",
        Path(__file__).resolve(),
    ]
    return {str(path.relative_to(root)): sha256(path.read_bytes()).hexdigest() for path in files}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-record", action="store_true",
                        help="write the branch's small JSON execution record")
    args = parser.parse_args()

    start = perf_counter_ns()
    checks = Checks()
    cases = {"weyl": finite_weyl_checks(checks), "moving_polynomial": forced_checks(checks),
             "first_variation": first_variation_checks(checks)}
    hashes = source_hashes()
    elapsed = perf_counter_ns() - start
    failures = {key: value for key, value in checks.residuals.items() if value != "0"}
    record = {
        "schema_version": 1,
        "packet": "AGC-JH-E04 r1",
        "date_local": "2026-11-19",
        "checked_at": datetime.now(ZoneInfo("America/New_York")).isoformat(),
        "intended_author": "Edward Baker",
        "llm_assistance": "OpenAI Codex",
        "helper_dispatch": {"model": "gpt-6.2-sol", "effort": "ultra"},
        "provenance_scope": "Dispatch metadata only. Lead settings and independent backend metadata unavailable.",
        "evidence_scope": "Exact algebra controls with rational arithmetic; no canonical theta data.",
        "environment": {"python": platform.python_version(), "implementation": platform.python_implementation(),
                        "system": platform.system(), "architecture": platform.machine(),
                        "arithmetic": "Python standard-library fractions.Fraction"},
        "runtime_ns_checks_and_hashing": elapsed,
        "source_sha256": hashes,
        "passed": not failures,
        "failed_residuals": failures,
        "exact_residuals": checks.residuals,
        "sensitivity_residuals_prediction_minus_actual": checks.sensitivity,
        "cases": cases,
    }
    output = json.dumps(record, indent=2) + "\n"
    if args.write_record:
        RECORD.write_text(output, encoding="utf-8")
        print(f"{len(checks.residuals)-len(failures)}/{len(checks.residuals)} exact checks passed")
        print("Sensitivity residuals:", {key: value for key, value in checks.sensitivity.items()
                                         if key.startswith("D:") or key.startswith("M:")})
    else:
        print(output, end="")
    if failures:
        raise SystemExit(f"Exact checks failed: {failures}")


if __name__ == "__main__":
    main()
