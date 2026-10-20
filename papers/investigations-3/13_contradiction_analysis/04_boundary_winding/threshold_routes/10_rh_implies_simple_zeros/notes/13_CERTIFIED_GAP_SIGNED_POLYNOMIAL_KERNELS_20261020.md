# Certified-gap signed polynomial kernels: exact comparison and prime cost

20 October 2026. Prepared for Edward Baker with LLM assistance by **gpt-6-astra, ultra**. Same-model derivation; no specialist-review or novelty claim.

**Result.** For an even polynomial times a nonnegative bandlimited carrier, a sign-changing region confined to an independently certified zero-free gap has a globally nonnegative companion of the same bandwidth and degree whose complete zero sum is no larger. For the explicit quartic-times-sixth-sinc family, the signed member also has a larger leading absolute prime payment, uniformly in its two gap parameters. This is a scoped comparison: it does not prove arithmetic-estimation dominance for all sign-changing kernels, transfer gamma/pole budgets, or give an unrestricted signed-kernel barrier.

The [result index](../../../../../../../result-summaries/README.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply, especially [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [quantitative gain](../../../../../../../avoid/20_volume_without_a_gain.md).

[Internal review](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) · [Finite evaluation comparison](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md).

## 1. The gap is an input, and all other zeros remain

Assume RH, fix a zero ordinate `gamma` of arbitrary multiplicity `m`, and suppose an independent certificate establishes

\[
|\lambda-\gamma|\ge g>0
\quad\text{for every distinct noncentral zero ordinate }\lambda.
\tag{S1}
\]

Equality is allowed. Let `K` be entire, nonnegative on the real axis, with `K(0)=1` and compact Fourier support. Let `P` be a real polynomial with `P(0)=1` and `P(t)>=0` for `t>=g^2`. Suppose `h(x)=P(x^2)K(x)` has the quadratic strip decay required for the explicit formula. It may change sign within the unused gap. Its complete zero sum is nevertheless a valid majorant:

\[
m\le\mathscr S_h(\gamma)
=m+\sum_{\lambda\ne\gamma}m_\lambda h(\lambda-\gamma).
\tag{S2}
\]

The sum is absolutely convergent by the usual all-multiplicity zero count. The certified gap supplies the sign assertion; it is not inferred from RH or from the event under investigation.

## 2. Same-bandwidth nonnegative replacement

Every positive root of `P` above `g^2` has even multiplicity. List the roots of odd multiplicity in `(0,g^2]` in increasing pairs `a_j<b_j`. There are an even number: `P(0)>0` and the eventual sign is positive. Factoring off one copy of each such root gives

\[
P(t)=R(t)\prod_j(1-t/a_j)(1-t/b_j),\qquad R(t)\ge0\ (t\ge0).
\]

The assertion about `R` follows by factoring the remaining roots into even positive factors, negative-root factors, and conjugate pairs, all nonnegative for real `t>=0`. Set

\[
P_+(t)=R(t)\prod_j(1-t/b_j)^2.
\tag{S3}
\]

Then `P_+(0)=1`, `deg P_+=deg P`, and `P_+(t)>=0` for all `t>=0`. For `t>=g^2`,

\[
(1-t/a)(1-t/b)-(1-t/b)^2
=t(1/a-1/b)(t/b-1)\ge0.
\tag{S4}
\]

All factors on that region are nonnegative, so `P_+(t)<=P(t)`. Thus `h_+(x)=P_+(x^2)K(x)` is globally nonnegative, has the same central normalization, degree and Fourier support, and satisfies

\[
\boxed{m\le\mathscr S_{h_+}(\gamma)\le\mathscr S_h(\gamma).}
\tag{S5}
\]

Polynomial multiplication differentiates the carrier's Fourier transform without enlarging its support. Equal degree also preserves the stated strip decay; at infinity the quotient of the two polynomial factors is bounded, and the compact part is harmless. Every exterior zero and every multiplicity is retained in (S5).

This is exact zero-consumer dominance. It does **not** compare the difficulty of acquiring or estimating the two different arithmetic sums. Nor does it transfer the signed kernel's gamma/pole budget to its companion. In particular, Note11 is not automatically a theorem about the signed kernel.

## 3. A fully explicit quartic family

For `delta>0` and `0<c<=g`, let

\[
K_\delta(x)=\left(\frac{\sin(\pi\delta x)}{\pi\delta x}\right)^6,
\qquad
h_{c,g}(x)=\left(1-\frac{x^2}{c^2}\right)
           \left(1-\frac{x^2}{g^2}\right)K_\delta(x).
\tag{S6}
\]

For `c<g`, the negative regions are exactly `c<|x|<g`, apart from carrier zeros. The bandwidth is `Delta=3delta`; quadratic strip decay holds. The companion in (S3) is `h_{g,g}`. More explicitly,

\[
h_{c,g}(x)-h_{g,g}(x)
=(c^{-2}-g^{-2})x^2(x^2/g^2-1)K_\delta(x),
\tag{S7}
\]

which is nonnegative at every noncentral zero covered by (S1).

Fourier convolution of six unit intervals gives the moments

\[
\int K_\delta=\frac{11}{20\delta},\qquad
\int x^2K_\delta=\frac1{4\pi^2\delta^3},\qquad
\int x^4K_\delta=\frac3{8\pi^4\delta^5}.
\]

Consequently the signed mass is exactly

\[
\boxed{I_{c,g}=\frac{11}{20\delta}
-\frac{c^{-2}+g^{-2}}{4\pi^2\delta^3}
+\frac3{8\pi^4c^2g^2\delta^5}.}
\tag{S8}
\]

The sign-changing member decreases this mass relative to its companion if and only if

\[
\delta g>\frac{\sqrt{3/2}}\pi,
\quad\text{since}\quad
I_{c,g}-I_{g,g}
=\frac{c^{-2}-g^{-2}}{4\pi^2\delta^3}
 \left(\frac3{2\pi^2\delta^2g^2}-1\right).
\tag{S9}
\]

Here the strict equivalence assumes `c<g`. In the opposite range, writing `t=pi^2 delta^2 g^2<=3/2` gives

\[
I_{c,g}\ge I_{g,g}
=\delta^{-1}\left(\frac{11}{20}-\frac1{2t}+\frac3{8t^2}\right)
\ge\frac{23}{60\delta}=\frac{23}{20\Delta}.
\tag{S10}
\]

Thus reducing the signed mass requires actual gap resolution, not merely placing a negative lobe inside an arbitrarily small certified interval.

## 4. Complete absolute prime payment, uniformly in c and g

Use the Fourier convention `phi(v)=int h(x)e^(-2pi ivx)dx` and define the full payment

\[
C_{c,g}(\delta)=\frac1\pi\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}|\phi_{c,g}(\log n/(2\pi))|.
\tag{S11}
\]

Every prime power is included. As `delta->infinity`, uniformly for all `0<c<=g` (which may vary with `delta`),

\[
\boxed{C_{c,g}(\delta)
=(1+o(1))\frac{2e^{3\pi\delta}}{\pi^6\delta^6}
 \left(1+\frac1{4c^2}\right)
 \left(1+\frac1{4g^2}\right).}
\tag{S12}
\]

Here is a direct proof of the constant and uniformity. The Fourier transform of `K_delta` is `delta^-1 B_6(v/delta)`, where

\[
B_6(z)=\frac1{120}\sum_{k=0}^6(-1)^k{6\choose k}(z+3-k)_+^5.
\]

This formula follows by convolving six normalized interval indicators. It gives `B_6(0)=11/20`, `B_6''(0)=-1`, and `B_6''''(0)=6`, proving the moments above. On the final support segment, write `v=3delta-s`, `0<=s<=delta`. Differentiating the transform gives

\[
\phi_{c,g}(3\delta-s)=\delta^{-6}
\left[\frac{s^5}{120}
 +\frac{(c^{-2}+g^{-2})s^3}{24\pi^2}
 +\frac{s}{16\pi^4c^2g^2}\right]\ge0.
\tag{S13}
\]

The prime number theorem in its von Mangoldt form, `psi(x)=x+o(x)`, implies, for each `r=1,3,5`,

\[
\frac1\pi\sum_{e^{4\pi\delta}\le n\le e^{6\pi\delta}}
 \frac{\Lambda(n)}{\sqrt n}
 \left(3\delta-\frac{\log n}{2\pi}\right)^r
=(1+o(1))\frac{2r!}{\pi^{r+1}}e^{3\pi\delta}.
\tag{S14}
\]

For completeness, write the sum as a Stieltjes integral against `psi`; its nonnegative decreasing weight permits integration by parts using `sup_{x>=exp(4pi delta)}|psi(x)/x-1|=o(1)`. The main integral is `2e^(3pi delta) int_0^delta e^(-pi s)s^r ds`. Thus the errors in (S14) are uniform over the finite set of three powers. Multiplying by their nonnegative coefficients in (S13) preserves a relative `o(1)` independent of `c,g`.

On the remaining interval `0<=v<=2delta`, the three relevant carrier derivatives are bounded by constants times `delta^-1`, `delta^-3`, and `delta^-5`. Chebyshev's bound gives total absolute payment there at most

\[
O\!\left(e^{2\pi\delta}
 [\delta^{-1}+(c^{-2}+g^{-2})\delta^{-3}
      +c^{-2}g^{-2}\delta^{-5}]\right).
\]

Relative to the positive final-segment main term, this is `O(delta^5 e^(-pi delta))`, uniformly in `c,g`. This proves (S12) without omitting prime powers or presuming a sign on the interior Fourier pieces. The PNT input and its weighted formulation are standard primary material in [Tao, *246B Notes 4*, §1](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/). No RH is needed for (S8)--(S14).

There is also a uniform difference statement, including when `c/g->1`. For `c<g`,

\[
\boxed{C_{c,g}-C_{g,g}
=(1+o(1))\frac{e^{3\pi\delta}}{2\pi^6\delta^6}
 (c^{-2}-g^{-2})\left(1+\frac1{4g^2}\right)>0.}
\tag{S15}
\]

To justify subtraction despite possible near-equality, subtract transforms before estimating. Their difference is `(c^-2-g^-2)[phi_K''/(4pi^2)+phi_K''''/(16pi^4g^2)]`, positive on the final segment. On the interior use `||f+D|-|f||<=|D|`; the relative interior allowance is `O(delta^3 e^(-pi delta))`. Applying (S14) for `r=1,3` gives (S15) directly. It does not follow merely by subtracting two independent relative asymptotics.

## 5. Matched-data interpretation and remaining budget

For a certified gap `g=kappa/L`, fixed `kappa>0` and `L=log(gamma/(2pi))`, a strict mass reduction in (S9) requires

\[
\Delta>\frac{3\sqrt{3/2}}{\pi\kappa}L,
\quad
e^{2\pi\Delta}>
\exp\!\left(\frac{6\sqrt{3/2}}\kappa L\right).
\tag{S16}
\]

The second quantity is this exact bandlimited prime sum's cutoff, not a bit-complexity measure. The current Riemann--Siegel precision calculation improves the matched baseline beyond Note09's elementary Euler-sum implementation: **both** its gap-certified geometric extraction and its one-width comparator have sufficient total Dirichlet-summand count `gamma^(1/2+o(1))`, including all discrete Cauchy samples. A direct exact acquisition of the nonzero prime coefficients near the upper cutoff in (S16) has the same exponential scale as that cutoff, up to logarithmic factors. Any comparison is between these declared acquisitions, not all algorithms or optimal complexity. Equation (S12) also shows that in the mass-reducing range the absolute prime payment itself grows at least as `exp((3sqrt(3/2)/kappa-o(1))L)`.

The nonnegative companion has the smaller exact zero sum (S5) and the smaller leading absolute prime payment (S15). Nevertheless the signed gamma mass can decrease, as (S9) explicitly shows. This note has **not** proved a uniform inequality between the two complete gamma-plus-pole-plus-prime envelopes. Such a claim would have to pay the exact signed gamma difference and both pole terms, using the complete explicit formula, for example [Goldston--Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092). No such dominance is inferred merely from (S5) or (S15).

The gap remains externally certified and every noncentral zero remains in the consumer. An exact signed-prime calculation might exploit information absent from absolute payment; that possibility is outside this comparison. No original multiple zero is excluded.

**Control and false-premise screen.** The replacement argument applies to any real zero configuration with the certified gap, including the all-real endpoint controls. At a control double zero, both central contributions in (S5) remain two; the comparison supplies no upper bound below two. The algebraic and Fourier identities concern test kernels, not a modification of the theta source. Computing (S11) with genuine zeta weights is legitimate for every displayed test kernel, but identifying that calculation with a changed field's zero sum requires that field's own complete explicit formula. The normalized positive-source control fails unchanged ordinary Dirichlet-series arithmetic; the finite-data arithmetic control fails unchanged reflection and the full tail. Neither control is rejected by silently assigning it both preservation lists. The certified gap and any claimed gamma/pole budget must be acquired independently, exactly as in Notes04 and09.
