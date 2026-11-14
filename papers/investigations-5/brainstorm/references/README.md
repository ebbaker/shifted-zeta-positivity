# Tensor network references

13 November 2026, America/New_York. Prepared for Edward Baker with substantial
OpenAI Codex LLM assistance. Actual backend model and reasoning effort are
unavailable in this chat's recorded model configurations.

References for the [MPS brainstorm](../01_MPS_NEWMAN_FLOW_20261113.md).
This is a targeted source check, not a literature-completeness or novelty claim.
Reading copies belong outside the repository under the
[reference policy](../../../../REFERENCE_WORKFLOW.md).

| Source | Relevance and inspection status |
| --- | --- |
| Ulrich Schollwöck, *The density-matrix renormalization group in the age of matrix product states*, Annals of Physics 326 (2011), 96–192, [DOI](https://doi.org/10.1016/j.aop.2010.09.012), [arXiv:1008.3477v2](https://arxiv.org/abs/1008.3477v2), 3 January 2011 | Checked PDF §4.1.3, equations (30)–(36), on successive-SVD MPS construction, and §7.1.1 on time evolution and compression. Its nearest-neighbor Trotter presentation is not an assumption satisfied by the all-pairs bit Hamiltonian. No ground-state approximation theorem is imported for the Newman state. |
| Boris N. Khoromskij, *O(d log N)-Quantics Approximation of N-d Tensors in High-Dimensional Numerical Modeling*, [MiS preprint 55/2009](https://www.mis.mpg.de/publications/preprint-repository/article/2009/issue-55) | Historical quantics reference. Repository abstract inspected only. PDF retrieval failed; no theorem is imported from an unexamined passage. The brainstorm directly derives factorization of its Fourier readout. |
| Michael Lindsey, *Multiscale interpolative construction of quantized tensor trains*, [arXiv:2311.12554v3](https://arxiv.org/html/2311.12554v3), 22 April 2024 | Checked §3.2, Lemma 1 and Proposition 5, and §4.1, equations (4.1)–(4.3), Lemma 12 and Proposition 13. The latter gives a polynomial-exact interpolative QTT and its uniform interpolation error. The analytic bound requires a bounded analytic extension to a specified Bernstein ellipse; no height-uniform theta constants are assumed. This is a selected-passage inspection, not a full proof audit. |
| Hiroshi Shinaoka, Markus Wallerberger, Yuta Murakami, Kosuke Nogaki, Rihito Sakurai, Philipp Werner and Anna Kauch, *Multiscale Space-Time Ansatz for Correlation Functions of Quantum Systems Based on Quantics Tensor Trains*, Physical Review X 13, 021015 (2023), [DOI](https://doi.org/10.1103/PhysRevX.13.021015), [arXiv:2210.12984v3](https://arxiv.org/abs/2210.12984v3), 28 April 2023 | Checked publisher §§I–II and v3 HTML §§II.1 and III.1–III.2: binary scale indices, compressed Fourier operations and elementwise products. Their small Fourier-MPO ranks are reported with truncation tolerances, not as exact fixed ranks. Their many-body Green functions differ from this project's strip Green potential; no Newman-flow rank or zero theorem is imported. |

Retrieved 13 November 2026 in the author's timezone. See
[BibTeX](tensor_networks.bib) and the
[retrieval manifest](READING_COPIES_20261113.json). All four attempted local
PDF downloads failed with host name-resolution errors. No local reading copy
or file hash is claimed. The successful web PDF/HTML inspections above and
the stable primary-source links remain available.
