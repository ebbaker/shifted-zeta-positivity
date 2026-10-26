# Negative-time bridge and a paid time join through zero

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from this turn's metadata. Ansatz chat0001, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Status: proved in-note from the named inputs of Notes04--05;
same-model internal assessment only.** This returns
[HDA-A02-AN02 r1][packet]. The unchanged finite representation of
Note05 extends to `4/L_X<=T<=2` at outer-carrier precision. A time-only
join with Note04 supplies full fixed-buffer field, spatial j<=3 and
first time estimates on **`-2<=t<=0`**, with its actual heat residual
paid. No physical observable transfer or all-real-time theorem follows.

The [input manifest][inputs] pins opening versions. [Assessment05][review]
records internal acceptance; the [chat-wide summary][summary] distinguishes
all results obtained in this conversation. No numerical, symbolic,
exact-arithmetic or interval research was executed. Finite onsets and
constants remain analytical, without an evaluated X0.

## 1. Frozen contract and the gain over Note05

Keep the complete canonical H, `H_t=-H_zz`, and
`H(0,z)=xi((1+iz)/2)/8`, with

\[
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad
\alpha=M'/M,\quad s(z)=(1+iz)/2.
\tag{NB1}
\]

The physical `q=epsilon_g^2`, fixed averaging kernel `K_phys=k_ell k_h`,
unnormalized observables, signed covariance and regulator are unchanged.
No root simplicity or collision-exclusion premise is introduced.

On a right chart fix `r,b>0`, with physical choice `r=ell+2`,
`b=1+h+2` and one extra analytic unit. Let

\[
\Omega_X=\{|\Re z-X|\le r,\ |\Im z|\le b\},\quad
L=\log(X/(4\pi)),\quad \Lambda=1+L,
\]
\[
N=\lfloor\sqrt{X/(4\pi)}\rfloor,\quad K=\lceil L\rceil,
\quad J=\lceil3L\rceil,\quad V=8L,\quad R=X^{1/3}.
\tag{NB2}
\]

Here K is the RS order, not K_phys. Every parameter in NB2 is frozen
at X, independently of z,T. In particular no derivative of a floor,
window endpoint or order occurs. Set
`G(z)=[M(s(z))M(1-s(z))]^(1/2)` using the branch positive on the real
segment, and keep the elementary arm envelope
`E_o=|C_+|+|C_-|` from Note03.

We will use, uniformly for **all** `0<=T<=2`,

\[
E_o(-T,z)\ge c_{r,b}G(X)e^{-TL^2/16}.
\tag{NB3}
\]

This is an elementary envelope calculation, not reuse of Note05's
`T>=1` constant. Indeed `E_o=|A_o| cosh(Im Theta_o)>=|A_o|` and
`Log(z/(4pi))=L+O_{r,b}(1/X)`. The explicit amplitude and sectorial
gamma calibration give
`|A_o(-T,z)| asymp G(X) exp[-TL^2/16+pi^2 T/64]` on fixed charts.
Its error is bounded uniformly for bounded T. No true field or cosine
is a denominator.

Note05 FN25 defines the finite model `Fhat_X`: all N arithmetic modes
are replaced by finite Gaussian moments of a common gamma-curvature
polynomial, and a bounded real-initial-data correction integral retains
all K+1 RS terms and exact adjacent cutoff transfer. Those definitions
are unchanged here. Note05 FN26 covers only `1<=T<=2`; below we prove
the missing uniformity as T decreases.

This is an approximation milestone under [avoid/01][a01]. Read the
[result index][results], [heat-flow cluster11][r11], [collision controls12][controls]
and [avoid index][avoid], especially [05][a05], [07][a07], [08][a08],
[12][a12], [16][a16] and [19][a19]. The control premises are screened
in Section8; this is not an RH criterion.

## 2. Complex kernel and every inverse-time factor

Write `d=z-X=a+iy`, `q=u-X`, and

\[
\mathsf k_T(d-q)=(4\pi T)^{-1/2}e^{-(d-q)^2/(4T)},
\quad
D_j(T,B)=T^{-j/2}(1+B/\sqrt T)^j,\quad D_0=1,
\tag{NB4}
\]

where B is one fixed number at least `r+b+1`. The exact real-initial-value
identity of Note05 FN4 is valid at every T>0 and complex z:

\[
H(-T,z)=\int_\mathbb R\mathsf k_T(d-q)H(0,X+q)\,dq.
\tag{NB5}
\]

Its kernel modulus is exactly
`(4pi T)^-1/2 exp(y^2/(4T)) exp(-(q-a)^2/(4T))`.
For each fixed c>=0 and 0<=j<=3, Hermite differentiation and Gaussian
rescaling prove

\[
\int_\mathbb R |\partial_z^j\mathsf k_T(d-q)|e^{c|q|}\,dq
 \le C_{r,b,c,j}e^{b^2/(4T)}D_j(T,B),\quad0<T\le2.
\tag{NB6}
\]

To see the complete payment, substitute `q=a+sqrt T v`. The original
normalization T^-1/2 is canceled by dq only at this step. Differentiation
costs T^-j/2 times a fixed degree-j polynomial in `v-iy/sqrt T`.
Its modulus is at most
`C_j(1+|v|)^j(1+B/sqrt T)^j`. Also
`e^{c|q|}<=e^{cr}e^{c sqrt2 |v|}`. The remaining normalized Gaussian
moment is finite independently of T. No inverse-time loss is declared
bounded before this integration. In particular

\[
e^{b^2/(4T)}\le e^{b^2L/16},\qquad
D_j(T,B)\le C_{B,j}\Lambda^j,\qquad 4/L\le T\le2.
\tag{NB7}
\]

The transverse cost is a fixed height power; derivative costs are
logarithmic powers. The direct first T derivative has exactly the j=2
kernel, since `partial_T k_T=partial_zz k_T`; equivalently its explicit
factor is `-1/(2T)+(d-q)^2/(4T^2)`. Thus NB6 with j=2 also pays
direct time differentiation. We will use the exact heat identity only
after proving the corresponding field/spatial comparisons.

## 3. Uniform source remainder and exact cutoff transfer

Retain Note05's real initial data f_K and Q_XK on `I_X=[X-V,X+V]`:

\[
f_K=S_N+Q_{X,K},\quad
Q_{X,K}=S_{m(u)}-S_N+R_{m(u),K},\quad m(u)=\lfloor\sqrt{u/(4\pi)}\rfloor.
\tag{NB8}
\]

The full transfer `S_m-S_N` is exact. Its real integration partitions
are independent of z,T, and at most one adjacent mode is present
after the cutoff-span gate. Real parts remain inside the real initial
data, before multiplication by the complex kernel. They are never taken
after target-dependent complex integration.

The imported classical bound is precisely Note05 FN13--14, including
`Gamma((K+1)/2)` growth. Put `a_min=sqrt((X-V)/(4pi))` and

\[
\mathcal A_K=X^{-1/4}\Gamma((K+1)/2)(1.1/a_{\min})^{K+1}.
\]

NB6 and `G(X+q)<=CG(X)e^{c|q|}` on the window give

\[
\left|\partial_z^j\int_{I_X}\mathsf k_T(z-u)
             [H(0,u)-f_K(u)]\,du\right|
 \le C_jG(X)\mathcal A_K e^{b^2/(4T)}D_j(T,B).
\tag{NB9}
\]

After NB3 and `K=ceil L`, the logarithm of its outer-relative bound is
at most

\[
-\tfrac38L^2+\tfrac12L\log L+C_{r,b,j}L+j\log\Lambda.
\tag{NB10}
\]

The coefficient ratios and K-uniform size control of Note05 are
unchanged. NB10 pays both their growing-order remainder constant and
the new transverse/derivative factors. Its leading coefficient is
strictly more negative than -1/4.

## 4. Full arithmetic heat curvature and artificial tails

Use exactly Note05 FN20--22: the n-independent analytic factors
`A_epsilon(q)`, exact Taylor coefficients a_epsilon,k, degree-J
polynomials P_epsilon,J, and finite Gaussian-moment sum M_XNJ.
Their complex disk `|q|<=R` has `sup|A_epsilon|<=2`, so

\[
|a_{\epsilon k}|\le2R^{-k},\qquad
|A_\epsilon-P_{\epsilon,J}|\le4(V/R)^{J+1}\quad(|q|\le V).
\tag{NB11}
\]

These bounds are uniform in J. The entire initial population is
`sum_epsilon,n<=N |h_epsilon,n|<=CG(X)X^1/4`, and all real tilts
`Re lambda_epsilon,n=-pi/8+O(1/X)` are uniformly bounded. Thus NB6
pays the local arithmetic error. Including the artificial tails,
the difference between the true arithmetic convolution on I_X and
the completed Gaussian moments has j<=3 error at most

\[
C_jG(X)X^{1/4}e^{b^2/(4T)}D_j(T,B)
 \left[(V/R)^{J+1}+e^{-V^2/64}+e^{-R^2/128}\right].
\tag{NB12}
\]

For completeness, impose `V>=8r` and `R/2>=8r`. On either tail,
`(q-a)^2>=3q^2/4`. On `V<|q|<=R/2`, `|P|<=4`. On the far ray,

\[
|P_{\epsilon,J}(q)|\le2(J+1)\max(1,(|q|/R)^J).
\]

After extracting D_j, the remaining Hermite factor is at most
`C_{B,j}(1+|q|)^j`: divide its degree-j polynomial by
`(1+B/sqrt T)^j`, and use `sqrt T+B>=B`. Its bound is now explicitly
independent of T. The logarithm of the degree-J polynomial, the bounded
real tilt and this fixed degree-j factor are eventually at most `q^2/(16T)` together.
This is uniform for all `|q|>R/2` and 0<T<=2: at T=2 it follows
from `J=O(log X)<<R^2`, while the rescaled Hermite polynomial is
dominated by its Gaussian uniformly as `|q|/sqrt T` grows. The same
argument on the near tail has no degree-J factor. The remaining
integrand is bounded by the normalized Gaussian `exp(-q^2/(8T))`,
apart from the displayed transverse and D_j factors. Splitting its
exponent and rescaling yields `C exp(-a_0^2/(16T))` for tail edge a_0.
For `a_0=V` this is stronger than `exp(-V^2/64)`; for `a_0=R/2`
it is at most `exp(-R^2/128)`. This proves the artificial terms in NB12
without extending the true RS correction to unbounded arguments.

After outer conversion, NB12's local logarithm is at most

\[
-\tfrac78L^2+3L\log L+C_{r,b,j}L+j\log\Lambda.
\tag{NB13}
\]

The near artificial tail has leading exponent at most -7/8 L^2,
and the far one is smaller than every inverse height power. All are
eventually bounded by `C E_o exp(-L^2/2)`.

## 5. Both genuine source tails

For `V<|q|<=X/2`, retain the real height exponential from Note05:

\[
|H(0,X+q)|\le C X^P e^{-\pi X/8+\pi|q|/8},\quad P=4\text{ suffices}.
\]

Take V large enough compared with fixed r and the source tilt. As in
Section4, its linear exponential and the degree-j kernel factor can be
absorbed while leaving `exp(-q^2/(8T))`. Gaussian splitting pays the
tail and normalization. The outer-relative result, uniformly j<=3, is

\[
C_j X^{P-7/4}D_j(T,B)
 \exp\{TL^2/16+b^2/(4T)-V^2/(16T)\}.
\tag{NB14}
\]

Its worst leading coefficient on the entire bridge is -15/8 L^2,
since T<=2 and V=8L. The additional height powers, transverse loss
and derivatives contribute only O_{r,b,j}(L+log L).

Only for `|q|>X/2` use the global real bound
`|H(0,u)|<=integral|Phi|`. The same rescaled derivative calculation
gives the safe outer-relative allowance

\[
C_jX^{-7/4}D_j(T,B)
 \exp\{\pi X/8+TL^2/16+b^2/(4T)-X^2/(128T)\}.
\tag{NB15}
\]

It is super-Gaussian after NB7, uniformly on this bridge. The global
source bound has not been used at the nearer edge V. All genuine and
artificial tails, source growth, gamma population and new T factors
have now been paid.

## 6. Bridge theorem, heat identity and onsets

Combining NB9--15 proves, for the **unchanged** Note05 model,

\[
\boxed{|\partial_z^j(H-\widehat F_X)(-T,z)|
 \le C_{r,b,j}E_o(-T,z)e^{-L^2/4},\quad 0\le j\le3,\quad4/L\le T\le2.}
\tag{NB16}
\]

For each frozen X the bounded initial-data integral and every completed
exponential-polynomial transform are entire in z and smooth for T>0.
Dominated differentiation holds on compact positive-T subintervals;
the explicit NB6 estimates give the required uniformity on the moving
domain. The domain constraint `T>=4/L` is not differentiated. Their
fixed data and endpoints give exactly

\[
(\partial_t+\partial_{zz})\widehat F_X=0,\qquad
|\partial_t(H-\widehat F_X)|\le C_{r,b}E_o e^{-L^2/4}.
\tag{NB17}
\]

The second conclusion consumes the proved j=2 comparison. It is also
consistent with the direct kernel calculation in Section2. A zero
residual has not been substituted for a field estimate.

Choose X0 larger than the Note05 zero-time and sectorial gamma onsets,
all its order/window gates, and the following eventual gates:

    L>=16, V>=8r, R/2>=8r, X>=16(r+1),
    the polynomial/tilt domination in Sections4--5,
    -(3/8)L^2+(1/2)L log L+C0 L+3log Lambda <= -(1/4)L^2,
    -(7/8)L^2+3L log L+C1 L+3log Lambda <= -(1/2)L^2,
    -(15/8)L^2+C2 L+3log Lambda <= -(1/2)L^2.

Also impose NB15 below the same final allowance; its negative quadratic
in X makes this eventual. The constants depend on the fixed buffers
and classical inputs, not on T,X,K,J once these gates hold. These are
finite analytical onset specifications, not a numerical certificate.

## 7. A time-only join and its actual heat residual

Let F_c be **exactly** Note04 CS4, and F_b=Fhat_X. Choose the fixed
smooth step

\[
g(v)=\begin{cases}e^{-1/v},&v>0,\\0,&v\le0,\end{cases}\qquad
\chi(s)=\frac{g(s-4)}{g(s-4)+g(8-s)}.
\tag{NB18}
\]

It has `0<=chi<=1`, is zero for s<=4, one for s>=8, and is flat
at both endpoints. It depends on time only through s=TL_X on each
frozen chart. Define the join piecewise:

\[
F_\mathrm j(-T,z)=
\begin{cases}
 F_c(-T,z),&0\le TL\le4,\\
 (1-\chi(TL))F_c(-T,z)+\chi(TL)F_b(-T,z),&4<TL<8,\\
 F_b(-T,z),&8\le TL,\ T\le2.
\end{cases}
\tag{NB19}
\]

This avoids `0 times F_b(0,z)`, which would refer to an undefined
T=0 formula. Near zero the join is exactly F_c and inherits Note04's
through-zero differentiability. Flatness joins the other endpoints.
It is holomorphic in z; no spatial cutoff derivative is present.

Write `theta=chi(TL)`, `a=1-theta`,
`delta=X^-3/4 exp(TL^2/16)` only on TL<=8, and `rho=exp(-L^2/4)`
only on TL>=4. In the formulas below absent branch terms are omitted,
not evaluated outside their proved domains. Comparing both models
to the same H gives, on the overlap, `|F_b-F_c|<=C E_o(delta+rho)`.
For 0<=T<=2 the precise joined allowances are

\[
|\partial_z^j(H-F_\mathrm j)|
 \le C_jE_o\{a\delta\Lambda^j+\theta\rho\},\qquad0\le j\le3,
\tag{NB20}
\]
\[
|\partial_t(H-F_\mathrm j)|\le CE_o\{
 a\delta\Lambda^2+\theta\rho+
 L|\chi'(TL)|(\delta+\rho)\}.
\tag{NB21}
\]

To check the sign and the missing-term risk, set E_c=H-F_c,
E_b=H-F_b. Since `partial_t theta=-L chi'(TL)`, exactly

\[
\partial_t(H-F_\mathrm j)
=a\partial_tE_c+\theta\partial_tE_b
 +L\chi'(TL)(E_c-E_b).
\tag{NB22}
\]

Here `E_c-E_b=F_b-F_c`. NB21 pays its derivative-of-chi term using
the **field** comparison, not a differentiated error allowance.

Let `R_c=(partial_t+partial_zz)F_c`. Note04 CS28 gives
`|R_c|<=C E_o delta Lambda`. The actual joined residual is

\[
\boxed{R_\mathrm j=(\partial_t+\partial_{zz})F_\mathrm j
 =aR_c-L\chi'(TL)(F_b-F_c),}
\]
\[
\boxed{|R_\mathrm j|\le CE_o\{
 a\delta\Lambda+L|\chi'(TL)|(\delta+\rho)\}.}
\tag{NB23}
\]

Only the derivative-of-chi contribution is confined to 4<TL<8.
The crossover residual persists for TL<=4; the **total** residual
vanishes for TL>=8, not throughout the joined interval. This residual
identity also checks the direct time estimate through the exact H
heat identity and NB20 with j=2.

In particular `delta<=C X^-1/4` for TL<=8, and bounded chi,chi'
give the simple uniform summary on the whole negative interval:

\[
\boxed{|\partial_z^j(H-F_\mathrm j)|
 \le C_j E_o X^{-1/4}\Lambda^j,\quad0\le j\le3,\quad-2\le t\le0,}
\]
\[
\boxed{|\partial_t(H-F_\mathrm j)|\le CE_oX^{-1/4}\Lambda^2,
 \qquad |R_\mathrm j|\le CE_oX^{-1/4}\Lambda.}
\tag{NB24}
\]

All these relative errors tend to zero. NB20--23 retain stronger
pointwise information: at T=0 delta=X^-3/4; for TL<=4,
delta<=C X^-1/2; for TL>=8 the field/jet/time allowances are rho
and the residual is exactly zero. The estimates are chartwise; comparing
overlapping charts through H does not perform a physical spatial join.
Reflection supplies the left-height tail with reflected frozen charts.

## 8. Scope, control screen and disposition

The actual gain is a full fixed-buffer **negative interval [-2,0]**,
including its overlap and direct time defect, rather than two disjoint
negative-time regions. No result is obtained for T>2, growing T,
arbitrary compact endpoints or the negative infinite-time Gaussian
overlap. Note05's short gamma-scale formula is still a different
representation with a different error scale; NB16 does not strengthen
its outer allowance or prove correction dominance.

The finite model still has all N~sqrt X modes, growing K,J and a
bounded correction integral. Provider conditioning, working precision,
quadrature cost and useful runtime are not analyzed. No physical
U,W,R,J,Q transfer, near-zero collar theorem, root simplicity, RH
conclusion or independent specialist review is supplied.

The collision-control screen is unchanged but explicit: Euler-factor
and normalized-endpoint controls lack the unchanged ordinary Dirichlet
coefficients; finite weighted-square, theta-tail and zero-tail controls
lack the full canonical xi/RS identity; reflected super-Gaussian,
smooth-shape and positive-primitive controls lack the same gamma-times-
ordinary-zeta completion and tail; counter-kernel, atomic/profile and
finite-prime-orbit controls lack the full canonical coefficient/reflection
premises. NB8--10 use these complete source-specific inputs. A Gaussian
kernel or positivity alone would not do so. This is an analytical
premise screen, not a new numerical campaign or universal exclusion.

**Disposition — Analysis, Sol:** accept NB16--17 and NB20--24 at the
stated scales, with same-model internal review only. Close
HDA-A02-AN02 r1 at its bounded bridge-and-join analytical scope.
HDA-A02 remains **Partial** as a broader negative-time/short-formula
program. Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
remain unchanged.

**Next — Analysis, Sol:** the separate HDA-A03 regulator branch: obtain
a corrected one-arm comparison on one bounded switch neighborhood and
quantify the corresponding center changes against the actual physical
rounding scale, retaining the exact regulator and named center definition.
The [next frozen packet][next] is prepared, not dispatched. General
compact-negative-time parameterization remains possible follow-through,
but the new packet targets the distinct regulator accuracy gap. No
specific resistant estimate here warrants Astra escalation.

[packet]: ../research-progress/handoffs/HDA-A02-AN02.md
[inputs]: 06_NEGATIVE_BRIDGE_INPUTS_20261025.json
[review]: ../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md
[summary]: 07_CHAT0001_RESEARCH_SUMMARY_20261025.md
[next]: ../research-progress/handoffs/HDA-A03-AN01.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a19]: ../../../../../avoid/19_status_files_that_lag_the_findings.md
