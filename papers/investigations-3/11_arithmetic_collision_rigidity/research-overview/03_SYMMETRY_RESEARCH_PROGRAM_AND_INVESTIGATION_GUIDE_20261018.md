# Symmetry research program and investigation guide

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual reasoning
effort **max**, verified from this turn's metadata. Research plan and
context consolidation; no new numerical experiment or exclusion theorem
is reported by this document.

## Purpose and program map

Investigate whether exact, approximate, or asymptotic symmetries can make
the complete arithmetic collision equations easier to estimate or evaluate.
The objective is a quantitative improvement after all signed contributions,
derivatives, tails, and transition costs have been included. The four
directions in the [symmetry continuation context][continuation] are retained,
and the [manifold assessment][hodge-review] adds two supporting directions.
The rotation-defect calculation belongs to the existing first-jet direction.
At Edward Baker's subsequent request, S07 adds the broader geometric-duality
and quaternionic-operator continuation from the coverage review. The
original six directions and their historical findings retain their identities.

The [symmetries directory][directory] is the entry point for these seven
investigations. Each linked folder contains its own mathematical context,
reading order, bounded first task, controls, deliverables, and stop rule.

| ID and folder | Research question | Present status |
| --- | --- | --- |
| [S01 Modular self duality][s01] | Can full theta reflection improve an estimate of the retained signed arithmetic sum? | Exact symmetry and coefficient rigidity known; quantitative use open |
| [S02 Cutoff reflection][s02] | Can the even normalized Riemann–Siegel correction be combined with cutoff terms to reduce the complete jet error? | Leading profile and published value error known; signed jet improvement open |
| [S03 Normalized jet rotation][s03] | Can arithmetic correlations control the complete rotation defect and keep the first jet away from zero? | Exact defect identity known; required arithmetic bound open |
| [S04 Time height scaling][s04] | Which complete signed quantities have a uniform description at fixed kappa? | Low-mode amplitude limit known; growing-cutoff signed limit open |
| [S05 Covariant theta jets][s05] | Does the normalized modular basis simplify complete-source differentiation or certified evaluation quantitatively? | Constant-coefficient ladder and reflection signs derived; practical gain unmeasured |
| [S06 Hodge and transverse geometry][s06] | Can transverse, hyperkähler or coupled geometry supply an independent estimate that survives physical restriction? | Exact maps, scoped obstructions and inherited signed transfer known; independent estimate open |
| [S07 Geometric duality and quaternionic symmetry][s07] | Can supported/relative duality or quaternionic and hyperholomorphic operator identities yield an independently useful physical estimate? | Zero-form Green identity, canonical self-flux and scoped first-order path-trace obstruction proved in-note; independent physical estimate open |

S01–S04 correspond to every direction in the original handoff. S05 carries
the normalized covariant-jet basis from this conversation. S06 carries the
Hodge/ASD question, transverse derivatives, and the coupled two-source
possibility. S07 carries broader supported/relative duality and quaternionic
or hyperholomorphic operator identities; S06 keeps its developed scalar
source-transfer work. These tasks share the same physical field; success
in one can supply an input to another.

The [overview 02 execution plan][old-plan] remains the contract and history
for its numbered stages, including its recorded model assignments. The
S01–S07 identifiers do not rename those stages. Record the actual model and
effort for every future execution; this note's authoring configuration is
not a claim about future runs.

## Baseline and scope

Read the repository [result summaries][summaries] and [patterns to avoid][avoid]
before beginning. The relevant clusters are [collision controls][controls],
[theta identities][theta-summary], [local collision geometry][local-summary],
and [geometric realizations][geometry-summary]. The controlling cautions are
[target reformulation][a01], [premises shared by controls][a02],
[generic geometric lifts][a03], [scoped exclusions][a07], and
[preserving cancellations][a12].

The current [manuscript guide][manuscript] and [build record][build] identify
the 45-page, twelve-file source set. At program initialization its source-set
SHA-256 is `2690c3052927702a7f25d7e0519cc8ae10abfd202ac891bb8c06208eaa9a7b0c`.
This is a historical baseline pin; verify current bytes before reusing a
certificate and retain old pins when a source changes.

Write
\[
 E=H^2+H_x^2,\qquad \mathcal L_0=H_x^2-HH_{xx}.
\]
The [whole-round summary][round-summary] and [integration review][integration]
record the established starting point:

- Complete finite certificates and propagation give E positive on
  \([1/100,1/5]\times[-1001,1001]\).
- The signed rectangles include \([1/100,1/5]\times[25,45]\) and
  \([1/100,1/5]\times[999,1001]\), with \(\mathcal L_0>E/100\).
- For \(0<\varepsilon\le1/2\), the real exterior is covered when
  \(\varepsilon\le t\le1/2\) and \(|x|\ge e^{20/\varepsilon}\).
- The remaining real bridge on \([1/100,1/5]\) is
  \(1001<|x|<e^{2000}\). The specified direct enumeration would be
  prohibitive near its upper end. The earlier matched timing ratio was
  1.480, below the factor-two gate.

The positive arithmetic carrier and envelope-relative tail estimates do
not lower-bound the complete signed field. Real first-jet exclusion also
does not supply the complex exterior required by the conditional Newman
route in [global scope][global]. The earlier results have the internal
review status recorded in their sources; organizing this program does not
upgrade that status.

## Shared mathematical conventions

Use the full source
\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad H_t=-H_{xx}.
\]
The physical positive heat time t differs from Jacobi evolution of the
elliptic parameter. Source differentiation in u differs from spectral
differentiation in x. Keep those distinctions in code and prose.

For spectral work use the [fixed-cutoff exterior contract][outer], with
\(s=(1-iz)/2\), its nonvanishing symmetric normalizer \(\mathcal A_t\),
phase \(\vartheta_t\), weights, and normalized field
\(Q=H/\mathcal A_t\). This normalizer is distinct from the positive
arithmetic carrier \(A_{\mathcal P}\). On a real interval with
\(\omega=\partial_x\vartheta_t\ne0\), put
\(D_\theta=\omega^{-1}\partial_x\).

When normalizing errors, retain the return to the physical field. If
\(H=\mathcal A_t(F+r)\) and \(a=\partial_x\log\mathcal A_t\), then
\[
 \delta H=\mathcal A_t r,\quad
 \delta H_x=\mathcal A_t(r_x+ar),\quad
 \delta H_{xx}=\mathcal A_t\{r_{xx}+2ar_x+(a^2+a_x)r\}.
\]
An error measured in one normalization cannot be compared numerically
with a bound measured in another without these factors.

All source or mode rearrangements must retain the complete cancellation
before estimating. Keep primitive lower edges and corners, source tails,
mode tails, spectral phases, and derivative correction terms. Freeze every
integer cutoff on its analytic neighborhood; differentiating a floor-defined
cutoff is invalid. A transition uses an exact added/removed-mode identity.

## Recommended order and dependencies

Begin the first quantitative experiment in **S02**. Use S01 to identify the
arithmetic symmetry that is actually retained and S04 to describe the
chosen regime. S05's existing normalized basis is available immediately
as an algebraic aid; reproving it is not a preliminary research milestone.

Next feed S02's complete signed approximation and derivative bounds into
**S03**. Compare a direct first-jet certificate with an integrated rotation
defect. The latter has a second-derivative cost and should be continued
only if its preserved cancellation pays for that cost.

Run a bounded **S05** evaluation or error-analysis comparison if the source
algebra is the identified bottleneck. A reduction in formula length is
useful documentation but must be distinguished from a measured evaluation
or bound improvement.

**S06** is a separate exploratory direction. Its first requirement is an
explicit mechanism beyond the already flat physical pullback: a transverse
identity with a justified observation map, or a coupled signed estimate
that retains both sources. No compactification, new metric, or additional
holonomy construction is needed merely to restate the existing pairing.
S06 can continue without a successful S02 result if it specifies such a
mechanism and a bounded estimating objective.

**S07** starts from its [initial geometric findings][s07-note] and the
existing marked metric, not a new ambient construction. Its bounded first
task is one polarized J-Dolbeault/Weitzenböck Green identity on
p∈[−1/4,1/4], q∈[1,4], with full torus fibers. The operator/form degree,
dual-test extension, all boundary fluxes, curvature action, physical trace
cost and omitted source tail must be specified. The diagonal J/K insertion
audit is inherited background. The [opening execution](../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md)
now derives that zero-form identity and proves the generic first-order
path-trace comparison fails. The complete theta self-flux vanishes, while
the raw rough-Laplacian insertion restores a divergent zero mode. Any
continuation must add a specified theta/PDE constraint, higher-regularity
payment, other form degree or independently estimated mixed current.
An independent physical estimate remains open. For Edward Baker with
substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**,
18 October 2026; same-model internal review.

The IDs are stable names, not a requirement to execute seven projects in
numerical order. Saving this program does not launch the experiments.

## A bounded first experiment

Use \(t\in[1/100,1/5]\), \(x\in[999,1001]\) as the initial comparison
domain, unless the opening derivation gives a concrete reason to change it.
It has a current signed reference certificate and lies in the published
remainder range. Agreement there validates the new method; it is not new
coverage. Choose the fixed analytic disks and cutoffs before evaluating.

Separately include a small transition neighborhood around a natural
cutoff crossing, for example the crossing a=9,
\[
 x=4\pi(81-t/16).
\]
Choose an explicit bounded enclosure and prove which cutoffs it contains.
This neighborhood is initially a test of the error and transition formula;
no noncollision claim is assumed there. Include the removable profile
points \(p=\pm1/2\) in a separate local check if the chosen parameter
cover reaches them.

For S02 compare the current absolute correction payment with a revised
approximation retaining the signed correction and nearby modes. Both
methods must enclose the same physical jet on the same domain, with the
same precision and stopping rules. Separate the signed finite expression
from its residual; do not compare the correction error alone.

Choose one primary objective before computing:

| Objective | Required evidence |
| --- | --- |
| Smaller complete error | A strict certified decrease of the specified uniform value/jet error under the same normalization and coverage |
| Lower evaluation cost | Matched accuracy and coverage, all setup/replay costs disclosed, measured time and work; use the prior factor-two gate for a claimed performance milestone |
| Larger finite exclusion region | Complete interval coverage, strictly positive paid margin, and all boundaries and transitions included |
| More effective exterior | A proved uniform onset with every constant evaluated; a smaller asymptotic coefficient alone is not an effective onset |
| A scoped obstruction | A proof or explicit counterexample for the named representation, norm, constraint, and parameter class |

For example, errors \(\epsilon_0,\epsilon_1\) for Q and Q_x and a
lower bound \(|\omega|\ge\omega_*\) give the normalized jet error
\(\sqrt{\epsilon_0^2+(\epsilon_1/\omega_*)^2}\). State whether that
quantity or the returned physical error is the comparison target. A
Laguerre consumer also needs the paid second derivative.

## Common execution and review guide

1. **Write the contract.** State the transformation, exact preserved
   quantity or leading model, defect, domain, normalization, derivative
   order, and the output that consumes the estimate. Classify a global
   nonvanishing reformulation as such once. State the numerical or
   analytic milestone separately.
2. **Reconcile prior work.** Read the direction's sources and the older
   collision manuscript labels `sc:vector`, `prop:absmass`, `sc:packet`,
   and `lem:phase` where applicable. Identify the exact extra estimate
   proposed beyond those results. Preserve the scope of every obstruction.
3. **Derive before scanning.** Retain signs and all correction terms.
   Establish convergence, differentiability, and fixed-cutoff transition
   formulas. Prove which controls fail a substantive premise. If all
   premises are shared, record that the mechanism alone cannot exclude
   their events.
4. **Build a bounded comparison.** Reuse the existing complete evaluator
   as a reference. Expose separate contributions from mode truncation,
   source-integral tails, quadrature, rounding, analytic differentiation,
   and whole-cell propagation. Recombine before any absolute estimate
   whose purpose is to exploit cancellation.
5. **Screen and challenge.** Run applicable source-specific controls
   when the method or acceptance test changes. Include the proposed
   method's special failure cases: cutoff jumps, removable singularities,
   slow cutoff phases, vanishing complete source combinations, or nearly
   singular normalizations. Do not substitute theta error constants for
   control-specific ones.
6. **Decide and save.** Compare against the declared gate. Record a
   successful bounded result, a specified obstruction, or an inconclusive
   attempt with its dominant unpaid term. Do not expand a scan merely
   because no gain was found. Link the derivation, small record, and
   assessment from the direction's README.

For a failed estimate distinguish the failure of the bound from a failure
of the actual theta quantity. A positive upper-bound exponent does not
prove growth of the signed sum. A local success or a useful new identity
does not close the unbounded bridge.

## Control map

Use the [control summary][controls] and [Hodge assessment][hodge-review] for
the constructions and their exact status. The [symmetry replay][symmetry-record]
and [Hodge replay][hodge-record] contain existing five-event rejection tests
and a separate Euler witness; they are baseline interface checks, not a
validation of any proposed new bound.

| Family | What is shared | What a theta-specific argument must actually use |
| --- | --- | --- |
| Finite-prime orbit controls | Selected-prime identities, finite measurements, positive coefficients | Complete normalized analytic reflection or another evaluated theta-specific estimate; their event height is not effective |
| Three-square and four-square controls | Square support and finitely many endpoints | Full reflection and the unchanged complete coefficient data |
| Reflected super-Gaussian control | Reflection and positive source structure | The normalized theta integer-square expansion and its quantitative use |
| Smooth shape and positive-primitive controls | Strong source shape, primitive positivity, and specified endpoint data | Complete theta arithmetic data; no numerical damping/event box is supplied by their analytic construction |
| Euler-factor controls | Even positive sources and substantial arithmetic/flow structure | Unchanged level-one theta coefficient data; the negative-Laguerre witness is not a double-event box |
| Counter-kernels and polynomial heat events | Generic heat evolution, holomorphic jets, Hodge and rotation identities | The exact theta source plus a paid estimate absent at the control event |
| Smooth-density and two-channel controls | Auxiliary positive realizations | A comparison to the complete signed physical observation |

A strict collision-exclusion test must reject a control on a domain
containing its event. A valid local certificate may pass on a collision-free
control domain. Generic Hodge self-duality and the rotation identity alone
fail to distinguish the controls. Full reflection plus the normalized
integer-square series selects theta in the stated coefficient class;
selection still does not prove a signed lower bound.

## Deliverables and file organization

Each direction currently has a contextual README. When executing that
direction, create its `notes/`, `numerics/`, and `reviews/` subfolders as
needed. Save incremental proofs and failed estimates in `notes/`, code and
small run records in `numerics/`, and assessments in `reviews/`. This keeps
the new work together while following the repository's research layout.

Use the same minimum record for every direction: date and actual model/
effort; exact source/code identities; rational domains and precision where
applicable; accepted hypotheses; formulas and derivative conventions;
separate error terms; applicable controls and missing premises; comparison
against the original gate; and an explicit next decision. Label floating
experiments, exact algebra, interval certificates, analytic proofs, and
review status according to the evidence.

Existing brainstorm notes, Note 07, Review 14, certificates, and manuscript
sources remain canonical at their present paths. Link to them rather than
copying or moving them. Future milestones belong in the existing
[draft history][history], with concise links or commits/tags; create no
manuscript snapshot folders. Follow [LARGE_FILES.md][large]: regenerable
bulk data stays external, with small reproducibility records in the tree.

New direction-specific chats should use that direction's `chat-histories/`
when first registered. A new program-wide chat may use
`symmetries/chat-histories/`. Existing chats keep their unique registrations,
including this conversation in `brainstorm/chat-histories/`; a new folder
does not authorize re-registration or relocation. Follow the repository
[history workflow][chat-workflow] at the beginning and end of each reply.

## Geometric symmetry coverage

The seven directions organize selected research mechanisms; they are not an
exhaustive classification of geometric symmetries. The [broader geometric
review](../symmetries/06_hodge_and_transverse_geometry/reviews/03_GEOMETRIC_SYMMETRY_COVERAGE_POINCARE_AND_HYPERKAHLER_20261018.md)
distinguishes Poincaré/relative/compact-support duality, quaternionic J/K,
twistor and hyperholomorphic structures, Lefschetz and Hodge–Riemann
identities, actual isometries, periods/monodromy, and bundle transforms.
It crosslinks the already developed relative Euler/winding route.
The separate [S07 investigation][s07] now consolidates this material in its
[initial note][s07-note], preserving the original S06 review and checks.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**, 18 October 2026; organizational initialization only.

For the existing semi-flat source, its exact J/K check finds that the raw
second J insertion restores a divergent zero mode; the second K insertion
returns the weighted base-p channel and its existing primitive compensation.
These statements concern the declared source and directional iterations,
not every rotated or coupled estimate. A bare-star or finite-jet obstruction
must retain its original scope. Future geometric continuations should name
their extra input and complete physical observation, then pay its boundary,
commutator and scale costs. This audit supplies coverage and exact identities,
not an independent signed bound or a change to the quantitative priorities.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**, 18 October 2026; same-model internal review.

## Starting a continuation

Open the chosen direction's README, this guide, and its first cited
mathematical source. State the proposed bounded contract and the exact
unpaid estimate. Begin with S02 if no different mechanism has been selected.
Use the normalized source basis from S05 and the exact defect from S03
where they make that contract simpler. A successful round ends with a
reviewable estimate or a clearly scoped failed attempt, with the original
global gap still stated unless it has actually been closed.

[directory]: ../symmetries/README.md
[s01]: ../symmetries/01_modular_self_duality/README.md
[s02]: ../symmetries/02_cutoff_reflection/README.md
[s03]: ../symmetries/03_normalized_jet_rotation/README.md
[s04]: ../symmetries/04_time_height_scaling/README.md
[s05]: ../symmetries/05_covariant_theta_jets/README.md
[s06]: ../symmetries/06_hodge_and_transverse_geometry/README.md
[s07]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/README.md
[s07-note]: ../symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md
[continuation]: ../brainstorm/02_SYMMETRY_PROGRAM_CONTINUATION_CONTEXT_20261018.md
[hodge-review]: ../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[old-plan]: 02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta-summary]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[local-summary]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[geometry-summary]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[manuscript]: ../manuscript/README.md
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[round-summary]: ../research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md
[integration]: ../reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md
[outer]: ../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[global]: ../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex
[symmetry-record]: ../numerics/SYMMETRY_BRAINSTORM_CONTROL_REPLAY_20261018.json
[hodge-record]: ../numerics/HODGE_MODULAR_ROTATION_REVIEW_CHECKS_20261018.json
[history]: ../DRAFT_HISTORY.md
[large]: ../../../../LARGE_FILES.md
[chat-workflow]: ../../../../tools/CHAT_HISTORY.md
