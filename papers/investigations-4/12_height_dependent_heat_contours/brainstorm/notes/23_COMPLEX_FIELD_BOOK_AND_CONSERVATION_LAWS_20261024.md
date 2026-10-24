# Complex-field book rewrite and conservation laws

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**. Same-assistant analytic derivation and self-review; no independent specialist review or novelty claim.

## Author instruction and preserved version

The author requested an exclusive rewrite of the book around the complex-field results in [Note 22](22_COMPLEX_ZERO_FIELDS_AND_CONSTRAINED_OPERATOR_TOOLS_20261024.md), an exact new draft preserving the current book, emphasis on analytic calculations, and identification of conserved quantities.

The former book was copied byte-for-byte to [draft 03](../../manuscript/drafts/book_draft_20261024_03_conserved_contours.tex) before editing. Its size is 47,699 bytes and SHA-256 is `b460b60387ff6446418b9f7ada92ee00700f56ff359a63948b7f274f6b5e054e`; the [preservation receipt](../../manuscript/BOOK_PRE_FIELD_DRAFT_RECEIPT_20261024.json) records the authorization and identity. No snapshot folder was created.

The maintained [book](../../manuscript/book.tex) is now *Complex zero fields and conserved heat evolution*. Its proofs concern the smooth amplitude, zero-density limit, phase motion, Schrödinger–Poisson/DS-II equations, conservation laws, normalization and multiplicity observable. The former fixed-offset contour proof and resource exposition remain in the preserved draft and existing research sources. The broader main.tex was not edited.

## Classification and reading anchors

These are exact generic field identities, conditional conservation theorems, a classical area/Picard classification, and finite-divisor observable calculations. They supply no new theta-specific multiplicity upper bound, simplicity proportion or RH implication. This is the author-requested manuscript milestone, not completion of the existing SIMP, SCF, OBF or HDC research goals.

Consult the [result index](../../../../../result-summaries/README.md), [local heat geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md); and the [avoid index](../../../../../avoid/README.md), particularly [target restatements](../../../../../avoid/01_restating_the_target.md), [lifts](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [normalization slips](../../../../../avoid/08_normalization_and_constant_slips.md) and [unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## Analytic additions beyond Note 22

Write \(\rho=|A|^2\), with the amplitude and real potential defined in Note 22. Select the potential by the bounded selfadjoint Fourier multiplier

\[
\widehat{\mathcal T f}(k)=-8\pi\frac{k_xk_y}{|k|^2}\widehat f(k),
\qquad V=\mathcal T\rho.
\]

For smooth solutions with the stated integrability and vanishing boundary terms, the book proves conservation of

\[
M=\int\rho,\qquad P_i=\int\Im(\bar A A_i),\qquad
\mathcal E=\int\Re(\overline{A_x}A_y)+\frac12\int\rho\mathcal T\rho.
\]

The mixed kinetic operator and Hamiltonian are indefinite. The factor one-half in the potential energy is necessary because the potential evolves with the density. The proof differentiates the functionals explicitly; it does not infer conservation from a quantum analogy.

With sufficient moments, \(C_x=\int x\rho\), \(C_y=\int y\rho\), \(\mathcal D=\int(xp_x+yp_y)\) and \(\mathcal B=\int xy\rho\) obey

\[
\dot C_x=P_y,\quad\dot C_y=P_x,\quad
\dot{\mathcal B}=\mathcal D,\quad\dot{\mathcal D}=2\mathcal E.
\]

Thus \(C_x-tP_y\), \(C_y-tP_x\), \(\mathcal D-2t\mathcal E\), and \(\mathcal B-t\mathcal D+t^2\mathcal E\) are conserved. The virial is a signed mixed moment, not a positive variance. Adding a real external/harmonic potential \(W\) gives \(\dot P_i=-\int\rho W_i\) and \(d(\mathcal E+\int W\rho)/dt=\int W_t\rho\), with the integrability assumptions retained.

The holomorphic lift also satisfies
\(\partial_t[g(H)\rho]+\nabla\cdot[g(H)\mathbf j]=0\) for each fixed smooth target weight \(g\). These local conservation laws retain \(H\) as well as \(A\); they are not claimed for arbitrary solutions of the larger DS-II equation.

### The normalization question is now resolved for this amplitude

The new mass theorem is

\[
\int_{\mathbb C}|A_\epsilon|^2=
\begin{cases}
\deg H,&H\text{ a nonconstant polynomial},\\
\infty,&H\text{ transcendental entire}.
\end{cases}
\]

The proof is the area formula with target weight \(k_\epsilon\), followed by Great Picard at infinity. Almost every value of a transcendental entire function has infinitely many preimages. The canonical theta heat slice is transcendental because it tends to zero on the real axis while remaining positive at zero. Therefore its mass is infinite for **every fixed positive regulator and every real heat time**. This answers the uncertainty retained in Note 22; that note and its hash-bound historical receipt are unchanged.

This excludes a global constant normalization of this specific amplitude. It does not exclude spatial weighting or fixed-window normalization. The book retains all cutoff flux and normalization terms. Infinite mass alone does not prove that every other signed global quantity diverges; no finite theta energy or momentum theorem is claimed.

### Polynomial charges give an explicit control

For degree \(n\), the area formula and the first two Newton sums give

\[
\int z\rho=-a_{n-1}/a_n,\qquad
\int z^2\rho=(a_{n-1}/a_n)^2-2a_{n-2}/a_n\quad(n\ge2).
\]

Since \(\dot a_{n-2}=-n(n-1)a_n\), the second moment has real derivative \(2n(n-1)\). The conservation and virial calculations then give
\(P_x=P_y=\mathcal E=0\) and the restricted angular moment \(L=n(n-1)\). The angular moment is not claimed conserved for general DS-II solutions. The degree-one case has a divergent second absolute spatial moment and is handled separately by its radial stationary profile.

The exact field \(H=z^2-2t\) has global norm squared two, both momenta zero, Hamiltonian zero and angular moment two throughout a double collision. Thus finite normalization, smoothness and these invariants cannot themselves exclude multiplicity.

### The multiplicity observable has a resolution cost and a transport law

For a finite divisor, the self-subtracted Gaussian density square satisfies the identity and small-scale limit of Note 22. The book now adds:

- An exponential bound for the off-diagonal contribution when the distinct support points have a specified separation.
- For equal-mass measures of mass \(N>0\), the analytic comparison
  \(|Q_s(\mu)-Q_s(\nu)|\le N e^{-1/2}s^{-1/2}W_1(\mu,\nu)\), and an explicit extra mass-error term when the masses differ.
- The exact track derivative and a field-level transport formula retaining fixed-window flux. For \(z^2-2t\), \(Q_s(t)=2e^{-|t|/s}\): it is not conserved or universally monotone.
- The order of regulator and spatial-scale limits. Reversing them gives the negative regularized mass rather than multiplicity excess.

The missing task is a useful bound using the unchanged theta source, including the scale, localization, regulator and height costs. Neither the Lipschitz comparison nor conservation supplies that bound.

## Control screen and source scope

Every holomorphic collision control in Summary 12 passes the local field identities and admits compact localization. The Euler-factor, weighted-square, reflected super-Gaussian, smooth positive-primitive, finite-prime/profile and close-source controls therefore fail no generic local premise. Transcendental controls fail finite **global** mass, as does theta; this hypothesis does not distinguish theta. The polynomial control satisfies the global assumptions and still collides. The complete normalized theta arithmetic, absent from these changed-source controls, is not used in the generic conservation proofs.

The DS-II convention is the previously checked Klein–Stoilov equation (1); Taimanov remains related prior-art context only. The new imported theorem statement is [DLMF 1.10(iii), Picard and classification at infinity](https://dlmf.nist.gov/1.10#iii), recorded in the investigation [reference catalog](../../references/README.md). No global DS-II existence or scattering theorem was imported.

## Verification and continuation

The [self-review](../reviews/13_COMPLEX_FIELD_BOOK_SELF_REVIEW_20261024.md) records the proof audit and limits. The new [checker](../numerics/18_check_field_conservation.py) and [execution record](../numerics/18_FIELD_CONSERVATION_CHECKS_20261024.json) verify local momentum and continuity balances, the normalized equation, residual source, multiplier homogeneity, Newton coefficients for degrees 2–7 and the Gaussian gradient constant. The earlier eight generic heat-jet identities remain in [record 17](../numerics/17_COMPLEX_ZERO_FIELD_CHECKS_20261024.json). These checks support algebra; global arguments are analytic proofs.

The [build record](../../manuscript/BOOK_COMPLEX_FIELD_BUILD_RECORD_20261024.json) records source and PDF identities, compilation and visual inspection. Work continues in the same [history 0009](../chat-histories/0009_2026-10-24T12-58-27Z_review-conserved-contour-results.json). No commit/tag or new automatic research task was created.
