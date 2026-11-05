# Reciprocal comparison and finite-zero source records

4 November 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance; actual **gpt-6-astra / ultra**, chat0004.
These are selected primary-source checks for [Note10][note], not full
paper or certificate audits. No numerical certificate was imported or run.
Public reading copies are outside Git; [receipts][receipts] identify them.
Bibliography entries are in [additional_sources.bib](additional_sources.bib).

## KenanFifteenShifts2026

kenan.works, *The first fifteen Xi-coefficient shifts are nonnegative at
every Toeplitz rank*, web note dated 22 July 2026.
[Primary page](https://kenan.works/posts/fifteen-shifts-of-xi/).
No personal byline was exposed in the inspected text; the site is used
as the attribution, not an inferred identity.

The page describes the same reciprocal rectangular-duality/pole-margin
mechanism used in Note10, and reports all-rank nonnegativity for k≤15.
This is prior mechanism disclosure, not a premise validating Note10's
self-contained proof. Direct opening returned HTTP 502; primary-page
search-index text was inspected. The named supporting notebooks
C-0187, C-0026, K-0055 and C-0191 were not located or audited. No authorized
PDF was identified. Reported coverage must not be promoted to locally
verified evidence or a growing-index theorem.

## GarciaGarciaTierz2020Accepted

David García-García and Miguel Tierz, *Toeplitz minors and specializations
of skew Schur polynomials*, Journal of Combinatorial Theory, Series A
172 (2020), 105201. DOI
[10.1016/j.jcta.2019.105201](https://doi.org/10.1016/j.jcta.2019.105201).
[Repository accepted manuscript](https://repositorio.iscte-iul.pt/bitstream/10071/20917/1/Toeplitz%20minors_postprint.pdf),
deposited 14 December 2020.

Section 2.1, printed p.3 / PDF p.4, gives H(z)E(−z)=1 and the two
Jacobi–Trudi identities. Checked as algebraic background/conventions.
Note10 supplies its own finite Toeplitz-inverse proof. No positivity or
asymptotic theorem from this paper is imported.

## PlattTrudgian200409765v1

David J. Platt and Timothy S. Trudgian, *The Riemann hypothesis is true
up to 3·10^12*, Bulletin of the London Mathematical Society 53(3)
(2021), 792–797; first published 22 January 2021.
[DOI 10.1112/blms.12460](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.12460),
[arXiv:2004.09765v1, 21 April 2020](https://arxiv.org/abs/2004.09765v1).

The published abstract explicitly includes simplicity and the critical-line
location through the stated height. A contributor inspected v1 Theorem 1
and §2's counting argument; the coordinator checked the published abstract.
Note10 uses only the finite-height consequence through 20, together with
the next source's first-zero locations. Published computational input,
not a local replay of the calculation or certificates. The archived
preprint and the published statement are distinguished deliberately.

## Odlyzko1987AuthorCopy

Andrew M. Odlyzko, *On the Distribution of Spacings Between Zeros of the
Zeta Function*, Mathematics of Computation 48(177) (1987), 273–308.
[DOI 10.1090/S0025-5718-1987-0866115-0](https://doi.org/10.1090/S0025-5718-1987-0866115-0),
[author-hosted reading copy](https://www-users.cse.umn.edu/~odlyzko/doc/arch/zeta.zero.spacing.pdf).
This 63-page author copy has its own pagination; no explicit version
number is displayed.

Checked §2, printed pp.7–8: zeros are ordered with multiplicity, the
first two ordinates lie in (14,15) and (21,22), and (2.3), (2.5), (2.6)
supply the ordinary zero-count asymptotic. These support Note10 §§6,8.
No spacing conjecture or statistical inference is used.

## SraXiPositivityV3 — newer version of an existing catalogued work

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
author-site v3, 2 November 2026, 53 pages; separate arXiv identifier
2611.02944v1. [Author version page](https://suvrit.github.io/papers/riem-xi/),
[versioned PDF](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf).
The [canonical parent record](../../../../references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md#sra2026xipositivityv2)
retains its earlier v2 annotation and receipt. This is a local version
supplement, not replacement of that provenance.

A read-only contributor inspected Appendix C, Lemma C.15, printed p.36,
for finite-residue expansions with contour remainders. Its objects are
the continuous densities Θ and Λ, not the coefficient rectangles D_{r,k}.
The coordinator checked the author page's v3 metadata. No theorem or
certificate is imported into Note10; no full-proof audit is claimed.
The new version is recorded because it was discovered in this search,
not as permission to extend the bounded B02 task.

[note]: ../notes/10_RGD_B02_R2_RECIPROCAL_POLE_INDUCTION_AND_SCOPED_STOP_20261104.md
[receipts]: REFERENCE_RECEIPTS_B02_R2_20261104.json
