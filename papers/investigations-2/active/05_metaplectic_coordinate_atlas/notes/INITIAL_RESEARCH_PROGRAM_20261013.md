# Initial research program for metaplectic coordinate atlas

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**.
Status: **initialized, awaiting Claude review**. No new chart benchmark, certificate or external communication has been performed.

## Source contract and established seed

This supporting program implements [search card 5](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#5-metaplectic-covariance-and-a-regular-coordinate-atlas). Its purpose is to make a genuine source identity or its error ledger simpler to analyze, while preserving the physical observation `(H,H_x)` and Newman backward heat. A coordinate atlas is potentially useful even when it adds no new inequality by itself.

The [Wigner/Husimi scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/notes/1_HUSIMI_READOUT_DRIFT_AND_COHERENT_INTERFERENCE_20261010.md) already supplies the genuine state, full phase-space generator and exact reconstruction, including negative momentum diffusion, drift and contact terms. [De Gosson's symplectic Radon analysis, section 3](https://arxiv.org/html/2204.07106v1#S3) supplies a primary covariance precedent, not invariance of theta preparation.

For the real squeeze `D_rψ(u)=e^{r/2}ψ(e^ru)`, the chord substitution is

\[
\mathcal A_{D_r\psi}(k,\ell)=\mathcal A_\psi(e^{-r}k,e^r\ell).
\]

If `S_r` denotes this substitution and `𝒢=−∂_k²+ℓ²/4`, then `S_r𝒢S_r⁻¹=e^{2r}𝒢`. Moving `r` adds its connection term. General complex metaplectic images require conjugation on the second wavefunction in the chord correlation; their generator and readout must be derived with that convention.

## Research objective

Find two or more regular charts that simplify a source-specific reflection, gradient or boundary identity and improve its final paid conditioning. Preserve the distinction between passive covariance of a representation and an active transform that changes the prepared state. The target is a controlled physical reconstruction or symmetry-defect bound, not positivity of an unrelated transformed marginal.

Under a passive state change `Ψ̃=TΨ`, use `𝒫̃=𝒫T⁻¹` for the same observation and `𝒢̃=ṪT⁻¹+T𝒢T⁻¹` for evolution. Spatially dependent charts likewise differentiate the basis and projection. The [coordinate-invariance note](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md) explains why a smooth lifted chart can remove trajectory-coordinate singularities while retaining a physical-time fold.

## First bounded task

Choose one genuine closed physical cell and compare a fixed unsqueezed chart with one explicitly parameterized squeeze or Fourier-rotation chart. Write the transformed generator, source law, physical observation pair and moving connection exactly. Carry one candidate identity from the cutoff-reflection or chord program through both charts.

If a later benchmark is approved, use identical complete-source data and precision. Report the final `(H,H_x)` error, normalizer cost, reconstructed derivative cost and residual payment in each chart. Retain all entries of the doubled coherent density matrix: both phase differences and reflected phase sums matter. A visual change in smoothness is not the measurement of interest.

## Validation failure criterion and exclusions

Validate conjugations, Jacobians, half-density factors, time rescaling and projection derivatives before comparing numerical costs. A finite truncation needs its own boundary commutator. Independent passive-chart computations should recover the same physical jets within their paid enclosures.

Continue with a chart if it reveals a simpler complete-source constraint or reduces the final certified conditioning loss. Stop that chart choice if reconstruction consumes the entire apparent gain, if the transform silently changes the source, or if it omits moving-normalizer terms. In particular, fixed-width Husimi value errors are amplified by `exp(a x²)` when reconstructing `H`; this cannot be hidden behind positive smoothing.

Generic metaplectic covariance, uncertainty, purity and positive norms do not exclude collision controls. Dissipative quadratic-semigroup results require their stated sign and domain hypotheses; unbounded Newman source multiplication does not automatically qualify. This program is an analytical helper for the source-specific investigations, not a standalone RH mechanism or a claim that a visible lifted component prevents physical cancellation.
