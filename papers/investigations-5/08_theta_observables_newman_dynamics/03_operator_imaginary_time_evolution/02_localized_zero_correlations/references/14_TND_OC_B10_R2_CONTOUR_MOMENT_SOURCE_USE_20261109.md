# B10 r2 source use: contour first moments and certified evaluation

9 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex assistance, OC chat0009. Recorded current thread
settings gpt-6-astra/max; per-turn backend configuration unavailable.

Research use: [Note20](../notes/20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md) and
[E13 request27](../research-progress/handoffs/27_TND_OC_E13_R1_CONTOUR_CENTROID_EVALUATOR_REQUEST_20261109.md).
Selected passages checked; no full library correctness audit or literature
novelty claim.

- **Terence Tao, Math 246A, Notes 4: singularities of holomorphic functions**,
  11 October 2016, [Lemma 30, Theorem 32 and Corollary 33](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/).
  Reopened 9 November 2026. The log derivative has a residue equal to the
  zero multiplicity; a boundary avoiding zeros/poles gives the count by
  the argument principle. Multiplying by z−a_C gives the first moment
  directly by residues. Reuse the canonical entry in
  [b03 bibliography](b03_real_divisor_sources.bib); no duplicate article.
- **NIST DLMF §25.10(i)**, [Zeros](https://dlmf.nist.gov/25.10).
  Reopened 9 November 2026. The nontrivial divisor is in the open critical
  strip without assuming RH. Along with the inherited H0/xi identity,
  this supplies |Im z|<1. No critical-line assertion is imported.
- **python-flint contributors, displayed documentation version 0.9.0**,
  [acb_series](https://python-flint.readthedocs.io/en/latest/acb_series.html),
  inspected 9 November 2026: series coefficients/precision, differentiation
  and zeta. These identify the derivative-ball access path; an execution
  must record its actual runtime and validate whole-segment denominators.
  The centered-moment quadrature remainder is derived in Note20, not
  imported from an uninspected integrator.
- The main acb documentation fetch timed out twice during this pass.
  [B07 source-use08](08_TND_OC_B07_CERTIFIED_EVALUATOR_SOURCE_USE_20261108.md)
  retains its earlier verified complex-ball/winding access record.
  FLINT's acb_calc and acb_dirichlet old URLs returned moved-page notices;
  no unseen integration API was made a premise. The fixed execution uses
  the explicit midpoint remainder and formal derivatives instead.
- Inherited local sources: Note02 §4 supplies the complete source and its
  arithmetic majorant; Note13 supplies the canonical source identity and
  interval-image winding test; Note19 defines the exact Gaussian target.
  Note20 newly derives the explicit coarse global tail and first-moment
  error improvement for that target.

These are existing classical sources and online documentation; no new
research article or PDF reading copy was discovered. No source estimate
is inferred from a bibliography entry. The default python3 had no flint,
mpmath or sympy installed at preflight; this is not a claim about every
environment on the machine.

The model handoff follows [the repository workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and the official [model-selection guidance](https://learn.chatgpt.com/docs/model-selection)
already opened in this chat on 9 November. E13's method and limits are
fixed, so Sol is recommended. Actual model selection remains the author's.

