# Review of the seven symmetry programs and research priorities

18 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**, actual reasoning effort **ultra**, verified from the session metadata. Three delegated readers used the same reviewing model. Most execution notes reviewed here were written by gpt-6.1-sol; this is an internal cross-model LLM assessment of those executions, not specialist human review.

## Assessment and recommended priorities

The seven programs have produced useful approximation estimates, a concrete residual-cancellation result, and several precise obstructions. **S01 and S02 have the clearest complete-error improvements ready for reuse. S03 has the most promising lead for a new arithmetic mechanism, but has not beaten the direct first-jet consumer.** S04 supplies a rigorous growing-cutoff model in which to investigate that mechanism. S05 is a useful local source-evaluation component. S06 and S07 have clarified the physical observation and ruled out specific inadequate estimates; further geometric work needs an additional estimating input.

The common successful practice is to combine the actual signed terms before bounding them: reflected endpoints in S01, the correction and entering mode in S02, and residual derivatives and spatial increments in S03. This is stronger evidence for continuing cancellation-preserving arithmetic estimates than for introducing another symmetry representation alone.

The [original symmetry questions][questions] and [program guide][guide] proposed S02 first, followed by S03. That opening sequence has now been executed. The next round should **consolidate the best S01/S02 error payments and give S03 one bounded analytic continuation**, using S04 where its regime applies. The guide's initial status table should be read alongside the completed lane notes and this assessment, rather than as the current execution ledger.

The program has not yet enlarged the established real collision-free region, improved the effective exterior onset, or supplied a new Newman bound. On the existing slab \(1/100\le t\le1/5\), the real bridge
\[
1001<|x|<e^{2000}
\]
remains open in this research route. The global consumer also needs a complex exterior; real first-jet nonvanishing alone does not supply it. The four isolated large-height checks in S04 do not fill an interval of this bridge. These scope statements follow the [integrated baseline][baseline] and [global consumer][global].

## Accomplishments at a glance

Here \(E=H^2+H_x^2\), \(\mathcal L_0=H_x^2-HH_{xx}\), and the common pilot is \(\mathcal B=[1/100,1/5]\times[999,1001]\). Numerical comparisons below refer to the specified certified allowances, not measured exact errors or optimal possible bounds.

| Program | Accomplishment | What the result supports |
| --- | --- | --- |
| **S01 Modular self duality** | Pairs the omitted-mode endpoints before absolute estimation; complete added errors at derivative orders 0, 1, 2 fall to about 85.15%, 92.78%, 97.01% of the old allowances on \(\mathcal B\). | A modest but directly usable complete-error improvement for the existing source evaluator. |
| **S02 Cutoff reflection** | Retains a holomorphic signed correction and pays its continuation, cutoff transition and derivatives; disk error falls from about 0.887748 to below 0.226300 on the pilot, and from about 2.897966 to below 0.431778 across the tested cutoff crossing. | A substantially better analytic approximation than the declared absolute-correction baselines. |
| **S03 Normalized jet rotation** | Bounds the complete correlated residual increment below 0.000266448, compared with 0.002011747 from independent endpoints using the same source data; exports an oscillator-calibrated first-jet approximation. | A real finite arithmetic-cancellation gain and a specific hypothesis to investigate at growing height. |
| **S04 Time height scaling** | Proves a full-cutoff, phase-retaining scalar/first-derivative replacement error below \(e^{-\kappa(\kappa+12)/(16t)}\) for \(1\le\kappa\le2\), \(0<t\le1/20\). | A uniform regime model with explicit costs; the signed core still needs estimation. |
| **S05 Covariant theta jets** | Uses complete-source parity and Taylor expansion to tighten source-jet interval enclosures near \(u=0\), including all tails. | A reusable local source component, subject to a named downstream consumer. |
| **S06 Hodge and transverse geometry** | Derives observation maps, proves \(0.37<x^2K<0.375\) and \(K^2>10^{310}E\) on the pilot, and constructs exact source compensation with a signed current. | A useful diagnosis of the raw channel's scale mismatch and an exact transfer of the existing physical sign. |
| **S07 Geometric duality and quaternionic symmetry** | Derives the complete zero-form Green identity, zero canonical self-flux, and failure of a generic first-order bulk-energy bound for the physical path observation. | A precise limitation on the proposed geometric route and requirements for a different estimate. |

## Findings for each program

### S01 Modular self duality

The [paired-endpoint note][s01-note] makes quantitative use of reflection after the complete theta source has been shifted. Its gain comes from summing the reflected endpoint contributions and the two source monomials with their signs intact. The remaining nonstationary integrals retain their absolute payment. The theorem covers spectral derivatives on a fixed complex neighborhood and retains the vertical boundary term for sources that do not have the required analytic reflection.

On the real pilot, the same retained polynomial has complete added errors in the fixed scale \(G_c=1000^{7/4}e^{-125\pi}\) reduced approximately as follows:

| Physical derivative order | Old allowance divided by \(G_c\) | New allowance divided by \(G_c\) | Reduction |
| --- | ---: | ---: | ---: |
| 0 | 4.620515e-12 | 3.934535e-12 | 14.85% |
| 1 | 3.469201e-12 | 3.218759e-12 | 7.22% |
| 2 | 3.055846e-12 | 2.964413e-12 | 2.99% |

The isolated tail improves more, to approximately 0.616–0.627 of a stronger matched unpaired allowance. The smaller complete gains are correctly explained by the unchanged Taylor and quadrature costs. This is the cleanest demonstration that the self-duality question has yielded a useful error estimate.

Its limitation is specific: the omitted modes must satisfy a positive phase gap. The retained modes below the stationary threshold do not satisfy that premise, so this theorem does not estimate the difficult signed core. In the displayed one-step bound, even perfect endpoint cancellation leaves the remaining integral payment; it cannot by itself remove that whole error. **Reuse the theorem where its error component matters, then investigate the retained arithmetic sum separately.** Recompute its endpoint allowance on a new domain; the pilot's ratio is not a uniform all-height constant. See the [review and replay guide][s01-review].

### S02 Cutoff reflection

The [analytic correction note][s02-note] turns the known correction profile into a holomorphic fixed-cutoff approximant and pays for the difference from the published correction. It also combines an entering arithmetic mode with the correction jump before taking absolute values. Derivative errors through order two follow from the complete analytic residual on radius-one-half disks. The removable profile points and the fixed-cutoff transition are treated explicitly.

This is a substantial bounded implementation result. On \([1017,1019]\), the test includes the entire cutoff-eight-to-nine crossing for the declared time slab. It certifies the error theorem there; it does not certify noncollision throughout that rectangle. Its novelty also needs the qualification already made in the source: the correction machinery and exact cutoff identity existed in [transport Notes 20][old20] and [22][old22], and the improved value approximation comes from [Polymath Corollary 6.4][polymath]. The new comparison is against specified absolute baselines, not against the strongest earlier correlated implementation.

The remaining budget identifies a concrete next task. On the pilot, the published correction residual contributes about 0.209083 of the 0.226300 allowance, roughly 92%. At the crossing, the correction residual and the relatively loose signed transition allowance contribute about 0.206434 and 0.206301. Therefore better transition matching has an immediate target at the crossing, whereas optimizing the much smaller holomorphic-continuation term will have limited pilot benefit.

**Benchmark the full analytic correction against the existing frozen-exponential correction and analytic edge matching on the same disks.** Retain the same physical normalization, derivative orders and coverage. A useful next result is a smaller complete allowance or a demonstrated cost improvement at matched accuracy; tighter isolated formulas are insufficient. S03 has already consumed the current S02 formula, so repeating that initial handoff is no longer the next milestone.

### S03 Normalized jet rotation

The [opening result][s03-open] showed why scalar transport using two independent endpoint errors is dominated by the ideal direct first-jet test based on the same data. The [continuation][s03-note] addresses the exception left open by that result: a smaller estimate for the complete correlated residual increment.

With \(Q=H/\mathcal A\), the full corrected arithmetic approximation \(f\), \(r=Q-f\), and \(\omega=\theta_x\), it retains
\[
R_r=r+\frac{r_{xx}}{\omega^2}-\frac{\omega_xr_x}{\omega^3},\qquad
I_r(t,x)=\int_{999}^{x}e^{-i\theta}\omega R_r\,dy.
\]
Subtracting the complete approximation at the polynomial-coefficient level preserves the correlation between \(r\) and \(r_{xx}\). Signed complex integration then preserves additional cancellation. The complete allowances are:

| Same-source comparison on the pilot | Upper allowance |
| --- | ---: |
| Independent residual endpoints | 0.002011747 |
| Integrated absolute residual defect | 0.000374760 |
| Signed residual increment | 0.000266448 |

The signed allowance is about 13.24% of the independent-endpoint allowance. The further reduction from absolute to signed integration is about 29%. These are meaningful gains with the same source information; the much larger improvement relative to the older 0.827470 disk payment mostly came from obtaining better source data.

The consumer comparison is less dramatic. The paid scalar transport radius rises from more than 1.122848 to more than 1.124460, an increase of about 0.001612, or 0.144%. The same-data direct radius exceeds 1.336516 and remains stronger. Both source-informed transport versions already pass. Thus the correlation has not established transport as the better exclusion method.

The exported oscillator calibration is nevertheless useful: its complete real phase-scaled first-jet error is below 0.000266449, and its physical value/derivative error divided by the local \(\mathcal A\) is below 0.000408734. Its anchor is obtained from complete-source quadrature, rather than known for free. This calibrated error supplies neither a new complex-disk theorem nor a second-derivative bound.

**This is the best lead for new arithmetic understanding:** the actual residual is much closer to a rotating oscillator than separate derivative estimates reveal. The next step must explain and bound that behavior from the analytic arithmetic representation, with its anchor and full remainder costs. Another pilot reconstructed from complete-source data can diagnose a mechanism, but cannot establish an all-height law or a cost advantage. The [internal review][s03-review] supports one focused continuation rather than an expanding scan.

### S04 Time height scaling

The [scaling note][s04-note] advances beyond a fixed-mode heuristic. It retains the growing cutoff, actual arithmetic phases and the amplitude factor \(e^{t\log^2 n/4}\), and differentiates the same scalar model consistently at fixed heat time. For \(L=\kappa/t\), its normalized first-jet replacement error is less than
\[
e^{-\kappa(\kappa+12)/(16t)},\qquad 1\le\kappa\le2,\quad0<t\le1/20.
\]
This added payment is at most about \(9.08\times10^{-6}\) of the stated inherited disk-error upper bound. The comparison is between upper bounds. It does not show that the actual new approximation is more accurate: the new description adds a small error to the old one.

The four point and transition checks have complete scaled-jet lower bounds exceeding approximately 0.4678, 1.1875, 1.1765 and 2.7399. They confirm the implementation at those points. The uniform theorem concerns the replacement error, not a positive lower bound for the signed field throughout the scaling regime.

This is the strongest asymptotic support for S03, but it currently supplies only value and first derivative. **Before using it in a pointwise rotation-defect or Laguerre estimate, pay the second derivative of the same model and the transitions.** Then estimate a signed quantity in the intermediate arithmetic core. The established terminal-edge estimates leave an \(N-o(N)\) core, so simply discarding the edge does not resolve that obligation. The fixed-mode power profile fails as a uniform coefficientwise substitute near the cutoff; this says nothing against every possible signed asymptotic. See the [review][s04-review].

### S05 Covariant theta jets

The [source-enclosure note][s05-note] converts exact parity at the modular fixed point into substantially narrower complete-source interval enclosures. On \([0,1/1024]\), the expanded baseline's radii for \(\Phi,\Phi_u,\Phi_{uu}\) exceed the Taylor radii by factors greater than 894.47, 7.29 and 2394.90. Against a stronger fused Horner baseline, the factors still exceed 694.40, 1.63 and 639.05. All omitted modes and the eighth-derivative Taylor remainder are included.

The useful mechanism is parity-aware complete-source Taylor evaluation; the covariant basis organizes it but is not uniquely responsible for it. The wider complex comparison also exposes a limit: fused Horner improves the second-derivative enclosure on only 30 of 64 shifted cells and widens it on the other 34, by up to about 8.71%.

These are widths of source-coordinate range enclosures, not spectral approximation errors or speedups. The high spectral derivatives in the complete evaluator arise through powers of the integration variable, so the local source improvement does not automatically accelerate that calculation. Even a small absolute source error can be far too large relative to the exponentially small physical field.

**Keep S05 as an available component for a named endpoint or local-source consumer.** Choose that consumer before further optimization and demonstrate a decrease in its complete error or matched total cost. It has lower research priority than S03's signed residual question, despite its larger displayed width ratios. See the [review][s05-review].

### S06 Hodge and transverse geometry

The [opening note][s06-open] derives the actual transverse observation, retaining its boundary term. It proves scoped restrictions on raw vertical insertions, finite constant-coefficient normalized jets of definite reflection parity with ordinary convergent transforms, and positivity preservation by the specified mixed generator. The subsequent [signed continuation][s06-note] adds a genuine auxiliary estimate for \(K=-iG_1\), where \(G_1\) is the complete base-\(p\) observation:
\[
0.37<x^2K(t,x)<0.375\quad\text{on }\mathcal B.
\]
However, the same calculation gives \(K^2>10^{310}E\), with a recorded quotient exceeding \(2.64\times10^{318}\). Its leading lower-endpoint term is on the wrong scale for a small magnitude payment by physical energy. Higher arithmetic precision cannot remove that term.

The exact complete-source compensation is an important structural repair:
\[
C=qg+\tfrac34(D-1)\psi=\tfrac14(9-D)\Phi,
\qquad Z=\frac{9H+i(xH-2tH_x)}4.
\]
It makes the full-line observation convergent and gives
\[
J_c=\operatorname{Im}(\overline Z Z_x)-\tfrac9{16}H^2
=\tfrac{9t}{8}\mathcal L_0.
\]
Consequently its proved pilot bound \(J_c>9tE/800\) transfers the already established \(\mathcal L_0>E/100\). It supplies no independent sign mechanism. The two terms defining the compensated source diverge separately at the negative cusp, so recombination before integration is essential.

The finite-endpoint-subtraction obstruction is also useful: a fixed finite subtraction cannot give the stated polynomial-in-height magnitude payment by \(E\) on an unbounded fixed-time half-line. This does not exclude bounded high-order subtraction, one-sided bounds, or complete source compensation. The [geometric coverage review][geometry-review] additionally distinguishes Poincaré duality, quaternionic actions, twistor structures, and relative winding without treating them as interchangeable positivity arguments.

**Continue only with an independently estimated recombined remainder or mixed source current.** Reusing \(\mathcal L_0\)'s sign to prove the completed current's sign closes the observation bookkeeping, not the arithmetic problem. The [signed review][s06-review] supports keeping this lane conditional on that new input.

### S07 Geometric duality and quaternionic symmetry

The [initial S07 note][s07-initial] consolidates the preceding S06 coverage review; it should not be counted as a second discovery of those identities. The new work is the [zero-form Green and trace note][s07-note]. On its declared bounded tube and line-bundle-valued zero-forms, it derives the polarized Green identity with every boundary face and an explicit dual-test extension.

For that operator the curvature contraction vanishes, although the ambient curvature does not. The canonical theta source has exactly zero full-fiber-averaged self-current on each boundary face. The resulting identity equates two nonnegative bulk energies and gives no positive zero-order term or physical signed margin. The mixed source–test flux remains a separate quantity; zero self-flux does not make it vanish. The raw rough-Laplacian restriction also restores a growing zero mode and fails ordinary positive-time half-line integration.

The trace obstruction is decisive for the specific attempted comparison. Smooth sections can concentrate in the three directions transverse to the physical path while keeping their path value fixed. Their bulk first-order energy tends to zero and all boundary currents vanish. Thus no uniform first-order-energy bound for that path observation exists over the unrestricted smooth-section class.

The concentrating sections destroy canonical theta/PDE data. **The result therefore leaves theta-constrained trace estimates, paid higher regularity, other form degrees, and complete mixed-current estimates open.** Additional regularity could address trace continuity but would not by itself supply a favorable arithmetic sign. S07 is worth retaining as a tightly scoped exploratory option; it should not displace the arithmetic work without a specified new controlling term. See the [review][s07-review].

## Recommended next round and decision gates

The ranking depends on what is being optimized. For immediate reuse, put **S01 and S02 first**. For a new arithmetic explanation, give **S03 the principal bounded research task**, supported by S04. Use S05 when a concrete source bottleneck calls for it. Keep S06 and S07 conditional on an independent physical estimate.

| Work item | Concrete next deliverable | Continue only if |
| --- | --- | --- |
| Consolidate S01 and S02 | Compare the strongest current source/correction methods on the existing pilot and crossing, including Notes 20–22's analytic edge matching. Insert S01's tail payment only in a compatible source-error budget. | A complete error decreases, or matched total cost improves; retain the prior factor-two gate for a performance milestone. |
| Explain the S03 residual | Derive a bound for the recombined residual defect from its complete analytic mode/correction structure, including an executable anchor. | It gives a new quantitative bound beyond independently estimated endpoints on a declared domain, or a specified obstruction explains why that proposed mechanism fails. |
| Transfer toward growing height | Select an explicit domain within S04's regime, pay the second derivative and transitions, and bound the signed intermediate core or S03 defect there. | The bound is uniform over that domain with evaluated constants and full physical return costs; isolated point passes do not satisfy it. |
| Use S05 selectively | Apply the parity-aware source enclosure to one named boundary or local derivative estimate. | That consumer's complete error or accuracy-matched cost improves after setup and spectral-transfer costs. |
| Reopen S06 or S07 | Specify an arithmetic/PDE constraint, completed mixed current, higher-regularity norm, or other form-degree identity and its observation map. | It supplies a physically useful estimate without importing the sign it is supposed to prove; all flux, tail and trace costs are paid. |

S01's \(G_c\)-scaled source errors, S02's disk residual in \(Q\), S03's real phase-scaled jet, and S05's source range widths are different quantities. Their improvement factors cannot be multiplied or compared as if they used the same error norm. Likewise, reducing an already negligible tail need not improve the consumer controlled by a much larger residual or margin loss.

For S03, a further computational pilot should be diagnostic and predeclared. Compare the calibrated approximation with the best direct method using the same complete source data, and include the cost of obtaining its anchor. A small residual alone does not control radial nonvanishing without a paid anchor and drift estimate. A useful uniform analytic estimate is a milestone even before new coverage; another algebraic rewriting of global nonvanishing is not.

## Controls and review evidence

The [result summaries][summaries] and [patterns to avoid][avoid] govern this assessment, especially [collision controls][controls], [theta identities][theta-summary], [geometric realizations][geometry-summary], [target reformulations][a01], [separate absolute bounds][a12], and [scoped exclusions][a07]. Full reflection together with the normalized square expansion selects theta in the stated coefficient class; source selection still does not lower-bound the signed field.

The control distinctions remain necessary. Finite-prime and finite weighted-square controls lack the complete normalized reflection/coefficient data. Reflected smooth and positive-primitive controls can preserve reflection but lack the unchanged theta square expansion. Euler-factor controls change the level-one data; their negative-Laguerre witness is distinct from a double-event enclosure. Polynomial heat events share the generic transport and geometric identities. Auxiliary positive realizations lack the required complete signed physical comparison. The finite-prime and smooth-primitive existence constructions do not supply effective event boxes here.

Fresh source-specific replay again rejected the five supplied event boxes at the strict first-jet and signed interfaces and rejected the separate Euler signed witness. These tests check the acceptance interface using each control's own errors. They neither prove the new analytic estimates nor require rejection on a collision-free control box. S03 additionally retains its exact residual and heat-polynomial tests; S05's parity check and S07's concentration proof address their particular mechanisms.

The reviewed repository baseline is commit `a36d80e4d2c50f747fe5b8bad7e6aab708277dca`. The [review record][review-record] identifies the source set, replay scope, reproduction guides and evidence. Fresh bounded checks covered S01, S02, S03's opening and correlated continuation, S04, S05, S06's source and signed calculations, and S07's geometric and Green algebra. S06's signed calculation was rerun at both 192 and 256 bits; other precision scope is recorded explicitly there. Analytic proofs and imported hypotheses remain distinct from finite computational checks.

Historical source-pin comparisons found later changes to the organizational guide in the S01, S04 and S05 records. Their checked mathematical and executable input pins matched; S02's listed pins matched as well. The historical records have been preserved. Documentary guide drift is not a mathematical-input mismatch, but an old blanket claim that every source byte is unchanged would be inaccurate.

No blocking discrepancy was found in the reviewed claims under their stated hypotheses. The most consequential corrections are interpretive: S02 has not beaten its strongest prior comparator; S03 has not beaten direct exclusion; S04 does not give a uniform signed lower bound; S05 has no paid spectral handoff; and S06's completed sign is inherited. These distinctions determine the research priorities above.

[questions]: ../brainstorm/01_SELF_DUALITY_AND_ADDITIONAL_SYMMETRY_QUESTIONS_20261018.md
[guide]: ../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[baseline]: ../research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md
[global]: ../manuscript/positive_arithmetic_packets/sections/11_global_scope.tex
[s01-note]: 01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[s01-review]: 01_modular_self_duality/reviews/01_PAIRED_ENDPOINT_INTERNAL_REVIEW_20261018.md
[s02-note]: 02_cutoff_reflection/notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md
[old20]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md
[old22]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[polymath]: https://arxiv.org/html/1904.12438v2#S6.SS3
[s03-open]: 03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md
[s03-note]: 03_normalized_jet_rotation/notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md
[s03-review]: 03_normalized_jet_rotation/reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md
[s04-note]: 04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[s04-review]: 04_time_height_scaling/reviews/01_FULL_CUTOFF_SCALING_INTERNAL_REVIEW_20261018.md
[s05-note]: 05_covariant_theta_jets/notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md
[s05-review]: 05_covariant_theta_jets/reviews/01_COMPLETE_SOURCE_ENCLOSURE_INTERNAL_REVIEW_20261018.md
[s06-open]: 06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[s06-note]: 06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md
[s06-review]: 06_hodge_and_transverse_geometry/reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md
[geometry-review]: 06_hodge_and_transverse_geometry/reviews/03_GEOMETRIC_SYMMETRY_COVERAGE_POINCARE_AND_HYPERKAHLER_20261018.md
[s07-initial]: 07_geometric_duality_and_quaternionic_symmetry/notes/01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md
[s07-note]: 07_geometric_duality_and_quaternionic_symmetry/notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md
[s07-review]: 07_geometric_duality_and_quaternionic_symmetry/reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta-summary]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry-summary]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review-record]: numerics/SEVEN_PROGRAM_REVIEW_REPLAY_20261018.json
