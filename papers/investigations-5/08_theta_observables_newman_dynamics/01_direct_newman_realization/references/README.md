# References and source use: Direct Newman realization

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort ultra**. Investigation08 chat0003.

This is the branch-local use index for TND-D work. Follow [REFERENCE_WORKFLOW.md](../../../../../REFERENCE_WORKFLOW.md) when a relevant source is found and when importing a claim. Cite the exact source/passages in the consuming note or review, with its hypotheses and inspection status.

Canonical records already used by the parent remain at their existing homes. This branch links them rather than duplicating inherited annotations or bibliography entries; its own bibliography contains only newly recorded branch-specific articles. New branch-specific sources should be recorded here promptly; sources shared with the sibling should normally be cataloged once at the parent, with both branches' use links.

| Input/reference home | Use and current inspection status |
| --- | --- |
| [Parent reference guide](../../references/README.md) and [E01 Note02](../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md) | Inherited spinor spectrum/curvature, complete source and normalization conventions. The parent guide records its checked passages; this setup has not reread the primary articles. E01's new comparisons remain proof-author work. |
| [Canonical MC11 source records](../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md) | Camporesi–Higuchi v1 angular Dirac spectrum/curvature and DLMF theta inversion; reuse their recorded passage-level scope. Later measurement/Newman annotations do not upgrade pending MC11-OBS-E01 claims. |
| [Reusable BibTeX bibliography](../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/references.bib) | Existing bibliography for inherited sources. Retain stable keys and source versions; do not create a second competing copy solely for this branch. |
| [Parent continuation and prompts](../../notes/03_BRANCH_CONTINUATION_AND_PASTEABLE_PROMPTS_20261106.md) | Next task, exact reading dependencies, source-use obligations and status/history ownership. |

For each new use, record authors/title, pinned version/identifier and stable primary link; the exact theorem/equation/section/page and assumptions; the branch note/section using it; what was actually inspected and when; and material limitations. Check the primary source before newly importing a theorem. Distinguish inherited inspection from fresh checking and downloaded identity from proof verification.

Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) for external PDF reading copies and their URL/date/size/hash provenance. No third-party PDF belongs in Git. A compact catalog/manifest can be added when needed; no empty citation or invented retrieval record is created here.

**Coverage at setup:** inherited pointers only. This is the start of branch-local reference tracking, not a complete reference backfill or literature audit. Update it as sources are consumed.

## TND-D-B01 source use — 6 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / max**, branch chat0001. [Decision01](../brainstorm/notes/01_TND_D_B01_CONDITIONAL_QUADRATURE_DECISION_20261106.md) and [request r1](../research-progress/handoffs/02_TND_D_E01_R1_REQUEST_20261106.md) use the following source scopes. These are passage checks and inherited-use records, not an assessment of the proposed realization.

| Source | Exact use and canonical record |
| --- | --- |
| Castin–Dalibard–Mølmer, *A Wave Function approach to dissipative processes*, arXiv:0805.4002v1, 26 May 2008 (1992 proceedings manuscript reproduced) | Primary HTML §1 (2), (4)–(11) checked for no-count effective-Hamiltonian and norm/probability conventions. The cylinder's unbounded coupling and complete instrument are new local proof obligations, not imported theorems. [Canonical branch record](01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json), [primary version](https://arxiv.org/abs/0805.4002v1). |
| Jacobs–Steck, *A Straightforward Introduction to Continuous Quantum Measurement*, quant-ph/0611067v1, 6 November 2006; Contemporary Physics 47, 279–303 | Primary HTML §III (17)–(19), with the preceding completeness condition, checked for conditional-state and effect normalization. §IV (22)–(24) inspected only for context; its diffusive instrument is not selected. [Canonical branch record](01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json), [primary version](https://arxiv.org/abs/quant-ph/0611067v1). |
| Dalibard–Castin–Mølmer, PRL 68 (1992), 580–583 | Related original article discovered; metadata only, no proof/formula imported. The separate proceedings version above supplies the checked passages. [Canonical discovery record](01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json), [DOI](https://doi.org/10.1103/PhysRevLett.68.580). |
| Rodgers–Tao, arXiv:1801.05914v5, 3 July 2021 | Introduction (1)–(4) and following heat sign freshly rechecked in primary HTML for source/calibration only. Follow-up appended to the existing [canonical catalog](../../../02_heat_flow_rh_applications/references/sources.json); no zero theorem or full proof audit imported. [Primary passage](https://arxiv.org/html/1801.05914v5#S1). |
| DLMF 20.7.32 and Camporesi–Higuchi v1 | DLMF's theta transformation and principal-root convention freshly checked at z=0, tau=i*R^2, R>0. Camporesi–Higuchi spectrum/curvature reused through accepted MC11 and parent E01 at their existing levels; no fresh full-paper reading. Use supplement appended to [MC11's canonical record](../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md). |

New article metadata, passages, limitations, consuming notes and external PDF provenance are in the single [branch catalog](01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json). The [local BibTeX file](references.bib) contains only those new sources; inherited keys stay in the linked MC11 bibliography. Three public reading copies were retained outside Git with PDF-header, size and SHA-256 records. Their bodies were not inspected as PDFs; the two stated passage checks used primary HTML. No full-paper audit or implementation claim follows from a download. Existing inherited PDF records are preserved without claiming a fresh file check.

## TND-D-E01 r1 execution use — 6 November 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol/ultra**, direct-branch chat0002. [Analytical Note02](../notes/02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md) consumes the canonical records above without upgrading their inspection or evidence scope. Fresh primary HTML passage checks in this execution were:

| Existing canonical source | Checked passage and use | Limit |
| --- | --- | --- |
| [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), linked MC11 record above | Principal-root convention, z=0, tau=i*R^2 with R>0; full theta reflection, then the local smooth-source argument in Note02 §3 | No filtered or finite-truncation reflection inferred |
| [Rodgers–Tao, arXiv:1801.05914v5](https://arxiv.org/html/1801.05914v5#S1), existing Investigation02 catalog above | Introduction (1)–(4) and following heat sign: canonical source, H0=xi((1+iz)/2)/8 and decreasing laboratory-to-Newman clock convention | No endpoint zero theorem or full-paper audit imported |
| [Castin–Dalibard–Mølmer, arXiv:0805.4002v1](https://arxiv.org/html/0805.4002v1), branch catalog above | §1 (4)–(11): effective-Hamiltonian sign, no-count norm/probability and conditioning | The full unbounded cylinder instrument is proved locally in Note02 §4 |
| [Jacobs–Steck, quant-ph/0611067v1](https://arxiv.org/html/quant-ph/0611067v1), branch catalog above | §III completeness preceding (17), conditional update (17), trace probabilities (18), subset effects (19) | Countable trace limits are proved locally; displayed (16) is not used; no diffusive model substituted |

These are selected passage checks retrieved 6 November 2026, not full-paper reading. No new article, new PDF download, or change to existing archived-PDF provenance was made. Inherited Camporesi–Higuchi geometry/spectra and Investigation05 scalar benchmarks remain at their existing recorded levels; no fresh full-paper check is claimed. The [return record](../research-progress/handoffs/02_TND_D_E01_R1_RETURN_RECORD_20261106.json) records this execution scope. L1–L3 do not close external MC11 tasks.
