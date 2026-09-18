# The shift is half a dimension: the archimedean factor is a horocycle integral, and the Loewner proposal closes

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Fourth note of the Loewner investigation, carrying out items 2 and 3
of the [opening note's](MARKOV_PART_AND_REALIZATIONS_20260917.md) plan --- the
Beta law from a radial chain, and the endpoint $\omega=\frac12$ --- and the one
part of the [previous note's](REGISTERED_ASSEMBLY_AND_THE_HORIZONS_20260918.md)
item 1 that had teeth. Programme:
[`numerics/check_beta_realization.py`](../numerics/check_beta_realization.py)
(registered, standard library, 43 cases, record
[`beta-realization-checks.json`](../numerics/records/beta-realization-checks.json)).

**Nothing here is a positivity statement, and nothing here is about the zeros.
The results are an exact identification of the archimedean factor and three
proofs that a conformal chain does not produce it.**

---

## 0. Summary

1. **The archimedean factor is a horocycle integral, in dimension $2\omega$.**
   Exactly, for every $\omega\in(0,\tfrac12]$,
   \[
    K^\Gamma_\omega(p)=\int_{\mathbb R^{d}}\big|t+i\big|^{-(p+b)}\,dt,
    \qquad d=2\omega,\quad b=\tfrac12+\omega ,
   \]
   and the causal kernel $k^\Gamma_\omega(\tau)\,d\tau$ is the push-forward of
   $|t+i|^{-b}\,dt$ under $\tau=\log|t+i|$. Its prefactor
   $2\pi^\omega/\Gamma(\omega)$ is **exactly the surface area of the unit sphere
   $S^{2\omega-1}$**. The archimedean delay is the log-modulus along the
   horocycle --- the arithmetic coordinate itself (Proposition 1.1).
2. **At $\omega=\frac12$ that is the modular surface, and it is the only integer
   in the family.** $d=1$ is the constant-term integral of the Eisenstein series
   over the one-dimensional horocycle of $PSL(2,\mathbb Z)\backslash\mathbb H$,
   which is why the endpoint is realized. $d=2\omega$ ranges over $(0,1]$ as
   $\omega$ ranges over $(0,\frac12]$, and contains exactly one integer.
   **The shift is half a dimension, and every geometry quantizes it.**
3. **Contraction at $\omega=\frac12$ is unconditional.** The poles of
   $K_{1/2}(p)=\xi(p)/\xi(p+1)$ are at $p=\rho-1$, with
   $\re p\in(-1,0)$ for every zero in the critical strip, so $K_{1/2}$ is inner
   on the right half-plane with no hypothesis at all and every compression is a
   contraction (Proposition 3.1). The family therefore runs from a *free*
   endpoint at $\omega=\frac12$ to the Riemann hypothesis at $\omega\downarrow0$:
   **the entire content of the program is the deformation inward**, and what
   obstructs it is the quantization of item 2 (Section 3).
4. **No radial chain produces the Beta law.** Three obstructions, each
   sufficient on its own (Section 2): the additivity fraction is *independent of
   the total*, so a dimension-$b$ chain cannot see the split $b=a+2\omega$ at all
   (Proposition 2.1); the antipodal exponent of the chord law of any radial
   chain is $-\frac12$ **for every driving**, because the Loewner drift vanishes
   at the antipode and only the Itô curvature survives, so the chord law is
   always $\mathrm{Beta}(\cdot,\frac12)$ while the transfer needs
   $\mathrm{Beta}(\frac a2,\omega)$ with both parameters below $\frac12$
   (Proposition 2.2); and the delay has a *power-law* singularity at zero delay,
   $E[U^q]\sim q^{-\omega}$, which no first-passage time from an interior start
   can have (Proposition 2.3). The pinned $\frac12$ is $d/2$ at $d=1$: the same
   quantization as item 2, in the other geometry.
5. **The Loewner proposal closes.** The comb was excluded on 17 September
   (far-field transport is a pure delay), the rational correction was shown to be
   forced and to carry no arithmetic, and the archimedean factor is excluded
   here. All three factors are now closed, with proofs. **The investigation's
   name records its origin, not a direction.**
6. **Side run: the second-order coefficient does not grow with the horizon.**
   Fitting $\lambda_{\min}(D_{N\subset N'})/2\omega=m_L^{(N)}(1+\alpha\omega+\beta\omega^2)$
   at $N=24$, $N'=64$ over four shifts gives $\beta=1.64,\,3.33,\,1.79$ at
   $L=\log3,\log5,\log7$, against the a-priori scale $\kappa_L^2$ of
   $3.7\times10^{3},\,6.4\times10^{12},\,5.4\times10^{22}$. The sufficient
   condition is pessimistic by 3, 12 and 22 orders of magnitude and the gap
   widens superexponentially: **the validity window of the first-order law does
   not collapse with $L$** (Section 5).

---

## 1. What the archimedean factor is

**Proposition 1.1 (the horocycle integral).** Let $0<\omega\leq\frac12$,
$a=\frac12-\omega$, $b=\frac12+\omega$, $d=2\omega$. Then for $\re p>0$
\[
 K^\Gamma_\omega(p)=\pi^\omega\frac{\Gamma\big(\frac{a+p}2\big)}{\Gamma\big(\frac{b+p}2\big)}
 =\int_{\mathbb R^{d}}\big(1+|t|^2\big)^{-\frac{p+b}2}\,dt
 =\int_{\mathbb R^{d}}\big|t+i\big|^{-(p+b)}\,dt ,
\]
the integral being read through
$\int_{\mathbb R^d}(1+|t|^2)^{-s}dt=\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)$ at
$s=\frac{p+b}2$. Moreover
\[
 k^\Gamma_\omega(\tau)\,d\tau
 =\text{push-forward of }\ |t+i|^{-b}\,dt\ \text{ under }\ \tau=\log|t+i|=\tfrac12\log(1+|t|^2),
\]
and the prefactor $2\pi^\omega/\Gamma(\omega)$ of $k^\Gamma_\omega$ is the
surface area $\lvert S^{d-1}\rvert=2\pi^{d/2}/\Gamma(\frac d2)$ of the unit
sphere in dimension $d=2\omega$.

*Proof.* With $s=\frac{p+b}2$ one has $s-\frac d2=s-\omega=\frac{p+a}2$, which
is the first identity. For the second, polar coordinates give
$dt=\lvert S^{d-1}\rvert r^{d-1}dr$, and $\tau=\frac12\log(1+r^2)$ gives
$r^2=e^{2\tau}-1$, $r\,dr=e^{2\tau}d\tau$, hence
$r^{d-1}dr=(e^{2\tau}-1)^{\frac d2-1}e^{2\tau}d\tau$. With $d=2\omega$ and
$e^{2\tau}-1=e^{\tau}\,2\sinh\tau$ this is
$e^{(\omega-1)\tau}(2\sinh\tau)^{\omega-1}e^{2\tau}d\tau$, and multiplying by the
weight $(1+r^2)^{-b/2}=e^{-b\tau}$ leaves
$(2\sinh\tau)^{\omega-1}e^{(\omega+1-b)\tau}=(2\sinh\tau)^{\omega-1}e^{\tau/2}$,
since $\omega+1-b=\frac12$. The prefactor is $\lvert S^{2\omega-1}\rvert$ by
inspection. $\square$

Three readings.

*The delay is the arithmetic coordinate.* $\tau=\log|t+i|$ is the log-modulus of
a point on the horocycle $\{y=1\}$ of the upper half-plane. The Wilson-lines
manuscript's arithmetic coordinate is $x=\log r$; the archimedean delay is that
coordinate, measured along a horocycle. The inherited note's first structural
affinity --- "Loewner time is log-conformal-radius, which is the arithmetic
coordinate exactly" --- turns out to be about the right variable and the wrong
object: the log-radius is a horocycle coordinate, not a capacity.

*The sphere is fractional.* The opening note observed that the two Bessel
dimensions $a$ and $2\omega$ are "fractional and below one, so there is no sphere
and no angle". Proposition 1.1 says there is a sphere, exactly: the prefactor of
$k^\Gamma_\omega$ is $\lvert S^{2\omega-1}\rvert$, and the statement is not that
the sphere is absent but that its dimension is $2\omega-1\in(-1,0)$.

*The Beta variable is the horocycle coordinate.* Substituting
$u=(1+|t|^2)^{-1}=e^{-2\tau}$ in the Riesz integral turns it into
$\frac{\pi^\omega}{\Gamma(\omega)}B\big(\frac{p+a}2,\omega\big)$, which is the
Beta identification of the previous note ($U=e^{-2\tau}\sim\mathrm{Beta}(\frac a2,\omega)$)
with the second Beta parameter now identified: $\omega=d/2$. **The second Beta
parameter is half the dimension of the horocycle.** That is the fact that does
all the work in Section 2.

---

## 2. Why no radial chain produces it

The proposal (opening note, item 3): a conformal-radius or hitting law of radial
Loewner evolution driven by a Bessel process of dimension $b$, whose squared
radius ratio is $U\sim\mathrm{Beta}(\frac a2,\omega)$. Three obstructions.

### 2.1 The fraction is independent of the total

**Proposition 2.1.** Let $Z_\delta$ denote the value at a fixed time of
$\mathrm{BESQ}^{(\delta)}$ from $0$. With $U=Z_a/(Z_a+Z_{2\omega})$ and
$S=Z_a+Z_{2\omega}\stackrel d=Z_b$, the variables $U$ and $S$ are independent;
at the level of processes, the Jacobi process $U_t$ and the total $Z_t$ are
independent (Warren--Yor). Hence $U$ is not a functional of the dimension-$b$
path.

*Proof of the fixed-time statement.* $\mathbb E[U^qS^r]=\mathbb E[Z_a^qS^{r-q}]$,
and in the coordinates $(s,u)=(x+y,\,x/(x+y))$ the Gamma density factorizes:
$\mathbb E[U^qS^r]=B(\frac a2+q,\omega)\Gamma(\frac b2+r)/(\Gamma(\frac a2)\Gamma(\omega))
=\mathbb E[U^q]\,\mathbb E[S^r]$. Checked to $10^{-15}$ over a grid of shifts and
exponents. $\square$

So a chain whose driving process has dimension $b$ cannot see the split
$b=a+2\omega$: the additivity fraction is fresh randomness, orthogonal to
everything the chain knows, and "dimension $b$" does no work in producing it.
This closes the *mechanism* the proposal names, whatever observable is chosen.

### 2.2 The antipodal exponent is pinned at one half

**Proposition 2.2.** Let a radial Loewner chain be driven by $e^{iW}$ with $W$ a
continuous semimartingale whose local volatility $\sigma$ is continuous and
non-vanishing at the antipode. A marked boundary point has angle obeying
$d\theta=\cot\frac\theta2\,dt-\sigma\,dB$, and the chord variable
$x=\sin^2\frac\theta2$ is a diffusion with
\[
 \sigma_x^2(x)=\sigma^2x(1-x),\qquad
 \mu_x(x)=(1-x)+\tfrac{\sigma^2}4(1-2x).
\]
Its speed density, the solution of $\tfrac12(\sigma_x^2m)'=\mu_xm$, satisfies
\[
 m(x)\asymp x^{\,2/\sigma^2(0)-1/2}\ \ (x\to0),\qquad
 m(x)\asymp (1-x)^{-1/2}\ \ (x\to1),
\]
the second exponent being $-\frac12$ **for every $\sigma$**. For constant
$\sigma^2=\kappa$ this is exactly $\mathrm{Beta}(\frac d2,\frac12)$ with
$d=1+\frac4\kappa$ the Bessel dimension.

*Proof.* Itô on $x=\sin^2\frac\theta2$ with
$\frac{dx}{d\theta}=\frac12\sin\theta$ and
$\frac{d^2x}{d\theta^2}=\frac12\cos\theta$ gives the coefficients, using
$\frac12\sin\theta\cot\frac\theta2=\cos^2\frac\theta2=1-x$ and
$\cos\theta=1-2x$. Then $2\mu_x/\sigma_x^2=N(x)/(x(1-x))$ with
$N(x)=2\mu_x/\sigma^2$, so the endpoint exponents of
$m=(\sigma_x^2)^{-1}\exp\int2\mu_x/\sigma_x^2$ are $N(0)-1$ and $-N(1)-1$. Now
$N(0)=2/\sigma^2(0)+\frac12$ is free, while
$N(1)=2\mu_x(1)/\sigma^2(1)=2(-\sigma^2(1)/4)/\sigma^2(1)=-\frac12$
**independently of $\sigma$**, because the Loewner drift $\cot\frac\theta2$
vanishes at $\theta=\pi$ and the only surviving term is the Itô curvature of the
chord map. For constant $\sigma^2=\kappa$ the identity
$\frac\kappa2\big[(p+1)(1-x)-\frac x2\big]=\mu_x(x)$ with $p=\frac2\kappa-\frac12$
is algebraic; checked to $10^{-13}$ at seven $\kappa$ and five $x$, and the two
limits checked to $10^{-5}$ for five drivings including two with $x$-dependent
$\sigma$. $\square$

**Corollary 2.2'.** The chord law of a radial chain, whenever it is a Beta law,
is $\mathrm{Beta}(\cdot,\frac12)$ --- or $\mathrm{Beta}(\frac12,\cdot)$ with the
orientation reversed. The target $\mathrm{Beta}(\frac a2,\omega)$ has
$\frac a2=\frac14-\frac\omega2<\frac14$ and $\omega<\frac12$: **both parameters
are strictly below $\frac12$ for every $\omega\in(0,\frac12)$**, so neither
orientation matches, at any shift. The two families meet only at
$\omega=\frac12$, where the target degenerates to $\mathrm{Beta}(0,\frac12)$ and
the dimension is forced to $0$.

And the pinned $\frac12$ is not a coincidence: by Section 1 the second Beta
parameter is $d/2$ with $d$ the dimension of the space integrated over, and the
radial chord law integrates over a one-dimensional fold. **The same quantization,
in the other geometry.**

### 2.3 The delay is singular at zero; first-passage times are not

**Proposition 2.3.** $k^\Gamma_\omega(\tau)\sim\frac{\pi^\omega2^\omega}{\Gamma(\omega)}\tau^{\omega-1}$
as $\tau\downarrow0$, and dually
$\mathbb E[U^q]\sim\frac{\Gamma(b/2)}{\Gamma(a/2)}q^{-\omega}$ as $q\to\infty$:
a power law, whose exponent is the shift. A first-passage time of a
non-degenerate diffusion from a fixed interior starting point has a density
vanishing faster than any power at $0$ and a Laplace transform decaying like
$e^{-c\sqrt q}$. So the archimedean delay is not such a hitting time, whatever
the driving.

*Proof.* The first is $(1-e^{-2\tau})^{\omega-1}\sim(2\tau)^{\omega-1}$ in the
form $k^\Gamma_\omega=\frac{2\pi^\omega}{\Gamma(\omega)}e^{-a\tau}(1-e^{-2\tau})^{\omega-1}$;
the second is Stirling in
$\mathbb E[U^q]=B(\frac a2+q,\omega)/B(\frac a2,\omega)$. Both checked
numerically ($10^{-8}$ and $10^{-6}$ relative at $\tau=10^{-9}$, $q=10^{7}$).
$\square$

### 2.4 What this leaves, and what it does not claim

The conformal radius seen from the marked point is $e^{-t}$, deterministic in the
capacity parametrization, so it is not a candidate at all; the transported radius
of an exterior point is a pure delay in the far field and not
translation-invariant elsewhere (opening note, Proposition 2.1); the chord law is
Proposition 2.2; hitting times are Proposition 2.3. That is a sweep of the
observables the proposal named --- "a conformal-radius or hitting law" --- and
not a theorem covering every conceivable functional of a chain. What *is*
general is Proposition 2.1: the mechanism, the additivity fraction of the chain's
own dimension, cannot work for any observable.

---

## 3. The endpoint, and what quantizes

### 3.1 Contraction there is unconditional

**Proposition 3.1.** $K_{1/2}(p)=\xi(p)/\xi(p+1)$ is inner on $\re p>0$
unconditionally, and consequently $\sup_L\lVert V_{1/2,L}\rVert=1$: every
compression is a contraction, with no hypothesis.

*Proof.* The poles of $K_{1/2}$ are the zeros of $\xi(p+1)$, i.e. $p=\rho-1$ with
$\rho$ a nontrivial zero; every such $\rho$ lies in the critical strip, so
$\re p\in(-1,0)$ and $K_{1/2}$ is holomorphic and bounded on $\re p>0$.
Unimodularity on the axis is the functional equation together with reality
(Wilson-lines Proposition 4.1). The conclusion is the dichotomy, whose
hypothesis "no zero at distance $>\omega$ from the line" is vacuous at
$\omega=\frac12$. $\square$

The instrument agrees: at $L=\log3$, $N=24$, $1-\lVert V_{\omega,L}\rVert$ is
$2.28\times10^{-8}$, $3.32\times10^{-8}$, $4.45\times10^{-8}$ at
$\omega=0.3,0.4,0.49$, growing with the shift, with $P_{\omega,L}\succ0$
throughout (records `cmgj_om{0.3,0.4,0.49}_log3_N24.json`).

So the shifted family runs between two very different ends. At $\omega=\frac12$
the conclusion is free. At $\omega\downarrow0$ it is the Riemann hypothesis.
**The whole content of the program is the deformation inward**, and the endpoint
is not a special case to be understood but the one place where nothing has to be
proved.

### 3.2 What the deformation would have to move

At $\omega=\frac12$ the transfer is, by the opening note's Section 3.3, the
Eisenstein scattering matrix of $PSL(2,\mathbb Z)\backslash\mathbb H$ with its
pole at $s=1$ removed by one Blaschke factor --- the Lax--Phillips modification.
Its archimedean part is, by Proposition 1.1 at $d=1$, the constant-term integral
\[
 \int_{\mathbb R}\lvert t+i\rvert^{-(p+1)}\,dt
 =\sqrt\pi\,\frac{\Gamma\big(s'-\frac12\big)}{\Gamma(s')},\qquad s'=\tfrac{p+1}2,
\]
over the one-dimensional horocycle at the cusp, and the arithmetic part is
$\zeta(2s'-1)/\zeta(2s')$, whose offset $1$ is the same $1$: both come from the
single $x$-integration that produces the constant term.

That is the obstruction, stated as sharply as this investigation can state it.
**The offset of a scattering matrix is the dimension of the horocycle it
integrates over, hence an integer; the shifted transfer's offset is $2\omega$.**
The $\omega$-deformation is a deformation of that dimension, and there is no
automorphic object with a cusp of dimension $2\omega\in(0,1)$. This is the same
statement as the opening note's "for $\omega<\frac12$ Eisenstein constant terms
give only unit offsets in $2s'$", with the reason supplied: the unit is a
dimension.

What this does *not* say: that no realization exists, only that no realization
of the kind that produces scattering matrices does, because those quantize the
offset. Nor does it say anything about the Lax--Phillips semigroup estimate at
the endpoint, which remains a reading task --- but a less urgent one, since the
endpoint conclusion is free and the estimate cannot transport inward past the
quantization.

---

## 4. The Loewner proposal closes

The three factors of $K_\omega=B_b\widehat K_\omega$, and their status:

| Factor | What it is | Loewner realization |
|---|---|---|
| Comb $K^\zeta_\omega$ | Hecke/Bost--Connes operator $\sum_n\widetilde c_n\mu_n$ | **Excluded** (opening note, Prop. 2.1): far-field transport is a pure delay, so a translation-invariant induced kernel has no atoms at $\log n$. |
| Correction $R_\omega$ | one Blaschke factor at the pole of $\zeta$ | **Excluded as data** (opening note, Prop. 3.1): forced by unimodularity, residues carry no arithmetic. |
| Archimedean $K^\Gamma_\omega$ | horocycle integral in dimension $2\omega$ (Prop. 1.1) | **Excluded** (Props. 2.1--2.3): the fraction is independent of the total, the antipodal exponent is pinned, the zero-delay singularity is a power law. |

All three are closed. The founding proposal of this folder --- that a
Loewner-type evolution could construct the deformation paths, with positivity
coming from conformality --- is answered in the negative, with proofs rather than
with an expectation. **The investigation's name records where it came from, not
where it is going.**

What survives of it is worth keeping. The proposal was right that the arithmetic
coordinate $x=\log r$ is the natural variable and that the transfer should be
read as transport in it; Proposition 1.1 says the log-radius is a *horocycle*
coordinate rather than a capacity, and the delay is the log-modulus along it. The
proposal was right that a realization must act on non-analytic observables; it is
the fractional dimension, not the analyticity, that blocks it.

---

## 5. Side run: the second-order coefficient does not grow with the horizon

The previous note left the question of whether the second-order coefficient of
the first-order law is of order $m_L$ or of order $m_L\kappa_L^2$ --- that is,
whether the window of shifts over which the first-order law is usable collapses
with the horizon as the sufficient path condition $\omega\kappa_L<\pi/4$ would
suggest. Fitting
$\lambda_{\min}(D_{N\subset N'})/2\omega=m_L^{(N)}(1+\alpha\omega+\beta\omega^2)$
to the nested defect at $N=24$, $N'=64$, over $\omega\in\{0.01,0.02,0.05,0.1\}$:

| $L$ | $m_L$ | $\kappa_L$ | $\kappa_L^2$ (a-priori scale) | $\alpha$ | $\beta$ (measured) |
|---|---|---|---|---|---|
| $\log3$ | $5.54\times10^{-8}$ | $61.1$ | $3.7\times10^{3}$ | $+0.044$ | $1.64$ |
| $\log5$ | $9.29\times10^{-18}$ | $2.53\times10^{6}$ | $6.4\times10^{12}$ | $-1.240$ | $3.33$ |
| $\log7$ | $6.80\times10^{-28}$ | $2.33\times10^{11}$ | $5.4\times10^{22}$ | $-1.356$ | $1.79$ |

(the quadratic fits reproduce all four shifts to $1\times10^{-4}$; $\kappa_L$ and
$m_L$ are from the Wilson-lines manuscript's Section 7; record
[`second_order_fit_N24_nested64.json`](../numerics/exploratory/README.md)). The
plain, unnested defect at $L=\log3$ gives $\alpha=0.537$, $\beta=0.400$ instead,
so $\beta$ is basis-dependent at the level of a factor of a few --- and at no
level beyond it.

**The measured coefficient is of order unity at every horizon, where the
a-priori scale runs $10^{3}$, $10^{12}$, $10^{22}$.** The sufficient condition is
pessimistic by 3, 12 and 22 orders of magnitude, and the gap widens
superexponentially. In practical terms the first-order law
$\lambda_{\min}(D_{\omega,L})/2\omega=m_L(1+O(\omega))$ is good to a few percent
for $\omega$ of order $10^{-1}$ at $L=\log7$, where the sufficient condition
would allow only $\omega<3\times10^{-12}$. The Wilson-lines remark that the
generator boundary $\omega_*\asymp\sqrt{m_L}$ is an artifact of a sufficient
condition is thereby quantitative: **it is not where the first-order law fails.**

A further datum, from the same runs: the Cayley-minus-defect gap of the previous
note, which is the basis-robust second-order quantity because the Galerkin term
cancels in it, is $0.036$, $0.030$, $0.027$ times $m_L\omega^2$ at the three
horizons --- flat across fourteen orders of magnitude of margin --- and holds its
shape out to $\omega=0.49$, where it is $0.053$.

---

## 6. What remains

With items 1, 2 and 3 of the opening note's plan closed or answered, the ranked
list is short and the top of it has changed.

1. **The fractional dimension, taken seriously.** Proposition 1.1 says the
   archimedean factor is $\int_{\mathbb R^{2\omega}}|t+i|^{-(p+b)}dt$. There are
   established frameworks in which integration over a space of fractional
   dimension $d$ is defined and has exactly the measure
   $\lvert S^{d-1}\rvert r^{d-1}dr$ used here --- dimensional regularization, and
   the Bessel/Hankel calculus of index $\frac d2-1$. The question is whether the
   comb and the pole factor also have expressions in that calculus at the same
   $d=2\omega$, so that the whole transfer is one object in a
   fractional-dimensional space rather than three pieces. If they do, the
   program has a realization of a different kind than it was looking for; if they
   do not, the obstruction is located at the comb and one knows where.
   This is the direction the note's own results point at, and it is new.
2. **The comb in the Bost--Connes algebra** (opening note, item 4), which is now
   also the question of what the comb is at $d=2\omega$.
3. **The passivity statement** (opening note, item 5).
4. The Lax--Phillips semigroup estimate at the endpoint, demoted: the endpoint
   conclusion is unconditional (Proposition 3.1) and the estimate cannot
   transport inward past the quantization of Section 3.2.

---

## 7. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 2.1 (fixed-time), 2.2,
  2.2', 2.3, 3.1.
- **Quoted:** the Warren--Yor process-level independence in Proposition 2.1; the
  dichotomy; the Eisenstein identification of the opening note's Section 3.3;
  $\kappa_L$ and $m_L$ from the Wilson-lines manuscript.
- **Registered computation (standard library, replayed byte-identically):**
  Sections 1 and 2, 43 cases, record
  [`beta-realization-checks.json`](../numerics/records/beta-realization-checks.json).
- **Labelled numerical computation (unregistered, `mpmath`):** the contraction
  data at $\omega=0.3,0.4,0.49$ of Section 3.1 and the fits of Section 5, with
  records in [`numerics/exploratory/`](../numerics/exploratory/README.md).
- **Reading:** Section 2.4 (the sweep is of the named observables, not of all
  functionals); the offset-is-a-dimension statement of Section 3.2 beyond the
  $SL(2,\mathbb Z)$ case written out; the direction proposed in Section 6, item 1.
- **Not claimed:** that no realization of any kind exists; anything about the
  zeros; any positivity.

See the [notes index](README.md) and the [investigation index](../README.md).
