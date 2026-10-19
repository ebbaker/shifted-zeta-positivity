# UAR-05: internal review of the paid bounded anchor

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Separate delegated same-model analytic/consumer review, including an independently written elementary interval evaluator; this is internal LLM work, not independent specialist human review or implementation independence of every premise.

**Review status: passed at the bounded anchor/separation gate.** The [formal note][note] proves a strict first-jet and physical-energy margin on its exact closed box. A fresh 192-bit replay of the final producer passes, as recorded in the [source-pinned reviewer receipt][receipt]. UAR-05 can be marked Complete for this bounded contract; UAR-06 receives only this contract. Uniform separation across every J_t remains open. Direct endpoint certification retains the smaller error, so no stronger-margin or total-cost advantage is established.

## Analytic contract reviewed

The deliberately bounded domain is

\[
T=[1/20-10^{-14},1/20],\quad x_0=4\pi e^{20}+1,
\qquad X=[x_0-.01,x_0+.01].
\]

It is a closed positive-time box within the UAR sector, with frozen natural cutoff 22026. This restriction must be checked at its endpoints, including the time-dependent left sector boundary and both extremal disk cutoffs. The profile is near .0684, so this particular box permits ordinary analytic division by its nonzero cosine denominator. This does not justify division at removable half-integers elsewhere.

The normalized sum uses the entire full-cutoff weights

\[
p_n=\exp[-s\ell_n+t(\ell_n^2-2\alpha(s)\ell_n)/4],
\quad P=\sum_{n\le22026}p_n,
\quad s=(1-ix)/2,
\]

and its exact spatial derivatives with t and N frozen. In particular

\[
\lambda_n=i\ell_n(1+t\alpha'(s)/2)/2,
\quad P''=\sum p_n[\lambda_n^2+t\ell_n\alpha''(s)/8].
\]

The last positive term comes from \(s_x=-i/2\); dropping it or reversing its sign would change the consumer. With \(\beta=\alpha(1+t\alpha'/2)\), the identities \(\omega=-\Re\beta/2\), \(b=\Im\beta/2\) and \(\omega_x=-\Im m_t''/4\) have the correct orientation.

The reviewer independently re-derived the primitive

\[
Z_{G/A}=2P-\frac{i}{\omega}[P'+e^{-2i\theta}\overline{P'}]
\]

and its derivative. The derivative has \(-2e^{-2i\theta}\overline{P'}\), \(-i(P''+e^{-2i\theta}\overline{P''})/\omega\), and \(+i\omega_x(P'+e^{-2i\theta}\overline{P'})/\omega^2\). For \(C=\widehat C_N^{an}/A\),

\[
Z_C'=e^{-i\theta}\{-i\omega C-iC''/\omega
 +i\omega_x C'/\omega^2\}.
\]

The two ordinary \(C'\) terms cancel before a norm. Subtracting this derivative from the finite one retains the prescribed corrected approximation. A series with an interval constant coefficient and a unit linear coefficient encloses all frozen derivatives at once; it does not differentiate the interval endpoints or the cutoff.

## Independent elementary acquisition

The separate reviewer probe imported only S02's elementary m0, alpha and analytic profile formulas, rather than its B-only evaluator. At t=1/20 and x=x0, a new 192-bit full 22,026-mode sum gave

\[
f=.403818865956330167\ldots,\quad
f_x=7.45220685579726808\ldots,\quad
\omega=-5.00000000004261562\ldots,
\quad |J_f|=1.54417782568202355\ldots.
\]

The prefactor was evaluated through S02's exact real scaled expression W_real, independently of the producer's exponential difference of large logarithms. A complex second-order series on the whole selected box gave \(C_{xx}\) near \(-2.22215\times10^{-14}\), with enclosure radius below \(4\times10^{-20}\). The primitive and phase conventions agree with the producer derivation. These point and component checks do not themselves enclose the complete box or replace its derivative propagation.

## Payments and physical return

The UAR-04 pointwise envelope

\[
E(c)=1.53S_c+\Delta_{AB}(c)+9\epsilon_c
\]

is a legitimate complete acquisition error for the physical anchor, even though no direct H integral is evaluated. This certifies a physical anchor by enclosure, not an independently measured residual value. The t-band is enclosed directly, so there is no uncharged time interpolation.

UAR-04's primary increment starts at \(a_t=4\pi e^{1/t}\). Re-centering it at x0 costs **2B(t)**, since
\(I(x_0,x)=I(a_t,x)-I(a_t,x_0)\). This holds also for x<x0. Each primary prefix owns all its switches according to UAR-01; the absence of a switch in X does not permit replacing this paid rebase by B without an additional proof.

The resulting physical inequality must retain anchor acquisition E, approximant propagation, and 2B as separate payments. The same-information direct comparator pays E at the endpoint and uses the same approximant propagation. Its error is smaller than E+2B. Thus strict positivity of this box can pass UAR-05 while an improvement or cost claim fails. A local two-endpoint residual payment can improve on 2B, but adding it to an already paid anchor E yields 3E; the direct comparator still pays only E.

For the physical energy, the exact map is

\[
\frac1A\binom{H}{H_x}
=\begin{pmatrix}1&0\\b&-\omega\end{pmatrix}
\binom{Q}{-Q_x/\omega}.
\]

A positive minimum singular-value bound must be paid. The determinant/Frobenius lower estimate is sufficient on this box; \(Q_x\) cannot be identified with \(H_x/A\). Since A is real positive, a lower bound for \((H^2+H_x^2)/A^2\) is meaningful without numerically underflowing A.

## Scope and controls

This is a single small closed box near height 6.097e9. It is new bounded physical validation in the investigation's uncovered real region; it is not a general anchor selection mechanism on every J_t, an exhaustion argument, a uniform bridge, a complex-wall theorem, or a Newman bound. UAR-06 may compare this exact bounded consumer. UAR-E1 remains conditional on its separate cost/coverage gate.

The final producer's actual paid-consumer helper rejects the polynomial event using its own variation, rejects uncertainty equal to the nominal anchor and residual increment equal to the nominal anchor, and accepts an exact nonzero oscillator. Omitting each required payment would create a false positive in the corresponding fixture. Its guards reject all four negative input positions, a nonfinite input, altered domain widths, t=0 and an inexact domain parameter. The producer also checks the fixed cutoff and profile denominator before evaluation. Replaying an old source screen alone would not exercise this newly changed physical acceptance interface. The five freshly replayed inherited source-specific event boxes and Euler negative-Laguerre witness retain their own-source scope; theta constants are not substituted into those sources.

## Final code and fresh execution

The reviewed producer has SHA-256 `56db653c379f9ebb4b6954e972a06552487b1984b5330bdd0831cd143a2109bf`. The reviewer receipt binds that script, the staged formal note and control bytes intended for installation, and the currently read inherited sources. The installing root agent must check installed byte identity; the reviewer did not mutate the research checkout. The fresh same-producer 192-bit execution gives

| Quantity | Outward result sufficient for acceptance |
| --- | ---: |
| Whole-box supremum of the signed approximant derivative | <100.509370 |
| Anchor-to-cell variation payment | <1.00509370 |
| Complete acquired anchor error | <1.3409300e-7 |
| Global increment after correct rebasing | <5.6897500e-7 |
| Paid rotating first-jet margin on the whole box | >.5390834252 |
| Same-information direct rotating margin | >.5390839942 |
| Physical determinant/Frobenius factor | >.9776855124 |
| Physical Euclidean first-jet norm divided by A | >.5270540548 |

The formal note's conservative headline `(H^2+H_x^2)/A^2>.27` follows. No numerical value of the exponentially small physical A is needed. The full time-band anchor radius is above 1.5441778256; all finite modes, near-cutoff heat weights, reflected coefficients and rounding remain included.

An additional independent automatic-series check differentiates the entire finite approximation and scaled analytic correction at the whole-time-band anchor. It encloses `Z_f'` near `3.516516369-2.308896261i`, with modulus below 4.206767086714, and `f_xx` near 10.93836378. This checks the signs and normalizer terms in the producer's closed derivative formula. It is a limited separate implementation check at the anchor, not the whole-X derivative bound and not full implementation independence. Its temporary diagnostic and elementary source hashes are recorded in the reviewer receipt; the retained producer and mathematical proof reproduce the actual theorem.

Read [the established results][results] and [patterns to avoid][avoid], especially the [collision-controls][controls] and [theta-bookkeeping][theta] clusters, [normalization][a08], [replay status][a04], [same-model review][a05] and [certifying the known][a11]. A higher-precision replay is a consistency check and does not supply independent specialist review. The complete result must be recorded with this limited scope in the progress register and round summary.

[note]: ../notes/11_PAID_ANCHOR_AND_BOUNDED_PHYSICAL_SEPARATION_20261019.md
[receipt]: ../numerics/UAR05_REVIEW_REPLAY_192_20261019.json
[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a04]: ../../../../../../avoid/04_counts_and_precision_as_evidence.md
[a05]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a08]: ../../../../../../avoid/08_normalization_and_constant_slips.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
