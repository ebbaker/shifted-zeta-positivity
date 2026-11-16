# Investigations 6 — Tensor networks and recursive Newman representations

**16 November 2026 — Volterra tail-closure program prepared:** Branch 03
now has a [detailed induction overview](03_volterra_coefficient_dynamics/research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md),
[new plan](03_volterra_coefficient_dynamics/research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md),
[sole successor VCD register](03_volterra_coefficient_dynamics/research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md)
and [continuation prompt](03_volterra_coefficient_dynamics/notes/03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md).
Its author-authorized multi-step sessions use bounded Sol 6.1 subtasks
without a mandatory handoff after each task. Setup is not activation;
other branches and parent TN6 statuses are unchanged. Prepared for Edward
Baker with OpenAI Codex assistance, recorded gpt-6-astra/max.

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in this conversation's recorded configurations.

**14 November 2026 — four analytical drafts completed:** Read the [manuscript index and result map](notes/09_ANALYTICAL_MANUSCRIPT_SCOPE_AND_RESULT_MAP_20261114.md), [internal cross-review](reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md) and [current continuation/model handoff](notes/10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md). Each paper develops analytical proofs systematically and ends with outstanding challenges. All reading PDFs and build products are external to the repository. The sole register records TN6-E04 completion.

**14 November 2026 — finite acquisition update:** [TN6-E02](notes/06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md) acquired sixteen complete-source coupling enclosures and nine certified readouts on the fixed low-height domain. Read [round results](notes/07_TN6_FINITE_ACQUISITION_ROUND_RESULTS_20261114.md), [finite-round handoff](notes/08_TN6_CONTINUATION_AND_MODEL_HANDOFF_20261114.md) and the sole register for assessment status. The first-round acquisition limitation below is superseded only within this finite scope; speed and signed-field conclusions remain unestablished.

**14 November 2026 — first research round:** Read the [quantified results](notes/04_FIRST_RESEARCH_ROUND_RESULTS_20261114.md) and [historical first-round handoff](notes/05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md). The four branches now have analytical returns and internal assessment records; the shared coefficient-to-chain transfer gives an explicit sufficient scalar-accuracy depth. These are approximation results; coefficient acquisition, computational advantage and signed-field conclusions remain unestablished. The linked sole registers own live status. Coordinator backend/effort unavailable; workers explicitly dispatched Astra/Ultra for B and Sol 6.1/Ultra for E.

This program explores tensor-network and related quantum methods for the
complete de Bruijn–Newman flow. Its central question is whether the
theta-source wavefunction has a useful recursive structure across height,
imaginary time or resolution. We seek representations that preserve the
literal field and expose manageable coefficients, transport laws or
transfer estimates that might support new proofs.

The [program research overview](research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
explains the common source, the distinct roles of the four branches and
the open mathematical questions. Approximation and exact representation
are complementary parts of the program: finite QTT constructions explore
rank and accuracy, while the other branches study exact infinite chains,
their coefficient dynamics and convergent tensor products.

| Branch | Broad scientific question | Research overview |
| --- | --- | --- |
| [01 — QTT for the Newman flow](01_qtt_newman_flow/README.md) | Can binary-coordinate tensor trains give useful rank, precision and observation-error bounds as height grows? | [QTT overview](01_qtt_newman_flow/research-overview/01_QTT_RESEARCH_OVERVIEW_20261113.md) |
| [02 — Jacobi-chain height flow](02_jacobi_chain_height_flow/README.md) | Can an exact infinite chain generate a useful continuous family of wavefunctions and describe propagation toward higher heights? | [Jacobi-chain overview](02_jacobi_chain_height_flow/research-overview/01_JACOBI_CHAIN_RESEARCH_OVERVIEW_20261113.md) |
| [03 — Volterra coefficient dynamics](03_volterra_coefficient_dynamics/README.md) | Can source-constrained tail responses support degree induction with a Fourier-zero consequence? | [Current induction overview](03_volterra_coefficient_dynamics/research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md) |
| [04 — Exact infinite tensor products](04_exact_infinite_tensor_products/README.md) | Can factors approaching identity provide a manageable exact recursive network, including growing-height and full-source limits? | [Infinite-product overview](04_exact_infinite_tensor_products/research-overview/01_INFINITE_PRODUCTS_RESEARCH_OVERVIEW_20261113.md) |

The exact single-excitation MPS and height-propagation questions belong to
branch 02; theta coefficient relations belong to 03; recursive scale
transfers belong to 04. Finding an invariant or estimate for the signed
boundary amplitude is a shared scientific goal, developed within the
representation that supplies it.

## Setup and continuation

The collection now has a [research plan](research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
in the author's requested `research-overview/` location and a
[sole TN6 shared progress register](research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md).
The plan covers all four workstreams and conditional interfaces. It creates
only shared TN6 tasks; it does not duplicate branch registers or activate research.

**All four branches now have research plans and sole progress registers.**
The subsequent request supersedes the earlier branch-planning deferral.
Branch 01 retains its existing QTT identities; branches 02–04 introduce
distinct JCH, VCD and ITP families. Each begins with a bounded conceptual
decision before a reserved derivation and assessment. At the original setup, research had not
started and no execution packet was issued. That dated state is superseded
by the research round linked above. The subsequent
[parallel continuation authorization](notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
selects **Astra / Ultra** for coordination and B tasks and **Sol 6.1 /
Ultra** for E tasks. Begin all four lanes on continuation and proceed to
the next ready task without renewed permission, retaining task limits,
frozen requests and actual dependency checks.

| Branch | Plan | Sole progress register |
| --- | --- | --- |
| 01 — QTT | [QTT plan](01_qtt_newman_flow/research-plan/01_QTT_RESEARCH_PLAN_20261113.md) | [QTT progress](01_qtt_newman_flow/research-progress/01_QTT_RESEARCH_PROGRESS_20261113.md) |
| 02 — Jacobi chain | [JCH plan](02_jacobi_chain_height_flow/research-plan/01_JACOBI_CHAIN_RESEARCH_PLAN_20261113.md) | [JCH progress](02_jacobi_chain_height_flow/research-progress/01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md) |
| 03 — Volterra coefficients | [VCD plan](03_volterra_coefficient_dynamics/research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md) | [Sole VCD progress](03_volterra_coefficient_dynamics/research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) |
| 04 — Infinite products | [ITP plan](04_exact_infinite_tensor_products/research-plan/01_INFINITE_PRODUCTS_RESEARCH_PLAN_20261113.md) | [ITP progress](04_exact_infinite_tensor_products/research-progress/01_INFINITE_PRODUCTS_RESEARCH_PROGRESS_20261113.md) |

- [Shared continuation note and branch prompts](notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md).
- [Source and ownership crosswalk](notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md).
- [Reference ownership](references/README.md), [shared notes](notes/README.md),
  [brainstorm](brainstorm/README.md) and [milestones](DRAFT_HISTORY.md).

The [first brainstorm](../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
and [exact-height discussion](../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
remain the inherited sources. Their representation identities, floating
pilot and same-assistant checks keep their original evidence levels.
No theta-specific coefficient asymptotic, signed Green estimate or new
zero exclusion is established by this setup.

The complete source and existing Green observations retain their home in
[Investigation 5/09](../investigations-5/09_green_potentials_newman_flow/README.md).
The founding conversation keeps its unique
[Investigation 5 archive](../investigations-5/chat-histories/README.md).
New branch-only chats use the branch's history folder; new shared chats
use [this collection's folder](chat-histories/README.md).

Follow the [setup workflow](../../INVESTIGATION_SETUP_WORKFLOW.md), with
the author's parent-plan location and subsequent branch-planning request above, the
[result index](../../result-summaries/README.md) and
[avoid index](../../avoid/README.md). The
[program overview](research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
links the applicable control and classification rules.
