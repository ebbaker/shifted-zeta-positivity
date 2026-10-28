# Classical inputs for the projected evolution and elliptic response

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008. Selected passages inspected; no complete lecture-note audit.

These inputs support [Note23](../notes/23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md). Its projected operator, explicit annular coercivity constant, source-cost comparison, interface accounting and signed adjoint are derived there. No novelty claim is made for semigroup or elliptic existence theory.

## Roland Schnaubelt

**Lecture Notes: Evolution Equations**, version dated **19 March 2026**, based on the winter 2023/24 course. [Author's KIT PDF](https://iana.math.kit.edu/downloads/iana3/schnaubelt/Skripten/evgl-skript.pdf). Retrieved 27 October 2026 local date.

Checked Theorem1.50 and the form construction (1.31)–(1.32), printed pp.41–42; Corollary2.28, printed p.66; Example2.30, printed p.67; Theorem3.4, printed pp.74–76. These provide coercive-form inversion, analytic semigroups for densely defined self-adjoint dissipative operators, the smooth-domain Dirichlet Laplacian domain, and bounded perturbations. Note23 applies them to −A on the zero-average Hilbert space, verifying symmetry, domain, density, and coercivity. Smooth annular boundaries and bounded χ are retained. The exterior inverse instead uses its mass term for coercivity. No positivity-preserving property of the projected semigroup is imported.

External reading copy: `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Schnaubelt_Evolution_Equations_20260319.pdf`; **948351 bytes**; SHA-256 `5451d43af7b329412a0d78835d76230e13e0f6cd9635b1bb1b3be01198f07791`. The URL is mutable; this hash identifies the inspected retrieval, not mathematical correctness.

## John K. Hunter

**Notes on Partial Differential Equations**, revision **18 June 2014**, University of California, Davis. [Author's PDF](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf). Retrieved 27 October 2026 local date.

Checked Theorem4.20, printed p.103, and Section4.12, printed pp.114–116, especially Theorems4.30–4.31 and Corollary4.32. The Hilbert-space Lax–Milgram theorem applies to the exterior mass form without a bounded-domain Poincaré assumption. The displayed global boundary-regularity theorems assume bounded smooth domains; Note23 uses them on the annulus and their localized boundary argument near r=1. It asserts only local regularity on the exterior domain, including across the artificial faces. Higher regularity requires the corresponding source regularity; extension by zero does not create a smooth global parabolic solution. These passages supply no collision or sign theorem.

External reading copy: `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Hunter_Notes_on_Partial_Differential_Equations_20140618.pdf`; **1597256 bytes**; SHA-256 `0dbade1806f7a1ea79cc444a0eecfe19e157b286c964f1f48f2d744c460c12dd`. The PDF remains outside Git. No whole-book reading or independent theorem verification is claimed.

The spherical eigenvalue convention needed for the constant2 in Note23 remains the existing [DLMF annotation09](09_SPHERICAL_LAPLACIAN_AND_ANGULAR_FLOW_CONVENTIONS_20261027.md); it is not a new source entry. The [catalog](sources.json) and [BibTeX](sources.bib) retain reusable identifiers and these retrieval receipts.

## Additional heat passages for Note25

The same Hunter PDF was consulted for Section5.1, formulas(5.5)–(5.6), printed pp.129–130, and Theorem5.5 with the Gaussian normalization discussion on printed p.131. These support the explicit heat kernel, positive-time smoothing and initial L¹ convergence. Section5.B.3, printed p.171, was also inspected for the L¹ Fourier convention. Note25 supplies its own Gaussian-convolution argument for cosine-transform uniqueness, its theta normalization, conservation by Fubini, and its central moment-remainder calculation. The ordinary heat theory is classical; no collision-specific result is imported from Hunter. The existing archived reading copy and retrieval hash above are retained.
