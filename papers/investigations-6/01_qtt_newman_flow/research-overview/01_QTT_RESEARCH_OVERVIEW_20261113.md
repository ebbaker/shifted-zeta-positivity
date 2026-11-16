# QTT research overview

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort are
unavailable in recorded configurations. **Setup and inherited-evidence
synthesis; research unactivated.**

## Question and intended consequence

Can a quantics tensor train represent the prescribed theta-source orbit
with ranks and working precision that remain useful as observation height
increases, while controlling the complete signed field or a specified
Green observation? A useful first result would be a quantitative rank/error
bound with all source, quadrature, contraction and normalization costs, or a
precise limitation of one declared allowance. Representability alone is an
inherited identity, not a new arithmetic estimate.

The [broader program](../../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
now separates this finite-accuracy question from exact Jacobi-chain
height transport, moving-basis Volterra dynamics and exact scale products.
Those sibling overviews do not change the QTT source, plan or live register.

The [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md) apply. In particular use
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[stable-model scopes 17](../../../../result-summaries/17_constructive_stable_model_obstructions.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[control premises 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The [plan](../research-plan/01_QTT_RESEARCH_PLAN_20261113.md) classifies the
next work before execution; the [register](../research-progress/01_QTT_RESEARCH_PROGRESS_20261113.md)
alone owns current status.

## Fixed source and clock

Retain the complete source and normalization from
[GNP source §2](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
 \Phi(u)=e^u\sum_{n\ge1}(2r_n^2-3r_n)e^{-r_n},\quad
 r_n=\pi n^2e^{4u}\quad(u\ge0),
 \qquad \Phi(-u)=\Phi(u),
\]
\[
 W_\lambda=e^{\lambda u^2}\Phi,\quad
 H_\lambda(z)=\tfrac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \quad H_0(z)=\xi(1/2-iz/2)/8.
\]

The complete sum supplies smooth reflection; a reflected finite prefix
does not automatically share all endpoint derivatives. The initial scope
is \(0\le\lambda\le1/2\), with \(\lambda_0=1/2\),
\(\tau=\lambda_0-\lambda\in[0,1/2]\), and

\[
 \psi_\tau(u)=e^{-\tau u^2}W_{1/2}(u),\qquad
 \partial_\tau\psi=-X^2\psi,\qquad
 \partial_\lambda H=-H_{zz}.
\]

This is the source-amplitude version of the
[calibrated first-shell operator](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/03_geometry_operator.tex).
Contractive imaginary time decreases Newman time. The alternative
square-root-density state has generator \(X^2/2\) and a different readout;
it is not silently substituted into this branch's formulas.

Let \(z=x+iy\). Newman height \(|x|\) is twice zeta height. Increasing-height
domains, transverse offsets, error tolerances and source cutoffs are to be
specified by QTT-B01. The existing Green construction uses offsets 0, 4, 8;
these are a concrete inherited consumer, not mandatory offsets for every
future estimate. No endpoint \(\lambda=0\) assertion is imported from a
strictly positive-time domain without its own uniformity proof.

## Tensor representation and inherited approximation

For \(N=2^L\) midpoint samples on \([-U,U]\), let
\(h=2U/N\), \(a=-U+h/2\), \(w_k=h2^{L-k}\), and
\(u_{\boldsymbol b}=a+\sum_kw_kb_k\). The sites are binary resolutions
of one coordinate. The
[opening note §§2–6, equations (3)–(16)](../../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
derives

\[
 \sqrt h\,\psi_\tau(u_{\boldsymbol b})\approx
 A_1^{b_1}(\tau)\cdots A_L^{b_L}(\tau),\qquad
 \widehat K=(aI+\sum_kw_kn_k)^2,
\]
\[
 \widetilde H_{1/2-\tau}(z)=\frac{\sqrt h}{2}e^{iza}
 \prod_k[A_k^0(\tau)+e^{izw_k}A_k^1(\tau)].
\]

The generator has an explicit MPO with bond dimension at most three.
Its full semigroup is contractive; individual affine-expansion gates need
not be. The Gaussian multiplier's exact unfolding ranks can be full in
this ordering, so small generator rank is not a fixed-rank evolution theorem.
An initial polynomial of degree \(d\), multiplied by a heat polynomial of
degree \(2m\), has a sampled MPS with bond dimension at most \(d+2m+1\).
The note gives compact-clock convergence and the absolute field allowance

\[
 |H-\widetilde H|\le E_{\rm tail}
   +Uh^2M_2/24+\tfrac12\sqrt{2U}\,e^{bU}\varepsilon,
 \qquad |y|\le b,
\]

where \(\varepsilon\) is finite-state Euclidean error and \(M_2\) bounds
the complete integrand's second source-coordinate derivative on the chosen
compact domain. Source truncation, computed-core and arithmetic errors
are additional payments. This is an inherited sufficient allowance, not
an optimal rank or precision lower bound.

For general MPS decomposition, the inherited reference inspection covers
Schollwöck v2 §4.1.3, equations (30)–(36). Lindsey v3 §4.1, Proposition 13,
provides a polynomial-exact interpolative QTT; its §3.2 analytic bound
requires an analytic extension bounded on a specified ellipse. The branch
has not supplied theta-specific, height-uniform constants for that theorem.
Shinaoka et al. v3 §§II.1 and III.1–III.2 supply the scale-encoding and
compressed-operation precedent. All versions, primary links and inspection
limits are in the [branch reference record](../references/README.md).

## Evidence levels and the missing estimate

The opening source calls its status **exploratory representation and
approximation analysis, with one floating compression pilot**. Its
[self-check](../../../investigations-5/brainstorm/reviews/01_MPS_SELF_CHECK_20261113.md)
is by the same assistant. Its
[pilot record](../../../investigations-5/brainstorm/numerics/MPS_NEWMAN_PILOT_20261113.json)
uses a finite eight-mode prefix, binary64 arithmetic, dense initialization
and independently compressed time slices. Observed ranks 8 and 10 do not
give a height-dependent law, interval certificate or end-to-end cost gain.
The exact finite algebra checks support their stated instances, not an
independent proof audit. Setup does not promote any of these statuses.

The central unresolved choice is the observation norm. Ordinary source
fidelity can be inadequate after Fourier cancellation and gamma
normalization. The complete
[Riemann–Siegel baseline](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/10_riemann_siegel.tex)
retains both arms, gamma factors and remainder. A comparison with it must
use the same target field and paid errors. The
[boundary-log theorem](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/07_boundary_log.tex)
and [deflation method](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/09_deflation.tex)
provide consumers for acquired field information; their anchors, tails
and denominator costs remain obligations. The
[square-root conditioning control](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/11_conditioning.tex)
limits one enlarged-source information class, not all theta QTT methods.

QTT-B01 may compare ordinary weighted-source compression, an observation-
weighted QTT approximation, and QTT treatment of a complete normalized
expression. Any transformed generator or observation must be derived; the
simple source-coordinate operator cannot be assigned unchanged by analogy.
One explicit first bound and method must be selected before QTT-E01 starts.
Construction, propagation, contraction, precision and certification costs
belong to the same comparison. No presumed speed advantage is an input.

## Controls and classification

The [opening note §§9–10](../../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
already screens the catalog families against tensorization and supplies
\(F_\lambda(z)=2+2e^{\lambda-T}\cos z\), whose two-site state is a product
at its positive-time double event. This defeats a generic collision barrier
from low rank or positive amplitudes. It does not supply the complete theta
source, full arithmetic/profile or eventual threshold simplicity.

The same screen distinguishes Euler-factor controls by their altered
xi/source, weighted-square and finite-prime controls by missing complete
coefficients/reflection, reflected and smooth-primitive controls by missing
canonical square arithmetic, and variable-readout controls by their missing
literal cosine/Newman observation. No control is assigned theta's observed
efficient ranks without proof. Each proposed quantitative inequality must
name the particular premise its actual witnesses fail.

Representation, compact convergence and rank/error estimates are separate
from a signed arithmetic result. Universal time-zero Green vanishing is
the inherited RH-equivalent reformulation, stated once rather than tested
numerically. No equivalence with a restricted tensor ansatz is asserted.
The present setup opens no zero-exclusion task. Prime-occupation models and
other physical constructions remain possible future sibling questions.

See the [crosswalk](../notes/02_QTT_SETUP_AND_SOURCE_CROSSWALK_20261113.md)
for exact source ownership and the
[continuation](../notes/01_QTT_CONTINUATION_AND_PROMPT_20261113.md)
for the bounded next decision.
