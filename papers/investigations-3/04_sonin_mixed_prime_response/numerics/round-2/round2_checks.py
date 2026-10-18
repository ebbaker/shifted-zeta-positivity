#!/usr/bin/env python3
"""Small exact diagnostic for Project 04's round-two return expansion.

Prepared for Edward Baker with LLM assistance, 17 October 2026.
Recorded model: gpt-6.1-sol (Codex); effort: ultra.

Reuses the round-one Claude review's Fraction matrix helpers and its
rank3_CF1 model verbatim. This is a same-model check of new algebra, not an
independent implementation or a model of the actual Sonin projection.
All comparisons are exact rational arithmetic; there is no norm fit,
asymptotic scan, actual-prime computation or numerical enclosure.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import platform
from pathlib import Path


def load_review(path):
    spec = importlib.util.spec_from_file_location("round1_review", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def determinant(a):
    if not a:
        return 1
    return sum((-1) ** j * a[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in a[1:]]) for j in range(len(a)))


def psd_exact(a):
    """All principal minors, on these matrices of size at most three."""
    n = len(a)
    return all(a[i][j] == a[j][i] for i in range(n) for j in range(n)) and all(
        determinant([[a[i][j] for j in indices] for i in indices]) >= 0
        for size in range(1, n + 1)
        for indices in itertools.combinations(range(n), size))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-module", type=Path, default=(
        Path(__file__).resolve().parents[1] /
        "round-1/claude-review/review_checks_claude_20261017.py"))
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("ROUND2_CHECKS.json"))
    args = parser.parse_args()
    r = load_review(args.review_module)
    F = r.Fr
    mm, add, sub, scale, tr = r.mm, r.madd, r.msub, r.msc, r.mtr
    inv, eq = r.minv, r.meq
    # This is exactly section B's rank3_CF1 model, not a newly selected case.
    up = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)),
          (F(-8, 17), F(15, 17)), (F(7, 25), F(24, 25))]
    uq = [(F(20, 29), F(21, 29)), (F(-12, 37), F(35, 37)),
          (F(9, 41), F(-40, 41)), (F(28, 53), F(45, 53))]
    cf = [(1, 2), (-3, 1), (2, -1), (F(1, 2), 1)]
    basis = [[1, 0, 2], [2, 1, 0], [0, 1, 1], [1, -1, 0],
             [0, 2, -1], [1, 0, 1], [-1, 1, 0], [0, 0, 1]]
    m = r.Model(up, uq, cf, basis, F(1, 2), F(2, 5))
    ep, eqp = scale(1 / m.bp, m.Ep), scale(1 / m.bq, m.Eq)
    a, b, c = m.br(ep), m.br(eqp), m.br(mm(ep, eqp))
    n0 = m.br(m.AF)
    np, nq, npq = (m.br(mm(op, m.AF)) for op in (ep, eqp, mm(ep, eqp)))
    lp, lq, lpq = sub(np, mm(a, n0)), sub(nq, mm(b, n0)), sub(npq, mm(c, n0))
    k0 = sub(sub(lpq, mm(b, lp)), mm(a, lq))
    # The double-return expression in reviewer section 7, and its swap.
    k0_return = sub(m.br(mm(eqp, m.Q, ep, m.Q, m.AF)), mm(a, lq))
    k0_swap = sub(m.br(mm(ep, m.Q, eqp, m.Q, m.AF)), mm(b, lp))
    mu2 = tr(k0)
    x, y = m.bp, m.bq
    rp, rq = inv(add(m.Ik, scale(x, a))), inv(add(m.Ik, scale(y, b)))
    resolvent = inv(add(add(add(m.Ik, scale(x, a)), scale(y, b)), scale(x * y, c)))
    return_qp, return_pq = sub(c, mm(b, a)), sub(c, mm(a, b))
    correction = add(scale(x, mm(return_qp, rp, lp)), scale(y, mm(return_pq, rq, lq)))
    rhs = x * y * tr(mm(resolvent, sub(k0, correction)))
    direct_corners = [m.direct_B(factors) for factors in (
        [], [(m.Up, m.rp)], [(m.Uq, m.rq)], [(m.Up, m.rp), (m.Uq, m.rq)])]
    bs, bp, bq, bpq = direct_corners
    mixed = bpq - bp - bq + bs
    dropped_return = x * y * tr(mm(resolvent, k0))
    g = (1 - x) * (1 - y)
    bound = 2 * x * y / g * (1 / (1 - x) + 1 / (1 - y)) * bs
    old_bound = 2 * x * y / g * (
        1 + (1 + x) / (1 - x) + (1 + y) / (1 - y)) * bs
    remainder = mixed - x * y * mu2
    remainder_bound = x * y / g * (
        4 * (x + y - x * y) + 2 * x / (1 - x) + 2 * y / (1 - y)) * bs
    # D is selfadjoint in the Gram metric of the reused nonorthogonal basis.
    d = sub(add(mm(b, a), mm(a, b)), c)
    contraction = all(psd_exact(mm(m.G, add(m.Ik, scale(sign, d)))) for sign in (-1, 1))
    checks = {
        "ambient_ep_eq_commute": eq(mm(ep, eqp), mm(eqp, ep)),
        "nondegenerate_compressions_do_not_commute": not eq(mm(a, b), mm(b, a)),
        "K0_equals_review_double_return_operator": eq(k0, k0_return),
        "K0_is_symmetric_in_p_q_as_operator": eq(k0, k0_swap),
        "exact_normalized_return_identity_matches_direct_corners": rhs == mixed,
        "dropped_return_negative_control_differs": dropped_return != mixed,
        "D_is_contraction_by_exact_psd_checks": contraction,
        "mu2_bound_holds": abs(mu2) <= 4 * bs,
        "sharpened_generic_bound_holds": abs(mixed) <= bound,
        "sharpened_bound_smaller_than_review_bound": bound < old_bound,
        "explicit_cubic_remainder_bound_holds": abs(remainder) <= remainder_bound,
    }
    record = {
        "schema": "project04_round2_exact_return_diagnostic_v1",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "prepared_for": "Edward Baker",
        "date": "2026-10-17 America/New_York",
        "llm_assistance": {"model": "gpt-6.1-sol (Codex)", "effort": "ultra"},
        "status": "exact rational diagnostic of generic matrix algebra; no actual-Sonin estimate",
        "reused_source": "../round-1/claude-review/review_checks_claude_20261017.py",
        "reused_source_sha256": hashlib.sha256(args.review_module.read_bytes()).hexdigest(),
        "reused_model": "section B rank3_CF1, all parameters and basis unchanged",
        "checks": checks,
        "values": {key: str(value) for key, value in {
            "beta_p": x, "beta_q": y, "B_S": bs, "B_p": bp, "B_q": bq, "B_pq": bpq,
            "mixed_direct": mixed, "mixed_return_identity": rhs,
            "mixed_with_returns_dropped": dropped_return, "mu2": mu2,
            "sharpened_generic_bound": bound, "review_generic_bound": old_bound,
            "cubic_remainder": remainder, "cubic_remainder_bound": remainder_bound,
        }.items()},
        "all_checks_pass": all(checks.values()),
    }
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"all_checks_pass": record["all_checks_pass"],
                      "output": str(args.output), "failed": [k for k, v in checks.items() if not v]}))
    raise SystemExit(0 if record["all_checks_pass"] else 1)


if __name__ == "__main__":
    main()
