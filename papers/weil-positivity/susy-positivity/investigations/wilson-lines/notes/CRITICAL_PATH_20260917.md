# The critical path in $(\omega,L)$, read through the inner function

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note,
continuing Section 5.1 of the
[inner-function note](INNER_FUNCTION_AND_RESONANCE_20260917.md) at the
investigator's direction, against the critical-path material of the
`papers/shifted-zeta` program:
[`storage-depth/archive/background/1-critical_path_research.md`](../../../../shifted-zeta/storage-depth/archive/background/1-critical_path_research.md)
and
[`2-cumulative_storage_path.md`](../../../../shifted-zeta/storage-depth/archive/background/2-cumulative_storage_path.md),
both 10 September 2026.

**No manuscript change has been made.** Section 7 lists what this note
recommends. Sections 2 and 3 are the results; Section 6 corrects a claim of my
own earlier note.

---

## 0. Summary

1. **The contraction region has no boundary.** $L\mapsto\lVert V_{\omega,L}\rVert$
   is nondecreasing with supremum $\lVert V_\omega\rVert_{L^2(\mathbb R)}$, and
   that supremum is **1 or $\infty$, with nothing between**. For each $\omega$,
   contraction at every $L$ is *equivalent* to $\xi$ having no zero at distance
   more than $\omega$ from the critical line. So under RH the region is the
   entire quadrant: the critical path of the contraction condition does not
   exist, and the whole content sits at $L=\infty$.
2. **The generator region does have a boundary, and it is an artifact.** Its
   observed location $\omega_*(L)\asymp\sqrt{m_L}$ is explained here: the
   quantity $\kappa_L$ of the earlier note is an inverse **zero-placement
   precision**, and $\kappa_L\sqrt{m_L}$ is nearly constant --- $0.0144$,
   $0.0077$, $0.0061$ across twenty orders of magnitude in $m_L$ on the three
   recorded horizons. That boundary collapses superexponentially **even under
   RH**, so its collapse carries no arithmetic information.
3. **The gap is eleven orders of magnitude at $L=\log7$ and widens
   superexponentially.** The generator criterion is available at $\log7$ only
   for $\omega<4\times10^{-12}$, while anything detectable there needs
   $\omega\sim1/L\approx0.5$. This is the quantitative reason the earlier
   program became numerical and stalled: it was tracking the slack of a
   sufficient condition, not the arithmetic.
4. **The Cayley coordinate of the cumulative note is the classical
   positive-real criterion.** On the critical line
   $(1-K_\omega)/(1+K_\omega)=i\tan\Psi$ exactly --- purely imaginary, verified
   to 26 digits --- so the cumulative-storage object is "$K_\omega$ inner
   $\iff$ $Z_\omega$ positive-real", which is the Krein--Nevanlinna circle where
   the companion investigation's top open item already lives.

A useful negative by-product: **the sufficient generator path should not be
revived**, and the $(\omega,L)$ numerics should be reorganized as a *disproof*
search, which is the only thing monotonicity in $L$ permits them to be.

## 1. What the earlier program set up

For the reader who has not opened those files. With $Q=Q_{0,L}$, $X$ centred
coordinate multiplication, $C_\omega=\cosh(\omega X)$, $S_\omega=\sinh(\omega X)$,
$T_\omega=\tanh(\omega X)$:

- **the hyperbolic identity** $Q_{\omega,L}[f]=Q[C_\omega f]-Q[S_\omega f]$, and
  the congruence $Q_{\omega,L}=C_\omega(Q-T_\omega QT_\omega)C_\omega$;
- **the exact generator criterion** $Q_{\omega,L}\succeq0\iff\lVert T_\omega\rVert_{Q\to Q}\le1$;
- **the sufficient path** $\omega\kappa_L<\pi/4$ with
  $\kappa_L=\lVert X\rVert_{Q\to Q}$, giving
  $Q_{\omega,L}\succeq\cos(2\omega\kappa)Q$ and
  $\lVert V_{\omega,L}\rVert\le\exp[-(m/2\kappa)\sin(2\kappa\omega)]<1$;
- **a depth recursion** for $m_L$, the normalized cross coupling $c$, and
  $\kappa_L$, with an explicit but ruinous extension lemma (extension lengths
  $\sim e^{-\mathrm{const}/m_L}$);
- **a certified witness**: at $L=\log7$, $\omega=10^{-11}$, an explicit degree
  $\le126$ polynomial has $Q_{\omega,L}[f]/\lVert f\rVert^2\in(-2.999,-2.998)\times10^{-27}$,
  so *generator* positivity fails there, while the cumulative defect on the same
  input is positive;
- **a two-sector model** showing a local path can simply end at a finite $L_*$;
- **the Cayley/cumulative coordinates** $Z_{\omega,L}=(I-V)(I+V)^{-1}$,
  $P=\frac2\omega\operatorname{Re}Z$, $D=\frac\omega2(I+V^*)P(I+V)$, so
  $P\succeq0\iff\lVert V\rVert\le1$, with causal symbol
  $a_{\rm cum,\omega}(p)=\frac2\omega\frac{1-K_\omega(p)}{1+K_\omega(p)}$.

**Attribution.** The hyperbolic identity is this earlier note's, from 10
September. Proposition 5.1 of the wilson-lines manuscript rediscovered it
independently on 17 September, deriving it from the generator rather than from
the kernel; the two agree and the priority is the earlier one. The manuscript
should cite it, which is item 1 of Section 7 below.

## 2. The contraction region has no boundary

Recall from the inner-function note that $|K_\omega(i\tau)|=1$ identically, and
that under RH $K_\omega$ is inner on $\operatorname{Re}p\geq0$ with poles at
$\operatorname{Re}p=-\omega$.

> **Proposition A (monotonicity).** For each fixed $\omega$,
> $L\mapsto\lVert V_{\omega,L}\rVert$ is nondecreasing, and
> $\sup_L\lVert V_{\omega,L}\rVert=\lVert V_\omega\rVert_{L^2(\mathbb R)}$.

*Proof.* $V_{\omega,L}=P_LV_\omega P_L$ and the intervals are nested, so for
$L<L'$ the first is a compression of the second and its norm is no larger.
$P_L\to I$ strongly, so $\lVert P_LV_\omega P_Lf\rVert\to\lVert V_\omega f\rVert$
for each $f$, giving the supremum. $\square$

> **Proposition B (dichotomy).** Fix $\omega\in(0,\frac12]$ and suppose no zero
> of $\xi$ has $|\operatorname{Re}\rho-\frac12|=\omega$ exactly. Then
> \[
>  \sup_L\lVert V_{\omega,L}\rVert=
>  \begin{cases}1,&\text{if $\xi$ has no zero with }|\operatorname{Re}\rho-\tfrac12|>\omega,\\
>  \infty,&\text{otherwise.}\end{cases}
> \]

*Proof.* The poles of $K_\omega$ are at $p=\rho-\frac12-\omega$, so a pole lies in
$\operatorname{Re}p>0$ exactly when some $\operatorname{Re}\rho>\frac12+\omega$;
by the functional equation that is the same as some
$|\operatorname{Re}\rho-\frac12|>\omega$. If there is none, $K_\omega$ is analytic
and bounded on $\operatorname{Re}p\geq0$ and unimodular on the boundary, the
inverse Laplace contour may be moved to the imaginary axis, and $V_\omega$ is the
Fourier multiplier by $K_\omega(i\cdot)$, of norm exactly 1. If there is one, at
$\operatorname{Re}p=\delta-\omega>0$, the contour shift picks up a residue and
$k_\omega$ acquires a component growing like $e^{(\delta-\omega)x}$, so
$V_\omega$ is unbounded on $L^2(\mathbb R)$. $\square$

> **Corollary C.** For each $\omega$, the following are equivalent:
> (i) $\lVert V_{\omega,L}\rVert\le1$ for every $L>0$;
> (ii) $\xi$ has no zero with $|\operatorname{Re}\rho-\frac12|>\omega$.
> In particular, **under RH the contraction region is the whole quadrant
> $(0,\frac12]\times(0,\infty)$.**

This is Proposition 4 of the inner-function note, upgraded from a sketch to a
statement with a proof and a dichotomy, and it settles the critical-path question
for the contraction condition:

> **There is no critical path.** Under RH the region is everything and has no
> boundary; if RH fails at distance $\delta$, the region is everything for
> $\omega>\delta$ and, for $\omega<\delta$, is cut off at a finite $L$. The
> $(\omega,L)$ plane has no curve in it whose shape is worth computing: the
> $L$-direction is monotone bookkeeping and the entire content is the $L=\infty$
> limit, which is the $H^\infty$ norm of $K_\omega$.

### 2.1 The one thing the plane is good for

Monotonicity cuts one way, and it is worth saying which.

> A finite computation exhibiting $\lVert V_{\omega,L}\rVert>1$ at a single
> $(\omega,L)$ proves that $\xi$ has a zero at distance more than $\omega$ from
> the critical line. A computation showing $\lVert V_{\omega,L}\rVert\le1$ at any
> finite $L$ proves nothing at all.

So the $(\omega,L)$ numerics are a **disproof instrument**, exactly like the
Collatz--Wielandt disproof test of the companion investigation, and they should
be organized as one: certified *lower* bounds on Rayleigh quotients, scanning
$\omega$ downward and $L$ upward, looking for a value above 1. Certified upper
bounds --- which is what most of the recorded effort produced --- are on the side
that certifies nothing. This is the same one-sidedness lesson the
source-selection-rules investigation records as method note E.

It also explains the shape of Proposition 1.1 of the background. Its two limits do
different jobs: $L_j\to\infty$ realizes the supremum of Proposition A, and
$\omega_j\downarrow0$ closes the detection threshold of Corollary C.

## 3. The generator boundary: $\kappa_L$ is an inverse zero-placement precision

The generator condition $Q_{\omega,L}\succeq0$ is strictly stronger than
contraction --- the earlier program's own witness shows it failing at
$(\log7,10^{-11})$ where the cumulative defect is positive --- and it *does* have
a boundary. Here is what that boundary is.

Use the spectral form $Q[f]=\sum_\rho|\widehat F(\gamma_\rho)|^2$. Under
$X_af=(x-a)f$, $\widehat{X_af}=i\widehat F{}'-a\widehat F$, so
\[
 Q[X_af]=\sum_\rho\big|i\widehat F{}'(\gamma_\rho)-a\widehat F(\gamma_\rho)\big|^2 ,
\]
and on a near-null vector, where $\widehat F$ is small at every $\gamma_\rho$, the
second term drops out whatever $a$ is. (That is also why the earlier note found
the centring $a$ to matter only mildly.) Hence
\[
 \boxed{\ \kappa_L^2=\sup_f\frac{\sum_\rho|\widehat F{}'(\gamma_\rho)|^2}
 {\sum_\rho|\widehat F(\gamma_\rho)|^2}\ }
\]
--- the ratio of derivative samples to value samples of $\widehat F$ **at the
Riemann zeros**.

Now let $e_L$ be the ground vector, $Qe_L=m_Le_L$, and let $\varepsilon_L$ be the
root-mean-square distance from the zeros of $\widehat e_L$ to the nearest
$\gamma_\rho$, weighted by $|\widehat e_L'(\gamma_\rho)|^2$. Then
$\widehat e_L(\gamma_\rho)\approx\varepsilon_L\widehat e_L'(\gamma_\rho)$, so
\[
 m_L\approx\varepsilon_L^2\,Q[Xe_L],\qquad
 \kappa_L\approx\varepsilon_L^{-1},\qquad\text{hence}\qquad
 \boxed{\ \kappa_L\sqrt{m_L}\approx\sqrt{Q[Xe_L]}\ }
\]
with the right-hand side an ordinary, slowly varying quantity.
**$\kappa_L$ is an inverse zero-placement precision: it measures how accurately a
function supported in $I_L$ can put its own spectral zeros on the Riemann
zeros.**

The recorded values test this across twenty orders of magnitude:

| horizon | $m_L$ | $\kappa_L$ | $\kappa_L\sqrt{m_L}$ | $\pi/(4\kappa_L)$ | recorded root | root$/\sqrt{m_L}$ |
|---|---|---|---|---|---|---|
| $\log3$ | $5.537\times10^{-8}$ | $6.112\times10^{1}$ | 0.01438 | $1.29\times10^{-2}$ | $1.64\times10^{-2}$ | 69.7 |
| $\log5$ | $9.293\times10^{-18}$ | $2.534\times10^{6}$ | 0.00773 | $3.10\times10^{-7}$ | $3.95\times10^{-7}$ | 129.5 |
| $\log7$ | $6.802\times10^{-28}$ | $2.326\times10^{11}$ | 0.00607 | $3.38\times10^{-12}$ | $4.30\times10^{-12}$ | 164.9 |

$\kappa_L\sqrt{m_L}$ moves by a factor of 2.4 while $m_L$ moves by $10^{20}$, and
the earlier note's own diagnostic root sits within a factor of 1.3 of
$\pi/(4\kappa_L)$ at all three horizons. So the generator boundary is
\[
 \omega_*(L)\approx\frac{\pi}{4\kappa_L}\asymp\sqrt{m_L},
\]
up to a slowly growing factor.

**The consequence is the point of this section.** $m_L$ collapses
superexponentially --- and it does so *under RH*, since $m_L=\lambda_{\min}(Q_{0,L})$
is positive precisely when RH holds on $I_L$. So the generator region's boundary
collapses to zero even in the world the program is trying to prove. **It is a
property of the sufficient condition, not of $\zeta$.** Any "critical path"
extracted from it is measuring slack.

## 4. The gap, and why the earlier program stalled

How small may $\omega$ be and still be *useful*? By Proposition B, a zero at
distance $\delta$ makes the kernel grow like $e^{(\delta-\omega)x}$, so it becomes
visible on $I_L$ only once $(\delta-\omega)L\gtrsim1$. Taking $\omega\sim\delta/2$,
the working curve is $\omega\sim1/L$ --- a power law. Against the generator
boundary:

| horizon | $1/L$ | $\pi/(4\kappa_L)$ | ratio |
|---|---|---|---|
| $\log3$ | 0.910 | $1.29\times10^{-2}$ | $7.1\times10^{1}$ |
| $\log5$ | 0.621 | $3.10\times10^{-7}$ | $2.0\times10^{6}$ |
| $\log7$ | 0.514 | $3.38\times10^{-12}$ | $1.5\times10^{11}$ |

Eleven orders of magnitude at $L=\log7$, and the ratio grows like
$\sqrt{1/m_L}/L$, superexponentially. The two curves are not close and are
diverging. That is the quantitative content of the earlier note's own remark that
its extension lemma "asks for extension lengths roughly
$\exp(-\mathrm{const}/m_L)$", and of its Section 7 warning that a local path need
not reach unbounded depth.

**Recommendation: do not revive the sufficient generator path.** Section 2 says
the cumulative path is the one with content, and that its content is entirely in
the $L\to\infty$ limit.

## 5. The Cayley coordinate is the positive-real criterion

The cumulative note's Section 2 is, I think, the most valuable part of the older
material, and the inner function identifies what it is.

Since $|K_\omega(i\tau)|=1$ and $K_\omega(i\tau)=e^{-2i\Psi}$ with
$\Psi=\arg\xi(\frac12+\omega+i\tau)$,
\[
 \frac{1-K_\omega(i\tau)}{1+K_\omega(i\tau)}
 =\frac{e^{i\Psi}-e^{-i\Psi}}{e^{i\Psi}+e^{-i\Psi}}
 =i\tan\Psi(\tau,\omega),
\]
**purely imaginary on the critical line.** The Cayley transform carries the unit
circle to the imaginary axis, so the cumulative symbol is a *reactance* there.
Verified: at $\omega\in\{0.4,0.1,0.01\}$ and
$\tau\in\{3,14.5,40,101.7\}$, $|\operatorname{Re}Z|<1.4\times10^{-26}$ and
$|Z-i\tan\Psi|<3.6\times10^{-25}$ at 25 digits.

Consequently:

> $\lVert V_{\omega,L}\rVert\le1$ for all $L$ $\iff$ $Z_\omega=(I-V_\omega)(I+V_\omega)^{-1}$
> is **accretive**, i.e. $a_{\rm cum,\omega}$ is a **positive-real function** of
> $p$ on the right half-plane $\iff$ $K_\omega$ is inner.

That is the classical passivity/impedance criterion, and positive-real functions
are Nevanlinna functions after rotation, with a Herglotz representation. So the
cumulative-storage object sits in the **Krein--Nevanlinna circle**, which is
exactly where the companion investigation's top-ranked open item lives: Suzuki's
screw-function and de Branges work, item A1 of its open directions. Two
independent routes now point at the same literature, which is the strongest
argument yet for reading it.

Two cautions, both instances of the trap recorded in Section 1.1 of the
inner-function note.

- $a_{\rm cum,\omega}$ is purely imaginary on the imaginary axis, so **its real
  part --- the entire form --- is carried by the poles crossed when the Laplace
  contour is moved there.** Any expansion performed on the imaginary axis loses
  it. The earlier note's expansion (7),
  $a_{\rm cum}=a_0+\omega^2(a_0''/6-a_0^3/12)+O(\omega^4)$, is taken "on a
  sufficiently far right Laplace line" and is therefore safe as stated; it must
  not be evaluated at $p=i\tau$ term by term.
- The natural tool for a positive-real function is its Herglotz representation,
  not a Taylor expansion in $\omega$. The measure in that representation is
  supported on the resonances --- the zeros --- which is the same statement as
  Proposition 3 of the inner-function note.

## 6. A correction to the inner-function note

Section 6 of that note proposed that the superexponential collapse of $m_L$ is
prolate leakage at bandwidth $\gamma_1$. **That is too simple.** The recorded
values give
\[
 \frac{d\log m_L}{dL}\approx-44\ \ (\log3\to\log5),\qquad
 \approx-69\ \ (\log5\to\log7),
\]
against the bandwidth-$\gamma_1$ prolate rate of $-\gamma_1=-14.13$. The observed
decay is far steeper and is steepening.

The corrected reading is Section 3 above: bandlimiting below $\gamma_1$ is only
the first factor, and the second is the zero-placement precision,
$m_L\approx\varepsilon_L^2Q[Xe_L]$. The mechanism question is therefore **how
$\varepsilon_L$ collapses**, not how prolate leakage does. The three slopes are
consistent with $\log m_L\sim-\alpha L^2$, $\alpha\approx16$ to $19$ --- *this is
numerology on three points and must not be quoted as a fit*, but it is the right
shape to test, and it would follow from $\varepsilon_L$ decaying geometrically per
unit of Nyquist count, since that count itself grows linearly in $L$.

## 7. Recommendations

For a later pass; nothing has been changed.

1. **Cite the earlier note** for the hyperbolic identity in manuscript
   Proposition 5.1, as an independent rediscovery.
2. **Replace the manuscript's Problem 8.1 with Corollary C**, which is stronger
   than the three arguments of the inner-function note's Section 5 and subsumes
   them: the contraction region is the whole quadrant under RH.
3. **Add Section 2.1 as a method remark** --- the $(\omega,L)$ plane is a disproof
   instrument and only certified lower bounds above 1 carry information.
4. **Add Section 3's reading of $\kappa_L$**, which is cheap, explains a
   twenty-order-of-magnitude numerical law, and retires the generator path.
5. **Fold Section 5 into whatever the manuscript says about Suzuki**: the
   cumulative criterion is positive-realness, and that is a second independent
   reason to read arXiv:2301.00421.
6. **Replace item 6 of the inner-function note's Section 9** (the prolate
   reference) with the $\varepsilon_L$ question of Section 6 above.

## 8. Status of each claim

- **Propositions A and B and Corollary C** are written proofs. B's second case
  rests on the residue/growth argument, stated without an estimate on the
  residue; its conclusion that the supremum is infinite does not need one.
- **Section 3**'s identity for $\kappa_L^2$ is exact. The relation
  $\kappa_L\sqrt{m_L}\approx\sqrt{Q[Xe_L]}$ is a **heuristic with a
  single-order-parameter derivation**, supported by three recorded data points;
  it is not proved, and $\varepsilon_L$ is defined only up to the weighting
  stated.
- **Section 4**'s detection scale $\omega\sim1/L$ is a **heuristic** from the
  growth rate in Proposition B, not an estimate. The tabulated ratios are
  arithmetic on recorded values.
- **Section 5**'s identity $i\tan\Psi$ is exact given Proposition 1 of the
  inner-function note; the positive-real reading is classical. Verified
  numerically at twelve points to 25 digits.
- **Section 6**'s corrected mechanism is a **proposal**; the $\alpha L^2$ shape is
  numerology on three points and is labelled as such.
- All numerics here are either arithmetic on values recorded in the
  `papers/shifted-zeta` program, or `mpmath` computations run outside the
  repository. Neither is a registered check programme. The `mpmath` ones belong
  in `numerics/exploratory/` on the next pass.
