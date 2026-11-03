# Sources for the Vafa–Witten RH literature review

2 November 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra / xhigh**, verified in this chat's turn metadata. The [review](../01_jensen/01_mellin_curvature/07_donaldson_witten_theory/reviews/03_VAFA_WITTEN_RH_LITERATURE_REVIEW_20261102.md) owns the historical assessment. This record extends existing article records and adds three sources; it is not a full-paper proof audit.

## Existing sources rechecked

- **Riemann-1859-Wilkins-199812.** Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*, November 1859. [David Wilkins translation, December 1998](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf). Printed p.3, PDF page4, read in extracted text and rendered image: theta integral and its completed form. Original archive identity preserved.
- **VafaWitten1994.** Cumrun Vafa and Edward Witten, *A Strong Coupling Test of S-Duality*, Nuclear Physics B 431 (1994), 3–77. [hep-th/9408074v2, 1 September 1994](https://arxiv.org/pdf/hep-th/9408074v2). Section4.2, especially (4.30) and (4.32), printed pp.65–67. Formula pages65 and67 inspected visually. The derivative is already explicit in (4.32); the older eta convention is retained when comparing numerators.
- **DabholkarPutrovWitten2020.** Atish Dabholkar, Pavel Putrov and Edward Witten, *Duality and Mock Modularity*, SciPost Physics 9, 072 (2020), DOI [10.21468/SciPostPhys.9.5.072](https://doi.org/10.21468/SciPostPhys.9.5.072). [2004.14387v3, 20 October 2020](https://arxiv.org/pdf/2004.14387v3). Introduction, Section3.1, (3.1)–(3.11), and the sign discussion beside (4.38). Printed pp.14–15 visually rechecked. The 2020 contribution is a physical derivation and explanation of an already known anomaly, not an RH theorem.
- **NISTDLMF.** [25.4.4](https://dlmf.nist.gov/25.4#E4) and [25.5.13–14](https://dlmf.nist.gov/25.5#E13), inspected online on this date. Modern normalization cross-check only; no PDF copy.

The three reused PDFs matched the bytes and hashes in their existing catalog receipts. No retrieval date or earlier inspection provenance was replaced.

## Zagier1975

Don Zagier, *Nombres de classes et formes modulaires de poids 3/2*, C. R. Acad. Sci. Paris, Série A, 281 (1975), 883–886. The scan bears 24 November 1975; its presentation footnote says session of 6 October 1975. [Author-hosted scan](https://people.mpim-bonn.mpg.de/zagier/files/scanned/NombresDeClassesEtFormesModulaires/fulltext.pdf).

All four pages viewed; relied-on passage: Section2, Theorem2 and corollary, p.884. This establishes the historical completion and theta-period ancestry. Its scalar normalization is not copied into the SO(3) vector component. No RH statement is imported.

## Manschot2018

Jan Manschot, *Vafa-Witten theory and iterated integrals of modular forms*. First submitted 28 September 2017; inspected [arXiv:1709.10098v2, 19 July 2018](https://arxiv.org/pdf/1709.10098v2). Associated publication DOI [10.1007/s00220-019-03389-5](https://doi.org/10.1007/s00220-019-03389-5), as linked by arXiv; publisher full text was not retrieved.

Checked introduction, (2.7)–(2.9), printed p.7, and Section3.4, (3.18)–(3.22), p.16. These identify the ordinary theta shadow and its nonholomorphic Eichler integral in VW theory before DPW. The higher-rank results are background only. No Mellin identity or zero-location theorem is imported.

## JohnstonMales2022

Daniel R. Johnston and Joshua Males, *Exact formulae and Turán inequalities for Vafa–Witten invariants of K3 surfaces*. Inspected [arXiv:2204.05465v1, 12 April 2022](https://arxiv.org/pdf/2204.05465v1). Publication metadata: Proceedings of the Edinburgh Mathematical Society 66(3) (2023), 845–861, published online 8 August 2023; DOI [10.1017/S001309152300041X](https://doi.org/10.1017/S001309152300041X). Publisher metadata and abstract checked; theorem numbering here is from the preprint.

Checked Section1.2, Theorem1.7, Theorem2.2, Section3.5 and the opening of Section4.1. Printed p.4 visually inspected. Fixed-degree eventual hyperbolicity for stated K3 sequences, with sector/subsequence restrictions, is the relevant scope. Detailed asymptotic constants and formulas were not recertified. This does not provide the CP² signed Mellin comparison.

## Search record and screened leads

Search date: 2 November 2026. General web search, with targeted arXiv/domain variants and primary-source follow-through. Core query strings included:

```text
"Vafa Witten" "Riemann hypothesis"
"Vafa-Witten" "Riemann hypothesis"
"Vafa-Witten" "Riemann zeta"
"Vafa-Witten" "Mellin" zeta
"Vafa-Witten" "Mellin transform"
"Vafa-Witten" "Mellin period"
"Vafa-Witten" "Riemann xi"
"Vafa-Witten" "zeta zeros"
"holomorphic anomaly" "Riemann hypothesis"
"holomorphic anomaly" "Riemann zeta function"
"2004.14387" "Riemann hypothesis"
"9408074" "Riemann hypothesis"
"Duality and Mock Modularity" zeta Mellin
"Zagier" "shadow" "Riemann hypothesis"
"Exact formulae and Turán inequalities" arxiv
```

Supplementary full extracted-text searches of VW1994, DPW2020 and Manschot v2 returned no “Mellin” or “Riemann hypothesis” occurrence. This supports a bounded statement about the inspected texts, not universal absence of a prior formulation.

- [Hirosi Ooguri, interview with Edward Witten](https://www.ias.edu/sites/default/files/sns/Interview.pdf), Notices of the AMS version, printed p.497: RH is an analogy for a conjectural explanatory framework. Checked the surrounding passage; it does not assert a VW–RH theorem. No theorem imported and no full interview review.
- [Michele and Antonio Nardelli, viXra:2005.0061v1](https://vixra.org/pdf/2005.0061v1.pdf), *On some possible mathematical connections between various equations concerning the Mock Modularity closely related to N = 4 super Yang-Mills, φ, ζ(2) and some parameters of Particle Physics*. Title, selected numerical-comparison passages around pp.8–27, and concluding text inspected online. It cites DPW, Moser and Ramanujan and compares selected numerical values; the inspected material does not establish the exact anomaly Mellin period. Not used as mathematical evidence or accepted precedent. Many formulas are images; the absent extracted-text “Mellin” match is not a complete content audit.

These screened leads are retained for search transparency, outside the canonical theorem bibliography. Unrelated appearances of zeta special values, Riemann surfaces, and different Vafa–Witten theorems were not treated as evidence of the proposed equivalence. No exhaustive forward-citation database search or author inquiry is claimed.

## Storage

[New PDF receipts](PDF_RECEIPTS_VAFA_WITTEN_RH_LITERATURE_20261102.json) record the three new author/arXiv reading copies under `/Users/Shared/szp-archive/positive-theta-primitives/references/`. No third-party PDF is in Git. [sources.json](sources.json) keeps one record per article, with appended checks for reused sources; [sources.bib](sources.bib) includes the three additions.

## Follow-up tool assessment

2 November 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra / xhigh**. DPW Sections4.3–4.4 rechecked in [primary HTML](https://arxiv.org/html/2004.14387v3) for the supertrace and boundary-supercurrent identity: HTML (66),(77), corresponding to PDF (4.21),(4.32). PDF p.29 trace notation was also checked in extracted text. These are identities, not imported positivity theorems for the repository's signed determinant. The strategic conclusion is appended to Review03; no further identity has been worked and MC07-B03 remains unexecuted.

## MC07-B03 follow-up inspection

2 November 2026, for Edward Baker with substantial LLM assistance, gpt-6-astra / xhigh. Rechecked DPW v3 Sections 4.3–4.4 in the version-pinned [primary HTML](https://arxiv.org/html/2004.14387v3): (66),(77),(81)–(83), corresponding to PDF (4.21),(4.32),(4.36)–(4.38), with equation numbering cross-checked against the previously archived PDF text. Selected graded-trace, boundary-supercurrent, Wess–Zumino factor and anomaly formulas only; not a full paper audit. Existing PDF version and receipt are unchanged.

[MC07-B03 Return03](../01_jensen/01_mellin_curvature/07_donaldson_witten_theory/notes/03_BOUNDARY_WARD_FEASIBILITY_RETURN_20261102.md) differentiates the explicit completed response, retaining its normalization, and carries it through the signed determinant. No new arbitrary-insertion Ward theorem, interchange with an unevaluated path-integral limit, or physical positivity theorem is imported. [Same-assistant self-check](../01_jensen/01_mellin_curvature/07_donaldson_witten_theory/reviews/04_MC07_B03_BOUNDARY_WARD_SELF_CHECK_20261102.md); no new comparison domain.
