# Angular Jacobi gluing

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Current execution model: `gpt-6-astra` (Codex); reasoning effort **ultra**.
The original initialization configuration is preserved in its research note.

Status: **continued through a proved positive correction bound and stable
source recovery; physical transfer blocked at a specific cancellation
inequality**. Independent review remains outstanding.

This project develops brainstorm card 2. Its first proposed output is:
Full angular gluing and its Newman heat compatibility defect.

Read the [initial research program](notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
for the exact source, generator, physical reduction, bounded first task,
validation criteria and exclusions. Readiness: **first tier**.
This classification describes the next useful calculation, not the probability
of an RH proof.

The [elliptic transport calculation](notes/ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md)
now gives the exact inserted moving-period law, an entire short-period
identity, and its endpoint and projection corrections. A single full-line
period has a growing carrier. The short-period repair has a negative value
at the origin and introduces a cusp; its auxiliary visibility cannot be
transferred to the physical pair without paying the correction. The entire
finite angular Taylor hierarchy is explicitly a scalar derivative dictionary.
Full elliptic preparation still supplies a global restriction, but that
first calculation obtained no stationary sign or value-and-slope lower bound.

The [Volterra continuation](notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md)
now proves exact recovery, a stable weighted source-norm inverse, and
`P_t(x)>1/[3000(1+x²)]` for the complete correction transform at all real
frequencies and `0<=t<=1`. Its positive density is strictly convex after
heating. The physical sum `H=A+P` still cancels every algebraic endpoint
term; no constant or polynomial-scale relative transfer bound can hold.
The [source controls](notes/3_COMPLETE_CHANNEL_VOLTERRA_CONTROLS_20261013.md)
show that nearby positive sources with exact remote collisions retain
even this positive correction bound. They violate full imaginary gluing.

The [continuation assessment and ChatGPT brainstorm brief](reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md)
states the exact remaining inequality and supplies a self-contained
question about an adjoint multiplier using the genuine integer preparation.
That source-dependent cancellation estimate is the current blocker;
no physical stationary sign or new collision-exclusion region is claimed.

The [standard-library checker](numerics/check_elliptic_transport.py) and
[small execution record](numerics/ELLIPTIC_TRANSPORT_RECORD_20261013.json)
verify exact polynomial identities through angular order 24, an elementary
rational negative-source bound, and diagnostic direct theta evaluations.
Those original numerical residuals are not interval enclosures. The new
[complete-channel checker](numerics/check_complete_angular_channels.py)
verifies the positive-anchor constants and certifies `|A|>P` at `t=0,x=32`,
with all tails paid, rejecting a simple absolute-value transfer. Its
[record](numerics/COMPLETE_ANGULAR_CHANNELS_RECORD_20261013.json) keeps finite
Volterra diagnostics separate from outward bounds. The rank-two task has
already been completed; current work stops at the explicit angular
cancellation inequality instead of repeating either identity calculation.
This 13 October execution was prepared for Edward Baker with substantial
LLM assistance using the recorded `gpt-6-astra`, effort **ultra** configuration.

The [active portfolio](../README.md) maps related programs. The original
[broad brainstorm](../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md)
remains the common context.

Save derivations in `notes/`, reproducible code and small records in
`numerics/`, assessments in `reviews/`, and this project's future
conversations in `chat-histories/`. Include date, authorship, model and effort
in research records. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
Manuscript milestones use concise `DRAFT_HISTORY.md` entries; no manuscript
snapshot folder is initialized here.
