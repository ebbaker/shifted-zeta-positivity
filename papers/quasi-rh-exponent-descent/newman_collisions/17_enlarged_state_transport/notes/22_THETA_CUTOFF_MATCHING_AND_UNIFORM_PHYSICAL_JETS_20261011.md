# Theta correction across cutoff changes and uniform physical jets

11 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
worker and is not inferred. The derivation and separate-agent algebraic
checks are internal LLM work, not independent mathematical validation.

This continues [Note 20's explicit theta correction](20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md). The source is the same
[Polymath A+B-C approximation, Corollary 6.4 and Proposition 6.6](https://arxiv.org/html/1904.12438v2#S6.SS3).
No new external theorem is invoked. The result removes Note 20's
fixed-natural-cutoff restriction from its disk and physical-jet bounds.
It does not supply the remaining signed lower bound or a global collision
exclusion theorem.

## 1. Result

One entering finite term matches the corresponding correction jump with
an explicit relative error of order `1/x`. The comparison holds at every
point of the upper complex rectangle, not merely at the real cutoff edge.
After paying this error, a single fixed finite sum and a single holomorphic
exponential correction give a complete disk approximation through the
natural cutoff change. The final residual remains of order `Z/N`; the new
edge payment is smaller, of order `Z/N^2` on a fixed-width crossing patch.

All physical derivatives keep the chosen integer cutoff fixed. The
changing natural cutoff appears only in the pointwise source estimate
before its extra term is matched and paid.

## 2. Notation and profile bounds

Fix `0<t<=1/2`, a real center `X`, and `0<r<=1`, with `x_-=X-r>=200` and
`x_+=X+r`. Put
\[
k=\pi/8,\quad \tau(x)=x/2+\pi t/8,\quad
a(x)=\sqrt{\tau(x)/(2\pi)},\quad
p_n(x)=1-2(a(x)-n).
\]
Let `G_n` be the complete prescribed reflected finite sum through `n`,
`A(X)>0` its symmetric normalizer, and `C_n(t,x)` the formal real correction
from Note 20, defined with the indicated integer `n` even when that integer
is not the natural cutoff at `x`:
\[
C_n(t,x)=(-1)^{n+1}\frac{\sqrt\pi}{4}
e^{-kx-t\pi^2/64}\tau(x)^{3/2}
\left[u(p_n(x))-v(p_n(x))/\tau(x)\right].\tag{1}
\]
Here
\[
C_0(p)=u(p)+iv(p)=
\frac{e^{i\pi(p^2/2+3/8)}-i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)}
\tag{2}
\]
on the real axis, with its removable values understood.

Write `tau_+=tau(x_+)`, `tau_-=tau(x_-)`, and `a_+=a(x_+)`, `a_-=a(x_-)`.
The allowed natural integers are
\[
n_- =\lfloor a_-\rfloor,\qquad n_+=\lfloor a_+\rfloor.
\]
They differ by at most one. In fact
\[
a_+-a_- =\frac{r}{2\pi(a_++a_-)}<\frac1{40},\tag{3}
\]
since `a_->sqrt(200/(4pi))>7/2` and `pi>3`. Choose and freeze either
`N in {n_-,n_+}`. Then throughout the real projection
\[
|p_N(x)|<21/20.\tag{4}
\]
In particular `n_->=3`, so every source-error denominator used below is
positive. Taking the upper cutoff `N=n_+` is always permitted.

Note 20 proves `|C_0|<4` on the complex rectangle
`|Re p|<=5/4`, `|Im p|<=1/4`. A radius `1/5` circle about any real
`|p|<=21/20` stays in that rectangle. Thus Cauchy's estimate supplies
\[
|u|,|v|\le4,\qquad |u'|,|v'|\le20.\tag{5}
\]
These bounds include every formal phase encountered when the cutoff is
frozen through a crossing. If a smaller phase range has separately been
verified, the sharper constants from Note 20 may be substituted.

For later use define
\[
W_\tau=(\tau_+/\tau_-)^{3/2},\qquad
J_* =\frac3{\tau_-}+\frac1{\tau_-^2}
+\frac{20+20/\tau_-}{4\pi a_-}.\tag{6}
\]
This is the slow-amplitude derivative bound obtained from the exact
derivative of `exp(kx) C_N(t,x)` in Note 20, using (5).

## 3. The exact jump is one wave

The explicit quotient (2) gives the entire identity
\[
\boxed{C_0(p+2)+C_0(p)=e^{i\pi(p^2/2+p+3/8)}.}\tag{7}
\]
The identity first holds off the removable points and extends there by
analyticity. If `n_-=m-1`, `n_+=m`, the crossing is at
\[
b=4\pi m^2-\pi t/4,\qquad x_-\le b\le x_+.
\]
Define
\[
\psi(x)=2\pi(a(x)-m)^2-\pi/8.
\]
Since `p_m=p_(m-1)+2`, the correction jump becomes exactly
\[
\boxed{C_m-C_{m-1}=(-1)^{m+1}\frac{\sqrt\pi}{4}
e^{-kx-t\pi^2/64}\tau^{3/2}
\Re\{(1+i/\tau)e^{i\psi}\}.}\tag{8}
\]
There is no unknown error in this identity. The task is to compare it with
the entering physical term of `G`, including its heat and Stirling factors.

## 4. Complete complex matching and its explicit error

Write `z=x+iy`, `0<=y<=r`, `T=x/2`, `tau=T+pi t/8`, and put
`sigma_-= (1-y)/2`, `sigma_+=(1+y)/2`. Define the upper-half-plane finite
channel for a real `sigma` by
\[
\mathcal W_\sigma=
M_0(s)m^{-s}\exp\{t(\alpha(s)-\log m)^2/4\},\qquad
s=\sigma+iT.\tag{9}
\]
The entering reflected term is exactly
\[
G_m(z)-G_{m-1}(z)=\mathcal W_{\sigma_-}
+\overline{\mathcal W_{\sigma_+}}.
\tag{10}
\]
Conjugation in (10) applies to the channel evaluated at the real parameters
`sigma_+,T,t`; it is the pointwise representation of the already holomorphic
reflected finite sum.

Let
\[
U(\tau)=\exp\{-i[\tau\log a-\tau/2-\pi/8]\},\qquad
P(t,x)=e^{t\pi^2/64}|M_0(i\tau)|,
\]
and define the corresponding jump channel
\[
\mathcal Q_\sigma=(-1)^m e^{t\pi^2/64}M_0(i\tau)U(\tau)
e^{i\pi\sigma/4}e^{i\psi}.
\tag{11}
\]
Then `|Q_sigma|=P(t,x)`, and (8), or the original phase formula, gives
\[
\mathcal Q_{\sigma_-}+\overline{\mathcal Q_{\sigma_+}}
=e^{-kiy}[C_m(t,x)-C_{m-1}(t,x)].\tag{12}
\]

Here is an explicit error bound valid simultaneously for the entire upper
rectangle. Set
\[
\begin{gathered}
T_-=x_-/2,\qquad
d=\max\{m-a_-,a_+-m\},\qquad E=d/a_-,\\
\sigma_*=(1+r)/2,\qquad
\Delta=\sqrt{\sigma_*^2+(\pi t/8)^2},\\
D_0=3/(2\tau_-),\quad
D_1=1/(2T_-)+3/(2T_-^2),\quad D_s=D_0+\Delta D_1,
\end{gathered}\tag{13}
\]
\[
\boxed{\begin{split}
\Lambda_{\mathrm{edge}}={}&\sigma_*E+\frac t4E^2
+\frac{2\pi d^3}{3a_-}+\Delta D_0+\frac{\Delta^2D_1}{2}\\
&+\frac t4\{2(E+\pi/4)D_s+D_s^2\}.
\end{split}}\tag{14}
\]
The value `E` may instead be any verified upper bound for
`max_(a in [a_-,a_+]) |log(a/m)|`; its endpoint maximum is often sharper.
Then
\[
\boxed{|G_m(z)-G_{m-1}(z)
-e^{-kiy}(C_m(t,x)-C_{m-1}(t,x))|
\le2P(t,x)(e^{\Lambda_{\mathrm{edge}}}-1).}\tag{15}
\]

**Proof.** Put `delta=s-i tau=sigma-i pi t/8`,
`eta=log(a/m)`, and `gamma=log a+i pi/4`. The exact logarithmic derivative
satisfies
\[
\alpha(i\tau)=\gamma+r_0,\qquad
r_0=\frac1{2i\tau}+\frac1{i\tau-1},\qquad |r_0|\le D_0.
\]
On the straight segment from `i tau` to `s`, the imaginary part is at
least `T_-`, so the exact formula for `alpha'` gives `|alpha'|<=D_1`.
Taylor's formula with an integral remainder therefore yields
\[
\begin{aligned}
m_0(s)&=m_0(i\tau)+\delta\gamma+\varepsilon_M,
&|\varepsilon_M|&\le\Delta D_0+\Delta^2D_1/2,\\
\alpha(s)&=\gamma+\varepsilon_s,
&|\varepsilon_s|&\le D_s.
\end{aligned}\tag{16}
\]
All logarithms use the prescribed branches in the upper half-plane; the
segment crosses no cut. Also `|eta|<=E` by the mean value theorem for the
real logarithm, since `a,m in [a_-,a_+]`.

Substituting (16) into (9), and completing the square involving the heat
term, gives
\[
\begin{split}
\mathcal W_\sigma=\mathcal Q_\sigma\exp\{&\sigma\eta+t\eta^2/4
+i2\pi f(a)+\varepsilon_M\\
&+\tfrac t4[2(\eta+i\pi/4)\varepsilon_s+\varepsilon_s^2]\},
\end{split}\tag{17}
\]
where
\[
f(a)=a^2\log(a/m)-a^2/2-(a-m)^2+m^2/2.\tag{18}
\]
The factors linear in `i t eta` cancel exactly. For the parity in (17),
the raw phase difference differs from `2pi f(a)` by `-pi m(m+1)`, an
integer multiple of `2pi`; the exponential identity is exact.

One has `f(m)=f'(m)=f''(m)=0` and `f'''(a)=2/a`. Hence
\[
|f(a)|\le d^3/(3a_-).
\]
The exponent in (17) has modulus at most (14). The elementary inequality
`|exp(w)-1|<=exp(|w|)-1` proves
`|W_sigma-Q_sigma|<=P(exp(Lambda_edge)-1)`. Add the two errors in
(10)--(12) to obtain (15). This is a bound at every `x+iy` in the
rectangle and pays both reflected channels. QED.

For fixed `r<=1`, `t<=1/2`, the fact that `b` belongs to the real projection
gives `d=O(r/m)` and `E=O(r/m^2)`. Thus
\[
\Lambda_{\mathrm{edge}}=O((1+r+r^2)/m^2),\tag{19}
\]
with all constants already explicit in (13)--(14). In particular an
uncompensated edge mass of order `P` does not reappear.

## 5. One complete disk theorem through the crossing

Use the following positive majorants, which coincide with Note 20 except
that the source cutoffs are bounded by their two extrema:
\[
\begin{gathered}
q_\pm=x_\pm/(4\pi),\quad V=x_-/2,\quad
S=\tfrac12\sqrt{x_+^2+(1+r)^2},\\
\alpha_- =\tfrac12\log q_- -V^{-2},\quad
A_* =\frac3{2V}+\frac12\sqrt{\log^2(S/(2\pi))+\pi^2/4},\\
D_* =\frac3{2V^2}+\frac1{2V},\quad
L_*=A_*(1+tD_*/2),\quad K=e^{rL_*/2},\\
V_j=j^{-1/2}e^{t(\log^2j/4-\alpha_-\log j/2)},\quad
\ell_j=\max\{|\log(q_-/j^2)|,|\log(q_+/j^2)|\},\\
\kappa_* =tr/[2(x_--6)],\quad
U_j=\exp\frac{t^2\ell_j^2/16+0.626}{x_--6.66}-1,\\
E_{AB}=\sum_{j\le n_+}(1+n_+^{\kappa_*}j^r)V_jU_j,
\end{gathered}\tag{20}
\]
\[
\begin{aligned}
Z={}&q_-^{-1/4}\exp\left\{-t\log^2q_-/16
+\frac{3\sqrt{\log^2q_++\pi^2/4}+3.58}{x_--8.52}\right\},\\
B_C={}&\frac{1.24(3^r+3^{-r})}{n_--0.125}+\frac{6.92}{x_--12}.
\end{aligned}\tag{21}
\]
If `n_-=n_+`, set `B_edge=0`. If `n_+=n_-+1`, take
\[
B_{\mathrm{edge}}=2(e^{\Lambda_{\mathrm{edge}}}-1),
\tag{22}
\]
with `m=n_+` in (13)--(14). Finally set
\[
\boxed{\eta_{\mathrm{cross}}
=K\{E_{AB}+Z[B_C+B_{\mathrm{edge}}+2rW_\tau J_*]\}.}\tag{23}
\]

**Theorem.** For either frozen `N in {n_-,n_+}`,
\[
\boxed{\sup_{|z-X|\le r}
\frac{|H_t(z)-G_N(z)+C_N(t,X)e^{-k(z-X)}|}{A_t(X)}
\le\eta_{\mathrm{cross}}.}\tag{24}
\]

**Proof.** On the upper half-disk, apply the source theorem at its actual
natural integer `n(x)`. Its error, divided by `|M_t(s_+(z))|`, is at most
`E_AB+Z B_C`, since (20) uses the larger cutoff in every positive sum
and multiplicative upper bound, while (21) uses the smaller cutoff in the
positive reciprocal error bound. Note 20's direct segment argument gives
`|M_t(s_+(z))|/A_t(X)<=K`; its prefactor estimate gives
`P(t,x)/|M_t(s_+(z))|<=Z`.

If the actual integer differs from `N`, their difference is exactly one
entering reflected term and one correction jump. Equation (15) pays their
entire complex mismatch by `K Z B_edge` after division by `A_t(X)`.
If they agree there is no such cost.

It remains to replace the formal printed correction
`exp(-kiy) C_N(t,x)` by the fixed holomorphic exponential
`C_N(t,X)exp(-k(z-X))`. The derivative of
`D_N(t,x)=exp(kx)C_N(t,x)` and (5) give the bound `J_*` in (6).
The real fundamental theorem of calculus, followed by the same prefactor
and segment estimates, pays this difference by
`2 K Z r W_tau J_*`, exactly as in Note 20. Combining the three costs
gives (24) on the upper half-disk. The function in (24) is holomorphic and
has real symmetry, so reflection gives the lower half. QED.

**A family of centers and times.** The same argument allows `x_-` and
`x_+` to enclose all real disk projections of a family of centers, rather
than to equal one center plus or minus `r`. In this version, verify
`n_+-n_-<=1` and the range of the frozen formal profile separately on the
whole enclosing rectangle. Freeze either of these global integers, even
on an individual disk whose own natural integer is constant and different.
The pointwise comparison (15) still pays at most one entering term; the
normalizer segment has length at most `r/2` and the correction comparison
still has `|x-X|<=r`. Thus the factors `K` and `2r` are unchanged.

For a time interval `[epsilon,t_+]`, use the joint extrema of `tau` and
`a`, use `t_+` in positive increasing error factors and `epsilon` in the
negative time exponent of `Z`. In `V_j`, use the maximum of the two endpoint
time exponents, since their coefficient may have either sign. All other
bounds follow by the same positive majorants. The numerical certificate
below implements these interval choices explicitly. This extension does
not follow merely by differentiating or switching individual certificates.

## 6. Physical derivatives, exact correlations, and remaining scope

With `c_N=C_N(t,X)/A_t(X)` and `f_j=G_N^(j)(X)/A_t(X)`, Cauchy's formula
now proves across every natural cutoff crossing
\[
\boxed{\frac{H_t^{(j)}(X)}{A_t(X)}
=f_j-c_N(-k)^j+\delta_j,\qquad
|\delta_j|\le j!r^{-j}\eta_{\mathrm{cross}}.}\tag{25}
\]
The chosen `N` is frozen throughout the derivative calculation. Thus
Note 20's demodulated bounds remain valid with `eta_cross`, including
\[
\frac{|(\partial_x+k)(H_t-G_N)(X)|}{A_t(X)}
\le\eta_{\mathrm{cross}}(r^{-1}+k),\tag{26}
\]
and its division-free collision test based on `G_N'+kG_N`. The stationary
amplitude elimination and higher powers of `partial_x+k` carry over
unchanged. There is no differentiation of a jumping finite cutoff and no
use of Cauchy's formula on the printed nonholomorphic correction.

On the shrinking sector `L=log(X/(4 pi))`, `t=kappa/L`,
`1<=kappa<=3/2`, and `r=1/L`, the parent sum estimates still give
`E_AB=O(Z/N)`. In (23), `B_C=O(1/N)`, `B_edge=O(1/N^2)`, and
`r J_*=O(1/(LN))`. Consequently the full matched residual obeys
\[
\eta_{\mathrm{cross}}=O(Z/N),\qquad
|\delta_j|=O_j(ZL^j/N),\tag{27}
\]
uniformly through natural cutoff changes. The constants are supplied by
(6), (13)--(14), and (20)--(23), rather than by differentiating an
uncontrolled asymptotic statement.

This removes a genuine coverage obstruction from the improved remainder
interface. It does not turn its absolute residual into a loss vanishing
with `H^2+H_x^2`; the complete signed finite response, predecessor coverage,
and other global candidate regions still require proof.

The piecewise expression obtained by changing `G_n` and `C_n` together at
the natural edge is not asserted to be exactly continuous. The matching
error in (15) is a paid small jump. In particular it would be invalid to
differentiate that piecewise leading approximation. The holomorphic object
used for every derivative in (25) is instead the single frozen expression
`G_N(z)-C_N(t,X)exp(-k(z-X))` throughout its disk. A direct entering-term
numerical check may detect a nonzero small jump without contradicting any
of the statements above.

## 7. Outward certificate on a rectangle containing the moving cutoff

The [checker](../numerics/check_theta_cutoff_matching.py) and
[small record](../numerics/THETA_CUTOFF_MATCHING_RECORD_20261011.json)
verify the family version of (24) with
\[
m=22066,\quad t_0=\frac1{2\log m},\quad
 t\in[t_0,t_0+10^{-8}],\quad
 X\in4\pi m^2+[-0.1,0.1],\quad r=0.05.
\]
The reference cutoff is frozen at `N=m` for every disk. The enclosing
real rectangle is `4 pi m^2+[-0.15,0.15]`. Its natural integers are
`22065` and `22066`, and the moving edge
`b(t)=4 pi m^2-pi t/4` lies inside the center interval at every time.
The directed phase enclosure is
\[
0.99999931745395317<p_m<1.00000039935561586.
\]
Consequently Note 20's sharper local profile constants
`|u|<=1`, `|v|<=2`, `|u'|<=4`, `|v'|<=6` apply. Here (6) is replaced by
\[
J_{\rm local}=\frac3{4\tau_-}+\frac1{2\tau_-^2}
 +\frac{4+6/\tau_-}{4\pi a_-}.
\]
The script uses 60-digit directed Decimal arithmetic, explicit elementary
function enclosures, and the two hash-checked interval modules from
investigation 13. All numbers in the following table are rounded upward.
The source theorem remains an imported analytic input.

| Quantity | Certified upper bound |
| --- | ---: |
| Complex matching exponent `Lambda_edge` | `2.995742e-10` |
| Source error `K(E_AB+Z B_C)` | `3.099443e-7` |
| Added cutoff payment `K Z B_edge` | `1.484686e-12` |
| Holomorphic exponential comparison | `3.574655e-9` |
| Complete disk residual `eta_cross` | `3.135204e-7` |
| Physical derivative residual, order 1 | `6.270408e-6` |
| Physical derivative residual, order 2 | `2.50816294e-4` |
| Physical derivative residual, order 3 | `0.015048978` |
| First annihilating combination, (26) | `6.393527e-6` |

The derivatives here use the constant center normalizer `A_t(X)` directly.
Note 20's retained cell checker instead divides by an analytic varying
normalizer before Cauchy and restores its derivatives. The difference
between its third-derivative payment and this table therefore also reflects
the normalization convention; it is not an improvement caused by crossing
the cutoff. The present rectangle has different spatial parameters and
makes no new stationary-sign or first-jet-separation claim.

At the exact real edge and time `t_0`, a separate evaluation of the actual
single entering finite term and correction jump gives
\[
\begin{aligned}
(G_m-G_{m-1})/A&\simeq-0.00356301854620869822412,\\
(C_m-C_{m-1})/A&\simeq-0.00356301854660070192558,\\
[(G_m-G_{m-1})-(C_m-C_{m-1})]/A
&\in[3.92003701457415,3.92003701457417]\,10^{-13}.
\end{aligned}
\]
The last displayed interval is outward; the two preceding lines are
rounded descriptions only. This confirms a nonzero small jump, well inside
the complete complex matching payment. The point check is not used to infer
a complex-disk bound. A separate internal reviewer also evaluated the
unrearranged logarithmic carrier and large phase, independently confirming
the stable phase reduction and the positive mismatch.

Replay from the investigation's `numerics/` directory without changing the
saved record:

```sh
python3 check_theta_cutoff_matching.py --record /tmp/THETA_CUTOFF_MATCHING_RECORD_20261011.json
```

The optional `--interval-source-dir` supports staged replay; the default is
relative to the installed source. The record includes dependency hashes,
the checker hash, all directed endpoints, parameters and scope limitations.
See the [internal review](../reviews/11_THETA_CUTOFF_MATCHING_REVIEW_20261011.md).

## 8. The next target: signed control on the remaining candidate set

The correction and its cutoff matching now define a uniform local
first-jet candidate test. With the notation of (25), write
\[
\widetilde f_0=f_0-c_N,\qquad
\widetilde f_1=f_1+kc_N,\qquad \eta=\eta_{\rm cross}>0.
\]
At a genuine joint zero, the real-symmetric Schur function
\[
g(w)=\frac{H_t(X+rw)-G_N(X+rw)
 +C_N(t,X)e^{-krw}}{A_t(X)\eta}
\]
has modulus at most one, with
`g(0)=-tilde f_0/eta`, `g'(0)=-r tilde f_1/eta`. The Schwarz--Pick
coefficient inequality therefore gives the necessary condition
\[
\boxed{\left(\frac{\widetilde f_0}{\eta}\right)^2
 +\left|\frac{r\widetilde f_1}{\eta}\right|\le1.}\tag{28}
\]
This is [Note 18's](18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md)
exact first-jet geometry applied to the smaller, cutoff-uniform remainder.
Violation excludes a joint zero on that disk center; satisfaction is only
a candidate condition. On the shrinking sector, its physical widths are
`O(Z/N)` and `O(ZL/N)`. No sign can be inferred merely from membership.

The next substantive target is a signed estimate for the complete theta
response on this candidate neighborhood and its required predecessor
stationary branches. In particular the targets of
[Note 16](16_NEXT_STEPS_AND_BOUNDED_LOSS_COLLISION_CRITERION_20261010.md) remain
\[
H_x=0\ \Longrightarrow\ HH_{xx}\le B_0(H^2+H_x^2),\qquad
H_{xx}=0\ \Longrightarrow\ H_xH_{xxx}\le B_1(H^2+H_x^2),
\]
with `B_0,B_1` locally bounded up to a candidate collision, or the precise
multiplicity-budget Hölder alternative of
[Note 17](17_MULTIPLICITY_BUDGETS_AND_HOLDER_LOSS_CRITERION_20261010.md).
The exact complete Gaussian moments in
[Note 21](21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md) provide a
source representation for this signed question. Those identities do not
already prove the estimate.

A further absolute error reduction can shrink (28), but by itself cannot
supply a loss that vanishes with the genuine joint first jet. The next
investigation should retain the actual signed residual or establish actual
first-jet separation on a declared family; another collection of bounded
sign calibrations does not discharge the global predecessor and parameter
coverage obligations.

## Appendix: a less sharp independent check at the real edge

At the real edge `b`, take the source approximation's limits from the two
sides. Continuity of the same genuine `H` cancels it, leaving the mismatch
between the entering finite term and the correction jump bounded by the
sum of the two complete source errors, of order `A(b)Z/m`. This is not a
hypothetical favorable choice of an unknown theta remainder. It confirms
that the source estimates are compatible at the edge, but is weaker than
(15) and does not by itself supply a complex-disk derivative theorem.
