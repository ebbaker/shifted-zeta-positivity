# Theta cusp construction and uniformity in moving primes

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is an internal proof read-through and finite checking, not independent
specialist validation or formal verification.

## Scope and result

The primary source is the manuscript dated 5 October 2026,
[`paper2.tex` at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Line numbers refer to its physical TeX lines. The target statements are
`lem:reflection` and `lem:reflection-uniformity` (1807–1857); the portion
audited here is `app:fixed-ray`, 2874–3279, and the final uniformity
paragraph, 3438–3451. The Mellin/archimedean continuation and the subsequent
quadratic mean square are separate audit targets.

**Result:** under the stated theta automorphy and cubic reciprocity
inputs, the finite Fourier expansion, reduced cusp denominator,
three cusp reductions, conjugated multiplier, additive CRT phase and
fixed finite family `(d,psi,c0)` close. The moving primes do not have
to enter the fixed modulus. No unresolved estimate or moving-prime
dependence in the cusp constants was found in this portion.

One omitted technical choice merits an explicit clarification: the
September 30 text avoids zero entries before using residue-symbol
formulas, while October 5 omits that paragraph. Section 5 below supplies
the allowed translations and CRT changes. They preserve all fixed data,
so this is a repairable choice convention rather than a missing analytic
estimate. No claim about the theorem's validity is inferred from its
large consequences.

## 1. Fixed data and the finite Fourier expansion

Keep `Psi0` and `S` fixed. Choose `L` supported on `S`, divisible by the
ray conductor, every prime in `S`, and sufficiently high powers above
2 and 3. The fixed multiplier is

\[
 \phi(n)=\begin{cases}
 \chi_n(\lambda)^2\Psi_0(n),&n\equiv1\pmod3, (n,S)=1,\\
 0,&\text{otherwise}.
 \end{cases}
\]

This is a piecewise definition: no value of `chi_n(lambda)` is
evaluated outside the indicated primary domain prime to `S`.
Its supplementary cubic factor is periodic modulo a fixed power of
`lambda`; thus it is genuinely periodic modulo such an `L`. The zero
extension is retained. This is source 2906–2940; the elementary local
expansion `eq:ray-fourier` is at 2984–2995.

Writing `q=N(p)`, the four possible Fourier coefficients are

\[
 C_{p,j}(h)=
 \begin{cases}
 q^{-1/2}\chi_p(-1)^j\gamma_j(p)\chi_p(h)^{-j},&j\ne0, h\ne0,\\
 0,&j\ne0, h=0,\\
 -q^{-1},&j=0, h\ne0,\\
 1-q^{-1},&j=0, h=0.
 \end{cases}
\]

For nonzero `h`, substitute `y=h^(-1)*u` in the defining finite Fourier
sum; the sign in `e(-u/p)` contributes `chi_p(-1)^j`. At `h=0`, use
orthogonality or count the `q-1` units. In particular `j=0` is still
the unit mask, not the constant-one function.

An active prime means `h_p!=0`. Every prime with `j_p!=0` is forced
active; only a zero-exponent prime has a second, inactive branch.
The finite sum of translates has shift and coefficient

\[
 z_{\boldsymbol h}=\lambda^2\left(h_0/L+
              \sum_{p\in\mathcal P}h_p/p\right),\qquad
 c_F(\boldsymbol h)=\widehat\phi(h_0)\prod_p C_{p,j_p}(h_p).
\]

The factor `lambda^2` follows from
`e(z)=breve_e(z/lambda)` and `n=lambda^3*ell`. This checks the
orientation against the conjugate theta Fourier series. The constant
terms cancel in this finite expansion because the sum of Fourier
coefficients is `phi(0)*product chi_p^j(0)=0`, including when the
moving prime set is empty (2962–2972). This cancellation precedes the
later differentiation at the cusp; it does not assert that every
individual translated theta function has zero constant term.

## 2. Reduced fractions and the fixed congruence sector

For each fixed frequency choose a reduced fraction
`lambda^2*h0/L=a0/c0`. Normalize `a0` to be primary if `lambda|c0`,
and `c0` to be primary otherwise. All active primes are primary, so
this unit choice depends only on `h0`. With their product `r`,

\[
 c=c_0r,\qquad
 a=a_0r+\lambda^2c_0\sum_{p\mid r}(r/p)h_p.
\]

At `p|r`, the numerator is `lambda^2*c0*(r/p)*h_p mod p`, a unit.
At a prime of `c0`, it is the unit `a0*r`. Hence `gcd(a,c)=1`;
nonunit `h0` causes no problem. In particular, the actual denominator
is the active denominator `c0*r`, not necessarily the conductor of the
original multiplicative character. Source 2997–3025 makes this distinction.

Set `M=lambda^12*L^4`. Each active frequency can be lifted with
`h_p=0 mod M^2`, since the moving primes are outside `S`. Its residue
modulo `p` remains arbitrary nonzero. Such a lift changes a translate
only by `lambda^2*O=3*O`, a period of theta. Because `c0` divides `L`
up to a unit, fixing `r mod M^2` fixes `a mod M*c0`.

The CRT conditions for `delta` in source 3056–3059 specify

- `a*delta=1` modulo the prime-power parts of `M*c0` at primes of `c0`;
- `delta=0` modulo the prime-power parts of `M` at its other primes;
- `a*delta=1 mod r`.

They are compatible. Their combined modulus is `M*c`, up to a unit.
For `b_g=(a*delta-1)/c`, division leaves

\[
 b_g\equiv0\pmod{q^{v_q(M)}}\quad(q\mid c_0),
 \qquad
 b_g\equiv-c^{-1}\pmod{q^{v_q(M)}}\quad(q\mid M, q\nmid c_0).
\]

Thus the needed fixed-prime residues of `a,b_g,c,delta` are constant
as the active frequencies vary. Their magnitudes need not be bounded;
the proof needs these residues, not bounded integer representatives.

## 3. The three matrices really reduce to three fixed expansions

Let `g=[[a,b_g],[c,delta]]`; its determinant is one. Put
`E=[[0,-1],[1,0]]`, `T_z=[[1,z],[0,1]]`, and
`L_z=[[1,0],[z,1]]`. The three source choices of `H` give

| Condition | `H` | `g1=g*H^(-1)` | Residues forcing `g1=I mod 3` |
| --- | --- | --- | --- |
| `3|c` | `I` | `g` | `a=delta=1`, `b_g=c=0 mod 3` |
| `v_lambda(c)=1` | `L_u`, `u=+lambda` or `-lambda`, `u=c mod 3` | `[[a-u*b_g,b_g],[c-u*delta,delta]]` | `a=delta=1`, `b_g=0`, `c=u mod 3` |
| `(c,lambda)=1` | `T_u*E`, `u=a mod 3` | `[[-b_g,a+u*b_g],[-delta,c+u*delta]]` | `c=1`, `delta=0`, `b_g=-1 mod 3` |

These are the matrices of source 3076–3089. In the middle case the
two nonzero residues divisible by `lambda` modulo 3 are exactly
`+lambda` and `-lambda`; there is no omitted ramified cusp branch.

To check the reduction of `theta(Hw)`, use
`L_z=E*T_(-z)*E^(-1)`. Theta is invariant under left multiplication
by `E` and under translations by `Z+3*O`; `E^(-1)` and `E` have the
same action on upper half-space. Consequently

\[
 \theta(L_z w)=\theta(T_{-z}Ew),\qquad
 \theta(\gamma_-w)=\theta(T_\omega Ew),\qquad
 \theta(\gamma_+w)=\theta(T_{-\omega}Ew).
\]

For `H=L_lambda`, this is the minus cusp; `H=L_(-lambda)` gives the
plus cusp. For `H=T_(s+t*omega)*E`, reduce `t mod 3`: `t=0,1,2`
gives respectively the infinity, minus and plus cusp. These reductions
use transformations with multiplier one; an additional unexplained
root of unity is not needed.

The direct external comparison was with
[Dunn–Radziwiłł, Section 5.1, equations (5.4)–(5.16), and Appendix A](https://arxiv.org/html/2109.07463v3#S5.SS1).
Their matrices numbered 1, 10 and 19 are the source's `gamma0`,
`gamma+`, `gamma-`. Their coefficient table agrees with
`t_-(ell)=omega^2*tau1(omega^2*ell)*breve_e(ell)` and
`t_+(ell)=omega*tau2(omega*ell)*breve_e(ell)`.
Their conjugation formula changes the frequency to `-ell`, so the
source's `d_sigma(ell)=conj(t_sigma(-ell))` is correct. The two
non-infinity cusps have no constant term. This checks the cited
interface, not Patterson's theorem or a new construction of theta.
No GRH assumption from the other results of that paper is invoked in
these Section 5 automorphy formulas.

In particular, one must not replace `d_sigma(ell)` by
`conj(t_sigma(ell))` merely because the infinity coefficient is even;
the non-infinity sequences have different support.

## 4. Re-deriving the multiplier instead of relying on its claim

The imported automorphy law is
`theta(g1*w)=kappa(g1)*theta(w)` with `kappa(g1)=(c1/a1)_3`
for a nonzero lower-left entry, and one for the upper-triangular
case. The three calculations below verify `eq:ray-multiplier`
(3174–3205). Residue symbols in intermediate manipulations can be
assumed to have nonzero entries by the choices in Section 5.

**If `3|c`:** `a` and `r` are primary, so cubic reciprocity gives

\[
 \kappa(g_1)=(c/a)_3=(c_0/a)_3(r/a)_3
                         =(c_0/a)_3(a/r)_3.
\]

The fixed-prime factor `(c0/a)_3` is determined by `a mod 9` for its
unit and ramified parts, and by residues of `a` at the primes of
`c0` after reciprocity. These are among the already fixed residues.

**If `v_lambda(c)=1`:** let `A=a-u*b_g`, `C1=c-u*delta`. Both `A`
and `a` are primary and coprime: `gcd(a,b_g)=1` and `gcd(a,u)=1`.
The determinant identity gives

\[
 aC_1=cA-u,\qquad b_gc\equiv-1\pmod a.
\]

Therefore

\[
 \begin{aligned}
 \kappa(g_1)
 &=(-u/A)_3(a/A)_3^{-1}\\
 &=(-u/A)_3(A/a)_3^{-1}\\
 &=(-u/A)_3((c/u)/a)_3\\
 &=(-u/A)_3((c_0/u)/a)_3(a/r)_3.
 \end{aligned}
\]

The third equality uses `A=-u*b_g mod a` and `b_g*c=-1 mod a`.
The factor `c0/u` is integral and supported on `S`. Both fixed
factors depend only on `a,A mod 9` and the fixed-prime residues.
Since `A=a-u*b_g`, those data were fixed in Section 2.

**If `(c,lambda)=1`:** `g1` has upper-left entry `-b_g` and lower-left
entry `-delta`. Both `-b_g` and `c` are primary. Put

\[
 q=-b_gc=1-a\delta\equiv1\pmod9.
\]

Factor `delta=epsilon*lambda^k*delta0`, with `delta0` primary. The
supplementary laws give `(epsilon*lambda^k/q)_3=1`; reciprocity gives
`(delta0/q)_3=(q/delta0)_3=1`, since `q=1 mod delta0`. Thus

\[
 (\delta/(-b_gc))_3=1,\qquad
 \kappa(g_1)=(\delta/(-b_g))_3
   =(\delta/c)_3^{-1}=(a/c)_3=(a/c_0)_3(a/r)_3.
\]

This justifies the compressed step at source 3191–3196. It does not
require the moving numerator `delta` to have support on `S`.
The fixed factor is now directly determined by `a mod c0`.

In all cases

\[
 \kappa(g_1)=\kappa_0\prod_{p\mid r}\chi_p(a)^2,
 \quad |\kappa_0|=1,
\]

with `kappa0` constant in the fixed sector. The conjugate theta in
`eq:theta-cusp-automorphy` requires `conj(kappa(g1))`, hence local
exponent **-2**, not +2. Combining with the original Fourier
coefficient `chi_p(h)^(-j)` and `a=sigma_p*h mod p` gives
`chi_p(h)^(-j-2)`. After `y=h^(-1)` the Gauss-sum exponent is `j+2`;
the resulting column exponent is `-j-2`. Thus `j=1` becomes the
quadratic factor `chi_p(x)^3`, exactly as needed downstream.

The special `j=4` exponent gives a Ramanujan sum
`-1+N(p)*1_(p|x)`, and active `j=0` retains its factor `N(p)^(-1/2)`.
The former can be as large as `N(p)^(1/2)` after normalization and
must stay in `B_(p,4)`, not be absorbed into the bounded scalar.
Source 3231–3279 handles both exceptional cases explicitly.

## 5. The omitted zero-entry convention is repairable

The September 30 source at the same pinned commit explicitly discusses
this at lines 2122–2127 of
[`build/paper.tex`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex#L2122).
October 5 no longer states the paragraph. It is possible, for example,
to have `a=0,c=1,delta=0` for the zero shift, whereas a proof that
factors `delta` must first avoid or handle that case.

The available choices are enough. Replace the cusp by

\[
 a/c\longmapsto a/c+\lambda^2M^2z,
 \qquad a\longmapsto a+\lambda^2M^2cz.
\]

This is a theta period, preserves `gcd(a,c)=1`, and preserves `a mod
M*c0`. Choose `z` to avoid `a=0`. Next choose a CRT solution and vary

\[
 \delta\longmapsto\delta+Mc\,t,
 \qquad b_g\longmapsto b_g+aM\,t.
\]

All prescribed congruences and the determinant equation are preserved.
Avoid the finitely many `t` that make any entry needed in the relevant
residue-symbol calculation zero, including `delta`, `b_g`, `a-u*b_g`
and `c-u*delta` in the middle case. Those expressions are nonconstant
affine functions after `a!=0`, so this excludes only finitely many
values in an infinite lattice.

The choices retain `H`, `kappa0`, and `psi`: `b_g mod M` is unchanged,
and `lambda^3*c0` divides `M*c`. Nothing requires these new
representatives to be small. Alternatively the simple upper-triangular
exception can use its multiplier-one convention directly. This note
records the clarification rather than silently crediting October 5
with its predecessor's explicit paragraph.

## 6. Additive phase and the finite-family conclusion

The source's cusp coordinates `eq:theta-cusp-coordinates` (3166–3169)
give the phase `breve_e(-delta*ell/c)` at `z=0`. Set
`x=lambda^4*ell in O` and `D0=lambda^3*c0`. Then

\[
 \breve e(-\delta\ell/c)=e(-\delta x/(D_0r)).
\]

The local CRT numerators for the coprime factors `D0` and `r` are

\[
 -\delta_0r^{-1}\pmod{D_0},\qquad
 -\delta(D_0r/p)^{-1}\pmod p.
\]

With `sigma_p=lambda^2*c/p`, the congruence `a=sigma_p*h_p mod p`
gives `delta=sigma_p^(-1)*h_p^(-1) mod p`. The second CRT numerator
is consequently `epsilon_p*h_p^(-1)`, where

\[
 \epsilon_p=-\big((\lambda^3c/p)\sigma_p\big)^{-1}\pmod p.
\]

This proves the signs and lambda powers in `eq:ray-additive-crt`
(3218–3229), with
`psi(x)=e(-delta0*r^(-1)*x/D0)`. The residual character has modulus
`D0`, supported solely on `S`. Its numerator lies in a finite residue
ring. The source is not asserting that its conductor contains no
ramified factor, or that it is a multiplicative ray character.

For the uniformity lemma, every prime of `k0` has local exponent one
and is forced active. Thus, for a fixed active subset of the other
prime factors,

\[
 r=k_0r_{\rm fix}.
\]

Fixing `k0 mod M^2` fixes `r mod M^2`. The number of such classes
depends only on `Psi0,S`. All relevant data are now accounted for:

| Datum | Dependence left after fixing the sector |
| --- | --- |
| `c0` | One of the finitely many reduced denominators from `h0 mod L` |
| `d` | One of the three cusp sequences fixed by `H mod 3` |
| `psi` | A character modulo one of the fixed `D0=lambda^3*c0` |
| `kappa0` | Fixed-prime residues just derived |
| Full denominator `c=c0*r` | Varies explicitly in the reflection scale |
| `sigma_p,epsilon_p`, Gauss phases | May vary with moving primes; their contributions to the exterior scalar have modulus one |
| `B_(p,j)(x)` | Explicit local column factor, retaining its zero and collision behavior |

The indexing in `lem:reflection-uniformity` therefore needs only a
fixed finite index (one can use the fixed Fourier index and any fixed
normalization choices) and the active subset of `P_fix`. There is no
binary active/inactive choice for a prime of `k0`. Finite ray-class
splitting does not convert a growing frozen good prime into part of
`S`. Such a prime stays in its explicit local factor and in `r_fix`.

## 7. Verification and remaining imports

The previous
[upstream review](../../../../quasi-rh/quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md)
was read for scope and comparison. Its
[exact checker](../../../../quasi-rh/quasi-rh-character-amplification/numerics/check_upstream_reflection_interfaces.py)
was replayed without modifying it, writing the temporary result to
`/private/tmp/arithmetic-source-audit-20261012/cusp-interface-replay.json`.
It passed 69,881 assertions. Relevant coverage includes the actual
Eisenstein CRT construction with `L=18`, all 324 fixed frequencies,
three ramified branches, nonunit fixed frequencies, and additive CRT
orientation. The finite local Fourier and reflection checks also pass.

The checker does **not** evaluate the global cubic multiplier formulas
for arbitrary composite entries, prove the supplementary reciprocity
laws, or construct the theta function. Sections 3–4 above supply the
general algebraic derivations under those imported laws; the finite
assertion count is supplementary evidence, not their substitute.

The remaining deep input is the cubic theta automorphy/coefficient
theorem and the classical reciprocity laws. This audit checks their
use and the source's extension to fixed ray factors with nonunit
Fourier frequencies. It does not use the unit-Fourier-support
Corollary 5.1 of Dunn–Radziwiłł outside its hypotheses. The full
reflection identity additionally needs the Mellin normalization,
continuation and kernel estimates, and `prop:R` further needs the
coefficient bounds and quadratic sieve. Those obligations remain
separate from the finite cusp-family conclusion established here.
