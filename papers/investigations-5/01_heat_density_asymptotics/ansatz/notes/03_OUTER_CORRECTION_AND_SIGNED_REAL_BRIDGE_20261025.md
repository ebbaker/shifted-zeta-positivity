# Outer correction and a bounded signed-time real-axis bridge

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from this turn's session metadata. Ansatz chat0001, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Status: proved in-note from named classical inputs; same-model internal
assessment only.** Return to [HDA-A01-AN01 r1][packet]. The compact outer
calibration is completed, including its first correction. A corrected
finite sum gives a uniform **real-axis field** comparison through zero
on `|t| log(X/(4pi))<=8`. The full buffered signed-time field/jet theorem
is **not proved**. Section 8 identifies the exact missing estimate and
a failed way of obtaining it. Constants are finite analytical constants;
no numerical onset is certified. No numerical, symbolic, field-sampling,
exact-arithmetic or interval research was executed.

The [opening input manifest][inputs] pins the input versions. The
[assessment][review] records acceptance and limitations. Parent Notes27--31,
60 and Summary62 remain inputs with their existing review qualifications.
Their all-time construction and physical observable claims are neither
reproved nor enlarged here.

## 1. Contract, classification and buffers

Keep exactly

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8,
\]
\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),
\qquad \alpha=M'/M,\qquad s(z)=(1+iz)/2.
\tag{CB1}
\]

The physical `q=epsilon_g^2`, fixed `K=k_ell k_h`, potential offsets,
actual signed covariance and joining/regulator defects are unchanged.
There is no physical-observable transfer claim in this note.

This is an approximation task under [avoid/01][a01], rather than an
RH-equivalent criterion. Read the [result index][results], especially
[11][r11] and [12][controls], and the [avoid index][avoid], especially
[02][a02], [05][a05], [07][a07], [08][a08], [12][a12], [16][a16]
and [19][a19]. The control screen in Section 9 names the failed premises.

For fixed positive averaging widths `ell,h`, target `|y|<=1`, reserve

\[
\Omega_X=\{|\Re z-X|\le\ell+2,\ |\Im z|\le1+h+2\},
\quad
\Omega_X^+=\{|\Re z-X|\le\ell+3,\ |\Im z|\le1+h+3\}.
\tag{CB2}
\]

These include the averaging supports, a fixed collar margin, and an
additional analytic margin. No root collar is assumed or divided by
in this note. Part A holds on these full fixed buffers. Part B below
only proves real-axis fields, uniformly on fixed horizontal windows;
it does not pay the transverse portion of CB2.

On the right tail use `z`, not `|Re z|`, as the holomorphic coordinate:

\[
L=\Log(z/(4\pi)),\quad b_\pm=L/2\pm i\pi/4,
\quad C_\pm=A_o(t,z)e^{\pm i\Theta_o(t,z)}/2,
\quad E_o=|C_+|+|C_-|.
\tag{CB3}
\]

The powers and logarithms use the branch continued from positive real
height. The lower arm is reflected conjugately. On the real axis
`E_o=A_o>0`; off it the envelope includes the growth
`exp(|y| log X/4)` of the dominant arm. A real-axis amplitude alone
would not be an adequate strip envelope. Evenness supplies the left
tail after the right-tail estimates have been proved.

## 2. Exact normalization and first gamma coefficient

Sectorial log-gamma asymptotics, with unwrapped log Gamma and principal
`Log w` inside its sector, give

\[
\begin{split}
\log M(s(z))={}&\log\frac{\pi^{1/4}z^{7/4}}{32}-\frac{\pi z}{8}
 +i\left\{\frac z4(L-1)+\frac{7\pi}{8}\right\}
 +\frac{i}{24z}+O_B(X^{-2}),\\
\alpha(s(z))={}&b_+-\frac{7i}{2z}+O_B(X^{-2}),\qquad
\alpha'(s(z))=-\frac{i}{z}+O_B(X^{-2}).
\end{split}
\tag{CB4}
\]

Here and below `X` is the large real chart center and `B` is a fixed
strip bound. These expansions are holomorphic on a larger sector;
their differentiated remainders are obtained by Cauchy's formula there.
They are not differentiated real-axis asymptotic allowances.

For completeness, set `q_0=iz/2` and write `s=q_0+1/2`. Stirling at
`s/2` gives

\[
\log M(s)=\frac s2[\Log(s/(2\pi))-1]
 +\frac32\Log s+\log(\sqrt\pi/8)
 +\Log(1-1/s)+\frac1{6s}+O(s^{-3}).
\]

Expanding about `q_0`, the coefficient of `1/q_0` is
`1/16+3/4-1+1/6=-1/48`, hence `i/(24z)`. The logarithm of the
polynomial `s(s-1)` contributes the phase `pi`; the gamma part gives
`-pi/8`. This fixes the unwrapped constant `7pi/8`, without reducing
it modulo `2pi`.

Thus the opening `A_o,Theta_o` are correct:

\[
A_o=\frac{\pi^{1/4}}{16}X^{7/4}
 e^{-\pi X/8+t(\ell_X^2-\pi^2/4)/16},
\quad
\Theta_o=\frac X4(\ell_X-1)+\frac{\pi t\ell_X}{16}+\frac{7\pi}{8},
\quad \ell_X=\log(X/(4\pi)).
\tag{CB5}
\]

`A_o` is the full cosine amplitude; one arm has half of it. Zeta height
is `X/2`. The first gamma correction on the real axis is a phase
correction; there is no real `1/X` correction in the zero-time modulus.
Primary input: [DLMF 5.11.1--5.11.2 and sectorial bounds][gamma].

## 3. The actual heat carrier, not only its linearization

Work on `32<=t<=33`. Put `B=1+h+3` and choose the **fixed** endpoint
`V=(B+3)/2`. For `w=s(z),1-s(z)` on CB2, `Re(w+v)>=2` for `v>=V`.
Define the holomorphic arm

\[
J_V(t,w)=\frac1{\sqrt{\pi t}}\int_V^\infty e^{-v^2/t}M(w+v)\,dv.
\tag{CB6}
\]

Split the exact xi heat integral at `-V,V` and reflect the left piece
using `xi(w)=xi(1-w)`. This retains two arms CB6, the full bounded
middle, and the full ordinary Dirichlet-series remainders on both tails.
The fixed endpoints are essential for holomorphy; an endpoint depending
on `Re w` cannot be differentiated as an analytic definition.

On `V<=v<=X^(1/3)`, Taylor's formula gives

\[
\log M(w+v)=\log M(w)+\alpha v+\tfrac12\alpha'v^2
 +O_B(v^3/X^2).
\]

Expand the quadratic exponential once. After completing the square,
the complex tilted Gaussian moments are

\[
\langle v^2\rangle=t/2+t^2\alpha^2/4,
\qquad \langle |v|^k\rangle_{\rm abs}\le C_{B,k}(1+\log^kX).
\]

The absolute-to-complex Gaussian loss `exp(t(Im alpha)^2/4)` is bounded
on this compact interval. The quadratic-square and cubic remainders
are at most `C_B(1+log^4 X)/X^2` after carrier division. Therefore

\[
\log J_V=\log M+\frac t4\alpha^2+
 \frac t4\alpha'+\frac{t^2}{8}\alpha^2\alpha'
 +O_B((1+\log^4X)/X^2).
\tag{CB7}
\]

The logarithm in CB7 is chosen by the ratio to
`M exp(t alpha^2/4)`, which tends to one. This proves the manuscript's
formal checkpoint. In the quadratic Gaussian formula the determinant
factor is `(1-t alpha'/2)^(-1/2)` and its log begins `t alpha'/4`;
the displaced mean gives `t^2 alpha^2 alpha'/8`.

All other terms are paid separately:

| Contribution after division by its nonzero carrier | Bound on `[32,33]` |
| --- | --- |
| Full arithmetic remainder, using `|zeta(w+v)-1|<=3*2^(-Re(w+v))` | `C_B X^(-t log(2)/4)` |
| Bounded middle xi integral and omitted lower linearized Gaussian tail | `C_B exp(-2 ell_X^2+C_B(1+ell_X))` |
| Both infinite right tails, retaining the gamma height exponential | `C_B exp(-c_B X^(2/3))` |
| Local gamma Taylor/exponential remainder | `C_B(1+log^4 X)/X^2` |

The ray estimate used for the third row is
`log(|M(w+v)|/|M(w)|)<=C_B v+(v/2)log(X+v)`. It is dominated by
the Gaussian beyond `X^(1/3)`. The middle uses the bounded-strip bound
`|xi/8|<=C_B X^(B+6) exp(-pi X/8)`. The fixed endpoints here allow
real parts as large as `B+2`; the fourth power sufficient for the
smaller middle strip in parent Note27 cannot be used for arbitrary
buffers. This only changes the linear-log coefficient in the second
row. None of these pieces is replaced by a height-independent source moment before
carrier division.

Since `8 log 2>2`, arithmetic is below the new `X^-2` allowance here.
This ordering is specific to this interval and cannot be carried to
zero time. It establishes a correction to the **true H**, rather than
only a correction to an auxiliary gamma arm, on `[32,33]`.

## 4. Corrected cosine, jets, time derivative and residual

Set

\[
D_\pm=\frac{\pm i}{z}\left\{\frac1{24}-\frac t4-
 \frac{7t}{4}b_\pm-\frac{t^2}{8}b_\pm^2\right\},
\quad F_1=\sum_\pm C_\pm(1+D_\pm),\quad F_o=C_++C_-.
\tag{CB8}
\]

Substitution of CB4 in CB7 proves

\[
|\partial_z^j(H-F_o)|\le C_jE_o\frac{1+\log^{2+j}X}{X},
\qquad
|\partial_z^j(H-F_1)|\le C_jE_o\frac{1+\log^{4+j}X}{X^2},
\quad 0\le j\le3.
\tag{CB9}
\]

For the jets use disks of radius `1/[8(1+log X)]`, lying within the
extra margin in CB2. Each arm's logarithmic derivative is `O(log X)`,
so its modulus changes by a bounded factor on these disks. Fixed-radius
Cauchy bounds would lose powers of height and do not prove CB9.

On the real axis CB8 can equivalently be displayed as

\[
H(t,X)=A_o e^{a_1/X}\cos(\Theta_o+p_1/X)
 +A_o O((1+\ell_X^4)/X^2),
\tag{CB10}
\]
\[
a_1=\frac{7\pi t}{16}+\frac{\pi t^2\ell_X}{32},\qquad
p_1=\frac1{24}-\frac t4-\frac{7t\ell_X}{8}
 -\frac{t^2\ell_X^2}{32}+\frac{\pi^2t^2}{128}.
\]

This exponential/trigonometric rewrite differs from CB8 only within its
stated remainder. No division by a vanishing cosine occurs.

There is also an exact residual formula. With

\[
Q(b)=21/16+t/8+5tb/8+t^2b^2/16,
\]
\[
R_\pm:=\frac{(\partial_t+\partial_{zz})C_\pm}{C_\pm}
 =\frac{\pm i(1+7b_\pm+t b_\pm^2)}{4z}
  +\frac{Q(b_\pm)}{z^2}.
\tag{CB11}
\]

This follows by differentiating the displayed elementary logarithm:
`(log C)_z=+-i b/2+(7/4+tb/4)/z` and
`(log C)_t=b^2/4`. Its leading squares cancel. For the corrected arm
the exact residual divided by `C_\pm` is

\[
(1+D_\pm)R_\pm+(D_\pm)_t+
2(\log C_\pm)_z(D_\pm)_z+(D_\pm)_{zz}.
\tag{CB12}
\]

The `1/z` term in CB11 is exactly cancelled by `(D_\pm)_t`. Thus
`|(partial_t+partial_zz)F_o|<=C E_o(1+log^2X)/X` and the residual of
`F_1` is at most `C E_o(1+log^4X)/X^2`. Using the exact heat equation,

\[
\partial_t(H-F)=-(H-F)_{zz}-(\partial_t+\partial_{zz})F,
\]

CB9 and CB11--12 directly prove

\[
|\partial_t(H-F_o)|\le C E_o(1+\log^4X)/X,\qquad
|\partial_t(H-F_1)|\le C E_o(1+\log^6X)/X^2.
\tag{CB13}
\]

This is an identity plus already proved spatial estimates, not
differentiation of a big-O allowance. Direct differentiation of CB6
by the Gaussian kernel factor `v^2/t^2-1/(2t)` gives the same bounds.
A small residual by itself is not used to propagate field error.

## 5. Zero-time correction and analytic handling of the cutoff

For real `u>0`, let

\[
a(u)=\sqrt{u/(4\pi)},\quad m=\lfloor a(u)\rfloor,\quad p=a-m,
\quad G(u)=|M(s(u))|,
\]
\[
\mathcal C(p)=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)}.
\tag{CB14}
\]

All apparent poles of this quotient are removable: at
`p=(2k+1)/4` the numerator also has a simple zero (its phase is an
odd half-integer multiple of `pi`). In particular `C(1/4)=C(3/4)=1/2`.
The entire continued quotient obeys

\[
\mathcal C(p)+\mathcal C(p-1)
 =2\cos(2\pi(p-1)^2-\pi/8).
\tag{CB15}
\]

The real-axis Riemann--Siegel formula with its first correction gives

\[
H(0,u)=S_m(u)+(-1)^mG(u)a(u)^{-1/2}\mathcal C(a(u)-m)
 +O(G(u)u^{-3/4}),
\tag{CB16}
\]
\[
S_N(z)=\sum_{n\le N}\{M(s(z))n^{-s(z)}+
                         M(1-s(z))n^{-(1-s(z))}\}.
\]

The sign in CB16 follows from `H(0,u)=-G(u)Z(u/2)` and
`arg M=theta(u/2)+pi`. The conventional Riemann--Siegel correction
has sign `(-1)^(m-1)` before multiplication by `-G`.
The imported statement is [DLMF 25.10.3--25.10.4][rs], on the real
axis, with its uniform removable-singularity interpretation.

For a fixed real center `X`, choose `N=floor a(X)` once on the chart.
Take the analytic square root `G(z)=[M(s(z))M(1-s(z))]^(1/2)` positive
on its real segment. Define

\[
\mathcal R_N(z)=(-1)^N G(z)a(z)^{-1/2}\mathcal C(a(z)-N).
\tag{CB17}
\]

This is holomorphic on the whole fixed far-height chart, including
cutoff crossings. It is not obtained by differentiating a floor.
For any fixed horizontal radius `R`, the interval `|u-X|<=R` meets
at most one threshold `4pi n^2` once `X` is sufficiently large.
CB15 shows that the difference between the two adjacent correction
formulas exactly has the leading size and phase of the added mode.
More explicitly, at `a=n+d`,

\[
\arg M(s(u))-(u/2)\log n
 =-\pi n^2+7\pi/8+2\pi d^2+O_R(X^{-1}),
\quad n^{-1/2}=a^{-1/2}(1+O_R(X^{-1})).
\]

Here `|d|=O_R(X^-1/2)` when the threshold meets the fixed interval.
Combining this with CB15 proves

\[
\mathcal R_N(u)=(-1)^m G(u)a^{-1/2}\mathcal C(a-m)
                  +S_m(u)-S_N(u)+O_R(G(u)X^{-5/4}).
\]

Consequently, **uniformly across the cutoff**,

\[
H(0,u)=S_N(u)+\mathcal R_N(u)+E_N(u),\qquad
|E_N(u)|\le C_R G(u)X^{-3/4},\quad |u-X|\le R.
\tag{CB18}
\]

CB18 is proved for real values. The analytic definition CB17 alone
does not extend the remainder estimate off the axis.

## 6. Negative-time bridge: window, population and tails

Write `t=-T`, `tau=T ell_X`, and assume

\[
0<T\ell_X\le8,\qquad \ell_X\ge16.
\tag{CB19}
\]

The exact starting identity is

\[
H(-T,X)=\frac1{\sqrt{4\pi T}}\int_\mathbb R
 e^{-v^2/(4T)}H(0,X-v)\,dv.
\tag{CB20}
\]

It is derived by source integration, so it is not a continuation of
a positive-time error theorem. Use the fixed central window `|v|<=16`
and apply CB18 on the slightly larger real chart. The remainder there
has Gaussian average at most `C G(X)X^-3/4`: indeed
`G(X-v)/G(X)<=C exp(pi v/8)` on that window, and its Gaussian average
is bounded because `T<=1/2`.

For each of the `N` gamma modes put
`h_n(z)=M(s(z))n^(-s(z))`. Its logarithmic spatial derivative is
`beta_n=(i/2)(alpha(s)-log n)` and its second log derivative is
`O(X^-1)`, uniformly for **all** `n<=N`. Hence

\[
h_n(X-v)=h_n(X)e^{-\beta_n v}(1+O(v^2/X)),
\]

where `Re beta_n` is bounded independently of the mode. Exact Gaussian
completion of the linear part yields

\[
M(s_X)n^{-s_X}\exp\{-T(\alpha(s_X)-\log n)^2/4\}.
\tag{CB21}
\]

The absolute Taylor errors over the entire mode population are bounded
by `C T G(X)X^-1 sum(n^-1/2)<=C T G(X)X^-3/4`. This is a uniform
population estimate, rather than a fixed-mode limit.

The retained correction has a short leading heat evolution. On the
real window, `G(X-v)=G(X)e^(pi v/8)(1+O(|v|/X))`, while
`a(X-v)-a(X)=O(|v|/sqrt X)` and `C'` is bounded on the compact
fractional-cutoff chart. Thus replacing its convolution by

\[
e^{\pi^2T/64}\mathcal R_N(X)
\tag{CB22}
\]

costs at most `C G(X)X^-3/4(sqrt T+T)`. This keeps the leading
Riemann--Siegel correction as part of the field.

The tails in CB20 are also paid. On `16<|v|<=X/2`, bounded-strip
Stirling and elementary zeta growth give
`|H(0,X-v)|<=C X^4 e^(-pi(X-v)/8)`. Since `T<=1/2`,
`-v^2/(4T)+(pi/8)|v|<=-v^2/(8T)` on this range. After division by
`A_o(-T,X)`, this piece is at most

\[
C X^{9/4}e^{\tau\ell_X/16}e^{-16^2/(8T)}
 \le C X^{-5/4}.
\tag{CB23}
\]

The normalized Gaussian tail prefactor is bounded. For `|v|>X/2`,
use the genuine global real-axis source bound
`|H(0,u)|<=int_0^infinity |Phi|`, giving a normalized bound
`C X^(-7/4) exp(pi X/8+tau ell_X/16-X^2/(16T))`, smaller than every
inverse height power here. The artificial linear Gaussian tails in
CB21--22 obey the same central-window tail estimates, with the finite
mode population included. Applying a global source bound already at
`|v|=16` would fail at the exponentially small carrier scale; CB23
retains the height exponential until `|v|=X/2`.

Finally replace CB21 by the elementary arithmetic modes of the handoff.
CB4 changes each exponential by `O((1+tau)/X)` relative to that
mode's nonzero envelope. For negative time,

\[
\sum_{n\le N}w_n(-T,X)
 \le 2\sqrt N\,e^{T\ell_X^2/16}
 \le C X^{1/4}e^{\tau\ell_X/16}.
\tag{CB24}
\]

Therefore all retained-mode replacement, source-remainder, correction
freezing and tail errors are bounded by

\[
C A_o(-T,X)X^{-3/4}e^{\tau\ell_X/16}
 \le C A_o(-T,X)X^{-1/4}.
\tag{CB25}
\]

In contrast, starting with only the bare Riemann--Siegel error would
leave `A_o X^-1/4 exp(tau ell_X/16)`, which permits growth for
`tau>4`. This is a failure of that error budget, not a lower bound
for the actual error and not a no-go theorem for negative time.

## 7. A signed-time real-axis statement

On each fixed real chart use the same fixed `N=floor a(X)` and CB17.
For real `u` in its bounded horizontal target window define

\[
F_N(t,u)=A_o(t,u)\sum_{n\le N}w_n(t,u)
 \cos\left(\Theta_o(t,u)-(u/2+\pi t/8)\log n\right)
 +e^{-\pi^2t/64}\mathcal R_N(u).
\tag{CB26}
\]

The functions in CB26 have a holomorphic definition on a fixed chart;
the following error theorem is only for real values. For all sufficiently
large `X`, uniformly for real `u` in any fixed horizontal target window
and `|t| log(u/(4pi))<=8`,

\[
\boxed{|H(t,u)-F_N(t,u)|\le C A_o(t,u)u^{-1/4}.}
\tag{CB27}
\]

Negative times follow from CB19--25, and zero follows from CB18 plus
CB4 and the full mode count. On the positive side take
`0<t<=8/log(u/(4pi))<=1/2`, `y=0`, `u>=200` in Polymath Theorem1.3.
Its equations (23)--(24) give, after its single-arm normalization,
`e_A+e_B<=C u^-1 sum w_n<=C u^-3/4` and
`e_C,0<=C u^-1/4 exp(-t ell_u^2/16)`. The factor in (23) is
`O((1+(t ell_u)^2)/u)` throughout this work window. Replacing its
Stirling arms and logarithmic derivatives by the elementary CB5 modes
costs `C u^-3/4`, since `sum w_n<=C u^1/4` at positive time.
Its cutoff `floor sqrt(u/(4pi)+t/16)` and the chart cutoff differ
by at most one term for sufficiently large `X`; that term is at most
`C A_o u^-1/4`. The added correction in CB26 has size at most the
same allowance on this positive side. Thus CB27 follows without
continuing a positive-time theorem to negative time.

The positive-side allowance does not assert that CB17 is Polymath's
full evolved `C_t`, or that it has that theorem's sharper corrected
remainder. It is a common short correction within CB27's coarser
accuracy. The negative side requires it for the stated budget.

The correction itself can be as large as `A_o X^1/4` near the negative
edge `T ell_X=8`. It is retained, not assigned the size of the error.
No bound on a fixed set of modes replaces CB24. No universal critical
`tau` or limiting one-variable profile is inferred.

### Constants and onset status

Here is the onset ledger, rather than an unsupported numerical `X0`.
For the real bridge choose a finite `X0(R)` with
`X0>=max(64,4pi exp(16),2R)` and the classical real RS onset on
`[X/2,3X/2]`, and require
`sqrt((X+R)/(4pi))-sqrt((X-R)/(4pi))<1/2` for all `X>=X0`,
with the additional positive cutoff displacement
`sqrt((X+R)/(4pi)+1/32)-sqrt((X+R)/(4pi))<1/4`.
Increase it for the finite sectorial gamma constants in CB4 and the
Taylor smallness gates. Every requirement is eventual and finite;
the imported RS and sectorial constants have not been evaluated.

For the positive outer theorem also require `X>=2(ell+3)+8(B+V+1)`,
`C_B X^-1/3<=1/2`, and
`132[C_B+(1/2)log(2X)]<=X^(1/3)` for the local and infinite-tail
arguments; enlarge the onset until the middle Gaussian bound is at
most `X^-2`. These explicit inequalities explain its dependence on
the fixed buffers. They do not constitute an instantiated onset.
**A full-strip signed-time onset is not supplied**, because the estimate
in the next section has not been proved. This part of the packet's
larger acceptance contract remains open.

## 8. Precise unpaid estimate and failed complex route

For the analytic fixed-cutoff error

\[
E_N(z)=H(0,z)-S_N(z)-\mathcal R_N(z),
\quad E_{\Gamma,0}(z)=|M(s(z))|+|M(1-s(z))|,
\]

the missing sufficient estimate is

\[
\boxed{|E_N(z)|\le C_{B,R}X^{-3/4}E_{\Gamma,0}(z),\quad
 |\Re z-X|\le R+16+1,\quad |\Im z|\le B+1,}
\tag{CB28, OPEN}
\]

uniform in `X`, the fractional cutoff and the adjacent threshold.
For the requested consumer take `R=ell+2`, `B=1+h+2`. A small loss
`X^epsilon`, with a specified `epsilon<1/4`, would also suffice for a
vanishing negative-edge field error. Its buffers and tail constants
must be paid before using Cauchy's formula for signed-time jets.

Real CB18 plus holomorphy does not prove CB28. There is an explicit
failed route: express the complex Gaussian evolution using **real**
initial values and take absolute values. Its kernel modulus acquires
`exp(y^2/(4T))`. Dividing the real `X^-3/4` remainder by the two-arm
complex heat envelope permits the factor

\[
X^{-3/4}\exp\left\{\frac{y^2}{4T}+
 \frac{T\ell_X^2}{16}-\frac{|y|\ell_X}{4}\right\}
 =X^{-3/4}\exp\left\{\ell_X\left(
 \frac{y^2}{4\tau}+\frac\tau{16}-\frac{|y|}{4}\right)\right\},
\tag{CB29}
\]

up to fixed chart constants, with `tau=T ell_X`. This is not uniformly
small as `tau` tends to zero for a fixed nonzero `y`. This failure
concerns absolute estimation on that real integration line. It does
not exclude a better analytic contour or interpolation estimate.

One tractable continuation is a fixed-cutoff Riemann--Siegel contour
estimate; another is a local three-lines argument on a wider fixed
strip and a slowly growing real rectangle, using CB18 at its real
edge and a separately paid upper-edge bound. Neither is proved here.
The full positive-time theorem also cannot simply be used on arbitrary
averaging/differentiation buffers outside its stated domain.

**Stop condition reached:** CB28, with its actual buffer constants and
onset, is the first unpaid estimate needed to promote CB27 to the
requested signed strip/jet result. No signed-time spatial-jet or direct
time-derivative theorem is claimed. The physical tuple, density/current/
covariance transfer, useful runtime, global negative times and
all-real-time regime union remain outside this return.

## 9. Controls, disposition and next owner

| Control | Premise not supplied by that control |
| --- | --- |
| Euler-factor and RH-conditional normalized endpoint controls | The unchanged ordinary zeta coefficient series in CB1 and the full arithmetic tail. |
| Finite weighted-square and finite theta-tail/zero-tail controls | The complete canonical coefficients, completed xi identity and its RS contour remainder. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | The gamma-times-ordinary-zeta identity and Riemann--Siegel expansion, despite shared symmetry or positivity. |
| Counter-kernels, atomic fixed-event and finite-profile controls | The same canonical completion and full arithmetic expansion. |
| Finite-prime orbit controls | Full canonical source/reflection and all coefficients, rather than selected finite identities. |

This is an analytical premise screen, not a numerical control campaign.
No positivity, simplicity or RH assumption is substituted for a missing
estimate, and no collision conclusion is drawn.

**Disposition — Analysis, Sol:** accept CB4--13 as the bounded compact
outer calibration, and CB27 as a signed **real-axis field** bridge from
the stated imports. Accept CB29 as a scoped failed bound. Keep HDA-A01
**Partial**; close AN01 at its permitted bounded partial-return scope.
No global impossibility follows from the failed route. Parent HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

**Next deliverable — Analysis, Sol:** prove CB28, or a precise sufficient
`X^epsilon` version, uniformly across the frozen cutoff, then carry it
through the already paid small-negative-time convolution to the full
buffered field and `j=0,1,2,3` jets. Time differentiation remains a
separate direct estimate. See [AN02 r1][next]. This is a tractable
focused continuation; no exceptional Astra escalation is justified yet.

[packet]: ../research-progress/handoffs/HDA-A01-AN01.md
[next]: ../research-progress/handoffs/HDA-A01-AN02.md
[inputs]: 03_CALIBRATION_BRIDGE_INPUTS_20261025.json
[review]: ../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a19]: ../../../../../avoid/19_status_files_that_lag_the_findings.md
[gamma]: https://dlmf.nist.gov/5.11
[rs]: https://dlmf.nist.gov/25.10
