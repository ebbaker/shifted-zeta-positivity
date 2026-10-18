# Draft history: Arithmetic constraints at collision scale

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

Keep entries concise: date, project, source path or commit/tag, why the
version matters, and supporting notes or reviews. Detailed research history
belongs in those sources; create no new manuscript snapshot folders.

- **18 October 2026 — project 11 exploratory initialization.**
  Source identity: [initial exploratory proposal](research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md).
  Establishes the research question, opening round, controls and criteria for
  progress from the [candidate discussion][candidates] and [shared plan][overview].
  No research result or manuscript milestone; no independent review.
  Prepared for Edward Baker with LLM assistance, **gpt-6-astra (Codex), max**.

- **18 October 2026 — project 11 opening research round.**
  Source paths: [packet matching](notes/02_COMPLETE_PACKET_MATCHING_CODEX_20261018.md)
  and [finite-prime controls](notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md).
  Extends the high-gap collision construction to complete prime orbits and
  finite exact linear tests; isolates the missing full-reflection input.
  [Self-review with hashes](reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md)
  and [bounded checks](numerics/README.md). No manuscript or snapshot created.
  Prepared for Edward Baker with LLM assistance, **gpt-6-astra (Codex), max**.

- **18 October 2026 — project 11 positive packet continuation.**
  Source: [positive packets and modular cancellation](notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md).
  Uniform relative {2,3} arithmetic-tail error below 7.3e-25 and a carrier
  payment below 117 E; the signed residual remains open.
  [Self-review and source hashes](reviews/02_POSITIVE_PACKET_AND_MODULAR_CANCELLATION_SELF_REVIEW_CODEX_20261018.md).
  No manuscript snapshot or commit created. Prepared for Edward Baker with
  substantial LLM assistance, **gpt-6-astra (Codex), max**.

- **18 October 2026 — project 11 self-contained manuscript milestone.**
  Canonical source: [Positive Arithmetic Packets for the Theta Heat Flow](manuscript/positive_arithmetic_packets/main.tex).
  The 23-page draft consolidates complete packet algebra, positive carriers,
  modular cancellation and scoped collision controls; adds a self-contained
  reflection-rigidity proof and rational constant-enclosure recipe.
  [Manuscript self-review](reviews/03_MANUSCRIPT_SELF_REVIEW_CODEX_20261018.md)
  and [build/source record](manuscript/positive_arithmetic_packets/BUILD_RECORD.json).
  Signed theta residual still open; no independent review or Git commit.
  Drafted for Edward Baker with LLM assistance, **gpt-6-astra, max**.

[candidates]: ../brainstorm/notes/03_NEW_FIXED_FUNCTION_PROJECTS_CODEX_20261018.md
[overview]: ../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md

- **18 October 2026 — project 11 review and quantitative continuation.**
  [Note 05](notes/05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md)
  gives broad-strip positivity and the E/64 carrier payment;
  [Note 06](notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md)
  supplies a cancellation-preserving finite approximation and scoped roadmap.
  [Review 04](reviews/04_MANUSCRIPT_AUDIT_AND_STRENGTHENING_REVIEW_CODEX_20261018.md)
  and [scalar checks](numerics/STRIP_CARRIER_CHECKS_20261018.json).
  Manuscript unchanged; no new snapshot or commit. For Edward Baker with
  LLM assistance, **gpt-6-astra, ultra**, same-model internal review.

- **18 October 2026 — project 11 strengthened manuscript and Sol plan.**
  [Current source](manuscript/positive_arithmetic_packets/main.tex), source-set
  `f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`: 30 pages incorporating the E/64 carrier payment,
  complex-strip estimates and cancellation-preserving shifted approximation.
  [Integration review](reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md) and
  [detailed future Sol plan](research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md).
  Internal LLM checks only; no collision exclusion, new bound, snapshot or
  Git commit. For Edward Baker with LLM assistance, **gpt-6.1-sol, ultra**,
  coordinated and edited by **gpt-6-astra, ultra**.

- **18 October 2026 — overview 02 bounded evaluator and signed certificate.**
  [Research notes](notes/02_updated_research_plan/README.md),
  [claim ledger](numerics/FINAL_CLAIM_LEDGER_20261018.json) and
  [closure review](reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md).
  Complete interval evaluator and L0>E/100 on the known pilot rectangle;
  performance gate failed and global finite bridge unclosed. Manuscript
  sources unchanged; no new bound or snapshot. For Edward Baker with LLM
  assistance, **gpt-6.1-sol, actual effort max**, same-assistant internal review.

- **18 October 2026 — overview 02 effective nonstationary contour tail.**
  [Note 11](notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md) improves the omitted-mode
  error by log(x)/x, gives explicit uniform onset constants, and measures
  retained point-quadrature costs at heights 1000 and 10000.
  [Review 10](reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md) and [reproducible records](numerics/README.md).
  Manuscript pin unchanged; no new snapshot, commit or Newman bound.
  For Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
  actual effort ultra**, with parallel same-model checks.

- **18 October 2026 — overview 02 finite signed and vertical wall consumer.**
  [Notes 12–13](notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md) and
  [Review 11](reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md) close E>0 on [1/100,1/5] × [-1001,1001]
  using a complete wall, named published initial verification and heat
  splitting; the new arithmetic tail is consumed. [Code and ledger](numerics/high_height_consumer/README.md).
  Timing gate fails; exterior bridge remains open. No manuscript snapshot,
  Git commit or new Newman bound. For Edward Baker with substantial LLM
  assistance, **gpt-6.1-sol, actual effort ultra**, internal same-model review.

- **18 October 2026 — overview 02 sharper exterior and final round summary.**
  [Note 14](notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md),
  [replay source identities](numerics/analytic_continuation/ANALYTIC_CONTINUATION_REPLAY_20261018.json),
  [Review 12](reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md)
  and [separate whole-round summary](research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md).
  Explicit real exterior exp(20/epsilon), A/x contour tail and scoped
  remote control; slab gap reduced to (1001,exp(2000)), still open.
  Manuscript pin unchanged; no new snapshot, commit or Newman bound.
  For Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
  actual effort ultra**, with parallel same-model checks.

- **18 October 2026 — project 11 current-results manuscript integration.**
  [Current source](manuscript/positive_arithmetic_packets/main.tex), source-set
  `2690c3052927702a7f25d7e0519cc8ae10abfd202ac891bb8c06208eaa9a7b0c`: 45 pages incorporating the complete overview 02 round,
  finite-height exclusion and exp(20/epsilon) exterior, with the open bridge
  explicit. [Review 13](reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md),
  [fresh replay](numerics/MANUSCRIPT_INTEGRATION_REPLAY_20261018.json) and
  [round summary](research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md).
  For Edward Baker with substantial LLM assistance, **gpt-6-astra, actual
  effort max**; internal integration review. No new bound, snapshot or commit.

- **18 October 2026 — project 11 symmetry program organization.**
  [Overview 03](research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md)
  and [six direction guides](symmetries/README.md) consolidate the four
  brainstorm directions and the covariant-jet/Hodge continuation from
  [Note 07](notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md) and
  [Review 14](reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md).
  Bounded tasks and decision rules; program setup, no new estimate or
  manuscript snapshot. For Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**.
