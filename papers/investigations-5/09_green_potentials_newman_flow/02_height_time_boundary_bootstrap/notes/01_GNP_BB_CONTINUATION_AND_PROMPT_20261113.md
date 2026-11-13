# Boundary bootstrap continuation and model change guidance

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in research chat0001's recorded configurations.

**Dated return snapshot: B01 complete; E01 r1 and B02 ready and unactivated.**
The [sole progress register][progress] is authoritative. This updates the
earlier setup-only handoff; its setup provenance remains in the
[crosswalk][crosswalk] and DRAFT_HISTORY.

| Next task | Type | Recommended model and reason | Readiness | Expected output |
| --- | --- | --- | --- | --- |
| GNP-BB-B02 — analytical contour and observation protocols over unbounded height | B | GPT-6 Astra: explore geometry, selection rules and the estimates needed as the band approaches the line | Suggested next; ready, unactivated; [revised specification](../research-overview/01_GNP_BB_RESEARCH_OVERVIEW_20261113.md#separate-contour-and-observation-investigation), [Note05][program] | Explicit height-dependent rules or a well-posed analytical protocol, separate/joint comparisons, iteration assessment and a fixed proof contract or precise bottleneck |
| GNP-BB-E01 r1 — acquire the complete outer-layer estimate | E | GPT-6.1 Sol: fixed analytical proof and complete error accounting | Ready alternative benchmark; [frozen request][packet] and [input manifest][inputs] intact | Prove the uniform estimate and one width gain of 1/16, or return its exact failed allowance |

**Default next: [B] GNP-BB-B02 — GPT-6 Astra.** The author now prioritizes
an analytical program extending to infinite zeta height, with open
exploration of strategies and protocols that might continue contracting
toward the line. This is a conceptual design task under the
[author's B/E workflow][models], not a claim about the actual model here.
[Official OpenAI model-selection guidance](https://learn.chatgpt.com/docs/model-selection)
was checked on 13 November 2026. No model, effort or chat setting was
changed; the author chooses the continuation.

**Scope revision, 13 November:** Note05 supersedes B02's original cap on
rectangle/offset alternatives. It provides an illustrative contour over
all real heights, a height-varying observation formula, and obligations
for infinite-domain limits and iteration. Different contour families,
selection protocols and changes of estimating strategy remain open.
Numerical work serves a named analytical question or compact remainder.
E01's unproved gain 1/16 remains a benchmark; its coarse allowance does
not justify iteration below \(y>3/4\). Preserve r1 and explicitly version
any different execution contract. The revision itself proves no new gain.

## Inherited B01 baseline and its limits

[Research Note03][note] and the [decision][decision] choose one family:
X∈[U,2U], λ_X=1/L_X, L_X=log(X/(4π)), with the initial
width a_X=√(1−2/L_X), observation b_X=a_X+1/16 and target a_X−1/16.
Use the rectangle |Re z−X|<1, 7/8<Im z<9/8. Time is frozen across
each rectangle, rather than changed at every spatial point.

The selected normalization is H/(C_−ζ(s_λ(z))), using the explicit
carrier and shifted argument in Note03. The ordinary ζ factor is
independently nonzero throughout the rectangle because Re s_λ>9/8.
The substantive estimating choice retains heat suppression in the
**entire reflected finite arm**, giving a feasible x^(−3/128) payment
where the old coarse reflected allowance did not decay. Dominant-arm
heat-weight removal has a convergent O(1/L_X) payment.

The **unproved E01 target** is a uniform normalized error at most 1/16.
Conditional on that estimate, the full derivative disks give m=1/2,
M=2 and h=1/8>η=1/16. The same data give the complete rectangle
Green comparison log(17/15)<log(19/16). Those geometric implications
were checked, but the arithmetic threshold has not yet been acquired.
The full uniform provider constants, cutoff coverage and finite onset
gates are the remaining proof work. The [assessment][review] is by the
same assistant and does not accept the future E01 theorem.

A successful estimate would already imply direct nonvanishing in the
rectangle; the Green construction offers no additional arithmetic gain
from these data. B10 remains an averaged theorem with its original
clock/offset/domain. No B10 extension, RH result, Λ improvement,
finite-height coverage, common-time global enclosure or convergent
iteration is proved here. The displayed coarse absolute allowance
requires y>3/4; that limit is scoped to this allowance, not all methods.

Before execution, read the [result index][results] and [avoid index][avoid],
especially [heat-flow cluster11][r11], [collision controls12][r12],
[target classification01][a01], [control premises02][a02] and
[scoped exclusions07][a07]. Note03 §5 performs the analytical control
screen. The [source-use record][sources] names the exact imported
passages and review levels; the [reference index][refs] retains their
canonical ownership. No new field computation or manuscript was made.

## Standalone B02 analytical-program prompt

~~~text
Work in /Users/ebbaker/Documents/shifted-zeta-positivity.

Read AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md and
tools/CHAT_HISTORY.md. Read result-summaries/README.md and avoid/README.md,
especially clusters 11/12 and patterns 01/02/07.

Destination:
papers/investigations-5/09_green_potentials_newman_flow/02_height_time_boundary_bootstrap

Read the sole progress register, research overview, research plan, and
Notes03–05. Complete [B] GNP-BB-B02, recommended GPT-6 Astra, under its
revised analytical/exploratory scope. Record actual model and effort only
when available; the recommendation does not change settings.

Seek expressions or well-posed analytical rules for contours over the
continuum of heights with no upper cutoff, and for observation points
varying with height. Explore contour choices at a fixed observation rule,
and observation choices on a fixed contour family; then study their
coupling. Keep different graph, conformal, local-cover and other justified
strategies available. The illustrative formula in Note05 is not mandatory.
Preserve the complete canonical field and use one fixed heat time within
each contour integral. Record the actual time domain of every claim.

Seek a complete canonical gain estimate, paying infinite-height/end
terms or uniform local coverage, and identifying the compact-height
obligation. Examine whether the estimates can persist toward the line:
track width recurrences, shrinking-domain losses and iteration-dependent
height onsets. The initial 1/16 gain is a benchmark, not a fixed step at
all depths. Address the current y>3/4 estimating limitation without
turning it into a universal obstruction. Do not infer time zero from
a positive-time theorem or a height-dependent heat curve.

Numerics may support a named analytical question or a bounded remaining
region; they do not replace the analytical tail or convergence proof.
Apply the collision-control premise screen to new proposals. End this
design pass with a supported strategy and a fixed next E proof contract
for Sol, or an exact bottleneck with scoped alternatives. A contour
parameterization alone is not an acquired estimate. Preserve E01 r1.

Save arguments in notes/, decisions in brainstorm/notes/, assessments
in reviews/, and actual small computation records in numerics/. Update
the sole register, DRAFT_HISTORY and continuation guidance. Refresh this
chat's registered history and arrange exact-turn final capture as the
last tool action; register a new chat only with its actual provenance.
~~~

## Retained E01 benchmark prompt — alternative continuation

**Geometry clarification, 13 November:** [Note04](04_GNP_BB_CONTOUR_AND_OBSERVATION_CLARIFICATION_20261113.md)
distinguishes Γ_X=∂D_X, the interior observation p_X, the zero bounds
a_X and a_X−1/16, and the two auxiliary disk constructions. Read it
with E01 r1. It changes no parameter, proof obligation or frozen input.

~~~text
Work in /Users/ebbaker/Documents/shifted-zeta-positivity.

Read AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, REFERENCE_WORKFLOW.md,
LARGE_FILES.md and tools/CHAT_HISTORY.md. Read result-summaries/README.md
and avoid/README.md, especially clusters 11/12 and patterns 01/02/07.

Destination:
papers/investigations-5/09_green_potentials_newman_flow/02_height_time_boundary_bootstrap

Complete [E] GNP-BB-E01, frozen request r1, recommended GPT-6.1 Sol.
Check the sole research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md
before activating it. Read research-progress/handoffs/GNP-BB-E01-r1.md,
notes/03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md,
notes/04_GNP_BB_CONTOUR_AND_OBSERVATION_CLARIFICATION_20261113.md,
brainstorm/notes/01_GNP_BB_B01_DECISION_20261113.md,
reviews/01_GNP_BB_B01_SAME_ASSISTANT_ASSESSMENT_20261113.md and
references/01_GNP_BB_B01_SOURCE_USE_20261113.md. Verify the frozen inputs
in numerics/01_GNP_BB_B01_INPUTS_20261113.json. Actual model/effort must
come from available metadata, not from this recommendation.

Keep the complete theta field, H_0=xi((1-iz)/2)/8 and partial_lambda H=-H_zz.
For every sufficiently large X use lambda=1/log(X/(4pi)), held fixed
on |Re z-X|<=1, 7/8<=Im z<=9/8. Prove the request's complete comparison
with the explicit C_minus*zeta(s_lambda) carrier, whose independent
zero-free domain must be checked before division. Keep both finite RS
arms, cutoff, correction and full provider/Gaussian errors. Preserve
the reflected heat suppression and do not introduce an infinite
heat-weighted Dirichlet series.

Acquire the uniform relative error <=1/16, including symbolic constants
and a finite list of eventual onset gates. Then verify m=1/2, M=2,
h=1/8 and buffer 1/16, and conclude the specified one-step width gain.
Check the same-data complete Green inequality, including both sides.
An unevaluated but justified finite onset is acceptable; a numerical
sample or an implication merely assuming the target estimate is not.

One analytical pass, one domain family, one step. No numerical field
campaign, manuscript, iteration or changed time slab. If the provider
cannot pay the target, return the exact failed term and its scope; a
new canonical premise or mechanism returns to a dated B01 revision.
Do not silently revise r1 or another investigation's proof.

Save the proof in notes/, its assessment in reviews/, any small actual
records in numerics/, and a separate r1 return in research-progress/handoffs/.
Update the sole progress register, DRAFT_HISTORY and this continuation
note with evidence level, unpaid inputs and justified next model/task.
Follow the reference workflow for newly checked inputs.

Register a genuinely new branch-only chat in this branch's chat-histories/
using tools/refresh_chat_history.py and its actual identity/title/source.
Keep an existing chat's unique registration unless relocation is requested.
Refresh at entry and arrange the bounded exact-turn final capture as the
last tool action. Never bypass identity or public-prefix checks.
~~~

## Ownership and capture

The parent retains GNP foundations; child 01 retains GNP-RS/B10;
Investigation10 retains RSCT. HDA retains its provider theorem. E01
owns only this branch's new comparison and consumer, borrowing those
inputs without transferring their tasks or editing their proofs.

This research chat is “Begin GNP boundary bootstrap”, thread
`01a1d570-d742-77e2-94e1-780baac55672`, registered as this branch's
chat0001. Entry capture succeeded using its exact local public-text
source. Read the current [registry][registry] for counts, timestamps,
hashes and model configurations; do not copy stale values from a note.
The unsent final is captured only after it is recorded, through the
bounded exact-turn follow-up; native hook activation is not asserted.

The earlier setup chat remains child 01 chat0007 with its historical
creation-time conflict. That separate archive was neither relocated
nor repaired here. See [chat-history guidance][chat].

[entry]: ../README.md
[progress]: ../research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md
[crosswalk]: 02_GNP_BB_SETUP_AND_SOURCE_CROSSWALK_20261113.md
[note]: 03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md
[decision]: ../brainstorm/notes/01_GNP_BB_B01_DECISION_20261113.md
[packet]: ../research-progress/handoffs/GNP-BB-E01-r1.md
[inputs]: ../numerics/01_GNP_BB_B01_INPUTS_20261113.json
[review]: ../reviews/01_GNP_BB_B01_SAME_ASSISTANT_ASSESSMENT_20261113.md
[sources]: ../references/01_GNP_BB_B01_SOURCE_USE_20261113.md
[refs]: ../references/README.md
[chat]: ../chat-histories/README.md
[registry]: ../chat-histories/index.json
[program]: 05_GNP_BB_ANALYTICAL_PROGRAM_AND_SELECTION_PROTOCOLS_20261113.md
[models]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
