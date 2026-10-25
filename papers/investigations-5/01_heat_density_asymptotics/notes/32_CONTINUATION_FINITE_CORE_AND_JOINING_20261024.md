# Continuation: finite-core accuracy and joining the endpoint models

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0007's session metadata. Thread
`01a17067-eabc-7872-abc9-d9319b53bc41`.

**Status: continuation and research specification; no new theorem or
numerical result.** This is the current research handoff after
[Notes 30][saddle] and [31][positive]. It supersedes [Note 29][previous]
as the next-task entry point, while preserving that note's historical
instructions and findings. The endpoint and outer comparisons now exist
at their stated eventual scopes. The missing work is an informative
finite core and the errors introduced when the models are joined.

The manuscript is a separate, versioned deliverable. Sol has completed
HDA-10-MI1 r1 through Note 30 in the **54-page** reading copy. Note 31 was
deliberately excluded from that frozen production request. The author's
current request produced [Review 15][manuscript-review], with proposed
changes for a subsequent Sol revision. No manuscript, PDF, frozen
integration specification or research proof was changed in this turn.

## 1. Read first and preserve the workflow

Start with the repository [AGENTS.md][agents], [chat-history policy][history-policy],
[model workflow][workflow] and [large-file policy][large]. Then read the
[result index][results], particularly [heat-flow results][geometry] and
[collision controls][controls], and the [avoid index][avoid]. The most
relevant cautions are [shared-premise reviews][a05], [evidence and status][a06],
[scoped exclusions][a07], [numerics before a question][a10], and
[separate estimates losing cancellation][a12]. This remains a quantitative
approximation program, not an RH-equivalent criterion or a simplicity test.

Use the existing [overview][overview] and sole [progress register][progress].
Do not create another task ledger. Astra owns the analysis; Sol owns
numerical implementation and execution, including machine symbolic and
exact-arithmetic checks. Edward Baker carries requests between chats.
Manuscript production is a separate housekeeping assignment and is not
a numerical research packet. No agent, chat message or computation is
dispatched by this note.

Read these mathematical inputs in order:

1. **Note 31, PE1--PE44 and Review 13:** positive evolution, actual
   covariance, residual corrections, differentiated inner overlap and
   compact-time outer estimates. This is the latest result.
2. **Note 30, FS3--FS34 and Review 12:** the implicit branch, complete
   convolution proof, physical collars, mass anchor, static comparison
   and exact nonzero residual on which Note 31 depends.
3. **Note 26, NE1--NE24:** negative endpoint, direct time/current estimates,
   sharper covariance cancellation and source-derived traces.
4. **Note 25:** complete-source pre-switch tails and the precisely scoped
   positive-cutoff obstruction. These determine where a finite core is
   sufficient and where a fixed source cannot be the exterior model.
5. **Notes 20 and 23:** finite heat field, source/jet and nonlinear
   transfer, actual covariance, declared transition contract and failed
   trial. Read the recorded failure before proposing a new computation.
6. **Notes 14, 16 and 19 as needed:** exact adaptive equations and the
   sharper inner clock transport theorem. Notes 27--28 remain the source
   of the linear gamma switch-layer profile and uniform-positive-q
   transfer; their exponential height restriction is historical for
   that model, not a restriction on the full saddle.

## 2. Mathematical state to carry forward

All results in this table retain **proved in-note; same-assistant review
only**. The constants/onsets of the positive saddle theorems have not
been numerically instantiated.

| Input | Established scope and useful error | What it does not supply |
| --- | --- | --- |
| [Note 26][negative] | At t=-T, all real x and the declared expanding transverse buffer: density O(T^-2), current O(T^-5/2), density time derivative O(T^-3), physical potential/weight O(T^-1), potential time O(T^-2), actual covariance O(T^-3), covariance Laplacian O(T^-4); forcing and traces paid | A finite-time transition or an earlier-simplicity conclusion |
| [Note 25][tails], before the spatial switch | Every fixed compact time slab ending at 64: complete-source exponential tails for the regulated background, time/current, covariance and traces, with explicit slab-dependent constants | A bound uniform as the slab's upper time tends to infinity; the same floor argument after the spatial switch |
| [Note 30][saddle] | Full gamma saddle for t>=32 and 2+t+X sufficiently large: static U,W jets through four and density error C e; all-height late-time rate O(t^-1/2 log^-2(2+t)); compact [32,T] outer rate O_T(X^-2) | Evolution merely from differentiating that static allowance |
| [Note 31][positive], PE6 | All real x at sufficiently large t: current, direct time terms, forcing/source and actual Q/Delta Q error C A<=C t^-1/2; density/curvature spatial jets through two retain C e | Relative accuracy at every small inner transport scale; an autonomous closure |
| Note 31, PE44 | Every fixed [32,T], including the flat switch: static errors O_T(X^-2), current/covariance O_T(log^2 X/X^2), time-dependent terms O_T(log^2 X/X), retained equation corrections O_T(X^-3) | An exchange of compact-time and late-time limits without their separate quantifiers |
| [Notes 16/19][inner] | Buffered inner window of size kappa^(1/3): explicit phase density error O(kappa^-1/2), current and density-time error O(L kappa^-7/6)=o(L/kappa) | A source-anchored potential or actual covariance attached to the clock by definition |
| [Notes 20/23][finite] | Arbitrarily accurate finite-source jets on each fixed compact slab; explicit nonlinear and actual-covariance transfer on a full buffer with positive regulator floor | Acceptance of the old 192-cell trial, useful transition cost or global joining |

In this table, for the positive saddle,

\[
X=|x|,\qquad \mathcal L=\log(2+t+X),\qquad
N_*=1+X+t\mathcal L,
\]
\[
e=\frac{t^{3/2}}{N_*^2},\qquad
A=e\mathcal L^2,\qquad d=\frac{t}{N_*^3}.
\]

The model's observable equation corrections have allowance C d, with
late-time bound C/[t^2 log^3(2+t)]. This smaller residual is separate
from the C A comparison error. Closeness was proved from the complete
source and nonlinear transfer, not inferred from a small residual.

The differentiated overlap with the explicit clock is only

\[
\|J_{P_*}-J_L\|_{\rm inner}
+\|(R_{P_*})_t-(R_L)_t\|_{\rm inner}
\le C t^{-1/2}+C L\kappa^{-7/6}.
\]

It tends to zero absolutely but does not inherit the sharper inner
relative scale. The full saddle already covers all heights at late
time; a spatial splice to the clock is unnecessary for that endpoint.

**Ledger status:** HDA-16 and HDA-19 are Complete at the stated eventual
comparison scopes. HDA-17 is Ready, with no accepted finite bridge;
HDA-18 is Gated by the finite-core and joining budgets. HDA-04/05/06
retain their broader unresolved obligations. HDA-20 is Ready but has
no distinct-reviewer audit. This continuation changes none of these.

## 3. Fixed physical conventions

Keep the complete canonical theta source and

\[
H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8,\qquad z=x+iy.
\]

Height is x. The physical density is unnormalized. Fix ell,h>0 and
the spatial kernel K=k_ell k_h with
`k(v)=(315/256)(1-v^2)^4` on [-1,1], zero outside. It has bounded
weak derivatives through order four. All bounds require the full
convolution support and the analytic disks used by the collar proofs.
Time averages or moving widths require their own extension of the contract.

Use the **same** q=epsilon_g^2 and r=log q for every field. The regulator
is exactly Note 20 FB1--FB2 / manuscript Section 2:

\[
\epsilon_b=\eta\frac{\Phi(0)\sqrt\pi}{2}(1+t^2)^{-1/4},\quad
\epsilon_+=M_0\kappa^{-1}e^{-x^2/(2\kappa)},\quad
\epsilon_g=\epsilon_b^{1-\chi}\epsilon_+^\chi
\]

where the last expression is used above 64, epsilon_g=epsilon_b below,
and chi is the specified flat switch from 64 to 128. The real saddle
satisfies `4 pi exp(4L)=2tL+9`, `kappa=8tL-2t+36`, and

\[
M_0=2\pi^2 e^{tL^2+9L-\pi e^{4L}}\sqrt{2\pi/\kappa}.
\]

The values 32,64,128 are proof/switch parameters, not certified onsets.
For t>64 the regulator has no positive lower bound on the whole height
axis. A positive floor may only be used on a declared compact full buffer.

For any comparison field F, retain the actual definitions

\[
S_F=\log(|F|^2+q),\quad w_F=q/(|F|^2+q),\quad
\rho_F=\frac{q|F_z|^2}{\pi(|F|^2+q)^2},\quad
j_F=\frac{qF_{zz}\overline{F_z}}{\pi(|F|^2+q)^2},
\]
\[
U_F=K*S_F,\quad R_F=K*\rho_F,\quad J_F=K*j_F,\quad
Q_F=K*((S_F)_x^2-(S_F)_y^2)-((U_F)_x^2-(U_F)_y^2).
\]

Retain the physical potential offset, actual signed source, potential
forcing and spatial curvature. Both partial_t averaged C and
(partial_x^2-partial_y^2) averaged C occur in the density equation.
The signed stress must be paired before taking absolute bounds; separate
gradient-square estimates can lose uniformity as q shrinks.

The full saddle P_* is PE1 with the specified large right-half-plane
branch, not the older P_lin. Its residual is PE8, and its observable
equations are PE37--PE39. Its algebraic current residue F_zz/F_z at a
root differs from that root's velocity by the residual divided by F_z.
Do not substitute a fitted zero speed into the current formula.

## 4. The next bounded analytical deliverable

**Derive one finite-core-to-overlap error contract for HDA-17/HDA-18.**
The first result should be a theorem with a specified finite input and
explicit error composition, not another list of possible approximations.
Proceed in this order.

### A. Declare a cover and the required norms

Choose eventual endpoint cutoffs T_- and T_+, and positive overlap
widths tau_-,tau_+. The negative model is available for t<=-T_-;
the positive full saddle for t>=T_+. Supply the finite model on a slab
containing `[-T_- - tau_-, T_+ + tau_+]`, with its full spatial buffer.
The endpoint overlap bands then lie within that slab. Keep the cutoffs
symbolic until their gates and error bounds have been made effective;
do not present a guessed finite value as an established onset.

On this compact slab, Note 25 covers outer heights up to time 64 and
PE44 covers outer heights from 32 onward. The interval [32,64] allows
the exterior descriptions to be compared through H. After choosing
uniform outer thresholds for the two **fixed** slabs, the remaining
spatial problem is a finite core. Include overlap bands and full support
buffers in the core width; no contour or kernel may cross an unpaid edge.

State errors for U,W through spatial order four; R and averaged C
through order two; J,Q and the direct time/forcing/source terms through
the orders consumed by the adaptive equations. Include normal potential
and current traces. A smaller norm is permissible only after showing
which terms no longer need its omitted derivatives. Specify useful
absolute tolerances or scales for each component; no relative error is
required at a zero of an observable. This cover is a proposed assembly
plan, not an already proved global approximation.

### B. Identify exactly what finite input the joins consume

Start from Note 23's cellwise source allowances and amplitude-aware
transfer, rather than its rejected mesh. Derive how finite source/jet
errors on the buffered core pay the preceding observable norms,
including adaptive curvature and forcing after time 64. Derive the
needed jet orders before selecting a mesh. Preserve separate source
interpolation, arithmetic-mode tail, source tail, arithmetic evaluation
and averaging allowances.

For two source-compared models F_i,F_j on an overlap, their observable
difference is bounded by their two errors against H. Their derivatives
and traces need the corresponding already-proved derivative errors.
The first useful output is a finite table of these overlap allowances
and the source accuracy sufficient to meet them. Note 23's original
[-16,64] trial is evidence about that trial, not a chosen cover of the
new all-time task.

### C. Specify the object being joined before using its equations

An overlapping collection of field-derived observable tuples is a useful
intermediate deliverable. It is not yet a single globally smooth model.
For the eventual assembly, distinguish:

- A **time blend of holomorphic fields**, which retains spatial
  holomorphy. Even for exact heat fields its residual includes
  `chi'(F_2-F_1)`; the full-saddle component has its own residual as well.
  That field residual must be transferred to each observable equation,
  with the common q and actual covariance.
- A **spatial cutoff of fields**, which generally destroys holomorphy.
  Existing holomorphic density identities then cannot be reused unchanged.
  Either avoid that construction or derive all extra terms first.
- A **blend of observables**, for which potential/density compatibility,
  the current balance, cutoff derivatives and covariance do not follow
  from a componentwise convex average. Specify a legitimate potential
  and fluctuation term and pay their joining differences; do not define
  a fictitious Q by the desired equation.

Choose one route after the overlap estimates identify its actual costs.
If a reduced PDE is used to propagate errors, state and prove the
required stability estimate. Direct source comparisons do not themselves
give stability of an unrelated closed PDE.

### D. Stop at an explicit analytical disposition

A successful next round should produce the cover, full norms, finite
source accuracy requirement, and one proved compatibility/joining
estimate, with remaining terms named. If the proposed join fails,
record the term and class of constructions that fail. Do not silently
weaken physical normalization, remove an equation or enlarge a failed
numerical campaign.

Only then, if evaluation of a finite quantity can change a decision,
prepare a bounded Sol numerical packet in the existing handoff directory.
Name the exact formulas, input hashes, finite cases, precision/tolerance,
separate errors and stopping rule. The numerical queue is currently empty.

## 5. Scope, controls and manuscript follow-up

The negative Taylor and finite-field inequalities are generic enough to
hold for smooth colliding controls with their own constants. The gamma
application needs the unchanged completed xi source, reflection and full
ordinary Dirichlet coefficients; changed-source controls do not inherit
those premises. Atomic/heat-polynomial controls do not have the required
canonical smooth source. A simple-root collar result applies only on its
proved domains, and excludes no collision elsewhere. Use the detailed
premise screen in Note 31 Section 10 and the collision register before
claiming anything beyond approximation.

Keep both cutoff obstructions at their proved scopes: fixed compact
sources fail at positive infinite time; a finite piecewise-linear source
with positive cutoff value fails the fixed-time off-axis physical-potential
contract after 64. Neither is a universal impossibility for adaptive
cutoffs, tapered/noncompact sources, different norms or density alone.

[Review 15][manuscript-review] recommends fixing the remaining source-bound
notation, integrating Note 31 with its full proof and residual equations,
adding an early model/domain guide, and making the inner finite allowances
more self-contained. Edward Baker will ask Sol to make changes. Preserve
HDA-10-MI1 r1 as completed historical production; do not rewrite its
frozen scope to include Note 31. The new review is not HDA-20.

## 6. Records and next-chat entry

Save derivations in `notes/`, assessments in `reviews/`, any authorized
numerics in `numerics/`, and updates in the existing progress register.
Use concise DRAFT_HISTORY entries, without new manuscript snapshots.
The current thread retains history 0007. A new research or Sol chat must
register its own actual identity in this investigation's `chat-histories/`;
never reuse this thread ID or renumber an existing conversation. Refresh
at the beginning and end, with the bounded exact-turn final capture until
trusted hook activation is verified.

Suggested next research instruction:

> Continue from Note 32 using GPT-6 Astra and the live progress register.
> Derive the first finite-core-to-overlap error contract in Section 4,
> using Notes 25, 26, 30 and 31 as scoped inputs and Note 23's local
> source transfer. Specify the cover, required jet/observable norms and
> an informative joining allowance before requesting any computation.
> Preserve the physical regulator, actual covariance and model residuals;
> record a failed route explicitly. Save notes, progress and chat history.

**Next: Analytical — Astra.** The finite-core accuracy consumed by a
legitimate join is the missing estimate. Manuscript changes can proceed
separately in Sol from Review 15; no numerical research task is ready.

[agents]: ../../../../AGENTS.md
[history-policy]: ../../../../tools/CHAT_HISTORY.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[large]: ../../../../LARGE_FILES.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[previous]: 29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md
[saddle]: 30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[positive]: 31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[negative]: 26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
[tails]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[inner]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[finite]: 23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md
[manuscript-review]: ../reviews/15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md
