# ITP-E03 analytical manuscript integration

14 November 2026, America/New_York. Intended author **Edward Baker**.
Substantial OpenAI Codex LLM assistance. Recorded execution dispatch
**gpt-6.1-sol / ultra**. Independent backend metadata unavailable.

The [editable draft](../manuscript/main.tex) integrates the results
**proved in-note** by [ITP-E01](02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
and accepted at that scope in the [ITP-E02 assessment](../reviews/01_ITP_E02_EXACT_CELL_PHASE_ASSESSMENT_20261114.md).
ITP-E03 follows the [frozen TN6-E04 request](../../research-progress/handoffs/TN6-E04-r1.md).
All 30 [manifest entries](../../numerics/14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json)
matched their recorded lengths and SHA-256 identities before drafting.
The manifest SHA-256 is
`520b0908840cc690a9ee64ef37ff35f8d57ec1a426683158375d63b393883b99`.
The [build record](../numerics/02_ITP_E03_MANUSCRIPT_BUILD_20261114.json)
identifies this output. The
[internal assessment](../reviews/02_ITP_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
checks the integrated exposition.

## Proof map

| Draft location | Source and work performed |
| --- | --- |
| §2, (1)–(6) | [GNP source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex), through complete domination and the heat equation. Derived the Mellin split, its elementary endpoint term, and the factor \(H_0=\xi(1/2-iz/2)/8\). The [reference guide](../references/README.md) records checked DLMF passages. |
| §3, (7)–(10) | [Founding exact-height note](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md), §5 (9)–(10), and [E01](02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md), §2. The exact parent–child mass equality gives an isometry with coefficients equal to square roots of conditional masses. The common Hilbert limit appends the uniform reference bit. It identifies coefficient vectors with normalized cell indicators and uses density of finite dyadic step functions. The isometry updating the prepared state is distinct from the embedding in this limit. The square-root inequality transfers the weighted \(L^1\) estimate to the squared weighted \(L^2\) error. |
| §4, (11)–(13) | Founding note §5 and E01 §2. The bit phase product converges on each unit interval for bounded complex \(z\); its conditional mean over unresolved bits equals the cell phase integral. The sum over all intervals is justified by the complete exponential moments. |
| §5, (14)–(17) | E01 §§2–3. Derive the ordered-pair kernel, \(V_8<868\), one spatial tail, and the rational allowance \(2066/2^{32}<5\cdot10^{-7}\). The absolute field error is uniform for \(0\le\lambda\le1/2,\ x\in\mathbb R,\ |\Im z|\le8\). |
| §6 | E01 §4. At every fixed \(L,\lambda\), alias frequencies give error tending to \(Z_\lambda/2\) for the full-line center-point rule. The matched direct integration baseline equals the exact-cell field. |
| §§7–8, (18) | E01 §§5–6 and [B01 decision](../brainstorm/notes/01_ITP_B01_EXACT_CELL_PHASE_DECISION_20261113.md). The projected reverse-time orbit uses an extra in-cell moment. The future arithmetic allowance is conditional on actual mass and contraction bounds. |

The Hilbert-space details complete the specified construction; the
bound and comparison retain their original hypotheses and constants.
The draft uses \(Q_j\) for source derivative polynomials and \(P_h\)
for cell averaging. No mathematical correction to the accepted E01
result was needed. There was no source-mass acquisition or numerical
research run. The formal finite construction uses \(2^{32}\) masses
at \(U=2,L=30\).

## Control and claim screen

The [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md) and their
[tensor bounds](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
place this work at the quantitative approximation milestone in
[avoid 01](../../../../avoid/01_restating_the_target.md). The analytical
screen reuses the catalog's exhibited witnesses. Resolve the premises
of the generic projection, the positive mass-splitting construction,
the specific constant, and the literal phase separately.

| Existing control | Applicability and missing premise |
| --- | --- |
| Euler-factor translated sources | Each fixed translation preserves integrability of the time- and exponentially weighted density and its derivative by double-exponential decay. The complete unmodified normalized theta density fails. |
| Three-/four-weight squares and finite source changes | Weighted regularity can hold for their continuous even reflection with integrable piecewise derivatives. Complete coefficients and full smooth reflection together fail for the nontrivial changes. The event times are distinct from all-real thresholds in the finite-source audit's classes. |
| Finite-prime orbit controls | Weighted regularity can hold for the reflected square-source perturbations even when finitely many prime identities and linear measurements pass. Full reflection and unchanged complete coefficients fail. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | They can satisfy weighted regularity and local positivity and still collide. The normalized square expansion fails, even where their parity, endpoint, and primitive data agree. |
| Three-atom, BW-01 and atomic finite-profile thresholds | The absolutely continuous density and weighted derivative premises fail. Their exact finite representations also lack the complete theta source and can have many simultaneous threshold events. |
| Continuous compact finite-profile extensions | A triangular convolution supplies a weighted integrable weak derivative. Exterior zero-mass cells violate strict positivity for the ratios. Complete theta arithmetic and full profile fail. |
| RH-conditional normalized endpoint controls | Their regular density can admit the projection estimate, subject to the source construction's conditional status. Ordinary Dirichlet-series arithmetic fails. |
| Fixed amplitude with variable kernel | The literal exponential phase and the full cosine/Newman observation fail, even with unchanged amplitude and finitely many observation terms. |
| Actual-profile relaxed positive measure | Its measure is an object in a relaxed zero-profile fit. The specified source-coordinate density and exponential readout are absent from that feasibility result. |
| Earlier Gaussian counter-kernels | Some smooth versions meet weighted regularity at the allowed times. The canonical arithmetic density used for \(V_8\) and \(T_8\) is absent. [Counter-kernel cluster](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md). |

This screen retains [the premise rule](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[the scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and the [normalization rule](../../../../avoid/08_normalization_and_constant_slips.md).
The aliasing obstruction concerns precisely a fixed-level center-point
lattice with the full-line masses in a supremum over all real heights.
Positive local ratios and the general weighted approximation theorem
are compatible with the smooth controls' collisions. The theta envelope
gives the numerical constant in the canonical case without a zero or
signed-field consequence.

The [assessment](../reviews/02_ITP_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
is same-worker and shares the frozen premises. The
[review limits](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[evidence status](../../../../avoid/06_status_stronger_than_the_evidence.md),
[reference discipline](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
and [quantitative milestone](../../../../avoid/20_volume_without_a_gain.md)
govern its use. Remaining challenges are certified acquisition and
uniform arithmetic, core ranks and comparison cost, whole-line
operator-product bounds, a closed time approximation, and any
relative or signed-field transfer.
