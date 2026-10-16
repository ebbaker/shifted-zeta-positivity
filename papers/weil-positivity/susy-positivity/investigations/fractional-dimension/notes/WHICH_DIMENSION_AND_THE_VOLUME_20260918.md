# Which coordinate carries the dimension, and the correction as a volume term

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Second note of the fractional-dimension investigation, carrying out
items 1 and 3 of the [opening note's](OPENING_NOTE_20260918.md) plan: deciding
between the Euclidean dimension $2\omega$ and the hyperbolic dimension $\omega$,
and asking whether the Blaschke factor's pole is a volume. Programmes:
[`check_which_dimension.py`](../numerics/check_which_dimension.py) (56 cases) and
[`check_residue_volume.py`](../numerics/check_residue_volume.py) (27 cases), both
standard library, with records beside them.

**Nothing here is a positivity statement and nothing here is about the zeros.**

---

## 0. Summary

1. **The dimension is $2\omega$, and the factor of two was a coordinate
   artifact.** $\tau=\log|t+i|$ is a *Busemann* function on the horocycle, not a
   distance: the hyperbolic distance from $i$ to $t+i$ is
   $d_H=2\operatorname{arcsinh}(t/2)$, which tracks the **Euclidean radius**
   $r=|t|$ at small scale ($d_H\sim r$) and $2\tau$ at large scale, while
   $\tau\sim r^2/2$ near the origin. A measure with local exponent $r^{2\omega-1}dr$
   therefore has local exponent $\tau^{\omega-1}d\tau$; the two normalized limits
   differ by exactly $2^{1-\omega}$, the Jacobian of that square, and that is the
   entire difference between the two readings (Proposition 1.1).
2. **In the true distance both readings agree, and name the same space.** With
   $u=d_H/2$, so that $r=2\sinh u$, Lebesgue measure on $\mathbb R^{2\omega}$
   becomes $2^{2\omega}|S^{2\omega-1}|(\sinh u)^{2\omega-1}\cosh u\,du$, which is
   the radial Jacobian of **complex hyperbolic space of complex dimension
   $\omega$ and real dimension $2\omega$**. In Jacobi/Heckman--Opdam parameters:
   $(\alpha,\beta)=(\omega-1,0)$ with $\rho=\omega>0$ in the true distance,
   against $(\frac\omega2-1,-\frac12)$ with $\rho=\frac{\omega-1}2<0$ in the
   Busemann coordinate. Only the first has $\rho>0$, and only the first accounts
   for every factor of the kernel; the Busemann reading leaves $e^{\tau/2}$ over
   (Proposition 2.1).
3. **And the comb has no coordinate at all.** Its offset in
   $\zeta(2s-d)/\zeta(2s)$ and the exponent in its Jordan-totient weights are
   $d=2\omega$, with no radial variable in which to re-read them. Since comb and
   archimedean factor multiply to make $\Lambda(2s-d)/\Lambda(2s)$, they carry
   the same dimension. That settles it independently of any geometry
   (Section 2.3).
4. **So "the shift is half a dimension" is exact, with the halving named**:
   $2\omega$ is the real dimension and $\omega$ the complex one. With the caveat
   of Section 2.4 --- the complex reading is a parametrization, not a space: $CH^\omega$
   exists only at integer $\omega$, which the family never reaches, whereas the
   real dimension $2\omega$ reaches the integer $1$ exactly once, at
   $\omega=\frac12$, where the object is the horocycle $\mathbb R$ of the modular
   surface and has no complex structure at all.
5. **The correction is a volume term, and its coefficient is computable as one.**
   The single pole of the Markov part in the right half-plane sits at
   $p=b=\frac{d+1}2$ --- exactly where the Blaschke factor cancels it --- with
   \[
    \operatorname*{Res}_{p=b}\widetilde K_\omega
    =\frac{\pi^{(d+1)/2}}{\Gamma\!\big(\frac{d+1}2\big)\zeta(d+1)}
    =\frac{\lvert S^{d}\rvert}{2\,\zeta(d+1)} .
   \]
   Both factors belong to dimension $d+1$: $\lvert S^d\rvert$ is the unit sphere
   of $\mathbb R^{d+1}$ and $1/\zeta(d+1)$ the density of primitive vectors in
   $\mathbb Z^{d+1}$. **The lattice has rank $d+1$ and its cusp a horocycle of
   dimension $d$** --- differing by one, as a cusp must. At $d=1$ the residue is
   $6/\pi=2/\mathrm{vol}(PSL(2,\mathbb Z)\backslash\mathbb H)$, recovering the
   classical $\operatorname{Res}_{s=1}\varphi=1/\mathrm{vol}$ (Proposition 3.1).
6. **The dictionary is now closed on all three entries**, and every one of them
   points at a single object: a rank-$(d+1)$ lattice in $\mathbb R^{d+1}$ whose
   cusp integrates over a $d$-dimensional horocycle, $d=2\omega$. At $d=1$ that
   object is $\mathbb Z^2\subset\mathbb R^2$ and the modular surface. Whether it
   means anything at fractional $d$ is now the whole question, and it has a
   sharper form than before: **a lattice rank is a cardinality**, while $J_d$ and
   $1/\zeta(d+1)$ are defined for every $d$ (Section 5).

---

## 1. $\tau$ is a Busemann coordinate, not a distance

The archimedean kernel is
$k^\Gamma_\omega(\tau)=\lvert S^{2\omega-1}\rvert(2\sinh\tau)^{\omega-1}e^{\tau/2}$,
and the ambiguity of the opening note was that $(\sinh\tau)^{\omega-1}$ is the
radial Jacobian of a real hyperbolic space of dimension $\omega$, half the
$2\omega$ of the prefactor and of the Riesz representation. The resolution is
that $\tau$ is not a distance.

> **Proposition 1.1.** On the horocycle $\{y=1\}$ of the upper half-plane, the
> hyperbolic distance from $i$ to $t+i$ is
> \[
>  d_H(i,t+i)=\operatorname{arccosh}\Big(1+\tfrac{t^2}2\Big)=2\operatorname{arcsinh}\frac t2 ,
> \]
> while $\tau=\log|t+i|=\frac12\log(1+t^2)$. Hence $d_H\sim r$ and $\tau\sim r^2/2$
> as $r=|t|\to0$, and $d_H\sim2\tau$ as $r\to\infty$. Consequently a
> rotation-invariant measure with density $\propto r^{2\omega-1}$ in $r$ has
> density $\propto\tau^{\omega-1}$ in $\tau$, and the two normalized limits differ
> by exactly $2^{1-\omega}$.

*Proof.* $\cosh d_H=1+\frac{|z_1-z_2|^2}{2y_1y_2}=1+\frac{t^2}2$, and
$\cosh2v=1+2\sinh^2v$ gives the second form with $v=\operatorname{arcsinh}(t/2)$.
The asymptotics are $\operatorname{arccosh}(1+x)\sim\sqrt{2x}$ and
$\log(1+t^2)\sim t^2$. For the exponents, $\tau=\frac12\log(1+r^2)$ gives
$d\tau=r\,dr/(1+r^2)$, so $r^{2\omega-1}dr=r^{2\omega-2}(1+r^2)\,d\tau$ and
$r^2=e^{2\tau}-1\sim2\tau$, whence $r^{2\omega-2}\sim(2\tau)^{\omega-1}$. Checked
to $10^{-8}$ at five separations and to $10^{-6}$ for the $2^{1-\omega}$ ratio at
six shifts. $\square$

So the halving is a square, and nothing else. The question is then which
coordinate to trust, and there are three answers, all the same.

---

## 2. The dimension is $2\omega$

### 2.1 The true distance names a space, the Busemann coordinate does not

> **Proposition 2.1.** Put $u=d_H/2$, so that $r=2\sinh u$. Then
> \[
>  \lvert S^{2\omega-1}\rvert\,r^{2\omega-1}dr
>  =2^{2\omega}\lvert S^{2\omega-1}\rvert\,(\sinh u)^{2\omega-1}\cosh u\,du ,
> \]
> and $(\sinh u)^{2n-1}\cosh u$ is the radial Jacobian of complex hyperbolic space
> $CH^{n}$ at $n=\omega$: complex dimension $\omega$, real dimension $2\omega$. In
> the Jacobi weight $\Delta_{\alpha,\beta}(x)=(2\sinh x)^{2\alpha+1}(2\cosh x)^{2\beta+1}$,
> $\rho=\alpha+\beta+1$, the same measure has
> \[
>  (\alpha,\beta)=(\omega-1,0),\ \rho=\omega>0\quad\text{in }u,
>  \qquad
>  (\alpha,\beta)=\big(\tfrac\omega2-1,-\tfrac12\big),\ \rho=\tfrac{\omega-1}2<0\quad\text{in }\tau .
> \]
> Moreover the transfer integral written in $u$,
> $\lvert S^{2\omega-1}\rvert\int_0^\infty(2\sinh u)^{2\omega-1}(2\cosh u)(2\cosh2u-1)^{-(p+b)/2}du$,
> reproduces $\pi^\omega\Gamma(\frac{a+p}2)/\Gamma(\frac{b+p}2)$.

*Proof.* $dr=2\cosh u\,du$ and $r^{2\omega-1}=(2\sinh u)^{2\omega-1}$ give the
first identity. The $CH^n$ Jacobian is $(\sinh u)^{2n-2}\cdot\sinh u\cosh u$: all
but one direction of the geodesic sphere scale like $\sinh u$, and the Hopf
direction like $\sinh u\cosh u$. The Jacobi parameters follow by matching
exponents, using $1+r^2=2\cosh2u-1$ for the weight. The transfer integral was
checked by an independent quadrature --- the substitution $u=v^{1/2\omega}$ on
$[0,1]$ to remove the endpoint singularity, plus Gauss--Legendre panels out to
$u=40$ --- agreeing with the closed form to $3\times10^{-11}$ at four shifts and
two values of $p$. $\square$

$\rho>0$ is the range in which these weights belong to a space at all: $\rho$ is
the exponential rate of the spherical asymptotics, and $\rho<0$ means they grow.
The Busemann reading has $\rho<0$ for the entire family.

### 2.2 The Euclidean reading accounts for every factor; the other does not

Written in $\tau$, the kernel is $\Delta_{\omega/2-1,-1/2}(\tau)$ times
$e^{\tau/2}$, and nothing in the hyperbolic reading explains that factor. The
Euclidean reading explains all of it: prefactor $\lvert S^{2\omega-1}\rvert$,
Jacobian $r^{2\omega-2}e^{2\tau}$, weight $(1+r^2)^{-b/2}=e^{-b\tau}$, and
$\omega+1-b=\frac12$. Checked to $10^{-13}$ at six shifts and five delays, with
the leftover confirmed to be exactly $e^{\tau/2}$.

### 2.3 The comb has no coordinate

The strongest argument needs no geometry. The comb is $\zeta(2s-d)/\zeta(2s)$
with weights $J_d(n)/n^{(d+1)/2}$, and $d=2\omega$ appears there as an offset
between two arguments of $\zeta$ and as an exponent in a multiplicative function.
Neither is attached to a radial variable, so neither can be re-read in another
coordinate. Comb and archimedean factor multiply to make
$\Lambda(2s-d)/\Lambda(2s)$; they must carry the same $d$; so the dimension of
the object is $2\omega$.

### 2.4 What the complex reading is and is not

$\omega$ is the complex dimension **as a parameter on the Jacobi line**
$(\alpha,\beta)=(n-1,0)$ whose integer points are the spaces $CH^n$. It is not a
space: $CH^\omega$ exists at integer $\omega$ only, and the family
$\omega\in(0,\frac12]$ contains none. The real dimension $2\omega$, by contrast,
reaches the integer $1$ exactly once, at $\omega=\frac12$ --- and there the
object is the horocycle $\mathbb R$ of the modular surface, a real line with no
complex structure. **The two readings are realizable in complementary places, and
the Euclidean one is realizable where the family actually touches a geometry.**
That is why the dimension to quote is $2\omega$, with $\omega$ named as its half.

---

## 3. The correction is a volume term

The opening note's third dictionary entry was the weakest: the Blaschke factor
sits at $p=b=\frac{d+1}2$, "the pole of $\zeta(2s-d)$, i.e. the volume term",
which was a reading. It is a computation.

> **Proposition 3.1.** $\widetilde K_\omega$ has a single pole in $\Re p>0$, at
> $p=b=\frac{d+1}2$, and
> \[
>  \operatorname*{Res}_{p=b}\widetilde K_\omega
>  =\frac{\pi^{(d+1)/2}}{\Gamma\!\big(\frac{d+1}2\big)\,\zeta(d+1)}
>  =\frac{\lvert S^{d}\rvert}{2\,\zeta(d+1)} .
> \]
> At $d=1$ this is $6/\pi=2/\mathrm{vol}(PSL(2,\mathbb Z)\backslash\mathbb H)$,
> and since $2s=p+b$ makes a residue in $p$ twice one in $s$, it is the classical
> $\operatorname{Res}_{s=1}\varphi(s)=3/\pi=1/\mathrm{vol}$.

*Proof.* $\zeta(2s-d)=\zeta(p+a)$ has its only pole at $p+a=1$, i.e. $p=1-a=b$,
with residue $1$ in $p$. There $2s=2b=d+1$, so $s=\frac{d+1}2$ and
$s-\frac d2=\frac12$, giving
$\pi^{d/2}\Gamma(\frac12)/\big(\Gamma(\frac{d+1}2)\zeta(d+1)\big)$, which is the
first form; $\lvert S^{d}\rvert=2\pi^{(d+1)/2}/\Gamma(\frac{d+1}2)$ gives the
second. The two forms and the endpoint values were checked to $10^{-12}$.
$\square$

**The reading, now with teeth.** $\lvert S^{d}\rvert$ is the unit sphere of
$\mathbb R^{d+1}$ and $1/\zeta(d+1)$ is the density of primitive vectors in
$\mathbb Z^{d+1}$ --- verified by brute-force counts of primitive lattice points
in balls, agreeing with $\mathrm{vol}(B^m)X^m/\zeta(m)$ to $5\times10^{-5}$,
$3\times10^{-4}$ and $3\times10^{-3}$ at $m=2,3,4$. Their product is the volume
term of a **lattice of rank $d+1$**, whose cusp integrates over a horocycle of
dimension $d$. The two differ by one, as a cusp requires: the unipotent radical
has one less dimension than the lattice it stabilizes. At $d=1$: rank-$2$ lattice
$\mathbb Z^2$, one-dimensional horocycle, $SL(2,\mathbb Z)$ on $\mathbb H$.

So the correction, which the Loewner investigation proved was forced by
unimodularity and carried no arithmetic, is not merely a repair. It is the third
$d$-dimensional entry, and it supplies the one number the other two do not: the
**rank**.

---

## 4. The dictionary, closed

| Entry | In the $d$ variable | Dimension it carries |
|---|---|---|
| Archimedean | $\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)=\int_{\mathbb R^{d}}\lvert t+i\rvert^{-(p+b)}dt$ | horocycle, $d=2\omega$; prefactor $\lvert S^{d-1}\rvert$ |
| Comb | $\zeta(2s-d)/\zeta(2s)$, weights $J_d(n)/n^{(d+1)/2}$ | $d$, coordinate-free |
| Correction | pole at $p=\frac{d+1}2$, residue $\lvert S^{d}\rvert/2\zeta(d+1)$ | lattice rank $d+1$; sphere $\lvert S^{d}\rvert$ |
| The whole | $\Lambda(2s-d)/\Lambda(2s)$ | at $d=1$, the modular surface |

Every entry names the same object: **a rank-$(d+1)$ lattice in $\mathbb R^{d+1}$,
whose cusp integrates over a $d$-dimensional horocycle, $d=2\omega$.** The shift
is that horocycle's dimension, halved; the Blaschke factor is that lattice's
volume term; the comb counts that horocycle's reduced fractions. At $d=1$ all of
it is $\mathbb Z^2$ and $PSL(2,\mathbb Z)\backslash\mathbb H$.

---

## 5. What remains, re-ranked

Items 1 and 3 of the opening note are done, and the answer to both sharpens the
question rather than settling it.

1. **The rank.** A dimension can be continued; a **rank is a cardinality**. The
   dictionary now needs a lattice of rank $d+1=2\omega+1\in(1,2]$, and that is a
   harder object to imagine than a space of fractional dimension. But the two
   invariants the dictionary actually uses --- $J_d(n)$, and $1/\zeta(d+1)$ ---
   are defined for every real $d$ and specialize correctly at integers. So the
   question is exactly: **is there anything of which $J_d$ and $\zeta(d+1)$ are
   the invariants, when $d$ is not an integer?** This is the investigation's
   question in its sharpest form and it is what to attack next.
2. **Dimensional regularization of the criterion.** The whole transfer is now one
   function of $d$, $\Lambda(2s-d)/\Lambda(2s)$ with $2s=p+b$ and $b=\frac{d+1}2$.
   Whether $\lVert V_{\omega,L}\rVert$ continues in $d$, and whether contraction
   is stable under that continuation, is testable numerically with the inherited
   instrument before it is understood.
3. **$d=1$ as a boundary condition.** The endpoint is where the object exists and
   where contraction is unconditional. What does $\partial_d$ there compute, and
   is the derivative of the criterion at $d=1$ an accessible quantity?
4. **The complex-hyperbolic line.** $(\alpha,\beta)=(\omega-1,0)$ with
   $\rho=\omega$ is a Heckman--Opdam parameter, where a transform theory exists
   for arbitrary multiplicities. Whether the transfer is natural in that
   transform --- rather than merely having its weight --- would decide whether
   Section 2.1 is a coincidence of Jacobians or a structure.

---

## 6. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 2.1, 3.1.
- **Registered computation (standard library):** Sections 1--3, $56+27$ cases,
  records [`which-dimension-checks.json`](../numerics/records/which-dimension-checks.json)
  and [`residue-volume-checks.json`](../numerics/records/residue-volume-checks.json).
  The second evaluates $\zeta$ at real arguments above $1$ only, by a convergent
  series; no value on or near the critical line is computed anywhere in this
  investigation.
- **Reading:** the identification of the object as a rank-$(d+1)$ lattice with a
  $d$-dimensional horocycle (Section 4) --- it is exact at $d=1$ and is a reading
  of the formulas elsewhere; and the remark of Section 2.4 about which reading is
  realizable where.
- **Not claimed:** that any object exists at fractional $d$; that $CH^\omega$ is a
  space; anything about the zeros; any positivity.

See the [notes index](README.md) and the [investigation index](../README.md).
