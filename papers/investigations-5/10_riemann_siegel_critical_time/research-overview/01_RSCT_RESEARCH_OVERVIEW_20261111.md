# Riemann–Siegel at the Newman threshold research overview

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Actual backend model and reasoning effort are unavailable in the recorded session configuration; recommendations below are separate from provenance.

## Question and evidence level

Assume the canonical de Bruijn–Newman constant satisfies \(\Lambda>0\). Can the complete symmetric Riemann–Siegel expression, together with the all-real zero configuration at time \(\Lambda\), yield an independently proved arithmetic estimate incompatible with a multiple real zero at that time?

This is a research question, not an acquired estimate. The [original collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), Proposition “A positive threshold entails a finite collision” and Corollary “Exact endpoint target,” already supplies the reduction. [Investigation 02 Note02 §3](../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md) explains it, and [09's Note20](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md) records the author's present RS-specific clarification. These are inherited analytical arguments, not newly independently audited proofs.

The [result index](../../../../result-summaries/README.md), particularly [heat-flow reductions](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [local geometry and equivalent criteria](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md) govern interpretation. Apply [target classification](../../../../avoid/01_restating_the_target.md), [control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Fixed source, clock and domain

Keep
\[
 H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
 \qquad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda,
\]
\[
 \Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \qquad
 H_0(z)=\tfrac18\xi((1-iz)/2).
\]
The reflected argument \((1+iz)/2\) gives the same field. These are the [complete-source normalization](../../09_green_potentials_newman_flow/manuscript/sections/02_source.tex) and Polymath (1)–(4), not a freely chosen real-entire model.

The event domain is the unknown \(0<\Lambda\le1/2\), \(x_*>0\), with
\[
 H_\Lambda(x_*)=H_\Lambda'(x_*)=0,\qquad
 \text{all zeros of }H_\Lambda\text{ real}.
 \tag{1}
\]
Multiplicity is any finite \(m\ge2\); the problem is not restricted to ordinary double zeros. Evenness supplies the reflected event at \(-x_*\); \(H_\Lambda(0)>0\) excludes the origin. The real \(z\)-axis represents the critical line, with absolute zeta ordinate \(x/2\) at time zero. At positive time this is a deformed field, not the original zeta function.

The inherited finite-attainment argument uses [Polymath v2, Theorem 1.5(i)](https://arxiv.org/html/1904.12438v2#S1): nonreal zeros cannot have \(|\Re z|\ge e^{C/\lambda}\), for an absolute \(C\), when \(0<\lambda\le1/2\). For times approaching \(\Lambda\) from below with \(\lambda\ge\Lambda/2\), this confines such zeros to a common compact set. A limit lies on the real axis, and simplicity would contradict the implicit-function theorem and conjugation. This reasoning is already proved in the sources above.

The compact height bound deteriorates as \(\Lambda\downarrow0\). A final exclusion must cover every possible event height and every positive threshold, including that limit and bounded heights. There is no premise that \(\Lambda\log(x_*/(4\pi))\) lies in \([1/2,1]\) or equals one. Any narrower intermediate domain must state its remaining coverage gap. Fixed-positive-time high-zero simplicity is already known and cannot be counted as a new discriminator.

A shift \(\lambda=\Lambda+s\) changes the source to \(e^{\Lambda u^2}\Phi(u)\); it cannot turn the threshold field into the original zeta slice. Negative-forward-time notation in older sources must be converted explicitly.

## Complete symmetric expression and the event

[Polymath v2 §4, (35)–(39)](https://arxiv.org/html/1904.12438v2#S4) gives the exact Gaussian-evolved reflected formula. In that paper's notation, for real \(x\ne0\), \(\lambda>0\), and a fixed integer \(N\ge0\), set
\[
 A_{\lambda,N}(x)=
 \sum_{n=1}^{N}r_{\lambda,n}((1+ix)/2)
       +R_{\lambda,N}((1+ix)/2).
\]
The complete remainder belongs to this definition. Then
\[
 H_\lambda(x)=2\Re A_{\lambda,N}(x),\qquad
 H_\lambda'(x)=2\Re A_{\lambda,N}'(x).
 \tag{2}
\]
Keep \(N\) fixed locally when differentiating, or justify all cutoff changes with the compensating remainder. The exact formula has broader scope than Theorem 1.3's effective approximation region; derivative estimates must have their own justified domains.

At (1), both real parts in (2) vanish. If \(A_{\Lambda,N}\ne0\), write \(A=\rho e^{i\psi}\). At a real zero,
\[
 H_\Lambda'=-2\rho\psi'\sin\psi,
 \qquad \psi'=\Im(A'/A).
 \tag{3}
\]
Thus the event forces a stationary complete phase in this case. The alternative \(A=0\) must also be handled. These are inherited identities from [Note20 §3](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md), not bounds on either case. A phase for the leading saddle alone is insufficient.

Schwarz symmetry makes (2) real at every real time, even when other zeros are nonreal. The extra hypothesis at the threshold is the global all-real configuration and its relationship to the impending collision. A prospective argument must identify how that additional information produces a quantitative restriction on the actual arithmetic arms.

## What would count as progress

Excluding every positive-time common real zero is the inherited RH-equivalent endpoint target; rewriting it in (2) or (3) is not a gain. Symmetric representation, local Hermite splitting and an all-real product description are background identities. Known Laguerre inequalities allow multiple zeros and cannot simply be made strict.

A useful intermediate result must give a quantitative estimate with explicit parameter dependence, a new covered part of the event domain, or a proved obstruction to a precisely stated method. The first conceptual task may instead freeze a fixed proof obligation, clearly marked unproved.

Two possible formulations for B01 are:

- Keep the exact complex arm and determine whether the threshold's all-real product information constrains its amplitude and phase derivative, including the amplitude-zero case.
- Work directly with the coupled complete value and derivative, using the all-real threshold condition to preserve arithmetic cancellation rather than bounding the two components or the omitted modes independently.

These are candidate formulations only. B01 may examine at most two and need not invent a second if the first fails decisively. No source-specific sign or nonvanishing estimate is currently available. A proposed uniform first-jet floor with no use of threshold conditioning must be compared with, and routed to, existing HCB-05 ownership rather than duplicated here.

## Inherited limits and neighboring ownership

| Existing work | Reuse and boundary |
| --- | --- |
| [02 positive-threshold analysis](../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md) | Finite-event reduction and the failure of a simple time shift to import time-zero spacing information. Explanatory analysis and aspirational specifications; no acquired upper bound. |
| [03 current overview](../../03_heat_flow_collision_bounds/research-overview/02_POST_CALIBRATION_RESEARCH_OVERVIEW_20261028.md) and [register](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) | HCB-05 owns existing joint first-jet acquisition. Its calibrated exterior floor and scoped leading-pair, exponent-pair and signed-remainder failures remain at their recorded internal-review levels. They do not exclude every threshold-conditioned estimate. |
| [04 three-regime overview](../../04_three_regime_heat_flow_dynamics/research-overview/01_THREE_REGIME_DYNAMICS_RESEARCH_OVERVIEW_20261026.md) | Positive-threshold versus zero-threshold multiplicity regimes; conditional dynamics and energy tasks retain their owners. |
| [08 collision constraints](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/README.md) | Regular deflation, force and finite-pair survival interfaces; the parked acquisition cycle is not reactivated. |
| [09 RS section](../../09_green_potentials_newman_flow/manuscript/sections/10_riemann_siegel.tex) and [child](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/README.md) | Exact evolution, full reflected representation and Green-band results remain there. At the threshold \(J_\Lambda=0\), including at multiple real zeros, so its value alone does not separate the event. |

## Collision-control requirements

Use the [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) on the proposed estimate's actual witness domain, not on an unrelated collision-free box.

| Control class | Premise unavailable in this critical-time argument |
| --- | --- |
| Euler-factor and translated controls | Unchanged canonical arithmetic coefficients and source; reflection and physical heat evolution can survive. |
| Weighted-square, finite-tail and finite-prime-orbit controls | Full canonical reflection and/or the complete coefficient sequence. Many lack a finite all-real threshold, so local events are not automatically threshold examples. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical theta square-series arithmetic, despite surviving shape or primitive identities. |
| Atomic and exact finite-profile controls, including continuous extensions | Full theta profile and the published eventual simple-zero behavior at positive time. |
| RH-conditional endpoint controls | Their conditional assumption remains; they cannot become unconditional theta counterexamples. |
| Variable-readout and heat counter-kernel controls | Literal cosine readout, complete canonical source and/or physical Newman generator. |
| Relaxed Green profiles | Identification with the exact canonical zero multiset and complete boundary field. |

No new arithmetic inequality has been screened successfully during setup because none has been proposed. These are premise requirements for B01, not evidence that the intended conclusion holds. In particular, even real backward-heat polynomials can have an all-real slice with a multiple zero and nonreal roots just before it. Symmetry and the all-real endpoint alone therefore provide no contradiction.

The [plan](../research-plan/01_RSCT_RESEARCH_PLAN_20261111.md) bounds the first decision. All research remains unactivated.

