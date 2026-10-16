# Same-model reviews and shared-premise checks treated as independent

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

The model that wrote a manuscript reviews it, often the same day, and the
review is filed as validation. Two extractions of the same source by the
same kind of system agree and the agreement is filed as a check. A saved
`PASS` string is trusted without being bound to the data it describes.
Because every round shares the premises, these checks are blind to premise
errors, and a wrong "fact" can travel through several reviews before a
different system reads the source.

## What it looks like here

Review folders with ten or fifteen entries by one assistant; "verified"
labels on manuscripts no other system has read; normalization checks
against Suzuki that are still the highest-risk open item after two months.

## Evidence

- [YM cross-model verification](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md): "The earlier reviews were all produced by the same assistant that wrote the manuscript (GPT-6 Codex); this is the first assessment from a different system." It needed errata.
- [WZW assessment](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/WZW/reviews/review_claude_wzw_program_assessment_20260924.md): "All ten reviews are same-assistant audits".
- [External review 12 of project 17](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md): "Internal Reviews 2–5 are same-model restatements."
- Fact (D) about Polymath 15 passed through two Claude reviews and brainstorm rule R5 before the [cross-assessment](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md) §3.1 read the source: "Fact (D) is not what Polymath 15 proves".
- [Protocol C1/C2](../verification/first-slab/PROTOCOL_C1_C2.md): "Two LLM extractions agreeing is not independence — they share failure modes."; [`verification/README.md`](../verification/README.md): rounds are "blind to premise error, because every round shares the premises".
- [Weil-depth v0.2 review](../papers/weil-positivity/shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.2_claude/REVIEW_CLAUDE_20260909.md): "The analyzer trusted a saved `PASS` string without binding it to the actual matrix archive."
- [Parallel-plan review](../papers/investigations-2/brainstorm/reviews/REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md): "The first cross-family pass on the Newman audit was Codex's response, and it found the slack error" (a claimed tolerance of "several hundred" was really \(\times1.497\)).
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §3: "fifteen reviews by the same coordinating model, of material produced on the same day, are not independent review".

## What it cost

Errata on the YM manuscript; a wrong Polymath fact in two reviews and a
rule; a corrected audit order with correction blocks across two folders;
the first-slab normalization check C1 and the human checklist still open.

## Instead

Label every review with its model and whether it is same-model or
cross-model, as the [investigations-2 README](../papers/investigations-2/README.md) asks ("Distinguish internal LLM checks from independent review"); route every manuscript through at least one cross-model round before any status word stronger than "working draft"; bind a `PASS` to the hash of what passed; and keep the human-verification columns of the [blueprint](../blueprint/first-slab/statements.md) in view. No result in this repository has had independent specialist human review, and the result summaries say so.
