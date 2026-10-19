# What S07 is missing, and which geometric alternatives deserve work

18 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring and coordinating model **gpt-6-astra (Codex)**, actual reasoning effort **ultra**, verified from session metadata. Internal LLM assessment with delegated review; no specialist human review. Recommendations below are proposed research tasks, not established new theta estimates.

## Assessment

S07 has supplied an exact geometric dictionary, a complete boundary identity, and an informative obstruction. It has not supplied the quantitative estimate connecting that geometry to a smaller error or a positive margin for the physical pair $(H,H_x)$. That missing connection has two parts: controlling the observation on the physical path, and turning that control into signed information or a certified nonzero approximation.

The strongest practical geometric alternative is **physical boundary winding**, whose collision-counting theorem and finite pilot already exist elsewhere in the repository. The most promising new analytic direction within S07 is **a theta-constrained evaluation estimate for the actual source and its approximation error**, followed by a paid physical comparison. A mixed Green/adjoint method is a reasonable second option if its observation functional is first shown to be admissible. Changing form degree merits only a short sign audit at present.

Across the whole portfolio, the demonstrated S01/S02 error reductions and S03's residual cancellation remain better supported priorities than a new ambient construction. This is a judgment about evidence and the number of missing estimates, not a theorem that geometry cannot help. The [overview][plan] assigns these proposals stable task IDs; the [tracker][tracker] records their unexecuted status. Read the repository [result summaries][summaries] and [patterns to avoid][avoid], particularly [geometric realizations][results16], [local collision geometry][results13], [target reformulations][avoid01] and [scoped exclusions][avoid07].

## What the completed work establishes

The [S07 continuation][s07] works on

$$
\Omega=[-1/4,1/4]_p\times[1,4]_q\times\mathbb T^2,
\qquad \gamma(q)=(0,q,0,0).
$$

The canonical complete source is the global covariant differential image

$$
S=\frac{q^{1/4}}{16\pi^2}
   (q^2\mathcal D_z^4-3\pi^2)\vartheta(z,p+iq).
$$

Its restriction is the physical source $\Phi(u)$ with $q=e^{4u}$. The original theta section is holomorphic in the original complex structure; this fourth-order covariant source is generally not itself holomorphic. Physical source integration uses $du=dq/(4q)$, rather than the path's metric arclength. A bulk integral over the tube, a fiber norm, and the oscillatory physical transform are therefore different observables.

Three conclusions constrain the next step.

1. **The zero-form identity has no positive curvature term.** Although the line-bundle curvature is nonzero, $\Lambda_JF=0$. For the canonical source, the full-fiber-averaged self-current vanishes on each of the four $p/q$ boundary faces. The identity consequently equates bulk energies; it does not provide a positive physical margin. This does not say that every mixed source–test boundary term vanishes.
2. **Generic first-order bulk control cannot bound the path observation.** A smooth section can concentrate in the three directions transverse to $\gamma$, retain a fixed path value, and have first-derivative energy tending to zero. The exhibited family also has zero boundary current. This excludes the specified estimate for arbitrary smooth sections. The cutoffs destroy canonical theta coefficients, holomorphy and Jacobi relations, so the counterexample does not settle a genuinely constrained theta/PDE class.
3. **The simplest additional operator is not automatically integrable.** The raw rough-Laplacian restriction restores a growing zero mode. Its ordinary positive-heat half-line transform diverges. Any compensation must be combined before integration, and its physical image must be derived. S06's completed current already shows the risk: its sign is exactly inherited from the known Laguerre quantity, rather than supplying an independent estimate.

These are useful accomplishments because they identify precisely which convenient shortcuts are unavailable.

## Five inputs still missing

| Missing input | What would count as supplying it |
| --- | --- |
| An admissible source/error class | Explicit automorphy, gauge, differential constraints and norms containing the actual source **and the residual to be estimated**, or a paid bound for the residual outside that class. |
| A quantitative observation estimate | An explicit constant controlling the physical path functional on that class, including the remaining base-variable trace. Fiber holomorphy alone does not prevent concentration in $p$. |
| Complete observation bookkeeping | The physical measure and oscillatory test, all four tube faces when used, cutoff/commutator terms, gauge changes, source tails outside the tube and conversion to the physical normalization. |
| An independent exclusion input | A certified nonzero approximant/anchor plus a smaller complete error, or a genuinely independent signed estimate. An upper norm bound or positive bulk norm is insufficient. |
| Useful constants and scope | Uniform constants on a declared domain that improve a matched existing estimate, margin, cost or coverage. A formal identity and isolated point values do not establish this. |

For example, with a physical first-jet approximant $\widehat V$ and a proved error bound $\|V-\widehat V\|\leq\varepsilon$, a bound $\|\widehat V\|>\varepsilon$ excludes collision. The geometric work would have to improve $\varepsilon$ or its acquisition cost. Merely bounding $\|V\|$ from above supplies neither inequality needed for exclusion.

A one-dimensional reproducing kernel built from the exact full source can be circular as an estimating device: its evaluation constant may encode the very point value one needs to control. A useful constrained space must permit an independently computable estimate, with explicit approximation and tail errors.

## Alternative A: constrained theta-jet evaluation

**Recommendation: the first new analytic feasibility task within S07. Tasks S07-T1, then S07-T2/T3 if successful.**

Start with the existing metric and marked tube. A candidate fiber space is the covariant jet span

$$
V_4(p,q)=\operatorname{span}\{
\vartheta,\mathcal D_z\vartheta,\ldots,\mathcal D_z^4\vartheta\}.
$$

This is a proposal to audit, not an assertion that every approximating remainder lies in it. Verify transition laws, the relevant inner product, linear independence or the proper quotient, and the relation between the chosen covariant derivative and the level decomposition. On a valid independent basis $e_j$, form the Gram matrix $G$ and evaluation row $\ell=(e_j(z_0))_j$ in a compatible frame. Elementary finite-dimensional duality gives an evaluation constant of the form $\ell G^{-1}\ell^*$; an orthonormal basis makes it the sum of squared point evaluations. This algebra does not by itself establish source admissibility, uniform constants or useful physical errors.

The finite-dimensional theta/Landau-level analogy is legitimate background: Onofri constructs a finite-dimensional holomorphic lowest level on a torus and obtains higher levels through a covariant creation operator; those higher levels need not be holomorphic. It does **not** identify that model with the present metric and source operator, or prove the needed residual estimate. That identification is a task. See [Onofri, Sections 4–5](https://arxiv.org/html/quant-ph/0007055v1).

Proceed in this order:

1. Prove source inclusion and determine what happens to the error of the intended approximation. A naive Fourier cutoff may violate the bundle's automorphy; if so, include a projection/complement payment.
2. Bound the fiber evaluation constant uniformly on the existing base rectangle.
3. Supply the remaining trace to $p=0$ from paid base derivatives, analyticity or the actual differential relations. Removing the two fiber concentration directions does not remove the third one.
4. Apply the estimate to an error functional that enters S03 or a direct first-jet consumer. Keep the signed integral intact where possible; bounding the full positive source mass can erase the cancellation the calculation needs.
5. Compare the resulting physical error with the strongest arithmetic estimate on the same box. Stop if the conversion and tails consume the entire gain.

The advantage is a small, explicit calculation using canonical theta restrictions that the smooth concentration controls lack. The risk is that the estimate is true but far too large, or applies only to the exact source and not to its approximation error.

## Alternative B: physical boundary winding

**Recommendation: the nearest established geometric route to a usable certificate. Task GEO-T1.**

The [Investigation 22 winding note][winding] and its [review][winding-review] already give a boundary degree for $(H,H_x)$, or $H+iH_x$. Under the theorem's isolation and boundary hypotheses, local collision indices all have the same sign, with contribution $-\lfloor m/2\rfloor$ for multiplicity $m$. Thus a certified nonzero boundary with winding zero excludes interior collisions.

This approach uses the physical first jet directly. It does not need S07's bulk-to-path estimate, and a paid real first-jet enclosure such as S03's calibrated output is a potential input. The spectral and temporal faces, both walls, tangential root flux, corner compatibility and whole boundary segments all have to be controlled. An ordinary root of $H$ on a wall need not be a collision when $H_x\ne0$; its flux cannot simply be discarded.

The existing sign-changing pilot on $[0.01,0.2]\times[25,45]$ used 234 certified boundary segments and obtained winding zero. Both the winding and direct method succeeded. Winding used 464 segment-range and 234 vertex evaluations, versus 255 direct range evaluations; these are not interchangeable units of work. Both shared 76 validated midpoint integrals, with two additional redundant wall checks in the winding run. The reported timing benefited from fixed-time coefficient reuse. This establishes feasibility, not a universal cost advantage from checking a boundary.

The bounded next task is to select a box from an identified consumer bottleneck, freeze the common source/accuracy/setup budget, and compare complete winding and optimized direct certification. Existing-box success is validation. A milestone requires new covered cells or a matched cost improvement. The [fresh planning controls][screen] replay moving-wall examples precisely because equal endpoint root counts can conceal collisions when wall flux is omitted.

Winding is consequently more promising for practical certification than additional abstract duality at present. Its limitation remains serious: the boundary itself must be separated from zero. A succession of finite rectangles does not solve the uniform real bridge or complex exterior.

## Alternative C: an observation-specific mixed Green or adjoint estimate

**Recommendation: conditional second analytic option, not an immediate parallel construction. Tasks S07-T1/T2.**

Choose the physical error functional first. Derive an operator equation for the **complete** fourth-order source or remainder, including commutators and compensations. A successful adjoint construction would express its physical observation error as a residual–adjoint pairing plus all boundary, tail and approximate-adjoint errors.

The general idea of weighting residuals by a dual problem to estimate a particular output is standard; [Becker and Rannacher](https://doi.org/10.1017/S0962492901000010) develop it for finite-element error estimation. Their result is methodological background, not an applicable theorem for this source or singular observation.

The main obstacle is admissibility. A delta distribution on a codimension-three path is not automatically a bounded functional on the first-order energy space already ruled out by S07. One must use a proved constrained projection, stronger paid regularity, or a regularized observation with its bias explicitly controlled. A convenient ambient dual test whose restriction matches the physical test does not by itself turn its bulk pairing into the physical path integral.

This route may preserve the sign and phase information lost by a self-energy estimate. It also has more moving parts than the finite-jet calculation: the operator, dual domain, boundary realization, convergence and complete physical return must all be justified. Stop early if the representer requires exactly the unavailable trace inequality.

## Alternative D: other form degrees and curvature identities

**Recommendation: low priority; perform a short algebraic screen before expanding the geometry. Task S07-T4.**

The zero-form result alone does not show that curvature acts trivially on every bundle-valued form. It is therefore reasonable to compute a specific positive-degree Weitzenböck or ordinary Kodaira curvature action, its eigenvalues, boundary conditions and source/test projection.

There is, however, an additional limitation for the natural quaternionic proposal. Verbitsky identifies $\Theta_+$ with the weight-two curvature component and uses it in the commutator $[\Theta_+,\Lambda_\Omega]$; see [Proposition 3.3 and Theorem 3.6](https://arxiv.org/pdf/math/0604303). Hyperholomorphic curvature is SU(2)-invariant; see [the earlier paper, Section 2](https://arxiv.org/html/alg-geom/9307008v1). **Inference for the present connection:** this invariant curvature has zero weight-two component. Merely changing degree in that same quaternionic identity therefore does not create a positive curvature term. This is a local projection argument, not a new coercive theorem.

An ordinary positive-degree curvature operator can still be nonzero, but nonzero is not positive. Any favorable eigenspace must contain the relevant physical object, remain compatible with the differential/boundary problem, and lead to an independently paid physical estimate. Compact vanishing results do not automatically apply to the marked tube with boundary.

Accordingly, new metrics, compactifications, twistor rotations and transform constructions should wait for a named source/test pair and a candidate controlling term. This is a sequencing recommendation; it does not rule out those subjects.

## Decision and evidence status

Allocate the principal analytic work to S03's complete residual and consolidate S01/S02. Within geometry, select **one** initial branch: constrained theta-jet admissibility for new analytic information, or a matched physical winding comparison for practical certification. Keep mixed-adjoint work conditional and form-degree work at the algebraic-screen stage.

The [planning control record][screen] contains fresh inherited collision/witness checks and 2,122 moving-wall assertions across 88 control domains. Those checks support the relevance of the safeguards, not the truth of any proposed new trace, kernel, adjoint or curvature estimate. The exact premise screen and future validation obligations are in the [overview][plan]. No result in this planning note closes the real bridge or the complex exterior.

[plan]: 01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[tracker]: ../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[s07]: ../07_geometric_duality_and_quaternionic_symmetry/notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md
[screen]: ../numerics/RESEARCH_PLAN_CONTROL_SCREEN_20261018.json
[winding]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[winding-review]: ../../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[results16]: ../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[results13]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid01]: ../../../../../avoid/01_restating_the_target.md
[avoid07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
