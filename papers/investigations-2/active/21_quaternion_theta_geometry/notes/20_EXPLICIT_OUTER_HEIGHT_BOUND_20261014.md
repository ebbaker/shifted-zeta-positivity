# An explicit outer height bound at threshold five

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**,
verified from the active turn metadata. Parallel derivation and independent
internal LLM review used the inherited configuration. This is an analytic
research proof with internal review, not a formal verification.

This completes the quantitative target in
[Note 18](18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md). The
[companion Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
improves the asymptotic sufficient threshold to three, with its own
unevaluated height. The explicit number here applies to threshold five.
The [internal review](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md)
checks both statements independently.

## Claim

Use exactly the definitions of Note 17, especially

\[
 L=\log(x/(4\pi)),\qquad \omega=L/4,
 \quad Q=M_t((1+ix)/2)\zeta\big((1+ix)/2+(t/2)\alpha((1+ix)/2)\big).
\]

A concrete sufficient threshold is

\[
 \boxed{X_1=4\pi\exp(10^9).}
\]

For \(x\ge X_1\), \(0<t\le1/2\), and \(tL\ge5\), every coordinate
of the normalized four-jet in Note 17 differs from
\((\cos\phi,-\sin\phi,-\cos\phi,\sin\phi)\), \(\phi=\arg Q\), by at
most \(108000000/L\le0.108<1/8\). Thus Note 17's lower bounds
\(1/2\) for the normalized first-pair norm and \(31/64\) for each
normalized Laguerre form apply. Evenness supplies the negative-height
version. The bound is deliberately enormous and supplies no feasible
finite-strip coverage.

All the elementary bounds below hold already for \(L\ge1000\), provided
\(0<t\le1/2\) and \(tL\ge5\). We prove the stronger explicit error
bound \(108000000/L\) on that domain and impose \(L\ge10^9\) only at
the final sign step.

## Imported primary estimate

The exact source is D. H. J. Polymath, *Effective approximation of heat
flow evolution of the Riemann xi function, and a new upper bound for the
de Bruijn-Newman constant*, arXiv:1904.12438v2, Theorem 1.3,
[HTML equations (13)–(24)](https://arxiv.org/html/1904.12438v2#S1),
[PDF page 6](https://arxiv.org/pdf/1904.12438v2#page=6).
The equation text was checked in the primary HTML and PDF extraction.
For \(z=u+iv\), \(u\ge200\), \(0\le v\le1\), it gives Note 17's
identity with the complete errors \(e_A+e_B+e_{C,0}\).
The error exponent in its (23) is precisely

\[
 q_n=\frac{(t^2/16)\log^2(u/(4\pi n^2))+0.626}{u-6.66}.
\]

The positive correction to the negative main exponent in its (24) is
precisely

\[
 c_C=\frac{1.24(3^v+3^{-v})}{N-0.125}
  +\frac{3|L_u+i\pi/2|+10.44}{u-12},\qquad L_u=\log(u/(4\pi)).
\]

In particular, no factor of \(t\) multiplies \(0.626\). The theorem
also gives \(|\gamma|\le e^{0.02v}e^{-vL_u/2}\) and
\(|\kappa|\le tv/(2(u-6))\). The second finite sum in its (14)
corresponds exactly to \(w_+\) because
\(\overline{s_*}+\kappa-v=w_+\), while \(s_*=w_-\).
These identities, together with its \(\gamma\), preserve both common
normalization factors; no unspecified multiplicative comparison is used.

## 1. Disc geometry, alpha and the summable exponent

Put \(D_x=\{|z-x|\le L^{-1}\}\) and write \(z=u+iv\). On this disc,

\[
 u\ge x/2\ge e^L,\quad |L_u-L|\le2/(xL)<1,
 \quad \theta_u=tL_u\ge5-1/(xL)\ge19/4.
\]

For \(s=s_\pm(z)=(1\pm iz)/2\), the real part lies in \([0,1]\),
and \(|s|,|s-1|\ge u/2\). The explicit formula

\[
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}(s/(2\pi))
\]

gives

\[
 \Re\alpha(s)\ge L_u/2-3/u,\quad |\alpha(s)|\le L_u/2+1\le L,
 \quad |\alpha'(s)|\le1/u+6/u^2\le2/u.
\]

For the magnitude bound, \(|s|\le(u/2)\sqrt{1+4/u^2}\),
\(|\arg s|\le\pi/2\), and the rational terms cost at most \(3/u\).
Thus the displayed magnitude bound follows, with much room, when
\(u\ge e^{1000}\). Consequently

\[
 \sigma_\pm:=\Re w_\pm\ge\frac12-\frac1{2L}
       +\frac{\theta_u}{4}-\frac{3t}{2u}\ge\frac32.
\]

For \(N=\lfloor\sqrt{u/(4\pi)+t/16}\rfloor\),

\[
 \frac12 e^{L_u/2}\le N,
 \qquad \log N\le L_u/2+1/u.
\]

The latter follows from \(\log(1+y)\le y\); the extra logarithmic
term is at most \(\pi t/(8u)<1/u\). Therefore, for \(1\le n\le N\),

\[
 e^{t\log^2n/4}n^{-\sigma_\pm}\le n^{-p},\quad
 p=\frac12+\frac{\theta_u}{8}-\delta,
 \quad\delta=\frac1{2L}+\frac{7t}{4u}\le\frac1{32}.
\]

Writing \(s_0=\theta_u-19/4\ge0\), this proves

\[
 p\ge\frac{17}{16}+\frac{s_0}{8}.
\]

For the upper half-disc, the same bound applies to the first branch
with the extra factor \(n^v\): before multiplication its real exponent
has the stronger term \((1+v)/2\), so afterward it has
\((1-v)/2\), already paid in \(\delta\).

## 2. Explicit weighted-sum discrepancy

For \(a>0\) and integer \(m\ge0\), comparison on each interval
\([n-1,n]\), using \(\log n\le\log y+1\) there for \(n\ge2\), gives

\[
 \sum_{n=2}^\infty (\log n)^m n^{-1-a}
 \le \int_1^\infty(\log y+1)^m y^{-1-a}\,dy.
\]

At \(a=1/16,m=2\), the right side is
\(2/a^3+2/a^2+1/a=8720<9000\). Using
\(e^q-1\le qe^q\) and \(n^{-s_0/8}\le2^{-s_0/8}\) for \(n\ge2\),

\[
 \begin{split}
 |S_{t,N}(w_\pm)-\zeta(w_\pm)|
 &\le \frac{9000}{4L_u}(19/4+s_0)2^{-s_0/8}
       +2N^{-1/2}\\
 &\le\frac{29250}{L_u}+3e^{-L_u/4}\\
 &\le\frac{31000}{L}.
 \end{split}
\]

Here \(s_0e^{-s_0\log2/8}\le8/(e\log2)<8\), so the parenthesis
with its exponential is less than \(19/4+8<13\).
Also \(L_u\ge L-1\) and \(L\ge1000\), so
\(29250/L_u<30000/L\). Finally \(3Le^{-(L-1)/4}\le1\): for example,
\(e^{(L-1)/4}\ge(L-1)^2/32\ge3L\) at and beyond \(L=1000\).
This controls the zeta tail as well as every weighted finite-sum term,
uniformly even when \(tL\) grows.

## 3. Every imported approximation error

Work on the upper half-disc; the lower half will follow by Schwarz
symmetry. The imported gamma bound gives \(|\gamma|\le2\), and

\[
 |\kappa|\log N
 \le\frac{tv}{2(u-6)}(L_u/2+1/u)<1/2,
\]

so \(N^{|\kappa|}\le2\). Section 1 and
\(\zeta(17/16)\le1+16=17\) then give

\[
 \sum_{n\le N}(1+|\gamma|N^{|\kappa|}n^v)
   e^{t\log^2n/4}n^{-\Re w_-}\le5\cdot17=85.
\]

Since \(-2/u\le\log(u/(4\pi n^2))\le L_u\),

\[
 0\le q_n\le\frac{L^2}{16u}<1.
\]

Indeed \((L+1)^2/64+1\le L^2/32\), and \(u-6.66\ge u/2\).
The elementary bound \(e^q-1\le2q\) for \(0\le q\le1\) yields

\[
 e_A+e_B\le\frac{85L^2}{8u}\le\frac{11L^2}{u}\le\frac1L.
\]

The last inequality follows from \(u\ge e^L\) and
\(e^L\ge L^4/24\ge11L^3\) for \(L\ge1000\).

For the third error, \(3^v+3^{-v}\le4\), \(N-0.125\ge N/2\), and
\(|L_u+i\pi/2|\le L_u+2\) imply

\[
 c_C\le20e^{-L_u/2}+7L/u\le1.
\]

For a purely elementary verification of the last inequality,
\(20e^{-(L-1)/2}\le160/(L-1)^2<1/2\) and
\(7L/e^L\le168/L^3<1/2\). The main exponent gives

\[
 e_{C,0}\le e\exp[-(1/4+19/64)L_u]
       \le3e^{-L_u/2}\le\frac1L.
\]

Thus

\[
 \boxed{e_A+e_B+e_{C,0}\le2/L.}
\]

## 4. Microscopic-disc amplitude comparison and Cauchy errors

Let \(\Gamma=|M_t(s_+(x))|=|M_t(s_-(x))|\). On \(D_x\),

\[
 \left|\frac{d}{dz}\log M_t(s_\pm(z))\right|
 \le\frac{|\alpha|}{2}(1+t|\alpha'|/2)\le L.
\]

Integrating along the straight segment from the real center, of length
at most \(1/L\), gives

\[
 |M_t(s_\pm(z))|\le e\Gamma<3\Gamma.
\]

There is no branch problem: both discs in the \(s\)-plane have large
nonzero imaginary parts and lie away from the principal branch cut.
For \(\Re w\ge3/2\), the absolutely convergent zeta and reciprocal
Dirichlet series give

\[
 |\zeta(w)|\le\zeta(3/2)\le3,\quad |1/\zeta(w)|\le3,
 \quad\Gamma\le3|Q|.
\]

Let \(\mathcal A=Q_++Q_-\) with Note 17's analytic definitions.
Combining Sections 2–3 with the two branch amplitudes yields

\[
 \begin{split}
 |H_t(z)-\mathcal A(z)|
 &\le 2(3\Gamma)\frac{31000}{L}
        +(3\Gamma)\frac2L\\
 &=\frac{186006\Gamma}{L}
  \le\frac{558018|Q|}{L}
  \le\frac{560000|Q|}{L}.
 \end{split}
\]

This was proved on the upper half-disc, where the imported theorem
applies. Both analytic functions obey Schwarz symmetry, so it holds
throughout the disc. Although the finite sum has a moving cutoff, only
the analytic function \(H_t-\mathcal A\) is differentiated.
Cauchy's inequality on the circle of radius \(1/L\) gives

\[
 \frac{|\partial_x^k(H_t-\mathcal A)(x)|}{2|Q|\omega^k}
 \le\frac{280000\,k!\,4^k}{L}
 \le\frac{107520000}{L},\qquad 0\le k\le3.
\]

## 5. Explicit derivatives of the analytic carrier

Set \(s=(1+ix)/2\), \(w=s+t\alpha(s)/2\), and let
\(g=\log Q_+\) be a local logarithm. At the real center,

\[
 |\alpha(s)-(L/2+i\pi/4)|\le4/x,
 \quad |\alpha'|\le2/x,\quad |\alpha''|\le3/x^2,
 \quad |\alpha'''|\le9/x^3.
\]

For the first estimate use
\(s=(ix/2)(1-i/x)\) and
\(|\operatorname{Log}(1-i/x)|\le2/x\); the rational terms cost \(3/x\).
The higher bounds follow by differentiating the explicit formula:

\[
 \alpha'=-\frac1{2s^2}-\frac1{(s-1)^2}+\frac1{2s},\quad
 \alpha''=\frac1{s^3}+\frac2{(s-1)^3}-\frac1{2s^2},\quad
 \alpha'''=-\frac3{s^4}-\frac6{(s-1)^4}+\frac1{s^3}.
\]

Let \(G(x)=\log M_t(s(x))\). Direct differentiation gives

\[
 \begin{split}
 G'&=(i/2)\alpha(1+t\alpha'/2),\\
 G''&=-\tfrac14\{\alpha'+(t/2)[(\alpha')^2+\alpha\alpha'']\},\\
 G'''&=-\tfrac i8\{\alpha''+(t/2)[3\alpha'\alpha''+\alpha\alpha''']\}.
 \end{split}
\]

At \(L\ge1000\), the preceding bounds imply
\(|G'-i\omega|\le1\), \(|G''|\le1\), \(|G'''|\le1\).
For the first one a concrete majorant is
\(\pi/8+2/x+L/(4x)<1\); for the others insert the stated powers of
\(1/x\), \(t\le1/2\), \(|\alpha|\le L\), and \(x\ge e^L\).
Also

\[
 |w'|\le1,\qquad |w''|\le1,\qquad |w'''|\le1.
\]

The prime-power Dirichlet series for the logarithmic zeta derivatives
satisfies, for \(r=1,2,3\),

\[
 |(\log\zeta)^{(r)}(w)|
 \le\sum_{n=2}^\infty (\log n)^r n^{-3/2}.
\]

Section 2's integral comparison with \(a=1/2\) bounds these respectively
by \(6,26,158\). The chain rule therefore yields

\[
 |g'-i\omega|\le7,\quad |g''|\le1+26+6=33,
 \quad |g'''|\le1+158+3\cdot26+6=243.
\]

Writing \(d=g'-i\omega\), the exponential derivative identities give

\[
 \begin{array}{c|c}
 k & |Q_+^{(k)}/Q-(i\omega)^k|/\omega^k\\ \hline
 1&28/L\\
 2&56/L+1312/L^2\\
 3&84/L+3936/L^2+81856/L^3.
 \end{array}
\]

All entries are at most \(100/L\) for \(L\ge1000\). For example, at
order three the numerator is bounded by
\(21\omega^2+246\omega+1279\), from
\((i\omega+d)^3+3(i\omega+d)g''+g'''\).
The conjugate branch has the conjugate derivatives at real \(x\).
Thus \(\mathcal A\)'s normalized real four-jet differs from the common
phase vector by at most \(100/L\) (and by exactly zero at order zero).

## 6. Total error and scope

Combining the two estimates, each normalized coordinate error is at most

\[
 \frac{107520100}{L}<\frac{108000000}{L}.
\]

At \(L\ge10^9\), this is below \(0.108<1/8\), proving the stated
threshold. The only analytic import is Polymath's stated effective
Riemann–Siegel theorem; the remaining bounds are elementary and explicit.
No interval quadrature, floating-point evaluation of \(e^{10^9}\), RH,
unknown gap, phase exclusion, or division by a physical jet is used.

The complement of this explicit outer region and the existing finite
certificate contains \(104<|x|<4\pi e^{10^9}\) and, at higher heights,
\(t\log(|x|/(4\pi))<5\). Note 19 narrows the asymptotic unresolved
region further, to below \(3+\varepsilon\), but its transition height
has not been evaluated. The explicit bound here gives no practical bridge
from the finite certificate through height 104.

## 7. Exact arithmetic audit and continuation

The [standard-library checker](../numerics/check_explicit_outer_constants.py)
passed **52 exact checks**. Its [small receipt](../numerics/EXPLICIT_OUTER_CONSTANT_CHECKS_20261014.json) records the script hash,
all rational budgets, and sufficient polynomial inequalities valid for
every real \(L\ge1000\). A polynomial is checked by writing
\(L=1000+y\), \(y\ge0\), and verifying that all resulting coefficients
are nonnegative and the constant is strictly positive. No value of
\(e^{10^9}\) is evaluated. This audits the explicit arithmetic and
monotonic majorants; the mathematical arguments establishing the primary
approximation, analytic identities, and reductions to these inequalities
remain the proof above. It is not a quadrature or formal analytic proof.


The [independent internal review](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md)
checks the analytic steps and independently replays the arithmetic. From
this investigation's `numerics/` directory:

```sh
python3 check_explicit_outer_constants.py --output /tmp/inv21-outer-constants.json
```

A useful next refinement would retain sharper summability exponents and a
larger optimized analytic-disc radius, provided the gamma-amplitude
comparison and all four derivative payments remain explicit. Any such
refinement must distinguish an explicit threshold-five statement from
the stronger asymptotic threshold-three theorem. No finite-strip coverage
is asserted by the present bound.
