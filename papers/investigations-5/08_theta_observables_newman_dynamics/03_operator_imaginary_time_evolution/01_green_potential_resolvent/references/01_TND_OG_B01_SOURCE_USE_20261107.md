# B01 source use: fixed-source conditioning and mollifier transfer

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual session metadata: **gpt-6-astra / max**, branch chat0001. Checked passages and internal derivations only; no full literature or proof audit.

## New branch-specific primary record

Maksym Radziwiłł, *Limitations to mollifying ζ(s)*, **arXiv:1207.6583v3**, 11 October 2012; first submission 27 July 2012. [Pinned metadata](https://arxiv.org/abs/1207.6583v3), [primary HTML](https://arxiv.org/html/1207.6583v3), [PDF](https://arxiv.org/pdf/1207.6583v3). No earlier repository record was found in the bounded Markdown/BibTeX search excluding histories. This record and [the branch bibliography](green_resolvent_sources.bib) are canonical for this new branch-specific use; inherited shared articles remain parent-owned.

Inspected 7 November: §1, definition (1), Theorem 1, **Proposition B (attributed to Soundararajan)**; §7, (13)–(16), Lemmas 9–10, and the stated bounds in Lemmas 11–14. The PDF's printed pages **2 and 13** were rendered and visually checked. Proposition B gives the asymptotic lower bound **1/θ** for the mean square of **1−ζM** when fixed **0<θ<1/2**, a(1)=1 and the stated coefficient-growth hypothesis holds. Complex coefficients are explicit. This is not yet a theorem for the branch's center-normalized two-boundary residual. E01 must prove that transfer and its uniformity over |a(n)|≤1. The RH-dependent Theorems 2–3 are not used. No claim of a numerical onset or new mollifier theorem.

The initial v2 HTML inspection was discovery only. **Freeze v3:** its displayed main term includes **2 log 2**, confirmed in the PDF; do not inherit a missing term from an earlier conversion. The new application needs the lower bound, not a reconstructed main-term constant.

Reading copy successfully retained outside Git after an initial sandbox DNS failure:

- Source: `https://arxiv.org/pdf/1207.6583v3`
- Archive: `/Users/Shared/szp-archive/theta-observables-newman-dynamics/references/1207.6583v3.pdf`
- Bytes: **217253**; SHA-256: `7a19b7c1bd88d8e6030e38a6dcbdbd68f4e0a8750b82df4e3a4cb868b7d71135`
- PDF signature verified. Hash identifies the retrieved version, not correctness. No third-party PDF enters the repository.

Consumers: [B01 decision](../brainstorm/notes/01_TND_OG_B01_RESOLVENT_CONDITIONING_DECISION_20261107.md), [Note01 §6](../notes/01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md), and [E01 request](../research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md).

## Reused internal inputs and bounded inspection

| Source | Passage used | Limit |
| --- | --- | --- |
| Parent [source section](../../manuscript/sections/02_source.tex) | Complete smooth even positive theta source; fixed weighted moments and arithmetic/radial majorants | Inherited proof, no new modular-identity theorem imported |
| Parent [Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) | §§1–5: strip Green sum, boundary zeros, complete convergence, defect margin and square-root event signal | Reused at its internally assessed scope |
| Parent [Decision17 §6](../../brainstorm/notes/17_TND_O_B04_R5_SIGNED_ACQUISITION_DECISION_20261107.md) | Translated positive-source Euler multiplier and lattice Green sum | New calculation fixes the prime and varies amplitude; earlier prime-growth obstruction remains unchanged |
| Parent [Notes28](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md)–[29](../../notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md), [Review12](../../reviews/12_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_20261107.md) | Analytic mean/variance, pole cancellation, exact-source acquisition and actual obstruction classes | BCR applications inherited; no new BCR primary-paper audit |
| Parent [Note11 §§3–4](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md) and [locator20](../../brainstorm/notes/20_TND_O_PRIOR_HIERARCHY_LOCATOR_20261107.md) | Primitive endpoint, existing contour-margin method, earlier regulated W and HDA hierarchy | No new contour advantage or HDA transfer claimed |

DLMF [§4.21](https://dlmf.nist.gov/4.21) and [§4.23](https://dlmf.nist.gov/4.23) were opened as elementary-function checks; the cosine/hyperbolic calculations are derived in Note01. A bounded discovery search also returned Polymath/Dobner background already held in the [heat-flow applications catalog](../../../../02_heat_flow_rh_applications/references/README.md) and its [bibliography](../../../../02_heat_flow_rh_applications/references/sources.bib), along with unrelated claims; none supplies a new theorem here. The [parent source-use record](../../references/17_TND_O_GREEN_CORRELATION_SETUP_SOURCE_USE_20261107.md) and existing shared bibliographies retain ownership and provenance.

Follow [REFERENCE_WORKFLOW](../../../../../../REFERENCE_WORKFLOW.md), [LARGE_FILES](../../../../../../LARGE_FILES.md), and [unchecked imports](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). Broader uniformity and the full normalized-residual proof are E01 obligations, not facts established by this receipt.
