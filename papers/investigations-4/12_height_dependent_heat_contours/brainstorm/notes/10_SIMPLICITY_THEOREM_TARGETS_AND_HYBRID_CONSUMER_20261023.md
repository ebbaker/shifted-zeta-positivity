# Strong simplicity targets and a hybrid multiplicity consumer

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Two contributing agents using the same model checked the literature calibration and multiplicity algebra. This is a research discussion with an elementary proved consumer; it is **not a new theta resource estimate, improved simplicity proportion, or specialist review**.

**Subsequent program clarification, 23 October 2026:** the [new research overview](../research-overview/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md) and [progress register](../research-progress/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRESS_20261023.md) govern the research direction. The author asks for the best analytic result available toward RH implying simple zeros, with no fixed theorem form. The density-one headline, quantitative rate and microscopic clock proposed below are candidate outcomes and mechanisms, not commitments. The proved hybrid consumer and its calibration retain their stated status. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**.

The author wants the best result available and explicitly permits replacing or rewriting `book.tex` if a superior argument emerges. No manuscript was edited in this discussion. Percentage thresholds below are diagnostics, not a ceiling or a decision to settle for a weaker objective.

Read the repository [result index](../../../../../result-summaries/README.md), especially [local heat geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../avoid/README.md), especially [target reformulation](../../../../../avoid/01_restating_the_target.md), [shared premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coupled estimates](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scoped conclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). This note continues [Continuation 09](09_CONTINUATION_BOOK_PROOF_AND_ARITHMETIC_RELATIVE_FLUX_20261023.md), [book.tex](../../manuscript/book.tex), and the [spectral section of main.tex](../../manuscript/spectral_forest.tex).

## 1. The strongest currently motivated headline

The best-supported direction is RH-conditional simplicity, with the principal target

\[
 \mathrm{RH}\Longrightarrow N(T)-N_s(T)=o(N(T)).
 \tag{1}
\]

Here N counts all nontrivial zeta zeros with 0<Im rho<=T with multiplicity, and N_s counts simple zeros. A quantitative strengthening worth seeking is

\[
 N(T)-N_s(T)\ll N(T)(\log T)^{-\delta}
 \quad\text{for some proved }\delta>0.
 \tag{2}
\]

Neither a positive exponent nor (1) has been acquired. A proof of (1) would already be a substantial result. Every-zero simplicity is a separate stronger target: a diverging exceptional-count allowance permits sparse multiple zeros. The current machinery gives consumers at both strengths, but does not show that the needed arithmetic estimates are attainable.

The checked RH-only benchmark is **19/27** simple, from [Bui–Heath-Brown](https://arxiv.org/abs/1302.5018). [Lamzouri's September 2026 introduction](https://arxiv.org/html/2609.02882v2) still records this benchmark. A smaller proportion alone would not improve the known numerical result, though a new quantitative local or heat-stability theorem might have a separate contribution. No complete priority survey is claimed.

## 2. An improved consumer using existing arithmetic

For the endpoint population up to T write

\[
 M=N-N_s=\sum_{m_\rho\ge2}m_\rho,\qquad
 C=\sum_{\rho\ \mathrm{distinct}}m_\rho(m_\rho-1),\qquad
 B=\sum_{m_\rho\ge2}2\lfloor m_\rho/2\rfloor.
\]

Assume RH, so these endpoint sites are real in the H coordinate. Let R be the sum of the book's complete resources over windows covering these sites with total endpoint weight at least one:

\[
 R=\sum_j\left(N_{\psi_j,\mathrm{nr}}(a_j)
                  +F^+_{\psi_j,\mathrm{nr}}\right).
\]

All windows have endpoint time zero. Different initial times are allowed, but each resource is computed for its own genuine heat trajectories. The balance gives B<=R; earlier collisions, recrossings and localization can make R larger. No flux or exterior population is dropped.

**Elementary hybrid bound.**

\[
 \boxed{M\le\min\left\{N,C,\frac32R,\frac{3R+C}{4}\right\}.}
 \tag{3}
\]

The first three bounds are immediate. For the fourth, for every integer m>=2,

\[
 m\le\frac34\,2\lfloor m/2\rfloor+\frac14m(m-1).
 \tag{4}
\]

For m=2k its right side minus m is k(k-1); for m=2k+1>=3 it is k^2-1. The slack is nonnegative, with equality exactly at m=2,3. Summing and using B<=R proves (3).

The gain is structural: the book's 3/2 factor is worst at triples, whereas M<=C is worst at doubles. Coupling avoids paying both worst cases independently. For abstract multiplicity populations, the envelope in (3) is asymptotically sharp, subject to integer rounding and available total population. In the mixed region R<=C<=3R, take (3R-C)/4 double sites and (C-R)/4 triple sites, then add simple sites. For C<=R use doubles; for C>=3R use triples. This is optimality for these two upper-budget inputs, not an optimality claim about every arithmetic argument.

[Chirre–Gonçalves–de Laat, Theorem 1](https://arxiv.org/pdf/1810.08843v2) proves under RH

\[
 Q(T):=\sum_{\rho\ \mathrm{distinct}}m_\rho^2
       \le(1.3208+o(1))N(T).
\]

Their sum N* is taken over repeated zero labels with summand m_rho, hence equals Q here. Therefore C=Q-N<=(0.3208+o(1))N. From (3), if limsup R/N<=r, then

\[
 \liminf\frac{N_s}{N}\ge
 \max\left\{\frac{19}{27},\ 1-\frac32r,\ 0.9198-\frac34r\right\}.
 \tag{5}
\]

The 19/27 entry imports the existing theorem; the other entries are the calibrated consumers. None supplies an upper estimate for R.

| Complete resource estimate to prove | Consequence under RH |
| --- | --- |
| limsup R/N < (32/27-0.3208)/3 = 0.288128395... | Strict improvement over 19/27 |
| R <= (0.28+o(1))N | At least 70.98% simple |
| R <= (1/4+o(1))N | At least 73.23% simple |
| R <= (0.2264+o(1))N | At least 75% simple |
| R=o(N) | Density-one simplicity |
| R << N/(log T)^delta | Same exceptional-count rate, with factor 3/2 |

For small r the standalone 3R/2 bound is stronger than the hybrid. The fixed published moment bound does not by itself turn a constant resource fraction into density one.

These are **cumulative** statements. A global upper bound on Q(T) cannot be subtracted from another upper bound to obtain the same constant on (T,2T]. Dyadic acquisitions must be assembled into cumulative R(T), or supplied with a separately justified local moment theorem. Omitted labels need their own allowance; o(N) omissions preserve density results, but a fixed positive omitted fraction consumes the claimed improvement.

## 3. What the substantive arithmetic theorem should say

A promising target, stronger than a mere endpoint reformulation, is quantitative microscopic backward stability. On a band of zeta height h, the H-coordinate density is

\[
 \nu_h=\frac1{4\pi}\log\frac{h}{2\pi}
\]

at leading order; H's real coordinate is twice the zeta ordinate. Prescribe a_j=-lambda/nu_h^2 for a positive dimensionless lambda on each sufficiently high band. Include a fixed initial region separately. Construct complete windows by an explicit source-controlled rule, with all joins, overlap and outer flux paid. The desired theorem is

\[
 \limsup_{T\to\infty}\frac{R_T(\lambda)}{N(T)}
       \le A(\lambda),\qquad A(\lambda)\to0\quad(\lambda\downarrow0).
 \tag{6}
\]

Take the height limit first at fixed lambda, then lambda down to zero. This would imply (1). A uniform estimate and effective remainder may permit lambda=lambda(T) and yield (2), but the two-limit assertion alone gives no quantitative rate.

Classification: (3) is a proved generic consumer; (6) is an **unproved arithmetic target**, not progress merely because it has been formulated. Allowing the time to be chosen after resolving the unknown endpoint multiplicities returns to the reformulation described in [parent Note 05](../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md). A proof must use complete theta/xi arithmetic to establish useful size. A small reference error controls neither its own clustered zeros nor the earlier nonreal population. Estimating only the determinant's flux leaves the latter unpaid. Full pair-correlation assumptions would also import a known route to density-one simplicity rather than prove it from RH alone.

## 4. Compare routes by the missing estimate

The positive-time route in main.tex has M<=4q(t). RH supplies the complete real simple system for t>0; its corrected microscopic Riemann–Siegel reference is more concrete arithmetic infrastructure than the generic anchor in book.tex. A source-prescribed q=o(N) would also prove (1). Its direct short-gap equivalence is a diagnosis, not an arithmetic bound. An all-simple local threshold is q<1/2.

The negative-time route has the simpler population/relative-flux meaning and the hybrid advantage (3). It needs earlier nonreal discrimination in addition to the relative-flux estimate. Appending C to q does not similarly improve the key double-dominated constant: both M<=4q and M<=C are sharp at doubles. This is a reason to investigate both routes against actual arithmetic estimates; there is no theorem that one route must win. The eventual manuscript should center the estimate that succeeds, even if that requires replacing book's present organization.

For every-zero simplicity, complete local windows with R<2 exclude a real multiple site. This demands control below one event, including at sparse exceptional locations; an average estimate cannot do it. No present source estimate supplies that bound at all heights.

The book's balance itself is not intrinsically conditional on RH. If windows cover the full endpoint zero strip, let O count off-line labels and M_real count nonsimple real labels. It gives

\[
 O+\tfrac23 M_{\mathrm{real}}\le R,
 \qquad N_{\mathrm{simple,critical}}\ge N-\tfrac32R.
\]

These follow immediately from the existing balance. An unconditional R=o(N) would therefore imply density-one simple critical-line zeros. The current work has substantially less arithmetic support for that estimate than for an RH-conditional simplicity program.

## 5. Controls and status

The quadratic and cubic heat fields satisfy (3), and attain (4). At a single wholly multiple endpoint population they fail the proposed small-resource targets. Euler-factor, weighted-square, reflected and primitive-compatible controls obey the generic consumer; the new algebra does not exclude them. Their failures of unchanged canonical coefficients, full reflection, or ordinary Dirichlet-series arithmetic are recorded in the control register, but naming those failures does not prove (6). Source ordering alone still admits the positive weighted-square controls.

The theta-close endpoint controls particularly warn against obtaining every-zero simplicity from a fixed source tolerance; their ordinary Dirichlet-series arithmetic fails. Sparse doubles may coexist with a true density-one theorem, so such a control need not fail every density-one premise. Any claimed arithmetic estimate must be screened on controls that actually contradict its stated conclusion and scale.

No new theta estimate, global proportion, rate, or OBF completion is claimed. The concrete advance of this discussion is the checked hybrid consumer and the resulting stronger calibration. No manuscript, milestone snapshot, numerical campaign or benchmark certificate was produced. The principal research objective remains the strongest arithmetic exception bound available, with (1) and ideally (2) as the headline targets.
