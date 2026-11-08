# Fresh brainstorm session: TND-OC-B03 and chat-source verification

8 November 2026. Prepared for **Edward Baker** with substantial OpenAI
Codex assistance. Exact backend model and reasoning effort are unavailable
in exposed session metadata. Recommended settings below are not recorded
execution settings. No new research or model switch was executed in
preparing this handoff.

The author requested a new brainstorm session after B02 and the project
explanation. This note supersedes Continuation04's **default routing only**.
B02 remains **proved in-note; proof-author self-check only**. E03 remains
ready and unstarted; a new session or model does not supply its assessment.
The [sole register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
owns current status.

| Next task | Type | Recommended model | Readiness / dependency | Expected output |
| --- | --- | --- | --- | --- |
| **TND-OC-B03 — default for the requested fresh brainstorm** | B | **GPT-6 Astra**, author-selected effort; the missing canonical input and comparison method require conceptual selection | Ready for provisional exploration using accepted E02; retain B02's unassessed status | Compare at most two routes, identify a usable canonical input and fixed proof contract, or record a scoped failure and park |
| TND-OC-E03 — pending assessment | E | **GPT-6.1 Sol / ultra**, where supported; written claims and scope are fixed | Ready under the existing frozen request; complete before promoting B02 or relying on it as assessed evidence in a downstream contract | Separate claim-level assessment, at most one bounded correction, final disposition and hashes |

## First: verify the new conversation's history source

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity`. The destination
is this **02_localized_zero_correlations** branch, not its Green sibling.
Read [root AGENTS.md](../../../../../../AGENTS.md) and
[tools/CHAT_HISTORY.md](../../../../../../tools/CHAT_HISTORY.md). Use the
**new conversation's actual** thread id, title and source; do not reuse
this handoff session's identity.

```sh
python3 tools/refresh_chat_history.py --thread-id "$CODEX_THREAD_ID" --diagnose
```

Run that command only when the environment supplies the actual nonempty
thread id; otherwise obtain it from an authoritative session source.
The diagnostic reports discovery and registration, not successful capture.
If an authoritative source and actual title are available, register using
the documented recorder, this branch's `chat-histories/` destination and
the actual title. Use an explicit `--rollout` only for an authentic matching
JSONL source; the recorder also supports verified paginated local history.
Read the resulting registry entry and archive to verify that the new
thread's completed public messages were saved. Preserve creation time,
message prefix, provenance and hashes. Refresh at subsequent turns.

Before finishing a reply, arrange the documented bounded
`--after-turn ACTUAL_CURRENT_TURN_ID --wait-seconds 60 --defer` capture as
the last tool action, unless a trusted completion hook has been verified
to supply it. Check the worker's eventual result on the following turn.
The actual final message and completed turn must exist before capture;
never insert a planned answer or invent a turn id.

**Known failure, rechecked on 8 November:** thread
`01a1b947-82cc-732d-94e1-f3709c4410fd` is unregistered and its exact local
source is unavailable. Earlier direct paginated-source and app-reader
checks also failed. The current environment exposes no turn id. Repository
file writing works. The recorder's compatibility repair is documented in
[the diagnosis](../../../../../../tools/CHAT_HISTORY_COMPATIBILITY_20261107.md);
it does not manufacture an absent source. No native hook activation for
this conversation has been verified.

A new session may help **if it exposes an authentic readable history**;
opening another chat alone is not a verified fix. A local Codex session
opened in this repository is a possible setting to test. Do not change hook
trust, edit the app database, repurpose a sibling transcript or restart
other active work to claim success. If discovery still fails, report the
failure, keep a clearly labelled unregistered partial record of completed
public text, and continue the authorized research. Do not let capture
diagnosis become an open-ended replacement for B03.

The current fallback is
[the unregistered partial exchange](../chat-histories/UNREGISTERED_PARTIAL_TND_OC_B02_PUBLIC_TEXT_20261107.md).
It is not a complete native transcript. The existing registered chat0001
belongs to a different conversation and must retain its identity.

## Read order and mathematical state

Read the [model workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md),
[result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), followed by:

1. [Project explanation with equations](../brainstorm/explanations/01_PROJECT_STATE_AND_LESSONS_20261108.md), the sole register and [research plan](../research-plan/01_TND_OC_RESEARCH_PLAN_20261107.md).
2. Accepted [E02 consumer Note03](../notes/03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md), its [assessment](../reviews/02_TND_OC_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md), and the underlying [local log-transfer Note02](../notes/02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md).
3. [B02 Note04](../notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md), [Decision03](../brainstorm/notes/03_TND_OC_B02_SIGNED_COMPARISON_DECISION_20261107.md) and [author self-check](../reviews/03_TND_OC_B02_AUTHOR_SELF_CHECK_20261107.md).
4. The pending [E03 request](../research-progress/handoffs/07_TND_OC_E03_ASSESSMENT_REQUEST_20261107.md) and [frozen input manifest](../research-progress/handoffs/07_TND_OC_E03_INPUTS_20261107.json). Preserve these issued packets.

At time zero, write the zeros as \(z_j=x_j+iy_j\) with multiplicity and use

\[
Q_{X,h}=\sum_j w((x_j-X)/h)y_j^2,
\qquad Z(\eta)=\prod_j(1+\eta w((x_j-X)/h)y_j^2).
\]

A conjugate pair in the window plateau at heights \(\pm d\) forces
\(Q\ge2d^2\) and \(\log Z\ge2\log(1+\eta d^2)\). E02 pays the
source approximation and log-transfer errors; the missing step is a small
**signed canonical value**, sufficient for

\[
\widehat Q+E_Q<2d^2
\quad\text{or}\quad
\widehat L_\eta+E_\eta<2\log(1+\eta d^2).
\]

B02's separate-moment route leaves the coupled Jensen-gap difference
uncontrolled in
\[
S_\varphi=\frac{b}{4\pi}
\left[\log(A_+/A_-)+J_--J_+\right].
\]
Its other result is the sharp local harmonic-distance bound
\[
\inf_{v\ {m harmonic}}\int_{D(a,\ell)}
|\log|F|-v|\,dA\ge\frac{\pi\log2}{2}\,m\ell^2
\]
for an \(m\)-fold zero at \(a\). In the E02 geometry, a real zero at the
window center forces \(E_Q\ge m\log2/36\) for the **harmonic-baseline,
full-disk absolute-error recipe**. This is an allowance floor, not a lower
bound on true transverse mass. It does not exclude approximants retaining
real zeros, weighted errors or signed remainders. The original E02 theta
approximant may have zeros and remains valid. These B02 statements still
await E03 assessment.

## B03's bounded question

Can an available canonical input control the logarithmic comparison while
retaining the cancellation at the real axis? Compare at most two routes:

1. A weighted or directly signed log-error estimate exploiting the test's
   real-axis vanishing before absolute values are taken.
2. A comparison retaining a controlled real-zero divisor, rather than
   replacing its log modulus by a harmonic function.

These are directions to test, not endorsed proof mechanisms. For each,
identify the exact canonical information, the inequality it actually
implies, the remaining error and the one-pair margin. A newly named norm,
an unknown coupled Jensen gap, or an assumption that the unknown zeros
are already real does not provide an independent input. Permit one focused
clarification about a specific input/inequality; then choose a fixed route
or record the scoped failure. No numerical sweep is authorized by this
handoff.

Preserve canonical time zero, source normalization, all multiplicities and
collar zeros, the E02 disk and support conditions, height/window regime,
the exponent \(2/(n_X+2)\), enlarged-disk and derivative costs, complete
arithmetic/radial tails, and separate quadrature/rounding payments when
applicable. Do not turn a center average into an every-center estimate or
erase single-pair dilution. Record any justified conceptual change before
dependent execution. Consult the sibling's current register read-only if
using its results; do not alter its work or import a broader obstruction.

Before writing a new mechanism, apply
[target classification](../../../../../../avoid/01_restating_the_target.md),
[collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [premise screening](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
Name the premise each relevant control fails; generic identities which
also hold on colliding controls are not exclusion estimates. Retain
[scoped negative conclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and the warning about
[separate absolute bounds](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

Save the decision in `brainstorm/notes/`, any actual derivation in `notes/`,
assessment in `reviews/`, and update the sole progress register. Issue an
E successor only when its source, method, constants, errors, success
threshold and stop rule are fixed; complete E03 first if it consumes B02 as
assessed evidence. A precise failed route or decision to park is a valid
return. Do not promote the existing author self-check by changing models.
End with continuation guidance and an updated model-change note.

## Pasteable new-session prompt

> Work in /Users/ebbaker/Documents/shifted-zeta-positivity. Read
> papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/continuation-notes/05_TND_OC_NEW_BRAINSTORM_SESSION_20261108.md.
> First verify this new conversation's authentic chat source and capture;
> report a failure honestly and preserve completed public text if needed.
> Begin [B] TND-OC-B03 using GPT-6 Astra at my selected effort. Compare the
> two bounded real-zero-aware/signed-log routes and identify an independent
> canonical input, or record a scoped failure. E02 is accepted; B02 has
> author checking only and E03 remains pending. Do not promote B02 or start
> a numerical campaign. Track progress in the sole register, save research
> notes in this branch, maintain chat history, and finish with a concrete
> continuation and model-change recommendation.
