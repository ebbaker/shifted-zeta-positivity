# The universal inner turning profile

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, supplied by the parent session. Internal LLM-assisted derivation and comparison; not external mathematical refereeing or formal verification.

This continues the [manuscript](../../manuscript/theta_manifold_geometry.tex), the preceding [real Gauss-map analysis](../../../21_quaternion_theta_geometry/notes/02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md), and its [positive primitive collision control](../../../21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md).

## Assessment

The manuscript's full stationary predecessor, parity split, quarter-turn limit, and conditional one-sided continuity theorem are correct as stated. Its fixed-sign argument supplies regularity on the whole tested interval, including the second branch, and resolves the angle-lift ambiguity. The criterion does require uniformity through candidate events; continuity on individual regular slices supplies no such uniformity.

A sharper scale is available. The existing quarter-turn is measured on a spatial interval of order `sqrt(T-t)`, whereas the nontrivial angular core has width of order `T-t`. On that finer scale its universal profile is an arctangent, and its angular derivative is a positive Cauchy kernel. This is a local heat-flow theorem, not a theta-specific exclusion estimate.

## 1. The finite inner-window theorem

Let `H_t=-H_xx` be real analytic near `(T,a)`, and suppose its exact spatial multiplicity there is `m=2r+j`, with `r>=1` and `j=0,1`. Set

\[
s=T-t,\qquad W=\partial_x^jH,\qquad
A=\partial_x^{2r}W(T,a),\quad B=\partial_x^{2r+1}W(T,a),
\quad k=A/r!\ne0.
\]

Let `chi(s)` be the analytic full stationary predecessor, so

\[
W_x(T-s,\chi(s))=0,\qquad
\chi(s)=a-\frac{B}{rA}s+O(s^2).
\]

For every fixed `C<infinity`, uniformly for `|xi|<=C`,

\[
\begin{aligned}
W(T-s,\chi(s)+s\xi)&=ks^r\{1+O_C(s)\},\\
W_x(T-s,\chi(s)+s\xi)&=ks^r\{r\xi+O_C(s)\},\\
W_{xx}(T-s,\chi(s)+s\xi)&=ks^{r-1}\{r+O_C(s)\}.
\end{aligned}\tag{1}
\]

The remainders and any fixed number of derivatives in `xi` are uniform on that compact interval. Consequently `W` has the sign of `k` throughout the interval for sufficiently small positive `s`. With any continuous angle lift `alpha_j=arg(W+iW_x)`, let

\[
\Theta_s(\xi)=\alpha_j(T-s,\chi(s)+s\xi)
             -\alpha_j(T-s,\chi(s)).
\]

Then

\[
\boxed{\Theta_s(\xi)=\arctan(r\xi)+O_C(s),\qquad
s\,\partial_x\alpha_j(T-s,\chi(s)+s\xi)
=\frac{r}{1+r^2\xi^2}+O_C(s).}\tag{2}
\]

In particular, the angular derivative is strictly positive on each such fixed inner window for sufficiently small `s`.

**Proof.** Use the convergent heat Taylor expansion

\[
W(T-s,a+y)=\sum_{p,q\ge0}
 \frac{s^p y^q}{p!q!}\partial_x^{2p+q}W(T,a).
\]

Write `chi(s)-a=s eta(s)`, with analytic `eta(0)=-B/(rA)`, and put `y=s(eta(s)+xi)`. Terms below total `s` degree `r` in `W` vanish. Its degree-`r` coefficient is `A/r!=k`, independent of `xi`. For `W_x`, the degree-`r` coefficient is

\[
\frac{A}{(r-1)!}(\eta(0)+\xi)+\frac{B}{r!}=kr\xi.
\]

For `W_xx`, the lowest degree is `r-1` with coefficient `A/(r-1)!=kr`. The quotient series after those powers of `s` are removed are analytic in `(s,xi)` on every fixed compact `xi` interval for small `s`; this proves (1), including the differentiable remainders.

Because `W` has one sign and `W_x=0` at the center,

\[
\Theta_s(\xi)=\arctan(W_x/W).
\]

There is no winding ambiguity. Substitute (1) into this expression and into

\[
\partial_x\alpha_j=\frac{WW_{xx}-W_x^2}{W^2+W_x^2}
\]

to obtain (2). The limiting positive kernel has a positive minimum on every fixed compact `xi` interval, which proves the final assertion.

The peak height is asymptotic to `r/s`; the half-width at half maximum is asymptotically `s/r`, giving full width `2s/r`. These descriptions refer to the limiting inner profile, and do not assert uniqueness of all extrema outside the window.

## 2. Finite-window turning and the precise status of the pi mass

Equation (2) gives, for every fixed `C>0`,

\[
\begin{aligned}
\alpha_j(T-s,\chi(s)+Cs)-\alpha_j(T-s,\chi(s))
 &\longrightarrow\arctan(rC),\\
\int_{\chi(s)-Cs}^{\chi(s)+Cs}\partial_x\alpha_j(T-s,x)\,dx
 &\longrightarrow2\arctan(rC).
\end{aligned}\tag{3}
\]

The integrand is positive on the whole inner interval for sufficiently small `s`. Therefore the unambiguous iterated limit is

\[
\boxed{\lim_{C\to\infty}\lim_{s\downarrow0}
 \int_{\chi(s)-Cs}^{\chi(s)+Cs}(\partial_x\alpha_j)_+(T-s,x)\,dx
 =\pi.}\tag{4}
\]

This asserts positive mass in successively larger **finite inner windows**. It does not interchange the two limits, assert an error uniform for unbounded `C`, or assert a weak limit of the signed measures on a fixed spatial neighborhood. Those stronger statements would require separate tail control.

The two-sided version of the already established parabolic profile also gives net turning `pi` across `[chi(s)-c sqrt(s),chi(s)+c sqrt(s)]` for each fixed `c>0`: `F_r` is even and positive, `F_r'(-c)=-F_r'(c)`, and `W` has fixed sign throughout. This is an endpoint statement about the continuous lift; it does not assert that the angular derivative stays positive on that larger interval.

## 3. Source-estimate targets implied by the core

A one-sided modulus tending to zero is a sufficient target, but the local theorem requires less. Suppose the tested rightward stationary-start intervals obey a uniform upper bound `theta_*<pi/2` throughout sufficiently small covered neighborhoods. Choose fixed `C` so that `arctan(rC)>theta_*`. The length `Cs` tends to zero, and (3) contradicts the bound. Thus a uniform strict quarter-turn gap suffices for collision exclusion. This is another conditional criterion; no such source-prescribed gap is established here.

The core gives an explicit obstruction to uniform integrability of the positive angular derivative. For `p>1`, fixed `C>0`, and sufficiently small `s`,

\[
\int_{\chi(s)-Cs}^{\chi(s)+Cs}
 (\partial_x\alpha_j)_+^p\,dx
=s^{1-p}\left\{\int_{-C}^C
 \left(\frac{r}{1+r^2\xi^2}\right)^p\,d\xi+O_C(s)\right\}.
\tag{5}
\]

Accordingly, a source-prescribed uniform local `L^p`, `p>1`, bound on the positive part, covering both branch intervals, would exclude collisions. Uniform `L^1` boundedness by itself does not: finite nonzero mass can concentrate. A direct uniform-integrability estimate is also sufficient. These are possible targets for the source bridge, and their denominators remain the branch jet energies.

## 4. The second branch differs at leading order even in the inner window

For an odd collision, `j=1`, the same heat Taylor counting gives uniformly on every fixed inner window

\[
H(T-s,\chi(s)+s\xi)=O_C(s^{r+1}),
\qquad h_1=ks^r(1+O_C(s)).
\]

Consequently

\[
\boxed{\frac{E_1^{\rm jet}}{E}
=\frac{h_1^2+h_2^2}{H^2+h_1^2}
\longrightarrow1+r^2\xi^2.}\tag{6}
\]

The energies agree asymptotically at the stationary point `xi=0`, as the manuscript states. They are **not** asymptotically equal on a fixed nonzero inner scaled window, despite that window's physical length tending to zero. Any source-to-turning argument importing a bound paid by the physical energy must carry this factor explicitly. A bounded fixed-window comparison is available from (6), but a comparison constant independent of window size does not follow.

## 5. Controls and exact finite checks

All conclusions apply to the positive, strongly log-concave, rapidly decaying source family of Investigation 21 Note 56 at its proven nondegenerate positive-time collision. There `r=1`, and the core is `arctan(xi)` with positive derivative kernel `1/(1+xi^2)`. Thus that control fails every proposed uniform modulus, strict quarter-turn gap, uniform-integrability condition, or local positive-part `L^p` bound for `p>1`. Generic positivity, convexity, decay, primitive reconstruction, and generic calibrated jet geometry cannot supply those bounds. A successful proof must still identify extra complete-theta information.

The companion standard-library checker [check_inner_turning_profile.py](../../numerics/check_inner_turning_profile.py) passed **792 exact rational assertions across 72 cases**: `j=0,1`; `r=1,...,12`; and pure, asymmetric, and negative-asymmetric finite polynomial germs. It checks the backward-heat sign through `H_s=H_xx`, the first two stationary-center coefficients, all three leading inner jet coefficients, the angular numerator and denominator, and the odd-branch physical-energy distinction. It does not prove the analytic theorem, certify a theta sign, supply a source estimate, or control an unbounded spatial domain.

The [continuation review](../../reviews/02_CONNECTION_BRIDGE_AND_INNER_TURNING_REVIEW_20261015.md) records the proof and replay scope. The existing quarter-turn theorem needs no correction.
