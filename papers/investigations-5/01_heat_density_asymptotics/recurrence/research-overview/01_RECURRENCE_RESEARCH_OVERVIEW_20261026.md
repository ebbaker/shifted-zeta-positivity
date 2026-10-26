# Research overview: recurrence and fluctuation hierarchies

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Origin: ansatz chat0004, thread 01a1765a-5c4e-7dd1-9de8-d70dd1725e34.

**Current recurrence overview.** The [progress register][progress] owns
execution status; the [analysis continuation][continuation] supplies a
three-round sequence. These documents develop the [opening brainstorm][brainstorm].
They were originally prepared without new analysis. The execution update
below records the subsequently saved results; the progress register owns
live dispositions.

## Objective and useful outcomes

Organize the canonical heat asymptotics into recursively generated
fluctuation levels, and prove what a finite number of levels buys in
field accuracy, derivative accuracy and retained complexity. The index
should reflect increasingly complicated shape corrections. Continuous
smoothing and a continuous generating parameter are complementary
descriptions of the same structure.

The immediate objective is a controlled finite-order hierarchy. The
larger questions concern order selection, cancellation-preserving
reconstruction and the relation between discrete levels and continuous
scales. A shorter formula is an organizational gain; an improved estimate
or a newly covered domain is a separate analytical gain. Neither exact
heat evolution nor a new name for the components proves the latter.

## Starting point and inherited evidence

The canonical normalization is
\[
H_t=-H_{zz},\qquad H(0,z)=\tfrac18\xi((1+iz)/2),\qquad
h(T,z)=H(-T,z),\quad h_T=h_{zz}.
\]
The complete theta source and both exact gamma arms are retained.
Physical regulators, averaging kernels, signed covariance and joining
defects remain those of the parent investigation; this branch's opening
sequence estimates the field, without claiming physical transfer.

| Input | Available evidence | Limit to retain |
| --- | --- | --- |
| Ansatz [Notes05–06][note05] | Proved in-note finite representations at natural gamma and outer-carrier scales, with the separate growing-degree construction and a paid through-zero join. | The outer-scale construction uses its original polynomial-degree cutoff and bounded RS integral. |
| Ansatz [Notes10–12][note12] | First target-centered curvature correction: \(O(|G|X^{-5/4})\) field, spatial-through-three and first-time errors on declared fixed compact negative-time families; actual residual and its spatial derivative \(O(|G|X^{-7/4})\). | Endpoint constants and height onsets depend on the family; source status and same-model internal assessments remain unchanged. |
| Ansatz [Notes15–16][note16] | Exact Gaussian-moment identities, the finite recurrence, and a local continuous deformation. | No new truncation-error or infinite-series convergence theorem. |
| AN06 [manuscript][manuscript] and [Review11][review11] | Integrated 33-page reading version and subsequent source-level internal review. | Production checks and internal reviews do not close the full-chain or specialist-review requirements. |

For fixed \(X\), set \(d=z-X\), \(L=\log(X/(4\pi))\),
\(N=\lfloor\sqrt{X/(4\pi)}\rfloor\). With
\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\qquad
w_\epsilon(z)=\frac{1+\epsilon iz}{2},
\]
put \(h_{\epsilon n}(z)=M(w_\epsilon(z))n^{-w_\epsilon(z)}\),
\(b_{\epsilon n}=h_{\epsilon n}(X)\),
\(\lambda_{\epsilon n}=(\log h_{\epsilon n})'(X)\), and
\(\kappa_{\epsilon,r}=(\log M(w_\epsilon))^{(r)}(X)\), \(r\ge2\).
The latter are independent of \(n\) and have fixed-\(r\) coefficient
size \(O_r(X^{1-r})\).

The working hierarchy is
\[
U_{\epsilon,0}=\sum_{n=1}^N b_{\epsilon n}
e^{\lambda_{\epsilon n}d+T\lambda_{\epsilon n}^2},\qquad
\mathcal Q_T=d+2T\partial_d,
\]
\[
\mathcal D_{\epsilon,r}
=\frac{\kappa_{\epsilon,r+1}}{(r+1)!}\mathcal Q_T^{r+1},
\qquad
jU_{\epsilon,j}=\sum_{r=1}^j r\mathcal D_{\epsilon,r}U_{\epsilon,j-r}.
\]
Every finite level solves forward heat evolution on a frozen chart.
The approximation is
\[
F^{[p,K]}(T,z)=
\sum_{\epsilon=\pm1}\sum_{j=0}^p U_{\epsilon,j}(T,z-X)
+\mathcal I_{X,K}(T,z),
\]
where \(\mathcal I_{X,K}\) is the bounded Gaussian integral of the
real RS coefficients through \(K\), including exact cutoff transfer.
The [continuation][continuation] specifies the comparison norm, buffers
and the terms that must be paid. No arithmetic mode is discarded.

## Questions and order of work

| ID | Question / concrete output | Dependency |
| --- | --- | --- |
| HDA-R01 | Prove the \(p=2,\ K=4\) comparison on \(1\le T\le2\), or identify the precise failing estimate. | Existing recurrence and classical real RS input. Completed; Note02/Review01 in the execution update. |
| HDA-R02 | Derive a theorem for every fixed finite \(p\), a matching RS choice \(K(p)\), and the actual order-dependent constants/onsets on the same slab. | R01 accepted; completed in Note03/Review02. |
| HDA-R03 | Extend the proved fixed-order statement to declared \(0<\tau\le T\le B<\infty\), retaining explicit endpoint dependence. | R02 accepted; full fixed-p family completed in Note04/Review03. |
| HDA-R04 | Quantify the continuous fluctuation deformation and its truncation remainder; compare its usefulness with the discrete recurrence. | A paid finite-order norm and remainder mechanism; not in the opening three rounds. |
| HDA-R05 | Determine whether growing order, a different grouping, or resummation gives useful outer-carrier accuracy or cost. | Bounded R05-AN01 r1 completed in Note05/Review04; broad evaluator-cost question remains Partial. |
| HDA-R06 | Explore a more structural transform or a controlled moment closure only when it produces a specific reconstruction estimate. | A concrete operator/data/reconstruction proposal and a test against existing estimates. Exploratory. |

R01 inherits the bounded mathematical question from the prepared
[ansatz AN07 request][oldpacket]. The active successor and output home
are now [R01-AN01][packet1] and this branch. R02 and R03 have prepared,
dependency-gated requests. This prevents duplicate execution while
supporting the author's practice of continuing for several rounds.

The first target is \(O(|G|X^{-11/4})\) for R01, suggested by formal
counting. R02 may test \(K=2p\) and an exponent \(p+3/4\). These are
initial candidate outcomes, not opening inputs or promises. The execution
update below records their later proofs at fixed-order scope.
If the proof supports another rate, state it with its actual logarithmic
and parameter losses. A focused failed estimate is a legitimate return,
but it does not complete the desired quantitative theorem.

## How the continuous and physical ideas enter

The exact Fourier and Laplace forms are
\[
h(T,z)=\int_{\mathbb R}e^{-Tu^2+izu}\rho(u)\,du
=\int_0^\infty e^{-TE}
\frac{\Phi(\sqrt E)\cos(z\sqrt E)}{2\sqrt E}\,dE .
\]
Thus \(T\) is smoothing time and \(E=u^2\) is spectral energy.
Separately, the local deformation
\[
A_{\epsilon,s}(q)=
\exp\!\left(\frac{\log A_\epsilon(sq)}s\right),\qquad A_{\epsilon,0}=1,
\]
generates the fluctuation order \(j\). Its bounded-window meaning is
established algebraically; replacing it by an infinite whole-line
operator series still needs convergence and tail estimates.

The literal moments satisfy
\(\partial_T\mu_j=-\mu_{j+2}\) and
\(\partial_z\mu_j=i\mu_{j+1}\). Their closure problem is different from
truncating the \(U_j\) hierarchy. The indices for arithmetic carriers,
fluctuations, RS completion and spectral energy must stay distinct.

Twistor/ADHM and inverse scattering motivate structured reconstruction;
KdV and sine-Gordon illustrate evolution simplified in transform data.
Quantum chemistry motivates independent basis/correlation resolutions,
and BBGKY motivates explicit closure errors. These remain useful
comparisons, not imported theorems or constructed correspondences.
The [reference guide][refs] records exactly which sources were inspected.
The particular Atiyah passage recalled in the discussion remains unidentified.

## Acceptance, controls, and downstream boundaries

Each round must compare to the same canonical \(H\), on the full fixed
complex chart, with spatial derivatives through three, first time error,
the actual model residual, and an explicit initial/local/tail error budget.
Do not differentiate a scalar error allowance or infer holomorphic
derivatives of real RS coefficient functions. Keep the real coefficient
data inside their fixed-window integral.

The currently displayed outer-relative allowance
\[
X^{-5/4}\exp(TL^2/16-\pi^2T/64)
\]
grows at fixed \(T>0\). No fixed algebraic exponent by itself compensates
for this conversion. That says what the allowance fails to prove; it is
not an actual-error lower bound or an exclusion of cancellation-preserving
methods. A fixed-\(p\) result also does not license \(p=p(X)\).

This is an approximation program under [avoid01][a01], not an RH criterion.
Read the [result index][results], [heat-flow cluster][heat],
[controls12][controls] and [avoid index][avoid], especially
[shared premises][a02], [scoped conclusions][a07] and
[separate bounds][a12]. The heat/recurrence structure is shared by
suitable noncanonical sources. Euler-factor/finite-prime controls fail
the unchanged full canonical coefficients; weighted-square/cutoff
controls fail the full canonical completion; reflected, smooth and
positive-primitive controls lack the complete canonical gamma/arithmetic
identity. No collision is excluded by the organizing identities alone.

HDA-A02 remains Partial; HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
remain. Positive-time comparison A08, through-zero/growing-time assembly,
physical transfer, numerical certification, coefficient-evaluation cost and
manuscript integration are outside this opening sequence. At its close,
report what the broader ansatz program can actually consume and recommend
the next bounded task. **Next owner: Analysis — Sol**, beginning R01.

[progress]: ../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md
[continuation]: ../notes/01_ANALYSIS_CONTINUATION_20261026.md
[brainstorm]: ../brainstorm/01_RECURRENCE_AND_GENERALIZED_TRANSFORM_HIERARCHIES_20261026.md
[note05]: ../../ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[note12]: ../../ansatz/notes/12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md
[note16]: ../../ansatz/notes/16_GAUSSIAN_FLUCTUATION_HIERARCHY_20261026.md
[manuscript]: ../../ansatz/manuscript/main.tex
[review11]: ../../ansatz/reviews/11_CURRENT_ANSATZ_AND_NEXT_STEPS_REVIEW_20261026.md
[oldpacket]: ../../ansatz/research-progress/handoffs/HDA-A02-AN07.md
[packet1]: ../research-progress/handoffs/HDA-R01-AN01.md
[refs]: ../references/README.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

## Execution update — 26 October 2026

Prepared for Edward Baker with substantial LLM assistance, actual
**gpt-6.1-sol, ultra**, recurrence chat0001. [Note02](../notes/02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md),
[Note03](../notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md) and
[Note04](../notes/04_COMPACT_TIME_RECURRENCE_FAMILY_20261026.md), with
[Review01](../reviews/01_FIRST_FINITE_FLUCTUATION_ASSESSMENT_20261026.md),
[Review02](../reviews/02_FIXED_ORDER_HIERARCHY_ASSESSMENT_20261026.md) and
[Review03](../reviews/03_COMPACT_TIME_RECURRENCE_ASSESSMENT_20261026.md),
are proved in-note from named inputs, same-model internal assessments only.
R01: p=2,K=4, X^-11/4 on [1,2]. R02: every fixed p>=1,K=2p,
X^-(p+3/4) on [1,2]. R03: the same fixed-order rate on declared fixed
0<tau<=T<=B, with explicit endpoint factors and sufficient onsets. All
are in the full buffered (3,1) norm, no logarithmic loss. The bounded
real RS integral and every mode remain; frozen residual=residual_z=0.

The first unpaid outer-scale step is a simultaneous estimate for order
growth, constants and onsets before converting the natural scale. The
closing R03 recommendation chooses that bounded Analysis — Sol audit;
it is not started. Continuous-s, growing-time, useful evaluation cost,
physical transfer and manuscript integration are still outside the proved
sequence. HDA-A02 and all parent statuses remain unchanged.

## Controlled-order execution update — 26 October 2026

For Edward Baker with substantial LLM assistance, actual gpt-6.1-sol,
ultra. [Note05](../notes/05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md) and
[Review04](../reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md)
separately establish growing-order scope on [1,2]: simultaneous finite
costs for 1<=p<=cL, fixed c, K=2p; chosen p=floor(L/2) pays e^-L²/4
outer-envelope field/spatial-through-three/direct-time accuracy. The
full rate range, failed old absorption, stronger fixed-theta tail costs
and common onsets are in Note05. All modes and bounded RS integral remain.
This closes the formerly recommended order-growth audit, not the broad
R05 evaluator-cost program. Same-model internal review only.

Next unpaid step: coefficient/carrier input sensitivity, rounding and
bounded-integral quadrature error at that chosen outer accuracy. The
formal O(p³+Np) scalar arithmetic count does not pay those costs. No
new time-endpoint, infinite-series, physical-transfer or manuscript result;
parent statuses unchanged. Next Analysis — Sol deliverable is bounded in
the R05 packet and remains unexecuted pending a new request.

## Evaluation-error audit update — 26 October 2026

For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**, recurrence chat0001. [Note06](../notes/06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md)
and [Review05](../reviews/05_EVALUATION_ERROR_ASSESSMENT_20261026.md)
close R05-AN02 r1 at its bounded analytical scope. The total e^-L²/4
outer target at p=floor(L/2),K=2p now has explicit coefficient/carrier,
scale, rounding, RS-data, quadrature and geometry budgets. Named exact
coefficient identities and derived complex bounds pay RS regularity and
O(L²)-node-per-branch quadrature. All modes, integral and buffers remain.

The sufficient requested normalized input/circuit accuracy is
3L²/(8log2)+O(Llog L) bits under the declared provider contracts.
Concrete providers, their internal precision/runtime and frozen descriptor
handling are unverified; broad R05 stays Partial, with no parent-status
change. This is a conditional evaluator specification, same-model
internal assessment only. **Next recommended owner: Analysis — Sol**,
a new analytical provider-algorithm audit, not executed. No manuscript
or numerical campaign. The live register owns the disposition.
