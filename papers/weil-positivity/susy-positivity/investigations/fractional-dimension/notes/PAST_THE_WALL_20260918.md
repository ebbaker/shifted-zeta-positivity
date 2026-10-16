# Past the wall the decomposition survives and the criterion does not

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Fourth note of the fractional-dimension investigation, attacking
item 1 of the [third note's](THE_RANK_AND_THE_LATTICE_20260918.md) plan --- the
half-integer points beyond the range, and the first obstacle it named. Programme:
[`check_two_blaschke.py`](../numerics/check_two_blaschke.py) (266 cases),
standard library, with its record beside it.

**Nothing here is a positivity statement about the Weil form and nothing here is
about the zeros.** $\zeta$ is evaluated at real arguments $u\ge1.2$ only.

**A warning about $\xi$.** The parent manuscript defines $\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$,
which has the poles, and $\xi(u)=\frac12u(u-1)\Lambda(u)$, which is entire. The
first three notes of *this* investigation write $\xi$ for what the parent calls
$\Lambda$ --- the third note's Section 2 says so outright ("$\xi$ has simple poles
at $0$ and $1$"). The clash is harmless inside each document and lethal across
them, because the two differ by exactly the rational factor this note is about.
**Everything below is in the parent's convention.**

---

## 0. Summary

Item 1 had two halves. Both are answered, and they point opposite ways.

1. **The decomposition survives past the wall, and it needs no repair.** With
   $a=\frac12-\omega$, $b=\frac12+\omega$ and $c=-a=\omega-\frac12$, the rational
   factor is $R_\omega=B_b\cdot\frac{p+a}{p-a}$ at every $\omega$, and
   $\frac{p+a}{p-a}=B_c$ is a *Blaschke factor of the right half-plane* exactly
   when $\omega\ge\frac12$. So past the wall $R_\omega=B_bB_c$ is **inner**, where
   before it was a ratio $B_b/B_a$ with a right-half-plane pole
   (Proposition 1). The two Blaschke factors the handoff asked for are there, and
   they meet at $\omega=\frac12$ where $B_c\equiv1$.
2. **And the positivity survives too, once the Gamma factors are regrouped.** The
   parent's grouping $\widehat K_\omega=\frac{p+a}{p-a}\widetilde K_\omega$ exhibits
   complete monotonicity only for $\omega\le\frac12$, because the kernel of
   $\frac{p+a}{p-a}$ is $\delta_0+2a\,e^{at}$ and $2a<0$ past the wall. But with
   $z=\frac{p+a}2$,
   \[
    \widehat K^\Gamma_\omega(p)=\pi^\omega\,\frac{\Gamma(z+c)}{\Gamma(z+\omega)}\cdot
    \frac{\Gamma(z+1)}{\Gamma(z+c+1)},
   \]
   a product of two Gamma ratios whose parameter gaps are $\frac12$ and $c$, both
   non-negative exactly when $\omega\ge\frac12$. Each is completely monotone by the
   Beta integral. **So $\widehat K_\omega$ is completely monotone for every
   $\omega>0$: the parent's Proposition 3.6 was uncapped, only its proof was**
   (Proposition 2). The two groupings are *exchanged* at the wall.
3. **The instrument needed no second Blaschke factor at all.** The registered
   assembly is built from the *partial fractions* of $R_\omega$, which are the same
   algebra at every $\omega$. The only change required was a removable $0/0$ in the
   Gauss--Jacobi recurrence at $\omega=1$ exactly. The assembly's own Laplace
   certificate then passes at $\omega=1,\frac32,2$ to $10^{-13}$ with nothing else
   touched (Section 2).
4. **But the test cannot fail.** For every $\omega\ge\frac12$, *no* zero of $\zeta$
   satisfies $\lvert\Re\rho-\frac12\rvert>\omega$, because $0\le\Re\rho\le1$. By the
   parent's own dichotomy this makes $K_\omega$ inner, $V_\omega$ unitary and every
   $V_{\omega,L}$ a contraction --- **unconditionally, on the strength of the Euler
   product alone** for $\omega>\frac12$, with the classical zero-free region needed
   only at the single boundary point $\omega=\frac12$ (Proposition 3). The proposed experiment at ranks $3,4,5$ has a
   known answer. It is a calibration of the instrument, not a test of the
   mathematics, and Section 3 reports it as one.
5. **So the criterion has arithmetic content on exactly $\omega\in(0,\frac12)$,
   which is exactly $d\in(0,1)$, which is exactly $m\in(1,2)$ --- the open interval
   on which the third note proved the lattice point count is negative.** Same open
   interval, same endpoints, both switching at $a=\frac{1-d}2$ changing sign.
   **The shifted Weil criterion has arithmetic content precisely where the lattice
   does not exist** (Section 4).
6. **A correction.** The third note's Section 0.3 and the handoff place "the
   modular surface, and RH, at the right endpoint". The modular surface is there;
   RH is not. The criterion is *weakest* at $\omega=\frac12$ --- it is empty --- and
   strongest as $\omega\downarrow0$. In the rank reading: **the Euler product is the
   criterion's value at rank two, and RH is its derivative at rank one**, where
   $\widetilde K_0=1$, $V_0=I$ and $E^{*}_{\mathbb Z}\equiv2$. The gap between the
   two lowest ranks interpolates between them, by zero-free strips of half-width
   $\omega=\frac{m-1}2$ (Section 5).

---

## 1. The decomposition past the wall

Throughout, $s=\frac12+p$, $\omega>0$,
\[
 a=\tfrac12-\omega,\qquad b=\tfrac12+\omega,\qquad c=-a=\omega-\tfrac12,\qquad
 d=2\omega,\qquad m=d+1,
\]
so $a+b=1$, $b-a=2\omega$, $b-c=1$. Write $B_\gamma(p)=\frac{p-\gamma}{p+\gamma}$ for
$\gamma>0$, and
\[
 K_\omega(p)=\frac{\xi(p+a)}{\xi(p+b)},\qquad
 \widetilde K_\omega(p)=\frac{\Lambda(p+a)}{\Lambda(p+b)},\qquad
 R_\omega=\frac{K_\omega}{\widetilde K_\omega}.
\]

> **Proposition 1 (the second factor is a Blaschke factor exactly past the wall).**
> For every $\omega>0$,
> \[
>  R_\omega(p)=\frac{(p+a)(p-b)}{(p+b)(p-a)}
>  =B_b(p)\cdot\frac{p+a}{p-a}
>  =1-\frac{4\omega b}{p+b}-\frac{4\omega a}{p-a},
> \]
> and $\frac{p+a}{p-a}=B_c(p)$ with $c=\omega-\frac12$. Consequently
> * for $\omega<\frac12$: $c<0$, and $R_\omega=B_b/B_a$ has a pole at $p=a>0$. It is
>   unimodular on $\Re p=0$ but **not inner**; $\sup_{\Re p>0}\lvert R_\omega\rvert=\infty$.
> * for $\omega\ge\frac12$: $c\ge0$, and $R_\omega=B_bB_c$ is a product of two
>   Blaschke factors of the right half-plane, hence **inner**:
>   $\lvert R_\omega\rvert\le1$ on $\Re p>0$.
>
> At $\omega=\frac12$ exactly, $c=0$ and $B_c\equiv1$: the two regimes meet at a
> single factor $B_b$.

*Proof.* $\xi(u)=\frac12u(u-1)\Lambda(u)$ at $u=p+a$ and $u=p+b$, with $a-1=-b$ and
$b-1=-a$, gives the product form; the partial fractions are the parent's
Proposition 3.1. For the middle expression, $\frac{p+a}{p-a}=\frac{p-(-a)}{p+(-a)}=B_{-a}=B_c$.
A Blaschke factor with positive parameter is inner and a product of inner functions
is inner; and for $\omega<\frac12$ the pole at $p=a>0$ lies in the open right
half-plane. $\square$

The two poles of $\widetilde K_\omega$ that $R_\omega$ cancels have **different
origins**, and this is what makes the repair below the natural one. Writing
$\Lambda(p+a)=\pi^{-(p+a)/2}\Gamma(\frac{p+a}2)\zeta(p+a)$:

| pole of $\widetilde K_\omega$ | comes from | in the right half-plane iff |
|---|---|---|
| $p=b$ | $\zeta(p+a)$ at $p+a=1$ --- the **comb**, the prime number theorem's main term | always |
| $p=-a=c$ | $\Gamma(\frac{p+a}2)$ at $p+a=0$ --- the **archimedean factor** | $\omega>\frac12$ |

(The remaining poles of $\Gamma(\frac{p+a}{2})$, at $p+a=-2,-4,\dots$, are cancelled
by the trivial zeros of $\zeta(p+a)$; $\zeta(0)=-\frac12\ne0$, so the pole at
$p+a=0$ is exactly the archimedean one.) **Past the wall the correction must remove
one pole from each half of the transfer.** The second Blaschke factor is
archimedean, so it belongs with the Gammas --- which is Proposition 2.

> **Proposition 2 (complete monotonicity, uncapped).**
> **(a)** $\widetilde K_\omega$ is completely monotone on $(b,\infty)$ for every
> $\omega>0$.
> **(b)** $\widehat K_\omega(p)=\frac{p+a}{p-a}\widetilde K_\omega(p)$ is completely
> monotone on $(b,\infty)$ for every $\omega>0$.
>
> For (b) the parent's argument covers $\omega\le\frac12$; for $\omega\ge\frac12$,
> with $z=\frac{p+a}2$ and $\widehat K_\omega=\widehat K^\Gamma_\omega K^\zeta_\omega$,
> \[
>  \widehat K^\Gamma_\omega(p)=\pi^\omega\,\frac{\Gamma(z+c)}{\Gamma(z+\omega)}\cdot
>  \frac{\Gamma(z+1)}{\Gamma(z+c+1)},
>  \qquad
>  K^\zeta_\omega(p)=\frac{\zeta(p+a)}{\zeta(p+b)}=\sum_{n\ge1}\widetilde c_n\,n^{-p},
> \]
> with $\widetilde c_n=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega})>0$.

*Proof.* **(a)** is the parent's Proposition 3.2 verbatim; its proof uses the cap
$\omega\le\frac12$ nowhere. It needs only $p>b\Rightarrow p+a>1$, which holds for
every $\omega>0$, so that $\Lambda(p\pm\ )$ are positive and
$\frac{d}{du}\frac{\zeta'}\zeta(u)=\sum\Lambda(n)\log n\,n^{-u}$ converges on the
whole range of integration; $\psi'$ and $n^{-p}$ are completely monotone, hence so
is $\Phi'=-\partial_p\log\widetilde K_\omega$, hence so is $e^{-\Phi}$.

**(b)** The parent writes $\frac{p+a}{p-a}=1+\frac{2a}{p-a}$, of causal kernel
$\delta_0+2a\,e^{at}\mathbf 1_{t>0}$, which is a positive measure iff $a\ge0$, i.e.
iff $\omega\le\frac12$. Past the wall regroup instead. From
$(p+a)\Gamma\!\left(\frac{p+a}2\right)=2\Gamma(z+1)$, $\frac{p+b}2=z+\omega$ and
$p-a=2(z+c)$,
\[
 \frac{p+a}{p-a}\cdot\pi^\omega\frac{\Gamma(\frac{p+a}2)}{\Gamma(\frac{p+b}2)}
 =\pi^\omega\,\frac{\Gamma(z+1)}{(z+c)\,\Gamma(z+\omega)}
 =\pi^\omega\,\frac{\Gamma(z+c)}{\Gamma(z+\omega)}\cdot\frac{\Gamma(z+1)}{\Gamma(z+c+1)},
\]
the last step by $\Gamma(z+c+1)=(z+c)\Gamma(z+c)$. Each factor has the form
$\Gamma(z+\alpha)/\Gamma(z+\beta)$ with gap $\beta-\alpha\ge0$ --- the gaps are
$\omega-c=\frac12$ and $(c+1)-1=c\ge0$ --- and
\[
 \frac{\Gamma(z+\alpha)}{\Gamma(z+\beta)}
 =\frac1{\Gamma(\beta-\alpha)}\int_0^\infty e^{-zt}\,e^{-\alpha t}(1-e^{-t})^{\beta-\alpha-1}\,dt
\]
is completely monotone in $z$, hence in $p$ since $z$ is an increasing affine
function of $p$. On $p>b$ one has $z>\frac12$, inside both domains. The comb has
positive coefficients and converges for $p>b$. Products of completely monotone
functions are completely monotone. $\square$

**What the wall separates, at the level of positivity.**

| object | $\omega<\frac12$ | $\omega>\frac12$ |
|---|---|---|
| $\frac{p+a}{p-a}$ | completely monotone, **not** inner | inner, **not** completely monotone |
| $R_\omega=B_b\cdot\frac{p+a}{p-a}$ | not inner | inner |
| $\widetilde K_\omega$ (Markov part) | completely monotone | completely monotone |
| $\widehat K_\omega$ | completely monotone (parent's grouping) | completely monotone (regrouped) |

So the factor that changes character at $d=1$ is $\frac{p+a}{p-a}$, and it does not
*lose* positivity: it **exchanges one positivity for another**. That is a concrete
piece of item 3 of the third note's plan, which asked for a factorization
exhibiting which factor loses positivity at fractional $d$. The answer is that this
one trades, and that the trade is exactly at $d=1$.

At $\omega=1$ the two Gamma ratios collapse against each other:
$\widehat K^\Gamma_1(p)=\frac{2\pi}{p+\frac12}$, of kernel $2\pi e^{-\tau/2}$ ---
checked against the assembly to $5\times10^{-10}$, which is the accuracy of the
comparison route, not of the identity.

---

## 2. What the instrument needed: one removable $0/0$

The handoff expected the registered assembly to need re-derivation with two
Blaschke factors. It does not, and the reason is worth recording: **the assembly
never used the Blaschke factorization.** It is built from
\[
 \kappa_\omega=k^\Gamma_\omega-4\omega b\,J_{-b}-4\omega a\,J_a,\qquad
 J_\gamma(\tau)=\int_0^\tau e^{\gamma(\tau-u)}k^\Gamma_\omega(u)\,du,
\]
which is the *partial-fraction* form of $R_\omega$ --- the same algebra at every
$\omega$, with $a<0$ simply making the second smoothing decay instead of grow. The
Blaschke factorization enters the proofs of positivity, not the computation.

The one real obstacle was arithmetic, not analytic. `gauss_jacobi_unit` writes the
$k=0$ Jacobi recurrence coefficient as $(\beta^2-\alpha^2)/(\delta(\delta+2))$ with
$\delta=\alpha+\beta$, which is $0/0$ when $\alpha=\beta=0$ --- that is, at
$\omega=1$ **exactly**, and nowhere else. Its removable value is
$(\beta-\alpha)/(\alpha+\beta+2)$, equal to the old expression whenever
$\delta\ne0$. With that one line changed and nothing else, the assembly's own
certificate,
\[
 \int_0^\infty e^{-p\tau}\kappa_\omega(\tau)\,d\tau
 =\pi^\omega\frac{\Gamma(\frac{a+p}2)}{\Gamma(\frac{b+p}2)}\cdot
 \frac{(p+a)(p-b)}{(p+b)(p-a)} ,
\]
holds at the new shifts. Relative error, $p\in\{3,5,8\}$:

| $\omega$ | $0.1$ | $\tfrac12$ | $1$ | $\tfrac32$ | $2$ |
|---|---|---|---|---|---|
| worst relative error | $1.2\times10^{-13}$ | $9.1\times10^{-14}$ | $5.7\times10^{-14}$ | $6.4\times10^{-14}$ | $3.3\times10^{-13}$ |

The right-hand side contains $\Gamma$ and nothing else: no $\zeta$, no $\xi$, no
zeros. The two controls at $\omega=0.1,\frac12$ are inside the family's range and
reproduce the parent's own numbers.

---

## 3. The criterion is vacuous past the wall

> **Proposition 3 (vacuity).** Let $\omega\ge\frac12$. Then no nontrivial zero of
> $\zeta$ satisfies $\lvert\Re\rho-\frac12\rvert>\omega$. Hence, by the parent's
> Proposition 2.4, $K_\omega$ is inner on $\Re p>0$, $V_\omega$ is unitary and causal
> on $L^2(\mathbb R)$, and
> \[
>  \lVert V_{\omega,L}\rVert\le1\qquad\text{for every }L>0,
> \]
> **unconditionally**. For $\omega>\frac12$ the only arithmetic input is
> $\zeta(u)\ne0$ for $\Re u>1$ --- the Euler product --- together with the functional
> equation, which give $0\le\Re\rho\le1$. At the single point $\omega=\frac12$ the
> hypothesis is still satisfied by the Euler product, but the contour argument behind
> it wants the poles strictly inside the left half-plane, which is
> $\zeta(1+it)\ne0$: the classical zero-free region.

*Proof.* $0\le\Re\rho\le1$ gives $\lvert\Re\rho-\frac12\rvert\le\frac12\le\omega$,
so the hypothesis of the parent's dichotomy holds with nothing assumed. Equivalently
at the level of poles: the poles of $K_\omega$ are at $p=\rho-b$, with
$\Re p\le1-b=a\le0$, and $a<0$ as soon as $\omega>\frac12$. At $\omega=\frac12$,
$a=0$, and $\Re p=\Re\rho-1$ is negative for every zero but has supremum $0$, the
zeros approaching $\Re\rho=1$ as the height grows; moving the realization contour to
the axis there uses $\Re\rho<1$, which is de la Vallée Poussin and not the Euler
product. Nothing in the rest of this note turns on the boundary point: the
informative range is the **open** interval $(0,\frac12)$ either way. $\square$

> **Corollary 3.1 (where the criterion has content).** By the parent's dichotomy in
> both directions, $\sup_L\lVert V_{\omega,L}\rVert\le1$ **iff** every zero satisfies
> $\lvert\Re\rho-\frac12\rvert\le\omega$. Therefore
> * for $\omega\ge\frac12$ the statement is unconditionally true and equivalent to
>   nothing about the zeros: the criterion is **vacuous**;
> * for $\omega\in(0,\frac12)$ it is equivalent to the zero-free strip of half-width
>   $\omega$, a nontrivial statement;
> * RH is the conjunction over all $\omega\in(0,\frac12)$, that is, the limit
>   $\omega\downarrow0$.

**So the experiment item 1 proposed cannot fail.** Running the assembly at
$\omega=1,\frac32,2$ does not ask whether the criterion is rank-generic; the answer
was fixed by the Euler product before the programme started. What the run *can* do
is calibrate --- it is the first point in this programme where the answer is known
in advance --- and that is how it is recorded.

**The calibration, $L=\log3$, $N=24$, $32$ Gauss--Jacobi nodes per atom.**
$m_L^{(24)}=6.247514\times10^{-8}$.

| $\omega$ | rank $m$ | mass on window | $1-\lVert V_N\rVert$ | $\lambda_{\min}(D_N)$ | $\lambda_{\min}(D_N)/(2\omega\,m_L^{(24)})$ |
|---|---|---|---|---|---|
| $0.1$ | $1.2$ | $0.940662658$ | $6.61\times10^{-9}$ | $1.3217\times10^{-8}$ | $1.058$ |
| $\tfrac12$ | $2$ | $0.774030153$ | $4.58\times10^{-8}$ | $9.1686\times10^{-8}$ | $1.468$ |
| $1$ | $3$ | $0.707371247$ | $1.72\times10^{-7}$ | $3.4445\times10^{-7}$ | $2.757$ |
| $\tfrac32$ | $4$ | $0.762741187$ | $5.38\times10^{-7}$ | $1.0761\times10^{-6}$ | $5.741$ |
| $2$ | $5$ | $0.891128215$ | $1.55\times10^{-6}$ | $3.1068\times10^{-6}$ | $12.432$ |

Quadrature drift from $32$ to $48$ nodes per atom is $\le5\times10^{-6}$ relative
and falls to $2\times10^{-8}$ at the larger shifts; the residue is the
double-precision floor of an absolute quantity of size $10^{-8}$ read off matrices
of norm one, not the rule.

**Which direction these numbers certify.** $\lambda_{\min}(D_N)$ is a trial-space
Rayleigh quotient on the $N$-mode sine basis, and
$\langle f,D_Nf\rangle=\lVert f\rVert^2-\lVert P_NVf\rVert^2\ge\lVert f\rVert^2-\lVert Vf\rVert^2$ for
$f\in E_N$. So $\lambda_{\min}(D_N)\ge\lambda_{\min}(D_{\omega,L})$: it
**overstates** the margin, and a positive value **does not certify contraction**.
Contraction here is certified by Proposition 3 and by nothing in the table. What
the table shows is that the instrument returns the known answer, and how the
first-order law $\lambda_{\min}(D_N)/2\omega=m_L^{(N)}$ degrades once $\omega$ is no
longer small --- by a factor $12$ at $\omega=2$, smoothly and monotonically, with no
feature at the wall. **The wall is invisible to the numerics, because it is not a
wall in the transfer; it is a wall in what the transfer is evidence for.**

Nothing was run at $L=\log5,\log7$: there $m_L^{(24)}$ is $10^{-17}$ and $10^{-22}$,
below what double precision reads off a matrix of norm one, and a trial run returned
$\lambda_{\min}(D_N)$ of either sign at the $10^{-14}$ level --- the floor the trap
list warns about, not a signal.

---

## 4. The two intervals are the same interval

Corollary 3.1 says the criterion has arithmetic content exactly on
\[
 \omega\in(0,\tfrac12)\iff d\in(0,1)\iff m\in(1,2).
\]
The third note's Proposition 3.2 says the unique interpolation of the point count
satisfies
\[
 r_{d+1}(3)=\tfrac43(d+1)d(d-1)<0\quad\text{exactly for } d\in(0,1),
\]
vanishing exactly at $d=0$ and $d=1$, so that $\theta(it)^{d+1}$ is not completely
monotone anywhere strictly inside. **These are the same open interval, with the same
endpoints.**

> **Observation 4.1.** The shifted Weil criterion has arithmetic content precisely
> on the set where the lattice fails to exist.

Both switch on the sign of $a=\frac{1-d}2$, and the reason they do is the one the
third note already gave for its own interval: $(1,2)$ is the first gap of the rank
sequence, and Proposition 2.1 of that note put the family exactly there. The two
statements are one statement --- "$m$ lies strictly between the two lowest ranks" ---
seen once through the transfer's second pole and once through the theta series. At
$m=2$ both switch off: $a=0$, $R_\omega=B_b$ alone, the criterion is vacuous, and
$r_{d+1}(3)=0$. At $m=1$ both switch off at the other end.

What this does **not** do is explain the split the third note asked about. Both
positivity statements still sit on the same family; what is now known is that they
also share an interval, and that on the transfer side the carrier of the change is a
single rational factor which trades complete monotonicity for innerness rather than
losing either. Whether that trade and the theta's failure are the same fact is the
question, and it is now the sharpest one on the list.

*Caveat.* The coincidence is proved only on $(0,1)$, where both sides are theorems.
Beyond $d=1$ the third note's scan --- an observation, not a theorem --- finds
$\theta^m$ losing positivity again on $(2,3)$ and part of $(3,4)$, where the
criterion stays vacuous. So the correspondence is exact on the first gap and is not
claimed anywhere else.

---

## 5. A correction: which endpoint is RH

The third note's Section 0.3 and the handoff paragraph both place the family in
$m\in(1,2]$ "with the modular surface, and RH, at its right endpoint". The modular
surface is at the right endpoint. **RH is not.** By Corollary 3.1 the criterion is
*emptiest* at $\omega=\frac12$ and sharpest as $\omega\downarrow0$: the shift
$\omega$ is exactly the half-width of the zero-free strip it certifies.

The rank reading is then cleaner than the one it replaces:

| endpoint | rank | the object | the criterion |
|---|---|---|---|
| $m=2$, $\omega=\frac12$ | two: $\mathbb Z^2$, the modular surface | $\varphi(s)=\Lambda(2s-1)/\Lambda(2s)$ | its **value** is the Euler product |
| $m\in(1,2)$ | none: no lattice | a scattering matrix without a space | zero-free strips of half-width $\frac{m-1}2$ |
| $m=1$, $\omega=0$ | one: $\mathbb Z\subset\mathbb R$, $E^{*}_{\mathbb Z}\equiv2$ | $\widetilde K_0=1$, $V_0=I$ | its **derivative** is the Weil form, hence RH |

The bottom row is worth stating on its own. At rank one the primitive Epstein zeta
is the constant $2$, its reflection ratio is $1$, the transfer degenerates to the
identity, and the first-order law $D_{\omega,L}=2\omega\,Q_L+O(\omega^2)$ makes the
localized Weil form its $\partial_\omega$ there. **RH is the derivative of the
rank-$(d{+}1)$ scattering matrix at rank one; the Euler product is its value at rank
two; and the gap between them is filled by the zero-free strips.** The family is a
monotone interpolation between the easiest theorem about $\zeta$ and the hardest
conjecture, parameterized by a rank that is not an integer anywhere strictly inside.

---

## 6. What remains, re-ranked

1. **Is the trade the explanation?** (Successor to item 3, now with both carriers
   named.) On the transfer side, $\frac{p+a}{p-a}$ exchanges complete monotonicity
   for innerness at $d=1$. On the lattice side, $\theta(it)^{d+1}$ loses complete
   monotonicity on $(0,1)$. Both live on the same interval. A statement deriving one
   from the other --- or a proof that they are independent --- would close the
   investigation's central question. This is now the head item.
2. **Rank two as a boundary condition, restated.** $\partial_d$ at $d=1$ is *not*
   the criterion's informative derivative: by Corollary 3.1 the criterion's
   derivative is at $d=0$, and it is the Weil form, already known. What
   $\partial_d$ at $d=1$ measures is how fast the criterion *acquires* content on
   entering the gap. That is a real object --- and $r_{d+1}(3)$ leaves positivity
   with slope $\frac83$ there, while $a$ leaves zero with slope $-\frac12$, so both
   are linear --- but it is a different question from the one item 2 posed, and it
   should be re-posed before it is worked on.
3. **The complex-hyperbolic line.** Unchanged in rank, and now with one more
   datum: the second Blaschke factor is *archimedean* (Section 1), so the
   Heckman--Opdam side is where the wall is felt, not the arithmetic side.
4. **A small piece of hygiene.** The $\xi/\Lambda$ clash between this
   investigation's notes and the parent manuscript should be resolved in one
   direction before a manuscript is started here; the two conventions differ by
   exactly $R_\omega$.

**Closed by this note.** Item 1 in both halves: the re-derivation is possible
(Propositions 1 and 2), the instrument carries it (Section 2), and the experiment it
unlocks is vacuous (Proposition 3). **Do not run the criterion at $\omega\ge\frac12$
expecting information.**

---

## 7. Status of every statement

- **Written proof, unconditional:** Propositions 1, 2 and 3, Corollary 3.1, and the
  pole table of Section 1. Proposition 3 uses the Euler product and the functional
  equation for $\omega>\frac12$, and additionally the classical zero-free region
  $\zeta(1+it)\ne0$ at the single point $\omega=\frac12$; it is *not* conditional on
  RH.
- **Inherited, used as stated:** the parent's Proposition 2.4 (flux and dichotomy),
  in both directions; its Propositions 3.1--3.3 and 3.6; the third note's
  Propositions 2.1 and 3.1--3.2.
- **Registered computation (standard library):** $266$ cases, record
  [`two-blaschke-checks.json`](../numerics/records/two-blaschke-checks.json), two
  fresh runs byte-identical. $\zeta$ is evaluated at **real arguments $u\ge1.2$
  only**, in one group, by Euler--Maclaurin; no value off the real axis is computed
  and no zero is located.
- **Calibration, not evidence:** every number in the table of Section 3. It is a
  trial-space Rayleigh quotient, it overstates the margin, and it certifies nothing
  about contraction; contraction there is Proposition 3.
- **Observation:** 4.1, the coincidence of the two intervals --- both sides are
  theorems on $(0,1)$, but that they are the *same* interval for a common reason is
  a reading of the two proofs, not a third proof.
- **Not claimed:** that any object exists at fractional $d$; that the transfer is a
  contraction at any $\omega<\frac12$; anything about the zeros; any positivity of
  the Weil form.

See the [notes index](README.md) and the [investigation index](../README.md).
