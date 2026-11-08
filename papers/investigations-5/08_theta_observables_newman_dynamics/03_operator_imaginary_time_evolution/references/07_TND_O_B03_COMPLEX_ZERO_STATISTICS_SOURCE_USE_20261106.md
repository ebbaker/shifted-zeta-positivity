# Complex-zero statistics: primary-source register

**Source check completed 8 November 2026:** the
[bounded BGST audit](../02_localized_zero_correlations/reviews/BGST_IMPORT_SOURCE_CHECK_20261108.md)
resolves the warning below for the parent manuscript. Its cumulative
`eq:BGST` is exactly v3 (3.5), **first line**, divided by
T log(T)/(2 pi), and survives unchanged. The weaker dyadic theorem (3.2)
and the erroneous multiplicative formula reproduced on v3 p.7 are
different statements. Pinned 2306.04799v1 (1.4) already prints the
manuscript's additive form; the 2024 journal text was not compared.
Cite the corrected proof on any new use. This supersedes the request to
reconcile this particular equation, not the historical reading provenance
or unrelated assessments. Prepared for Edward Baker with substantial
OpenAI Codex assistance; actual backend model/effort unavailable, chat0004.

**Source correction found 8 November 2026:** the later BGST paper
[arXiv:2501.14545v3, §3](https://arxiv.org/html/2501.14545v3#S3)
corrects the uniform error term of the earlier unconditional Montgomery
theorem and explains the cumulative/dyadic versions. The older v1 reading
below is preserved as historical provenance. Reconcile the imported
parent manuscript (eq:BGST) before reusing that uniform bound; no full
dependency audit is claimed. The authors state their original applications
survive. [TND-OC source-use04](../02_localized_zero_correlations/references/04_TND_OC_PAIR_MARGINAL_LITERATURE_SOURCE_USE_20261108.md)
owns the new article record and checked-passage receipt. Prepared for
Edward Baker with OpenAI Codex assistance; actual current model/effort
unavailable. This warning does not alter historical assessments.

6 November 2026. Prepared for Edward Baker with substantial LLM assistance,
actual gpt-6-astra / max. TND-O-B03, chat0004. Entries are recorded on
discovery; the final source-use update specifies the passages actually
checked. PDF retention does not certify the contents. No third-party PDF
is stored in the repository.

| Source | Exact version / primary link | Relevance and inspection at discovery |
| --- | --- | --- |
| H. L. Montgomery, The pair correlation of zeros of the zeta function | Proc. Sympos. Pure Math. 24 (1973), 181–193; [author-hosted PDF](https://websites.umich.edu/~hlm/paircor1.pdf) | Original theorem assumes RH; first theorem, (1)–(2), and Corollary3 located; visual verification pending |
| S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function | [arXiv:2306.04799v1](https://arxiv.org/abs/2306.04799v1), submitted 7 June 2023; published Acta Arith.214 (2024),357–376, DOI10.4064/aa230612-20-3 | Complex-difference statistic and unconditional theorem; v1 selected-passages inspection in progress; journal publication metadata is not a claim that journal text was compared |
| D. A. Goldston, J. Lee, J. Schettler, A. I. Suriajaya, Pair Correlation Conjecture for the Zeros of the Riemann Zeta-function I: Simple and Critical Zeros | [arXiv:2503.15449v4](https://arxiv.org/abs/2503.15449v4), 30 March 2026 | Ordinate-only PCC without an RH premise; horizontal multiplicity and density-one conclusion conditional on PCC; selected passages in progress |
| Z. Rudnick, P. Sarnak, Zeros of principal L-functions and random matrix theory | Duke Math. J.81 (1996),269–322; [DOI](https://doi.org/10.1215/S0012-7094-96-08115-6); [institutional PDF mirror](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/rudnick-sarnak.pdf) | Earlier complex-zero extension for restricted analytic tests; exact RH-removal passage to be checked before any import |

Rodgers–Tao v5 is reused through the existing canonical records and branch
receipt06. The present fresh inspection includes §9, especially (93):
almost all gaps become near their mean under Lambda<0, in conflict with
a positive proportion of small gaps. Their explicit final contradiction
uses the Conrey–Ghosh–Goldston–Gonek–Heath-Brown gap theorem; it does not
assume the full pair-correlation conjecture. Their Remark2 also flags
positive-time asymptotic spacing, to be checked at its primary source.

HTML generated dates are not substituted for pinned arXiv submission
versions. Search-only pages are discovery aids, not theorem sources.

## Positive-time tail source discovered

Haseo Ki, Young-One Kim and Jungseob Lee, *On the de Bruijn–Newman constant*,
Advances in Mathematics222 (2009),281–306,
[DOI10.1016/j.aim.2009.04.003](https://doi.org/10.1016/j.aim.2009.04.003).
Author-hosted reprint URL: https://web.yonsei.ac.kr/haseo/p23-reprint.pdf.
The secondary HTML reference in Rodgers–Tao Remark2 was initially
transcribed as “Theorem1.14”. Direct primary inspection corrects the
numbering to **Theorems1.3 and1.4**, as recorded below. No uniformity as positive time tends to zero is
inferred from a fixed-positive-time assertion.


## Final selected-passage ledger — 6 November 2026

For Edward Baker with substantial LLM assistance, actual **gpt-6-astra / max**.
The discovery descriptions above are historical; the completed inspection
scope is the following table. None is a full-paper proof audit.

| Source/version | Actually inspected | Imported use and limitations |
| --- | --- | --- |
| Montgomery1973, author PDF, 13 pages | First theorem, (1)–(2), Corollary3; text and PDF pages1,3 rendered/visually checked | Manuscript12.1: original restricted-frequency theorem assumes RH; the full PCC is a stronger conjecture |
| BGST arXiv2306.04799v1 | Theorem1, (1.2)–(1.4), Lemma2 count bound, Lemma3/(2.6) positive Cauchy-kernel integral; selected Section2; text and PDF pages1,3,4 visually checked, including conjugations | ManuscriptTheorem12.1, Propositions12.2/12.4: exact analytic complex-difference weight, nonnegativity and uniform 0<=alpha<=1 asymptotic. No unchanged ordinate-only theorem imported. Arithmetic proof not independently rederived |
| GLSS arXiv2503.15449v4 | Theorem1, Sections4–8: ordinate PCC, second moment/horizontal multiplicity definitions, Theorem2 and PCC-to-multiplicity implication; selected text and rendered PDF pages1,5,6,7 | Manuscript12.3: density-one simple critical zeros **conditional on their PCC**, without an additional RH assumption. Not an unconditional RH conclusion. Horizontal coincidence inequalities derived directly and credited |
| Rudnick–Sarnak1996, 60-page prepublication copy | Test-function context and Theorems1.1–1.2; text and rendered PDF pages4,5 | Manuscript12.2: precedent for complex zero coordinates under entire smoothing and restricted Fourier support. Theorem1.1 has support sum|xi_j|<2/m and, for general L-functions, m<=3 or the stated coefficient hypothesis(1.7). Theorem1.2's sharper window statement assumes RH. Only the restricted-test precedent is used |
| Ki–Kim–Lee2009, published author reprint via archived primary URL | Browser-extracted primary text: normalization(1.1), Theorems1.3–1.4, journal pages282–284 | ManuscriptTheorem12.5: for every fixed positive parameter, all but finitely many zeros are real/simple, with asymptotically regular gaps. Conversion Xi_mu(t)=8H_(4mu)(2t), so our gap constant is4pi. No time-uniform exceptional-height estimate is imported |
| Rodgers–Tao arXiv1801.05914v5 | Fresh selected HTML reading: Introduction, Remark2 and Section9/(93), in addition to receipt06's renormalization passages | Manuscript11 and12.1: all-real ordered flow under Lambda<0; final contradiction uses a positive proportion of small gaps through Conrey–Ghosh–Goldston–Gonek–Heath-Brown, not the full PCC. No extension of their estimates to Lambda>0 is imported |
| Csordas arXiv1309.0055v2 | Inherited fresh selected passage recorded in receipt06, Definition1.1, reused here without another claimed inspection | Manuscript5.6: conditional real Laguerre–Pólya product, Gaussian factor and multiplicities retained; no unproved all-real hypothesis made unconditional |

BGST v1 was submitted7 June2023 and its PDF is dated9 June2023; the
HTML generation date is not a new research version. Publication metadata
Acta Arithmetica214(2024),357–376 was checked; the journal text was not
compared. GLSS v4 was submitted30 March2026 and its PDF is dated1 April2026;
it is cited as a preprint, with no publication status inferred.

The KKL primary text was accessible through
[the archived author reprint](https://web.archive.org/web/20170809013021if_/http://web.yonsei.ac.kr/haseo/p23-reprint.pdf).
A direct author-host download timed out; attempted archive download
returned HTTP429. No retained local KKL PDF or successful page-image
inspection is claimed. The theorem numbers, fixed-time quantifier and
normalization were read in the extracted primary text. The source's
[DOI](https://doi.org/10.1016/j.aim.2009.04.003) remains the stable locator.

Rudnick–Sarnak's author URL failed in the web retrieval; the institutional
Exeter mirror supplied the author text used above. The citation retains
both author and mirror links. Retained reading-copy URLs, bytes and hashes
are in [the acquisition receipt](COMPLEX_STATISTICS_PDF_RECEIPTS_20261106.json).
Four theorem-source PDFs were retained outside Git before the related
abstract-only additions below. Archived bytes identify versions, not
mathematical validation.

## Related discoveries — abstract and metadata only

These were found during the focused search, recorded for follow-up, and
are **not theorem inputs to the manuscript**.

- Daniel A. Goldston and Ade Irma Suriajaya, *Zeta Zeros on the Critical
  Line*, [arXiv:2511.20059v2](https://arxiv.org/abs/2511.20059v2),
  revised5 February2026 (first submission25 November2025), 9-page expository
  preprint. The abstract describes what would follow if the RH hypothesis
  could be removed from Montgomery's simple-zero argument; it is not a
  claim of an unconditional two-thirds simple-critical-zero theorem.
- Daniel A. Goldston, Junghun Lee, Jordan Schettler and Ade Irma Suriajaya,
  *Pair Correlation Conjecture for the zeros of the Riemann zeta-function II:
  The Alternative Hypothesis*,
  [arXiv:2507.06823v1](https://arxiv.org/abs/2507.06823v1),
  9 July2025, 11 pages. Related conditional density-one conclusions under
  a different hypothesis; no theorem, proof or hypothesis details imported.

Their reading-copy acquisition status is appended to the same manifest;
retention alone does not expand the abstract-only inspection claim.

## Consumers and evidence level

[Note13](../notes/13_TND_O_B03_COMPLEX_ZERO_STATISTICS_AND_MANUSCRIPT_RETURN_20261106.md)
and manuscript Sections11–12 consume this record.
The finite Gram identity, finite-change estimates and transverse balance
are directly proved in the manuscript; literature arithmetic asymptotics
are explicitly imported. The [same-author production check03](../reviews/03_TND_O_E04_B03_ANALYTICAL_AND_PRODUCTION_CHECK_20261106.md)
does not independently certify the cited arithmetic proofs.
[Continuation14](../notes/14_TND_O_E04_B03_CONTINUATION_AND_MODEL_CHANGE_20261106.md)
preserves the model and next-assessment handoff.
