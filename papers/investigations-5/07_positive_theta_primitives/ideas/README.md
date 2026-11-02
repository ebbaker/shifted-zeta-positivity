# Parallel research ideas for Jensen hyperbolicity

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task J-E04.

Five note folders separate the directions developed in the [higher-order and radial-flow assessment](../jensen/notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md). They are organized for separate discussions and parallel development. The [Jensen progress register](../jensen/research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) remains the sole source of live task status; this index describes the questions and their connections.

The folders are under **`jensen/notes/`**, where the originating assessment and coefficient work live. The investigation-level `notes/` folder retains shared tools for Jensen and spectral Laguerre. Existing Notes01–14, certificates, reviews, and chat identities remain at their original paths.

**Next session:** use [Continuation15](../jensen/notes/15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md) to evaluate all five branches in parallel, then save a comparative review and give Edward Baker a high-level chat summary. The packet defines worker ownership, evidence requirements and deliverables; evaluation has not started. Prepared 1 November 2026, **gpt-6-astra / xhigh**.

## The five directions

| Direction and note folder | Question | First conceptual task |
| --- | --- | --- |
| [01 Higher order signed averaging](../jensen/notes/01_higher_order_signed_averaging/README.md) | Can coordinatewise monotonicity of the higher-order signed observable transfer the positive k=0 anchor to every k? | **J-B05:** select a sufficient condition for the full r=4 observable, retaining separated-node and endpoint obligations. |
| [02 Determinant order induction](../jensen/notes/02_determinant_order_induction/README.md) | Can strict log-concavity across neighboring coefficient indices propagate determinant positivity to the next order? | **J-B06:** select an estimate for the complete normalized order-raising balance, beginning with r=3 and k>=1. |
| [03 Conservative flows and negative mass](../jensen/notes/03_conservative_negative_mass_flows/README.md) | Can a flow preserve a determinant integral while forcing its total negative mass to zero? | **J-B04, retained:** select a theta-specific conservative flux and decay estimate for the r=4,k=1 mechanism pilot. |
| [04 Paired source and test deformations](../jensen/notes/04_paired_source_test_deformations/README.md) | Can a paired deformation preserve the required moments or determinant and make a concrete signed estimate easier? | **J-B07:** choose one deformation and consumer, retaining all forcing, boundary and inverse-comparison terms. |
| [05 Source flows and Jensen hyperbolicity](../jensen/notes/05_source_flows_and_jensen_hyperbolicity/README.md) | Can a source-changing path induce a proved hyperbolicity-preserving polynomial evolution leading to theta? | **J-B08:** choose a reflection-compatible candidate and identify its exact moment/root-preservation obligation. |

These are **B — conceptual tasks, recommended for Astra**, because the missing estimates or generators are not fixed. Sol is the default recommendation for subsequent E tasks once a method, finite scope and acceptance test are specified. The author selects the actual model and effort. Folder numbering groups ideas; it does not impose an execution order. This organization creates no agents, chats, schedules or running research tasks.

## How the branches can proceed in parallel

Directions 01 and 02 are independent coefficient arguments. The first compares normalized averages across k at fixed r; the second uses neighboring-index log-concavity to raise r. Success in one may help the other, but neither is an assumed prerequisite.

Direction 03 is the author's asymptotic-positivity proposal. Its invariant is the complete determinant integral, and its target is total negative mass, not pointwise decay. Pure transport cannot remove negative mass; ordinary heat supplies a sign-dependent benchmark. A new theta estimate is required.

Direction 04 develops an alternative representation with a specified consumer. It may support 01, 02 or 03. Its initial question can proceed independently, provided it names the determinant or observable whose estimate it aims to improve.

Direction 05 changes the coefficient sequence and therefore needs a root-preservation or return theorem. It cannot use conservation of the original determinant as its transfer argument. The recorded failure of one radial transport remains restricted to that family.

The spectral Laguerre route remains separately organized in [spectral_laguerre/](../spectral_laguerre/README.md). This index does not change its tasks. A tool’s use in a second route requires an explicit mathematical transfer.

## Common baseline and research standards

The [accepted order-three review](../jensen/reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) establishes the global canonical source signs and normalized index comparison within internal same-model assessment. Note14 gives conditional extensions and scoped flow comparisons with same-assistant checking. None of the new folders establishes a higher-order theta sign.

Keep \(D_{r,k}=\det[c_{k+j-i}]\), \(c_n=b_n/(2n)!\), and \(\gamma_n=n!c_n\) distinct from raw moment Hankel matrices and Jensen degree/shift. The easy identity \(D_{r,0}=c_0^r\) is not all-degree Jensen hyperbolicity at shift zero. Any all-order argument must cover the omitted small-index regime, preserve all needed endpoint terms, and justify the selected-minor-to-full-criterion passage, including strictness.

Each branch starts with a bounded decision or derivation. A known low-order positivity result can validate a mechanism but is not a new coefficient range. Return a useful estimate, precise obstruction, or a fixed execution contract before launching numerics. Constants may depend on arbitrary finite order; a finite list of successful tests does not supply that arbitrary-order theorem.

Use the repository [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), together with the [avoid index](../../../../avoid/README.md), especially [restating the target](../../../../avoid/01_restating_the_target.md), [shape-only premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md). Note14's control screen is inherited; any changed premise needs a fresh, claim-specific screen.

## Filing and shared ownership

Each linked folder contains a starting brief with its question, equations, first bounded task, completion rule, limitations and reading list. Save later analytical notes in that folder, and use matching branch names under `jensen/numerics/` and `jensen/reviews/` as those artifacts are first produced. Use the common [reference catalog](../references/README.md).

Future branch conversations should register their own histories with their actual identities, ordinarily under `jensen/chat-histories/`; this organizing chat retains its unique existing registration. Keep the live register as the single task ledger. Parallel workers should own separate branch files and coordinate changes to shared indexes and the register. No existing evidence needs to be moved or duplicated to begin a branch.
