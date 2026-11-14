# B05 upper estimates for the exact local Poisson moment

13 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance. Subagent dispatch
**gpt-6.1-sol / ultra**. Backend configuration beyond dispatch
is unavailable.

**Status.** Bounded analytical comparison. The uniform localization
and the center-average bound below follow from the stated inputs.
The remaining every-center moment is unpaid. No field scans,
new exponent-pair search or onset calculations were run.
Read the [B05 packet][packet], [continuation][cont], [result index][results]
and [avoid index][avoid], especially [cluster11][r11], [controls12][r12],
[classification01][a01], [premises02][a02], [scope07][a07],
[separate bounds12][a12] and [imports16][a16].

## 1. Pay both ends of the exact moving tail

Keep the exact definitions of [Note15][green]. Write
\(L=L_X=\log(X/(4\pi))\),
\(\tau_X=X/2+\pi/(8L)\), \(K=\lfloor e^{L/32}\rfloor\),
\(N=\lfloor e^{L/2}\rfloor\), and
\(w_n=n^{-65/64}e^{(\log n)^2/(4L)}\). Let
\[
 S_{A,B}(X,v)=\sum_{A<n\le B}w_n
                    e^{i(\tau_X+v/2)\log n},\qquad
 M_X=\int_{\mathbb R}P(v)|S_{K,N}(X,v)|^2\,dv.
\]
Here \(v\) is the physical spatial displacement. The strip
kernel is exactly Note15's \(P\), with mass \(2/5\) and
\(P(v)\ll e^{-\pi|v|/H}\) as \(|v|\to\infty\), \(H=5/64\).
Use \(\|\cdot\|_P=\|\cdot\|_{L^2(P(v)\,dv)}\).
Choose the integer boundaries
\[
 A_X=\lfloor e^{3L/64}\rfloor,\qquad B_X=\lfloor e^{5L/16}\rfloor.
\]
These are interior boundaries of the fixed tail and do not change
the time, kernel or coefficients. Write
\(M_X^{\mathrm{mid}}=\|S_{A_X,B_X}\|_P^2\).

For \(K<n\le A_X\),
\(w_n\le n^{-65/64+3/256}=n^{-1-1/256}\).
Summing the majorant from \(K+1\) gives the uniform absolute
estimate \(O(K^{-1/256})=O(X^{-1/8192})\) and hence the same
\(P\)-norm bound. For \(B_X<n\le N\) use clipped dyads beginning
at the real boundary \(e^{5L/16}\), open on the left and closed
on the right. This includes the correct integers at both cuts.
On \(|v|\le\log X\), \(T=\tau_X+v/2\) is real and
\(X/3\le T\le2X/3\) eventually. Use the existing classical pair
\[
 (k,l)=AABABA(1/6,2/3)=(1/24,27/32)
\]
in the right-to-left word convention of [Note14][pairs].
The individual process statements and exact log-sum theorem
are [Montgomery–Vaughan][mv], Definitions 16.1–16.2,
(16.55)–(16.58), and Theorems 16.23, 16.25. For
\(T\log u/(2\pi)\) the derivative parameter is 1, the scale is
\(T/(2\pi)\), and the relative derivative error is zero.
This is the previously checked [source-use passage][src].
The partial sum bound on each subinterval of \([D,2D]\) is
\(O(X^kD^{l-k}+D/X)\), with the secondary term retained.

For \(D\ge1\), \(n\) in the dyad, the logarithmic derivative of
the continuous weight has bounded product with \(n\):
\(-65/64+\log n/(2L)\). Abel summation costs \(O(w_D)\), where the
same continuous weight defines \(w_D\). With \(a=\log D/L\)
in \([5/16,1/2]\), the primary power of \(X/(4\pi)\) is
\[
 \frac1{24}-\frac{41}{192}a+\frac{a^2}{4}.
\]
This convex function has endpoint values \(-1/1536,-1/384\).
The secondary cost is \(O(X^{-1/2})\) per block since \(w_D\le1\).
Over \(O(1+L)\) blocks the high summands therefore cost
\(O((1+L)X^{-1/1536})\) in supremum norm on \(|v|\le\log X\).
Multiplying by \(\sqrt{2/5}\) suffices in the \(P\)-norm there.

For the exterior, \(w_n\le n^{-57/64}\) for all \(n\le N\), so
every subsum is bounded in modulus by \(O(X^{7/128})\) on the
whole real \(v\)-axis, including locations where \(T\) is small.
The squared exterior norm beyond \(|v|=\log X\) is
\(O(X^{7/64-\pi/H})\). Thus by the triangle inequality,
\[
 \left|\sqrt{M_X}-\sqrt{M_X^{\mathrm{mid}}}\right|
 \ll X^{-1/8192}+(1+L)X^{-1/1536}
                    +X^{7/128-\pi/(2H)}=o(1).                    \tag{1}
\]
This holds for every sufficiently large real \(X\), with constants
independent of cutoff fractions. Splitting first and applying
the norm inequality also bounds the effects of cross pairs
with the paid ends. An eventual upper bound on \(M_X^{\mathrm{mid}}\)
strictly below \(4/66^2\) suffices for Note15. The complete consumer
and the independent carrier floor still use Note15's other payments.
Equation (1) also preserves any strict lower surplus above that
constant along an unbounded sequence.

## 2. Two absolute uses of signed-sum tools and their limits

For fixed \(X\), the restricted signed quadratic form retains all
pairs \(A_X<m<n\le B_X\) with the exact multiplier
\(\widehat P(\log(n/m)/2)\) of Note15. A fixed-scale Gram bound
uniform in coefficients cannot bypass the small frequency gaps.
Indeed on \((D,2D]\) the entries of the unphased Gram matrix are
at least one positive constant, by continuity and positivity of
\(\widehat P\) on \([-\log(2)/2,\log(2)/2]\).
The all-ones vector has Rayleigh quotient \(\gg D\); the center
phase conjugates the Gram matrix by a diagonal unitary.
Thus a bound based exclusively on an operator norm times the
diagonal weight incurs at least a factor of order \(D\).
For the actual positive weights on that dyad, the resulting
scale is \(D^2 w_D^2\). With \(a=\log D/L\), its power of
\(X/(4\pi)\) is \(2(a^2/4-a/64)\), positive when \(a>1/16\).
This is a loss for coefficient-independent Gram bounds, not a
lower bound on the canonical signed value.

The proven finite-pair comparison through word length eight
also leaves a middle scale unpaid if one estimates blocks
separately in modulus. At \(a_*=1040/5847\) in the remaining band,
[Note14][pairs] gives the minimum
\(g(a_*)=406319/12161760\) of
\(g_{k,l}(a)=k/a+l-k-1+a/4\) among those pairs.
The best primary power they furnish for the weighted norm
estimate at that scale is
\[
 a_*(g(a_*)-1/64)=432583/136749636>0 .
\]
The secondary term and local variation have already been paid.
Taking convex combinations of this finite set does not lower a
pointwise minimum of its affine-in-pair powers. This only tests
the specified pair bounds applied separately, including their
use followed by a positive Poisson integral. It leaves joint
two-variable cancellation, other pairs and other amplitudes open.

One may instead use an average of the exact local moment.
For any interval \(I\subset[U,2U]\) of length \(1\le h\le U\),
the localized question has the bound
\[
 \frac1h\int_I M_X^{\mathrm{mid}}\,dX
 \ll U^{-21/512}+\frac{U^{5/128}\log U}{h}.                       \tag{2}
\]
To prove it put \(\alpha=15/16\).
On the retained support \(w_n\le n^{-\alpha}\) because
\(\log n\le5L_X/16\). For each \(n\), its cutoff membership
\(A_X<n\le B_X\) is an interval of centers, possibly empty,
since both cutoff functions are increasing. A pair's intersection
with \(I\) is also an interval. On this interval \(w_mw_n\) is
positive decreasing in \(X\). The phase derivative is
\[
 \tau_X'\log(n/m)=\left(\frac12-\frac{\pi}{8XL_X^2}\right)\log(n/m)
\]
and is monotone and at least \(\log(n/m)/4\) for large \(U\).
First-derivative integration by parts followed by Abel summation
gives \(O(m^{-\alpha}n^{-\alpha}/\log(n/m))\) for the
integral of an off-diagonal pair. The bounded Poisson multiplier
is independent of \(X\) and is still present. For \(n/2<m<n\),
use \(1/\log(n/m)\le n/(n-m)\), giving at most
\(O(n^{1-2\alpha}\log n)\) for the entire near-diagonal sum at
fixed \(n\). For \(m\le n/2\) the logarithm is at least \(\log 2\)
and the sum is \(O(n^{1-2\alpha})\). Sum through \(O(U^{5/16})\)
to get the stated off-diagonal power \(5/128\). The diagonal
is \(O(U^{(3/64)(1-2\alpha)})=O(U^{-21/512})\), since
every included integer is \(\gg U^{3/64}\).
This argument includes cutoff endpoints and every small gap.

The exact full tail has the same average tending to zero on
\(h\ge U^{5/128+\epsilon}\) for fixed \(\epsilon>0\), by (1)
and Minkowski. This supports a density statement there and gives
no every-center bound. At fixed \(h\) the displayed off-diagonal
allowance grows. The sibling [B10][b10], [audit][audit] and
[review][review] concern another set of weights and a growing
center window, with its Mellin mean error retained. The
\(U^{17/81+\rho}\) regime of that result cannot substitute for
the fixed local moment or the independent observation floor.

## 3. Signed Gaussian representation and cutoff expense

For each fixed \(X,v\) set \(s=65/64-i(\tau_X+v/2)\).
For any finite integer interval \(A<n\le B\), define its
ordinary polynomial \(D_{A,B}(s)=\sum_{A<n\le B}n^{-s}\).
Completing a real square gives the exact realization
\[
 S_{A,B}(X,v)=\sqrt{L/\pi}
       \int_{\mathbb R}e^{-Lr^2}D_{A,B}(s-r)\,dr .                \tag{3}
\]
All summands are finite. Replacing the shifted polynomial by an
ordinary infinite series is only justified in \(\Re(s-r)>1\)
unless a separate continuation and remainder estimate is proved.
For fixed \(0<r_0<1/64\), the integral on \(r\le r_0\) costs
\(O(A^{-(1/64-r_0)})\) by absolute summability.
On a dyad of scale \(e^{aL}\) the absolute-term integral ledger
has primary exponent \((r-1/64)a-r^2\). Its saddle is \(r=a/2\)
and the maximum is \(a^2/4-a/64\), positive for \(a>1/16\),
including the unpaid middle. For the full cutoff at \(a=1/2\)
this gives \(7/128\). Using an exponent pair at the shifted
real part and taking absolute values under (3) gives precisely
the weighted block primary power of §2 after square completion.
This realization therefore does not improve that separate-pair
estimate.

For analytic continuation, [DLMF 25.2.8][em] gives the exact
finite difference, for integers \(1\le A\le B\),
\[
 D_{A,B}(z)=\frac{B^{1-z}-A^{1-z}}{1-z}
              -z\int_A^B \{u\}\,u^{-z-1}\,du .                  \tag{4}
\]
The two zeta terms cancel on subtraction. The finite formula
extends to all complex \(z\) by removal at \(z=1\).
In (3) the continuous integral remainder in (4) contains
an oscillatory fractional-part factor at the exact frequency.
Its elementary absolute-value payment loses a factor
\(O(|\Im s|)\) inside the integral, so it supplies no replacement
for signed cancellation in the middle. A horizontal complex
translation \(r\mapsto r+a_0\) in (3) keeps the same saddle in
the original real \(r\)-coordinate. A vertical translation
\(r\mapsto r+i b_0\) multiplies the Gaussian modulus by
\(e^{Lb_0^2}\) and only changes the ordinary phase frequency.
For fixed translations these changes of contour of the
finite entire integrand are legal by Gaussian decay on the
closing sides. Absolute integration on the shifted line
again supplies no strict saving at the cited middle scale.
An application of a zeta continuation bound alone would
still need to pay the exact cutoff remainder or a joint
signed cancellation with it.

## 4. Decision and screen

The exact unpaid target after (1) is a uniform moment of the
signed middle band \(e^{3L_X/64}<n\le e^{5L_X/16}\) with the
same Poisson kernel and budget, with a strict margin to transfer
through (1). Bounds (1) and (2) acquire localization and an
average; they do not justify an E contract for every center.
The paid low and high norms can also be inherited in a separately
specified growing-resonator comparison. No estimate here says
the actual signed moment exceeds \(4/66^2\).

The [Note15 screen][green] and [collision controls][r12] apply.
Euler-factor and translated controls fail the unchanged arithmetic
and full theta provider. Weighted-square, finite-tail and finite-prime
controls fail complete coefficient identification with full reflection.
Reflected, smooth and positive-primitive controls fail theta square
arithmetic. Atomic, compact and finite-profile controls fail complete
source identification. RH-conditional normalized endpoint controls
fail the ordinary Dirichlet arithmetic. Variable readouts lack the
physical cosine/Newman equation, and relaxed measures lack an exact
integer zero configuration. Altered free phases fail the exact
logarithmic model. The Gaussian identity and positive Gram comparison
are general algebraic tools. Their conclusions about this optimizer
class do not separate collision sources on their own.

[packet]: ../research-progress/handoffs/GNP-BB-B05-r1.md
[cont]: 19_GNP_BB_CONTINUATION_AFTER_FIVE_PAIR_TRANSFER_20261113.md
[green]: 15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[pairs]: 14_GNP_BB_B04_BROADER_PAIR_COMPARISON_20261113.md
[src]: ../references/02_GNP_BB_SIGNED_TAIL_SOURCE_USE_20261113.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf
[em]: https://dlmf.nist.gov/25.2.E8
[b10]: ../../01_riemann_siegel_evolution/notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[audit]: ../../01_riemann_siegel_evolution/notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[review]: ../../01_riemann_siegel_evolution/reviews/16_GNP_RS_B10_PREINTEGRATION_ASSESSMENT_20261112.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
