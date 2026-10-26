# Fixed-cutoff complex remainder and buffered signed-time crossover

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from the current turn metadata. Ansatz chat0001, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Status: proved in-note from named classical inputs; same-model internal
assessment only.** This executes [HDA-A01-AN02 r1][packet]. The open
fixed-cutoff complex estimate CB28 of [Note03][n03] is proved **without
an epsilon loss**. Its buffered signed-time field, spatial jets through
order three and a direct first time derivative are then proved on
`|t| log(X/(4pi))<=8`. This closes the bounded AN01--AN02 calibration
and crossover request, not the all-real-time program or physical
observable transfer. Constants and onset gates are finite but have not
been numerically instantiated. No numerical, machine-symbolic,
exact-arithmetic or interval research was executed.

The [opening manifest][inputs] fixes the input versions. The
[internal assessment][review] records the result's actual review status.
The same chat registration is retained; no new history identity or
manuscript snapshot is created.

## 1. Contract, notation and final statement

Keep the canonical complete source, `H_t=-H_zz`, and

\[
H(0,z)=\xi(s)/8=M(s)\zeta(s),\quad s=(1+iz)/2,
\quad M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16.
\tag{CS1}
\]

The functional equation also gives `H(0,z)=M(1-s)zeta(1-s)`.
Use exactly the physical `q=epsilon_g^2`, fixed `K=k_ell k_h`, and
actual signed covariance of the parent. No estimate of those physical
observables is deduced from the field estimates here.

This is a source-specific approximation milestone under [avoid/01][a01].
Read the [result index][results], especially [11][r11] and
[collision controls12][controls], and the [avoid index][avoid], especially
[02][a02], [05][a05], [07][a07], [08][a08], [12][a12], [16][a16]
and [19][a19]. Section 9 performs the analytical premise screen.

Fix real widths `r,b>0`. For the physical strip and averaging/analytic
buffers take `r=ell+2`, `b=1+h+2`, and reserve one additional unit
of margin. On the right tail use the holomorphic coordinate z and
branches continued from real positive height. Let

\[
L_X=\log(X/(4\pi)),\quad L(z)=\Log(z/(4\pi)),\quad
a(z)=\sqrt{z/(4\pi)},\quad N=\lfloor a(X)\rfloor,
\]
\[
G(z)=[M(s)M(1-s)]^{1/2},\quad
\mathcal C(p)=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)},
\quad \mathcal R_N(z)=(-1)^NG(z)a(z)^{-1/2}\mathcal C(a(z)-N),
\]
\[
S_N(z)=\sum_{n\le N}[M(s)n^{-s}+M(1-s)n^{-(1-s)}].
\tag{CS2}
\]

Choose G positive on the real segment. All apparent poles of C are
removable. Freeze N once per chart and keep it throughout time and
differentiation; no floor is differentiated. Note03 proves the exact
recurrence
`C(p)+C(p-1)=2cos(2pi(p-1)^2-pi/8)` and the real-axis corrected
Riemann--Siegel estimate used below.

Classical inputs were rechecked in [DLMF25.10.3--4][rs],
[DLMF25.2.1 and25.2.8][zeta], and [DLMF5.11][gamma]. The real-axis
RS statement is not imported as an off-axis theorem; Sections2--4
supply that extension.

**Zero-time complex theorem.** For some finite `C_{r,b},X0(r,b)`,

\[
|H(0,z)-S_N(z)-\mathcal R_N(z)|
\le C_{r,b}X^{-3/4}E_{\Gamma,0}(z),\quad
E_{\Gamma,0}=|M(s)|+|M(1-s)|,
\quad |\Re z-X|\le r,\ |\Im z|\le b.
\tag{CS3}
\]

This is precisely the formerly open CB28, for arbitrary declared fixed
buffers and uniform in every fractional-cutoff position.

Use the elementary `A_o,Theta_o,w_n,phi_n` of Note03, holomorphically
continued on this fixed chart, and set

\[
F_N(t,z)=A_o(t,z)\sum_{n\le N}w_n(t,z)\cos\phi_n(t,z)
                         +e^{-\kappa t}\mathcal R_N(z),
\quad \kappa=\pi^2/64.
\tag{CS4}
\]

Let `C_+=A_o exp(iTheta_o)/2`, `C_-=A_o exp(-iTheta_o)/2` and
`E_o=|C_+|+|C_-|`. This is a positive envelope, including the
off-axis growth of the dominant arm. Define

\[
\delta(t,X)=X^{-3/4}\exp\{t_- L_X^2/16\},\quad
t_-=\max(-t,0),\qquad \Lambda_X=1+L_X.
\tag{CS5}
\]

**Buffered crossover theorem.** For sufficiently large X, uniformly
on the fixed target rectangle and `|t|L_X<=8`,

\[
\boxed{|\partial_z^j(H-F_N)(t,z)|
 \le C_j E_o(t,z)\delta(t,X)\Lambda_X^j,\quad 0\le j\le3,}
\tag{CS6}
\]
\[
\boxed{|\partial_t(H-F_N)(t,z)|
 \le C E_o(t,z)\delta(t,X)\Lambda_X^2.}
\tag{CS7}
\]

In particular `delta<=C X^-1/4` throughout the signed window; at
nonnegative time the stronger `delta=X^-3/4` holds, including t=0.
No division by a vanishing cosine occurs. The left tail follows by
reflection after proving these right-tail assertions.

## 2. The real edge on a slowly growing fixed-cutoff chart

For the proof of CS3 put

\[
A=(\log X)^2,\quad D=\max(4,b+1),\quad
Q_X=\{|\Re z-X|\le A,\ 0\le\Im z\le D\}.
\tag{CS8}
\]

The initially fixed cutoff remains usable on this growing rectangle.
Require `a(X+A)-a(X-A)<1/2`, so the natural cutoff m at any real
u in the bottom edge differs from N by at most one. If a threshold
`4pi n^2` lies between X and u, write `d=a(u)-n=O(A/sqrt X)`.
The exact correction recurrence gives

\[
\mathcal R_{n-1}(u)-\mathcal R_n(u)
 =2(-1)^{n-1}G(u)a(u)^{-1/2}\cos(2\pi d^2-\pi/8).
\]

The added exact-gamma mode has phase

\[
\arg M(s(u))-(u/2)\log n
 =-\pi n^2+7\pi/8+2\pi d^2
 +O(X^{-1}+|d|^3/n).
\]

Also `n^-1/2=a(u)^-1/2[1+O(A/X)]`. Thus the mismatch of the
added mode and the correction difference is at most

\[
CG(u)[(A+1)X^{-5/4}+A^3X^{-9/4}].
\tag{CS9}
\]

Both signs of a crossing follow from the same recurrence. Under the
eventual gates `A^3<=X` and `(A+1)/sqrt X<=1`, CS9 is within
`C G(u)X^-3/4`. The classical corrected **real** Riemann--Siegel
formula therefore gives

\[
|E_N(u)|\le CG(u)X^{-3/4},\quad
E_N=H(0,\cdot)-S_N-\mathcal R_N,\quad |u-X|\le A.
\tag{CS10}
\]

This proves the growing-window extension; it is not an application
of a fixed-radius constant to an increasing radius.

## 3. Upper edge: retain the ordinary Dirichlet tail

On the upper half-rectangle let `w=1-s(z)` and normalize by the
nonzero analytic gamma arm:

\[
f(z)=E_N(z)/M(w).
\]

At `y=D`, `Re w=(1+D)/2>1`, so the exact arithmetic identity groups
the leading two terms as

\[
f=\left(\zeta(w)-\sum_{n\le N}n^{-w}\right)
 -\frac{M(s)}{M(w)}\sum_{n\le N}n^{-s}
 -\frac{\mathcal R_N}{M(w)}.
\tag{CS11}
\]

The three terms are bounded respectively by

\[
C_D N^{(1-D)/2}\le C_D X^{(1-D)/4},\quad
C_D X^{-D/2}N^{(D+1)/2}\le C_D X^{(1-D)/4},\quad
C_D X^{-(1+D)/4}.
\tag{CS12}
\]

The first is absolute summation of the ordinary Dirichlet tail.
The second uses the sectorial ratio `|M(s)/M(w)|<=C_D X^-D/2`.
For the third use `|G/M(w)|<=C_D X^-D/4` and boundedness of C on
a fixed compact neighborhood of `[0,1]`; the whole growing rectangle
has `a(z)-N` in that neighborhood eventually. Since `D>=4`,

\[
|f(u+iD)|\le C_D X^{-3/4}.
\tag{CS13}
\]

Bounding H and its dominant finite sum separately on this edge would
give only O(1) and lose a power in interpolation. Their exact grouping
as a Dirichlet tail is what preserves the exponent.

## 4. Vertical edges and the maximum principle

On `0<=y<=D`, `1/2<=Re w<=(1+D)/2`. Euler summation at the integer
cutoff `ceil X` gives `|zeta(w)|<=C_D X^1/2`: the finite sum is at
most `2sqrt(ceil X)`, and the integral remainder is bounded by
`C|w| X^(-Re w)/(Re w)<=C_D X^1/2`. The pole term is harmless
because `|Im w|` is comparable to X.

The dominant finite sum is `O(X^1/4)`. The reflected finite sum is
bounded uniformly in y by

\[
C_D X^{-y/2}N^{(y+1)/2}\le C_D X^{1/4}.
\]

The normalized correction is `O_D(X^-1/4)`. Consequently
`|f|<=C_D X^1/2` on both vertical edges; this is a genuine bound
on those edges, not an unproved absence of boundary growth.

Apply the maximum-modulus principle to the analytic function

\[
g(z)=X^{3/4}f(z)e^{-(z-X)^2}.
\tag{CS14}
\]

The lower and upper edges are bounded by `C_D exp(D^2)` by
CS10 and CS13. On either vertical edge,

\[
|g|\le C_D X^{5/4}e^{-A^2+D^2},
\]

which is bounded after a finite onset. Inverting the weight on the
fixed target core costs only `exp(r^2)` and gives

\[
|E_N(z)|\le C_{r,b}X^{-3/4}|M(1-s(z))|,\quad 0\le y\le b.
\tag{CS15}
\]

Conjugation gives the lower half-strip with M(s), proving CS3.
There is no appeal to real values plus holomorphy alone: the upper
and vertical edge estimates and their analytic weight are paid.

An adequate zero-time onset ledger is the classical real RS and fixed-D
sectorial gamma onsets, plus

    X>=16pi, A>=r, A<=X/2, A+D<=sqrt X,
    a(X+A)-a(X-A)<1/2, A^3<=X, (A+1)/sqrt X<=1,
    A^2>=(5/4)log X+D^2.

Every gate is eventual. No numerical value of the imported constants
or the resulting X0 is claimed.

### Direct contour cross-check

A separate analytical check uses **Polymath Proposition6.2**, not
its narrower positive-time Proposition6.3. Proposition6.2 permits
all real sigma; for negative sigma its remainder requires `K+sigma>=2`.
For `|y|<=b`, choosing
`K=max(1,ceil(2-(1-b)/2))` in its equations (54)--(57) gives a
uniform next-term error `O_b(a_x^-1)`. Combining the two exact
contours (36)--(38), sectorial gamma transport and the leading C0
identity yields even `|E_N(z)|<=C_{r,b}G(Re z)X^-3/4` on fixed
charts. The matching uses

\[
M(1/2+ix/2+d)a_x^{-1/2-d}
 =M(1/2+ix/2)a_x^{-1/2}e^{i\pi d/4}(1+O_b(x^{-1})),
\]

and `2 Re C0(1-2q)=C(q)`. This check agrees with CS3; the main proof
above does not require importing that stronger statement. The inspected
primary source is [Polymath v2][polymath], including its explicit
all-sigma qualifications. The underlying Arias de Reyna paper was not
independently read in this continuation; its PDF access returned 403.
No new novelty claim is made.

## 5. Fixed windows and height-relative tails for both heat signs

Prove CS3 first on **every fixed** radius and strip that will be needed.
For the heat estimates reserve target `(r+1,b+1)`. The local negative
convolution uses initial radius `r+V_b+2` and strip `b+1`; the positive
one uses radius `r+1` and strip `b+1+2V_b`. These are all fixed data,
so the just-proved theorem supplies them with their own finite onsets.

Choose the constants as follows. Sectorial gamma bounds on the base
physical strip, reflection and ordinary zeta bounds give a finite
`c_b>=1` and an exponent, for example `P_b=b+12`, such that

\[
|H(0,u+iy)|\le c_b (1+u)^{P_b}e^{-\pi u/8}
\quad (u\ge X/3,\ |y|\le b+1).
\tag{CS16}
\]

On a real shift v of either xi argument, the same gamma ray bounds
retain its height exponential. For `|v|<=X^(1/3)` they imply

\[
|H(0,z-2iv)|\le c_bG(X)X^{P_b}
 \exp\{|v|L_X/2+c_b|v|+c_bv^2/X\}.
\tag{CS17}
\]

For all v the corresponding bound has logarithm at most
`P_b log(X+|v|)+c_b(|v|+1)+(|v|/2)log(X+|v|)` relative to G(X),
after increasing `c_b` once here. Freeze these tail constants before
choosing the window. In the unbounded ray tails choose reflection
so that the xi argument has real part at least two, and use the
absolutely convergent zeta series. The bounded remaining strip uses
Euler summation. Thus no growing-v zeta bound is silently imported.

Take one fixed window

\[
V_b\ge\max\{16,\ b+8,\ 16c_b,\ 8\sqrt{P_b+6}\}.
\tag{CS18}
\]

This explicitly enlarges Note03's window16 for arbitrary averaging
widths, as permitted by AN02. The number16 alone cannot absorb every
fixed-strip polynomial under a coarse absolute tail bound.
All subsequent enlarged-chart/local constants may depend on this fixed
V_b; they only affect the final prefactor and X0. They do not retroactively
change c_b or its window gate.

**Negative sign.** For `T=-t`, use the exact source identity

\[
H(-T,z)=\frac1{\sqrt{4\pi T}}\int_\mathbb R
e^{-v^2/(4T)}H(0,z-v)\,dv.
\tag{CS19}
\]

For `V_b<|v|<=X/2`, CS16, gamma transport and `T<=1/2` yield,
after E_o division, a bound at most

\[
C_bX^{P_b-7/4}e^{TL_X^2/16}e^{-V_b^2/(8T)}
 \le C_bX^{P_b-5/4-V_b^2/64}.
\tag{CS20}
\]

This is smaller than the desired allowance by CS18. At `|v|>X/2`,
the global complete-source strip bound
`sup_u |H(0,u+iy)|<=int_0^infinity |Phi(q)|cosh((b+1)q)dq<infinity`
gives `C_b X^-7/4 exp(pi X/8+TL_X^2/16-X^2/(16T))`, smaller
than every inverse power. The source bound is used only at that
distant tail.

**Positive sign.** For `t>0`, use the exact identity

\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_\mathbb R
e^{-v^2/t}H(0,z-2iv)\,dv.
\tag{CS21}
\]

On `V_b<|v|<=X^(1/3)`, use `tL_X<=8` in CS17. Since the tilted
centers have absolute size at most `2+o(1)`, CS18 and a finite
large-X gate give

\[
-v^2/t+|v|L_X/2+c_b|v|+c_bv^2/X\le-v^2/(4t).
\]

The normalized tail is at most `C_b X^{P_b-V_b^2/32}`. For
`|v|>X^(1/3)`, the full ray logarithm after CS17 is bounded by
`v^2/(2t)` once X exceeds a fixed onset, uniformly for `t<=1/2`.
Gaussian integration then gives a superpolynomial tail. This is the
same large-ray domination used in Note03, with its base-strip constants
retained. The full height exponential is never replaced by a global
source bound near `|v|=V_b`.

Artificial tails introduced by completing the **linear** mode and
correction Gaussians have bounded imaginary tilts or real tilted centers
of size at most `2+o(1)`. The same CS18 window, including the complete
finite-mode count, pays them. The true analytic correction R_N is not
extended along infinite shifted arguments without a bound: only its
local approximation is completed to an elementary full Gaussian.

## 6. Local field comparison and the entire mode population

On each enlarged fixed chart, sectorial gamma calibration gives

\[
E_o(t,z)\asymp E_{\Gamma,0}(z)e^{tL_X^2/16},
\quad |t|L_X\le8,
\tag{CS22}
\]

with fixed constants. Bounded `exp(-pi^2 t/64)` and small chart
variations are included. Set `alpha=M'/M` and
`h_n(z)=M(s(z))n^-s(z)`. On the negative convolution window,

\[
h_n(z-v)=h_n(z)e^{-\beta_n v}(1+O_b(v^2/X)),
\quad \beta_n=\tfrac i2(\alpha(s)-\log n),
\]

uniformly for **every** `n<=N`. Exact Gaussian completion gives
`M(s)n^-s exp[-T(alpha(s)-log n)^2/4]`. The absolute local Taylor
error is at most `C_b T/X` times the full initial-mode population.

On the positive window replace `s` by `s+v` (and the reflected
argument by `1-s-v`). The log-gamma quadratic error is `O_b(v^2/X)`.
Gaussian completion gives the signed formula

\[
M(w)n^{-w}\exp\{t(\alpha(w)-\log n)^2/4\},\quad w=s,1-s.
\tag{CS23}
\]

The tilted moments cost `O(t+t^2|alpha-log n|^2)<=C` because
`|t|L_X<=8`. The absolute/complex Gaussian loss is bounded on this
shrinking-time window. Hence the positive per-mode Taylor error is
at most `C_b/X` times its evolved nonzero arm modulus.

The required population estimate does not assume bounded n. For
`0<=y<=b+1`, the initial dominant-arm sum is at most
`E_Gamma sum n^-1/2<=C E_Gamma X^1/4`. For the other arm use
`|M(s)|/E_Gamma<=C_b X^-y/2` and
`sum n^{(y-1)/2}<=C_b N^{(y+1)/2}`. It also costs at most
`C_b E_Gamma X^1/4`. Reflect for negative y. The same argument
applies to elementary evolved arms, with

\[
\sum_{\pm,n\le N}|P_{\pm,n}(t,z)|
 \le C_bE_o(t,z)X^{1/4}e^{t_-L_X^2/16},
\tag{CS24}
\]

where

\[
P_{\pm,n}=C_\pm(0,z)n^{-1/2}e^{\mp iz\log n/2}
  e^{t(b_\pm-\log n)^2/4},\quad b_\pm=L(z)/2\pm i\pi/4.
\]

Indeed `|w_n|<=n^-1/2` for positive time, with the eventual gate
`log N<=Re L(z)`; for negative time its
additional exponent is at most `T L_X^2/16+O_b(X^-1)` uniformly
through the cutoff. The initial-to-heat carrier loss is exactly the
exponential in CS24. Replacing the exact-gamma modes CS23 by these
elementary modes costs `C_b/X` per arm from Note03 CB4, including
all their exponent differences when `|t|L_X<=8`.

It remains to pay the correction. On the relevant fixed charts,

\[
G'/G=-\pi/8+O_b(X^{-1}),\quad
f_N=a^{-1/2}\mathcal C(a-N),
\quad |f_N|\le C_bX^{-1/4},\quad
|f_N'|\le C_bX^{-3/4},\quad |f_N''|\le C_bX^{-5/4}.
\tag{CS25}
\]

Thus local negative smoothing replaces R_N(z-v) by
`exp(pi v/8) R_N(z)` with error
`C_b|G(z)|X^-3/4 |v| exp(C_b|v|)`; positive smoothing replaces
R_N(z-2iv) by `exp(i pi v/4) R_N(z)` with the analogous error.
Their Gaussian averages give the same signed short term
`exp(-kappa t)R_N(z)`, with error at most
`C_b|G(z)|X^-3/4(sqrt(|t|)+|t|)`.

Finally apply CS3 to the initial remainder on these whole local
windows. In CS19 its absolute Gaussian average costs at most
`C_b E_Gamma X^-3/4`, hence at most `C_b E_o delta` by CS22.
In CS21, `|M(w+v)|<=C_b|M(w)|exp(v L_X/2)` for fixed v, and the
other arm has the opposite tilt. Their Gaussian averages cost
`C_b exp(tL_X^2/16)`, precisely matching CS22. The positive remainder
therefore costs `C_b E_o X^-3/4`.

Combining CS18--25 proves the field part of CS6. In particular no
arithmetic modes, cutoff terms or Gaussian tails remain unpaid.
This derivation supplies arbitrary fixed positive-time buffers directly;
it does not silently extend the restricted domain of Polymath's
positive-time Proposition6.3 or Theorem1.3.

## 7. Holomorphic jets and a direct time derivative

All definitions are holomorphic at the fixed N. Prove the field bound
on the one-unit enlarged rectangle, with the same center condition
`|t|L_X<=8`. On disks of radius `1/(8 Lambda_X)`, each elementary
arm changes modulus by a bounded factor because its log derivative is
`O_b(Lambda_X)`. Cauchy's formula gives CS6 for j=0,1,2,3. The fixed
chart center avoids a boundary problem in the time/height condition;
replacing L_X by the real local logarithm changes only bounded constants.

For time, do not differentiate a Gaussian remainder estimate. Every
elementary mode has an exact residual. Put `c=b_pm-log n`. Then

\[
\frac{(\partial_t+\partial_{zz})P_{\pm,n}}{P_{\pm,n}}
 =\frac{\pm i(1+7c+t c^2)}{4z}
 +\frac{21/16+t/8+5tc/8+t^2c^2/16}{z^2}.
\tag{CS26}
\]

Since `|c|<=C_b Lambda_X` and `|t|Lambda_X<=C`, this is at most
`C_b Lambda_X/X`. CS24 therefore pays the summed mode residual by
`C_b E_o delta Lambda_X`. Also CS25 and
`G''/G=kappa+O_b(X^-1)` give

\[
\mathcal R_N''-\kappa\mathcal R_N
 =O_b(|G|X^{-3/4}).
\tag{CS27}
\]

Its signed exponential factor is bounded, and CS22 places its residual
inside `C_b E_o delta`. We have proved the actual model bound

\[
|(\partial_t+\partial_{zz})F_N|
 \le C_b E_o\delta\Lambda_X.
\tag{CS28}
\]

Use the exact identity

\[
\partial_t(H-F_N)=-(H-F_N)_{zz}
                       -(\partial_t+\partial_{zz})F_N.
\]

The j=2 bound and CS28 prove CS7 uniformly through t=0. Both H and
the fixed-chart F_N are differentiable there. No `1/T` factor or
differentiated big-O allowance is involved, and a small residual alone
has not been used to propagate an unproved field estimate.

## 8. Remaining onset gates, compatibility and scope

CS3 is available on all the enlarged fixed charts in Section 5. Choose
V_b by CS18, then choose a single X0 exceeding their zero-time onsets,
with `L_X>=16`, `X>=max(2(r+V_b+2),6(r+1))`, all local gamma Taylor smallness
gates, `c_b v^2/X<=v^2/(8t)` on the near positive tail, and the
large-ray Gaussian domination after CS17. These gates are all eventual;
there is no numerical certified cutoff. Constants can depend strongly
on r,b and the chosen enlarged charts. Useful runtime is not claimed.

The fixed chart formula is the same F_N as Note03. Globally choosing
a fresh N at every height produces small truncation mismatches; CS6--7
are claims on holomorphic **fixed-N charts**, not claims that a global
floor-valued formula is differentiable. Overlapping chart models compare
through the same H within their respective proved allowances. No new
spatial join or physical join defect is silently set to zero.

The compact positive-time corrected cosine from Note03 remains valid
at its own `[32,33]` scope. The current shrinking-time theorem does not
cover all intervening fixed times or compact negative-time intervals.
The correction can exceed the outer envelope near the negative edge;
it is retained in F_N, not mistaken for a small error. No universal
crossover constant, no all-time domain union, and no RH or simplicity
conclusion follows.

The formerly unpaid CB28 and signed buffered jet/time obligations are
closed at this bounded analytical scope. Parent HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain. Independent specialist
review and physical U,W,R,J,Q transfer remain separate obligations.

## 9. Control screen and disposition

| Control family | Exact premise absent here |
| --- | --- |
| Euler-factor perturbations and RH-conditional normalized-endpoint controls | The unchanged ordinary Dirichlet coefficients used in the upper-edge tail CS11. |
| Finite weighted-square, finite theta-tail and zero-tail controls | The full canonical completed xi identity and its corrected real RS expansion. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Gamma times ordinary zeta and the canonical arithmetic tail; symmetry/positivity alone give neither. |
| Counter-kernels, atomic fixed-event and finite-profile controls | The same full completion and arithmetic sequence. |
| Finite-prime orbit controls | The complete reflection/coefficient premises, rather than finitely many selected identities. |

This is an analytical premise screen, not a numerical campaign. The
specific source information pays the approximation; it is not an assumed
collision-free conclusion. Note03's failed complex real-line absolute
bound is preserved as a scoped failure, now bypassed by a paid strip
estimate.

**Disposition — Analysis, Sol:** accept CS3 and CS6--7 from the cited
inputs and the proof above, subject to same-model internal review only.
Close AN02 r1 and the AN01--AN02 bounded calibration/crossover scope
of HDA-A01. The larger all-real-time representation objective remains
open. The next analytical regime is HDA-A02: fixed compact negative
times, where `exp(T L_X^2/16)` can no longer be absorbed by this fixed
RS truncation. That is a new bounded Sol task, not an automatic
continuation of the present error by substitution.

[packet]: ../research-progress/handoffs/HDA-A01-AN02.md
[n03]: 03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[inputs]: 04_COMPLEX_STRIP_INPUTS_20261025.json
[review]: ../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
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
[polymath]: https://arxiv.org/html/1904.12438v2
[rs]: https://dlmf.nist.gov/25.10
[zeta]: https://dlmf.nist.gov/25.2
[gamma]: https://dlmf.nist.gov/5.11
