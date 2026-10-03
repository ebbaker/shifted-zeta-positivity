# All-window scaling and finite-place relative compactness audit

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), separate same-model subagent audit; the exact serving
variant and configured reasoning effort are not exposed and are not inferred.
This is internal mathematical review, not independent specialist refereeing.
The analytic results below do not assume RH. Any decimal evaluations quoted
without an outward record are diagnostics, not certificates.

This audit checks the [session handoff](../notes/NEXT_SESSION_ALL_WINDOW_HANDOFF_20261003.md),
the [local certificate proof](../notes/LOCAL_COERCIVITY_LOW_BAND_20261003.md),
the [finite Euler identity](../notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md),
and the [closed-source analysis](../notes/CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md).
It finds no missing dilation factor in the proposed general formulas. It also
removes one qualitative obstacle from the strategy: the **relative** correction
is compact for every fixed finite prime set, even without proving that the
unweighted correction kernel is locally square integrable.

## 1. General window and the complete arithmetic multiplier

Let `I_L=(-L/2,L/2)` and set `f(y)=sqrt(L) F(Ly)` on `I_1`. This is a
unitary dilation and

\[
\widehat F(t)=\sqrt L\int_{I_1}f(y)e^{-iLty}\,dy.
\]

The source subspace `E_L` is the orthogonal complement of
`1, exp(Ly/2), exp(-Ly/2)`. It contains both parity sectors and is a complex
Hilbert space. For each active prime power `a=m log p<L`, write
`c_a=2(log p)p^{-m/2}`. Then

\[
q_L(t)=\gamma(t)-\sum_{a<L}c_a\cos(at),\qquad
\gamma(t)=\Re\psi(1/4+it/2)-\log\pi.
\tag{1}
\]

Prime powers at `a=L` contribute zero because a source and its translate
have disjoint supports up to a null set. Thus either strict or non-strict
event enumeration is acceptable only if this endpoint fact is kept explicit.
At `L=6/5` the complete active list is `2,3`; `4` is inactive.

Put `C_L=sum c_a`. A sufficient frequency cutoff is
`gamma(T)>=lambda+C_L`, since gamma is increasing on the positive axis.
This cutoff belongs to the sufficient estimate; it is not a necessary
frequency scale for the true source form.

## 2. Exact moment projection after dilation

Define

\[
\beta=L/2,\quad z=L/4,\quad m=\sinh(z)/z,
\quad n_s=\sinh(L/2)/L-1/2,
\quad n_c=\sinh(L/2)/L+1/2-m^2.
\]

An orthonormal constraint family is

\[
u_0=1,\qquad u_s(y)=\frac{\sinh(\beta y)}{\sqrt{n_s}},
\qquad u_c(y)=\frac{\cosh(\beta y)-m}{\sqrt{n_c}}.
\tag{2}
\]

For `L>0` both squared norms are strictly positive. Small `L` causes
numerical cancellation in these displayed formulas, but does not alter
their analytic meaning. At the present anchor no limiting expansion is
needed if outward arithmetic proves their positivity.

With `ell_n(y)=sqrt(2n+1)P_n(2y)`, the nonzero moment coefficients are

\[
(u_s)_n=\frac{\sqrt{2n+1}\,i_n(z)}{\sqrt{n_s}}
\quad(n\text{ odd}),\qquad
(u_c)_n=\frac{\sqrt{2n+1}\,i_n(z)}{\sqrt{n_c}}
\quad(n\ge2\text{ even}).
\tag{3}
\]

For `k=Lt` put `s=sin(k/2)/(k/2)` and

\[
b_s=\frac{2[\beta\cosh(\beta/2)\sin(k/2)
                  -k\sinh(\beta/2)\cos(k/2)]}{\beta^2+k^2},
\]
\[
b_c=\frac{2[\beta\sinh(\beta/2)\cos(k/2)
                  +k\cosh(\beta/2)\sin(k/2)]}{\beta^2+k^2}.
\tag{4}
\]

Let `p_n=(-1)^floor(n/2) sqrt(2n+1) j_n(k/2)`, stripping the common
factor `i` from the odd coordinates. The real parity coordinates of
`v_t=P_E exp(iLty)` are

\[
v_0=0,\qquad
v_n=p_n-(u_s)_n b_s/\sqrt{n_s}
          -(u_c)_n(b_c-ms)/\sqrt{n_c}\quad(n\ge1).
\tag{5}
\]

This projects out the full analytic constraint vectors before coordinate
truncation. Replacing them by finite approximations and then inverting
their Gram matrix would describe a different projection unless its error
were separately controlled.

## 3. Positive-part majorant and all omitted source modes

For `w=(lambda-q_L)_+` supported in `[-T,T]`, the capped source operator is

\[
D_L=\frac L\pi\int_0^T w(t)\,\Re|v_t\rangle\langle v_t|\,dt,
\qquad Q\ge\lambda I-D_L.
\tag{6}
\]

The factor `L` is essential. The real part denotes the real-coordinate
matrix; integration over the negative half-band eliminates cross-parity
entries, and the resulting operator represents the Hermitian form on
complex sources as well.

Let `h=T/N`, `W=integral_0^T w`, `W_mid=h sum w(t_i)` and

\[
V_1=\gamma(T)-\gamma(0)+T\sum_{a<L}c_a a.
\]

Since `||v_t||<=1` and `||v'_t||<=L/sqrt(12)`, one has

\[
|W-W_{\rm mid}|\le hV_1/2,\qquad
\|D_L-D_{L,\rm mid}\|
\le\frac{Lh}{2\pi}\left(V_1+\frac{LW}{\sqrt3}\right).
\tag{7}
\]

For an even rank `M`, define

\[
\tau_M(z)^2=
\frac{(2M+1)z^{2M}}{((2M+1)!!)^2}
\left(1-\frac{z^2}{(2M+1)(2M+3)}\right)^{-1}.
\tag{8}
\]

The ratio in parentheses must be strictly positive. The omitted projected
plane-wave norm is bounded uniformly for `0<=t<=T` by

\[
\delta_M=\tau_M(LT/2)
+e^{L/4}\tau_M(L/4)(n_s^{-1/2}+n_c^{-1/2}).
\tag{9}
\]

Indeed the real and imaginary Legendre tails obey the same Rodrigues
bound; the modified Bessel coefficient bound adds the factor `exp(L/4)`.
The normalized constraint pairings with a unit plane wave have absolute
value at most one. Therefore, if `D_{L,M}` compresses the midpoint matrix,

\[
\|D_{L,\rm mid}-D_{L,M}\|
\le\frac{2L\delta_M}{\pi}W_{\rm mid}.
\tag{10}
\]

One may instead truncate the exact integral and use `W`. These bounds
include the source complement and mixed entries, rather than just the
discarded diagonal block. Rank and cutoff must resolve `LT/2`, not `T/2`.

## 4. A signed low-band operator with a quadratic midpoint remainder

Positive-part capping discards useful positive energy before compression.
A direct alternative retains it on the whole certified band. Put
`r=lambda-q_L`, without taking its positive part, and define

\[
A_L=\frac L\pi\int_0^T r(t)\Re|v_t\rangle\langle v_t|\,dt.
\tag{11}
\]

If `q_L>=lambda` outside the band, then still

\[
Q\ge\lambda I-A_L.
\tag{12}
\]

Unlike the capped integrand, this integrand is smooth. Set

\[
W_{\rm abs}=\int_0^T|r(t)|dt,\qquad
V_2=15\sqrt3/2+T\sum_{a<L}c_a a^2.
\]

The digamma expansion has `a_n=2n+1/2` and
`gamma_n'(t)=4a_n t/(a_n^2+t^2)^2`. Its maximum is
`9/(4sqrt(3)a_n^2)`, attained at `t=a_n/sqrt(3)`. Consequently

\[
\int_0^T|\gamma''(t)|dt
\le\frac9{2\sqrt3}\sum_{n\ge0}a_n^{-2}
\le\frac9{2\sqrt3}\left(4+\int_0^\infty
                 \frac{dx}{(2x+1/2)^2}\right)
=15\sqrt3/2.
\tag{13}
\]

Termwise differentiation on compact intervals and the integral bound
are justified by the convergent derivative series. Also
`integral |r'|<=V_1` and `integral |r''|<=V_2`.

For `B(t)=Re|v_t><v_t|`, contraction of the exact projection gives

\[
\|v_t''\|\le L^2/\sqrt{80},\quad
\|B'\|\le L/\sqrt3,\quad
\|B''\|\le L^2(1/\sqrt{20}+1/6).
\]

Thus

\[
\int_0^T\|(rB)''\|dt
\le V_2+\frac{2L}{\sqrt3}V_1
 +L^2(1/\sqrt{20}+1/6)W_{\rm abs}=:V_{\rm op,2}.
\tag{14}
\]

On each midpoint cell the second-order Peano kernel is `s^2/2` in the
left half and `(h-s)^2/2` in the right half. Its maximum is `h^2/8`, so

\[
\boxed{\|A_L-A_{L,\rm mid}\|
\le\frac{Lh^2}{8\pi}V_{\rm op,2}.}
\tag{15}
\]

This is a dimension-independent bound on the full source space. A scalar
absolute midpoint sum gives
`W_abs<=h sum |r(t_i)|+h V_1/2`. Formula (10) applies to the signed
matrix with `W_mid` replaced by `h sum |r(t_i)|`. A signed weight must
not be replaced by its positive part in building the matrix, while every
norm error must use absolute weights.

The finite matrix is tested by outward LDL of `mu I-A_{L,M}` in both
parities. Its complement contributes zero to the finite-rank operator,
so the full bound is `max(mu,0)+error`; choosing positive `mu` avoids
this extra notation. If `lambda-mu-error>=delta>0`, (12) proves an
all-source gap `delta`. Such a pass supports the value of preserving
positive energy; it does not by itself supply an all-window theorem.

## 5. Centered arithmetic is an exact null-form freedom

The continuous-prime identity in the strategy note is correct. There is
a useful explicit finite-window version. Define

\[
r_{\rm cont,L}(t)=2\int_0^L e^{u/2}\cos(tu)du
=\frac{e^{L/2}(\cos Lt+2t\sin Lt)-1}{t^2+1/4},
\qquad j(t)=\frac1{t^2+1/4}.
\tag{16}
\]

For any pole-neutral source supported in `I_L`,

\[
\int (j+r_{\rm cont,L})|\widehat F|^2\frac{dt}{2\pi}=0.
\tag{17}
\]

This is the kernel identity
`exp(-|u|/2)+exp(|u|/2)=2 cosh(u/2)` on the difference interval;
its quadratic form is
`2 Re(conj(integral e^(-x/2)F) integral e^(x/2)F)`.
Thus the centered multiplier `q_L+j+r_cont,L` represents the same
compressed source form as `q_L` exactly. It can change a pointwise
majorant, but cannot change the exact answer on the same source space.
Its high-frequency remainder is `O(e^(L/2)/|t|)` and does not remove the
large prime-amplitude cutoff by itself. A genuine global improvement
needs an estimate of signed discrepancy or positive energy retained
after compression.

## 6. Two-prime boundary gap and source correction norm

The original transport proves, for a finite prime set at exponent `1/2`,

\[
I-C_S^2=T_ST_S^*\ge g_S I,\qquad
g_S=\left[\prod_{p\in S}\frac{1-p^{-1/2}}{1+p^{-1/2}}\right]^2
                  \frac{57}{10^6}.
\tag{18}
\]

The inherited archimedean factor is a full-space prolate certificate;
transport uses the actual inverse compressed metric. In particular

\[
g_{\{2,3\}}=(17-12\sqrt2)(7-4\sqrt3)\frac{57}{10^6}.
\tag{19}
\]

The crossing factorization holds for every finite set and every `L`:

\[
P C_F^*C_F\chi=P C_F^*1_{I_L}C_F\chi,
\qquad\|P a_{F,e}(D)\chi\|_1\le\frac L2\|F\|_2^2.
\]

Combining it with
`||C_S(I-C_S^2)^(-1)T_S||<=sqrt((1-g_S)/g_S)` gives

\[
|K_S[F]|\le k_{S,L}\|F\|_2^2,\qquad
k_{S,L}=L\sqrt{(1-g_S)/g_S}.
\tag{20}
\]

Ordinary floating evaluation gives `g_{2,3} approximately 1.2046947543e-7`
and `k_{2,3,6/5} approximately 3457.3449313`. These numbers recommend the
simple rational cap `3458`, subject to its outward scalar check. The
old cap `772` cannot be carried to the `{2,3}` representation.
Once an independent arithmetic gap `delta` is certified, the exact
conversion is `Q >= delta/(k+delta) B`. It proves no statement about
the positive spectral part of the unweighted correction operator.

## 7. Relative compactness for every fixed finite prime set

Here the dense two-prime resonance set is **not** an obstruction. The
following argument does not assert that the unweighted correction `K_S`
has a locally square-integrable kernel, and does not need that assertion.

Fix finite `S`, `L>0`, and any of the closed source spaces obtained by
imposing the displayed pole moments, with or without the mean condition.
The finite Euler identity is valid on all compact smooth sources, before
those restrictions. Its independent correction is a Hermitian quadratic
form. By (20) and complex polarization, it extends uniquely to a bounded
selfadjoint source operator `K_{S,L}` with norm at most `k_{S,L}`.

Let `S_map F=C_F Pi_S`, with domain those supported `L2` sources for
which this operator is Hilbert--Schmidt. This map is closed: convergence
of sources in `L2(I_L)` gives operator-norm convergence of convolutions,
since `||C_F||<=||F||_1<=sqrt(L)||F||_2`; a simultaneous Hilbert--Schmidt
limit must therefore be `C_F Pi_S`. Its squared Hilbert--Schmidt norm is
a densely defined closed positive form `b`.

For fixed finite `S`, the full prime series is uniformly bounded. Hence
the fixed-set bulk symbol satisfies, for finite constants `M_0,M_1`,

\[
\log(2+|t|)-M_0\le q_S(t),\qquad
|q_S(t)|\le M_1\log(2+|t|).
\tag{21}
\]

The closed-form domain is exactly

\[
\mathcal V_L=\left\{F\in\mathcal H_L:
\int\log(2+|t|)|\widehat F(t)|^2\frac{dt}{2\pi}<\infty\right\}.
\tag{22}
\]

For completeness, use a nonnegative compact smooth approximate identity
`rho_epsilon`. All mollified sources lie in one slightly larger interval.
On that larger interval the same fixed-`S` identity and bound (20) hold,
regardless of whether `S` captures every newly active prime. If `C_F Pi_S`
is Hilbert--Schmidt, then
`C_(rho_epsilon*F) Pi_S=C_rho_epsilon C_F Pi_S` converges in that norm.
The lower bound in (21), the uniform bounded correction, and Fatou prove
membership in (22). Conversely, convergence of mollifications in the
logarithmic norm and the smooth identity make these operators Cauchy
in Hilbert--Schmidt norm. Closedness identifies the limit. This proves
the domain equality and the identity

\[
b[F]=\int q_S(t)|\widehat F(t)|^2\frac{dt}{2\pi}
                   +\langle F,K_{S,L}F\rangle.
\tag{23}
\]

There is also an explicit smooth moment-neutral core on the original
open interval. First dilate a supported source inward by factors tending
to one. Dilation is strongly continuous in the weighted Fourier norm,
because `log(2+|t|/r)` is uniformly comparable to `log(2+|t|)` for `r`
near one. Mollify inside the resulting support margin. Finally correct
the finitely many moment errors using fixed compact smooth interior
functions whose moment matrix is invertible. Those coefficients tend to
zero by `L2` continuity of the moments, and the correcting functions have
finite logarithmic norm. This proves density in (22), including exact
complex moment neutrality, without a hidden support-enlargement step in
the final core.

The embedding of (22) into `L2(I_L)` is compact: low-frequency restriction
followed by spatial restriction is compact, while the Fourier tail is
bounded by the logarithmic energy divided by `log(2+R)`. Equations
(20)--(23) transfer this compactness to the `b+L2` form norm. Thus the
associated positive selfadjoint source operator `B_{S,L}` has compact
resolvent.

It has no zero eigenvector. A nonzero compactly supported source has a
nonzero entire Fourier transform, nonvanishing almost everywhere on the
real axis. Its convolution operator is injective. The nonzero Sonin
space is preserved under the established bounded invertible finite-place
transport, so `C_F Pi_S` cannot vanish. Compact resolvent and nonnegativity
then give a strictly positive, initially nonnumerical gap `beta_{S,L}`.

Therefore

\[
\boxed{H_{S,L}=B_{S,L}^{-1/2}K_{S,L}B_{S,L}^{-1/2}
\text{ is compact and selfadjoint for every fixed finite }S,L.}
\tag{24}
\]

Indeed `B^(-1/2)` is compact and `K` is bounded. No compactness theorem
for the unweighted `K` is used. This strengthens the qualitative scope
of the earlier one-prime reduction. It does **not** establish a numerical
lower bound for `beta`, effective eigenvalue tails, or any uniformity as
`L` and `S` grow.

For example, if `E` is an actual spectral projection of `B` and its
complement has `B>=Lambda I`, then

\[
\|H_{11}\|\le k/\Lambda,\qquad
\|H_{01}\|\le k/\sqrt{\beta\Lambda}.
\tag{25}
\]

These inequalities identify useful missing quantitative inputs. Using
them requires certified control of that spectral split and the finite
block; merely knowing that some such split exists proves no sign.

## 8. Remaining all-window obligation

The required quantifier is positivity on an unbounded sequence of nested
support windows with the same three moments. In the signed arithmetic
route, one needs a theorem ensuring valid parameters and

\[
\lambda_j-\mu_j-\epsilon_j\ge0
\]

for every member of such a sequence, where `mu_j` controls the compressed
signed band and `epsilon_j` contains the complete source and integration
remainders. In the relative route, one needs effective finite-block,
complement, and mixed-block estimates proving `H_{S_j,L_j}<=I` for every
member. Compactness (24) justifies a finite spectral reduction at each
fixed window; it does not supply the required inequality or its uniform
construction.

The full prime-amplitude cutoff, rank scale `LT`, and transported gap
still deteriorate as the support grows. A finite pass should be described
as a test of the signed-energy mechanism. It cannot justify an unlimited
sweep, a nonaccumulating continuation, place monotonicity, or an RH claim.
