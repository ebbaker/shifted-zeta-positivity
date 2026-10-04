# Actual prime error after trend removal and frequency localization

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Internal checks by agents using the inherited model configuration are not
independent specialist review.

The signed actual-prime upper bound in
[note 08](08_dyadic_shifted_correlations_20261003.md) remains unproved.
This continuation establishes three useful facts: the negative part of
that remainder has an unconditional quadratic bound; four explicit trends
in the Chebyshev error can be removed exactly before taking its norm; and
the outer additive frequencies already have the required variance bound.
The unresolved part is the signed central-frequency projection, or a
sufficient mean-square estimate for the fitted Chebyshev error. The
arithmetic estimates tested here do not close either target without RH.

Use the same \(a=1/4\), \(A=e^{-a}\), \(B=e^a\), normalized \(g\),
and zero-extended \(w(t)=t^{-1/2}g(-\log t)\). Write
\(E(t)=\psi(t)-t\), \(\mathcal V(X)=\int_X^{2X}V(x)^2dx\), and keep
the complete active coordinate band \((AX,2BX)\) throughout. All
asymptotic constants below may depend on this fixed probe.

## 1. A quadratic bound for the negative arithmetic remainder

Note 08 isolated the exact singular-series main and actual error:

\[
\mathcal V(X)=\mathcal D(X)+\mathcal C_{\rm SS}(X)+\mathcal R(X).
\tag{1}
\]

The classical effective PNT supplies more than the leading diagonal
asymptotic. For example,
[Platt and Trudgian, Theorem 1 and Corollary 1](https://arxiv.org/pdf/1809.03134)
give unconditional exponentially decaying relative errors in \(\psi\)
and \(\theta\) on the square-root-logarithm scale. We only use the weaker
consequence \(\theta(t)=t+o(t/\log t)\).
Partial summation and the \(O(\sqrt t\log^2t)\) higher-power contribution
give

\[
\sum_{n\le t}\Lambda(n)^2=t\log t-t+o(t).
\]

Indeed the prime contribution is
\(\theta(t)\log t-\int_2^t\theta(u)du/u\); its endpoint error is
\(o(t)\) and its integrated error is also \(o(t)\). The derivative of
the cumulative main \(t\log t-t\) is \(\log t\), with no additional
constant subtraction.

The diagonal weight vanishes at \(AX,2BX\), has derivative \(O_g(1)\),
and total variation \(O_g(X)\). Integrating the preceding error against
it therefore gives, uniformly for real \(X\to\infty\),

\[
\mathcal D(X)=X^2\left[\frac32\log X+C_D\right]+o_g(X^2),
\qquad C_D=2\log2-\frac34.
\tag{2}
\]

With \(c_F\) from note 08, put

\[
\beta_g=C_D+2c_F-3/2.
\]

The unconditional singular-series calculation now yields

\[
\boxed{\mathcal R(X)=\mathcal V(X)-\beta_gX^2+o_g(X^2).}
\tag{3}
\]

Since \(\mathcal V\ge0\), it follows that
\(\mathcal R(X)_-=\max(-\mathcal R(X),0)=O_g(X^2)\).
Only its positive side remains uncontrolled at the required scale. This
is an actual arithmetic consequence, but it supplies no upper estimate
for \(\mathcal V\).

There is a useful differentiation-free formula for the coefficient.
Let \(C_w(q)=\int w(t)w(t+q)dt\), \(R_0=B-A<1\), and

\[
K_C=\log R_0+\int_0^{R_0}\frac{C_w(q)-1}{q}dq.
\]

Then \(C_w(0)=1\), \(C_w'(0)=0\), and integration by parts gives

\[
\beta_g=\frac32[-\gamma-\log(2\pi)-K_C].
\tag{4}
\]

For \(\widehat w(\xi)=\int w(t)e^{-2\pi i\xi t}dt\), this is also

\[
\beta_g=\frac32\int_{\mathbb R}|\widehat w(\xi)|^2\log|\xi|\,d\xi.
\tag{5}
\]

One justified route to (5) inserts \(e^{-\eta q}\) and uses
\(\int_0^\infty e^{-\eta q}[\cos(bq)-e^{-q}]dq/q
=\log(1+\eta)-\tfrac12\log(\eta^2+b^2)\), then lets \(\eta\downarrow0\).
The constant \(\int_0^\infty[e^{-q}-\mathbf1_{q\le1}]dq/q=-\gamma\)
fixes the normalization, consistently with the
[cosine-integral identities](https://dlmf.nist.gov/6.2).
The zero \(\widehat w(0)=0\) and sixth-power decay justify the limiting
spectral integral. Absolute Fubini on the undamped cosine-over-\(q\)
integral would not be legitimate.

Floating calculations give \(\beta_g\approx2.20041004891337\); no
outward enclosure of that decimal is claimed. The quadratic negative-part
theorem does not require a numerical sign determination of \(\beta_g\).

## 2. Exact removal of four Chebyshev error trends

For \(1\le s\le2\), put \(\varepsilon_X(u)=E(Xu)\) on
\(\mathcal I=(A,2B)\). Stieltjes integration by parts has zero boundary
terms because the complete kernel vanishes at both coordinate endpoints:

\[
\boxed{V(Xs)=T\varepsilon_X(s),\qquad
Tf(s)=-\frac1s\int_A^{2B}f(u)w'(u/s)du.}
\tag{6}
\]

Consequently

\[
\mathcal V(X)=X\|T\varepsilon_X\|_{L^2(1,2)}^2
=X\iint_{\mathcal I^2}\varepsilon_X(u)\varepsilon_X(v)
\mathcal K_E(u,v)du\,dv,
\]
\[
\mathcal K_E(u,v)=\int_1^2s^{-2}w'(u/s)w'(v/s)ds.
\tag{7}
\]

This is a positive Gram kernel, retaining all signed cross terms.
The derivative norm is
\(\|w'\|_2^2=\int_{-a}^ae^{2v}|g'(v)+g(v)/2|^2dv\), rather than the
unweighted derivative norm from earlier notes.

The three preparation moments are

\[
\int w(t)dt=\int t^{-1/2}w(t)dt=\int t^{-1}w(t)dt=0.
\]

They imply the four exact identities

\[
T1=Tu=T\sqrt u=T\log u=0.
\tag{8}
\]

For example, integration by parts pairs \(\sqrt u\) with
\(t^{-1/2}w(t)\), and \(\log u\) with \(t^{-1}w(t)\). More generally,
with the minus-transform convention \(G(z)=\int g(v)e^{-zv}dv\),

\[
T(u^z)(s)=z s^zG(z-1/2).
\tag{9}
\]

The multiplier has a double zero at \(z=0\) and zeros at \(1/2,1\).
There are further oscillatory null modes at the imaginary zeros of the
Bessel factor. We only claim that the explicit four-dimensional span
\(\mathcal N=\operatorname{span}\{1,u,\sqrt u,\log u\}\) lies in
\(\ker T\); it is not the whole nullspace.

Let \(\Pi\) be the ordinary \(L^2(\mathcal I)\) orthogonal projection
onto \(\mathcal N\). Its fixed Gram matrix is positive definite because
these four functions are linearly independent. It has no unknown prime
or Sonin inverse in its definition. Equation (8) gives exactly
\(T\varepsilon_X=T(I-\Pi)\varepsilon_X\).
The squared Hilbert--Schmidt norm is

\[
\|T\|_{\rm HS}^2
=\int_1^2\int_A^{2B}s^{-2}|w'(u/s)|^2du\,ds
=(\log2)\|w'\|_2^2.
\tag{10}
\]

Thus, defining the actual fitted error in physical coordinates by

\[
\mathcal H(X)=\inf_{b_0,b_1,b_2,b_3\in\mathbb R}
\int_{AX}^{2BX}|E(t)-b_0-b_1t-b_2\sqrt t-b_3\log t|^2dt,
\]

we have the unconditional comparison

\[
\boxed{\mathcal V(X)\le(\log2)\|w'\|_2^2\mathcal H(X).}
\tag{11}
\]

The scale conversion is \(\mathcal H(X)=X\|(I-\Pi)\varepsilon_X\|_2^2\).
The coefficients may vary with \(X\), since only their annihilation by
the fixed kernel is used. A concrete sufficient target is therefore

\[
\mathcal H(X)\le C_gX^2\log(2X)
\quad\text{for every sufficiently large real }X.
\tag{12}
\]

This improves the earlier raw Chebyshev-error comparison by removing
known harmless directions. It is still stronger as a direct norm estimate
than controlling the exact Gram projection (7).

## 3. What the fitted error comparison does and does not prove

Under RH,
[Brent, Platt, and Trudgian, Theorem 1](https://arxiv.org/pdf/2008.06140)
prove \(\int_U^{2U}E(t)^2dt\le0.8603U^2\) for sufficiently large \(U\).
Two dyadic intervals starting at \(AX\) cover \((AX,2BX)\), because
\(B<2A\). Hence RH gives the stronger \(\mathcal H(X)=O(X^2)\).
Conversely (12), through (11) and note 06, implies RH. Thus (12) is an
RH-equivalent obligation, not a known unconditional mean-square theorem.
The unconditional lower bound in that paper cannot provide this upper
bound and is not substituted for it.

Nor does finite-dimensional trend removal turn PNT alone into (12).
Use the sparse discrete PNT countermodel already constructed in note 06:
\(\widetilde\psi(t)=t+\delta\operatorname{Re}(t^{\beta+i\gamma}/
(\beta+i\gamma))+O(\log t)\), where \(1/2<\beta<1\) and \(\gamma\ne0\).
On \(\mathcal I\), its error is a rotating linear combination of
\(u^\beta\cos(\gamma\log u)\) and
\(u^\beta\sin(\gamma\log u)\), multiplied by \(X^\beta\), with
\(O(\log X)\) tracking error. Neither combination can lie in
\(\mathcal N\): in the variable \(\log u\) their exponents are distinct
from \(0,1/2,1\), including the repeated zero exponent for \(\log u\).
The two projected functions have a strictly positive two-dimensional
Gram matrix. Therefore, uniformly in the rotating phase,

\[
\widetilde{\mathcal H}(X)\asymp X^{1+2\beta},
\tag{13}
\]

which exceeds the target. This is a countermodel to generic PNT and trend
removal, not a counterexample involving actual Euler primes.

## 4. Additive Fourier formulation with complete caps

Put \(e(z)=e^{2\pi iz}\) and let \(\mathcal J_X\) contain every integer
\(AX<n<2BX\), including those with zero von Mangoldt weight. Define

\[
A_X(\alpha)=\sum_{n\in\mathcal J_X}(\Lambda(n)-1)e(n\alpha),
\qquad f_X(\xi)=A_X(\xi/X).
\]

For \(x\in[X,2X]\) the complete lattice kernel is

\[
K_x(\alpha)=\sum_{n\in\mathbb Z}w(n/x)e(-n\alpha)
=x\sum_{k\in\mathbb Z}\widehat w(x(\alpha+k)).
\tag{14}
\]

Poisson summation applies because \(w\) is compactly supported, has
vanishing derivatives through order four at the endpoints, and its sixth
distributional derivative is a finite measure. In particular
\(|\widehat w(\xi)|\le C_g(1+|\xi|)^{-6}\).
The finite Fourier identity is

\[
V(x)=\int_{-1/2}^{1/2}A_X(\alpha)K_x(\alpha)d\alpha
+\sum_{n\in\mathbb Z}w(n/x).
\tag{15}
\]

All integers in the coordinate band are included in \(A_X\); replacing
it by a sum over primes only would invalidate this centering.
The lattice density term is \(O_g(X^{-5})\), since \(\widehat w(0)=0\).
The noncentral Poisson aliases have kernel supremum \(O_g(X^{-5})\).
Also \(\sum_{n\in\mathcal J_X}(\Lambda(n)-1)^2=O(X\log(2X))\),
by the unconditional diagonal count and the number of integers.
Cauchy--Schwarz therefore bounds their paired amplitude by
\(O_g(X^{-9/2}\sqrt{\log(2X)})\). Changing variables \(\xi=X\alpha\)
gives the uniform identity

\[
\boxed{V(Xs)=s\int_{-X/2}^{X/2}f_X(\xi)\widehat w(s\xi)d\xi
+O_g(X^{-9/2}\sqrt{\log(2X)}).}
\tag{16}
\]

The complex integral is real by conjugate symmetry. Keeping the common
complete integer band preserves both caps in this formulation.

## 5. The outer frequencies are already controlled unconditionally

Parseval on the one-period interval gives exactly

\[
\int_{-X/2}^{X/2}|f_X(\xi)|^2d\xi
=X\sum_{n\in\mathcal J_X}(\Lambda(n)-1)^2
=O(X^2\log(2X)).
\tag{17}
\]

For \(1\le L<X/2\), split the integral in (16) at \(|\xi|=L\),
writing its central part as
\(P_{X,L}(s)=s\int_{-L}^Lf_X(\xi)\widehat w(s\xi)d\xi\) and its
outer part as \(U_{X,L}\). Sixth-power decay and Cauchy--Schwarz give

\[
|U_{X,L}(s)|^2\le C_gX^2\log(2X)L^{-11},\qquad
X\|U_{X,L}\|_{L^2(1,2)}^2
\le C_gX^3\log(2X)L^{-11}.
\tag{18}
\]

Taking \(L=X^{1/11}\), for sufficiently large \(X\), proves an
unconditional \(O_g(X^2\log(2X))\) bound for the entire outer piece.
The aliases are smaller. The triangle inequality, in both directions,
therefore makes the original target equivalent to the central estimate

\[
\boxed{\int_1^2|P_{X,X^{1/11}}(s)|^2ds
\le C_gX\log(2X).}
\tag{19}
\]

In original additive frequencies the unproved band is
\(|\alpha|\le X^{-10/11}\). Its kernel is naturally concentrated at
\(|\alpha|\asymp1/X\). The exact zero \(\widehat w(0)=0\) removes the
constant density but does not remove this neighborhood.

The central quadratic kernel is explicitly

\[
\mathcal K_L(\xi,\eta)=\int_1^2s^2\widehat w(s\xi)
\overline{\widehat w(s\eta)}ds.
\]

It is positive semidefinite. Its off-diagonal frequency entries and the
complex phases of \(f_X\) remain part of (19). Estimating them separately
or using global Parseval as a bound for the full central projection gives
only \(O(X^3\log X)\) for the variance. The missing factor of \(X\)
must come from arithmetic information in this central projection.

## 6. Tested arithmetic inputs and the next obligation

The effective PNT above, applied by Stieltjes partial summation on the
complete band, gives
\(|f_X(\xi)|\le C_gX e^{-c_g\sqrt{\log X}}(1+|\xi|)
+O_g(1+|\xi|)\), after absorbing logarithmic factors into \(c_g>0\).
Integrating against \(\widehat w(s\xi)\) yields the actual unconditional
bound

\[
\mathcal V(X)=O_g(X^3e^{-2c_g\sqrt{\log X}}).
\tag{20}
\]

This remains larger than \(X^2\log X\) by a power-sized factor. The
zero-free input improves relative error but does not supply central
square-root cancellation. The almost-all-shift errors audited in note 08
also remain insufficient when summed absolutely. The conditional
Chebyshev mean-square theorem reaches (12), but assumes RH.

The classical prime exponential-sum estimate recorded in the author-hosted
[Montgomery--Vaughan draft, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf)
has size
\((Nq^{-1/2}+N^{4/5}+N^{1/2}q^{1/2})(\log N)^{5/2}\), when
\((a_1,q)=1\) and \(|\alpha-a_1/q|\le q^{-2}\).
At \(\alpha\asymp1/X\), using \(q=1\) retains the \(X\) term; a
denominator of order \(X\) retains the last term of that size. This
estimate for the uncentered sum supplies no square-root estimate for the
centered quantity in (19). This is an input test, not a claim that all
circle-method approaches fail.

A coefficient-only improvement is also impossible at this scale. Choose
a fixed \(\xi_0\ne0\) with \(\widehat w(\xi_0)\ne0\), and artificial
complex coefficients \(c_n=e(-\xi_0n/X)\) on the complete integer band.
Their squared norm is \(\asymp X\), but Poisson summation gives

\[
\sum_{n\in\mathcal J_X}c_nw(n/(Xs))
=Xs\widehat w(s\xi_0)+O_g(X^{-5}),
\]

and its dyadic squared norm is \(\asymp X^3\). Thus a Parseval or large
sieve estimate depending only on \(\sum|c_n|^2\) cannot produce the
needed bound. These coefficients are not actual primes; the example
isolates the missing arithmetic information rather than refuting the
prime target.

The exact physical projection is more selective than an absolute norm
of the centered exponential sum. In its continuous-density version,
partial summation of that sum exposes endpoint terms involving
\(E(AX)\) and \(E(2BX)\). The full inverse transform pairs them with
\(w(A/s)=w(2B/s)=0\). A generic positive frequency weight need not
annihilate those harmless endpoint terms. Such a stronger norm must not
be treated as equivalent to (19) without an additional argument.

The next useful arithmetic input is thus either the signed central
covariance estimate (19), the fitted physical error bound (12), or the
sharper exact Gram estimate (7). The outer frequencies and the negative
part of \(\mathcal R\) need no further global assumption. None of the
tested inputs controls the remaining central actual-prime contribution
unconditionally.

The [actual remainder diagnostic](../../numerics/selective_loss_arithmetic_remainder_20261003/README.md)
retains every shift and both caps through small noninteger shells ending
at \(X=501.125\). The actual remainder takes both signs. It also checks
the four-trend projection by stable numerical least squares. These are
floating checks, not a growth estimate or interval certificate. See the
[internal review](../../reviews/SELECTIVE_LOSS_ACTUAL_ERROR_REVIEW_20261003.md).
No manuscript revision, snapshot, commit, or push is part of this work.
