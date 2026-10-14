# Initial research program for chord geometry and nonlocal closure

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**.
Status: **initialized, awaiting Claude review**. This note defines a bounded investigation; it reports no new research run or source inequality.

## Source contract and established seed

This program implements [search card 4](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#4-chord-geometry-and-nonlocal-gradient-closure). Use the complete genuine source `m_t(u)=e^{tu²}Φ_e(u)` and its real positive wavefunction `ψ_t=√m_t`. The chord field is

\[
\mathcal A_t(k,\ell)=\int e^{iku}
\psi_t(u+\ell/2)\psi_t(u-\ell/2)\,du.
\]

The exact physical projection is `𝒜_t(k,0)=2H_t(k)`, with generator `−∂_k²+ℓ²/4`. The observed slice evolves autonomously. Transverse coordinates therefore do not supply an inequality merely by being present. The [full dictionary in Heat Note 25](../../../../quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md) also introduces the derivative-wavefunction overlap and transverse curvature `C=𝒜_ℓℓ|_{ℓ=0}`.

Let `W=−log m_t`, fix `β>0` under physical differentiation, and set `E=Fourier[m_t(W'−βu)²]`, `D=4C+E`. On the physical slice,

\[
D=-\beta^2\mathcal A''-2\beta k\mathcal A'
-(k^2+2\beta)\mathcal A.
\]

This equality is a seed, not the missing theta sign. Complete theta sums retain every cross contribution. A finite constant-coefficient polynomial closure of `C` in terms of `𝒜` is already excluded by the genuine exponential score tail; a nonlocal arithmetic relation remains open.

## Research objective

Find a theta-specific reflection, angular gluing or nonlocal operator identity that constrains `(𝒜,D,D')` jointly with the physical projection. The most direct targets are

\[
\mathcal A[D+(k^2+2\beta)\mathcal A]\ge0\quad(\mathcal A'=0),
\]

\[
\mathcal A'[D'+(k^2+4\beta)\mathcal A'+2k\mathcal A]\ge0
\quad(\mathcal A''=0).
\]

The [stationary-sign criterion](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md) explains how both signs, on the required predecessor neighborhood, exclude every finite multiplicity. A rigorously sufficient bounded-loss variant is also eligible; it must retain its actual joint-energy denominator and hypotheses.

## First bounded task

Select one explicit reflection or gluing operation on the complete source. Derive its action on the chord and gradient overlaps before imposing stationarity. Record operator domains, transformed generator, source law, physical projection and every endpoint term. Determine whether it produces an independent restriction on `D,D'`, or only rewrites the existing scalar derivatives.

Use a compact time interval and an explicitly bounded physical neighborhood for the first comparison. The [paired-source contour and remainder bounds](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md) supply an existing analytic interface where applicable. They do not license an unsupported complex-`ℓ` square-root branch or interchange of raw full-line product sums at positive heat.

## Validation failure criterion and exclusions

Test the proposed hypothesis against the earlier positive double and triple collision controls, which share generic purity and chord identities. The actual theta coefficients or modular preparation must visibly distinguish them. Preserve all physical drift, fixed-`β` conventions, cross terms, natural-cutoff payments and outward product errors.

Continue if the identity yields a signed covariance restriction or an independently justified nonlocal closure with controlled constants. Stop the specific architecture if it relies only on positive phase-space norm, requires the excluded finite polynomial closure, or defines its coefficients through ratios containing unknown physical zeros. Separate absolute overlap estimates are not a signed correlation.

A local calibration does not cover all stationary branches. Promotion requires both signs on open predecessor neighborhoods, all relevant positive times and heights, compatible boundary crossings and errors at the vanishing first-jet scale. This initialized program supplies none of that coverage yet.
