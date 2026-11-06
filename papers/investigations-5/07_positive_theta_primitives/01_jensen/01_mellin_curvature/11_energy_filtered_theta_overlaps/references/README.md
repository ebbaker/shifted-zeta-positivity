# References for the radial quantization brainstorm

4 November 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / xhigh**, MC11 history0002. These references support [Brainstorm Note05](../brainstorm/notes/05_MC11_RADIAL_QUANTIZATION_MODEL_COMPARISON_20261104.md); they are not specialist reviews of that note. Public PDFs are retained outside Git; exact source URLs, paths, byte sizes and hashes are in the [download manifest](MC11_BR01_REFERENCE_DOWNLOADS_20261104.json). Citations are in [references.bib](references.bib).

## Camporesi and Higuchi 1995

R. Camporesi and A. Higuchi, *On the eigenfunctions of the Dirac operator on spheres and real hyperbolic spaces*. arXiv:gr-qc/9505009v1, 9 May 1995; Journal of Geometry and Physics 20 (1996), 1–18. [Pinned preprint](https://arxiv.org/abs/gr-qc/9505009v1), [DOI](https://doi.org/10.1016/0393-0440(95)00042-9).

Checked passages: section 3.1, spectrum discussion following equation (3.68), and degeneracy formula (3.54), in the arXiv HTML rendering. Specializing to the unit two-sphere gives self-adjoint Dirac eigenvalues ±n, n>=1, with multiplicity 2n per sign. The paper uses an anti-Hermitian slash operator with imaginary eigenvalues; Note05 inserts the factor -i before squaring. Both signs together give multiplicity 4n for the square. No full-paper audit, novel spectral claim or theta determinant estimate is inferred.

## Lindblom, Taylor and Zhang 2017

Lee Lindblom, Nicholas W. Taylor and Fan Zhang, *Scalar, Vector and Tensor Harmonics on the Three-Sphere*. arXiv:1709.08020v1, 23 September 2017. [Pinned preprint](https://arxiv.org/abs/1709.08020v1), [version read in HTML](https://arxiv.org/html/1709.08020v1).

Checked section 2, equations (1)–(4), (9)–(10): the scalar Laplacian eigenvalues, round metric, separated radial equation, harmonic labels and normalization. On radius one, -Delta has eigenvalue k(k+2); summing the given angular labels yields (k+1)^2 modes. Note05's shift by one and restriction to the rotationally invariant sector are explicitly derived there; the full trace and the restricted trace differ. Vector/tensor sections and numerical results were not audited.

## Lachieze-Rey 2004

Marc Lachièze-Rey, *Laplacian eigenmodes for the three-Sphere*. arXiv:math/0401153v1, 14 January 2004. [Pinned preprint](https://arxiv.org/abs/math/0401153v1).

Discovery and abstract-only inspection: the stated scalar eigenvalues and their multiplicities agree with the checked passages in Lindblom et al. This reference is retained as a related harmonic-analysis source, not as an independently checked proof. Its detailed bases and quotient constructions were not read. A public PDF was archived without treating download as verification.

## MIT Physics 8.05 2007

*Supplementary Notes on Solving the Radial Wave Equation Using Operator Methods*, alternative title *An Introduction to Supersymmetric Quantum Mechanics*, 12 November 2007. Author not identified in the inspected document heading; institution recorded rather than inferred. [Primary course handout](https://web.mit.edu/8.05/handouts/SusyHydrogen2007.pdf).

Checked section 6, equations (54)–(60), printed pages 15–16: centrifugal term, oscillator Gaussian radial ground function, and energies hbar omega (ell+2 nu+3/2). Note05 derives its coupled Hamiltonian and weights directly in its own units. The handout does not propose or assess that theta construction. Only relevant passages were inspected.

## Additional checked use in Note06

4 November 2026, gpt-6-astra / xhigh. [Note06](../brainstorm/notes/06_MC11_ANGULAR_WEIGHT_DIRAC_SQUARE_AND_RADIAL_GREEN_20261104.md) also uses Camporesi–Higuchi equations (5.35)–(5.36) for the squared Dirac curvature term and the section 3 polar-coordinate formula to orient the radial/angular split. The product-cylinder factorization, one-dimensional Green kernels, and Euclidean reduced-operator algebra in Note06 are written out directly and have proof-author checks only. No new paper version or PDF was substituted.

## AR-E01 r1 checked use — 5 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol / ultra**, MC11 history0003. [Assessment03](../reviews/03_MC11_AR_E01_R1_ANGULAR_RADIAL_IDENTITY_ASSESSMENT_20261105.md) and [Note05](../notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md) use Camporesi–Higuchi v1 (3.54), the end of section 3.1 and (5.35)–(5.36), inspected in the same v1 HTML. The previously archived PDF still matches its manifest hash; no PDF was replaced. Inspection covers the imported spectrum, multiplicity and curvature conventions, not the entire paper. The cylinder and Euclidean calculations are derived in the note.

**NIST Digital Library of Mathematical Functions**, §20.7(viii), [equation 20.7.32](https://dlmf.nist.gov/20.7.E32), consulted 5 November 2026. The inspected transformation specifies tau-prime=-1/tau and principal square roots. At z=0 and tau=i r² it gives the unit-weight real-radius Jacobi law for r>0. Note05 derives its harmonic correction and filtered-source defect. This live web reference has no separate PDF archive; no full-chapter audit is claimed.

The frozen r1 catalog hash refers to the pre-assessment catalog. This dated annotation is an output supplement; the [version record](../research-progress/handoffs/05_MC11_AR_E01_R1_INPUT_VERSIONS_20261105.json) distinguishes the consumed input from the updated catalog.


## BR01 r1 reused passages — 5 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / max**, MC11 history0004. [Decision Note06](../notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md) reuses the accepted AR-E01 spectral and Jacobi premises. Camporesi–Higuchi v1 (3.54) and DLMF 20.7.32 with its principal-root convention were re-opened in the same primary-source HTML; no new article, version or reading-copy replacement was introduced. The scalar potential theorem in the E02 request is a future local derivation, not a theorem imported from these sources. No full-paper audit or independent review is claimed.

## Teschl second edition — AR-E02, 5 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol / ultra**, MC11 history0003. Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, AMS Graduate Studies in Mathematics 157 (2014), [author-hosted online edition](https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf). Checked §6.1, Theorem 6.4 and proof, printed p.159 (PDF p.171): bounded real multiplication has relative bound zero, so the self-adjoint domain is preserved. [Note07](../notes/07_MC11_AR_E02_R1_BOUNDED_POTENTIAL_DEFECT_AND_RIGIDITY_20261105.md) proves pointwise kernel positivity/comparison directly. Selected web PDF passages only; no full-book audit.

The [reference receipt](MC11_AR_E02_REFERENCE_RECEIPT_20261105.json) records retrieval limitations: direct download failed and an approved retry timed out, so no local PDF copy/hash is claimed. The public web PDF was readable. No frozen E02 theorem input or issued source catalog version was replaced.


## Ipsen and Rehman 2008 — B01 background

5 November 2026, prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / max**, history0004. Ilse C. F. Ipsen and Rizwana Rehman, *Perturbation Bounds for Determinants and Characteristic Polynomials*, SIAM Journal on Matrix Analysis and Applications **30**(2), 762–776 (2008), [DOI/publisher page](https://epubs.siam.org/doi/10.1137/070704770). Publisher metadata records online publication on 2 July 2008.

Inspection: publisher abstract and bibliographic metadata only. The article concerns absolute and relative determinant sensitivity and related characteristic-polynomial bounds. No theorem, formula or full-paper audit is imported into [B01 Note09](../notes/09_MC11_B01_R1_SIGNED_TRANSFER_ROUTES_AND_SCOPED_STOP_20261105.md); its collected-polynomial payment is derived directly and attributed to the existing RGD method. The [author-hosted PDF](https://ipsen.math.ncsu.edu/ps/simax070477.pdf) is retained outside Git; its path, bytes and SHA-256 are in the [retrieval receipt](MC11_B01_REFERENCE_RECEIPT_20261105.json). Archiving is not proof inspection or a novelty claim.


## BR02 r1 observable/Newman crosswalk — 5 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra/max**, history0006, for [Note13](../notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md).

**Brad Rodgers and Terence Tao**, *The De Bruijn-Newman constant is non-negative*, Forum of Mathematics, Pi 8 (2020), e6, [DOI](https://doi.org/10.1017/fmp.2020.6). Selected Introduction equations (1)-(4) and the following heat sign were checked in [arXiv:1801.05914v5 HTML](https://arxiv.org/html/1801.05914v5#S1), corrected version dated 3 July 2021. Use: canonical source, xi normalization, Gaussian reweighting and heat sign only; no proof of the main theorem re-audited. [Prior canonical annotation](../../../../../05_radial_theta_collision_geometry/references/14_NEWMAN_FLOW_AND_SOURCE_PERTURBATION_REFERENCES_20261028.md) is linked rather than copied. Existing external reading PDF `/Users/Shared/szp-archive/height-dependent-heat-contours/references/1801.05914v5.pdf` rechecked: 503405 bytes, SHA-256 `376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91`, PDF header present; source [PDF](https://arxiv.org/pdf/1801.05914v5). No duplicate downloaded.

**D. H. J. Polymath**, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn-Newman constant*, Research in the Mathematical Sciences 6 (2019), article 31, [arXiv:1904.12438v2](https://arxiv.org/abs/1904.12438v2), 4 August 2019. Abstract/metadata inspection only for the same normalization; no bound or theorem newly imported. Existing external reading PDF `/Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf` rechecked for header and identity: 2158176 bytes, SHA-256 `60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603`; source [PDF](https://arxiv.org/pdf/1904.12438v2). A verified file identity is not a proof inspection.

**David Tong**, [*Statistical Physics*, sections 1.3.1-1.3.2](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), live online lecture text consulted 5 November 2026. Checked canonical ensemble and energy derivatives; the conditional measurement effect and theta-source observable in Note13 are direct calculations from MC11, not claims of the lectures. This web reference is retained as a section link, without an artificial PDF copy. Tao’s [19 January 2018 author exposition](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/) was also used for orientation; the pinned Rodgers–Tao article is the canonical source for (9).

## Direct Newman B01 use — 6 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / max**, direct-branch chat0001. [TND-D-B01 Decision01](../../../../../08_theta_observables_newman_dynamics/01_direct_newman_realization/brainstorm/notes/01_TND_D_B01_CONDITIONAL_QUADRATURE_DECISION_20261106.md) and [E01 request r1](../../../../../08_theta_observables_newman_dynamics/01_direct_newman_realization/research-progress/handoffs/02_TND_D_E01_R1_REQUEST_20261106.md) reuse the complete angular spectrum/curvature through MC11's accepted operators and parent E01's proof-author comparison. Camporesi–Higuchi v1 is not freshly reread here, and no acceptance level changes.

DLMF [20.7.32](https://dlmf.nist.gov/20.7.E32), including tau-prime=-1/tau and the principal-root convention, was rechecked in the primary page on 6 November 2026 for z=0, tau=i*R^2, R>0. It supports the inherited full unit-weight reflection only; finite filtered/truncated sources do not inherit smooth reflection at zero. No chapter audit or new PDF was made.

New measurement references are canonical in the [direct-branch catalog](../../../../../08_theta_observables_newman_dynamics/01_direct_newman_realization/references/01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json). The branch expressly assigns its square-root preparation, count instrument and absolute cosine readout to local E01 checks L1–L3. This annotation does not assess or close MC11-OBS-E01, MC11-E05 or parent TND-E03.
