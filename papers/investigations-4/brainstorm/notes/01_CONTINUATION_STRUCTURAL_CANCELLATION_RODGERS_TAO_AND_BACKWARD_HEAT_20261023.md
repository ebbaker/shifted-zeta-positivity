# Continuation on structural cancellation and backward heat contours

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. This is a research continuation and brainstorm, with elementary explanatory calculations and same-assistant checking; it has not received independent specialist review.

The next research question is whether a complete topological boundary formula can be reorganized into a remainder that is easier to estimate than the original integral. Rodgers–Tao provides an instructive precedent: remove the reference contribution and its first variation, retain a quantity that detects departures from equilibrium, and prove enough control of its evolution and localization to obtain a theorem. Our current contour work supplies exact cancellation identities, but has not supplied an analogous quantitative mechanism or a competitive zero-free-region estimate.

The immediate priority is a coupled estimate on one declared height window, including every boundary contribution. Further polishing of either manuscript should wait for a mathematical or demonstrable computational advantage. Elegant bounds and a transparent proof matter more to the author than squeezing constants. An informative bound on creation events, including a bound relative to a growing zero population, remains a worthwhile intermediate outcome.

## What the next chat should read

Start with the repository [result index](../../../../result-summaries/README.md) and [avoid index](../../../../avoid/README.md), especially [local heat geometry and topology](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [reformulations](../../../../avoid/01_restating_the_target.md), [separate bounds on cancelling terms](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [scoped negative results](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The two essential local sources are:

1. [Review 05 on usefulness](../../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md): the complete late boundary cancels exactly; no comparative gain has been established.
2. [Note 13 on height dependent backward heat contours](../../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md): the signed curved-collar identity, its slope contribution, the microscopic time scale, and its remaining analytic task.

The maintained manuscripts are [Topological Zero Transport and the Phase of the Discriminant](../../manuscript/topological_zero_transport/README.md), the focused paper, and [Zero Counts, Heat Transport, and Localized Hodge Energy](../../manuscript/zero_count_heat_transport/README.md), the broader catalogue. Preserve their separate roles. This continuation does not revise either manuscript or create another snapshot.

The original [Continuation 08](../../notes/08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md) led to [Note 09 on sharp divisor stability](../../notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) and [Note 10 on growing clock windows](../../notes/10_GROWING_CLOCK_WINDOWS_20261022.md). Those tasks should not be restarted as if still only proposals. The present question arose after the later cap estimates and the focused manuscript exposed the need for a stronger cancellation mechanism.

## The author's research objective

The author initially sought a memorable equation relating an integral at time zero to later zero creation, with the other faces controlled by moving boundaries and a Vandermonde determinant. The subsequent discussion sharpened the criterion for success: the formula should make a difficult estimate genuinely more tractable, ideally leading to a better zero-free region. A new representation, a topological interpretation, or a catalogue of separately bounded terms does not establish that advantage.

The physical intuition is that large contributions which nearly cancel may be constrained by a conservation law, symmetry, equilibrium condition, or evolution identity. The desired mechanism should preserve that constraint before inequalities are applied. Topology can explain why a complete integral stays fixed while local contributions fluctuate. Heat evolution might provide a better representative or an energy controlling the fluctuations. Neither observation alone supplies a bound on the remaining signed quantity.

The latest concrete proposal is **very small negative real heat time, with its magnitude allowed to shrink with spatial height**. Literal imaginary heat time gives a Schrödinger-type equation. For the convention below, reversing real time gives ordinary forward heat flow. These are different proposals and must remain distinct.

## The complete topological formula and its exact cancellation

Write

\[
H_\tau=-H_{zz},\qquad G=(H,H_z),\qquad
\tau=t+i\sigma,\quad z=x+iy.
\]

Let \(\mathcal C\) be the normalized Chern–Hopf three-form of the physical jet \(G\), as defined in the [boundary derivation](../../manuscript/topological_zero_transport/boundary.tex). For a compact domain with \(G\ne0\) on its complete boundary,

\[
Q(W)=\int_{\partial W}\mathcal C
 =\sum_{p\in W:\,G(p)=0}\binom{m_p}{2}\ge0.
\tag{1}
\]

Here \(m_p\) is the spatial zero multiplicity. This counts complex joint events with their local degrees. It is not simply the number of real pair births, although every distinct enclosed real creation event contributes at least one.

With the initial cap assigned forward integral \(I_0\), terminal cap \(I_T\), and all remaining outward faces collected in \(S_+\), the formula is

\[
\boxed{I_0=I_T+S_+-Q_+.}
\tag{2}
\]

The initial observable here is a physical three-form integral. It must not be silently replaced by the distinct real angular integral involving \(\arg(H+iH_x)\).

On regular root tubes with constant projective radius \(\rho\), the wall \(|H/H_z|=\rho\) has zero flux. For an oriented complex-time edge \(e\), their cap reduction is

\[
I(e)=\frac{k_\rho}{2\pi}\operatorname{Im}\int_e d\log\mathscr D,
\quad k_\rho=\frac{\rho^2}{1+\rho^2},\quad
\mathscr D=\prod_{j=1}^{m}H_z(\tau,z_j)
 =(-1)^{m(m-1)/2}\Delta\mathscr U,
\tag{3}
\]

where \(\Delta=\prod_{j<k}(z_k-z_j)^2\) and \(\mathscr U=\prod_jU(\tau,z_j)\) for the local factorization \(H=U\prod_j(z-z_j)\). The analytic factor retains information absent from the chosen zero configuration. Root speeds need not be small for the wall flux to vanish. Changing radius along a tube introduces additional terms.

For an event-free regular extension from \(a\) to \(T\), with the same population and radius, let \(E_{a,T}\) denote its outward imaginary-time faces. Then

\[
\boxed{I_T+E_{a,T}=I_a.}
\tag{4}
\]

Thus adding a longer late tube cannot improve the exact complete event balance by itself. Bounding its cap and closures separately can destroy an identity that is already exact. The gain sought must come from estimating the remaining quantity, or from additional propagation information.

The existing large-heat estimates control the full terminal cap per root, a smaller Vandermonde contribution, and late edge flux. They do not close the early boundary starting at zero. Moreover, the proof of the full cap estimate uses the complete product \(\mathscr D\) directly and does not require the separate Vandermonde perturbation lemma. Any claim that the determinant decomposition improves the estimate must therefore be demonstrated by a comparison. [Review 05](../../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md) gives the estimates together, including their different limiting geometries.

## What Rodgers–Tao renormalizes

The physical picture is an overdamped logarithmically repelling particle system when the zeros are real. Infinite unrenormalized interaction sums contain a large background even near regular spacing. Under the contradiction hypothesis \(\Lambda<0\), the zeros remain real on a fixed negative-time interval ending at zero. Their dynamics would force excessive local regularity at zero, incompatible with known pair-correlation information. This proves \(\Lambda\ge0\); it does not supply the opposite inequality needed for RH. [Tao's author exposition](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/) explains this strategy.

For ordered real zeros, let \(d=x_k-x_j>0\), \(a=\xi_k-\xi_j>0\), and \(u=d/a\). The classical positions \(\xi_j\) reflect the mean density; they are not one globally uniform lattice. Rodgers–Tao replace the pair energy by

\[
\boxed{\widetilde E_{jk}=a^{-2}V(u),\qquad
 V(u)=u^{-2}-1+2(u-1).}
\tag{5}
\]

Their related logarithmic remainder is \(L(u)=-\log u+u-1\). Localization, exterior interactions, and the summed linear corrections are controlled. In particular, the localized Hamiltonian initially subtracts the reference logarithm; its expression using positive \(L\)-terms includes an error. Under the contradiction hypothesis, Proposition 8.43 gives

\[
\widetilde E^{[R\log R,\,2R\log R]}(0)=o(R\log^3R).
\tag{6}
\]

Here \(R\) denotes their large height parameter, renamed to avoid confusing it with our terminal heat time. This is smallness relative to a natural scale, not absolute convergence to zero. See [Rodgers–Tao, corrected v5, §§7–9](https://arxiv.org/html/1801.05914), especially (63), (69)–(71), Lemmas 7.25, 7.28, 7.30 and Proposition 8.43. A precise global monotonicity formula with all cutoff terms erased would misstate the argument.

## Why the subtraction is a structural mechanism

The following elementary calculation explains the mechanism independently of the infinite zero system. For a twice differentiable convex function \(f\),

\[
f(u)-f(1)-f'(1)(u-1)
 =(u-1)^2\int_0^1(1-r)f''(1+r(u-1))\,dr.
\tag{7}
\]

For \(f(u)=u^{-2}\), this yields the exact factorization

\[
V(u)=\frac{(u-1)^2(2u+1)}{u^2}\ge0,
\qquad V(1+\delta)=3\delta^2+O(\delta^3).
\tag{8}
\]

The linear response is removed before estimating the remainder. A perturbation of size \(\delta\) therefore produces a quadratic cost near equilibrium. Estimating the original energy and its reference separately would generally retain errors of first order or background size. This is a relative convex energy, often called a Bregman remainder. In physics terms, it is the deformation energy after the background and first variation have been subtracted.

The subtraction does not remove the collision singularity: \(V(u)\sim u^{-2}\) as \(u\downarrow0\). It measures both small departures from regular spacing and severe compression. Nor is it uniformly quadratic for all strains: \(V(u)\sim2u\) as \(u\to\infty\). Any coercive estimate must state its strain regime.

The simplest cancellation model for the linear correction is a reference lattice \(\xi_j=aj\) and finitely supported displacements \(\eta_j\). The absolutely convergent ordered-pair sum satisfies

\[
\sum_{j\ne k}\frac{\eta_k-\eta_j}{(k-j)^3}
 =-2\sum_j\eta_j\sum_{k\ne j}\frac1{(k-j)^3}=0.
\tag{9}
\]

The inner sum vanishes by pairing opposite separations. On a finite interval it leaves endpoint terms; with varying density or weights it leaves further defects. This calculation illustrates why organizing the sum first matters. It does not justify setting those defects to zero for theta.

Three ingredients should remain separate: the algebraic subtraction; positivity or coercivity of the resulting remainder; and estimates linking that remainder to dynamics and the desired observable. An arbitrary subtraction may have the first property without either of the others. The operative physics analogy is a reference-state energy and its counterterms. A change of scale alone would not explain the cancellation.

## A direct bridge to the Vandermonde and its limitation

For two finite ordered real configurations \(x_1<\cdots<x_m\) and \(\xi_1<\cdots<\xi_m\), set \(u_{jk}=(x_k-x_j)/(\xi_k-\xi_j)>0\). Define their squared Vandermondes \(\Delta(x)\) and \(\Delta(\xi)\). Directly expanding the logarithm gives

\[
\boxed{
\mathcal R_\Delta(x\mid\xi)
 =-\frac12\log\frac{\Delta(x)}{\Delta(\xi)}
   +\sum_{j<k}(u_{jk}-1)
 =\sum_{j<k}L(u_{jk})\ge0.
}
\tag{10}
\]

This finite identity makes a possible connection concrete: a determinant has a relative logarithmic energy whose background and tangent are removed. It requires no conjecture, but by itself proves nothing special about theta. The reference must be specified independently and its errors paid.

There are three obstacles to using (10) in the physical cap:

1. **The cap uses a phase.** Equation (3) contains \(\operatorname{Im}d\log\mathscr D\), whereas (10) concerns real logarithmic magnitudes. Convexity on the positive real axis does not give complex-phase positivity. For example, with the logarithm continued near one,
   \[
   \operatorname{Re}[-\log(1+i\eta)+i\eta]
       =-\tfrac12\log(1+\eta^2)<0\quad(\eta\ne0).
   \]
   A transfer through analyticity would need a nonvanishing domain, transverse bounds, and the corresponding boundary costs.
2. **The analytic factor remains.** Replacing \(\mathscr D\) by \(\Delta\) loses \(\mathscr U\). A viable relative expression must include it, or prove why its contribution is independently controlled at the required scale.
3. **The reference also evolves.** For \(u=d/a\),
   \[
   \dot u=\frac{\dot d-u\dot a}{a},\qquad
   \frac d{dt}L(u)=(1-u^{-1})\dot u.
   \]
   Neither derivative has a fixed sign for an arbitrary reference. The real-zero assumptions, exterior forces, and population entry or exit terms must be retained.

Thus a worthwhile next question is whether a relative energy for the complete source product can control the complete cap-and-edge expression. Merely naming that expression a renormalized cap would not answer it. No such inequality is asserted here.

## The proposed shrinking backward-time collar

Let \(\epsilon(x)>0\) be \(C^1\) on a finite height interval. Consider the compact collar between \(t=-\epsilon(x)\) and \(t=0\), with a fixed base in \((\sigma,x,y)\). Give both cap integrals the forward parameter orientation, and let \(S_\epsilon\) include all other outward faces. If \(G\ne0\) on the complete boundary, [Note 13](../../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md) gives

\[
\boxed{I_0=I_\epsilon-S_\epsilon+Q_-
              \ge I_\epsilon-S_\epsilon.}
\tag{11}
\]

Negative-time events need not be excluded for this lower-bound consumer. However, exactly \(I_\epsilon-S_\epsilon=I_0-Q_-\): increasing the collar across events can weaken the lower bound. On nested event-free collars, the complete combination is constant. Smoothing can improve the tractability of an estimate, but this topological identity supplies no automatic strict gain.

Combining (2) and (11),

\[
Q_+\le I_T+S_+-(I_\epsilon-S_\epsilon).
\tag{12}
\]

The target is therefore a lower estimate for the coupled quantity \(I_\epsilon-S_\epsilon\), not a small absolute bound for one of its parts. Boundary joint zeros, including any on the time-zero cap, require explicit excisions and their charges; no simplicity assumption is hidden in (11).

Use \(h\) for height in the \(H\)-variable, twice the zeta ordinate, and

\[
\ell(h)=\tfrac14\log\frac{h}{4\pi},\qquad
\epsilon(h)=\frac{c(h)}{\ell(h)^2},\qquad h>4\pi.
\tag{13}
\]

This is a candidate microscopic scale, not a proved safe width. The mean spacing is approximately \(\pi/\ell(h)\); the Gaussian smoothing width is \(\sqrt{2c(h)}/\ell(h)\). The author's proposal permits \(c(h)\) very small or tending to zero. A fixed negative-time interval, as in the Rodgers–Tao contradiction, has duration tending to infinity in these local time units. A collar with \(c(h)\to0\) has vanishing local duration. The evolution direction also differs: their repulsive real-zero dynamics advances \(t\), while this smoothing advances reversed time \(s=-t\). Their relaxation conclusion cannot simply be imported.

The slope must be paid. With \(E=H^2+H_x^2\) and \(\mathcal L=H_x^2-HH_{xx}\), the real angular trace obeys

\[
-\frac d{dx}\arg\{H(-\epsilon(x),x)+iH_x(-\epsilon(x),x)\}
 =\left.\frac{\mathcal L+\epsilon'(x)\mathcal L_x}{E}
   \right|_{t=-\epsilon(x)}.
\tag{14}
\]

For constant \(c\), \(\epsilon'=-c/(2h\ell^3)\); variable \(c\) adds \(c'/\ell^2\). Small slope alone is insufficient near a small first jet. Equation (14) is a diagnostic one-form, not the full three-form pullback. The latter needs its own tilted-fiber and joining-face calculation.

## Heat smoothing and positive remainders

There is a simple model for the kind of evolution identity worth seeking. For the ordinary heat semigroup \(P_s\), and a real smooth function with sufficient decay,

\[
P_s(f^2)-(P_sf)^2
 =2\int_0^s P_{s-r}\big[(\partial_xP_rf)^2\big]\,dr\ge0.
\tag{15}
\]

To verify it, differentiate \(F(r)=P_{s-r}[(P_rf)^2]\). The product rule gives \(F'(r)=-2P_{s-r}[(\partial_xP_rf)^2]\), and integration gives (15). The difference of the two large terms is represented directly by a nonnegative integrand. This is an elementary illustration of structural cancellation, not a theta estimate.

The relevant sign does not follow for every quadratic observable. If \(U_s=U_{xx}\), direct differentiation gives

\[
(\partial_s-\partial_{xx})(U_x^2-UU_{xx})
 =2(U_xU_{xxx}-U_{xx}^2),
\tag{16}
\]

whose right side has no universal sign. At a nondegenerate double zero it is strictly negative. A positive variance remainder therefore cannot simply be substituted for the oscillatory jet or its phase. A proposed entropy must control the actual consumer and keep its singular denominators visible.

The actual negative-time field has the Gaussian representation

\[
H(-\epsilon,z)=\frac1{\sqrt{4\pi}}
\int_{\mathbb R}e^{-r^2/4}
 H(0,z+\sqrt\epsilon\,r)\,dr.
\tag{17}
\]

The source and interchange justification are in [Note 13](../../notes/13_HEIGHT_DEPENDENT_BACKWARD_HEAT_CONTOURS_20261023.md). Keeping this coupled averaging before taking absolute values is available to both the contour approach and its direct comparator. A height-dependent time trace is not generally holomorphic in the spatial variable; apply topology to the original spacetime domain, not an invented holomorphic trace.

## Control screen and scope

The identities above are generic within their stated hypotheses. Their compatibility with collision controls is expected. They become exclusion tools only when an additional quantitative estimate fails on the relevant event-containing control domain. The [control register](../../../../result-summaries/12_collision_controls_and_screening.md) and [premise rule](../../../../avoid/02_shape_only_arguments_and_the_controls.md) provide the detailed examples.

| Control | What survives | Premise absent from a complete canonical-theta application |
| --- | --- | --- |
| Euler-factor modifications | Heat evolution, positivity and symmetry, degree accounting; actual collision witnesses | The unchanged source and arithmetic coefficients |
| Finite weighted-square sources | Square support, positive weights, selected endpoint conditions, local heat geometry | Full reflection and the complete normalized coefficient sequence |
| Reflected and positive-primitive controls | Their stated reflection or primitive properties and generic heat/topological identities | The unchanged arithmetic square expansion |
| Finite-prime compatible controls | Any fixed selected-prime identities and the matched finite measurements in their construction | Full reflection; they do not satisfy every prime condition simultaneously |
| RH-conditional normalized endpoint controls | Their stated completion, normalization and source closeness | Ordinary Dirichlet-series arithmetic |

No new source-specific inequality in this note rejects these controls. Their failed source premises identify where distinguishing information might enter; they do not prove that a subsequently derived weak inequality distinguishes theta.

Two exact local tests are immediately useful. Reversed heat sends \(x^2-a^2\) to \(x^2-a^2+2s\), so a gap \(g=2a\) closes at \(s=g^2/8\). Mean spacing gives no uniform protection for smaller gaps. Reversed heat sends \(\cos(\ell x)\) to \(e^{-s\ell^2}\cos(\ell x)\), changing only the positive amplitude of its real first jet. Smoothing alone therefore does not improve that phase. Both examples lack the full theta source; they limit generic claims, not all source-specific estimates.

A bound \(Q\le o(N)\) for a specified growing zero population \(N\) would be a legitimate quantitative milestone. It would not imply \(Q=0\). Exclusion from integrality requires a complete upper bound strictly below one. A population limit must also pay for changing windows and entry or exit terms.

## A bounded plan for the next chat

The intended deliverable is one new applicable inequality or a precise obstruction to a declared candidate. It is not another general RH-equivalent sign criterion. Follow the [classification rule](../../../../avoid/01_restating_the_target.md) before treating a reformulation as a milestone.

1. **Choose the consumer and reference.** Fix a finite height window and explicit \(\epsilon(h)\). State whether the target is the physical cap, a real angular integral, or a bound for \(Q_+\). Specify the reference configuration or complete reference jet without defining its accuracy by an unknown collision distance.
2. **Perform exact cancellations first.** Collapse regular late tubes using (4). For the negative collar retain \(I_\epsilon-S_\epsilon\) as one object. If using a reference subtraction, expand the complete product including its analytic factor, endpoints, slope and any changing-population terms.
3. **Ask for the missing structural property.** Does the first variation cancel? Is the remainder coercive in a stated norm? Is there a signed evolution identity, or a controllable error in one? Equation (10) is a finite real model; (15) is an evolution model. Neither already controls the complex cap. Keep separate the real-to-complex transfer and the source-specific estimate.
4. **Compare under the same information.** Give the direct method the same theta source, Gaussian formula, signed correlations, analytic continuation bounds, and critical-value or discriminant reductions. The existing [scalar-source comparison](../../03_heat_transport_and_charges/notes/03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md) explains why independent absolute moment payments alone are an inadequate starting point. Compare a proved bound, required information, verification cost, or meaningful simplification of proof.
5. **Decide from the complete result.** A sharper event count, an improved threshold or region, a rigorously cheaper certificate, or an equally strong theorem under substantially simpler hypotheses justifies continuation. If a specified ansatz only transfers the original unknown sign, record that scoped failure and stop that ansatz. It does not establish that every geometric or renormalized approach must fail.

Before a novelty claim, compare the completed inequality with the primary sources under matching hypotheses. The current [literature and proof review](../../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) and [usefulness review](../../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md) are starting maps, not a conclusion that a useful new result exists or that the field is exhausted. The next Rodgers–Tao reading should focus on how the linear corrections and exterior interactions are paid, alongside the definition of the positive remainder.

## Continuation instructions and provenance

A new chat can start with the request: “Read this continuation, Review 05, and Note 13. Investigate one structural cancellation mechanism for the complete shrinking backward-time collar. Start from the reference-state subtraction in Rodgers–Tao, retain the analytic factor and every boundary cost, and compare with a direct estimate using the same information. Preserve both manuscripts until a useful inequality or a precisely scoped failure is established.”

This chat is **Continue divisor stability research**, uniquely archived as history **0010** in [Investigations 4](../../chat-histories/0010_2026-10-23T03-12-24Z_continue-divisor-stability-research.json). The continuation is saved in the brainstorm area at the author's request; this does not relocate or duplicate that history. A new chat should retain its own identity and follow [the history workflow](../../../../tools/CHAT_HISTORY.md). Saving this brainstorm does not select a new investigation series or establish a manuscript milestone.
