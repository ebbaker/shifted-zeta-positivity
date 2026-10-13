# Initial research program for gaussian hermite correlations

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**.
Status: **initialized, awaiting Claude review**. No new Gaussian integration, coefficient survey or physical certificate has been run.

## Source contract and established seed

This program implements [search card 10](../../../inactive/brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#10-gaussian-hermite-coefficients-and-source-selected-correlations). The input is the actual complete time-zero theta transform

\[
H_0(z)=\tfrac18\xi((1+iz)/2),\qquad
f_{t,x}(Z)=H_0(x+i\sqrt{2t}Z),
\]

where `Z` is standard normal and `t>0`. This is not a freely chosen analytic Gaussian state or a raw divisor-channel continuation. Complete theta decay supplies the Gaussian/source domination required by the [exact readout note](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md).

Write `a=Re f`, `b=Im f`, and `s=√(2t)`. The real coefficients are `m0=E[a]`, `m1=E[Zb]`, `m2=E[(Z²−1)a]`, and `m3=E[(Z³−3Z)b]`. They recover the physical jets exactly:

\[
H=m_0,\quad H_x=m_1/s,\quad H_{xx}=-m_2/s^2,
\quad H_{xxx}=-m_3/s^3.
\]

Hermite Parseval gives a positive norm of the entire coefficient sequence. That norm does not prevent simultaneous vanishing of its first two coordinates. The earlier [Gaussian-lift scout](../../../../quasi-rh-exponent-descent/newman_collisions/01_analytic_gaussian/README.md) supplies explicit generic controls and the existing scope boundary.

## Research objective

Find a modular, reflection or arithmetic relation that restricts the actual low Hermite coefficients, or relates them to a controlled higher-order tail. A zero-loss sufficient target is `m0 m2≥0` when `m1=0`, together with `m1 m3≥0` when `m2=0`. A qualified bounded-loss alternative is

\[
m_0m_2\ge-s^2C_0m_0^2\quad(m_1=0),
\]

\[
m_1m_3\ge-s^4C_1(m_0^2+m_1^2/s^2)\quad(m_2=0),
\]

with the local boundedness and predecessor hypotheses required by the existing criterion. The joint-energy denominator must remain intact. An unproved bound of the whole Gaussian norm by first-jet energy would simply reintroduce the observation problem.

## First bounded task

Transport one complete angular-gluing or two-source addition identity through the specified Gaussian transform. Derive its coefficient relation before numerical evaluation, stating Fubini, growth, normalization and endpoint requirements. Determine whether it constrains theta coefficients independently or merely restates the jet dictionary.

For a later outward comparator, select a small set of genuine stationary cells from [the corrected theta interface](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md). Compare all four Gaussian moments with the corresponding physical jets, paying complete-xi evaluation errors and Gaussian tails. Such cells are calibrations; agreement adds no global collision coverage where the existing first jet already excludes a joint zero.

## Validation failure criterion and exclusions

Check the factors of `i`, Hermite normalization, even/odd conjugation and powers of `s`. Spatial derivatives hold time fixed. Time identities differentiate `s`, normalization and every source dependence. A finite coefficient relation must include its omitted tail. The `t=0` limit needs direct jets or justified rescaling rather than literal division by zero.

Test any proposed signed relation against the earlier Gaussian double and triple collision controls. Continue if theta preparation forces a new coefficient correlation or yields a stronger independent source comparator with controlled error. Stop the specific claim if parity, generic Gaussian positivity or an arbitrary coefficient truncation supplies its only justification.

The eventual target is a uniform source estimate on the necessary stationary predecessor neighborhoods. A bounded experiment or positive Parseval norm is not that theorem, and neither establishes RH or a new zero-free region.
