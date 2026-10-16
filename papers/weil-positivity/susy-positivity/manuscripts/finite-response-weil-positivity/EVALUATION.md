# Evaluation and publication status

Updated 14 September 2026 after the [current-draft novelty assessment](reviews/assessment_claude_current_draft_20260914.md) and the author's decision to defer arXiv submission. The [revision response](reviews/response_novelty_framing_20260914.md) records the resulting editorial changes. The previous evaluation, sources and PDFs are preserved in the [snapshot](drafts/2026-09-14-before-novelty-framing-revisions/SNAPSHOT.md).

## Current decision

Retain **Boundary corrections and finite responses for the localized Weil form** as a technical research note. Defer arXiv submission while further work on the project develops a clearer mathematical contribution. The present material does not establish a new positivity interval, a practical computational advantage, or priority for its specific formulas. Further polishing alone would not resolve those questions.

For subsequent work, assess novelty and mathematical usefulness before investing in extensive computational reviews. Use that assessment to select the claims worth developing, then choose targeted derivation and computational checks. Human author review, and specialist input where needed, should precede reconsideration of publication. The existing human review checklist remains unfilled.

## What the note records

The main subject is the explicit boundary correction between the localized gamma operator and its diagonal Neumann comparison. The correction is bounded and noncompact, with essential norm pi/2. Finite mass sums have controlled tails on fixed finite input spaces. A different expansion groups images, retains the endpoint singularities, and converges in operator norm with an explicit exponential remainder at fixed interval length.

An unconditional lower bound gives a positive high sector. Exact Schur elimination leaves a finite response containing all couplings to the low modes, and standard residual identities give lower and upper enclosures. These are analytic statements about the specified operator. The finite matrix still contains an infinite-dimensional inverse; approximability of its entries is distinct from an efficient algorithm.

The matrix conjecture now appears after the response is defined. Its equivalence to RH follows from localized positivity, square completion and the classical Weil criterion. It specifies the unresolved arithmetic sign and is not the main novelty claim. The smooth-density counterexample shows that replacing exact prime information by its leading density can destroy positivity; it does not exclude every approach using prime-counting estimates.

## Prior work and the limits of the novelty finding

Localized Weil positivity and finite-codimension positivity have substantial antecedents, summarized in [Suzuki's introduction](https://arxiv.org/html/2606.09096v2#S1). The RH equivalence and general Schur machinery should not carry a novelty claim.

[Connes, Consani and Moscovici](https://arxiv.org/html/2511.22755v1) study finite restrictions of the localized form and discuss the prolate approximation in Sections 7-8. The present small-eigenvalue table is an illustration of the response formulas; it establishes no new spectral mechanism.

For fractional Laplacians, [Musina and Nazarov, Theorem 2](https://arxiv.org/html/1308.3606v2) establish the restricted-versus-spectral-Dirichlet form comparison, and [Nazarov, Theorem 3](https://arxiv.org/html/2108.05416v1) establishes the spectral-Neumann comparison. These are close precedents for the structure, with different multipliers. The draft proves its digamma comparison using positive resolvent energies, in the [complete Bernstein function framework](https://arxiv.org/abs/1707.02475). Pointwise ordering of heat kernels alone is insufficient for the quadratic-form ordering; the shortcut proposed in Section 4.1 of the assessment was not adopted.

The essential-norm calculation uses classical Carleman theory, and the enclosure identities use standard operator and numerical methods. Whether the specific image formula, norm and error bounds are previously unpublished, and whether their combination has sufficient mathematical usefulness for a standalone paper, remain open assessment questions. A consequence of established theory can be a new result, but that possibility does not establish significance here. The present recommendation is conservative without treating the assessment as a proof that no contribution exists.

## Computational limits and possible future value

The smallest cutoff admitted by the present sufficient bound satisfies log log N_min(L) = L/2 + O(log L). This is a limitation of the bound, not a lower bound for every possible method. The length-one example contains numerical upper responses only; neither the complete residual Gram nor rounding and truncation errors have been enclosed to certify the full form's sign. A high-sector cutoff certificate is not a full positivity certificate.

A rigorous fixed-length certificate could validate a method or provide a partial result. Its value would depend on the method, cost and best existing unconditional support bounds, which this review has not settled. No costly certificate calculation is planned on the current evidence. A sharper arithmetic estimate using signed prime information, a demonstrable certification advantage, or a quantitative spectral result beyond existing work would justify reassessing the contribution.

## Provenance and verification status

The source investigation is repository commit `efb908ab32245eba55c0c751f3b4a33b7306e6b7`, dated 13 September 2026. Its physical constructions remain separate from the operator arguments in this note. `SOURCE_RECORD.json` retains the original source identity.

The earlier mathematical reviews and their exact checks and floating-point diagnostics remain unchanged in the reviews folder. This revision changes framing, placement and attribution while retaining the mathematical formulas and proofs. It is checked by source comparison, citation verification and PDF build/layout inspection, without another computational review suite. `VALIDATION.json` distinguishes current editorial/build validation from historical mathematical checks.

Human verification and independent specialist review remain pending. The disclosure continues to describe substantial assistance from ChatGPT, Codex and Claude. No release, DOI or arXiv submission was created in this revision.
