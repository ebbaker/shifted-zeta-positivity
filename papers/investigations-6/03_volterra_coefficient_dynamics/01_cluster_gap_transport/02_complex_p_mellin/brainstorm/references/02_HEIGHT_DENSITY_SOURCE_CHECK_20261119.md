# Height-density source check

19 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance; actual recorded model and effort unavailable.
Selected primary-source HTML passages checked, not a full-paper audit.

- Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is
  non-negative*, arXiv:1801.05914v5 (3 July 2021).
  [Primary HTML](https://arxiv.org/html/1801.05914v5).
  Checked the normalization in (1), the smooth counting main term and
  its derivative in §3, (38)–(39). The paper's RH-conditioned short-interval
  improvement and contradiction assumption Lambda<0 are not imported.
- D. H. J. Polymath, *Effective approximation of heat flow evolution of
  the Riemann ξ function, and a new upper bound for the de Bruijn–Newman
  constant*, arXiv:1904.12438v2 (4 August 2019).
  [Primary HTML](https://arxiv.org/html/1904.12438v2).
  Rechecked Theorem 1.5's clock, positive-time domain and exponential
  onset; Remark 9.4's velocity discussion. No onset constant is extracted.

Both articles are already in the
[parent bibliography](../../../../references/induction.bib).
The [existing Polymath receipt](../../references/04_VCD_GT_CM_POSITIVE_TIME_SOURCE_AUDIT_20261118.md)
owns its reading-copy provenance. No new PDF was downloaded or added.
This receipt supports [Discussion09](../notes/09_VCD_GT_CM_HEIGHT_DENSITY_AND_GAP_FLUCTUATIONS_20261119.md).

Follow-up for [Discussion10](../notes/10_VCD_GT_CM_SOURCE_LOCALIZATION_AND_DYNAMICAL_INFORMATION_20261119.md):
rechecked Polymath Theorem 1.5's individual localization and uniqueness
input, and the Rodgers–Tao abstract's dependence on hypothetical backward
extension and known zero statistics. Their lower-bound argument is cited
as an example of dynamics combined with additional information; no
upper-bound consequence is imported. Same-assistant selected-passage
reading, 19 November 2026; actual model and effort unavailable.

Further follow-up, 19 November 2026, for Edward Baker with OpenAI Codex
assistance; the chat registry records `gpt-6-astra`, effort `max`.
Rechecked Theorem 1.5(i)--(ii) and the proof following (102)--(104):
the height and index onsets are exponential in 1/t; the argument-principle
count is one with multiplicity; the proof sharpens the displacement to
O(x^(-ct)/log x). This supports Discussion10 §7's interpretation of
Polymath as initial separation data for a prospective backward extension.
No numerical onset, new coverage or new reading-copy download is claimed.

## Error-structure follow-up

19 November 2026. Prepared for Edward Baker with OpenAI Codex assistance;
guarded chat configuration `gpt-6-astra`, effort `max`. Selected passages
checked for [Discussion11](../notes/11_VCD_GT_CM_POLYMATH_ERROR_STRUCTURE_AND_BACKWARD_USE_20261119.md):
Theorem 1.3, §4 (35)--(41), Proposition 6.1 and (44), Proposition 6.3,
Corollaries 6.4--6.5 and (69)--(74), Lemma 8.4 and (92), and §9
(99)--(104). The retained finite approximation and its derivatives are
existing Polymath methods. Discussion11's explicit heat-defect identity
is a direct differentiation of their approximant, not an imported theorem
or a claim of literature novelty. No complete proof audit was performed.

The existing external PDF was rehashed at
`/Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf`:
2,158,176 bytes, SHA-256
`60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603`.
The source receipt above retains ownership. No new PDF or raw article
text was stored in the repository. HTML and PDF text were checked;
the web PDF screenshot service was unavailable, so no visual-page audit
is claimed.

**Coefficient caution for any numerical reuse.** The intermediate §9
display after (99) in the read version uses t/2 times log(x/(4pi)) in
Re(s*). Definitions (9), (17), the explicit bound (21), and (76) give
the leading coefficient t/4 instead. The discrepancy also appears in
the PDF text on printed page 57; it is not merely an HTML conversion.
This appears to be a factor-two inconsistency in that intermediate
display. No onset constant here is taken from it. Direct substitution
into the definitions, with L=log(x/(4pi)) and y=0, gives
\[
 \left|b_n^t n^{-s_*}\right|
 =n^{-1/2}\exp\left[-\frac t4\log n\,(L-\log n)
                  +O(t\log n/x^2)\right].
\]
Since log n<=L/2+O(1/x) at the prescribed cutoff, an integral bound
still yields decay of the qualitative form x^(-ct) when t log x is
sufficiently large, after reducing c. This observation does not dispute
the qualitative exponential-onset theorem or certify its numerical
constants. Discussion11 uses the exact definitions throughout.
