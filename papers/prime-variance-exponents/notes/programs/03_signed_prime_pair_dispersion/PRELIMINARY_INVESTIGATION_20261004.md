# Preliminary investigation: a complete exception and shift budget

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
These are internal deductions and a bounded primary-source audit, not an
independent specialist review. No new global exponent is proved.

## Outcome and inherited inputs

The pair route remains a good third program. The useful next input is a
signed aggregate estimate; a weaker substitute is an almost-all-shift
estimate with **both** power-saving error and a power-saving exceptional
set. The calculation below charges every omitted or exceptional shift,
including a useful cheaper budget at the extreme upper endpoint.

Use the probe and target from the [overview](../../PROJECT_OVERVIEW_20261004.md).
The inherited [exact pair identity](../../../../investigations/sonin-critical-boundary/notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md)
and [constant-order model evaluation](../../../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md)
give, for every sufficiently large real X,

\[
\mathcal R=-2\sum_{1\le h<h_*}\int_{l_h}^{u_h}E_{X,h}(t)D_{X,h}(t)\,dt,
\qquad \mathcal V_g=\beta_gX^2+\mathcal R+o(X^2),\quad
\mathcal R_-=O(X^2),
\]
\[
c=B/A-1,\quad h_*=2(B-A)X,\quad
l_h=\max(AX,h/c),\quad u_h=2BX-h,\quad
D_{X,h}(t)=\frac d{dt}W_X(t,t+h).
\]

The full weight vanishes at both endpoints, satisfies |D|=O_g(1),
and retains both shell caps. Here E is the actual cumulative
von Mangoldt pair count minus the singular-series density, starting at
l_h. The target is only \(\mathcal R_+\ll X^{3-\kappa+o(1)}\),
for one fixed \(0<\kappa\le1\). An absolute estimate below is a sufficient
condition, not an asserted necessity.

## Fresh deduction: good shifts, exceptions, and partial sums

Put \(e_h=\sup_{l_h\le t\le u_h}|E_{X,h}(t)|\),
\(L_h=u_h-l_h\), and \(v_h=\int|D_{X,h}|\).
Then, without assuming the sign of a shift contribution,

\[
|\mathcal R|\le2\sum_hv_he_h,\qquad v_h\ll_g L_h\ll_g X. \tag{1}
\]

The elementary uniform bound is
\(e_h\ll (L_h+1)X^{o(1)}\): use
\(\Lambda(n)\le\log(2BX)\), at most \(L_h+1\) integer points,
and \(\mathfrak S(h)\le X^{o(1)}\). The last inequality follows from
the explicit product: for fixed epsilon, all sufficiently large prime
factors contribute at most \(p^\epsilon\), and the finitely many small
factors contribute a constant. Thus for ordinary shifts the safe cost
per exception is \(X^{2+o(1)}\). No unproved prime-pair asymptotic is used.

If all good shifts satisfy \(e_h\le X^{1-\eta+o(1)}\), while there
are at most \(X^{1-\eta_E+o(1)}\) exceptions, (1) yields

\[
|\mathcal R|\ll X^{3-\eta+o(1)}+X^{3-\eta_E+o(1)}. \tag{2}
\]

Hence one may take \(\kappa=\min(1,\eta,\eta_E)\). If the exceptional
errors themselves save \(X^{\xi}\), their cost improves to
\(X^{3-\eta_E-\xi+o(1)}\). Every bound on good shifts must hold
simultaneously for the full partial-sum range t: a different exceptional
set at each t is insufficient without controlling their union.

| Proposed information | Charged variance/remainder exponent | First fixed saving |
| --- | --- | --- |
| All shifts: \(e_h\le X^{1-\eta+o(1)}\) | \(3-\eta\) | \(\kappa\le\eta\) |
| Good shifts as above; \(X^{1-\eta_E+o(1)}\) arbitrary exceptions | \(\max(3-\eta,3-\eta_E)\) | Both exponents must save |
| Uniform square-root errors \(e_h\le X^{1/2+o(1)}\) | \(5/2\) | \(\kappa=1/2\) |
| Square-root good errors; \(X^{3/4+o(1)}\) arbitrary exceptions | \(11/4\) | \(\kappa=1/4\) |
| Errors and exceptional fraction each save only log powers | \(3\), with log improvement | None from this estimate |
| \(\sum_he_h^2\le X^{3-2\eta+o(1)}\) | \(3-\eta\) by Cauchy–Schwarz | \(\kappa\le\eta\) |
| Complete signed weighted sum \(-2\sum_h\int ED\le X^{3-\kappa+o(1)}\) | \(3-\kappa\) | Direct target; no separate exception theorem |

These rows also charge a major/minor-arc decomposition: if the *signed*
major and minor contributions have exponents \(3-\eta_M\) and
\(3-\eta_m\), and unhandled shifts number \(X^{1-\eta_E}\),
the sufficient saving is \(\min(\eta_M,\eta_m,\eta_E,1)\).
The singular-series calculation evaluates a model main; it cannot serve
as the actual major-arc error estimate.

## Fresh deduction: which shift ranges can be left to trivial bounds?

For a lower tail \(1\le h\le X^\theta\), with \(0\le\theta\le1\),
(1) gives \(X^{2+\theta+o(1)}\). It can be left untreated when
\(\theta\le1-\kappa\). In particular finitely many fixed shifts are
within the quadratic budget; solving the twin-prime problem is not a
separate prerequisite of this sufficient route.

For the upper tail \(0<h_*-h\le X^\theta\), with \(0<\theta<1\),
one instead has exactly

\[
L_h=\frac{B}{B-A}(h_*-h).
\]

Its total cost is
\(\sum_hL_h(L_h+1)X^{o(1)}\ll X^{3\theta+o(1)}\),
so it may be discarded at a cost within the target if
\(\theta\le1-\kappa/3\). Integer rounding near h_* is covered by
the +1. For example, at a proposed \(\kappa=1/10\), the sufficient
unresolved shift region is

\[
X^{9/10}<h<2(B-A)X-X^{29/30}.
\]

This region still includes a proportional number of shifts of size X.
A theorem only covering \(h\le X^{1-\epsilon}\) cannot fill it.
These are algebraic budget deductions; no estimate for its actual prime
errors is obtained.

## Source check and bounded next investigation

[Matomäki–Radziwiłł–Tao, v3, Theorem 1.3(i), p. 8](https://arxiv.org/pdf/1707.01315)
gives errors \(O_A(X\log^{-A}X)\) for all but
\(O_A(H\log^{-A}X)\) shifts in its stated long-shift range;
footnote 6 discusses extension to H comparable to X. It does not state
our simultaneous capped partial-sum estimate. Even granting that extension
and partial-sum uniformity, the logarithmic row above yields no fixed
power. The source's divisor variants cannot be substituted for prime
correlations. This is a bounded source audit, not an exhaustive literature
claim.

The next viable pair project is to write a cap-preserving signed
dispersion identity on the unresolved middle shift region and isolate a
specific arithmetic term with a power-saving conjecture. Use (2) as a
pass/fail check before a larger theorem search. Prefer a weighted
exceptional cost \(\sum_{h\in\mathcal E}v_he_h\) to an unweighted count
when the mechanism naturally places exceptions near the top endpoint.
Do not infer such localization from the mere number of exceptions.

Assessment: more ready than programs 05 and 09 below, but currently lacks
the arithmetic input. The work done here is a complete exponent budget,
including an endpoint saving, rather than evidence of cancellation.
