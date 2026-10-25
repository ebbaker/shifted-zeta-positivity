# Research program: asymptotics and evolution of averaged zero density

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**,
verified from the original turn's metadata.

**Current consolidation and program revision, 25 October 2026, chat 0016:**
prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
actual effort max**. The maintained manuscript now consolidates Notes
42–45: the fixed-gap full-support comparison, constructive positive source,
and explicit complete outer-field/jet bounds. [Note 46][integration46] maps
the production work; [Review 28][production28] records its checks.
[Review 27][review27] supplies the preceding focused assessment.
AN01–AN03 are closed at their bounded analytical scopes. The next task is
[HDA-18-AN04 r1][an04], followed by the fixed-width and conditioning work
specified below. HDA-17 remains Partial, HDA-18 Gated, HDA-20 unfulfilled.

**Author's governing goal, reaffirmed 25 October:** results must extend to
infinite height and across all real time in an analytic form. The domain
is every real x and t, on each declared bounded transverse strip with
full averaging/analytic buffers; the limits |x|→infinity and t→±infinity
must be quantitatively controlled. A finite interval, finite set of
samples or growing window is an intermediate input with a named global
consumer, not a substitute completion target.

**Earlier program amendment, chat 0012:** 24 October 2026; gpt-6-astra, actual effort
xhigh. Incorporates Notes 34–38 and the author's crossover, order-parameter
and correlation goals; [Note 39][manuscript39] gives the requested analytical
manuscript recommendations. This amendment is planning and synthesis,
not a new theorem or manuscript build.

**GPT model ownership, revised by the author on 24 October:** GPT-6.1 Sol
is the default for routine and moderately difficult analysis and all
numerical work. Reserve GPT-6 Astra for extra high difficulty analytical
tasks, and hand tractable subproblems to Sol promptly.
The author manages the chats manually. Follow the
[shared handoff workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md);
the existing progress register records the next owner and packet.

**Purpose.** Find a relatively simple explicit formula for the unnormalized
smoothed density, defined for every real heat time \(t\), and progressively
refine it into an approximation to the canonical theta solution with
proved control extending to arbitrarily large height. Analytical estimates
on unbounded height domains have priority; numerics support named steps
in those estimates.

**Long-term goal, clarified on 24 October and reaffirmed on 25 October 2026.** The
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

The final analytic representation may combine finite Gaussian primitives,
a specified implicit gamma-saddle branch and explicit smooth joining
functions. It must give a finite evaluation prescription at each point
and explicit errors for the actual observables, without inserting the
unknown H, Q or fitted data as an unspecified closure. Smooth cutoffs
are allowed; the objective does not impose global holomorphy or real
analyticity on a cutoff-based approximation. Simplicity and cost remain
criteria alongside proved accuracy. A time-dependent error scale is
allowed, but it must remain informative throughout the declared domain.

Each improvement should sharpen the explicit approximation, reduce its
proved error or extend the domain on which the bound is useful. The
current endpoint formulas and bounded-window estimates are intermediate
steps toward this all-time objective. A reduced formula with omitted
fluctuations must retain their quantified equation residual and a stability
estimate connecting that residual to solution error. This global
construction and error theorem remain open.

## Revision decision and the current starting point

**Current priority:** complete analytic coverage of unbounded height and
all real time. Notes 26/30/31 supply the endpoint/outer comparisons;
Note 34 pays compact transfer and a local holomorphic time join.
Notes 42/43 now pay a nonholomorphic spatial join on a fixed-gap short
slab, with the complete support, curvature, current, source and actual
covariance ledger. Note 44 supplies a constructive clipped-cubic source
for any finite jet demand. Note 45 pays the full complex-buffer H-P jets
on [95,97] above an explicit enormous height. The next finite consumer
is AN04's complete observable budget. HDA-22 then targets fixed-width
time coverage; HDA-23 improves growing-core conditioning; HDA-24 handles
the switch before parent HDA-18 joins the two time endpoints. No numerical
pilot or onset optimization is a completion target in isolation.

The author's phase-transition suggestion adds a focused analytical question:
explain the known regulator crossover and determine whether a precisely
defined connected correlation or response has additional scaling.
[Note 38][crossover] separates this question from global assembly. The
regulator's chosen switch at 64 is not an established intrinsic critical
time. HDA-21 first specifies the limiting regime, diagnostic order parameter,
connected statistic and response; a criticality theorem is not assumed.

The maintained manuscript integrates Notes 42–45 in addition to the
previous Notes 34–37 and scoped Note 38 outlook. [Note 46][integration46]
and [Review 28][production28] record this author-directed consolidation.
The completed 78-page MI2 version remains a historical milestone in
[Note 41](../notes/41_NOTE39_MANUSCRIPT_IMPLEMENTATION_20261024.md) and
[Review 22](../reviews/22_NOTE39_ANALYTICAL_INTEGRATION_PRODUCTION_ASSESSMENT_20261024.md).
The older [Note 32][priority] remains the broader assembly specification;
this overview and the sole register supply current dependencies.

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
| Interpret the regulator crossover | Separate the exact-center shift and rounding width; define an order-parameter diagnostic, connected correlation and response before testing additional scaling. Do not infer intrinsic criticality from the regulator-induced limiting jump. |

**HDA-15 checkpoint:** [Note 23][local-bounds] supplies a transition
contract and sharper source, nonlinear and actual-covariance bounds. Its
192-cell diagnostic fails the contract. Those findings remain useful,
but a larger mesh is not the default continuation.

The present analytical inputs are:

- [Notes 42][spatial42] and [43][support43] supply exact spatial defects
  and the complete full-support transfer on a fixed gap and short slab.
  With the stated source/gap inputs the largest allowance is
  O_J(X^-2 log^3 X + X^-3 log^2 X), plus retained polynomial-exponential
  terms. Every real observation height is covered; the time width shrinks
  with X and no fixed-width or all-time assembly follows.
- [Note 44][finite44] gives finite model/cutoff/core coefficients and a
  clipped rational-cubic source with four-jet error 29epsilon/64 before
  evaluation/filtering. Its sufficient cost is an upper bound; the coarse
  core floor can force exponentially many cells. [Note 45][effective45]
  now pays the formerly open field gate: 12000 A/x^2 on the full strip,
  explicit jets through three and onset X>=2^2050 for the gap consumer.
  Exterior collar/unit, signed-pole and weighted-observable constants are
  still AN04 inputs; no selected source or complete budget is accepted.

- [Note 34][compact-join] supplies an explicit compact transfer from field
  errors of orders zero and two and the heat residual to the full filtered
  system. It pays a local time join and identifies the uncorrected spatial
  cutoff's nonholomorphic defect. Symbolic covering thresholds and an
  attainable compact error tolerance do not give an informative global
  construction.
- [Notes 35][weak-decision], [36][source-refinement] and [37][hermite]
  retain both weak and local transfer, sharpen complete source curvature
  and signed-source comparison, and give a positive cubic-Hermite source
  with explicit complete fourth-order, arithmetic-category and ideal
  evaluator remainders. The sampled gains remain diagnostic; refer to
  these notes for numerical evidence, including failures.
- [Note 38][crossover] places Note 28's existing switch profile alongside
  finite-size scaling, order parameters and connected correlations. Its
  alternative-switch scaling calculation is conditional; it proves no
  intrinsic phase transition, CFT structure or new differentiated layer.
  [Review 21][review21] is a limited cross-model assessment, not the
  complete HDA-20 audit.

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
  only. Notes 25--28 and 30--31 were integrated in the 65-page revision;
  MI2 adds Notes 34–37 and the scoped Note 38 interpretation;
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
- The [maintained manuscript][manuscript] consolidates results through
  Notes 42–45, with the scoped Note 38 outlook and brief diagnostic support.
  The [current build record](../manuscript/BUILD_RECORD_20261025.json),
  [integration map][integration46] and [production assessment][production28]
  record the revision. MI1, Review 15 and MI2 retain their original
  historical scopes. Production is not an independent mathematical audit.

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
potential and model residuals. Use Note 34's compact transfer and local
time join as existing inputs; use Notes 42–45 for the fixed-gap full-support construction and its
source/field inputs. Complete its finite observable budget and extend
its time domain for HDA-17/HDA-18/HDA-22–24. Identify the
source/jet accuracy consumed by the joins before selecting a finite
numerical calculation. Note 19's
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

The current compact transfer has the explicit form
\[
\mathcal E_{V,\alpha}=A_{V,\alpha}d_0+B_{V,\alpha}d_2+
C_{V,\alpha}\eta_E,\qquad \eta_E\ge|F_t+F_{zz}|,
\tag{P8}
\]
with frozen positive coefficients from Note 34 CJ5–CJ14 on a full compact
buffer, with \(d_j\ge|\partial_z^j(H-F)|\) for \(j=0,2\).
Notes 36–37 improve the local signed-source and source interpolation
inputs; use whichever proved route gives a useful allowance on the same
domain. For a time blend \(F=(1-\theta)F_1+\theta F_2\),
\[
E_F=(1-\theta)E_1+\theta E_2+\theta'(F_2-F_1).
\tag{P9}
\]
The overlap must pay the field mismatch, component residuals and actual
joined observables. For a spatial blend, the additional defect is
\[
\partial_{\bar z}F=(\partial_{\bar z}\lambda)(P_*-H_f).
\tag{P10}
\]
Notes 42–43 now pay this term, its mixed/time derivatives and all
filtered equations on a fixed-gap short slab. Their proof uses weighted
primitive integrals over complete supports before weak differentiation;
the separate exterior heat partition retains every cutoff derivative.
For a moving gap the extra residual lambda_t(P-H_f) and its consumers
must be proved afresh. The fixed-band construction is not yet a fixed-width
time cover.
Neither enlarging a symbolic overlap nor refining a source mesh removes
an unpaid endpoint field error or the shrinking spatial regulator floor.

**Alternative route: a reduced potential-density evolution.** If a useful
closure is obtained, formulate a compatible boundary/anchor problem and
prove the needed existence, uniqueness and stability estimates. Do not
assume (P3a) is an ordinary forward parabolic equation or prescribe
incompatible data at both time ends. Direct source-error estimates can
establish approximation without such PDE propagation; a residual-based
claim of solution accuracy still requires its own stability argument.

## 4a. Resolve the crossover and test correlation scaling

This is a supporting analytical direction, not a replacement for the
all-time approximation contract. The baseline regulator and filter remain
unchanged. Note 28 gives the exact-center relation
\(b(t_c,X)=0\), where \(b=\log(\epsilon_g/A_X)\), and
\[
t_c-64\sim64/\log X,\qquad
t=t_c-\frac{128\tau}{\pi X\log X},
\]
\[
\frac{R(t,X,y)}{\log X}
=\frac{k_h(y-\tau_+)+k_h(y+\tau_+)}{8\pi}
+O((\log X)^{-1}).
\tag{P11}
\]
This is uniform for bounded \(\tau\) and \(|y|\le Y\) under Note 28's buffer conditions.
The center's shift is much larger than the rounding width. Retain the
implicit center on that width; the absolute error here is O(1).
A normalized profile is a diagnostic, while the physical target remains
unnormalized. No differentiated estimate follows from differentiating
this static remainder.

The first HDA-21 deliverable is a precise specification, using Notes
27–28/31/38, of the following objects and estimates:

- A limiting regime and the diagnostic order parameter
  \(m_X=4\pi R(t,X,0)/(k_h(0)\log X)\), with its regulator dependence.
- One observable \(O\), an explicit normalized averaging window \(W_X\)
  and width, and a connected statistic
  \[
  \mathcal C_X(s;t)=\langle O(t,X+u)O(t,X+u+s)\rangle_{W_X}
  -\langle O(t,X+u)\rangle_{W_X}
   \langle O(t,X+u+s)\rangle_{W_X}.
  \]
  State centering, separation scales and known carrier/amplitude growth.
  A finite-window average is not an assumed stationary Gibbs ensemble.
- A declared perturbation and derivative defining response. An integral
  of \(\mathcal C_X\) is not automatically susceptibility. A correlation
  length also needs a definition appropriate to the derived decay.
- The field, current, direct-time and actual-covariance error estimates
  needed to compare the scaled system with theta. Existing outer
  comparison may supply inputs; it does not automatically resolve every
  finer scaled observable or derivative.

The existing Q is a signed difference of local gradient variances, not
the separated-point statistic above. Check individual correlations and
regulator/filter dependence before interpreting their growth as critical.
Any alternative regulator is a separately declared comparison target;
Note 38's conditional switch calculation does not alter the physical q.

Use the [primary-literature scope record][phase-references]: finite-size
shift/rounding is an immediate analogy; Landau theory requires a derived
order parameter/effective structure, RG requires a scale transformation,
and CFT/anomalous dimensions require justified correlation scaling and
symmetry hypotheses. Holomorphy or logarithmic growth alone supplies none
of these. A finite-separation two-point function need not diverge even
when correlation length or integrated response grows. Stop the first
specification at a precise missing estimate rather than add a numerical
sweep. A resistant uniform differentiated-layer proof can then be routed
as a named hard analytical problem.

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

The [progress register][progress] owns live statuses. Existing input
results are not tasks to repeat. Sol is the default analytical owner;
Astra is reserved for a documented resistant structural estimate.

| Task | Deliverable and current scope | Acceptance / global consumer |
| --- | --- | --- |
| HDA-16/19 — completed inputs | Retain both all-height endpoint systems and the compact-time outer comparison | Use the complete physical-regulator, current/time, potential, actual Q/Delta Q, trace and model-residual budgets. General endpoint onsets remain to be instantiated as needed for joining. |
| HDA-18-AN04 — next, Sol | Effective remaining exterior constants and one complete fixed-gap budget on the Note 45 regime | Pay every FT7/FT9/FT15 constant, gap selection and full tuple row; state finite source tolerances/cost or the first failed row. No source/gamma/theta sampling is commissioned. This pays the finite inputs used by HDA-18 and calibrates HDA-22/23. |
| HDA-22, under HDA-18 — ready analytical extension | Fixed positive time-width spatial assembly, initially [95,97]; [AN05 r1][an05] | Width independent of X; all real heights, full supports, all moving-gap or overlap derivatives, direct time/source rows and actual covariance. Give a decreasing error with controlled number of charts/cutoff costs, or identify the exact loss. Uniform symbolic constants may be used if their finite consumer is named. |
| HDA-23, under HDA-17/18 — ready analytical improvement | Improve growing-core conditioning; [HDA-17-AN04 r1][core04] | Replace the coarse single expanding-rectangle regulator floor by a proved local field/collar or equivalent comparison; quantify the source-tolerance/cost gain for the same tuple and through possible core multiple events. No assumed zero separation, changed q or unaudited normalized observable. |
| HDA-24, under HDA-18 — gated by fixed-width assembly | Switch-uniform spatial/time construction across 64; [AN06 r1][an06] | Use the compact [32,T] outer estimates and exact switch center; retain polynomial regulator derivatives where exponential smallness is nonuniform. Cover the moving layer in absolute physical units, including differentiated/covariance rows. Return a proved cover or exact singular missing estimate. |
| HDA-17 — finite bridge | Consume the improved source/transfer contract on the finite central time region | One source representation per declared chart, complete continuous source/evaluation/filtering bounds and explicit cost. The older frozen-point certificate is optional support with a named global consumer; passing it alone does not accept HDA-17. |
| HDA-18 — final assembly | A computable analytic approximation on all real time and height | Combine the central strip, switch construction and both endpoint regions with nonempty paid time overlaps. List domains whose union is R_t x R_x on the declared y strip; give formula selection/joins, finite prescription and full error envelope. Retain actual covariance, both curvature derivatives, source anchor, traces and endpoint limits. Direct comparison is sufficient; propagation requires its own stability proof if used. |
| HDA-10 — consolidation | Notes 42–45 integrated, [Note 46][integration46] | Source-to-manuscript map, reproducible checked PDF and synchronized scope; production changes no research status. |
| HDA-20 — ready, unfulfilled | Distinct-reviewer audit | Audit source, collar/unit, signed cancellation, covariance and joins with provenance and shared inputs recorded; production checks and limited LLM assessments do not complete it. |
| HDA-21 — supporting, ready | Crossover/correlation specification | Define observable/window, limiting and separation scales, perturbation/response and needed differentiated error; no assumed intrinsic criticality or numerical sweep. |

The immediate sequence is AN04, then fixed-width assembly and improved
core conditioning, then switch-uniform assembly and the two endpoint
overlaps. HDA-22/23 analytical work can use the current symbolic estimates
without waiting for a numerical implementation, but its final effective
constants must be reconciled with AN04. HDA-24 is not started by preparing
its packet. The 95–97 slab is a controlled test of a reusable joining
mechanism; a proof confined there must state what extends to a general
compact interval and what fails near 64 or either time endpoint. Once a
finite gate is decided, move to the next domain/conditioning obstacle
rather than repeatedly improve the same finite onset.

Completion is assessed by the global domain and the useful error, not by
note count, finite mesh size or formal existence with prohibitive cost.
No single height cutoff, shrinking time cover or normalized profile may
stand in for the stated all-time physical-density theorem.

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

[compact-join]: ../notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md
[weak-decision]: ../notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md
[source-refinement]: ../notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md
[hermite]: ../notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md
[crossover]: ../notes/38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md
[manuscript39]: ../notes/39_MANUSCRIPT_ANALYTICAL_RECOMMENDATIONS_20261024.md
[review21]: ../reviews/21_NOTES35_37_PROJECT_AND_JOIN_ASSESSMENT_20261024.md
[phase-references]: ../references/PHASE_TRANSITION_METHODS_20261024.md
[mi2]: ../research-progress/handoffs/HDA-10-MI2.md

[integration46]: ../notes/46_NOTES42_45_MANUSCRIPT_CONSOLIDATION_20261025.md
[production28]: ../reviews/28_NOTES42_45_CONSOLIDATION_PRODUCTION_ASSESSMENT_20261025.md
[review27]: ../reviews/27_RECENT_PROGRESS_AND_NEXT_STEPS_REVIEW_20261025.md
[spatial42]: ../notes/42_GAP_LOCALIZED_SPATIAL_DEFECTS_20261024.md
[support43]: ../notes/43_FULL_SUPPORT_FIXED_GAP_TRANSFER_20261024.md
[finite44]: ../notes/44_FINITE_INPUTS_CLIPPED_SOURCE_AND_OUTER_GATE_20261024.md
[effective45]: ../notes/45_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_20261025.md
[an04]: ../research-progress/handoffs/HDA-18-AN04.md
[an05]: ../research-progress/handoffs/HDA-18-AN05.md
[core04]: ../research-progress/handoffs/HDA-17-AN04.md
[an06]: ../research-progress/handoffs/HDA-18-AN06.md
