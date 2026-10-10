# An exact matrix heat lift, a threshold control, and a theta remainder

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Validation below is internal.

The finite matrix lift retains a positive-time threshold collision and the
universal rank-one commutator. A genuine theta Taylor polynomial has a paid
compact approximation, but that approximation does not confer an independent
matrix constraint. This scouts program 14 of
[Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The collision targets and normalizer are those in
[Heat Note 13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md).

## 1. Finite dictionary and the time sign

Let a monic squarefree degree-d polynomial at reference time t* have roots
r_1,...,r_d. Define

\[
D=\operatorname{diag}(r_i),\qquad
C_{ij}=\frac1{r_i-r_j}\ (i\ne j),\qquad
C_{ii}=\sum_{j\ne i}\frac1{r_i-r_j}.
\]

The finite polynomial heat identity is

\[
\det(zI-D-2(t-t_*)C)
=e^{-(t-t_*)\partial_z^2}\prod_i(z-r_i).
\tag{1}
\]

This is the exact matrix theorem in
[Hall–Ho, Proposition 3.4](https://arxiv.org/html/2202.09660v3#S3.SS2),
with their time replaced by -2d(t-t*) and their matrix Y by C/d.
It is an imported finite identity, not a new arithmetic realization.
For a nonmonic polynomial multiply the determinant by the leading
coefficient; heat preserves that coefficient. The root formula needs a
squarefree reference polynomial. Multiple reference roots can be treated
by limits of squarefree polynomials for the determinant identity, but the
individual entries printed above are then undefined and are not used.

Coefficient space itself is an exact finite lift: the generator is
-D_z^2, with the nilpotent terminating exponential. No boundary domain
issue occurs there. At simple moving roots,

\[
\dot x_i=\frac{P''(x_i)}{P'(x_i)}
=2\sum_{j\ne i}(x_i-x_j)^{-1}.
\tag{2}
\]

Repulsion holds for simple real roots in increasing time. It does not
exclude a multiple root at the first all-real time; that root is the
singular initial endpoint for (2). The affine pencil remains finite there.
For real reference roots, C has antisymmetric off-diagonal entries, and
the pencil is generally not Hermitian.

The matrix relation is particularly transparent:

\[
[D,C]+I=\mathbf1\mathbf1^{\mathsf T}.
\tag{3}
\]

Off-diagonal commutator entries are one, diagonal entries zero. This
rank-one relation holds for every squarefree reference polynomial. It
cannot distinguish a theta polynomial from a collision control.
The fixed matrix C and the evolving eigenvalues of the pencil are different
objects; invariance of the former is not invariance of particle positions.

## 2. A rational matrix control at an arbitrary positive threshold

Fix T>0, a=1, t*=T+2/3, and reference roots (-3,-1,1,3). Write
tau=t-t*. The exact determinant is

\[
P_t(z)=z^4-(10+12\tau)z^2+9+20\tau+12\tau^2.
\tag{4}
\]

At t=T, tau=-2/3 and P_T=(z^2-1)^2. Equivalently, with delta=t-T,

\[
P_t=z^4-(2+12\delta)z^2+1+4\delta+12\delta^2.
\]

The discriminant as a quadratic in z^2 is 32 delta(1+3 delta).
For delta>=0 its two z^2 roots are positive. For -1/3<delta<0 they
are nonreal, and for delta<=-1/3 both are negative. Its all-real
threshold is therefore precisely T. At the positive collision x=1,

\[
P_2=8,\quad P_3=24,\quad P_4=24,\qquad
2P_3^2-3P_2P_4-9P_2^2/x^2=0.
\tag{5}
\]

This matrix has (3), exact backward heat, and the necessary threshold
sign, while retaining a freely chosen positive threshold. The scout rules
out exclusion based solely on these properties. It does not rule out a
constraint tied to the actual theta coefficients. The quartic is not a
positive theta-kernel transform.

## 3. A genuine finite preparation and its complete compact remainder

Retain the manuscript's full kernel

\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad I_j=\int_0^\infty u^j\Phi(u)\,du.
\]

The initial polynomial and exact finite heat evolution are

\[
P_{M,0}(z)=\sum_{k=0}^M\frac{(-1)^kI_{2k}z^{2k}}{(2k)!},\qquad
P_{M,t}=e^{-t\partial_z^2}P_{M,0}.
\tag{6}
\]

The arithmetic coefficients in (6) are full theta moments. This is not a
polynomial made by discarding a selected list of zeta zeros. Its leading
coefficient is nonzero because I_{2M}>0. If it is squarefree, (1) lifts it
at t*=0 after dividing by that coefficient. Squarefreeness for every M
is not asserted. At M=1 it holds directly: the reference roots are
plus/minus r with r^2=2I_0/I_2, and

\[
P_{1,t}=-(I_2/2)(z^2-r^2-2t).
\tag{7}
\]

For complex |t|<=T_0 and |z|<=R, any fixed alpha>1 and integer j>=0,
define the finite constant

\[
K_j(\alpha,R,T_0)=\int_0^\infty u^j\Phi(u)
e^{\alpha Ru+\alpha^2T_0u^2}\,du.
\]

Super-exponential theta decay makes this finite. The joint remainder is

\[
\sup|H_t^{(j)}-P_{M,t}^{(j)}|
\le\alpha^{j-2M-2}K_j(\alpha,R,T_0).
\tag{8}
\]

To prove it, expand the exact integral into the absolutely convergent
double series

\[
H_t(z)=\sum_{k,l\ge0}
\frac{(-1)^kI_{2k+2l}z^{2k}t^l}{(2k)!l!}.
\]

The finite evolution in (6) consists exactly of k+l<=M. After j spatial
derivatives, only 2k>=j remains. On the omitted set k+l>=M+1, insert
alpha^{-2(k+l)}, rescale the positive majorant by z to alpha R and t
to alpha^2 T_0, and sum it using e^{alpha Ru}. This gives (8), including
odd derivatives and derivatives that exceed the finite degree.
No heat evolution of an unpaid initial Taylor error is assumed.

For an explicit compact payment, the Gaussian scout proves

\[
\Phi(u)\le4\pi^2e^{-\pi}e^{-(4\pi-9)u-8\pi u^2},\qquad
B_j(a)=2\pi^2e^{-\pi}(8\pi-a)^{-(j+1)/2}\Gamma((j+1)/2).
\]

If alpha^2 T_0+c<8pi, Young's inequality yields

\[
K_j\le e^{\alpha^2R^2/(4c)}B_j(\alpha^2T_0+c).
\tag{9}
\]

For example |t|<=1/20, |z|<=1, alpha=2 and c=1 give
E_j<=2^{j-2M-2} e B_j(6/5), through j=6 and beyond.
These are exact compact analytic payments. They are inefficient at the
very large heights of the shrinking sector, where the factor involving
R is enormous, and supply no uniform degree or signed margin there.

## 4. Readout, normalization, and the next test

Set Q=H/A on a compact complex neighborhood where the manuscript's
normalizer is nonvanishing, and d_m=A partial_x^m(A^{-1}). The normalized
polynomial readout is P/A, with paid errors

\[
\delta_j\le |A|^{-1}\sum_{r=0}^j\binom jr|d_{j-r}|E_r.
\tag{10}
\]

The value/slope vector uses both coordinates from the same P, at fixed
time. Any fourth-jet test needs the measured quadratic payment in Note 13,
and multiplicities three/four need fifth/sixth jets and their own payments.
A determinant identity cannot replace those checks.

The executable [checker](../numerics/check_matrix_heat.py) computes the
full bivariate 4-by-4 determinant in exact rational arithmetic and checks
(4), backward heat, and the ordinary threshold collision. Its
[record](../numerics/matrix_heat_record_20261010.json) is source-hash bound.
It does not check the infinite theta state or prove (8); that bound is
derived above.

The bounded continuation is to select an independent constraint on the
theta-moment coefficients and prove that it survives the pencil readout
with (10). Neither (3), root repulsion after the threshold, nor generic
integrability supplies that constraint. This scout ends at exact finite
representation, compact approximation, and a scoped invariant obstruction.
