# Finite-horizon two-packet Weil detector

12 October 2026. Prepared for Edward Baker. Model: GPT-6-astra (Codex); reasoning effort: ultra, verified from the session configuration. Prepared with substantial LLM assistance. Internal checks are not independent mathematical validation.

[Investigation portfolio](../../README.md)

## Objective and status

**Scoped; research not started.** Determine whether two separated, oppositely signed packets improve a certified finite-horizon Weil detection or exclusion problem. This is an exploratory cost comparison against the existing Weil-depth framework, not a claimed quasi-RH descent mechanism. Reuse the existing quadratic form, normalization, and certification infrastructure through links.

For the centered transform $G(s)=\int g(u)e^{(s-1/2)u}\,du$, take an even, nonnegative compactly supported packet $\varphi$ and

\[
g(u)=e^{-i\gamma u}\{\varphi(u-L/2)-\varphi(u+L/2)\}.
\]

At a hypothetical zero $\rho=1/2+a+i\gamma$, the paired contribution is

\[
G(\rho)\overline{G(1-\bar\rho)}
=-4\Phi(a)^2\sinh^2(aL/2),
\qquad \Phi(a)=\int\varphi(v)e^{av}\,dv.
\]

This exact calculation repairs the claim that translation factors always cancel. It does not establish negativity of the complete Weil functional.

## First bounded task

Declare a finite target $a\ge a_{\min}>0$, $|\gamma|\le T$, a compact packet shape and width, and an allowed horizon. Derive the complete quadratic-form and error ledger for this family under the existing manuscript's conventions. Compare its detection margin, conditioning, support cost, and certification effort with the existing finite-horizon basis on the same declared target.

If a parameter grid is used, distinguish sample diagnostics from uniform coverage: a finite grid requires an explicit interpolation or enclosure argument before it supports a claim for every target in the region. The first milestone is a complete cost comparison, not an isolated large negative zero contribution.

## Deliverables

- A normalization and admissibility note connecting the two-packet family to the existing complex-test framework.
- A ledger including other zeros, pole and archimedean terms, the prime side, truncation, and numerical conditioning.
- A bounded pilot with reproducible parameters and appropriately labelled numerical or certified results.
- A review explaining whether the proposed family improves a concrete finite problem and what prevents a uniform extension.

## Continue and stop tests

Continue if the complete test yields a better certified margin, smaller useful horizon, or lower certification cost than the baseline. Stop or redesign if an apparent gain disappears after the remaining contributions and conditioning are included. Stop treating this as global descent if the horizon depends uncontrollably on $a_{\min}$ or $T$.

Quasi-RH bounds displacement from the critical line above; it does not supply the positive lower displacement needed here. Arbitrarily small displacements and unbounded heights remain. If $\varphi$ has support in $[-w,w]$, the combined support spans $L+2w$, and the prime-side calculation reaches a scale of order $\exp(L+2w)$. Increasing packet separation therefore has a substantial cost that must be assessed with the exact functional.

## Inherited work and records

Start from the [two-packet calculation and bounded task](../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md), its [cross-assessment](../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md), and the [finite-horizon Weil manuscript](../../../weil-positivity/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex). Compare with existing work before claiming novelty.

Place research in `notes/`, computations and small records in `numerics/`, reviews in `reviews/`, and conversation provenance in `chat-histories/`. Follow the [large-file policy](../../../../LARGE_FILES.md); large regenerable data remain outside Git. At notable milestones update `DRAFT_HISTORY.md` with concise commit/tag references and links. Do not create manuscript snapshot directories.
