# Heat counterkernel features and solidification

12 October 2026. Prepared for Edward Baker. Model: GPT-6-astra (Codex); reasoning effort: ultra, verified from the session configuration. Prepared with substantial LLM assistance. Internal checks are not independent mathematical validation.

[Investigation portfolio](../README.md)

## Objective and status

**Scoped; research not started.** Test precisely which combination of spectral-kernel properties still permits a positive-time collision. The bounded question is whether a positive even kernel can combine a specified theta-like counting law, eventual reality and simplicity of high zeros at every positive time, and a positive de Bruijn–Newman collision time. This is a counterexample and hypothesis-design investigation, not a new collision-exclusion claim.

The existing positive counterkernel has transform $2K_{iz}(1)\cos^2(bz)$ at its collision time. After rescaling, its leading zero density matches the theta normalization. This already defeats an appeal to logarithmically growing mean density alone. It does not automatically match the full counting law, a specified remainder, simplicity, or uniformity in heat time.

## First bounded task

Build a feature table for the existing counterkernels and the theta source. Separate positivity, evenness, decay, leading and linear counting terms, remainder estimates, multiplicities, and time dependence. State exactly what “solidification” means: for every fixed positive time, sufficiently high zeros are real and simple, with any stronger location or uniformity requirement recorded separately.

Then examine one finite-zero-surgery construction starting from a proved real-rooted heat member. Replace selected real zeros by a conjugate pair while preserving the required symmetries. Determine whether the resulting Fourier kernel can be proved positive and whether its heat evolution retains the declared counting and solidification properties. Use numerical exploration only to select or reject candidates, not to certify global positivity.

## Deliverables

- A sourced feature ledger that distinguishes established properties, local consequences, conjectures, and untested assumptions.
- A fully specified bounded construction attempt, including transform conventions, admissible parameters, and every required global estimate.
- Either a proved counterexample to the named conjunction of properties, or a precise obstruction for the attempted construction class.
- A short review stating which proposed proof inputs survive the test and what further source-specific information would be needed.

## Continue and stop tests

Continue if the construction identifies a genuinely new discriminating condition with an independent source for theta, or yields a counterexample satisfying every declared hypothesis. Stop adding generic conditions already satisfied by the controls. Cap unsuccessful construction attempts unless a concrete mathematical obstruction suggests a new test.

Failure of one surgery scheme is not evidence that the desired conjunction forces RH. A numerical positivity scan cannot establish positivity on the whole spectral line. A local splitting of a double zero does not by itself establish complex zeros at every lattice point for every earlier time. Keep those quantifiers explicit.

## Scope and inherited work

A no-go theorem names its inputs. A positive-collision kernel cannot satisfy the actual sufficient stationary-sign inequalities throughout the required predecessor neighborhood. Generic identities must not be confused with these inequalities. Likewise, local disk-tube ambiguity does not preserve theta's global initial condition or arithmetic structure.

Start from the [feature proposal and density correction](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md), [solidification proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md), [existing positive counterkernel](../../quasi-rh-exponent-descent/newman_collisions/01_analytic_gaussian/notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md), and [local heat ambiguity theorem](../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md). Reuse these results without copying their implementations.

## Records

Place research in `notes/`, computations and small records in `numerics/`, reviews in `reviews/`, and conversation provenance in `chat-histories/`. Follow the [large-file policy](../../../LARGE_FILES.md). At notable milestones update `DRAFT_HISTOR.md` with concise commit/tag references and links; do not create manuscript snapshot directories.
