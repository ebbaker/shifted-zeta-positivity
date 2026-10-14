# Manuscript rewrite integration review

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**, as
verified from the parent turn configuration. This is an internal LLM
review, not external specialist refereeing or formal verification.

## Delivered version and outcome

The author requested a fresh exposition and an explicit backup. The
[source](../manuscript/quaternion_theta_geometry.tex) is now titled
**Uniform Laguerre signs and hypercomplex jets of the theta heat flow**.
The [export](../../../../../output/pdf/quaternion_theta_geometry.pdf) has
24 pages. The previous 35-page source, PDF, and build record were copied
and hash-verified before replacement; see the
[backup receipt](../manuscript/BACKUP_RECORD_20261014.json).

- Final source: 72,475 bytes, SHA-256
  `6242fd49c4d1c8f08efbfa798ef5f1ac66544999e11e1426af43418950971e12`.
- Final PDF: 489,116 bytes, SHA-256
  `3999525f5fedd9508881e9bd28b65bbf9529fe425b274d66c93c8f3149746b3e`.

The focused reviewer found no substantive mathematical defect in the
sections independently reviewed. Three transcription/notation issues
and one symbol conflict were resolved before final compilation. Root
checked integration of the collision/certificate sections and the final
source and export. The collision/certificate author did not independently
review their own sections. The review statement below preserves that
scope. Existing source-note Reviews 10–12 remain relevant; prior numerical
replays are retained in Reviews 6, 9, and 11.

## Current build and replay checks

The saved final source passed the desktop LaTeX compiler. The stabilized
terminal export has no warnings. A source audit found 118 unique labels,
six bibliography entries, no missing references/citations, and no invalid
control characters. All 24 pages were inspected in contact sheets;
individual inspections of pages 3, 5, 11, 15, 18, and 23 checked the main
theorem, uniform proof, octonion formulas, residual identities, certificate
table, and reproducibility text. No clipping or layout defect was found.

Fresh exact checks all passed:

| Check | Count | Scope |
| --- | ---: | --- |
| Higher-height record auditor | 6682 | Exact retained endpoints, coverage, signs, norm floors, source bindings |
| Centered-band record auditor | 547 | Exact 32-cell cover, cone, stationary decisions, endpoints, source bindings |
| Octonion jet checker | 248 | Exact polynomial/algebraic identities under the declared conventions |
| Centered-residual checker | 9 | Exact stationary-ideal and balanced-evolution identities |

The [current check receipt](../numerics/MANUSCRIPT_REWRITE_CHECKS_20261014.json)
records input/source hashes and the final manuscript identity. No full
interval-quadrature certificate was rerun for this editorial rewrite.
The compact audits complement earlier numerical replays and the written
source estimates; they do not formalize those analytic estimates.
The final bibliography's Sudbery title, volume, year, page range, and DOI
were additionally checked against the
[Cambridge primary publication record](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/quaternionic-analysis/308CF454034EC347D4D17D1F829F8471).

The [continuation](../notes/18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md)
records what was condensed, what remains open, and the next precise
analytic and quantitative targets. No all-height sign or RH conclusion
has been added.

---

## Focused independent review of the assembled rewrite

14 October 2026. Prepared for Edward Baker with gpt-6-astra, reasoning effort ultra, as verified by the parent turn. This reviewer authored the collision and bounded-certificate fragments; the main outer proof, hypercomplex section, centered-residual section, obstruction discussion, and source-payment appendix were independently reviewed here. This is an internal analytic review, not external specialist refereeing or formal verification.

### Assessment

No substantive mathematical defect was found in the assembled outer theorem or its proof, the octonionic extension and signed associators, the residual identities, or the declared finite/global scope. Three local transcription/notation corrections and one symbol cleanup were identified, communicated, and verified as corrected in the parent’s updated assembly. The distinction between proved outer positivity, closed finite coverage, and the unresolved inner region is maintained.

The reviewed source is `/tmp/inv21-rewrite/quaternion_theta_geometry.tex`, approximately 1796 lines at first inspection. Root is editing/building it concurrently, so this report identifies exact expressions and labels rather than treating transient line numbers as a frozen release identity. No repository files were changed and no lengthy numerical certificates were rerun.

### Local corrections identified and resolved

1. In the hypercomplex physical-zero paragraph immediately after `eq:hc-observations`, replace “`H_t` has a multiple real zero” with “`H(t,\cdot)` has a multiple real zero.” Elsewhere the manuscript uses `H_t` for the time derivative, so the present wording would assert a different and false equivalence under that convention.
2. Immediately before `eq:C-stationary`, replace the malformed factor `-2a,i(u+ia)` with `-2a\,i(u+ia)`. The intended exact polynomial identity and all subsequent formulas have the correct sign.
3. In the adaptive-payment proof after `eq:adaptive-payments`, replace `e^{-a_xx}=e,e^{-\pi x/8}` with `e^{-a_xx}=e\,e^{-\pi x/8}`.

Recommended notation cleanup: the scalar holomorphic model `\mathcal A_t(z)=Q_+(z)+Q_-(z)` and the later octonionic time associator `\mathcal A_t=[F\ii,F_t\kk,\ell]` reuse the same symbol. Their contexts distinguish them, so this does not invalidate a proof, but renaming one avoids ambiguity in a manuscript whose point is to connect analytic and geometric objects.

**Resolution verified:** the updated assembly uses `H(t,\cdot)` in the collision paragraph, correct thin-space multiplication in both identities, and `\mathcal P_t` for the scalar analytic model throughout its proof. Its SHA-256 at this follow-up inspection was `6242fd49c4d1c8f08efbfa798ef5f1ac66544999e11e1426af43418950971e12`. Later formatting changes may legitimately produce another final hash.

### Main theorem and proof

The source normalization, definition of `M_0`, logarithmic derivative `alpha`, both arithmetic exponents, and all three imported error terms agree with the primary [Polymath Theorem 1.3 and equations (20)–(24)](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3), opened directly during this review. The finite approximation is used for values only.

The key uniform step survives the rewrite: after allowing theta to grow, the weighted-zeta discrepancy is controlled by `(theta_0+r)2^{-r/8}/L`, uniformly for `r>=0`. Thus the conclusion is not merely a fixed-time or fixed-theta limit. The ordinary zeta tail and imported errors are smaller. The analytic model replaces the moving cutoff before Cauchy differentiation, and Schwarz symmetry supplies the lower half of the shrinking disc. Radius `1/L` keeps the gamma amplitudes comparable by constants; no unjustified fixed-radius comparison occurs.

Nonvanishing of the common amplitude uses the independent zero-free Dirichlet-series half-plane `Re w>=5/4`, rather than a physical norm assumption. Differentiation with time held fixed gives the four common-phase jet components and errors of the claimed orders. Expanding the two quadratic forms gives leading value one uniformly in phase, including near component zeros. The explicit lower bounds `1-4delta-delta^2` and `1-4delta` and the values at `delta=1/8` are correct.

The constant four is correctly identified as a sufficient summability threshold. The theorem does not assert optimality, epsilon-zero boundary control, an evaluated height cutoff, or an RH conclusion. The limsup collision localization follows with the stated quantifiers.

### Hypercomplex section

The declared quaternion coefficient placement, Fueter operator, complex time displacement and coordinate derivatives are consistent. The lift is globally real analytic because the scalar family is jointly entire.

For the octonion convention, left multiplication by `(e_mu,0)` and `(0,e_mu)` gives exactly the displayed split operator. The correction `-G_(m+3) conjugate(r)/2` cancels the second-component defect `2G_(m+3)`; associativity is used only in the quaternion components. The extension really is eight-dimensional and uses higher jets, as the text explicitly notes. It imposes no extra condition on the original pair. The physical trace lies in an associative quaternion subalgebra, and its total octonionic norm cannot detect the distinguished first-pair collision.

The twisted commutators give the stated factors and orientations of the energy, stationary, and time associators. The ray condition is a scalar signed inequality, not an order on octonions. Its bounded-loss version has the correct factor `E_t+2KE`.

The positive entire-source control is valid: quartic decay dominates every compact complex `(t,z,epsilon)` parameter set in the transformed representation. The normalization gives the claimed two-frequency limit, whose collision Jacobian is nonzero. The analytic transform, not the density containing `epsilon^{-1}`, extends through epsilon zero. A positive-time double zero persists for sufficiently small positive epsilon and violates locally bounded stationary loss. The manuscript states precisely that scope.

### Residuals, common carrier, and source payments

The complete-source contour shift correctly removes the vertical edge only after summing the even theta source. The centered residual, both sum-of-squares identities, one-sided paid residual estimate, and variable-parameter term in the balanced metric are algebraically correct. In particular the previously corrected first SOS retains its extra `eta/2` coefficient.

The index translation, staircase domain, logarithmic weights, common carrier majorant and centered multiplier are consistent. The fixed-cusp absolute first-channel obstruction concerns a pointwise carrier sum only. The phase-projection diagnostics and staircase cancellation are described with their appropriate integrand scope; they are not substituted for signs after integration.

The index/integration tail bounds retain all omitted indices and the whole half-line. The majorant ratios, tangent bounds, centered degree-two replacement and adaptive choices give the stated absolute error scales. Their limitations relative to physical norm and sign are explicit.

### Intro, certificate, and conclusion consistency

The introductory all-positive-time collision equivalence is supported by the later Hermite argument: RH excludes a multiple zero at any positive time; the converse already needs only the interval `(0,1/2]`. The bounded certificate covers the entire closed rectangle through height104, includes both time endpoints and all spatial boundaries, and is joined to the central proof by overlap and evenness.

The height100 rational norm floor and height104 floor safely imply the common `1e-16` bound. The residual cone's second-level bounded loss is explicitly distinguished from that band's separately certified strict second stationary sign. Existing replay records and exact auditors provide provenance; they are not represented as an all-height or formal proof.

The remaining domain and one-sided target preserve local boundedness through each candidate positive-time joint zero, allow growth towards time zero, and do not define the loss by an uncontrolled energy quotient. Evaluating an outer cutoff and proving the inner signed estimate remain open. Previous authoritative internal Reviews10–12 are consistent with this assembled exposition.

### Limits of this review

Root owns compilation, reference checks, visual inspection, and final release hashes. The collision/certificate fragments were checked for integration consistency, not represented as independently reviewed by their author. Existing exact algebra and numerical records were inspected through their derivations and prior independent reviews; no claim of a fresh full replay is made.
