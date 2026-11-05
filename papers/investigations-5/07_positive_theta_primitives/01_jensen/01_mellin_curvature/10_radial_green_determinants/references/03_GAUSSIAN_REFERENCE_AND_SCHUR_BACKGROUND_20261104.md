# Gaussian-reference control and standard Schur background

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra / ultra**, chat0007.
Read with the existing [reference index](README.md) and
[additional BibTeX](additional_sources.bib). This adds selected inspected
passages; it is not a full literature or priority audit. [Note12][note]
uses a direct Vandermonde proof, not a new determinant identity.

## NIST Digital Library of Mathematical Functions

Online version 1.2.8, released 15 September 2026; retrieved 4 November
2026. The existing canonical citation key is
NISTDLMFPositiveThetaPrimitives in the parent bibliography. Checked
[Section 4.36, equation 4.36.2](https://dlmf.nist.gov/4.36.E2): the product
for cosh z over its imaginary zeros. Substituting z=ell sqrt(w) supplies
the infinite positive alphabet for Note12 Section7. The strict determinant
consequence is proved there by bidiagonal Cauchy–Binet; it is not an
RH or canonical-theta claim. Online reference; no PDF copy is required.

## Etingof and collaborators: optional standard background

Pavel Etingof, Oleg Golberg, Sebastian Hensel, Tiankai Liu, Alex Schwendner,
Dmitry Vaintrob and Elena Yudovina, **Introduction to representation
theory**, author-hosted lecture-note version dated **10 January 2011**.
[Inspected author PDF](https://math.mit.edu/~etingof/replect.pdf).
Related AMS Student Mathematical Library 59 (2011),
[DOI 10.1090/stml/059](https://doi.org/10.1090/stml/059); related preprint
[arXiv:0901.0827](https://arxiv.org/abs/0901.0827). Do not equate the
inspected January version with an uninspected arXiv version.

A read-only same-model source contributor checked Sections4.15 Theorem4.47
(Frobenius formula), 4.17 Theorem4.53 (hook length), and 4.20 Proposition4.61
(power-sum/Schur change of basis). These identify the standard
representation-theoretic form of the exponential determinant and finite
character expansions. They do **not** supply a theta residual bound.
The final Note12 uses direct matrix algebra instead; this is optional
background found during the bounded attempt, not an additional research
mechanism or a mathematical dependency. No full book reading is claimed.
A public reading copy is archived outside Git; its exact source, size and
hash appear in [the receipt](REFERENCE_RECEIPT_B02_R3_20261104.json).

## Jonathan Novak: optional transposition background

**Math 202B: Lecture 25**, author lecture dated 14 March 2025,
[primary page](https://jinovak.com/2025/03/14/math-202b-lecture-25/),
retrieved 4 November 2026. Theorem25.3 identifies the transposition
class-sum scalar with the sum of Young-diagram contents. Selected passage
checked by the same-model source contributor. It explains a possible
character expansion of the same Gaussian comparison, but no such
classwise payment is used in Note12. No uniform theta estimate or new
positivity coverage follows. Online lecture; no separate PDF obtained.

The existing García-García–Tierz accepted-manuscript record in
[References02](02_RECIPROCAL_COMPARISON_AND_FINITE_ZERO_SOURCES_20261104.md)
already supplies elementary/complete generating functions, rectangular
Jacobi–Trudi duality and zero negative-index conventions. Its archive
receipt and prior source qualifications are unchanged.

[note]: ../notes/12_RGD_B02_R3_GAUSSIAN_REFERENCE_GROWTH_STOP_20261104.md
