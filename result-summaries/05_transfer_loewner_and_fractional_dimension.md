# Transfer structure: all-pass, even tower, Loewner, fractional dimension

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

- **All-pass transfer and the dichotomy.** \(|K_\omega(i\tau)|=1\)
  unconditionally; the \(\omega\)-flow lies in one commutative algebra; and
  \(\|V_{\omega,L}\|\le1\) for all \(L\) if and only if no zero lies more
  than \(\omega\) from the critical line. So there is no "critical path":
  any transfer-side candidate reduces to a zero-free strip, and the
  contraction margin "carries essentially no arithmetic information".
- **Even-tower splits.** \(n_\gamma=G_o+G_-\) and
  \(n_\gamma=\tfrac12(G_s+G_o)\) with \(G_o=1/(2\cosh(u/2))\), whose
  transform \(\pi/\cosh\pi\tau\) is positive; the archimedean tower is a free
  fermion's two spin structures (1,196 checked cases).
- **The Loewner decomposition.** \(K_\omega=B_b\cdot\hat K_\omega\) with
  \(\hat K_\omega\) completely monotone, so \(k_\omega=\hat k_\omega-2\,\mathrm{EMA}_b[\hat k_\omega]\);
  \(B_b\) is forced by unimodularity; extended to every \(\omega>0\). The
  registered zero-free assembly of \(V_{\omega,L}\) matches the certified
  margins to 0.54%, 1.20% and 1.85%.
- **Far-field pure delay.** A translation-invariant Loewner radial kernel
  is a pure delay with no atoms at \(\log n\): the prime comb is
  Hecke/Bost–Connes, not Loewner. Scope: map-induced transport, not
  field-dependent Wilson observables.
- **Horocycle integral and quantization.**
  \(K^\Gamma_\omega(p)=\int_{\mathbb R^{2\omega}}|t+i|^{-(p+b)}dt\) and
  \(K_{1/2}\) is inner unconditionally; the quantization claim beyond
  \(\mathrm{SL}(2,\mathbb Z)\) is a reading, not a theorem.
- **Fractional dimension.** The comb weights are \(J_d(n)/n^{(d+1)/2}\),
  \(\tilde K_\omega\) is the rank-\((d+1)\) Epstein ratio, \(r_{d+1}(3)<0\)
  on \((0,1)\), and the criterion is vacuous for \(\omega\ge\tfrac12\):
  "\(d\) is a parameter", "a scattering matrix without a space".
- **Quarter-shift classification.** The delay invariants \(I_{2m}\) do not
  depend on the dictionary, and a single \(\Gamma\)-factor is pinned to
  \(a\in\{\tfrac14,\tfrac34,\tfrac12\}\); Liouville, FZZT, \(H_3^+\), JT and
  the cigar all fail the test.

## Status

Written proofs, "unconditional" where so marked; the wilson-lines
cross-model review calls Thm 5.2, Prop 7.2 and Prop 11.3 "airtight" (with
a boundedness repair in Prop 7.2); every proposition of fractional
dimension "proved in place"; the quarter-shift survey rows are "reading"
and the cigar rows least checked.

## Caveats

The Loewner investigation is closed "with proofs rather than with an
expectation" (18 September), and its README is the template for a branch
closure. Contraction at \(\omega\ge\tfrac12\) is not evidence of anything
(it holds unconditionally), and boundary phase identities alone do not
prove transfer contraction; manuscript §11.6 of wilson-lines was retracted
when convenience hypotheses were found to exclude the matching amplitude.

## Reusable for

Reducing any proposed transfer mechanism to the strip statement it
encodes; the even tower and the \(\cosh\) kernel; the registered
contraction margins as calibration data; the quarter-shift filter for
\(\Gamma\)-ratio amplitudes.

## Where

- Wilson lines: [all-pass](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/sections/04_allpass.tex), [abelian flow](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/sections/05_abelian.tex), [region](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/sections/07_region.tex), [delay](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/sections/11_delay.tex); [cross-model review](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/reviews/review_claude-fable-5-1_2026-09-17.md); [notes index](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/README.md); [even tower](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md); [quarter-shift survey](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/THE_QUARTER_SHIFT_SURVEY_20260917.md); [critical path](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/notes/CRITICAL_PATH_20260917.md).
- Loewner: [README (closure template)](../papers/weil-positivity/susy-positivity/investigations/loewner/README.md), [decomposition](../papers/weil-positivity/susy-positivity/investigations/loewner/sections/03_decomposition.tex), [realizations](../papers/weil-positivity/susy-positivity/investigations/loewner/sections/04_realizations.tex), [Markov part](../papers/weil-positivity/susy-positivity/investigations/loewner/notes/MARKOV_PART_AND_REALIZATIONS_20260917.md), [the shift is half a dimension](../papers/weil-positivity/susy-positivity/investigations/loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md), [contraction margins](../papers/weil-positivity/susy-positivity/investigations/loewner/numerics/records/contraction-margin-checks.json).
- Fractional dimension: [README](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/README.md), [rank](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/sections/03_rank.tex), [wall](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/sections/04_wall.tex), [criterion](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/sections/05_criterion.tex), [trap list](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/notes/NEW_SESSION_PROMPT.md).
