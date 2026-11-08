# Localized correlations and full zero configurations

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Root authoring model/effort unavailable; hierarchy discovery was tool-selected **gpt-6.1-sol/ultra**, shared Green check **gpt-6-astra/ultra**. Dispatch settings are not independent backend verification.


**Evidence: setup and proposed mechanisms.** Existing internal derivations retain their original assessment scopes. The [shared synthesis](../../brainstorm/notes/19_TND_O_GREEN_CORRELATION_BIFURCATION_SYNTHESIS_20261107.md) contains the theta–primitive–H dictionary and exact Green comparison. This document specifies what a correlation construction would add.

## 1. Fixed zero object and localization

**Author clarification, 8 November 2026:** the objective remains a localized
correlation/marginal framework for possibly nonreal zeros, generalizing the
real-zero spacing perspective of Montgomery and Rodgers–Tao. The particular
quadratic reduction and later log-comparison route do not exhaust it.
[Alignment Note05](../brainstorm/notes/05_TND_OC_AUTHOR_GOAL_ALIGNMENT_20261108.md)
records this distinction; no new theorem or execution is asserted.
Prepared for Edward Baker with OpenAI Codex assistance; actual current
model/effort unavailable.

Use the canonical Newman family \(H_\lambda\) and its full zero multiset \(z_j=x_j+iy_j\), with multiplicity copies indexed separately. For \(0\le\lambda\le1/2\), inherited zeros lie in \(|y_j|\le1\). At time zero \(z=2\gamma+i(1-2\beta)\). Newman time satisfies \(\partial_\lambda H=-H_{zz}\); forward heat time reverses its sign. The variable \(x\) here is twice zeta height.

For a nonnegative compactly supported smooth window \(w\), let
\[
w_{X,h}(x)=w((x-X)/h),\qquad h>0.
\]
This localizes a statistic near a freely chosen height X. Gaussian windows or other justified decays remain available but require complete zero tails. Compact support makes the initial finite products literal; it does not by itself establish a bound uniform in \(X\to\infty\). Width h, local spacing, transverse displacement d and Newman time must be assigned a joint regime.

The underlying deterministic measure is
\[
\nu_\lambda=\sum_j\delta_{z_j}
=\frac1{2\pi}\Delta\log|H_\lambda|.
\tag{C1}
\]
The sum uses multiplicity copies. Equivalently \(\partial_{\bar z}(H_\lambda'/H_\lambda)=\pi\nu_\lambda\). These distributional identities are the interface to the [Green branch](../../01_green_potential_resolvent/README.md), not an assumed probability law.

## 2. What Vandermonde marginalization does

For a genuine unitary ensemble with finite normalizing integral,
\[
p_N(\mathbf x)=Z_N^{-1}|\Delta(\mathbf x)|^2\prod_{j=1}^N w_0(x_j),
\quad \Delta(\mathbf x)=\prod_{j<k}(x_k-x_j),
\]
and
\[
R_2(x,y)=N(N-1)\int p_N(x,y,x_3,\dots,x_N)\,dx_3\cdots dx_N.
\tag{C2}
\]
It is the complete density, including the squared determinant and weight, that is marginalized. The density's positivity, normalization and ensemble law are premises. [Borodin §2 and §4](../../references/17_TND_O_GREEN_CORRELATION_SETUP_SOURCE_USE_20261107.md) supplies the general point-process/correlation framework; its determinantal formulas require the relevant process and operator hypotheses.

Montgomery's original paper studies height-averaged deterministic zeta-zero sums under RH and restricted Fourier support. The sine-kernel pair expression is the conjectural full limiting connection, not an established finite-height joint distribution of actual zeros. See [Montgomery source receipt](../../references/17_TND_O_GREEN_CORRELATION_SETUP_SOURCE_USE_20261107.md) and manuscript [§13 complex statistics](../../manuscript/sections/11_complex_statistics.tex). Pair statistics can depend on X; a separation-only law is a feature of a stationary unfolded limit.

The author's spatial weighting has the natural formulation
\[
\mathcal Z_{X,h}(\eta)=
\frac1{Z_N}\int|\Delta(\mathbf x)|^2
\prod_{j=1}^N w_0(x_j)[1+\eta w_{X,h}(x_j)]\,d\mathbf x
=\mathbb E\prod_j(1+\eta w_j).
\tag{C3}
\]
The multiplier is one outside the window, so the insertion does not force all particles into it. Expanding,
\[
\mathcal Z_{X,h}(\eta)
=\sum_{k=0}^N\frac{\eta^k}{k!}
\int \prod_{\ell=1}^k w_{X,h}(x_\ell)
R_k(x_1,\dots,x_k)\,d\mathbf x.
\]
Arbitrary test functions give the full factorial hierarchy. For a justified determinantal point process, the corresponding expectation is a Fredholm determinant; require trace-class/integrability assumptions as in Borodin (2.4). None of this establishes a determinantal law for \(\nu_\lambda\).

## 3. Candidate A: marked pairs

Define the ordered factorial measure
\[
\alpha_\lambda^{(2)}
=\sum_{j\ne k}\delta_{(z_j,z_k)}
=\nu_\lambda\otimes\nu_\lambda-\operatorname{diag}_*\nu_\lambda.
\tag{C4}
\]
At a location of multiplicity m the diagonal coefficient is \(m(m-1)\), not zero. Subtracting the whole geometric diagonal would incorrectly remove distinct multiplicity copies.

A localized statistic is
\[
S_{\lambda,X,h}[\Psi]=\int w_{X,h}(x)w_{X,h}(x')
\Psi(x-x',y,y')\,d\alpha_\lambda^{(2)}.
\tag{C5}
\]
For example \(\Psi=\chi(x-x')(y-y')^2\) with nonnegative \(\chi\), \(\chi(0)=1\), vanishes for every all-real configuration. A simple conjugate pair \(x\pm id\) contributes \(8d^2w_{X,h}(x)^2\) from its two ordered pairs, with additional nonnegative terms. This elementary diagnostic is not an acquired source-side upper bound. It avoids a statistic whose zero condition would also demand simplicity of real zeros.

Height-only Vandermonde factors cannot distinguish identical ordinates of a nonreal conjugate pair from a multiple real zero. The full complex Vandermonde resolves their nonzero separation, but no canonical nonnegative ensemble with that law has been derived. A collision-sensitive statistic must retain y marks or an equivalent realness-sensitive structure.

Using (C1), a compact smooth pair test can be expressed distributionally through the tensor product of zero measures, with the self-pair correction explicit. Integration by parts transfers derivatives to the test in each variable. This supplies source access in principle; products of log fields and their conditioning may cost more than the one-point Green integral. Establishing a favorable estimate is exactly the open task. Source positivity is not an answer.

## 3.1. Current direction: localized two-zero marginals

**8 November 2026, author-requested direction and literature update.**
Prepared for Edward Baker with OpenAI Codex assistance; actual current
model/effort unavailable. Develop (C4)–(C5) as a full marked pair measure,
then select a useful marginal or test. For a finite local configuration,
symmetrize its N labeled zero atoms into P_N. Its first-two-coordinate
push-forward satisfies N(N-1)(pi_12)_*P_N=sum_(j!=k)delta_(z_j,z_k).
This construction is valid without a random-matrix hypothesis; see
[Note06](../brainstorm/notes/06_TND_OC_PAIR_MARGINAL_AND_RODGERS_TAO_SPACING_20261108.md).

Retain common height, separation and both transverse coordinates before
projection. Real-axis mass, conjugation relations and repeated geometric
locations require measures rather than an assumed smooth planar density.
An optional center-averaging law must be specified, with its dilution
cost. Recover the all-real pair statistic as a benchmark without imposing
simplicity; a pair correlation is different from a consecutive-gap law.

[The literature review, Note07](../brainstorm/notes/07_TND_OC_LOCALIZED_PAIR_MARGINAL_LITERATURE_AND_DIRECTION_20261108.md)
selects two canonical access candidates for B04: localized arithmetic
complex-difference tests, and direct weak pair statistics from correlated
log fields. The closest tools are BGST's unconditional arithmetic
framework, Tao–Vu's local replacement principle and the existing
whole-cluster Poisson transfer. Gaussian/Pfaffian correlations and
heat-evolved random polynomials supply comparison examples, not a law
for H. [Source-use04](../references/04_TND_OC_PAIR_MARGINAL_LITERATURE_SOURCE_USE_20261108.md)
records versions, hypotheses and exact inspected passages.

**Source correction:** BGST arXiv:2501.14545v3 §3 corrects the earlier
uniform error. Reconcile the parent manuscript's imported (eq:BGST)
before using it in candidate A; no automatic status upgrade or global
retraction is implied.

The next milestone is one specified test with independently controlled
canonical data and a complete error/regime, or a scoped failure. Defining
a marginal is a representation. A future dynamical estimate must pay
outside-window interactions, time and localization boundaries, and any
unclosed higher-correlation terms. Do not replace the pair object by
B01's quadratic projection or B03's scalar logs without a new recorded
choice. E02 is accepted, B02 author-checked only, and E03 remains pending.
The sole register owns B04 readiness and the independent audit queue.

## 4. Candidate B: full configuration functional

For compactly supported f,
\[
\mathcal Z_\lambda[f]=\prod_j(1+f(z_j))
=\sum_{k\ge0}\frac1{k!}\int\prod_{\ell=1}^k f(z_\ell)
\,d\alpha_\lambda^{(k)} .
\tag{C6}
\]
There are finitely many nonzero terms for compact support. No expectation or random process is implicit. If center averaging or another ensemble is introduced, specify its measure before using probabilistic terms. For positive factors, or nonvanishing factors with a specified logarithm convention, a deterministic fixed configuration satisfies \(\log\mathcal Z=\sum_j\log(1+f(z_j))\). Compact support alone does not guarantee this: a factor may vanish. Its logarithm already encodes diagonal factorial cumulants; an averaging law introduces additional statistical correlations. This algebra alone is not an independently controlled response estimate.

A Green specialization on upper-half-plane zeros is
\[
f_{s,X}(z)=e^{-sG(X-\Re z,\Im z)}-1,\quad s\ge0,
\qquad \mathcal Z_\lambda[f_{s,X}]=e^{-s\mathcal J_\lambda(X)}.
\tag{C7}
\]
Here define \(f_{s,X}(z)=0\) for \(\Im z\le0\); the displayed formula applies only for \(\Im z>0\). This noncompact extension is justified by the complete Green tail in manuscript [§18](../../manuscript/sections/17_green_strip.tex). The identity itself contains exactly the same information as \(\mathcal J_\lambda\). A useful new route would independently estimate the weighted product, a response coefficient, or its remainder with a gain at the one-defect scale.

Do not import determinant positivity from a surrogate ensemble while leaving the source-to-zero identification unproved. If an auxiliary positive process is used, a quantitative transfer theorem with its complete error must be the deliverable.

## 5. Earlier hierarchies and what can transfer

**Additional predecessors identified by the author, 8 November:**
[02_heat_flow_rh_applications](../../../../02_heat_flow_rh_applications/summary/CURRENT_SUMMARY.md)
supplies corrected Rodgers–Tao boundary/exterior-force accounting and a
fixed two-root comparison; [03_heat_flow_collision_bounds](../../../../03_heat_flow_collision_bounds/summary/CURRENT_SUMMARY.md)
supplies a Poisson L2 statistic that is exactly an ordered pair sum and a
conditional whole-cluster transfer. The latter assumes real true roots,
although its approximant may have complex roots. Extending that premise
is a concrete question; its RH-conditional simplicity threshold is not
the present nonreal-defect criterion. HCB's later physical-jet correlations
concern arithmetic summands, with scoped stops that do not close this
pair-marginal direction. Note07 links the inspected notes and reviews;
original registers and same-model internal evidence levels are retained.

**Author clarification:** [01_heat_density_asymptotics](../../brainstorm/notes/20_TND_O_PRIOR_HIERARCHY_LOCATOR_20261107.md#4-author-identified-hierarchy-heat-density-asymptotics) is the intended predecessor. Read its ansatz Notes15–16 and current recurrence overview first. The exponential operator generating family and triangular recurrence organize field corrections; later recurrence Notes05/20 supply controlled growing-order field/jet estimates in their stated negative-Newman-time regimes. The zero-functional hierarchy instead organizes factorial zero statistics. A transfer needs a matching domain and paid source/denominator/contour errors. Other located constructions below are optional comparisons.

- Mellin-curvature fermionic, biorthogonal and Schur constructions give source/coefficient determinant hierarchies. Their all-sector algebra may suggest generating functions, but determinant positivity or physical ensemble interpretations do not transfer to canonical zeros. The later author's temperature/source-variable correction must accompany reuse.
- Earlier theta correlation kernels give a direct all-order source hierarchy and its time recursion. This is particularly relevant for constructing a source-side response, but its kernel positivity does not automatically bound a nonlinear zero statistic.
- A forest partition determinant is a genuine functional of fixed real-zero gaps, with forests random at a fixed configuration. It is not a probability law over zeros and presupposes a real-zero setting.
- The author-identified HDA hierarchy is primary field-approximation background. Its order is distinct from factorial zero order; the present Gaussian-Laguerre hierarchy also retains its own variables and limits.

The [Gaussian-Laguerre source/order package](../../notes/24_TND_O_E15_GAUSSIAN_LAGUERRE_HIERARCHY_20261107.md) remains available. Its derivative order is not the factorial order in (C6). Reuse its complete-source estimates only after identifying the actual operator and weight.

## 6. Success, limits and controls

A single nonreal defect must force a declared lower signal while an independently accessible canonical estimate supplies a strictly smaller upper value, or a paid comparison must reduce that question to a genuinely more tractable quantity. Fix dependence on \(X,h,d,\lambda\), all multiplicities, source cutoff and any hierarchy order.

Averaging centers over an interval of size T can dilute one localized defect by roughly h/T. An asymptotic bulk law, a density bound allowing finitely many exceptions, or every-fixed-order estimates do not automatically exclude an isolated defect at unbounded height. The limit \(d\downarrow0\) requires separate explicit control. A theorem at fixed order uniform in unbounded X is acceptable; increasing order is required only if used.

The inherited [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md) and [result index](../../../../../../result-summaries/README.md) apply. Read the [avoid index](../../../../../../avoid/README.md), particularly [target restatement](../../../../../../avoid/01_restating_the_target.md), [shape-only controls](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate changes](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). RH-equivalent positivity, an absolute allowance and finite numerical evidence are not a signed bound.

The [plan](../research-plan/01_TND_OC_RESEARCH_PLAN_20261107.md) selects at most two mechanisms per conceptual cycle. All widths, tests and sufficient inequalities remain revisable through a recorded B decision.

