# Sources for the signed-averaging decision

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

Companion to Jensen [Note05](../01_jensen/notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md).
The first two classical sources support general mathematical tools. A third entry records a background lead. Neither
establishes the proposed canonical-theta hypotheses. Reading copies are
outside Git; see the [receipts](PDF_RECEIPTS_SIGNED_AVERAGING_20261101.json).

## FortuinKasteleynGinibre1971

C. M. Fortuin, P. W. Kasteleyn and J. Ginibre, *Correlation Inequalities on
Some Partially Ordered Sets*, Communications in Mathematical Physics 22
(1971), 89–103. DOI: [10.1007/BF01651330](https://doi.org/10.1007/BF01651330).
[Primary article, institutional reading copy](https://math.bme.hu/~balint/oktatas/perkolacio/percolation_papers/fortuin_kasteleyn_ginibre.pdf).

**Inspected:** Section 2, pp. 90–91, Proposition 1 and (2.1)–(2.2), including
the support-sublattice discussion; the Proposition 1 page was also visually inspected. It proves nonnegative covariance for
two increasing real functions on a finite distributive lattice when the
measure satisfies the multiplicative meet/join inequality. The support
may be a sublattice. The article's full proof was not independently audited.

**Use and limit:** Note05 checks that inequality directly for its positive
ordered-chamber weight, then supplies a finite-grid limit argument. That
continuous application is our derivation, not a theorem about theta stated
in FKG. The signed function being averaged is allowed to take negative
values; its monotonicity is a separate, unproved theta condition.

## deBoor2005DividedDifferences

Carl de Boor, *Divided Differences*, Surveys in Approximation Theory 1
(2005), 46–69. [Journal/author landing page](https://pages.cs.wisc.edu/~deboor/sat/papers/2/),
[author PDF](https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf).
The PDF is dated 21 December 2004; the journal page gives publication on
14 January 2005 and an arXiv:math/0502036 link. The archived copy is the
author PDF, not an inferred arXiv revision.

**Inspected:** Section 9, pp. 63–65, specifically formula (52) and its
nested-simplex measure on p. 64, also visually inspected. At order two the simplex has area 1/2.
The second divided difference of a function with increasing second
derivative is increasing in each node. The full survey was not audited.

**Use and limit:** Note05 applies this identity to the curve
T = g(R). It does not assume that g second derivative is nonnegative;
only its monotonicity is proposed. The Gaussian check fixes the factor
1/2. Whether the canonical curve has the required third-derivative sign
is the first unpaid source estimate.

## KarlinRinott1980MTP2

Samuel Karlin and Yosef Rinott, *Classes of orderings of measures and
related correlation inequalities. I. Multivariate totally positive
distributions*, Journal of Multivariate Analysis 10(4), December 1980,
467–498. [Publisher page](https://www.sciencedirect.com/science/article/pii/0047259X80900652),
DOI 10.1016/0047-259X(80)90065-2.

**Inspection and use:** Publisher metadata and abstract were readable in
search results; direct article access returned HTTP 403. This is a
background lead only. No PDF was acquired and no theorem is imported.
The selected primary basis for association is FKG Proposition 1.
No comprehensive novelty search for the normalized determinant inequality
has been made.
