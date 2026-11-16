# Volterra coefficient dynamics

**Three collision-control sub-investigations, 16 November 2026, chat0004:**
the routes from [discussion28](notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
now each have a README and research overview. Edward selects the first
for initial setup; branch research plans and progress files are deferred
until each investigation starts. Prepared for Edward Baker with OpenAI
Codex assistance; actual model/effort unavailable. Existing VCD-B07/E25
retain their status and ownership.

| Route | Entry point | Current stage |
| --- | --- | --- |
| 1. Signed gap transport in physical heat time | [Cluster gap transport](01_cluster_gap_transport/README.md) | First choice; [setup continuation](01_cluster_gap_transport/notes/01_VCD_GT_SETUP_CONTINUATION_20261116.md) ready |
| 2. Contraction of nonreality under degree refinement | [Degree induction](02_degree_nonreality_contraction/README.md) | Overview only; individual planning deferred |
| 3. Averaged bounds across resolution scales | [Multiscale collision bounds](03_multiscale_collision_bounds/README.md) | Overview only; individual planning deferred |

**Cluster-resolution discussion, 16 November 2026, chat0004:** [note27](notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md) develops the author's unresolved-pair idea in manuscript §10.4: compact convergence uniform in heat time, error bounds for the pair center and squared separation, and shrinking uncertainty near a stipulated fixed double event. §5.3 now explicitly says polynomial phase does not count F zeros. [Assessment11](reviews/11_VCD_CLUSTER_RESOLUTION_ASSESSMENT_20261116.md) is same-assistant checking; no collision exclusion or growing-domain result. B07 unactivated/E25 unissued. For Edward Baker with Codex assistance; actual model/effort unavailable.

**Fixed-zero discussion, 16 November 2026, chat0004:** [note26](notes/26_VCD_FIXED_ZERO_STABILIZATION_AND_PHASE_20261116.md) records manuscript Proposition 10.2 and Corollary 10.3: isolated clusters stabilize, and a fixed simple real zero has an alternating displacement asymptotic with successive ratio O_r(log²(N+1)/N²). The statement is conditional on the chosen limiting zero and is not uniform over increasing zero index. [Assessment10](reviews/10_VCD_FIXED_ZERO_COROLLARY_ASSESSMENT_20261116.md) is same-assistant checking. B07 remains ready/unactivated and E25 unissued. For Edward Baker with Codex assistance; actual model/effort unavailable.

**Analytical manuscript expanded, 16 November 2026, chat0004:** the [reading guide and editable manuscript](manuscript/README.md) now develop the source, Jacobi readouts, complete signed error, quantitative phase estimate and conditional zero geometry systematically. [Integration25](notes/25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md) maps the existing results and new background derivations; [assessment09](reviews/09_VCD_READOUT_MANUSCRIPT_ASSESSMENT_20261116.md) is a same-assistant check. The reading PDF is under ignored root output. B07 remains unactivated; no canonical zero confinement is proved. For Edward Baker with Codex assistance; actual model/effort unavailable.

**Current signed-error research, 16 November 2026, chat0003:** B06 selected a directed enclosure for the complete E15 error and completed E21/E22/E24 with [E23 internal acceptance](reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md). [Synthesis23](notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md) records the explicit phase budget, real parity brackets, coefficient-cost comparison and conditional zero/count consumers. A canonical model margin and zero count remain open; the phase estimate also holds for the stated collision controls. [Register02](research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) and [continuation03](notes/03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md) route B07. For Edward Baker with Codex assistance; lead actual settings unavailable, fixed helpers explicitly Sol6.1/ultra. Earlier setup/B04/B05 paragraphs are historical.

**16 November 2026 — tail closure and degree induction:** the new
[research overview](research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md),
[research plan](research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md),
[sole live VCD register](research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md)
and [starting continuation prompt](notes/03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md)
develop the source-constrained omitted-tail program. Edward authorizes
substantial multi-step lead sessions at ultra with Sol 6.1 subtasks;
individual work packets remain bounded, while their completion does not
force a user handoff. The first connected research session is completed within its recorded scope; see the [session synthesis](notes/09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md) and current register for assessed findings and the next open task.
Setup was prepared for Edward Baker with OpenAI Codex assistance; actual setup
configuration gpt-6-astra/max, distinct from requested future settings.

**Historical midpoint extension and archive repair, 16 November:** the current
overview/plan/register also investigate the intermediate-mode amplitude
sum. B04 remains the next decision, E12 its reserved proof, and E13 is
ready fixed support; completed research and control scopes are preserved.
Chat0001's missing public replies were recovered through the repaired
recorder. See the [update receipt](numerics/06_VCD_ARCHIVE_AND_MIDPOINT_UPDATE_20261116.json).
Prepared for Edward Baker with Codex assistance, recorded revision
gpt-6-astra/max; this update executes no new research task.

13 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual backend model and effort are unavailable
in recorded configurations.

Explore the nonlinear lattice of orthogonal-polynomial recurrence coefficients generated by the complete Newman source. The broad question is which special relations, growth estimates or invariants the theta initial data impose on the classical Volterra deformation.

This branch owns the moving polynomial basis, its recurrence coefficients,
and the source-constrained tail-closure induction developed here. Branch
02 retains fixed-initial-basis transport and its JCH results; branch 04
owns exact scale products. No sibling task or status is transferred.

The [founding research overview](research-overview/01_VOLTERRA_RESEARCH_OVERVIEW_20261113.md) gives the fixed
source, inherited identities, mathematical domains, evidence and open
questions. See the [program overview](../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
for the common purpose and relationships among all four branches.

**Research planning added 13 November 2026.** At the author's subsequent
request, the branch received its [first-round plan](research-plan/01_VOLTERRA_RESEARCH_PLAN_20261113.md)
and [historical progress record](research-progress/01_VOLTERRA_RESEARCH_PROGRESS_20261113.md).
The successor register linked above now owns live VCD status.
VCD-B01 selected the logarithmic coefficient envelope with a normalized
monic norm-product consumer. E01 [proves the estimate](notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md)
for every degree and \(0\le\lambda\le1/2\), and E02
[accepts it in a same-worker assessment](reviews/01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md).
Both weighted-square controls also satisfy the bound at their known
collisions. The inherited coefficient equation remains the starting point.

- [Analytical manuscript](manuscript/README.md) and [internal manuscript
  assessment](reviews/02_VCD_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md),
  14 November 2026. The draft derives the exact coefficient dynamics,
  the logarithmic envelope and its fixed-chain scalar consequence.
- [Current branch continuation and activation prompt](notes/03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md);
  [historical shared setup/branch prompts](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md).
- [Source and ownership crosswalk](../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md).
- [References](references/README.md), [chat routing](chat-histories/README.md)
  and [setup milestone](DRAFT_HISTORY.md).
- Working locations: [notes](notes/README.md),
  [conceptual decisions](brainstorm/notes/README.md),
  [numerics](numerics/README.md), [reviews](reviews/README.md),
  [plan guide](research-plan/README.md) and
  [progress guide](research-progress/README.md).

The [parent plan](../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
and [TN6 register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
own shared interfaces only; they do not duplicate VCD status.

The [founding discussion](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
and its existing chat archive remain in Investigation 5. Future branch-only
research belongs here. Follow the [setup workflow](../../../INVESTIGATION_SETUP_WORKFLOW.md)
and return to the
[collection index](../README.md) for sibling navigation.

**Parallel continuation, 13 November 2026:** the
[canonical note](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
records Edward Baker's authorization to proceed into the next ready task
without renewed permission, using Astra / Ultra for B tasks and Sol 6.1 /
Ultra for E tasks. Frozen requests, finite limits and prerequisites remain.

The 16 November plan preserves completed requests and adds the author's
explicit sustained-session policy for the new phase. Its live register
contains the ownership/task crosswalk; the earlier plan/register are
historical, not competing current instructions.
