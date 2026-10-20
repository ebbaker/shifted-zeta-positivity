# Exact theta modes and the cost of their signed Gram cancellation

20 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model: **gpt-6-astra**, reasoning effort **ultra**. This is an analytic estimate for the unchanged theta source, with no numerical sign scan or literature-novelty claim. Status: the displayed asymptotics and their scoped comparison consequence are proved below; RH implies simplicity remains open.

The positive theta modes have a nonzero diagonal first-jet energy of order \(a^{-4}\), while their complete first-jet energy is exponentially small. Consequently their signed off-diagonal contribution is asymptotic to the negative of the entire diagonal, at every large real height. This gives an explicit precision cost for a separately paid mode-diagonal argument. It supplies no lower bound for the full energy and no contradiction at a multiple zero.

## 1. Original source, exact normalization and all-mode endpoint bounds

Use the track's source and time-zero normalization
\[
\begin{split}
Y_n&=\pi n^2,\qquad s_n(u)=Y_ne^{4u},\\
\Phi_n(u)&=e^u[2s_n(u)^2-3s_n(u)]e^{-s_n(u)},\qquad
\Phi(u)=\sum_{n\ge1}\Phi_n(u),\\
f_n(a)&=\int_0^\infty\Phi_n(u)\cos(au)\,du,\\
F(a)&=H(0,a)=\sum_{n\ge1}f_n(a)
       =\frac18\xi\!\left(\frac12+\frac{ia}{2}\right).
\end{split}
\tag{T1}
\]
In particular \(a=2\gamma\) for a zeta ordinate \(\gamma\). Each \(\Phi_n\) is strictly positive on \(u\ge0\), because \(s_n\ge\pi>3/2\). Its individual extension across zero need not be even; evenness belongs to the complete modular source.

Define polynomials
\[
P_0(s)=2s^2-3s,\qquad
P_{r+1}(s)=(1-4s)P_r(s)+4sP_r'(s).
\tag{T2}
\]
Then
\[
\Phi_n^{(r)}(u)=e^uP_r(Y_ne^{4u})e^{-Y_ne^{4u}},
\qquad \deg P_r=r+2.
\]
For each fixed \(r\), substitution \(s=Y_ne^{4u}\) gives
\[
\begin{split}
|\Phi_n^{(r)}(0)|&\ll_r Y_n^{r+2}e^{-Y_n},\\
\|\Phi_n^{(r)}\|_{L^1(0,\infty)}
&\le\frac{Y_n^{-1/4}}4
 \int_{Y_n}^\infty s^{-3/4}|P_r(s)|e^{-s}\,ds
 \ll_r Y_n^{r+1}e^{-Y_n}.
\end{split}
\tag{T3}
\]
The same argument permits any fixed power of \(u=\tfrac14\log(s/Y_n)\), changing only the polynomial bound in \(Y_n\). These estimates are summable in \(n\). They justify termwise differentiation and integration, every integration by parts used below, and all complete double sums. They also ensure vanishing of every upper boundary term.

The first endpoint derivative is
\[
A_n:=\Phi_n'(0)
 =e^{-Y_n}(-8Y_n^3+30Y_n^2-15Y_n).
\tag{T4}
\]
Complete theta modularity makes \(\Phi\) even, so the summable endpoint series satisfies \(\sum_nA_n=\Phi'(0)=0\). In contrast,
\[
c_\theta:=\sum_{n\ge1}A_n^2\in(0,\infty).
\tag{T5}
\]
Finiteness follows from (T3). For strict positivity, \(Y_2=4\pi>12\) implies \(-8Y_2^2+30Y_2-15<0\), hence \(A_2<0\). Thus modular cancellation annihilates the summed endpoint derivative without annihilating its diagonal square sum.

## 2. Uniform summable value and derivative remainders

For \(a\ge1\), four integrations by parts give the exact formula
\[
f_n(a)=-\frac{A_n}{a^2}
 +\frac{\Phi_n'''(0)+\int_0^\infty\Phi_n^{(4)}(u)\cos(au)\,du}{a^4}.
\tag{T6}
\]
Set \(g_n(u)=u\Phi_n(u)\). Since \(g_n(0)=0\) and \(g_n''(0)=2A_n\), a separate sine-integral expansion, rather than differentiation of an uncontrolled remainder, gives
\[
f_n'(a)=\frac{2A_n}{a^3}
 -\frac{g_n^{(4)}(0)+\int_0^\infty g_n^{(5)}(u)\cos(au)\,du}{a^5}.
\tag{T7}
\]
In particular, with
\[
B_n=|\Phi_n'''(0)|+\|\Phi_n^{(4)}\|_1,
\qquad C_n=|g_n^{(4)}(0)|+\|g_n^{(5)}\|_1,
\]
one has
\[
\left|f_n+\frac{A_n}{a^2}\right|\le\frac{B_n}{a^4},
\qquad
\left|f_n'-\frac{2A_n}{a^3}\right|\le\frac{C_n}{a^5},
\qquad
\sum_n(|A_n|+B_n+C_n)<\infty.
\tag{T8}
\]
It follows by direct multiplication, with the errors summed absolutely, that the actual diagonal energy obeys
\[
D(a):=\sum_{n\ge1}\bigl(f_n(a)^2+f_n'(a)^2\bigr)
 =\frac{c_\theta}{a^4}+O(a^{-6}).
\tag{T9}
\]
In particular \(D(a)>0\) for all sufficiently large \(a\). No RH hypothesis is used.

## 3. A complete exponential upper bound with the derivative paid

The bound needed here is coarse and unconditional. On the complex disk \(|z-a|\le1/2\), put \(s=1/2+iz/2=\sigma+it\). For large real \(a\),
\[
\frac14\le\sigma\le\frac34,\qquad t=\frac a2+O(1).
\]
Euler summation with the integer \(N=\lceil a\rceil\) gives, uniformly on this disk,
\[
\zeta(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1}
 -s\int_N^\infty(x-\lfloor x\rfloor)x^{-s-1}\,dx,
\qquad |\zeta(s)|\ll a^{1-\sigma}.
\tag{T10}
\]
The identity is valid for \(\Re s>0\), \(s\ne1\); see [DLMF 25.2.8](https://dlmf.nist.gov/25.2.E8). The bound follows by separately estimating its three displayed terms; here \(|s|\asymp a\), \(|s-1|\asymp a\), and \(\sigma\ge1/4\).

Using the [completed-zeta formula, DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4), and [the vertical Stirling estimate, DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), uniformly in this fixed strip,
\[
\begin{split}
|\xi(s)|
&\ll a^2 a^{\sigma/2-1/2}e^{-\pi t/4}a^{1-\sigma}\\
&\ll a^{5/2}e^{-\pi a/8}.
\end{split}
\tag{T11}
\]
Thus (T1), continued holomorphically, and Cauchy's derivative estimate on this fixed disk bound both \(|F(a)|\) and \(|F'(a)|\) by the right side of (T11), with an absolute constant. Consequently
\[
0\le J(a):=F(a)^2+F'(a)^2
 \ll a^5e^{-\pi a/4}.
\tag{T12}
\]
The squares are ordinary real squares at real \(a\). This argument does not differentiate a pointwise big-O estimate and does not assume simple zeros, RH, or derivative-moment bounds.

## 4. Exact signed cancellation and its scope

Keep the complete signed off-diagonal term
\[
X(a):=2\sum_{n<\ell}
  \bigl(f_n(a)f_\ell(a)+f_n'(a)f_\ell'(a)\bigr).
\]
Absolute convergence from (T3) or (T8) gives the exact Gram identity
\[
J(a)=D(a)+X(a).
\tag{T13}
\]
Combining (T9) and (T12), for all sufficiently large real \(a\),
\[
\boxed{
\frac{X(a)}{D(a)}=-1+\frac{J(a)}{D(a)},
\qquad
0\le\frac{J(a)}{D(a)}\ll a^9e^{-\pi a/4}.}
\tag{T14}
\]
In the zeta ordinate \(\gamma=a/2\), the relative upper bound is \(O(\gamma^9e^{-\pi\gamma/2})\). At any hypothetical real zero of multiplicity \(m\ge2\), \(J=0\), and hence \(X=-D\) exactly whenever \(D>0\). But near-total negative off-diagonal cancellation in (T14) already occurs at every large real height, whether or not a zero is present.

This excludes a fixed or algebraic relative coercivity inequality \(J(a)\ge\eta(a)D(a)\) for the unchanged individual theta modes whenever \(\eta(a)\) exceeds the exponential upper bound in (T14). More precisely, any claimed positive diagonal margin in \(X\ge-(1-\eta)D\) must satisfy \(0<\eta\le J/D\). Likewise, a sign guarantee that must survive every independently allowed additive perturbation of magnitude at most \(\eta D\) requires \(\eta<J/D\): otherwise the perturbation \(-J\) is allowed. Such a robust separately paid allowance must therefore be at most \(O(a^9e^{-\pi a/4})\) relative to \(D\). The actual required error can be smaller: (T12) is an upper bound, not a lower bound for \(J\). This statement does not prohibit a favorable one-sided enclosure with a larger reported two-sided radius. It is not a lower complexity bound for coherent signed evaluation, rescaled zeta evaluation, or all methods using the exact theta coefficients.

The result retains the unchanged square-supported theta coefficients and their full modular relation. It does not enlarge the source class to manufacture a collision. It also does not extract a sign contradiction from the positive discrete Laplace representation: positivity of the modes in the source variable does not make their oscillatory cross terms nonnegative. No event-conditioned signed lower bound has been obtained here.

## 5. Relation to prior screens and the continuation boundary

The [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md) govern the classification. This is a scoped estimate, not a new sufficient criterion; apply the classifications in [avoid/01](../../../../../../../avoid/01_restating_the_target.md), [avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [avoid/12](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The relevant existing results are indexed in [result-summaries/12](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [result-summaries/14](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md).

The sibling Investigation 21 [Note 52](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md) derives a positive auxiliary primitive of algebraic spectral size and retains its signed reconstruction of the exponentially small physical field. Its [Note 56](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) shows that matching all algebraic primitive asymptotic coefficients does not prevent a collision in a broader source class. Here the additional estimate is the explicit \(c_\theta a^{-4}\) diagonal and the relative signed cancellation rate for the **actual original theta-mode first jets**; no auxiliary primitive or changed source is used.

Investigation 22's [weighted-comb reflection rigidity](../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) already establishes that complete reflection plus square support fixes the coefficients under its stated growth assumptions. Coefficient uniqueness is not an event-conditioned positive identity. The present calculation makes one attempted diagonal-positive extraction from those fixed coefficients quantitatively unsuitable.

The normalized positive-source control in [Note 05](05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md) fails the ordinary Dirichlet-series premise. The distinct ordinary-Dirichlet control in [Note 09](09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md) fails completed reflection and entireness. Neither has the unchanged theta-mode decomposition used here, and neither is excluded by this calculation. Their preservation lists remain separate.

The changed-source and Jensen controls in local [Note 05](05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md) and [Note 07](07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_COMPARISONS_20261020.md) remain distinct. The direct Riemann–Siegel acquisition analysis in [Note 12](12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) does not split the physical energy into this positive diagonal and independently paid cross terms, and is not restricted by (T14). A useful next signed theorem must retain and control the cancellation itself; merely invoking theta modularity or the positive discrete source again supplies no further estimate.

[Separate same-model review](../reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md) · [Progress](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md).
