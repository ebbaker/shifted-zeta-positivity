# B07 certified evaluator source use

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, authenticated chat0006. Actual model
and effort are unavailable in the recorded configurations. Root alone
authored this record.

[Note13](../notes/13_TND_OC_B07_COMPLETE_DIVISOR_AND_GAUSSIAN_EVALUATOR_20261108.md)
uses certified complex function evaluation and a complete contour count.
The stability and quadrature constants are derived there. No zero list,
contour certificate or pair value has been acquired.

## Primary passages inspected

- **NIST DLMF, §3.5(v), Gauss Quadrature**, [online section](https://dlmf.nist.gov/3.5#v).
  Retrieved 8 November 2026. Inspected positivity of Christoffel weights,
  the degree-2n remainder in 3.5.19–20 and the Gauss–Legendre specialization
  3.5.21. These supply polynomial exactness and positive weights for the
  normalized interval. Note13 derives its separate analytic-ellipse error;
  no tabulated decimal node is treated as an exact algebraic input.
- **NIST DLMF, §25.10(i), Distribution**, [online section](https://dlmf.nist.gov/25.10).
  Retrieved 8 November 2026. The opening paragraphs locate nontrivial zeros
  in the open critical strip and distinguish this unconditional statement
  from RH. Equations 25.10.1–2 give the real Hardy Z-function. Used for the
  finite canonical rectangle and the optional real sign test; no global
  critical-line claim is imported. Selected passage inspection only.
- **python-flint documentation, displayed version 0.9.0**:
  [acb](https://python-flint.readthedocs.io/en/latest/acb.html) and
  [arb](https://python-flint.readthedocs.io/en/latest/arb.html), retrieved
  8 November 2026. Inspected complex/real ball representations, zeta,
  zeta_zero/zeta_zeros, zeta_nzeros, absolute bounds and unique_fmpz.
  These identify candidate APIs; they are not a completed computation.
  The E09 contract requires interval evaluation on entire contour segments.
  It treats proposed zero ordinates only as candidates and demands a
  separate complete winding count. Actual installed versions and finite
  enclosures must be recorded during execution.
- **Arb 2.23.0, acb_dirichlet**, [archived official documentation](https://arblib.org/acb_dirichlet.html),
  sections “Riemann zeta function zeros” and “Hardy Z-functions”, retrieved
  8 November 2026. Inspected the descriptions of Turing counting,
  multiplicity-sensitive N(t), real-zero isolation and zeta-zero wrappers.
  This is archived documentation, not the installed runtime. No
  implementation-wide correctness audit is claimed. E09's selected
  completeness proof is the independently checked contour partition.
- **FLINT v3.3.1**, [zeta_zeros.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/zeta_zeros.c),
  copyright Juan Arias de Reyna and D.H.J. Polymath, and
  [hardy_z_zero.c](https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/acb_dirichlet/hardy_z_zero.c),
  copyright D.H.J. Polymath and Fredrik Johansson. Retrieved 8 November
  2026. The complete small wrapper and selected refinement passages were
  inspected: the wrapper puts the proposed zeros on Re(s)=1/2, and the
  refinement uses definite endpoint signs. Neither inspection establishes
  completeness of an arbitrary returned list. This is the reason for
  E09's separate full-complex count, not an allegation of a library defect.

The current FLINT documentation entry redirected to a development version
with an October 2026 documentation-revision notice. It was discovery
material only. Requests for guessed hardy_z_zeros.c and zeta_nzeros.c paths
returned 404; gram.c was unavailable. A bounded direct GitHub directory
retrieval failed at local DNS resolution. No missing code was inferred.

## Reused analysis and storage

The canonical F=D H0 identity is inherited from manuscript section 4 and
the accepted E02/E07 scope. The argument principle source already belongs
to the B03 record in [the reference index](README.md), Tao's 246A Notes4,
Theorem32/Corollary33. Note13 supplies the finite interval-image homotopy
test explicitly; citing the argument principle does not supply its inputs.

These are online documentation/source records; no article PDF was
discovered or downloaded. No artificial PDF, local archive hash or
novelty claim is supplied. [Bibliography](b07_certified_evaluator_sources.bib).
Follow [REFERENCE_WORKFLOW](../../../../../../REFERENCE_WORKFLOW.md) and
[avoid16](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
