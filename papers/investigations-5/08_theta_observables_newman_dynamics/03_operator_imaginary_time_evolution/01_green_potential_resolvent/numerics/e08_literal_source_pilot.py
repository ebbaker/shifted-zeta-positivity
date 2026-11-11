"""E08 r1 ordered literal-source pilot. Requires python-flint.

Prepared for Edward Baker, 2026-11-10, with OpenAI Codex assistance.
Recorded orchestration turn: gpt-6.1-sol / ultra. No Green field integration.
"""
import argparse
import json
import math
import platform
import signal
from time import monotonic

import flint
from flint import acb, arb, ctx

from e08_contours import ContourBudget, candidates, circle, clusters, rectangle
from e08_source import SourceCap, acquire

TIERS = (128, 256, 512)
PATCH_RADII = (arb(1) / 2, arb(3) / 4, arb(1))
CASES = (
    ("direct", arb(30)),
    ("patch 128", arb(113) / 4),
    ("patch 132", arb(121) / 4),
    ("patch 263", arb(383) / 4),
)
CASE_SECONDS = 300


class CaseTimeout(Exception):
    """The single per-case wall-clock cap expired."""


def timed(stats, key, fn, *args, **kwargs):
    start = monotonic()
    try:
        return fn(*args, **kwargs)
    finally:
        stats[key] = stats.get(key, 0.0) + (monotonic() - start)


def export(value):
    """Serialize exact dyadic endpoints, with decimal balls for reading."""
    if isinstance(value, arb):
        if not value.is_finite():
            return {"nonfinite": str(value)}

        def endpoint(x):
            m, e = x.man_exp()
            return [str(m), int(e)]

        return {
            "lower": endpoint(value.lower()),
            "upper": endpoint(value.upper()),
            "ball": value.str(16, more=True),
        }
    if isinstance(value, acb):
        return {"real": export(value.real), "imag": export(value.imag)}
    if isinstance(value, dict):
        return {k: export(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [export(v) for v in value]
    return value


def check_coefficients(coefficients, radii, enclosures):
    if not (len(coefficients) == len(radii) == len(enclosures) == 65):
        raise ValueError("incomplete coefficient evidence")
    for a, radius, raw in zip(coefficients, radii, enclosures):
        if not a.is_exact() or not a.is_finite() or not raw.is_finite():
            raise ValueError("coefficient must be finite and exactly dyadic")
        if not radius.is_exact() or not radius >= 0:
            raise ValueError("invalid coefficient radius")
        if a == raw.mid():
            required = raw.rad()
        else:
            required = abs(raw - a).upper()
        if not required <= radius:
            raise ValueError("understated coefficient radius or non-enclosing interval")


def strictly_certified(result, epsilon, allow_zero_count=True):
    count = result.get("count")
    lower = result.get("lower")
    upper = result.get("upper")
    return (
        result.get("status") == "certified"
        and type(count) is int and count >= int(not allow_zero_count)
        and result.get("winding") is not None
        and result["winding"].unique_fmpz() == count
        and lower is not None and upper is not None
        and lower > epsilon and upper >= lower
    )


def check_cluster_counts(outer_n, disks, s, epsilon):
    if type(outer_n) is not int or not 0 <= outer_n <= 4:
        return False
    if sum((result.get("count") or 0) for _, _, result in disks) != outer_n:
        return False
    for i, (w, r, result) in enumerate(disks):
        if not w.real.is_exact() or not w.imag.is_exact():
            return False
        if not r in (arb(2)**-24, arb(2)**-32, arb(2)**-40):
            return False
        if not w.abs_upper() + r < s or not strictly_certified(result, epsilon, False):
            return False
        for z, q, _ in disks[:i]:
            if not (w - z).abs_lower() > r + q:
                return False
    return True


def polynomial_value(coefficients, z):
    total = acb(0)
    for a in reversed(coefficients):
        total = total * z + a
    return total


def deflate(coefficients, knots):
    regular = list(map(acb, coefficients))
    for knot in knots:
        quotient = [acb(0)] * (len(regular) - 1)
        quotient[-1] = regular[-1]
        for i in range(len(quotient) - 2, -1, -1):
            quotient[i] = regular[i + 1] + knot * quotient[i + 1]
        regular = quotient
    return regular


def derivative_bound(coefficients, A, order):
    return sum(
        math.prod(range(k - order + 1, k + 1)) * abs(a) * A**(k - order)
        for k, a in enumerate(coefficients) if k >= order
    ).upper()


def factor_bounds(coefficients, eps, A, outer, disks):
    s = A - arb(1) / 8
    n = outer["count"]
    m = outer["lower"] - eps[0]
    M = outer["upper"] + eps[0]
    mu0 = (m / (A + s)**n).lower()
    V0 = (M / (A - s)**n).upper()
    sum_rho = sum((r * result["count"] for _, r, result in disks), arb(0))
    orders = [derivative_bound(coefficients, A, n + j + 1) if n else arb(0) for j in range(3)]
    error = [
        (math.factorial(j) * eps[n + j] / math.factorial(n + j)
         + math.factorial(j) * orders[j] * sum_rho / math.factorial(n + j + 1)).upper()
        for j in range(3)
    ]
    return {"m": m, "M": M, "mu0": mu0, "V0": V0, "sum_rho": sum_rho,
            "polynomial_derivative_bounds": orders, "e": error}


def log_D0(x):
    s = acb(1, -x) / 2
    return arb(16).log() + s.real * arb.pi().log() / 2 - 2 * abs(s).log() - (s / 2).lgamma().real


def gamma_and_factor(coefficients, center, A, disks, bounds, counts):
    mu = (bounds["mu0"] - bounds["e"][0]).lower()
    V = (bounds["V0"] + bounds["e"][0]).upper()
    lam = (V / mu).log().upper()
    B = (arb(13) / 4 + 2 * lam / (A - arb(1) / 4)**2).upper()
    bounds.update(mu=mu, V=V, lambda_upper=lam, B=B)
    if lam > 32:
        return "charged log range exceeds 32"
    offsets = (-arb(1) / 4, arb(0), arb(1) / 4)
    gamma = [log_D0(center + offsets[i]) for i in (0, 2)]
    counts["gamma_calls"] += len(gamma)
    H_D = (max(x.abs_upper() for x in gamma) + arb(13) / 128).upper()
    H = (H_D + max(mu.log().abs_upper(), V.log().abs_upper())).upper()
    bounds.update(log_D0_endpoints=gamma, H_D=H_D, H=H)
    if H > 256:
        return "charged H exceeds 256"
    knots = [w for w, _, result in disks for _ in range(result["count"])]
    regular = deflate(coefficients, knots)
    counts["synthetic_steps"] += sum(len(coefficients) - 1 - j for j in range(len(knots)))
    values = [polynomial_value(regular, acb(offset)) for offset in offsets]
    counts["factor_horner_calls"] += len(values)
    counts["factor_horner_steps"] += len(values) * len(regular)
    radii = [abs(v - acb(v.real.mid(), v.imag.mid())).upper() for v in values]
    allowed = (mu * arb(2)**-17).lower()
    bounds.update(factor_points_local=offsets, factor_values=values, factor_radii=radii,
                  factor_radius_allowed=allowed)
    if not all(radius <= allowed for radius in radii):
        return "factor evaluation interval too wide"
    if not all(x.rad() <= arb(2)**-17 for x in gamma):
        return "gamma endpoint interval too wide"
    return None


def inspect_case(name, center, payload, stats, counts, budget, limits):
    # One polynomial per precision tier. Refine the source alone to keep
    # inadequate coefficient radii from consuming contour or solver caps.
    is_direct = name == "direct"
    max_A = arb(3) / 2 if is_direct else arb(1)
    coefficient_target = arb(2)**(-80 if is_direct else -92)
    for bits in TIERS:
        ctx.prec = bits
        attempt = {"precision_bits": bits, "source_refinements": [], "radii": []}
        payload["attempts"].append(attempt)
        cache = {}
        for refinement in range(8):
            source = timed(stats, "coefficient", acquire, center, bits, limits, counts,
                           refinement=refinement, cache=cache)
            check_coefficients(source.coefficients, source.radii, source.enclosures)
            eps_max = source.errors(max_A)
            fixed = source.fixed_errors(max_A)
            rounding = sum((r * max_A**j for j, r in enumerate(source.radii)), arb(0)).upper()
            attempt["source_refinements"].append({
                "dyadic_depth": refinement, "source_evaluations_to_date": counts["source_panels"],
                "coefficient_error_value_at_max_radius": rounding, "epsilon0_at_max_radius": eps_max[0],
            })
            if rounding <= coefficient_target or refinement == 7:
                break
        coeffs = source.coefficients
        attempt.update(coefficients=coeffs, coefficient_radii=source.radii, coefficient_intervals=source.enclosures,
                       fixed_error_at_max_radius=fixed)
        if is_direct:
            evidence = timed(stats, "contour", rectangle, coeffs, -arb(1), arb(1),
                             arb(1) / 2, arb(1), eps_max[0], budget)
            attempt.update(error_radius=max_A, epsilon=eps_max, direct=evidence)
            if strictly_certified(evidence, eps_max[0]):
                if evidence["count"] == 0:
                    return "certified pilot pass", None
                return "specified gate failure", "certified nonzero target winding"
            continue

        proposed = None
        for A in PATCH_RADII:
            s = A - arb(1) / 8
            eps = source.errors(A)
            current = {"A": A, "s": s, "epsilon": eps, "cluster_proposals": []}
            attempt["radii"].append(current)
            outer = timed(stats, "contour", circle, coeffs, acb(0), A, eps[0], budget)
            current["outer"] = outer
            if not strictly_certified(outer, eps[0]):
                current["gate"] = "outer contour margin or winding unresolved"
                continue
            n = outer["count"]
            if n > 4:
                current["gate"] = "certified count exceeds four"
                continue
            if n and proposed is None:
                counts["root_solver_calls"] += 1
                proposed = timed(stats, "root", candidates, coeffs, arb(1), budget=budget)
                attempt["candidate_points_local"] = proposed
            choices = clusters(proposed, n, s) if n else [()]
            for geometry in choices:
                disk_record = {"disks": []}
                current["cluster_proposals"].append(disk_record)
                disks = []
                for w, rho in geometry:
                    inner = timed(stats, "contour", circle, coeffs, w, rho, eps[0], budget)
                    disk_record["disks"].append({"w_local": w, "rho": rho, "contour": inner})
                    disks.append((w, rho, inner))
                    if not strictly_certified(inner, eps[0], False):
                        break
                if len(disks) != len(geometry) or not check_cluster_counts(n, disks, s, eps[0]):
                    disk_record["gate"] = "strict inner margin, count completeness or cluster geometry"
                    continue
                bounds = timed(stats, "floor", factor_bounds, coeffs, eps, A, outer, disks)
                disk_record["bounds"] = bounds
                relative_target = (bounds["mu0"] / 1024).lower()
                bounds["relative_error_allowed"] = relative_target
                if not bounds["e"][0] <= relative_target:
                    disk_record["gate"] = "charged e0 exceeds mu0/1024"
                    continue
                failure = timed(stats, "gamma_factor", gamma_and_factor,
                                coeffs, center, A, disks, bounds, counts)
                if failure:
                    disk_record["gate"] = failure
                    continue
                disk_record["gate"] = "all passed"
                current["gate"] = "all passed"
                return "certified pilot pass", None
            current["gate"] = "no accepted complete cluster/factor proposal"
    return "inconclusive at cap", "no certified pass at the prescribed precision and radii"


def run_case(name, center):
    def alarm(_signum, _frame):
        raise CaseTimeout("300-second per-case cap")

    start = monotonic()
    limits = {"deadline": start + CASE_SECONDS, "source_panels": 32768,
              "source_live": 4096, "source_depth": 12}
    budget = ContourBudget(max_tests=65536, max_depth=24, deadline=limits["deadline"])
    stats = {k: 0.0 for k in ("coefficient", "contour", "root", "floor", "gamma_factor")}
    counts = {k: 0 for k in ("root_solver_calls", "gamma_calls", "synthetic_steps",
                             "factor_horner_calls", "factor_horner_steps")}
    payload = {"case": name, "center": center, "attempts": []}
    signal.signal(signal.SIGALRM, alarm)
    signal.setitimer(signal.ITIMER_REAL, CASE_SECONDS)
    try:
        status, reason = inspect_case(name, center, payload, stats, counts, budget, limits)
    except (SourceCap, CaseTimeout, TimeoutError) as exc:
        status, reason = "inconclusive at cap", str(exc)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    wall = monotonic() - start
    payload.update(status=status, reason=reason, wall_seconds=wall,
                   seconds=stats, counts=counts,
                   peak_precision_bits=payload["attempts"][-1]["precision_bits"],
                   warm_increment_after_polynomial_seconds=wall - stats["coefficient"],
                   contour_counts={k: getattr(budget, k) for k in (
                       "tests", "polynomial_evaluations", "polynomial_translations", "max_depth_seen",
                       "rejections", "candidate_calls", "candidate_iterations",
                       "candidate_polynomial_evaluations")})
    return export(payload)


def stage_a():
    """Exact polynomial and rejection controls before any source acquisition."""
    ctx.prec = 128
    epsilon = arb(0)
    test_budget = ContourBudget(max_tests=2048, max_depth=12)
    product = [arb(0), -arb(1) / 4, arb(1)]
    outer = circle(product, acb(0), arb(1), epsilon, test_budget)
    assert strictly_certified(outer, epsilon) and outer["count"] == 2
    inner = circle(product, acb(0), arb(2)**-24, epsilon, test_budget)
    assert strictly_certified(inner, epsilon, False) and inner["count"] == 1
    assert not check_cluster_counts(2, [(acb(0), arb(2)**-24, inner)], arb(7) / 8, epsilon)
    boundary = circle([arb(-1), arb(1)], acb(0), arb(1), epsilon, test_budget)
    assert not strictly_certified(boundary, epsilon)
    assert not strictly_certified({"status": "certified", "lower": arb(1), "upper": arb(1)}, epsilon)
    for eta in (arb(0), arb(2)**-16):
        polynomial = [eta, arb(0), arb(1)]
        assert deflate(polynomial, [acb(0), acb(0)]) == [acb(1)]
        assert deflate(polynomial, []) == list(map(acb, polynomial))
        assert polynomial_value(polynomial, acb(1)) != 0
        assert deflate(polynomial, [acb(1)]) == [acb(1), acb(1)]
    a = [arb(0)] * 65
    raw = [arb(0)] * 64 + [arb(0, arb(2)**-50)]
    check_coefficients(a, [v.rad() for v in raw], raw)
    for wrong in (arb(2)**-51, arb(0)):
        try:
            check_coefficients(a, [arb(0)] * 64 + [wrong], raw)
        except ValueError:
            pass
        else:
            raise AssertionError("understated coefficient radius accepted")
    rect = rectangle([arb(0), arb(1)], -arb(1), arb(1), arb(1) / 2, arb(1),
                     epsilon, test_budget)
    assert strictly_certified(rect, epsilon) and rect["count"] == 0
    return {"omitted_root_rejected": True, "boundary_root_rejected": True,
            "missing_counts_rejected": True, "repeated_and_nonroot_knots": True,
            "order_zero": True, "understated_coefficient_and_non_enclosure_rejected": True,
            "synthetic_direct_count": 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage-a-only", action="store_true")
    args = parser.parse_args()
    control = stage_a()
    header = {"kind": "E08 r1", "runtime": {"python": platform.python_version(),
              "python_flint": flint.__version__, "FLINT": flint.__FLINT_VERSION__},
              "stage_a": control, "limits": {"per_case_seconds": CASE_SECONDS, "tiers": TIERS},
              "format": "JSONL. Enclosure endpoint [m,e] means m*2**e."}
    print(json.dumps(header), flush=True)
    if not args.stage_a_only:
        for name, center in CASES:
            record = run_case(name, center)
            print(json.dumps(record), flush=True)


if __name__ == "__main__":
    main()
