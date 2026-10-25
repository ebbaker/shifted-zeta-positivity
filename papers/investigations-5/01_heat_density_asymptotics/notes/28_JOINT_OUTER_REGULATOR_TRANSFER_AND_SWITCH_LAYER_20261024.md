# Uniform regulator transfer, a joint outer range, and the switch layer

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this conversation's session metadata. Chat 0006.

**Status: proved in-note; same-assistant review only.** This continues
HDA-19 from [Note 27][n27] with three quantitative gains:

- A comparison with the density of the explicit two-gamma field, using
  the unchanged regulator, uniform across its switch at t=64. On each
  compact interval `[32,T]`, its absolute error is O(log^2 X/X). The
  physical averaged potential and filtered w have the same spatial-jet
  error through order four.
- A joint range `32<=t<=(log X)/4`, with absolute error
  O(X^(-3/4)(1+log^4 X)); constants are independent of t in that range.
- A coarse description of the regulator transition, its center near
  `64+64/log X`, and its much smaller time width `1/(X log X)`.

Here `X=|x|` tends to infinity, spatial widths and the transverse strip
are fixed, and all buffers are paid. The approximation retains the fixed
spatial average of an explicit special-function field; it is not a new
finite elementary formula for that average. The simpler layer profile
has O(1) absolute error, or O(1/log X) error after dividing by log X.

There is still no overlap with the large-time inner window, no complete
positive current/potential/covariance comparison, no instantiated onset
and no independent review. The exact heat residual of the two-gamma
field is recorded rather than discarded. HDA-19 remains **Partial**.
No numerical or machine-symbolic execution was performed. See
[Review 11][review] and the [next-session continuation][continuation].

## 1. Objects, buffers and theorem

Keep the canonical H, `H_t=-H_zz`, `H(0,z)=xi((1+iz)/2)/8`, and the
unchanged positive regulator from [Note 20][n20]. Extend the notation

\[
\epsilon_g(t,u)=E_0(t)e^{-\beta(t)u^2/2},\quad
\beta(t)=0\ (t\le64),\qquad \beta(t)=\chi(t)/\kappa(t)\ (t>64),
\quad q=\epsilon_g^2,\quad r=\log q.
\tag{JT1}
\]

Thus E_0 is epsilon_b below the switch and the geometric interpolation
of epsilon_b and M_0/kappa above it. These functions are smooth across
64. The switch does not modify H or its heat equation.

Use fixed `ell,h>0`, `|y|<=Y`, and
`K(u,v)=k_ell(u)k_h(v)`, with the normalized degree-eight kernel of
Note 27. All estimates use `|Re z-X|<=ell+2`, `|Im z|<=Y+h+2`, plus
fixed smaller margins when taking collars. Enlarge this fixed margin
once if necessary; never discard the kernel boundary or a root disk
meeting its support. Constants depend on these widths, Y and fixed eta.
They do not depend on t or X in the stated joint range.

Retain Note 27's **exact** gamma factors

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha=(\log\mathcal M)',\quad
\mathcal G_t(w)=\mathcal M(w)e^{t\alpha(w)^2/4},
\quad s=(1+iz)/2,
\]
\[
P(t,z)=\mathcal G_t(s)+\mathcal G_t(1-s),\quad
D_t(w)=\alpha(w)+\tfrac t2\alpha(w)\alpha'(w),
\quad
P_z=\tfrac i2[\mathcal G_t(s)D_t(s)-\mathcal G_t(1-s)D_t(1-s)].
\tag{JT2}
\]

P is holomorphic on the far-height buffer; a global entire extension of
its separate meromorphic factors is not required. Define, for F=H or P,

\[
\rho_F=\frac{q|F_z|^2}{\pi(|F|^2+q)^2},\qquad
R_F=K*\rho_F,\quad S_F=\log(|F|^2+q),\quad
w_F=\frac q{|F|^2+q}.
\tag{JT3}
\]

**The same physical q is used for both fields.** There is no mass
normalization and no replacement of the adaptive density by a zero
measure in the transition layer.

**Joint static theorem.** There exist finite C and X_0 such that

\[
\boxed{\sup_{32\le t\le\frac14\log X,\ |y|\le Y}
 |R_H(t,X,y)-R_P(t,X,y)|
 \le C X^{-3/4}(1+\log^4X),\qquad X\ge X_0.}
\tag{JT4}
\]

Take X_0 large enough that this interval is nonempty. Separately, for
each fixed finite `T>=64`,

\[
\boxed{\sup_{32\le t\le T,\ |y|\le Y}|R_H-R_P|(t,X,y)
\le C_T\frac{1+\log^2X}{X},\qquad X\ge X_0(T).}
\tag{JT5}
\]

Evenness and conjugation give the same statements at negative heights.
Both estimates include t=64. They are static density comparisons;
time derivatives of these errors are not asserted.

The work is an approximation milestone under [avoid/01][a01]. Read the
[result index][results], [heat-flow cluster][geometry], [control
screen][controls] and [avoid index][avoid], especially [cancellation][a12]
and [scope][a07]. Section 8 records the control premises and limits.

## 2. A time-dependent field budget

Start with the exact all-positive-time convolution

\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}e^{-v^2/t}
\frac{\xi(s+v)}8\,dv,
\tag{JT6}
\]

as derived from the complete source in Note 27 and [Polymath (35)][poly].
No high-zero theorem with a different time range is imported.

Let `a=Re alpha(w)`, `b=Im alpha(w)` for w=s or 1-s. The same
sectorial estimates, now with constants independent of t, give on the
fixed buffer

\[
a=\tfrac12\log X+O_Y(1),\quad |b|\le2,\quad
\alpha'=O_Y(X^{-1}),\quad \alpha''=O_Y(X^{-2}).
\tag{JT7}
\]

Increase X_0 for the harmless bound 2. Holomorphic remainders on larger
sectors and Cauchy's formula justify the derivatives, as in Note 27 and
[DLMF 5.11][gamma]. Put `V=X^(1/3)`. For the bounded right-arm lower
endpoint v_0 and `v_0<=v<=V`,

\[
\mathcal M(w+v)=\mathcal M(w)e^{v\alpha(w)+E(w,v)},
\quad |E(w,v)|\le C_Yv^2/X,
\quad |e^{E(w,v)}-1|\le C_Yv^2/X.
\]

The absolute linear Gaussian, divided by the modulus of its exact
complex integral, costs `exp(tb^2/4)<=exp(t)`. Its second moment is
`t/2+t^2a^2/4`. Therefore the local gamma contribution is bounded by

\[
 C\,\frac{e^t(t+t^2\log^2X)}X.
\tag{JT8}
\]

This time dependence was hidden inside the compact-time constant of
Note 27; it is retained here. No oscillatory cancellation is claimed
in this absolute estimate.

All other pieces remain paid. Split the convolution at real parts 2
and -1, and reflect the left arm by xi(w)=xi(1-w). The arithmetic
remainder on either arm obeys `|zeta(w+v)-1|<=3*2^(-Re w-v)`.
Changing the Gaussian tilt from a to a-log 2 and using JT7 gives

\[
\exp\{-ta\log2/2+t((\log2)^2+b^2)/4\}
 \le X^{-t\log2/8}
\tag{JT9}
\]

for sufficiently large X, uniformly in t. The constant terms in the
exponent are absorbed by the difference between the coefficients
log(2)/4 and log(2)/8 of `t log X`, not by a t-dependent constant.

The bounded middle and the missing lower linearized Gaussian tail
have relative bound
`C X^(C_Y) exp(-t log^2 X/128)`. Indeed `a>=(log X)/4` eventually,
the middle xi value is at most `C X^4 exp(-pi X/8)` by Euler summation
[DLMF 25.2.8][zeta], and both pieces retain the gamma exponential.
The bounded lower endpoint contributes only a fixed power of X.

For the infinite positive tails use, for every v>=0,

\[
\log\frac{|\mathcal M(w+v)|}{|\mathcal M(w)|}
 \le C_Yv+\tfrac12v\log(X+v).
\]

On `t<=(log X)/4`, this is at most v^2/(2t) for every v>=V, once X
is large: `V/log^2 X` tends to infinity and the corresponding ray ratio
is increasing. The true and linearized far tails are consequently at
most `C exp(t-X^(2/3)/(16t))` relative to the carrier. The denominator
16 is a conservative common Gaussian-tail allowance.

Combining these bounds gives, uniformly on the full buffer in JT4,

\[
|H-P|\le C\mathcal E(t,X)
 (|\mathcal G_t(s)|+|\mathcal G_t(1-s)|),
\tag{JT10}
\]
\[
\mathcal E(t,X)=\frac{e^t(t+t^2\log^2X)}X
 +X^{-t\log2/8}
 +X^{C_Y}e^{-t\log^2X/128}
 +e^{t-X^{2/3}/(16t)}
 \le C X^{-3/4}(1+\log^4X).
\tag{JT11}
\]

Here `e^t<=X^(1/4)`; the other terms are smaller than X^-1 after an
onset independent of t>=32. For a fixed interval `[32,T]`, the first
term is instead O_T(log^2 X/X), giving the sharper compact-time field
rate. The floor 32 is a convenient conservative choice making the
arithmetic power harmless; it is not an onset for any zero theorem.
The field proof extends Note 27's time range by tracking its actual
estimates, not by changing the hypotheses of a cited theorem.

Let A and Theta be the analytic carrier and phase from Note 27,
`P=2 A cos Theta`, with A positive on the real axis, and put

\[
A_X=|\mathcal G_t((1+iX)/2)|,\quad
\theta=\Theta(t,X),\quad \omega=\partial_x\Theta(t,X).
\]

On the joint range,

\[
\omega=\tfrac14\log(X/(4\pi))+O(t\log X/X),\quad
\Theta_{zz}=O(X^{-1}),\quad
|(\log\mathcal A)_z|\le C.
\tag{JT12}
\]

The bound on the carrier derivative uses cancellation of the leading
logarithms, as in GO19. The terms involving t in these derivatives are
uniformly smaller than their displayed main bounds because
`t<=(log X)/4`. Thus A is comparable to A_X on the entire fixed buffer.

The Rouche/phase proof of GO20--GO22 now applies with error
`e=C E(t,X)`, tending uniformly to zero. P and H have exactly one real
simple zero in each relevant disjoint collar of radius c/omega; their
zeros are displaced by O(e/omega). Both physical fields have exterior
floor c A_X and interior slope floor c A_X omega. There are O(omega)
collars, including every collar meeting the averaging support. These
facts are inputs to the next step, not consequences of a regulator floor.

## 3. A local comparison uniform over every positive q

The following elementary lemma avoids dividing the field error by the
smallest regulator. Its hypotheses are stronger than a bare absolute
field bound: the complete simple-root collars and analytic units are
already controlled. It is not a multiple-event theorem.

On a phase-scaled collar use `u=omega(z-d)`, where d is its P zero, and
write

\[
P/\mathcal A=u B(u),\qquad
H/\mathcal A=(u-e_0)C(u),\quad |e_0|\le C e.
\tag{JT13}
\]

On a fixed-radius disk, B and C are holomorphic, bounded above and below
by positive constants, and `|B-C|<=C e`. To prove the last assertion,
compare `(H/A)/(u-e_0)` and `(P/A)/u` on the collar boundary, where the
field error and e_0 are O(e). Their difference extends holomorphically
through both removable points, so the maximum principle gives the bound
throughout the disk. No differentiation of a noisy root estimate enters.

For **any positive function Q(u)**, even one with large variation,

\[
\int_D\left|\log\frac{|(u-e_0)C(u)|^2+Q(u)}{|uB(u)|^2+Q(u)}\right|dA_u
 +\int_D\left|\frac{Q(u)}{|(u-e_0)C(u)|^2+Q(u)}
             -\frac{Q(u)}{|uB(u)|^2+Q(u)}\right|dA_u
 \le C e.
\tag{JT14}
\]

First replace C by B; relative unit error O(e) changes each integrand
by O(e), uniformly in Q. For the remaining translation put
`q_0(u)=Q(u)/|B(u)|^2`, and vary the root from 0 to e_0 while keeping
q_0(u) fixed. The absolute derivatives along this segment are bounded by

\[
\frac{2|e_0|}{|u-se_0|},\qquad
\frac{|e_0|}{2|u-se_0|},\qquad 0\le s\le1,
\tag{JT15}
\]

respectively. The second uses
`q_0 |u-se_0|/(|u-se_0|^2+q_0)^2<=1/(4|u-se_0|)`.
The planar function 1/|u-se_0| is uniformly integrable on the fixed
disk. Integrate first in u and then in s to prove JT14. Points on the
segment cause no problem for the area integral. There is no derivative
or lower bound of Q in this argument.

Apply it with `Q=q/|A|^2`, and restore the area factor omega^-2.
Outside the collars the relative field error is O(e), so both logarithm
and w differences are O(e) pointwise, uniformly in q. Summing O(omega)
collars gives the full-buffer bound

\[
\boxed{\|S_H-S_P\|_{L^1(\Omega)}+
\|w_H-w_P\|_{L^1(\Omega)}\le C e.}
\tag{JT16}
\]

No physical field normalization has been made: log|A|^2 cancels in the
logarithmic difference, and Q is exactly the same physical q divided by
the same nonzero factor on both sides. The arbitrary-Q lemma is derived
here. The sibling [C2 divisor note][sibling] concerns a different compact
regularization and supplies useful context, not this adaptive lemma.

For any holomorphic F, the weak identity from [Note 14][n14], VE15,
combined with the distributional identity for log|F|^2 is

\[
4\pi\langle\rho_F,\psi\rangle=
\int S_F\Delta\psi+2\int w_F\nabla r\cdot\nabla\psi
+\int\{w_F\Delta r+w_F(1-w_F)|\nabla r|^2\}\psi.
\tag{JT17}
\]

It does not require F to solve a heat equation. Subtract the H and P
identities, use `|a(1-a)-b(1-b)|<=|a-b|` for a,b in [0,1], and apply
JT16. For fixed translated kernels,

\[
|R_H-R_P|\le C e(1+B_1+B_2+B_1^2),\quad
B_1=\|\nabla r\|_\infty,\quad B_2=\|\Delta r\|_\infty.
\tag{JT18}
\]

Both adaptive corrections remain in the proof. This is a comparison of
two actual regularized densities, not a zero-measure approximation.


There is also a direct source-anchored potential corollary. Set
`U_F=K*S_F`, `W_F=K*w_F`. Every weak kernel derivative through total
order four is bounded: k is C3 with a bounded piecewise-polynomial
fourth derivative, and no boundary delta occurs. Hence JT16 gives

\[
\boxed{\sum_{|\gamma|\le4}\left(
|\partial^\gamma(U_H-U_P)|+|\partial^\gamma(W_H-W_P)|\right)
\le C e.}
\tag{JT18a}
\]

Here gamma is a spatial multi-index and the inequality is uniform on the
observation strip. Transfer the derivatives to K and bound its derivative
supremum times the L1 error. The fields are smooth for q>0, so the weak
calculation represents their ordinary filtered derivatives. This retains
the physical additive potential normalization from JT3. It supplies
static potential/spatial-jet comparison in both regulator regimes, with
the joint rate JT4 or compact rate JT5. It does not control potential
time derivatives or the products of unfiltered gradients in Q.

## 4. Uniform density transfer, including both regulator regimes

If `beta(t) X<=pi`, then `r_u=-2 beta u` and `Delta r=-2 beta` are
uniformly bounded on the fixed buffer. JT18 directly gives O(e).
This covers the entire switch layer, including cases where epsilon/A_X
is large and replacing the density by the real zero measure is wrong.

For `beta(t) X>pi`, use the proved collars to compare each density to
its own zero measure. The relevant regulator ratio is

\[
\lambda_X(t)=\frac{\sup_{|u-X|\le\ell+2}\epsilon_g(t,u)}{A_X}.
\tag{JT19}
\]

We claim uniformly on this part of the joint range that
`lambda_X<=C exp(-cX)`, `|log lambda_X|<=C X^2`, and
`B_1+B_2<=C(1+X)`. Here is the needed time dependence.

For t>=64, the larger real saddle satisfies

\[
\tfrac14<L(64)\le L(t)\le C\log(2+t),\qquad
ct\le\kappa(t)\le Ct\log(2+t),\qquad
|\log E_0(t)|\le Ct\log^2(2+t).
\tag{JT20}
\]

Indeed the saddle equation has negative residual at u=1/4 when t=64
(`4pi e<41`), so its larger root exceeds 1/4; `L'=2L/kappa>0`.
The upper bound follows by taking logarithms of
`e^(4L)<=C t(1+L)` and using `log(1+L)<=L`. The kappa bounds follow
from `kappa=8tL-2t+36`. Finally substitute
`pi e^(4L)=tL/2+9/4` into the explicit M_0 and E_0 formulas. All
bounds extend over the finite switch interval by smoothness and
positivity. In particular beta is globally bounded on t>=32, and
`beta>=c/[t log(2+t)]` for t>=128.

For `64<t<128`, E_0 is bounded. Since X is larger than the fixed buffer,

\[
\log\lambda_X\le-\tfrac14\beta X^2+\pi X/8+C\log^2X
\le-\pi X/8+C\log^2X.
\]

For t>=128 in the joint range, JT20 gives
`beta>=c/[log X log(2+log X)]`, whereas log E_0 is at most
`C log X log^2(2+log X)`. These are dominated by the negative quadratic
regulator exponent. The gamma carrier has log modulus
`-pi X/8+O(log X)+t Re(alpha^2)/4`; its last term is nonnegative for
large X. Thus the claimed exponential smallness of lambda_X follows
uniformly. The remaining logarithmic and derivative bounds follow
from the same formulas.

The simple-collar logarithmic integral, as in GO24, now gives for F=H,P

\[
|R_F-K*\nu_F|\le
C(1+X^2)\lambda_X^2
\left[1+\frac{1+\log(1+C/\lambda_X^2)}{\omega}\right]
\le Ce^{-cX}.
\tag{JT21}
\]

The O(e/omega) root displacement and O(omega) count give
`|K*nu_H-K*nu_P|<=C e`. Combining the two regimes proves JT4.
The same proof with the sharper compact-time field rate proves JT5.
No switch-dependent regulator floor appears in either conclusion.

For t>=128 the regulator is uniformly in the second regime after a
single joint-range onset. Consequently the finite Bernoulli phase model
of Note 27, evaluated with the current theta and omega, also has
O(X^(-3/4)(1+log^4 X)) error on `128<=t<=(log X)/4`. Phase freezing
costs O(1/X), and the five-term periodization has zero truncation error.
This last statement is not applied inside the unresolved-regulator layer.

## 5. The coarse layer profile

Define the explicit logarithmic regulator/carrier ratio and displacement

\[
b(t,X)=\log\frac{\epsilon_g(t,X)}{A_X(t)},\qquad
d(t,X)=\frac{\max(b(t,X),0)}{\omega(t,X)},
\tag{JT22}
\]
\[
R_{\rm layer}(t,X,y)=\frac{\omega(t,X)}{2\pi}
\{k_h(y-d(t,X))+k_h(y+d(t,X))\}.
\tag{JT23}
\]

These are **regularized-density layers, not nonreal zeros**. For d=0,
the two terms merge into `omega k_h(y)/pi`. For large d they leave the
fixed observation strip. No divisor interpretation is assigned to the
off-axis layers.

Uniformly on the joint range, and also on each fixed compact `[32,T]`,

\[
\boxed{|R_H(t,X,y)-R_{\rm layer}(t,X,y)|\le C,\qquad |y|\le Y.}
\tag{JT24}
\]

The compact statement has its own constant C_T. This O(1) error is
weaker than JT4/JT5; its purpose is to expose the transition shape.
After division by log X it gives a uniform O(1/log X) error against
`[k_h(y-d)+k_h(y+d)]/(8pi)`.

**Proof.** In the regime beta X<=pi, the logarithmic regulator/carrier
ratio varies by at most a constant on the whole fixed buffer. JT12 also
gives `Im Theta(t,u+iv)=omega v+O(1/X)`. Outside fixed phase collars,
`|cos Theta|` is comparable to `exp(|Im Theta|)`. Inside each collar,
the sole logarithmic singularity is bounded by `C+2|log|omega(z-d_j)||`,
which has bounded integral after phase rescaling. There are O(omega)
collars of area O(omega^-2). It follows, uniformly in the possibly very
large or very negative value of b, that

\[
\|S_P-2\log|\mathcal A|-2\max(b,\omega|v|)\|_{L^1(\Omega)}\le C.
\tag{JT25}
\]

For the lower estimate when b is positive the q term itself supplies
the bound; when b is negative the integrable cosine logarithm supplies
it. The upper estimate follows from `|cos Theta|<=exp(|Im Theta|)`.
The carrier logarithm is harmonic. The retained adaptive terms in JT17
are O(1), since w is between 0 and 1 and the spatial r derivatives are
bounded here. Finally,

\[
\partial_v^2\max(b,\omega|v|)=
\begin{cases}
\omega(\delta_{d}+\delta_{-d}),&b>0,\\
2\omega\delta_0,&b\le0.
\end{cases}
\]

Test against K and use its unit horizontal integral to obtain JT23--JT24.
In the complementary regime beta X>pi, Section 4 gives b<0 eventually;
zero-measure transfer and the finite phase formula yield
`R_H=omega k_h(y)/pi+O(E+1/X+omega^-4+exp(-cX))`, which is stronger
than JT24. This completes the uniform proof. In particular the
horizontal average is not omitted: it integrates out because the
leading layer potential freezes b and omega at X.

## 6. Center, time width, and a resolved switching law

Let `kappa_0=kappa(64)`. For all sufficiently large X there is a unique
solution `t_c(X)` in a fixed small right neighborhood of 64 to

\[
\boxed{b(t_c(X),X)=0,\quad\hbox{equivalently}\quad
\epsilon_g(t_c(X),X)=|\mathcal G_{t_c(X)}((1+iX)/2)|.}
\tag{JT26}
\]

This defines a center by known regulator parameters and the explicit gamma approximation, not by unknown theta zeros or the
target density. The exact implicit center is retained in the thin-layer
formula below.

On a fixed neighborhood of 64, bounded-real-part Stirling gives

\[
\log A_X(t)=-\pi X/8+\tfrac74\log X+
\frac t{16}\log^2(X/(4\pi))+O(1),
\tag{JT27}
\]

where the error is uniform in t there. Write Delta=t-64>0. The actual
switch in Note 20 obeys

\[
\log\beta(64+\Delta)=-\frac{64}{\Delta}+1-\log\kappa_0+O(\Delta),
\qquad
\frac{\beta'}\beta=\frac{64}{\Delta^2}+O(1).
\tag{JT28}
\]

These follow directly from the two exponential switch terms and the
smooth saddle, including the denominator of chi. Near 64, beta'>0.
Moreover

\[
b_t=(\log E_0)'-\tfrac12\beta'X^2-\tfrac14\Re\alpha(s_X)^2.
\tag{JT29}
\]

The first term is bounded and the last is negative of order log^2 X.
Thus b is strictly decreasing in that neighborhood for large X. At
64 it is positive of order X, and at any fixed time just above 64 it
is negative of order X^2. This proves existence and uniqueness of JT26
in the stated neighborhood, without claiming uniqueness at all times.

Equations JT26--JT28 give

\[
\beta(t_c)=\frac\pi{4X}+O(\log^2X/X^2),\qquad
\boxed{t_c(X)-64=\frac{64}{\log X+c_0+O(1/\log X)},\quad
c_0=\log\frac{4e}{\pi\kappa_0}.}
\tag{JT30}
\]

The fixed eta and the amplitude constants affect finer terms; they do
not enter c_0. At this center,

\[
b_t(t_c,X)=-\frac{\pi X\log^2X}{512}
 (1+O(1/\log X)),\qquad
\omega(t_c,X)=\tfrac14\log X+O(1).
\tag{JT31}
\]

Indeed beta'/beta is asymptotic to log^2 X/64, and beta is asymptotic
to pi/(4X). On a time interval of width O(1/(X log X)) around t_c,
`b_tt=O(X log^4 X)` from JT28 and the smooth gamma/E_0 factors.
The direct derivatives of the switch justify this bound; it is not
obtained by differentiating the error in JT30.

For a bounded real parameter tau, set

\[
t_X(\tau)=t_c(X)-\frac{128\tau}{\pi X\log X},\qquad
\tau_+=\max(\tau,0).
\tag{JT32}
\]

Taylor's formula with the stated derivative bounds gives
`b(t_X(tau),X)/omega(t_X(tau),X)=tau+O(1/log X)` uniformly on bounded
tau intervals. Combine this with JT24 and the Lipschitz continuity of
k_h to obtain the resolved law

\[
\boxed{\frac{R_H(t_X(\tau),X,y)}{\log X}=
\frac{k_h(y-\tau_+)+k_h(y+\tau_+)}{8\pi}
+O(1/\log X),}
\tag{JT33}
\]

uniformly for bounded tau and `|y|<=Y`. Times in this layer lie above
64 for large X. Before the center, the two regularized layers approach
the real axis; at and after it their leading profiles merge. This
resolves the nonuniform limit in Note 27 GO33 without changing q.

**Centering warning.** The asymptotic location JT30 is much less accurate
than the width in JT32. Replacing t_c by `64+64/log X`, or even by the
two displayed inverse-logarithm terms, does not justify JT33: their
omitted time errors are far larger than `1/(X log X)`. Retain the exact
implicit center or separately prove the required finer centering error.
This is not a numerical certificate of t_c at any chosen height.

## 7. Exact heat residual and the remaining spatial gap

The field P does not solve the heat equation exactly. Differentiating
its explicit factors gives

\[
\mathcal R_P:=(\partial_t+\partial_{zz})P
=\frac14\sum_{w=s,1-s}\mathcal G_t(w)
 [\alpha(w)^2-D_t(w)^2-D_t'(w)],
\tag{JT34}
\]
\[
\alpha^2-D_t^2-D_t'=
-\alpha'-t\alpha^2\alpha'
-\tfrac t2\{(\alpha')^2+\alpha\alpha''\}
-\tfrac{t^2}4\alpha^2(\alpha')^2.
\tag{JT35}
\]

Consequently on the joint range

\[
|\mathcal R_P|\le C\frac{1+t\log^2X}{X}
 (|\mathcal G_t(s)|+|\mathcal G_t(1-s)|).
\tag{JT36}
\]

This is a paid field residual. It is neither a propagated error theorem
nor a bound for the differentiated density, actual current, forcing,
potential time derivative, Q or Delta Q. Those comparisons still require
work, and all adaptive terms in the original equations remain present.
JT4/JT5 instead use direct static comparison with the canonical field.

The new joint range is genuinely unbounded in time, but at a fixed large
t it requires `X>=exp(4t)` (and the fixed onset). The inner theorem in
[Note 19][n19] has a buffered window of size `kappa^(1/3)`, with
`kappa=O(t log(2+t))`. These domains have **no proved overlap** as t
tends to infinity. The exponential restriction comes from a conservative
absolute Gaussian integration estimate. It is not a proved necessary
limitation of the gamma pair, much less of all outer representations.

**Next owner: Analytical — Astra.** Develop a complex-contour/saddle
version of JT6 that removes or replaces the `exp(t b^2/4)` loss, with
both gamma contributions, middle/connecting contours and arithmetic
remainder paid. Deliver a new proved joint validity range and compare
its endpoint explicitly with the inner window. A smaller outer threshold
alone is not an overlap. If a further intermediate regime is required,
name it and give its missing source estimate before requesting numerics.
The exact residual JT34 is available for the later evolution comparison.
No bounded numerical question has yet been issued; the Sol queue is empty.

## 8. Error ledger, control screen and provenance

| Component | Established payment | Remaining limitation |
| --- | --- | --- |
| Field on full complex buffer | JT10--JT11, including all modes and convolution regions | Constants/onset are not instantiated; no claim outside the stated joint or compact range |
| Arbitrary positive regulator on controlled simple collars | JT14--JT18, without a regulator floor | Requires the acquired analytic units and simple-collar geometry; not a multiple-event estimate |
| Density through the switch | JT4--JT5, same physical q, vanishing absolute error | Fixed spatial average of the explicit gamma field remains in the model |
| Physical potential and filtered w | JT18a, spatial derivatives through order four at the same rate | No time derivative or unfiltered gradient-product comparison follows |
| Coarse switch shape | JT24, O(1) absolute; JT33, O(1/log X) normalized | Exact implicit center required at the very narrow time scale |
| Finite phase density in the resolved regime | JT21 and Note 27's exact five terms; same joint static rate for t>=128 | Not used for the unresolved regulator layer |
| Heat equation | Exact residual JT34--JT36 | Positive observable evolution, actual covariance and stability remain open |
| Global matching | A joint outer range and a switch-layer model now exist | No inner/outer overlap, finite-transition acceptance or all-time assembly |

The canonical source identity, exact reflection and full arithmetic tail
remain the distinguishing premises. Euler-factor controls change the
completion and added factor; weighted-square and finite-tail changes
lack the unchanged full coefficients/reflection; reflected, smooth and
positive-primitive controls lack the canonical gamma-times-zeta identity;
finite-prime orbit controls lack full reflection; atomic/finite-profile
controls lack the completed xi/source profile; and the RH-conditional
normalized-endpoint controls fail ordinary Dirichlet-series arithmetic.
Thus the [Note 27 Section 8 screen][n27] applies with its exact scopes.
The local lemma alone is not claimed to reject any control: it can hold
in a simple-root region of a source that collides elsewhere.

This is no RH or global simplicity criterion. No source is excluded by
its shared shape properties, and no zero outside the covered buffers is
counted. Same-assistant review, reference inspection and file checks do
not constitute independent mathematical validation. The [catalog][refs]
records the reused primary sections and sibling inspection. No numerical
run, new third-party PDF, manuscript snapshot or manuscript integration
was performed in this continuation.

[n27]: 27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md
[n20]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[n19]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[n14]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[review]: ../reviews/11_JOINT_OUTER_AND_SWITCH_LAYER_SELF_REVIEW_20261024.md
[continuation]: 29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md
[refs]: ../references/README.md
[sibling]: ../../../investigations-4/notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md
[poly]: https://arxiv.org/html/1904.12438v2
[gamma]: https://dlmf.nist.gov/5.11
[zeta]: https://dlmf.nist.gov/25.2
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
