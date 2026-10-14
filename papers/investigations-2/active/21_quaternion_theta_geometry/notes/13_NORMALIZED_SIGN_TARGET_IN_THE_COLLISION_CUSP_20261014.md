# The normalized signed target in the possible collision cusp

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded current-turn model: **gpt-6.1-sol (Codex)**; reasoning effort:
**ultra**, verified from the local turn-context metadata.

The higher-height calculation and the shifted-contour construction
improve bounded coverage and absolute approximation, respectively. The
remaining global obligation is a signed estimate on the genuine
stationary sets. This note identifies the moving region that still needs
it and states the normalized target without assuming a physical norm
lower bound or simplicity at time zero.

## 1. A quantitative shape, with an unspecified classical constant

The primary input is [D. H. J. Polymath, Theorem 1.5(i)](https://arxiv.org/html/1904.12438v2):
for a sufficiently large absolute C>0 and 0<t<=1/2, a zero of H(t,x+iy)
with x>=exp(C/t) is real. The normalization is the manuscript's exact
H(0,z)=xi(1/2+iz/2)/8. Evenness supplies negative real parts. The theorem
states no numerical value for C; this is a qualitative localization
input, not an executable numerical cutoff.

Suppose H(T,a)=H_x(T,a)=0, 0<T<=1/2, and a is real with |a|>1.
The manuscript's proved local Hermite splitting supplies nonreal zeros
z_h of H(T-h,.) for arbitrarily small h>0, with Re z_h tending to a.
The imported localization then gives

\[
|\operatorname{Re}z_h|<\exp(C/(T-h)).
\]

Taking the limit proves the necessary condition

\[
\boxed{T\log|a|\le C.}
\tag{1}
\]

The inequality need not stay strict in the limit. No simplicity theorem
or numerical value of C is needed for this deduction. In particular,
a finite-height certificate through X_0>1 reduces a possible positive
threshold collision to

\[
|a|>X_0,\qquad 0<T\le1/2,\qquad T\log|a|\le C.
\tag{2}
\]

Choose any C'>C when prescribing an open neighborhood for stationary
signs. Then every candidate in (2), together with its sufficiently close
predecessor branches, lies in

\[
\mathcal D_{C'}=\{(t,x):0<t\le1/2,\ |x|>X_0,
                              \ t\log|x|<C'\}.
\tag{3}
\]

The existing strict bounded norm gap excludes |a|=X_0, so it supplies
spatial padding for an individual candidate. At T=1/2 its predecessor
times are smaller than 1/2. Thus signs on (3) suffice for the collision
argument even though the time ceiling is closed.

For a fixed lower time epsilon>0, (1) confines candidates to a finite
height exp(C/epsilon). As epsilon decreases to zero this height is
unbounded. No one finite rectangle, and no asymptotic argument only
uniform for t>=epsilon, covers all of (3).

## 2. Normalize physical jets before forming the observation

Put c=pi/8, x>0, and

\[
Z_k(t,x)=e^{cx}h_k(t,x),\qquad
\mathcal N=Z_0^2+Z_1^2=e^{2cx}\mathcal E,
\]
\[
\mathcal Q_j=Z_{j+1}^2-Z_jZ_{j+2}
            =e^{2cx}\mathscr L_j(H),\qquad j=0,1.
\tag{4}
\]

These are normalized physical jets, not successive ordinary derivatives
of Z_0. The exact relations are

\[
\partial_xZ_k=Z_{k+1}+cZ_k,\qquad
\partial_tZ_k=-Z_{k+2}.
\tag{5}
\]

Consequently the genuine stationary constraint is Z_(j+1)=0, equivalently
(partial_x-c)Z_j=0. Substituting ordinary stationarity partial_x Z_j=0
would change the problem. On a genuine stationary branch chi(t),

\[
\frac12\frac d{dt}Z_j(t,\chi(t))^2
=\mathcal Q_j+c\chi'(t)Z_j(t,\chi(t))^2.
\tag{6}
\]

The extra spatial-scale term in (6) matters: increasing normalized
amplitude along a moving branch is not by itself the physical signed
observation. At a fixed x, the norm identity remains

\[
\partial_t\mathcal N=-2(Z_0Z_2+Z_1Z_3),
\]

and gives 2 Q_0 on Z_1=0 and 2 Q_1 on Z_2=0.

## 3. The finite-contour remainder must still be signed

Let p_k approximate Z_k using the complete-source shifted-contour
identity, and write Z_k=p_k+r_k with |r_k|<=epsilon_k, k=0,...,3.
The bounds must include all omitted indices, the integration half-line,
retained quadrature, rounding, and whole-cell parameter variation.
On genuine stationarity Z_(j+1)=0,

\[
\mathcal Q_j=p_{j+1}^2-p_jp_{j+2}-r_{j+1}^2
-p_jr_{j+2}-p_{j+2}r_j-r_jr_{j+2}.
\tag{7}
\]

Thus a sufficient nonnegative signed target is

\[
p_{j+1}^2-p_jp_{j+2}\ge
\epsilon_{j+1}^2+|p_j|\epsilon_{j+2}
+|p_{j+2}|\epsilon_j+\epsilon_j\epsilon_{j+2}
\quad\text{on }Z_{j+1}=0.
\tag{8}
\]

Every cross term in the retained sum remains in the left side of (8).
The contour construction supplies an error payment, not this sign.
A variable shift a(x) is selected only after fixing the physical jet
identity; derivatives of the finite approximation with its selected
cutoff and shift are not automatically the other p_k.

A locally bounded-loss alternative can be certified without division.
If L_k=max(0,|p_k|-epsilon_k), put N_low=L_0^2+L_1^2. For an explicit
K_j>=0, the direct sufficient condition

\[
p_{j+1}^2-p_jp_{j+2}-E_j+K_jN_{\rm low}\ge0,
\quad
E_j=\epsilon_{j+1}^2+|p_j|\epsilon_{j+2}
+|p_{j+2}|\epsilon_j+\epsilon_j\epsilon_{j+2}
\tag{9}
\]

implies Q_j>=-K_j N on the genuine stationary set. A cell version uses
its interval lower bound for the signed expression and certified upper
bounds in E_j. For an interval enclosure P_k of the retained jet, replace
|p_k| in L_k by dist(0,P_k); an upper endpoint for |P_k| is used in E_j.
The prescribed coefficients K_j must remain locally
bounded through every possible joint zero. Defining K_j as an
uncontrolled quotient by N would not establish that property.

There is also a stronger direct norm test N_low>0, useful on bounded
cells. For the global criterion no lower bound uniform in height is
required. The needed conditions are restricted to positive time; a
strict gap on the entire closed t=0 boundary would additionally exclude
time-zero multiple zeros, which RH alone does not require.

## 4. What is and is not reduced

Equation (1) narrows the possible collision region, and adaptive contour
shifting can pay absolute error on its natural exponential scale. A
proof of (8), or of the locally bounded form (9), throughout the padded
moving region (3) would complete the stationary collision route.
Neither follows from the localization theorem, the ability to make
absolute quadrature error small, or the regularity of the quaternion
lift. The unresolved arithmetic content is now the retained normalized
signed surplus in this moving small-time region.
