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
