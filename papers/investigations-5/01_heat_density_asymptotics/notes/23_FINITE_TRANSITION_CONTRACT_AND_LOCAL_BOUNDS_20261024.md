# Finite-transition contract and source-local comparison bounds

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this chat's session metadata.

**Status: HDA-15 completed at its declared analytical scope; bounds proved
in-note, with a bounded floating diagnostic and same-assistant review.** This is HDA-15, a quantitative
approximation milestone under [avoid 01][a01]. It does not complete HDA-17
or an all-time approximation. Read the [result index][results],
[heat-flow cluster][geometry], [collision controls][controls] and
[avoid index][avoid]. The starting estimates are [Note 20][fb], FB8--FB13.

**Current continuation:** [Note 24](24_CONTINUATION_FOR_GPT_ASTRA_INFINITE_HEIGHT_ANALYSIS_20261024.md) records the Astra infinite-height
starting point and manual Sol handoff rules. The author's earlier priority
amendment remains in [Note 22](22_CONTINUATION_FOR_FINITE_TRANSITION_CONTRACT_20261024.md).
The results and failed trial below retain their original scope. Further
numerical refinement must serve a named analytical estimate; the bounded
trial is not the default next task.

## 1. Contract fixed before the diagnostic

Use the physical density and common regulator of Note 20, without mass
normalization. Fix

\[
 I=[-16,64],\quad D=[-8,8]\times[-1/2,1/2],\quad
 D^+=[-10,10]\times[-1,1],\quad \eta=1/2.
\tag{LC1}
\]

Use spatial averaging only, with

\[
 k(v)=\frac{315}{256}(1-v^2)^4\mathbf1_{|v|\le1},\qquad
 K(x,y)=\frac1{\ell_x\ell_y}k(x/\ell_x)k(y/\ell_y),\quad
 (\ell_x,\ell_y)=(2,1/2).
\]

Thus D+ is the full convolution buffer, including boundary points of D.
This first trial includes both heat signs and positive saddle formation;
it deliberately stops before the regulator develops spatial dependence.
It is not asserted to span the entire endpoint-to-endpoint transition.
On I, epsilon_g=eta C(1+t^2)^(-1/4), C=Phi(0)sqrt(pi)/2,
r_t=-t/(1+t^2), r_x=r_y=0. Consequently the spatial curvature correction
C_curv is exactly zero, B=r_t w, and the adaptive current source is
s=r_t(1-2w)rho. The time-dependent regulator terms remain present.

The norm is the absolute supremum on I x D, including its time and spatial
boundary. The prospective component tolerances are fixed as follows:

| Components | Absolute tolerance |
| --- | --- |
| R, complex J, R_t, U, U_t, U_x, U_y, W=K*w, K*s | 10^-4 each |
| actual Q | 10^-3 |
| actual Delta Q | 10^-2 |

The complex current is j=q H_zz conjugate(H_z)/(pi D_H^2), where
D_H=|H|^2+q; the real flux is (Re j, Im j), since
2 Re(partial_z j)=partial_x Re j+partial_y Im j.
For alpha a spatial multi-index, put L_alpha=||partial^alpha K||_1.
Also require errors <=L_alpha*10^-4 for partial^alpha R (1<=|alpha|<=2),
partial^alpha J (|alpha|=1), partial^alpha U (2<=|alpha|<=4), and
partial^alpha W (1<=|alpha|<=2). U_x,U_y keep their stricter tabulated
thresholds. The fourth derivatives of this compact C3 kernel are
integrable weak derivatives; no boundary delta occurs at that order.
All these are fixed, nonvanishing reference scales, not errors divided
by observed values. Boundary U, its normal derivative and normal current
inherit the corresponding component tolerances from the supplied buffer.
Initial/final time traces are part of the same sup norm.

These quantities cover P3a--P5a in the [overview][overview]:
Delta U=4pi R, the potential equation includes r_t W, the density equation
includes r_t Delta W/(4pi), and current balance includes K*s. There is no
unpaid curvature derivative on this slab because C_curv is identically
zero. On a later slab, both curvature derivatives and spatial regulator
sources must be restored. Exact source fields satisfy these equations
exactly; numerical evaluation of them needs the stated derivative budgets.

For a future acceptance test reserve 80% of each threshold for the
analytical source/nonlinear allowance, 10% for nodal/field arithmetic,
and 10% for filter integration. No unused category is silently set to zero.
The present diagnostic fixes U_s=3/2, N=4, and uniform meshes of 48, 96
and 192 cells. It measures costs, not HDA-17 acceptance. The small fixed
sample set and any refinement failures are retained in its record.

## 2. Cellwise source and nodal errors

Write [a_i,b_i]=[u_i,u_(i+1)], h_i=b_i-a_i, and let B_i bound
sup_[a_i,b_i]|Phi''|. Let f interpolate implemented values v_i satisfying
|v_i-Phi_N(u_i)|<=sigma_i. Positivity of f must be checked or ensured
if arithmetic values replace the exact positive nodal values.
For t<=b and |y|<=Y use the positive weight
W_j(u;t,Y)=u^j exp(t u^2+Yu). A time tile uses its upper endpoint in
this weight; no sampling in time is used to justify that replacement.
Let l_i be the usual piecewise linear nodal hat. Then

\[
\begin{split}
 \delta_j^{\rm cell}(t,Y)&=I_j+M_j+A_j+T_j,\\
 I_j&=\frac12\sum_i B_i\int_{a_i}^{b_i}
       (u-a_i)(b_i-u)W_j(u;t,Y)\,du,\\
 M_j&=\sum_i\tau_N(u_i)\int_0^{U_s}l_i(u)W_j(u;t,Y)\,du,\\
 A_j&=\sum_i\sigma_i\int_0^{U_s}l_i(u)W_j(u;t,Y)\,du.
\end{split}\tag{LC2}
\]

Here T_j is FB7 with s=max(t,0), assuming its gates, and

\[
 \tau_N(v)=\frac{2\pi^2(N+1)^4
       e^{9v-\pi(N+1)^2e^{4v}}}{1-r_N(v)},\qquad
 r_N(v)=\left(1+\frac1{N+1}\right)^4e^{-\pi(2N+3)e^{4v}}.
\tag{LC3}
\]

**Claim.** |partial_z^j(H-H_f)|<=delta_j^cell for j=0,1,2,3,
uniformly in every real x and on the declared time tile/transverse strip.
The same statement holds for higher fixed j if the corresponding tail
and weights are supplied.

**Proof.** Apply the elementary interpolation remainder to the complete
Phi, so |Phi-LPhi|<=B_i(u-a_i)(b_i-u)/2. The difference between LPhi
and f is bounded by the positive hats times tau_N(u_i)+sigma_i. Every
omitted source term is positive and bounded by its leading term;
consecutive leading-term ratios decrease with the mode and are <=r_N(v).
Their geometric sum proves LC3. Integrate the three errors against W_j,
using |partial_z^j cos(zu)|<=u^j exp(Yu), and add the complete tail.
This also proves that a time tile is covered between its endpoints. No
oscillatory cancellation or root information is assumed.

All LC2 weights are finite Gaussian moments. A fully elementary upper
bound avoids quadrature: let V_ij=max_[a_i,b_i] W_j. Replace the three
cell contributions by

\[
 \widehat I_j=\sum_i B_i h_i^3V_{ij}/12,\quad
 \widehat M_j=\sum_i\frac{h_iV_{ij}}2
       (\tau_N(a_i)+\tau_N(b_i)),\quad
 \widehat A_j=\sum_i\frac{h_iV_{ij}}2(\sigma_i+\sigma_{i+1}).
\tag{LC4}
\]

The maximum V_ij is attained at an endpoint or at a positive solution of
2t u^2+Yu+j=0 (with the regular u=0 limit when j=0). For t>=0 it is
simply W_j(b_i). Thus the formulas can be enclosed without source/filter
quadrature. To guarantee a no-worse allowance even for a coarse mesh, take
the minimum of LC4 plus T_j and FB8 including the same arithmetic terms.

### An explicit complete-source cell constant

For p in {5/4,9/4,13/4,17/4}, let c_p=(75,330,224,32),
A_n=pi n^2 exp(4a_i), B_n=pi n^2 exp(4b_i), and
m_p(A,B)=[clamp(p,A,B)]^p exp(-clamp(p,A,B)). Then

\[
 B_i=\pi^{-1/4}\sum_{n\ge1}n^{-1/2}
       \sum_p c_p m_p(A_n,B_n)
\tag{LC5}
\]

is valid. Indeed the exact differentiated summand is
pi^(-1/4)n^(-1/2)e^-A[-75 A^(5/4)+330 A^(9/4)-224 A^(13/4)+32 A^(17/4)].
Bounding its four monomials on the cell proves LC5. For evaluation through
n=N_B>=1, the omitted sum is bounded by its n=N_B+1 expression at a_i,
divided by 1-r_i^B, where
r_i^B=(1+1/(N_B+1))^8 exp[-pi(2N_B+3)exp(4a_i)]<1.
All omitted A_n exceed 17/4, so each monomial decreases in u, and the
mode ratios give this tail. Every theta mode is retained analytically.

### Quantitative gain over the global allowance

For the infinite-series definitions, B_i<=B_2 and tau_N(u_i)<=tau_N(0).
LC2 is therefore no larger than FB8 with the same h=max h_i, cutoff,
mode count, time ceiling, and nodal sup error. Unlike a fixed global
nodal arithmetic allowance, relative nodal errors sigma_i<=gamma Phi_N(u_i)
also retain the source decay through A_j; this is a hypothesis to verify,
not an assumption that floating evaluation is certified.

There is a stronger cutoff distinction. For fixed finite t,Y,j and
0<h_i<=h_0, the coefficient of h^2 in LC2's interpolation bound stays
bounded as U_s grows. To prove it, bound B_i at u by the supremum of
the positive derivative envelope over |v-u|<=h_0, v>=0. On the far tail
it is a polynomial in exp(4(u+h_0)) times exp[-pi exp(4(u-h_0))],
which is integrable against W_j. Then I_j<=h^2/8 times that integral.
The analogous hat envelope proves boundedness of M_j and of A_j under
the stated relative nodal hypothesis. In contrast, B_2 h^2 F_j/8 diverges
with U_s for t>0 (and also for t=0,Y>=0). This removes an artificial
cutoff amplification; it does not eliminate true growth with positive t,
the h^2 interpolation order, or the other error categories.

## 3. Amplitude-aware nonlinear transfer, including zeros

At a fixed point write g=H_f, g_j=partial_z^j H_f,
q=epsilon_g^2, d_j>=|partial_z^j(H-H_f)|, P_j=|g_j|+d_j,
m=(|g|-d_0)_+, M=|g|+d_0, and D_*=q+m^2. Define maxima on [m,M]:

\[
 A_*={q\over\pi D_*^2},\quad
 A_1=\max_v{4qv\over\pi(q+v^2)^3},\quad
 a_* =\max_v {v\over q+v^2},\quad b_*={1\over D_*},\quad
 w_1=\max_v {2qv\over(q+v^2)^2}.
\tag{LC6}
\]

The maxima occur at the clamped points epsilon/sqrt(5), epsilon,
and epsilon/sqrt(3), respectively. These positive denominators remain
valid at zeros and multiple events, including when d_0>=|g|.
Along the segment g+theta(H-g), LC6 bounds A, |grad A|,
|h/(|h|^2+q)|, the derivative norm of that last map, and |grad w|.
The last map has radial eigenvalues (q-v^2)/(q+v^2)^2 and 1/(q+v^2),
so b_* is valid.

Set

\[
\begin{split}
 E_\rho&=2A_*P_1d_1+A_1P_1^2d_0,\\
 E_j&=A_*(P_1d_2+P_2d_1)+A_1P_1P_2d_0,\\
 E_{13}&=A_*(P_1d_3+P_3d_1)+A_1P_1P_3d_0,\\
 E_w&=w_1d_0,\quad E_S=2a_*d_0,\quad \rho_*=A_*P_1^2,\\
 E_{\rho,t}&=2E_{13}+|r_t|(E_\rho+2\rho_*E_w)
 +4\{P_2a_*E_\rho+\rho_*(a_*d_2+P_2b_*d_0)\}.
\end{split}\tag{LC7}
\]

These bound the actual differences of density, complex current,
log-potential and density time derivative. Product differentiation along
the segment proves the first three; the exact rho_t identity in FB11
proves the last directly. No derivative of an error allowance is taken.
Also

\[
 E_{S_t}=2(a_*d_2+P_2b_*d_0)+|r_t|E_w,\quad
 G_i=2P_1a_*+|r_i|,\quad
 d_i^S=2a_*d_1+2P_1b_*d_0+|r_i|E_w.
\tag{LC8}
\]

Here |S_i|,|(S_f)_i|<=G_i and |S_i-(S_f)_i|<=d_i^S.
For LC1, E_B=|r_t|E_w and E_s=|r_t|(E_rho+2rho_*E_w).
There is no transformed evolution: all computations use the original
physical H, q and rho. A time-dependent internal rescaling is unnecessary.

Each LC6 constant is at most its global counterpart in FB10--FB12:
A_*<=1/(pi epsilon^2), A_1<=c_0/(pi epsilon^3),
a_*<=1/(2epsilon), b_*<=epsilon^-2, w_1<=epsilon^-1.
Thus for identical jet errors and majorants these are no worse bounds.
If m/epsilon tends to infinity, their ratios to the discarded-denominator
bounds tend to zero at explicit powers: A_* gains (epsilon/m)^4,
A_1 gains O((epsilon/m)^5), a_* gains O(epsilon/m), b_* gains
O((epsilon/m)^2), and w_1 gains O((epsilon/m)^3).
This gain vanishes at a field zero; no uniform amplitude floor is claimed.

## 4. Filter the local allowances and compare the actual covariance

The pointwise envelopes in LC7--LC8 can vary with t,x,y. For any observable
V with pointwise error E_V, |partial^alpha K*(V-V_f)| is at most
|partial^alpha K|*E_V. This controls the stipulated derivatives and
boundary traces on D from D+. Time derivatives use the independently
proved E_(rho,t),E_(S_t). There is no need to maximize over the entire
spatial buffer before filtering.

Let d_i=d_i^S, and define convolution quantities at the observation point.
The actual covariance, with its signed x/y definition unchanged, obeys

\[
 E_Q=2\sum_i\{K*(G_id_i)+(K*G_i)(K*d_i)\},\tag{LC9}
\]
\[
\begin{split}
 E_{\Delta Q}=\sum_i\{&2|\Delta K|*(G_id_i)
 +2(K*d_i)(|\Delta K|*G_i)+2(K*G_i)(|\Delta K|*d_i)\\
 &+4\sum_{a=x,y}(|\partial_aK|*G_i)(|\partial_aK|*d_i)\}.
\end{split}\tag{LC10}
\]

**Proof.** Compare K*(S_i^2) and the squared mean gradients separately.
For the first Laplacian term move both derivatives onto K. For the means
v_i=K*S_i use Delta(v_i^2)=2v_i Delta v_i+2|grad v_i|^2 and the product
difference inequality. Summing absolute bounds over the two signed
components gives LC9--LC10. This is the covariance calculated from H_f,
not a field defined to repair an equation.

With constant envelopes G_i,d_i, LC9 becomes FB13, while LC10 gives

\[
 E_{\Delta Q}\le\left[6\|\Delta K\|_1+
     4(\|K_x\|_1^2+\|K_y\|_1^2)\right]\sum_i G_id_i.
\tag{LC11}
\]

This slightly sharpens FB13's squared sum of derivative norms. More
substantially, LC9--LC10 retain spatial amplitude information before
averaging. Numerical evaluation of these positive convolutions requires
an integration enclosure; sparse values of G_i,d_i do not supply it.

## 5. A removable-singularity-safe finite evaluator

The error-function expression remains an exact finite definition of H_f.
It can suffer severe subtraction near t=0; analyticity is not numerical
stability. A local alternative has an explicit truncation allowance.
In a source cell let c=(a+b)/2, d=(b-a)/2, u=c+v, and f=f(c)+f'v.
For either sign use

\[
 e^{tu^2\pm izu}=e^{tc^2\pm izc}
 \sum_{n=0}^{M_e}{[(2tc\pm iz)v+tv^2]^n\over n!}
       +\text{remainder}.\tag{LC12}
\]

Multiply by the linear f and (c+v)^j, integrate each polynomial on [-d,d],
and take the two derivative factors (plus/minus i)^j/2. These are finite
polynomial evaluations without division by t or z. Put
Theta_i=(2|t|c+|z|)d+|t|d^2. The total jet truncation is at most

\[
 E_j^{\rm eval}\le\sum_i 2d\,\max(f(a),f(b))\,b^j
 e^{tc^2+|y|c+\Theta_i}{\Theta_i^{M_e+1}\over(M_e+1)!}.
\tag{LC13}
\]

Taylor's absolute exponential remainder and positivity of f prove this
formula, uniformly on the specified buffer after bounding |z|. It pays
series truncation only. Rounding in coefficients, summation, exponentials,
nodal values and the regulator remains separate. It does not assert that
the field defined by a truncated implementation solves heat exactly.
The exact H_f does; implementation error is compared back to that field.
The error-function definition/series were checked against
[NIST DLMF 7.2.1](https://dlmf.nist.gov/7.2.E1) and
[7.6.1](https://dlmf.nist.gov/7.6.E1); LC12--LC13 are derived here.

## 6. Diagnostic outcome and acceptance status

The [script][script] and [66 kB record][record] retain 48/96/192-cell
source budgets, twelve filtered observations, source/filter refinements,
six local-evaluation checks, six raw primitive checks and 128 algebra
checks, including zero/double-event jets. All computations are floating;
none encloses a continuous time/space box.

The following are zeroth-jet source allowances, with U_s=1.5, N=4, Y=1
and 192 cells (193 nodal coefficients, each using four theta modes):

| Time ceiling | Original FB8 | Cellwise LC4 | Ratio, old/new |
| --- | ---: | ---: | ---: |
| 0 | 1.63828e-2 | 5.71282e-4 | 28.68 |
| 64 | 3.78785e58 | 5.63935e-2 | 6.71681e59 |

These are evaluations of proved formulas, not outward-rounded numerical
certificates. At t=64 the new zeroth-jet budget separates interpolation
5.63935e-2, omitted theta modes 4.53059e-33, candidate nodal arithmetic
1.49592e-12, and complete tail about 10^-483.767. At 48 and 96 cells the
interpolation terms are 3.55494 and 0.350787. Refining modes or cutoff
will not repair the dominant interpolation term in this regime.
The other jet orders and every tail are retained in the JSON, including
logarithmic tail values instead of silently calling underflow zero.

For the same improved jet errors and the same local P_j, retaining the
denominator reduces the sampled filtered density allowance by factors
from 1.11 to 3.79e6. At t=64,x=y=0 it gives about 3.10e-6 instead of
11.76; at t=64,x=4,y=.5 it still gives 2.291, well above 10^-4.
Those filter integrals are diagnostic quadratures, not uniform bounds.
The latter point's Q and Delta Q allowances are about 146 and 1.47e4.
The improvement is substantial away from small denominators and inadequate
near the unresolved peak region. No tolerance claim follows from the
large ratio itself.

The initially proposed nodal arithmetic allowance
1e-14 Phi_N(u_i)+1e-300 **failed**: its maximum observed error ratio
against 80-digit nodal evaluation was 8.589. The revised candidate
1e-12 Phi_N(u_i)+1e-300 has maximum sampled ratio 0.08589. This is still
not a rounding certificate. Its uniform proof, the regulator's arithmetic
and all evaluation rounding remain open. The new sigma term is recorded
separately; it is negligible compared with interpolation in this pilot.

Source-rule refinement (8 to 12 Gaussian nodes per source cell, and
256 to 384 nodes for the theta reference) changes the sampled density
by at most 6.57e-16 and potential by 3.65e-14. The source tail is supplied
analytically; source quadrature refinement alone is not a proof of the
observed error. Filter refinement is a different cost and **fails** its
reserved budget. At t=64,(x,y)=(4,.5), 40-to-64 nodes per filter direction
still change R_t by 5.93e-4 and Delta Q by 1.38. The original 12-to-20
values are retained. At 64 filter nodes the observed potential difference
is about 0.01110, the Q difference 0.03586, and the Delta Q difference
0.12396; the last value is unresolved by this refinement. The working
192-cell trial is not accepted, and none of these samples establishes
an error supremum or a lower bound for all possible source meshes.

The unmodified error-function primitive fails catastrophically at
(t,z,u)=(1e-8,10+i,.25), even with 80-digit arithmetic. Its exact formula
is correct; subtracting its huge/small intermediate values is unusable
in this implementation. LC12 with M_e=18 at six selected points, including
t=0,z=0 and t=+/-1e-8, differs from source-cell quadrature by at most
1.12e-16 in jets through order three. Its analytic truncation allowances
are at most 3.76e-28 at those points; the larger observed difference is
floating arithmetic/reference error, not covered by that truncation term.
Thus the local formula resolves the algebraic singularity, while certified
rounding remains a separate production-evaluator task.

**Disposition.** HDA-15 has a declared contract, proved source and nonlinear
gains, actual-covariance transfer and an explicit failed-trial diagnosis.
HDA-17 has no accepted representation. The next useful work is to refine
or improve source interpolation according to its cell contributions and
to control the peak-sensitive filter integrals, with arithmetic enclosed.
A large generic time/height sweep is not justified by this diagnostic.
The [self-review][review] records scope and proof checks. The new lemmas
are integrated into the maintained manuscript; endpoint results retain
their original scopes.

## 7. Control screen and remaining obligations

The interpolation estimate is generic for C2 sources; the particular
LC3/LC5 constants require the canonical theta expansion. Euler-factor
controls alter that source, weighted-square/finite-prime controls alter its
canonical weights or full reflection, and reflected/positive-primitive
controls lack its canonical square expansion. Atomic controls are not C2
densities; polynomial fields do not have this positive theta-source
representation. Smooth colliding controls can satisfy the generic local
stability and covariance bounds with their own constants. None of LC6--LC11
requires a simple root, so the double-event model H=z^2-2t is admitted.
These statements approximate regulated observables; they do not exclude
collisions, establish RH, or pay regulator removal.

HDA-17 still needs informative uniform budgets, including arithmetic and
filter integration, between all sampled points. HDA-16 still owes endpoint
evolution quantities; HDA-18 still owes whole-tail thresholds, both overlaps
and joining terms. The trial slab does not include the regulator switch
interior. Larger slabs require its spatial curvature terms and derivatives.
The fixed-cutoff failure at positive infinity remains scoped as in Note 20.

[fb]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[overview]: ../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md

[script]: ../numerics/finite_transition_local_bounds.py
[record]: ../numerics/FINITE_TRANSITION_LOCAL_BOUNDS_20261024.json
[review]: ../reviews/08_FINITE_TRANSITION_LOCAL_BOUNDS_SELF_REVIEW_20261024.md
