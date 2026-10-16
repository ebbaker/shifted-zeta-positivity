# The rank is realized at every integer, and the lattice does not continue

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Third note of the fractional-dimension investigation, attacking the
head item of the
[previous note's](WHICH_DIMENSION_AND_THE_VOLUME_20260918.md) re-ranked plan:
*is there anything of which $J_d$ and $\zeta(d+1)$ are the invariants, when $d$
is not an integer?* Programme:
[`check_epstein_scattering.py`](../numerics/check_epstein_scattering.py)
(327 cases), standard library, with its record beside it.

**Nothing here is a positivity statement and nothing here is about the zeros.**
Values of $\zeta$ are taken at real arguments only.

---

## 0. Summary

1. **The object at integer $d$ is named, and it is named at *every* integer, not
   just at $d=1$.** For a covolume-one lattice $L\subset\mathbb R^m$ write
   $E^{*}_L(s)=\sum_{v\in L\ \mathrm{primitive}}\lvert v\rvert^{-2s}$ for the
   **primitive Epstein zeta**. Poisson summation plus the primitive factorization
   $Z_L=\zeta(2s)E^{*}_L$ gives
   $\xi(2s)E^{*}_L(s)=\xi(m-2s)E^{*}_{L^{*}}(m/2-s)$, so the reflection ratio is
   **independent of the lattice and depends only on the rank**. Under this
   investigation's dictionary that ratio *is* the Markov part:
   \[
    \widetilde K_\omega(p)=\frac{\xi(m-2s)}{\xi(2s)}
    =\frac{E^{*}_L(s)}{E^{*}_{L^{*}}(m/2-s)},\qquad m=d+1=2\omega+1,\ \ 2s=p+b .
   \]
   So for every integer $d\ge1$ the shifted Weil transfer's Markov part is the
   scattering matrix of the space of unimodular lattices of **rank $d+1$**
   (Propositions 1.1, 1.2). The investigation's previous position --- $d=1$ the
   only realized point --- was too modest: $d=1,2,3,\dots$ are *all* realized, as
   ranks $2,3,4,\dots$; they simply lie outside the family's range.
2. **And the transfer's own reflection is the lattice's functional equation.**
   $p\mapsto-p$ is exactly $s\mapsto m/2-s$; on $\Re p=0$ the two arguments are
   complex conjugates, so $\lvert\widetilde K_\omega\rvert=1$ there. The all-pass
   property is the Epstein functional equation, nothing more.
3. **The family lives in the first gap of that sequence, and the gap closes at
   rank two.** $\omega\in(0,\frac12]$ is $m\in(1,2]$. The cap is not a convention:
   $\xi$ has poles at $0$ and $1$, so the numerator $\xi(m-u)$ has exactly two
   poles in $p$ --- at $p=b$, the one the Blaschke factor cancels, and at
   $p=\omega-\frac12$, which is in the closed left half-plane **iff $m\le2$**. In
   the lattice variable that second pole sits at $s=\frac{m-1}2=\omega$, where
   $\zeta(2s)$ has its pole precisely at $\omega=\frac12$. **The family's cap and
   the rank cap are one statement, and both are $\zeta$'s own pole reaching the
   boundary** (Proposition 2.1). Rank two --- the lattice $\zeta$ comes from, the
   modular surface --- is the right endpoint, and it is RH.
4. **Inside the gap the lattice does not exist.** The point count of $\mathbb Z^m$
   has a unique interpolation: the $q$-coefficients of $\theta^m$, well defined
   for every real $m$ because $\theta$ does not vanish on $\mathbb H$, and
   polynomial in $m$ (Proposition 3.1). With $m=d+1$,
   \[
    r_{d+1}(3)=\tfrac43\,(d+1)\,d\,(d-1)\ <\ 0\quad\text{for every }d\in(0,1),
   \]
   vanishing exactly at the two endpoints. Equivalently $\theta(it)^{d+1}$ is
   **not completely monotone** anywhere strictly inside the family
   (Proposition 3.2). There is no positive measure, hence no point set.
5. **So the answer is: not a lattice, and specifically not a point count.** What
   continues positively is all of the *cusp* data --- $J_d(n)>0$,
   $1/\zeta(d+1)\in(0,1)$, the horocycle integral, the unimodularity on the
   critical line. What fails is the interior. At fractional $d$ the object is a
   **scattering matrix without a space**.

---

## 1. The integer points

> **Proposition 1.1 (primitive Epstein scattering).** Let $L\subset\mathbb R^m$ be
> a lattice of covolume $1$, $L^{*}$ its dual, and for $\Re s>m/2$
> \[
>  Z_L(s)=\sum_{0\neq v\in L}\lvert v\rvert^{-2s},\qquad
>  E^{*}_L(s)=\sum_{v\in L\ \mathrm{primitive}}\lvert v\rvert^{-2s} .
> \]
> Then $Z_L=\zeta(2s)E^{*}_L$, both continue meromorphically, and
> \[
>  \xi(2s)\,E^{*}_L(s)\;=\;\xi(m-2s)\,E^{*}_{L^{*}}(m/2-s).
> \]
> In particular $E^{*}_L(s)\big/E^{*}_{L^{*}}(m/2-s)=\xi(m-2s)/\xi(2s)$ is
> **independent of $L$**: it is an invariant of the rank alone.

*Proof.* Every nonzero $v\in L$ is uniquely $k\,v_0$ with $k\ge1$ and $v_0$
primitive, so $Z_L(s)=\sum_{k\ge1}k^{-2s}E^{*}_L(s)=\zeta(2s)E^{*}_L(s)$. Poisson
summation in dimension $m$ gives $\theta_L(1/x)=x^{m/2}\theta_{L^{*}}(x)$ for
$\theta_L(x)=\sum_{v\in L}e^{-\pi x\lvert v\rvert^{2}}$ at covolume one, whence
Riemann's theta argument yields
$\pi^{-s}\Gamma(s)Z_L(s)=\pi^{-(m/2-s)}\Gamma(m/2-s)Z_{L^{*}}(m/2-s)$. Divide by
the factorization and use $\pi^{-s}\Gamma(s)\zeta(2s)=\xi(2s)$ and
$\pi^{-(m/2-s)}\Gamma(m/2-s)\zeta(m-2s)=\xi(m-2s)$. $\square$

Both halves were checked: Poisson summation on its own to $10^{-15}$, and the
completed integral
$\Lambda_m(s)=\frac1{s-m/2}-\frac1s+\int_1^\infty(\theta_m(x)-1)(x^{s-1}+x^{m/2-s-1})dx$
against **direct lattice summation** with the exact continuum tail, at
$m=2,3,4$, to $10^{-8}$ --- a non-tautological test, since that formula is
symmetric in $s\leftrightarrow m/2-s$ by construction. It also reproduces
$\zeta(2),\zeta(4),\zeta(6),\zeta(-1),\zeta(-3)$ to $10^{-13}$.

> **Proposition 1.2 (the integer points of the family).** Put $d=2\omega$,
> $b=\frac{d+1}2$, $u=\frac12+p+\omega=2s$, $m=d+1$. Then for every $d>0$
> \[
>  \widetilde K_\omega(p)=\frac{\Lambda(\frac12+p-\omega)}{\Lambda(\frac12+p+\omega)}
>  =\frac{\xi(u-d)}{\xi(u)}=\frac{\xi(m-u)}{\xi(u)}=\frac{\xi(m-2s)}{\xi(2s)},
> \]
> and for every **integer** $d\ge1$ this equals
> $E^{*}_L(s)\big/E^{*}_{L^{*}}(m/2-s)$ for every covolume-one lattice $L$ of rank
> $m$. Moreover $s(-p)=\frac m2-s(p)$ identically, so the transfer's reflection is
> the Epstein functional equation; and on $\Re p=0$ the two arguments are complex
> conjugates, so $\lvert\widetilde K_\omega\rvert=1$ there.

*Proof.* $\xi(w)=\xi(1-w)$ turns $\xi(u-d)$ into $\xi(1-u+d)=\xi(m-u)$; the rest
is Proposition 1.1. For the reflection, $s(p)=\frac{p+b}2$ and
$\frac m2-s(p)=\frac{d+1-p-b}2=\frac{2\omega+1-p-\omega-\frac12}2=\frac{b-p}2=s(-p)$.
On $p=it$ this is $\overline{s}$, and $E^{*}$ has real coefficients, so for
$L=L^{*}=\mathbb Z^m$ the ratio is $E^{*}(s)/\overline{E^{*}(s)}$. $\square$

Checked at $d=1,\dots,5$ and four values of $p$ each, all three expressions
agreeing to $10^{-11}$, with the reflection verified in exact rationals.

**Corollary 1.3 (all three dictionary entries at once).** At integer $d$ the
three entries of the dictionary are simultaneously the three parts of one
constant term: the archimedean factor
$\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)=\int_{\mathbb R^{d}}\lvert
t+i\rvert^{-(p+b)}dt$ is the integral over a $d$-dimensional unipotent radical;
the comb $\zeta(2s-d)/\zeta(2s)=\sum_n J_d(n)n^{-2s}$ is the sum over that
radical modulo $n$, which is what $J_d$ counts; and the residue of $E^{*}$ at its
rightmost pole $s=m/2$ is $\lvert S^{d}\rvert/2\zeta(d+1)$, which is exactly the
$\operatorname{Res}_{p=b}\widetilde K_\omega$ of the second note. Those two
residues coincide for a reason worth recording: $dp=2\,ds$ doubles a residue in
$s$, and the other factor $E^{*}(m/2-s)\to E^{*}(0)=Z(0)/\zeta(0)=(-1)/(-\frac12)=2$
halves it again. (Richardson extrapolation at $m=2,\dots,6$ to $10^{-5}$;
$Z_L(0)=-1$ and $E^{*}(0)=2$ checked separately.) In standard
language $g\mapsto E^{*}_{\mathbb Z^{m}g}(s)$ is the degenerate Eisenstein series
of the maximal parabolic $P_{1,m-1}$ of $SL(m)$ and $\xi(m-2s)/\xi(2s)$ is its
$c$-function; the formulas above are what is verified, and the group-theoretic
reading is the standard interpretation of them. At $m=2$ it is the classical
$\varphi(s)=\xi(2s-1)/\xi(2s)$ of $PSL(2,\mathbb Z)\backslash\mathbb H$.

---

## 2. The wall at rank two

The family's range $\omega\in(0,\frac12]$ has always been read as a convention
inherited from the width of the critical strip. It is also exactly a rank cap,
for a reason internal to the transfer.

> **Proposition 2.1.** $\xi$ has simple poles at $0$ and $1$, with residues $-1$
> and $+1$. Hence the numerator $\xi(m-u)$ of $\widetilde K_\omega$ has exactly
> two poles in $p$:
> \[
>  p=b=\omega+\tfrac12\qquad\text{and}\qquad p=\omega-\tfrac12 .
> \]
> The first is what the Blaschke factor $B_b$ cancels. The second lies in the
> closed left half-plane **iff $\omega\le\frac12$, iff $m\le2$**. In the lattice
> variable it sits at $s=\frac{m-1}2=\omega$, where $\zeta(2s)$ has its pole
> precisely at $\omega=\frac12$.

*Proof.* $\xi(m-u)$ is singular where $m-u\in\{0,1\}$, i.e. $u\in\{m,m-1\}$, i.e.
$p\in\{m-b,\ m-1-b\}=\{\omega+\frac12,\ \omega-\frac12\}$; and
$\omega-\frac12\le0\iff\omega\le\frac12\iff m=2\omega+1\le2$. The second
corresponds to $m-2s=1$, i.e. $s=\frac{m-1}2=\frac d2=\omega$. $\square$

**What this says.** The cap $\omega\le\frac12$ and the cap $m\le2$ are one
statement, and both are the pole of $\zeta$ at $1$ arriving at the boundary
$\Re p=0$. Rank two is the largest rank at which the transfer has a *single*
cancelled pole in the right half-plane --- and rank two is $\mathbb Z^{2}$, the
modular surface, the lattice $\zeta$ itself comes from. The endpoint of the
family is not an arbitrary edge; it is the last lattice.

---

## 3. Inside the gap there is no lattice

$\omega\in(0,\frac12]$ is $m\in(1,2]$: the family lies in the **first gap** of the
sequence of ranks, with the rank-$2$ lattice at its right endpoint and nothing
but the rank-$1$ lattice below. So the question is whether the lattice
interpolates into $(1,2)$.

> **Proposition 3.1 (the interpolation exists and is forced).** $\theta$ does not
> vanish on $\mathbb H$, so $\theta^{m}=\exp(m\log\theta)$ is a well-defined
> holomorphic function there for every real $m$, a form of weight $m/2$ with
> multiplier. Its $q$-coefficients are
> \[
>  r_m(n)=\sum_{j\ge1}\binom mj 2^{\,j}R_j(n),\qquad
>  R_j(n)=\#\{\text{ordered reps of }n\text{ as }j\text{ positive squares}\},
> \]
> a **polynomial in $m$ of degree at most $n$** which at every integer $m\ge0$ is
> the representation number of $\mathbb Z^{m}$. Being of degree $\le n$ and
> matching at $m=0,\dots,n$, it is the unique such interpolation. The first three
> are $r_m(1)=2m$, $r_m(2)=2m(m-1)$, $r_m(3)=\frac43m(m-1)(m-2)$.

Checked exactly in rationals against brute-force lattice enumeration at
$m=1,\dots,5$ for $n\le20$; the degree bound by vanishing $(n{+}1)$-st finite
differences; the three closed forms at five rational $m$.

> **Proposition 3.2 (and it is not positive).** With $m=d+1$,
> \[
>  r_{d+1}(3)=\tfrac43\,(d+1)\,d\,(d-1),
> \]
> which is **strictly negative for every $d\in(0,1)$** and vanishes exactly at
> $d=0$ and $d=1$. Consequently $\theta(it)^{d+1}=\sum_n r_{d+1}(n)e^{-\pi nt}$,
> being a Laplace expansion with discrete support, is **not completely monotone**
> for any $d$ in the open range: by uniqueness of Laplace transforms its
> representing measure is forced to be $\sum_n r_{d+1}(n)\delta_{\pi n}$, which is
> not positive.

*Proof.* Immediate from Proposition 3.1; the cubic $\frac43m(m-1)(m-2)$ has roots
$0,1,2$ and positive leading coefficient, so it is negative exactly on
$(-\infty,0)\cup(1,2)$, and $m=d+1\in(1,2)\iff d\in(0,1)$. $\square$

In the family's own variable $r_{d+1}(3)=\frac43(d^{3}-d)$ is a single arch below
zero: slope $-\frac43$ leaving $d=0$, slope $+\frac83$ arriving at $d=1$, deepest
at $d=1/\sqrt3$ ($\omega=1/2\sqrt3\approx0.2887$) where it equals
$-8/9\sqrt3\approx-0.513$. There is no interior point at which it recovers.

**The negativity interval is exactly the family's open range.** That is not a
coincidence: $(1,2)$ is the first gap between consecutive ranks above one, and
Proposition 2.1 put the family exactly there. The companion statement below rank
one is $r_m(2)=2m(m-1)<0$ for $m\in(0,1)$, the same phenomenon one gap down.

**An observation, not a theorem.** A scan of the $q$-expansion to $n=160$ over a
grid of $m$ finds the first negative coefficient at $n=2$ on $(0,1)$, $n=3$ on
$(1,2)$, $n=7$ on $(2,3)$, and at varying $n$ on $(3,4)$ --- and **none at all
for $m\ge4$**, the Lagrange four-square threshold. Only the two exact statements
above are claimed; the scan is recorded because it says the obstruction is a
low-rank phenomenon and dies exactly where every integer becomes representable.

---

## 4. What does continue

The failure is specific, and it is worth being precise about how little it takes
with it.

| Datum | At fractional $d$ | Why |
|---|---|---|
| Comb weights $J_d(n)/n^{(d+1)/2}$ | **positive**, every real $d>0$ | $J_d(n)=n^{d}\prod_{p\mid n}(1-p^{-d})$, each factor in $(0,1)$ |
| Primitive density $1/\zeta(d+1)$ | **in $(0,1)$**, every real $d>0$ | $\zeta(d+1)>1$ |
| Archimedean factor | **exists**, every real $d>0$ | Riesz integral over $\mathbb R^{d}$; and, in the true distance, a rank-one Heckman--Opdam weight, where the "dimension" is a multiplicity and multiplicities are continuous by construction |
| Transfer kernel $\widehat K_\omega$ | **completely monotone**, every $\omega$ | inherited from the parent investigation |
| $\lvert\widetilde K_\omega\rvert=1$ on $\Re p=0$ | **holds**, every real $d$ | Proposition 1.2; the argument is formula-level and never mentions a lattice |
| The point count $r_{d+1}(n)$ | **fails**, every $d\in(0,1)$ | Proposition 3.2 |

So every *cusp* invariant continues and the *interior* does not. The two
positivity statements in the table --- $\widehat K_\omega$ completely monotone,
$\theta(it)^{d+1}$ not --- sit on the same family at the same $\omega$, which is
the sharpest thing this note produces and the thing it does not explain.

---

## 5. The dictionary, with the fractional column

| Entry | In the $d$ variable | At integer $d$ | At fractional $d$ |
|---|---|---|---|
| Archimedean | $\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)$ | integral over the $d$-dimensional unipotent radical | survives; a continuous multiplicity |
| Comb | $\zeta(2s-d)/\zeta(2s)=\sum J_d(n)n^{-2s}$ | that radical counted modulo $n$ | survives as a positive multiplicative function that counts nothing |
| Correction | residue $\lvert S^{d}\rvert/2\zeta(d+1)$ at $s=\frac{m}2$ | residue of the primitive Epstein zeta of a rank-$(d{+}1)$ lattice | survives as a number; the lattice does not |
| The whole | $\xi(m-2s)/\xi(2s)$ | the rank-$(d{+}1)$ scattering matrix | a scattering matrix without a space |

---

## 6. What remains, re-ranked

1. **The half-integer points beyond the range: ranks $3,4,5$.** The criterion
   continues analytically to $\omega=1,\frac32,2$, where the object is a *genuine
   lattice*. This is cheap and decisive with the inherited registered assembly,
   and it is decisive either way: if contraction fails at $\omega=1$ the criterion
   is not rank-generic and we have calibrated the instrument; if it holds, it is a
   nontrivial statement about rank-three lattices with no zeros in it. **First
   obstacle, and itself the first thing to settle:** by Proposition 2.1 the second
   pole is in the right half-plane for $\omega>\frac12$, so $B_b$ alone no longer
   makes $\widehat K_\omega$ completely monotone and the assembly must be
   re-derived with two Blaschke factors. Whether that re-derivation is possible is
   the concrete question.
2. **Rank two as a boundary condition.** $\partial_d$ at $d=1$ is now a derivative
   taken *off the lattice sequence into the gap*, from the one point of the family
   where a space exists. That is a sharper object than "the endpoint derivative":
   $r_{d+1}(3)=\frac43(d^{3}-d)$ has $\partial_d r_{d+1}(3)=\frac83$ at $d=1$ and
   $-\frac43$ at $d=0$, so the point count leaves positivity linearly on entering
   the gap from either end, and the whole gap is one arch below zero.
3. **What replaces the lattice.** Two positivity statements on the same family,
   one surviving and one not (Section 4). A factorization of the transfer that
   exhibits *which* factor loses positivity at fractional $d$ would explain the
   split. This is the successor to "the rank" as the investigation's central
   question, and it is better posed than its predecessor because both sides are
   now proved.
4. **The complex-hyperbolic line.** $(\alpha,\beta)=(\omega-1,0)$, $\rho=\omega$
   is a Heckman--Opdam parameter with a transform theory at arbitrary
   multiplicity. It is now clearly the archimedean half's continuation, to be
   matched against the arithmetic half's failure rather than pursued alone.
5. **Bost--Connes at fractional $d$** --- demoted. It was a candidate for making
   $J_d$ count at non-integer $d$; the counting reading is exactly the one that
   failed.

---

## 7. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 1.2, 2.1, 3.1, 3.2 and
  Corollary 1.3's formulas.
- **Registered computation (standard library):** $327$ cases, record
  [`epstein-scattering-checks.json`](../numerics/records/epstein-scattering-checks.json).
  $\zeta$ is evaluated at **real arguments only**, including negative ones, by a
  convergent theta integral; the real segment of the critical strip is
  unavoidable --- it is where a scattering matrix lives --- but no value off the
  real axis is computed and no zero is located.
- **Reading:** the group-theoretic language of Corollary 1.3 (degenerate
  Eisenstein series, $c$-function, unipotent radical), which is the standard
  interpretation of the verified formulas and not something checked here.
- **Observation, explicitly not a theorem:** the positivity scan of $\theta^{m}$
  beyond $m=2$, including the apparent Lagrange threshold at $m=4$.
- **Not claimed:** that any object exists at fractional $d$; that the transfer is
  a contraction at any $\omega$; anything about the zeros; any positivity of the
  Weil form.

See the [notes index](README.md) and the [investigation index](../README.md).
