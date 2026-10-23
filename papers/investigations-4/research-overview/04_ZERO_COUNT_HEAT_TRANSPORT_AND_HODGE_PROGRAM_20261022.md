# Zero counts, heat transport, and localized Hodge energy: analytic program

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Status: the finite-domain analytic manuscript and its stated extensions are prepared; the research questions beyond those results remain open.** The maintained manuscript is [Zero Counts, Heat Transport, and Localized Hodge Energy](../manuscript/zero_count_heat_transport/main.tex), with its [reader guide](../manuscript/zero_count_heat_transport/README.md), [internal review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md), [progress register](../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md), and [extension note](../notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md). The initial manuscript had separate-agent same-model checks; the fixed-disk stability and growing-window continuation has same-assistant self-review only; no independent specialist review, mathematical priority, RH proof, or endpoint-simplicity theorem is claimed.

This program follows the [result index](../../../result-summaries/README.md), [avoid index](../../../avoid/README.md), [collision-control register](../../../result-summaries/12_collision_controls_and_screening.md), and patterns [01: reformulations](../../../avoid/01_restating_the_target.md), [12: coupled errors](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [13: a factor is not the target](../../../avoid/13_a_factor_is_not_the_target.md). The exact identities below are accounting results and quantitative finite-domain estimates. They are not independent evidence for an RH-equivalent sign criterion.

## Purpose and surviving mathematical statements

The user's cap-cancellation idea survives as a complete transport identity: ordinary real roots contribute on both regular caps, transported roots cancel, and interior births remain after signed wall crossings are included. Earlier Investigation 2/22 already established that balance. Complex zeros with multiplicity are instead conserved in a proper spatial domain, while the complex-time discriminant counts events. The manuscript proves these distinctions without requiring the reader to consult earlier notes.

The analytic extension connects the ordinary complex count to a localized energy. For a holomorphic f with boundary floor b>0, zero count N including multiplicity, p>0, and 0<epsilon<b,

\[
 \int_{\Omega\cap\{|f|<\epsilon\}}|f'|^2|f|^{p-2}\,dA
       =\frac{2\pi}{p}\epsilon^pN.
\]

Consequently the derivative-weighted energy is exactly 4 pi epsilon N, and the energy of q dw on the normalized cover w^q=f is exactly pi q^2 epsilon^(2/q) N. These are refinements of the holomorphic degree/area formula, valid through every finite multiplicity. The chosen differential and the complete boundary floor are essential.

The compact power potential gives positive divisor measures of exact mass N, explicit field-error allowances, a weak divisor limit, and a local bias bounded using the analytic units at the zeros. Its scalar Lipschitz cost 1/epsilon is optimal only in the declared radial logarithmic-matching class. A smooth logarithmic kernel improves that scalar constant but incurs a paid boundary bias. Neither statement is an algorithmic lower bound or a collision exclusion.

For heat flow H_t=-H_zz, the real birth weight is floor(m/2), whereas the complex event residue is binom(m,2). The normalized root-cover Euler characteristic, reciprocal differential dz/w, exact differential 2 dw, and physical cap phase retain different information. Their formulas explicitly include singular fibers, amplitude dependence, wall crossings, and endpoint indentations.

The inverse-square pair matrix has quantitative finite clock comparisons and exact forced heat dynamics. The elementary canonical theta proof uses every source mode and the whole source half-line. Its finite tests give normalized matrix error O(K/(L sqrt(kappa))) uniformly for blocks ending by K=o(L sqrt(kappa)), where L~(log t)/4 and kappa~8tL. The integrated exterior contribution cancels the leading positive pair contribution, leaving the logarithmic discriminant change. This proof uses a first-moment concentration estimate and does not import the stronger differentiated saddle theorem or differentiate a root-location remainder.

## Completed preparation and remaining research

Tasks ZHM-01–08 in the linked register cover the invariant contract, localized powers and root covers, regularization, cover geometry, pair dynamics, the complete-source theta theorem, statistical/cap scope, and integration into one maintained analytic manuscript. The prior fixed-rank and cap notes remain provenance; the manuscript supplies its essential proofs. No new snapshot directory is created.

The current disposition of the three research questions is:

- **ZHM-09:** obtain a useful bound for the complete centered exterior residual, especially in a specified growing-rank regime. Pair positivity alone does not control that force.
- **ZHM-10:** the [specified fixed-disk C² task](../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) is complete: harmonic reproduction, improved bias and direct weighted-divisor exponent min(1,2/m), with paid boundary/unit constants. Weaker-information and uniformly merging-cluster variants remain separate future questions. The scalar potential optimality is unchanged.
- **ZHM-11:** prove a signed estimate on a fully specified physical boundary, including its cap phase and every closing face, strong enough to improve the event balance.

The generic transport, energy, and matrix identities accept the applicable collision controls. The unchanged canonical source is used for the theta concentration theorem; its late clock conclusion alone is not an arithmetic discriminator. The Euler-factor controls change that source, weighted-square and finite-prime controls fail its complete reflection constraints, and reflected/positive-primitive controls lack the unchanged integer-square expansion. Those differences do not justify assigning a favorable signed boundary estimate to theta without proving it.

## Numerical and archival scope

The main results are analytic. Only the supporting appendix imports [RHE Note 04's existing finite-disk certificate](../09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md); it was **not rerun** for this manuscript. The exact localized-energy value is a consequence of that recorded count and floor, not an independent recertification.

This work stays in the base of **investigations-4**. The original manuscript conversation retains its unique existing home-11 archive **0001**, linked through [that history register](../11_late_heat_caps_and_charge_transport/chat-histories/README.md). No history is moved, copied, or renumbered, and no investigation-5 program is created.

## Original prioritization — 22 October 2026 (completed in the scope below)

Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra, ultra**. The [continuation note](../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md) recommends ZHM-10 first: harmonic cancellation, a C² localization bias, and a direct weighted-divisor perturbation bound with exact exponent controls and a matched-information literature comparison. These candidate estimates remain open. A short growing-clock corollary can be extracted from the existing explicit finite tests; it needs no new concentration estimate for K=o(L sqrt(kappa)), but supplies no temporal-force or PCC theorem. ZHM-09 and ZHM-11 retain their distinct open estimate requirements.

## Completed stability continuation — 22 October 2026

Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra, effort max**. [Note 09](../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) and manuscript Proposition 3.5/Theorem 3.6 settle the fixed-geometry C² question, including attained bias coefficient and sharp exponent controls. [Note 10](../notes/10_GROWING_CLOCK_WINDOWS_20261022.md) and Corollary 9.4 extract growing spatial clock windows directly from the existing first-moment estimate, with a smaller sufficient window for vanishing absolute physical-matrix error. No time-varying-population balance is inferred.

The [self-review](../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) separates classical inputs, proved estimates and unproved extensions. This is a useful explicit specialization of classical trace/root-perturbation methods, without a priority claim. The continuation's distinct chat is base archive 0010; all earlier registrations remain unchanged. The next source/cap work must retain the full exterior force and every closing face. A specialist assessment of the compact core is recommended before broader expansion; no reviewer has been contacted.

## Initial integrals and creation counts at increasing height

23 October 2026, for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort max**. The user has selected a compact initial-cap
balance and characterization of its extra contributions as the next
direction. Relative boundary estimates and upper bounds on creation
events are useful first milestones, to be refined later. [Note 11](../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md)
supplies the literal real initial-cap identity, a separate physical-cap
product formula, and canonical bounds away from a shrinking initial time
layer. The sole [progress register](../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md)
records the completed first bounds and the outstanding early-layer task.
This increasing-height limit is distinct from large heat time. The
complete physical Chern–Hopf closure estimate remains a separate task.

## Focused physical transport paper and the next boundary estimate

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, effort max**. The user has selected a separate readable manuscript centered on the complete physical topological formula. [Topological Zero Transport and the Phase of the Discriminant](../manuscript/topological_zero_transport/README.md) now gives the growing-population complex-time cap, its Vandermonde/analytic-factor decomposition, zero moving projective side flux, and O(1/log T) late imaginary-face flux per root. [Note 12](../notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md) and [Review 04](../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) supply incremental provenance and primary-source comparisons. The prior catalogue remains separate and unchanged.

The late bounds are uniform for K=o(L√κ) as heat time grows. A fixed event core retains nonzero closure charge; its constants have not been controlled uniformly in height. The next analytic objective is therefore an independently bounded complete early attachment/imaginary-time contribution, together with a useful lower bound for the fixed initial cap. Relative estimates and event-count uppers remain acceptable first targets. The sole progress register records this as completed ZHM-13 with ZHM-11 still open; no new invariant, RH result or verified novelty is claimed.
