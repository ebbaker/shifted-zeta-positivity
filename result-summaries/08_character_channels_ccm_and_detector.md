# Character channels, CCM realizations, and the RH detector

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

- **Character channels are the Dirichlet family.** The Bost–Connes
  relations hold on \(L^2(\mathbb R\times\hat{\mathbb Z})\); character
  packets have winding limits \(a^{-1/2}\bar\chi(a)\langle f,U_{\log a}g\rangle\);
  the interacting YM state mixes same-parity sectors; and the
  \(Q_\chi\) normalization reproduces the zeros of six real characters to
  about \(2\cdot10^{-9}\). What is not gained: "any positivity mechanism".
- **CCM finite realizations.** A positive mass–stiffness pair, a
  point-mass string, and a unitary map to a graph Dirac operator; the
  inverse-frequency trace equals the first mass moment; the odd tail is
  \(\ge2/5\) above mode 4096 at \(L=\log13\) (rational certificate). The
  determinant limit is conditional on a positive continuum odd gap.
- **CCM weighted operator and the threshold-energy obstruction.** \(H\) has
  a simple zero mode, essential edge \(1/4\) and only discrete spectrum in
  \((0,1/4)\); RH \(\iff H-s\) has one negative direction. The threshold
  profiles are dense in the bare energy completion, so
  \(\inf\sigma(S_\delta)\to-\infty\) and every fixed prime tail is unbounded
  relative to that energy. This paused CCM (28 September).
- **RH detector.** The velocity residual \(V_j=\Xi''/\Xi'(\gamma_j)\) equals
  the field of the full zero multiset; a quadrupole sign separates
  off-axis from on-axis hidden pairs; at \(K=1000\) residuals are
  \(\sim10^{-7}\) against bands \(\sim10^{-3}\); and
  \(e^{-t\partial^2}p=\det(zI-X-tY)\) (Wilson's formula), so the Newman
  constant of a polynomial is the reality threshold of a matrix pencil.

## Status

Character channels: "[proof]" and "[floating]" per statement; no reviews
folder and no manuscript. CCM: "Exact finite realization"; the obstruction
has "working proofs" and its review found "No material mathematical flaw".
Detector: "proved in-paper", certificates "rigorous modulo floating point"
(mpmath, not interval arithmetic), "Not released", seven blocking items, no
external human review.

## Caveats

"Most realizations are algebraic transformations available for broad
classes of positive finite pencils"; the literal-\(k\) normalization
\(\Xi/4\) was corrected in two supporting notes; the fractal-coordinate
realization fails within its stated scope (stiffness, mass, refinement,
and a folded-odd Markov obstruction). The meta-analysis rule: "Do not build
another geometry without a new arithmetic estimate it would yield."

## Reusable for

A verified Weil-form normalization for the Dirichlet family; the graph
Dirac dictionary for finite positive pencils; the threshold-energy
obstruction as a control on any energy-completion route; the velocity
residual and the pencil interpretation of the de Bruijn–Newman constant
for polynomial controls.

## Where

- Character channels: [the Dirichlet-family note](../papers/investigations/character-channels/notes/CHARACTER_CHANNELS_AND_THE_DIRICHLET_FAMILY_20260926.md).
- CCM: [program overview](../papers/investigations/ccm-operator-realizations/PROGRAM_OVERVIEW.md), [README](../papers/investigations/ccm-operator-realizations/README.md), [strings, graph Dirac and cutoff obstructions](../papers/investigations/ccm-operator-realizations/notes/CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md), [weighted operator reduction](../papers/investigations/ccm-operator-realizations/notes/CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md), [threshold-energy obstruction](../papers/investigations/ccm-operator-realizations/notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) and its [review](../papers/investigations/ccm-operator-realizations/reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md), [string realization review](../papers/investigations/ccm-operator-realizations/reviews/STRING_REALIZATION_CRITICAL_REVIEW_20260926.md), [bounded audit](../papers/investigations/ccm-operator-realizations/notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md).
- Fractal Laplacians: [obstructions](../papers/investigations/ccm-fractal-laplacians/notes/CCM_PRIME_JUMP_GEOMETRY_OBSTRUCTIONS_20260926.md), [critical review](../papers/investigations/ccm-fractal-laplacians/reviews/PRIME_JUMP_GEOMETRY_CRITICAL_REVIEW_20260926.md).
- Detector: [manuscript](../papers/misc/rh-detector/rh_detector.tex), [STATUS](../papers/misc/rh-detector/STATUS.md), [README](../papers/misc/rh-detector/README.md).
- Program-wide context: [program meta-analysis](../papers/investigations/program-meta-analysis/reviews/PROGRAM_META_ANALYSIS_20260926.md), [CCM threshold update](../papers/investigations/program-meta-analysis/notes/CCM_THRESHOLD_OBSTRUCTION_UPDATE_20260928.md).

## Dirichlet Newman continuation on 17 October 2026

Prepared for Edward Baker with substantial LLM assistance; recorded model
**gpt-6.1-sol (Codex), reasoning effort ultra**. Status in the source:
"proved in-note; internal same-model checks only." The
[round-3 sine-tail proof](../papers/investigations-3/01_dirichlet_newman_families/notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
bypasses the confinement premise in the positive-time comparison, yielding
Lambda_chi <= 0.27 for every primitive q >= 10^12 and
O((log q)^(-4/7)) -> 0 in the conductor aspect. The zero lower bound is
imported from Dobner. This is positive-time smoothing, with no GRH claim.
The [manuscript](../papers/investigations-3/01_dirichlet_newman_families/manuscript/main.tex)
and [focused same-model check](../papers/investigations-3/01_dirichlet_newman_families/reviews/02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md)
record the theorem and dependencies; specialist review and a priority
audit remain outstanding. Ki–Kim–Lee's earlier qualitative real-character
result corrects the initial search. H12 for the original flow remains open.

**17 October review continuation — gpt-6-astra, max, for Edward Baker with
LLM assistance.** [Review 03](../papers/investigations-3/01_dirichlet_newman_families/reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md)
found no substantive defect using another GPT model and replayed the exact
certificate. The [response](../papers/investigations-3/01_dirichlet_newman_families/notes/round-4/04_REVIEW_RESPONSE_AND_SIBLING_BENCHMARK_CODEX_20261017.md)
adds analytic manuscript appendices and reconciles status. At the same
q >= 10^12 threshold, Project 03's proved-in-note 0.215 is the stronger
finite benchmark; 0.27 remains the simpler initial-floor application.
The new appendix text has authoring checks only; specialist review remains
outstanding. This updates, rather than replaces, the preceding milestone.

## Investigations 4 compact-circle screen — 21 October 2026

Prepared for Edward Baker with substantial LLM assistance; **gpt-6-astra,
effort ultra**. The [circle note](../papers/investigations-4/01_compact_weil_positivity/notes/01_CIRCLE_COMPARISON_AND_POSITIVE_COMPLETION_OBSTRUCTIONS_20261021.md)
is “proved in-note, with separate same-model agent review.” It derives a
complete fixed-test comparison with an exponentially small archimedean
image error when P>2L and max(2,e^L)<=X<=e^(P-L). Literal sampled-circle
positivity and finite image corrections fail in the specified odd-mode
regime; the positive jump completion pays a nonvanishing scalar/pole cost.
Fixed-rank and successful nonnegative diagonal repairs have separate stated
cutoff obstructions. The conclusion is candidate/map/schedule-specific:
“This candidate is not the Connes–Consani–Moscovici construction.”
[Review](../papers/investigations-4/01_compact_weil_positivity/reviews/01_CIRCLE_COMPARISON_REVIEW_20261021.md);
checks are exact algebra plus floating diagnostics, not new certified theta
or Weil positivity. I4-W02 and the actual CCM gates remain unchanged.
