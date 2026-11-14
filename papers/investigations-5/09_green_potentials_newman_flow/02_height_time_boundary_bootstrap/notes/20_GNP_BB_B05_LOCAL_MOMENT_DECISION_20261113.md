# B05 decision: isolate the middle band and test growing resonators

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The conceptual decision agent
was explicitly dispatched as **gpt-6-astra / ultra**; the upper-estimate
and resonance comparisons used **gpt-6.1-sol / ultra**. Independent
backend configuration and usage are unavailable. The parent owns the
[sole register][progress], frozen execution requests and chat capture.

**Decision.** The requested every-center moment has not been acquired
or disproved. The analytical pass does isolate a strictly shorter
middle band and supports a quantitative result about the actual moment
and a specified growing-resonator class. Select the fixed E09 synthesis
below; retain the pointwise middle-band estimate as unpaid. This is the
bounded return to [B05 r1][request], following [Note19][start], not a
new zero-exclusion theorem.

| Next task | Type and recommended model | Readiness | Required output |
| --- | --- | --- | --- |
| GNP-BB-E09 | E — GPT-6.1 Sol / ultra; fixed localization, product-frequency estimate and constants | Ready after the parent freezes r1 | Prove the stated actual-moment mean and the localized growing-resonator bound, or identify their exact failed payment |
| Additional-agent assessment of E09 | E — GPT-6.1 Sol / ultra; fixed analytical check | After the saved proof | Check actual moving endpoints, coefficient uniformity, pointwise localization, normalization and all scope qualifications |

Read the [result index][results] and [avoid index][avoid], specifically
[heat-flow cluster11][r11], [collision controls12][controls],
[classification01][a01], [premises02][a02], [scope07][a07],
[separate bounds12][a12] and [imports16][a16]. The prospective milestone
is an actual moment decay rate and an explicit estimating-class range,
not evidence for an RH-equivalent assertion. The original Green
identity and its conditional width are not counted again as progress.

## 1. The unchanged question and the attempted methods

Use exactly [Note15][green]. For \(X>4\pi\), set
\[
 L_X=\log(X/(4\pi)),\quad t_X=1/L_X,\quad
 \tau_X=X/2+\pi/(8L_X),\quad
 K_X=\lfloor e^{L_X/32}\rfloor,\quad N_X=\lfloor e^{L_X/2}\rfloor,
\]
\[
 w_n(X)=n^{-65/64}e^{(\log n)^2/(4L_X)},\quad
 T_X(v)=\sum_{K_X<n\le N_X}w_n(X)e^{i(\tau_X+v/2)\log n},
 \qquad Q(X)=\int_{\mathbb R}P(v)|T_X(v)|^2\,dv.
\]
Here \(P\) is the unchanged strip Poisson kernel with height \(5/64\),
observation distance \(3/64\) above its lower edge, mass \(2/5\), and
Fourier transform
\(\widehat P(\omega)=\sinh(|\omega|/32)/\sinh(5|\omega|/64)\),
continued at zero. The target remains \(Q(X)\le4/66^2\) for every
sufficiently large real \(X\). Time is fixed inside each spatial
integral. A later average over \(X\) follows this family; it is not
an integral for one common-time theta field.

The [upper-estimate comparison in Note21][upper] tested actual-phase block estimates,
fixed-scale spacing bounds and a Gaussian representation of the heat
weight. These did not acquire the required constant. In particular,
the absolute Gaussian wing ledger has exponent
\((r-1/64)/2-r^2\), whose maximum at \(r=1/4\) is \(7/128>0\).
Discarding those wings would remove a growing allowed contribution.
The termwise absolute quadratic allowance \(X^{7/64}\) and fixed-scale
spacing losses also remain upper allowances, not lower bounds on
\(Q(X)\). The precise tests and their domains are in Note21.
No wider exponent-pair search is selected.

The [resonance comparison][resonance] instead estimates the actual
moment under positive arithmetic weights. It pays the moving lower
cutoff rather than transferring the [HCB resonator][hcb] by analogy.
HCB's \(tL=2\) fixed small-mode surplus disappears below this
\(K_X\); surviving fixed-ratio coincidences are handled by the
integer product calculation below. The result limits the specified
weighted-average lower-witness method, not every resonance argument.

## 2. A concrete reduction of the unpaid population

Freeze
\[
 a=3/64,\quad b=5/16,\quad
 K_{a,X}=\lfloor e^{aL_X}\rfloor,\quad
 N_{b,X}=\lfloor e^{bL_X}\rfloor,
\]
and define the middle sum, with all its original weights and phases,
\[
 M_X(v)=\sum_{K_{a,X}<n\le N_{b,X}}
                  w_n(X)e^{i(\tau_X+v/2)\log n}.
\]
This changes neither \(T_X\) nor its desired bound: the removed
pieces must be paid. The selected fixed payment is
\[
       \|T_X-M_X\|_{L^2(P\,dv)}\le C X^{-1/8192}.                 \tag{1}
\]

For the low piece \(K_X<n\le K_{a,X}\),
\(w_n(X)\le n^{-1-1/256}\), so its absolute sum is
\(O(K_X^{-1/256})=O(X^{-1/8192})\), uniformly in \(v\).
For the high piece \(N_{b,X}<n\le N_X\), use only
\(AABABA(1/6,2/3)=(1/24,27/32)\), with words acting right to left.
On a block of scale \(s=\log M/L_X\), its primary weighted power is
\[
 E(s)=1/24-41s/192+s^2/4,
 \quad E(5/16)=-1/1536,\quad E(1/2)=-1/384.
\]
Convexity, arbitrary clipped intervals, Abel variation, the inverse
frequency term and the logarithmic block count give a power saving
uniformly for \(|v|\le\log X\), where the actual phase frequency
\(\tau_X+v/2\asymp X\). On the exterior, the same complete finite
population has absolute sum \(O(X^{7/128})\), and the exponential
Poisson tail pays the quadratic integral. The fixed imported
logarithmic-phase theorem is the Montgomery–Vaughan A/B result already
checked in the [source record][source]; no new short-interval zeta
theorem is assumed. E09 must retain all floor endpoints and both
pieces in (1).

Writing \(Q_M(X)=\|M_X\|_{L^2(P\,dv)}^2\), (1) yields
\[
 |\sqrt{Q(X)}-\sqrt{Q_M(X)}|\le C X^{-1/8192}.                  \tag{2}
\]
The remaining sufficient pointwise estimate is, for example,
\(\sqrt{Q_M(X)}\le1/33-CX^{-1/8192}\) at every large center.
A fixed strictly smaller cap would also suffice eventually. Conversely,
a fixed positive excess over the raw target along an unbounded sequence
could transfer a genuine counterexample to that raw bound. Neither is
proved here. An equality-level cap on \(Q_M\), without paying (2),
cannot simply be substituted for the original cap.

The acquired localized center-average comparison in Note21 is also
retained: for any interval \(I\subset[U,2U]\) of length \(1\le h\le U\),
\[
 \frac1h\int_I Q_M(X)\,dX
       \ll U^{-21/512}+U^{5/128}\log U/h.                        \tag{2a}
\]
Together with (1), this gives a vanishing full-tail average on
\(h\ge U^{5/128+\epsilon}\), for each fixed \(\epsilon>0\) with
nonempty interval range. At fixed \(h\), its off-diagonal allowance
grows. This concrete short-window limitation does not supply the
every-center Poisson cap. It is a statement about the present moment,
not a restatement or strengthening of B10's different observable.

## 3. The supported growing-resonator synthesis

For each dyadic interval \([U,2U]\), take
\[
 R\ge1,\quad \sum_{r\le R}|c_r|^2=1,\quad
 \mathcal B(X)=\left|\sum_{r\le R}c_r e^{i\tau_X\log r}\right|^2,
 \qquad D_R=\frac1U\int_U^{2U}\mathcal B(X)\,dX.
\]
The coefficients are arbitrary complex numbers, may depend on \(U\),
and are fixed as \(X\) runs through that interval. Support is restricted
to positive integers at most \(R\). The proposed constants are uniform
over every such coefficient vector. This uniformity includes vectors
chosen after inspecting the window; it excludes coefficients changed
with the integration variable \(X\).

The denominator has the elementary bound
\[
                         D_R=1+O(R\log(2R)/U).                  \tag{3}
\]
The [raw-tail calculation in Note22][resonance], using the weighted
log-separation improvement below, supports
\[
 \frac1U\int_U^{2U}\mathcal B(X)Q(X)\,dX
 \ll_\varepsilon U^{-25/1024}R^\varepsilon(1+\log R)
       +U^{-57/64}R^{1+\varepsilon}(1+\log R)\log(2UR).          \tag{4}
\]
For \(R=1\), no divisor loss is needed, and this gives
\[
 \frac1U\int_U^{2U}Q(X)\,dX\ll U^{-25/1024},\qquad
 \frac{\operatorname{meas}\{X\in[U,2U]:Q(X)>h\}}U
                    \ll_h U^{-25/1024}\quad(h>0).              \tag{5}
\]
These are quantitative statements about the actual local moment.
They permit exceptional spikes. They are not a new uniform width,
a zero-count estimate, or an all-height Green acquisition. No
almost-everywhere center statement is promoted to a statement about
zeros on the height-dependent heat curve.

For the middle sum, \(w_n\le n^{-15/16}\). Applying the same product
calculation with \(\alpha=15/16\), lower exponent \(a=3/64\) and
upper exponent \(b=5/16\) gives
\[
 \beta=a(2\alpha-1)=21/512,\qquad J\ll U^{5/16}R.
\]
Combining it with (1) by the triangle inequality in the joint weighted
\(L^2(dX\,P(v)dv)\) space gives the fixed E09 target
\[
 \boxed{\ \frac1U\int_U^{2U}\mathcal B(X)Q(X)\,dX
 \ll U^{-1/4096}D_R+
 C_\varepsilon\bigl[U^{-21/512}R^\varepsilon(1+\log R)
       +U^{-123/128}R^{1+\varepsilon}(1+\log R)\log(2UR)\bigr].\ }\tag{6}
\]
The first term pays the square of the removed-piece norm; it is not
dropped because the middle average is smaller. For each fixed
\(0<\delta<123/128\), choosing \(\varepsilon>0\) sufficiently small
and using \(R\le U^\delta\) makes the right side tend to zero,
uniformly in all the stated coefficients. Indeed
\[
                 1-b(2-2\alpha)=123/128.
\]
Also \(D_R\to1\) by (3). Thus the normalized positive weighted
average cannot supply a fixed positive lower witness by this criterion
in that support class. This improves the raw-tail class
\(\delta<57/64\) furnished by (4). Neither boundary is claimed
optimal, and no assertion is made at either equality endpoint.

The structural argument is explicit. Product coincidences in the
expanded weighted square satisfy \(nr=ms\). With
\(r=dh,s=dk,(h,k)=1\), they have \(n=kq,m=hq\), and their positive
envelope is bounded by
\[
 C K^{1-2\alpha}\frac{\gcd(r,s)}{\sqrt{rs}}.
\]
Weighted Schur rows with weights \(r^{-1/2}\) are at most
\(d(r)(1+\log R)\). The elementary bound
\(d(r)\ll_\varepsilon r^\varepsilon\) pays their operator norm.
For noncoincident products, exact integration by parts in the physical
\(\tau_X\) costs \(1/|\log(nr/(ms))|\). Let \(b_j\) be the
positive product-coefficient envelope at product \(j\le J\).
The elementary weighted log-separation bound is
\[
 \sum_{j\ne k}\frac{b_jb_k}{|\log(j/k)|}
                 \le3(1+\log J)\sum_j j b_j^2.                 \tag{7}
\]
To verify it, apply Schur to coefficients \(\sqrt j\,b_j\) and
weights \(j^{-1/2}\). The row is
\(\sum_{k\ne j}1/[k|\log(j/k)|]\). For \(k<j\), its summand
is at most \(1/k+1/(j-k)\); for \(k>j\), at most \(1/(k-j)\).
The sum is at most \(3(1+\log J)\). The same exact product
substitution gives
\[
 \sum_j j b_j^2\ll N^{2-2\alpha}
        \sum_{r,s}|c_rc_s|\gcd(r,s)
 \ll_\varepsilon N^{2-2\alpha}R^{1+\varepsilon}(1+\log R).
\]
Indeed the inner sum over \(q\le N/\max(h,k)\) costs
\(dN^{2-2\alpha}(\min(h,k)/\max(h,k))^{1-\alpha}\le
dN^{2-2\alpha}\). The earlier gcd Schur estimate applied to
\(\sqrt r\,c_r\) pays the last inequality. With
\(N\ll U^{5/16}\), \(N^{2-2\alpha}\ll U^{5/128}\), giving
the second term in (6) after division by \(U\).
This pays all near-equal products, assumes no fixed frequency gap,
and chooses no artificial phases. The coarser maximum-product bound
and its smaller support ranges remain valid in the input comparison;
the fixed execution uses (7).

All moving intervals must be retained. In the full tail, an integer
is active on \([4\pi n^2,4\pi n^{32})\). In the middle it is active
on \([4\pi n^{16/5},4\pi n^{64/3})\). Intersection with the dyadic
window and with another mode's interval remains one interval. Endpoint
terms and the derivative of \(w_n(X)\) are paid before summing.
The frequency derivative is
\(\tau_X'=1/2-\pi/(8XL_X^2)\asymp1\); it is the derivative along
this auxiliary family, not a spatial derivative of \(H_{t_X}\) with
its time frozen. No cutoff is differentiated.

## 4. Fixed completion test and precise limits

E09 should prove (1), (2a), (3), (5) and (6), with constants and onsets uniform
in their declared parameters, preserving the raw-tail proof (4) and
its own scope. A finite exact check may verify the one A/B word and
the displayed rational powers; the analytical proof supplies the
theorem. A suitable decay exponent for each strict \(\delta\) may
be recorded, but numerical evaluation of onsets is not required.
Retain the distinction between the stronger unweighted mean rate in
(5) and the slower error term used to enlarge the resonator class in
(6). A completed proof and separate internal assessment are needed
before integrating the synthesis as an accepted result.

Stop the execution at a precise failed inequality if this supported
assembly breaks. Changing the tail, clock, kernel, coefficient class,
window quantifier or arithmetic input requires a new B decision.
No numerical field scan, expanded pair search, changed contour, new
zero target or manuscript is included.

The scoped negative consequence concerns **a constant lower witness
obtained by a positive whole-dyadic weighted average**, with the displayed
integer support bound and fixed coefficients. Longer or differently
organized sparse support, shorter/adaptively centered windows, coefficients
varying with \(X\), other weights and other large-value mechanisms are
outside it. It is not failure of the actual \(4/66^2\) cap. Even actual
failure of that cap would stop only the chosen sufficient raw-moment
budget, not automatically Note15's normalized Green consumer.

Note15's independent carrier floor, observation floor \(15/16\),
Green signal \(\log(13/5)\) and complete remaining edge/provider
payments are retained in place. Its conditional width \(9/16\)
remains conditional and curve-only. E07's accepted common-time width
\(567/1000\), with its symbolic onset, is unchanged. The initial-height,
near-zero-time barrier and iteration obligations remain separate;
[Note16's][global] cutoff-only comparison against \(1/5\) retains
its **width-4/7** scope. No new global width or Newman bound follows.

## 5. Evidence, controls and ownership

The two input comparisons are internal analytical work by Sol6.1/ultra;
this Astra/ultra design checks their compatibility and exact powers.
It is not independent specialist assessment or a new validation of
the complete HDA provider. The resonator product estimate and divisor
bound are derived directly. The fixed A/B import retains its existing
primary-source verification; HCB is a scoped precedent, not an imported
theorem for this moving tail. No literature priority is asserted.

The moment bounds apply to arithmetic sums satisfying their stated
coefficient and phase premises; they need not distinguish every
collision control. They make no collision claim. For the full theta
interpretation, the [control screen][controls] retains these failures:

| Control class | Failed premise of the canonical interpretation |
| --- | --- |
| Euler-factor and translated sources | Unmodified ordinary coefficients and full canonical two-arm identification |
| Weighted-square, finite-tail and finite-prime controls | Complete coefficients jointly with full normalized reflection |
| Reflected, smooth and primitive-compatible sources | Exact normalized theta integer-square arithmetic |
| Positive counter-kernels and threshold models | The completed xi field and its canonical arithmetic arms |
| Atomic, finite-profile and compact continuous controls | Full source, coefficients and profile beyond matched observations |
| RH-conditional normalized endpoints | Ordinary Dirichlet arithmetic; their conditional premise remains conditional |
| Variable readouts | Actual cosine/Newman evolution |
| Relaxed measures or freely altered phases | Exact integer zero divisor or common physical logarithmic phase, respectively |

A small average can coexist with a control collision or a localized
defect. A zero in a Green target with all the strict consumer hypotheses
would contradict its paid Green margin; a disjoint box may pass.
The new average is not substituted for that every-center premise.

**Next: [E] GNP-BB-E09 — GPT-6.1 Sol / ultra**, after the parent records
the frozen synthesis request. Prove and assess the stated localization
and moment bounds; leave the pointwise middle-band acquisition open.

[progress]: ../research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md
[request]: ../research-progress/handoffs/GNP-BB-B05-r1.md
[start]: 19_GNP_BB_CONTINUATION_AFTER_FIVE_PAIR_TRANSFER_20261113.md
[green]: 15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[upper]: 21_GNP_BB_B05_LOCAL_MOMENT_UPPER_ESTIMATES_20261113.md
[resonance]: 22_GNP_BB_B05_MOVING_TAIL_RESONATOR_TEST_20261113.md
[global]: 16_GNP_BB_B04_GLOBAL_CONSUMER_AUDIT_20261113.md
[source]: ../references/03_GNP_BB_B04_SOURCE_USE_20261113.md
[hcb]: ../../../03_heat_flow_collision_bounds/notes/14_SIGNED_LAG_RESONATOR_AND_ACTUAL_REMAINDER_20261028.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
