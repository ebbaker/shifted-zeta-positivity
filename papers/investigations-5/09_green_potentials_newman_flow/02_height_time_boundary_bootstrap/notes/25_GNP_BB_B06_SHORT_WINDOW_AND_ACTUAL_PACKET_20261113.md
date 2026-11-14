# B06: paid short-window freezing and one actual-phase packet test

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. The current root model and reasoning
effort are unavailable in chat0003's recorded configurations; no model
change or additional-agent dispatch is asserted.

**Status: proved in-note from E09's accepted localization and the direct
estimates below; same-assistant assessment, not independent review.**
This returns the third alternative of [B06 r1][packet]: a precisely
quantified failure of one actual-phase lower mechanism. The fixed
short-center witness and the every-center raw budget remain open.

The contribution is an explicit mass obstruction for sparse frequency
packets, including their interaction with the complete tail, and a
genuine arithmetic alignment whose contribution is too small. Freezing
alone is not counted as the milestone. Read the [result index][results]
and [avoid index][avoid], especially [cluster11][r11], [controls12][r12],
[classification01][a01], [premises02][a02], [scope07][a07] and
[separate bounds12][a12]. No RH-equivalent criterion is being tested.

## 1. Fixed question and the norm in which errors are paid

Keep [Note15][green] and [E09 Note23][e09] unchanged. In particular

\[
L_X=\log(X/(4\pi)),\quad \tau_X=X/2+\pi/(8L_X),\quad
w_n(X)=n^{-65/64}\exp((\log n)^2/(4L_X)),
\]
\[
T_X(v)=\sum_{\lfloor e^{L_X/32}\rfloor<n\le\lfloor e^{L_X/2}\rfloor}
w_n(X)e^{i(\tau_X+v/2)\log n},\qquad Q(X)=\|T_X\|_P^2.
\]
The unchanged positive strip kernel has mass \(2/5\) and transform
\(\widehat P(\omega)=\sinh(|\omega|/32)/\sinh(5|\omega|/64)\),
continued at zero. It satisfies \(|\widehat P|\le2/5\).
Fix exactly
\[
H=U^{1/32},\quad \chi(s)=(1-|s|)_+,\quad
Y\in[U+H,2U-H],\quad d\nu_H(s)=H^{-1}\chi(s/H)\,ds.
\]
This last measure has mass one and support \([-H,H]\). Define
\[
A_U(Y)=\int Q(Y+s)\,d\nu_H(s).
\]
The requested witness is \(A_U(Y)\ge5/66^2\) at some actual centers
along an unbounded sequence of \(U\). We neither establish nor refute it.

All transfers use the joint Hilbert norm with measure
\(d\nu_H(s)P(v)\,dv\). Let \(M_X\) retain the middle indices
\[
I_X=\{n:\lfloor e^{3L_X/64}\rfloor<n\le\lfloor e^{5L_X/16}\rfloor\}.
\]
E09's pointwise localization implies, uniformly in \(U,Y\),
\[
\|T_{Y+s}-M_{Y+s}\|_{\nu_H\otimes P}\ll U^{-1/8192}.       \tag{1}
\]
This is a square-root moment payment. We do not multiply it by a
possibly growing moment envelope and call the resulting additive error
vanishing.

## 2. Uniform freezing, including every moving endpoint

Put
\[
G_Y(s,v)=\sum_{n\in I_Y}w_n(Y)
 e^{i(\tau_Y+(s+v)/2)\log n},\qquad F_U(Y)=\|G_Y\|^2.
\]
For each fixed \(p\in\{3/64,5/16\}\), the real cutoff
\(e^{pL_X}\) has derivative \(p e^{pL_X}/X\). Its total movement
over the window is \(O(U^{p-31/32})=o(1)\). Thus each of its
floors changes by at most one eventually. No floor is differentiated.
There are at most two indices in the symmetric difference of \(I_X,I_Y\).
At the lower and upper endpoints respectively their weights are
\[
O(U^{-771/16384}),\qquad O(U^{-75/256}).                       \tag{2}
\]
Indeed at \(\log n=pL_Y+O(1)\) the weight power is
\(-65p/64+p^2/4\); replacing \(L_Y\) by \(L_X\) changes the
logarithm of that weight by a bounded amount uniformly here.

For common indices,
\[
\partial_X\log w_n(X)=-\frac{(\log n)^2}{4XL_X^2}=O(U^{-1}),
\quad \tau_{Y+s}-\tau_Y-s/2
=\frac\pi8(L_{Y+s}^{-1}-L_Y^{-1})=O(H/(U\log^2 U)).
\]
The phase error after multiplication by \(\log n\) is
\(O(H/(U\log U))\). Since \(w_n(Y)\le n^{-15/16}\) on \(I_Y\),
\(\sum_{I_Y}w_n(Y)\ll U^{5/256}\). The sum of the common-index
weight and phase errors is consequently \(O(U^{-243/256})\),
uniformly for every real \(v\). Combining with (2) gives
\[
\|M_{Y+s}-G_Y\|_{\nu_H\otimes P}\ll U^{-771/16384},\qquad
|\sqrt{A_U(Y)}-\sqrt{F_U(Y)}|\ll U^{-1/8192}.                  \tag{3}
\]
All constants are independent of the cutoff fractions and of \(Y\).
For example a fixed surplus in \(\sqrt F\) above \(\sqrt5/66\)
transfers to the witness eventually; an equality-level cap does not
transfer without the error in (3).

The convolution identity for the triangular density, obtained by
convolving two normalized indicators of \([-H/2,H/2]\), gives exactly
\[
F_U(Y)=\sum_{n,m\in I_Y}w_n(Y)w_m(Y)e^{i\tau_Y\log(n/m)}
\widehat P(\log(n/m)/2)
\operatorname{sinc}^2(H\log(n/m)/4).                         \tag{4}
\]
Here \(\operatorname{sinc}(0)=1\). The factors of two follow from
the actual frequency \(1/2\). Every pair, including all unequal
nearby indices, remains present. The form is real and nonnegative
because it is the displayed joint squared norm, not because its
individual signed cross terms are nonnegative.

## 3. How much mass can a few coherent frequency packets carry?

Partition the middle indices by
\[
\mathcal C_j=\{n\in I_Y:j\le H\log n<j+1\},\qquad
a_j=\sum_{n\in\mathcal C_j}w_n(Y).
\]
This is a proof partition at the fixed window scale, not a search over
window powers or a change of weights. For \(n\in\mathcal C_j\),
\(m\in\mathcal C_k\), the absolute multiplier in (4) is at most
\(C(1+|j-k|)^{-2}\). For \(|j-k|\ge2\), use
\(H|\log(n/m)|\ge|j-k|-1\) and \(|\operatorname{sinc} z|\le
\min(1,|z|^{-1})\); boundedness covers the adjacent cells.
The summability of this row and \(2a_ja_k\le a_j^2+a_k^2\) give
\[
F_U(Y)\le C\sum_j a_j^2.                                    \tag{5}
\]
The same inequality holds for any selected subset of cells and any
subset of indices within them, retaining their actual phases. It is
also valid with arbitrary coefficient phases, a deliberately stronger
upper comparison; no artificial alignment is asserted.

Write \(D_j=e^{j/H}\). Since the smallest middle index divided by
\(H\) tends to infinity, each occupied cell has at most \(CD_j/H\)
integers. Consequently
\[
a_j\le C D_j^{1/16}/H,\qquad
\max_j a_j^2\ll H^{-2}U^{5/128}=U^{-3/128}.
\]
Summing the geometric series \(\sum_j e^{j/(8H)}\ll
H U^{5/128}\) also shows
\[
F_U(Y)\ll U^{1/128},\qquad A_U(Y)\ll U^{1/128}.              \tag{6}
\]
The second assertion uses (3) at the square-root level. The triangular
profile removes the logarithm from the older allowance, but (6) still
grows and does not stop the requested witness.

For a set \(S\subset I_Y\) meeting at most \(r\ge1\) cells, its
standalone frozen energy is at most
\[
F_S\ll rU^{-3/128}.                                         \tag{7}
\]
The indices \(I_Y\) are strictly inside the original full-tail cutoffs
throughout this short window, eventually: \(3/64>1/32\) and
\(5/16<1/2\). Define the actual packet
\(P_{S,X}(v)=\sum_{n\in S}w_n(X)e^{i(\tau_X+v/2)\log n}\).
There is no moving membership for this fixed selected set. The common
weight/phase estimate from §2 pays its freezing error by
\(O(U^{-243/256})\), hence its joint norm is
\(O(\sqrt r\,U^{-3/256})\).

Let \(A_U^{\setminus S}(Y)\) be the same actual average with this
packet removed from the complete \(T_X\). Expanding the two squared
norms, including their cross term, and using (6), gives
\[
|A_U(Y)-A_U^{\setminus S}(Y)|
\ll \sqrt r\,U^{-1/128}+rU^{-3/128}.                         \tag{8}
\]
Thus a fixed number of these frequency packets has a vanishing effect
on the full averaged moment, even after its interaction with all other
indices. The same holds for \(r=o(U^{1/64})\). A standalone packet
energy of fixed positive size would require \(r\gg U^{3/128}\)
under (7); this is a different threshold from the full perturbation
threshold in (8). Neither assertion bounds the untouched remainder
below the desired constant. These are scoped sparse-packet estimates.

## 4. Test one actual-height lower mechanism: quartic integer alignment

Choose an integer \(D\to\infty\), and choose the unique large real
\(Y=Y_D\) satisfying
\[
\tau_Y=24\pi D^4.
\]
Existence and uniqueness follow from continuity and \(\tau_Y'\ge1/4\)
eventually. Then \(Y\sim48\pi D^4\). Set \(U=2Y/3\), so the
actual center \(Y=3U/2\) belongs to the allowed interval eventually,
and keep the prescribed \(H=U^{1/32}\asymp D^{1/8}\).
Take exactly
\[
J=\lfloor D^{1/5}/4\rfloor,\qquad S_D=\{D,D+1,\ldots,D+J\}.
\]
This entire packet is in the middle band, since \(\log D/L_Y\to1/4\).

The first four terms of the Taylor expansion give
\[
24\pi D^4\log(1+j/D)
=2\pi\{12D^3j-6D^2j^2+4Dj^3-3j^4\}+R_j,
\quad |R_j|\le\frac{24\pi}{5}\frac{j^5}{D}
\le\frac{3\pi}{640}<\frac1{32}.                             \tag{9}
\]
The braces contain an integer. The remainder bound follows directly
by integrating the geometric-series remainder for \(1/(1+x)\),
for \(0\le j/D\le1\). This is a common physical phase at an
actual real center, not separately selected phases.

Across \(|X-Y|\le H\) and \(|v|\le1\), the additional relative
phase against the \(n=D\) term is at most
\[
C(H+1)J/D=O(D^{-27/40})=o(1).
\]
Thus eventually all the packet terms have relative arguments within
\(1/16\). They really add constructively throughout that part of the
joint integration domain. Their amplitudes, uniformly there, satisfy
\[
w_{D+j}(X)\asymp D^{-61/64},
\]
because \(L_X=4\log D+\log12+o(1)\). Projection onto the phase
of the first term gives a lower bound by
\(\cos(1/16)\sum_{S_D}w_n(X)\); the triangle inequality gives
the matching upper bound for all \(v\). Since
\(\int_{-1}^1P(v)\,dv>0\) and \(\nu_H\) has mass one, the
actual standalone packet energy has the two-sided order
\[
\|P_{S_D,X}\|_{\nu_H\otimes P}^2
\asymp D^{2/5-61/32}
=D^{-241/160}\asymp U^{-241/640}.                           \tag{10}
\]
There is an actual lower estimate, but it tends to zero. Moreover the
full background cannot make this packet supply a fixed incremental
surplus: (6) and the exact squared-norm difference give
\[
|A_U(Y_D)-A_U^{\setminus S_D}(Y_D)|
\ll U^{1/256}U^{-241/1280}+U^{-241/640}
\ll U^{-59/320}=o(1).                                       \tag{11}
\]
No lower bound on the whole moment is obtained by deleting the rest.
The rest can cancel a selected vector, and its own moment is unknown.
Equation (11) explicitly pays that interaction rather than silently
discarding it. The packet also lies in at most two cells of §3
eventually, since \(H\log(1+J/D)=o(1)\).

## 5. Decision, remaining input, and collision controls

**Stop this isolated quartic-packet lower mechanism.** It succeeds at
actual phase alignment but fails the fixed-mass payment in (10); its
complete effect is vanishing by (11). More generally, (8) limits the
specified sparse collections of frequency packets. No scan of packet
orders, heights, window scales, supports or exponent pairs was made.

**This stops the tested packet-supported lower mechanism. It does not
disprove the short-center witness.** To obtain that witness, a further
argument must control a sufficiently distributed portion of the actual
signed quadratic, together with its remaining background. Merely
aligning one small block or replacing the remaining signed terms by a
growing absolute allowance does not do so. No supported proof contract
for the fixed positive witness, or uniform upper bound below it, is
available from this mechanism.

The results are auxiliary-moment estimates and a scoped failure, not
a zero theorem. Applying the [control catalog][r12] to the canonical
interpretation gives the following premise failures, as in [Note20][b05].

| Control class | Premise absent from the canonical interpretation |
| --- | --- |
| Euler-factor and translated sources | Unmodified ordinary coefficients and full canonical two-arm identification |
| Weighted-square, finite-tail and finite-prime controls | Complete coefficients jointly with full normalized reflection |
| Reflected, smooth and positive-primitive sources | Exact normalized theta integer-square arithmetic |
| Positive heat counter-kernels and threshold models | Completed xi source and its canonical arithmetic arms |
| Atomic, compact and finite-profile controls | Full source, coefficients and profile beyond the matched observations |
| RH-conditional normalized endpoints | Ordinary Dirichlet arithmetic; the conditional premise stays conditional |
| Variable readouts | Physical cosine/Newman evolution |
| Relaxed zero measures or freely altered phases | Integer zero divisor, or the common physical logarithmic phase, respectively |

The Hilbert and cell estimates hold on any sums with their hypotheses;
they are not themselves collision discriminators. The quartic example
uses the unmodified arithmetic phases, but establishes only a small
packet's energy. A source-control collision is neither ruled out nor
constructed by it. The every-center \(4/66^2\) budget and B06's
\(5/66^2\) witness remain open. Conditional width \(9/16\) stays
curve-only and unpaid; accepted width \(567/1000\), its symbolic
onsets, and the compact/time-zero/global/iteration gaps are unchanged.

## 6. Evidence and next task

The only inherited analytic estimate is E09's uniform localization;
its [E10 review][e10] and classical-input scope are retained. The new
freezing, convolution, summable cell rows, Taylor remainder and mixed
norm bounds are derived above. [Source-use06][sources] records the
limited primary-source reinspection; no new large-value theorem,
numerical onset, specialist review or novelty claim is imported.
The small rational/provenance record checks powers and source identity,
not the validity of the analytic inequalities.

**Next: [E] GNP-BB-E11 — GPT-6.1 Sol / ultra**, a fixed analytical
assessment of (1)–(11), especially endpoint weights, norm rather than
additive transfer, the cell row, and the complete-background payment.
Its [request][e11] is ready. The present assessment is [same-assistant][review].

[packet]: ../research-progress/handoffs/GNP-BB-B06-r1.md
[green]: 15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[e09]: 23_GNP_BB_E09_LOCALIZATION_AND_RESONATOR_MEANS_20261113.md
[e10]: ../reviews/09_GNP_BB_E09_ADDITIONAL_AGENT_REVIEW_20261113.md
[b05]: 20_GNP_BB_B05_LOCAL_MOMENT_DECISION_20261113.md
[sources]: ../references/06_GNP_BB_B06_SOURCE_USE_20261113.md
[review]: ../reviews/10_GNP_BB_B06_SAME_ASSISTANT_ASSESSMENT_20261113.md
[e11]: ../research-progress/handoffs/GNP-BB-E11-r1.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
