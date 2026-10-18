# Round 2: diverging heat tilts and Newman's classical source class

17 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**;
reasoning effort: **ultra**. Same-model agents independently checked the
convolution, product, weak closure and scope. No cross-model or specialist
review of this continuation has occurred.

**Status: proved in-note using Newman's classical classification.** A weak
limit of diverging positive heat tilts of symmetric LP seeds belongs to
the class whose every Gaussian downweight has real-zero transform.
Consequently neither theta nor the stable Bessel source can be such a
limit. This is a sequential application of Newman's 1976 mechanism,
not a new real-zero principle or an RH claim.

This follows [Note 01](01_WEAK_CLOSURE_AND_ALL_BASE_TIMES_CODEX_20261017.md)
and the [round-one review](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md),
under the [result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md), especially
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[checked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
and [volume without a gain](../../../../../avoid/20_volume_without_a_gain.md).
The gain over the review's stopping point is closure of its named
unbounded-time escape, with a stable reverse control.

## 1. The class and its closedness

Let \(\mathcal P\) be the nonzero finite even positive measures for which
\[
\int e^{-bu^2+izu}\,d\rho(u)
\quad\text{has only real zeros for every }b>0.
\tag{1}
\]
The primary source is [Newman, *Fourier transforms with only real zeros*,
Theorem 2, equations (1.5), (1.8)–(1.10) and (2.2), printed
pp. 246–248](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf).
The source class, Gaussian convolution and quartic tail comparison used
below are all present there. In particular it contains densities
\[
C e^{-d u^2}\prod_j(1+c_ju^2),\qquad
d>0,\quad c_j\ge0,\quad\sum_jc_j<\infty,
\tag{2}
\]
which is the unrenormalized subclass in (1.5).

The probability measures in \(\mathcal P\) are weakly closed. For fixed
\(b>0\) and \(|z|\le R\), the integrands in (1) are bounded by
\(e^{-bu^2+R|u|}\), whose tails vanish uniformly. Truncation and weak
convergence therefore give complex-compact convergence of these entire
transforms; equicontinuity follows from the same bound with one factor
\(|u|\). The limiting transform is nonzero at zero. Hurwitz preserves
zero-freeness off the real axis. This works for every \(b>0\).

## 2. Varying seeds and diverging heat

Let \(\mu_n\) be symmetric LP probability laws with
\[
M_n(h)=e^{a_nh^2}\prod_j(1+h^2/r_{nj}^2),\qquad
a_n\ge0,\quad\sum_jr_{nj}^{-2}<\infty.
\tag{3}
\]
As in Note 01, these are actual Laplace transforms, not merely formal
products. Suppose \(\lambda_n>0\),
\(Z_n=\int e^{\lambda_nu^2}\,d\mu_n(u)<\infty\), and let
\(\nu_n=T_{\lambda_n}\mu_n\).

Convolve \(\nu_n\) with a centered Gaussian of variance
\(1/(2\lambda_n)\). Completing the square gives its exact density
\[
\begin{split}
q_n(x)
&=\frac{\sqrt{\lambda_n/\pi}}{Z_n}
 e^{-\lambda_nx^2}M_n(2\lambda_nx)\\
&=C_n e^{-d_nx^2}\prod_j(1+c_{nj}x^2),\\
d_n&=\lambda_n-4a_n\lambda_n^2,\qquad
c_{nj}=4\lambda_n^2/r_{nj}^2.
\end{split}
\tag{4}
\]
For independent Rademacher seeds the equivalent formula is
\(q_n(x)=C_ne^{-\lambda_nx^2}\prod_j\cosh(2\lambda_nb_{nj}x)\).
There is no bound on seed complexity or on the changing amplitudes.

Integrability of the probability density in (4) forces \(d_n>0\), since
the product is at least one. Also \(\sum_jc_{nj}<\infty\) for each \(n\).
Thus (2) applies and \(q_n(x)\,dx\in\mathcal P\).

**Proposition.** If \(\lambda_n\to\infty\) and \(\nu_n\Rightarrow\nu\),
then \(\nu\in\mathcal P\).

**Proof.** The Gaussian added in (4) tends in probability to zero, so
\(q_n(x)\,dx\Rightarrow\nu\). Apply the weak closedness just proved.
\(\square\)

## 3. Theta and the stable Bessel control both fail

Apart from the degenerate law at zero and symmetric two-point laws,
Newman's classification says that
the densities in \(\mathcal P\) have the form
\[
K u^{2m}e^{-\alpha u^4-\beta u^2}
\prod_j\{(1+u^2/s_j^2)e^{-u^2/s_j^2}\},
\quad \alpha\ge0,\quad\sum_js_j^{-4}<\infty,
\tag{5}
\]
with the source's additional integrability conditions. Only a necessary
consequence of (5) is needed here. Since
\(\log(1+y)-y\ge-y^2/2\) for \(y\ge0\), every such density satisfies
\[
\rho(u)\ge K u^{2m}
\exp\{-(\alpha+\tfrac12\sum_js_j^{-4})u^4-\beta u^2\}.
\tag{6}
\]
This is Newman's (1.9)–(1.10), with explicit normalization of its product.

Theta's source has
\(\log\Phi(u)=-\pi e^{4u}+9u+O(1)\) as \(u\to\infty\), from its
first summand and an exponentially smaller positive remainder. The
Bessel source \(B(u)=e^{-2\pi\cosh4u}\) has the same leading
\(-\pi e^{4u}\) term. Both contradict the quartic lower bound (6).
They are continuous positive laws, so are not the two-point alternative.
The proposition excludes both as diverging-heat limits of the seeds (3).

The Bessel source has a real-zero transform by the classical Bessel
argument already checked in round one. Accordingly the exclusion tests
family expressiveness, not whether theta is stable. No new numerical
certificate is needed: all signs and tail comparisons are analytic.

A local consequence of (4) is also useful. In the squared source
coordinate \(r>0\), set \(W_n(r)=-\log q_n(\sqrt r)\). Then
\[
W_n''(r)=\sum_j\frac{c_{nj}^2}{(1+c_{nj}r)^2}\ge0,
\qquad
W_n'''(r)=-2\sum_j\frac{c_{nj}^3}{(1+c_{nj}r)^3}\le0.
\tag{7}
\]
The full class (5) retains \(W'''\le0\); a possible factor \(u^{2m}\)
adds \(-2m/r^3\). Thus this inequality also passes to positive smooth
limits by the proposition and classification. For Bessel it fails
immediately: \(2\pi\cosh(4\sqrt r)\) has a strictly positive third
derivative, as is seen from its positive power series. This is the same
classical obstruction in local coordinates, not a second result about RH.

## 4. What this does not close

Fixed Cardon multipliers \(G(iu)\) are not forward quadratic heat
weights. [Cardon's Theorem 1 and Lemma 1](https://mathdept.byu.edu/cardon/papers/FourierRealZeros.pdf)
include non-Gaussian limits of normalized Rademacher sums. For example,
\(S=\sum_{j\ge1}(c/j)\varepsilon_j\) converges in \(L^2\), and
\[
\log\mathbb E e^{hS}=\sum_j\log\cosh(ch/j)=ch\log h+O(h).
\]
Split at \(j=\lfloor ch\rfloor\): the initial sum is
\(ch\sum_{j\le ch}1/j+O(h)\), and the tail is \(O(h)\) using
\(\log\cosh x\le x^2/2\). At \(c=1/4\) this matches theta's leading
field-growth scale. This persists for a concrete nonconstant Cardon
multiplier: take \(G(z)=1-z^2\), so \(G(iu)=1+u^2\). If
\(K(h)=\log M(h)\), termwise differentiation gives
\(K'(h)=O(\log h)\), \(0\le K''(h)\le c^2\sum_jj^{-2}\), and
\[
M_G(h)=\frac{M(h)+M''(h)}{1+\mathbb ES^2},\qquad
\log M_G(h)=K(h)+O(\log\log h).
\]
Thus leading field growth alone cannot reject all fixed nonconstant
Cardon multipliers. No Bessel approximation for that family has been supplied.

General initially interacting networks are likewise outside the
independent-spin all-base-times theorem in Note 01. They must satisfy
the weak persistent-site condition, and this proposition closes their
diverging-heat-seed subclass when (3) and (4) apply. It does not exclude
all interacting infinitesimal arrays or all stable approximation schemes.
