# E11 additional-agent review of the B06 short-window estimates

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The E11 dispatch explicitly
selected **gpt-6.1-sol / ultra**. Independent backend and usage metadata
are unavailable. The reviewer is distinct from the B06 proof and
decision author. This is a shared-source internal assessment, with no
independent specialist review. [Result index][results], [heat-flow
cluster11][r11], [avoid index][avoid], [shared premises05][a05].

**Disposition.** Accept [Note25][proof], equations (1)–(11), from the
named E09 localization input and within the fixed [E11 r1][request]
and [B06 r1][b06] scope. No mathematical correction requested. The
quantitative conclusion is the vanishing contribution of the specified
actual quartic packet, including its interaction with the complete
moment. The full short-center witness remains open. The [review
record][record] binds the 14,733-byte proof at SHA-256
`41bfd38537a3744b25598cd323624b18a8ecab613611b14eb2054182d1b90cb5`.

## 1. Fixed object and inherited localization

[Note15][green] uses \(L_X=\log(X/(4\pi))\), \(t_X=1/L_X\),
\(\tau_X=X/2+\pi/(8L_X)\) and the spatial phase \(v\log n/2\).
I checked the complete raw index range
\(\lfloor e^{L_X/32}\rfloor<n\le\lfloor e^{L_X/2}\rfloor\) and
the exact amplitude \(n^{-65/64}\exp((\log n)^2/(4L_X))\).
The strip has width \(d=5/64\), and the observation lies \(a=3/64\)
above its bottom. In the convention \(\widehat P(\omega)=
\int P(v)e^{i\omega v}\,dv\), the separated bounded harmonic extension of
the bottom datum \(e^{i\omega v}\) with zero top datum has height factor
\(\sinh((d-a)|\omega|)/\sinh(d|\omega|)\). Its zero-frequency solution
is linear in height and gives \(P\) mass \((d-a)/d=2/5\).
The explicit \(P\) is positive and even, including on \([-1,1]\).

At the fixed scale \(H=U^{1/32}\), the triangular probability measure has
density \(H^{-1}(1-|s|/H)_+\) and mass
\(2\int_0^1(1-u)\,du=1\). Its entire support gives
\(X=Y+s\in[U,2U]\), including the endpoint choices \(Y=U+H,2U-H\).
Thus \(A_U(Y)\) is exactly the squared norm of \(T_{Y+s}(v)\) in
\(\mathcal H=L^2(d\nu_H(s)P(v)\,dv)\). The spatial integral in each
\(Q(X)\) fixes \(t_X\), while the center integral follows the curve
\(t_X=1/L_X\). The target is \(A_U(Y)\ge5/66^2\) at some admissible
actual center along an unbounded sequence of \(U\). By positivity and
mass one this would force some \(Q(X)>4/66^2\) within that window, a
violation of the raw sufficient budget in Note15.

[E09 Note23, §2 and (1)][e09], accepted in [E10 Review09][e10], supplies
the pointwise Poisson norm estimate for the complement of the moving
middle band \(3/64<\log n/L_X\le5/16\). I checked its exact cutoff
interface, including the half-open high blocks. For the lower
population the weight is bounded by \(n^{-1-1/256}\), whose tail over
\(n>\lfloor e^{L_X/32}\rfloor\) has order at most \(X^{-1/8192}\).
For the higher population and \(|v|\le\log X\),
\(F=\tau_X+v/2\asymp X\). I rechecked the relevant selected passages
of Montgomery–Vaughan's chapter 16. Definitions 16.1–16.2 and
(16.55)–(16.58) apply to the exact model \(F\log u/(2\pi)\) on
any clipped block inside \([D,2D]\) at derivative parameter \(1\).
Theorems 16.23 and 16.25 give the A/B operations. The fixed word
\(AABABA\) on \((1/6,2/3)=AB(0,1)\) yields \((1/24,27/32)\).
The resulting primary and inverse-frequency bounds are
\(X^{1/24}D^{27/32-1/24}\) and \(O(D/X)\). Decreasing weights give Abel
cost \(w_D(X)\). The weighted primary exponent
\(1/24-41p/192+p^2/4\), with \(p=\log D/L_X\), has endpoint values
\(-1/1536,-1/384\) and is convex on the high band. The \(O(1+L_X)\)
block count is absorbed before reaching the weaker \(X^{-1/8192}\)
bound. Beyond \(|v|=\log X\) the absolute high sum costs at most
\(O(X^{7/128})\) and the squared Poisson norm costs
\(O(X^{7/64-64\pi/5})\). This verifies the consumed localization
interface, including its classical input and its entire Poisson
exterior. No other E09 estimates are needed in (1)–(11).
[Primary chapter 16 passages][mv], [B06 source-use record][sources].

Integrating the square of the uniform E09 estimate against the center
probability measure and taking its square root proves Note25 (1).
The two triangle inequalities in \(\mathcal H\) then transfer
square-root moments once the freezing norm is paid.

## 2. Moving floors and exact frozen form

For \(p=3/64,5/16\), the derivative of \(e^{pL_X}\) is
\(p e^{pL_X}/X=O(U^{p-1})\). Its excursion over \([Y-H,Y+H]\) is
\(O(HU^{p-1})\), with exponents \(-59/64,-21/32\). The real cutoff is
monotone and its excursion is eventually less than one. Each floor
can therefore change by at most one integer over the entire window.
There are at most two affected indices, including exact equality
with a cutoff. Each changed index satisfies \(\log n=pL_Y+O(1)\)
at its corresponding cutoff. Also \(L_X-L_Y=O(H/U)\). Substitution
in the exact weight yields
\[
 \log w_n(X)=(-65p/64+p^2/4)L_Y+O(1),
\]
and the resulting two weight exponents are \(-771/16384,-75/256\).
The same bound applies to \(w_n(Y)\) if the affected term occurs
only in the frozen sum. These estimates are uniform in the fractional
parts of the real cutoffs and in the admissible center.

On the common indices, the logarithmic weight derivative is
\(-(\log n)^2/(4XL_X^2)=O(U^{-1})\). Integrating the derivative and
using \(|e^z-1|\ll |z|\) for small real \(z\) gives relative
weight error \(O(H/U)\). In the phase, the exact residual after
subtracting \(s/2\) is \((\pi/8)(L_{Y+s}^{-1}-L_Y^{-1})\).
This is \(O(H/(U\log^2 U))\), which costs \(O(H/(U\log U))\)
after multiplication by \(\log n\). The spatial \(v/2\) phase is
identical on both sides. Since \(w_n(Y)\le n^{-15/16}\) on \(I_Y\)
and \(n\ll U^{5/16}\), the summed weights are \(O(U^{5/256})\).
Using \(|e^{i\theta}-1|\le|\theta|\) gives the common-term error
\(O(HU^{-1}U^{5/256})=O(U^{-243/256})\), uniformly for all real \(v\).
Adding the endpoints gives \(O(U^{-771/16384})\) in \(\mathcal H\),
and reverse triangle with (1) gives (3), with
\(\big|\sqrt{A_U(Y)}-\sqrt{F_U(Y)}\big|\ll U^{-1/8192}\).
The transfer consumes a fixed surplus in the square-root norm;
the crude full norm size \(U^{1/256}\) times the transfer error
would give the growing power \(U^{31/8192}\).

To check (4), write \(\Delta=\log(n/m)\). The probability density
\(H^{-1}\boldsymbol 1_{[-H/2,H/2]}\) has transform
\(\operatorname{sinc}(H\omega/2)\); its self-convolution has exactly
density \(H^{-1}(1-|s|/H)_+\). In the finite squared sum the
frequency of \(s\) is \(\Delta/2\), so its transform is
\(\operatorname{sinc}^2(H\Delta/4)\). The \(v\) frequency is
\(\Delta/2\), and the remaining factor is \(e^{i\tau_Y\Delta}\).
This expansion accounts for every ordered pair, with multiplier
\(2/5\) on the diagonal. The squared joint norm gives real
nonnegative total energy, and individual off-diagonal terms can
have either sign after pairing conjugates.

## 3. Cell counts, standalone norm and full perturbation

For cells of unit length in \(H\log n\), write \(q=|j-k|\). At
\(q\ge2\), \(H|\Delta|\ge q-1\), so the core multiplier has modulus
at most \((2/5)\min(1,16/(q-1)^2)\). At \(q=0,1\) the finite
kernel mass gives a uniform bound. These estimates yield a majorant
\(C(1+q)^{-2}\) with uniformly summable rows. For nonnegative cell
masses \(a_j\), the inequality \(2a_ja_k\le a_j^2+a_k^2\) yields
(5), including all nearby indices. The same argument uses the
restricted cell masses for any chosen subset of indices and also
bounds sums with arbitrary fixed coefficient arguments.

For \(D_j=e^{j/H}\), a cell occupies \([D_j,D_je^{1/H})\). The
number of integers is at most \(D_j(e^{1/H}-1)+1\). A nonempty
middle cell has \(D_j\ge e^{-1/H}e^{3L_Y/64}\), so
\(D_j/H\gg U^{1/64}\) uniformly and absorbs the \(+1\). Each
weight in the cell is at most \(D_j^{-15/16}\). It follows that
\(a_j\ll D_j^{1/16}/H\). Since occupied cells have
\(D_j\le e^{5L_Y/16}\), their individual squared masses are
\(O(H^{-2}U^{5/128})=O(U^{-3/128})\). For \(j_*\) the last
occupied cell, the geometric bound over all cells is
\[
 \sum_{j\le j_*}e^{j/(8H)}
 =\frac{e^{j_*/(8H)}}{1-e^{-1/(8H)}}\ll H U^{5/128}.
\]
With the factor \(H^{-2}\) this proves \(F_U(Y)\ll U^{1/128}\).
Using \(\sqrt{A_U(Y)}\ll U^{1/256}+U^{-1/8192}\) proves the same
upper allowance on \(A_U(Y)\). These allowances grow with \(U\).

A subset \(S\subset I_Y\) meeting at most \(r\ge1\) cells has frozen
squared norm \(O(r U^{-3/128})\). Every element of \(I_Y\) lies
strictly between the original real cutoff values for each
\(X\in[Y-H,Y+H]\), eventually and uniformly, by the fixed margins
\(1/32<3/64\) and \(5/16<1/2\) and \(L_X/L_Y\to1\).
Thus actual deletion of \(S\) from \(T_X\) has fixed membership
throughout the window, with common-term freezing cost
\(O(U^{-243/256})\) and actual joint norm \(O(\sqrt r\,U^{-3/256})\).
For \(V=T_{Y+s}\) and \(W=P_{S,Y+s}\) in \(\mathcal H\),
\[
 \|V\|^2-\|V-W\|^2=2\Re\langle V,W\rangle-\|W\|^2.
\]
Bounding the inner product by \(\|V\|\|W\|\) uses the full \(T\),
including the low and high populations omitted in \(M\).
The absolute difference is \(O(\sqrt r\,U^{-1/128}+rU^{-3/128})\).
The estimate guarantees vanishing full perturbation for
\(r=o(U^{1/64})\) and vanishing standalone energy for
\(r=o(U^{3/128})\). Both are sufficient ranges. The latter bound
also gives the necessary \(r\gg U^{3/128}\) if the standalone energy
is bounded below by a fixed positive constant.

## 4. Actual quartic packet and its complete effect

On the large-\(X\) branch \(\tau_X'\!=1/2-\pi/(8XL_X^2)\ge1/4\)
eventually, and \(\tau_X\to\infty\). Thus \(\tau_{Y_D}=24\pi D^4\)
defines a unique large real center for each sufficiently large
integer \(D\), and \(Y_D\sim48\pi D^4\). The choice \(U=2Y_D/3\)
puts \(Y_D=3U/2\) in the admissible interval since \(H=o(U)\).
Uniformly for the whole window,
\(L_X=4\log D+\log 12+o(1)\). For
\(0\le j\le J=\lfloor D^{1/5}/4\rfloor\) we have
\(\log(D+j)=\log D+O(D^{-4/5})\). The ratio
\(\log(D+j)/L_X\) tends uniformly to \(1/4\), strictly inside both
the middle and raw cutoff ranges, so integer endpoints create no
packet membership changes.

Integrating the exact geometric-series identity for \(1/(1+x)\)
with \(x=j/D\ge0\) shows that the remainder after \(x-x^2/2+x^3/3-x^4/4\)
is \(\int_0^x t^4/(1+t)\,dt\), between zero and \(x^5/5\).
Multiplication by \(24\pi D^4\) gives the integer polynomial in (9)
after division by \(2\pi\), with coefficients \(12,-6,4,-3\) on
\(D^3j,D^2j^2,Dj^3,j^4\), and remainder at most \(3\pi/640<1/32\).
At any center \(X\) in the window the additional phase relative to
\(n=D\) is
\[
 \big(\tau_X-\tau_Y+v/2\big)\log(1+j/D).
\]
Because \(\tau_X'\) is bounded and \(|v|\le1\), this is
\(O((H+1)J/D)=O(D^{-27/40})\). Eventually all relative arguments
are within \(1/16\) modulo \(2\pi\), uniformly on the entire support
of the triangular average and \(|v|\le1\).
The span \(H\log(1+J/D)=o(1)\) also places the packet in at most
two cells.

The exact \(L_X\) asymptotic yields
\((\log(D+j))^2/(4L_X)=\log D/16+O(1)\) uniformly over the window,
so the packet weights are comparable to \(D^{-61/64}\).
On \(|v|\le1\), real projection after rotation by the \(D\)-term
phase is at least \(\cos(1/16)\) times the weight sum. For every
\(v\) the triangle inequality gives that weight sum as upper bound.
The positive restricted \(P\)-mass and mass-one center measure
give the two-sided energy
\[
 \|P_{S_D,Y+s}\|^2\asymp
 (D^{1/5}D^{-61/64})^2=D^{-241/160}\asymp U^{-241/640}.
\]
In the full squared-norm difference the corresponding norm is
\(O(U^{-241/1280})\). Its product with the full background bound
\(O(U^{1/256})\) is \(O(U^{-59/320})\), which dominates the
standalone term. Thus (11) includes the entire cross term. It
leaves the energy of the complementary sum undetermined.

## 5. Scope, controls and supporting checks

Equations (1)–(11) give auxiliary-moment estimates and delimit the
specified sparse-packet and actual quartic mechanisms. The frozen
identity leaves every pair in the target. The positive packet energy
supplies no lower value of the full signed sum, whose cross terms
can cancel. The growing allowance supplies no lower value or
uniform cap at the witness threshold. [Classification01][a01],
[scope07][a07], [separate bounds12][a12].

I checked the canonical-premise screen in Note25 §5 against the
[control catalog][r12] and the scope in [Note15][green]. Euler-factor
and translation controls lack unchanged ordinary coefficients with
complete canonical two-arm identification. Weighted-square, finite-tail
and finite-prime controls fail the conjunction of complete coefficients
and full normalized reflection, including the finite-prime controls
that preserve selected Hecke relations. Reflected, smooth and
primitive-compatible controls lack exact normalized integer-square
arithmetic. Positive heat counter-kernels and threshold models do
not supply the completed xi source and its arithmetic arms. Atomic,
compact and finite-profile controls fail the full canonical source and
profile beyond their matched data. The RH-conditional normalized
endpoints lack ordinary Dirichlet arithmetic within their stated
conditional scope. Variable readouts fail the physical cosine/Newman
evolution. Relaxed measures need not represent an integer zero
divisor, and freely altered phases need not arise from the same
physical logarithmic phase. The norm and cell estimates apply wherever
their own hypotheses hold; this screen identifies the source
requirements in a separate canonical interpretation.
[Control premises02][a02].

The fixed short-center witness and the every-center \(4/66^2\)
budget remain open. The \(9/16\) curve-only Green consumer is
conditional. The accepted \(567/1000\) width keeps its original
curve and fixed-positive-time high-height domains and symbolic
onsets. Compact heights, near-zero heat time, global Newman bounds
and iteration retain their previous limitations.
[Note15][green], [E07 proof][width], [E08 Review07][widthreview].

The [exact review record][record] confirms all nine prior source
identities in Record21 and its bound proof and script hash. It also
checks the E09 proof against the E10 review record. A separate
rational derivation matches all 19 powers and the four Taylor
coefficients, with additional exact checks of both cell thresholds
and the normalization. These are provenance and finite arithmetic
checks. The arguments above provide the analytical assessment.
No new field evaluations, scan, imported theorem, numerical onset
or novelty assessment was used. [Imports16][a16].

[request]: ../research-progress/handoffs/GNP-BB-E11-r1.md
[b06]: ../research-progress/handoffs/GNP-BB-B06-r1.md
[proof]: ../notes/25_GNP_BB_B06_SHORT_WINDOW_AND_ACTUAL_PACKET_20261113.md
[record]: ../numerics/23_GNP_BB_E11_REVIEW_CHECKS_20261113.json
[green]: ../notes/15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[e09]: ../notes/23_GNP_BB_E09_LOCALIZATION_AND_RESONATOR_MEANS_20261113.md
[e10]: 09_GNP_BB_E09_ADDITIONAL_AGENT_REVIEW_20261113.md
[sources]: ../references/06_GNP_BB_B06_SOURCE_USE_20261113.md
[width]: ../notes/18_GNP_BB_E07_FIVE_PAIR_WIDTH_20261113.md
[widthreview]: 07_GNP_BB_E07_ADDITIONAL_AGENT_REVIEW_20261113.md
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
