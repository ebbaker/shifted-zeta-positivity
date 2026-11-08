# TND-OG-E04 manuscript source use

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are not recorded in this chat's capture metadata. This is a bounded
manuscript-integration source check, not a full external proof audit or a
novelty survey.

## Internal sources actually consumed

The starting handoff is
[Continuation05](../continuation-notes/05_TND_OG_B02_RESULTS_AND_MODEL_CHANGE_20261108.md).
The author explicitly permits the parent manuscript as background.
Its [source section](../../manuscript/sections/02_source.tex) and
[complete Green section](../../manuscript/sections/17_green_strip.tex),
together with parent
[Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md),
supply the normalization, product, strip, boundary convergence and prime
decomposition. The local unit-count bound is a separate inherited input
from the parent localization analysis, not inferred from the global
Jensen count in the new draft.

The branch's [Note01](../notes/01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md),
[Note02](../notes/02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_20261107.md),
[Note03](../notes/03_TND_OG_E02_REAL_MIXED_TERM_AND_ACQUISITION_CLARIFICATIONS_20261107.md)
and [Note04](../notes/04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md)
are the proof sources for manuscript sections 5–8.
[Review01](../reviews/01_TND_OG_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md)
and [Self-check02](../reviews/02_TND_OG_B02_BOUNDARY_LOG_SELF_CHECK_20261108.md)
determine their evidence status. The E03
[request](../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md)
is cited only as an outstanding task.

Existing source-use
[01](01_TND_OG_B01_SOURCE_USE_20261107.md),
[02](02_TND_OG_E01_SOURCE_USE_20261107.md),
[03](03_TND_OG_E02_SOURCE_USE_AND_PRINTED_FORMULA_CLARIFICATION_20261107.md)
and [04](04_TND_OG_B02_SIGNED_LOG_SOURCE_USE_20261108.md)
retain their original inspection scope and attribution.

## Primary passages reopened in this session

| Primary source | Actual passage and manuscript use | Limit |
| --- | --- | --- |
| [Radziwiłł, *Limitations to mollifying ζ(s)*, arXiv v3](https://arxiv.org/html/1207.6583v3) | Local pinned PDF page 2, Proposition B: unconditional short-mollifier lower moment, attributed there to Soundararajan, with complex coefficients. Local PDF page 15, Lemma 13: the printed dependence is on the excess itself. Both pages were rendered and visually checked. | Imported mean-value theorem; its complete proof was not independently audited here. The square-root-excess estimate in manuscript §6.4 is the project's direct real calculation from Note03, not the displayed statement of printed Lemma 13. |
| [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) | Theta-three modular transformation with principal square root; the zero-argument, imaginary-parameter specialization gives the real theta reflection in §2.1. | Selected formula only. |
| [DLMF §25.4](https://dlmf.nist.gov/25.4) | Completed xi definition and reflection; §2.1 derives the exact half-Fourier normalization using the theta Mellin split. | The parent owns the canonical DLMF reference record; no new citation key. |
| [DLMF 5.8.2](https://dlmf.nist.gov/5.8.E2) | Reciprocal-gamma product and its sign/exponential normalization; used to derive the compact multiplier estimate in §7.1. | A compact-strip upper bound only, not a bound used on the infinite approximate boundary. |
| [Tao, 246B Notes 1](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/) | Theorem 2, disk Jensen formula with nonzero center and multiplicity; used in §8.1. | The line-sublevel and envelope estimates are derived in the draft, not attributed to this source. |
| [Tao, 246A Notes 5](https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/) | Exercise 69, Harnack inequality and the radius ratio; applied to the nonnegative harmonic function after Blaschke division. | The canonical anchor, chosen disks and resulting constant 51 are checked locally. |

The already archived Radziwiłł PDF was read at
/Users/Shared/szp-archive/theta-observables-newman-dynamics/references/1207.6583v3.pdf.
It contains **217253 bytes**, with SHA-256
**7a19b7c1bd88d8e6030e38a6dcbdbd68f4e0a8750b82df4e3a4cb868b7d71135**,
rechecked this session. This is the existing archive, not a new download.
No third-party PDF or reference-page image is added to Git. The image
checks were temporary local files.

## Bibliography and integrity

[prepare_bibliography.py](../manuscript/prepare_bibliography.py) selects
18 records from the existing parent, sibling, shared theta and branch
bibliographies. Only eight branch-specific internal manuscript records
are added in [manuscript_sources.bib](manuscript_sources.bib).
The combined bibliography is generated outside the manuscript source tree.

All 33 non-tooling files in the E03 input manifest match their frozen
hashes. The one mismatch is the already updated shared
tools/CHAT_HISTORY.md, which this manuscript task did not edit.
The individual results are recorded in the
[build record](../numerics/01_TND_OG_E04_MANUSCRIPT_BUILD_20261108.json).
The historical input manifest is not rewritten, and its mathematical
proof inputs remain unchanged.

Follow the [reference workflow](../../../../../../REFERENCE_WORKFLOW.md),
[large-file convention](../../../../../../LARGE_FILES.md) and
[unchecked-import pattern16](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
No claim of originality or specialist independence is made.
