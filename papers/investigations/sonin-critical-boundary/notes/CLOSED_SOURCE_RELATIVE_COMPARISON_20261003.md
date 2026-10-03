# Closed source form, compact relative correction, and a finite comparison certificate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), separate same-model subagent derivation; exact serving
variant and configured effort are not exposed and are not inferred.
This is internal analytic research, not independent human specialist
refereeing. The closed-form and compactness statements below are proved;
the finite spectral comparison tests identify obligations. The companion
local arithmetic certificate supplies the delta used in Section 9. No RH
assumption is used.

## 1. Source space and the fixed first-prime identity

Fix `I=(-L/2,L/2)`, with `log 2<L<log 3`, and the prime set `{2}` at
exponent `1/2`. The eventual numerical target is `L=1`. All source functions
are extended by zero outside `I`. Let

\[
\mathcal H_0=\{F\in L^2(I):\ \int_I e^{x/2}F(x)\,dx
=\int_I e^{-x/2}F(x)\,dx=0\}.
\]

One may instead use the closed subspace `H_1` obtained by imposing
`integral F=0` as well. These are kernels of bounded linear functionals on
`L2(I)`, hence closed. Write `H` for either choice.

On compact smooth sources, the two exponential moment conditions are
exactly the range of the preparation operator
`A_prep=-d^2/dx^2+1/4` without enlarging support. Indeed the Green solution

\[
h(x)=\int_{\mathbb R}e^{-|x-y|/2}F(y)\,dy
\]

vanishes outside the convex hull of the support when the two moments
vanish, and satisfies `A_prep h=F`. It is smooth when `F` is smooth.
Integrating that equation also gives `integral h=4 integral F`.
Compact smooth moment-neutral functions are dense in the indicated closed
moment kernels: approximate in `L2`, then correct the finitely many small
moment errors using a fixed finite smooth family with invertible moment
matrix. Thus no unproved closure statement about the pre-preparation
profile variable is needed.

The [finite Euler identity](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md) gives
on these sources

\[
Q[F]=B[F]-K[F],\qquad
B[F]=\|C_F\Pi\|_{\rm HS}^2,
\]

where `Pi` is the actual first-prime Sonin projection. For the fixed prime
set, the bulk has the explicit multiplier

\[
q(t)=\gamma_\infty(t)
 -2\sum_{m\ge1}(\log2)2^{-m/2}\cos(mt\log2),
\quad
\gamma_\infty(t)=\Re\psi(1/4+it/2)-\log\pi.
\tag{1}
\]

The series in (1) is uniformly absolutely convergent. Since all active
primes are captured at the stated support, this bulk is the complete
pole-neutral arithmetic form. For the analytic domain arguments below,
the fixed-prime identity can also be used on slightly larger intermediate
supports without asserting active-prime capture there.

## 2. An explicit nuclear source bound without source derivatives

Let `P=1_(0,infinity)` and `chi=1_(-infinity,0)` in logarithmic coordinates,
and let `J_I` denote multiplication by `1_I` on the intermediate
convolution variable. Initially use the noneven multiplier
`a_F=|Fhat|^2`. The crossing operator factors exactly as

\[
P C_F^*C_F\chi=P C_F^*J_I C_F\chi.
\tag{2}
\]

To verify the support assertion, its kernel integrates
`conj(F(z-x)) F(z-y)` with `x>0>y`. The first factor forces `z>-L/2`,
and the second forces `z<L/2`. The inserted cutoff therefore changes
nothing. This verification also fixes the conjugation orientation.

Both factors on the right of (2) are Hilbert--Schmidt, with squared norms

\[
a=\int_I (L/2-v)|F(v)|^2\,dv,\qquad
b=\int_I (L/2+v)|F(v)|^2\,dv.
\]

Hilbert--Schmidt multiplication and `a+b=L||F||_2^2` give

\[
\|P C_F^*C_F\chi\|_1\le\sqrt{ab}
\le\frac L2\|F\|_2^2.
\tag{3}
\]

For the even multiplier `a_e(t)=(a_F(t)+a_F(-t))/2`, reflect the source.
Reflection swaps `a,b` and preserves their product, so the same bound holds
for `X=P a_e(D)chi`, including complex sources.

Let `A_boundary=I-C^2=TT*>=gI` and `||C||<=c<1`. The audited resolvent
identity gives `||C A_boundary^(-1)T||<=c/sqrt(g)`. Consequently

\[
\boxed{|K[F]|\le k_L\|F\|_2^2,\qquad k_L=\frac{Lc}{\sqrt g}.}
\tag{4}
\]

This is a source-form norm bound, not a truncation error or sign assertion.
It needs no derivatives or Legendre tail constants.

At `L=1`, the inherited gap permits

\[
g=(17-12\sqrt2)\frac{57}{10^6},\qquad c=\sqrt{1-g}.
\]

An outward Arb calculation at 192 bits gives
`c/sqrt(g)=771.9933840785181666843310059416792133843429379831613819`
with radius below `5.2e-53`; in particular the convenient rational bound

\[
\boxed{|K[F]|\le772\|F\|_2^2}
\tag{5}
\]

is valid conditional only on the already certified inherited gap. The
calculation uses `python-flint 0.9.0`; it does not evaluate a correction sign.

## 3. The compact source correction

The [translated resonance analysis](FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md)
represents the correction by a real even difference kernel `k`:

\[
K[F]=\int\kappa_F(u)k(u)\,du.
\]

On every bounded difference interval, its first-return part has only
finitely many logarithmic singularities. Its higher-return part is
continuous because `C^3(I-C^2)^(-1)T` is trace class. Thus
`k in L2(-L,L)`, and

\[
(K_I F)(x)=\int_I k(y-x)F(y)\,dy
\]

is a bounded selfadjoint Hilbert--Schmidt operator. In fact

\[
\|K_I\|_{\rm HS}^2
=\int_{-L}^L(L-|u|)|k(u)|^2\,du<\infty.
\tag{6}
\]

Compress this operator to `H`, writing `K_H`. It still represents the
correction there and remains compact. Equation (4) supplies the explicit
operator norm estimate `||K_H||<=k_L` without requiring numerical
integration of the logarithmic kernel. Compactness concerns the source
`F`, not the unbounded preparation map acting on `h`.

## 4. Closed positive realization of B and its precise domain

On `H`, define the densely defined linear map

\[
\mathcal S F=C_F\Pi,
\qquad
\mathcal D(\mathcal S)=\{F\in H:C_F\Pi\in\mathfrak S_2\}.
\]

It is closed. Indeed `F_n->F` in `L2(I)` gives

\[
\|C_{F_n}-C_F\|\le\|F_n-F\|_1
\le\sqrt L\|F_n-F\|_2.
\]

If simultaneously `S F_n` converges in Hilbert--Schmidt norm, its operator
norm limit must therefore be `C_F Pi`. The graph is closed. Compact smooth
neutral sources belong to its domain by the existing smoothing lemma and
are dense. Hence

\[
b[F]=\|\mathcal SF\|_{\rm HS}^2
\]

is a densely defined closed nonnegative quadratic form, with an associated
nonnegative selfadjoint source operator `B_H`.

Its domain is exactly the logarithmic form domain

\[
\mathcal V=\left\{F\in H:
\int_{\mathbb R}\log(2+|t|)|\widehat F(t)|^2\frac{dt}{2\pi}<\infty
\right\}.
\tag{7}
\]

Here is a way to prove this without presuming the smooth prepared core is
a core for the unknown closed form. Use a nonnegative compact smooth
approximate identity `rho_epsilon`, and put `F_epsilon=rho_epsilon*F`.
All these sources lie in one slightly larger fixed interval. Their
convolutions obey

\[
C_{F_\epsilon}\Pi=C_{\rho_\epsilon}C_F\Pi,
\qquad \|C_{\rho_\epsilon}\|\le1.
\]

If `F` belongs to `D(S)`, strong convergence of the uniformly bounded
left factors gives Hilbert--Schmidt convergence to `C_F Pi`. The smooth
identity applies to `F_epsilon`. The digamma asymptotic and bounded prime
series give constants `M_0,M_1` such that

\[
\log(2+|t|)-M_0\le q(t),\qquad
|q(t)|\le M_1\log(2+|t|).
\tag{8}
\]

The correction on the slightly larger interval is bounded by (4). The
smooth identity and (8) therefore give a uniform bound for the logarithmic
norm of `F_epsilon`. Fatou's lemma implies `F in V`.

Conversely, if `F in V`, its mollifications converge in the logarithmic
norm by dominated convergence. Applying the smooth identity to
`F_epsilon-F_delta`, with (8) and the bounded correction, makes
`C_(F_epsilon) Pi` Cauchy in Hilbert--Schmidt norm. Its operator norm limit
is `C_F Pi`, proving `F in D(S)`. Passing to the limit also proves

\[
b[F]=\int q(t)|\widehat F(t)|^2\frac{dt}{2\pi}
       +\langle F,K_HF\rangle,
\qquad F\in\mathcal V.
\tag{9}
\]

The intermediate mollifications need not stay inside the original interval;
the identity and bound are used in the one fixed larger interval and then
restricted back. Thus no boundary cutoff or form-core assumption is hidden.

## 5. Compact resolvent and a positive, initially nonnumerical gap

From (8)--(9),

\[
b[F]\ge\int\log(2+|t|)|\widehat F(t)|^2\frac{dt}{2\pi}
 -(M_0+k_L)\|F\|_2^2.
\tag{10}
\]

The embedding of this logarithmic domain, with fixed spatial support, into
`L2(I)` is compact. For example the low-frequency restriction
`P_I 1_[-R,R](D) P_I` has a square-integrable kernel and is compact, while

\[
\|F-1_{[-R,R]}(D)F\|_2^2
\le\frac{1}{\log(2+R)}
\int\log(2+|t|)|\widehat F(t)|^2\frac{dt}{2\pi}.
\]

Restricting the left side back to `I` only decreases it. Uniform
approximation by these compact maps proves compactness of the embedding.
Equation (10) transfers this conclusion to the `b+L2` form norm. Thus
`B_H` has compact resolvent.

Moreover `b[F]>0` for every nonzero `F in V`. A nonzero compactly supported
`L2` source is also `L1`, and its Fourier transform is a nonzero entire
function. Its real zero set has measure zero. Consequently multiplication
by `Fhat`, and hence convolution by `F`, is injective on the ambient `L2`
space. Since `Pi` is nonzero, `C_F Pi` cannot vanish.

The nonzero Sonin-space fact does not need RH: use a smooth physical seed
supported in `(1,2)` and increasingly rapid modulations. Its cosine output
on `(0,1)` tends to zero. The already established archimedean gap shows
that its exact Sonin projection has norm tending to the nonzero seed norm.
The bounded invertible finite-prime transport then preserves nontriviality.

A nonnegative operator with compact resolvent has its spectral bottom as
an eigenvalue. Strict positivity excludes zero. Therefore

\[
\boxed{B_H\ge\beta_L I\quad\text{for some }\beta_L>0.}
\tag{11}
\]

This proves existence of a fixed-window source gap. It does not give a
certified numerical value of `beta_L`, nor any lower bound uniform in the
window or prime set.

## 6. Relative correction and a less conservative spectral split

By (11), the relative correction

\[
H_B=B_H^{-1/2}K_HB_H^{-1/2}
\tag{12}
\]

is bounded compact and selfadjoint. For every source in the form domain,

\[
Q[F]=\langle B_H^{1/2}F,(I-H_B)B_H^{1/2}F\rangle.
\tag{13}
\]

Since `B_H^(1/2)` maps its form domain onto `H`,

\[
Q\ge0\quad\Longleftrightarrow\quad H_B\le I.
\tag{14}
\]

The infinitely many positive correction directions produce infinitely
many positive relative eigenvalues tending to zero. They do not imply
that the largest relative eigenvalue exceeds one.

Write `H_B=(H_B)_+-(H_B)_-`. The exact modified form

\[
b_{\rm rel,new}[F]
=\langle B_H^{1/2}F,(I-(H_B)_+)B_H^{1/2}F\rangle
\]

satisfies

\[
Q[F]=b_{\rm rel,new}[F]
 +\langle B_H^{1/2}F,(H_B)_-B_H^{1/2}F\rangle.
\tag{15}
\]

Unlike subtracting the positive part of the unweighted source operator
`K_H`, positivity of this relative modified form is equivalent to `Q>=0`:
`(H_B)_+<=I` if and only if `H_B<=I`. It therefore avoids that extra
conservatism. It is a structural reduction to a compact comparison, not a
proof of the remaining eigenvalue inequality.

## 7. Full-space finite block and tail tests

Let `E` be an orthogonal finite-rank projection on `H`, and decompose
`H_B` into blocks `H_00,H_01,H_10,H_11` against `E` and `I-E`. Suppose a
rigorous full-complement estimate gives

\[
H_{11}\le\vartheta I,\qquad \vartheta<1.
\]

Then the block Schur complement gives the exact equivalence

\[
H_B\le I\quad\Longleftrightarrow\quad
I_E-H_{00}-H_{01}(I-H_{11})^{-1}H_{10}\ge0.
\tag{16}
\]

A sufficient, directly bounded finite test is

\[
I_E-H_{00}-\frac{H_{01}H_{10}}{1-\vartheta}\ge0.
\tag{17}
\]

The cross block cannot be dropped. Its Gram is

\[
H_{01}H_{10}=E H_B^2E-(E H_BE)^2,
\]

so the same distinction between compression of a square and square of a
compression appears here. A scalar cross bound `||H_01||<=b` permits the
weaker test `lambda_max(H_00)+b^2/(1-vartheta)<=1`.

If instead one has a full operator approximation `J_N=E J_NE` with
`||H_B-J_N||<=eta`, the simpler sufficient test is

\[
\max(0,\lambda_{\max}(J_N))+\eta\le1.
\tag{18}
\]

This full-norm estimate already covers the complement and mixed blocks;
there is no need to introduce a weaker Schur estimate in that case.
All numerical entries, function evaluations, source projections and
operator tails must be included in the quoted bounds.

## 8. A finite resolvent test for the conservative source allowance

The proposed source-space approximation offers a second concrete route.
Suppose a finite-rank selfadjoint `A_N` approximates `K_H` with error at most
`eta`, and write `(A_N)_+=W W*` with finitely many columns. Then

\[
K[F]\le\langle F,WW^*F\rangle+\eta\|F\|_2^2.
\]

If a numerical gap `beta_L>eta` is known, set `D=B_H-eta I`. Its lower
bound is `d_0=beta_L-eta>0`. The full comparison is equivalent to a finite
matrix inequality:

\[
B_H\ge WW^*+\eta I
\quad\Longleftrightarrow\quad W^*D^{-1}W\le I.
\tag{19}
\]

This follows by congruence with `D^(-1/2)`; it does not discard the
infinite source complement. For approximate solution columns `Y` in the
operator domain of `D`, let `R=W-DY`. The exact completion of the square is

\[
W^*D^{-1}W
= W^*Y+Y^*W-Y^*DY+R^*D^{-1}R.
\tag{20}
\]

Thus

\[
W^*D^{-1}W
\le W^*Y+Y^*W-Y^*DY+d_0^{-1}R^*R.
\tag{21}
\]

An outward upper enclosure of this finite matrix below the identity is a
complete sufficient certificate. The residual is the full source-space
residual, not only the tested rows. If only its Hilbert--Schmidt norm is
available, `R*R<=||R||_HS^2 I` gives a valid coarser substitute. This is a
legitimate finite-column completion of the square, without separately
tracing any unsmoothed half-line bulk.

A finite *state-space* Galerkin trace for B is not generally finite rank
as a *source* form. On a fixed source interval it is nevertheless trace
class: each map `F -> F*psi_j` has Hilbert--Schmidt norm squared
`L||psi_j||_2^2`, and the source form is a finite weighted sum of
`T_j* T_j`. Therefore such a trace alone cannot dominate `eta I` on the
whole infinite-dimensional source space. A genuine analytic lower bound
or resolvent argument remains necessary.

## 9. Conditional quantitative absorption from a local arithmetic gap

There is a simpler completed algebraic consequence if an independent
first-window calculation supplies an all-source coercive bound

\[
Q[F]\ge\delta\|F\|_2^2,\qquad\delta>0,
\tag{22}
\]

on the chosen prepared source space. This must be an all-source bound;
a value for one bump or a finite trial family is insufficient.
Together with `K[F]<=k||F||_2^2`, it gives

\[
B[F]=Q[F]+K[F]
\le Q[F]+k\|F\|_2^2
\le\left(1+\frac{k}{\delta}\right)Q[F].
\]

Put

\[
\boxed{\theta=\frac{\delta}{k+\delta},\qquad
B_{\rm new}=\theta B,\qquad R=(1-\theta)B.}
\tag{23}
\]

Then

\[
Q\ge\theta B,\qquad K\le(1-\theta)B,
\qquad
\boxed{Q=B_{\rm new}+(R-K),\quad B_{\rm new}\ge0,\ R-K\ge0.}
\tag{24}
\]

At `L=1`, the certified rational choice `k=772` may be used. No numerical
value of `delta` is asserted in this note. If an independently established
`delta` is supplied, (23)--(24) give an explicit revised positive main term
and a relative correction bound immediately. They accommodate the
infinite positive index because `R` is an energy allowance, not a finite
list of scalar moments.

This route reuses an arithmetic coercivity result to validate the revised
Sonin decomposition. It is useful local progress and an exact certificate
of accommodation, but it is not an independent derivation of arithmetic
positivity from Sonin geometry. Extending the argument to unbounded
support-adapted prime sets still requires a new all-window coercivity or
comparison mechanism.


## 10. Completed first-window corollary

The companion [local coercivity proof](LOCAL_COERCIVITY_LOW_BAND_20261003.md)
now certifies delta=9/100 on H_1 at L=1. Substitution in (23) gives

    theta=9/77209 > 1/9000.

Consequently Q>=B/9000 and K<=(8999/9000)B on the full smooth prepared
mean-zero source space in this window. The [certificate package](../numerics/local_weil_gap_20261003/README.md)
contains the outward arithmetic and a fresh replay of the inherited prolate gap.
This corollary does not assert the same constant on H_0 without zero mean,
and does not settle the conservative unweighted positive-part inequality.
