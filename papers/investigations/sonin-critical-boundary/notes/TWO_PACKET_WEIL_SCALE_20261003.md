# Weil form size for the two packet obstruction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort are not exposed and are not inferred. The lead and a separate same-model agent independently checked the scaling argument. This is internal research, not specialist refereeing.

This supplements the [translated resonance proof](FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md). Its normalized counterexamples to the strong correction sign have a Weil form tending to positive infinity. They therefore illustrate the failure of the strong Sonin comparison without approaching a failure of the weaker arithmetic comparison.

Let a=log 2, epsilon=2^{-N}, and use that note's real compact mean-zero profile g, f=-g'', f_epsilon=f+epsilon²g/4 and paired prepared source F_epsilon. Put G_epsilon=F_epsilon/||F_epsilon||_2. The packet supports are disjoint for small epsilon, and the total support can be kept strictly inside the length-one window.

## Exact normalization and prime term

Disjointness gives

\[
\|F_\varepsilon\|_2^2=2\varepsilon^{-1}\|f_\varepsilon\|_2^2,
\qquad
|\widehat G_\varepsilon(t)|^2
=\frac{\varepsilon}{\|f_\varepsilon\|_2^2}
 (1+\cos(at))|\widehat f_\varepsilon(\varepsilon t)|^2.
\]

At shift a, precisely one pair of identical packets overlaps. Consequently kappa_G(a)=1/2 exactly. Only the first power of prime 2 is arithmetically active, so

\[
W_{\{2\},1/2}[G_\varepsilon]=\frac{\log2}{\sqrt2}.
\]

## Archimedean asymptotic

The [digamma expansion, DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) implies

\[
\gamma_\infty(t)=\log(|t|/(2\pi))+O(|t|^{-2})
\quad (|t|\longrightarrow\infty).
\]

Rescale u=epsilon t in Gamma[G_epsilon]. The coefficient of log(1/epsilon) is exactly one: the nonoscillating integral is ||f_epsilon||² and the oscillating integral is its autocorrelation at a/epsilon, which vanishes once that shift is outside the fixed correlation support.

For the remaining multiplier, gamma_infinity(u/epsilon)-log(1/epsilon) tends to log|u|-log(2pi). On |u|<=epsilon its absolute value is bounded by C+|log|u||; on |u|>=epsilon the digamma estimate gives a comparable bound, with logarithmic growth at infinity. The transforms of f_epsilon have uniform Schwartz decay. Dominated convergence therefore gives convergence of the nonoscillating integral and L1 convergence of the weighted integrand. Riemann-Lebesgue then makes the oscillating remainder tend to zero. It follows that

\[
\Gamma[G_\varepsilon]=\log(1/\varepsilon)+c_f-\log(2\pi)+o(1),
\qquad
c_f=\frac{1}{2\pi\|f\|_2^2}
\int_{\mathbb R}|\widehat f(u)|^2\log|u|\,du.
\]

This integral is finite. Combining the exact prime term and pole neutrality yields

\[
Q[G_\varepsilon]=\log(1/\varepsilon)
+c_f-\log(2\pi)-\frac{\log2}{\sqrt2}+o(1)
\longrightarrow+\infty.
\]

The resonance theorem independently gives

\[
K[G_\varepsilon]=c_g\varepsilon+o(\varepsilon),\qquad c_g>0.
\]

Since B=Q+K on this support-adapted class, B also grows logarithmically and K/B tends to zero. These statements are asymptotic; no finite threshold or outward numerical enclosure is asserted.

## Consequences for continuation

The obstruction rules out K at most zero and finite-rank penalty domination of this correction. It does not refute K at most B. Infinitely many positive directions need not be large relative to the positive trace.

An explicit finite-width witness would validate a concrete instance and provide a reproducible benchmark for the resonance and numerical methods. Once the analytic proof is accepted, it is unnecessary for the qualitative refutation and does not supply a replacement positivity mechanism. Forward work would need a joint estimate comparing the positive resonant contribution with a controlled part of B, or a different positive operator construction. Merely renaming K at most B as the target restates the unresolved Weil positivity problem.
