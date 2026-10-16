# The trade is not the explanation: the rank enters one side as an exponent and the other as a binomial index

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Fifth note of the fractional-dimension investigation, attacking item 1
of the [fourth note's](PAST_THE_WALL_20260918.md) plan: *is the trade the
explanation?* Programme:
[`check_the_trade.py`](../numerics/check_the_trade.py) (774 cases), standard
library, with its record beside it.

**Nothing here is a positivity statement about the Weil form and nothing here is
about the zeros.** No value of $\zeta$ is computed anywhere in the programme.
Conventions are the parent manuscript's: $\Lambda$ has the poles, $\xi$ is entire.

---

## 0. Summary

**The answer is no, and it takes one line to see.** The lattice's positivity fails
on $(2,3)$ as well as on $(1,2)$; the criterion has content only on $(1,2)$. At
$m=3$ the point count is positive and the transfer's rational factor is not. So no
equivalence between the two can hold, and the coincidence of intervals the fourth
note recorded is the first gap and nothing more.

What the session produced beyond the negative:

1. **The theta side's mechanism, now a theorem instead of a scan.** Writing
   $\theta^m=\sum_j\binom mj(\theta-1)^j$, the coefficient
   $r_m(n)=\sum_j\binom mj2^jR_j(n)$ with $R_j(n)$ the number of ordered
   representations of $n$ as $j$ **positive** squares. On the gap $m\in(k,k+1)$ the
   binomial is positive through $j=k+1$ and first negative at $j=k+2$
   (Proposition 1.1), so $r_m(n)>0$ automatically for $n\le k+1$ (Proposition 1.2),
   and the first coefficient that can be forced negative sits at $N_k$, the least
   integer needing $k+2$ positive squares. $N_0=2$, $N_1=3$, $N_2=7$, and
   **$N_k$ does not exist for $k\ge3$ --- because Lagrange's four-square theorem
   makes $s(n)\le4$ for every $n$** (Proposition 1.3). The third note's Lagrange
   threshold at $m=4$ is exactly that, and its "observation" is a theorem for every
   gap in which anything is forced (Proposition 1.4).
2. **The transfer side has exactly one positivity threshold, and it is at $m=2$.**
   Every factor of the Markov part has a positive kernel at every real $\omega>0$;
   the only object in the decomposition whose positivity depends on $\omega$ at all
   is $\frac{p+a}{p-a}$, and it turns at $a=0$ (Proposition 2.1). The transfer's
   only other feature at an integer is at $m=3$, where the archimedean exponent
   $\omega-1=\frac{m-3}2$ vanishes --- a **regularity** threshold, not a positivity
   one, and it points the wrong way, since at $m=3$ the point count *regains*
   positivity.
3. **So the coincidence is forced and carries no information.** The criterion's
   window has its endpoints at the two smallest ranks: $m=1$, where the transfer
   degenerates to the identity, and $m=2$, where $a$ changes sign. The first gap of
   the rank sequence is, by definition, $(1,2)$. Any two thresholds at the two
   smallest ranks coincide with it (Section 3).
4. **And here is what does explain the split.** In the transfer the rank enters
   every positive object **as an exponent** --- $(2\sinh\tau)^{\omega-1}$ in the
   archimedean kernel, $(1-e^{-t})^{\beta-\alpha-1}$ in each Beta density,
   $p^{-d}$ in each Euler factor of the comb. An exponent of a positive quantity is
   positive at every real value, and each such positivity is a *local* inequality
   --- at one $\tau$, at one prime --- which continuation in the parameter cannot
   break. In the point count the rank enters **as a binomial index**, where
   positivity is a global cancellation and continuation breaks it at once
   (Proposition 4.1). **That, and not the trade, is why the two part company.**
5. **Consequently item 3 of the third note, as posed, has no solution.** It asked
   for "a factorization of the transfer that exhibits *which* factor loses
   positivity at fractional $d$". No factor does, because no factor of the transfer
   carries the rank as a binomial index.

---

## 1. The theta side is Lagrange's theorem seen through a binomial series

Write $q=e^{-\pi t}$, $\theta=\sum_{k\in\mathbb Z}q^{k^2}=1+u$ with
$u=2q+2q^4+2q^9+\dots$, and for $j\ge1$ let $R_j(n)$ be the number of **ordered**
$j$-tuples of positive squares summing to $n$, so that $u^j=\sum_n2^jR_j(n)q^n$.
The third note's unique interpolation is then
\[
 \theta^m=\sum_{j\ge0}\binom mj u^j,\qquad
 r_m(n)=\sum_{j=1}^{n}\binom mj\,2^j\,R_j(n),
\]
the sum terminating because $R_j(n)=0$ for $j>n$. Let
$s(n)=\min\{j:R_j(n)>0\}$ be the least number of **positive** squares summing to
$n$.

> **Proposition 1.1 (the sign law).** Let $k\ge0$ be an integer and
> $m\in(k,k+1)$. Then
> \[
>  \operatorname{sign}\binom mj=(-1)^{\max(0,\;j-k-1)} ,
> \]
> that is: $\binom mj>0$ for $1\le j\le k+1$, $\binom m{k+2}<0$, and the sign
> alternates thereafter. No $\binom mj$ vanishes.

*Proof.* $\binom mj=\frac1{j!}\prod_{i=0}^{j-1}(m-i)$, and for integer $i$ one has
$m-i<0$ exactly when $i\ge k+1$. Among $i=0,\dots,j-1$ the number of such $i$ is
$\max(0,j-1-k)$. None vanishes because $m$ is not an integer. $\square$

> **Proposition 1.2 (the free region).** For $m\in(k,k+1)$ and $1\le n\le k+1$,
> $r_m(n)>0$.

*Proof.* $R_j(n)=0$ for $j>n$, so every contributing $j$ satisfies $j\le n\le k+1$
and has $\binom mj>0$ by Proposition 1.1; and at least one $R_j(n)$ is positive
($j=n$, all ones). $\square$

So negativity can only begin at $n\ge k+2$, and the first place it is *forced* ---
where no positive term is present at all --- is the following.

> **Proposition 1.3 (where the forcing lives, and where it stops).** Put
> $N_k=\min\{n\ge1:s(n)\ge k+2\}$. Then
> \[
>  N_0=2,\qquad N_1=3,\qquad N_2=7,
> \]
> with $s(N_k)=k+2$ in each case; and **$N_k$ does not exist for any $k\ge3$**,
> because Lagrange's four-square theorem gives $s(n)\le4$ for every $n\ge1$.

*Proof.* The three values are a finite verification: $2=1+1$ and $2$ is not a
square, so $s(2)=2$; $3=1+1+1$, and $3$ is not a square nor a sum of two positive
squares, so $s(3)=3$; $7=4+1+1+1$, and $7$ is not a square, not $a^2+b^2$
($7-1=6$, $7-4=3$, neither a square), and not a sum of three positive squares
($7-1-1=5$, $7-1-4=2$, neither a square), so $s(7)=4$. For the last clause,
Lagrange writes every $n$ as a sum of four squares; discarding the zero entries
leaves at most four positive ones. $\square$

> **Proposition 1.4 (the forced coefficient).** For $k=0,1,2$ and every
> $m\in(k,k+1)$,
> \[
>  r_m(N_k)<0,\qquad\text{while } r_m(n)>0 \text{ for every } 1\le n<N_k .
> \]
> Explicitly, $r_m(2)=2m(m-1)$, $r_m(3)=\frac43m(m-1)(m-2)$ and
> $r_m(7)=64\binom m4+128\binom m7$.

*Proof.* At $n=N_k$ every contributing $j$ has $R_j(N_k)>0$, hence $j\ge s(N_k)=k+2$.
For $k=0$ and $k=1$ only one $j$ contributes at all --- $R_j(2)=0$ except $R_2(2)=1$,
and $R_j(3)=0$ except $R_3(3)=1$ --- so $r_m(2)=4\binom m2$ and $r_m(3)=8\binom m3$,
both negative on their gap by Proposition 1.1. For $k=2$, $R_j(7)=0$ except
$R_4(7)=4$ and $R_7(7)=1$, so $r_m(7)=64\binom m4+128\binom m7$, and
\[
 r_m(7)=m(m-1)(m-2)(m-3)\Big[\tfrac83+\tfrac8{315}(m-4)(m-5)(m-6)\Big].
\]
On $(2,3)$ the prefactor is negative, and $(m-4)(m-5)(m-6)\in(-24,-6)$, so the
bracket lies in $(\frac83-\frac{192}{315},\ \frac83-\frac{48}{315})\subset(2.05,2.52)$
and is positive; hence $r_m(7)<0$.

For the second clause: $n\le k+1$ is Proposition 1.2, which covers $n=1$ for $k=0$,
$n\le2$ for $k=1$, and $n\le3$ for $k=2$. The three remaining cases are on $(2,3)$
and are bounded by hand. $R_1(4)=R_4(4)=1$ gives $r_m(4)=2m+16\binom m4
=2m\big[1+\tfrac13(m-1)(m-2)(m-3)\big]$, and $(m-1)(m-2)(m-3)\in(-2,0)$ there, so
the bracket exceeds $\frac13$. $R_2(5)=2$, $R_5(5)=1$ gives
$r_m(5)=8\binom m2+32\binom m5$, and on $(2,3)$ both binomials are positive by
Proposition 1.1. $R_3(6)=3$, $R_6(6)=1$ gives $r_m(6)=24\binom m3+64\binom m6$ with
$\binom m3>0$ and $\binom m6<0$, and
$\frac{64\binom m6}{24\binom m3}=\frac8{3}\cdot\frac{(m-3)(m-4)(m-5)}{120}$, whose
modulus is below $\frac83\cdot\frac6{120}=\frac2{15}<1$. $\square$

**What this says.** The point count's failure is a statement about **sums of
squares**: on the gap $(k,k+1)$ it is forced by the least integer that needs
$k+2$ positive squares, and it stops being forced at $k=3$ for one reason only ---
Lagrange. The third note recorded the threshold at $m=4$ as an observation from a
scan to $n=160$; it is a theorem, and this is the theorem.

*(Unforced negativity is a different matter. On $(3,4)$ nothing is forced, yet the
third note's scan found negative coefficients at varying $n$: there the negative
$j=k+2$ terms compete with positive ones rather than standing alone. That
competition, and the positivity for $m\ge4$, remain observations and this note does
not touch them.)*

---

## 2. The transfer side has exactly one positivity threshold

> **Proposition 2.1.** In the decomposition
> $K_\omega=R_\omega K^\Gamma_\omega K^\zeta_\omega$ of the parent manuscript:
> * $k^\Gamma_\omega(\tau)=\frac{2\pi^\omega}{\Gamma(\omega)}(2\sinh\tau)^{\omega-1}e^{\tau/2}>0$
>   for every $\tau>0$ and every real $\omega>0$;
> * $\widetilde c_n=n^{\omega-\frac12}\prod_{p\mid n}(1-p^{-2\omega})>0$ for every
>   $n\ge1$ and every real $\omega>0$;
> * $\widetilde K_\omega$ and $\widehat K_\omega$ are completely monotone on
>   $(b,\infty)$ for every real $\omega>0$ (fourth note, Proposition 2);
> * and the only object in the decomposition whose positivity depends on $\omega$
>   is $\frac{p+a}{p-a}$, of causal kernel $\delta_0+2a\,e^{at}$, positive exactly
>   when $a\ge0$, that is when $m\le2$.
>
> Hence the transfer has exactly one positivity threshold in $m$, at $m=2$.

*Proof.* $\Gamma(\omega)>0$ and $\sinh\tau>0$ for $\omega,\tau>0$; each Euler
factor $1-p^{-2\omega}$ lies in $(0,1)$; the third item is the fourth note; the
fourth is the kernel of $1+\frac{2a}{p-a}$. $\square$

**The one other feature at an integer, and it is the wrong kind.** At $m=3$, i.e.
$\omega=1$, the archimedean exponent $\omega-1=\frac{m-3}2$ vanishes: the atom
$k^\Gamma_\omega$ goes from unbounded at the origin ($m<3$) through bounded ($m=3$,
where it is exactly $2\pi e^{\tau/2}$) to vanishing there ($m>3$). That is a
**regularity** threshold and not a positivity one --- $k^\Gamma_\omega$ is positive
throughout --- and it points the wrong way: at $m=3$ the point count *regains*
complete monotonicity, while nothing on the transfer side is regained or lost.

---

## 3. The decisive comparison

| $m$ | $\theta(it)^{m}$ completely monotone | $\frac{p+a}{p-a}$ completely monotone | criterion has arithmetic content |
|---|---|---|---|
| $(1,2)$ | **no** --- $r_m(3)<0$ | yes ($a>0$) | **yes** |
| $2$ | yes (rank-two lattice) | yes ($a=0$, factor $\equiv1$) | no (vacuous) |
| $(2,3)$ | **no** --- $r_m(7)<0$ | no ($a<0$) | no (vacuous) |
| $3$ | yes (rank-three lattice) | no ($a<0$) | no (vacuous) |

> **Corollary 3.1.** The point count's failure set and the criterion's content set
> agree on $(1,2)$ and differ on $(2,3)$; and at $m=3$ the point count is
> completely monotone while the transfer's rational factor is not. No statement of
> the form "$\theta(it)^m$ is completely monotone if and only if [any of the
> transfer's positivities]" can hold. **The trade is not the explanation.**

**And the agreement on $(1,2)$ is forced.** The criterion's window is bounded below
by $m=1$, where $\omega=0$, $\widetilde K_0=1$ and $V_0=I$ --- the transfer
degenerates --- and above by $m=2$, where $a$ changes sign. Those are the two
smallest ranks. The first gap of the rank sequence is $(1,2)$ by definition. Any
pair of thresholds sitting at the two smallest ranks produces the first gap, so the
coincidence the fourth note recorded is a statement about the number $2$ and not
about either positivity. The fourth note was right to call it an observation and
right not to call it a proof; it is now clear that it is not evidence either.

---

## 4. What does explain the split

The two sides are not merely different: they carry the rank in different *places*,
and the place is what decides.

> **Proposition 4.1 (exponent versus binomial index).** Every positivity in the
> transfer is produced by one of two mechanisms, in each of which the rank enters
> as an exponent of a positive quantity:
> * **Beta densities.** For $\beta>\alpha$,
>   $\dfrac{\Gamma(z+\alpha)}{\Gamma(z+\beta)}
>   =\dfrac1{\Gamma(\beta-\alpha)}\displaystyle\int_0^\infty e^{-zt}\,e^{-\alpha t}(1-e^{-t})^{\beta-\alpha-1}\,dt$,
>   a positive density for every real $\beta-\alpha>0$. This is the archimedean
>   factor, and the fourth note's regrouping, and $k^\Gamma_\omega$ itself, where
>   the rank sits in $(2\sinh\tau)^{\omega-1}$.
> * **Euler factors.** The comb's local factor at $p$ is
>   \[
>    \frac{1-p^{-u}}{1-p^{-(u-d)}}=1+\sum_{k\ge1}p^{(k-1)d}\big(p^{d}-1\big)\,p^{-ku},
>   \]
>   whose coefficients are positive for every real $d>0$ because $p^{d}>1$.
>
> In both, positivity is a *local* inequality --- at one $\tau$, at one prime ---
> in which $d$ appears as an exponent; and an exponent of a positive quantity is
> positive at every real value. The point count has neither structure: its unique
> continuation is the binomial series of Section 1, in which the rank appears as an
> **index**, and $\binom mj$ changes sign at $j=\lfloor m\rfloor+2$.

*Proof.* The Beta integral is the substitution $x=e^{-t}$ in
$B(z+\alpha,\beta-\alpha)$; the Euler factor expands as
$(1-p^{-u})\sum_{k\ge0}p^{k(d-u)}$, whose $p^{-ku}$ coefficient is
$p^{kd}-p^{(k-1)d}=p^{(k-1)d}(p^{d}-1)$; multiplicativity over $p\mid n$ recovers
$J_d(n)=n^{d}\prod_{p\mid n}(1-p^{-d})$. The last clause is Proposition 1.1.
$\square$

**Reading.** This is the answer the investigation has been circling. The transfer's
positivity was never inherited from a lattice --- there is no proof of complete
monotonicity that goes through one, and a ratio in which the lattice cancels could
not carry one. It comes from a Beta density and an Euler product, both of which
take the rank as an exponent and therefore continue to every real value without
noticing that a lattice has stopped existing. The point count takes the rank as a
binomial index and notices immediately. **The two positivity statements sit on the
same family because the family has one parameter, and they part company because
that parameter occupies a different position in each.**

And this closes item 3 of the third note as it was posed. It asked for a
factorization of the transfer exhibiting *which* factor loses positivity at
fractional $d$. There is none: no factor of the transfer loses positivity at any
real $d>0$, because none of them carries $d$ as a binomial index. The only factor
that changes character does so at $m=2$, an integer, for a reason internal to
$\Lambda(u)=\Lambda(1-u)$.

---

## 5. What remains

The investigation's own question --- *is $d$ a dimension, or a parameter?* --- now
has a complete answer, and it is **a parameter**. The dictionary named a single
object (second note); the object is a rank-$(d{+}1)$ lattice at every integer and
nothing strictly in between (third note); the transfer continues past the family's
range with its decomposition and its positivity intact, and its criterion does not
(fourth note); and the transfer's positivity continues for reasons that have
nothing to do with the lattice, so the failure of the lattice leaves no trace in it
(this note). There is no remaining sense in which $d$ is a dimension away from the
integers.

**I think the material is now manuscript-shaped**, and I have not started one.
A manuscript would be short and would contain: the dictionary and the
rank identification; the primitive-Epstein scattering matrix at every integer rank;
the rank-two wall as the sign of $a$, with the three things that change there; the
two-Blaschke decomposition and complete monotonicity at every $\omega>0$ by two
exchanged groupings; the vacuity of the criterion past the wall; the point count's
failure with the Lagrange threshold as Proposition 1.3 above; and
Proposition 4.1 as the reading. Six of those seven are written proofs.

What is genuinely still open, ranked:

1. **The complex-hyperbolic line.** $(\alpha,\beta)=(\omega-1,0)$ with
   $\rho=\omega$ is a Heckman--Opdam parameter with a transform theory at arbitrary
   multiplicity. It is now clearly the archimedean half's continuation --- and
   Proposition 4.1 explains why that half continues at all: its positivity is a
   Beta density with $\omega$ in the exponent. Whether the Heckman--Opdam theory
   adds anything beyond a name for that is the question.
2. **Convention hygiene**, before any manuscript: the first three notes here write
   $\xi$ for the parent's $\Lambda$, and the two differ by exactly $R_\omega$.
3. **Two clean conjectures, not to be chased in this investigation.** That
   $r_m(n)\ge0$ for every $n$ and every real $m\ge4$; and that on $(3,4)$ the
   negative coefficients are produced by competition rather than forcing. Both are
   statements about sums of squares, not about $\zeta$, and both belong to whoever
   wants them.

**Closed by this note.** Item 1 of the fourth note's plan (*is the trade the
explanation?* --- no), and item 3 of the third note's plan as posed (*a
factorization exhibiting which factor loses positivity* --- there is none).

---

## 6. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 1.2, 1.4, 2.1, 4.1 and
  Corollary 3.1. None is conditional on RH; none mentions a zero.
- **Written proof, citing a classical theorem:** Proposition 1.3, whose last clause
  is Lagrange's four-square theorem, used and not reproved. Its first clause
  ($N_0,N_1,N_2$) is a finite verification, done by hand in the proof and
  independently in the programme.
- **Inherited, used as stated:** the fourth note's Propositions 1--3 and
  Corollary 3.1; the third note's Propositions 3.1--3.2; the parent's
  Propositions 2.3, 2.4 and 3.1--3.3.
- **Registered computation (standard library):** $774$ cases, record
  [`the-trade-checks.json`](../numerics/records/the-trade-checks.json), two fresh
  runs byte-identical. Exact rational arithmetic throughout the theta side. **No
  value of $\zeta$ is computed anywhere in the programme.**
- **Observation, explicitly not a theorem, and not touched here:** the behaviour of
  $r_m(n)$ on $(3,4)$, and its positivity for $m\ge4$.
- **Judgement, not a result:** Section 5's assessment that the investigation's
  question is answered and the material is manuscript-shaped.
- **Not claimed:** that any object exists at fractional $d$; that the transfer is a
  contraction at any $\omega<\frac12$; anything about the zeros; any positivity of
  the Weil form.

See the [notes index](README.md) and the [investigation index](../README.md).
