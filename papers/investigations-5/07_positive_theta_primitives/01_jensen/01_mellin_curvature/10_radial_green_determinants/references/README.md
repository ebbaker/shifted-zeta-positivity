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
