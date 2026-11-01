# Annotated bibliography for positive theta primitives

31 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **xhigh**.

This bibliography supports the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md). It covers the classical Riemann representation, demonstrated sign and zero mechanisms, and a small set of adjacent tools. It is a selected bibliography, not an exhaustive survey or a full proof audit. The first reading priorities are Riemann’s normalization, the Hardy discussion in Dixit et al., and Csordas–Norfolk–Varga’s integrated kernel.

Inspection records are inherited from Investigation05’s [classical-source record](../../05_radial_theta_collision_geometry/references/13_RIEMANN_THETA_MELLIN_ATTRIBUTION_20261028.md) and [31 October literature record](../../05_radial_theta_collision_geometry/references/21_POSITIVE_THETA_PRIMITIVE_LITERATURE_SOURCES_20261031.md). Establishing this investigation does not turn selected-passage inspection into a complete reading. The entries below are the local annotations for this investigation; those earlier records retain their historical provenance. Original short annotations and formulas are used rather than copied abstracts.

The [BibTeX file](sources.bib) is reusable. The [catalog](sources.json) records versions and applications. The [PDF receipts](PDF_RECEIPTS_20261031.json) reuse existing external reading copies without duplicating PDFs in Git; hashes identify files, not verified mathematics. Riemann was retrieved on 28 October, the other PDF records on 31 October 2026. Sato remains an unsuccessful retrieval, and DLMF remains an online reference.

## Riemann1859

Bernhard Riemann. *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse*. Monatsberichte der Berliner Akademie, November 1859. Version read: David R. Wilkins’s English translation, *On the Number of Prime Numbers less than a Given Quantity*, preliminary version December 1998. [Public translation](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf).

**Checked passage.** Printed p. 3 (PDF page 4), extracted text: theta Mellin integral, Jacobi transformation, and split-at-one continuation. This was selected-passage inspection on 28 October 2026, not a reading of the full paper or its prime-counting argument.

**Use and scope.** Section 1 of the brainstorm rewrites this scalar formula in the p, G, H normalization and shows the substitution explicitly. The unsplit Mellin integral initially requires Re(s)>1; the split expression continues it. The source does not use this investigation’s notation or supply the separate three-dimensional construction. PDF size, SHA-256, and existing external path are in the receipt manifest.

## NISTDLMF

National Institute of Standards and Technology. *Digital Library of Mathematical Functions*. Online version recorded in the prior inspection: 1.2.8, released 15 September 2026. [Xi normalization, 25.4.4](https://dlmf.nist.gov/25.4.E4); [theta Mellin representation, 25.5.13](https://dlmf.nist.gov/25.5.E13); [theta-tail convention, 25.5.14](https://dlmf.nist.gov/25.5.E14).

**Checked passages.** These three formulas were inspected on 28 October 2026; the Mellin formulas were rechecked on 29 October in Investigation05. Related theta inversion is [20.7.32](https://dlmf.nist.gov/20.7.E32). Selected formulas, not entire chapters, were used.

**Use and scope.** Fixes the factor one-half in xi and the rational boundary term in Riemann’s formula. DLMF attributes the theta integral to Titchmarsh (1986), p. 22; that book was not separately inspected here. No theorem about the physical signed interaction is inferred from the representation alone. No artificial PDF is retained.

## Csordas13090055v2

George Csordas. *Fourier transforms of positive definite kernels and the Riemann xi-Function*. arXiv:1309.0055v2, 21 February 2014. [Primary source](https://arxiv.org/html/1309.0055v2).

Checked or discovered passages: Theorems 3.4–3.7; Theorem 4.2; Open Problem 4.7.

Selected statements and the full-line normalization in (3.11)–(3.14) checked. Pólya's convex-kernel criterion and the associated-kernel characterization are used as classical tools. Theorem 4.6 switches to a half-line transform; the brainstorm derives constants from the full-line statement instead of copying (4.7).

PDF receipt: see the entry for `Csordas_1309.0055v2.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Sections 2 and 5: separate the convex primitive criterion from positive definiteness of associated kernels. The latter is stronger than pointwise positivity. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## CNV1986Turan

George Csordas, Timothy S. Norfolk, Richard S. Varga. *The Riemann Hypothesis and the Turan Inequalities*. Transactions of the AMS 296(2) (1986), 521–541. [Primary source](https://www.math.kent.edu/~varga/pub/paper_157.pdf).

Checked or discovered passages: Printed pp. 522–524: equations (1.8)–(1.12), Theorem 1.1, Proposition 2.1.

Selected primary pages inspected as rendered images because the PDF is scanned. The integrated kernel is K(t)=integral from t to infinity of Phi(sqrt(u)) du. It is not the half-line primitive p. The proof treats moment indices at least two analytically and the first separately; the full 21-page proof was not audited.

PDF receipt: see the entry for `Csordas_Norfolk_Varga_1986_Turan.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 4: the principal precedent for integrating first and then proving a stronger shape inequality. K is explicitly distinguished from p and G. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## Romik190206330v3

Dan Romik. *Orthogonal polynomial expansions for the Riemann xi function*. arXiv:1902.06330v3, 5 May 2019; related published article Acta Arithmetica 200 (2021), 259–329. [Primary source](https://arxiv.org/html/1902.06330v3).

Checked or discovered passages: Section 3.1, (3.1)–(3.5), Theorem 3.1; introduction; Section 4.2 discovered but excluded from the requested primitive-centered review.

Version-specific section numbers refer to v3, not the later journal article. Coefficient positivity and compact convergence were checked. This is an adjacent basis-change approach, not a direct theorem about the half-line primitive p. No assertion that real-rooted basis functions force real-rooted partial sums.

PDF receipt: see the entry for `Romik_1902.06330v3.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 6: a possible change of basis with positive coefficients. No real-rootedness conclusion is imported from coefficient signs alone. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## BianePitmanYor9912170v1

Philippe Biane, Jim Pitman, Marc Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*. Bulletin of the AMS 38(4) (2001), 435–465; version read arXiv:math/9912170v1, 21 December 1999. [Primary source](https://arxiv.org/html/math/9912170v1).

Checked or discovered passages: Section 2.1, (12)–(19); Section 2.2, Proposition 1, (20)–(25); Section 3.1, (29).

Selected transformations and probability identities checked. The HTML shows an apparent recompilation date; bibliographic provenance uses the submission record and publication date. Positivity and infinite divisibility apply to the specified variables/transforms, not automatically to the logarithmic variable relevant to xi zeros.

PDF receipt: see the entry for `Biane_Pitman_Yor_math9912170v1.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 6: retain the precise random variable and transform when translating theta identities into probabilistic language. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## DixitEtAl171208435v1

Atul Dixit, Rahul Kumar, Bibekananda Maji, Alexandru Zaharescu. *Zeros of combinations of the Riemann Xi-function and the confluent hypergeometric function on bounded vertical shifts*. arXiv:1712.08435v1, 22 December 2017. [Primary source](https://arxiv.org/html/1712.08435v1).

Checked or discovered passages: Introduction, (1.1)–(1.6); Theorem 2; Section 2 boundary calculation at z=0, (2.5)–(2.10) and Lemma 6.

Direct link between the undifferentiated theta expression and Hardy's zero argument checked. The brainstorm only uses the ordinary z=0 circular approach to the theta boundary, with its decay independently explained; it does not import the paper's more general all-route boundary assertion or audit its hypergeometric extension.

PDF receipt: see the entry for `Dixit_Kumar_Maji_Zaharescu_1712.08435v1.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 3: the principal modern source for Hardy’s use of the same undifferentiated theta expression. Hardy’s original 1914 paper was not separately inspected; attribution is through this account. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## Sato2005PolyaCriterion

Ken-iti Sato. *Remarks on Polya's theorem on characteristic functions*. Institute of Statistical Mathematics, Cooperative Research Report 175, 133–145; author PDF dated 13 December 2004. [Primary source](https://www.ksato.jp/pdf/polya6.pdf).

Checked or discovered passages: Discovery: indexed first-page Theorems 1.1–1.2 and author bibliography.

Full primary PDF retrieval failed (web timeout/502 and verified-certificate download failure). Retained as a reading lead, not an imported theorem source. The convex criterion used in the brainstorm is checked directly in Csordas Theorem 3.4. Pólya's 1949 original is bibliographically identified there but was not separately read.

PDF receipt: see the entry for `Sato_Polya_characteristic_functions_20041213.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Secondary reading lead for the convexity criterion. No dependent theorem relies on the unavailable full text. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## Sra2026SharpOrderFourV1

Suvrit Sra. *Sharp order-four sign regularity of a Jacobi theta kernel*. Author-hosted preprint v1, 10 October 2026. [Primary source](https://suvrit.github.io/papers/csordas/).

Checked or discovered passages: Opening theorem statements and Section 4 consequences.

Recent preprint: selected claims checked, not independently verified; interval certificates were not rerun. Concerns the square-root-rescaled differentiated theta kernel, not the undifferentiated primitive. Included only as a current finite-order sign result and a scope warning.

PDF receipt: see the entry for `Sra_csordas_v1_20261010.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 6 background only: a recent finite-order claim about a different kernel. It is not an input to the opening arguments. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## Sra2026XiPositivityV2

Suvrit Sra. *On some positivity properties of the Riemann Xi function*. Author-hosted preprint v2, 29 October 2026; separate site/version numbering. [Primary source](https://suvrit.github.io/papers/riem-xi/).

Checked or discovered passages: Theorems 1.1–1.3; Section 2.1 inputs.

Selected claims and finite verified-zero dependence checked, not independently audited. The reciprocal-transform densities are different from the primitive in this investigation. The reported PF256 and finite-interval generalized Laguerre results are not treated as a new global theta sign bound.

PDF receipt: see the entry for `Sra_riem_xi_v2_20261029.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 6 background only: preserve the finite verified-zero and finite-order qualifications. It is not an input to the opening arguments. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).

## GriffinEtAl190207321v1

Michael Griffin, Ken Ono, Larry Rolen, Don Zagier. *Jensen polynomials for the Riemann zeta function and other sequences*. arXiv:1902.07321v1, 19 February 2019; PNAS 116(23) (2019), 11103–11108. [Primary source](https://arxiv.org/html/1902.07321v1).

Checked or discovered passages: Introduction (1)–(5); Theorems 1–3.

Fixed-degree eventual hyperbolicity and its Hermite limit checked. The sufficiently large shift depends on degree. This does not establish the all-degrees/all-shifts RH criterion and is not a uniform statement about physical heat time.

PDF receipt: see the entry for `Griffin_Ono_Rolen_Zagier_1902.07321v1.pdf` in [the manifest](PDF_RECEIPTS_20261031.json).

**Use in this investigation.** Section 4: a subsequent coefficient-based result with a fixed-degree quantifier, distinct from a global all-degrees conclusion. See the [opening brainstorm](../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).
