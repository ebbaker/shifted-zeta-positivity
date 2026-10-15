---
research_program: PR03
secondary_programs: [PR02-CORR, PR02]
status: certified_bounded_baseline
---

# Full stationary roots on three fixed theta curves

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. Internal ball-arithmetic certification using the existing analytic source and tail lemmas; not formal verification or external refereeing.

Six fresh complete-source calculations isolate genuine roots of both stationary observations at the predetermined values \(\theta\in\{1/2,3/4,1\}\). The stationary Laguerre form is strictly positive in every resulting root bracket. These calculations provide a reusable bounded baseline within the previously certified region \(0\le t\le1/2,\ |x|\le112\). They add no sign domain and do not validate the global Poisson sector split rejected in [Note 38](../05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md).

## 1. Frozen protocol and the full stationary conditions

Use the complete source, \(h_k=\partial_x^kH\), and

\[
 L(x)=\log(x/(4\pi)),\qquad t_\theta(x)=\theta/L(x),\qquad
 S_j=\{h_{j+1}=0\},\quad j=0,1.
\]

The protocol was fixed before these fresh quadratures: theta values \(1/2,3/4,1\); initial windows \([101,102]\) for \(S_0\) and \([103,104]\) for \(S_1\); six sign bisections; \(a=\pi/16\), source index cutoff 8, integration cutoff \(U=3/2\); 192-bit Arb/Acb arithmetic; spatial Taylor order 8 and temporal order 4; and the loss rule \(\kappa_0=\kappa_1=0\). All six cases are retained. No coefficient was fitted from an energy floor and no cases were selected after their outcomes were known.

The windows use known stationary-branch neighborhoods from earlier work, so this is not a statistically independent holdout of the old height certificate. The fixed-theta curve evaluations and root rectangles are fresh computations. A future arithmetic-mechanism validation should freeze its own decomposition and coefficient rule before selecting fresh validation cells.

Since \(H_t=-H_{xx}\),

\[
 \frac d{dx}h_{j+1}(t_\theta(x),x)
 =h_{j+2}+\frac{\theta}{xL(x)^2}h_{j+3}.                 \tag{1}
\]

Thus monotonicity for \(S_1\) needs \(h_4\). Opposite certified endpoint signs prove existence; a nonzero enclosure of (1) on the final containing rectangle proves uniqueness **in the final bracket**. At that root,

\[
 \mathcal L_j=-h_jh_{j+2}.                              \tag{2}
\]

Every occurrence of stationarity concerns the full source. The computational source cutoffs are paid quadrature devices, not replacements for the manuscript's hybrid staircase or definitions of retained stationarity.

## 2. Complete error payments

The [driver](../../numerics/certify_theta_stationary_baseline.py) uses the existing complete-index and integration-tail lemmas in [the contour checker](../../numerics/check_shifted_contour_payments.py). For each required order \(k\), let \(\epsilon_k^N,\epsilon_k^U\) denote those payments at \(t_{\max}=1/2\). A finite shifted integral \(I_k\) at a center \((t_c,x_c)\) gives

\[
 e^{\pi x_c/8}h_k(t_c,x_c)
 \in e^{(\pi/8-a)x_c}
 \left(I_k+[-\epsilon_k^N-\epsilon_k^U,
                  \epsilon_k^N+\epsilon_k^U]\right).       \tag{3}
\]

Validated quadrature radii are already contained in \(I_k\) and are also recorded separately. Both omitted source regions are paid independently. The complete source contour identity supplies (3); it is not assumed separately for each raw theta term.

Let \(M_k\) be the complete absolute contour moment majorants from [the transport helper](../../numerics/certify_phase_centered_residual.py). On \(|x-x_c|\le d_x\), \(|t-t_c|\le d_t\), a bound for the constantly normalized jet is
\(\widehat M_k=e^{(\pi/8-a)x_c+ad_x}M_k\). Taylor expansion with the heat equation uses the independently paid center jets through order 17. For each \(0\le k\le4\), the explicit payments are

\[
 R_{x,k}=\sum_{\ell=0}^{3}\frac{d_t^\ell}{\ell!}
              \frac{d_x^8}{8!}\widehat M_{k+2\ell+8},
 \qquad
 R_{t,k}=\frac{d_t^4}{4!}\widehat M_{k+8}.                 \tag{4}
\]

Moments through order 18 suffice. The complete closed rectangle lies in \(0<t<1/2\), and its time interval contains the entire fixed-theta curve above the bracket. Equations (3)–(4) account for center quadrature, both full-source tails, spatial transport, and temporal transport. No derivative of a retained stationary condition is substituted in (1).

## 3. Results and their normalization

Each final bracket has width \(1/64\). Times below are approximate centers, not enclosures. The last column is a conservative lower bound for the signed product in (2), multiplied by \(e^{\pi x_c/4}\); the unscaled form has the same strict sign. Exact dyadic endpoints, every error payment, and the derivative enclosures are in the [receipt](../../numerics/THETA_STATIONARY_BASELINE_20261015.json).

| Theta | Stationary set | Certified x bracket | Approximate time | Scaled Laguerre lower bound |
| --- | --- | --- | --- | --- |
| 1/2 | h1 = 0 | [3249/32, 6499/64] | 0.23930 | > 17532 |
| 1/2 | h2 = 0 | [3313/32, 6627/64] | 0.2371 | > 8914 |
| 3/4 | h1 = 0 | [3247/32, 6495/64] | 0.3591 | > 18207 |
| 3/4 | h2 = 0 | [3311/32, 6623/64] | 0.3557 | > 9226 |
| 1 | h1 = 0 | [6489/64, 3245/32] | 0.4789 | > 18843 |
| 1 | h2 = 0 | [6617/64, 3309/32] | 0.4745 | > 9524 |

The curve derivative is negative in the three \(h_1=0\) brackets and positive in the three \(h_2=0\) brackets. All endpoint signs and interval verdicts are strict. Endpoint jets use their own positive normalization \(e^{\pi x/8}\) only to test signs; rectangle jets use the constant normalization in (3). Neither normalization divides by the physical energy.

## 4. What this pilot does and does not test

This establishes a finite strict-sign baseline for the zero-loss rule at all six predeclared observations. It tests full stationary-root isolation on the correct theta curves, complete-source quadrature, and the signed product (2).

It does not evaluate the separately divergent axis and mixed global kernels of Note 38. Their integrability failure is an analytic rejection, not an undecided numerical enclosure. Nor does this baseline validate Note 38's finite-box signed mechanism: its component quadratures and a source-prescribed lower bound for their combined remainder have not been supplied. The finite-box formulas and source tail allowance are available for that next test.

A successful future localized test will still need an unbounded-domain proof and a domain covering predecessor neighborhoods on both stationary sets. Positive finite observations do not bound a relative loss through an unknown collision. The [coordination continuation](../00_research_coordination/41_POISSON_OBSTRUCTION_AND_REMAINDER_CONTINUATION_20261015.md) specifies the next admissible task.

Replay from the repository root, with Python and python-flint available:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/certify_theta_stationary_baseline.py --output /tmp/inv21-fixed-theta-baseline.json

The small receipt binds the driver and both imported helper sources by SHA-256. Those hashes establish implementation identity, not correctness of the imported analytic lemmas or formal verification of Arb/Acb. [Review 27](../../reviews/27_POISSON_OBSTRUCTION_AND_WEIGHTED_REMAINDER_REVIEW_20261015.md) records the internal audit.
