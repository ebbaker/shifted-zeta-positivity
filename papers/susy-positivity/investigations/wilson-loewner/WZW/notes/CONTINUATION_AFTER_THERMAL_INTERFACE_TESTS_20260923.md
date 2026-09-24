# Continuation after the thermal-interface tests

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).

**Effort:** not exposed; not inferred.

**Status:** continuation and research priorities after the completed finite-place and thermal boundary tests. This note records the five avenues discussed at the close of the investigation and incorporated into Section 8 of the manuscript. It adds no new numerical experiment, positivity theorem, or physical realization.

## Starting point and decision

The [17-page manuscript](../manuscript.pdf), with [editable source](../manuscript.tex) and [integration audit](../reviews/review_codex_interface_manuscript_integration_20260923.md), now incorporates the following results:

- The [Bost–Connes coefficient identity](ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md) remains valid: with \(\beta=2\omega\), \(c_n(\omega)=n^{(\beta-1)/2}\varphi_\beta(P_n)\). The centering factor still requires a physical interpretation in any proposed realization.
- The [finite-place interface test](FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md) gives a unitary controlled delay model with ordinary radiation-energy accounting and an identity limit, but its arithmetic amplitudes fail. Separately, an unchanged archimedean factor times a finite Euler product has a pole incompatible with the required global passivity for \(0<\beta<1\).
- The [energy-exchanging boundary test](THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md) supplies an exact native Kubo susceptibility and a conservative effective linear boundary model. A passive parallel load with finite total response spectral mass leaves the unchanged modular core's front exponent fixed, and cannot supply the arithmetic shift or its logarithmic tangent. This is not an exact finite-coupling microscopic quantum scattering construction or a theorem excluding all couplings.

**Current decision:** park incremental work on the regular finite-place passive parallel-load route. Retain its coefficient identity, valid energy balances and scoped exclusions. Adding further modes with finite total response spectral mass, or adjusting fixed loop constants, does not address the demonstrated obstruction.

Among the directions examined so far, the first two avenues below deserve the main arithmetic effort. A broader physical realization remains exploratory. This priority assessment updates the [earlier research-avenues note](RESEARCH_AVENUES_20260923.md); it is not a claim that any route is known to succeed.

## 1. Cumulative storage for the complete arithmetic transfer

**Priority: first concrete continuation.** Work with

\[
K_\omega(p)=\frac{\xi(\tfrac12+p-\omega)}{\xi(\tfrac12+p+\omega)}
\]

and its ordinary radiation norm. Start on the first arithmetic window \(\log2<L<\log3\), where the formal causal kernel contains the full archimedean term and its first translated copy. This exposes the first prime contribution and its interference with the archimedean response while retaining the actual completed target.

The next bounded task is to write the exact finite-window input/output energy difference, isolate those cross terms, and determine whether they admit a storage description from independently specified state variables and evolution. The [arithmetic-source analysis](../../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) and the earlier avenues note provide the cumulative-balance viewpoint and a finite polynomial calibration.

A useful outcome would be either a derived nonnegative storage expression with its assumptions and range explicit, or a precise unresolved term showing why the proposed state description fails. Defining storage to be the desired norm deficit does not establish its positivity; numerical positivity alone would not complete the task. Keep the full archimedean kernel and the interference terms throughout. A finite time-window comparison must not be promoted to a globally passive finite Euler completion.

## 2. Explicit canonical systems from prime and gamma data

**Priority: complementary main route.** Seek an explicit canonical-system Hamiltonian and state norm whose positivity can be established from the arithmetic data, without assuming RH or the target transfer's contractivity.

The next bounded task is to audit the explicit construction in [Suzuki, A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/abs/1204.1827), identify exactly where its parameter restriction enters, and compare its kernel and integral-equation structure with the first-window storage calculation. The cited explicit unconditional construction is for \(\omega>1\). Extending it into the required small-shift range is an open obligation, not a result available for use here.

The useful deliverable is a clearly stated extension problem: the operator, determinant, invertibility or Hamiltonian-positivity condition that must be controlled, together with which parts are unconditional. An abstract realization obtained only after assuming innerness would not close the present gap.

## 3. Global deformations of modular scattering

**Priority: exploratory physical route.** The [modular Hodge half-shift channel](MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) remains the strongest concrete physical reference among the tested constructions. A deformation that changes its asymptotic propagation, field structure or bulk dynamics may lie outside the fixed-core parallel-load exclusion.

Before investigating detailed prime echoes, a proposed deformation should derive the required positive-real-axis front and half-shift tangent:

\[
K_{\beta/2}(p)\sim(2\pi/p)^{\beta/2},\qquad
\left.\partial_\beta\log K_{\beta/2}(p)\right|_{\beta=1}
\sim-\tfrac12\log\frac{p}{2\pi},\qquad p\to+\infty.
\]

The next task, if this avenue is reopened, is to specify one independently motivated interaction, its domain, radiation normalization and positive energy, then test these two necessary conditions. Preserve the global completion. An infinite-spectral-mass continuum is outside the proved finite-mass theorem, but would need its own well-defined coupling and energy analysis. A fitted response chosen from the arithmetic target is not a derived physical model. No qualifying global deformation has been constructed in the present work.

## 4. Focused causality and support analysis

**Priority: support for the first two routes.** Use contour, residue and off-axis controls to identify the analytic obstruction to an unweighted causal realization, and to ensure finite-window manipulations remain faithful to the completed quotient.

A bounded continuation could trace which residues arise when passing from a safe far-right Laplace representation toward the boundary, keeping the gamma/rational completion and zeta factors together. The [finite-place note](FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md) gives the relevant warning: deleting primes while keeping the full archimedean factor creates an uncancelled pole that the full quotient cancels.

The expected output is a support or contour statement with explicit hypotheses, not an inference from unit boundary modulus alone. Distinguish a formal causal kernel on finite windows from a globally bounded causal transfer. Such analysis can expose what a storage or canonical construction must handle; it does not by itself establish the required positive norm or full-family innerness.

## 5. Independent review and consolidation of the retained results

**Priority: confidence in the foundation.** Obtain independent mathematical and physical review of the coefficient dictionary, fixed bounded-readout limitation, finite-Euler completion pole, and finite-spectral-mass front theorem. The existing audits are by the same assistant.

A reviewer should check the exact hypotheses and the distinctions between an isolated thermal expectation and a completed response, coherent signal energy and thermal fluctuations, exact uncoupled susceptibility and a finite-coupling microscopic model, and an unchanged-core boundary load and a global deformation. The relevant starting points are the [coefficient audit](../reviews/review_codex_arithmetic_orbit_weights_20260923.md), [interface audit](../reviews/review_codex_finite_place_interface_20260923.md), [boundary audit](../reviews/review_codex_thermal_boundary_structure_20260923.md), and [manuscript integration audit](../reviews/review_codex_interface_manuscript_integration_20260923.md).

The unchanged numerical records contain [87 coefficient controls](../numerics/records/arithmetic-orbit-weights-20260923.json), [144 interface controls](../numerics/records/finite-place-interface-20260923.json), and [203 boundary controls](../numerics/records/thermal-boundary-structure-20260923.json). Their [replay instructions](../numerics/README.md) and source hashes make them reviewable. The controls support the stated calculations and failures; they are not independent review or interval proofs of the analytical claims.

## Suggested opening task for the next investigation

Derive the ordinary finite-window energy expression for the complete shifted-zeta kernel on \(\log2<L<\log3\), retaining the full archimedean contribution and first-prime interference. Investigate whether it admits an independently defined positive storage realization. Record an explicit identity or an explicit remaining obstruction, with every assumption stated. Use numerical checks only to test that derivation; do not assume the desired contraction or reopen regular thermal boundary-load fitting without a mechanism outside the established exclusion.

This note supersedes the [original post-WZW continuation](CONTINUATION_AFTER_WZW_WRITEUP_20260923.md) as the current handoff. Earlier notes remain historical records. New analytical work belongs in `notes/`, programs and compact records in `numerics/`, and reviews in `reviews/`; the [live milestone index](../DRAFT_HISTOR.md) continues to identify manuscript revisions without dated snapshots.
