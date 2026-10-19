# Research program for uniform arithmetic residual control

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**, actual reasoning effort **max**. Internal LLM planning based on the completed research and [Review 15][review]; no specialist human review.

The next program will develop **S03's complete arithmetic residual estimate across changing height and cutoff**, using **S04's uniform scaling analysis** as the first setting. Its purpose is to obtain an independently justified estimate that improves a complete physical collision test or its total acquisition cost. The corresponding [progress document][progress] records execution; writing this program does not begin its mathematical tasks.

This is the current continuation program. The [18 October plan][old-plan], [original tracker][old-tracker] and [geometric alternatives][old-geometry] retain their task IDs, results and historical contracts. The new `UAR-*` IDs below do not reopen completed S01–S07 or GEO-T1 comparisons. The [progress summary][summary] remains the detailed account of findings through 19 October.

## Established starting point

| Input | Result available for reuse | Limitation carried forward |
| --- | --- | --- |
| S03 complete arithmetic residual | On B, with fixed N=8, the complete independent rotating increment is below 0.000854. Finite gamma/heat corrections, coherent RS edge, tails and derivative errors are paid. [Note 07][s03-7] | Fixed pilot only; the source-informed 0.000266448 allowance remains smaller. No complete cost or coverage advantage follows. |
| S03 calibrated consumer | Paid vector radius exceeds 1.3859351576; matched direct radius exceeds 1.3898732635. [Note 05][s03-5] | Stop that fixed-box comparison. Any new comparison must include the same information and propagation. |
| S04 uniform model and average | Full-cutoff model throughout the stated sector; signed intermediate average below 1.5e-6 and complete phase-matched average within 0.11 of one. [Notes 01][s04-1] and [02][s04-2] | Averaged energy permits isolated collisions; neither a chosen nonzero anchor nor pointwise first-jet exclusion follows. |
| S04 local transfer | Complete local residual charts and increment below 46.679 exp(-b*/t). The independent coefficientwise transition-disk rule pays more than .99 exp(1/(4t)) across the sector. [Note 03][s04-3] | The local residual differs from S03's corrected residual. The transition bound is an assigned-budget obstruction, not an actual-jump lower bound. |
| S01, S02 and S05 | Complete error improvements, coherent correction and coupled analytic jets; compatible source acquisition is assessed. | Their existing B comparisons provide no new coverage or demonstrated total cost gain. Reuse the methods when a new consumer needs them. |
| S06, S07 and GEO-T1 | Exact completions, admissible theta-jet space, paid geometric comparisons and validated physical winding. | Tested current and profile estimates lose to direct certification; winding fails its matched cost gate. A new information source or acquisition advantage is required. |

The manuscript's real coverage remains \([1/100,1/5]\times[-1001,1001]\) together with \(\varepsilon\leq t\leq1/2\), \(|x|\geq e^{20/\varepsilon}\). Thus \(1001<|x|<e^{2000}\) is open on the common slab. The required global complex exterior is also open. Neither a local estimate nor success within the sector below is coverage of that whole bridge. See the [manuscript][manuscript] and its summary of the symmetry findings.

## Objects and first domain

Retain the physical field, normalizer and phase of the existing source contract:

\[
H_t=-H_{xx},\quad E=H^2+H_x^2,\quad
Q=H/\mathcal A_t,\quad \omega=\theta_x,\quad
J_Q=(Q,-Q_x/\omega).
\]

The symmetric nonvanishing \(\mathcal A_t\) is not the positive arithmetic carrier. On B, S03 uses \(f=(G_8-\widehat C_8)/\mathcal A_t\) and \(r=Q-f\). For one analytic residual define

\[
Z_r=e^{-i\theta}(r-i r_x/\omega),\qquad
I_r(a,x)=i\{Z_r(x)-Z_r(a)\}.
\]

This exact identity is already available; deriving it again does not meet a new estimating milestone. The quantity to improve is its complete bound, including any transitions between the local approximations.

The initial analytic setting is S04's sector

\[
0<t\leq1/20,\quad 1\leq\kappa\leq2,\quad
L=\kappa/t,\quad x=4\pi e^L,\quad
N=\lfloor\sqrt{e^L+t/16}\rfloor,
\quad b_*=\kappa(\kappa+4)/16.
\]

It begins near \(x=6.097\times10^9\), far from B. UAR-01 must specify the corrected approximation on this sector, its analytic neighborhoods, and overlap conventions. It must also specify the physical interval over which increments will be combined. A one-chart bound and a bound across many cutoff changes are separate deliverables. The fixed-pilot RS profile chart and its 0.000854 constant are inputs for comparison on B only, not assumptions in the sector.

Freeze time and integer cutoff while differentiating each analytic approximation. Across a change of cutoff, retain the entering mode and matching edge correction together. Include the variation of phase and normalization, and any forcing term created by subtracting the approximation from the heat solution. An unproved assertion that the residual satisfies the homogeneous heat equation is not an admissible shortcut.

## Research tasks and decision gates

Priorities indicate order: P0 fixes the core contract and estimating mechanism, P1 supplies the physical application and validation, and P2 is conditional extension. Dependencies mean that the required usable output must exist, even when a predecessor has completed as a failed attempt.

### UAR-00 Program and manuscript integration

**P0; planning deliverable.** Establish this overview and its tracker, integrate a high-level account of the completed symmetry results into the manuscript, and preserve the old task register. Completion records documentation and source verification, with no additional estimating claim.

### UAR-01 Corrected residual and transition contract

**P0; contract complete on 19 October 2026.** See the [reviewed shared contract][uar01] and [new-round summary][round-summary], prepared by **gpt-6.1-sol, actual effort ultra**. This completes definitions/bookkeeping, with no new uniform estimate. Give a single precise definition of the corrected finite approximation, the complete residual and its rotating first jet on the sector. State domains, branches, normalizer, derivative orders and frozen-cutoff disks. Derive the relation between adjacent local models, including the correction required when the cutoff changes.

**Deliverable:** a shared note with a complete error ledger, proposed primary metric, comparison quantities in the same norm and a premise screen for the controls.

**Gate:** every retained, omitted and transition term has a defined source and destination. The contract identifies which new inequality could improve the established local or direct estimate. A renamed S04 residual or endpoint identity alone does not pass. If the proposed approximation cannot be made coherent, record that obstruction before numerical expansion.

### UAR-02 Uniform finite gamma and heat remainder

**P0; requires UAR-01.** Extend the prescribed finite-mode corrections of [S03 Note 06][s03-6] to the growing cutoff with explicit uniform remainders. Retain the full heat weights and phases at modes comparable to N; the fixed-mode limiting formula is not a uniform replacement there. Pay only the derivative orders selected by the consumer, with second derivatives added when the filtered-defect or Laguerre route requires them.

**Deliverable:** a proved complete finite-mode error bound, its dependence on t, L and N, and outward checks of the constants.

**Gate:** the sum of mode errors is controlled on the declared domain without source-H calibration. A bound that is valid but too large may complete this attempt as a scoped loss; it cannot be passed to the physical consumer as a useful estimate.

### UAR-03 Coherent edge and cutoff matching

**P0; requires UAR-01.** Derive the complete RS edge estimate on the same domain, including the gamma prefactor, heat convolution, tails, analytic-continuation discrepancy and any profile-chart changes. Prove how the edge compensates the entering or leaving finite mode.

**Deliverable:** a uniform edge/transition theorem with a common normalization and derivative budget. Any use of Cauchy estimates must be applied to the combined holomorphic error on a proved disk.

**Gate:** the estimate improves upon or avoids the specific independent coefficientwise transition payment in S04-T3. It must not assume cancellation from a center-point observation. If the old divergent payment remains, identify the responsible term and stop that rule. UAR-02 and UAR-03 are separate analytic obligations after UAR-01; neither assumes the other has supplied a bound.

### UAR-04 Combined signed residual increment

**P0; requires usable UAR-02 and UAR-03 outputs.** Recombine the signed finite correction and edge before taking norms or subtracting anchors. Bound the full rotating increment over the interval selected in UAR-01, including every partial prefix and cutoff overlap required by the physical test.

**Deliverable:** an explicit uniform increment theorem or a bounded theorem with a declared domain, together with its dominant-error breakdown and strongest applicable comparator.

**Gate:** a smaller complete allowance or a quantitatively new uniform domain in the same norm. Error gains must survive all transitions and remainder payments. Sampled cancellation, a small center defect or a theorem whose bound merely restates the unavailable physical margin does not pass. The fixed-pilot remainder is only about 1.44% of its reported total budget; more precision there is not the default research action.

### UAR-05 Physical anchor and approximant separation

**P1; requires UAR-01 for an anchor proposal and usable UAR-04 for the complete application.** Establish a nonzero first-jet margin for the corrected approximation or a rigorously selected anchor, and pay its acquisition and propagation errors. S04's signed average may be used only through a proved conversion to the selected physical observation. Average mass alone is not the desired anchor margin.

**Deliverable:** a closed-domain inequality combining the approximant, anchor and complete residual in one physical normalization.

**Gate:** strict positivity after all errors, with exact coverage. Compare the resulting error with direct endpoint certification before launching a large computation. If the anchor is the dominant unresolved term, identify it as the stopping point rather than recording residual success as exclusion.

### UAR-06 Matched complete consumer comparison

**P1; Complete on 19 October 2026 as a scoped losing comparison.** [S03 Note 12][uar06] and its [review][uar06-review] retain the stronger matched direct physical margin with the same dominant acquisition. Stop the exact UAR-05 consumer configuration; UAR-E1/G1 remain conditional. The following contract and gate are retained. Requires UAR-05 and review of its new acceptance input. Compare the complete method with optimized direct certification on a declared closed domain, with matched accuracy and source information. Charge setup, source and anchor acquisition, arithmetic correction, edge preparation, propagation, transitions and validation to the method that uses them.

**Deliverable:** reproducible physical margins and a cost ledger, including cold cost and separately reported reusable preparation.

**Gate:** a stronger paid physical margin, a factor-two total cost improvement at matched accuracy/coverage, or certified new coverage. Passing an already covered box is validation. If the comparison loses, retain the theorem and stop that consumer configuration. Do not choose the older raw direct radius when a stronger matched direct comparator is available.

### UAR-V1 Validation and review for each candidate

**P0; applies whenever UAR-01–06 or UAR-G1 supplies a new estimate or acceptance interface.** Review the analytic premises, source identity, normalization, derivatives, boundaries and full error return. Exercise applicable source-specific collision controls and invalid-input guards. Keep fresh acquisition distinct from a higher-precision evaluation of old data. Review status must identify same-assistant, same-model or cross-model LLM participation; none is specialist human review.

**Gate:** a linked assessment and small source-pinned receipt before promoting the candidate to a usable downstream input. A proof of a scoped failed estimate is also a valid reviewed outcome. An audit that only reproduces the same implementation does not establish implementation independence.

### UAR-E1 Finite extension after an earned advantage

**P2; conditional on UAR-06 and UAR-V1.** Select one tractable uncovered box or one explicitly stronger existing physical test. Keep the initial-zero verification and complex-wall hypotheses appropriate to that domain. This is the new program's possible extension route; the original EXT-01 remains conditional in its own register.

**Gate:** a complete closed-domain certificate or a documented failed extension. A sequence of finite boxes does not establish uniform exhaustion of the real bridge or the complex exterior.

### UAR-G1 Geometric representation with a useful observation bound

**P2; conditional.** Activate only for a specified representation of the actual corrected residual and a candidate estimate that changes the information or dominant acquisition cost. Prove source and error admissibility, all complement and trace payments, and the physical return. Compare first with the appropriate arithmetic bound.

**Gate:** a useful independent physical estimate or a precisely scoped obstruction. Repeating the existing annihilator identity, retuning the unchanged profile norm, or merely projecting onto the five-jet space does not pass. Original S07-T3 stays waiting for a useful estimate; S07-T4 stays deferred. GEO-T1 resumes only for a new, identified source-acquisition bottleneck.

## Controls and comparison discipline

Read the [result summaries][results] and [patterns to avoid][avoid], especially [collision controls][controls], [theta bookkeeping][theta], [target reformulations][a01], [scoped exclusions][a07], [normalization][a08] and [signed recombination][a12]. This program seeks quantitative milestones. It does not introduce another global RH-equivalent criterion.

| Control class | Premise or test that must be addressed |
| --- | --- |
| Finite-prime orbit and weighted-square controls | They do not retain the complete normalized theta reflection and coefficients. Identify the exact arithmetic premise used; no effective finite-prime event height may be invented. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Reflection and shape alone do not give the theta integer-square source. Any broader proposed estimate must be checked on the control's own source and errors. |
| Finite-Euler controls | The normalized coefficients and level change. Retain the certified negative-Laguerre witness as a witness, not as an enclosed double event. |
| Polynomial collision and moving-wall controls | Any general physical acceptance rule must reject a domain containing the event and account for wall flux. Equal endpoint root counts are insufficient. |

The [fresh review receipt][receipt] provides inherited control evidence and replay scope. It does not validate a future changed interface. Controls may pass a collision-free finite box; rejection is required where an event or contradicting witness is actually enclosed. Do not apply theta-specific constants to another source without its proof.

For \(H=\mathcal A(f+r)\), with \(a=\partial_x\log\mathcal A\), keep the physical return explicit:

\[
\delta H=\mathcal A r,\quad
\delta H_x=\mathcal A(r_x+ar),\quad
\delta H_{xx}=\mathcal A\{r_{xx}+2ar_x+(a^2+a_x)r\}.
\]

Source-coordinate widths, disk residuals, rotating first jets and physical Gc errors remain different quantities. Choose the primary metric before computation. Prefer a signed analytic estimate or a bounded feasibility calculation to a parameter sweep. Do not broaden tests after the stated checks pass unless a changed source, failed check or unresolved concern requires it.

## Recording progress

Use the existing S03/S04 lanes for their proofs, `symmetries/notes/` for shared contracts, the corresponding `numerics/` directories for small reproducible records, and `reviews/` for assessments. Record dates, actual model/effort, source identities, status, comparison norm and unresolved terms. Keep the [new progress document][progress] synchronized with completed evidence, and preserve original lane IDs and chronological logs.

Manuscript milestones use the canonical source and a concise `DRAFT_HISTORY.md` entry; no new snapshot folders. Follow [LARGE_FILES.md][large] for generated data and the [chat-history workflow][chat] for each conversation's unique existing registration. A plan creates no scheduled job and does not claim that an executor has begun.

[progress]: ../research-progress/02_UNIFORM_ARITHMETIC_RESIDUAL_PROGRESS_20261019.md
[review]: ../../reviews/15_MANUSCRIPT_AND_SYMMETRY_ACCOMPLISHMENTS_REVIEW_ASTRA_20261019.md
[receipt]: ../../numerics/MANUSCRIPT_SYMMETRY_REVIEW_REPLAY_20261019.json
[summary]: ../summary/01_SYMMETRY_RESEARCH_PROGRESS_SUMMARY_20261019.md
[old-plan]: 01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[old-geometry]: 02_S07_MISSING_ESTIMATES_AND_ALTERNATIVE_APPROACHES_20261018.md
[old-tracker]: ../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[manuscript]: ../../manuscript/README.md
[s03-5]: ../03_normalized_jet_rotation/notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md
[s03-6]: ../03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md
[s03-7]: ../03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md
[s04-1]: ../04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[s04-2]: ../04_time_height_scaling/notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md
[s04-3]: ../04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../../../LARGE_FILES.md
[chat]: ../../../../../tools/CHAT_HISTORY.md


[uar01]: ../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md
[round-summary]: ../summary/02_UNIFORM_ARITHMETIC_RESIDUAL_ROUND_SUMMARY_20261019.md

[uar06]: ../03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[uar06-review]: ../03_normalized_jet_rotation/reviews/12_UAR06_MATCHED_CONSUMER_INTERNAL_REVIEW_20261019.md
