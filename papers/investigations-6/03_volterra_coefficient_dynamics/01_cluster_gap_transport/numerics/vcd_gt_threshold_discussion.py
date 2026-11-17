"""Scalar budget explanation for Edward Baker, 17 November 2026.

Prepared with OpenAI Codex LLM assistance; recorded model/effort unavailable.
Exact rational Taylor brackets check arithmetic only, not new source data.
Run from any directory; the small discussion record is written beside this file.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
from pathlib import Path


DELTA = F(1, 10)
ANCHOR_LOWER = F("0.17873684703")


def budget_bounds(kappa):
    if kappa == 0:
        return 2 * DELTA, 2 * DELTA
    x = 4 * kappa * DELTA
    assert 0 < x < 1
    # For exp(-x), even and odd truncations bound above and below.
    term = F(1)
    partial = F(1)
    upper = None
    for n in range(1, 34):
        term *= -x / n
        partial += term
        if n == 32:
            upper = partial
    lower = partial
    return (1 - upper) / (2 * kappa), (1 - lower) / (2 * kappa)


def display(q):
    with localcontext() as context:
        context.prec = 35
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def main():
    rows = []
    for text in ("0", "0.57", "0.58", "0.59"):
        lower, upper = budget_bounds(F(text))
        margin_lower = ANCHOR_LOWER - upper
        margin_upper = ANCHOR_LOWER - lower
        verdict = "passes" if margin_lower > 0 else "fails" if margin_upper < 0 else "unresolved"
        rows.append({"kappa": text, "budget_decimal": display((lower + upper) / 2),
                     "margin_decimal": display((margin_lower + margin_upper) / 2),
                     "rational_verdict": verdict})
    threshold_lower = F("0.5729515")
    threshold_upper = F("0.5729516")
    assert budget_bounds(threshold_lower)[0] > ANCHOR_LOWER
    assert budget_bounds(threshold_upper)[1] < ANCHOR_LOWER
    assert [row["rational_verdict"] for row in rows] == ["fails", "fails", "passes", "passes"]

    # Inherited quadratic: D(v)=2(v-T), K=0, u=0, T=1/20.
    quadratic_margin = 2 * (DELTA - F(1, 20)) - 2 * DELTA
    assert quadratic_margin == -F(1, 10)

    # Inherited even quartic, monomials keyed by (power of tau, power of z).
    a = F(140101, 10)
    dt = {(0, 2): -F(12), (0, 0): 4 * a * a, (1, 0): F(24)}
    dzz = {(0, 2): F(12), (0, 0): -4 * a * a, (1, 0): -F(24)}
    assert all(dt[key] + dzz[key] == 0 for key in dt)
    # At tau=0, F=(z^2-a^2)^2 is positive off +/-a: no additional real brackets.
    assert all(((a + r) ** 2 - a ** 2) ** 2 > 0 for r in (F(2), F(3)))

    record = {
        "date_local": "2026-11-17", "timezone": "America/New_York",
        "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex",
        "model": None, "reasoning_effort": None,
        "status": "Explanatory scalar arithmetic; no new canonical source acquisition",
        "delta": str(DELTA), "incoming_lower_bound": str(ANCHOR_LOWER),
        "anchor_source": "../notes/16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md",
        "threshold_open_interval": [str(threshold_lower), str(threshold_upper)],
        "threshold_meaning": "Unique constant-budget break-even against the stated lower anchor; not a necessary bound on actual K",
        "method": "Exact Fraction arithmetic; alternating exp(-x) Taylor sums through degrees 32 and 33; B decreases strictly in kappa",
        "decimal_displays_are_rounded": True, "rows": rows,
        "controls": {"quadratic_exact_margin": str(quadratic_margin),
                     "quartic_heat_equation_exact": True,
                     "quartic_at_double": "(z^2-a^2)^2; no exterior real zero beyond the target and its reflection",
                     "other_families": "Premise screens in brainstorm note11; their numerical certificates were not rerun"},
        "new_xi_evaluations": 0,
    }
    destination = Path(__file__).with_name("19_VCD_GT_THRESHOLD_DISCUSSION_20261117.json")
    destination.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"record": str(destination), "threshold": record["threshold_open_interval"], "rows": rows}))


if __name__ == "__main__":
    main()
