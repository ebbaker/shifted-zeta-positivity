# Pair-product, sector and control sources

4 November 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance; actual **gpt-6-astra / ultra**, chat0007.
Selected primary passages for [Note14][note], not a full literature or
priority audit. Existing source records and frozen manifests are unchanged.
New citation keys are in [pair-reference BibTeX](pair_reference_sources.bib).

## Existing sources reused with explicit scope

**Olga M. Katkova, Multiple positivity and the Riemann zeta-function**,
[arXiv:math/0505174v1](https://arxiv.org/html/math/0505174v1), version wrapper
10 May 2005. Reuse canonical key Katkova0505174v1, the parent
[record](../../../../references/04_RH_FORMULATION_SOURCES_20261101.md#katkova0505174v1)
and its existing PDF receipt. Selected Section1 passages were rechecked:
xi1's order one-half, Hadamard product with summable reciprocal zeros,
TheoremB's sector implication, and the displayed Theorem1 argument.
The first two support Note14(2); the sector result identifies prior art.
No numerical PF cutoff is imported.

**Source qualification:** TheoremB displays the angle pi*m/(m+1).
Theorem1's proof displays the zero-free angle 43pi/44 but labels its
consequence PF44; that displayed implication corresponds to m=43.
This is an apparent integer mismatch in the displayed argument, not a
finding that PF44 is false. Earlier PF44 mentions retain reported status;
no frozen assessment is silently rewritten. Note14 derives its own
symbolic condition and makes no integer-coverage claim.

**Odlyzko1987AuthorCopy**, existing
[References02](02_RECIPROCAL_COMPARISON_AND_FINITE_ZERO_SOURCES_20261104.md)
and its unchanged receipt: selected Section2 equations2.3,2.5,2.6 rechecked
for zero counting with multiplicity. This supplies the inherited radial
count and summability, not a spacing conjecture. No new PDF or zero data.

**EtingofRepresentationTheory20110110**, existing [References03](03_GAUSSIAN_REFERENCE_AND_SCHUR_BACKGROUND_20261104.md)
and [receipt](REFERENCE_RECEIPT_B02_R3_20261104.json): additional
[author-PDF](https://math.mit.edu/~etingof/replect.pdf) inspection of
Sections4.18–4.21, especially Theorem4.63 identifying Schur polynomials
as polynomial GL characters. Restriction to finite block groups and
nonnegative multiplicities justifies the standard pair branching in
Note14. The two-variable multiplier is derived directly there.
This is a dependency of Note14, while its optional status for Note12
remains unchanged. No full book audit or new reading copy.

**García-García–Tierz**, existing References02: accepted Section2.1
conventions continue to supply elementary/complete duality and the
rectangle (r^k), with zero negative coefficients. The finite reversal
identity in Note14 is derived explicitly.

## NIST DLMF online passages

Version1.2.8, released 15 September 2026; retrieved 4 November 2026.
Reuse the parent's NISTDLMFPositiveThetaPrimitives citation key.
Checked [25.4.3–4](https://dlmf.nist.gov/25.4) and
[25.10(i)](https://dlmf.nist.gov/25.10.i) for xi normalization, reflection,
strip and conjugation symmetry. Checked [18.12.10](https://dlmf.nist.gov/18.12.E10)
and [18.5.2](https://dlmf.nist.gov/18.5.E2) for the Chebyshev-U generating
function and trigonometric representation. Their power-series identity
has radius |w|<1; coefficient identities extend algebraically.
These are standard inputs, not a canonical determinant-sign theorem.
Online records require no artificial PDF copies.

## Classical sector result and inspected author exposition

**I. J. Schoenberg**, *A note on multiply positive sequences and the
Descartes rule of signs*, Rendiconti del Circolo Matematico di Palermo,
series2, volume4 (1955), pages123–131,
[DOI10.1007/BF02846031](https://doi.org/10.1007/BF02846031).
Publisher metadata checked. Original full text is subscription-only
through the inspected source; no access bypass, PDF copy or original
proof audit is claimed. The theorem is also stated in the existing
Katkova primary research article above.

**Apoorva Khare**, *Matrix Analysis, Pólya frequency functions, and
Preservers of (Total) Positivity*, undated 329-page author-hosted text,
[public PDF](https://math.iisc.ac.in/~khare/teaching/Math341-notes.pdf).
The introduction says it grew from Spring2018/Fall2019 courses; these
are course dates, not an inferred date for the retrieved version.
Theorem30.27, printed pages210–211, was inspected for the classical
sector condition and its conjugate-quadratic/convolution proof. This
confirms that angular finite-order positivity is established background.
The exact retrieved bytes are retained outside Git with a
[reading-copy receipt](REFERENCE_RECEIPT_B02_R4_20261104.json).
Selected passages only; the original Schoenberg paper remains unexamined.

No external source supplies Note14's canonical all-order residual sign.
The explicit diagonal construction and its constants are proved in-note;
no novelty claim is made for the general instability of finite positivity
under complex-root perturbations.

[note]: ../notes/14_RGD_B02_R4_ENDPOINT_PAIR_REFERENCE_AND_DIAGONAL_CONTROL_20261104.md
