# First interacting slab test: positive construction, inadequate small family

24 September 2026. Prepared for Edward Baker with substantial GPT-6 (Codex) assistance. Reasoning effort: not exposed; not inferred. Exploratory finite-volume Monte Carlo, not a certified integration, a proof of mixing, or a continuum result.

This session completes the first interacting test proposed in the [opening research plan](YM_REFLECTION_AND_HIERARCHY_RESEARCH_PLAN_20260924.md). The [companion derivation](FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md) supplies the exact reflection-boundary dictionary and discrete error identities. Reproducible sources and the full small record are linked from the [numerics guide](../numerics/README.md).

**Finding.** The finite-lattice reflection construction works algebraically, and the experiment samples an actual four-dimensional interacting Wilson measure. However, the chosen identity/curvature/quadratic-curvature families leave most of the state outside the approximation after the very first step. Their error bounds do not support an accurate controlled truncation. Adding an observable can improve the immediate projection and still worsen a later Wilson expectation. This is new negative evidence about efficiency, not a failure of the positive norm.

## 1. Model, state and geometry fixed before sampling

The model is pure SU(2), theta zero, Wilson action

\[
S=1.6\sum_p(1-\tfrac12\operatorname{Re}\operatorname{tr}U_p),
\]

on \(6^3\) periodic spatial sites and five open physical-time slices \(-2,-1,0,1,2\). Measurements are on slice zero. The finite-slab amplitude is exactly the \(\Omega\) specified in the companion note; the sampler integrates the full lattice, so no approximation to \(\Omega\) is used. This is an interacting 4D lattice model at a single coarse coupling. It is not a two-dimensional plaquette model or a list of prescribed backgrounds. It is also not an established approximation to the infinite-volume YM vacuum.

The spatial contours are rasterized from the chordal Loewner trace driven by \(u(t)=t\). In capacity units the complex tip solves

\[
\dot q=1-2/q,\qquad q(t)=2i\sqrt t+\tfrac23t-\tfrac{i}{18}t^{3/2}+\tfrac1{135}t^2+\cdots.
\]

The solver uses \(s=\sqrt t\), initial \(s=10^{-5}\), and fourth-order integration with maximum \(\Delta s=10^{-4}\). Each point is snapped to its nearest lattice vertex. The trace uses the full prefix of this path; the return chord is rasterized from the straight line to the actual tip. Consecutive snapped vertices are checked to be nearest neighbors. Halving both geometric mesh scales leaves every link word unchanged. This checks the specified rasterization, not convergence of the physical observable as lattice spacing tends to zero.

The sampled capacities and oriented lattice areas are:

| Capacity | Approximate continuum tip | Signed enclosed plaquettes |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0.67418 + 1.94496 i | -1 |
| 2.8 | 1.92667 + 3.09420 i | -2 |
| 6 | 4.27804 + 4.14637 i | -6 |

Exact tip values and signed link words are in the record. The loops are translated over all 216 spatial anchors. The largest fits without winding around the torus. Periodic translations can cross the coordinate seam, which does not change the contractible loop word.

An independent geometry control checks the implicit equation \(q+2\log(1-q/2)=t\), on its continuous branch from the origin, with residual below \(3.8\times10^{-12}\). The refined tips differ by less than \(3.4\times10^{-12}\).

Our link convention is \(U(x,\mu)\mapsto g(x)U(x,\mu)g(x+\hat\mu)^{-1}\), with products ordered along the listed path. Accordingly \(Q_n=U_{\mathrm{trace},n}U_{\mathrm{chord},n}^\dagger\) is based at the initial vertex. This is the chosen lattice transport convention; the residual analysis uses it directly and does not assume a continuum clover insertion identity.

## 2. A fixed local family, not the exact final state as a basis vector

Write \(A(P)=(P-P^\dagger)/2\) for the anti-Hermitian part of a positively oriented spatial xy plaquette. Along the return chord with \(m\) edges, vertices \(v_j\), and prefix transport \(C_j\), define

\[
B_n=\sum_{j=0}^{m}w_j r_j\,C_jA(P_{xy}(v_j))C_j^\dagger,
\quad r_j=j/m,
\]

where \(w_j=1/m\) for interior vertices and \(w_0=w_m=1/(2m)\). At the collapsed chord set \(B_0=A(P_{xy}(b))/2\). Then \(B_n\) is anti-Hermitian, traceless, covariant at the base, and \(\|B_n\|_{\rm op}\le1/2\). It is a dimensionless lattice curvature probe. We do not claim it is the exact generator of a finite rasterized contour change.

For SU(2), let \(v_n^2=\tfrac12\operatorname{tr}B_n^\dagger B_n\), a scalar function of the configuration. Test the nested families

\[
S_n^{(1)}=\mathrm{span}\{I\},\quad
S_n^{(2)}=\mathrm{span}\{I,B_n\},\quad
S_n^{(3)}=\mathrm{span}\{I,B_n,v_n^2I\}.
\]

The last vector is equivalent, after centering, to the scalar quadratic fluctuation of this probe. It does not include all plaquette products, transverse covariant derivatives, or the entire first omitted sector. No \(Q_n\) itself is inserted into these trial families. The same families and coupling were fixed before inspecting their results.

Every configuration supplies the loop Gram matrix, family Gram matrices \(G_n\), and transition overlaps \(T_n\) from the companion construction. The estimates use their ensemble averages. These transition networks are additional observables that can themselves be expensive; this test does not establish a cheaper method of computing \(W\) than direct measurement.

## 3. Sampling and error accounting

There are four independent pseudorandom chains, two starting from identity links and two from independent Haar links. Each has 600 discarded sweeps and 2,400 production sweeps, measuring every sixth sweep: 400 measurements per chain, 1,600 total. A sweep attempts three left multiplications per existing link. The proposal chooses one of the three Pauli axes uniformly and an angle uniformly in \([-1.2,1.2]\); acceptance is \(\min(1,e^{-\Delta S})\). The proposal is symmetric under inversion, so the fixed-link update satisfies detailed balance. The three axes generate SU(2); no quantitative mixing theorem is asserted. Observed acceptance is about 0.599 in every chain.

We average over the 216 anchors **within** each measurement. Those anchors are correlated and are not counted as independent configurations. Standard errors use contiguous batches of 5, 10, 20 and 40 measurements. Nonlinear reduced-model errors use 400 batch-bootstrap replicates for each batch size, preserving all cross-observable correlations and resampling within each chain. The principal numbers below use batches of 20 measurements (120 sweeps), giving 20 batches per chain.

The reported plaquette and loop autocorrelation-time estimates range from 0.50 to 0.76 measurement intervals. These short estimates, including values at the estimator's lower floor, are diagnostics rather than proof of independence. The cold/hot differences for the plaquette and the three loops are 0.34, 0.70, 1.39 and 0.68 estimated standard errors. Error sizes remain comparable over the four batch choices. A two-chain fit checked against the other two chains reproduces the main truncation discrepancy. Longer chains and independent implementations remain appropriate before treating the numerical values as a benchmark.

## 4. What the interacting data say

The all-plaquette mean is \(0.385525\pm0.000207\). The central-slice loops are:

| Capacity | Direct Wilson estimate | Estimated standard error |
|---:|---:|---:|
| 1 | 0.388006 | 0.000716 |
| 2.8 | 0.150381 | 0.000939 |
| 6 | 0.002404 | 0.000891 |

The last loop has limited relative precision. It should not be used to rank differences of order \(10^{-3}\) between truncations.

The middle loop provides the clearest comparison:

| Family dimension | Reduced estimate at 2.8 | Reduced minus direct | Bootstrap error of that difference | Forward/backward bound |
|---:|---:|---:|---:|---:|
| 1 | 0.150548 | +0.000168 | 0.000746 | 0.849452 |
| 2 | 0.135442 | -0.014939 | 0.000666 | 0.800524 |
| 3 | 0.136709 | -0.013671 | 0.000678 | 0.798915 |

The corresponding 95% percentile ranges for the dimension-two and dimension-three differences are about \([-0.01629,-0.01368]\) and \([-0.01505,-0.01238]\). The scalar-family discrepancy is statistically unresolved. Its apparent success is not a controlled factorization theorem: this lattice geometry makes its prediction the square of the measured one-plaquette mean, while the exact dynamics also contain the memory terms in the companion note.

The first nonzero loop is reproduced exactly by every family on the common empirical measure. That is built into orthogonal projection when \(I\) is retained, since the discarded residual is perpendicular to the readout. It is not an independent accuracy test. On independent validation chains even this equality acquires ordinary sampling error.

The first-step residual norms are 0.92166, 0.86983 and 0.86949. The retained squared norms immediately afterward are only 0.15055, 0.24340 and 0.24398. Adding the curvature probe captures additional state, but most of the full unit norm remains outside the family. The quadratic probe supplies little further improvement at this first step.

For the middle loop, the simpler local-step output bounds are 1.01967, 0.96233 and 0.96196. The forward/backward estimate improves them to the values in the table but still gives no useful percent-level control. At the final loop, even the forward/backward bounds are 1.29808, 1.35460 and 1.36511. These should be compared with the normalized trivial bound \(|\widehat W-W|\le2\); a bound smaller than two is not by itself useful accuracy.

The actual successive-step distances are approximately 1.10634, 1.10634 and 1.39819 in the positive norm. These are large finite changes. The test is therefore not in the small smooth-step regime of the preliminary continuous theorem. Rasterized chord rearrangements can change several plaquettes at once even when the underlying continuum tip varies smoothly.

### Why the larger family can do worse

At one step, a larger destination subspace improves the projection of the **same** incoming state. In a sequence, enlarging the family changes the incoming approximate state as well. It can retain an amplitude that the following compression treats inaccurately, changing the later scalar readout. Nested trial spaces alone do not guarantee monotone improvement of the final output or of its accumulated bound.

The data display exactly that distinction: a substantially smaller first residual accompanies a substantially worse middle Wilson estimate. A basis must approximate the propagation and return of the retained modes, not merely explain more of one configuration-wise fluctuation.

## 5. Verification, and what its passing means

The sampler checks staples against independent full-action differences, including open-time boundary links; maximum observed discrepancy is below \(3.8\times10^{-12}\). It checks all measured moments under random lattice gauge transformations, with discrepancies below \(1.9\times10^{-12}\). Site reflection exchanges the two half actions and preserves the central part to below \(9.1\times10^{-12}\). Quaternion unitarity errors are below \(7\times10^{-16}\). Separate Python controls compare quaternion multiplication against explicit complex matrices and check Haar first and second moments.

Thirty independent dense complex-unitary examples verify the moving projection residual, norm loss and forward/backward output bound. All empirical Schur residuals and output inequalities also pass on the measured moment sets and their bootstrap resamples. The loop Gram matrix has minimum eigenvalue approximately 0.5213; the unnormalized three-vector family Grams have condition numbers from about 220 to 2,702.

Positivity of an empirical Gram matrix is largely algebraic when all moments are formed from the same configurations. It does not certify Monte Carlo convergence. Similarly, the rigorous residual inequalities apply to true ensemble moments; the numerical bound values and uncertainty estimates here are not interval-certified bounds on those moments. No new continuum theorem follows from these controls.

## 6. Updated viable route and the next bounded experiment

The reflection-boundary question has a concrete answer at fixed lattice spacing. The next work should therefore focus on the **choice and propagation of observable sectors**, with the following priorities.

1. **Use local contour-deformation sectors before adding more powers of one averaged chord probe.** Decompose each contour change into elementary plaquette moves. For a transported SU(2) plaquette \(P\), write \(P=\alpha I+A(P)\), \(\alpha=\tfrac12\operatorname{tr}P\). Both the fluctuating scalar part and the anti-Hermitian part are present in the exact finite step. A family containing these local pieces resolves a single such increment algebraically. Products of the pieces are then unavoidable when several moves are propagated. Test families truncated by local support and product degree, and record which omitted products dominate both forward and backward residuals. This is a structured hierarchy, not a new finite-closure claim. Including every exact target loop as a basis vector would make the test tautological and is not the proposed comparison.
2. **Test slice-only smoothing and a finer contour schedule together.** The companion note proves that gauge-covariant SU(2)-valued smoothing confined to the spatial boundary preserves the reflection construction. Predeclare a few smoothing scales, measure the change in the target loop as well as \(\ell_n\), and subdivide multi-plaquette changes. Smoothing may reduce state leakage, but it changes the observable; its bias cannot be hidden in the truncation bound. A four-dimensional smoothing prescription requires a fresh reflection-support argument.
3. **Use forward and backward residuals to select the family.** Equation (16) reveals which omitted state components can return to the Wilson readout. Compare the fixed basis in this session with a modest local-sector family under the same ensemble and geometry. Estimate basis coefficients on training chains; validate predictions and residual moments on held-out chains. Do not select a family because its scalar answer happens to agree through cancellation.
4. **Make success quantitative before increasing lattice size.** A proposed pilot gate is a forward/backward output bound below 0.01 for the middle contour, together with statistically resolved agreement on independent chains and a disclosed measurement cost. The number 0.01 is a proposed future decision threshold, not a property established here. Require stability under at least one added contour subdivision and one local-sector enlargement. If success depends on including essentially every path product, record that the hierarchy is descriptive but has not shown useful compression.

After that gate, vary the slab thickness and spatial volume, then relate lattice spacing, physical smoothing scale and contour geometry along a coupling trajectory. Those are necessary before drawing vacuum or continuum conclusions. The present one-coupling calculation supplies no such trajectory.

For the original N4SYM program, the result supports the value of keeping a full positive state and quantifying omitted sectors. It supplies no evidence that the scalar-coupled N4SYM hierarchy closes. For the arithmetic program, nothing here creates the specified prime-delay response or upgrades reflection positivity into the target cumulative Weil-form inequality. Those remain independent dictionary and norm-matching problems.

**Session conclusion.** A previously conditional boundary realization has become an explicit finite-slab derivation. A first genuine interacting calculation has made the efficiency obstacle measurable, and has ruled out treating the opening small-family ansatz as already controlled in this coarse regime. Local plaquette sectors, boundary-preserving smoothing, and the backward readout hierarchy are the next concrete tests; simply increasing the power of the same averaged curvature probe is no longer the best-supported first move.
