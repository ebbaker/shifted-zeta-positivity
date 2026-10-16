# Normalization, factor-of-two, endpoint and constant slips

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

Two papers use different support-length conventions; \(\xi\) means two
different things; a boxed representation is false at an endpoint; a
kernel bound is twice the sharp value; a constant is off by orders of
magnitude; a PDF extraction drops overbars; a formula misses a square
root. Each is a small slip, and in a program whose certified margins are
\(10^{-4}\) to \(10^{-28}\), a factor of two is not small.

## What it looks like here

Comparisons across papers made before reconciling conventions; "250 orders
of magnitude" discrepancies that are a factor of two; certified margins
compared against numbers computed in another normalization.

## Evidence

- [Frame-bound note](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/FRAME_BOUND_AND_THE_DENSITY_20260917.md) §1.3: "Both statements are wrong, and the cause is the factor of two."
- [First-slab round-1 review](../early-chat-logs/initial-project-files/rh3/claude/REVIEW_first_slab_positivity_20260831.md): "§4.2's boxed representation is false at ω = 1/2, by a quantity three orders of magnitude larger than the certified margin"; the kernel bound was "exactly twice the sharp Schur value", which cost half the headline margin.
- [First-slab checklist](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/CHECKLIST.md): a display "overstated the form by ½|∫f|² ≈ 0.24 … against a certified margin of 6.1e−4".
- [ROUND10](../early-chat-logs/initial-project-files/rh3/claude/ROUND10_boundary_data.md): "the constant was wrong by five orders of magnitude"; [ROUND6](../early-chat-logs/initial-project-files/rh3/claude/ROUND6_closeout.md): "that is the entire log 2".
- [Storage-depth v0.2 review](../papers/weil-positivity/shifted-zeta/storage-depth/archive/reviews/REVIEW_storage-depth_v0.2_claude_20260910.md): "floors are understated by four orders of magnitude".
- [CCM README](../papers/investigations/ccm-operator-realizations/README.md): "The literal-k normalization Xi/4 is corrected in two earlier supporting notes."; the [fractional-dimension trap list](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/notes/NEW_SESSION_PROMPT.md): "xi MEANS TWO DIFFERENT THINGS".
- [Short-family small-cofactor review](../papers/quasi-rh/quasi-rh-exponent-descent/reviews/SHORT_FAMILY_SMALL_COFACTOR_REVIEW_20261008.md): "the plain PDF extraction dropped overbars", so the "normalization was wrong".
- [Weil-depth v0.3 review](../papers/weil-positivity/shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.3_chatgpt/FINITE_HORIZON_WEIL_V03_REVIEW_20260909.md) §4: Lemma 3.3, "This is false for `p-beta`." (one local step corrected in v0.4); the [20 note](../papers/investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md): the 2017–18 spin-trace construction gave \(\cosh\), not the heat semigroup, "Equation (33) misses the square root."

## What it cost

Half a headline margin; a withdrawn gap law and a withdrawn "250 orders"
discrepancy; restated theorems in two finite-horizon papers; the C1
normalization check against Suzuki still open as "the single highest-risk
unverified item".

## Instead

Reconcile conventions before comparing ([program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md) §2: "Factors of two in support length differ between papers; comparisons must first reconcile…"); check endpoints of every boxed formula explicitly; recompute every imported constant once in a second normalization; "check object type" and "read the printed PDF" (house rules in [`CONTRIBUTING.md`](../CONTRIBUTING.md)); and keep a conventions block at the top of every investigation, as 22's manuscript does for its heat normalization.
