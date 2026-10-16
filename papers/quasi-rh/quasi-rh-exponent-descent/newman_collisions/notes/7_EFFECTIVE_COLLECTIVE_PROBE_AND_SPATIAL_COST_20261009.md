# An effective collective-attraction probe and the global spatial cost

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model cross-review is an internal check, not independent validation.

This completes the next analytic checkpoint after [Note 6](6_ANALYTIC_COLLECTIVE_ATTRACTION_AND_LANDING_20261009.md).
Its effective high-height estimate uses [Polymath, Theorem 1.3 and
equations (20)--(24)](https://arxiv.org/html/1904.12438#S1.Thmtheorem3).
The theorem is applied inside its proved domain. A separate global implication
uses the actual final-time canopy established in the published Polymath proof.
The new work samples no zeros or phases and extends no numerical grid.

The concrete result is a uniform exact attraction floor greater than four for
maximal nonreal zeros with real part at least \(10^{16}\), imaginary height at
most \(1/5\), and time in \([1/5,3/10]\). A reflected-pair estimate completes
a global landing argument, but its gain over the historical \(0.22\) baseline
is only about \(4\cdot10^{-36}\). No literature novelty or record bound is claimed.
The main progress is the effective field estimate and the identification of
the lower spatial sector as the remaining bottleneck.

## 1. Statement and fixed-cutoff setup

Write

\[
 H_0(z)=\xi(1/2+iz/2)/8,\quad \partial_tH_t=-H_t'',\quad
 L_\eta(t,x)=-\Im\frac{H_t'}{H_t}(x+i\eta).
\]

For every

\[
 x\ge 10^{16},\qquad 1/5\le t\le3/10,
\]

the effective conclusion is

\[
 L_{9/10}(t,x)\ge6. \tag{1}
\]

The derivative step below uses the uniform remainder lemma proved in
Section 5: on each disk
\(D_x=\{|z-(x+9i/10)|\le1/20\}\), the fixed-cutoff approximation to
\(U_t=H_t/B_t\), with \(B_t(z)=M_t((1-iz)/2)\), satisfies

\[
 |U_t-f_{t,N}|<10^{-12},\qquad
 |U_t'-f_{t,N}'|(x+9i/10)<2\cdot10^{-11}. \tag{2}
\]

The estimates use all natural-cutoff values on the outer disk and paid
cutoff jumps before Cauchy's derivative estimate is applied. It is not an
assumption about the exact heat flow or a derivative of the moving-cutoff
formula. For the deliberately coarse rational reserves below, both bounds
in (2) may be replaced by \(10^{-4}\).

Put \(r=1/20\), \(a=x-r\), \(A=a/(4\pi)\), and \(\ell=\log A\).
The entire disk lies in

\[
 \Re z\in[x-r,x+r],\quad
 17/20\le\Im z\le19/20,
\]

inside Polymath's approximation domain. The elementary inequalities
\(\log10>23/10\), \(\log(4\pi)<3\), and
\(\log(x-1/20)>16\log10-1/10\) give

\[
 \ell\ge67/2. \tag{3}
\]

Choose the single cutoff

\[
 N=\left\lfloor\sqrt{A+(1/5)/16}\right\rfloor.
\]

It remains fixed on the disk and at every time in the interval. Every
possible natural cutoff on this disk is at most
\(\sqrt{A+1}\). The same upper bound includes any crossing index
\(N+1\) that actually occurs, as proved in Section 5. Hence

\[
 \log N\le\ell/2+1/100. \tag{4}
\]

Write \(s=(1-iz)/2\),

\[
 p_n(s)=\exp\{(t/4)\log^2n-(s+t\alpha(s)/2)\log n\},
 \quad P_N(s)=\sum_{n\le N}p_n(s),
\]

and

\[
 \gamma=M_t(1-s)/M_t(s),\qquad
 f_{t,N}=P_N(s)+\gamma P_N(1-s)=:P+R.
\]

This is a holomorphic fixed-cutoff rewriting of Polymath's approximation;
the apparent conjugations in its second sum disappear after inserting
the stated \(\kappa\).

## 2. Main Dirichlet polynomial

Polymath (21) has zero positive-part correction on this disk, since
\(1-3y+4y(1+y)/(\Re z)^2<0\). Consequently

\[
 |p_n(s)|\le n^{-37/40-(t/4)(\ell-\log n)}.
\]

For \(2\le n\le16\), use \(\log16<3\), \(t\ge1/5\), and (3)
to bound this by \(n^{-12/5}\). For \(n>16\), (4) bounds it by
\(n^{-7/4}\). Thus the small head plus the integral tail give

\[
 \begin{split}
 |P-1|&\le\sum_{n=2}^{16}n^{-12/5}+
                   \sum_{16<n\le N}n^{-7/4}\\
 &<\frac{19}{100}+\frac{19}{50}\frac57+\frac16
 =\frac{1319}{2100}<\frac23. \tag{5}
 \end{split}
\]

Here \(2^{-12/5}<19/100\), \(2^{-7/5}<19/50\), and the two
tails are bounded by their decreasing integrals. Similarly,

\[
 \begin{split}
 \sum_{n=2}^{16}\log n\,n^{-12/5}
 &<\frac{19}{100}\frac7{10}+
   \frac{19}{50}\left(\frac12+\frac{25}{49}\right)
 =\frac{25327}{49000}<\frac{13}{25},\\
 \sum_{16<n\le N}\log n\,n^{-7/4}
 &\le\int_{16}^\infty\log u\,u^{-7/4}\,du
 <\frac{13}{18}.
 \end{split}
\]

Therefore

\[
 \sum_{2\le n\le N}\log n\,|p_n(s)|
 <\frac{559}{450}<\frac54. \tag{6}
\]

For both \(s\) and \(1-s\), their imaginary parts have magnitude at
least \(V=a/2\), and the direct formula for \(\alpha\) gives

\[
 |\alpha'|\le\frac{3}{2V^2}+\frac{1}{2V}
 \le\frac2a.
\]

In particular \(|1+t\alpha'/2|<1001/1000\). Differentiating the
fixed polynomial is now legitimate and gives

\[
 |P'|\le\frac12\frac{1001}{1000}\frac54
 =\frac{1001}{1600}<\frac{63}{100}. \tag{7}
\]

## 3. Reflected Dirichlet polynomial

The reflected argument has real part at least \(1/40\). Directly from
\(\alpha\), its real part is at least \(\ell/2-V^{-2}\).
The loss \(t/(2V^2)\) is far below the reserves in the following powers:

\[
 |p_n(1-s)|\le
 \begin{cases}
 n^{-3/2},&n\le16,\\
 n^{-17/20},&16<n\le N.
 \end{cases}
\]

Hence

\[
 |P_N(1-s)|\le3+\frac{20}{3}N^{3/20}
 \le3+7e^{3\ell/40}. \tag{8}
\]

Polymath (20), uniformly over the disk, gives

\[
 |\gamma|\le\frac{103}{100}e^{-17\ell/40}.
\]

Combining with (8),

\[
 |R|\le\frac{103}{100}
 (3e^{-17\ell/40}+7e^{-7\ell/20})
 <\frac{7519}{10^8}<10^{-4}. \tag{9}
\]

For the displayed rational bound use \(\ell\ge67/2\),
\(e^{-1139/80}<10^{-6}\), and \(e^{-469/40}<10^{-5}\).
For example these follow from \(\log10<231/100\).

The reflected function is holomorphic on the full fixed-cutoff disk.
Cauchy's estimate at its center therefore gives the simpler derivative bound

\[
 |R'|<20\frac{7519}{10^8}=\frac{7519}{5\cdot10^6}
 <\frac1{500}. \tag{10}
\]

## 4. Normalizer and exact logarithmic derivative

By definition \(B_t'/B_t=-im_t'(s)/2\), so

\[
 -\Im B_t'/B_t=\tfrac12\Re m_t'(s).
\]

For either argument \(s\) or \(1-s\), the explicit formula is

\[
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi},
 \qquad m_t'=\alpha(1+t\alpha'/2).
\]

Their imaginary parts have modulus at least \(a/2\), their real parts
lie between \(1/40\) and \(39/40\), and their arguments have modulus at
most \(\pi/2\). Also \(\log(|s|/(2\pi))\le\ell+1/100\): for example
\(2|s|\le\sqrt{(a+1/10)^2+4}\), whose ratio to \(a\) is less than
\(e^{1/100}\). Hence

\[
 |\alpha|\le\frac3a+\frac12(\ell+1/100+\pi/2)<\frac35\ell,
 \qquad \Re\alpha\ge\ell/2-4/a^2.
\]

The correction \(t\alpha\alpha'/2\) has modulus at most
\((9/50)\ell/a\), which is bounded above by \((3/10)\ell/a\).
Thus

\[
 \Re m_t'(s)\ge\ell/2-4/a^2-(3/10)\ell/a
 \ge\ell/2-1/1000.
\]

The loose final reserve follows, for instance, from
\(\ell\le\log a\le\sqrt a\) and \(a>10^{15}\).
Consequently at the probe center,

\[
 -\Im B_t'/B_t\ge67/8-1/2000. \tag{11}
\]

Applying the paid remainder and derivative bounds (2) to (5), (7),
(9), and (10) gives

\[
 |U_t|>1/3-10^{-4}-10^{-12}>33/100,
 \qquad |U_t'|<63/100+1/500+2\cdot10^{-11}<13/20.
\]

Thus \(|U_t'/U_t|<2\), which both certifies nonvanishing and yields

\[
 L_{9/10}(t,x)
 =-\Im B_t'/B_t-\Im U_t'/U_t
 >67/8-1/2000-2
 =12749/2000>6.
\]

This proves (1).

## 5. Complete approximation and cutoff error

This section proves (2). Write \(z=u+iy\) for a point in the disk, and
\(m=\lfloor\sqrt{u/(4\pi)+t/16}\rfloor\) for its source cutoff.
The squared-cutoff parameters across the disk and time interval have spread

\[
 \frac1{40\pi}+\frac1{160}<1.
\]

Since the square roots differ by less than one and the minimum cutoff is
\(N\), every \(m\) is either \(N\) or \(N+1\). For every index up to
\(N+1\) that occurs, put

\[
 \rho=\frac12\log\left(1+\frac{1/(40\pi)+3/160}{A}\right)<10^{-16}.
\]

The natural index obeys \(\log n\le\ell/2+\rho\). If a crossing occurs,
\(\ell/2<\log(N+1)\le\ell/2+\rho\). The upper bound uses the largest
squared-cutoff parameter; the lower bound uses \(N+1>\sqrt{A+1/80}\).
It applies to the crossing term exactly when that term needs to be paid.
For fixed \(N\), all indices in the approximant already obey (4).

All source cutoffs exceed \(10^7+1\), since \(A>4\cdot10^{14}\).
The coefficient bound, with the source's correction zero, gives

\[
 |p_n(s)|\le n^{-7/4},\qquad
 \sum_{n=1}^{m}|p_n(s)|\le\frac73. \tag{13}
\]

For the second leg, the exact holomorphic rewriting and source (20), (22)
give the modulus multiplier

\[
 |\gamma|m^{|\kappa|}n^y
 \le e^{.02y}\left(\frac{m^2}{u/(4\pi)}\right)^{y/2}
       e^{|\kappa|\log m}<\frac{103}{100}. \tag{14}
\]

The same estimate holds with a crossing index \(N+1\) in place of \(m\).
Indeed the squared-index quotient is at most \(e^{2\rho}\), while
\(|\kappa|\log m<10^{-14}\). For this reserve use
\(u>9\cdot10^{15}\), \(\log m\le\log u\),
\(\log(9\cdot10^{15})<37\), and the decreasing function
\((\log u)/u\). The total exponent in (14) is less than \(.02\), and
\(e^{.02}\le50/49<103/100\).

**Source errors.** In source (23),
\(|\log(u/(4\pi n^2))|\le\log u\): any negative endpoint is bounded
by \(\log(1+t/(16q))\), \(q=u/(4\pi)\). Its error exponent is at most

\[
 v(u)=\frac{.006(\log u)^2+1}{.99u}<1.1\cdot10^{-15}.
\]

The majorant decreases for \(u\ge9\cdot10^{15}\). At the endpoint it
is bounded using \(\log u<37\). Then
\(e^v-1\le v/(1-v)<1.12\cdot10^{-15}\), and (13)--(14) imply

\[
 e_A+e_B<10^{-14}. \tag{15}
\]

For source (24), the positive corrections have sum less than \(10^{-6}\).
The first is at most \(1.24(3+1)/(m-.125)<5\cdot10^{-7}\);
the second is at most \((3\log u+16)/(.99u)<2\cdot10^{-14}\).
Use \(\sqrt{L^2+\pi^2/4}\le L+\pi/2\), with \(L=\log q>0\).
The negative exponent has magnitude at least

\[
 \frac{37\ell}{80}+\frac{\ell^2}{80}
 \ge\frac{9447}{320}>29.5+10^{-6}.
\]

Therefore

\[
 e_{C,0}<e^{-29.5}<2\cdot10^{-13}. \tag{16}
\]

**Complete cutoff jump.** At a crossing put \(v=\log(N+1)\).
Completing the square gives
\(v^2-\ell v=(v-\ell/2)^2-\ell^2/4\), so

\[
 |p_{N+1}(s)|\le
 e^{-37\ell/80-\ell^2/80+\rho^2/20}
 <e^{-29.5}<2\cdot10^{-13}.
\]

Its reflected companion is at most \(103/100\) times this modulus,
by the crossing-index version of (14). Thus

\[
 |f_{t,N+1}-f_{t,N}|<5\cdot10^{-13}. \tag{17}
\]

Paying (15)--(17) yields \(|U_t-f_{t,N}|<10^{-12}\) on the full
disk. The remainder is holomorphic there; Cauchy's estimate with radius
\(1/20\) gives its center derivative modulus less than
\(2\cdot10^{-11}\). This proves (2) without differentiating a moving
cutoff and without assuming a relative lower bound for \(H_t\).

## 6. Exact-field consequence

Let \(z=x+iy\) be a simple nonreal zero with maximal imaginary height,
where \(0<y\le1/5\) and \(x\ge10^{16}\). Since
\((9/10)/y\ge9/2>\sqrt5\), the sharp exact-field comparison in Note 6
has factor one. Therefore

\[
 E_t(z)\ge\frac{L_{9/10}}{9/10}
       -\frac2{81/100-y^2}
 \ge\frac{20}{3}-\frac{200}{77}
 =\frac{940}{231}>4. \tag{12}
\]

This is an effective high-height attraction floor. It applies to every
height beyond the threshold, every time in the stated interval, and every
allowed maximal zero; it uses no assumption that the other zeros are real.
It does not by itself provide a global floor or a new Newman endpoint:
zeros whose real parts lie below the threshold must also be controlled.
The exact field \(E\), rather than an unproved projected-field claim, is
what (12) bounds.


## 7. Landing cost and a complete global implication

If every globally maximizing nonreal zero stays in the high sector,
(12) gives \(w'\le-2-16w\). Starting from \(t_0=1/5,w_0=1/25\),
its conditional landing endpoint is

\[
 t_{\mathrm{sector}}=\frac15+\frac1{16}\log\frac{33}{25}
 \in(0.21735,0.21736). \tag{18}
\]

The spatial premise is additional. Equation (18) is not a global Newman
bound from the presently proved probe estimate.

There is nevertheless a fully effective global patch. No nonreal zero
has real part zero: \(H_t(iy)>0\) follows from the positive defining
kernel and \(\cosh(yu)>0\). At a maximal zero \(x+iy\), \(x>0\),
its distinct reflected pair \(-x\pm iy\) contributes exactly

\[
 E_t(z)\ge\frac1{2(x^2+w)}. \tag{19}
\]

Its same-height member contributes zero to the exact field, and the other
member contributes \(2/(4x^2+4w)\). All other grouped contributions are
nonnegative. On \(0<x\le X=10^{16}\), (19) gives a floor
\(1/[2(X^2+w)]\); on \(x\ge X\), (12) gives a stronger floor.
Evenness covers negative real parts. Therefore the complete global floor is

\[
 E_t(z)\ge\frac1{2(X^2+w)},\qquad 0<w\le\frac1{25},
 \quad \frac15\le t\le\frac3{10}. \tag{20}
\]

No separation barrier, quantitative nonreal-zero cutoff, or unknown counting
constant enters this patch. The bounds are combined by a spatial minimum;
the reflected roots are not added to a probe bound that may already include
their contributions.

Put \(a=X^2\). The reciprocal-speed integral is

\[
 M_a(w)=\frac w4+\frac a8\log(1+2w/a),\qquad
 M_a'(w)=\frac{a+w}{2(a+2w)}.
\]

The maximum-envelope, finite multiple-event, and limiting arguments of
Note 6 apply to this continuous positive floor. The qualitative eventual
reality of high zeros gives compactness on each positive-time interval;
no effective value for that compactness cutoff is needed. Thus an actual
initial canopy \(W(t_0)\le w_0\) gives landing by \(t_0+M_a(w_0)\).
The required interval is covered because \(M_a(w_0)<w_0/2=1/50\).

The proof of [Polymath, Proposition 3.3 and Section 8](https://arxiv.org/html/1904.12438#S3.Thmproposition3)
establishes the actual canopy \(W(1/5)\le1/25\), using its already verified
finite RH, barrier, and final canopy hypotheses. We adopt those published
proof inputs, rather than rerunning their computation. The bare conclusion
\(\Lambda\le0.22\) alone would not imply this earlier-time canopy.

To avoid subtracting nearly equal logarithms, compute the gain directly:

\[
 \frac w2-M_a(w)=\int_0^w\frac{u}{2(a+2u)}\,du
 \ge\frac{w^2}{4(a+2w)}.
\]

Consequently the complete global implication is

\[
 \boxed{\Lambda\le\frac{11}{50}
        -\frac1{2500\cdot10^{32}+200}.} \tag{21}
\]

This is a tiny strict improvement of the chosen historical baseline under
the accepted published inputs. It is not a record bound or a substantial
reduction. Raising the high-sector field above four does not improve the
limiting spatial floor in (20).

## 8. Verification and the next bounded analytic target

The [scalar checker](../../numerics/check_effective_collective_probe.py)
and [small record](../../numerics/effective_collective_probe_record_20261009.json)
verify 105 exact rational, Taylor, and polynomial assertions, together with
an outward enclosure of the conditional landing time. Two runs reproduced
the small record byte-for-byte. They evaluate no heat functions and enumerate no large cutoff.
Universal analytic estimates, the imported approximation theorem, and the
published canopy proof remain mathematical inputs; scalar replay alone is
not independent validation of those inputs. The [scoped review](../../reviews/EFFECTIVE_COLLECTIVE_PROBE_REVIEW_20261009.md)
records the same-model audits and limitations.

The next useful bounded target is an analytic bridge to the published
barrier abscissa \(X_P=6\cdot10^{10}+83951.5\): seek a proved exact
attraction floor \(E\ge1\) for \(x\ge X_P\), \(0<y\le1/5\), and
\(t\in[1/5,11/50]\). Use a probe at \(\eta=99/100\), radius
\(1/200\), a small finite head, and logarithmic integral tail majorants,
paying all errors on the whole complex disk. If an absolute head estimate
fails, a finite Euler-product treatment may retain more cancellation.
The deliverable is a uniform derivative margin or an explicit obstruction
identifying the term that prevents one; it does not require a zero search
or a parameter grid.

That bridge alone still needs a compatible lower-sector estimate or a
strictly smaller left envelope and a barrier continuing after \(t=1/5\)
to yield a material global gain. The published barrier ends at \(1/5\);
it is not a later-time separator at \(10^{16}\). Any use of a stronger
left envelope or continued barrier must prove those additional premises.
The chosen positive-time milestone does not give an iteration to zero.
