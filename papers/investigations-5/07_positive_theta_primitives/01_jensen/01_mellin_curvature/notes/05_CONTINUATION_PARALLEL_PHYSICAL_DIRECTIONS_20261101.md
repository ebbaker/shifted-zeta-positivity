# Continuation: parallel investigation of six physical directions

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

## Purpose and scope of this packet

Edward Baker requests research overviews and progress files for the six
physical directions, and a continuation for a parallel investigation with
higher compute. This packet prepares that run; it does not launch workers
or claim their results. It is the entry point for the next session.

This is **parallel assessment packet r1**: six independent B assessments,
one worked candidate per branch, followed by separate checking and a
coordinator synthesis. Recommend Astra with a higher author-selected
effort, such as ultra if available, for the conceptual assessments. Record
the actual model/effort of every participant; the preparation itself used
Astra/xhigh. No model setting or numeric token budget has been changed.
Allocate extra compute to derivation, source inspection and adversarial
checking, rather than silently multiplying the number of campaigns.

The earlier [J-B10 plan r1](../research-plan/01_MELLIN_CURVATURE_RESEARCH_PLAN_20261101.md) remains an unchanged historical
single-attempt contract. The author’s new request broadens the next
Mellin investigation into these six bounded assessments; this packet
governs that launch and its new task IDs. It preserves the earlier
mathematical cautions. J-B10 remains the aggregate coordination objective
in the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md), with its quantitative estimate still
outstanding. The independent J-B11 signed-averaging session is outside
this packet and must not be edited or made a prerequisite.

## Read first and freeze the baseline

Read root instructions, the [model workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md), [result index](../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../avoid/README.md). In particular consult [physical-channel lessons](../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md),
[theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[target reformulations](../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[parallel-writer lessons](../../../../../../avoid/17_parallel_writers_and_broken_registries.md). The claim-specific controls below are
mandatory; they are not a demand to rerun all old certificates.

Mathematical inputs are [the accepted source/sign review](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md),
[the initial Mellin assessment](01_INITIAL_BRANCH_EVALUATION_20261101.md), [the comparative review](../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md),
[the explanatory route note](03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md), [the physical interpretations](04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md),
[the parent overview](../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md) and [the inspected primary-source record](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md).
Exploratory Notes03–04 have same-assistant analytical checking,
not independent assessment. Record exact commit/hash versions at launch
before workers begin; preparation hashes are in the J-E10 record under
the parent `numerics/`. Do not silently absorb later sibling edits.

### Shared formulas and status

At physical time zero keep the complete canonical source
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\]
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad c_n=0\ (n<0).
\]
Raw moments and exponential coefficients \(\gamma_n=n!c_n\) are different
normalizations. On the ordered chamber, the unnormalized Mellin integral is
\[
M_r(s)=\int_{\Omega_r}\Bigl(\prod_j u_j^{2s}\Bigr)
V(\mathbf u^2)\det[\Phi^{(2i)}(u_j)]\,d\mathbf u.
\]
At integer \(k\ge0\), \(M_r(k)=F_{r,k}D_{r,k}\), where
\(F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!\). Do not infer a noninteger
Toeplitz formula by formal integration by parts.

The accepted global pair \(R'>0,K>0\) gives the order-three signed-averaging
input at its stated internal-review scope. With
\[
w_s=\prod_{j=1}^3u_j^{2s}\Phi(u_j)V(\mathbf u^2)V(R(\mathbf u)),\quad
Z=\int_{\Omega_3}w_s,\quad d\mu_s=w_s/Z,\quad T=2\sum_j\log u_j,
\]
Here \(R=\Phi''/\Phi\), and the unchanged insertion is
\[
h=h_3=\frac{\det[\Phi^{(2i)}(u_j)/\Phi(u_j)]_{i=0,1,2;\ j=1,2,3}}
{V(R(\mathbf u))}.
\]
It satisfies \(A(s)=E_s h>0\) for
\(s\ge0\), and \(M_3=ZA\). Its negative origin region is retained.
Coordinatewise monotonicity does not extend unchanged to order four.
The target is the complete expression
\[
\mathcal C_3=(\log M_3)''=\operatorname{Var}_sT
+\frac{\operatorname{Cov}_s(h,(T-E_sT)^2)}{A}
-\left(\frac{\operatorname{Cov}_s(h,T)}{A}\right)^2.
\]
It is not an ordinary positive-state variance. Positive association or
monotonicity of \(A\) alone does not bound it.

The unproved sufficient comparison and its consequence are
\[
\mathcal C_3(s)\le\kappa_3(s)
=\sum_{j=0}^2\sum_{\nu\ge0}(s+j+\tfrac12+\nu)^{-2},\quad s\ge0,
\]
\[
Q_{3,k}:=\frac{M_3(k-1)M_3(k+1)}{M_3(k)^2}
\le G_{3,k}:=\frac{2k+5}{2k-1}
\quad\Longrightarrow\quad
D_{4,k}\ge\frac3{k+3}\frac{D_{3,k}^2}{D_{2,k}}>0.
\]
The middle comparison uses the triangular integral of the curvature over
\([k-1,k+1]\). Given positive lower-order inputs, the weaker exact condition
\[
Q_{3,k}<B_{3,k}:=\frac{(2k+6)(2k+5)}{2k(2k-1)}
\]
is just the next determinant’s sign condition. Classify it as a
reformulation, not a new estimate. Preserve the pointwise Gaussian →
integrated Gaussian → exact sign-condition hierarchy. The first
substantive index is \(k=1\), so \([0,2]\) matters; the \(k=0\) triangular
anchor is separate. Known order-four positivity makes this a method
pilot. No finite-order result establishes arbitrary-order induction or RH.

## Independent assignments and status ownership

Each local progress file is the sole live register for its `MCnn-`
namespace. J-B10’s aggregate status remains in the Jensen register; the
parent progress README is only a routing index. Historical J-B06, J-B10
discussion notes and J-E09 retain their identities. There is no duplicate
branch-status table in a shared register.

| Assignment | Distinct deliverable | Local documents |
| --- | --- | --- |
| MC01-B01 — Circle thermal trace | A source identity with a specific term in the complete Mellin curvature that it bounds. | [Overview](../01_circle_thermal_trace/research-overview/01_CIRCLE_THERMAL_TRACE_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../01_circle_thermal_trace/research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) |
| MC02-B01 — Fermionic correlators and Slater overlaps | A bound or exact obstruction for the original overlap or its Mellin response, with normalization and signs retained. | [Overview](../02_fermionic_correlators/research-overview/01_FERMIONIC_CORRELATORS_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../02_fermionic_correlators/research-progress/01_FERMIONIC_CORRELATORS_RESEARCH_PROGRESS_20261101.md) |
| MC03-B01 — Connected Mellin response | The Gaussian curvature bound or a clearly weaker integrated comparison, on an explicitly covered domain. | [Overview](../03_connected_mellin_response/research-overview/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../03_connected_mellin_response/research-progress/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_PROGRESS_20261101.md) |
| MC04-B01 — Biorthogonal ensembles and inserted Ward identities | A closed relation or explicit nonclosure term affecting the complete response, not just carrier fluctuations. | [Overview](../04_biorthogonal_ensembles/research-overview/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../04_biorthogonal_ensembles/research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md) |
| MC05-B01 — Schur specialization and Toda structure | An independently justified theta constraint with a definite effect on the rectangular minors or their neighboring-index ratio. | [Overview](../05_schur_toda_structure/research-overview/01_SCHUR_TODA_STRUCTURE_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../05_schur_toda_structure/research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) |
| MC06-B01 — Topological field theory and protected observables | An exact observable match plus an independent consequence, or a scoped obstruction to the selected candidate. | [Overview](../06_topological_field_theory/research-overview/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_OVERVIEW_20261101.md) · [Sole progress register](../06_topological_field_theory/research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md) |

The circle and fermionic tasks separate source spectrum from orbital
geometry; the ensemble and Schur tasks separate integration identities
from coefficient algebra. The response task directly addresses the
quantitative target. The topological task has an early feasibility gate.
All six start from the same baseline, not from one another’s unreviewed
output. A promising connection is sent as a conditional, versioned lead.

## Execution and use of additional compute

1. **Coordinator setup.** Refresh the current chat’s registered history,
   reread the aggregate and local registers, record input versions and
   actual settings, and check that no branch is already being worked by
   another writer. Preserve existing ownership instead of starting a
   duplicate task. Creating author-visible chats is separate from using
   subagents; this packet does not require six new sidebar chats.
2. **First assessment wave.** When this packet is invoked to execute the
   investigation, assign one worker per direction, subject to the actual
   concurrency limit. With four total agent slots, keep one coordinator
   and run up to three workers at a time; six branches then require two
   waves. Suggested first wave: MC03, MC04, MC01; second: MC02, MC05, MC06.
   This is a scheduling preference, not a mathematical dependency. Pass
   the shared formulas, local overview and register, and exact output
   ownership to each worker. Do not dispatch all six if slots are absent.
3. **Bound each attempt.** Each worker compares at most two concrete
   candidates, selects one, and works it to a proof, scoped failure or
   explicit surviving term. Record actual settings; never infer that a
   larger requested budget was selected. Progress updates should say
   what has been learned and what obligation remains.
4. **Separate checking.** Freeze each return before assigning its review
   to a different available worker. Allocate its stable local review task
   ID before starting and fix the claims, checks and disposition criteria
   from the frozen return. Use a separate same-model or
   cross-model internal pass as actually available and record that
   relationship. For a fixed algebraic/verification contract use E/Sol;
   conceptual strategy selection remains B/Astra. Check every claimed
   mathematical gain, rather than merely accepting a completion message.
   Do not overwrite an author’s return to hide a defect: save a correction
   or review disposition with links and exact scope.
5. **Synthesis.** The coordinator compares the six returns and their
   reviews, eliminates duplicate mechanisms, identifies which new input
   survived, and recommends at most one primary next task plus one
   fallback. Report unresolved branch work explicitly; an interrupted
   branch is not a completed assessment. Higher compute does not oblige
   a positive result or another unbounded search round.

A finite certificate is only ready after a B return fixes its expression,
cases/domain, method, error budgets, precision/refinement limits and
acceptance test. Do not launch growing grids, derivative escalation,
root/PDE simulations or coefficient acquisition merely because more
compute is available. Bounded exact checks supporting a derivation must
state their purpose and limits.

## Common acceptance and control screen

Every proposed criterion or mechanism must first be classified: generic
identity, equivalent reformulation, sufficient estimate, partial-domain
estimate or heuristic. A new estimate must add a premise or calculation
beyond the original unknown sign. Keep the signed insertion and all
normalizing factors. Account for the origin, coincident-node faces, full
spatial tails, \(s\in[0,2]\), remaining compact values and unbounded \(s\)
whenever claiming the global response bound. Explicitly state unpaid
regions for partial results. A spatial-tail estimate and a large-\(s\)
estimate are different claims.

- Gaussian equality checks normalization; it does not prove theta’s bound.
- The initial assessment’s two-point relaxation screens association-only
  reasoning. It does not realize theta, its orbital family or Toeplitz
  coefficients.
- Wick, wedge and Schur identities are generic and can survive the smooth
  even collision controls. Carrier biorthogonality additionally requires
  increasing \(R\); this premise has not been verified for all controls.
- Exact unchanged theta reconstruction distinguishes the canonical source
  from modified Euler-factor, weighted-square, reflected and
  positive-primitive controls. That identification alone supplies no
  quantitative estimate. For each candidate name the premise each
  relevant control fails or mark its status untested; do not fabricate
  a completed screen.
- A positive-time collision does not contradict a time-zero finite-order
  theorem. A finite-domain certificate need only be screened on a domain
  appropriate to its claim. Scope every failure to the tested class and
  mechanism.

An assessment may complete with a precise obstruction, while its target
remains open. Background-only returns, including new names for existing
identities, are insufficient. No supersymmetric index, Donaldson invariant,
local interacting theory or positivity-preserving integrable flow may be
claimed without the actual construction and applicable theorem.

## Files, shared writes and histories

Workers own only their assigned direction’s new `notes/`, `numerics/`,
local navigation and progress file. Reviewers own their assigned review
files; designate one writer to integrate their disposition. Preserve all
prior notes, evidence, issued plans and sibling directories as read-only
inputs. New sources are checked against primary statements and submitted
to the coordinator for the common reference catalog; PDFs remain outside
Git under [the large-files policy](../../../../../../LARGE_FILES.md).

Only the coordinator edits aggregate J-B10, shared navigation, reference
catalogs and cross-branch synthesis. Serialize any shared Jensen update
with exclusive `fcntl.flock` on
`papers/investigations-5/07_positive_theta_primitives/01_jensen/research-progress/.jensen-progress.lock`:
lock, reread, narrow edit, atomic replace, unlock in one process. Never
rebuild a shared file from a pre-lock read or edit J-B11’s row. Across
separate clones designate a single integrator; a local lock is insufficient.

Use [the history workflow](../../../../../../tools/CHAT_HISTORY.md) at the beginning and end of each
author-visible reply. This coordinator chat remains registered under the
parent Mellin `chat-histories/`; preserve its unique identity and original
number. Genuinely new author-visible branch chats register their actual
identity in the chosen child’s `chat-histories/`. Do not copy the coordinator
transcript into six homes, hand-edit generated histories or include
private subagent correspondence as public chat. The bounded exact-turn
final-capture call must be the last tool action unless a trusted active
completion hook is verified.

## Returns, review and launch prompt

Each overview names its first `notes/01_..._RETURN_YYYYMMDD.md` file;
use actual local dates and next unused numbers. Required content:
selected input and versions; actual model/effort; exact claim and status;
worked derivation or scoped obstruction; endpoints, tails and unpaid
domains; control screen; support files; and one next B/E recommendation.
Review files go in each child’s `reviews/`, with a distinct author/model
relationship and an accept/correct/unresolved disposition.

The coordinator saves the comparison in parent
`reviews/01_PARALLEL_PHYSICAL_DIRECTIONS_ASSESSMENT_YYYYMMDD.md` (next
unused number if needed), then a synthesis/continuation in parent
`notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_YYYYMMDD.md` (also next
unused). Explain actual mathematical gains, failed premises and remaining
obligations; update accepted-summary navigation without upgrading review
status. The final chat answer should give a brief outcome for every
branch and the best justified next step. Do not edit the issued packet
to make it appear to have anticipated later results.

Suggested restart instruction:

> Execute this parallel assessment packet for all six physical directions.
> Use the higher model/effort settings selected for the session and record
> their actual values. Follow the six local overviews and canonical progress
> files, use disjoint worker ownership within the available concurrency,
> retain the complete signed theta observable, and give each branch one
> bounded assessment followed by separate checking. Save the returns,
> reviews and coordinator synthesis, and report which new input, if any,
> advances the Mellin comparison. Return scoped failures honestly and do
> not start unspecified numerical campaigns.
