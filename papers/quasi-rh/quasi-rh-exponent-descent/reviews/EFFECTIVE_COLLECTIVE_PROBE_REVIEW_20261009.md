# Review of the effective collective probe and global landing cost

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a same-model internal cross-review, not independent validation.

Reviewed artifact: [Heat Note 7](../newman_collisions/notes/7_EFFECTIVE_COLLECTIVE_PROBE_AND_SPATIAL_COST_20261009.md).
This review includes a separate audit of the whole-disk remainder and a
separate audit of the global spatial patch.

Scope: the high-height probe at imaginary height \(9/10\), all
real parts \(x\ge10^{16}\), and all \(t\in[1/5,3/10]\). The audit imports
[Polymath, Theorem 1.3, equations (20)--(24)](https://arxiv.org/html/1904.12438#S1.Thmtheorem3),
not any numerical certificate from the recent collective-contraction
preprint. No zero search, grid, or assumption that external zeros are real
enters this derivation.

## 1. A complete explicit remainder lemma

Put

\[
r=1/20,\quad h=x-r,\quad q_-=h/(4\pi),\quad
q_+=(x+r)/(4\pi),\quad \ell=\log q_-,\quad
N=\left\lfloor\sqrt{q_-+(1/5)/16}\right\rfloor.
\]

Let \(D_x=\{|z-(x+9i/10)|\le r\}\), \(s=(1-iz)/2\),

\[
U_t(z)=H_t(z)/M_t(s),\qquad
f_{t,N}(z)=P_{t,N}(s)+\gamma_t(z)P_{t,N}(1-s),\quad
\gamma_t=M_t(1-s)/M_t(s).
\]

The analytic rewriting is exactly the one proved in Note 3, with an
asymmetric normalizer. Because the present entire disk lies in the upper
half-plane, it needs no reflection of an error estimate and no conversion
to the symmetric normalizer. Every \(z\in D_x\) has

\[
\Re z\ge h>9\cdot10^{15},\qquad
17/20\le\Im z\le19/20,
\]

inside the source theorem's domain. The normalizer is analytic and
nowhere zero on a neighborhood of the disk.

The complete bounds are

\[
|U_t(z)-f_{t,N}(z)|<10^{-12}\quad(z\in D_x),\qquad
|(U_t-f_{t,N})'(x+9i/10)|<2\cdot10^{-11}. \tag{A}
\]

The second estimate is a paid Cauchy error, not a differentiation of the
natural-cutoff approximation.

### Preliminary inequalities

The elementary bounds \(4\pi<13\), \(e^{67/2}<4\cdot10^{14}\), and

\[
q_->9\cdot10^{15}/13>4\cdot10^{14}
\]

give \(\ell>67/2\). Also every natural cutoff is greater than \(10^7+1\).
The largest squared cutoff parameter on the disk and time interval differs
from the smallest by

\[
q_+-q_-+(3/10-1/5)/16=1/(40\pi)+1/160<1.
\]

Their square roots differ by less than one, so all natural cutoffs are in
\(\{N,N+1\}\). For every index up to the largest cutoff,

\[
\log n\le\ell/2+\rho,\qquad
\rho=\tfrac12\log\left(1+\frac{1/(40\pi)+3/160}{q_-}\right)<10^{-16}. \tag{B}
\]

On this disk the source's positive-part correction in (21) vanishes:

\[
1-3y+4y(1+y)/(\Re z)^2<0.
\]

Consequently, for \(p_n(s)=\exp\{(t/4)\log^2n-(s+t\alpha(s)/2)\log n\}\),

\[
|p_n(s)|\le n^{-37/40-(1/20)(\ell-\log n)}\le n^{-7/4},\qquad
\sum_{n=1}^{m}|p_n(s)|\le1+\int_1^\infty u^{-7/4}\,du=7/3. \tag{C}
\]

Here \(m\) can be any natural cutoff or the larger cutoff \(N+1\).
The exponent before the negligible \(\rho\) loss is at least
\(37/40+67/80=141/80>7/4\).

At an actual source point \(z=u+iy\), its reflected modulus multiplier is

\[
|\gamma|m^{|\kappa|}n^y
\le e^{0.02y}\left(\frac{m^2}{u/(4\pi)}\right)^{y/2}
e^{|\kappa|\log m}<1.03. \tag{D}
\]

The same inequality holds with the paid crossing index \(n=N+1\) in
place of \(m\). In either case (B) bounds the quotient of the squared
index and the least \(q\) by \(e^{2\rho}\), while

\[
|\kappa|\log m\le\frac{(3/10)(19/20)}{2(h-6)}\log m<10^{-14}.
\]

For the last inequality use \(\log m\le\log h\) and the decreasing
function \((\log h)/h\), with \(h>9\cdot10^{15}\) and
\(\log(9\cdot10^{15})<37\). Thus the exponent in (D) is less than
\(.019+10^{-14}+\rho<.02\), and
\(e^{.02}\le50/49<103/100\).

### The source (A+B) error

For \(1\le n\le m\),

\[
\left|\log\frac{u}{4\pi n^2}\right|\le\log\frac{u}{4\pi}<\log u.
\]

Indeed the possible negative endpoint logarithm has magnitude at most
\(\log(1+t/(16q))\), which is much smaller than \(\log q\).
The exponent in Polymath (23) is at most

\[
v(u)=\frac{.006(\log u)^2+1}{.99u}<1.1\cdot10^{-15}. \tag{E}
\]

The displayed majorant is decreasing for \(u\ge9\cdot10^{15}\).
At its least endpoint use \(\log(9\cdot10^{15})<37\) to obtain the
last numerical inequality. Since \(e^v-1\le v/(1-v)<1.12\cdot10^{-15}\),
(C)--(D) and \((203/100)(7/3)<5\) imply

\[
e_A+e_B<10^{-14}. \tag{F}
\]

### The source (C) error

The two positive corrections in Polymath (24) have sum less than
\(10^{-6}\). The first is at most
\(1.24(3+1)/(m-.125)<5\cdot10^{-7}\); the second is at most

\[
\frac{3\log u+16}{.99u}<2\cdot10^{-14}.
\]

For the numerator use \(\pi<22/7\) and
\(\sqrt{L^2+\pi^2/4}\le L+\pi/2\), with \(L=\log(u/(4\pi))\).
Its negative exponent has magnitude at least

\[
\frac{37}{80}\ell+\frac1{80}\ell^2
\ge\frac{9447}{320}=29.521875.
\]

Therefore

\[
e_{C,0}<e^{-29.5}<2\cdot10^{-13}. \tag{G}
\]

### The complete cutoff jump

If the source cutoff is \(N+1\), its exact difference from \(f_{t,N}\)
is \(p_{N+1}(s)+\gamma p_{N+1}(1-s)\). The jump index satisfies

\[
\ell/2<\log(N+1)\le\ell/2+\rho.
\]

Writing \(v=\log(N+1)\), the identity
\(v^2-\ell v=(v-\ell/2)^2-\ell^2/4\) gives

\[
|p_{N+1}(s)|\le
\exp\{-37\ell/80-\ell^2/80+\rho^2/20\}
<e^{-29.5}<2\cdot10^{-13}. \tag{H}
\]

The source's exact analytic rewriting implies

\[
|\gamma p_{N+1}(1-s)|
\le|\gamma|(N+1)^y(N+1)^{|\kappa|}|p_{N+1}(s)|
<1.03|p_{N+1}(s)|.
\]

Thus the complete jump has modulus less than
\(2.03\cdot2\cdot10^{-13}<5\cdot10^{-13}\). Paying (F), (G), and
this jump proves the first part of (A). The holomorphic fixed-cutoff
remainder and the radius \(r=1/20\) then give the second part by Cauchy.
None of these estimates requires a relative lower bound for \(H_t\).

## 2. Audit of the finite polynomial and the logarithmic derivative

The companion main proof splits at index 16. I checked the following
inequalities independently:

* The main polynomial obeys \(n^{-12/5}\) below the split and
  \(n^{-7/4}\) above it. Its modulus tail is less than
  \(1319/2100<2/3\), and its logarithm-weighted tail is less than
  \(559/450<5/4\). The sum-to-integral comparisons apply to decreasing
  functions starting at the specified endpoints.
* The derivative formula
  \(p_n'(z)=(i/2)(1+t\alpha'(s)/2)(\log n)p_n(s)\)
  yields \(|P'|<63/100\). The derivative is of the fixed polynomial.
* The reflected polynomial obeys powers \(n^{-3/2}\) and
  \(n^{-17/20}\) on the two index ranges. Combined with
  \(|\gamma|\le(103/100)e^{-17\ell/40}\), this gives
  \(|R|<(103/100)(3e^{-17\ell/40}+7e^{-7\ell/20})<10^{-4}\).
  The direct analytic derivative bound
  \(|\gamma'/\gamma|\le\ell\) and the corresponding polynomial
  derivative bound yield \(|R'|<1/100\). The integrated note instead applies Cauchy to the whole-disk reflected
  bound \(7519/10^8\), obtaining the sharper center derivative bound
  \(7519/(5\cdot10^6)<1/500\). This simplification passes the audit.
* The direct normalizer formula gives
  \(-\Im B_t'/B_t=\Re m_t'(s)/2\), with the correct sign. The
  displayed lower bound \(67/8-1/2000\) includes the heat correction.
  The logarithmic derivative decomposition
  \(H_t'/H_t=B_t'/B_t+U_t'/U_t\) is applied only after the polynomial
  bounds and (A) prove \(U_t\ne0\).

In particular, even the looser error tolerance \(10^{-4}\) used in the
companion proof is valid both for the normalized value and the normalized
derivative. Its estimates imply

\[
|U_t|>33/100,\qquad |U_t'|<13/20,\qquad
L_{9/10}(t,x)>67/8-1/2000-2=12749/2000>6.
\]

I found no substantive gap in this conclusion. The integrated note proves (A) in Section 5 and applies Cauchy only to
the resulting holomorphic fixed-cutoff remainder.

## 3. Attraction consequence and scope

For a simple maximal-height nonreal zero with \(y\le1/5\) and

\[
1/5\le t\le3/10,\qquad |\Re z|\ge10^{16},
\]

Note 6's exact-field comparison has factor one, since
\((9/10)/y\ge9/2>\sqrt5\). It yields

\[
E_t(z)\ge\frac{20}{3}-\frac{200}{77}=\frac{940}{231}>4.
\]

Evenness transfers the positive-\(x\) result to negative \(x\).
This is a fully effective attraction estimate in an unbounded height
sector. It is not a global floor: lower real parts must have a separate
estimate, and any zero-location assumptions in a global endpoint remain
separate hypotheses. No current best Newman bound or progress to
time zero is asserted by this high-sector audit. The global implication
below uses an additional proved symmetry floor.

## 4. Exact scalar verification

Eleven independent rational checks passed in a short one-off Python
calculation. They include the exponent \(9447/320\), the source-weight
sum, the endpoint exponent bounds, and \(940/231\). For exponential
bounds, the lower bound is the rational Taylor sum through degree 120;
the upper bound adds the geometric-tail majorant

\[
\frac{a^{121}/121!}{1-a/122}
\]

for positive rational \(a<122\). This verifies in particular

\[
e^{29.5}>5\cdot10^{12},\quad
e^{33.5}<4\cdot10^{14},\quad e^{37}>9\cdot10^{15},
\]

and the two reflected-polynomial endpoint exponent inequalities.
These are exact scalar checks; they evaluate no heat function, zero,
or parameter grid. The analytic approximation theorem remains an
imported proof input.


## 5. Separate audit of the global patch

At a simple maximal nonreal zero \(z=x+iy\), \(x,y>0\), its reflected
pair \(-x\pm iy\) is external and contributes exactly
\(1/[2(x^2+y^2)]\) to both \(E\) and \(G\). The positivity of the
cosine kernel at imaginary arguments excludes \(x=0\). Other grouped
exact-field contributions are nonnegative at global maximal height.

On \(0<x\le X=10^{16}\), symmetry supplies
\(E\ge1/[2(X^2+w)]\). On \(x\ge X\), the newly proved \(E>4\)
is larger than that same floor. Evenness covers the negative half-line.
This gives a complete global floor without requiring that a maximizing
zero remain on one side of the cutoff. Combining the bounds by a spatial
minimum is valid; adding their values would double-count possible roots.

For \(a=X^2\), differentiation gives

\[
 M_a(w)=w/4+(a/8)\log(1+2w/a),\quad
 M_a'(w)=\frac{a+w}{2(a+2w)}
 =\frac1{2+2w/(a+w)}.
\]

This is exactly the reciprocal speed for the patched floor. Also

\[
 w/2-M_a(w)=\int_0^w\frac{u}{2(a+2u)}\,du
 \ge\frac{w^2}{4(a+2w)}.
\]

At \(w_0=1/25\) the rational gain is \(1/(2500a+200)\).
The interval \([1/5,3/10]\) covers the full possible landing duration,
which is less than \(w_0/2=1/50\). Maximum switching, absolute continuity,
and local multiple-root continuation use Note 6's already stated arguments
and the imported zero dynamics. The qualitative eventual-reality theorem
supplies compactness; no unpublished effective counting constant is needed.

The proof of [Polymath, Theorem 1.1 via Proposition 3.3](https://arxiv.org/html/1904.12438#S3.Thmproposition3)
provides the actual canopy \(W(1/5)\le1/25\). Its finite RH verification,
barrier at \(6\cdot10^{10}+83951.5\) through time \(1/5\), and final
canopy are accepted published proof inputs. This establishes the required
starting envelope; the bare bound \(\Lambda\le0.22\) would not.
Thus the complete deduction relative to those accepted inputs is

\[
 \Lambda\le11/50-1/(2500\cdot10^{32}+200).
\]

Its approximate gain \(4\cdot10^{-36}\) is mathematically positive and
practically negligible. The review treats the effective high-sector estimate
and spatial accounting as the milestone, and makes no record or literature
novelty claim.

The endpoint \(1/5+\log(33/25)/16\approx0.217352\) follows only if the
maximizing population is controlled by \(E\ge4\) throughout landing.
The high-sector estimate at \(X=10^{16}\) does not prove this extra global
premise. The integrated note correctly labels that endpoint conditional.
A stronger earlier-time canopy cannot be deduced backward from either
endpoint.

## 6. Replay boundary and disposition

The [scalar checker](../numerics/check_effective_collective_probe.py) and
[small record](../numerics/effective_collective_probe_record_20261009.json)
check fixed elementary reserves and landing algebra. Exact rational and
Taylor inequalities provide deterministic arithmetic; no heat function,
zero, phase, or parameter grid is evaluated. All 105 exact assertions pass. Two complete executions reproduced the
record byte-for-byte, and its checker hash matches the finalized script. It identifies arithmetic
replay, not independent specialist validation of the analytic proof.

Disposition: the effective high-sector result and global mirror implication
pass the scoped internal review. The substantial remaining issue is the
lower spatial sector. A bounded next target is \(E\ge1\) at the published
barrier using a \(99/100\) probe and radius \(1/200\), a finite head and
logarithmic integral tails, on \([1/5,11/50]\). Any later two-envelope gain
still needs a smaller left envelope and a proved continuation of the barrier;
the published barrier ends at time \(1/5\).
