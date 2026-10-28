# CTF-E05 manuscript refocus — editorial return R1

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, Investigation05 chat0012, **Refocus CTF-E05 manuscript**.

**[E] CTF-E05, request R1: complete.** The [existing source](../radial_deformations_and_zero_dynamics.tex) is now *Conservative Theta Flows and Collision Amplification*, including its PDF title. This is the requested editorial reorganization of accepted material; no B02 estimate or new mathematical claim was added. [Progress04](../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md) owns live status; the [issued request](../research-progress/handoffs/CTF-E05_MANUSCRIPT_REFOCUS_REQUEST_R1_20261028.md) remains fixed with an appended return link.

| E04 section | Current location |
| --- | --- |
| 1, purpose/variables | 1, purpose and conserved observation; rewritten abstract and introduction |
| 2, source/flux | 2, canonical source, full observation and tail lemma; unused tail flux removed |
| 3–7, forced/Darboux/zero/energy chapters | Removed from manuscript; existing Notes17–18 retain their proofs |
| 8, exact control | 3.3, compact positive-source family, convergence domain and physical event |
| 9–10, radial-integrand/projected flow | Removed from manuscript; existing Notes20–24 retain this work |
| 11, conservation/heat/diagnostic | 3, immediately after source setup |
| 12–15, feedback/carrier/residual/open estimate | 4–7, retained proofs and scopes |
| Fourth-moment appendix | Appendix A, retained |

The Darboux pairing preserves a complete integral while changing source and test function; its removal is editorial, not a retraction or reclassification as radial-profile conservation. No removed chapter was copied into a historical appendix.

Dependencies repaired: `eq:Q`, `lem:tails` and the relocated `eq:fullthetaflow`; local spherical averaging with its weighted-integrability condition; first-N truncation `Q_{t,N}`; both former literal Section8 references; physical-frequency and fixed-mark notation; the reflection prerequisite from Note01; and radiality for the gradient representation. The full source normalization, single exterior integral for all H, evolving unit ball, unit preparation/weights/diffusivity, true marked derivatives and J2, residual cancellation and origin qualifications remain intact. The control retains t<T_c+4, A*=2√6 and the later T_c=1/4 example. Unused macros, theorem declarations and bibliography entries were removed.

Source identity:

- Input: 1,967 lines, 82,925 bytes; SHA-256 `ecd862c935ffd3587c01f514339b7afeef77e07172d8152bf6950dfbc5dd0a71` (matches R1 baseline).
- Output: 1,250 lines, 54,347 bytes; SHA-256 `a3e8bc5b6f6a6d19ed74ab2466e7569adf7246e768271239b0344e918f605749`.

Verification: the saved original absolute source was compiled using `compile_latex_document`, including after final preamble/provenance cleanup. The final response was `kind: success`: “The current source compiled successfully with the desktop editor's compiler.” The response supplied no detailed warning log or page count. Source checks found 77 unique labels, all references resolved, 12 cited bibliography entries with no unused entries, balanced environments and seven retained proof blocks. A full continuity/dependency reading and a same-model read-only subagent check found no unresolved mathematical prerequisite or change of scope. These checks are internal, not independent specialist review. No visual inspection, separate PDF build/export, replacement source, new tab or snapshot was made.

Current navigation/build guidance and the E05 disposition were updated; Note33, Review19, record17, earlier notes and historical milestone rows retain their dated outcomes. Existing unrelated working-tree changes were preserved. This editorial return follows the [result index](../../../../result-summaries/README.md), especially [geometric/conservative results](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), especially [scoped failures](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [volume without a gain](../../../../avoid/20_volume_without_a_gain.md).

**Next substantive research remains [B] CTF-B02 — Astra**, the existing coupled signed-estimate contract in [Continuation32](32_SOURCE_RELATION_COMMUTATOR_CONTINUATION_20261028.md). E05 stops here; E02 remains optional and E03/B03 gated.
