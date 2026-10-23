# Pair-distance matrices, clock convergence and forced heat dissipation

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual delegated model **gpt-6-astra (Codex)**, reasoning effort **ultra**, inherited from the parent. Status: **proved in-note from the cited local saddle theorem; internal algebra checks only**. No independent specialist review or literature novelty claim.

This note isolates a valid quantitative version of the proposed pair-distance idea. A finite inverse-square graph Laplacian measures pair geometry and converges to an explicit clock matrix for the actual late-time theta field. Heat evolution has an exact dissipation identity, but the complete exterior unit supplies a forcing term with no available favorable sign. The natural late-time fixed-rank target is a clock, not a GUE sample. This is a quantitative finite-rank milestone, not a simplicity criterion.

Read the repository [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and patterns [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The source inputs are LHCT Note 03 and BW10 Note 20, linked below. No new uniformity in rank or height is asserted.

## 1. The actual finite clock matrix and its quantitative convergence

Fix a consecutive block of m>=2 positive roots, ranks ell+1,...,ell+m, K=ell+m. Use the complete theta field and the saddle parameters

\[
4\pi e^{4L}=2tL+9,\qquad \kappa=8tL-2t+36,\qquad L'/L=2/\kappa.
\]

The existing [differentiated saddle theorem][saddle] supplies, under its explicit finite conditions,

\[
|Lx_{\ell+i}-(\ell+i-1/2)\pi|\le e=\arcsin\epsilon_0,
\quad e=O_K((L\sqrt\kappa)^{-1}).
\]

It proves existence, simplicity and rank identification for these late roots without RH. Identifying the roots with walls from an unknown time-zero multiple event is a separate RH-conditional step. Define

\[
y_i=Lx_{\ell+i}/\pi,\qquad c_i=\ell+i-1/2,\qquad
\delta=e/\pi<1/4.
\]

Then |y_i-c_i|<=delta. For distinct i,j put W_ij(y)=(y_i-y_j)^(-2), and let the symmetric graph Laplacian be

\[
\mathcal L(y)_{ij}=-W_{ij}\ (i\ne j),\qquad
\mathcal L(y)_{ii}=\sum_{j\ne i}W_{ij}.
\]

Its clock target L_*=L(c) has W^*_ij=(i-j)^(-2). For every real vector v,

\[
v^T\mathcal L(y)v=\sum_{i<j}\frac{(v_i-v_j)^2}{(y_i-y_j)^2}.
\]

Consequently

\[
\boxed{(1+2\delta)^{-2}\mathcal L_*\preceq\mathcal L(y)
       \preceq(1-2\delta)^{-2}\mathcal L_*.}                 \tag{1}
\]

Indeed each label gap d=j-i>=1 has d-2delta<=y_j-y_i<=d+2delta, and (1-2delta)d<=d-2delta while d+2delta<=(1+2delta)d. Apply the resulting weight inequalities in the quadratic form. In particular every nonzero eigenvalue has the same multiplicative enclosure.

The explicit additive estimate is

\[
\boxed{\|\mathcal L(y)-\mathcal L_*\|_{op}
 \le16\delta\sum_{d=1}^{m-1}(d-2\delta)^{-3}
 =O_K((L\sqrt\kappa)^{-1}).}                               \tag{2}
\]

For proof the mean-value theorem gives |(y_j-y_i)^(-2)-d^(-2)|<=4delta/(d-2delta)^3. The absolute row sum of a Laplacian difference is at most twice the sum of the absolute weight differences, with at most two entries at each distance d. Symmetry bounds operator norm by the maximum absolute row sum. The matrix on the subspace perpendicular to constants has

\[
\lambda_2(\mathcal L_*)\ge m/(m-1)^2,\qquad
\|\mathcal L_*\|_{op}\le4\sum_{d=1}^{m-1}d^{-2}.
\]

The first bound compares with the complete graph of constant weight (m-1)^(-2); the second uses row sums. Thus a root-block matrix discrepancy converges to zero with a proved rate and paid complete-source input. Its finite sufficient conditions, not merely the asymptotic notation, are inherited from [saddle].

For clarity this is a fixed-rank limit. Its pair differences tend to the nonzero integers j-i; the associated finite empirical pair measure converges to a weighted atomic lattice. It supplies neither a high-height pair-correlation theorem nor a joint growing-rank/large-time limit. It does not replace a statistical topology by a stronger uniform topology without paying for that change.

## 2. Complete heat motion and the exterior-unit obstruction

On a proper local neighborhood of a simple real cluster factor H=U product_i(z-x_i), with U holomorphic and nonzero, and set b_i=U_z/U(t,x_i). For a real factorization b_i is real. Every omitted zero and any entire nonzero factor are contained in U. The complete heat equation gives

\[
x_i'=2S_i(x)+2b_i,\qquad S_i(x)=\sum_{j\ne i}(x_i-x_j)^{-1}.    \tag{3}
\]

The natural logarithmic pair energy is

\[
E(x)=-\log\prod_{i<j}(x_j-x_i)^2,
\qquad \nabla E=-2S,\qquad \nabla^2E=2\mathcal L(x).
\]

Its exact forced balance is

\[
\boxed{E'=-4\|S\|^2-4S\cdot b
 =-8\sum_{i<j}(x_j-x_i)^{-2}
  -4\sum_{i<j}\frac{b_j-b_i}{x_j-x_i}.}                      \tag{4}
\]

Here ||S||^2=2 sum_(i<j)(x_j-x_i)^(-2); the mixed terms cancel in triples, and S dot b=sum_(i<j)(b_j-b_i)/(x_j-x_i). Thus (4) is exactly the negative of the complete log-discriminant derivative, consistent with [BW12 Note 09][many]. The graph Laplacian is the Hessian of the pair energy, rather than an independent unforced law for the selected roots.

For the physical weights W^x_ij=(x_i−x_j)^(−2), the exact evolution retains the same force:

\[
(W^x_{ij})'=-2W^x_{ij}\frac{x_i'-x_j'}{x_i-x_j},\qquad
\frac{x_i'-x_j'}{x_i-x_j}
=\frac4{(x_i-x_j)^2}
-2\sum_{k\ne i,j}\frac1{(x_i-x_k)(x_j-x_k)}
+2\frac{b_i-b_j}{x_i-x_j}.                                \tag{5}
\]

For the normalized weights W(y)=alpha^(−2)W^x, differentiating also contributes −2(L'/L)W(y). No definite sign for (W^x_ij)', E', or a discrepancy follows by positivity of W alone. In the actual theta late-time block the existing [LHCT Note 03][pair] proves

\[
(\log\Delta)'=-2m(m-1)/\kappa+O_K(\kappa^{-5/4}),\quad
8\sum_{i<j}(x_j-x_i)^{-2}\asymp_m L^2.
\]

Therefore E'>0 eventually, although its internal pair contribution in (4) is negative of order L^2. The complete unit force reverses that sign. This is an actual theta counterexample to treating finite-block pair energy as an unforced decreasing quantity. It does not rule out another source-dependent functional.

## 3. A precise conditional clock-dissipation interface

Let alpha=L/pi. In normalized variables (3) reads

\[
y'=2\alpha^2S(y)+f,\qquad
f=(L'/L)y+2\alpha b.
\]

Put d=y-c, R=f+2alpha^2 S(c), and let P_0 denote orthogonal projection onto the vectors of mean zero. Since the components of S sum to zero, d_0=P_0d satisfies the exact identity

\[
\boxed{\frac12(\|d_0\|^2)'=
-2\alpha^2\sum_{i<j}
 \frac{(d_i-d_j)^2}{(y_i-y_j)(c_i-c_j)}
 +d_0\cdot P_0R.}                                      \tag{6}
\]

The mixed denominators are positive for ordered points. This follows pairwise from

\[
S_i(y)-S_i(c)=-\sum_{j\ne i}
 \frac{d_i-d_j}{(y_i-y_j)(c_i-c_j)}.
\]

If |d_i|<=delta, all mixed weights are at least
w_0=[(m-1)(m-1+2delta)]^(-1). Thus, with lambda(t)=2alpha(t)^2 m w_0,

\[
D^+\|d_0\|\le-\lambda\|d_0\|+\|P_0R\|,
\]

and the usual integrating-factor estimate gives

\[
\|d_0(t)\|\le e^{-\int_{t_0}^t\lambda}\|d_0(t_0)\|
+\int_{t_0}^t e^{-\int_s^t\lambda}\|P_0R(s)\|\,ds.         \tag{7}
\]

This is an explicit interface for a future coupled theta estimate. Pair geometry supplies coercivity; the remaining input is a bound on the complete centered residual R, including b. The center itself has separate motion, and (7) does not control it. Reconstructing R from already-proved root motion is a valid diagnostic but is not new independent dissipation evidence. No favorable theta bound on R beyond the existing saddle information is supplied here.

## 4. What the unforced polynomial model actually relaxes to

For a real-rooted polynomial heat flow P_t=-P_zz with no exterior factor, b=0. Fix t0>0 in its simple real regime. For u=x/sqrt(2t) and s=log t, its motion becomes

\[
\frac{du_i}{ds}=S_i(u)-u_i/2=-\partial_i V(u),\qquad
V(u)=\tfrac14\sum_i u_i^2-\sum_{i<j}\log(u_j-u_i).
\]

On the ordered chamber Hess V=(1/2)I+L(u)>=(1/2)I. The potential diverges at finite collisions and at infinity; it has a unique minimizer h. Its equations S_i(h)=h_i/2 characterize the roots of the monic probabilists' Hermite polynomial: for Q(z)=product_i(z-h_i), Q''-zQ'+mQ vanishes at every root and has degree at most m-1, so is identically zero. Strict convexity then gives

\[
\frac{dV}{ds}=-\|\nabla V\|^2,\qquad
\|u(t)-h\|\le(t_0/t)^{1/2}\|u(t_0)-h\|.                   \tag{8}
\]

The norm estimate follows by differentiating squared distance and applying strong monotonicity of the gradient. The coercive sublevel set also prevents finite-time collision or escape in this regime. This is deterministic convergence to one Hermite configuration; it is not convergence to a random matrix distribution. In particular the exact heat birth e^(-t partial_z^2)z^m has u(t)=h at every positive time while retaining its multiplicity-m event at t=0. Perfect late-time regularity therefore does not erase a past event or its charge.

For the canonical theta source the fixed-rank scale is 1/L, not sqrt(t), and b is essential. The Hermite Lyapunov must not be imported after dropping b. The broader collision controls in result-summary 12 all satisfy the local identities when they have a proper real simple cluster. Euler-factor controls change the theta source; weighted-square and finite-prime controls lack full reflection/normalized complete theta data; reflected, smooth and positive-primitive controls lack the unchanged integer-square expansion; close positive endpoint controls fail ordinary Dirichlet arithmetic. These source differences are absent from (3)--(8), so those generic identities distinguish none of them from theta.

## 5. Reciprocal-Hodge consumers need more than a distance matrix

For the physical cover w^2=H and differential omega=dz/w, home 09 uses

\[
\mathcal E(H;\Omega)=2\int_\Omega |H|^{-1}dA,
\qquad W(H;\Omega)=2\int_\Omega|H_z|^2|H|^{-1}dA.
\]

Multiplying a heat field by any nonzero constant c preserves every zero, pair distance, all root trajectories, the matrix L, and the heat equation. Nevertheless, after a consistent square-root choice,

\[
\omega_{cH}=c^{-1/2}\omega_H,\quad
\oint\omega_{cH}=c^{-1/2}\oint\omega_H,\quad
\mathcal E(cH)=|c|^{-1}\mathcal E(H),\quad W(cH)=|c|W(H).  \tag{9}
\]

Thus no finite estimate of these unnormalized quantities can come from the pair matrix alone over a class permitting arbitrary c. This is an information-content screen, not a permitted rescaling of the actual canonically normalized theta target. For theta, the fixed amplitude must be acquired from the complete source in addition to the pair data.

More generally on a simply connected finite base disk H=UP has a holomorphic square root of the nonvanishing unit U. The cover is identified with v^2=P by w=sqrt(U)v, but its physical differential is dz/(sqrt(U)v). The branch positions determine this local covering structure while U still affects the differential and its energy. The normalized period matrix of a compact algebraic cover, when such a compactification and homology basis have actually been specified, is a different object and is invariant under constant rescaling; (9) concerns the physical differential's unnormalized periods. The bordered covers in [RHE Note 01][rhe1] also retain physical boundaries and relative periods, so a compact period matrix alone does not specify their full energy.

The derivative-weighted differential is exact, H_z dz/w=2dw; [RHE Note 08][rhe8] proves its energy remains finite through every multiplicity. Its favorable bound is therefore not a simplicity detector. A pair-statistics-to-Hodge bridge needs the exact differential, the complete unit/amplitude, and every boundary/relative-period payment.

## 6. Verification and next permissible task

A small exact rational check on ordered configurations with m=2,...,8 verified the identities ||S||^2=2 sum gap^(-2), the complete forced discriminant derivative, and the mixed-Laplacian identity (6). These checks confirm algebra; the proofs above establish the statements. No numerical theta experiment or onset certificate is claimed.

The surviving work is concrete: (1)--(2) give a paid finite matrix target; (6)--(7) isolate the exact residual a useful new source estimate must control; (9) specifies data that a proposed reciprocal-energy consumer cannot discard. A growing-rank statistical theorem, uniform small-gap control, and a complete complex-time cap or closure estimate remain separate obligations. None follows from a finite pair matrix tending to a regular clock.

[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[pair]: 03_FIXED_RANK_PAIR_CANCELLATION_AND_TUBE_CONTROLS_20261022.md
[many]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md
[rhe1]: ../../09_reciprocal_hodge_energy/notes/01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[rhe8]: ../../09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
