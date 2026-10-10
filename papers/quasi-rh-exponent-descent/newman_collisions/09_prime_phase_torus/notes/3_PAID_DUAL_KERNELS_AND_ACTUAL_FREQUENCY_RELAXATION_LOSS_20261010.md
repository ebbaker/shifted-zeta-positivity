# Paid dual kernels and loss of an actual-frequency moment relaxation

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Checks and review are internal LLM
work, not independent mathematical validation.

This continues [Note 2](2_CENTERED_COLLISION_JETS_AND_RATIO_PRODUCT_CORRELATIONS_20261010.md).
The new result is a paid family of candidate-null quadratic kernels, with
both arithmetic channels and their newly introduced sine terms retained.
It gives a concrete sufficient signed certificate. A second result solves
the associated candidate-conditioned Hilbert-space relaxation: when its
residual Gram matrix is positive definite, its sharp upper bound remains
strictly positive. A positive three-term coefficient control uses the
actual common frequency, carrier, and derivative drift and satisfies both
finite candidate equations. These results identify precisely what a
coefficient-free positivity or conditional moment-norm mechanism loses.
No signed certificate for the prescribed heat coefficients is obtained.

## 1. Candidate data and a paid quadratic dual

Retain the complete natural cutoff and all definitions of Note 2 on
`kappa in [1,3/2]`, `0<t<=1/20`. Time, integer cutoff, centering
`mu=Omega/c`, and every coefficient selected below are frozen for raw
spatial differentiation. Write

\[
\epsilon=d/c,\quad Z_1=Y_1+\epsilon X_1,\quad
e=(X_0,Z_1)^T,\quad u=(X_2,Y_3,X_4)^T,
\quad Q=\begin{pmatrix}-\Gamma&0&3/2\\0&2&0\\3/2&0&0\end{pmatrix}.
\tag{1}
\]

Thus `K=u^T Q u`. The second candidate is not `Y_1=0`:
`c Z_1=A X_0-e_1`, where `A=-d mu` and `e_1=F_N'/2`.
At a genuine heat collision its complete lower-jet tolerances are

\[
|X_0|\le a_0:=\eta_N/2,\qquad
|Z_1|\le a_1:=(L+|A|)\eta_N/(2c).
\tag{2}
\]

For any real symmetric `2 x 2` matrix `Lambda` and real `2 x 3`
matrix `B`, define the exact candidate-null modification

\[
\mathcal K_{\Lambda,B}=
\mathcal K+e^T\Lambda e+2e^TBu.
\tag{3}
\]

It agrees with `K` at both exact finite candidate equations. At a paid
genuine candidate, every discarded term is bounded by

\[
\begin{split}
\Pi_{\Lambda,B}={}&|\Lambda_{00}|a_0^2+
2|\Lambda_{01}|a_0a_1+|\Lambda_{11}|a_1^2\\
&+2\sum_{j=0}^2(a_0|B_{0j}|+a_1|B_{1j}|)|u_j|.
\end{split}
\tag{4}
\]

This uses measured complete moments. Certified moment intervals may
replace `|u_j|` by their maximum absolute endpoints. No unobserved
quadrature, complement, or amplitude drift is removed.

Keep Note 2's exact raw residuals
`E_j=2 sum w_n |P_j(v_n)-(ic rho_n)^j|`, `j=2,3,4`,
the spatial payments `j! L^j eta_N`, the exact normalizer
`gamma=18 (log A_t)''+9/x^2`, and the measured `widehat Delta`
from its equation (14). If a rigorously paid actual-phase pair estimate
gives `K_{Lambda,B}<=U_{Lambda,B}`, the useful sufficient criterion is

\[
\boxed{U_{\Lambda,B}+\Pi_{\Lambda,B}
       +\widehat\Delta/(4c^6)<0.}
\tag{5}
\]

The same parameters occur in the upper bound and payment. Choosing large
dual coefficients does not create a free negative margin. Formula (5)
includes both lower-jet tolerances and all higher raw-jet/normalizer
payments. No such negative upper bound is established below.

## 2. Four pair terms at one actual frequency

Set

\[
\mathbb Q=\begin{pmatrix}\Lambda&B\\B^T&Q\end{pmatrix},\qquad
r(\rho)=(1,\epsilon\rho,\rho^2,0,\rho^4)^T,
\quad s(\rho)=(0,\rho,0,\rho^3,0)^T.
\tag{6}
\]

The five-vector of complete moments is
`(e,u)=sum w_n [r(rho_n) cos phi_n+s(rho_n) sin phi_n]`.
For an ordered pair let

\[
R_{nm}=r_n^T\mathbb Qr_m,\quad S_{nm}=s_n^T\mathbb Qs_m,
\quad C_{nm}=r_n^T\mathbb Qs_m.
\]

Product-to-sum gives the exact kernel

\[
\begin{split}
\mathcal K_{\Lambda,B}=\sum_{n,m\le N}w_nw_m\{&
D_c(n,m)\cos(T\log(n/m))+D_s(n,m)\sin(T\log(n/m))\\
&+P_c(n,m)\cos(2\theta_t+T\log(nm))\\
&+P_s(n,m)\sin(2\theta_t+T\log(nm))\},
\end{split}
\tag{7}
\]

where

\[
D_c=(R+S)/2,\quad P_c=(R-S)/2,
\quad D_s=(C_{mn}-C_{nm})/2,\quad P_s=(C_{nm}+C_{mn})/2.
\tag{8}
\]

The sign in `D_s` is fixed by
`sin(phi_n-phi_m)=sin phi_n cos phi_m-cos phi_n sin phi_m`.
With `Lambda=B=0`, the sine terms vanish and (7) reduces exactly to
Note 2's two kernels. Generic derivative-candidate null terms introduce
the sine terms; omitting them would destroy the dual identity.

Group both difference coefficients by `n=ja,m=jb`, `(a,b)=1`, and
both product coefficients by `nm=k`, exactly as in Note 2. Each
coefficient sum retains the true pair weight

\[
w_nw_m=(nm)^{-\sigma}
 \exp\{t\log^2(nm)/8+t\log^2(n/m)/8\}.
\tag{9}
\]

Thus this is a dual family of reduced-ratio and divisor-product
correlations, all at the same `T,theta_t`. The difference sine coefficient
is antisymmetric; the ordered-pair sum retains it because its sine phase
is also antisymmetric. Diagonal pairs, product squares, and every
`B x B`, `B x C`, `C x B`, `C x C` term for the physical block
`N/2<n<=N` remain present. There are no independent prime phases.

## 3. Normalized actual-phase moment shapes and the sharp norm relaxation

This section tests a specified possible way to bound (5): retain all
actual phases and positive weights, impose both candidate coordinates,
then bound the remaining moment vector only by its optimal Hilbert-space
norm envelope. It is a relaxation, with an exactly quantified outcome.

Let `W=sum w_n`, `R_*=sqrt(sum w_n rho_n^2/W)>0`, and
`p_n=w_n/W`. Work in the real Hilbert space with
`<f,g>=sum p_n f_n g_n`. Use the five actual functions

\[
a_n=\cos\phi_n,\quad b_n=(\rho_n/R_*)
 (\sin\phi_n+\epsilon\cos\phi_n),
\]
\[
f_{2,n}=(\rho_n/R_*)^2\cos\phi_n,\quad
f_{3,n}=(\rho_n/R_*)^3\sin\phi_n,\quad
f_{4,n}=(\rho_n/R_*)^4\cos\phi_n.
\tag{10}
\]

Define `G=Gram(a,b)`, `C_{ij}=<a_i,f_j>` with
`(a_0,a_1)=(a,b)`, and `F=Gram(f_2,f_3,f_4)`.
When `G` is invertible, set

\[
H=F-C^TG^{-1}C,\quad
z=(X_0/W,Z_1/(WR_*))^T,\quad
m=(X_2/(WR_*^2),Y_3/(WR_*^3),X_4/(WR_*^4))^T,
\]
\[
v=C^TG^{-1}z,\qquad E=1-z^TG^{-1}z\ge0.
\tag{11}
\]

Projection of each `f_j` off `span(a,b)`, and projection of the
constant function `1` off the same span, prove the exact matrix inequality

\[
\boxed{(m-v)(m-v)^T\preceq E H.}
\tag{12}
\]

For a vector `ell`, this is precisely Cauchy--Schwarz for
`<1-P1,sum ell_j(f_j-Pf_j)>`. All Gram entries use the complete
actual sum. If `G` is singular, project onto its span or use its
Moore--Penrose inverse; no inverse is silently assumed to exist.

The normalized threshold is

\[
\frac{\mathcal K}{W^2R_*^6}=m^TQ_*m,
\qquad Q_*=\begin{pmatrix}-\Gamma/R_*^2&0&3/2\\
0&2&0\\3/2&0&0\end{pmatrix}.
\tag{13}
\]

At exact candidate coordinates `z=0`, the relaxation (12) has sharp
maximum

\[
\sup_{mm^T\preceq H}m^TQ_*m
=\max\{0,\lambda_{\max}(H^{1/2}Q_*H^{1/2})\}.
\tag{14}
\]

This is the maximum over a norm *ball*. It is attained by an eigenvector
when positive; zero is also feasible. If `H` is positive definite,
Sylvester inertia is `(2 positive,1 negative)`: the `f_3` entry is `2`,
and the `f_2,f_4` block has determinant `-9/4`, irrespective of
`Gamma`. Therefore the right side of (14) is **strictly positive**.
The norm relaxation cannot establish (5), even with zero lower-jet and
higher-jet errors. It has two surviving positive directions, rather than
a merely oversized absolute constant.

For paid nonzero candidates put
`lambda_+=max(0,lambda_max(H^{1/2}Q_*H^{1/2}))`. The same ball gives
the valid upper bound

\[
m^TQ_*m\le E\lambda_+
 +2\sqrt E\,\|H^{1/2}Q_*v\|+v^TQ_*v.
\tag{15}
\]

Certified bounds `|z_0|<=a_0/W`, `|z_1|<=a_1/(WR_*)`
pay every term in `v=C^TG^{-1}z`. The measured `G,C,H` and spectral
bounds would themselves need interval certification in an application;
none is claimed here. Positive definiteness is a scoped hypothesis, not
an assertion about every actual height. If the residual Gram is singular,
(14) remains the exact criterion and its sign must be checked on its
range.

This positive-definite case is bound to one genuine physical state.
At `M=N=22066`, `kappa=1`, `t=1/(2 log M)`, `x=4 pi M^2`,
the checker encloses the determinant of the five *unnormalized* feature
rows in (10) at nodes `1,2,8,128,11033` in

\[
155566620.361144435998074432064855523590911385741551051983939
\ \le\det\ \le
155566620.361144435998074432064855523590911468247325214710896.
\tag{15a}
\]

The positive interval width is less than `1e-30`. The common height,
carrier, `mu=Omega/c`, and drift are outwardly enclosed with 60-digit
Decimal arithmetic; no floating phases or independent torus variables
enter. Column scaling by powers of the positive `R_*` preserves rank.
Since every actual heat weight is strictly positive, this selected-node
witness proves that the **complete prescribed-weight** five-feature Gram
and `H` are positive definite there. It does not claim this height is a
candidate. It verifies that the relaxation's positive directions occur
for genuine arithmetic data, rather than only in a formal test model.

Adding the dual terms (3) cannot change (14) at `z=0`. Equivalently, no
choice of `Lambda,B` makes `-mathbb Q` positive semidefinite on the
whole conditioned five-moment space: its restriction to `e=0` is
`-Q`, which has two negative directions. This rules out the proposed
global quadratic/norm certificate, not a phase-sensitive signed bound
for the actual constant vector, nor a certificate using the prescribed
coefficients more strongly than (12).

## 4. A positive control at the actual common height

There is a separate coefficient-free obstruction that preserves the
common frequency rather than enlarging to independently chosen phases.
Let `h=log 2`. At any height satisfying

\[
T h=(2k+1)\pi,
\tag{16}
\]

keep the genuine `theta_t,c,d,mu,Gamma` but replace the positive
coefficients on `n=1,2,4` by `1,2,1`, and set the other coefficients
to zero. This is a nonnegative finite coefficient control; it is not the
prescribed complete heat approximant or a genuine theta collision.
For every carrier angle, its centered moments satisfy

\[
M_0=M_1=0,\quad M_2=2h^2e^{i\theta_t},\quad
M_3=6h^2(h-\mu)e^{i\theta_t},
\]
\[
M_4=2h^2\{6(h-\mu)^2+h^2\}e^{i\theta_t}.
\tag{17}
\]

Both finite candidate equations are exact for any drift `d`:
`X_0=0` and `A X_0-dX_1-cY_1=0`. Substitution gives

\[
\boxed{\mathcal K=4h^4\{18(h-\mu)^2\sin^2\theta_t
 +(18(h-\mu)^2+3h^2-\Gamma)\cos^2\theta_t\}.}
\tag{18}
\]

In particular, if `mu!=h` and `Gamma<3h^2`,

\[
\mathcal K\ge4h^4\min\{18(h-\mu)^2,
18(h-\mu)^2+3h^2-\Gamma\}>0
\tag{19}
\]

uniformly over the *genuine* carrier angle. Every candidate-null term
in (3) vanishes. The pair channels in (7) recombine to this positive
value; separate cancellations of their coefficients cannot repair it.

These phase alignments occur in the physical common-height interval for
each sufficiently small fixed `t`: `T'(x)=c>0.49`, and the interval
between `4 pi exp(1/t)` and `4 pi exp(3/(2t))` has a `T`-range longer
than `2pi/h`. Also `mu=log N+O(1/N)` grows and
`Gamma=O(x^{-2})`, so the conditions in (19) hold there. This is an
existence statement for control heights, with the actual cutoff large
enough to contain `1,2,4`; it does not locate a genuine collision.

The raw derivative convention can also be retained. At such a center
`x_*`, reweight each actual summand by a fixed constant
`a_n/w_n(x_*)`, with `(a_1,a_2,a_4)=(1,2,1)`. These constants
are frozen. Since the actual weight is
`w_n=n^{-sigma(x)} exp(t log^2 n/4)`, its full local complex sum is

\[
S_{\rm control}(x)=e^{i\theta_t(x)}(1+r(x))^2,
\quad r(x)=e^{-(\sigma(x)-\sigma(x_*))h}e^{iT(x)h}.
\tag{20}
\]

It has `r(x_*)=-1` and `r'/r=(-d+ic)h`. Thus the control follows
the same raw carrier/drift multiplier of Note 1, and both real value and
first derivative vanish exactly at the center. No claim about its global
all-real zero property or the sign of a genuine heat remainder is made.
The coefficients have been changed deliberately: a theorem using their
prescribed values can distinguish this control, while positivity,
the common orbit, and the two candidate coordinates alone cannot.

When `cos(theta_t) [sin(theta_t)+epsilon cos(theta_t)]!=0`, the
control can also have strictly positive coefficients at *every* index
up to the frozen cutoff. Assign arbitrarily small positive coefficients
to the omitted indices, keep the coefficient at `2` fixed, and adjust
those at `1,4` to restore `X_0=Z_1=0`. Their two candidate columns have
determinant

\[
2h\cos\theta_t(\sin\theta_t+\epsilon\cos\theta_t)\ne0.
\tag{21}
\]

At fixed finite `N` the corrections tend to zero with the outside mass,
so the adjusted coefficients remain positive and the strict sign (19)
persists by continuity. This is a conditional finite perturbation lemma,
not a uniform perturbation of the prescribed coefficients. Degenerate
carrier angles are covered only by the original three-term control.

## 5. Check scope and the next signed task

The [standard-library checker](../numerics/check_paid_dual_kernels.py)
and [source-bound record](../numerics/paid_dual_kernel_record_20261010.json)
check the dual identity and tolerance payment, every sine/cosine sign,
complete pair regrouping, normalized threshold scaling, Gram projection,
and exact positive/negative feasible relaxation witnesses. The three-term
control identities are checked symbolically, including their arbitrary
carrier and drift and the full-support perturbation determinant. The run
passes **495 exact assertions**, followed by the genuine-height interval
rank check (15a). Its imported interval source is hash-bound and unchanged;
a different source fails closed. The own checker locally overrides integer
interval powers by exact rational endpoint powers and directed Decimal
division, avoiding dependence on `Context.power`'s general rounding
guarantee. Rational common-frequency examples
verify algebra; only the selected-node interval determinant is certified
for genuine numerical theta-approximant phase data. Neither it nor the
formal controls certify a negative candidate sign in (5).

The most useful next task is a rigorously paid estimate of (7) with its
**prescribed** coefficients, conditional on (2), which beats (4) and the
existing `widehat Delta`. Dual parameters may be chosen to reduce a
particular actual signed ratio/product correlation, but a norm bound on
the projected shape cannot furnish the needed negative sign. Program
13's complete-cutoff current/nonvanishing certificate is complementary:
an actual finite rectangle and a sector-wide conditional theorem have
different coverage. No collision exclusion, RH, or priority claim is
made; higher multiplicity and endpoint coverage remain open.

These are small sources and records under
[LARGE_FILES.md](../../../../../LARGE_FILES.md), with no large derived
dataset. The [internal review](../reviews/3_PAID_DUAL_KERNEL_INTERNAL_REVIEW_20261010.md)
records proof obligations and the deliberately enlarged state classes.
