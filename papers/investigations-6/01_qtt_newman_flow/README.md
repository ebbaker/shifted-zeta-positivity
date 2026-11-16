# Quantics tensor trains for the Newman flow

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in recorded configurations. Model recommendations
below describe future work, not this session's provenance.

Branch **01** of [Investigations 6](../README.md) asks whether QTT
representations of the complete theta-source wavefunction can give useful
rank, precision and observation-error estimates under Newman imaginary-time
evolution, including increasing-height approximation families.

Within the expanded [program overview](../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md),
this is the finite QTT approximation branch. Siblings study
[exact chain evolution](../02_jacobi_chain_height_flow/README.md),
[coefficient dynamics](../03_volterra_coefficient_dynamics/README.md) and
[infinite products](../04_exact_infinite_tensor_products/README.md).
The existing QTT plan and task ownership below are retained.

The subsequent collection-wide branch-planning request reuses this branch's
existing plan and sole register. Shared interfaces are described in the
[parent plan](../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
and owned by the [TN6 register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md).
They are not prerequisites for QTT-B01.

**The first QTT round is complete.** E01 [proves a formal rank cap of 641
and scaled absolute error below 2^-36](notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md)
on the prescribed compact box. E02
[accepts the proof in a same-worker assessment](reviews/01_QTT_E02_RANK_ERROR_ASSESSMENT_20261114.md).
The matched scalar integral has a smaller allowance because it omits
midpoint error. The [opening brainstorm](../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
retains its exploratory tensor formulas, floating pilot and low-rank
collision control.

- [Analytical manuscript](manuscript/README.md) and [internal manuscript
  assessment](reviews/02_QTT_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md),
  14 November 2026. The draft derives the formal fixed-box bound and
  identifies remaining coefficient acquisition, precision, growing-height
  and signed-observation problems.
- [Scientific overview](research-overview/01_QTT_RESEARCH_OVERVIEW_20261113.md):
  fixed source, clock, tensors, observations, inherited evidence and controls.
- [Bounded research plan](research-plan/01_QTT_RESEARCH_PLAN_20261113.md):
  conceptual selection before a specified derivation and assessment.
- [Sole live QTT progress register](research-progress/01_QTT_RESEARCH_PROGRESS_20261113.md).
- [Continuation note and pasteable prompt](notes/01_QTT_CONTINUATION_AND_PROMPT_20261113.md).
- [Source/ownership crosswalk](notes/02_QTT_SETUP_AND_SOURCE_CROSSWALK_20261113.md),
  [references](references/README.md), [chat routing](chat-histories/README.md)
  and [milestones](DRAFT_HISTORY.md).

Future derivations go in [notes](notes/README.md), conceptual decisions in
[brainstorm/notes](brainstorm/notes/README.md), permitted computations in
[numerics](numerics/README.md), and assessments in [reviews](reviews/README.md).
The [root setup workflow](../../../INVESTIGATION_SETUP_WORKFLOW.md) and
its reference, size, evidence and chat-history rules apply.

**Parallel continuation, 13 November 2026:** the
[canonical note](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
records Edward Baker's authorization to proceed into the next ready task
without renewed permission, using Astra / Ultra for B tasks and Sol 6.1 /
Ultra for E tasks. Frozen requests, finite limits and prerequisites remain.
