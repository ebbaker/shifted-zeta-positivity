# How should a spatial tensor tree evolve under Newman flow?

**Research update, 20 November 2026.** This is the founding overview. The [milestone and continuation](../notes/07_AGC_ST_MILESTONE_AND_CONTINUATION_20261120.md) and [live register](../research-progress/01_AGC_ST_RESEARCH_PROGRESS_20261119.md) give the subsequent analytical results and current task states. The separate [local](../reviews/02_AGC_ST_LOCAL_GENERATOR_ASSESSMENT_20261120.md) and [forcing](../reviews/03_AGC_ST_SPATIAL_FORCING_ASSESSMENT_20261120.md) assessments record the scope.

19 November 2026, America/New_York. Edward Baker proposed the spatial tree. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. The actual setup lead model and reasoning effort are unavailable in the registered history. Status: scientific setup. The spatial states, dynamics and limiting construction are open research choices. No AGC-ST research task has been activated.

## The physical object

Can neighboring spatial regions exchange enough information under Newman evolution to determine the motion of one marked pair of zeros? A useful tree should explain what each region contributes to the pair, how two regions combine, and what evolution does to the information discarded at a merge. A binary address can specify a location in height \(x\). A tree topology specifies which regions interact through a common node. Choosing the former leaves the latter and its dynamics open.

Use the literal even theta source, physical time \(t\in\mathbb R\), and \(H(t,z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv\), with \(H_t=-H_{zz}\). At time zero \(H(0,z)=\xi((1+iz)/2)/8\). A real spacing in Newman height is twice the corresponding critical-line zeta ordinate spacing. Work first on a compact real time chart with a conjugation-invariant contour enclosing two zero occurrences, boundary clearance, and complete exterior, including nonreal occurrences. A real adjacent gap needs two distinct real roots and exclusion of intervening real roots. A global zero number also needs an index anchor. The contour can persist through a local double. [AGC §1, normalization and count](../../manuscript/sections/01_source.tex), [§2, counted pair](../../manuscript/sections/02_pair_chain.tex)

The [fixed-time brainstorm](../../../brainstorm/notes/06_SPATIAL_TTN_ZERO_SPACING_20261119.md) proposed a height-window gap pilot and a direct cost comparison. It is historical motivation. In [01 QTT–Newman](../../../01_qtt_newman_flow/manuscript/main.tex), a quantics chain factors bits of the source variable \(v\); its contraction observes the field. Its formal compact-box approximation does not give a height-tree evolution, a denominator floor, or a scale-uniform rank bound. The [parallel Jacobi branch](../../01_jacobi_integer_hierarchy/README.md) owns evolution and signed defects as the *truncation degree* varies. Here spatial depth indexes a partition of observation height in the same physical field. Arithmetic dyadic groups in [AGC §§12–13](../../manuscript/sections/13_actual_phase_recurrence.tex) index summands by odd core and power of two. Their scoped loss concerns independently relaxed core rotations.

## What two adjacent children can tell their parent

Take a finite rectangle divided into adjacent child rectangles. Give each cell \(I\) a real expansion origin \(o_I(t)\), and write \(B=H_z/H\). On a cleared boundary its polynomial moments are

\[
 U_k(I)=\frac{1}{2\pi i}\oint_{\partial I}(z-o_I)^k B\,dz .
\]

The argument principle gives the sum of the \(k\)-th powers over interior zero occurrences. For \(\delta_I=o_I-o_P\), the merge is \(U_k(P)=\sum_{I=L,R}\sum_{j=0}^k {k\choose j}\delta_I^{k-j}U_j(I)\). Opposite internal edges cancel because both use the same analytic field. Appending a constant channel makes a translated sum a bilinear contraction of the two child messages. Arbitrary large counts, high-order moments and high-precision boundary evaluations still cost resources even when the number of routed channels is small.

At a count-two node \(c=o_P+U_1/2,\ D=U_2/2-U_1^2/4\). Its roots are \(c\pm\sqrt D\). The real-pair gap is \(g=2\sqrt D\) when \(D>0\); \(D=0\) is a double and \(D<0\) a conjugate pair. A split through a root invalidates its child integrals. Move the cut with verified clearance, or use the outer contour and treat the pair together. General nodes can pass untruncated local divisors, contour traces of \(B\), or truncated packets of moments plus an exterior analytic field. These give different answers to what one tree edge must carry. [AGC §2, deflation and exterior response](../../manuscript/sections/02_pair_chain.tex)

## The time generator and the missing exterior

On such a chart, a proposed exact state \(s_I(t)\), merge \(C_t\) and evolution must satisfy the chain rule

\[
 \dot s_P=\partial_t C_t(s_L,s_R)
      +(\partial_1 C_t)\dot s_L+(\partial_2 C_t)\dot s_R .
\]

This identity becomes an evolution on a proposed state space only if its right-hand side is supplied by that state and its specified boundary or exterior inputs. The derivative \(\partial_t C_t\) includes origin velocities for a translating merge. On fixed physical contours, or contours deformed within a cleared collar without crossings, the inherited Burgers identity \(B_t=-(B_z+B^2)_z\) gives a concrete test. For \(w=(z-o_I(t))^k\), differentiation and two closed-contour integrations by parts give

\[
 \dot U_k(I)=\frac{1}{2\pi i}\oint_{\partial I}
         \big[(w_t-w_{zz})B+w_zB^2\big]\,dz ,
 \qquad w_t=-o'_I w_z .
\]

At common origins internal integrals again cancel, including the nonlinear term, if one uses the **same full trace** of \(B\) on each side. At different origins the binomial translation and its derivative restore this cancellation. Motion of a closed contour contributes an integral of a total derivative while its collar stays cleared. Individual open moving edges have endpoint terms; they must be paired in the oriented boundary. A reset after a root crossing needs new counts or a verified overlap. For an approximate analytic field \(Y\), put \(r=(Y_t+Y_{zz})/Y\) on the cleared boundary. The formula using \(Y_z/Y\) gains the signed term \(-\oint w_z r\,dz/(2\pi i)\). A time-dependent compression also needs a bound for its own differentiation and projection error. [AGC §3, Burgers equation and contour time law](../../manuscript/sections/03_hierarchy.tex), [AGC-JH forced hierarchy, contour identity](../../01_jacobi_integer_hierarchy/notes/02_AGC_JH_FORCED_INTEGER_HIERARCHY_20261119.md)

A two-polynomial example isolates the missing information. At \(t=0\) initialize exact heat solutions at \(z^2-s^2\) and \((z^2-s^2)(z^2-R^2)\), with \(0<s<R\). A target box containing just \(-s,s\) has identical **interior divisor of every order** for both. From the parent pair law, \(D'(0)=2\) for the first and \(D'(0)=2-8s^2/(R^2-s^2)\) for the second. The two added exterior zeros change the target velocity even before anything crosses the boundary. This rules out an autonomous evolution using only an interior divisor for the class of these polynomial heat solutions. Their exterior traces distinguish them. The example is a symbolic screen for candidate states and supplies no theta-specific estimate. [AGC §2, pair law](../../manuscript/sections/02_pair_chain.tex)

An alternative candidate makes the two directions of communication explicit. On a cleared cell set \(P_I(z)=\prod_{\rho\in I}(z-\rho)\) with multiplicities, \(A_I=H/P_I\), and \(R_I=(A_I)_z/A_I\). The monic polynomial has time-analytic coefficients on a fixed-count chart, including at internal mergers; its factor \(A_I\) is holomorphic and nonvanishing near the counted roots. Upward the divisors multiply, \(P_P=P_LP_R\). Downward, near the left child's roots,

\[
 R_L=R_P+(P_R)_z/P_R .
\]

The analogous right-child equation uses \(P_L\). Holding physical \(z\) fixed in the heat equation for \(H=P_I A_I\) gives

\[
 \partial_tP_I+(P_I)_{zz}+2R_I(P_I)_z
       =-P_I\,\frac{(A_I)_t+(A_I)_{zz}}{A_I}.
\]

Thus the left side vanishes modulo \(P_I\) as a holomorphic germ at its roots, to full multiplicity. For degree \(m\), \(\partial_tP_I\) has degree \(<m\); the remainder of the other two terms there prescribes its coefficients if the exterior germ is supplied. The empty divisor \(P_I=1\) has no coefficient to evolve. Expressing the polynomials in a moving origin adds the usual transport term. For \(P_I=(z-c)^2-D\) this recovers the parent's pair law. The factorization exposes a candidate dynamical state and its boundary demand: polynomial degree grows with the count, and exact exterior evaluation or its controlled compression still has to be acquired. [AGC §2, counted quadratic and exterior factor](../../manuscript/sections/02_pair_chain.tex)

## What a dynamical root has to deliver

Let \(Q_\rho=(\rho-c)^2-D\) for each exterior occurrence. The inherited complete integer hierarchy has \(M=S_1,\ S_n=\sum_{\rm ext}Q_\rho^{-n}\) for \(n\ge1\) and \(T_n=\sum_{\rm ext}(\rho-c)Q_\rho^{-n}\) for \(n\ge2\). Split moments \(P_{p,q}\) have \(p,q\ge0,\ p+q\ge2\) on a separated chart. The symmetric hierarchy is regular at a double while the contour stays cleared. In forward physical time,

\[
 D'=2-4DM,\qquad M'=2M^2-\mathcal F,\qquad
 \mathcal F=12S_2+16DS_3 .
\]

These are inherited componentwise identities of the complete field. Their use backward from \(t_*\) with \(u=t_*-t\) reverses both derivative signs. A candidate state should say which of \(c,D,M,\mathcal F\) and the higher \(S_n,T_n\) it recovers, where the remaining interaction enters, and whether compression bounds the signed, integrated error in its chosen readout. The center also has its own drift. The parent already evaluates these same rational weights on the *single target contour*, for example \(M=-(2\pi i)^{-1}\oint [(z-c)^2-D]^{-1} B\,dz\). All equally informed direct comparisons receive the same geometry, correlations, time samples and arithmetic input. [AGC §2](../../manuscript/sections/02_pair_chain.tex), [§3, full hierarchy and forcing](../../manuscript/sections/03_hierarchy.tex), [§4, backward comparison](../../manuscript/sections/04_continuation.tex), [§6, complete joint allowance](../../manuscript/sections/06_residual_transport.tex)

One candidate joins a marked target packet to a hierarchy of its spatial exterior. Nearby blocks can retain an exact cleared response and distant blocks a finite expansion of the rational weights, translated between centers. The node states must be sourced from \(H\) or independently certified charts. For example, a far block centered at \(y\), of radius \(r\) and count \(N\), sees endpoints \(a,b\) with \(d=\min(|y-a|,|y-b|)>r\). In the Taylor expansion of \(1/[(\rho-a)(\rho-b)]\) about \(y\), the order-\(k\) coefficient has modulus at most \((k+1)d^{-k-2}\), by multiplying two geometric series. Truncating after order \(p\) therefore costs at most

\[
 \frac{N}{d^2}\frac{q^{p+1}[(p+2)-(p+1)q]}{(1-q)^2},
 \qquad q=r/d .
\]

This geometric estimate remains finite as \(a\) and \(b\) coalesce, if the distance to the far block persists. It assumes the endpoints, count and enclosure; it neither acquires these data nor controls time evolution of the packet. For predicting a gap, start from an independently acquired initial counted pair and evolve an enclosure, or solve self-consistently with the arithmetic trace. Positive lower bounds for the unknown gap along the very path to be protected would assume the desired outcome.

## What an infinite tree would mean

For a canonical far-block comparison there is a stronger existing benchmark than absolute summation. At \(0\le t\le1/2\), with an isolated pair of real parameters \(c,D\), \(c\ge16\pi,\ |D|\le1\), the complete exterior contribution from \(|\Re\rho-c|>R\) has main term \(\log(c/(4\pi))/(2\pi R)\) for \(3\le R\le c/2\). The error is bounded by an absolute, unevaluated constant times \(\log(2+c)(R^{-2}+R^{-3}+c^{-1})\). This is uniform slice by slice. Moving-cut differentiation and the sign of the complete \(M\) require further input. A proposed spatial truncation should be compared with this theorem in its regime. [VCD-GT signed far-tail estimate and its scope](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/35_VCD_GT_B07_B08_SYNTHESIS_AND_CONTINUATION_20261117.md)

The spatial structure is especially visible on an interval where the complete divisor is real and simple. Write \(g_n=x_{n+1}-x_n\). An exterior root \(m\) steps from the nearer endpoint has distance \(s=\sum_{j=1}^m g_{n-j}\) on the left or \(s=\sum_{j=1}^m g_{n+j}\) on the right. Its contribution to \(M_n\) is \(1/[s(s+g_n)]\), and the marked edge evolves by
\[
 g_n'=4/g_n-2g_n M_n.
\]
Two neighboring target edges therefore query many of the same spatial blocks, with different endpoints. AGC's block sum already cancels interior node forces exactly. A tree that preserves this cancellation must still control how much of the remaining response can concentrate on one marked edge. An analytical question is whether shared spatial data can bound that concentration or the error in the complete forcing \(12S_2+16DS_3\) uniformly across adjacent queries. For a finite real block with uncontrolled exterior, only its actual terms have the positive cumulative-distance form. Transverse positions matter for the rest. [AGC §2, cumulative distances and block sums](../../manuscript/sections/02_pair_chain.tex) and [fixed-slice control for projected exterior positions](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/35_VCD_GT_B07_B08_SYNTHESIS_AND_CONTINUATION_20261117.md)

Refinement of cuts in a fixed window, enlargement of the spatial window, growth of tensor rank or moment order, and enlargement of the time interval are distinct limits. A terminal count-two node can carry a double at finite depth. Repeated bisection does not ensure a usable wall floor. Infinite raw counts over all heights diverge. For the exterior readout the parent gives an absolutely summable \(M\) tail of order \(O_J(\log R/R)\) for fixed targets on a compact cleared chart, with constants depending on the chart. Fixed-order \(S_n,T_n\) have their own weighted tails. These bounds alone allow neither a uniform truncation in \(n\) nor a time-generator exchange through a growing sequence of trees. A proposed limit needs compatible states under refinement, contour clearance, summable propagated errors (including the weighted exterior and time derivative), and quantitative dependence on height, depth, rank and chart duration. A meaningful outcome could be stable reconstruction of the complete gap drift on a named family or an explicit lower bound on the state's required information. A finite-rank ansatz and a uniform theta gain are separate hypotheses. [AGC §§1–3](../../manuscript/sections/03_hierarchy.tex), [tensor results and scope](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)

## Tests and ownership

The algebra above is generic representation and a local closure diagnostic. An error bound for a named finite family is intermediate evidence. A whole-path improvement requires a paid comparison of the resulting gap, forcing or drift against the parent's direct readout. No universal separation criterion is proposed. The original [results index](../../../../../result-summaries/README.md) and [patterns index](../../../../../avoid/README.md) route the [classification](../../../../../avoid/01_restating_the_target.md), [control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate changes](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scope of exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Analytical premise screen against the [collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) and the [fixed-time premise screen](../../../brainstorm/notes/06_SPATIAL_TTN_ZERO_SPACING_20261119.md). Existing numerical witnesses retain their recorded status.

- The positive three-atom QTT control \(2+2e^{t-T}\cos z\) has a rank-one source at its double. A true count-two readout there has \(D=0,\ D'=2\). It passes the contour and merge identities and lacks the complete theta source. Low rank gives no separation.
- The \(0<c<1\) Euler-factor control has exactly the same real zeros as theta at \(t=0\). At a simple zero multiplying by \(f=1+c\cos(ax)\) changes the heat velocity by \(2f'/f\). An unchanged real-gap list lacks this exterior/analytic response. The full arithmetic source changes.
- Weighted squares, finite-source modifications and finite-prime orbit controls change the full coefficients or fail full reflection. Reflected super-Gaussian and smooth positive-primitive controls lack the theta square expansion. Within the normalized reflected square-comb class reflection rigidity identifies the source; it does not quantify a field floor.
- Fixed-event atoms and finite-profile controls lack the full profile or eventual simplicity. The RH-conditional endpoint perturbation fails ordinary Dirichlet arithmetic. The variable observation kernel fails the physical cosine equation. At their actual counted doubles the same algebra returns zero. A claim using a theta-specific advantage must name and bound an input that these controls fail.

AGC-ST-B01 is the first *conceptual* decision. It must choose a state, geometry, physical evolution and discriminator, with the cost of lost exterior information explicit. Its status and any subsequent authorizations belong to the [AGC-ST register](../research-progress/01_AGC_ST_RESEARCH_PROGRESS_20261119.md). The [AGC register](../../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md) and [Jacobi register](../../01_jacobi_integer_hierarchy/research-progress/01_AGC_JH_RESEARCH_PROGRESS_20261119.md) own their own work. Shared citations are recorded via the [branch reference guide](../references/README.md).
