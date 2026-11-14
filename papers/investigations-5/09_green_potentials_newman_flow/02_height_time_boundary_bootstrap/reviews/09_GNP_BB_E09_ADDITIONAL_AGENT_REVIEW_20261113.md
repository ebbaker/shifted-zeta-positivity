# E10 additional-agent review of the E09 Poisson moment proof

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Review dispatch explicitly selected
**gpt-6.1-sol / ultra**. Independent backend and usage metadata are
unavailable. The reviewer is distinct from the E09 proof and B05 comparison
authors. This is an internal review with the same selected model and shared
mathematical inputs. The inherited proofs retain their original assessment
levels. [Result index][results], [avoid index][avoid], [same-model scope][a05].

**Disposition.** Accept [Note23][proof] under the named classical logarithmic-phase
input and within [E09 r1][packet]. No mathematical correction requested.
The reviewed proof is 21,215 bytes, SHA-256
`e3a10effbb7892c8e58f2f5cbc561ad00b6c9f0ea18fd606dc3dff353f1ce1e2`. The
[review record][checks] binds that version, its proof-side record, and the
frozen inputs. All 17 original E01 manifest entries and the E07 request
and proof identities matched. The single fixed rational replay covers
the exponents below. Byte identity and rational checks address provenance
and finite arithmetic. The inequalities were reviewed separately.

## 1. Fixed population and uniform complement

The kernel matches [Note15][green]. Its strip height is \(5/64\) and the
observation lies \(3/64\) above the bottom, so the mass is \(1-3/5=2/5\)
and the tail rate is \(64\pi/5\). In the integral defining \(Q(X)\) the
time is \(1/L_X\) and remains fixed. In the auxiliary integrals over \(X\)
it follows \(1/L_X\). The frozen finite weights, the \(v/2\) spatial phase,
the \(\pi/(8L_X)\) correction, and all four floor cutoffs agree with the
request.

- The low part is bounded by \(\sum_{n>K_X} n^{-1-1/256}\ll
  X^{-1/8192}\) uniformly in \(v\). The exponent uses \(\log n\le3L_X/64\).
- On \(|v|\le\log X\) the frequency is exactly \(F=\tau_X+v/2\) and
  \(F\in[X/3,2X/3]\) eventually. I reopened Montgomery–Vaughan,
  Definitions 16.1–16.2 and (16.55)–(16.58), and Theorems 16.23 and
  16.25. They apply on arbitrary subintervals of \([D,2D]\) at real
  \(D>0\) for the exactly matching logarithmic phase with derivative
  parameter \(1\) and scale \(F/(2\pi)\). Passing from a clipped half-open
  interval to its included integers preserves the estimate, including
  singletons. The selected word \(AABABA\), acting from the right on
  \((1/6,2/3)\), yields \((1/24,27/32)\).
  [Primary chapter16 passages][mv], [source-use02][src02], [source-use05][src05].
- The real high blocks start at \(e^{5L_X/16}\) and stop at \(e^{L_X/2}\),
  and their half-open endpoints count the exact integers once. The
  decreasing continuous weight gives the Abel cost \(w_D(X)\), since its
  terminal value plus total variation equals its initial value. The
  primary exponent is \(1/24-41s/192+s^2/4\). Its endpoints
  \(-1/1536,-1/384\) bound the whole interval by convexity. The
  \(D/F\) term costs \(O(X^{-1/2})\) per block. The \(O(1+L_X)\)
  block count leaves an interior norm within \(O(X^{-1/8192})\).
- The bound \(\sum_{n\le N_X}w_n(X)\ll X^{7/128}\) applies over the
  entire real \(v\)-axis. The squared exterior norm beyond \(\log X\)
  costs \(O(X^{7/64-64\pi/5})\). Its square root fits the same
  complement bound even with \(\pi>3\). The low and high norms together
  give (1), uniformly at real centers including every floor change.

## 2. Center integral and product coincidences

For a lower exponent \(\sigma\) and upper exponent \(\rho\), an integer
enters at \(4\pi n^{1/\rho}\) and exits at \(4\pi n^{1/\sigma}\), with a
closed entry and open exit. These equalities recover the stated raw and
middle membership intervals and keep each two-mode intersection a
single interval. On it \(w_n\le n^{-\alpha}\) for
\(\alpha=65/64-\rho/4\). The derivative of the exact physical clock is
\(\tau_X'=1/2-\pi/(8XL_X^2)\ge1/4\) eventually and \(\tau_X''>0\).
Each weight is nonincreasing in \(X\), so \(g=w_nw_m/\tau_X'\) is
positive and nonincreasing. The two endpoint terms plus the total
variation of \(g\) give \(2g(p)\) at the left endpoint \(p\). This pays
the uniform bound \(8(nm)^{-\alpha}/|\log(nr/(ms))|\). The coincident
term uses the full allowed length \(h\); empty and singleton intersections
have zero integral. The remaining spatial factor has unit modulus, so
the same bounds integrate over the full Poisson measure.

The symmetric matrix \(1/(\sqrt{jk}|\log(j/k)|)\) on distinct product
indices uses weights \(j^{-1/2}\). The row divides by
\(k|\log(j/k)|\). The \(k<j\) and \(k>j\) sums are bounded by
\(H_{j-1}+H_{j-1}\) and \(H_{J-j}\), respectively, where
\(H_m=\sum_{q=1}^m 1/q\). This gives the stipulated constant
\(3(1+\log J)\) against \(\sum_j j b_j^2\) and covers arbitrarily small
logarithmic gaps. The same inequality applied to the resonator alone,
where the diagonal is exactly \(\sum|c_r|^2=1\), gives
\(D_R=1+O(R\log(2R)/U)\).

In both coincidence forms, \(r=dh_0,\ s=dk_0\) with
\((h_0,k_0)=1\) gives \(n=k_0q,\ m=h_0q\) and \(j=dh_0k_0q\).
The restrictions are exactly \(K/\min(h_0,k_0)<q\le
N/\max(h_0,k_0)\) for the envelopes. In the unweighted form the lower
cutoff and the \(q^{-2\alpha}\) tail give
\(K^{1-2\alpha}\gcd(r,s)/\sqrt{rs}\) up to a constant, including
\(K/\min(h_0,k_0)<1\) by convergence. In the \(j\)-weighted form the
upper cutoff and \(q^{1-2\alpha}\) give an entry bounded by
\(O_\alpha(N^{2-2\alpha}\gcd(r,s))\). The power is integrable at the
lower end because \(\alpha<1\). This derivation includes both
coincidence matrices with their respective cutoffs.

For \(G_{rs}=\gcd(r,s)/\sqrt{rs}\) the \(r^{-1/2}\) row uses
\(\sum_{s\le R}\gcd(r,s)/s\le d(r)(1+\log R)\) by summing the
divisors of \(r\). The prime-power proof of \(d(r)\ll_\varepsilon
r^\varepsilon\) gives a finite constant for each fixed
\(\varepsilon>0\). The weighted form adds at most \(R\) by
\(\sqrt{rs}\le R\). Both bounds are uniform over the normalized
complex vectors, including vectors chosen for individual dyadic
windows.

## 3. Rates, normalization and scope

At \(R=1\) the two forms reduce to single sums and the middle-band
powers are \(U^{-21/512}\) and \(U^{5/128}\) before the
\(h^{-1}\log U\) factor. This proves (10) for every interval in
\([U,2U]\) of length \(1\le h\le U\), uniformly in its position.
The squared complement adds \(O(U^{-1/4096})\) in (11).
This is vanishing, for example, uniformly on
\(U^{5/128+\eta}\le h\le U\) at each fixed
\(0<\eta\le123/128\). The raw unlocalized calculation has powers
\(U^{-25/1024}\) and \(U^{-57/64}\) in the dyadic bound, prior
to resonator support factors and logarithms. At \(R=1\),
\(U^{-57/64}\log(2U)\) is absorbed by \(U^{-25/1024}\).
The resulting rate in (13) controls the fixed-threshold exceptional
proportion for \(Q\) by Markov's inequality.

The weighted transfer uses the joint measure \(U^{-1}B(X)dX\,P(v)dv\).
The complement has norm \(O(U^{-1/8192}D_R^{1/2})\).
Triangle and squaring account for the cross terms and produce the
\(U^{-1/4096}D_R\) term in (14), in addition to the
\(U^{-21/512}R^\varepsilon(1+\log R)\) and
\(U^{-123/128}R^{1+\varepsilon}(1+\log R)\log(2UR)\) terms.
For each fixed \(0<\delta<123/128\), the proof takes
\(m_\delta=\min(21/512,123/128-\delta)>0\) and
\(\varepsilon=m_\delta/(2\delta)\). Both exponents are then at most
\(-m_\delta/2\) before logarithms, which fit \(U^{m_\delta/4}\) with
a \(\delta\)-dependent constant. The denominator converges to one
uniformly for \(1\le R\le U^\delta\) and is eventually bounded away
from zero. The normalized (15) follows with a finite onset that
may depend on \(\delta\). The raw open range \(\delta<57/64\) uses
the same argument with the raw exponents. Neither endpoint is included.

The excluded witness is a uniform positive lower bound obtained
from normalized positive whole-dyadic averages with the stated
integer support and coefficients fixed over each window. Actual
pointwise large values, shorter or adaptively centered windows,
other weights, and wider supports remain open. In particular the
every-center raw sufficient budget \(4/66^2\) required by [Note15][green]
remains unpaid. The exceptional set in (13) is a set of moment
values. The \(9/16\) curve consumer stays conditional, and the accepted
\(567/1000\) width retains [E07's][prior] domain and symbolic onset.
Interior heights, near-zero time, global bounds and iteration remain
separate. [Classification01][a01], [scope07][a07], [separate bounds12][a12].

The canonical screen in Note23 correctly ties Euler-factor and translated
controls to changed ordinary coefficients or missing full two-arm
identification. Weighted-square, finite-tail and finite-prime controls
fail the complete coefficient and normalized-reflection conjunction.
Reflected, smooth and primitive-compatible controls lack exact normalized
theta square arithmetic. Positive heat counter-kernels and atomic,
finite-profile and compact controls lack the full canonical source,
arithmetic arms or profile beyond matched observations. RH-conditional
normalized perturbations fail ordinary Dirichlet arithmetic. Variable
readouts fail the physical cosine/Newman evolution, and relaxed zero
measures and free phases fail the integer zero divisor and exact physical
phase, respectively. The arithmetic mean estimate applies to sums on
any such model that satisfy its own frequency and amplitude hypotheses.
A small mean permits a localized defect, whereas the Green application
requires a strict margin in each box under its separate hypotheses.
[Collision controls12][controls], [premises02][a02], [imports16][a16].

[proof]: ../notes/23_GNP_BB_E09_LOCALIZATION_AND_RESONATOR_MEANS_20261113.md
[packet]: ../research-progress/handoffs/GNP-BB-E09-r1.md
[green]: ../notes/15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[prior]: ../notes/18_GNP_BB_E07_FIVE_PAIR_WIDTH_20261113.md
[checks]: ../numerics/19_GNP_BB_E09_REVIEW_CHECKS_20261113.json
[src02]: ../references/02_GNP_BB_SIGNED_TAIL_SOURCE_USE_20261113.md
[src05]: ../references/05_GNP_BB_B05_SOURCE_USE_20261113.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
