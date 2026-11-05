# Source inspection for the radial Green comparison

4 November 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance; actual gpt-6-astra (Codex), effort max.

The canonical records and reusable BibTeX remain in the positive-theta
investigation's [catalog](../../../../references/README.md) and
[bibliography](../../../../references/sources.bib). No new research article
or PDF was introduced here. Existing versions and PDF receipts remain
unchanged. This records selected primary-source reinspection for
[RGD Note01](../notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md)
and its execution handoff, not a full literature audit.

- **NIST Digital Library of Mathematical Functions**, online
  [20.7.32](https://dlmf.nist.gov/20.7.E32), read 4 November 2026.
  At z=0, tau=i*R^2, the theta3 transformation gives
  Theta(R)=R^(-1)*Theta(1/R). This checks the inherited normalized
  reflection used for b=1/16; the endpoint differentiation is in Note01
  and the inherited Green derivation. Canonical BibTeX key:
  NISTDLMFPositiveThetaPrimitives. Online documentation, no PDF needed.
- **Olga M. Katkova, Multiple positivity and the Riemann zeta-function**,
  [arXiv:math/0505174v1, 10 May 2005](https://arxiv.org/html/math/0505174v1),
  Computational Methods and Function Theory 7 (2007), 13–31.
  Rechecked (4)–(5) and Theorem 1: b_j=8*4^j*c_j and PF44.
  This is the known finite-order baseline, not a new bound or a strictness
  theorem supplied by the present calculation. The full paper and cited
  sector theorem were not newly audited. Canonical record and archived
  reading-copy receipt: [formulation sources](../../../../references/04_RH_FORMULATION_SOURCES_20261101.md#katkova0505174v1).
  BibTeX key: Katkova0505174v1.
- **mpmath documentation, Numerical integration (quadrature)**,
  [official documentation](https://mpmath.org/doc/current/calculus/integration.html),
  page labeled 1.3.0, read 4 November 2026. Checked the breakpoint-list,
  tanh-sinh method, maxdegree and estimated-error options for the future
  fixed E03 diagnostic. The executing session must record its installed
  version. This documentation supplies no interval certification and no
  numerical calculation was run in B01.

## E02 rigorous acquisition API inspection

4 November 2026. Prepared for Edward Baker with substantial LLM assistance;
actual **gpt-6.1-sol (Codex), effort ultra**, chat0003.

- [python-flint acb.integral](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral),
  documentation labeled 0.9.0, and the installed method docstring: inspected
  the callback analytic flag, exact endpoint usage, tolerance goals and
  work-limit options. E02's integrand is entire, as proved in Note03.
- [python-flint arb](https://python-flint.readthedocs.io/en/latest/arb.html):
  inspected interval semantics, outward upper/lower/abs_upper endpoints,
  and exact midpoint/radius man_exp serialization. Decimal displays are
  reading aids, not certificate decision values.
- [FLINT author-hosted integration documentation](https://fredrikj.net/fdoc/html/acb_calc/integrate.html),
  labeled 3.7.0-dev, generated October 2026: inspected the rigorous
  enclosure contract, Gauss–Legendre/bisection route and distinction
  between tolerance goals and returned enclosures. The canonical link
  https://flintlib.org/doc/acb_calc/integrate.html was unavailable through
  the web reader. The executed library is FLINT **3.6.0**, via python-flint
  **0.9.0**; no claim of a 3.7 executable or full library audit is made.

These are software-documentation inspections, not new research articles;
no third-party PDF was downloaded or added. Note03 and the E02 certificate
record the actual arithmetic versions, code/input hashes and trust limits.

## E04 r2 actual-version control-flow inspection

4 November 2026, **gpt-6.1-sol (Codex), effort ultra**, for Edward Baker
with substantial LLM assistance, chat0003. Rechecked the python-flint
0.9.0 integration/Arb documentation above and selected
[FLINT v3.6.0 integration source](https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_calc/integrate.c).
The tagged source shows the direct enclosure, bounded Gauss–Legendre
attempt, and addition of remaining enclosures when stopping. This adds
an actual-version check alongside the prior 3.7.0-dev documentation;
it is not a complete library or numerical-algorithm proof audit. No new
paper/PDF, library installation or integration replay was introduced.

## B03/B02 mechanism and baseline reinspection

4 November 2026, for Edward Baker with substantial LLM assistance;
actual **gpt-6-astra / ultra**, chat0004. Rechecked the existing versioned
Katkova primary text: Theorem 2 and Proposition 1 (fixed-order eventual
positivity), Lemma 1 equation (12) (contour determinant), Theorem C and
Lemma 3 (the entire PF and strict-minor bridges). Selected passages only;
no complete asymptotic proof audit. Notes07–08 give their exact uses.

Rechecked the existing
[Michałowski catalog entry](../../../../references/04_RH_FORMULATION_SOURCES_20261101.md#Michalowski260716795v1)
and [version 1 primary text](https://arxiv.org/html/2607.16795v1),
Theorem 1.1 and selected Sections 3–6. Note08 Section 7 records the
baseline consequence and scoped majorant deduction. Earlier PDF provenance
is unchanged; the proof and certificates remain unaudited here.

[Additional background](01_ADDITIONAL_BACKGROUND_20261104.md) records
Rietsch's newly discovered version 3, with
[local BibTeX](additional_sources.bib) and an
[outside-Git PDF receipt](REFERENCE_RECEIPT_20261104.json).
It is not a premise of the new results. Existing Fomin–Zelevinsky
catalog/provenance is linked there rather than duplicated.
