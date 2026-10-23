# Zero counts, heat transport, and localized Hodge energy: progress register

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Status: ZHM-01–08 and ZHM-10's specified fixed-disk C² target are complete in their stated scope. ZHM-09 and ZHM-11 remain open; weaker-information and uniform merging-cluster stability remain future questions.** The later ZHM-13 entry completes the declared growing-population cap/late-edge task, while retaining the early physical-boundary gap. This records the analytic results and their integration, not a claim that the original RH or simplicity objective has been achieved. The maintained [manuscript](../manuscript/zero_count_heat_transport/main.tex), [reader guide](../manuscript/zero_count_heat_transport/README.md), [overview](../research-overview/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRAM_20261022.md), [extension note](../notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md), and [internal review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md) contain the supporting statements. The initial reviews were separate same-model checks; the present stability/clock continuation has same-assistant self-review only. Neither is independent specialist review.

The [result index](../../../result-summaries/README.md), [avoid index](../../../avoid/README.md), [controls](../../../result-summaries/12_collision_controls_and_screening.md), [pattern 01](../../../avoid/01_restating_the_target.md), [pattern 12](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [pattern 13](../../../avoid/13_a_factor_is_not_the_target.md) govern the status vocabulary and exclusions.

| ID | Task and completed scope | Status | Main evidence |
|---|---|---|---|
| ZHM-01 | Separate ordinary complex multiplicity, all-real cap counts, real births, complex event residues, and endpoint terms; provide proofs of Hermite splitting and complete wall balance. | Complete, proved in manuscript | [Transport](../manuscript/zero_count_heat_transport/sections/04_zero_transport.tex) |
| ZHM-02 | Prove the exact localized power-energy formula for p>0 and q-fold root-cover energy for every integer q>=1, allowing all finite multiplicities. | Complete, proved in manuscript | [Localized energy](../manuscript/zero_count_heat_transport/sections/02_localized_energy.tex) |
| ZHM-03 | Construct compact divisor regularizations; prove exact mass, field-error allowances, weak convergence, local bias, scoped scalar optimality, and the smooth-kernel comparison. | Complete, proved in manuscript | [Regularization](../manuscript/zero_count_heat_transport/sections/03_regularization.tex) |
| ZHM-04 | Prove normalized root-cover Euler characteristic and distinguish exact and reciprocal differentials, poles, amplitude, and analytic-unit dependence. | Complete, proved in manuscript | [Cover geometry](../manuscript/zero_count_heat_transport/sections/05_cover_geometry.tex) |
| ZHM-05 | Derive finite pair-matrix comparison, complete forced dynamics, centered contraction with residual, and deterministic polynomial Hermite relaxation. | Complete, proved in manuscript | [Pair matrices](../manuscript/zero_count_heat_transport/sections/06_pair_matrices.tex) |
| ZHM-06 | Prove an elementary complete-source first-moment concentration bound, first-K real-root identification, quantitative clock convergence, and cumulative exterior cancellation. | Complete, proved in manuscript; spatial growing windows added, cumulative dynamics fixed-population | [Theta concentration](../manuscript/zero_count_heat_transport/sections/08_theta_concentration.tex) |
| ZHM-07 | State and prove the singular-weight statistical transfer conditions and exact physical cap/closure formulas; retain the distinction between simple roots and vanishing cap phase. | Complete in the declared finite/statistical contracts | [Statistics and caps](../manuscript/zero_count_heat_transport/sections/07_statistics_caps.tex) |
| ZHM-08 | Integrate these proofs into one maintained analytic manuscript with author/LLM provenance, source crosswalk, internal review, and a separately identified supporting numerical appendix. | Complete in manuscript/preparation scope | [Main source](../manuscript/zero_count_heat_transport/main.tex), [review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md), [appendix](../manuscript/zero_count_heat_transport/sections/10_supporting_certificate.tex) |
| ZHM-09 | Bound the complete centered exterior residual from the unchanged source in a useful specified regime, including any growing-rank dependence. | Open | [Further questions](../manuscript/zero_count_heat_transport/sections/09_further_questions.tex) |
| ZHM-10 | Prove harmonic reproduction, C² bias, and direct weighted-divisor stability with full disk, boundary and unit data; calibrate the exponent and compare literature. | Complete for the fixed-geometry contract; broader variants open | [Proof Note 09](../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md), [Proposition 3.5 and Theorem 3.6](../manuscript/zero_count_heat_transport/sections/03_regularization.tex), [self-review](../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) |
| ZHM-11 | Obtain a complete signed physical-boundary estimate stronger than the transport identity on an explicit domain family. | Open | [Statistics and caps](../manuscript/zero_count_heat_transport/sections/07_statistics_caps.tex), [further questions](../manuscript/zero_count_heat_transport/sections/09_further_questions.tex) |
| ZHM-12 | Relate the literal initial angular integral to later births; characterize height boundaries and bound creation events relative to the zero population. | First positive-time and shrinking-layer bounds proved in-note; the full early-layer budget remains open | [Note 11](../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md), [self-review](../reviews/03_INITIAL_CAP_AND_HEIGHT_BOUNDARY_SELF_REVIEW_20261023.md) |
| ZHM-13 | Prove growing-population physical cap and late edge asymptotics, with complete closure accounting; prepare a focused sibling manuscript and assess prior art. | Complete in the stated large-heat and fixed-core contracts; priority and full early-boundary budget open | [Note 12](../notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md), [manuscript](../manuscript/topological_zero_transport/README.md), [review](../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) |

## Quantitative gains and limits

The exact localized count is W_<epsilon=4 pi epsilon N; the q-fold energy is pi q^2 epsilon^(2/q) N. For the compact regularization and p>=1, a field error eta costs at most eta ||Delta psi||_1/(2 pi epsilon). For fixed local geometry and maximum multiplicity M, harmonic reproduction improves the C² regularization upper rate to O(eta^(2/(M+2))). With full disk/boundary/unit data, direct divisor comparison has rate O(eta^min(1,2/m)) per cluster, attained in exponent by exact examples. These contracts and outputs differ; no uniform uncontrolled-collision or algorithmic minimax claim follows.

The normalized pair matrix approaches its clock target with operator error O(K/(L sqrt(kappa))), uniformly over blocks ending by K=o(L sqrt(kappa)). The absolute physical error is O(K L/sqrt(kappa)), vanishing under K=o(sqrt(kappa)/L). The integrated internal pair term is asymptotic to (8A_m/pi^2) T L(T)^2, and the integrated exterior term is its negative minus m(m-1) log L(T)+O(1). This proves cumulative cancellation and E(t)→+infinity. It does **not** prove eventual pointwise E'>0 by differentiating the location estimate; no differentiated saddle result is used in the manuscript's proof.

The exact energy identity admits every multiplicity; the complete cap balance admits the exact heat-double and heat-cubic controls. The inherited broader controls likewise satisfy the generic identities. Their different failures of the canonical source premises remain in the linked register. No favorable theta cap sign, endpoint exclusion, PCC theorem, or growing-population temporal force law is entered as complete. Spatial uniformity is exactly the newly stated window above.

## Verification, numerical support, and continuity

The internal review owns the mathematical audit and document checks; build/preview details belong in that review and the manuscript guide. This register does not convert a successful compile or a finite control check into a proof of a stronger theorem.

The appendix uses only the existing [RHE-04 finite disk](../09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md), with its recorded count two and boundary floor. No new numerical replay or acquisition was performed. Removing the appendix leaves every analytic theorem intact.

The research conversation remains in [home 11's existing archive 0001](../11_late_heat_caps_and_charge_transport/chat-histories/README.md). These base-level records do not change its registration or create a new investigation home. That sentence records the original manuscript conversation. The present continuation is a distinct new chat, uniquely registered as base history 0010. Future work should select ZHM-09, ZHM-11, or a precisely declared stability extension with a concrete quantitative target and a declared control screen; further equivalent restatements alone do not advance their status.

## Original prioritization — 22 October 2026 (completed in the scope below)

Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra, ultra**. The [continuation note](../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md) recommends ZHM-10 first: harmonic cancellation, a C² localization bias, and a direct weighted-divisor perturbation bound with exact exponent controls and a matched-information literature comparison. These candidate estimates remain open. A short growing-clock corollary can be extracted from the existing explicit finite tests; it needs no new concentration estimate for K=o(L sqrt(kappa)), but supplies no temporal-force or PCC theorem. ZHM-09 and ZHM-11 retain their distinct open estimate requirements.

## Fixed-geometry completion and spatial extraction — 22 October 2026

Prepared for Edward Baker with substantial LLM assistance; actual **gpt-6-astra, effort max**. [Note 09](../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) proves harmonic reproduction for every p>0, C² bias with attained factor p/(p+2/m), and the complete-disk estimate C2. Exact monomial, translation, complex, nonconstant-unit, amplitude, boundary and merging controls are recorded analytically. [Note 10](../notes/10_GROWING_CLOCK_WINDOWS_20261022.md) proves Corollary 9.4 with population-independent matrix allowance 128 ζ(3) δ. These replace the open-candidate language of the original prioritization, without changing the original note's historical status.

Proposition 3.5, Theorem 3.6 and Corollary 9.4 are integrated in place. [Self-review](../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) records assumptions, constants, primary-source comparison and build checks. No new numerical certificate or sweep was run. The bounded round is complete; complete exterior forcing (ZHM-09), full signed boundary (ZHM-11), and specialist review remain outstanding. The next substantive estimate must specify its norm and window before execution.

## Initial integral and high-height creation bounds — 23 October 2026

Prepared for Edward Baker with substantial LLM assistance, actual
**gpt-6-astra, effort max**. [Note 11](../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md) proves
I_R(0)=N_T-B-D_0-W+E_0, with the literal initial multiplicity defect
D_0=sum(m-1) and |E_0|<1/2. Its exact event-count consumer accepts lower
bounds on I_R(0) and the signed wall entry, and an upper late count.

Using Polymath Theorem 1.5 and its stronger root-localization proof,
the canonical wall flux on fixed positive times is
W_delta,T(R)=(T-delta)log(R/(4 pi))/16+O(1), of relative order O(1/R).
Moving half-integer phase barriers give at most
O(delta^(-1)exp(A/delta)) later positive-height birth pairs. For
delta_R=A/(alpha log R), 0<alpha<1, the count of all subsequent
positive-height real creation events divided by N_T(R) is
O_alpha(R^(alpha-1)). These are consequences of an imported high-height
theorem; no new saddle estimate or numerical onset is claimed.

The user's accepted first objective includes relative error and event
counts; exclusion is not required for this milestone. The next estimate
concerns 0<t<=delta_R, followed by useful lower bounds on the initial
integral and explicit constants. The physical cap's single product
prod H_z=(-1)^(m(m-1)/2) Delta_P prod U is also recorded with all phase factors,
but no equivalence of real and three-dimensional cap integrals is assumed.
ZHM-11's complete physical signed estimate and ZHM-09 remain open.
The [review](../reviews/03_INITIAL_CAP_AND_HEIGHT_BOUNDARY_SELF_REVIEW_20261023.md) is same-assistant only. The manuscript
is unchanged; this result is currently in the research note.

## Physical topological formula and growing complex caps — 23 October 2026

Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6-astra, effort max**. The user requested a readable paper centered on the physical topological formula, the terminal Vandermonde term, and moving boundaries. [Note 12](../notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md) and the [new maintained sibling](../manuscript/topological_zero_transport/README.md) complete ZHM-13 in its explicit regime; the previous catalogue is preserved.

For K=o(L√κ), a narrow-strip complete-source bound constructs actual complex-time inverse disks and controls the lifted derivative phase uniformly in rank. The new O(m eta) Vandermonde logarithm bound gives a population-linear pair contribution. At fixed imaginary width Y and physical radius r/L, the full cap per root tends to r²Y/pi, supplied at leading order by the analytic factor. On [theta T,T], each imaginary face has flux per root -r²Y log(1/theta)/(4pi L)+o(1/L). Every fixed-projective-radius spatial wall has zero flux. The population is fixed on each rectangle, and may grow between choices of T.

These are joint large-heat/growing-rank results, not fixed-heat high-height estimates. At a fixed event core the shrinking-width imaginary faces each retain Q/2 with an explicit O((B+m)/L²) error; this characterizes flux in terms of Q, and is not an independent event budget. ZHM-11 remains open for a height-controlled complete early boundary and an independently useful initial-cap lower bound. ZHM-12's real early-layer question and ZHM-09's exterior-force task are unchanged.

The [literature/proof review](../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) records substantial classical overlap and seventeen external references. The candidate novelty is the narrower quantitative physical-boundary realization, not a new invariant or zero dynamics. All checks here are same-assistant; the small floating diagnostics are not theta certificates. No specialist validation or priority claim is entered.

## Usefulness assessment before further manuscript revision

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, effort max**. The user's priority is now a demonstrated estimating advantage, preferably a better zero-free region, before further polishing. [Review 05](../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md) records the comparative assessment. ZHM-13 remains complete only in its declared analytic/expository scope; it has established no competitive zero-free-region or cost gain.

For a regular late extension with the same population and projective radius, the exact identity is I_T+E_(a,T)=I_a. Thus late-cap and closing-face bounds should be coupled before estimation. Taking T farther out does not by itself strengthen the complete event balance. The full cap estimate also follows directly from the product of H_z values without using the Vandermonde perturbation lemma. The large-T regime is already all-real by classical results.

The next priority within ZHM-11 is one quantitative bound on the complete difficult signed residual, compared with the strongest direct method using the same source data, scalar winding reductions and correlations. A larger region, lower effective height, materially cheaper certificate, or a meaningfully simpler proof under weaker hypotheses would justify further manuscript development. An improvement at small positive heat time is not automatically a zeta/time-zero region. The current assessment identifies the gap and classical overlap; it does not prove that all coupled topological methods must fail.

The user's clarified test uses a negative-time contour t=-epsilon(h), shrinking with height. [Note 13](../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md) gives I_0=I_epsilon-S_epsilon+Q_- with Q_->=0, so negative-time event exclusion is unnecessary for a lower bound on I_0. The complete connecting flux and curved-cap slope remain payable. The proposed epsilon(h)=c(h)/ell(h)² is a normalization to test, not a proved safe width or analytic gain. The next comparison should estimate I_epsilon-S_epsilon as one quantity and allow the direct comparator the same Gaussian formula. Both manuscripts remain intact.
