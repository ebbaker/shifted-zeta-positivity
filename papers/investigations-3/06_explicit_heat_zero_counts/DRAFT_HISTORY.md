# Draft history: Explicit heat zero counts

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

The baseline below was subsequently accepted by cross-model Review 02;
its historical creation entries remain unchanged. The new round-2
continuation has same-model checks only. The [initial proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
records the 16 October 2026 setup, model assignments and phase gates.

For future milestones, add only the date, investigation, commit/tag or
source identity, why the version matters, and links to supporting notes
and reviews. Detailed research history stays in those sources. Create no
new manuscript snapshot folders.

- **17 October 2026 — opening research ledger (no manuscript milestone).**
  Source identity: [Note 01](notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md), with its
  reviewed SHA-256 in [Review 01](reviews/01_OPENING_LEDGER_REVIEW_CODEX_20261017.md).
  Records the inactive consumer gate, a conditional count reduction and
  the unresolved off-axis cutoff; [arithmetic record](numerics/LOCAL_COUNT_REDUCTION_CHECKS_20261017.json).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.

- **17 October 2026 — round 2, unreviewed analytic development.**
  Source identity: [Note 02](notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md), SHA-256 in its
  [arithmetic record](numerics/OFF_AXIS_COMPARISON_CHECKS_20261017.json). Derives an explicit
  time-uniform local count for X>=2,000,000 and closes the off-axis
  constant obligations on that restricted domain. Review deferred at the
  user's request; no accepted manuscript milestone. **gpt-6.1-sol, ultra**.

- **17 October 2026 — first working manuscript, explicit heat zero counts.**
  Source identity: [current source](manuscript/explicit_heat_zero_counts.tex)
  and [PDF](manuscript/explicit_heat_zero_counts.pdf), hashes in the
  [build record](manuscript/BUILD_RECORD.json). Assembles
  [Note 01](notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md) and
  [Note 02](notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md)
  into a compiled 11-page draft with the explicit restricted-domain count.
  Review remains deferred; [Review 01](reviews/01_OPENING_LEDGER_REVIEW_CODEX_20261017.md)
  covers only its opening note. Drafted for Edward Baker with substantial
  LLM assistance, **gpt-6.1-sol, ultra**. No accepted manuscript milestone.

- **17 October 2026 — baseline review accepted; bounded continuation.**
  Baseline source commit `146b3f9`; cross-model review commit `001aaeb`,
  [Review 02](reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
  Original theorem: proved from named imports, one cross-model LLM review,
  X>=2000000. [Round-2 Note 01](notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md)
  lowers the cutoff to 100000 and gives 0.9 log(X+2)+6; source identity in
  its [execution record](numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json),
  [same-model assessment](reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md).
  The user requested this bounded continuation after review; the new proof
  has no cross-model review and is not a new manuscript milestone.
  Manuscript integration and consumer tolerance remain pending.
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol (Codex), ultra**.

- **17 October 2026 — round-2 manuscript integration.**
  [Current manuscript](manuscript/README.md), source/PDF identities in its
  [build record](manuscript/BUILD_RECORD.json); earlier manuscript at
  commit `146b3f9`. Includes the X>=100000 count, high-height corollary,
  complete two-regime proof and Review 02's editorial corrections.
  [Round-2 note](notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md),
  [same-model assessment](reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md).
  This working revision has same-model checks only; cross-model review
  of the extension remains pending. Drafted for Edward Baker with substantial
  LLM assistance, **gpt-6.1-sol (Codex), ultra**. No snapshot folder.
