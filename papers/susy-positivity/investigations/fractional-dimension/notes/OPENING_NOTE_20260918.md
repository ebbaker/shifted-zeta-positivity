# Opening note: the whole transfer at $d=2\omega$, and whether the dimension is more than a parameter

**Author: Claude Opus 5 (Anthropic), model `claude-opus-5`.** 18 September 2026
(New York). Opening note of the fractional-dimension investigation, written at
Edward Baker's direction and opened from the
[Loewner investigation](../../loewner/README.md), whose
[note of the same day](../../loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md)
identified the archimedean factor as a horocycle integral in dimension $2\omega$
and closed the Loewner proposal on all three factors. That investigation is
inherited whole and not repeated; its Proposition 1.1 is the starting point
here. Programme:
[`numerics/check_dimension_dictionary.py`](../numerics/check_dimension_dictionary.py)
(standard library, 72 cases, record
[`dimension-dictionary-checks.json`](../numerics/records/dimension-dictionary-checks.json)).

**Nothing here is a construction, no positivity is proved, and nothing assumes
the Riemann hypothesis. No value of $\zeta$ or $\xi$ is computed in the
programme.**

---

## 0. Summary

1. **All three factors are $d$-dimensional, with $d=2\omega$.** Put
   \[
    d=2\omega,\qquad s=\tfrac{p+b}2\quad(\text{so }2s=p+b,\ 2s-d=p+a,\ b=\tfrac{d+1}2).
   \]
   Then the Markov part of the transfer is
   $\Lambda(s_0-\omega)/\Lambda(s_0+\omega)=\Lambda(2s-d)/\Lambda(2s)$, and factor
   by factor: the archimedean part is the Riesz integral of $|t+i|^{-(p+b)}$ over
   $\mathbb R^{d}$ (inherited); **the comb's weights are the Jordan totient**,
   $\widetilde c_n=J_d(n)/n^{(d+1)/2}$ with $J_d(n)=n^d\prod_{p\mid n}(1-p^{-d})$,
   which for integer $d$ counts the primitive vectors in $(\mathbb Z/n\mathbb Z)^d$
   (Proposition 1.2); and the Blaschke factor sits at $p=b=\frac{d+1}2$, i.e.
   $2s=d+1$, the pole of the volume term. At $d=1$ this is the Eisenstein
   scattering matrix of $PSL(2,\mathbb Z)\backslash\mathbb H$, the horocycle is
   one-dimensional and $\widetilde c_n=\varphi(n)/n$.
2. **So the comb is $d$-dimensional in the same sense the archimedean factor
   is.** The question the Loewner note posed --- whether the comb and the pole
   factor also have expressions in the $d=2\omega$ calculus --- is answered *yes*
   at the level of formulas, and answered on the first day rather than after a
   search. The dictionary is now complete and is the object of this
   investigation (Section 1).
3. **What that does not settle, and what this investigation is for.** $J_d(n)$ is
   a perfectly good multiplicative function at fractional $d$, but it stops
   counting anything; $\mathbb R^{d}$ stops being a space; and
   $\Lambda(2s-d)/\Lambda(2s)$ stops being anybody's scattering matrix. The
   dictionary may therefore be a reparametrization and nothing more. **The
   question is whether $d$ is a dimension or a parameter** --- and, if it is only
   a parameter, whether analytic continuation in it can still carry an argument,
   as it does in dimensional regularization (Section 2).
4. **Why it is worth asking.** Three independent obstructions found in the
   Loewner investigation were all the same obstruction: the Eisenstein offset is
   an integer because it is a horocycle dimension; the antipodal exponent of a
   radial chord law is $\frac12=d/2$ at $d=1$ because the fold is
   one-dimensional; and the SLE dictionary $d=1+4/\kappa$ never reaches $(0,1)$.
   Every geometric realization quantizes the dimension. If $d$ is only a
   parameter, that is the whole story and this investigation closes quickly with
   a clean statement of why. If it is not, the family is a deformation of the
   modular surface in its cusp dimension, and the deformation is the content of
   the Riemann hypothesis (Section 3).

---

## 1. The dictionary

Throughout $s_0=\frac12+p$, $a=\frac12-\omega$, $b=\frac12+\omega$,
$0<\omega\leq\frac12$, and
\[
 d=2\omega,\qquad s=\frac{p+b}2 .
\]
Then $2s=p+b$, $2s-d=p+a$, and $b=\frac{d+1}2$.

> **Proposition 1.1 (the transfer in the $d$ variable).** The Markov part of the
> shifted Weil transfer is
> \[
>  \widetilde K_\omega(p)=\frac{\Lambda(s_0-\omega)}{\Lambda(s_0+\omega)}
>  =\frac{\Lambda(2s-d)}{\Lambda(2s)}
>  =\pi^{d/2}\frac{\Gamma\big(s-\frac d2\big)}{\Gamma(s)}\cdot
>   \frac{\zeta(2s-d)}{\zeta(2s)} ,
> \]
> and the full transfer is $K_\omega=R_\omega\widetilde K_\omega$ with the
> Blaschke factor's pole at $p=b=\frac{d+1}2$, that is at $2s=d+1$.

*Proof.* Substitution; $\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$ gives the third
form. At $d=1$ the middle expression is $\Lambda(2s-1)/\Lambda(2s)$, the
Eisenstein scattering matrix. $\square$

This is a reparametrization and is stated for bookkeeping. The content is that
each of the three factors, written in $d$, is an object that has a
$d$-dimensional meaning at integer $d$.

**The archimedean factor** (inherited, Loewner note Proposition 1.1):
$\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)=\int_{\mathbb R^{d}}|t+i|^{-(p+b)}\,dt$,
the delay is $\log|t+i|$, and the kernel's prefactor is the area of
$S^{d-1}$. At $d=1$ it is the constant-term integral over the horocycle at the
cusp.

**The comb** is the new half.

> **Proposition 1.2 (the comb weights are the Jordan totient).** The Dirichlet
> coefficients of $\zeta(u-d)/\zeta(u)$ are the Jordan totient
> $J_d(n)=n^d\prod_{p\mid n}(1-p^{-d})$, and the transfer's comb weights are
> \[
>  \widetilde c_n=n^{\omega-\frac12}\prod_{p\mid n}\big(1-p^{-2\omega}\big)
>  =\frac{J_d(n)}{n^{(d+1)/2}} .
> \]
> For a positive integer $d$, $J_d(n)$ is the number of primitive vectors in
> $(\mathbb Z/n\mathbb Z)^d$ --- the $d$-dimensional reduced fractions with
> denominator $n$. At $d=1$, $J_1=\varphi$ and $\widetilde c_n=\varphi(n)/n$.

*Proof.* $\zeta(u-d)/\zeta(u)=\sum_n(\sum_{ke=n}e^d\mu(k))n^{-u}$, and at
$n=p^m$ the inner sum is $p^{md}-p^{(m-1)d}=p^{md}(1-p^{-d})$, so it is
multiplicative with the stated value. Then
$J_d(n)/n^{(d+1)/2}=n^{d-\frac{d+1}2}\prod(1-p^{-d})=n^{\frac{d-1}2}\prod(1-p^{-2\omega})$
and $\frac{d-1}2=\omega-\frac12$. The count is the standard interpretation of
$J_d$: inclusion--exclusion over the primes dividing $n$ on the $n^d$ vectors of
$(\mathbb Z/n\mathbb Z)^d$. Checked to $10^{-13}$ for $n<120$ at seven shifts, by
Möbius convolution for six $d$ including fractional ones, and by brute-force
primitive-vector counts for $d\in\{1,2,3\}$, $n\leq12$; and in exact rationals at
$d=1$. $\square$

So the dictionary reads:

| Factor | In the $d$ variable | What it is at integer $d$ |
|---|---|---|
| Archimedean | $\pi^{d/2}\Gamma(s-\frac d2)/\Gamma(s)$ | $\int_{\mathbb R^{d}}|t+i|^{-(p+b)}dt$; at $d=1$ the horocycle constant term |
| Comb | $\zeta(2s-d)/\zeta(2s)$, weights $J_d(n)/n^{(d+1)/2}$ | primitive vectors in $(\mathbb Z/n\mathbb Z)^d$; at $d=1$, $\varphi(n)/n$ |
| Correction | Blaschke factor at $p=\frac{d+1}2$ | the pole of $\zeta(2s-d)$ at $2s=d+1$: the volume term |
| The whole | $\Lambda(2s-d)/\Lambda(2s)$ | at $d=1$, the Eisenstein scattering matrix |

Two remarks. The shift enters *only* as a dimension: nowhere in the table does
$\omega$ appear except through $d=2\omega$, and $\frac{d+1}2=b$ carries the
Blaschke factor, so the pole factor is a dimension too. And the $d$-dependence is
uniform: the same $d$ appears in the sphere area, in the Gamma shift, in the
$\zeta$ offset and in the Euler factors, which is why the dictionary is worth
taking seriously rather than treating as four coincidences.

---

## 2. The question

At $d=1$ every entry of the table is an object. At fractional $d$ every entry is
still a *formula*, and the formulas remain consistent with each other --- that is
what Section 1 establishes. Nothing in it says the formulas describe anything.

**The question of this investigation.** Is $d=2\omega$ a dimension, or a
parameter? Concretely, in decreasing order of what would be gained:

1. *Is there an object?* A space, a lattice, a groupoid, an algebra, in which
   $d$ is not required to be an integer and in which $\Lambda(2s-d)/\Lambda(2s)$
   is a scattering matrix, a spectral determinant, or a transfer. If so, the
   shifted family is a deformation of the modular surface in the dimension of its
   cusp, and the Riemann hypothesis is a statement about that deformation.
2. *Is there a calculus?* Failing an object, is there a calculus in which the
   $d$-dependence is legitimate as analytic continuation --- as it is in
   dimensional regularization, where $\int d^dk$ is defined for complex $d$ by the
   rotation-invariant, additive, homogeneous extension, and where the radial
   measure $|S^{d-1}|r^{d-1}dr$ used by Proposition 1.1 is exactly what carries
   it. If so, the question becomes whether an argument about $\lVert V_{\omega,L}\rVert$
   can be run at complex $d$ and continued back.
3. *Or is it neither?* In which case the right output is a clean statement of
   why: which property of the transfer at $d=1$ fails to continue, and what that
   says about the family. That would be a real result and it closes this
   investigation.

**What would count as failure, stated in advance.** The comb's Euler product
$\prod_p(1-p^{-d})^{-1}$-type structure converges for $\Re d>1$; at $d=2\omega\leq1$
it is on or inside the boundary of convergence, which is exactly where
$\zeta(2s-d)$ has its pole and where the arithmetic lives. If every candidate
object requires $d>1$ to exist, the family's range $d\in(0,1]$ is precisely the
inaccessible one, and that is the answer.

---

## 3. What to do, ranked

1. **The Bessel--Hankel index.** The radial Laplacian in dimension $d$ has Bessel
   index $\nu=\frac d2-1=\omega-1$, and the archimedean kernel is
   $k^\Gamma_\omega(\tau)\propto(2\sinh\tau)^{\omega-1}e^{\tau/2}=(2\sinh\tau)^{\nu}e^{\tau/2}$.
   The factor $(\sinh\tau)^{\nu}$ is also the radial Jacobian of hyperbolic space
   of dimension $\nu+1=\omega$. Two dimensions are therefore in play, $d=2\omega$
   Euclidean and $\omega$ hyperbolic, and they are not the same. Establish which
   one the kernel is really carrying, or that the coincidence is formal. This is
   self-contained, needs no arithmetic, and should be done first because
   everything below depends on which calculus is the right one.
2. **The comb at fractional $d$.** $J_d$ is multiplicative and defined for any
   $d$; is there anything it counts, or bounds, or is a dimension of? The natural
   candidates are a Bost--Connes-type algebra with a $d$-dependent state, and the
   zeta function of a lattice or a space of fractional dimension. This is the
   Loewner investigation's open item 4 in a sharper form.
3. **The Blaschke factor as a volume term.** At $d=1$ the pole at $2s=d+1$ is the
   residue of the Eisenstein series, the volume of the surface. At general $d$ it
   is the pole of $\zeta(2s-d)$, and the Loewner investigation proved the factor
   is forced by unimodularity and carries no arithmetic. If $d$ is a dimension,
   that factor should be a volume, and its coefficient should be computable as
   one. A short check with a decisive outcome.
4. **Dimensional regularization of the criterion.** Whether
   $\lVert V_{\omega,L}\rVert$, or the first-order law
   $\lambda_{\min}(D_{\omega,L})/2\omega\to m_L$, has a meaning as a function of
   complex $d$, and whether the contraction statement continues. The Loewner
   investigation's instrument computes the left-hand side for any $\omega$ in
   $(0,\frac12]$ already, so this is testable numerically before it is
   understood.
5. **The endpoint as a boundary condition.** $d=1$ is where the family is both
   realized and unconditional (Loewner note Proposition 3.1). Any continuation in
   $d$ has a known boundary value there; what does the derivative in $d$ at $d=1$
   compute?

---

## 4. What not to redo

- Do not look for a Loewner or conformal-chain realization of any factor: all
  three are closed ([Loewner note of 18 September](../../loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md),
  Section 4).
- Do not treat the Blaschke factor's residues as arithmetic data (Loewner
  investigation, Proposition 3.4 of its manuscript).
- Do not expect structural positivity of the Markov part to bound
  $\lVert V_{\omega,L}\rVert$; the cancellation between the positive part and its
  exponential moving average is the whole content.
- Do not re-derive the elementary assembly of $V_{\omega,L}$: it exists, is
  registered, and runs in double precision at any horizon whose atoms one is
  willing to sum ([Loewner investigation](../../loewner/numerics/README.md)).
  Use it.

---

## 5. Status of every statement

- **Written proof, unconditional:** Propositions 1.1 and 1.2.
- **Inherited:** the horocycle representation of the archimedean factor and the
  three exclusions, from the Loewner investigation, with their own proofs there.
- **Registered computation (standard library):** the dictionary of Section 1,
  72 cases, record
  [`dimension-dictionary-checks.json`](../numerics/records/dimension-dictionary-checks.json).
  It will be wired into a `CHECKS` dictionary once this investigation has a
  manuscript.
- **Reading:** the hyperbolic-versus-Euclidean remark of Section 3, item 1; the
  expectation in Section 2 that the boundary of convergence is where the
  difficulty sits.
- **Not claimed:** that $d$ is a dimension; that any object realizes the family
  at fractional $d$; anything about the zeros; any positivity.

See the [notes index](README.md) and the [investigation index](../README.md).
