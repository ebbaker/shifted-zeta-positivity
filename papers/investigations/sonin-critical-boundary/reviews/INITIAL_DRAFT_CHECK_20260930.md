# Initial draft: internal mathematical and editorial check

30 September 2026. Prepared for Edward Baker.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort were not exposed.
This is a sequential self-check by the drafting assistant, not independent specialist refereeing. No subagent or external reviewer was used in this drafting task.

## Scope checked

The manuscript consolidates the established internal analytic notes. The following checks were made while preparing the draft:

- Fourier measure is dt/(2*pi) throughout; the phase-difference diagonal is -phi'.
- The logarithmic reflection is linear; the deformed transform is a selfadjoint unitary involution.
- The projection retains the inverse compressed metric. The bounded inverse formula is confined to sigma greater than one.
- Abel operators are treated as positive contractions. Their trace is not replaced by the squared Hilbert–Schmidt norm of the contraction.
- Full smooth-source finiteness follows from uniform unit-window bounds. The crossing scalar is represented by a trace-class cutoff product.
- Small-cutoff convergence uses an explicit Hilbert–Schmidt estimate. Strong convergence alone is not used to infer trace convergence.
- The polar return measure has no atom at one at a fixed parameter, while its possible mass approaching one is left open.
- The rational model's inverse Fourier kernel, rank-one blocks, positive prelimit gap, zero exact projection, and three Abel crossover regimes agree algebraically.
- The arithmetic comparison includes pole crossings, half residues on exceptional lines, and the entire source weight at nonreal arguments.
- The general Weil form includes the pole term explicitly; the prepared source class removes it at the critical parameter.
- The main theorem's assertions are proved in the later sections without relying on numerical certificates or unavailable internal files.

The static source check found no duplicate labels, missing cross-references, missing bibliography keys, mismatched LaTeX environments, or external input dependencies.

## Compilation

The final source compiled successfully with the Codex desktop editor’s built-in compiler on 30 September 2026. The first compilation identified an unavailable script-font macro for the reflection operator; it was replaced by the already available calligraphic notation, and recompilation succeeded. No separate TeX installation was used. The source was sent to the native editor for its PDF preview; the app reported that opening was queued. The compiler returned success without a page count or detailed layout diagnostics. Visual page-by-page inspection was not performed.

Final manuscript SHA-256: b81bdbdb91541e7fae0f5da781792fb23ab09b1f7a09b34e4b9cffa69c446404.

## Limits of this check

The inherited interval calculations were not replayed because none are used by the manuscript. The check does not establish priority or replace a human proof review. The principal remaining research questions are total return-mass vanishing for the zeta family and identification with the complete arithmetic form.

Before submission, a specialist should examine the uniform local-factor estimates through exceptional lines, operator-ideal trace passages, and the paired contour argument. The existing manuscript states the unresolved conclusions explicitly.
