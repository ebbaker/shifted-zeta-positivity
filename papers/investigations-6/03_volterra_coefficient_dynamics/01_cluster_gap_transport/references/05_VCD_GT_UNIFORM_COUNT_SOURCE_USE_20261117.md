# Uniform complete-divisor counts for B07

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0006. Actual lead model/effort unavailable;
Astra/ultra design and Sol6.1/ultra audit/proof dispatches are recorded
separately. This is a selected-passage inspection, not a full-paper audit.

Canonical article: D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann ξ function, and a new upper bound for the de
Bruijn–Newman constant*, arXiv:1904.12438v2, 4 August 2019;
DOI 10.1007/s40687-019-0193-1. [Primary v2 PDF](https://arxiv.org/pdf/1904.12438v2).
The [existing catalog](../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json)
owns bibliography and reading-copy provenance; the parent
[bibliography](../../references/induction.bib) remains canonical here.

Inspected anew online: Theorem 1.5, printed pp.9–10; its absolute-constant
convention; and the proof of (iv), printed p.61, equation (105) and the
following safe-line/Jensen and argument-variation paragraphs. The same
normalization is H0(z)=ξ((1+iz)/2)/8 and H_t=-H_zz. Write N_t(X) for the
number of zeros with positive real part at most X, counting multiplicity,
including nonreal zeros. With a harmless endpoint-constant enlargement,

    N_t(X)=g(X,t)+O(log(2+X)),
    g(X,t)=X/(4π) log(X/(4π))-X/(4π)+11/8+t/16 log(X/(4π)),

for X≥4π and 0<t≤1/2, with an absolute error constant independent of t.
The same part supplies unit-window upper counts. These claims do not
require the exp(C/t) onset of parts (i)–(iii). The proof uses a safe
horizontal line outside the zero strip and argument variation, not an
all-real assumption. No numerical value for the implicit constant was
extracted. The cumulative estimate's extension to t=0 is a separate
compact argument-principle step required in E12, not a verbatim theorem
at the excluded endpoint.

Existing reading copy rechecked this session, without downloading:
`/Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf`,
2158176 bytes, SHA-256
`60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603`.
Its identity does not validate the theorem. No third-party PDF enters Git.

The [TND-O E10 note](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md)
§1 already extends the unit upper count to t=0, and §3 pays an
inverse-square shell tail. B07 reuses those arguments at their stated
scope. The proposed new branch output is the *centered signed far-tail
main term and its normalized rate*, not another proof of those upper
counts or a claim of literature priority.

Consumers: [Decision15](../brainstorm/notes/15_VCD_GT_B07_NEAR_FAR_COUNT_DECISION_20261117.md)
and [E12 r1](../research-progress/handoffs/VCD-GT-E12-r1.md).
