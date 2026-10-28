# Collision magnification without a prescribed spatial direction

27 October 2026, America/New_York. Proposal clarified by **Edward Baker**; recorded for him with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008. **Status: research objective, not an established mechanism.**

Edward Baker asked for simpler auxiliary dynamics that can act directly on the explicit theta sum and have a clear geometric interpretation. After examining removal of a directional forcing term, he clarified the desired effect:

> What if it is not related to an explicit direction but it tends to magnify zeros generally?

> I mean collisions

The target is therefore amplification of the degeneracy H=H_a=0, without requiring localization around a chosen axis or curve. At this stage of the discussion the radial integrand was still fixed; the subsequent clarification below relaxes that requirement to the entire integral. A direction was a design choice of earlier examples, not a requirement of the proposal.

The projected source-cost flow in Note23 is a proved baseline. Its weight χ_out is freely prescribed, and no theorem connects its cost decrease to collision magnification. The unforced zero-start damped heat model is stationary. [Note24](../notes/24_EXPLICIT_THETA_FLOW_AND_COLLISION_MAGNIFICATION_SCOPE_20261027.md) makes those distinctions and gives an explicit theta-sum application with a controlled truncation allowance.

A useful next construction should specify the evolving auxiliary field, its dependence on the spectral response, its observation map and regularity, and what precisely grows or concentrates under a multiple-event hypothesis. The physical H itself stays fixed. A canonical bound preventing that amplified behavior would be an additional mathematical result, not a consequence of preserving the observation.

Rotational symmetry alone does not rule out such a response construction. The uniqueness/symmetry argument in Note24 concerns angular redistribution of a source field starting from radial data. A radial response, an enlarged spectral state, or another allowed realization is outside that limitation.

Known colliding controls are essential: a general collision magnifier can legitimately amplify their events too. The question is whether an estimate derived from the complete theta source prevents the same behavior. Avoid a new reformulation of the target without such an estimate; use the [target-classification rule](../../../../avoid/01_restating_the_target.md), [transported-identity caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [control register](../../../../result-summaries/12_collision_controls_and_screening.md).

No flow with both a proved collision-sensitive amplification law and a separating canonical bound has been constructed in this return. This proposal refines the purpose of the existing localization program rather than reporting completion of its collision-exclusion tasks.

## Later clarification of the invariant

Edward Baker further clarified: “The flow in 3d could change the integrand, as long as the entire integral is invariant”. This supersedes fixed radial-integrand preservation as the general requirement in the preceding discussion. A flow may move contributions across radii and angles; all resulting terms and boundary fluxes must be included in the complete observation.

[Note25](../notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) supplies the conservative equation ∂_s j+div J=0 and the explicit choice J=−ε∇j for the full signed theta density. It preserves H and every finite spectral derivative, changes the radial integrand, and needs no prescribed direction. At a collision, two leading central diffusion coefficients vanish, giving one additional inverse power of auxiliary time in their decay. This is a proved diagnostic, not a collision-specific growing instability or a separating theta bound.

The fixed-marginal symmetry argument above applies only to its stated stronger assumptions. The new radial heat evolution is nontrivial and lies outside those assumptions. The present next task is a useful collision-sensitive conservative dynamics and an actual canonical estimate; neither fixed radial marginals nor an angular target are requirements.
