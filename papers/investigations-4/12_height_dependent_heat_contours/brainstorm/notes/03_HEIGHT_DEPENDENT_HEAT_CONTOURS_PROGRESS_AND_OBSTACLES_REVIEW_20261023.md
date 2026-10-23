# Height-dependent heat contours: progress and obstacles

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model: **gpt-6-astra (Codex)**; reasoning effort: **max**.

This is a high-level research assessment of the current [manuscript][manuscript], [Overview 02][overview], [Progress 02][snapshot], the [authoritative HDC task register][ledger], and supporting notes and reviews. It is saved in the brainstorm folder at the author's request. The conversation **Review curved contour manuscript** is uniquely registered as [brainstorm history 0002][chat].

The review reads the manuscript source and checks selected underlying derivations, source imports, and recorded computational outcomes. It does not constitute specialist refereeing, a novelty survey, formal verification, or a fresh replay of the numerical certificates. The reviewing model is the same model family recorded for the manuscript. Twenty manuscript/supporting-file, receipt, and script hashes were checked against the [build record][build]; all matched. Hash agreement verifies the checkpoint's identity, not mathematical correctness.

Read with the repository [result index][results] and [patterns to avoid][avoid], especially the [local heat-flow results][geometry], [collision controls][controls], [target-reformulation rule][a01], [coupled-estimate rule][a12], and [scoped-exclusion rule][a07]. This assessment adds no proposed simplicity criterion and changes no HDC task status.

## Overall assessment

The program has developed a coherent finite method connecting the complete theta field to polynomial coefficients and then to a bounded measure of zero clustering. It has also supplied an actual bounded theta certificate, improved the available approximation on the relevant microscopic real-time scale, and identified concrete limitations of the late-time and contour approaches tested so far.

The global arithmetic estimate remains open. The manuscript establishes neither RH implying density-one simplicity, nor RH implying every zero simple, nor RH itself. Its strongest current claim is a collection of finite analytical tools with explicit source requirements, together with a certified example and informative comparisons. The manuscript and latest progress snapshot generally preserve that scope accurately.

The most important distinction for future work is between **acquiring reliable information about a population** and **proving that the acquired population has sufficiently little clustering**. An accurate reference and a nonzero enclosing wall address the first question. They do not answer the second: a perfectly regular outer wall can enclose a multiple zero.

## What has been accomplished

### 1. A quantitative detector of endpoint multiplicity

For a complete finite real population at a common positive time, the inverse-square pair Laplacian is

\[
L=\sum_{i<j}(x_i-x_j)^{-2}(e_i-e_j)(e_i-e_j)^T,
\qquad
q(t)=\operatorname{Tr}\bigl(I-(I+4tL)^{-1}\bigr).
\]

The bounded statistic retains the signature of a multiple endpoint even though the unscaled matrix becomes singular as the descendants meet. The exact endpoint limit is

\[
q(0^+)=\sum_a(m_a-\mathsf H_{m_a}),
\]

where \(m_a\) is the multiplicity at an endpoint site and \(\mathsf H_m\) is the harmonic number. A double contributes \(1/2\); a triple contributes \(7/6\). Under the complete real adjacent-gap law used in the RH-conditional theta application, [Note 10][n10] sharpens the finite transfer to

\[
M_0\le4q(t),
\]

with sharp constant four, where \(M_0\) counts multiplicity labels at nonsimple endpoint sites. Thus \(q<1/2\) excludes every multiple endpoint in the covered population, whereas \(q=o(N)\), with negligible uncovered mass, yields density-one simplicity.

The accompanying two-sided inequalities identify exactly the relevant gap scale: vanishing normalized filter mass is equivalent to a vanishing fraction of adjacent gaps below every fixed multiple of \(\sqrt t\) along the prescribed family. This clarifies what a source estimate must control. The equivalence itself is an interface, not an arithmetic upper bound. The Hermite spectrum is inherited local geometry; the continuation adds the scalar encoding, sharper transfer, and coverage accounting.

[Note 05][n5] retains an alternative earlier-time route: a near-zero upper bound for the pair measure of the real projections of **all** earlier roots, including nonreal conjugates, can imply density-one simplicity under RH. Full pair correlation is stronger than the needed input. This route still lacks its theta statistical estimate and does not require the physical-cap branch to be completed first.

### 2. Finite transport that does not assume internal root separation

The structural center of the manuscript is the connection between [Notes 11 and 12][n11]. A complete isolated population is represented by its monic polynomial \(P\), with the entire field written \(H=UP\). Values on an enclosing zero-free wall retain the effect of exterior roots and the nonvanishing factor \(U\).

The prepared coefficients obey an exact equation driven by wall moments of \(H_{zz}/H\). Its operators are commuting, degree-lowering coefficient shifts. At fixed degree, the backward propagator is therefore a finite polynomial in integrated source moments. Internal collisions do not invalidate this coefficient equation. The reference's failure to satisfy the heat equation and the complete source error are explicitly included in the error formula. See [Note 12][n12].

The forest polynomial

\[
D=\Delta\det(I+aL),\qquad q_a=\frac{a\,\partial_aD}{D}
\]

expresses the scalar filter directly in the complete coefficients. This can avoid isolating each root. Its enclosure preserves the combined residual before taking absolute values and states the required denominator margin. This is a concrete improvement in representation and error accounting, with explicit limits at higher collisions and shrinking heat scales.

[Note 07][n7] also controls the distant exterior contribution with an explicit filtered error of order \(N C_T\log R_c/R_c\) in its stated regime, without an internal-gap or \(1/t\) loss. The nearby coupled contribution remains the unresolved part. This separates a controlled tail from the local expression where new theta information must enter.

### 3. A useful theta approximation on the microscopic real-time scale

[Note 14][n14] retains the complete finite Riemann–Siegel sums and constructs an analytic version of the explicit correction. On the real axis, for bounded \(t\log^2x\), both its normalized field-error allowance and total heat-defect allowance have order \(x^{-3/4}\). The off-axis correction cost, fixed truncation charts, and derivative requirements are explicit.

This is more directly relevant to the proposed small-time application than replacing the field by the much later two-carrier clock model. It is also an actual source approximation, rather than a generic heat identity.

For the source-import check, [Polymath, Theorem 1.3, Corollary 6.4 and Proposition 6.6][polymath] supply real-time approximation bounds and the corrected remainder. Their stated domain is \(0<t\le1/2\), \(x\ge200\), \(0\le y\le1\). Theorem 1.5's clock localization instead has onset \(x\ge\exp(C/t)\). These source statements support the manuscript's distinction between the two regimes; the analytic correction and its heat-defect bookkeeping are the local continuation in Note 14.

### 4. A certified application to the unchanged theta field

[Note 13][n13] supplies complete source and wall data on

\[
\Omega=[26,46]+i[-2,2],\qquad
\tau\in[-10^{-4},10^{-4}]+i[-10^{-4},10^{-4}].
\]

The recorded interval calculation proves a complete count of two roots throughout the time square, a nonzero discriminant throughout it, and a positive lower bound for \(|H|^2+|H_z|^2\) on the entire box. On real time slices the roots are real and simple. It assumes neither RH nor individual root locations. At \(t=10^{-4}\), the enclosed filter is approximately \(4.2163\times10^{-6}\).

This validates a bounded wall-to-coefficient-to-filter acquisition using the actual source. It does not test the unbounded-height arithmetic estimate. Direct terminal evaluation with the same source gives a much tighter filter enclosure: radius about \(2.34\times10^{-18}\), versus \(1.28\times10^{-9}\) for the continuation allowance uniform over the complex time square. Those calculations deliver different coverage; the comparison does not establish a general superiority theorem. For real-time simplicity in this example, direct sign changes plus the shared count are also cheaper.

### 5. Complete contour accounting and useful diagnoses of failed shortcuts

[Notes 02–03][n3] and [Note 08][n8] specify the full physical observable, exterior factor, complements, orientations, and joining faces. They distinguish a common complex-time path from a height-dependent time graph; the latter is generally nonholomorphic and requires slope, orientation, and area corrections. Distinct roots alone also do not guarantee invertibility of the complex spectral resolvent.

The complete negative-time cap identity retains its nonnegative event term:

\[
I_0=I_{-\epsilon}-S_\epsilon+Q_-,\qquad Q_-\ge0.
\]

[Note 15][n15] then encloses all faces on the original box. Both the direct and deformed intervals have negative lower endpoints. Their widths are approximately \(0.000283522\) and \(0.000283934\), respectively, so the deformed implementation demonstrates no gain at the declared 512-leaf budget. This does not prove the cap itself negative. Spatial range overestimation dominates, while complete source errors are already below \(6\times10^{-27}\).

The controls rule out specific shortcuts: dropping the exterior factor, carrying a real-slice positivity assertion unchanged into complex time, discarding complements, or reading exact path independence as an improvement in an estimate. Their scope is important; none excludes every possible theta-specific contour improvement.

## Current obstacles

### The central arithmetic estimate is still missing

With \(r_h\) uncovered labels among \(N_h\) endpoint labels, the finite transfer yields

\[
\frac{M_h}{N_h}\le\frac{r_h}{N_h}+\frac{4q_h(t_h)}{N_h}.
\]

Density-one simplicity therefore needs both \(r_h=o(N_h)\) and an independently proved \(q_h(t_h)=o(N_h)\), including acquisition errors, at times prescribed from the source/height rather than chosen after learning unknown endpoint gaps. Every-zero simplicity needs complete coverage and the stronger unnormalized threshold \(q<1/2\) on covering populations. An averaged bound can leave a sparse exceptional family of doubles.

No present argument supplies these upper estimates. Source positivity, mean zero density, generic repulsive heat dynamics, and a re-expression of the short-gap condition do not distinguish the required theta behavior. An arithmetic estimate must control the actual local clustering, or an independently bounded observable with a proved implication for that clustering. Improving approximation accuracy does not automatically make the reference's own \(q\) small.

### Growing-height acquisition has separate conditioning costs

The microscopic reference still needs a whole-wall lower bound exceeding its error, including the vertical portions. Source derivative errors, population counts, coefficient errors, and the forest denominator/residual margin must all be propagated quantitatively. Fixed source-truncation degree and the number of enclosed roots are different quantities. Covering many blocks requires accounting for their boundaries, exceptional blocks, and omitted multiplicity labels.

Removing inverse-gap denominators from the coefficient equation does not remove all collision sensitivity. For a double birth, a constant coefficient error is measured against the heat scale \(t\); cubic examples require corresponding centered coefficient precision on scales \(t\) and \(t^{3/2}\). A finite polynomial propagator at fixed degree is not a uniform polynomial bound as height, population size, or integrated source moments grow. These are explicit limitations in [Notes 11–12][n11], rather than missing hypotheses that may be ignored.

### Existing late-time information does not close the early-time estimate

There are two different diagnoses. In the published high-height clock regime, the unmodified normalized filter tends to one, rather than zero; [Note 10][n10] proves this using the natural spacing normalization. The proposed microscopic scale is different. Separately, [Note 09][n9] shows that the scalar backward gap estimate with separately bounded errors has amplification satisfying

\[
\log A(t_0,T)\sim\frac{T(\log T)^2}{2\pi^2}
\]

for fixed theta ranks at large heat time. Its available algebraic terminal allowance cannot close that error budget. The unknown actual error is not proved this large. A correlated complete-source residual or a different estimator could behave better, but no useful growing-height bound for that joint amplified error has yet been acquired.

### A curved path must improve an actual complete error budget

The reference has an analytic complex-time extension, but the imported bound for its error against \(H\) is a real-time theorem. Extending the error is a separate task. A complex path also needs the appropriate denominator or resolvent control. A varying-height graph has the extra corrections described above, and joining faces remain part of a multi-band cap estimate.

For exact heat fields, the homogeneous integrated coefficient moments can be obtained from lifted endpoint wall logarithms. Bending the path alone does not add information. A useful contour must improve source error, conditioning, integration cost, or a complete signed estimate enough to pay its additional obligations. The current finite comparisons do not demonstrate such an advantage. The cap pilot identifies a spatial integration bottleneck; simply adding source precision will not address it.

### An eventual RH argument has an additional requirement

The positive-spectrum global simplicity implication uses the complete real-root dynamics supplied by RH. The RH-free contour and coefficient tools are reusable, but a future proof of RH must establish endpoint reality independently. Zero collision mass does not exclude simple nonreal zeros. This is a distinct obstacle from proving simplicity conditional on RH.

## Research priority after this review

The [research reset in Note 16][n16] makes a reasonable distinction between a bounded diagnostic and a global proof task. A single predeclared high-height block on a microscopic clock, for example \(t=\log(x/(4\pi))^{-3}\) with spatial dimensions of order \(1/\log x\), could identify which part of the method fails first. Its ledger should contain the complete normalized wall margin, source error, population count, coefficient errors, forest denominator/residual, the reference filter itself, and an equally informed direct calculation.

Such a calculation would test acquisition and conditioning. It would not establish a limiting simplicity law. The substantive global priority is an independent arithmetic upper estimate for clustering with explicit coverage and exceptional-set losses. A proposed joint small-value estimate for the field and derivative is meaningful only after its implication for root clustering is proved with all interpolation and counting errors included.

Further backward or curved-contour work should be tied to a concrete correlated source estimate that improves the final error or cost. Low-height cap refinement is lower priority for the global objective unless it answers a specified integration question. This conversation launches no new experiment and makes no manuscript or task-ledger edits.

[manuscript]: ../../manuscript/main.tex
[overview]: ../../research-overview/02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md
[snapshot]: ../../research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md
[ledger]: ../../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[build]: ../../manuscript/BUILD_RECORD_20261023.json
[n3]: ../../notes/03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md
[n5]: ../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[n7]: ../../notes/07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md
[n8]: ../../notes/08_CURVED_CONTOUR_TRANSPORT_AND_HEIGHT_GRAPH_20261023.md
[n9]: ../../notes/09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md
[n10]: ../../notes/10_EXACT_COLLISION_SPECTRUM_AND_GLOBAL_REDUCTION_20261023.md
[n11]: ../../notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md
[n12]: ../../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[n13]: ../../notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md
[n14]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[n15]: ../../notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md
[n16]: ../../notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md
[results]: ../../../../../result-summaries/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[polymath]: https://arxiv.org/html/1904.12438v2
[chat]: ../chat-histories/0002_2026-10-23T20-20-56Z_review-curved-contour-manuscript.json
