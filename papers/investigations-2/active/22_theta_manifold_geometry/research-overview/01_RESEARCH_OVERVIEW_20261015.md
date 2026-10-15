# 01 — Theta manifold geometry research overview

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

Historical overview of the initial manuscript and first continuation. The current priorities and integrated manuscript are described in [Overview 02](02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md).

The goal of this investigation is to find a geometric reason why the physical theta heat flow cannot develop a collision of a zero with its derivative at positive time. Such an exclusion, with the full domain requirements in place, would connect to the Riemann Hypothesis through the existing heat-flow framework.

The proposed route connects two concrete geometries. The physical function and its derivative define a holomorphic surface whose induced metric degenerates exactly at a common zero. Separately, the arithmetic theta source belongs to a family of elliptic curves carrying a curved hyperkähler metric and a theta line bundle. The central research problem is to transfer information from the arithmetic family to the signed motion of the physical surface.

## Why this is a separate investigation

Investigation 21 studies a broader collection of signed theta estimates, correlations, hypercomplex representations and outer-region bounds. This project takes its physical criterion and signed-form constructions as a foundation, then concentrates on manifolds, connections, real tangent directions and the arithmetic geometry of the source.

The new direction has a specific geometric target and a distinct set of tools. It therefore merits its own manuscript, proof checks and research sequence. The original investigation remains the home of its existing analytic and numerical results. Shared results retain clear provenance rather than being silently reassigned.

## What is established

The starting manuscript constructs a holomorphic jet surface carrying precisely the physical first-jet energy. It identifies collisions with degeneration of its parametrization, computes its curvature, and gives actual calibrated realizations. Curvature records the magnitude of the signed obstruction but loses its direction. The real tangent angle keeps that direction.

A finite collision forces this angle to make a positive quarter-turn over an interval whose length tends to zero. A uniform one-sided continuity estimate would prevent such concentration and therefore exclude collisions. That estimate is a sufficient target, not an established property of theta.

On the source side, the complete theta kernel is an explicit covariant derivative expression in the theta line bundle. The elliptic family has a local curved hyperkähler metric. A suitable Hermitian metric on the same line bundle also produces an explicit abelian ASD connection without changing the vertical derivatives used to express the source. These identities provide concrete objects on which to work. Their current form lives on a noncompact cover and does not yet imply a bound for the oscillatory physical transform.

## The overall objective

Prove a source-specific geometric estimate that rules out positive turning concentration for both physical stationary branches. A useful result must remain meaningful when the physical energy is arbitrarily small and must cover every possible finite positive-time collision. The estimate may instead take the equivalent role of controlling the complete signed boundary current, provided the transfer to collision exclusion is fully justified.

Special holonomy and self-duality are tools for deriving that estimate. Their existence by itself does not ensure that the relevant section is nonzero or that an oscillatory transform has the required sign.

## The steps needed to get there

1. **Make the source geometry intrinsic.** Fix the theta line bundle, its connection, the vertical derivative convention and the transition laws on a suitable cover of the elliptic family. Determine exactly which identities are preserved under changes of coordinates and which require additional modular data. The deliverable is a globally coherent source formula on a declared domain.

2. **Derive the bridge to the physical field.** Apply those connection and curvature identities to the complete transform defining the heat flow. Keep the arithmetic lattice, spectral phase, heat multiplier and boundary terms together. The deliverable is an exact signed identity relating geometric source data to the physical jet direction or boundary current.

3. **Obtain an estimate that survives cancellation.** Use the identity to bound positive turning on short intervals beginning at full stationary points. The bound must be specified from the source and remain uniform near possible collisions. A bound on a larger auxiliary norm is useful only with a proved comparison to the physical energy.

4. **Test the proposed mechanism against known collisions.** Positive, rapidly decaying control sources can satisfy many of the same generic geometric properties and still collide. A successful mechanism must identify a theta-specific hypothesis that these controls fail. This is a way to discover which geometric information is doing real work.

5. **Validate a fixed proposal and close its domain.** Once an inequality and its constants are specified, perform independent analytic review and a discriminating certified calculation. Then prove coverage of the unbounded region and the full collision predecessors. A finite successful calculation is evidence about that proposal, not a substitute for the domain argument.

## Immediate priorities

The first priority is to understand what the explicit ASD theta connection adds to the complete two-source or boundary-current identity. In particular, determine whether its curvature yields a useful signed term after physical reconstruction, and account for the growth introduced by its Hermitian metric.

The second priority is to investigate the one-sided continuity of the real jet angle. It tolerates favorable turning and isolates the concentration forced by collisions. Its second branch has a different denominator away from stationarity, so regularity of each whole tested interval must be retained.

Global compactification or a K3 realization should be pursued when it supplies a missing estimate or a useful boundary condition. A larger nonabelian, twistor, or exceptional-holonomy construction should similarly be tied to a precise benefit. The explicit local models already provide a concrete starting point.

## What would count as progress

An exact transform identity exposing a new arithmetic term would be meaningful progress. So would a proof that one proposed geometric estimate fails on a declared control family, a bounded signed estimate with an honest remaining domain, or a complete treatment of a previously hidden connection or boundary contribution.

The decisive result would be a uniform theta-specific control of positive turning concentration, together with the required global coverage. The present manuscript establishes the geometric setting and conditional criterion; that decisive estimate remains open.

The [manuscript](../manuscript/theta_manifold_geometry.tex), [initial derivation review](../reviews/01_INITIAL_MANUSCRIPT_DERIVATION_REVIEW_20261015.md), and [origin and integration note](../notes/00_research_coordination/01_ORIGIN_AND_INITIAL_INTEGRATION_20261015.md) provide the technical arguments, checks and provenance.

## Continuation of 15 October 2026

The first source-connection bridge calculation is now complete; see the [continuation handoff](../notes/00_research_coordination/02_CONNECTION_BRIDGE_AND_INNER_TURNING_CONTINUATION_20261015.md). Base-only ASD metrics have an explicit classification, including a representative with unit norm and zero connection along the physical path. Thus the originally displayed cusp growth is not intrinsic to the curvature. The path and its external two-source product have flat pulled-back connections, so direct tangential differentiation adds no new curvature-sign term. Transverse jet commutators survive and are included in an exact recurrence and complete signed transform with all lower endpoints.

The turning criterion also has a sharper local model: on `x=chi(s)+s*xi`, the increment tends to `arctan(r*xi)` and its scaled derivative to `r/(1+r²*xi²)`. The odd-branch jet energy differs from physical energy by the limiting factor `1+r²*xi²`. A uniform strict quarter-turn gap is a sufficient conditional target, and still requires theta-specific input.

The next gate is an arithmetic inequality for the complete signed observation, or a transverse/global geometric identity that reaches it with its full remainder. The direct restricted ASD connection has now been evaluated and does not by itself supply that inequality. The stable manuscript remains the initial version; new proofs and checks are in the linked notes.
