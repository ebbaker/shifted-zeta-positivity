# Shrinking late caps and concentration on the imaginary-time closures

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from the parent turn metadata.

**Status: proved in-note for the declared ordinary-double window and its two continued projective tubes; separate same-model internal checks recorded in the linked review.** The canonical late caps in Note 02's shrinking-width regime tend to zero; its fixed-width regime has a nonzero limit. In the shrinking-width regime the complete signed boundary converges face by face to two imaginary-time contributions of one half. This is a scoped failure of the proposed zero-cap/zero-side payment in this geometry, not an obstruction to all canonical-source estimates or an endpoint exclusion.

The [result index][results], [avoid index][avoid], [heat geometry][geometry], [collision controls][controls], [scope rule][scope] and [coupled-error discipline][coupled] apply. [Note 01][n1] supplies the actual window; [Note 02][n2] supplies the unchanged-source late-cap estimate. This note pays the previously unestimated local closures analytically, conditional on the hypothetical event.

## 1. Fixed local core and shrinking heat thickness

Use real type H(conjugate tau, conjugate z)=conjugate H(tau,z), the backward heat equation H_tau=-H_zz, and an ordinary real event H(0,a)=H_z(0,a)=0, h_2=H_zz(0,a) nonzero. The inherited complete local construction gives positive d,t_0,R,Y_0 and

\[
 W_0(Y)=\{ -d\le t\le t_0,\ |s|\le Y,\ |z-a|\le R\},\qquad 0<Y\le Y_0,
\]

with exactly this one event, a regular complete boundary, and its two simple roots at t_0 inside the spatial disk. All quantities d,t_0,R remain fixed below. The continuation in Note 01 attaches two disjoint root tubes for t_0<=t<=T along subsets of the t_0 face. The unattached part of that face remains a joining face. The regular projective walls have zero flux. The full union W_T is a compact piecewise smooth Lipschitz domain, with reentrant attachment corners; Stokes may be applied separately to the core and tubes, cancelling their common faces with opposite induced orientations. No candidate event lies on its boundary.

Write G=(H,H_z) and C=A wedge dA/(4 pi^2), with the complex orientation dt wedge ds wedge dx wedge dy. A forward real-time cap has orientation ds wedge dx wedge dy. The top imaginary-time face has orientation -dt wedge dx wedge dy; the bottom has +dt wedge dx wedge dy.

Choose any source-paid numbers b>0 and D<infinity with

\[
 |G|\ge b,\qquad \|DG\|_{\rm op}\le D
\]

on the compact union K of the early face t=-d, the full joining-level face t=t_0, and the spatial wall |z-a|=R, allowing |s|<=Y_0. Their existence follows from the local construction; quantitative choices can use its explicit boundary floors and complete canonical moments. This is a boundary floor away from the event, not an internal simplicity assumption. For example, moment bounds M_j dominate the physical complex derivatives, so D can be taken at least sqrt(M_1^2+2M_2^2+M_3^2). No finite theta numerical value is asserted.

The normalized Hopf form is radial Euclidean sphere volume:

\[
 \mathcal C=G^*\left[\frac{1}{2\pi^2|w|^4}
       \sum_{j=1}^4(-1)^{j-1}w_j\,dw_1\wedge\cdots\widehat{dw_j}\cdots\wedge dw_4\right]. \tag{1}
\]

Consequently its comass on K is at most D^3/(2 pi^2 b^3). With

\[
 B=\frac{D^3}{2\pi^2b^3}\left(4\pi R^2+4\pi R(d+t_0)\right), \tag{2}
\]

the total absolute flux over the early, full t_0 and local spatial faces of W_0(Y) is at most BY. The same bound holds after removing the two attachment disks from the t_0 face. Their moving shape changes neither this containment nor the Euclidean face measure. All source modes and tails are retained in b,D; shrinking Y needs no stronger source approximation.

## 2. Exact half-charge limit on the two local imaginary-time faces

Let J_+(Y),J_-(Y) denote the oriented fluxes over s=+Y and s=-Y of the local core. Simultaneous conjugation

\[
 (t,s,x,y)\longmapsto(t,-s,x,-y)
\]

preserves the four-dimensional orientation and exchanges those faces with their outward boundary orientations. Real type gives G after conjugation equal to conjugate G. Conjugation changes A to -A and dA to -dA, hence leaves C unchanged. Therefore

\[
 J_+(Y)=J_-(Y). \tag{3}
\]

The complex Jacobian of G at the event is

\[
 \begin{pmatrix}-h_2&0\\-h_3&h_2\end{pmatrix},\qquad
 \det=-h_2^2\ne0,
\]

so its local complex degree is one. Equivalently use the inherited complete-window charge theorem. The sum of all core boundary fluxes equals one. Combining this with (2)-(3) gives the explicit complete local bound

\[
 \boxed{\left|J_\pm(Y)-\frac12\right|\le\frac{BY}{2}.} \tag{4}
\]

This avoids a singular pointwise estimate on the imaginary faces. They approach the event as Y decreases, so no uniform boundary-jet floor on them is asserted. Their small separation does not imply small integrated flux.

## 3. Attach the late root tubes and retain every term

For each of the two branches let

\[
 h_j(\tau)=H_z(\tau,z_j(\tau)),\qquad
 k_\epsilon=\frac{\epsilon^2}{1+\epsilon^2}.
\]

The branch and h_j are holomorphic and nonvanishing on the finite rectangle of Note 01. On its real segment h_j is real and has a constant sign. There is therefore a holomorphic logarithm of h_j divided by that sign whose imaginary part vanishes on the real segment. Set

\[
 \theta_j(t,Y)=\operatorname{Im}\log\frac{h_j(t+iY)}{h_j(t)}.
\]

The continuous logarithm is part of this definition; principal arguments alone are insufficient. Reality makes the lower-end value -theta_j(t,Y). Note 01's exact radial mean formula yields, for each tube,

\[
 I_{T,j}=\frac{k_\epsilon}{\pi}\theta_j(T,Y),\quad
 I_{0,j}=\frac{k_\epsilon}{\pi}\theta_j(t_0,Y),\quad
 J_{{\rm tube},+,j}=J_{{\rm tube},-,j}
   =\frac{k_\epsilon}{2\pi}\{\theta_j(t_0,Y)-\theta_j(T,Y)\}. \tag{5}
\]

Thus I_{T,j}-I_{0,j}+J_tube,+,j+J_tube,-,j=0 exactly. These are regular tubes containing no joint zero. The zero projective side contributes nothing, and all phase constants at the real endpoints cancel.

Choose one finite constant C_* bounding |h_j'/h_j| on the two fixed t_0 vertical segments |s|<=Y_0, after reducing Y_0 if needed. Then

\[
 |\theta_j(t_0,Y)|\le C_*Y. \tag{6}
\]

This is a paid compact local boundary quantity. The heat equation and root derivative give h_j'/h_j=-H_zzz/H_z+(H_zz/H_z)^2 along a simple root, so complete source upper bounds and the fixed t_0 derivative floor supply C_*.

Use the very same late geometry as Note 02:

\[
 S_T=L_T^2Y_T\le S,\qquad L_T\epsilon_T\le r,
\]

with fixed S>0 and admissible r, and any further reductions of Y_T,epsilon_T needed by finite continuation. Both are positive at every finite T. Write D_T for the quantity D(T) in Note 02 (20)-(21), its explicit full-source phase-rate remainder tending to zero. Its vertical estimate gives

\[
 |\theta_j(T,Y_T)-S_T|\le S_TD_T. \tag{7}
\]

For N=2 branches, write J_full,± for each complete imaginary-time face (core plus the tube pieces). Equations (4)-(7) prove

\[
 \boxed{\left|J_{{\rm full},\pm}-\frac12\right|
 \le\frac{BY_T}{2}+\frac{k_{\epsilon_T}}{\pi}
             \{C_*Y_T+S_T(1+D_T)\}.} \tag{8}
\]

The forward sum of the two late caps obeys

\[
 \left|I_T-\frac{2k_{\epsilon_T}S_T}{\pi}\right|
 \le\frac{2k_{\epsilon_T}S_TD_T}{\pi},\qquad
 |I_T|\le\frac{2r^2S(1+D_T)}{\pi L_T^2}. \tag{9}
\]

The early, joining-complement and local spatial faces have total absolute flux at most BY_T. Every projective side is exactly zero. The edges and chart seams are lower-dimensional gluing interfaces, not omitted external three-faces. Formulae (8)-(9), together with the exact signed identity

\[
 \boxed{\int_{\partial W_T}\mathcal C=1,} \tag{10}
\]

supply the complete face accounting:

\[
 I_T\to0,\quad I_{\rm early}+I_{\rm join}+I_{\rm local\ wall}\to0,
 \quad I_{\rm projective\ sides}=0,\quad
 J_{{\rm full},+}\to\tfrac12,\quad J_{{\rm full},-}\to\tfrac12. \tag{11}
\]

Since Y_T<=S/L_T^2 and k_epsilon<=r^2/L_T^2, the displayed absolute errors are O(L_T^{-2}) with fixed event-dependent local constants, plus Note 02's smaller cap error. No lower bound on Y_T or epsilon_T is required. This handles arbitrary further shrinking demanded by continuation; no unproved uniform tube width to infinity is used.

## 4. Fixed imaginary-time thickness and a nonzero canonical late cap

Note 02 also pays fixed physical width |s|<=Y_max: in its exact finite inequalities substitute the growing scaled range S(T)=Y_max L_T^2. The complete source still concentrates enough that its near-one logarithm error b_T=O(L_T/sqrt(kappa_T)) tends to zero. The common e^{isL_T^2} phase must be retained. The paired endpoint estimate gives

\[
 \left|I_{T,j}-\frac{k_{\epsilon_T}Y L_T^2}{\pi}\right|
 \le\frac{k_{\epsilon_T}b_T}{\pi}. \tag{12}
\]

Note 01's source-assisted growing-interval corollary joins these late inverses to the compact initial segment. For each fixed candidate and finite set of born roots, it supplies some fixed Y>0 and, for all sufficiently large finite terminal T, a common constant-on-the-tube radius epsilon_T=r_0/L_T, with fixed 0<r_0<1/4. This uses a new source estimate to control the late strip; it is not an inference from compactness alone or a fixed positive q radius to infinity.

Let R_0(Y) be the signed sum of the full local core's early, t_0 and spatial-wall faces. It is independent of T and |R_0(Y)|<=BY. For n=2,

\[
 I_T\longrightarrow\frac{2r_0^2Y}{\pi},\qquad
 J_{{\rm full},\pm}\longrightarrow
     \frac{1-R_0(Y)}2-\frac{r_0^2Y}{\pi},
\]
\[
 I_{\rm early}+I_{\rm join}+I_{\rm local\ wall}
        \longrightarrow R_0(Y). \tag{13}
\]

Indeed each late root cap has reference r_0^2Y L_T^2/[pi(L_T^2+r_0^2)] and error at most k_epsilon b_T/pi. Each initial attachment cap is O(k_epsilon Y); by (5) each tube imaginary face contributes minus half the late cap plus half its initial cap. Equations (3)-(4) give the remaining local term. Thus all limits in (13) follow with errors O(L_T^-2)+O(1/(L_T sqrt(kappa_T))) and fixed local constants. The sum is exactly one at each finite T and in the limit. The exact nonzero reference and its canceling tube closures survive together.

This gives two distinct fully paid regimes on the same projective tube construction. With Y_T<=S/L_T^2 the late cap vanishes and each full imaginary face tends to one half. With fixed Y>0 the late cap has a nonzero canonical limit, while the complete signed charge still stays one. Neither regime obtains the proposed strict subunit margin.

## 5. Every fixed finite multiplicity, with event-dependent constants

The same closure statement covers an arbitrary fixed finite multiplicity n>=2 once Note 01's higher-multiplicity geometry corollary is used. A real heat event of spatial order n is isolated in complex (tau,z) and has local charge q_n=binom(n,2), by the inherited local multiplicity theorem. Equivalently, the local Weierstrass discriminant is nonzero at all sufficiently small positive real times and so is not identically zero; shrink its heat disk until the sole discriminant zero is tau=0. Rouche's theorem supplies a proper n-root spatial cluster on that disk. Under RH its n simple roots at fixed t_0>0 continue as n fixed finite positive ranks, after reducing to a>0 by evenness. The canonical positive integral H(t,0)>0 rules out a=0.

Choose a symmetric spatial disk and a real-centered heat rectangle with this sole joint event; the ordinary-double numerical constants are not reused. Compactness supplies the boundary floor and derivative bounds in (1)-(2). Attach n tubes with common minimum positive widths and radii from Note 01. The same source cap theorem applies with K chosen above their highest fixed rank. It is uniform over this finite set, with constants allowed to depend on n and that rank.

Reality still gives equal imaginary-face fluxes. Equations (8)-(10) become

\[
 \left|J_{{\rm full},\pm}-\frac{q_n}{2}\right|
 \le\frac{BY_T}{2}+\frac{n k_{\epsilon_T}}{2\pi}
                 \{C_*Y_T+S_T(1+D_T)\},
\]
\[
 \left|I_T-\frac{n k_{\epsilon_T}S_T}{\pi}\right|
 \le\frac{n k_{\epsilon_T}S_TD_T}{\pi},\qquad
 \int_{\partial W_T}\mathcal C=q_n. \tag{14}
\]

Thus each complete imaginary face tends to q_n/2, while all real-time caps and the fixed local spatial wall tend to zero and the projective walls vanish exactly. The conclusion holds for **every arbitrary fixed finite candidate height and multiplicity**, with event-dependent constants and thresholds. There is no simultaneous uniform estimate as height, multiplicity or the number of late ranks tends to infinity. The fixed-width limits (13) likewise hold with 1 replaced by q_n and the total late-cap coefficient 2 replaced by n; each imaginary-face correction is n r_0^2Y/(2pi). This extends the geometry and closure allocation; it excludes no event and does not complete LHCT-07's exclusion task.

## 6. Interpretation, controls and remaining task

**For this assembled shrinking-strip family, cap vanishing is accompanied by a unit closure flux, not a subunit complete-charge bound.** The quantitative result identifies the missing flux rather than simply citing charge conservation. It shows which individual faces carry the charge, with explicit bounds valid for the unchanged canonical field conditional on the endpoint event and the RH continuation used in Note 01; (8)-(11) are the ordinary-double case, and (14) gives the finite-multiplicity extension.

The quadratic heat double obeys (3)-(4) exactly in its small-core geometry and retains degree one. The cosine heat model has no event and fails the sole-event hypothesis, so its corresponding full boundary has zero charge; its nonzero fixed-cap calculation remains an independent control against deleting common phase. The punctured projective shell is not a complete event-enclosing core and retains its inner closure. Other controls in the linked register retain their distinct arithmetic/reflection failures: none is assigned the canonical complete-source saddle remainder. These checks screen only the asserted generic geometry and complete-source estimate.

This result stops the specified inference from shrinking late caps and projective-side cancellation to endpoint exclusion. It does not prove that RH permits a canonical double, or that every alternative cap family fails. It does not pay a theta-specific opposing bound on the signed closures. LHCT-06's strict upper below one and LHCT-07's full multiplicity exclusion remain unproved; LHCT-05 receives a complete closure allocation for this family, not the requested exclusion-producing improvement.

The [internal review][review] checks the signs, constants and multiplicity scope. The next substantive estimate would have to use unchanged theta data to bound the **complete** imaginary-face/closure sum below its conditional charge value, with source errors retained, or supply a different fully specified family with a paid complete margin. A late-root statistic or an arbitrarily small terminal cap alone does not provide that estimate.

[n1]: 01_FINITE_PROJECTIVE_TUBES_AND_COMPLETE_ATTACHMENTS_20261022.md
[n2]: 02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

[review]: ../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md
