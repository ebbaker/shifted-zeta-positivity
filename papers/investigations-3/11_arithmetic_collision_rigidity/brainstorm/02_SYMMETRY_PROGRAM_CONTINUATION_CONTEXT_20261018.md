# Continuation context for the symmetry research program

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; actual reasoning
effort: **max**, verified from the authoring turn metadata.

Continue from the [self-duality and symmetry questions](01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md).
Edward Baker accepted the known self-duality question as one question for
the next research program and requested additional possible symmetries,
including approximate or asymptotic ones. This handoff preserves those
proposals. No new symmetry-based estimate has been proved or implemented.

## Decisions from this conversation

The phrase “controls fail the full reflection law” referred to classical
theta modular self-duality. It was corrected to distinguish square-series
controls that fail full reflection from reflected controls that lack the
normalized arithmetic square expansion. There is no new exact reflection
hypothesis waiting to be imposed. The accepted question is whether the
known law yields a new quantitative estimate for the retained oscillatory
arithmetic sum.

Three additional mechanisms were proposed: reflection of the normalized
Riemann–Siegel correction within a cutoff interval; approximate rotation of
the normalized first jet; and approximate low-mode amplitude invariance at
fixed \(\kappa=t\log(x/(4\pi))\). Their equations, scope, controls, and
sources are in the companion note. The suggested priority is cutoff
reflection, then first-jet rotation, using scaling to organize regimes.
These priorities are proposals for the next program, not completed stages.

## Current manuscript and established coverage

The canonical source is
[positive_arithmetic_packets/main.tex](../manuscript/positive_arithmetic_packets/main.tex).
The [manuscript guide](../manuscript/README.md) links the current 45-page
reading copy and build record. The preceding part of this conversation
integrated the overview 02 results through Notes 07–14 into twelve TeX files
and eleven numbered sections. The [integration review](../reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md)
and [replay manifest](../numerics/MANUSCRIPT_INTEGRATION_REPLAY_20261018.json)
record internal verification and exact source coverage. The brainstorm
handoff does not modify those TeX sources or their certificates.

The current source-set SHA-256 is
`2690c3052927702a7f25d7e0519cc8ae10abfd202ac891bb8c06208eaa9a7b0c`.
It identifies the compact sorted JSON map of relative TeX filenames to
file SHA-256 values, as recorded in the
[build record](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json).
Historical source pins belong to earlier versions; do not overwrite them
or bypass their checks when replaying a revised manuscript.

For \(E=H^2+H_x^2\) and \(\mathcal L_0=H_x^2-HH_{xx}\), the current
milestones are:

| Result | Scope and location |
| --- | --- |
| Positive complete arithmetic carriers and logarithmic derivative payment | The carrier contribution is bounded by \(E/64\); the small relative higher-mode tail is not a relative error bound for the complete physical field. Sections 2–4. |
| Effective omitted-mode tail | First three jets have error below \(2\times10^{-9}\mathcal G_0\) for the stated contour/mode rule, \(x\ge1000\), \(0\le t\le1/2\), \(|\operatorname{Im}z|\le1\); constant-distance contours also give a normalized \(O(x^{-1/4})\) tail. Section 7. |
| Finite signed rectangles | \(\mathcal L_0>E/100\) on \([.01,.2]\times[25,45]\) and \([.01,.2]\times[999,1001]\), with 314 strips and 40 cells respectively. Section 8. |
| Complete wall and finite-height propagation | Seven wall cells at \(\operatorname{Re}z=1000\), published initial verification, and local heat splitting give \(E>0\) for \(0<t\le.2\), \(|x|\le1000\); together with the signed rectangle, for \(.01\le t\le.2\), \(|x|\le1001\). Section 8. |
| Explicit real exterior | \(E>0\) for \(\varepsilon\le t\le1/2\), \(|x|\ge\exp(20/\varepsilon)\), \(0<\varepsilon\le1/2\). Section 9. |

The remaining real bridge on \(.01\le t\le.2\) is
\(1001<|x|<e^{2000}\). A small error relative to a positive envelope
supplies no lower bound for the complete signed field. Direct enumeration
in the present implementation would exceed \(10^{433}\) modes near the
outer endpoint. The original matched timing ratio was 1.480, below the
factor-two gate. These are obstacles for the specified implementations,
not impossibility theorems for other arithmetic representations.

The [global scope section](../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex)
also records the conditional \(\Lambda\le.18\) route: it still needs
nonvanishing at \(t=.1\), \(x>1000\), \(.4\le y\le\sqrt{.8}\).
Real first-jet exclusion does not supply that complex exterior. The remote
polynomial heat control shows that the listed finite wall, baseline, strip,
and exterior information alone cannot bridge an unobserved collision;
it fails the stronger high signed-rectangle condition. No improved Newman
bound has been obtained. The reviews remain internal LLM assessments,
without independent specialist review.

## Read before starting the next attempt

Start with the repository [AGENTS.md][agents], [result summaries][summaries]
and [patterns to avoid][avoid]. The relevant clusters are
[collision controls][controls] and [theta identities and arithmetic bookkeeping][theta].
The relevant cautions are [reformulating the target][reformulation],
[premises shared by controls][shared], [separate absolute bounds][separate],
and [scoped negative results][scope].

Then read these mathematical sources in this order:

1. The [whole-round summary](../research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md)
   and [current manuscript guide](../manuscript/README.md), for earned results.
2. The [reflection and coefficient-rigidity section](../manuscript/positive_arithmetic_packets/sections/05_controls.tex),
   followed by the [fixed-cutoff exterior contract](../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex).
   The latter fixes \(s=(1-iz)/2\), \(\mathcal A_t\), \(\vartheta_t\), and
   the arithmetic weights. Its \(\mathcal A_t\) is distinct from the
   earlier positive arithmetic carrier \(A_{\mathcal P}\).
3. [Polymath, §6.2](https://arxiv.org/html/1904.12438v2#S6.SS2),
   especially equation (53) and Proposition 6.3, and the signed assembly in
   Corollary 6.4. Preserve their normalizations before comparing errors.
4. The [earlier collision manuscript][earlier]. Search for labels
   `sc:vector`, `prop:absmass`, `sc:packet`, and `lem:phase`: these contain
   the exact joint vector, the terminal-block obstruction, genuine adjacent
   cancellation, and the conditional amplitude–phase criterion. Read its
   growing-edge cancellation and shrinking-time estimates before claiming
   any of those as new work.

## Suggested first research task

Characterize the signed cutoff contribution in the current normalization
and compare it with the current absolute \(E_m^C\) payment. Begin with a
fixed-cutoff analytic neighborhood or a transition formula that handles
cutoff changes. Specify the reflected variable, all amplitude and phase
multipliers, and value/derivative defects before choosing a numerical scan.
For a first-jet consumer, pay for both value and first derivative; for
\(\mathcal L_0\), also pay for the second derivative.

Choose one bounded domain and one measurable objective: a smaller uniform
error with the same normalization, less work for the same certified
accuracy, or new certified coverage. A successful comparison must include
all retained terms, the correction, every tail, and cutoff-transition
costs. An improvement only in the correction term need not improve the
complete error budget. Stop and reassess if the benefit disappears after
these costs are included; do not promote a value-only identity to a jet
bound or enlarge the scan without a concrete reason.

For a rotation attempt, the new obligation is an estimate for the actual
arithmetic amplitudes and phases, not a renamed nonvanishing criterion.
For scaling, retain the growing terminal block; a fixed-mode limit is not
uniform summation. The existing adjacent-packet obstruction concerns the
specified diagonal bound and leaves complete signed correlations open.

## Control replay and reproducibility

The [saved control record](../numerics/SYMMETRY_BRAINSTORM_CONTROL_REPLAY_20261018.json)
is the replay executed during the symmetry discussion, preserved byte for
byte from its external output. It records five rejected event boxes and
the separate Euler negative-Laguerre witness, with source and receipt
hashes. Its analytic screen distinguishes finite-prime, smooth-primitive,
and other controls for which no effective event box was tested. It does
not validate a new symmetry criterion.

The [numerical guide](../numerics/README.md) includes the regeneration
command. Use Python with python-flint 0.9.0 and a fresh external receipt
folder; future records must use the future run's actual model and effort.
The [current manuscript regeneration guide](../numerics/manuscript_integration_20261018/README.md)
reproduces the larger verification suite if a mathematical change requires
it. It also explains why the unchanged historical pilot emits an obsolete
exp(6400) budget; exp(2000) is the current slab endpoint.

Save new derivations in `notes/`, code and small execution records in
`numerics/`, and assessments in `reviews/`. Keep the speculative proposals
in this brainstorm folder. Follow [LARGE_FILES.md][large]; regenerable bulk
outputs stay external. Use Git milestones and the existing draft history
rather than creating new manuscript snapshot directories.

## Conversation identity for the next chat

This conversation is registered as number **5**, title **Summarize arithmetic
collision work**, thread `01a15121-910f-7382-86ec-a03da64b8dea`, in the
investigation's [chat history archive](../chat-histories/README.md). Its
[canonical history](../chat-histories/0005_2026-10-18T22-28-36Z_summarize-arithmetic-collision-work.json)
retains the overview, manuscript integration, reflection clarification, and
symmetry discussion. Saving notes in `brainstorm/` does not relocate that
registration. A new chat must use its own actual identity and follow
[tools/CHAT_HISTORY.md][history]; do not reuse this chat's number or id.

A suitable opening request for the next chat is:

> Read the continuation context and symmetry questions in Investigation
> 11's brainstorm folder, then develop a bounded research plan beginning
> with the signed Riemann–Siegel cutoff correction. Characterize its
> normalization, reflection, and uniform derivative errors, and identify
> a quantitative improvement over the current exterior contract. Build
> on the earlier terminal-block and adjacent-packet results, and screen
> any proposed exclusion estimate against the applicable collision controls.

[agents]: ../../../../AGENTS.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[reformulation]: ../../../../avoid/01_restating_the_target.md
[shared]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[separate]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[earlier]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[large]: ../../../../LARGE_FILES.md
[history]: ../../../../tools/CHAT_HISTORY.md
