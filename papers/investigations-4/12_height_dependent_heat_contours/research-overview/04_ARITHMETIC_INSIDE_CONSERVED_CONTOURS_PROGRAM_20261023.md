# Arithmetic inside conserved heat contours toward simple zeta zeros

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is the current research continuation after the fixed-offset theorem and the author-directed book rewrite. [Internal scope review](../brainstorm/reviews/11_POST_CONTOUR_RESEARCH_PROGRAM_REVIEW_20261023.md).

The overarching objective is to get as close as the mathematics permits to **RH implies simple zeros**, using the actual theta field and allowing arbitrary multiplicities in the RH hypothesis. The outer contour is now proved. The next substantive advance must restrict the possible multiplicities inside it, or supply a quantitative arithmetic estimate with a clear role in such a restriction. The observable, scale and final theorem remain flexible: an individual-zero result, an exceptional-count estimate, a stronger proportion or a useful intermediate theorem should emerge from the strongest argument obtained.

The [new progress register](../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) tracks this continuation. The existing [SIMP register](../brainstorm/research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md) and [SCF register](../brainstorm/research-progress/03_CONSERVED_SPATIAL_CONTOURS_PROGRESS_20261023.md) retain ownership of their goal IDs and historical completion evidence. This overview replaces the earlier contour-acquisition plan as the starting point for new work; it does not reopen the completed fixed-offset proof or close the open simplicity goals.

## The acquired analytic starting point

Write F(z)=H(0,z)=xi(1/2+iz/2)/8, p=F'/F and L=log Y, with H_t=-H_zz. Under RH, with multiplicities allowed, [Note 18](../brainstorm/notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md) proves, at fixed positive spatial offsets and for every fixed c>0,

\[
\frac{H(-s,z)}{F(z)e^{sp(z)^2}}
 =1+s p'(z)(1+2sp(z)^2)+O(L^{-2}),
 \qquad 0\le s\le cL^{-2}.
\]

The proof includes the complete Gaussian tail relative to the small initial field, fixed-order spatial derivative bounds on smaller strips, and an acquired nonvanishing floor. It yields an actual finite-buffer material graph, with displacement and tangent change O(L^-1), horizontal coverage and upward motion as backward duration increases. It preserves H dz and the primitive image. The theorem concerns real heat time and fixed offsets bounded away from zero; a shrinking-offset or complex-time extension needs a new proof.

The [book](../manuscript/book.tex), *Conserved heat contours toward simple zeta zeros*, now contains this full proof. Its Corollary 5.4 places the upper and lower transitions of a smooth window in the acquired zero-free corridor. For S=c/L^2 and a window covering [Y,2Y], define the complete resource

\[
\mathcal R_Y=N_{\psi_Y,\mathrm{nr}}(-S)
                  +\mathcal F^+_{\mathrm{ends},\mathrm{nr}}.
\]

The exact collision balance gives M_Y <= 3R_Y/2, where M_Y counts labels at nonsimple endpoint sites. The upper and lower transition contributions vanish, but the earlier interior nonreal population and the one-sided horizontal-end influx remain. Neither term, nor their sum, has a useful upper bound at this stage. A fixed wall inside the same zero-free corridor gives the same removal of those transition terms; material conservation alone adds no simplicity estimate. See [Note 20](../brainstorm/notes/20_THEOREM_CENTERED_BOOK_REVISION_20261023.md), [Review 09](../brainstorm/reviews/09_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_REVIEW_20261023.md) and [Review 10](../brainstorm/reviews/10_THEOREM_CENTERED_BOOK_REVIEW_20261023.md).

## The arithmetic distinction still needed

The control

\[
G_0(z)=F(z/2)^2\left[1+\cos\!\left(\frac{\log2}{4}z\right)\right]
\]

has only even-multiplicity real zeros under RH. It has a positive even superexponentially decaying Fourier source, the same two leading zero-count terms, and all the coarse logarithmic and fixed-offset Gaussian bounds used above. Those shared bounds cannot give a positive simple-zero proportion. The exact canonical theta source is absent from this control, but merely naming that absent identity does not show that a proposed inequality uses it effectively.

For every proposed multiplicity-restricting estimate, identify the arithmetic step that changes the bound, and test the inequalities actually consumed by the proof on G_0. If a supporting bound also holds for G_0, record what it pays and what discrimination is still missing. Apply the other [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) when they meet the proposed hypotheses; state each failed premise rather than treating a control outside the hypothesis class as a refutation.

## Two live approaches

**Estimate the complete nonreal resource.** Start from the full-field population and current formulas in book Section 6.1 and Appendix A. Seek an arithmetic bound on R_Y that can be passed to the collision balance. Separate small estimates for its two terms are not mandatory: a coupled argument for the sum, or a sharper compatible observable, may be stronger. A small boundary flux without earlier-mass control is insufficient. Use complete theta/xi information; retain source tails, carrier derivatives, localization and small-value denominators through the estimate. A chosen reference must earn its floor and approximation error.

**Develop a near-axis comparison retaining the cluster.** At an offset comparable to 1/log Y, an allowed double already invalidates the naive extension of the fixed-offset formula. A useful comparison must keep the actual local zero or cluster factor and control its interaction with the remaining analytic factor and the complete source. It must allow the multiple zero being investigated, rather than assume a floor that excludes it. A successful near-axis method may lead to a better observable than R_Y; it need not return to the present resource route.

The first approach uses the completed outer wall most directly. The second remains available whenever its arithmetic is more tractable. The positive-time spectral or joint consumer in [Note 12](../brainstorm/notes/12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md), or another genuinely different observable, can be reconsidered if it offers a stronger complete estimate. No route is retained merely to preserve the current manuscript structure.

## The next analytic round

Choose one concrete estimate from the two approaches and work it through. Specify its normalization, height/time/offset range, actual arithmetic input and intended consequence before estimating. Then retain the full coupled quantity, bound the relevant errors, and compare the result with a direct estimate using the same information. The available S=c/L^2 window is a starting input, not a mandatory law for all future work; any different scale must have its own analytic justification.

A successful round proves an applicable quantitative improvement of a named bottleneck, with its contribution to the multiplicity argument explicit. An exact representation, another fixed-offset correction, or a conditional criterion without an acquired estimate does not complete that task. If the attempted bounds remain unchanged on G_0, isolate the information class responsible and redirect. A scoped obstruction is useful research evidence, but does not complete the positive arithmetic goal. No numerical campaign is required by this plan; computations should answer a named analytic uncertainty and have a possible failure outcome.

## From an estimate to the strongest conclusion

For N_Y the total endpoint multiplicity, R_Y<=alpha N_Y gives at least (1-3alpha/2)N_Y simple zeros in the covered band. R_Y=o(N_Y) gives density-one simplicity on those bands. An individual-site window with resource below two excludes a multiple zero there. These conversions are already proved; none is an acquired bound on R_Y. A better consumer is welcome if the arithmetic supports it. Compare any resulting proportion or exceptional-count theorem with the relevant verified literature before claiming an advance.

Transfer must pay the exact obligations of the selected route: moving domains and endpoint coverage, source and carrier errors, small-value behavior, localization, and any limit interchanges. The field formulas take rho to zero before delta; their fixed-window validity is not a uniform high-height theorem. Material velocity H_z/H and root velocity H_zz/H_z are distinct. Signed transport does not control repeated one-sided inward crossings. Cumulative or every-zero conclusions need the corresponding height coverage and treatment of exceptional ranges.

## Research records and manuscript development

Follow the [result index](../../../../result-summaries/README.md), [local heat-geometry summary](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), [shared-premise screening](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [coupled-estimate discipline](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). A reformulation is labeled as such; a substantive intermediate estimate is judged by its proved gain.

Save derivations in notes, assessments in reviews and supporting calculations in numerics. Track relevant articles and precise import scope in the [reference catalog](../references/README.md). Promote a substantive advance into the book with its full proof and honest scope. The author's book-specific preference is to retain dated standalone TeX drafts alongside Git history; the [manuscript guide](../manuscript/README.md) indexes the preserved versions. Planning alone does not require another manuscript rewrite or draft.

This conversation retains [history 0008](../brainstorm/chat-histories/0008_2026-10-24T00-32-16Z_continue-contour-conservation-study.json), **Continue contour conservation study**. The [verification receipt](../brainstorm/chat-histories/VERIFICATION_POST_CONTOUR_PROGRAM_20261023.json) records the source and integrity checks at its snapshot. Later refreshes legitimately change counts and hashes. Follow the [chat-history workflow](../../../../tools/CHAT_HISTORY.md) at the beginning and end of each reply, preserving the existing identity and using bounded exact-turn capture until native completion capture is verified.
