# Unresolved clusters and physical heat collisions

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0004. Actual model and
reasoning effort are unavailable in the recorded configuration. No
subagents or numerical research campaign were used.

**Status: local analytical consequences derived and incorporated;
same-assistant checking only.** The author's unresolved-pair idea is
developed in manuscript §10.4, Propositions 10.4–10.6. These are conditional
local approximation statements, not a collision exclusion or a bound on
the Newman constant. B07 remains ready/unactivated and E25 unissued.

Read the [result index](../../../../result-summaries/README.md), especially
[cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
for established local heat geometry and
[cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
for the VCD error inputs; also the [avoid index](../../../../avoid/README.md),
specifically [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[13](../../../../avoid/13_a_factor_is_not_the_target.md), and
[15](../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## Phase clarification

The angle arg(q_(N−1)+i q_N) counts source-polynomial zeros, not zeros
of F. It was introduced as an analogy for a possible comparison lemma;
no such connecting theorem is established. The manuscript now says this
at the start of §5.3. Its Gaussian example makes the distinction explicit:
the polynomial phase has many crossings while F(z)=exp(−z²/2) has no zeros.
The phase directly relevant to F is its change of argument around a
zero-free contour in the observation plane. That count is the basis of
the cluster treatment below.

## Resolution without individual root labels

There are two parameters: N is approximation degree, while λ is physical
backward heat time. Proposition 10.4 makes the existing compact
convergence uniform on every fixed compact real λ interval. It follows
by dominating the normalized moments at all earlier times by a fixed
multiple of the moments at the upper endpoint. No heat equation is
assumed for the finite moving-node readouts themselves.

Fix a real-centered circle of radius ρ that is zero-free throughout a
compact time interval and contains exactly two limiting zeros, counted
with multiplicity. A strict boundary comparison transfers that count
to the approximants. The circle can contain the whole pair even when
available bounds cannot separate its members. This is uncertainty in
what G_N establishes about F, not an intrinsic prohibition on resolving
exact zeros of G_N.

The contour moments in (10.13) yield the center and squared half-separation:

\[
c=(z_1+z_2)/2,\qquad D=((z_1-z_2)/2)^2.
\]

Both are analytic in λ through a double event. For a conjugation-symmetric
two-zero cluster, D>0 means distinct real zeros, D<0 means a nonreal
conjugate pair, and D=0 means a real double zero. No persistent ordering
of the two roots is needed.

If the uniform boundary error is ε_N and the limiting boundary modulus
is at least η>ε_N, Proposition 10.5 gives

\[
b_N=-\log(1-\varepsilon_N/\eta),\qquad
|c_N-c|\le\rho b_N/2,\qquad
|D_N-D|\le d_N:=2\rho^2b_N.
\]

The proof integrates log(G_N/F) by parts on the circle. It requires no
lower bound on an individual root slope, which vanishes at a collision.
The moment-tail allowance supplies a decreasing budget in N once below
η. A finite-model alternative replaces η by a verified model boundary
margin in log(F/G_N), while also requiring its two-zero count. The
boundary margin is an actual premise; the error upper bound alone does
not establish it on a prescribed growing family.

The band |D_N|≤d_N formalizes an unresolved pair. Inside it the true
separation is at most 2 sqrt(2 d_N); outside it the sign is certified by
the sign of D_N. At a fixed isolated real double event, Proposition 10.6
derives D'(λ*)=2 from the normalized heat equation. If D'≥κ>0 locally,
the unresolved time band lies within 2 d_N/κ of λ*. Each sufficiently
large finite readout has at least one double event nearby; any such event
in this interval lies within d_N/κ. Uniqueness of the finite-degree event
is not asserted. This is a fixed-event limit, not a uniform assertion over
all events, heights or multiplicities.

The quadratic model (z−a)²−2(λ−λ*) explains the orientation. Increasing
λ converts a conjugate pair into two real roots; the reversed clock
τ=1/2−λ reverses that description. Root separation has square-root scale,
whereas D is smooth. Higher multiplicities need additional symmetric
cluster coordinates. No actual theta collision is asserted or excluded.

## Prior work, classification and controls

This uses standard argument-principle and holomorphic perturbation ideas;
no novelty claim is made. The prior
[theta-manifold manuscript](../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex),
its analytic heat equation and local heat-Taylor development, were read
through the routing in cluster13. The present addition couples that
local geometry to a quantitative Jacobi approximation error. The checked
[Rodgers–Tao passages](../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md#fixed-cluster-discussion-supplement-16-november-2026-chat0004)
give background on individual simple-real-zero dynamics; that ODE is
not used across a double event here.

Applied [catalog12](../../../../result-summaries/12_collision_controls_and_screening.md)
as a premise screen, with no rerun of numerical certificates:

- Euler-factor, weighted-square, reflected super-Gaussian and smooth
  shape/positive-primitive sources can satisfy the local heat, compact
  approximation and cluster hypotheses. None of those local premises
  must fail. They fail unchanged complete theta arithmetic, which the
  generic local collision law does not use. Their collisions must be
  reproduced, not ruled out, by a valid local resolution theorem.
- Finite canonical-score, selected-prime and smooth finite-data controls
  likewise are not excluded by this local estimate. Their failed full
  canonical identities remain distinct from any unproved fixed-region
  zero geometry; in particular E10 is not upgraded to a collision control.
- Atomic controls do not provide an infinite nondegenerate Jacobi chain
  past their support size. The local contour/heat argument still applies
  to their exact fields. Continuous compact triangular sources do have
  all needed compact-time moments; the positive full-line confinement
  hypothesis they fail in other estimates is not used in Proposition 10.4.
- RH-conditional endpoint controls retain that assumption and fail
  unchanged arithmetic; they do not furnish an unconditional theta event.
- Changed observation kernels fail the literal Fourier/backward-heat
  premise. Abstract finite-profile relaxations do not specify a physical
  analytic field or an actual isolated zero cluster.

The mathematical gain is a quantitative local uncertainty bound that
survives loss of simplicity. The open question is whether the complete
source controls the required cluster boundary margins and coverage as
the height and time domain expand. The RH-equivalent global objective
is not reissued as a new criterion or supported by finite checks.

## Checks and archive repair

[Assessment11](../reviews/11_VCD_CLUSTER_RESOLUTION_ASSESSMENT_20261116.md)
records the proof and scope check; [build14](../numerics/14_VCD_CLUSTER_RESOLUTION_MANUSCRIPT_BUILD_20261116.json)
records the reading PDF and document checks. The PDF stays in ignored
root output, with intermediates outside the repository.

The separately requested chat refresh repair is documented in
[the recorder diagnosis](../../../../tools/CHAT_HISTORY_CREATION_METADATA_REPAIR_20261116.md)
and [receipt13](../numerics/13_VCD_CHAT_CREATION_METADATA_REPAIR_20261116.json).
It recovered the preceding final reply while preserving the original
creation time and complete public prefix. No mathematical claim is
validated by conversation capture or a file hash.
