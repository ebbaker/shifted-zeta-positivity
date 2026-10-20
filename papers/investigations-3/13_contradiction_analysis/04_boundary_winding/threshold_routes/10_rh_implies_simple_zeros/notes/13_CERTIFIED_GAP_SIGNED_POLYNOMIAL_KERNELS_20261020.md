# Certified-gap signed polynomial kernels: exact comparison and prime cost

20 October 2026. Prepared for Edward Baker with LLM assistance by **gpt-6-astra, ultra**. Same-model derivation; no specialist-review or novelty claim.

**Result.** For an even polynomial times a nonnegative bandlimited carrier, a sign-changing region confined to an independently certified zero-free gap has a globally nonnegative companion of the same bandwidth and degree whose complete zero sum is no larger. For the explicit quartic-times-sixth-sinc family, the signed member also has a larger leading absolute prime payment, uniformly in its two gap parameters. This is a scoped comparison: it does not prove arithmetic-estimation dominance for all sign-changing kernels, transfer gamma/pole budgets, or give an unrestricted signed-kernel barrier.

The [result index](../../../../../../../result-summaries/README.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md) apply, especially [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [complete payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [quantitative gain](../../../../../../../avoid/20_volume_without_a_gain.md).

[Internal review](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) · [Finite evaluation comparison](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md).

**Later scope extension (20 October 2026).** Section 6 removes the polynomial-factor assumption for the exact zero-side comparison: all negative intervals must lie in an independently certified central gap. The construction handles non-even kernels and asymmetric gaps, preserves the original Fourier bandwidth when present, and has a strip-analytic version. It still does not transfer prime, gamma or pole budgets. [Separate same-model review](../reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md).

**Remote-gap continuation (20 October 2026).** Sections 7–8 treat a different, noncentral empty interval. For every fixed even sinc power, the fully paid remote-gap multiplier cannot improve its centered carrier at any bandwidth once the height is sufficiently large. The gamma and exact signed pole terms are retained. A separate-payment lemma for added remote components has narrower normalization hypotheses; the coherent construction in §9 now recovers the exact signed base value with a quantitative error. This supplies no opposing bound at a multiple zero. [Earlier review](../reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md).

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


## 6. General central-gap replacement at unchanged bandwidth

20 October 2026 continuation, prepared for Edward Baker with LLM assistance by **gpt-6-astra, ultra**. This is an addendum to Note13, not a new estimating theorem or an original-zero exclusion.

**Theorem.** Let `h` be real entire, `h(0)=1`, with Fourier support in `[-Delta,Delta]` and the quadratic decay on fixed horizontal strips used above. For finite `g_-,g_+>0`, suppose

\[
h(x)\ge0\qquad x\notin(-g_-,g_+).
\tag{S17}
\]

Then there is a real entire `h_+`, with the same normalization, minimal symmetric Fourier bandwidth, and quadratic strip decay, such that

\[
h_+(x)\ge0\quad(x\in\mathbb R),\qquad
0\le h_+(x)\le h(x)\quad(x\notin(-g_-,g_+)).
\tag{S18}
\]

Neither evenness nor symmetry of the certified gap is required.

**Finite real-zero construction.** Since `h(0)=1`, the zeros in the compact closed gap are finite. All exterior real zeros have even multiplicity. Boundary zeros may have odd multiplicity. The sign is positive near zero and in the exterior away from isolated zeros; therefore the odd real zeros on each side can be paired consecutively. Each positive-side pair has `0<a<b<=g_+`, and each negative-side pair has `-g_-<=a<b<0`. The sign between its odd endpoints is negative, apart from possible even zeros. Pairing odd zeros is essential: even zeros can split the open set `{h<0}` without changing sign.

For each such pair use the normalized rational factor

\[
R_{a,b}(z)=
\begin{cases}
(1-z/b)/(1-z/a),&0<a<b,\\
(1-z/a)/(1-z/b),&a<b<0,
\end{cases}
\qquad
h_+(z)=h(z)\prod_{(a,b)}R_{a,b}(z).
\tag{S19}
\]

Every denominator cancels one copy of the inner endpoint zero, and the numerator adds one copy of the outer endpoint zero. Both odd endpoint multiplicities become even. Each factor equals one at zero, is negative only between its endpoints, and is positive elsewhere on the real line. The finite product therefore gives an entire globally nonnegative function. Complex zeros and untouched real zeros keep their multiplicities; no infinite canonical factorization is used.

For a positive pair, `0<=R_{a,b}(x)<=1` when `x<=0` or `x>=b`; for a negative pair this holds when `x<=a` or `x>=0`. Every exterior point lies in these regions for every pair, proving (S18). Denominator zeros are strictly inside the central gap. An outer endpoint may be a gap boundary; both functions then vanish there. A negative sign interval cannot cross the origin because `h(0)=1`.

**Fourier support and strip decay.** Division by a removed real zero preserves the support directly. Set `q(x)=h(x)/(x-a)`, with its removable value at the zero, and write `phi=hat h`, `psi=hat q` using the Fourier factor `exp(-2pi ixv)`. Both `q` and `xq=h+aq` are integrable, so

\[
\psi'(v)+2\pi ia\psi(v)=-2\pi i\phi(v),\qquad
\psi(v)=-2\pi i e^{-2\pi iav}
 \int_{-\infty}^{v}e^{2\pi iaw}\phi(w)\,dw.
\tag{S20}
\]

The second formula follows from the Riemann--Lebesgue limit at negative infinity. It vanishes below `-Delta`; above `Delta` the integral equals the Fourier inversion value `h(a)=0`. Multiplication by the new linear factor is a linear combination of `q` and `h`, so it also preserves support. This proves the assertion after finitely many moves. Each inverse move is legal as well, hence the minimal symmetric bandwidth is unchanged; internal Fourier-support gaps need not be preserved.

The multiplier in (S19) tends a finite positive constant at infinity and is bounded outside a fixed disk. After cancellation the resulting entire function is bounded on each remaining compact rectangle. Thus every fixed-strip quadratic bound persists. This proof uses only the stated hypotheses and elementary Fourier inversion; it imports no factorization theorem.

The same finite root moves also apply when `h` is only holomorphic in a strip containing the real axis and satisfies the corresponding quadratic bounds on smaller closed strips. They preserve that strip, its decay contract, normalization, and the real-axis order (S18). In particular they preserve Note11's contract (X1). The Fourier-support assertion above is made only when the original kernel is bandlimited; no such assertion is needed for this strip version. Neither version transfers the separate gamma or pole budgets.

**Exact all-zero consequence.** Under RH let an ordinate `gamma` have arbitrary multiplicity `m`, and independently certify that every other distinct ordinate satisfies `lambda-gamma` outside `(-g_-,g_+)`. Complete quadratic-decay zero sums converge absolutely, with all multiplicities retained, and (S18) gives

\[
\boxed{
m\le m+\sum_{\lambda\ne\gamma}m_\lambda h_+(\lambda-\gamma)
\le m+\sum_{\lambda\ne\gamma}m_\lambda h(\lambda-\gamma).}
\tag{S21}
\]

The endpoint convention includes noncentral zeros on the gap boundary. Consequently a negative region confined to this one independently certified central gap cannot improve the exact zero-sum majorant over every globally nonnegative kernel of the same bandwidth.

This is **zero-sum dominance only**. The mass, prime payment, gamma term and pole terms can change; Note11's budgets are not automatically inherited. Formula (S20) may require Fourier information beyond the original prime samples, so equal arithmetic acquisition cost is not asserted. The finite-zero construction is an analytic existence procedure, not an implemented or complexity-bounded factorization algorithm. Nonnegativity merely at the actual zeros is insufficient for (S17); negative regions in other gaps or infinitely many negative intervals are outside scope. Moving roots in a noncentral gap can increase values between that gap and the origin.

At a control double zero, the central mass in (S21) remains two. These are transformations of test kernels, not changes to the theta source or its arithmetic coefficients. Any use for a changed field requires that field's complete explicit formula; no source receives preservation properties it lacks. No original multiple zero is excluded.


## 7. A remote known gap does not improve centered sinc-power carriers

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, reasoning effort ultra**. Continuation of this note;
same-model internal derivation, no specialist or novelty claim.

**Result.** Fix an integer `q>=2` and a number `g>0`. For all sufficiently
large `gamma` (depending on `q,g`), uniformly for **every** `delta>0`, let

\[
 k(x)=\left(\frac{\sin(\pi\delta x)}{\pi\delta x}\right)^{2q},
 \quad D=\gamma^2-g^2,
 \quad h(x)=\frac{(x+\gamma)^2-g^2}{D}k(x).
 \tag{RG1}
\]

With the same bandwidth `q delta`, the exact gamma term, both signed pole
terms, and the complete absolute prime payment, the two envelopes satisfy

\[
                         U(h)\ge U(k).
 \tag{RG2}
\]

Thus this remote-gap multiplier provides no complete-envelope gain for
centered sinc-fourth or sinc-sixth powers, or any other fixed even power
in this class. This is not an application of the central-gap companion
theorem: the negative interval here is centered at `-gamma`.

If RH holds and the original zero ordinates have an independently known
gap `|lambda|<g`, then `h(lambda-gamma)>=0` and `h(0)=1`. It is therefore a
valid multiplicity majorant at a zero of ordinate `gamma>g`. The comparison
of its displayed arithmetic envelopes is itself unconditional; RH and the
known gap enter only this zero-side interpretation. Neither comparison
excludes a multiple zero.

### Exact terms and arithmetic comparison

Use Fourier convention `phi(v)=integral k(x) exp(-2 pi i x v) dx`. Define

\[
\begin{split}
 w(y)&=\Re\psi(1/4+iy/2)-\log\pi,\\
 G(f)&=\frac1{2\pi}\int_{\mathbb R}f(x)w(\gamma+x)dx,\\
 P(f)&=f(-\gamma+i/2)+f(-\gamma-i/2),\\
 C(f)&=\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                 |\widehat f(\log n/(2\pi))|,
 \qquad U(f)=G(f)+P(f)+C(f).
\end{split}
\tag{RG3}
\]

Both kernels are entire with quadratic or faster decay in each fixed
horizontal strip: multiplication by the quadratic in (RG1) leaves
`O(|x|^(2-2q))`. The complete explicit formula therefore applies.
All prime powers are retained. No pole term is replaced by its modulus
in the definition of `U`.

The transform `phi` is the convolution of `2q` uniform densities on
`[-delta/2,delta/2]`. It is nonnegative, even, supported in
`[-q delta,q delta]`, and `C^2` for `q>=2`. It is log-concave by
[Prékopa, Theorem 7, pp. 342–343](https://rutcor.rutgers.edu/Prekopa/pdf/SCIENT2.pdf),
which states that convolution preserves log-concavity; the primary theorem
and its marginalization proof were inspected. Hence
`phi phi'' <= (phi')^2` wherever `phi>0`, with continuity at all knots.

The transform of the signed kernel is exactly

\[
 \widehat h=\phi+i\alpha\phi'-\beta\phi'',
 \qquad \alpha=\frac{\gamma}{\pi D},\quad
 \beta=\frac1{4\pi^2D}.
 \tag{RG4}
\]

Consequently

\[
\begin{split}
 |\widehat h|^2-\phi^2
 &=\alpha^2(\phi')^2-2\beta\phi\phi''+\beta^2(\phi'')^2\\
 &\ge(\alpha^2-2\beta)(\phi')^2+\beta^2(\phi'')^2\ge0,
 \qquad
 \alpha^2-2\beta=\frac{\gamma^2+g^2}{2\pi^2D^2}>0.
\end{split}
\tag{RG5}
\]

At the support endpoints `phi=phi'=phi''=0`, so this also covers those
points. Thus `C(h)>=C(k)` exactly. The same transform comparison holds
for other sufficiently regular, nonnegative log-concave Fourier
densities, but (RG2)'s fully paid conclusion below is proved for the
specified sinc-power carriers.

### The complete gamma term increases

The [digamma series, DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) shows that
`w` is even and increasing in `|y|`: for `y>0` its derivative is the
convergent positive series

\[
 w'(y)=\sum_{j\ge0}
 \frac{(j+1/4)y/2}{((j+1/4)^2+y^2/4)^2}>0.
\]

Also `w(gamma)=log(gamma/(2 pi))+o(1)` by the
[digamma asymptotic, DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2). Pairing
`x` and `-x` in the exact difference gives

\[
\begin{split}
G(h)-G(k)=\frac1{2\pi D}\int_0^\infty k(x)
\{x^2[w(\gamma+x)+w(\gamma-x)]
 +2\gamma x[w(\gamma+x)-w(\gamma-x)]\}dx.
\end{split}
\tag{RG6}
\]

The second bracket is nonnegative, since
`gamma+x>=|gamma-x|`. The first bracket is at least
`w(gamma)+w(0)`. Writing

\[
 M_2(k)=\int_{\mathbb R}x^2k(x)dx=m_{2,q}\delta^{-3},
 \qquad 0<m_{2,q}<\infty,
\]

we obtain, uniformly in `delta>0`,

\[
 G(h)-G(k)\ge\frac{M_2(k)}{4\pi D}[w(\gamma)+w(0)]
 \gg_q\frac{\log\gamma}{\gamma^2\delta^3}>0
 \tag{RG7}
\]

for all sufficiently large `gamma` depending on `g`. This is a bound
on the complete signed gamma integral, including the remote interval;
no central Taylor expansion or omitted gamma tail is used.

### Exact poles and the two uniform width ranges

At either pole evaluation the multiplier in (RG1) equals
`-(g^2+1/4)/D`. Therefore

\[
 P(h)-P(k)=-\frac{\gamma^2+1/4}{D}P(k).
 \tag{RG8}
\]

Only a positive `P(k)` can lower the new envelope. For `gamma>=max(2g,1)`
the coefficient in (RG8) is bounded by an absolute constant. The bounds
`|sin z|<=exp(|Im z|)` and
`|sin z/z|<=exp(|Im z|)` give

\[
 |P(k)|\ll_q e^{q\pi\delta}
                \min\{1,(\delta\gamma)^{-2q}\}.
 \tag{RG9}
\]

For all `0<delta<=delta_0`, where `delta_0` is any fixed number, set
`v=delta gamma`. Equation (RG7) is at least a constant times
`gamma log(gamma)/v^3`. If `v<=1`, this exceeds the bounded pole allowance
in (RG9). If `v>=1`, its ratio to that allowance is at least a constant
times `gamma log(gamma) v^(2q-3)`, which tends to infinity uniformly.
Thus the complete gamma increase alone pays any pole decrease in this
entire bounded-width range, including widths tending to zero arbitrarily
quickly. Together with (RG5), this proves (RG2) there.

For the remaining large widths, write `B=2 pi q delta`, `r=2q-1` and
`z=B-u`, where `u=log n`. On the fixed outer shell `1<=z<=2`, once
`delta` is sufficiently large, the exact outer spline is

\[
 \phi(u/(2\pi))=c_q\delta^{-2q}z^r,
 \qquad c_q=\frac1{r!(2\pi)^r}.
\]

Equations (RG4)–(RG5) give the exact squared modulus ratio

\[
\frac{|\widehat h(u/(2\pi))|^2}{\phi(u/(2\pi))^2}-1
 =\frac{2r((r+1)\gamma^2+(r-1)g^2)}{D^2z^2}
  +\frac{r^2(r-1)^2}{D^2z^4}.
 \tag{RG10}
\]

For `1<=z<=2` and sufficiently large `gamma`, this lies between positive
constant multiples (depending on `q`) of `gamma^-2`. Taking square roots
therefore yields
`|hhat|-phi >>_q delta^(-2q) gamma^-2` on that shell. No subtraction of
two separately approximated prime sums is involved. The prime number
theorem in its von Mangoldt form ([Tao, Notes 4, Theorem 6](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/)),
followed by partial summation, gives

\[
\sum_{e^{B-2}\le n\le e^{B-1}}\frac{\Lambda(n)}{\sqrt n}
 \sim2(e^{-1/2}-e^{-1})e^{B/2}.
\]

Thus there is a fixed `delta_0(q)` beyond which, uniformly in `gamma`,

\[
 C(h)-C(k)\gg_q
      \gamma^{-2}\delta^{-2q}e^{q\pi\delta}.
 \tag{RG11}
\]

By (RG9), the possible pole loss is at most
`O_q(gamma^(-2q) delta^(-2q) exp(q pi delta))`. Its ratio to (RG11)
tends to zero as `gamma` grows, uniformly for `delta>=delta_0` because
`q>=2`. The gamma difference is already nonnegative by (RG7).
This proves (RG2) for all remaining widths. Combining the two ranges
gives one height threshold depending only on fixed `q,g`.

The threshold is not numerically instantiated; this is a proved uniform
large-height comparison, not an executed finite-height certificate.
The prime-number-theorem input is the standard unchanged-von-Mangoldt
asymptotic, not an assumed event-conditioned prime cancellation.

### Scope

This comparison retains an actual signed kernel outside Notes 11's
globally nonnegative class and Note 13's central-gap companion class.
It shows precisely why its favorable signed pole factor cannot improve
these centered carriers after the same arithmetic and completion data
are paid. The proof does not cover `q` growing with height, a gap `g`
growing with height, non-even carriers, arbitrary non-log-concave Fourier
densities, or carriers concentrated near the remote gap. The separate
remote-carrier calculation must retain its own full completion and
prime terms. No bound for a retained signed prime sum has been obtained.

The result/avoid indexes and their scoped-exclusion and complete-payment
rules remain applicable; this is one complete comparison, not a new
simplicity criterion or an absolute-envelope optimization over all signed
kernels.


## 8. An independent small gap and separately paid remote components

The remote negative interval need not be inferred from the desired simplicity statement. For example, an elementary zero-free segment has g=1/8 in zeta-ordinate units. Euler summation gives
\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{x\}x^{-s-1}\,dx
\quad(\Re s>0,\ s\ne1).
\]
Splitting the remainder at two bounds its absolute integral at Re s=1/2 by
\[
\int_1^2(x-1)x^{-3/2}dx+\int_2^\infty x^{-3/2}dx=4\sqrt2-4.
\]
Thus for s=1/2+it and |t|<=1/8,
\[
\Re\zeta(s)\le-\frac{15}{17}+\frac{\sqrt{17}}8(4\sqrt2-4)<0.
\tag{RG12}
\]
Under RH every nontrivial zero ordinate therefore satisfies |lambda|>g. This small gap is used only to make the negative test interval legitimate; it is not a new high-height exclusion.

For a different carrier let ell>=0 be real and bandlimited, with quartic decay on fixed horizontal strips, and put
\[
q_\gamma(x)=D^{-1}[(x+\gamma)^2-g^2]\ell(x+\gamma),
\qquad
\mathcal B(v)=-\widehat\ell''(v)/(4\pi^2)-g^2\widehat\ell(v).
\]
Then hat q_gamma(v)=D^(-1) exp(2 pi i gamma v) B(v). Its shift cancels the actual-height phase in the signed prime sum. The complete explicit formula, with every multiplicity and prime power retained, is
\[
\begin{split}
D S_\gamma(q_\gamma)
={}&\sum_\lambda m_\lambda(\lambda^2-g^2)\ell(\lambda)\\
={}&-(g^2+1/4)[\ell(i/2)+\ell(-i/2)]
 +\frac1{2\pi}\int_{\mathbb R}(u^2-g^2)\ell(u)w(u)\,du\\
&-\frac1\pi\Re\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
          \mathcal B(\log n/(2\pi)).
\end{split}
\tag{RG13}
\]
Here S_gamma(f)=sum m_lambda f(lambda-gamma), and w is from (RG3). This is a test at ordinate zero, apart from the factor D. Its left side is nonnegative by the known gap, so a negative pole term must be considered together with the rest of this same formula.

There is an exact non-improvement statement for a separately paid addition. Require ell(gamma)=0, so q_gamma(0)=0; such carriers exist, for example a sixth sinc power with delta gamma a nonzero integer. For any a>=0, adding a q_gamma preserves the base kernel's normalization and its nonnegativity at all zero offsets. If its prime contribution receives a separate absolute payment, the added envelope is
\[
a\{G(q_\gamma)+P(q_\gamma)+C(q_\gamma)\}
=a\{S_\gamma(q_\gamma)+Q_\gamma(q_\gamma)+C(q_\gamma)\}\ge0,
\tag{RG14}
\]
because |Q_gamma(q_gamma)|<=C(q_gamma). This argument is independent of a hypothetical multiple zero. It does not apply after taking the coherent modulus C(f+a q_gamma), nor after changing the normalization by using ell(gamma)>0. No general dominance theorem for remote carriers is claimed.

These statements use the genuine zeta completion and weights. A changed-source or Euler control must use its own gap and complete formula; none is assigned the unchanged arithmetic. The normalized source control in Note 05 fails the ordinary Dirichlet-series premise, while Note 09's ordinary-Dirichlet control fails completed reflection and entireness. The general separate-payment statement applies to a control only when its own formula has the same required positivity and payment properties. No control event or original multiple zero is excluded.

[Separate same-model review](../reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md). The [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md) retain their stated scope and status rules.


### 9.9. Coherent remote-gap saturation of a fixed signed consumer

20 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model: **gpt-6-astra**; reasoning effort: **ultra**. Proved in-note under the stated RH and fixed-test hypotheses, with
separate same-model internal derivations and review; no specialist review
or novelty claim.

**Status and changed quantity.** Under RH and the independently known
central ordinate gap, a coherent remote component reduces the complete
absolute-prime overpayment of any fixed admissible bandlimited base to
`O(delta^(1/2-q))`. Its limit is exactly the base's signed zero sum. This
is a proved saturation construction, not an estimate making that sum
less than two. It extends Note 13 §8 beyond separate prime payment and
does not contradict the globally nonnegative class of Note 11.

The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md), and specifically
[scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [quantitative-gain rule](../../../../../../../avoid/20_volume_without_a_gain.md)
govern this statement.

### 9.1. Fixed data and complete normalization

Assume RH. Count distinct nontrivial ordinates `lambda` with their actual
multiplicities `m_lambda`. Fix `g>0` for which `|lambda|>g`; the elementary
choice `g=1/8` is proved in Note 13 §8. Fix `gamma>g` and put
`D=gamma^2-g^2`. The center need not be a zero.

Let `f` be real on the real axis, analytic in a strip wider than
`|Im x|<=1/2`, decaying there as `O((1+|x|)^(-1-epsilon))`, with
`f(0)=1`, finite Fourier support `[-Delta_f,Delta_f]`, and
`f(lambda-gamma)>=0` at every zero. Use

\[
\widehat f(v)=\int_{\mathbb R}f(x)e^{-2\pi ixv}\,dx,
\quad v_n=\frac{\log n}{2\pi},
\quad w_n=\frac{\Lambda(n)}{\pi\sqrt n}.
\tag{CS1}
\]

Write

\[
\begin{split}
S_\gamma(f)&=\sum_\lambda m_\lambda f(\lambda-\gamma),\\
G_\gamma(f)&=\frac1{2\pi}\int_{\mathbb R}f(x)
 \left\{\Re\psi\left(\frac14+\frac{i(\gamma+x)}2\right)-\log\pi\right\}dx,\\
P_\gamma(f)&=f(-\gamma+i/2)+f(-\gamma-i/2),\\
Q_\gamma(f)&=\sum_{n\ge2}w_n\Re\{n^{-i\gamma}\widehat f(v_n)\},
\qquad C(f)=\sum_{n\ge2}w_n|\widehat f(v_n)|,\\
U_\gamma(f)&=G_\gamma(f)+P_\gamma(f)+C(f).
\end{split}
\tag{CS2}
\]

The complete explicit formula is

\[
S_\gamma(f)=G_\gamma(f)+P_\gamma(f)-Q_\gamma(f),
\qquad U_\gamma(f)-S_\gamma(f)=C(f)+Q_\gamma(f)\ge0.
\tag{CS3}
\]

All prime powers and both poles are retained. The imported formula is
[Goldston–Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092), applied to
`x -> f(x-gamma)`; their Fourier convention is (CS1). The decay hypotheses
above imply absolute convergence on the zero and gamma sides. No
asymptotic replacement of `G` or absolute replacement of `P` is made.

### 9.2. A remote component with exactly negative prime phases

Fix an integer `q>=2`. For `delta>0` with `delta gamma` a positive integer,
define

\[
\ell_\delta(u)=\left(\frac{\sin\pi\delta u}{\pi\delta u}\right)^{2q},
\qquad
r_\delta(x)=\frac{(x+\gamma)^2-g^2}{D}\ell_\delta(x+\gamma).
\tag{CS4}
\]

These entire functions have the required strip decay: `r_delta` is
`O(|x|^(2-2q))` on each fixed horizontal strip, with constants allowed
to depend on `delta,gamma`. Its Fourier support is `[-q delta,q delta]`.
The lattice condition gives `r_delta(0)=0`, while
`r_delta(lambda-gamma)>=0` at every zero. Thus `f+a r_delta` has the
original normalization and zero-side positivity for every `a>=0`.

Let `F_q` be the `2q`-fold convolution of the indicator of `[-1/2,1/2]`.
Elementary Fourier multiplication gives

\[
\widehat\ell_\delta(v)=\delta^{-1}F_q(v/\delta),
\qquad
\widehat r_\delta(v)=-b_\delta(v)e^{2\pi i\gamma v},
\quad
b_\delta(v)=\frac{g^2\delta^{-1}F_q(v/\delta)
             +(4\pi^2)^{-1}\delta^{-3}F_q''(v/\delta)}D.
\tag{CS5}
\]

Here `F_q` is positive on `(-q,q)`, is `C^(2q-2)` on the real line,
and vanishes off `[-q,q]`. On either outer unit interval its exact
simplex-convolution formula is

\[
F_q(t)=\frac{(q-|t|)^{2q-1}}{(2q-1)!}
\quad(q-1\le |t|\le q).
\tag{CS6}
\]

Consequently `F_q''/F_q` is continuous in the interior and is positive
near both endpoints. It therefore has a finite lower bound. Define

\[
K_q=\max\left(0,-\inf_{|t|<q}\frac{F_q''(t)}{F_q(t)}\right)<\infty.
\tag{CS7}
\]

For `delta^2>=K_q/(4 pi^2 g^2)`, (CS5) gives `b_delta>=0`
everywhere, including the endpoints by continuity. This proof uses only
elementary convolution and compactness; it does not import a
log-concavity assertion. For `q=2` one can take the exact value `K_2=3`:
on `0<=t<=1`, `F_2=2/3-t^2+t^3/2` and
`F_2''+3F_2=(3/2)t((t-1)^2+1)>=0`; on `1<=t<=2`, `F_2''>=0`.
Thus `delta>=sqrt(3)/(2 pi g)` suffices in the quartic case.

On the fixed base support, (CS5) also gives uniformly

\[
D\delta b_\delta(v)\longrightarrow g^2F_q(0)>0
\quad(|v|\le\Delta_f).
\tag{CS8}
\]

Hence there are `c_0>0` and `delta_0`, depending only on `g,q,Delta_f`,
such that `b_delta(v)>=c_0/(D delta)` there for `delta>=delta_0`.

The factor `exp(2 pi i gamma v_n)=n^(i gamma)` in (CS5) cancels the
actual-height phase at every prime power. Therefore

\[
Q_\gamma(r_\delta)=-C(r_\delta),
\qquad U_\gamma(r_\delta)=S_\gamma(r_\delta).
\tag{CS9}
\]

This is exact at each finite `delta`, not an asymptotic assertion about
prime distribution.

### 9.3. The zero-side leakage is small

The independently known gap and `|sin|<=1` give

\[
0\le S_\gamma(r_\delta)
\le\frac{\delta^{-2q}}{D\pi^{2q}}
          \sum_\lambda m_\lambda\frac{\lambda^2-g^2}{|\lambda|^{2q}}
=\frac{A_q}{D}\delta^{-2q},
\qquad A_q<\infty.
\tag{CS10}
\]

The summand is bounded above by `m_lambda |lambda|^(2-2q)`.
Convergence follows from `N_abs(T)=O(T log(2+T))` and `q>=2`;
dyadic shells are `O(T^(3-2q) log(2+T))`. For an explicit source of the
zero-count bound, see [Simonič, equation (1)](https://arxiv.org/pdf/1910.08274).
The finite low-ordinate part is separated from zero by `g`; all
multiplicities remain in `A_q`. Neither a local spacing assertion nor
simplicity is used.

### 9.4. Coherent modulus: finite residual and quantitative saturation

Put `h=f+a r_delta`, and at each prime power write
`z_n=n^(-i gamma) fhat(v_n)` and `t_n=a b_delta(v_n)>=0`. Linearity
of the exact completion and (CS9) give

\[
U_\gamma(h)-S_\gamma(f)
=aS_\gamma(r_\delta)
  +\sum_{n\ge2}w_n\{ |z_n-t_n|-t_n+\Re z_n\}.
\tag{CS11}
\]

The summand is nonnegative. If `z_n=0` it is exactly zero, so only the
fixed finite set `v_n<=Delta_f` contributes, even though the remote
component has bandwidth `q delta`. For `t>0` with `t>=2|z|`,
rationalization yields

\[
0\le |z-t|-t+\Re z
=\frac{(\Im z)^2}{|z-t|+t-\Re z}
\le\frac{|z|^2}{t}.
\tag{CS12}
\]

The degenerate case `t=z=0` has zero residual and is handled directly.

Choose, for definiteness,

\[
a=D\delta^{q+1/2}.
\tag{CS13}
\]

By (CS8), `t_n>=c_0 delta^(q-1/2)` on the fixed prime set. This
eventually exceeds `2 sup |fhat|`. Combining (CS10)–(CS13) proves

\[
\boxed{\quad
0\le U_\gamma(f+D\delta^{q+1/2}r_\delta)-S_\gamma(f)
\le
\left(A_q+c_0^{-1}\sum_{v_n\le\Delta_f}w_n|\widehat f(v_n)|^2\right)
\delta^{1/2-q}\longrightarrow0 .\quad}
\tag{CS14}
\]

The limit is along the unbounded lattice `delta gamma in N`. The
displayed constants and onset depend on the fixed base and on `g,q`;
there is no hidden zero separation or multiplicity premise. In
particular this proves the requested fixed-height result, with quartic
rate `O(delta^(-3/2))`. The same algebra holds for every `gamma>g`
with the stated data, but no uniform bound for a varying family `f_gamma`
or numerical evaluation cost is asserted.

This can be an actual reduction from the base envelope: if
`C(f)+Q_gamma(f)>0`, then (CS3) and (CS14) imply `U_gamma(h)<U_gamma(f)`
for all sufficiently large admissible `delta`. It cannot improve on the
exact signed consumer `G_gamma(f)+P_gamma(f)-Q_gamma(f)=S_gamma(f)`.

### Effective quartic constants and a strict comparison

For `q=2` and `g=1/8`, the existing paired-xi-product identity in Note 01
§3 yields

\[
Z:=\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}
=2\frac{\xi'(1)}{\xi(1)}
=2+\gamma_{\!E}-\log(4\pi).
\tag{CS14a}
\]

The first equality is the product logarithmic derivative at `s=1`;
the second follows from `xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`,
`(s-1)zeta(s)=1+gamma_E(s-1)+O((s-1)^2)`, and
`psi(1/2)=-gamma_E-2log 2`. All zeros and multiplicities are retained.
For `t>=g^2`, direct maximization gives
`(t-g^2)(t+1/4)/t^2 <=(g^2+1/4)^2/g^2=289/64`. Therefore

\[
A_2\le\frac{289}{64\pi^4}\{2+\gamma_{\!E}-\log(4\pi)\}.
\tag{CS14b}
\]

If `delta>=2Delta_f` and `delta^2>=3/(2 pi^2 g^2)`, the cubic formula
gives `F_2(v/delta)>=23/48` on the base support and (CS5) gives
`b_delta>=23g^2/(96D delta)`. Hence, writing `M=sup |fhat|` and
`R_f=sum_(v_n<=Delta_f) w_n |fhat(v_n)|^2`, (CS14) becomes the effective bound

\[
U_\gamma(f+D\delta^{5/2}r_\delta)-S_\gamma(f)
\le\left[\frac{289Z}{64\pi^4}+\frac{96R_f}{23g^2}\right]\delta^{-3/2},
\tag{CS14c}
\]

provided also `delta^(3/2)>=192M/(23g^2)` and `delta gamma in N`.
This is an explicit analytic allowance; no numerical scan is required.

For a concrete strict margin, suppose `fhat` is real and nonnegative
and is positive at `v_p,v_(p^2)` for one prime `p`. Put
`c_1=w_p fhat(v_p)>0` and `c_2=w_(p^2) fhat(v_(p^2))>0`. Since every
other term of `C+Q` is nonnegative, writing `x=cos(gamma log p)` gives

\[
C(f)+Q_\gamma(f)\ge c_1(1+x)+2c_2x^2\ge\kappa,
\quad
\kappa=
\begin{cases}
c_1-c_1^2/(8c_2),&c_1\le4c_2,\\
2c_2,&c_1>4c_2,
\end{cases}
\qquad\kappa>0.
\tag{CS14d}
\]

Choosing the right side of (CS14) or (CS14c) below `kappa/2` proves
`U_gamma(h)<=U_gamma(f)-kappa/2`. The elementary `p,p^2` relation itself
already belongs to Note 06's universal multiplicative-phase information
class; it is not a new prime cancellation estimate. Its role here is to
exhibit a strict full-envelope reduction using the different coherent
remote construction. No leading-height or simplicity improvement follows.

### 9.5. Exact completion cost and interpretation

The pole term retained above is explicitly

\[
aP_\gamma(r_\delta)
=-2(g^2+1/4)\delta^{q+1/2}
   \left\{\frac{\sinh(\pi\delta/2)}{\pi\delta/2}\right\}^{2q}
\sim-\frac{2(g^2+1/4)}{\pi^{2q}}
       e^{q\pi\delta}\delta^{1/2-q}.
\tag{CS15}
\]

In the unshifted gamma integral, scaling `u -> u/delta` and the
standard bound `|Re psi(1/4+iu/2)-log pi|=O(log(2+|u|))` give
`aG_gamma(r_delta)=O_(g,q)(delta^(q-1/2))` for `delta>=1`; the
required integrals converge already at `q=2`. Thus (CS9)–(CS10)
also show `aC(r_delta)~ -aP_gamma(r_delta)`, with the exponential size
in (CS15). No polynomial-size precision claim is hidden in (CS14).
The growth bound follows, for example, from the
[digamma asymptotic, DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)
and boundedness on compact real ordinates.

Moreover `h(-gamma)=f(-gamma)-g^2 delta^(q+1/2)` is negative for
large `delta`. The construction is outside the globally nonnegative
kernel class and its stated gamma/pole budgets. It also lies outside
the separately paid addition in Note 13 §8: (CS11) takes the coherent
modulus before summing and retains the signed poles exactly.

At an actual zero of multiplicity `m_gamma`, the base assumptions give
`S_gamma(f)>=m_gamma`. Hence a putative double zero forces the limit in
(CS14) to remain at least two. The construction supplies no opposing
signed arithmetic bound, no event exclusion, and no RH-to-simplicity
theorem. It shows quantitatively why a universal barrier for coherent
remote-gap carriers cannot be inferred from separate payment.

The unchanged zeta arithmetic is essential to the exact completion
used here. A collision control must retain its own zero set, gap and
explicit formula; it is not assigned these prime weights or pole terms.
The source control in Note 05 fails ordinary Dirichlet-series arithmetic,
and the arithmetic control in Note 09 fails the completed reflection
and entire-function premise. No control zero or original multiple zero
is ruled out by (CS14).


**Scope of unrestricted optimization.** At a fixed actual ordinate of multiplicity `m`, the infimum of these envelopes over unbounded auxiliary bandwidth and pole magnitude is `m`. Indeed the bases `f_T(x)=sinc²(pi T x)` have `S_gamma(f_T)->m`, by dominated convergence with the complete all-zero majorant `min(1,1/(pi²x²))` for `T>=1`. For each fixed `T`, (CS14) approximates that sum arbitrarily closely; conversely every admissible member has `U>=S>=m`. This limit estimates neither `m` nor a sufficient bandwidth, and is recorded only to delimit extension of Note11 to this signed class, not as a simplicity criterion.

[Separate same-model review](../reviews/15_COHERENT_REMOTE_GAP_SATURATION_REVIEW_20261020.md) checks the complete formula, explicit constants, controls and limiting interpretation.
