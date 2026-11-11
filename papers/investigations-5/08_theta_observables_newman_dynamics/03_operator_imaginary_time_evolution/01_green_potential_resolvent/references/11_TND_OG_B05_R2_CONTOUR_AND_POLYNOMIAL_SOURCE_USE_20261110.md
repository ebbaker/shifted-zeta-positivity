# B05 r2 source use: contour floors and local polynomial acquisition

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Chat0009 has no recorded model/effort
configuration; neither is inferred. Selected passages only, not a
literature or priority audit.

NIST DLMF remains owned by the [parent source record](../../references/14_TND_O_GREEN_PRIME_BASELINE_SOURCE_USE_20261107.md).
The online version inspected is **1.2.8, 15 September 2026**. No separate
PDF is needed for these online references and no duplicate article is
introduced. Newly inspected passages on 10 November:

| Primary passage | Use and limits |
| --- | --- |
| [DLMF §1.10(i)](https://dlmf.nist.gov/1.10#i) | Analytic Taylor expansion. Note14 derives its finite-source remainder directly from the exponential/cosine integral, with coefficient errors included. |
| [DLMF §1.10(iv)](https://dlmf.nist.gov/1.10#iv), argument principle and Rouché's theorem | A strictly nonzero boundary and holomorphy on a neighborhood are required. Counts include multiplicity. A root candidate or a small residual is not a count. |
| [DLMF §1.10(v)](https://dlmf.nist.gov/1.10#v) | Apply the boundary maximum principle to both U and 1/U only after every disk zero has been removed. The explicit factor floor and logarithmic-curvature constants are derived in Note14. |
| [DLMF 5.15.1](https://dlmf.nist.gov/5.15.E1) | Trigamma series, with poles excluded. At Re(s/2)=1/4 it gives the uniform 13/4 bound for the real second derivative of log abs(D0). |

The general complex divided-difference identity is reused at the accepted
[E07 scope](../reviews/11_TND_OG_E07_ANALYTICAL_ASSESSMENT_20261110.md).
De Boor's canonical attribution remains [Source-use10](10_TND_OG_B05_DEFLATION_AND_COST_SOURCE_USE_20261110.md)
and its OA links; no new reading of that article is claimed. Polynomial
synthetic division and the harmonic Fourier-coefficient estimate are
proved directly in [Note14](../notes/14_TND_OG_B05_R2_CONTOUR_CONDITIONING_AND_COST_20261110.md).

Internal inputs read: OG Notes06, 10, 12, 13; E06 Request18 and directed
Record05; E07 Review11; the sole OG register; result/avoid indexes with
clusters11/12 and patterns01/02/07/11. The OC/OA status discussion uses
Note10's explicitly inherited scopes, not a fresh census or force replay.

The [official model-selection page](https://learn.chatgpt.com/docs/model-selection)
was searched and opened on 10 November. Its Astra/deep-analysis and
GPT-6.1 Sol/time-and-cost guidance is consistent with the repository's
[B/E workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
The E08 recommendation concerns a fixed contract, not a measured
speedup, account entitlement, change of settings or independent review.
