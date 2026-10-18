# Draft history: Sharp finite-sum bounds

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

No reviewed manuscript milestone exists. An unreviewed working draft was
added at the user’s request on 17 October 2026. The [initial proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
records the 16 October 2026 setup, model assignments and phase gates.

For future milestones, add only the date, investigation, commit/tag or
source identity, why the version matters, and links to supporting notes
and reviews. Detailed research history stays in those sources. Create no
new manuscript snapshot folders.

## Working manuscript

- **17 October 2026 — investigation 02, sharp finite-sum bounds:**
  [canonical source](manuscript/sharp_finite_sum_bounds/main.tex),
  [compiled draft](manuscript/sharp_finite_sum_bounds/sharp_finite_sum_bounds.pdf)
  and [build identity](manuscript/sharp_finite_sum_bounds/BUILD_RECORD.json).
  User-requested unreviewed assembly of the native sharp binding, four-leg
  strip transfer, first-window margin and revised infinite tail; remaining
  floors and conditional conclusion are explicit. Supporting
  [Note 01](notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
  and [Note 02](notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md).
  Drafted for Edward Baker with substantial **gpt-6.1-sol (Codex), ultra**
  assistance. Internal authoring checks only; formal reviews remain pending.
  No snapshot or accepted manuscript milestone.

- **18 October 2026 — investigation 02, Section 7 (activation along a leg):**
  the same [source](manuscript/sharp_finite_sum_bounds/main.tex),
  [compiled draft](manuscript/sharp_finite_sum_bounds/sharp_finite_sum_bounds.pdf)
  and [build identity](manuscript/sharp_finite_sum_bounds/BUILD_RECORD.json),
  edited on top of commit `72a149d`; the commit that records this change is
  still to be added here. Adds the activation lemma, the bound for the
  activation sums, the mesh criterion and a floating planning table of twenty
  rows, which reduce the open finite floors to a finite certificate that has
  not been produced; updates the abstract, draft status, Section 8,
  Appendix A, acknowledgements and bibliography. Sources: §3 of the
  [round-one cross-model review](reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md)
  and the [planning record](numerics/round-1/claude-review/ACTIVATION_PLAN_CLAUDE_20261018.json).
  Drafted for Edward Baker with LLM assistance, **Claude Opus 5.5**
  (`claude-opus-5-5`), Claude Cowork, effort **max**; same-model checks only.
  No accepted manuscript milestone or new Newman bound.

## Research execution record

- **17 October 2026 — sharp finite-sum bounds, round one:**
  [source ledger](notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
  and [numerical records](numerics/round-1/README.md). One sharp row and a
  revised all-index tail budget at t=0.157 are enclosed; automatic reuse of
  the plain transfer is disproved for a generic signed-sum class. Uniform
  theta strip transfer and complete finite coverage remain open. Prepared
  for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex)**,
  effort **ultra**. No manuscript milestone, snapshot or new Newman bound.

- **17 October 2026 — bounded gate implementation:**
  [continuation](notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
  and [combined gate record](numerics/round-1/SHARP_Y_TRANSFER_COMPLETION_RECORD_20261017.json).
  Full four-leg normalized sharp-weight strip transfer is certified by
  outward arithmetic plus the stated analytic cases; remaining finite
  floors/coverage are open. **gpt-6.1-sol (Codex), ultra**, substantial LLM
  assistance for Edward Baker, same-model checks. No manuscript milestone
  or new Newman bound.
