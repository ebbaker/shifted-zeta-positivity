# Continuation: complex zero fields, conserved quantities and multiplicity

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual reasoning effort max**. This is a research handoff and archival/organization record. It adds no mathematical theorem or completion claim; the preceding derivations and review are same-assistant work.

## Where to resume

The maintained manuscript is [book.tex](../../manuscript/book.tex), *Complex zero fields and conserved heat evolution*. At the author's request it now centers exclusively on the complex field, analytic calculations, conservation laws and multiplicity observables. Start with Sections 2–4 for the density, phase and evolution; Sections 5–7 for conservation, polynomial controls and normalization; and Section 8 for the observable and its transport. [Note 23](23_COMPLEX_FIELD_BOOK_AND_CONSERVATION_LAWS_20261024.md) records the latest additions and [Self-review 13](../reviews/13_COMPLEX_FIELD_BOOK_SELF_REVIEW_20261024.md) their hypotheses and limitations. [Note 22](22_COMPLEX_ZERO_FIELDS_AND_CONSTRAINED_OPERATOR_TOOLS_20261024.md) retains the original construction and the review of the three [constrained-operator source documents](../../../../investigations-2/active/20_constrained_operator_squares/source_documents). Its uncertainty about global normalization is resolved by the mass classification in the new book.

Read the repository [result index](../../../../../result-summaries/README.md), especially [local heat geometry and the field result](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md). Also read the [avoid index](../../../../../avoid/README.md), particularly [target restatements](../../../../../avoid/01_restating_the_target.md), [generic lifts](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [normalization errors](../../../../../avoid/08_normalization_and_constant_slips.md) and [unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). These are the classification and control rules for the next proposed estimate.

The older [arithmetic overview 04](../../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md) and [progress 04](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) remain records of the contour route and its open estimates. Their book numbering refers to [draft 03](../../manuscript/drafts/book_draft_20261024_03_conserved_contours.tex), not to the new field book. Existing SIMP, SCF, OBF and HDC ownership and completion statuses have not changed.

## Decisions from this conversation

The author wants a complex field with **total normalization** \(\int|\psi|^2\,dA=1\), a density interpretation, a relation between its gradient and zero motion, an evolution equation and an observable sensitive to multiplicity. Pointwise unit modulus was not the chosen convention. The operator source documents were consulted for constructions and estimates, with their incomplete implementations and domain requirements retained.

Here \(z=x+iy\) is the spatial complex variable and real \(t\) is heat time. A moving boundary would be a curve in this \(z\)-plane depending on \(t\). The current field formulation is primary and can use a fixed observation window. Movement is an optional localization choice; even a fixed window has flux across it.

The phase gradient, rather than the gradient of the density alone, supplies the velocity. The smooth amplitude need not be singular at a zero. It is nonzero at a simple zero and vanishes at a multiple zero, but also vanishes at nonzero critical points of \(H\). A pointwise zero of the amplitude therefore does not by itself certify multiplicity.

## Equations and established scope to retain

For \(H_t=-H_{zz}\), fixed \(\epsilon>0\), and \(D=|H|^2+\epsilon^2\), use

\[
A=\frac{\epsilon H_z}{\sqrt\pi D},\qquad
\rho=|A|^2=\frac1{4\pi}\Delta\log D,\qquad
V=-2\partial_{xy}\log D.
\]

The exact equations are

\[
iA_t=-A_{xy}+VA,\qquad
\Delta V=-8\pi\partial_{xy}\rho,\qquad
\rho_t+\nabla\cdot\mathbf j=0,
\]

with \(\mathbf j=(\Im(\bar A A_y),\Im(\bar A A_x))\). Where the phase \(\theta=\arg A\) is defined, \(\mathbf j/\rho=(\theta_y,\theta_x)\). At a simple zero this agrees with \(\dot a=H_{zz}/H_z\). The current remains smooth where the phase or track formula fails. The displayed rotation/scaling in the book converts the system to focusing DS-II; the reference convention was checked, but no global DS-II existence or scattering theorem was imported.

For the selected potential \(V=\mathcal T\rho\),
\(\widehat{\mathcal Tf}(k)=-8\pi k_xk_y|k|^{-2}\widehat f(k)\), the book proves conservation of mass, both momenta and the Hamiltonian

\[
M=\int\rho,\qquad P_i=\int\Im(\bar A A_i),\qquad
\mathcal E=\int\Re(\overline{A_x}A_y)+\tfrac12\int\rho\mathcal T\rho,
\]

under its explicit integrability, regularity and vanishing-boundary assumptions. First moments and mixed virial combinations are also conserved after their time corrections. The Hamiltonian is indefinite. The Poisson equation alone does not select the harmonic part of \(V\); external/harmonic forcing has additional terms. The lift also has local laws for \(g(H)\rho\), which retain \(H\) and are not automatically laws for every DS-II solution.

For every nonconstant entire slice, \(M\) equals the polynomial degree or is infinite in the transcendental case, at **every fixed positive regulator**. In particular theta has infinite unlocalized mass. This rules out constant global normalization of this amplitude; it does not rule out weighted/local states, nor settle convergence of all other signed quantities.

Use a fixed smooth compact cutoff \(h\) and retain both

\[
Z(t)=\int h^2\rho,\qquad \psi=hA/\sqrt Z,\qquad
\dot Z=\int2h\nabla h\cdot\mathbf j.
\]

The normalized equation includes cutoff derivatives and \(-i\dot Z\psi/(2Z)\). Keep the full potential selected by the original theta lift. Replacing it with \(\mathcal T|\psi|^2\) would define a different evolution. An approximate amplitude with residual \(r=iA_t+A_{xy}-VA\) adds \(2\Im(\bar A r)\) to the continuity equation, with the book's explicit localized error bound.

## The observable and the remaining obstacle

For a finite nonempty divisor \(\nu=\sum_a m_a\delta_a\) of mass \(N\), let \(K_s(z)=(4\pi s)^{-1}e^{-|z|^2/(4s)}\). Then

\[
Q_s(\nu)=8\pi s\int(K_s*\nu)^2-N
=\sum_a m_a(m_a-1)+\sum_{a\ne b}m_am_b e^{-|a-b|^2/(8s)}.
\]

The small-scale limit is multiplicity excess. Close distinct zeros also contribute at finite resolution. For the field measure \(\mu_\epsilon=h^2\rho\,dA\), take \(\epsilon\downarrow0\) at fixed \(s\), then \(s\downarrow0\), with the cutoff equal to one near the selected zeros and no zeros in its transition. Reversing these limits gives the negative regularized mass. Track and field transport formulas retain the flux through the window.

The equal-mass comparison is
\(|Q_s(\mu)-Q_s(\nu)|\le Ne^{-1/2}s^{-1/2}W_1(\mu,\nu)\), with \(W_1\) for measures of mass \(N\); the book also pays a mass-mismatch term. A quantitative regulator-to-divisor bound is still needed to use this estimate at a specified resolution and height.

The polynomial control \(H=z^2-2t\) has \(M=2\), \(P_x=P_y=\mathcal E=0\) through its double collision, while \(Q_s(t)=2e^{-|t|/s}\). Thus the displayed conserved charges allow collisions; \(Q_s\) is neither conserved nor universally monotone. This is a scoped obstruction for those charges, not a classification of every DS-II invariant. The missing result is a useful estimate from the **unchanged theta source** controlling a multiplicity-sensitive quantity with all regulator, scale, height and localization costs paid.

## Next analytic pass

1. **Fix one finite observation problem.** State the heat-time interval, height window, cutoff, value-plane regulator \(\epsilon\), spatial resolution \(s\), selected divisor and complete theta normalization. Keep possible multiple zeros. The deliverable is an explicit contract for an estimate, with a specified observable and required error size; do not assume a simple-zero separation or a small-value floor that already excludes the event.

2. **Quantify the field-to-divisor passage.** Seek bounds for \(|Z-N|\) and \(W_1((N/Z)\mu_\epsilon,\nu)\) from paid analytic data for the complete \(H\). Distinguish \(\epsilon\), measured in the value plane, from \(s\), measured in the spatial plane. State whether constants depend on a candidate cluster and its multiplicity, or remain uniform as height grows. Success is a proved error estimate with stated hypotheses and a useful scale range; local weak convergence alone is already established.

3. **Test one source-dependent upper estimate.** Use the exact observable transport law, or a retained target-weight law, to identify a theta input that can bound the complete quantity. Include the internal transport term, window flux and any approximation residual. If a higher invariant or constrained square is proposed, first establish that it is well defined on the intended theta/localized class and show what multiplicity information it controls. Neither formal conservation nor an indefinite energy supplies a positive bound automatically.

4. **Apply the collision controls before promoting the claim.** The polynomial control satisfies the finite global assumptions and still collides. The analytic changed-source controls satisfy the generic local identities and admit compact localization; transcendental controls fail finite global mass just as theta does. Name the precise arithmetic premise a proposed theta estimate uses and which controls fail it. If none fails, retain the result at its generic scope. Numerics may check algebra or a defined estimate after the analytic question is fixed; they do not establish exclusion or an all-height bound.

Keep incremental derivations in this brainstorm's `notes/`, assessments in `reviews/`, and small supporting computations in `numerics/`. Update a research status only when its stated estimate has actually been obtained. No automatic task or new goal is created by this handoff.

## Archive verification and draft organization

This conversation remains uniquely registered as **0009, Review conserved-contour results**, thread `01a16dfd-bc51-7251-91aa-4d3d6a8db609`, in the [brainstorm archive](../chat-histories/0009_2026-10-24T12-58-27Z_review-conserved-contour-results.json). The [verification receipt](../chat-histories/VERIFICATION_COMPLEX_FIELD_CONTINUATION_20261024.json) records stored/canonical integrity checks for all eight local histories, exact completed-public-source comparison for this conversation, the prior book-rewrite final reply, unique current-thread registration and preserved first-capture identity. It is a point-in-time audit, not mathematical validation. The current final reply can be captured only after it is sent, using the repository's bounded exact-turn follow-up.

The three existing standalone book drafts are now in [manuscript/drafts](../../manuscript/drafts/README.md). They were moved without changing their bytes; drafts 02 and 03 deliberately retain distinct milestone names despite having identical content. Markdown links were updated. Historical JSON receipts and recorded chat text keep their original paths; the [relocation receipt](../../manuscript/drafts/DRAFT_RELOCATION_20261024.json) maps those paths and records the documentation edits, including new hashes for notes whose links changed. Earlier build receipts identify their original documentation snapshots. The current book source and PDF are unchanged by this organization pass, and no new manuscript snapshot, commit or tag was created.
