# Initial research program for complete paired kernel factorization

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**.
Status: **initialized, awaiting Claude review**. No new kernel factorization, Gram computation or positivity certificate has been produced.

## Source contract and established seed

This program develops [search card 6](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#6-paired-kernels-and-positive-factorizations). Use the complete theta source `m_t(u)=e^{tu²}Φ_e(u)`, with every theta term and every cross contribution retained. With Fourier convention `f̂(x)=∫e^{ixu}f(u)du`, define

\[
J_{j,t}(s)=\int_{\mathbb R}r^2(r^2-s^2)^j
m_t(s+r)m_t(s-r)\,dr.
\]

The [complete-kernel note](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md) proves the exact normalization

\[
(H_t^{(j+1)}(x))^2-H_t^{(j)}(x)H_t^{(j+2)}(x)
=\widehat J_{j,t}(2x).
\]

For `j=0,1`, these are the first Laguerre expressions of `H` and `H_x`, respectively. Their source positivity language has a classical precedent in [Csordas's kernel analysis](https://arxiv.org/abs/1309.0055). The local identities and imported comparisons are seeds; no uniform positive-definiteness theorem for the required theta kernels is available here.

## Research objective

Derive from actual theta addition, reflection or arithmetic pairing a convergent autocorrelation factorization of `J_0,J_1`, or a weaker factorization after the physical stationary constraints are imposed. An independently derived global autocorrelation representation would make the Fourier response nonnegative. The weaker direct targets are

\[
\widehat J_{0,t}(2x)\ge0\quad(H_x=0),\qquad
\widehat J_{1,t}(2x)\ge0\quad(H_{xx}=0).
\]

Both signs are needed by the [all-multiplicity predecessor criterion](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md). The factorization must be justified from the source, rather than inferred from an assumed all-real zero product.

## First bounded task

Apply one explicit theta addition or modular-gluing identity to the complete paired source before separating individual product channels. Derive the resulting matrix-valued or integral kernel with exact normalization. Identify the precise quadratic form whose positivity would establish one of the physical stationary signs, and state its convergence and operator domain.

Choose a compact time interval and a finite source/frequency window for the first diagnostic. If Gram minors are computed later, retain complete-source remainder bounds and outward arithmetic. A negative minor is a valid falsification only after its full tail payment is included. A passing finite matrix is a finite test, not the positive-definiteness theorem. The [paired contour bounds](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md) may supply an existing analytic envelope on their stated domain.

## Validation failure criterion and exclusions

Distinguish pointwise positivity, positive definiteness of the source kernel and positive definiteness of its Fourier response. Pointwise `J_0>0` does not prove the needed Fourier sign. Recorded genuine values of `J_1` are negative; that refutes pointwise positivity but does not refute positive definiteness. Preserve the signed factor `(r²−s²)` and every divisor-channel endpoint.

Continue if the complete identity reveals an independently positive quadratic form, a controllable signed remainder or a stronger conditional covariance. Stop the specific factorization if it assumes real zeros, drops the second kernel, omits endpoint partners or demands pointwise positivity already contradicted by the genuine source. Raw full-line product Mellin exchanges at positive heat need a fresh convergence proof and cannot replace modular gluing.

One first-level sign does not detect triples. A bounded successful factorization still needs open predecessor coverage, all relevant times and heights, cutoff compatibility and errors appropriate to a vanishing first jet before it can support an RH implication. The initialized program claims none of those global conclusions.
