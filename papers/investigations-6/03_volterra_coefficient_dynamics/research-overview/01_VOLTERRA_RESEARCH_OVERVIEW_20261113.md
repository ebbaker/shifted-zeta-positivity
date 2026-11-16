# Volterra dynamics of the theta recurrence coefficients

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations. **Historical broad scientific
overview.** Its original setup was unactivated; the subsequent first round
is recorded in the [historical progress file](../research-progress/01_VOLTERRA_RESEARCH_PROGRESS_20261113.md).
For the 16 November tail-closure phase read the
[new overview](02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md),
[current plan](../research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md)
and [sole live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md).
The discussion below preserves the original questions and source scope.
Navigation update prepared for Edward Baker with OpenAI Codex assistance,
recorded gpt-6-astra/max.

## Scientific question

What does the complete theta source impose on the nonlinear lattice of
orthogonal-polynomial recurrence coefficients under Newman deformation?
This branch explores whether its exact arithmetic initial data yield
relations, asymptotics or inequalities useful to a tensor representation
or the signed field. The classical lattice equation is a starting
identity; the theta-specific information is the unresolved part.

The [program overview](../../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
places this coefficient problem beside fixed-basis chain transport and
scale refinement. This branch owns the moving orthogonal-polynomial basis
and its coefficients. It does not assume that the lattice admits a finite
closed system or a special solvable theta solution.

## Fixed source and moving coefficients

Retain the [complete source and normalization](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int W_\lambda(u)e^{izu}du,
 \quad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\); \(\tau=1/2-\lambda\) reverses
the clock. Let \(P_n(u;\lambda)\) be the monic polynomials orthogonal
for the unnormalized measure \(W_\lambda(u)du\), with squared norms
\(h_n(\lambda)\). Define

\[
 \beta_n=\frac{h_n}{h_{n-1}}\quad(n\ge1),\qquad \beta_0=0.
\]

Evenness gives the recurrence
\(uP_n=P_{n+1}+\beta_nP_{n-1}\). The inherited deformation law is

\[
 \partial_\lambda\beta_n
   =\beta_n(\beta_{n+1}-\beta_{n-1}).
\]

[Brainstorm 02 §4](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
derives it by differentiating \(h_n\) and using orthogonality. It is the
classical Volterra/Langmuir or Kac–van Moerbeke equation; Van Assche §2.3,
Theorem 2.4 and its symmetric specialization are the inspected reference
passages, linked through the [branch reference guide](../references/README.md).
The source's full tails justify the differentiated moments in the stated
time interval. Reversing to \(\tau\) reverses the coefficient-flow sign.

The moving Jacobi operator has off-diagonal entries
\(a_n(\lambda)=\sqrt{\beta_n(\lambda)}\), and

\[
 H_\lambda(z)=\frac{Z_\lambda}{2}
 \langle e_0,e^{izJ(\lambda)}e_0\rangle,
 \qquad Z_\lambda=\int W_\lambda.
\]

The scalar normalization remains part of the field. This moving-basis
formula differs from branch 02's fixed \(J(1/2)\) and separate
\(e^{-\tau J(1/2)^2}\). State derivatives in a moving basis require
the basis-connection terms.

## Broad directions within this branch

The coefficient sequence packages all source moments. Its positivity and
the generic deformation law hold for many sources, so the central issue
is how the canonical theta coefficients and reflection constrain that
sequence. Possible questions concern explicit relations, growth with
polynomial degree, comparison principles or invariants whose hypotheses
can actually be verified for the unchanged source.

Such information could determine propagation estimates for branch 02 or
help identify a transfer quantity with a signed-field consequence.
An exact determinant formula for the coefficients is an initial-data
description, not automatically a simpler recursive solution. Generic
integrability terminology alone supplies neither an explicit theta
solution nor a positivity theorem for its Fourier transform.

No asymptotic law, finite closure, comparison family or theorem target is
selected in this overview. Those choices belong to VCD-B01 in the research
plan. In particular, scalar return-amplitude zeros are not the real zeros
of the orthogonal polynomials themselves.

## Control example and evidence boundary

For the inherited control \(F_\lambda(x)=2+2e^{\lambda-T}\cos x\),
\(0<T\le1/2\), put
\(p=e^{\lambda-T}/(1+e^{\lambda-T})\). Its finite chain has
\(\beta_1=p\), \(\beta_2=1-p\), \(\beta_3=0\). These satisfy the
Volterra equation and remain regular at \(\lambda=T\), where
\(\beta_1=\beta_2=1/2\) and the field has a double zero at \(x=\pi\).
The control lacks the full theta source/profile, infinite support and
eventual threshold simplicity. Smooth positive-source controls screen
arguments that try to distinguish theta by regularity alone.

The inherited [same-assistant check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md)
supports the identities at its stated internal scope. No theta coefficient
asymptotic or arithmetic sign estimate is established. Use the source
note §8 and [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
to identify the premise each actual witness fails before proposing a new
coefficient inequality. Being a different source is not, by itself, a
verified failure of that inequality.

The [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[control premises 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
govern the interpretation. A coefficient representation is distinguished
from a new quantified consequence.

## Relation to the rest of the program

[Branch 02](../../02_jacobi_chain_height_flow/README.md) can consume coupling
information in a fixed chain; [branch 04](../../04_exact_infinite_tensor_products/README.md)
may provide a separate description of the same source. The
[QTT branch](../../01_qtt_newman_flow/README.md) retains its independent
approximation question. No task or status is transferred from them.

The [shared continuation note](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
provides the VCD-B01 prompt for choosing a first question under the branch
plan. The VCD register owns its task status; no execution request is issued
by planning setup. The [parent plan](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
keeps shared-interface work separate.
