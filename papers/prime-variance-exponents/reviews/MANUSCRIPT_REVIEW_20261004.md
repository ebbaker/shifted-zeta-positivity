# First manuscript: final verification record

4 October 2026; work began from the 3 October continuation.
Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate agents performed fresh internal checks using the inherited model.
These checks are not independent specialist refereeing or a novelty audit.

## Delivered source and scope

The single editable [manuscript](../manuscript.tex), *Prime response variance
exponents and the Riemann hypothesis*, has author Edward Baker, a 4 October
2026 draft date, and an explicit acknowledgement of substantial LLM assistance.
Its final source SHA-256 at this review is
`7c04e0351065e20dafc6c7f62ebac29a86590bb4f7e594de508905574df56ccf`.
It has 1,019 source lines and 44,413 bytes.

The paper includes full proofs of the fixed probe properties, elementary
transform noncancellation, sixth-power decay, the complete linear explicit
formula, the true-Laplace fixed-exponent equivalence, both endpoint exponents,
the RH limit corollary, PNT transfer, finite variance transfer, short-interval
averaging and signed covariance, and the finite-prefix generic obstruction.
Two appendices give certificate constants/hashes/budgets and the complete
countermodel proof. The introduction and conclusion keep the first global
actual-prime power saving and any descent mechanism open.

The complete explicit formula uses a direct inverse Mellin contour argument,
justified by the actual C4 probe's sixth distributional derivative. This
provides the smoothing/regularity justification requested by the continuation
without relying on the parent manuscript's operator framework. Every zero sum
includes both ordinate signs and multiplicities; the trivial-zero terms remain.

## Fresh review results and resolutions

- [Core proof pass](CORE_PROOF_REVIEW_20261003.md): no mathematical gap found
  in Sections 1–3. Checks cover transform signs, the energy argument for H,
  contour heights and the negative odd vertical lines, true-transform
  holomorphy, pole exclusion, both directions, closed boundaries, delta=0/1,
  nonuniform constants along exponents tending to zero, and the optimal
  exponent. The explicit decaying estimate for the left vertical integral
  was added to the final text.
- [Arithmetic pass](ARITHMETIC_REVIEW_20261003.md): no substantive error found
  in Sections 4–6 and Appendices A–B. Checks cover complete original/expanded
  support, noninteger centering, the exact approximation constants, both
  exponent transfers, the all-real-X phase minimum, and the prefix-qualified
  diagonal identity. The final text specifies real nonzero gamma and makes
  the finite-range asymptotic constant depend on the chosen ceiling C.
- [Primary-source audit](SOURCES_REVIEW_20261003.md): the four arithmetic
  inputs and final bibliography were checked against primary texts. The
  theta/psi distinction in Saffari–Vaughan is explicit; the manuscript also
  states the relative range U^(epsilon−5/6)<vartheta<1. Versioned author
  preprints and the published Johnston–Yang citation are retained.
- Three missing `equation` closures in the initial source were identified
  during review and fixed before native compilation. A final environment
  stack scan finds no mismatch or unclosed environment; all equation/section
  references and citation keys resolve, with no duplicate labels.

## Certificate and source identity

The [certificate replay record](CERTIFICATE_REPLAY_20261003.md) gives the
commands, exact budgets, input hashes, and limitations. The existing finite
generator was replayed into a temporary directory and its output matched
the retained record byte-for-byte. The original rational replay also passed.
Exact polynomial normalization, sixth-derivative norm, endpoint atoms, and
the variation majorant were independently reconstructed using rational
arithmetic. A second arithmetic reviewer checked those constants, all three
budgets, and the five identifiers printed in the appendix.

The resulting strict bounds remain finite: 38 X² through 10⁹⁹, 40 X² through
10¹⁰⁰, and 72 X² through 10¹⁰², all starting at e and valid for every real X
in the respective interval. The old 192/256-bit outward zero calculations
were imported, not regenerated; the published Platt–Trudgian verification
was not rerun. No large computation, zero cache, or third-party PDF was
added to the repository.

The continuation's parent-manuscript and finite-record hashes both matched
the actual files. The repository base at drafting was
`3a8e1b3c048d5c00eed12638ec9847e71ca58d78`, a later commit than the handoff's
recorded HEAD; reading the actual paths and matching their hashes reconciled
that difference. The parent project was left unchanged.

## Compilation and file checks

The saved source was submitted to `open_in_codex` for the built-in LaTeX
editor. The app accepted the request with status `queued`; visibility of
the tab was not independently confirmed. The native
`compile_latex_document` tool returned `kind: success` on the initial
complete repaired draft and again on the final source identified above.
No TeX distribution was installed and no replacement source was created.

The compiler returns diagnostics rather than an exported PDF or page count.
An attempted read-only view of Codex through the computer-use tool was
unavailable because that app is excluded from computer-use access. No
alternate UI-access method was used. Thus compilation is verified, but
page-by-page visual layout and the final rendered page count are not claimed.

The manuscript's local certificate links resolve. The project README,
verification ledger, and DRAFT_HISTOR record link the source, reviews, and
original packages. No draft snapshot directory, commit, or tag was created.
All new files are far below the repository's large-file threshold.

The drafting task is complete. The next mathematical obligation is the
actual-prime power-saving estimate formulated in the manuscript; it was
explicitly outside the completion requirement of this drafting session.
