# Direct radial-spectral Newman realization: research overview

**Current scope revision, 6 November 2026.** Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, direct-branch chat0003. The author requested an initial investigation of collisions within this dynamics before choosing a follow-up estimate, and broader collision-control goals if that investigation was promising. [Collision Note04](../notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md) supports that expansion at **proof-author/diagnostic scope**. The [sole register][progress] owns current status; [plan r2][plan] now governs future B02/E03 framing. The original plan and pre-reconnaissance continuation retain their historical scope.

[E02 Review01](../reviews/01_TND_D_E02_CONDITIONAL_REALIZATION_ASSESSMENT_20261106.md) continues to accept the fixed E01 conditional realization without required mathematical correction. Its same-assistant/same-chat internal-assessment qualifications remain. The source/loader, placement, ensemble, initial calibration and ideal access remain supplied. Note04 is subsequent exploratory work; E02 has not assessed its new identities.

**Analytical synthesis, 6 November 2026 — gpt-6-astra/max.** The [direct manuscript](../manuscript/README.md) now develops the complete preparation, instrument and absolute observation, followed by the count-sector calculus, local collision analysis, exact colliding control and outstanding tasks. It uses the parent manuscript as background. The [integration check](../reviews/02_TND_D_E05_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261106.md) preserves the realization’s internal acceptance and the later diagnostics’ proof-author status; manuscript completion supplies no new collision restriction or selected B02 target.

## Current research goals: collision mechanisms and quantitative consequences

The branch now asks both **what happens at a collision in the assessed dynamics** and **whether the canonical source supplies a mechanism that constrains such events**. Useful bounds and conditioning estimates remain a complementary goal; choosing a particular quantity is not a prerequisite for the initial mechanism exploration.

- Understand the conditional state, success probability, signed readout, local zero motion and complete count-output structure at a collision, including higher-multiplicity and endpoint limitations.
- Investigate source-specific relations, invariants or transport restrictions within the unchanged realization that could control the simultaneous signed balances defining an event. A qualitative mechanism is eligible before a numerical bound is fixed; it must eventually identify an independently justified premise and a concrete consequence.
- Compare any mechanism, identity or estimate with direct analysis using the same source information. Screen its actual premises on domains containing the recorded control witnesses. Distinguish an explanatory diagnostic, an intermediate gain and a target-equivalent reformulation.

### Initial findings and rationale

Note04 derives a precise local picture. At an interior double event, the state and positive success mass remain smooth while the signed cosine contrast and its first observation-parameter derivative vanish. Physical time runs toward decreasing Newman lambda, so the local real-zero pair coalesces and leaves the real axis. The singularity is in tracking zeros of a smooth observation, not in the state or fixed energy spectrum.

The existing instrument also supplies analytical signed traces D_j of each count output. With D_0=H_lambda(k)/H_(1/2)(0), they obey
\[
D_j=\frac{(-\gamma t)^j}{j!}\partial_k^{2j}D_0,\qquad
\partial_tD_0=-D_1/t\quad(t>0),\qquad
\sum_{j\ge0}D_j=C(0,k).
\]
Thus a double collision is an equal no-count outcome balance with unequal loss rates, and the first-count signed trace encodes its curvature. Source-sector covariance gives a complementary description of the same moments. Higher multiplicities require higher count/derivative information. These identities motivate examining signed transfer and balance constraints before deciding on an estimate.

The explicit reflected super-Gaussian control in Note04 has a collision at lambda=1/4, k=pi/4 (physical t=1/(4gamma)) while satisfying these generic identities and its own complete smooth-state domain bounds. **No collision-preventing mechanism or estimating advantage has yet been established.** Canonical arithmetic restrictions, rather than generic state positivity or count completeness, remain the prospective source of a separating result. The [local-collision summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [control register][controls], [result index][results] and [patterns index][avoid] retain their evidence and classification limits.

D_j for j>0 is an analytical trace of an already defined output; physically reading every post-count sector is not an added apparatus assumption. Any required change of source, controller, clock, observation or physical access returns to B01. Complete spectra/domains/tails, the literal cosine and absolute normalization stay fixed.

### Next decision and finite scope

B02's **initial collision reconnaissance is complete; mechanism/target selection remains open**. The later author-selected conceptual pass may compare at most two structural approaches and select at most one consequential follow-up, or record a precise missing input/scoped stop. No particular follow-up is chosen here. E03 remains reserved until its target and method are frozen; no numerical plan is activated. [Plan r2][plan] supplies the full phases and stopping rules.

## Historical opening overview — 5 November 2026

The opening text below preserves the original construction question and its then-current dependencies. Its unexecuted/pending statements are historical; the current scope and evidence are stated above.

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort ultra**, verified in turn metadata. Investigation08 chat0003.


**Opening overview, revision 1.** This branch asks whether the complete Dirac-cylinder model can support a specified physical preparation and evolution whose signed radial observation is the canonical Newman family. The author requested separate development of the direct and auxiliary avenues after the parent B01 comparison. This establishes a research program, not a selected controller or a realization theorem.

## Question and fixed starting point

Retain the complete cylinder and geometric operators
\[
C=\mathbb R_v\times S^2_{1/2},\quad
\mathcal D_C=-i\Gamma\partial_v+2D,\quad
L_0=\mathcal D_C^2=-\partial_v^2+4D^2,\quad
H_{\rm kin}=\varepsilon L_0,\quad \varepsilon=\hbar^2/(2m\ell_0^2).
\]
The inherited interpretation is a positive kinetic Hamiltonian with fixed curvature term \(2\varepsilon\). No wall, confinement or interaction is inserted. Every angular shell \(n\ge1\), both Dirac signs and the continuous radial spectrum remain part of the model. At each real \(k\), signed energies are \(\pm\sqrt{k^2+4n^2}\), multiplicity \(2n\) per sign; the square has multiplicity \(4n\). Plain radial evenness reduces the square, not the first-order Dirac operator.

For the canonical source,
\[
F_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
H_\lambda(z)=\int_0^\infty F_\lambda(u)\cos(zu)\,du,\qquad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]
Keep \(H_0(z)=\xi((1+iz)/2)/8\). [E01][e01] supplies complete source tails and each-finite-order bounds on compact real \(\lambda\) intervals, plus the full Fourier/cosine normalization. Complex \(z\) is analytic continuation, not a real self-adjoint spectral label.

## What is unresolved

The angularly damped full-line Green response is
\[
Q_1(\beta)=\operatorname{Tr}_K(e^{-\beta A}(4\sqrt A)^{-1})
=\sum_{n\ge1}e^{-\beta n^2},\qquad A=D^2.
\]
It is independent of probe position. The source scan
\[
\beta=\pi e^{4u},\quad p(u)=e^uQ_1(\pi e^{4u}),\quad
\Phi=(p''-p)/8
\]
and complete theta reflection already recover the source as response data. They do not derive its spatial preparation or identify \(u=v\) physically.

The direct spectral identity is exact: multiplication by \(v^2\) becomes \(-\partial_k^2\). Free kinetic evolution instead multiplies Fourier amplitudes by a function of \(k^2+4n^2\). The first conceptual task must explain the preparation and clock, or isolate the missing construction. Simply conjugating the known scalar generator \(L^{-1}u^2L\) into spinor notation does not explain it.

**Precise outstanding construction:** specify a preparation/evolution/readout triple on the complete cylinder, with a declared admissible source class and physical clock, that produces literal \(H_{\lambda(t)}\) with its absolute calibration. State which part produces the canonical spatial profile and which part implements its \(v^2\) reweighting. An intrinsic explanation and an externally controlled realization are distinct possible outcomes; neither is presumed by opening this branch.

## Choose the evolved object explicitly

| Object | Correct observation and burden |
| --- | --- |
| Linear source amplitude \(F_\lambda\), encoded in spinor fields | Its signed Fourier amplitude can recover \(H_\lambda\); angular encoding, position imprint and phase-sensitive readout are supplied unless derived. |
| Normalized state with position density \(F_\lambda/(2H_\lambda(0))\) | A cosine expectation recovers \(H_\lambda/H_\lambda(0)\), with absolute normalization restored separately. This is the transform of the density, not the momentum amplitude of its square root. State preparation and domain assertions require their own proof. |

These are choices of field/readout within the direct avenue, not two executed models. The state tangent would contain both the factor \(1/2\) and normalization subtraction; changing between these objects during execution changes the contract. Positive \(\lambda\)-increments are unbounded multipliers on unrestricted \(L^2\). Canonical double-exponential decay permits the prescribed source family for every finite real \(\lambda\); that fact is not a bounded physical operation on all states.

## Intended progress and limits

A coherent physical construction is a legitimate first outcome. It must keep source coordinate, radial position, angular damping, laboratory time, proper time and Newman parameter distinct until an explicit law relates them. The initial decision allows at most one declared extension and one complete-spectrum follow-through; it does not authorize a controller survey or fitted potential.

An eventual analytical consequence is a separate decision after assessment. It must state what becomes easier than the original Fourier/Newman representation and why. The [auxiliary sibling][sibling] keeps the natural Hamiltonian-flow question available without requiring this route to adopt its proper-time interpretation.

For every claimed operator power use the appropriate maximal weighted spectral domain. For instance \(\operatorname{Dom}L_0^p\) requires
\[
\sum_{n\ge1}\int_{\mathbb R}(k^2+4n^2)^{2p}
\|P_n\widehat\psi(k)\|^2\,dk<\infty.
\]
General finite-order identities require controlled order-dependent constants; uniform growth in order, an infinite expansion and an all-height estimate remain separate obligations. Source transforms are entire; inherited raw scalar \(G\)-field integrals initially have only \(|\operatorname{Im}z|<1\).

## Research navigation

The [research plan][plan] owns bounded task specifications. The [branch progress file][progress] is the sole live register for TND-D tasks. Start with TND-D-B01 on Astra when selected by the author. Shared E01 material and its assessment remain at the parent; no source files are moved or copied into this branch.

## Inherited evidence and controls

[E01 Note02][e01] is consumed at proof-author comparison scope; its new claims await the shared TND-E03 assessment. MC11's operator/source inputs retain their existing internal acceptance and shared-premise qualifications. Investigation05's companion retains its [same-assistant checking status][book-review]. MC11-OBS-E01 and MC11-E05 remain external tasks with unchanged statuses. No pending Note13-only preparation or measurement statement is silently imported; an eventual use requires its assessment or an explicitly assigned local proof/check.

The [result index][results], [theta cluster][theta], [control register][controls] and [patterns index][avoid] govern this branch. Classify a representation, diagnostic, intermediate estimate and target-equivalent reformulation separately under [avoid/01][a01]. [Coordinate re-realization][a03] supplies no sign gain by itself. Retain every negative conclusion's stated class under [avoid/07][a07].

The control screen is analytical at planning scope, without new computations:

| Control | Shared premises and exact limitation |
| --- | --- |
| Euler-factor sources | Smooth positive even source and applicable Green/Fourier constructions survive; the unchanged canonical arithmetic source fails. Their recorded positive-threshold witnesses remain controls. |
| Weighted-square and finite-prime perturbations | Applicable positive half-line/square-source formulas survive; complete unit coefficients and full canonical reflection fail. Matching finitely many endpoints does not give global smooth reflection. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Their applicable source regularity, positivity, reflection and Fourier transport survive; the exact canonical arithmetic expansion fails. Generic representation premises do not reject their collisions. |
| Atomic and finite-profile controls | Fourier observations and finite moments can survive; the smooth source and operator-domain assumptions used here need not. Do not infer a smooth-state realization without a separate construction. |

Naming the canonical input is not a quantitative collision restriction. Any future excluding estimate must reject relevant controls on a domain containing their witnesses, as [avoid/02][a02] requires. Keep the literal cosine observation; a finite cosine prefix or a changed kernel is a different hypothesis.


[e01]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[book-review]: ../../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[plan]: ../research-plan/02_DIRECT_NEWMAN_REALIZATION_RESEARCH_PLAN_R2_20261106.md
[progress]: ../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[sibling]: ../../02_hamiltonian_auxiliary_dynamics/README.md
