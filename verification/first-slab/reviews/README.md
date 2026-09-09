# Referee-round records — first-slab positivity

These are the two adversarial review reports the manuscript went through before
becoming preprint v1.0. Both were produced with language-model assistance under
the author's direction; every constant they cite was recomputed from the
printed definitions of the draft under review, not taken from the primary code.
They are published as part of the audit trail, not as independent peer review.

| File | Date | Draft reviewed | Outcome |
|---|---|---|---|
| `REVIEW_round1_20260831.md` | 31 Aug 2026 | Working draft of 31 Aug | Found: the §4.2 representation false at ω = ½ (by 0.24 against a 3e−4 margin); the kernel bound exactly 2× the sharp value (costing half the headline margin); the positivity horizon ~7 % past log 2; Prop. 4.1's proof not a proof; four gaps in §8; audit/primary certificate discrepancy unexplained. Ten items. |
| `REVIEW_round2_verdict_20260903.md` | 3 Sept 2026 | Response draft of 3 Sept | All ten items resolved and re-verified by recomputation. Four small items left — all folded into v1.0 (see `../CHECKLIST.md`, Part 0). |

Copy the round-1 report verbatim from the project store
(`claude/REVIEW_first_slab_positivity_20260831.md`) into this folder; the
round-2 verdict is included here.

Numbers quoted in the round-1 report refer to the *31 Aug draft* (kernel bound
0.024587, Schur loss 4.0157e−4, margins 3.0965e−4 / 5.2315e−2). The
corresponding v1.0 values are 0.012294, 9.9587e−5, 6.11635e−4 / 5.26167e−2
(certified margins) and 6.1159e−4 / 5.2613e−2 (coercivity constants).
