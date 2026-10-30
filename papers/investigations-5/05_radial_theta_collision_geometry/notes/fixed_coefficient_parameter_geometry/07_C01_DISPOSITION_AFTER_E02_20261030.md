# FCG-B03: C01 inactive after the assessed Poisson-budget test

**Routing clarification, 30 October 2026:** [Note09 — FCG-B03 R2 brainstorm](09_CONTINUATION_FCG_B03_R2_BRAINSTORM_20261030.md) supersedes this note's requirement that new signed information already be available before conceptual work begins. Discovering that information is now the task. The author-requested next brainstorm is ready, not started; the previous mathematical findings and their scoped disposition remain unchanged. This dated record is retained below. Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6-astra / max**, same chat0043.

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **max**, Investigation05 **chat0043**, *Compare FCG-B01 collision signatures*. B01 used xhigh; B02 and this B03 turn use max.

**Disposition: make FCG-C01 R1 inactive within the tested source-mechanism scope.** E02 R1 accepted B02's six obligations without correction. One concrete repair considered here—summing each complete dual Poisson series first—restores absolute integrability after regrouping, but supplies no signed inequality for the collision consumer. C01's collision law remains available; its theta restriction remains unproved. This is a research disposition, not a theorem against all signed C01 methods or an investigation closeout.

The predeclared [B03 contract][handoff] permits one disposition and at most one existing alternative. Only C02 is reconsidered below; C03 is not reopened. No execution packet is justified by this return. [Progress06][progress] owns live status; [the continuation][next] records the reopening and model-change boundary.

## 1. Accepted inputs and the decision standard

Keep the complete theta source, literal cosine, original drift, unit preparation, C01 R1, c=1 and K*=[1/8,3/8]×[4,45]. For fixed finite C≥0 the consumer is

\[
 F_s=D_1+C E_1
 =2\int_{\mathcal C}e^{2T\Omega}B_s\Phi(u)\Phi(v)\Psi_C\,dz\,dw,
 \quad u=z+w,\quad v=z-w,\quad\mathcal C=\{z\ge|w|\}.
\]

Here Ω=z²+w² and Ψ_C is [B02's exact consumer][b02]. The [E02 assessment][review] accepts the positive-window localization, infinite positive part of the undamped zero mode, endpoint rate ε log Aε→T², and exact loss from paying the exterior absolutely. The rate is established at B₀ and Q(1), not at every intermediate auxiliary time. The negative late-time lower bound for theta is conditional on a hypothetical double event. Fixed-window certificates, signed regrouping and correlated remainders are not universally excluded.

The limiting comparator remains

\[
 F_\infty=Q(1)(L+C E_J),\qquad
 L=H_A^2-HH_{AA},\qquad E_J=H^2+H_A^2.
\]

At an interior nondegenerate double, its stationary predecessor has L/E_J=−1/(T₀−T)+O(1). That is the derived collision signature, not a theta estimate. Under [avoid01][a01], the requested finite-coefficient inequality is a reformulation in this declared collision class until additional source information pays it. Choosing C from an assumed positive minimum of E_J would assume away the difficulty. Varying the finite spatial coefficient changes the positive factor Q(c) at the stationary endpoint; it does not change that endpoint's sign question. No finite-time impossibility follows from this observation.

## 2. A concrete regrouping repairs assembly, not the signed estimate

This is the inverse of [Note38's exact Poisson transformation][old38], worked out here to test a specific proposed repair. Its derivation has same-assistant checking only; **it was not among E02's assessed claims**. It neither needs nor asserts a new theta acquisition.

Retain B02's notation d=2cosh(4w), τ=tanh(4w) and a_mn. Put

\[
 y_+=e^{4u},\quad y_-=e^{4v},\quad S=y_++y_-=e^{4z}d,
 \qquad\alpha=y_+/S=(1+\tau)/2.
\]

Since (−1)^{mn}cos(πmnτ)=Re exp(2πinαm), the Gaussian Poisson identity used in Note38, in reverse, gives for every fixed m

\[
 R_m:=\sum_{n\in\mathbb Z}a_{mn}
 =e^{2z}\sum_{\ell\in\mathbb Z}
 \exp[-\pi\{y_+(m-\ell)^2+y_-\ell^2\}].                 \tag{1}
\]

Indeed, summing exp(−πn²/S)exp(2πinαm) produces
√S Σℓ exp[−πS(ℓ−αm)²]. The prefactor d^(−1/2)√S equals e^(2z), and completing the square yields (1). Thus this particular complete resummation returns to the original two square indices, grouped by their sum m.

Write p_j(x)=exp[x−πj²e^(4x)] and q_j=(p_j''−p_j)/16. Then q₀=0, and for j≠0, x≥0,

\[
 q_j(x)=\bigl(a_j(x)^2-\tfrac32a_j(x)\bigr)p_j(x)>0,
 \qquad a_j(x)=\pi j^2e^{4x}\ge\pi>3/2.                \tag{2}
\]

All differentiated series converge normally on compact coordinate sets. With 𝒟=16(∂u²−1)(∂v²−1), equation (1) therefore gives

\[
 \mathcal D R_m=4096\sum_{\ell\in\mathbb Z}q_{m-\ell}(u)q_\ell(v)\ge0,
 \qquad \sum_m\mathcal D R_m=4096\Phi(u)\Phi(v).        \tag{3}
\]

This also supplies a complete global domination argument **after** each n-series has been summed. Since 0≤B_s≤M, |Ψ_C|≤(1+C)Ω+C, and the complete theta moments are finite,

\[
 \frac2{4096}\sum_m\int_{\mathcal C}
 e^{2T\Omega}B_s\,|\Psi_C\mathcal D R_m|\,dz\,dw
 =2\int_{\mathcal C}e^{2T\Omega}B_s\Phi(u)\Phi(v)|\Psi_C|\,dz\,dw
 <\infty.                                             \tag{4}
\]

The upper bound is uniform in s≥0 and p∈K* for fixed C. Tonelli applies to the nonnegative grouped densities in (3), followed by domination of the signed consumer. A quartic window can consequently be removed at this grouped level. This does **not** justify integrating the individual a_mn without the window; it retains their infinite cancellation before integration. In particular, the accepted exponential cost of the individual-mode absolute budget is not an obstruction to (4).

The repair is useful but does not provide the missing inequality. It restores exactly the original source product and its complete-source absolute budget. The signed factor remains unchanged. At the interior point u=2π/A, v=π/A it is

\[
 \Psi_C=-\tfrac12(u^2+v^2)-C<0,
\]

whereas at u=v=z>0 it equals z²+C(cos²Az+z²sin²Az)>0. The grouped source densities in (3) are strictly positive at both kinds of point. Hence their positivity alone cannot imply pointwise positivity of the consumer. This does not decide the sign of any integrated group. No estimate of those integrated signs or their compensations has been obtained.

Full resummation avoids a separate cutoff exterior by retaining all of it. If one reintroduces χ_ε and pays the exterior absolutely, the unchanged identity M−Eabs=F−Δ, Δ=2∫(1−χ_ε)Ψ₊dμ_s, from B02 applies again. Thus neither the exact all-source assembly nor a new cutoff by itself supplies the required signed comparison. A different use of the grouping remains possible, but needs a new inequality, not just (1).

## 3. Controls and the one alternative

The accepted controls continue to screen any argument resting only on positive source densities, complete moments, preparation and regular fixed flow. Their event marks lie in K*:

| Control | Actual event and failed theta premise |
| --- | --- |
| Gaussian-polynomial source (64u⁴+6)e^(−17u²/4) | Double at (T,A)=(1/4,2√6), with H_AA≠0; finite prepared moments for T<17/4. It fails theta's full arithmetic source relation. |
| Three positive square weights | Certified double at T=1/4, A∈(44.1303,44.1304); fails unit coefficients/full reflection. This event is not a finite all-real threshold. |

Neither control is assigned theta's parity–Poisson identity. The generic positivity-and-moment inference is what they reject, not a yet-unproved arithmetic inequality using (1). Their existing certificates were not replayed. The broader [control register][controls] retains its separate hypotheses and scopes.

**Only C02 R1 was reconsidered as an alternative; retain inactive.** Its numerator N=||∂T W||²+||∂A W||² tends at a double to Q(c)(2b²+H_AT²)>0, b=H_AA≠0, while E→0. The full primitive identity gives an exact source representation and absolute derivative bounds; it has supplied no reverse estimate N≤C E. The positive-primitive controls in the register also show why primitive positivity alone cannot pay that estimate. No new primitive mechanism is proposed here. C03 stays inactive without another comparison.

## 4. Disposition and what would change it

The known absolute-budget route is stopped in its accepted scope. The concrete infinite regrouping above fixes integration but leaves the required signed estimate unpaid. **C01 R1 is therefore inactive pending named new signed information; its definition is not revised.** C02 and C03 remain inactive. The separate CTF integrated-feedback question keeps its existing open status and original-alpha obligations; this return does not activate it.

Reopening requires a source-derived signed estimate specifying the correlation retained, the complete exterior payment or justified all-source assembly, and constants independent of an assumed nonzero physical jet. It must explain its advantage over the direct limiting comparator and identify which extra premise the colliding controls fail. A signed-margin assertion, a smaller window or greater precision is not that input.

No E01 packet, fresh numerical campaign, coverage extension or manuscript integration is warranted now. The assessed B02 finding is recorded proportionately in the existing result/avoid indexes and milestone history. The new regrouping is not promoted there as an independently assessed result. See the [result index][results], [theta-identity cluster][identities] and [avoid index][avoid], particularly [separate absolute bounds][a12] and [scoped exclusions][a07]. No theta exclusion, RH consequence or broader impossibility is established.

[handoff]: 06_CONTINUATION_FCG_B03_AFTER_E02_20261030.md
[b02]: 03_POISSON_LOCALIZATION_AND_RELATIVE_LOSS_B02_20261030.md
[review]: ../../reviews/fixed_coefficient_parameter_geometry/01_FCG_E02_R1_POISSON_LOCALIZATION_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[next]: 08_CONTINUATION_AFTER_FCG_B03_20261030.md
[old38]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md
[results]: ../../../../../result-summaries/README.md
[identities]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
