# Positive three-dimensional theta lift and its nonlocal generator

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available in this session and are not inferred. These are internal checks,
not independent mathematical review.

This initial scout for program 12 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
proves that the genuine theta state has a smooth strictly positive radial
three-dimensional inverse marginal throughout \(0\le t\le1/20\).
Its exact radial evolution is nonlocal and not positivity-preserving on the
whole positive cone. The lift therefore provides a concrete geometric
representation, while a separate smooth positive radial control shows why
radial positivity alone cannot exclude a positive-time double zero.

## 1. Exact state, projection, and generator

Put \(m_t(u)=e^{tu^2}\Phi_e(u)\). Define, for \(r>0\),
\[
 R_t(r)=-\frac{m_t'(r)}{2\pi r},\qquad
 R_t(0)=-\frac{m_t''(0)}{2\pi}.
\tag{1}
\]
Even smoothness of \(m_t\) makes \(R_t(|v|)\) a smooth radial function
on \(\mathbb R^3\). Its axis marginal is exactly
\[
 \int_{\mathbb R^2}R_t(\sqrt{u^2+|v_\perp|^2})\,dv_\perp
 =2\pi\int_{|u|}^\infty R_t(r)r\,dr=m_t(u),
\tag{2}
\]
using the vanishing endpoint at infinity. The genuine Fourier observation is
\[
 H_t(z)=\tfrac12\int_{\mathbb R^3}e^{izv_1}R_t(|v|)\,dv
 =2\pi\int_0^\infty R_t(r)r^2\frac{\sin(zr)}{zr}\,dr.
\tag{3}
\]
At \(zr=0\), the quotient means its entire limiting value. This is the
dimension-three angular Bessel average. More generally the normalized
angular kernel is
\(\Gamma(d/2)(2/s)^{d/2-1}J_{d/2-1}(s)\); its positive angular
integral requires \(d>1\), as follows from
[DLMF 10.9.4](https://dlmf.nist.gov/10.9.E4). No fractional lattice is
introduced here.

Directly conjugating spectral multiplication through (2) gives
\[
 \partial_tR_t=\mathcal GR_t,
 \quad (\mathcal GR)(r)=r^2R(r)-2\int_r^\infty R(s)s\,ds,
 \quad R_t=e^{tr^2}\left(R_0-\frac t\pi\Phi_e\right).
\tag{4}
\]
Thus \(\mathcal P\mathcal G=-\partial_z^2\mathcal P\), where
\(\mathcal P\) is the Fourier readout (3). The entire nonlocal correction
is necessary. Ordinary radial multiplication \(r^2R\) would yield an
additional transverse second-moment term in (2). Ordinary three-dimensional
diffusion instead projects to \(\partial_tm=\partial_u^2m\), whose
Fourier equation is \(H_t{}_t=-z^2H_t\), a different evolution.

A convenient invariant class for (4) consists of radial smooth functions
whose derivatives decay faster than every fixed Gaussian and exponential,
and which are even smooth at the origin. The theta states belong to this
class for each bounded time interval. On this class every integral and
parameter derivative in (1)–(4) converges. The explicit formula defines the
genuine flow; no bounded semigroup on an ordinary radial \(L^2\) space is
claimed.

## 2. An elementary positivity proof in the required time range

The key criterion is
\[
 R_t(r)>0\quad\Longleftrightarrow\quad
 -\frac{\Phi'(r)}{\Phi(r)}>2tr\quad(r>0).
\tag{5}
\]
We verify it with conservative elementary bounds, rather than inferring it
from numerical plots. Set \(a_n=\pi n^2e^{4r}\). The exact summand and its
first two derivatives are
\[
 \phi_n=e^r(2a_n^2-3a_n)e^{-a_n},
\]
\[
 \phi_n'=-e^ra_ne^{-a_n}(8a_n^2-30a_n+15),
\]
\[
 \phi_n''=e^re^{-a_n}
 (32a_n^4-224a_n^3+330a_n^2-75a_n).
\tag{6}
\]
Termwise differentiation is justified by theta decay.

On \(0\le r\le1/100\), \(a_1\in[3.14,3.28]\). For
\(q(a)=32a^3-224a^2+330a-75\), its derivative
\(96a^2-448a+330\) is negative throughout this interval: it is convex,
and both endpoint values are negative. Also \(q(3.14)<-250\). Hence
the first second-derivative summand satisfies
\[
 e^{-a_1}a_1q(a_1)<-750/27<-27,
\]
where \(e^{3.28}<27\). The remaining second-derivative summands have the
upper bound
\[
 \sum_{n\ge2}(32a_n^4+330a_n^2)e^{-a_n}
 \le\sum_{n\ge2}(32(3n^2)^4+330(3n^2)^2)e^{-3n^2}<4.5.
\tag{7}
\]
Here \(a^ke^{-a}\) decreases for \(a\ge k\). The ratio of successive
terms in either positive series is bounded by
\((3/2)^8e^{-15}<8\cdot10^{-6}\), and the two first terms total less
than \(4.4\). Therefore \(\Phi''(r)<-20\) on this interval.

The theta functional equation gives \(\Phi'(0)=0\). A crude independent
bound is \(\Phi(0)<1\): drop the negative summand and use
\(\pi<22/7\), \(\pi>3\),
\(2(22/7)^2\sum n^4e^{-3n^2}<1\). More explicitly, its first term is
less than \(1/20\), its second term less than \(1/10000\), and the
successive ratio from the second term onward is less than
\((3/2)^4e^{-15}<2\cdot10^{-6}\). The resulting geometric upper bound,
multiplied by \(2(22/7)^2\), is less than one. Consequently, on
\(0<r\le1/100\),
\[
 -\Phi'(r)\ge20r,\qquad 0<\Phi(r)\le\Phi(0)<1,
 \qquad -\Phi'/\Phi>20r>2tr.
\tag{8}
\]

For \(r\ge1/100\), every \(a_n\) exceeds
\(3.14(1+4/100)=3.2656\), beyond the positive root of
\(8a^2-30a+15\). Each summand is decreasing and has logarithmic decay
\[
 \lambda(a)=-\phi_n'/\phi_n
 =\frac{8a^2-30a+15}{2a-3}.
\]
This function is increasing, since its derivative numerator is
\(16a^2-48a+60>0\). Direct rational evaluation at \(3.2656\) gives
\(\lambda>3/5\). For \(1/100\le r\le1\), the weighted average
\(-\Phi'/\Phi\) is therefore greater than \(3/5>r/10\).
For \(r\ge1\), \(a_n\ge\pi e^4>8\), and
\(\lambda(a_n)\ge2a_n\ge2\pi e^{4r}>r/10\). This proves (5) for
all \(r>0\) and \(0\le t\le1/20\).

At the center,
\[
 R_t(0)=-\frac{\Phi''(0)+2t\Phi(0)}{2\pi}
 >\frac{20-1/10}{2\pi}>0.
\tag{9}
\]
This explicitly resolves the removable \(1/r\) singularity and establishes
strict positivity of the whole genuine radial density in the requested
range. The bounds are deliberately loose; they are not an optimal
positivity-time threshold.

The replay script verifies the polynomial inequalities and the displayed
exponential/geometric constants with exact rational Taylor bounds. For
\(x\ge0\), its lower bound is \(\sum_{k=0}^N x^k/k!\); the omitted
tail is bounded by the first omitted term divided by
\(1-x/(N+2)\), for \(N+2>x\). Thus these constant checks do not depend
on floating-point transcendental values. The sampled theta values in the
record remain exploratory floating-point diagnostics.

## 3. Positivity of the theta trajectory is not cone preservation

For a positive compactly supported radial \(R\) that vanishes on an
interior interval below its support, (4) gives
\(\mathcal GR(r)=-2\int_r^\infty R(s)s\,ds<0\) there.
Thus \(\mathcal G\) fails the infinitesimal positivity test on the full
positive cone. The trajectory positivity just proved is a property of the
theta input and the stated time range, not a positive radial Markov
semigroup or positive selfadjoint factorization.

There is also a direct visibility control. Let \(\sigma\) be uniform
probability measure on the unit sphere in \(\mathbb R^3\), and let \(B\)
be any smooth nonnegative radial probability bump supported in \(|v|<1/2\).
Then \(R_*\), the density of \(\sigma*\sigma*B\), is smooth,
nonnegative, compactly supported and radial. Its characteristic function
on an axis is
\[
 \widehat R_*(x)=\left(\frac{\sin x}{x}\right)^2\widehat B(x).
\tag{10}
\]
At \(x=\pi\), \(\widehat B(\pi)>0\), because
\(|v_1|<1/2\) implies \(\cos(\pi v_1)>0\) throughout the support.
Thus (10) has an exact double zero there.

Let \(m_*\) be its even axis marginal and choose any \(T>0\). Set
\(m_0=e^{-Tu^2}m_*\). The inverse radial marginal
\(R_0=-m_0'/(2\pi r)\) is smooth and nonnegative, since
\(m_*'=-2\pi rR_*\le0\). For every \(0\le t\le T\),
\(m_t=e^{(t-T)u^2}m_*\) still has a nonnegative smooth radial inverse.
At \(T\), its Fourier observable has the double zero (10).
All integrals converge for all finite parameters because of compact support.
This is a counterexample to a universal inference from positive smooth
radial lift to joint nonvanishing. It is not a strictly positive full theta
kernel and makes no assertion about an all-real threshold.

The manuscript's positive decreasing kernel separately supplies a generic
positive-threshold control; its radial positivity interval would need its
own check. The genuine adjacent packet and complete twisted joint-zero
controls remain required for an arithmetic refinement. Their existence
does not invalidate the theta-specific positivity theorem above.

## 4. Tail, jets, normalizer, and next task

For \(r\ge1\), the same theta-series estimates give, conservatively,
\[
 |\Phi'(r)|\le700e^{13r-\pi e^{4r}},\qquad
 0<R_t(r)\le150e^{tr^2+13r-\pi e^{4r}}.
\tag{11}
\]
The constants follow by bounding the \(n^6,n^4,n^2\) Gaussian series in
(6). In particular every radial mass, Fourier jet and endpoint term is
integrable. For Fourier jets, using the exact marginal is sharper:
\[
 |H_t^{(j)}-(H_t^U)^{(j)}|
 \le\frac{32U^j e^{TU^2+(9+Y)U-\pi e^{4U}}}
 {4\pi e^{4U}-2TU-(9+Y)-j/U},
\tag{12}
\]
for \(T=1/20,Y=1,U\ge1,j\le6\). This is the paid spectral marginal
cutoff, not a claim that cutting the radial integral at the same radius
has identical boundary data. A radial cutoff adds its own endpoint term in
(2), which must be retained.

All spatial derivatives of (3) fix time and any cutoff. The normalized
observation is \((H/(2A),2(H'-bH)/(LA))\),
\(b=\partial_x\log A\). Higher normalized jets use the complete product
rule; the scalar normalized PDE is
\(Q_t{}_t=-Q''-2bQ'-(\partial_t\log A+b_x+b^2)Q\).
For a closed complex rectangle the tail (12) is multiplied by the suprema
of derivatives of \(A^{-1}\), exactly as in the kinetic scout's (7).
No omission of the small large-height normalizer is permitted. Note 13's
complete finite arithmetic jet payment remains necessary for a sign test.

The representation and genuine radial positivity are established here. A
promising next bounded task is to test a specific variation-diminishing or
total-positivity property of the *theta* radial kernel against the signed
jet condition, rather than infer it from radial positivity. Such a property
would have to distinguish (10) and survive the nonlocal correction (4).
No collision exclusion or RH conclusion follows from the present result.
