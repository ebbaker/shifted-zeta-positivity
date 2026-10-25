# Research program: asymptotics and evolution of averaged zero density

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**,
verified from this turn's metadata.

**GPT model ownership, author decision of 24 October:** GPT-6 Astra leads
analytical formulas and proofs; GPT-6.1 Sol performs all numerical work.
The author manages the chats manually. Follow the
[shared handoff workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md);
the existing progress register records the next owner and packet.

**Purpose.** Find a relatively simple explicit formula for the unnormalized
smoothed density, defined for every real heat time \(t\), and progressively
refine it into an approximation to the canonical theta solution with
proved control extending to arbitrarily large height. Analytical estimates
on unbounded height domains have priority; numerics support named steps
in those estimates.

**Long-term goal, clarified by Edward Baker on 24 October 2026.** The
eventual construction must satisfy the appropriate evolution equations,
with the required fluctuation terms retained, and the correct asymptotic,
spatial boundary and source-anchor conditions. It must remain provably
close to the true solution throughout time, including the finite-time
transition between the negative- and positive-time regimes. Any auxiliary
potential, current or covariance needed to express these equations is part
of that construction.

Seek a decomposition of the form
\[
R_{\mathrm{true}}(t,\cdot)
=R_{\mathrm{app}}(t,\cdot)+\mathcal E(t,\cdot),
\qquad
\|\mathcal E(t,\cdot)\|_{X_t}\le B(t),
\qquad t\in\mathbb R,
\]
where \(R_{\mathrm{app}}\) has a relatively simple mathematical form and
\(B\) is an explicit, proved error bound on the stated spatial domains,
with the averaging and regulator specified. The bound must remain
informative across the full time range; its scale may depend on time
because the physical density is unnormalized. Distinguish the error
against the regularized theta density from the additional regulator error
against smoothed zero counts, as in (P6) below.

Each improvement should sharpen the explicit approximation, reduce its
proved error or extend the domain on which the bound is useful. The
current endpoint formulas and bounded-window estimates are intermediate
steps toward this all-time objective. A reduced formula with omitted
fluctuations must retain their quantified equation residual and a stability
estimate connecting that residual to solution error. This global
construction and error theorem remain open.

## Revision decision and the current starting point

**Current priority, clarified by Edward Baker on 24 October 2026:**
analytical results extending to infinite height lead the program. The
earlier choice to finish a bounded-window bridge before starting positive
outer-height analysis is superseded. Notes 30--31 now supply HDA-19's positive model and HDA-16's
all-height endpoint evolution comparison. The current analytical
deliverable is HDA-17/HDA-18's finite-core and joining error contract.
HDA-17 supplies finite-transition estimates needed by that global program;
passing its existing bounded numerical pilot is not a prerequisite to
HDA-19. The [current new-session handoff][priority] specifies the next
finite-core and joining deliverable after Notes 30--31. The separate
[manuscript review][manuscript-review15] has now been implemented in the
65-page manuscript, including Note 31; this changes no research status.

Keep this overview and its existing [progress register][progress]. The
objective, canonical source, physical density and exact equations are
unchanged. Existing task identifiers and historical evidence are retained;
this priority amendment adds no theorem or completed research task.

| Program obligation | Current implementation |
| --- | --- |
| Define the unnormalized averaged density and its error | State the height/time quantifiers, transverse buffer, regulator, kernels and informative norm before a comparison; keep regulator-to-zero-measure error separate. |
| Obtain both time endpoints and their fluctuations | Use Note 26's negative system and Notes 30/31's positive system, actual covariance and differentiated inner overlap, retaining their scopes and model residuals. |
| Construct and compare the approximation | Use direct source comparison or another proved analytic representation; an autonomous reduced PDE remains an alternative with its own stability obligation. |
| Match asymptotic, boundary and source data | Pay both spatial interfaces and time overlaps, with full buffers, source-derived traces and all joining residuals. |
| Extend the approximation globally | Work on unbounded height domains now. A bounded-height all-time result is a supporting subresult when it supplies an explicit input to the global theorem. |

**HDA-15 checkpoint:** [Note 23][local-bounds] supplies a transition
contract and sharper source, nonlinear and actual-covariance bounds. Its
192-cell diagnostic fails the contract. Those findings remain useful,
but a larger mesh is not the default continuation.

The present analytical inputs are:

- [Note 31][positive-system] gives all-height positive current, time,
  forcing/source and actual Q/Delta Q errors O(t^-1/2), with derivatives
  required by the adaptive equations. Both curvature derivatives and
  O(t/N^3) model equation corrections are retained. It proves
  differentiated inner overlap and compact-time outer evolution across
  the flat regulator switch, with time errors O_T(log^2 X/X). HDA-16/19
  are complete at their stated comparison scopes, not the finite-core
  or all-time assembly. Global absolute rates do not replace sharper
  inner transport information. [Review 13][review13] is same-assistant
  only; no numerical onset or independent audit.
- [Note 30][full-saddle] replaces the linear gamma factors by their full
  implicit saddles and Gaussian determinants. For t>=32 and sufficiently
  large t+X, its density and physical potential/filtered-w spatial jets
  have error O(t^(3/2)/(1+X+t log(2+t+X))^2). This supplies an all-height
  positive endpoint O(t^-1/2 log^-2 t), an outer estimate uniform in t,
  and actual static overlap with Note 19. Both connectors, the middle,
  arithmetic modes, tails and physical regulator are paid. Its exact
  nonzero heat residual is retained. Note 31 supplies the subsequent
  evolution/covariance comparison; finite-transition assembly remains
  open. Onsets are eventual and [Review 12][review12] is same-assistant only.
- [Note 25][outer-tail] gives complete-source exponential jet bounds and
  explicit outer observable tails on compact slabs ending at 64. At fixed
  t>64, the finite positive-cutoff source has divergent source-anchored
  potential error on its stated off-axis buffers. Its scoped obstruction
  remains valid alongside the noncompact representation in Note 27.
- [Note 26][negative-system] completes the negative endpoint's stated
  all-height direct-comparison budgets, including actual Q and Delta Q
  errors O(T^-3) and O(T^-4). Note 31 supplies its positive counterpart; full assembly
  remains open.
- [Note 27][gamma-outer] supplies a complete-source gamma-pair estimate,
  physical zero collars and weak regulator transfer for each compact time
  interval strictly above 64. Its five-term static outer density has
  O(log^2|x|/|x|) absolute error; omitting phase adds O((log|x|)^-4).
  Constants/onset are not numerically instantiated. The outer limiting
  profile is nonuniform at the regulator switch, and no joint large-time
  overlap or positive evolution/covariance budget is claimed there.
- [Note 28][joint-outer] now gives density comparison with the explicit
  gamma pair using the same physical q, uniform across the switch, and
  a joint range 32<=t<=(log X)/4 with O(X^-3/4(1+log^4 X)) absolute
  error. Physical averaged-potential and filtered-w spatial jets through
  order four have the same rate. It resolves the narrow regulator layer
  and records the exact model heat residual. Its exponential outer
  threshold has no inner overlap within that older proof; Note 30 now
  supplies static overlap with a different saddle model; positive
  current/time/covariance comparisons were open at that stage; Note 31
  supplies the later comparison. Notes 25--31 have same-assistant review
  only. Notes 25--28 and 30--31 are now integrated in the 65-page manuscript;
  the older HDA-10-MI1 r1 freeze remains historical.

- [Notes 11][negative] and [12][positive] give the all-height negative Gaussian estimate,
  positive growing-window carrier, determinant bounds and global analytic
  fallback. [Note 14][adaptive] supplies the variable-regulator corrections
  and adaptive negative profile.
- [Notes 16][transport] and [19][explicit] give the differentiated explicit
  clock on buffered windows of size X~kappa^(1/3), with density error
  O(kappa^-1/2) and current/time error O(L kappa^-7/6). Its phase is exact;
  its actual potential/covariance comparison remains incomplete.
- [Note 20][bridge] fixes a smooth global regulator and proves finite-slab
  source/jet, density/current/time and actual covariance/Laplacian stability.
  Informative transition parameters and overlap have not been established.
- The [maintained manuscript][manuscript] consolidates results through Note 31 with brief diagnostic support. Its 65-page
  [build record](../manuscript/BUILD_RECORD_20261024.json) and
  [production assessment](../reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md) record the Review 15 revision.
  HDA-10-MI1 r1 remains the earlier completed through-Note-30 production. [Note 21][integration] records the
  earlier integration and sharper determinant mean term. Research review
  remains same-assistant; Sol production is not an independent audit.

The [progress register][progress] holds statuses, dependencies and the
research history; this overview holds the objective, equations and
acceptance contract. Read the [result index][results], especially
[heat geometry][geometry] and [collision controls][controls], alongside
the [avoid index][avoid], especially [target classification][a01],
[scope][a07] and [status synchronization][a19]. This is an approximation
program judged by a function, domain and error bound, with no RH or
simplicity criterion.

## 1. The object and the comparison target

Retain the source manuscript's normalization:
\[
H_t=-H_{zz},\qquad
\rho_\epsilon=
\frac{\epsilon^2|H_z|^2}
{\pi(|H|^2+\epsilon^2)^2},\qquad \epsilon>0.
\]
The research function is
\[
R_{\epsilon,\ell_x,\ell_y,\tau}=\mathcal F_{\ell_x,\ell_y,\tau}\rho_\epsilon,
\tag{P1}
\]
where \(\mathcal F\) is a positive, unit-weight spatial/time average.
No division by total density mass is made. The averaging can be spatial,
temporal, or both; the final choice and scale dependence are part of
the research.

To quantify how this represents zeros themselves, also define
\[
\nu_t=\sum_{H(t,a)=0}m_a\delta_a,\qquad
R_{\rm zeros}(t,z)=
\int k_\tau(s)\int K_{\ell_x,\ell_y}(z-a)\,d\nu_{t-s}(a)\,ds.
\tag{P2}
\]
Keep fixed positive spatial smoothing when using (P2) as a smooth
function, unless spatial regularity from time averaging alone is
separately proved. A time average of moving point measures can remain
spatially singular.

The book's compact measure limit motivates (P2), but a quantitative
regulator-bias bound
\(\|R_\epsilon-R_{\rm zeros}\|_X\le E_{\rm reg}\) must be obtained in the
chosen regime. In particular the fixed-\(\epsilon\), negative-time
\(T^{-3}\) density from the brainstorm can be regularization background
on a region with no zeros. Matching that term is not by itself a
description of a nonzero zero population.

Each new bounded contract must specify the domain, kernels, scales, norm \(X\),
and limits being taken. Treat fixed regions, diffusive spatial scales,
and growing height/rank as distinct regimes. For centered time averages,
provide data on both sides of the observation time; for causal evolution,
choose a one-sided kernel and state its history data.

## 2. Determine asymptotic values and fluctuation scales together

The endpoint density and evolution comparisons are available at the
stated scopes of Notes 26/30/31; retain these inputs in the finite-core
and joining theorem.
At negative time, [Note 26][negative-system] now supplies current/time,
potential and actual covariance/Laplacian comparisons with the exact
global regulator on all real heights and its full transverse buffer.
Retain these estimates in the assembly; the earlier fixed-region covariance
expansion does not supply an adaptive all-time endpoint automatically.

At positive time, Note 31 supplies the actual potential/covariance
comparison from the full-saddle field and a regulator-uniform pole
estimate. Retain its signed-stress identity and the finite phase in
the separate differentiated clock. Defining a covariance to make a
chosen density equation hold is not that comparison. The cosine-cell
calculation remains a starting model, not a proved theta closure.

All endpoint estimates must hold on the full averaging buffer, with the
same regulator and stated norms as the transition comparison. A static
error cannot be differentiated to obtain a derivative error. Choose
thresholds from bounds that hold for the entire corresponding time tail;
a check at one large time is insufficient. In particular, the regulator's
switch points 64 and 128 are not theorem-onset times.

The all-height objective governs the next estimates. Distinguish
|x| tending to infinity at fixed time, uniformity over a compact time slab,
and joint large positive time/height limits. The existing growing inner
window does not establish uniformity over all real x at a fixed time.
State joint limits in regulator or averaging widths explicitly.

## 3. The exact evolution identifies what the approximation must retain

Write \(S=\log(|H|^2+\epsilon^2)\), \(U=FS\), \(R=F\rho\), and retain
the actual filtered gradient covariance
\[
Q=F(S_x^2-S_y^2)-(U_x^2-U_y^2).
\]
For a fixed filter and constant regulator, [Note 02][filtered] gives
\[
R_t=-\tfrac12(R_{xx}-R_{yy})
-\frac1{8\pi}\Delta(U_x^2-U_y^2+Q),\qquad \Delta U=4\pi R.
\tag{P3}
\]
\[
U_t=-\tfrac12(U_{xx}-U_{yy})-\tfrac12(U_x^2-U_y^2+Q).
\tag{P4}
\]
With
\[
j=\frac{\epsilon^2 H_{zz}\overline{H_z}}
{\pi(|H|^2+\epsilon^2)^2},\qquad J=Fj,
\]
the fixed-regulator current balance is
\[
R_t+2\Re\partial_zJ=0.
\tag{P5}
\]
These are the original fixed-regulator equations, not the current adaptive
contract. For that contract put
\[
q=\epsilon_g^2,\quad r=\log q,\quad w=\frac{q}{|H|^2+q},\qquad
\mathcal D=\partial_x^2-\partial_y^2.
\]
[Note 14][adaptive] defines
\[
\mathcal B=w\{r_t+\tfrac12(r_{xx}-r_{yy}+r_x^2-r_y^2)\},
\]
\[
4\pi C=2\operatorname{div}(w\nabla r)-w\Delta r
-w(1-w)|\nabla r|^2,\qquad
\mathcal S=(1-2w)(r_t\rho+\nabla r\cdot\mathbf j).
\]
The fixed-filter equations to use in the next phase are
\[
U_t=-\tfrac12(\mathcal D U+U_x^2-U_y^2+Q)+F\mathcal B,
\qquad \Delta U=4\pi(R+FC),
\tag{P4a}
\]
\[
R_t=-\tfrac12\mathcal D R-\frac1{8\pi}\Delta(U_x^2-U_y^2+Q)
+\frac1{4\pi}\Delta(F\mathcal B)-\partial_t(FC)-\tfrac12\mathcal D(FC),
\tag{P3a}
\]
\[
R_t+\operatorname{div}(F\mathbf j)=F\mathcal S.
\tag{P5a}
\]
Both derivatives of FC are required. The positive algebraic density and
potential curvature are different when the regulator varies spatially.
Moving filters require the additional commutators in Note 14; they are
not included silently in these equations.

Q is a difference of gradient variances, not a density variance or a
quantity of assumed sign. Ordinary smoothing need not be an idempotent
projection; cross correlations and potential boundary/harmonic data remain.
For the adaptive contract, even the local fluctuation identity is
\[
\Delta(S-U)=4\pi\{\rho-R+C-FC\}.
\]
A source-generated approximant supplies its own U and Q. A reduced model
that omits or substitutes them must estimate the resulting equation
residual and justify any inference from that residual to solution error.

## 4. Solve with compatible asymptotic and boundary data

**Primary route: analytical comparison with the canonical source.**
Use Notes 26/30/31 for the negative endpoint, positive endpoint and
compact-time positive exterior, including actual covariance, physical
potential and model residuals. Next derive the finite-core and joining
error theorem for HDA-17/HDA-18. Identify the source/jet accuracy consumed
by the joins before selecting a finite numerical calculation. Note 19's
exact-phase clock remains the sharper inner transport input; Notes 20/23
provide finite-source bounds where their hypotheses hold. Direct
comparison does not require closing an autonomous density PDE. A splice
must pay its own derivative and covariance terms; endpoint value errors
alone do not supply them.

The source-to-jet allowances of Notes 20/23 already hold for every real x
on a stated transverse buffer and compact time slab. On slabs ending at
t<=64, the common regulator has a positive uniform floor, so the existing
nonlinear comparison can also be uniform in x, though its constants may
be uninformative. The bounded pilot is not the domain of those lemmas.
After spatial regulator dependence turns on, that global floor is lost.
An absolute jet allowance alone does not then supply a uniform observable
error by the same argument. Derive height-dependent comparison estimates
or an appropriate weak bound; do not silently replace the regulator or
claim that the fixed-regulator fallback proves the adaptive result.

Sharpen global interpolation allowances by source-weighted, cellwise
bounds where needed; retain separate theta-mode and source-tail errors.
Use amplitude-aware nonlinear estimates to avoid losing the source scale
before comparison. Any normalization used internally must preserve the
physical density and retain the extra time/space terms it induces in an
evolution equation. Proposed refinements require proofs; no gain is assumed
from their names. A fixed compact source cannot represent the positive
infinite-time endpoint, as Note 20 shows for that class.

Supply full convolution buffers, the common regulator, source normalization
and source-derived boundary traces. The negative endpoint, finite bridge
and positive clock must be compared to the same canonical field. Endpoint
shape alone does not select theta: compact source perturbations can preserve
leading asymptotics while changing finite time.

Prove overlap on nonempty time intervals using each approximation's own
error against theta. A triangle inequality pays their value mismatch;
a differentiable joined evolution also needs all switching or blending
terms. For example, blending two exact heat fields introduces
chi'(t)(H_2-H_1). Density/current blends require the analogous balance and
constraint calculation. No unestimated splice completes an all-time theorem.

**Alternative route: a reduced potential-density evolution.** If a useful
closure is obtained, formulate a compatible boundary/anchor problem and
prove the needed existence, uniqueness and stability estimates. Do not
assume (P3a) is an ordinary forward parabolic equation or prescribe
incompatible data at both time ends. Direct source-error estimates can
establish approximation without such PDE propagation; a residual-based
claim of solution accuracy still requires its own stability argument.

## 5. Constrain and improve the solutions against the actual equations

The principal acceptance target covers all real x on a declared transverse
strip, with full averaging buffers and explicit time quantifiers. A
proposed error contract may take the form
\[
\sup_{x\in\mathbb R,\ |y|\le Y_0}
\frac{|R_{\rm app}(t,x,y)-R_{\epsilon_g}(t,x,y)|}{W_R(t,x,y)}
\le B_R(t),
\tag{P7}
\]
with a positive, explicitly prescribed reference scale W_R and a useful
bound throughout the stated time regime. W_R=1 is the absolute-error case.
Any weight must have a stated physical interpretation and cannot be chosen
afterward to conceal uncontrolled outer error. This is a target contract,
not an established theorem. State analogous norms for the other required
observables; the final assembly must cover all real heat time.

A theorem on |x|>=X(t), paired with a proved inner theorem and a controlled
overlap, can supply all-height coverage. A growing window or a collection
of finite samples alone cannot. A bounded-height all-time result may be
used as a sublemma, but its necessity for the global argument must be
identified before making it an execution priority.

Fix the regulator protocol, eta, kernel widths and norms before comparison.
Spatial averaging with fixed widths remains the current baseline;
time averaging and moving widths remain allowed once their data and
commutators are paid. Any regulator change requires a declared new target
and comparison with the old target where claimed.

Before a pilot, declare componentwise tolerances or nonvanishing reference
scales for R, J, R_t, U, Q and Delta Q, together with the derivatives,
constraints and boundary traces actually needed by the stated theorem.
The principal error is against the regularized theta observables. Use
absolute norms where a comparison quantity vanishes; relative errors must
not divide by a sampled zero. Any time-dependent error scale must be stated
before using observed discrepancies to assess it.

Keep the source approximation, nonlinear transfer, arithmetic evaluation,
filter integration, endpoint and joining errors separate. When numerical
estimates are part of a theorem, enclose them over the whole slab and
buffer, including gaps between samples. Floating observations and held-out
checks are diagnostics, not uniform bounds. Before any numerical run,
record the named analytic estimate or theorem it supports, the question
and decision it can resolve, the fixed regime and numerical budget, and
a stopping condition. Useful roles include testing a proposed estimate,
evaluating explicit constants, checking a derived identity, or certifying
a finite input whose remaining height range has an analytical bound.
Stop when the question is answered, the method fails its declared gate,
or numerical uncertainty is below the dominant analytical allowance.
More heights, cells or precision require a new unresolved analytic need;
they are not independent milestones. See the [numerical policy][numerics]
and [avoid 10][a10].

For the zero measure, the additional comparison is still
\[
\|R_{\rm model}-R_{\rm zeros}\|_X
\le\|R_{\rm model}-R_\epsilon\|_X
+\|R_\epsilon-R_{\rm zeros}\|_X.
\tag{P6}
\]
The second term needs its own multiplicity-aware weak argument. It is not
a prerequisite for a theorem explicitly restricted to the regularized
density, and cannot be omitted when interpreting that theorem as a
zero-count approximation. Smooth regulated field estimates through a
multiple event do not by themselves control regulator removal there.

Record the number of source modes/cells or formula terms and its dependence
on domain and tolerance. A finite representation may be too large to meet
the intended simplicity goal. If a budget is uninformative, preserve the
failed regime and improve the dominant estimate; a finer sample grid does
not repair a loose analytical allowance. Independent comparisons must name
their provenance and shared dependencies.

## 6. Execution sequence and success conditions

The [progress register][progress] owns task statuses; the following defines
the next deliverables and their order. Earlier completed results are inputs,
not tasks to repeat.

| Task | Next deliverable | Acceptance condition |
| --- | --- | --- |
| HDA-19, under HDA-04 — completed comparison input | Retain Notes 30/31 outer and late-time model | Use the stated field, physical-regulator, current/time/covariance and overlap bounds. Constants/onsets remain uninstantiated and review remains same-assistant; no all-time joining is included. |
| HDA-16, under HDA-03--06 — completed endpoint input | Retain both endpoint systems | Use Notes 26/31's exact common-regulator current/time/potential/Q/Delta Q estimates, full buffers, traces and positive model defects. The global positive absolute rate does not replace the sharper inner transport theorem. |
| HDA-17, under HDA-14 — supporting task | Informative finite-transition bounds needed by the global comparison | Identify the analytic theorem using the finite input; prove the required whole-slab errors and height coverage with explicit cost. Finite certification is useful when coupled to analytic tails. Refining the Note 23 pilot requires a stated analytic benefit. |
| HDA-18, under HDA-07--09 — assembly | All-time approximation with complete height coverage | Combine HDA-16/17/19: whole-tail thresholds, time and spatial overlaps, full buffers and all joining/constraint residuals. Give direct comparison or required propagation stability. A bounded-height special case is recorded only at that scope. |
| HDA-20, supporting HDA-09 — review | Review with a distinct reviewer | Audit existing source, transport and covariance estimates and new outer/joining claims as available; record reviewer provenance and shared inputs. Same-assistant checks do not fulfill independent review. |
| HDA-15, under HDA-14 — completed input | Transition contract and sharper source/nonlinear allowances | Note 23 supplies its declared analytical/diagnostic deliverable; its failed trial does not pass HDA-17. No repeat is scheduled merely to produce a better numerical table. |

HDA-16/19 now provide the endpoint and outer inputs; their completion
at those scopes does not depend on passing HDA-17. The next analysis
identifies the finite input and joins needed by HDA-18. Review can
proceed independently. HDA-18 retains the all-time objective and complete
height coverage; a bounded-height construction is only an intermediate
result. Its finite-core and joining obligations are not yet proved.

The common control screen is [the collision register][controls] and the
source-specific discussions in Notes 19--20. Generic field stability must
remain valid for smooth colliding controls with their own constants. Atomic
and polynomial controls lack the smooth canonical-source premises;
Euler-factor, weighted-square, reflected and primitive controls do not
inherit the unchanged theta majorants. A simple-root collar fails at a
covered collision. No earlier simplicity or RH conclusion is an acceptance
criterion, and every failed approximation is excluded only in its proved
class and regime under [avoid 07][a07].

Keep derivations in notes, numerics and small execution records in numerics,
and assessments in reviews. Analytical results lead; numerical observations
support and diagnose. Update this overview's contract when the route or
scope changes and the existing progress register when evidence changes a
status. Preserve its historical checkpoints, original task IDs and chat
registration. No new overview, progress ledger or manuscript snapshot is
created for this continuation of the same objective.

[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[opening]: ../notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[filtered]: ../notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[negative]: ../notes/11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[adaptive]: ../notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[transport]: ../notes/16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[explicit]: ../notes/19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[bridge]: ../notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[manuscript]: ../manuscript/README.md
[integration]: ../notes/21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a19]: ../../../../avoid/19_status_files_that_lag_the_findings.md

[positive]: ../notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md

[local-bounds]: ../notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md

[priority]: ../notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md
[numerics]: ../numerics/README.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md

[outer-tail]: ../notes/25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[negative-system]: ../notes/26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md

[gamma-outer]: ../notes/27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md

[joint-outer]: ../notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md

[full-saddle]: ../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[review12]: ../reviews/12_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_SELF_REVIEW_20261024.md

[positive-system]: ../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md
[review13]: ../reviews/13_POSITIVE_EVOLUTION_AND_COVARIANCE_SELF_REVIEW_20261024.md


**Manuscript synchronization, 24 October 2026:** prepared for Edward
Baker with substantial LLM assistance, gpt-6.1-sol, actual effort ultra.
HDA-10-MI1 r1 integrates Notes 25--28 and 30 only; later research
statuses and HDA-17/HDA-18 joining priorities remain as stated above.

[manuscript-review15]: ../reviews/15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md


**Review 15 production completion, 24 October 2026:** prepared for Edward
Baker with substantial LLM assistance, gpt-6.1-sol, actual effort ultra.
The 65-page revision integrates Note 31 and all recommended exposition
changes, preserving the earlier frozen handoff and current HDA-17/HDA-18
joining priorities. [Assessment](../reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md).
