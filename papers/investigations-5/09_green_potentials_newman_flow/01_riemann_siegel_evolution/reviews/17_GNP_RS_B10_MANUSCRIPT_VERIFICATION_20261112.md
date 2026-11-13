# B10 manuscript verification

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance and separate integration
contributors. Child chat0008. Actual model and reasoning effort are
unavailable in the recorded configurations.

[The live section](../../manuscript/sections/10d_short_window_means.tex)
contains Theorem 14.1 and Corollary 14.2. The [integration note](../notes/33_GNP_RS_B10_MANUSCRIPT_INTEGRATION_20261112.md)
maps their sources. This check covers transcription, applicability of
the cited inputs, and production, with the earlier internal proof audit
as its mathematical basis. The published proofs and inherited
complete-field provider retain their original review scopes.

| Claim or interface | Verified in the live manuscript |
| --- | --- |
| Theorem 14.1 | \(c=1\), real \(U\) beyond a finite unevaluated onset, fixed \(0<\rho\le47/162\), \(U^{17/81+\rho}\le\ell\le U\), and uniform block-constant \(P\) up to \(\lfloor L_U^2\rfloor\). The power error is \(U^{-\min(7/6480,9\rho/28)}\). |
| Upper arm | Exact integer endpoints, pole and long-frequency tails are present. The cumulative Bourgain–Watt error remains in the translated bound. The exact quadratic expansion uses the real sum over all pairs. |
| Lower arm and convolution | The Montgomery–Vaughan input is applied to the reciprocal comparison phase, including its derivative gate and remainder. Both convex endpoints, all shifts, cutoff jumps and low–high cross terms are covered. The exact convolution retains its variation and mass deficit. |
| Residual comparison | The finite-head and multiplier terms, reflected frequencies, \(1/2\) in Fubini, physical clock and full-field error appear in (14.9)–(14.10). B08 supplies the closed \(\sqrt U\) overlap at its fixed margin \(19/72\). |
| Corollary 14.2 | Uses \(P_U=\lfloor L_U^2\rfloor\) throughout the outer interval. The simplified transfer uses \(R_{P_U}(X,1)\) and the omitted-prime allowance \(O(L_U^{-3})\). The two Green rates use the corresponding regulator choices. |

The [build record](../../numerics/03_GNP_RS_B10_INTEGRATION_BUILD_RECORD_20261112.json)
identifies the 68-page PDF. Rendered all pages and inspected the
contact sheets, with individual review of pages 43–49 and additional
checks of the front matter and evidence/outstanding pages. An overfull
convolution display in the first build was split and the final LaTeX
log has no overfull boxes, unresolved references or citation warnings.
BibTeX still reports the existing empty journal field in the Polymath
arXiv citation. The rendered reference includes the arXiv link.
The bibliography includes the checked Bourgain–Watt preprint and
journal records and the Montgomery–Vaughan chapter. Extracted PDF text
and the table of contents locate Theorem 14.1 on p. 43 and Corollary 14.2
on p. 49.

The result remains a translated mean estimate and a fixed-threshold
exceptional-measure estimate. Pointwise control, a numerical onset
and the varying-cutoff residual remain open.
