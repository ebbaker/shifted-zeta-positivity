# References for the flat quaternion Dirac operator

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Selected passages support the operator conventions in [Note12](../notes/12_FLAT_QUATERNION_DIRAC_AND_DYADIC_LATTICE_H_20261027.md). The lattice shell theorem is inherited from [annotation05](05_JACOBI_DERIVATIVE_AND_TERNARY_LATTICE_SUMS_20261027.md), not imported from the articles below.

## Sudbery quaternionic analysis

**Anthony Sudbery**, *Quaternionic analysis*, Mathematical Proceedings of the Cambridge Philosophical Society 85 (1979), 199–225. [Public reprint](https://dougsweetser.github.io/Q/Stuff/pdfs/Quaternionic-analysis.pdf). The retrieved PDF is a 28-page public reprint; no immutable reprint revision date is asserted.

Checked equations (2.33)–(2.35), PDF page 7, defining left and right Fueter operators with a factor 1/2 and their Laplacian factorization. Note12 uses the unnormalized left operator partial_t+sum e_i partial_i and derives D_X^2=-Delta_X directly. No integral-representation theorem from this paper is imported. The earlier [standard Fueter lift](../../../investigations-2/active/21_quaternion_theta_geometry/notes/3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md) is a separate internal predecessor.

Reading copy retrieved 27 October 2026:

- Source: https://dougsweetser.github.io/Q/Stuff/pdfs/Quaternionic-analysis.pdf
- Archive: `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Sudbery_Quaternionic_Analysis_public_reprint.pdf`
- Bytes: 174244.
- SHA-256: `c7d1d8326367dbeedaabfd3e134e024c4cf2ab2d5a9d3365a8a8d6df1b7ef9fb`.

## Cerejeiras Kähler and Kraußhar on parabolic Dirac operators

**Paula Cerejeiras, Uwe Kähler, Rolf Sören Kraußhar**, *Applications of parabolic Dirac operators to the instationary viscous MHD equations on conformally flat manifolds*, [arXiv:1804.09551v1](https://arxiv.org/abs/1804.09551v1), submitted 24 April 2018; the PDF title page is dated 26 April 2018. [Versioned PDF](https://arxiv.org/pdf/1804.09551v1).

Checked title metadata and Section 2.1, printed page 3: quaternion multiplication, Euclidean D=sum e_i partial_i, and D^2=-Delta. These are the only operator conventions imported. The subsequent enlarged parabolic system and Gaussian kernel were inspected for orientation, but their normalization and algebra are not relied on. In particular, no general-k formula, MHD existence result, spinor-index theorem or magnetic heat kernel is imported. The source's parabolic time is not identified with Newman time in Note12.

Reading copy retrieved 27 October 2026:

- Source: https://arxiv.org/pdf/1804.09551v1
- Archive: `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/1804.09551v1.pdf`
- Bytes: 222144.
- SHA-256: `929da05834de49b72c5d820924af321f7cdde88a556d199abe0c29e87ac06857`.

Both PDFs remain outside Git under the repository reference policy. Their hashes identify the retrieved files, not the correctness of their mathematical claims. This is selected-passage inspection, not a complete audit of either article.
