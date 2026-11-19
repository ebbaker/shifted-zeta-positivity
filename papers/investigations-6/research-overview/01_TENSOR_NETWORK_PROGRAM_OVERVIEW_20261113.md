# Tensor networks and recursive representations of the Newman flow

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations. **Broad program overview;
no new research execution.** The original overview-only setup has now
been followed by parent and branch plans at the author's request.

**Subsequent parent-planning update, 13 November 2026:** the requested
[collection research plan](02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
now covers all four workstreams and shared interfaces. The
[sole parent register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns TN6 shared tasks only. A subsequent branch-planning request added
JCH, VCD and ITP plans/registers; QTT retains its existing ownership. The
[collection index](../README.md) links all four plans and sole registers.
The history below retains the earlier overview-only scope.

## The program

The motivating idea is to use methods from condensed matter physics and
quantum chemistry to understand the complete Newman source through its
tensor structure. A useful representation might organize successive
heights recursively, give one continuous family covering all heights, or
assemble the exact state from an infinite sequence of controlled factors.
The program leaves open which architecture is most natural.

Exactness and tractability are distinct questions. An infinite chain or
product can represent the field exactly while retaining infinitely much
information in its coefficients. A finite approximation may nevertheless
be useful if its rank and errors are controlled. The branches separate
these questions so that a representation identity, an approximation bound
and an arithmetic consequence can each be assessed on their own terms.

The shared ambition is a new usable relation or estimate: for example,
height-dependent chain propagation, theta-specific coefficient structure,
or a transfer rule that constrains the signed field. This is an open
research direction, not a claim that a tensor representation forces the
desired zero geometry.

## Common source, clocks and observations

Keep the complete source from
[GNP §2](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
 \Phi(u)=e^u\sum_{n\ge1}(2r_n^2-3r_n)e^{-r_n},\quad
 r_n=\pi n^2e^{4u}\quad(u\ge0),\qquad \Phi(-u)=\Phi(u),
\]
\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \qquad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\in[0,1/2]\),
and \(z=x+iy\). Real Newman height \(x\) is twice zeta height.
Contractive imaginary time decreases \(\lambda\). Increasing height is
a different evolution from changing Newman time.

| Coordinate or index | Role |
| --- | --- |
| \(u\) | Source coordinate in the literal Fourier integral |
| \(x\), with optional \(y\) | Height and transverse observation offset |
| \(\tau\) | Reversed Newman time |
| QTT bit or refinement level \(k\) | Resolution of a source coordinate |
| Jacobi site \(n\) | Orthogonal-polynomial degree, not a height sample |

A finite complex-height domain or an increasing-height family must be
specified when a later estimate is formulated. Compact convergence does
not imply uniform convergence over unbounded height. Any changed Hilbert
space, normalization or tensorization must include its exact readout map.

## Four complementary branches

### 01 — Finite QTT approximation

[Branch 01](../01_qtt_newman_flow/README.md) studies binary-coordinate
tensor trains for the source-amplitude state. Its inherited work provides
an explicit Fourier contraction, a generator MPO of bond dimension at
most three, a compact approximation hierarchy and one floating pilot.
The next conceptual choice in its existing plan is the observation norm
and first quantitative rank/error estimate. Small source-state error must
be transferred through cancellation and normalization before it becomes
useful field information.

### 02 — Exact Jacobi-chain height flow

[Branch 02](../02_jacobi_chain_height_flow/README.md) uses orthogonal
polynomials for \(d\mu_*=W_{1/2}du/Z_*\), where \(Z_*=\int W_{1/2}\).
Multiplication by \(u\) becomes the self-adjoint tridiagonal operator
\(J_*\). The inherited identity is

\[
 H_{1/2-\tau}(z)=\frac{Z_*}{2}
 \langle e_0,e^{-\tau J_*^2}e^{izJ_*}e_0\rangle.
\]

Height evolves under \(iJ_*\), while imaginary time evolves under
\(-J_*^2\). The chain wavefunction has an exact single-excitation MPS
encoding. This branch asks how its coefficients and propagation can be
described recursively as height grows. It owns the fixed-basis evolution
and tensor encoding, including their domains and limiting topology.
The inherited construction and its relation to the physics chain mapping
are in [Brainstorm 02 §3](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
and the [Chin et al. passage record](../../investigations-5/brainstorm/references/EXACT_HEIGHT_REFERENCES_20261113.md).

### 03 — Volterra coefficient dynamics

[Branch 03](../03_volterra_coefficient_dynamics/README.md) studies the
coefficients obtained by rebuilding the polynomial basis for
\(W_\lambda du\). The squared recurrence coefficients satisfy

\[
 \partial_\lambda\beta_n
   =\beta_n(\beta_{n+1}-\beta_{n-1}),\qquad \beta_0=0.
\]

This classical Volterra/Langmuir equation is inherited from
[Brainstorm 02 §4](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md),
with its [Van Assche §2.3 reference](../../investigations-5/brainstorm/references/EXACT_HEIGHT_REFERENCES_20261113.md).
The scientific question is what the complete theta initial data impose
on this lattice beyond generic positivity and orthogonality. Coefficient
relations could inform branch 02 or a signed-readout argument. The moving
basis \(J(\lambda)\) is not substituted into the fixed-basis evolution
without its connection terms.

**16 November continuation:** the
[tail-closure induction overview](../03_volterra_coefficient_dynamics/research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md)
develops source-sensitive constraints on the omitted Jacobi tail and a
possible degree induction. Its [plan](../03_volterra_coefficient_dynamics/research-plan/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md)
implements Edward's sustained-session/Sol-subtask authorization. This is
ready setup, not a new zero theorem or a transfer of sibling tasks.
Prepared for Edward Baker with OpenAI Codex assistance, recorded
configuration gpt-6-astra/max.

### 04 — Exact infinite tensor products

[Branch 04](../04_exact_infinite_tensor_products/README.md) studies
infinite networks assembled by refinement. Binary source coordinates give
an exact product for the height phase. Ratios of successive dyadic source
averages give an exact source product whose factors approach identity on
each compact interval. The inherited constructions and norm bounds are
in [Brainstorm 02 §§5–6](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md).

The open question is whether these growing-support factors have a useful
recursive tensor description, or whether another scale decomposition is
better. Convergence, full-line assembly, complex-height dependence and
possible removal of a known leading oscillation belong here. Finite QTT
rank/error comparisons remain with branch 01.

## How the branches support one another

Branches 02 and 03 describe different aspects of the same polynomial
representation: one evolves a state in a fixed basis, the other evolves
the coefficients of a moving basis. Branch 04 organizes the source by
resolution; its exact constructions may suggest controlled finite
approximations for branch 01. None of the three new branches must wait
for QTT-B01 to complete before its own question can be discussed.

The three proposed proof directions are accounted for within this
structure: theta coefficient relations in 03, recursive scale transfers
in 04, and height transport in 02. Invariants for the signed boundary
amplitude are a shared aim, with any concrete proposal owned by the branch
that constructs it. This setup does not create a separate invariant task
without a specified mathematical object.

The existing [Green identity](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/05_green.tex),
[boundary-log acquisition](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/07_boundary_log.tex)
and [deflation](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/09_deflation.tex)
are possible consumers. Their required field data, tails and denominator
costs remain obligations. A computational comparison retains the complete
[Riemann–Siegel baseline](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/10_riemann_siegel.tex),
including both arms, normalization and remainder.

## Inherited evidence and controls

The [first brainstorm](../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
is exploratory representation and approximation analysis with a floating
pilot. The [second](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
is an open conceptual brainstorm with exact representation identities and
a [same-assistant analytical check](../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md).
Setup supplies no new proof audit, numerical result or strengthened status.

The [result index](../../../result-summaries/README.md) and
[avoid index](../../../avoid/README.md) are mandatory context, particularly
[classification 01](../../../avoid/01_restating_the_target.md),
[controls 12](../../../result-summaries/12_collision_controls_and_screening.md),
[control premises 02](../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes 03](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../avoid/07_scoped_exclusions_read_as_universal.md).

The inherited control \(2+2e^{\lambda-T}\cos x\) has a regular finite
Jacobi chain and regular Volterra coefficients at its positive-time double
zero. Smooth colliding sources also admit local refinement products.
These facts screen generic inferences from positivity, exactness or regular
tensor evolution. The [full premise screen](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
§8 distinguishes the missing complete-source/arithmetic, reflection,
profile or literal-readout premise in each catalog family. It is reused
at its recorded scope; its numerical witnesses were not rerun for setup.

Proposed quantitative inequalities must face those actual controls rather
than inherit rejection merely because a control is not theta. The narrow
finite constant-matrix exclusion and the fixed-prefix chain limitation
are not exclusions of all exact networks. No branch assumes a zero sign
from an exact representation or from self-adjointness alone.

## Scope and planning history

The initial request deferred detailed plans and progress files. The
subsequent parent plan and then branch-planning request supersede that
deferral: all four branches now have bounded plans and sole registers
under the [model/task workflow](../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
Their first B questions remain open; E derivations and assessments are
reserved, and setup issues no execution packet. Branch 01's existing
identities remain authoritative and unchanged in scope.

The [continuation note](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
provides one current B-task prompt per new branch without selecting a priority.
The [crosswalk](../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md) records
source ownership and the user-directed workflow adaptation. References
remain in their [canonical catalog](../references/README.md), and the
founding chat retains its existing unique archive.

## Subsequent arithmetic continuation investigation, 19 November 2026

The author added [05 — arithmetic gap continuation](../05_arithmetic_gap_continuation/README.md)
as a direct child of this collection to avoid further nesting. Its
[overview](../05_arithmetic_gap_continuation/research-overview/01_AGC_RESEARCH_OVERVIEW_20261119.md)
uses the gap/chain/Mellin results developed under VCD as background and
asks for a source-specific whole-time arithmetic error estimate. Its
[AGC register](../05_arithmetic_gap_continuation/research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns those tasks. The four original representation programs and their
historical scope above remain intact. For Edward Baker with OpenAI Codex
assistance; setup lead recorded gpt-6-astra/max, continuation requested ultra.
