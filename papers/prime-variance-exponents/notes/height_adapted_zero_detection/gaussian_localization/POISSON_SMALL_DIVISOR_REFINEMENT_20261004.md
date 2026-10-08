# A larger removable divisor range for Gaussian zero detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and internal cross-review are not independent
specialist refereeing or formal proof verification.
Repository base: `ef02c696bee11362286fe31c237fc169329c1812`, with existing
working-tree changes preserved.

This continuation proves that the Gaussian arithmetic reduction can remove
all divisors through \(e^{77k/5}=e^{15.4k}\), replacing \(e^{15k}\),
with the same detector error allowance. It assumes no Möbius cancellation.
A complex ray rotation handles both signs and the entire Poisson series;
no asymptotic saddle formula or uncharged transition range is used.
The retained signed arithmetic inequality remains open. No new zero-free
box or actual-zero certificate follows from this refinement alone.

## Parameters and the improved deletion theorem

Use the definitions of the
[finite Gaussian Möbius reduction](FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md):

\[
b=3/4,\quad T=|t|\ge100,\quad
g_k(y)=\frac{e^{-y^2/(4k)}}{\sqrt{4\pi k}},\quad
W_{k,t}(x)=x^{-b-it}g_k(20k-\log x),
\]
\[
\Phi_{k,t}(1)=\int_0^\infty W_{k,t}(x)\,dx,
\quad \eta_N=(8e)^{-N},\quad
k=4(N+1),4(N+2),\ldots,8N.
\tag{1}
\]

As before, \(N\) is an integer at least ten that is at least the prescribed
radius-three guard-count bound throughout the carrier band. In particular
\(T+1<e^N\). The zero-detection theorem, multiplicities, carrier coverage,
fixed-line remainder, and sample set remain those of the
[explicit finite-window note](EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md).

**Effective project deduction.** Put \(D_k=e^{77k/5}\). Then

\[
\boxed{
\sum_{d\le D_k}\log d\,
\left|\sum_{r\ge1}W_{k,t}(dr)-\frac{\Phi_{k,t}(1)}d\right|
<kT^{5/2}e^{-23k/16}<\eta_N/16.}
\tag{2}
\]

The first bound holds for \(T\ge100\), \(k\ge44\), without the
guard-count hypothesis. The second uses the sample and height budget.
Real cutoffs and literal integer inequalities are retained. The factor
\(|\mu(d)|\le1\) may be inserted without increasing the error.

## Exact Fourier contour bounds

Let \(w_k(x)=|W_{k,t}(x)|=x^{-b}g_k(20k-\log x)\) and use Fourier
convention \(\widehat W(\xi)=\int W(x)e^{-2\pi i\xi x}\,dx\).
The zero extension of \(W\) is Schwartz, flat at zero, so Poisson gives

\[
\sum_{r\ge1}W(dr)-\Phi(1)/d
=\frac1d\sum_{m\ne0}\widehat W(m/d).
\tag{3}
\]

The original real-integral Poisson series is absolutely convergent.
For a nonzero integer \(m\), rotate its Fourier integral to the ray
\(z=x e^{i\varphi}\), where
\(\varphi=-\operatorname{sgn}(m)\theta\), \(\theta=1/T\).
Use the principal logarithm in \(W(z)\). Along this ray,

\[
|W(xe^{i\varphi})e^{i\varphi}|
=w_k(x)e^{t\varphi+\varphi^2/(4k)},\qquad
|e^{-2\pi i(m/d)xe^{i\varphi}}|
=e^{-2\pi |m|\sin\theta\,x/d}.
\tag{4}
\]

The joining arcs vanish at zero and infinity. Throughout the chosen
sector the Fourier exponential has modulus at most one, and the
remaining arc bound is a constant times
\(R^{1-b}\exp[-(20k-\log R)^2/(4k)]\), which tends to zero at
both endpoints. The logarithm branch is never crossed. This justifies
the rotation for either sign of \(m\) and either sign of \(t\).

Define \(E=e^{T\theta+\theta^2/(4k)}\) and
\(a=2\pi\sin\theta\). Elementary rational bounds give

\[
E<3,\qquad a>6/T.
\tag{5}
\]

For example \(\pi>25/8\),
\(\sin\theta\ge\theta(1-\theta^2/6)\), and \(T\ge100\)
prove the latter. For the former, use \(e<11/4\),
\(\theta^2/(4k)\le1/1760000\), and
\(e^u\le(1-u)^{-1}\) for \(0\le u<1\).
Consequently

\[
|\widehat W(m/d)|\le E\int_0^\infty
                       w_k(x)e^{-a|m|x/d}\,dx.
\]

Tonelli applied to this positive majorant sums all nonzero modes:

\[
\left|\sum_{r\ge1}W(dr)-\frac{\Phi(1)}d\right|
\le\frac{2E}{d}\int_0^\infty
          \frac{w_k(x)}{e^{ax/d}-1}\,dx.
\tag{6}
\]

The geometric denominator has already paid for the entire mode series;
no additional zeta factor is needed in the next estimate.

Contour deformation for logarithmic Gaussian transforms has classical
precedents; see [Miles, Section 2](https://arxiv.org/html/1803.05878).
The present twisted bound and detector budget are derived explicitly
here. No broader novelty claim is made, and no unproved transform
approximation from that literature is imported.

## A fractional moment that improves the cutoff

For \(p=5/2\) and every \(u>0\),

\[
\frac{u^p}{e^u-1}<2.
\tag{7}
\]

For \(u\le1\), use \(e^u-1\ge u\). For \(u>1\),
\(e^u-1>e^u/2\), and the maximum of \(u^pe^{-u}\) occurs at
\(u=p\), with value \((p/e)^p<1\), since \(e>5/2\).
Equivalently, the degree-three positive Taylor lower bound for \(e^u-1\)
gives a direct algebraic proof; the replay checks that proof too.

The Gaussian fractional moment in (6) is exact:

\[
J_p=\int_0^\infty w_k(x)x^{-p}\,dx
=e^{k(1-b-p)^2+20k(1-b-p)}=e^{-639k/16}.
\tag{8}
\]

Thus each lattice discrepancy is below
\((4E/a^p)d^{p-1}J_p\). Since \(D_k>100\), the increasing-power
integral bound gives

\[
\sum_{d\le D_k}d^{p-1}\log d
\le\frac{(D_k+1)^p}{p}\log D_k
<\frac{11}{10p}D_k^p\log D_k.
\tag{9}
\]

Here \((1+1/D_k)^p\le(101/100)^3<11/10\).
Also \(\sqrt6>12/5\), so
\(4E/a^p<12T^p/6^p<(5/36)T^p\).
With \(\log D_k=77k/5\), (8)--(9) therefore give

\[
\sum_{d\le D_k}\log d\,|\text{lattice discrepancy}|
<\frac{847}{900}kT^{5/2}e^{-23k/16}
<kT^{5/2}e^{-23k/16},
\tag{10}
\]

because \(p(77/5)-639/16=-23/16\).
This proves the first part of (2) with an explicit strict margin.

## All prescribed samples fit the detector allowance

Use \(T^{5/2}<e^{5N/2}\) and \(\log(8e)<31/10\).
The ratio of the last expression in (10) to \(\eta_N\) is at most

\[
k e^{(28/5)N-23k/16}.
\]

It decreases for \(k\ge44\), so the least sample \(k=4(N+1)\)
is worst. The resulting bound is

\[
4(N+1)e^{-3N/20-23/4}
\le44e^{-29/4}<1/16,
\tag{11}
\]

where the first expression decreases for \(N\ge10\), since its
logarithmic derivative is \(1/(N+1)-3/20<0\).
For the base inequality,
\(e^{29/4}> (5/2)^7(5/4)=390625/512>704\).
All finite-budget decisions thus reduce to exact rational inequalities
and elementary positive-series bounds.

## The refined finite arithmetic target

Keep \(B_k=e^{26k}\), and replace only the divisor cutoff. Define

\[
L_{D_k}=\sum_{d\le D_k}\mu(d)\log d/d,
\]
\[
\mathcal G^{\rm new}_{k,t}=
-\sum_{\substack{d>D_k,r\ge1\\dr\le B_k}}
       \mu(d)\log d\,W_{k,t}(dr)
-\Phi_{k,t}(1)(1+L_{D_k}).
\tag{12}
\]

The full \(\Lambda\) identity, signs, continuum, and weak product cap
are unchanged. The retained cofactor range is now strictly

\[
\boxed{r<e^{53k/5}=e^{10.6k},\quad D_k<d\le B_k/r.}
\tag{13}
\]

The saved product-tail bound \(250k^{3/2}e^{-5k/2}\), fixed-line
remainder, and optional frequency-tail bound \(80k e^{-5k/2}\)
still hold. Their divisor-coefficient majorants were independent of
the lower divisor cutoff. No smaller lower product range is discarded.
The optional centered frequency band remains the continuous interval
\([-3,3]\), with the new cutoff inside its finite Dirichlet polynomial.

The continuum stays explicit and affordable. Since
\(|L_{D_k}|\le(77k/5)(1+77k/5)\),

\[
|\Phi(1)(1+L_{D_k})|
\le254k^2e^{-k(T^2-81/16)}<\eta_N/16.
\tag{14}
\]

For \(k\ge44\), \(T\ge100\), the inequality follows, for example,
from \(254k^2<e^k\), \(\eta_N>e^{-k}\), and
\(T^2-81/16-2>9992\). Retaining the term gives an exact identity
even though its magnitude is far below the allowance.

As before, \(|\mathcal G^{\rm new}_{k,t}|\le\eta_N/4\) for every
covered carrier and every prescribed sample would exclude the candidate
box \(3/4\le\beta<1\). The same statement holds for its band-limited
version. The existing proof pays three omitted sectors, and the optional
frequency sector, each strictly below \(\eta_N/16\). Only the small-divisor
sector has been improved here. Neither retained arithmetic inequality is
proved by this note.

## Scope of the gain and the next arithmetic attempt

The removable divisor range grows by \(e^{2k/5}\); the cofactor ceiling
falls by the same factor. At the existing illustrative \(N=41\),
\(168\le k\le328\), the logarithmic cofactor ceilings change from
\([1848,3608]\) to \([1780.8,3476.8]\). These are exact scale
calculations, not actual prime computations or new zero exclusions.

The gain is modest in logarithmic scale. In the continuous-order version
of (6), the leading budget exponent is
\(p^2+p(\alpha-81/4)+81/16+\log(8e)/4\).
Optimizing this particular absolute envelope suggests the limiting
cutoff coefficient

\[
\alpha<\frac{81}{4}
-2\sqrt{\frac{81}{16}+\frac{\log(8e)}4}
\approx15.41994.
\tag{15}
\]

This is a scale diagnostic for this method with \(T<e^N\) and
\(k\sim4N\). It is not an impossibility result for larger cutoffs,
sharper count information, cancellation between modes, or another contour.
The clean coefficient 15.4 is enough to stop this bounded optimization
and move to the signed estimate.

The [signed continuation](SIGNED_DYADIC_ATTEMPT_20261004.md) makes that
estimate explicit, including every terminal block. It identifies a
sufficient finite twisted-Möbius condition and tests ordinary modulus
and mean-square approaches; the needed signed cancellation remains open.
The [replay](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
checks exact constants, cutoff algebra, and source provenance. The
[internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/POISSON_AND_SIGNED_REVIEW_20261004.md)
records analytical checks and their limits. No manuscript snapshot,
commit, or actual-zero certificate is created.
