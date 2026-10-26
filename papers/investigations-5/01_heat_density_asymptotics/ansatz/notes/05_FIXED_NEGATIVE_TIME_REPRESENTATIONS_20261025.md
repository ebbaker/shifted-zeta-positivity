# Fixed negative times: a short natural-scale model and an outer-scale representation

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from this turn metadata. Ansatz chat0001, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Status: proved in-note from named classical inputs; same-model internal
assessment only.** Return to [HDA-A02-AN01 r1][packet]. The interval is
only `t=-T`, `1<=T<=2`. Two different results are established:

1. The existing short finite arithmetic formula has field, three spatial
   jets and a direct first time error `O(|G(z)|X^-3/4)` on every fixed
   buffered chart. This is a **natural gamma-scale** comparison.
2. A finite representation with `K=ceil L_X` Riemann--Siegel terms and
   `J=ceil(3L_X)` common gamma-curvature terms has those errors at most
   `C E_o(-T,z) exp(-L_X^2/4)`, at the smaller **outer heat-carrier**
   scale. It retains one bounded Gaussian integral of explicit RS
   correction data; it is not a low-parameter elementary ansatz.

Neither error is divided by the true field or a cosine. Neither result
states that an isolated correction dominates H. Constants and finite
onsets are analytical and not numerically instantiated. No numerical,
symbolic, exact-arithmetic or interval research was executed.

The [opening manifest][inputs] pins input versions. The
[assessment][review] records the actual acceptance and review scope.
[Notes03][n03] and [04][n04] remain historical inputs with their original
statuses. No previous shrinking-time error is substituted at fixed T.

## 1. Contract, buffers and the two positive envelopes

Keep the complete canonical source and normalization

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\quad
H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8,
\]
\[
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad \alpha=M'/M,
\quad s(z)=(1+iz)/2.
\tag{FN1}
\]

The physical `q=epsilon_g^2`, fixed `K=k_ell k_h`, actual signed
covariance, potential offsets and joining/regulator defects are unchanged.
No physical observable transfer is asserted in this packet.

Fix target radii `r,b>0`; the physical and averaging choice is
`r=ell+2`, `b=1+h+2`, with one extra unit of analytic margin.
Work first on the right chart

\[
\Omega_X=\{|\Re z-X|\le r,\ |\Im z|\le b\},\quad
L=L_X=\log(X/(4\pi)),\quad N=\lfloor\sqrt{X/(4\pi)}\rfloor.
\]

N and every truncation/window parameter below are frozen at the real
chart center X, throughout differentiation in z and time.
Use the branch `G(z)=[M(s(z))M(1-s(z))]^(1/2)` positive on the real
segment. It is nonzero on the far-height chart and satisfies

\[
G'/G=-\pi/8+O_b(X^{-1}),\qquad |G(z)|\asymp_{r,b}G(X).
\tag{FN2}
\]

Retain Note03's elementary arms `C_pm=A_o exp(+-iTheta_o)/2` and
`E_o=|C_+|+|C_-|`. Uniformly for `1<=T<=2` on this fixed chart,

\[
E_o(-T,z)\ge c_{r,b}G(X)e^{-TL^2/16}.
\tag{FN3}
\]

On the real axis, `E_o=A_o` and their ratio to G includes the actual
heat factor `exp(-TL^2/16+pi^2T/64)`, up to fixed constants. The
dominant-arm growth off the axis only improves the lower bound FN3.
These are distinct comparison scales; a gamma-scale allowance does
not imply an outer-scale allowance.

This is an approximation milestone under [avoid/01][a01]. Read the
[result index][results], especially [11][r11] and [controls12][controls],
and [avoid][avoid], especially [02][a02], [05][a05], [07][a07],
[08][a08], [12][a12], [16][a16], [19][a19] and [20][a20]. The
source-specific premise screen is in Section10.

## 2. The exact real-initial-value heat identity

For every T>0 and complex z,

\[
H(-T,z)=\frac1{\sqrt{4\pi T}}\int_\mathbb R
 e^{-(z-u)^2/(4T)}H(0,u)\,du.
\tag{FN4}
\]

This follows directly by inserting the canonical real-u Fourier
representation of H(0,u), interchanging its integrals and applying
the Fourier Gaussian identity. Absolute Fubini uses `int|Phi|<infinity`
and the real-u Gaussian integral; the initial cosine has real argument.
The complex kernel supplies `e^{y^2/(4T)}`, bounded by `e^{b^2/4}`
on this time interval. The identity can also be extended from real z
by entire continuation, but no contour deformation is needed.

This choice of real initial values is decisive. The factor that failed
uniformly as T tended to zero in Note03 is harmless on `1<=T<=2`.
It lets us retain real RS corrections with fixed real partitions while
the resulting field is holomorphic. A real part inside the initial data
is allowed; taking `Re` after integrating a complex kernel would not
define a holomorphic field and is not done here.

## 3. First result: the existing short formula at its natural scale

Keep the analytic fixed-cutoff correction of Notes03--04:

\[
a(z)=\sqrt{z/(4\pi)},\quad
\mathcal C(p)=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)},
\quad \mathcal R_N(z)=(-1)^NG(z)a(z)^{-1/2}\mathcal C(a(z)-N),
\]

with all apparent poles removed, and let `F_N` be exactly Note04 CS4,
the elementary arithmetic sum plus `exp(-pi^2t/64) R_N`.

**Natural-scale theorem.** For `1<=T<=2`, sufficiently large X and
the entire buffered target chart,

\[
|\partial_z^j(H-F_N)(-T,z)|\le C_{r,b,j}|G(z)|X^{-3/4},
\quad 0\le j\le3,
\]
\[
|\partial_t(H-F_N)(-T,z)|\le C_{r,b}|G(z)|X^{-3/4}.
\tag{FN5}
\]

There is no logarithmic derivative loss in FN5. Relative to the
positive RS correction envelope `|G|X^-1/4`, the error is O(X^-1/2),
throughout fixed buffers. This envelope is not a lower bound on H or
on R_N, both of which can have cancellations or zeros.

### 3a. Initial remainder and full mode curvature

Take the real smoothing window `|u-X|<=V`, `V=8L`. Eventually it lies
inside Note04's growing real chart `|u-X|<=log^2 X`. Its real
fixed-N expansion has remainder `O(G(u)X^-3/4)`, uniformly across the
at-most-one cutoff crossing. FN4 averages this to `O(G(X)X^-3/4)`;
the entire Gaussian moment against `G(u)/G(X)<=C exp(pi|u-X|/8)` is
bounded, even after fixed polynomial kernel factors.

For a mode `h_n(z)=M(s(z))n^-s(z)`, set
`beta_n=(i/2)(alpha(s)-log n)`. Its second logarithmic spatial
derivative is O(X^-1), independently of n. On the local window,

\[
h_n(u)=h_n(z)e^{\beta_n(u-z)}
 [1+O(|u-z|^2/X)e^{C|u-z|^2/X}].
\tag{FN6}
\]

Although h_n(z) separately has transverse n- and height-powers,
they cancel in this real-source comparison. Taylor first from z to
`x=Re z` gives

\[
|h_n(z)e^{-iy\beta_n}|\le C_b|h_n(x)|
 =C_bG(x)n^{-1/2}.
\tag{FN7}
\]

The remaining real tilt is bounded independently of n. Thus FN6's
absolute Gaussian error is `C_bG(X)n^-1/2/X` per mode. The complete
sum `sum_{n<=N}n^-1/2<=2sqrt N` gives `O(G(X)X^-3/4)`.
The completed linear Gaussian is exactly

\[
M(w)n^{-w}e^{-T(\alpha(w)-\log n)^2/4},\qquad w=s,1-s.
\tag{FN8}
\]

### 3b. Population near the cutoff, not fixed-mode convergence

To replace FN8 by the elementary heat modes, it is necessary to bound
all logarithmic moments over the growing population. For each fixed
integer d>=0,

\[
\sum_{\pm,n\le N}(1+|b_\pm-\log n|)^d
 |P_{\pm,n}(-T,z)|\le C_{b,d}|G(z)|X^{1/4},
\quad b_\pm=\tfrac12\Log(z/(4\pi))\pm i\pi/4.
\tag{FN9}
\]

Here P are Note04's elementary mode arms. Put `a_X=sqrt(X/(4pi))`
and `v_n=log(a_X/n)>=0`. A summand is at most

\[
C_b|G(z)|a_X^{-1/2}
 \exp\{(1+b)v_n/2-v_n^2/8\}
\]

times a fixed polynomial in v_n. The shell `v_n in[k,k+1]` contains
at most `2a_X e^-k` integers. Its Gaussian damping makes every such
moment summable with a constant independent of X. The gamma-to-
elementary relative defect is at most `C_b(1+|b_pm-log n|)/X` per arm, by
the sectorial calibration of Note03. FN9 pays it by `O(GX^-3/4)`.
Modes in `[a_X/2,a_X]` already have absolute population comparable
to `GX^1/4`; a fixed set of low modes cannot replace this estimate.

The correction's slowly varying factor has derivative O(X^-3/4)
after division by G. Its convolution therefore equals
`exp(pi^2T/64) R_N(z)+O(GX^-3/4)`. The local and artificial tails
are paid by Section7 below. This proves the field part of FN5.

Since G changes modulus by only a bounded factor on fixed-radius
disks, Cauchy's formula on a fixed extra margin gives j<=3 with no
log powers. The exact per-mode residual of Note04 CS26, summed with
FN9, is `O(GX^-3/4)` at fixed T. Explicitly,
`|R_N''-(pi^2/64)R_N|<=C_b|G|X^-3/4`, so the correction residual has
the same bound. The exact heat identity then gives FN5's first time
derivative; no error allowance is differentiated.

### 3c. The stronger error budget still fails for this short model

On the real axis FN5 divided by A_o permits

\[
X^{-3/4}e^{TL^2/16},
\tag{FN10}
\]

which grows for fixed T. This is a failure of that **bound**, not a
lower bound on the actual error. FN5 does not prove a leading amplitude
or phase for H at the outer-carrier scale. The next construction pays
that stricter target rather than silently changing its normalization.

## 4. Uniform high-order RS data on a real initial window

Use the same `V=8L`, and set

\[
K=\lceil L\rceil,\quad J=\lceil3L\rceil,\quad R=X^{1/3},
\quad I_X=[X-V,X+V].
\tag{FN11}
\]

For real u in I_X, let

\[
s_u=1/2+iu/2,\quad a_u=\sqrt{u/(4\pi)},\quad
m(u)=\lfloor a_u\rfloor,\quad p_u=1-2(a_u-m(u)),
\]
\[
U_u=\exp\{-i[(u/4)\log(u/(4\pi))-u/4-\pi/8]\}.
\]

Let `C_k(p,1/2)` be the classical coefficient functions in
[Polymath v2, Proposition6.2][polymath]. Define real initial data

\[
R_{m,K}(u)=2\Re\left\{(-1)^{m-1}M(s_u)U_u a_u^{-1/2}
 \sum_{k=0}^K C_k(p_u,1/2)a_u^{-k}\right\},
\]
\[
f_K(u)=S_{m(u)}(u)+R_{m(u),K}(u).
\tag{FN12}
\]

The imported expansion has arbitrary positive integer K. At sigma=1/2
its coefficient and remainder bounds specialize to

\[
|C_0|\le\tfrac12,\quad
|C_k|\le\frac{3\sqrt2}{2\pi}\frac{\Gamma(k/2)}{2^k},\quad
|RS_K|\le\frac{2^{3/4}}7\Gamma((K+1)/2)(1.1/a_u)^{K+1}.
\tag{FN13}
\]

Consequently

\[
|H(0,u)-f_K(u)|\le C G(u)a_u^{-1/2}
 \Gamma((K+1)/2)(1.1/a_u)^{K+1}.
\tag{FN14}
\]

The exact gamma M is retained; the source's separate Stirling factor
is not substituted. This construction invokes only real initial
sigma=1/2. The negative-sigma qualification `K+sigma>=2` in that
proposition was checked, but is not needed here. No positive-time
evolved remainder is imported at negative time. The source coefficient
functions are named classical inputs; no new working-precision or
coefficient-provider complexity theorem is claimed.

The retained coefficients also have a K-uniform size bound. For
`t_k=Gamma(k/2)/(2a)^k`,

\[
t_{k+2}/t_k=k/(8a^2).
\]

Eventually `K<=a_min^2`, where `a_min=sqrt((X-V)/(4pi))`. Summing
the odd and even subsequences then gives
`sum_{k=1}^K |C_k|/a^k<=C/a`. Hence
`|R_{m,K}(u)|<=C G(u)X^-1/4` throughout the whole window, without
hiding an exponentially growing K-dependent prefactor.

Freeze the main arithmetic cutoff exactly by writing

\[
Q_{X,K}(u)=S_{m(u)}(u)-S_N(u)+R_{m(u),K}(u),
\qquad f_K=S_N+Q_{X,K}.
\tag{FN15}
\]

After the gate `a(X+V)-a(X-V)<1`, the transfer contains at most one
adjacent arithmetic mode. It is retained **exactly**, without replacing
a high-order cutoff transfer by the lower-order recurrence allowance.
All real partitions at `u=4pi n^2` are fixed independently of z,T.
Thus `|Q_{X,K}(u)|<=C G(u)X^-1/4`; it need not be small relative to
the outer carrier. Assign either one-sided value at an isolated
threshold; it has measure zero in the integrals.

## 5. A finite heat-transform representation already pays the outer scale

Define

\[
\widetilde F_X(-T,z)=\frac1{\sqrt{4\pi T}}\int_{I_X}
e^{-(z-u)^2/(4T)}f_K(u)\,du.
\tag{FN16}
\]

This contains no H or zeta value in its initial data: f_K uses finitely
many ordinary powers, gamma factors and the named RS coefficient
functions. The real part in FN12 stays **inside** the real initial
data; it is not taken outside the complex kernel integral. FN16 is
entire in z, and its fixed initial data and endpoints give exactly
`partial_T Ftilde=Ftilde_zz` for T>0.

Let `a_min` be as above. Gaussian averaging FN14 costs at most

\[
C_{r,b}G(X)X^{-1/4}\Gamma((K+1)/2)
 (1.1/a_{\min})^{K+1}.
\tag{FN17}
\]

Spatial derivatives through order three only insert fixed polynomial
Gaussian factors; their moments against `exp(pi|u-X|/8)` are bounded
uniformly for T in[1,2]. After outer-envelope division by FN3, the
logarithm of FN17 is at most

\[
-\frac38L^2+\frac12L\log L+O_{r,b}(L).
\tag{FN18}
\]

This pays the actual Gamma(K/2) growth. The omitted true tails are
paid in Section7 and are smaller. Therefore the field, j<=3 spatial
jets and direct first time error of FN16 are at most

\[
C_{r,b,j}E_o(-T,z)e^{-L^2/4}
\tag{FN19}
\]

after a finite onset. Its time comparison follows from its exact heat
identity and the j=2 error, rather than differentiating FN18.

FN16 is a finite bounded Gaussian integral representation. It is not
yet a short arithmetic heat sum; in particular retaining it is how
one avoids an unpaid gamma-mode curvature approximation. The following
step pays that approximation explicitly.

## 6. Common high-order gamma curvature and finite Gaussian moments

At the fixed real center let, for epsilon=+1,-1,

\[
w_\epsilon=(1+\epsilon iX)/2,\quad
h_{\epsilon n}=M(w_\epsilon)n^{-w_\epsilon},\quad
\lambda_{\epsilon n}=\tfrac{\epsilon i}2
 [\alpha(w_\epsilon)-\log n].
\]

For real or complex q near0, factor the exact mode as

\[
M(w_\epsilon+\epsilon iq/2)n^{-w_\epsilon-\epsilon iq/2}
=h_{\epsilon n}e^{\lambda_{\epsilon n}q}A_\epsilon(q),
\]
\[
A_\epsilon(q)=\frac{M(w_\epsilon+\epsilon iq/2)}{M(w_\epsilon)}
 e^{-\epsilon i\alpha(w_\epsilon)q/2}.
\tag{FN20}
\]

The curvature factor is **independent of n**. Sectorial gamma bounds
give `alpha'=O(X^-1)` on `|q|<=R=X^1/3`; hence
`|log A_epsilon(q)|<=C |q|^2/X`. Choose the onset so its supremum
there is at most log2. Define exact Taylor coefficients

\[
a_{\epsilon k}=A_\epsilon^{(k)}(0)/k!,\quad
P_{\epsilon,J}(q)=\sum_{k=0}^J a_{\epsilon k}q^k.
\]

Cauchy's formula yields the order-uniform estimates

\[
|a_{\epsilon k}|\le2R^{-k},\qquad
|A_\epsilon(q)-P_{\epsilon,J}(q)|
 \le4(V/R)^{J+1}\quad(|q|\le V,\ V/R\le1/2).
\tag{FN21}
\]

No formal growing-order Stirling series is used to establish these
coefficient bounds. The exact derivatives define coefficients
analytically; no symbolic expansion or exact-arithmetic research was run.

For `d=z-X`, define the finite gamma-mode heat sum

\[
\mathcal M_{X,N,J}(T,z)=\sum_{\epsilon,n\le N}h_{\epsilon n}
 \sum_{k=0}^J a_{\epsilon k}
 \left.\partial_\lambda^k e^{\lambda d+T\lambda^2}
 \right|_{\lambda=\lambda_{\epsilon n}}.
\tag{FN22}
\]

This is a finite sum of elementary Gaussian moments, with exact gamma
parameters. The complete population satisfies
`sum_{epsilon,n}|h_epsilon,n|<=C G(X)X^1/4`; also
`Re lambda_epsilon,n=-pi/8+O(X^-1)` independently of n.
Comparing the actual arithmetic-mode convolution over `|q|<=V`
with FN22 gives the bound

\[
CG(X)X^{1/4}\left[(V/R)^{J+1}+e^{-V^2/64}+e^{-R^2/128}\right].
\tag{FN23}
\]

This holds for the field and spatial derivatives j<=3. The local term
uses FN21 and bounded Gaussian moments. The two artificial polynomial
tails are proved in Section7. Relative to FN3, FN23 is eventually
at most `C E_o exp(-L^2/2)`: its local logarithm is

\[
-\frac78L^2+3L\log L+O_{r,b}(L).
\tag{FN24}
\]

The growing common polynomial therefore pays all arithmetic heat
curvature at a precision below the stricter outer-carrier error.
Increasing only the initial RS order would not have done this.

The final finite representation is

\[
\boxed{\widehat F_X(-T,z)=\mathcal M_{X,N,J}(T,z)
 +\frac1{\sqrt{4\pi T}}\int_{X-V}^{X+V}
 e^{-(z-u)^2/(4T)}Q_{X,K}(u)\,du.}
\tag{FN25}
\]

All main arithmetic modes, all K+1 retained RS terms, and the exact
adjacent cutoff transfer are included. The correction integral is
bounded and explicit in named functions, but remains an integral.
It is not rebranded as an elementary single-cosine asymptotic.

**Outer-scale theorem.** Uniformly on the complete fixed buffered
chart and for `1<=T<=2`, after a finite onset,

\[
\boxed{|\partial_z^j(H-\widehat F_X)(-T,z)|
 \le C_{r,b,j}E_o(-T,z)e^{-L^2/4},\quad 0\le j\le3,}
\]
\[
\boxed{|\partial_t(H-\widehat F_X)(-T,z)|
 \le C_{r,b}E_o(-T,z)e^{-L^2/4}.}
\tag{FN26}
\]

Both terms of FN25 solve `partial_T F=F_zz` exactly: FN22 is a full
Gaussian transform of exponential-polynomial initial data, and the
correction integral has fixed initial data and endpoints. Thus its
negative-time heat residual is zero. The first time bound follows
directly from j=2. This residual identity is a consumer of the proved
field comparison, not a substitute for it.

## 7. All genuine and artificial tails

Put `q=u-X`, `d=z-X`. On fixed buffers the modulus of the kernel is
`exp[(Im d)^2/(4T)] exp[-(q-Re d)^2/(4T)]`. For large X and
`V=8L>=4r+2pi+1`, the gamma height exponential and elementary real
zeta growth give, on `V<|q|<=X/2`,

\[
|H(0,X+q)|\le C X^P e^{-\pi X/8+\pi|q|/8}
\]

for one fixed exponent, e.g. P=4. This retains the height exponential.
Gaussian dominance yields a safe common outer-relative bound, also
for the polynomial kernel factors needed at j<=3,

\[
C_{r,b}X^{P-7/4}(1+V^5)
 \exp\{TL^2/16-V^2/64\}.
\tag{FN27}
\]

Its worst leading exponent is `-7L^2/8+O(L+log L)`. At `|q|>X/2`,
the global real source bound `|H(0,u)|<=int|Phi|` and the Gaussian
give `exp[-cX^2+pi X/8+TL^2/16]` times a fixed power, smaller than
every inverse power relative to E_o. The global source bound is not
used already at q=V.

For the linearized or polynomial mode completions, retain their
entire population `C G(X)X^1/4` and uniformly bounded real tilts.
On `V<|q|<=R/2`, FN21's coefficient bound gives
`|P_epsilon,J(q)|<=4`; the Gaussian therefore costs at most
`C G(X)X^1/4 exp(-V^2/64)`. For `|q|>R/2`, use

\[
|P_{\epsilon,J}(q)|\le2(J+1)\max(1,(|q|/R)^J).
\]

Since J=O(log X) and R=X^1/3, its logarithm, the bounded linear
tilt and fixed-degree kernel factors are eventually dominated by
`q^2/32`, uniformly on this whole ray. The remaining tail is at most
`C G(X)X^1/4 exp(-R^2/128)`. This proves the artificial terms in
FN23. The short model's linear correction completion has the same
bounded-tilt Gaussian tail. No true analytic RS correction is extended
to infinite complex arguments without a bound.

## 8. Constants, onset gates and exact scope

Use one X0 large enough for the fixed buffers and all enlarged analytic
disks, with

    L>=16, X-V>=X/2, V+r+1<=log^2 X,
    a(X+V)-a(X-V)<1, K<=a_min^2,
    V/R<=1/2, C R^2/X<=log2, V>=4(r+1)+2pi+1,

and the classical real corrected RS and sectorial gamma onsets.
For the short model use the slightly stronger cutoff-span gate of
Note04 on its original log^2 X real chart. For the polynomial far
tail impose the displayed logarithmic domination after FN27;
it is eventual because J is logarithmic and R is a positive power.

Finally require the explicit error-ledger upper expressions to satisfy

    -(3/8)L^2+(1/2)L log L+C0 L <= -(1/4)L^2,
    -(7/8)L^2+3L log L+C1 L <= -(1/2)L^2,
    -(7/8)L^2+(P-7/4)log X+5log(1+V)+C2 <= -(1/2)L^2.

The finite constants C0,C1,C2 come from the displayed real gamma,
kernel and fixed-buffer bounds. These inequalities prove the existence
and dependence of the onset; they are not a certified numerical X0.
Any refinement must retain all K,J and population factors before
claiming a smaller onset.

The source order K, common curvature order J and window V are
O(log X). This is a parameter count, **not** a useful evaluated runtime
theorem. FN25 still contains N≈sqrt(X/(4pi)) modes and a correction
integral with potentially serious cancellation. The coefficients are
given by named exact functions/derivatives; provider conditioning,
working precision and quadrature cost are not analyzed here.

FN5 is the short natural-scale result; FN26 is a different, more
elaborate outer-scale representation. The latter closes the stronger
fixed-window representation request but does not upgrade FN5's error,
prove a single leading elementary amplitude/phase, or show that a
retained correction dominates the actual field. Fixed-N charts are
differentiated with their parameters frozen; overlap comparison is
through the same H. No physical joining defect is silently removed.

Theorems here cover only `1<=T<=2`, with T independent of X. A
parameterized compact-negative-time family and its explicit endpoint
dependence remain open. The next bounded continuation is instead the
bridge `4/L_X<=T<=2`, with overlap against Note04 on `4<=T L_X<=8`.
Growing T, the negative infinite-time Gaussian overlap, regulator
layers, physical tuple transfer and all-time assembly are outside scope.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

## 9. What has been paid and what has not

| Obligation | Actual result |
| --- | --- |
| Short finite arithmetic ansatz at fixed negative time | FN5, natural nonvanishing gamma envelope; jets/time included. |
| Outer carrier accuracy for that same short ansatz | Not proved; failed allowance FN10 preserved. |
| A finite representation at outer-carrier accuracy | FN25--26, with K and J logarithmic and a retained bounded correction integral. |
| Growing RS coefficient/remainder constants | FN13--18, including Gamma(K/2) growth and odd/even sum control. |
| Arithmetic mode heat curvature | FN20--24, one n-independent analytic factor per arm, high-order Cauchy bounds and all N modes. |
| Cutoff changes | Exact real initial-data transfer in FN15; partitions independent of target/time. |
| Time derivative | Short-model residual plus heat identity for FN5; exact heat model for FN26. |
| Numerical onset, provider cost, quadrature/runtime, independent specialist review | Not supplied. |
| Complete physical density/current/covariance or all-time theorem | Not supplied. |

## 10. Controls, disposition and next owner

The collision controls are screened analytically by failed premises:
Euler-factor and RH-conditional normalized-endpoint controls do not have
the unchanged ordinary coefficients; finite weighted-square, theta-tail
and zero-tail controls do not have the same complete xi/RS identity;
reflected super-Gaussian, smooth-shape and positive-primitive controls
do not supply gamma times ordinary zeta or its full coefficient sequence;
counter-kernels, atomic/profile and finite-prime-orbit controls likewise
lack the complete canonical arithmetic/reflection premises. These
differences are exploited in FN12--14 rather than replaced by positivity
or a no-collision assumption. This is a premise screen, not a numerical
control campaign or a universal exclusion theorem.

**Disposition — Analysis, Sol:** accept FN5 and FN26, with the separate
envelopes and representation classes stated above, from the named inputs
and same-model internal assessment only. Close HDA-A02-AN01 at its
bounded `1<=T<=2` analytical scope. HDA-A02 remains **Partial** as a
broader compact-negative-time/short-formula program.

**Next — Analysis, Sol:** pay the same finite outer-scale representation
on `4/L_X<=T<=2`, explicitly accounting for the complex-kernel and
kernel-derivative losses as T decreases, then join to Note04 on the
overlap `4<=T L_X<=8`. Keep the joining derivative and actual model
residual. This targets a full buffered negative-time interval `-2<=t<=0`,
not unbounded T or physical transfer. No Astra escalation is justified
by the completed routine estimates here.

[packet]: ../research-progress/handoffs/HDA-A02-AN01.md
[inputs]: 05_FIXED_NEGATIVE_TIME_INPUTS_20261025.json
[review]: ../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md
[n03]: 03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[n04]: 04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
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
[a20]: ../../../../../avoid/20_volume_without_a_gain.md
[polymath]: https://arxiv.org/html/1904.12438v2
