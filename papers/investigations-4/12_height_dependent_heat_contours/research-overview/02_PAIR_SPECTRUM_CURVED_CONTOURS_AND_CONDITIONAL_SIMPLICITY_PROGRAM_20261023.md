# Pair spectrum and curved heat contours for conditional simplicity

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model agents checked the source-to-force identities, spectral normalization and contour distinctions; no specialist review.

**Primary objective:** develop analytical control of the pair matrix and Vandermonde under the canonical theta heat flow, with **RH implying simple zeros** as the first application. RH implying **almost all zeros simple** is an important intermediate theorem. The tools should retain explicit assumptions so that an eventual investigation of RH can reuse the parts that do not depend on RH.

The central question is whether known information about theta and H can control how many collision modes survive as heat time approaches zero. Curved contours and backward transport from long-time data are candidate methods for obtaining that control. The work should proceed through analytical identities, inequalities and error theorems. Numerics may check algebra, constants and sharp examples; they are supporting evidence, not the main task sequence.

This overview sets the current analytical priority. The [first overview][old-overview] retains the original physical-cap program as a parallel application. The [sole progress register][progress] owns task status; HDC-07 through HDC-12 below are proposed work packages, not completed theta estimates. [Notes 04–06][notes] supply the existing statistical and spectral implications. No new simplicity proportion is claimed by this plan.

The [dated progress snapshot](../research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md) distinguishes the established identities and finite transfers from the open theta estimates, and specifies the next analytical deliverable. Task status remains in the existing register.

Read the [result index][results], [local heat geometry][geometry], [theta identities][theta], [control register][controls], and [avoid index][avoid], particularly [target classification][a01], [coupled estimates][a12], [numerics before structure][a10], and [scoped conclusions][a07].

## The field and the observable

Use the unchanged canonical source and normalization

\[
 H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
 \qquad H_\tau=-H_{zz},\qquad
 8H(0,z)=\xi(1/2+iz/2),
\]
\[
 \Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
 \tag{1}
\]

The complete coefficients, reflection identity, source tails and oscillatory correlations are available information. Positivity of a source or a collection of moments is a weaker premise. The [theta-identity register][theta] identifies the relevant exact reconstructions and cancellations; the first analytical note should state which of them it actually uses.

For a complete finite simple population at one common time, write H=UP, with P=product_j(z−z_j) monic and b=partial_z log U. Set

\[
 \Delta=\prod_{i<j}(z_j-z_i)^2,\qquad
 W_{ij}=(z_i-z_j)^{-2},\qquad
 L=\sum_{i<j}W_{ij}(e_i-e_j)(e_i-e_j)^T.
 \tag{2}
\]

For distinct real roots, L is a positive semidefinite graph Laplacian and equals one half of the Hessian of −log Delta. For complex roots it is generally complex symmetric, with no inherited positive order. Delta is a scalar discriminant, not a matrix; the raw matrix of squared distances has rank at most three and is not the N-mode object used here.

The collision singularity is part of the information. For H=z²−2t, Delta=8t and the nonzero eigenvalue of L is 1/(4t). Differentiating log Delta strengthens the singularity rather than smoothing it. The rescaled matrix tL and bounded spectral filters retain a finite collision signature. The distinction between a regular discriminant and singular logarithmic derivatives must be maintained along every contour.

## What each assumption supplies

| Input or conclusion | Required basis | Information it does not supply |
| --- | --- | --- |
| Heat equation, real type, complete source representation, reflection and source tails | Canonical theta data; no RH | A favorable sign for an oscillatory quotient |
| Prepared finite polynomial, wall integrals, discriminant evolution | A complete isolated population with H nonzero on its spatial wall; no RH needed | Such a wall on an arbitrary proposed domain |
| Positive semidefinite L and real spectral inequalities | Distinct real roots on the particular slice | Reality on a negative or complex-time continuation |
| All roots real at t=0, and real and simple for t>0 | RH plus the classical real-zero heat preservation and local splitting laws | Simplicity at t=0 or a negative all-real interval |
| Full adjacent-gap compression and the endpoint spectral consumer | Under RH, the complete canonical real-root system and its paired product | A useful upper spectral bound |
| Late-time clock approximations and complete-source saddle estimates | Their stated rank, height, time and complex-strip ranges; no RH for the proved late anchors | Uniform backward control to zero or growing-rank estimates outside those ranges |
| Curved-path or resolvent continuation | Its own wall, chart and invertibility bounds | Positivity merely because the path begins on a real slice |

Each future note should identify the first line where RH enters. A generic lemma that assumes a real population should say so; its application may obtain that reality from RH or from a separate late-time theorem. Neither origin should be hidden inside the notation.

For a future RH application, endpoint reality itself must be established. Simple nonreal roots are not excluded by a zero collision count, and the RH-conditional positive-spectrum consumer cannot be imported unchanged.

## The two simplicity targets

For a complete endpoint population of N labels and its positive-time descendants, define

\[
 R(t)=(I+4tL(t))^{-1},\qquad
 q(t)=\operatorname{Tr}(I-R(t)).
 \tag{3}
\]

Under RH, [Note 06][n6] uses the complete adjacent-gap bound g²<=8t and a matching comparison to prove that every multiple endpoint contributes at least one eigenvalue of L(t) at least 1/(4t). If M_0 counts all labels at multiple endpoint sites, then

\[
 M_0\le6q(t).
 \tag{4}
\]

Two distinct analytical targets follow:

- **Every-zero simplicity in a finite complete population:** prove q(t)<1/2 at a source-prescribed positive time. Any multiple endpoint would force q(t)>=1/2. An all-height theorem needs complete coverage and uniform control, not a finite collection of examples.
- **Almost-all simplicity:** prove q(t_h)=o(N(h)) for prescribed times and populations covering all but o(N(h)) endpoint labels. This tolerates a sparse exceptional set and is the first global milestone to pursue if the stronger threshold is inaccessible.

Full PCC is not required. The alternative earlier-time consumer in [Note 05][n5] uses a near-zero upper bound for the pair measure of the real projections of **all** roots, including nonreal conjugates. Keep it available for comparison; PCC for only the real-root subset misses the relevant defects.

The finite implications are established interfaces. Claiming that their upper bounds hold is the outstanding source problem. Choosing times after inspecting unknown endpoint separations would restate the conclusion.

## Analytical priority one is the complete evolution of L

The inherited root and weight equations are

\[
 z_i'=2\sum_{j\ne i}(z_i-z_j)^{-1}+2b_i,
\]
\[
 W_{ij}'=-2W_{ij}\left[
 4W_{ij}-2\sum_{k\ne i,j}
 \frac1{(z_i-z_k)(z_j-z_k)}
 +2\frac{b_i-b_j}{z_i-z_j}\right].
 \tag{5}
\]

The finite factor U contains all exterior roots and the nonzero source factor. Its forcing is essential. The [earlier pair-matrix note][pair] already shows that deleting it gives a false monotonicity prediction for actual late-time theta roots. Re-deriving an unforced equation is not the next task.

There is a useful way to obtain that forcing from H. Let Gamma be a positively oriented simple zero-free spatial wall enclosing exactly the complete cluster. For z inside it,

\[
 b(\tau,z)=\frac1{2\pi i}\oint_\Gamma
 \frac{H_w(\tau,w)}{H(\tau,w)}\frac{dw}{w-z},
\]
\[
 \frac{b(z_i)-b(z_j)}{z_i-z_j}
 =\frac1{2\pi i}\oint_\Gamma
 \frac{H_w/H}{(w-z_i)(w-z_j)}\,dw.
 \tag{6}
\]

Residues subtract the internal poles of H_w/H in the first formula; the second follows by taking its divided difference. Both extend across an internal collision when the proper cluster and wall survive. If the roots lie distance at least d from the wall, the second integral has the fallback bound length(Gamma) sup_Gamma|H_w/H|/(2pi d²). This avoids an internal-gap denominator, but still requires a proved wall floor and complete source bounds. The priority is to improve on separate absolute estimates by retaining the signed correlation needed in (5).

Differentiate the complete bounded statistic before estimating it. On a real simple slice, with v_ij=e_i−e_j,

\[
 \boxed{q'(t)=4\operatorname{Tr}[R^2(L+tL')]
 =4\sum_{i<j}(W_{ij}+tW_{ij}')\|Rv_{ij}\|^2.}
 \tag{7}
\]

Indeed R'=−R[4L+4tL']R and cyclicity of trace gives (7), without assuming that L commutes with L'. This expression retains the cancellation between time scaling and pair motion. In a pure Hermite birth W+tW'=0. Bounding L and tL' separately would lose that cancellation.

**HDC-07 deliverable:** one analytical note deriving the complete source-to-filter evolution on a declared finite domain and proving an explicit source-based estimate for its coupled force or residual. Express its constants through complete theta data, wall geometry and justified errors. State the estimate's height/time scaling and show what it gains over the absolute fallback. If it cannot improve that bound within the chosen information class, record the precise obstruction rather than beginning a numerical sweep.

## Curved contours and the evolving discriminant

Three geometries are useful, with different equations.

**A common complex-time path.** All roots are evaluated at tau=gamma(s). On regular segments,

\[
 \frac d{ds}\log\Delta
 =\dot\gamma\left[
 8\sum_{i<j}(z_j-z_i)^{-2}
 +4\sum_{i<j}\frac{b_j-b_i}{z_j-z_i}\right].
 \tag{8}
\]

The discriminant Delta, the squared Vandermonde, is invariant under root permutations. Its logarithmic differential retains event residues; going around a collision transports labels without removing the collision. Complex tangent directions do not preserve the real sign of an integrand.

For a scale a(s), set F=I−(I+aL)^−1. The exact path derivative is

\[
 \dot F=R_a[\dot a\,L+a\dot\gamma L_\tau]R_a,
 \qquad R_a=(I+aL)^{-1}.
 \tag{9}
\]

On a complex path the required estimate is a resolvent norm or smallest-singular-value bound. Event-freeness alone is insufficient. For H=z²−a_0²−2tau, a_0>0, the continuation of (3) is

\[
 q(\tau)=\frac{2\tau}{a_0^2+4\tau}.
 \tag{10}
\]

It has a pole at −a_0²/4 while the roots remain simple; their collision occurs at −a_0²/2. Thus a complex contour for q has an additional invertibility obligation beyond the discriminant contour.

**A moving spatial contour at common time.** Let Gamma_s enclose the same complete cluster at gamma(s), with H nonzero on the moving wall. Its power sums satisfy

\[
 p_k(s)=\frac1{2\pi i}\oint_{\Gamma_s}z^kH_z/H\,dz,
 \quad \dot p_0=0,
 \quad \dot p_k=\frac{k\dot\gamma}{2\pi i}
 \oint_{\Gamma_s}z^{k-1}H_{zz}/H\,dz\quad(k\ge1).
 \tag{11}
\]

Wall-motion terms integrate to an exact derivative around the closed curve. These power sums reconstruct the prepared polynomial and Delta through internal collisions, without choosing singular root labels. This is a natural analytical companion to spectral evolution on regular slices.

**A height-dependent time graph.** Sampling tau=−epsilon(x)+i sigma evaluates different spatial positions at different heat times. The resulting field is generally not holomorphic in z. Its sampled gaps do not obey (8) automatically. Start with common-time populations on bands, retain joins, and then derive the graph interpolation, slope and transversality terms. Any smooth graph theorem must state these terms explicitly.

**HDC-08 deliverable:** an analytical contour-transport theorem for the prepared polynomial, discriminant and chosen spectral observable, with a complete population and explicit wall/resolvent conditions. Establish common-time moving contours first, then the height graph. If the physical cap is used, retain its distinct product D=product_j H_z(tau,z_j), its analytic factor, complementary spatial pieces and all connecting faces. The Vandermonde phase alone is not the whole physical cap. Compare the resulting estimate with direct wall/discriminant estimation using the same source information.

## Transporting long-time information backwards

The [prior pair-matrix estimates][pair] and [differentiated saddle analysis][saddle] provide complete-source late-time information. Their fixed-rank large-heat regimes, growing-rank complex-cap regimes and high-height fixed-positive-time regimes must be kept separate. Each imported approximation needs its onset, spatial normalization, rank range and derivative errors stated. A scalar saddle scale must not be denoted L when L already means the pair matrix.

The backward task is to prove an error theorem that carries enough terminal information into a useful early bound. For an explicit reference q_*, the exact real-time identity is

\[
 q(t_0)=q_*(t_0)+[q(T)-q_*(T)]
       -\int_{t_0}^T(q'-q_*')\,dt.
 \tag{12}
\]

For example, a terminal upper error E_T and a lower bound q'−q_*'>=−e(t) give q(t_0)<=q_*(t_0)+E_T+integral e. This fixes the direction of the estimate actually needed. Use (7) and the complete source force to bound the residual together. Include moving normalization, population changes and accumulated backward error; forward contraction cannot simply be inverted as a stable estimate.

Leading long-time information alone can miss the endpoint defect. The simple-endpoint family in (10) has q(T)=1/2−a_0²/(8T)+O(T^−2), while the double-endpoint model a_0=0 has q(T)=1/2 exactly. A useful backward theorem must resolve the subleading information or obtain an independent source inequality that replaces it. This is a control on the proposed use of asymptotics, not an exclusion of backward analysis.

Decreasing real heat time damps source frequencies and smooths the field, but the reverse motion of individual zeros can still be sensitive to small errors. Distinguish smoothing of H from stable reconstruction of its zero geometry. A curved detour may improve available source estimates; exact analytic path equality by itself does not provide that improvement.

**HDC-09 deliverable:** one matched-reference backward theorem with a declared terminal regime, complete residual, explicit error amplification and a stated early-time conclusion. First seek a finite-population analytical estimate. Then determine exactly what additional uniformity is required for growing height. Use both simple and multiple endpoint controls to test whether the retained terminal precision can distinguish them.

## Source inequalities and the route to the first theorem

The main substantive estimate is an upper bound for q or its large-eigenvalue count, not another expression for the same unknown quantity. HDC-07 and HDC-08 identify source observables; HDC-09 provides a possible transport mechanism. **HDC-10** must prove a bound strong enough for one of the two simplicity targets, either directly from theta or by the complete backward/curved-contour estimate.

For the density-one route, a candidate scale is t_h nu_h²→0, where nu_h is the mean local root density. A uniform tightness theorem for the spectrum of L/nu_h² along these times would then suffice. That tightness is an unproved source estimate, not a consequence of naming a mean spacing. For the every-zero route, work with the unnormalized threshold q<1/2 on complete blocks, or an equally explicit event-sensitive alternative.

Prefer complete theta reconstructions, contour ratios and correlated estimates before separately bounding source modes. The exact reflection and arithmetic coefficients distinguish the canonical source, but identifying it is not itself an upper spectral bound. Every proposed approximation must report what information it discards and whether the discarded part could carry the collision signature.

**HDC-11** assembles the conditional theorem only after a useful estimate exists. Keep endpoint labels, spatial coverage, wall crossings and all multiplicities explicit. An o(N) set of omitted roots can be paid at the root-count stage; it does not automatically create an o(1) error in a pair statistic. Prove the density-one conclusion if that is what the error supports, and preserve the stronger all-simple goal without claiming it follows.

**HDC-12** is a future RH-free extension, presently limited to maintaining the assumption audit. Reusable ingredients include complete source formulas, prepared-polynomial transport, discriminant charges and verified late real anchors. Extending these to RH requires establishing endpoint reality without using the RH-derived global real spectrum or adjacency. A common negative all-height real anchor is unavailable: [Rodgers–Tao][rt] prove the de Bruijn–Newman constant is nonnegative. Height-dependent local constructions have separate scope.

## Controls and the supporting role of numerics

Apply the [registered controls][controls] to the premise actually being used. The quadratic and Hermite heat polynomials check the collision scale and prevent a bounded filter from erasing a real event. The simple-endpoint quadratic (10) checks extra resolvent poles and terminal asymptotic precision. The sine heat field checks the exterior factor. Euler-factor and close endpoint controls show why generic real-root heat dynamics cannot alone distinguish canonical simplicity. Do not assign global real-root hypotheses to weighted-square or reflected controls unless established; their source/reflection failures are recorded in the control register.

Future notes should contain proofs, stated domains and source-derived constants or asymptotic errors. Small exact computations may verify factors, signs and matrix identities. Targeted numerical experiments may discriminate between two precise analytical conjectures or locate a sharp regime, and interval numerics may later support a finite theorem. Broad heat/height sweeps, fitted spectral laws and large certification campaigns are not the default next step. No numerical observation upgrades an assumed wall, gap or RH premise.

The immediate next note is **HDC-07: complete source control of the filtered pair spectrum**. Its endpoint is a usable analytical force/residual bound, with control examples and its precise dependence on RH. HDC-08 may proceed in parallel on geometry. The backward and global tasks use those results, with separate acceptance criteria in the [progress register][progress].

## Reading path

Start with [HDC Note 06][n6] for the spectral consumer, [LHCT Note 06][pair] for the forced matrix dynamics, [BW10 Note 19][motion] for the full root product and tail estimates, and [BW10 Note 20][saddle] for differentiated late-time data. Use [HDC Note 03][n3] for complete physical boundary accounting and the scoped direct comparison; [HDC Note 05][n5] supplies the alternate earlier-time statistical consumer. The [current program review][review] checks this overview's assumptions and priorities.

For primary literature, [Polymath][poly], Proposition 3.1 and its stated asymptotic regimes, supplies heat-root dynamics and effective source estimates. [Rodgers–Tao][rt], Sections 4 and 7–8, supplies the model for retaining reference, linear and exterior terms before estimating. Its hypothetical negative all-real interval is not an unconditional input here.

[old-overview]: 01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRAM_20261023.md
[progress]: ../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[notes]: ../notes/README.md
[n3]: ../notes/03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md
[n5]: ../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[n6]: ../notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md
[pair]: ../../11_late_heat_caps_and_charge_transport/notes/06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[review]: ../reviews/03_ANALYTICAL_SPECTRAL_CONTOUR_PROGRAM_REVIEW_20261023.md
[poly]: https://arxiv.org/html/1904.12438
[rt]: https://arxiv.org/html/1801.05914
