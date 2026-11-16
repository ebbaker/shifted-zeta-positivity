# QTT reference use

13 November 2026, America/New_York. Prepared for Edward Baker with substantial
OpenAI Codex assistance. Actual backend model and effort are unavailable in
recorded configurations. **Inherited reference pointers and branch-use
mapping only; no new literature search or full-paper inspection at setup.**

Canonical records remain in the
[opening catalog](../../../investigations-5/brainstorm/references/README.md).
Use its [BibTeX](../../../investigations-5/brainstorm/references/tensor_networks.bib)
and [retrieval manifest](../../../investigations-5/brainstorm/references/READING_COPIES_20261113.json),
which records four failed local PDF downloads. Their earlier successful web
inspections retain the stated passage-level scope. The
[parent ownership guide](../../references/README.md) governs new shared sources.

| Canonical source and inspected version | Branch use and limitation |
| --- | --- |
| Schollwöck, *The density-matrix renormalization group in the age of matrix product states*, [1008.3477v2](https://arxiv.org/abs/1008.3477v2), 3 January 2011; §4.1.3, equations (30)–(36), and §7.1.1 | Successive-SVD representation and time-evolution/compression background in the overview. The nearest-neighbor example does not make this branch's all-pairs generator local. No ground-state area-law premise is imported. |
| Lindsey, *Multiscale interpolative construction of quantized tensor trains*, [2311.12554v3](https://arxiv.org/html/2311.12554v3), 22 April 2024; §3.2 Lemma 1/Proposition 5, §4.1 equations (4.1)–(4.3), Lemma 12/Proposition 13 | Candidate interpolation/rank route for B01. Preserve the analytic-extension region and its norm bound; theta-specific growing-domain constants remain unpaid. |
| Shinaoka et al., *Multiscale Space-Time Ansatz for Correlation Functions of Quantum Systems Based on Quantics Tensor Trains*, [2210.12984v3](https://arxiv.org/html/2210.12984v3), 28 April 2023; §§II.1, III.1–III.2 | Binary scale encoding and compressed Fourier/elementwise operations. Their quantum many-body Green functions differ from GNP's strip potential. Reported approximate ranks are not exact fixed-rank theorems for Newman flow. |
| Khoromskij, *O(d log N)-Quantics Approximation of N-d Tensors in High-Dimensional Numerical Modeling*, [MiS55/2009](https://www.mis.mpg.de/publications/preprint-repository/article/2009/issue-55) | Historical discovery pointer; abstract-only inspection remains abstract-only. No unexamined theorem is imported by setup. |

All prior inspections were recorded on 13 November 2026 in the author's
timezone. Internal source/evidence passages are linked individually in the
[source crosswalk](../notes/02_QTT_SETUP_AND_SOURCE_CROSSWALK_20261113.md)
and at their points of use in the
[overview](../research-overview/01_QTT_RESEARCH_OVERVIEW_20261113.md).

Follow [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md): record any
new relevant article immediately, cite the exact relied-on passage, retain
its assumptions and inspection status, and keep third-party PDFs outside
Git. An explicitly new branch-specific article can have its canonical record
here; do not duplicate an existing shared entry to make the folder look full.

**13 November 2026, QTT-B01 use update:** the Astra/ultra-dispatched worker
reopened the primary [Lindsey v3 HTML, §4.1](https://arxiv.org/html/2311.12554v3)
and checked Lemma 12/Proposition 13's polynomial-exact interpolation
statement. This is a passage-level reinspection, not a full-paper read or
a new PDF retrieval; the canonical record and earlier download status
remain unchanged. The issued QTT-E01 request may instead derive the
polynomial translation identity directly. No analytic constant for theta
or growing-height rank result is imported from this passage. Intended
author Edward Baker; substantial Codex assistance; dispatched model/effort
gpt-6-astra/ultra, independent backend metadata unavailable.
