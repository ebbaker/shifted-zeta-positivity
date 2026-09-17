# The delay expansion: the leading term is the degree, the next term is a selection rule, and it excludes Liouville

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note, doing the
calculation [the delay-test note](THE_DELAY_TEST_20260917.md) ends by asking for:
fix a dictionary between the Liouville momentum and the dilatation eigenvalue,
and see what the constant is.

**Applied to the manuscript.** Version 0.5 carried this note as Section 11.5,
11.6 and the rewritten Condition 10.1; Section 7 below is what was recommended and
done. `check_delay_test.py` is registered.

> **Partly corrected, 17 September 2026.** Item 3 of the summary below, and the
> sentence "and with it every amplitude built from $\Gamma(\text{integer}+i\,\cdot)$",
> assume $n_j>0$ and are **false without it**; the rigidity statement additionally
> assumes integer multiplicities, which excludes the one amplitude that matches.
> Both are corrected in
> [the quarter-shift survey note](THE_QUARTER_SHIFT_SURVEY_20260917.md), which
> replaces the single $\tau^{-2}$ coefficient by the dictionary-free graded
> sequence $I_{2m}$ and gives a complete single-factor classification. The
> Liouville exclusion itself stands. Manuscript version 0.6 carries the corrected
> statements.

---

## 0. Summary

1. **The dictionary is forced.** Requiring the leading coefficient to match fixes
   $\tau=4QP$, with no freedom left. There is then nothing to tune at the next
   order but $b$.
2. **Liouville is excluded, for every $b$ and every $\mu$.** With the dictionary
   fixed, the $\tau^{-2}$ coefficient of the Liouville delay is $+Q^2/3$ where the
   target is $-\frac1{24}$. Since $Q=b+b^{-1}\geq2$, the Liouville value is at
   least $\frac43$: **wrong sign, and at least $32$ times too large in
   magnitude.** The cosmological constant $\mu$ moves only the additive constant,
   so it cannot help. This closes the one lead the delay-test note had.
3. **The exclusion generalizes into a selection rule, and it is cheap.** For any
   unimodular $\Gamma$-ratio amplitude
   $S(\tau)=e^{2ic_1\tau}\prod_j\big[\Gamma(a_j+i\beta_j\tau)/\Gamma(a_j-i\beta_j\tau)\big]^{n_j}$,
   \[
    \mathcal T(\tau)=\Lambda\log\tau+c_0+\frac{1}{\tau^2}\sum_j\frac{n_jB_2(a_j)}{\beta_j}
    +O(\tau^{-4}),\qquad
    \Lambda=2\sum_jn_j\beta_j,\quad B_2(a)=a^2-a+\tfrac16 .
   \]
   Matching requires $\Lambda=1$ and $\sum_jn_jB_2(a_j)/\beta_j=-\frac1{24}$. With
   $n_j,\beta_j>0$ the second is negative only if some shift lies in
   \[
    \Big(\tfrac12-\tfrac1{2\sqrt3},\ \tfrac12+\tfrac1{2\sqrt3}\Big)
    =(0.21132\ldots,\,0.78867\ldots).
   \]
   $\Gamma_{\mathbb R}(s)$ at $s=\frac12+i\tau$ has $a=\frac14$ and is inside;
   $\Gamma_{\mathbb R}(s+1)$ has $a=\frac34$, also inside; $\Gamma_{\mathbb C}(s)$
   has $a=\frac12$, the deepest point. **$\Gamma(1+i\,\cdot)$ has $a=1$ and is
   outside** --- and that is what Liouville, and generic reflection amplitudes,
   are built from. **The shift has to sit near the critical line.**
4. **The three orders read as three arithmetic invariants.** $\Lambda$ is the
   *degree*: for $\prod_{j=1}^d\Gamma_{\mathbb R}(s+\mu_j)$ at $s=\frac12+i\tau$
   one has $\Lambda=d$ exactly. The $\tau^{-2}$ coefficient fixes the *shifts*,
   hence the place and the parity. The constant $c_0$ carries the *conductor*.
   So the delay expansion is not one weak test but a graded sequence, and the
   program has been reading only its first term.
5. **A rigidity theorem at a common shift.** If all $a_j$ are equal, the two
   conditions force $\sum_jn_j\leq\big(48|B_2(a)|\big)^{-1/2}$, with equality only
   when all $\beta_j$ agree. At $a=\frac14$ and $a=\frac34$ --- and only there ---
   the bound is exactly $1$, so with integer multiplicities there is **exactly one
   factor, $n=1$, $\beta=\frac12$, $a\in\{\frac14,\frac34\}$**: the archimedean
   factor of a degree-one $L$-function, of either parity, and nothing else.
6. **The hypothesis is needed.** With two different shifts the two conditions have
   solutions: $a_1=\frac12$, $a_2=1$, $n_1=n_2=1$,
   $\beta_1=0.157670\ldots$, $\beta_2=0.342329\ldots$ satisfies both. What is
   unconditional is the sign rule of item 3.

All of this is $200$ checks in the [delay-test check
programme](../numerics/check_delay_test.py), standard library only.

---

## 1. Fixing the dictionary

The target, from manuscript Proposition 4.3, is the group delay of the transfer
on the critical line,
\[
 \mathcal T_{\rm Weil}(\tau)=2\theta'(\tau)
 =\operatorname{Re}\psi\Big(\tfrac14+\tfrac{i\tau}{2}\Big)-\log\pi ,
\]
with $\tau$ conjugate to $x=\log r$. The candidate is the bulk Liouville
reflection amplitude, whose momentum $P$ is conjugate to the Liouville zero mode
$\phi$ through $e^{\pm2iP\phi}$.

The Liouville direction *is* the radial direction, so $\phi=\kappa x$ for some
constant $\kappa$, and the two spectral parameters are related linearly:
$2P\phi=\tau x$ gives $\tau=2\kappa P$. (This linearity is the one assumption. It
is what "the Liouville coordinate is the logarithm of the radius, up to
normalization" means; a nonlinear relation between two parameters that each
generate translations in their own coordinate is not available.)

Delays transform as $\mathcal T^{(\tau)}=\mathcal T^{(P)}/(2\kappa)$. Since
$\frac{d}{dP}\arg S=4Q\log P+O(1)$ with $Q=b+b^{-1}$, the leading coefficient in
$\tau$ is $2Q/\kappa$, and matching the target's coefficient of $1$ **forces**
\[
 \kappa=2Q,\qquad\text{that is}\qquad \tau=4QP .
\]
No freedom is left in the dictionary. The cosmological constant $\mu$ enters only
through the prefactor $(\pi\mu\gamma(b^2))^{-2iP/b}$, which is linear in $P$ and
therefore contributes only to the additive constant $c_0$. So at the next order
there is exactly one parameter, $b$, and one number to hit.

---

## 2. Liouville at second order

Writing $\operatorname{Re}\psi(a+iy)=\log y+\frac{B_2(a)}{2y^2}+O(y^{-4})$ with
$B_2(a)=a^2-a+\frac16$ --- verified to eight digits at five shifts --- the
Liouville delay is
\[
 \frac{d}{dP}\arg S(P)=4Q\log P+C_L+\frac{Q}{12P^2}+O(P^{-4}),
\]
the $Q/12$ confirmed to seven digits at three values of $b$. Substituting
$P=\tau/4Q$,
\[
 \mathcal T_L(\tau)=\log\tau-\log 4Q+\frac{C_L}{4Q}+\frac{Q^2}{3\tau^2}+O(\tau^{-4}),
\]
against
\[
 \mathcal T_{\rm Weil}(\tau)=\log\tau-\log2\pi-\frac{1}{24\tau^2}+O(\tau^{-4}).
\]

The constant matches for a unique $\mu$ at each $b$: $C_L=4Q\log\frac{2Q}\pi$.
**The $\tau^{-2}$ term cannot be matched at all.**

| $b$ | $Q$ | $\tau^{-2}$ coefficient | target | ratio |
|---|---|---|---|---|
| $0.3$ | $3.6333$ | $+4.4004$ | $-0.041667$ | $-105.6$ |
| $0.5$ | $2.5$ | $+2.0833$ | $-0.041667$ | $-50.0$ |
| $0.8$ | $2.05$ | $+1.4008$ | $-0.041667$ | $-33.6$ |
| $1.0$ | $2$ | $+1.3333$ | $-0.041667$ | $-32.0$ |
| $1.7$ | $2.2882$ | $+1.7453$ | $-0.041667$ | $-41.9$ |
| $3.0$ | $3.3333$ | $+3.7037$ | $-0.041667$ | $-88.9$ |

$Q\geq2$ for every $b>0$, so $Q^2/3\geq\frac43$: the sign is wrong at every
coupling and the magnitude is never within a factor of $32$. **Liouville is
excluded.** That the constant *can* be matched, by dialling $\mu$, is worth
noting on its own: in this candidate the conductor is not a discriminant, and the
discrimination has moved one order further out.

---

## 3. The general rule

Let a candidate's reflection amplitude be unimodular of $\Gamma$-ratio type,
\[
 S(\tau)=e^{2ic_1\tau}\prod_{j}
 \left(\frac{\Gamma(a_j+i\beta_j\tau)}{\Gamma(a_j-i\beta_j\tau)}\right)^{n_j},
 \qquad a_j>0,\ \beta_j>0,\ n_j>0,
\]
finitely many factors. Then $\arg S=2c_1\tau+2\sum_jn_j\arg\Gamma(a_j+i\beta_j\tau)$
and, since $\frac{d}{d\tau}\arg\Gamma(a+i\beta\tau)=\beta\operatorname{Re}\psi(a+i\beta\tau)$,

> **Proposition 3.1 (the expansion).**
> \[
>  \mathcal T(\tau)=\Lambda\log\tau+c_0+\frac{1}{\tau^2}\sum_j\frac{n_jB_2(a_j)}{\beta_j}+O(\tau^{-4}),
>  \qquad
>  \Lambda=2\sum_jn_j\beta_j,
> \]
> with $c_0=2c_1+2\sum_jn_j\beta_j\log\beta_j$.

> **Corollary 3.2 (the degree).** For the archimedean factor
> $\prod_{j=1}^d\Gamma_{\mathbb R}(s+\mu_j)$ of a degree-$d$ $L$-function,
> evaluated at $s=\frac12+i\tau$, one has $a_j=\frac{1/2+\mu_j}2$,
> $\beta_j=\frac12$, $n_j=1$, hence $\Lambda=d$. **The leading coefficient of the
> group delay is the degree**, which is the same statement as the zero density
> being $\frac{d}{2\pi}\log\frac{\tau}{2\pi}$. Matching the target's $\Lambda=1$
> therefore says: degree one.

> **Corollary 3.3 (the sign rule).** Matching the target's $\tau^{-2}$ coefficient
> $-\frac1{24}$ requires $\sum_jn_jB_2(a_j)/\beta_j<0$, hence at least one shift
> with $B_2(a_j)<0$, that is
> \[
>  \Big|a_j-\tfrac12\Big|<\tfrac1{2\sqrt3}=0.288675\ldots
> \]
> Every amplitude built solely from $\Gamma(m+i\,\cdot)$ with $m\geq1$ fails this,
> whatever its couplings and however many factors it has.

The values that matter:

| factor, at $s=\frac12+i\tau$ | $a$ | $B_2(a)$ | in the window |
|---|---|---|---|
| $\Gamma_{\mathbb R}(s)$ --- $\zeta$, even $\chi$ | $\frac14$ | $-\frac1{48}$ | yes |
| $\Gamma_{\mathbb R}(s+1)$ --- odd $\chi$ | $\frac34$ | $-\frac1{48}$ | yes |
| $\Gamma_{\mathbb C}(s)$ --- a complex place | $\frac12$ | $-\frac1{12}$ | yes, deepest |
| $\Gamma(1+i\,\cdot)$ --- Liouville, generic QFT | $1$ | $+\frac16$ | **no** |
| $\Gamma(\frac32+i\,\cdot)$ | $\frac32$ | $+\frac{11}{12}$ | **no** |

> **Proposition 3.4 (rigidity at a common shift).** Suppose all $a_j=a$. Then
> $\Lambda=1$ and $\sum_jn_jB_2(a)/\beta_j=-\frac1{24}$ determine the overall
> scales uniquely given the shape, and
> \[
>  \sum_jn_j\ \leq\ \frac{1}{\sqrt{48\,|B_2(a)|}},
> \]
> with equality if and only if all $\beta_j$ are equal.

*Proof.* $\sum n_j\beta_j=\frac12$ and $\sum n_j/\beta_j=\frac{1}{24|B_2(a)|}$;
Cauchy--Schwarz gives $(\sum n_j)^2\leq(\sum n_j\beta_j)(\sum n_j/\beta_j)$, with
equality iff the $\beta_j$ agree. $\square$

The bound is $1$ exactly when $|B_2(a)|=\frac1{48}$, that is $a\in\{\frac14,\frac34\}$.
So **if the multiplicities are integers**, as any Euler product gives, then
$\sum n_j=1$, one factor, $\beta=\frac12$, $a\in\{\frac14,\frac34\}$: the
archimedean factor of a degree-one $L$-function, either parity, uniquely.
Verified by exhaustive random search over exact solutions at four shifts: the
maximum of $\sum n_j$ is $1.000$, $1.000$, $0.500$, $0.693$ at
$a=\frac14,\frac34,\frac12,0.3$, in each case equal to the bound.

**The common-shift hypothesis is not removable.** With $a_1=\frac12$, $a_2=1$,
$n_1=n_2=1$ and $\beta_1=0.1576707808$, $\beta_2=0.3423292192$, both conditions
hold exactly. A positive $B_2$ can pay for a negative one. What survives without
hypotheses is Corollary 3.3.

---

## 4. What this changes

The delay-test note found that the leading $\log\tau$ is archimedean and cheap ---
the free dilatation generator on a half-line supplies it. This note finds where
the information actually is.

**Read as a sequence, the delay expansion recovers the arithmetic data of an
$L$-function one coefficient at a time:** the leading coefficient is the degree,
the $\tau^{-2}$ coefficient fixes the shifts and so the place and the parity, and
the constant is the conductor. That is a much better instrument than the single
test Condition 10.1 currently states, it costs nothing to apply, and it is
strong enough to have just removed the only candidate that survived the first
order.

It also relocates the arithmetic. The primes are not in this expansion at all ---
they are in the bounded fluctuation $S(\tau)=\pi^{-1}\arg\zeta(\frac12+i\tau)$,
which is invisible to every asymptotic order. So the expansion tests whether a
candidate has the right *archimedean* data, to any depth one likes, and says
nothing about whether it has any primes. Those are now cleanly separated
questions, which they were not before.

**An honest note on what has been excluded.** Liouville was a lead of one day's
standing; removing it costs the program nothing it had. What is worth keeping is
the shape of the failure. Liouville fails because its reflection amplitude is
built from $\Gamma(1+i\,\cdot)$, and it is built from $\Gamma(1+i\,\cdot)$ because
its spectrum is $\Delta=\frac{Q^2}4+P^2$ with the reflection acting on a
half-line with a *wall*, which puts the shift at an integer. An amplitude with the
shift at $\frac14$ would have to come from something whose natural variable is
$s/2$ --- a square root of the radial coordinate, or a two-sheeted cover. That is
a concrete structural hint and it is the first one this program has had about the
archimedean factor.

---

## 5. Status of every statement

* **Written proof.** Proposition 3.1 (from the Stirling expansion of $\psi$ and
  $\frac{d}{d\tau}\arg\Gamma(a+i\beta\tau)=\operatorname{Re}\psi$);
  Corollaries 3.2 and 3.3; Proposition 3.4 (Cauchy--Schwarz). The Liouville
  exclusion of Section 2 follows from 3.1 plus the dictionary of Section 1.
* **Assumption, stated once and used throughout Section 1.** That the relation
  between the Liouville momentum and the dilatation eigenvalue is linear. If it is
  not, Section 2 does not apply; Section 3 does not depend on it.
* **Written computation, verified.** Every number in Sections 1--3: group G of
  the [check programme](../numerics/check_delay_test.py), $43$ cases, standard
  library, worst error $1.7\times10^{-5}$ (the random-search bound), the algebraic
  identities to $10^{-10}$ or better; the programme now runs $200$ checks in seven
  groups and replays deterministically.
* **Reading.** The Liouville reflection amplitude and its normalization, from the
  Zamolodchikovs and from Fateev--Zamolodchikov--Zamolodchikov; quoted, not
  re-derived. Nothing else in this note is a reading.
* **Unconditional.** Nothing here uses the Riemann hypothesis, and nothing
  computes with $\zeta$: $\theta$ and $\psi$ are archimedean.
* **Not claimed.** No gauge theory is matched. The rigidity of Proposition 3.4 is
  a statement about $\Gamma$-ratio amplitudes with a common shift and positive
  couplings, not about all possible objects; Section 3's counterexample shows
  where it stops. The structural hint at the end of Section 4 is a hint.

---

## 6. Reproduction

```sh
python3 numerics/check_delay_test.py      # 200 checks, seven groups, standard library
```

Group G is this note.

---

## 7. Recommendation

Replace Condition 10.1 as Section 6 of the delay-test note proposes --- the object
is a ratio; the dilatation generator is not bounded below; the test is not the
leading term --- and add this note's expansion as the test itself, in three
graded clauses:

* **(i) degree.** $\Lambda=2\sum_jn_j\beta_j=1$.
* **(ii) place and parity.** $\sum_jn_jB_2(a_j)/\beta_j=-\frac1{24}$; in
  particular some shift must satisfy $|a_j-\frac12|<\frac1{2\sqrt3}$, which
  excludes every amplitude built from $\Gamma(\text{integer}+i\,\cdot)$.
* **(iii) conductor.** $c_0=-\log2\pi$, after (i) and (ii) are met and with no
  parameter left to absorb it.

And register `check_delay_test.py` in the `CHECKS` dictionary with that pass.
