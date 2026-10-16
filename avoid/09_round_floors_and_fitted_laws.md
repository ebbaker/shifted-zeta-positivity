# Round targets reported as measurements; finite data turned into laws

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A certificate is run against an inserted round floor (\(10^{-26}\),
\(10^{-34}\)) and the floor is reported as the result; a table rounds
certified lower values upward; three or seven data points are fitted to a
law "as \(L\to\infty\)"; a parameter optimized over a few floating samples
is reported as a bound. In each case a number that was chosen, fitted or
sampled is presented as a number that was proved.

## What it looks like here

"Super-exponential decay", a "ceiling ≈ 2.7", a zero-count law, a
sharp-weight constant \(0.1745354\), and understated floors that reversed
a comparison between two papers.

## Evidence

- [Weil-depth v0.2 review](../papers/shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.2_claude/REVIEW_CLAUDE_20260909.md) §4: "The floors \(10^{-26}\) and \(10^{-34}\) are round targets, not measurements".
- [Storage-depth v0.2 review](../papers/shifted-zeta/storage-depth/archive/reviews/REVIEW_storage-depth_v0.2_claude_20260910.md) §0: "the certified floors are understated by four orders of magnitude", which reversed the paper's comparison with record R6.
- [Weil-depth v0.3 review](../papers/shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.3_chatgpt/FINITE_HORIZON_WEIL_V03_REVIEW_20260909.md) §2: "They do not establish an asymptotic law as `L` tends to infinity."; the super-exponential-decay and "ceiling ~2.7" claims were rewritten in v0.4 ([STATUS](../papers/shifted-zeta/weil-depth/STATUS.md)), and the same review's §1 found Table 3 rounding certified lower values upward.
- [Barrier-theorem note](../papers/shifted-zeta/storage-depth/archive/reviews/NOTE_barrier_theorem_and_ladder_conjecture_20260911.md): a zero-count law fitted to three points, "that remark is withdrawn", the same day.
- [Newman certificate audit](../papers/investigations-2/newman_certificate_audit/README.md): the sharp-weight lane's \(\Lambda\approx0.1745\) "is recorded as an option, not pursued", and the [row-replay note](../papers/investigations-2/newman_certificate_audit/notes/3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md) says the bound 0.1745354 "looks reachable" subject to listed work; it is a projection from a few sampled rows, not a certified bound.
- [Paper 1 derivation record](../papers/shifted-zeta/psi-omega-margin/supplementary/DERIVATION_AND_VERIFICATION.md) §4: "The old Theorem 1.3 was vacuous as stated." (the "universal threshold u* ≈ 0.3748/ω" of the earlier concise version).

## What it cost

Both finite-horizon papers restated their main theorems; a withdrawn
remark; a vacuous theorem in a released concise version; readers who
compared R6 to a floor that was four orders of magnitude too low.

## Instead

Report the certified enclosure, not the target it beat; label fitted
laws as fits with their sample size; and say "candidate" for anything
sampled. The weil-depth and storage-depth records now carry two-sided
enclosures for this reason ([result-summaries 02](../result-summaries/02_finite_horizon_certificates.md)), and the [LESSONS_LEARNED](../notes/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md) note's rule to "freeze the depth work" was adopted because depth data were being read as laws.
