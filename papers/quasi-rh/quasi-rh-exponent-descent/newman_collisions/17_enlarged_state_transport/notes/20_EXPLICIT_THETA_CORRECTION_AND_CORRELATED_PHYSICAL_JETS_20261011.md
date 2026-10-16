# Explicit theta correction and correlated physical derivatives

11 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
worker and is not inferred. These are internal LLM derivations and internal
cross-checks, not independent mathematical validation.

This continues Notes 18--19. Their ambiguity statements concern the coarse
disk allowance. The stronger source input used here constrains the actual
theta remainder and therefore need not permit the alternative observations
constructed there. No relative signed source theorem near every possible
collision, new global collision covering, or RH conclusion follows.

## Result and source input

The dominant omitted Riemann--Siegel correction is almost a single physical
exponential, with logarithmic derivative `-pi/8`. Keeping this correction
reduces the residual by a factor of order `N` on the shrinking-sector
disks of radius `1/L` with fixed cutoff described in Section 6.
The local constants below are especially sharp near the beginning of a
cutoff interval; Section 1.1 supplies bounds for every cutoff phase. The resulting physical-jet errors lie
near one common vector, rather than filling independent derivative boxes.
Applying `partial_x+pi/8` removes the leading correction altogether.

The input is the genuine-theta `A+B-C` approximation in
[D.H.J. Polymath, Corollary 6.4 and Proposition 6.6(iv)--(vi)](https://arxiv.org/html/1904.12438v2#S6.SS3),
with its explicit remainder constants, on `0<t<=1/2`, `x>=200`,
`0<=y<=1`. Its finite `A+B` sum is exactly the project's `G=AF` after the
holomorphic reflection rewrite. The printed correction is
`C_poly(t,x+iy)=exp(-pi i y/8) C(t,x)` and is not holomorphic in its spatial
argument. We never differentiate that printed expression by Cauchy's
formula. The argument below constructs a holomorphic exponential surrogate,
pays the difference, and applies Cauchy's formula only to the resulting
holomorphic remainder. The elementary cancellation and bounds below are
derived here from the source formulas.

## 1. Exact cancellation in the leading correction

For fixed `t,N` put
\[
\tau(x)=\frac{x}{2}+\frac{\pi t}{8},\quad
a(x)=\sqrt{\frac{\tau(x)}{2\pi}},\quad
p(x)=1-2(a(x)-N),\qquad k=\frac\pi8.
\tag{1}
\]
Let
\[
u(p)=\frac{\cos[\pi(p^2/2+3/8)]}{2\cos(\pi p)},\qquad
v(p)=\frac{\sin[\pi(p^2/2+3/8)]-\sqrt2\cos(\pi p/2)}
 {2\cos(\pi p)}.
\tag{2}
\]
These are the real and imaginary parts of the source's `C_0(p)` on the real
axis. The apparent singularities at `p=+/-1/2` are removable; the sharper
local estimates below stay near `p=1`, where no division problem arises.

For the prescribed Stirling factor `M_0` and source phase
\[
U(\tau)=\exp\{-i[\tfrac\tau2\log(\tau/(2\pi))
-\tfrac\tau2-\tfrac\pi8]\},
\]
direct substitution of the project's exact `m_0=log M_0` gives
\[
\boxed{M_0(i\tau)U(\tau)e^{i\pi/8}
=-\frac{\sqrt\pi}{8}\tau^{3/2}(1+i/\tau)e^{-\pi\tau/4}.}
\tag{3}
\]
The large oscillatory phases cancel exactly. Consequently the real
correction in Corollary 6.4 is
\[
\boxed{C(t,x)=(-1)^{N+1}\frac{\sqrt\pi}{4}
 e^{-\pi x/8-t\pi^2/64}\tau(x)^{3/2}
 \left[u(p(x))-\frac{v(p(x))}{\tau(x)}\right].}
\tag{4}
\]
The sign is part of the formula: the physical approximation is `H=G-C`
plus its paid residual.

Define the slowly varying real amplitude
\[
D(t,x)=e^{kx}C(t,x).
\]
Since `tau'=1/2` and `p'=-1/(4 pi a)`, exact differentiation gives
\[
\begin{split}
D_x={}&(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-t\pi^2/64}\tau^{3/2}
\left[\frac{3u}{4\tau}-\frac{v}{4\tau^2}
-\frac{u'-v'/\tau}{4\pi a}\right].
\end{split}\tag{5}
\]
The primes on `u,v` mean differentiation in `p`; all other spatial
derivatives hold `t,N` fixed.

For real `|p-1|<=1/100`, the elementary bounds
\[
|u|\le1,\quad |v|\le2,\quad |u'|\le4,\quad |v'|\le6
\tag{6}
\]
hold. For verification, `|cos(pi p)|>=cos(pi/100)>.999`,
`|sin(pi p)|<.032`, `|p|<=1.01`, and the sine/cosine numerators have
modulus at most one, or at most `1+sqrt2`. Quotient differentiation gives
`|u'|<2` and `|v'|<3`; (6) keeps generous reserves. No unproved numerical
property of the correction function is used.

## 1.1 Uniform bounds through the removable points

The local profile restriction can be removed analytically. On the complex
rectangle `|Re p|<=5/4`, `|Im p|<=1/4`, the only zeros of the denominator
of `C_0` are the simple zeros at `p=+/-1/2`. Its numerator vanishes at both,
so the quotient extends holomorphically across them. On the vertical sides
`|2 cos(pi p)|>=sqrt(2)`; on the horizontal sides it is at least
`2 sinh(pi/4)>sqrt(2)`. The numerator has modulus at most
`exp(5 pi/16)+sqrt(2) cosh(pi/8)<3+2=5`. The maximum modulus principle gives
`|C_0|<5/sqrt(2)<4` on the rectangle.

A radius `6/25` circle around any real `|p|<=101/100` lies in that rectangle.
Cauchy's estimate therefore proves `|C_0'|<50/3<17`. Thus throughout this
real interval, including the removable points,

\[
|u|,|v|\le4,\qquad |u'|,|v'|\le17.
\tag{6a}
\]

Every theorem below remains valid for all natural cutoff phases after
replacing its local slope bound `J` by

\[
J_{\mathrm{all}}=\frac3{\tau_-}+\frac1{\tau_-^2}
+\frac{17+17/\tau_-}{4\pi a_-}.
\tag{6b}
\]

This follows directly from (5). The global profile bound is analytic; the
numerical implementation below uses the sharper bounds (6). The stability
condition on the integer cutoff remains necessary in either case.

## 2. Complete fixed-cutoff disk ledger

Fix a real center `X`, radius `0<r<=1`, and time `0<t<=1/2`, with
`x_-=X-r>=200`, `x_+=X+r`. Require that the same natural cutoff holds
throughout the disk's real projection:
\[
N^2\le\frac{x_-}{4\pi}+\frac t{16},\qquad
\frac{x_+}{4\pi}+\frac t{16}<(N+1)^2.
\tag{7}
\]
Also require `|p(x)-1|<=1/100` for `x in [x_-,x_+]`. The latter
restriction is convenient for the explicit derivative constants, not an
intrinsic limitation of the Riemann--Siegel correction.

Use the parent manuscript's disk constants at fixed time:
\[
\begin{gathered}
q_\pm=x_\pm/(4\pi),\quad V=x_-/2,\quad
S=\tfrac12\sqrt{x_+^2+(1+r)^2},\\
\alpha_- =\tfrac12\log q_- -V^{-2},\qquad
A_* =\frac3{2V}+\frac12\sqrt{\log^2(S/(2\pi))+\pi^2/4},\\
D_* =\frac3{2V^2}+\frac1{2V},\quad
L_*=A_*(1+tD_*/2),\quad K=e^{rL_*/2}.
\end{gathered}\tag{8}
\]
The notation `D_*` in (8) is a bound for `alpha'`, not the real amplitude
`D(t,x)` above. Define
\[
\begin{gathered}
V_n=n^{-1/2}\exp\{t[\log^2 n/4-\alpha_-\log n/2]\},\quad
\ell_n=\max\{|\log(q_-/n^2)|,|\log(q_+/n^2)|\},\\
\kappa_* =\frac{tr}{2(x_--6)},\quad
U_n=\exp\frac{t^2\ell_n^2/16+0.626}{x_--6.66}-1,\\
E_{AB}=\sum_{n\le N}(1+N^{\kappa_*}n^r)V_nU_n.
\end{gathered}\tag{9}
\]
These pay the complete two finite source sums. No arithmetic term is
discarded or independently rephased. Set
\[
Z=q_-^{-1/4}\exp\left\{-\frac t{16}\log^2q_-
+\frac{3\sqrt{\log^2q_++\pi^2/4}+3.58}{x_--8.52}\right\},
\tag{10}
\]
\[
B_C=\frac{1.24(3^r+3^{-r})}{N-0.125}+\frac{6.92}{x_--12}.
\tag{11}
\]
For the slow-amplitude comparison define
\[
\tau_\pm=x_\pm/2+\pi t/8,\quad
a_- =\sqrt{\tau_-/(2\pi)},\quad
W=\left(\frac{\tau_+}{\tau_-}\right)^{3/2},
\]
\[
J=\frac3{4\tau_-}+\frac1{2\tau_-^2}
+\frac{4+6/\tau_-}{4\pi a_-},\qquad
\boxed{\eta_*=K\{E_{AB}+Z[B_C+2rWJ]\}.}
\tag{12}
\]
Every constant has an explicit elementary definition. To cover a time
interval, use outward monotone bounds or the parent's endpoint maximum
for the affine time exponent in `V_n`; do not assume that exponent is
positive. The companion outward ledger uses exactly this rule.

## 3. Holomorphic rank-one correction theorem

**Theorem.** Under (7) and the hypotheses above, let
\[
C_X(z)=C(t,X)e^{-k(z-X)},\qquad
\mathcal E_X(z)=H_t(z)-G_{t,N}(z)+C_X(z).
\tag{13}
\]
Then `E_X` is holomorphic on a neighborhood of the disk and
\[
\boxed{\sup_{|z-X|\le r}\frac{|\mathcal E_X(z)|}{A_t(X)}\le\eta_*.}
\tag{14}
\]
Consequently, with `f_j=G^(j)(X)/A_t(X)` and `c=C(t,X)/A_t(X)`,
\[
\boxed{\frac{H_t^{(j)}(X)}{A_t(X)}
=f_j-c(-k)^j+\delta_j,\qquad
|\delta_j|\le j!r^{-j}\eta_*\quad(j\ge0).}
\tag{15}
\]
This is a physical-derivative statement: no derivative of the normalizer
has been omitted, because (14) divides by the fixed center value `A_t(X)`.
If instead a checker uses the analytic normalization `A_t(z)`, the usual
normalizer-convolution payment is also valid, but is a larger allowance.

**Proof.** Put `z=x+iy`, first with `0<=y<=r`, and
`s_+(z)=(1-iz)/2`. The source approximation, its explicit errors and the
same monotone majorants used in the parent give
\[
\frac{|H_t(z)-G_{t,N}(z)+e^{-kiy}C(t,x)|}{|M_t(s_+(z))|}
\le E_{AB}+ZB_C.
\tag{16}
\]
The source prefactor calculation used in Proposition 6.6 also gives
\[
\frac{P(t,x)}{|M_t(s_+(z))|}\le Z,\qquad
P(t,x)=e^{t\pi^2/64}|M_0(i\tau(x))|.
\tag{17}
\]
Indeed the intermediate prefactor bound has the factor
`(tau/(2pi))^(-(1+y)/4)` and exponent error
`[3|log(x/(4pi))+i pi/2|+3.58]/(x-8.52)`; replacing them monotonically
produces (10). This step does not divide a remainder bound by another
upper bound.

Along the straight segment from `s_+(X)` to `s_+(z)`, (8) gives
`|m_t'|<=L_*`. Since `|M_t(s_+(X))|=A_t(X)`,
\[
\frac{|M_t(s_+(z))|}{A_t(X)}
\le e^{L_*|z-X|/2}\le K.
\tag{18}
\]
This direct segment estimate is what permits center normalization with
the same `K`; it must not be replaced by an unproved identification of
`A_t(z)` and `A_t(X)`.

By (5)--(6),
\[
|D_x(t,\xi)|\le\frac{\sqrt\pi}{4}e^{-t\pi^2/64}
\tau_+^{3/2}J\qquad(x_-\le\xi\le x_+).
\]
The exact modulus from (3) is
\[
2P(t,x)=\frac{\sqrt\pi}{4}e^{-\pi x/8-t\pi^2/64}
\tau(x)^{3/2}\sqrt{1+\tau(x)^{-2}}.
\]
Therefore the fundamental theorem of calculus, (17), and (18) imply
\[
\begin{split}
\frac{|e^{-kiy}C(t,x)-C_X(z)|}{A_t(X)}
&=\frac{e^{-kx}|D(t,x)-D(t,X)|}{A_t(X)}\\
&\le\frac{2rWJ P(t,x)}{A_t(X)}
\le2rWJKZ.
\end{split}\tag{19}
\]
Combining (16)--(19) gives (14) on the upper half-disk. The actual
`H,G,C_X` all have real symmetry, so their holomorphic difference has the
same bound on the lower half. Cauchy's formula applied to this difference
gives (15). The nonholomorphic printed `C_poly` has only been used in the
pointwise comparison, never as a holomorphic function. QED.

## 4. New derivative constraints on the actual remainder

Let `B=partial_x+k`, with fixed `k=pi/8`. For every integer `j>=1`,
`B^j C_X=0`, and (14) yields
\[
\boxed{\frac{|B^j(H_t-G_{t,N})(X)|}{A_t(X)}
\le\eta_*\sum_{\ell=0}^j{j\choose\ell}
k^{j-\ell}\ell!r^{-\ell}.}
\tag{20}
\]
For the physical error coordinates
`e_j=(H_t^(j)-G^(j))/A_t(X)`, this includes
\[
\boxed{|e_1+ke_0|\le\eta_*(r^{-1}+k).}\tag{21}
\]
This signed relation distinguishes the true theta remainder from the
arbitrary bounded holomorphic perturbations used in Notes 18--19. It also
gives a division-free collision-exclusion test:
\[
\boxed{\frac{|G_{t,N}'(X)+kG_{t,N}(X)|}{A_t(X)}
>\eta_*(r^{-1}+k)
\quad\Longrightarrow\quad (H_t,H_t')(X)\ne(0,0).}
\tag{22}
\]
The finite sum in (22) must still be bounded from below using its actual
phases; (22) does not establish that lower bound uniformly.

There is another useful consequence directly on the genuine second
stationary set. Put `rho=-k` and suppose `H_t''(X)=0`. Eliminating the
common amplitude `c` in (15) gives exactly
\[
\begin{aligned}
K_3&=f_3-\rho f_2+(\delta_3-\rho\delta_2),\\
K_1&=f_1-f_2/\rho+(\delta_1-\delta_2/\rho),\\
K_0&=f_0-f_2/\rho^2+(\delta_0-\delta_2/\rho^2).
\end{aligned}\tag{23}
\]
Here `K_j=H_t^(j)/A_t(X)`. In particular the slope and third-jet errors
in these stationary formulas are at most
\[
\eta_*(r^{-1}+2r^{-2}/k),\qquad
\eta_*(6r^{-3}+2kr^{-2}),
\tag{24}
\]
respectively. This removes the leading correction without estimating its
sign or dividing by a potentially vanishing physical first jet. It does
not remove the small residual error, which remains absolute.

On the first stationary set `K_1=0`, the same elimination gives
`K_0=f_0-f_1/rho+delta_0-delta_1/rho` and
`K_2=f_2-rho f_1+delta_2-rho delta_1`. These are the corresponding
actual-source coordinates for the first signed target.

The same rank-one information can be transferred to Note 12's carrier
response. If its operator coefficients are denoted by `a_D,b_D` and
`k_D=b_D'/b_D`, the leading physical exponential contributes
`-c[rho^2-a_D rho+b_D]` to `R/A` and
\[
-c[\rho^3-(a_D+k_D)\rho^2+B_D\rho],\qquad
B_D=b_D-a_D'+a_Dk_D,
\]
to `mathcal R/A`. The coefficient derivatives cancel as shown; all
remaining terms are paid using the smaller common remainder (14).

## 5. Stable evaluation of the correction amplitude

An outward implementation need not form the exponentially tiny `C` and
`A` separately. Let `alpha_r,alpha_i` be the project's exact real and
imaginary parts of `alpha((1-iX)/2)`. Then
\[
c=(-1)^{N+1}e^{W_X}[u(p(X))-v(p(X))/\tau(X)],
\tag{25}
\]
where the cancellation-free exponent is
\[
\begin{split}
W_X={}&\frac14\log\pi+\log8+\frac14+
\frac32\log\tau(X)-\frac78\log(1+X^2)
-\frac X4\arctan(1/X)\\
&-\frac{t\pi^2}{64}-\frac t4(\alpha_r^2-\alpha_i^2).
\end{split}\tag{26}
\]
For example the exact identity
\[
\Re m_0((1-iX)/2)=\frac78\log(1+X^2)-5\log2
+\frac14\log\pi-\frac14-\frac X4\arctan X
\]
and `arctan X=pi/2-arctan(1/X)` prove (26). Thus neither huge phase
subtraction nor division of exponentially small numerical values is
required. Existing outward log, exponential, trigonometric and arctangent
routines suffice.

## 6. Scale improvement and scope

On the shrinking sector `t=kappa/L`, `1<=kappa<=3/2`, take `r=1/L` and
stay in the fixed-cutoff `p` patch above. The parent sum bounds give
\[
Z\asymp e^{-\mathfrak b/t},\quad
E_{AB}=O(e^{-\mathfrak d/t}),\quad B_C=O(N^{-1}),\quad
J=O(N^{-1}),\quad K=O(1),
\]
with `mathfrak b=kappa(kappa+4)/16`,
`mathfrak d=kappa(kappa+12)/16`, and `N asymp exp(L/2)`.
In particular `mathfrak d-mathfrak b=kappa/2`.
Consequently
\[
\eta_*=O(e^{-\mathfrak b/t}/N)=O(e^{-\mathfrak d/t}),\qquad
|\delta_j|=O_j(L^j e^{-\mathfrak d/t})
\tag{27}
\]
for each fixed order. The slow-amplitude comparison in (19) has the
additional `r` factor. This is a complete error improvement on the stated
patch, including both finite-source errors and the leading-correction
remainder. It is not obtained by treating the leading correction as
arbitrary disk noise.

Cutoff crossings are explicitly excluded by (7). Extending this interface
across them requires matching the correction change with the added or
removed finite term. Section 1.1 supplies uniform derivative bounds through the removable
points for every real cutoff phase. The retained numerical checker uses
the sharper local constants and verifies their domain explicitly. A
covering theorem must still pay every cutoff transition and predecessor
neighborhood.

The new derivative constraint resolves an error-analysis limitation and
can certify genuine weak stationary branches that the old disk envelope
could not determine. It remains an absolute approximation: near arbitrarily
small joint first jets, the residual in (14) need not vanish with their
energy. The remaining analytic task is a lower or one-sided signed bound
for the complete finite response, or a still more intrinsic source estimate,
on a region with the predecessor and cutoff coverage required by Notes
16--17.


## 7. Outward verification on the previously ambiguous stationary cell

The [corrected theta checker](../numerics/check_theta_corrected_stationary_cell.py)
and its [small record](../numerics/THETA_CORRECTED_STATIONARY_CELL_RECORD_20261011.json)
verify the complete source bound and physical stationary sign on

\[
N=22066,\quad t_0=\frac1{2\log N},\quad x_0=4\pi N^2,\qquad
(t,X)\in[t_0,t_0+10^{-8}]\times(x_0+[58.567,58.571]).
\tag{28}
\]

Every center uses a radius `r=0.05` disk. The natural cutoff stays equal
to `N` on all disks, and their entire real projections satisfy (6).
The checker regenerates all 22,066 finite terms and twelve moments,
pays the spatial and time transports, and uses eight contiguous real
subcells of width `0.0005`. The absolute twelfth moment pays every Taylor
remainder through derivative three. All sign decisions use 60-digit
directed Decimal intervals with explicit trigonometric remainders and
hash-checked inherited interval arithmetic.

The normalized analytic remainder is used in this implementation,
followed by the full normalizer convolution through order three. These
are conservative physical payments; the constant-center version of the
theorem permits the slightly smaller payments (15). The implementation
also retains the larger valid slope majorant

\[
J_{\mathrm{code}}=
\frac3{4\tau_-}(1+2/\tau_-)
+\frac{4+6/\tau_-}{4\pi a_-}+\frac1{\tau_-^2}\ge J.
\]

Rounded outward values from the record are:

| Quantity | Certified enclosure or upper bound |
| --- | ---: |
| `K` | `<1.285072` |
| `E_AB` | `<2.412707e-8` |
| `Z` | `<0.001928292` |
| `B_C` | `<0.000112561476` |
| `2r W J_code` | `<0.000001442561` |
| corrected normalized disk residual | `<3.135063e-7` |
| real correction `c=C/A` | `[-0.001781020134,-0.001781018077]` |
| physical first derivative residual divided by `A` | `<0.000006393239` |
| physical second derivative residual divided by `A` | `<0.000255777883` |
| physical third derivative residual divided by `A` | `<0.015346692` |

The retained leading correction accounts for the common physical error
vector `-c(1,-pi/8,(pi/8)^2,-(pi/8)^3)`. Its derivative contributions
are explicitly evaluated before the displayed residual is added.
On the full rectangle (28),

\[
H_x/A<-2.76859008,\qquad H_{xxx}/A>97.46819021.
\tag{29}
\]

At the left and right spatial endpoints respectively,

\[
H_{xx}/A<-0.20348773,\qquad H_{xx}/A>0.18618620.
\tag{30}
\]

Since `A>0`, (29) makes the physical `Hxx` strictly increasing in space.
Together with (30), this proves that every time in (28) has exactly one
real `Hxx=0` point. The implicit function theorem gives a smooth branch.
Only the subcell `x0+[58.5690,58.5695]` can contain this branch, and there

\[
\boxed{H_xH_{xxx}/A^2<-270.41505.}
\tag{31}
\]

A second check uses (23) on this candidate subcell to eliminate `c`
altogether; its conditional intervals also prove a negative slope and a
positive third derivative. It verifies the operational use of the actual
remainder correlation, not only the accuracy of an evaluated correction.

The earlier Note 19 allowed both stationary signs at a nearby point by
using an arbitrary perturbation within the coarse disk envelope. Its
particular third derivative error payment was about `472.219`; the
corrected payment here is below `0.015347`. Both statements remain valid:
those arbitrary alternatives need not satisfy the stronger source bound.
The former payment was not an optimal consequence of every available
unretained estimate. The parent also permits larger disks away from
cutoff edges, which can reduce an uncorrected derivative payment. The
source-specific result here is the retained signed correction and its
annihilating derivative combination, not a claim that this cell requires
this unique method of proof.

The old coarse first-derivative bound already separates the slope in
(28). Thus this certificate improves genuine stationary-sign resolution
without adding collision-exclusion coverage.

## 8. Next analytic target

The immediate target is to match the correction across a natural-cutoff
change with the entering finite term, using the same physical derivative
coordinates. The analytic profile bounds (6a) already cover all real
phases; what remains at a cutoff edge is the cancellation between the
jumping finite representation and its correction. An uncompensated edge
term would restore the old, larger error scale.

There is an exact starting identity for this matching:

\[
\boxed{C_0(p+2)+C_0(p)
 =\exp\{i\pi(p^2/2+p+3/8)\}.}
\tag{32}
\]

Indeed, the cosine terms in the two numerators cancel, and
`1+exp(2 pi i p)=2 exp(pi i p) cos(pi p)` cancels their denominator.
The identity extends across removable points. Increasing the formal cutoff
by one shifts `p` by two and reverses its parity factor in (4), so (32)
expresses the correction jump as one explicit wave. The required next
estimate must compare that wave with the entering term of `G`, including
its heat and Stirling corrections and physical derivatives. Identity (32)
alone provides no error bound across a cutoff change.

After that matching, use the recentered finite jets and the combinations
(21)--(24) to study the smallest genuine joint first jets. A global
bounded-loss or Hölder-loss theorem still needs a signed estimate for the
residual at their vanishing scale, with the predecessor coverage of
Notes 16--17. Improving a fixed absolute remainder, however far, does
not alone supply that estimate. The [complete Gaussian Hermite readout](21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md)
provides a separate exact-source formulation for that remaining question.

The [internal review](../reviews/10_EXPLICIT_THETA_CORRECTION_AND_STATIONARY_CELL_REVIEW_20261011.md)
records the source and arithmetic audits. These results have not been
integrated into the manuscript.
