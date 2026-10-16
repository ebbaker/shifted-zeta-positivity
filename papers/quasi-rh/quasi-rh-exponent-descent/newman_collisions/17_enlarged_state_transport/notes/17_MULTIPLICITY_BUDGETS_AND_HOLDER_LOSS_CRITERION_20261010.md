# Multiplicity budgets and Hölder losses for the stationary collision test

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
session and is not inferred. Derivations and separate-agent checks are
internal LLM work, not independent mathematical validation.

The [bounded-loss criterion](16_NEXT_STEPS_AND_BOUNDED_LOSS_COLLISION_CRITERION_20261010.md)
can be weakened to a fixed Hölder power of the joint first-jet energy on
any region with an independent upper bound on spatial multiplicity. For the
genuine theta flow, positive source integrals supply such a bound on every
finite window. This does not prove the required signed source estimate.
The elementary multiplicity budget can be large at high height.

## A sufficient Hölder loss with a multiplicity budget

Let \(H\) be jointly real analytic, solve \(H_t=-H_{xx}\), and put
\(E=H^2+H_x^2\). Suppose every spatial zero in an open positive-time
region \(\Omega\) has multiplicity at most the integer \(M\ge2\).
Set \(r_M=\lfloor M/2\rfloor\).

**Proposition.** If, for a fixed
\[
0<\delta<\frac1{2r_M},
\tag{1}
\]
there are locally bounded nonnegative functions \(C_0,C_1\) such that
\[
H_x=0\Longrightarrow HH_{xx}\le C_0 E^{1-\delta},
\qquad
H_{xx}=0\Longrightarrow H_xH_{xxx}\le C_1 E^{1-\delta}
\tag{2}
\]
throughout \(\Omega\), then \(H=H_x=0\) has no solution there.

**Proof.** At a multiple zero of even order \(2r\), the predecessor
branch of [Note 5](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md)
has \(H_x=0\), while at an odd order \(2r+1\ge3\) the branch of
Note 16 has \(H_{xx}=0\). In either case, writing \(h=T-t\downarrow0\),
the relevant product \(P\) and energy satisfy
\[
E=c^2h^{2r}(1+O(h)),\qquad
P=rc^2h^{2r-1}(1+O(h)),\qquad c\ne0.
\]
Consequently
\[
\frac{P}{E^{1-\delta}}
=r|c|^{2\delta}h^{2r\delta-1}(1+O(h))\longrightarrow+\infty,
\tag{3}
\]
since \(r\le r_M\). Openness supplies the predecessor neighborhood,
and local boundedness contradicts (2). QED.

For small \(E\), this allows a larger loss than \(CE\). A source error
that contributes \(\sqrt E\,\epsilon\) to a product is compatible with
(2) if \(\epsilon=O(E^{1/2-\delta})\); a fixed absolute error still
does not suffice. The exponent and coefficient bound must be established
independently of division by the observed small first jet.

One can use the normalized energy \(\widetilde E=E/A^2\) and physical
normalized products \(P/A^2\), with \(A>0\) nonvanishing. A bound
\(P/A^2\le\widetilde C\widetilde E^{1-\delta}\) is equivalent to
\(P\le\widetilde C A^{2\delta}E^{1-\delta}\), and the coefficient
remains locally bounded. The jets must still be physical derivatives,
including every normalizer term.

## An independent positive theta source bound for multiplicity

For the complete genuine source,
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \Phi(u)>0\quad(u\ge0).
\]
At every real \(t\) and \(R>0\),
\[
\max_{|z|\le R}|H(t,z)|=H(t,iR),\qquad H(t,0)>0.
\tag{4}
\]
Indeed \(|\cos((v+iw)u)|^2=\cos^2(vu)+\sinh^2(wu)
\le\cosh^2(wu)\), and \(|w|\le R\). The positive integral supplies
the bound, and \(z=iR\) attains it. Both positive integrals in (4)
increase with \(t\).

Suppose a nonzero real zero \(x\) has multiplicity \(m\), and take
\(R>|x|\). Evenness gives the same multiplicity at \(-x\). The factors
\[
B_a(z)=\frac{R(z-a)}{R^2-az},\qquad a\in\mathbb R,\quad |a|<R,
\]
have modulus one on \(|z|=R\). The quotient
\(H(t,z)/(B_x(z)^mB_{-x}(z)^m)\) is holomorphic in the disk after
removing its apparent singularities. The maximum principle at zero gives
\[
H(t,0)\le H(t,iR)(|x|/R)^{2m}.
\]
Thus
\[
\boxed{
m\le\frac{\log[H(t,iR)/H(t,0)]}{2\log(R/|x|)}.}
\tag{5}
\]
This elementary argument uses no information about the other zeros and
no RH assumption.

On \(t_-\le t\le t_+\), \(|x|\le X\), with \(R>X>0\), define
\[
B_* =\frac{\log[H(t_+,iR)/H(t_-,0)]}{2\log(R/X)}.
\tag{6}
\]
Every nonzero real zero in that window has \(m\le B_*\); at zero the
function is positive. If \(U\) is a rigorously proved upper bound for
\(B_*\), the integer \(M=\max(2,\lfloor U\rfloor)\) is safe, since
\(m\) is an integer. Positive-integral enclosures or analytic source
majorants therefore yield a usable exponent in (1). No numerical value of
\(U\) is asserted in this note. A buffered finite window around every
candidate supplies the corresponding open neighborhood.

This is independent source information, but not yet the signed estimate.
The global disk used in (4) can give an inefficient \(M\) at large
height, forcing \(\delta\) close to zero. Local source estimates on
better complex disks could improve the budget.

## The exponent threshold is sharp for a multiplicity budget alone

For \(r\ge1\), consider the heat polynomial
\[
P_r(t,x)=\sum_{k=0}^r
\frac{(2r)![-(t-T)]^kx^{2r-2k}}{k!(2r-2k)!}.
\tag{7}
\]
It obeys the backward heat equation and has order \(2r\) at \((T,0)\).
Before \(T\), its coefficients are positive. Its only real first
stationary point is zero, and its second derivative has no real zero.
There the ratio in (3) is exact with \(c=(2r)!/r!\). It is locally
bounded whenever \(\delta\ge1/(2r)\).

After \(T\), write \(\tau=t-T>0\). The polynomial equals
\[
(-2\tau)^{2r}e^{x^2/(4\tau)}
\frac{d^{2r}}{dx^{2r}}e^{-x^2/(4\tau)}.
\]
Integration by parts makes it orthogonal to all lower-degree polynomials
against the positive Gaussian weight. If it had fewer than \(2r\) real
sign-changing zeros, the product of those linear factors would have lower
degree and a nonzero constant-sign weighted product with \(P_r\), a
contradiction. Hence all its roots are real and simple; Rolle's theorem
gives the same property for its derivative.

For a polynomial \(p\) with simple real roots \(r_j\), at \(p'=0\),
\[
\frac{p''}{p}=-\sum_j(x-r_j)^{-2}<0.
\]
Apply this to \(P_r\) and \(P_r'\): both stationary products after
\(T\) are favorable. At \(T\), the relevant degenerate products
vanish. Consequently (7) satisfies both local inequalities (2) at every
\(1/(2r)\le\delta<1\), despite its collision. Taking
\(r=\lfloor M/2\rfloor\) shows why the strict threshold in (1) cannot
be improved from the multiplicity budget alone.

In particular, no fixed \(\delta>0\) covers arbitrary finite
multiplicity. A subpower loss \(E\ell(1/E)\), with
\(\ell(s)=o(s^\epsilon)\) for every \(\epsilon>0\), still excludes
all finite multiplicities by (3)'s scaling argument, but supplies no new
source estimate by itself.

## Exact carrier formulation and the remaining task

With \(D,R,\mathcal R,b,B\) from
[Note 12](12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md),
the two targets become
\[
HR\le bH^2+C_0E^{1-\delta}\quad(H_x=0),
\]
\[
H_x\mathcal R\le BH_x^2+C_1E^{1-\delta}\quad(H_{xx}=0).
\tag{8}
\]
A possible source mechanism would be a predeclared exact decomposition
\(R=uH+vH_x+S\), with \(u,v\) and their first derivatives locally
bounded. Writing \(k=b'/b\), it gives
\[
\mathcal R=(u'-ku)H+(u+v'-kv)H_x+vH_{xx}+S'-kS.
\]
Independent signed bounds for \(HS\) and \(H_x(S'-kS)\) at the
respective stationary sets would then imply (8), absorbing bounded
multiples of \(E\) locally. Such coefficients must come from the
complete prepared source. Defining them through uncontrolled division by
\(E\) would be circular.

Indeed, wherever \(E>0\) is already known, the bounded-loss constants
exist automatically by local continuity. Conversely Note 16 excludes every
joint zero. The same equivalence holds here once the multiplicity budget
is imposed. Finite measured ratios alone do not establish the needed
independent source estimate.

The concrete gain is the positive-source budget (5), which permits a
predeclared Hölder exponent and weakens the required vanishing order.
No signed theta bound or additional collision-free domain is proved.
The [correlated-error analysis](18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md)
explains why an arbitrary absolute disk remainder cannot close this task.
