# Theta Mellin normalization and kernel audit

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. This is
an internal mathematical read-through, not independent specialist
validation or formal verification.

## Source, assumptions, and result

The audited source is [`paper2.tex` at openai/math commit
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
dated 5 October 2026, SHA-256
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Physical source lines 3284–3478 are the main target, with definitions at
1649–1881 and cusp coordinates at 3160–3176. All source line references
below use this exact version. The September 30
[upstream review](../../../../quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md#3-continuation-constants-and-uniform-kernel-constants-have-different-roles)
was read as context; its conclusion is not a premise of this derivation.

**Result:** the angular phases, Mellin powers, scalar `-i/81`, reflected
norm scale, contour argument, and uniform kernel seminorms agree with the
October 5 formulas. No defect was found in this part of the argument.
An explicit sufficient derivative order is
`J=ceil(4A)+j+4` for the displayed kernel seminorm. The continuation
argument is valid separately for each fixed arithmetic choice; it is not
the source of a uniform estimate as the twisting primes vary.

This conclusion assumes the source's theta coefficient formula,
automorphy at the selected cusps, cusp Fourier expansions, coefficient
support/bounds, and finite local transformation identities. Their
arithmetic/cusp audit is separate. This note does not establish those
inputs, the quadratic large sieve, the full completed mean square, or the
claimed zero-free theorem.

## 1. Derivative and angular factor

Write `q_l=N(ell)` and `q_c=N(c)`, so `q_c=|c|^2`. The Fourier phase is

\[
\breve e(\ell z)=e^{2\pi i(\ell z+\overline{\ell z})},
\qquad
\partial_{\bar z}\breve e(\ell z)=2\pi i\bar\ell\breve e(\ell z).
\]

The Bessel integral in `eq:bessel-mellin` (3321–3323) follows by setting
`mu=2s+1`, `nu=1/3`, and rescaling the variable in
[DLMF 10.43.19](https://dlmf.nist.gov/10.43.E19):

\[
\int_0^\infty v^{2s}K_{1/3}(4\pi|\ell|v)\,dv
=\frac{2^{2s-1}\Gamma(s+1/3)\Gamma(s+2/3)}
{(4\pi|\ell|)^{2s+1}}.
\]

Its integral actually converges for `Re(s)>-1/3`; the source's stated
`Re(s)>0` is a sufficient restriction. Multiplying by the Fourier
derivative gives exactly

\[
\frac{i}{4}(2\pi)^{-2s}\Gamma(s+1/3)\Gamma(s+2/3)
\overline{\alpha(\ell)}q_\ell^{-s}.
\]

Since `omega=exp(2*pi*i/3)`, `lambda=1+2*omega=i*sqrt(3)` and
`lambda^(-3)=i/(3*sqrt(3))`. Therefore, for
`ell=lambda^(-3)*n*b^3`,

\[
i\overline{\alpha(\ell)}q_\ell^{-s}
=27^s\overline{\alpha(n)}\overline{\alpha(b)}^{\,3}
N(n)^{-s}N(b)^{-3s}.
\]

The `i` is canceled by the conjugate angular factor of `lambda^(-3)`;
it must not be silently dropped before that substitution. For the
allowed primary columns with `(nb,S)=1` (hence `(nb,6)=1`), define the
**full** multiplier

\[
\phi_\Psi(x)=\phi(x)\prod_{p\in\mathcal P}\chi_p^{j_p}(x).
\]

Here the source's `phi` in lines 2906–2920 contains only the fixed
`Psi0`, while the product contains the moving local twists. The source
theta coefficient formula therefore gives
`c_theta(nb^3)*phi_Psi(nb^3)=3^(5/2)*|b|*gamma_2(n)*Psi(n)*Psi(b)^3`.
For `Psi=Psi_k`, this full multiplier is the source's `phi_k`.
Thus one obtains `eq:ray-mellin` (3339–3343):

\[
\mathcal J(s)=\frac{3^{5/2}}4
\left(\frac{27}{(2\pi)^2}\right)^s
\Gamma(s+1/3)\Gamma(s+2/3)\mathcal T(s,\Psi).
\]

Absolute termwise integration on `Re(s)>1` follows from the separate
squarefree and cube majorants
`sum_n N(n)^(-sigma)` and `sum_b N(b)^(1/2-3*sigma)`. No cancellation
of the cubic coefficients is needed for this exchange.

## 2. Cusp inversion and the conductor power

The source coordinates `eq:theta-cusp-coordinates` are

\[
z'=-\delta'/c-\frac{\bar z}{c^2(v^2+|z|^2)},\qquad
v'=\frac{v}{q_c(v^2+|z|^2)}.
\]

At `z=0`, Wirtinger differentiation gives
`partial_bar_z z'=-1/(c^2*v^2)`,
`partial_bar_z conjugate(z')=0`, and
`partial_bar_z v'=0`. Thus a translated horizontal derivative is
`-conjugate(kappa(g1))*c^(-2)*v^(-2)*partial_z'` of the selected cusp
function, evaluated at `z'=-delta'/c`, `v'=1/(q_c*v)`.
There is no additional height derivative of a cusp constant term.

For the Mellin measure the substitution `u=1/(q_c*v)` gives

\[
-c^{-2}\int_0^\infty f(1/(q_cv))v^{2s-3}\,dv
=-c^{-2}q_c^{2-2s}\int_0^\infty f(u)u^{1-2s}\,du
=-\overline{\alpha(c)}^{\,2}q_c^{1-2s}
\mathcal J^\vee(1-s).
\]

This independently produces the phase and norm power in
`eq:theta-mellin-functional-equation` (3382–3385). Differentiating the
cusp Fourier expansion in `z`, rather than `bar(z)`, now supplies
`alpha(ell)`:

\[
\mathcal J^\vee(s)=
\frac{i\Gamma(s+1/3)\Gamma(s+2/3)}{4(2\pi)^{2s}}
\sum_{\ell\ne0}d(\ell)\alpha(\ell)q_\ell^{-s}
\breve e(-\delta'\ell/c).
\]

Combining these equations with Mellin inversion of the original test
gives, before local regrouping, the scalar and scale factor

\[
-i\,3^{-5/2}27^{-s}(2\pi)^{4s-2}
\overline{\alpha(c)}^{\,2}q_c^{1-2s}
q_\ell^{s-1}X^{s-1/2}.
\]

Set `s=1/2-t`. This becomes

\[
-\frac{i}{81}\overline{\alpha(c)}^{\,2}q_\ell^{-1/2}
\left(\frac{(2\pi)^4}{27}\frac{q_\ell X}{q_c^2}\right)^{-t}.
\]

In particular the denominator in the kernel is **`N(c)^2=|c|^4`**,
not `N(c)`. The gamma factor becomes precisely

\[
R(t)=\frac{\Gamma(7/6+t)\Gamma(5/6+t)}
{\Gamma(7/6-t)\Gamma(5/6-t)}.
\]

After the finite local summation, the remaining scalar in source
3420–3424 is `-i/81` times the phase just found,
`hat(phi)(h0)*conjugate(kappa0)`, the inactive factors
`1-1/N(p)`, and unit-modulus active local factors. Assuming those local
identities, `|C|<=1/81` follows with no factor increasing with an active
prime norm. This bound is separate from the number of resulting terms.

## 3. Entireness and a complete strip-contour justification

Let `f(v)=partial_bar_z Theta_Psi(0,v)` and fix the finite arithmetic
choice `Psi` for this paragraph. The original nonzero Fourier series
gives exponential decay as `v` tends to infinity. There are finitely
many translated cusps. At each, the coordinate calculation above
removes the constant Fourier mode and replaces height by `1/(q_c*v)`.
The discrete dual lattice has `|ell|>=1/9`, because
`ell` belongs to `lambda^(-4)*O` and is nonzero. The coefficient bounds
then give exponential decay in `1/v`, times a fixed power of `v`, at
zero. Thus, for some positive `a,b` and finite `M,C` depending on this
arithmetic choice, bounds of the following form suffice:

\[
|f(v)|\le C v^M e^{-av}\quad(v\ge1),\qquad
|f(v)|\le C v^{-M}e^{-b/v}\quad(0<v\le1).
\]

These bounds and their logarithmic multiples justify locally uniform
Mellin integration for every complex `s`; hence `J(s)` is entire.
Dividing by the two gamma factors multiplies by entire reciprocal gamma
functions, so `Tcal(s,Psi)` is entire too. No pole or residue from a
principal cusp constant remains. For each individual translated term,
the same inversion also supplies convergence at both ends for its dual
cusp Mellin integral.

The dual series is absolutely convergent on `Re(s)>1`: using the
source's support `ell=u*lambda^m*n*b^3` and bound
`|d(ell)|<=27*3^(m/6)*|b|`, it is bounded by a constant times

\[
\sum_{m\ge-4}3^{m(1/6-\sigma)}
\sum_{n\ {\rm squarefree}}N(n)^{-\sigma}
\sum_bN(b)^{1/2-3\sigma},\qquad \sigma>1.
\]

For clarity, the compressed Phragmen–Lindelof step at source 3395–3408
can be justified without assuming a prime-uniform strip bound. Choose
fixed edges `a<0` and `b>1`. On the right edge the original Dirichlet
series is bounded. On the left edge the functional equation, absolutely
convergent dual series and gamma comparison give polynomial growth of
degree at most `2-4a` in the imaginary part. On the whole closed strip,
the integral for `J(s)` is bounded in the imaginary direction, and the
reciprocal gamma factors give a crude bound

\[
|\mathcal T(\sigma+i\tau,\Psi)|
\le C_{a,b,\Psi}(1+|\tau|)^B e^{\pi|\tau|}.
\]

Choose an integer `K` larger than both edge polynomial degrees and a
real `B0` with `s+B0` having no zero in the strip. Apply the maximum
modulus principle on rectangles to
`Tcal(s,Psi)*(s+B0)^(-K)*exp(epsilon*s^2)`.
The horizontal edges vanish as their height tends to infinity, since
`exp(-epsilon*tau^2)` dominates the crude exponential bound. The vertical
edges are bounded. Sending `epsilon` to zero afterward produces a
polynomial bound throughout this fixed strip. This supplies the source's
contour shift; its constants may depend on the current twisting primes.

The rapid vertical decay of the Mellin transform of a fixed smooth
compactly supported test then allows the `s`-contour to move to any
chosen `a<0`; no poles are crossed. On the corresponding
`Re(t)=1/2-a>1/2` line, summation over the dual coefficients and
integration can be interchanged absolutely.

There is a useful order-of-operations condition here. Shift the kernel
contour **for each dual coefficient** and then use its rapid large-
argument bound to sum. One must not interchange the unweighted dual
series with the integral on `Re(t)=0` merely because that integral
converges for each coefficient. Taking any decay order `A>1/2` gives
the convergent majorant `sum |d(ell)|*q_l^(-1/2-A)` at large `q_l`.
There are only finitely many smaller lattice indices for any fixed
`X,c`. Thus the source's instruction to shift each kernel and then
form the reflected sum is justified.

## 4. Uniform kernel bounds and finite derivative order

The numerator poles of `R(t)` occur at `-5/6-n` and `-7/6-n`;
reciprocal denominator factors are entire. Therefore the entire closed
strip `-1/4<=Re(t)<=A`, for fixed `A>0`, contains no pole. Gamma
asymptotics, as in [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9), give

\[
|R(\sigma+iu)|\ll_A(1+|u|)^{4\sigma},
\qquad -1/4\le\sigma\le A.
\]

The two exponential gamma factors cancel in the quotient. In particular
`|R(iu)|=1`, since each denominator factor is the conjugate of its
numerator factor on that line. Compact imaginary intervals are harmless
even where a denominator gamma function has a pole: its reciprocal
has a zero there.

Shifting to `Re(t)=-1/4` for `x<=1`, or to `Re(t)=A` for `x>=1`,
gives `x^(1/4)` or `x^(-A)`. Applying `(x*d/dx)^j` only inserts
`(-t)^j`. Consequently the kernel is bounded by the source seminorm
at `eq:ray-kernel` (3460–3467), with weight exponent
`K=ceil(4A)+j+2` on the Mellin variable. In logarithmic coordinates,
`J` integrations by parts give uniformly for `-A<=eta<=1/4`

\[
|\widehat V_*(\eta+iu)|
\ll_{I,A,J}\|V_*\|_{C^J(I)}(1+|u|)^{-J}.
\]

Taking `J=K+2=ceil(4A)+j+4` makes the weighted integral absolutely
convergent. This proves the stated finite-derivative bound, with
constants depending only on `A,j,I` and fixed archimedean normalizations.
Multiplication `V_*(y)=sqrt(y)*W(y)` costs no additional derivative
order on a fixed interval bounded away from zero.

The dependence contract is therefore:

| Quantity | Permitted dependence | Use |
| --- | --- | --- |
| Endpoint decay and strip-continuation constants | Entire fixed twist, including its finite moving-prime set | Establish an exact reflection identity for that twist |
| Kernel gamma quotient and derivative order | `A,j` and fixed archimedean data; interval affects only norm-comparison constants | Uniform bound after reflection |
| Arithmetic scalar | Explicit local factors, bounded by `1/81` | Uniform amplitude per transformed term |
| Scale | `N(ell)*X/N(c)^2` | Retains moving-prime norm dependence explicitly |
| Cusp coefficient/additive-character choice | The separately required fixed-ray uniformity lemma | Makes coefficients independent of a moving row after finite class partition |

The last item is not proved by Mellin continuation. The dependency on
fixed ray classes and the arithmetic local factors must be checked in
the separate cusp audit; an archimedean estimate cannot repair a defect
there. Conversely, nonuniform constants used only to establish the
exact identity are not silently being used as a uniform power saving.

## Decision

This scoped audit finds no Mellin normalization, contour, or
prime-uniform kernel obstruction. It expands two compressed parts of
the October 5 presentation: the strip maximum-modulus argument and the
order of summing after individual kernel shifts. They close under the
stated cusp inputs. The remaining source-audit obligation is to verify
those arithmetic/cusp inputs and their uniformity, then the quantitative
composition with the quadratic sieve; this note does not validate the
complete reflection theorem or the global quasi-RH argument by itself.
