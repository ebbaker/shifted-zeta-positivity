# Zero Counts, Heat Transport, and Localized Hodge Energy

22 October 2026, America/New_York. Drafted for **Edward Baker** with substantial LLM assistance. Original recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The stability/growing-window continuation records **gpt-6-astra, effort max**, 22 October 2026.

Read the [manuscript PDF](main.pdf) or [main TeX source](main.tex). This is the shared analytic manuscript for Investigations 4, with its [overview][overview], [progress register][progress], [extension note][extensions] and [internal review][review] at the investigation base. It consolidates established transport and Hodge identities and proves the stated quantitative extensions. The main proofs are self-contained; classical ingredients and their provenance are identified. There is no mathematical priority claim, RH theorem or endpoint-simplicity theorem.

Separate agents of the same model reviewed the initial arguments. The stability/growing-window additions have [same-assistant self-review](../../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) only. These checks are internal, not independent specialist or human validation. The [result index][results], [avoid index][avoid] and [collision controls][controls] govern the scope of the claims. The original [LHCT][lhctprogress] and [ZTP][ztpprogress] ledgers retain their tasks and open signed-exclusion dependency.

## Theorem map

The following numbers refer to the 22 October manuscript build. Each row links to the source section containing the complete statements and proofs.

| Results | Content | Scope retained |
| --- | --- | --- |
| [Theorem 2.2; Proposition 2.5](sections/02_localized_energy.tex) | Exact localized power energy and the energy of `q dw` on the normalized cover `w^q=f`; the double-cover identity is `W_<ε=4πεN`. | The value cutoff lies below a paid boundary amplitude. All multiplicities are counted; this does not detect simplicity. |
| [Proposition 3.1; Theorem 3.2; Propositions 3.4–3.5; Theorem 3.6; Proposition 3.7](sections/03_regularization.tex) | Exact-mass regularization, harmonic reproduction and second-order bias, sharp-exponent direct divisor stability, and smooth-kernel errors. | Interior root units and the cutoff geometry are paid where used. Scalar Lipschitz optimality is restricted to its stated potential class. |
| [Theorems 4.2, 4.6, 4.10; Propositions 4.11, 4.13–4.14](sections/04_zero_transport.tex) | Local Hermite splitting, complete real cap/wall balance, complex discriminant residue and boundary-degree agreement, and oriented endpoint indentations. | Real event weight is floor(m/2); complex event weight is binom(m,2); ordinary complex multiplicity is conserved. These quantities and their endpoints are distinct. |
| [Propositions 5.1–5.3](sections/05_cover_geometry.tex) | Euler characteristic of normalized root covers, orders of the reciprocal differential, and amplitude/unit dependence. | The singular-fiber excess is distinguished from regular-fiber topology. Physical periods require more than root positions. |
| [Theorem 6.1; Proposition 6.2; Lemma 6.3; Theorems 6.4–6.5](sections/06_pair_matrices.tex) | Explicit inverse-square matrix bounds, complete forced root and weight evolution, centered contraction interface, and polynomial Hermite Lyapunov theorem. | The entire finite-cluster exterior unit and normalization terms remain. Polynomial relaxation is deterministic and admits a multiple initial zero. |
| [Proposition 7.1; Lemma 7.2; Corollary 7.3; Propositions 7.4–7.5](sections/07_statistics_caps.tex) | Clock/sine-kernel inverse-square targets, sparse-defect stability, density-one interpretation, singular-weight transfer and a shrinking-tent threshold. | Weak pair laws do not exclude isolated defects. A growing-population application must pay both small-gap and tail control. |
| [Lemma 8.1; Propositions 8.2–8.5](sections/07_statistics_caps.tex) | Exact physical projective-cap phase and imaginary-time closing faces, with heat controls. | A simple late cap need not have zero flux; tracked roots do not determine the phase of the complete jet. |
| [Theorem 9.1; Lemma 9.2; Theorem 9.3; Corollaries 9.4–9.5](sections/08_theta_concentration.tex) | Complete-source concentration, Fourier transfer, growing spatial clock windows and fixed-population cumulative cancellation. | Every source mode and integration tail is retained. Spatial bounds allow K=o(L√κ); cumulative dynamics keep fixed populations. No numerical onset or differentiated-location-error inference is asserted. |
| [Appendix A](sections/10_supporting_certificate.tex) | An exact low-value-energy consequence of an existing certified canonical-theta disk count and boundary floor. | Supporting illustration only. The certificate is imported without a new replay; no main theorem depends on it. |

## Exact source crosswalk

The manuscript is a synthesis and extension of the following existing sources. Earlier results retain their original homes and status; including their proofs here does not make them new results.

| Earlier source | Manuscript use and distinction |
| --- | --- |
| I2/22 physical-jet [Note 04: spacetime index][i2index] and [Note 06: wall flux][i2wall] | Section 4 restates and proves the real index and complete moving-wall birth balance, including their orientation. This is inherited transport structure, with analytic splitting and endpoint details supplied in the present exposition. |
| BW12 [Note 02: holomorphic reference and boundary degree][bwdegree], [Note 05: two-root discriminant][bwtwo], and [Note 09: many-root discriminant][bwmany] | Sections 4 and 6 retain the finite proper cluster, complete exterior factor and discriminant charge. The manuscript includes contour preparation and a regular-target/resultant proof of boundary-degree agreement; it does not import the two-root cap-sign formula for arbitrary multiplicity. |
| RHE [Note 08: derivative-weighted energy][rhe8] and [Note 09: paid count bound][rhe9] | Sections 2–3 begin from the established exact differential `2 dw`, modulus/Green identity and degree/area count mechanism. The localized equality refines the earlier full-energy bound; the general p-energy and q-cover family, stability and localization statements are extensions proved in this manuscript. |
| LHCT [Note 05: zero counts and relative topology][lhct5] | Sections 4–5 consolidate the three different counts and normalized-cover distinction. The full proofs and complete boundary conventions are included. |
| LHCT [Note 06: pair matrices and forced heat][lhct6] | Section 6 reproduces the finite matrix and forced-energy results with full proofs. Section 9 supplies a self-contained complete-source location proof for the canonical application, so the main argument no longer needs an internal saddle theorem. |
| LHCT [Note 07: weighted statistics and cap phase][lhct7] | Sections 7–8 give the precise weighted transfer and phase controls with full analytic proofs and primary literature context. No implication from weak PCC alone to full simplicity, or GUE relaxation, is asserted. |
| LHCT [Note 08: low-value Hodge count][lhct8] | Sections 2–3 generalize the p=1 localized count and its compact logarithmic regularization; Appendix A retains its inherited finite-theta illustration. |
| Earlier LHCT [Note 02: complex-time theta caps][lhct2] and [Note 04: closure concentration][lhct4] | These are the prior complete-cap and closure records. Section 8 proves its exact physical-cap/closing-face formulas; it does not replace the earlier canonical complex-time estimates by a claim that simple roots make every boundary contribution vanish. |
| BW10 [Note 20: differentiated saddle][bwsaddle] | This is the earlier fixed-rank location/velocity source used by LHCT Note 06. Section 9 gives a separate elementary proof of the location rate, with explicit full-source moment bounds, and a cumulative cancellation corollary. No pointwise velocity asymptotic is silently imported. |
| RHE [Note 04: actual regular theta fiber][rhe4], [certificate][rherecord], [replay script][rhereplay] and [review][rhereview] | Appendix A alone imports the certified count two and boundary floor on the disk centered at 35 with radius 8. It distinguishes the new localized derivative energy from the original reciprocal energy. No numerical replay or new acquisition was performed for this manuscript. |

The [extension note][extensions] separates the general power/root-cover family, regularization stability and localization, elementary canonical concentration proof, and cumulative cancellation from the inherited results. These are manuscript extensions and quantitative formulations; neither this crosswalk nor the term “extension” asserts mathematical priority over the literature.

## Files and build

`main.tex` contains the front matter, acknowledgements and references. The ten source files under [sections](sections/) contain the argument and supporting appendix. To build from this folder, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The revised 22 October internal build has 44 pages. The [build record](BUILD_RECORD.json) records the delivered compilation; mathematical review belongs to the [review record][review]. The PDF is a generated manuscript deliverable; auxiliary compilation files are not research records. Follow [LARGE_FILES.md][large] and keep derived bulk data outside Git. The main analytic proof requires no numerical data file, numerical replay, remote service or unproved statistical conjecture.

This is one maintained manuscript project, with concise milestones in the shared [DRAFT_HISTORY.md][milestones]. No manuscript snapshot directory, new investigation, commit or tag was created for this drafting round. The original manuscript conversation retains its unique existing home 11 history **0001**; the distinct stability continuation is base archive **0010**; [history guidance][history] is unchanged, and the shared manuscript does not create a second registration.

[i2index]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[i2wall]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[bwdegree]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md
[bwtwo]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[bwmany]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md
[bwsaddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[rhe8]: ../../09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
[rhe9]: ../../09_reciprocal_hodge_energy/notes/09_SIGNED_LAGUERRE_TRANSFER_AND_COUNT_BOUND_20261022.md
[rhe4]: ../../09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md
[rherecord]: ../../09_reciprocal_hodge_energy/numerics/03_ACTUAL_THETA_COMPARISON_20261022.json
[rhereplay]: ../../09_reciprocal_hodge_energy/numerics/03_compare_actual_theta_fiber_20261022.py
[rhereview]: ../../09_reciprocal_hodge_energy/reviews/03_ACTUAL_THETA_FIBER_COMPARISON_REVIEW_20261022.md
[lhct2]: ../../11_late_heat_caps_and_charge_transport/notes/02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md
[lhct4]: ../../11_late_heat_caps_and_charge_transport/notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
[lhct5]: ../../11_late_heat_caps_and_charge_transport/notes/05_ZERO_COUNTS_REAL_BIRTHS_AND_RELATIVE_TOPOLOGY_20261022.md
[lhct6]: ../../11_late_heat_caps_and_charge_transport/notes/06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[lhct7]: ../../11_late_heat_caps_and_charge_transport/notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md
[lhct8]: ../../11_late_heat_caps_and_charge_transport/notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md
[lhctprogress]: ../../11_late_heat_caps_and_charge_transport/research-progress/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRESS_20261022.md
[ztpprogress]: ../../11_late_heat_caps_and_charge_transport/research-progress/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRESS_20261022.md
[overview]: ../../research-overview/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRAM_20261022.md
[progress]: ../../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md
[extensions]: ../../notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md
[review]: ../../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[large]: ../../../../LARGE_FILES.md
[history]: ../../11_late_heat_caps_and_charge_transport/chat-histories/README.md
[milestones]: ../../DRAFT_HISTORY.md

## Completed next-step round — 22 October 2026

The [continuation note](../../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md) prioritizes sharp C² weighted-divisor stability and a short growing-clock corollary from the existing bounds. It records primary-source comparisons, exact controls and the verified chat-history identity. The original candidates are now proved in [Note 09](../../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) and manuscript Proposition 3.5/Theorem 3.6. The separate [Note 10](../../notes/10_GROWING_CLOCK_WINDOWS_20261022.md) proves Corollary 9.4. [Review 02](../../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) is a same-assistant audit with primary-source comparisons and the current PDF checks. ZHM-09 and ZHM-11 remain open.
