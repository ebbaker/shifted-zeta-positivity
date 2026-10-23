# Exact low-value Hodge counts and quantitative logarithmic regularization

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Status: **proved in-note; an explicit corollary and quantitative interface for established RHE area/Green identities**, not a literature novelty claim or a theta exclusion.

The user suggested that a topology counting simple zeros could be useful in the reciprocal Hodge setting. There is a particularly direct realization: the derivative-weighted Hodge energy restricted to sufficiently small values of the field is exactly a constant times the complete zero count. Unlike a simplicity detector, it counts every multiplicity and remains compatible with collisions. The price of extracting the integer is an acquired boundary amplitude and increasing sensitivity as the value cutoff shrinks.

Read the [result index][results], [avoid index][avoid], [collision controls][controls] and patterns [01][a01], [02][a02], [07][a07], [12][a12]. The topology and source-specific estimates remain distinct. The current RHE endpoint is [Note 15][rhe15], whose signed fixed-window trace is already certified positive; its former unacquired potential must not be reopened as though still missing.

## 1. Exact low-value energy count

Let f be holomorphic on a neighborhood of the closure of a bounded, finitely connected, piecewise C¹ planar domain Ω. Orient every boundary component positively relative to Ω. Assume

\[
b=\inf_{\partial\Omega}|f|>0,
\qquad N=\sum_{a\in\Omega:f(a)=0}\operatorname{ord}_a f.
\]

For any 0<ε<b, define

\[
W_{<\varepsilon}(f;\Omega)
=2\int_{\Omega\cap\{|f|<\varepsilon\}}
       \frac{|f'|^2}{|f|}\,dA.
\]

Then, without a simplicity or separation assumption,

\[
\boxed{W_{<\varepsilon}(f;\Omega)=4\pi\varepsilon N.} \tag{1}
\]

**Proof.** For each |w|<b, the boundary homotopy f−sw, 0≤s≤1, never vanishes. The argument principle on all boundary components gives the same N preimages with multiplicity for f−w. The holomorphic area formula, ignoring the measure-zero critical values, therefore yields

\[
2\int_{\Omega\cap\{|f|<\varepsilon\}}\frac{|f'|^2}{|f|}\,dA
=2N\int_{|w|<\varepsilon}|w|^{-1}\,dA_w
=4\pi\varepsilon N.
\]

The integrand is locally integrable at a zero of any finite multiplicity; at f=a(z−z_0)^m+…, its radial order is r^{m−2} before the area factor. No delta mass is silently discarded. The same argument covers nonzero constants, for which both sides vanish. □

This is the exact sublevel refinement of [RHE Note 09][rhe9], which already proves W(f;Ω)≥4πbN using the same area formula. It is useful as a reusable identity, but the representation alone improves no acquired bound.

On the normalized cover w²=f the differential f' dz/w=2dw has this energy over the preimage of the low-value region; [RHE Note 08][rhe8] supplies the normalization and factor two. The differential is exact, so (1) is an area count rather than a new nonzero homology period. The original reciprocal differential dz/w has a different energy and is not being replaced without notice.

## 2. A potential with exact boundary count

Define a dimensionless radial function

\[
v_\varepsilon(r)=
\begin{cases}r/\varepsilon,&0\le r\le\varepsilon,\\
1+\log(r/\varepsilon),&r\ge\varepsilon.
\end{cases}
\]

It is C¹ at ε, globally 1/ε-Lipschitz as a function of the complex field value, and has no logarithmic singularity at zero. Distributionally,

\[
\mu_\varepsilon(f):=\frac1{2\pi}\Delta v_\varepsilon(|f|)
=\frac{|f'|^2}{2\pi\varepsilon|f|}
          \mathbf1_{\{|f|<\varepsilon\}}\,dA. \tag{2}
\]

The matching normal derivatives at |f|=ε produce no interface measure. More explicitly, v_ε(|f|) is C^{1,1} near that level, even at a critical point of f; no regular-value assumption on ε is needed. At zeros the local integral in a disk of radius r tends to zero for each fixed ε, so there is no atom there either. For ε<b, the outer normal derivative equals that of log|f| along the complete boundary. Green's formula and the Cauchy–Riemann equations give

\[
\mu_\varepsilon(f)(\Omega)
=\frac1{2\pi}\int_{\partial\Omega}\partial_n\log|f|\,ds
=\frac1{2\pi}\int_{\partial\Omega}d\arg f=N. \tag{3}
\]

As ε↓0 these positive measures converge weakly on compact subsets to the divisor measure Σm_aδ_a. Indeed on a small disjoint disk around each zero their mass is exactly m_a once the boundary margin exceeds ε, and their support contracts to the zeros. Thus diffuse locally integrable modulus energy and atomic zero counting are connected by an explicit singular limit, with the factor 1/ε retained.

For ψ∈C_c²(Ω), integration by parts gives a root-free evaluation:

\[
\int\psi\,d\mu_\varepsilon(f)
=\frac1{2\pi}\int v_\varepsilon(|f|)\Delta\psi\,dA. \tag{4}
\]

If g is also holomorphic near supp ψ and sup_suppψ |f−g|≤η, the exact source-error allowance is (with μ_ε(g)=0 when g is identically zero)

\[
\boxed{\left|\int\psi\,d\mu_\varepsilon(f)
             -\int\psi\,d\mu_\varepsilon(g)\right|
\le\frac{\eta}{2\pi\varepsilon}\|\Delta\psi\|_1.} \tag{5}
\]

The proof uses ||f|−|g||≤|f−g| and the Lipschitz constant of v. In particular the cubic disk cutoff used in RHE08 has ||Δψ||₁=32π/9, giving 16η/(9ε). Formula (5) controls a weighted count, not automatically the unweighted N: to make ψ equal one on the entire low-value region and zero near the boundary, its support and a zero-free collar must also be paid. Green boundary terms are necessary if ψ is not compactly supported. No gain over an equally informed direct argument-principle calculation is claimed.

## 3. Smooth logarithmic alternative and all boundary costs

For comparison set u_ε(f)=½log(|f|²+ε²). Then

\[
\widetilde\mu_\varepsilon(f)
=\frac1{2\pi}\Delta u_\varepsilon(f)
=\frac{\varepsilon^2|f'|^2}{\pi(|f|^2+\varepsilon^2)^2}\,dA.
\]

Unlike (2), this kernel has an infinite target-space tail. Its exact finite-domain formula is

\[
\widetilde\mu_\varepsilon(f)(\Omega)
=\frac1{2\pi}\int_{\partial\Omega}
   \frac{|f|^2}{|f|^2+\varepsilon^2}\,d\arg f.
\]

Consequently, with V_∂=(2π)⁻¹∫∂Ω|darg f|,

\[
\boxed{|N-\widetilde\mu_\varepsilon(f)(\Omega)|
\le\frac{\varepsilon^2}{b^2+\varepsilon^2}V_\partial,\qquad
V_\partial\le\frac{\operatorname{length}(\partial\Omega)
                       \sup_{\partial\Omega}|f'|}{2\pi b}.} \tag{6}
\]

There is no sign assertion for the difference on an arbitrary domain because darg f need not be pointwise positive on its boundary. The source-error version of (5) has coefficient η/(4πε), since r/(r²+ε²)≤1/(2ε). Thus the smooth kernel improves that Lipschitz constant by two while requiring the boundary bias (6). Both formulations converge to the same divisor measure.

The derivative-weighted full energy supplies only the scale-dependent estimate

\[
\widetilde\mu_\varepsilon(f)(\Omega)
\le\frac{9}{32\sqrt3\pi\varepsilon}W(f;\Omega). \tag{7}
\]

Indeed the maximum of r/(r²+ε²)² is 9/(16√3 ε³). The divergence of the allowance as ε↓0 is real information, not a removable normalization. The stronger count bound with a paid b is already W≥4πbN from RHE09.

## 4. Heat transport: two distinct conserved or sourced quantities

Suppose f(t,z) is smooth in real t, holomorphic in z, and nonzero on [t₀,T]×∂Ω. Its common boundary minimum b_* is positive by compactness. Choosing ε<b_* gives

\[
\frac{W_{<\varepsilon}(f(t);\Omega)}{4\pi\varepsilon}
=N_\mathbb C(t)=N_\mathbb C(t_0) \quad(t_0\le t\le T). \tag{8}
\]

This needs no heat equation. Holomorphic collisions preserve the complex count with multiplicity. Persistent zeros cancel between the two caps, but so do the complex precursors of newly real zeros. Therefore (8) has no positive interior collision-source term.

For the smooth regularization the exact dynamical identity is

\[
\partial_t\widetilde\mu_\varepsilon
=\frac1{2\pi}\Delta\left(
\frac{\operatorname{Re}(\bar f f_t)}{|f|^2+\varepsilon^2}\right).
\tag{9}
\]

In the actual heat convention f_t=−f_zz this retains the complete numerator −Re(\bar f f_zz). It gives a boundary flux after integration; it has no automatic monotonicity sign.

The separate [real-time jet balance][transport] counts real-zero births by the local index floor(m/2), and the complex discriminant/Chern–Hopf balance counts events by binom(m,2). Those are the appropriate sourced balances. Neither is the conserved divisor count (8). In particular if a multiple zero is on the initial cap, its multiplicity is already counted there; an event link or a boundary indentation must be retained to assign an interior event contribution.

## 5. An actual canonical-theta corollary using the acquired RHE data

[RHE Note 04][rhe4] already certifies, without RH, that H_0 has exactly two zeros in Ω={|z−35|<8} and a full boundary floor greater than 6.6759×10⁻⁷. These are inherited interval-certified inputs; the present work does not rerun that acquisition. Formula (1) immediately gives the exact canonical identity

\[
\boxed{W_{<\varepsilon}(H_0;|z-35|<8)=8\pi\varepsilon,
\qquad 0<\varepsilon\le 6\times10^{-7}.} \tag{10}
\]

For example ε=10⁻⁷ gives exactly 8π×10⁻⁷. This evaluates a different, low-value derivative-weighted energy from the full reciprocal energy in RHE04; the latter's large numerical interval cannot be replaced by (10). The count and boundary floor, not a new root computation, prove this corollary. It is useful consistency and transfer information, not an independent proof of the already certified count or simplicity.

The same contract has a complete-source heat continuation. Put

\[
M_2=\int_0^\infty u^2 e^{u^2+8u}\Phi(u)\,du,
\qquad h=\min\{1,3\times10^{-7}/M_2\}.
\]

This finite positive moment uses the unchanged canonical source. For |τ|≤h on the same spatial circle, |H(τ,z)−H(0,z)|≤h M_2≤3×10⁻⁷ by integrating H_τ along the time segment. Hence the boundary floor remains greater than 3.6759×10⁻⁷, the complex count is two, and W_<ε=8πε throughout that closed complex-time disk for 0<ε≤3×10⁻⁷. No favorable size for h is claimed without evaluating M_2; this is an explicit source-defined positive continuation disk, not an effective large-time theorem.

## 6. Controls and the actual RHE opportunity

For f=az^m on a radius-R disk, b=|a|R^m and every ε<b gives W_<ε=4πmε. This verifies the constants at arbitrary multiplicity. For the heat solution f(t,z)=z²−2t on |z|<R and −T≤t≤T with 2T<R², the complex count is two on every cap. Across t=0 the real count grows from zero to two. The low-value Hodge formula stays exactly two, the real index is one and the complex event charge is one. For higher m these last two weights differ. These models fail the unchanged canonical theta source; they refute any inference using only the generic identities, not a future source-specific estimate.

RHE09's smooth Gaussian cosine controls have arbitrarily many simple zeros with arbitrarily small absolute W when amplitude is allowed to shrink. Their boundary margin shrinks too, exactly as (1) and W≥4πbN require. More generally H↦cH leaves every root distance unchanged but sends W↦|c|W and reciprocal energy E↦|c|⁻¹E. For the normalized theta field c is fixed, so a valid bound must acquire its amplitude rather than quotient it out. The remaining Euler-factor, weighted-square, finite-prime, reflection-completed and positive-primitive controls in [the control register][controls] all obey these generic holomorphic identities; their listed arithmetic/source failures remain the distinguishing missing premises.

The viable RHE connection is therefore exact counting with a boundary amplitude, or a coupled signed trace retaining the physical jet denominator. It is not that simple late zeros make either Hodge energy or cap integral vanish. [RHE15][rhe15] has completed the potential and trace on its fixed window and proved the trace positive, with a tighter direct comparator. This note does not reopen that stopped negative-witness target, does not acquire a new theta window, and does not claim an asymptotic energy or exclusion advantage. It supplies a reusable exact count, explicit regularization costs, and the complete heat transport formula for a future genuinely different consumer.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[rhe8]: ../../09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md
[rhe9]: ../../09_reciprocal_hodge_energy/notes/09_SIGNED_LAGUERRE_TRANSFER_AND_COUNT_BOUND_20261022.md
[rhe15]: ../../09_reciprocal_hodge_energy/notes/15_SIGNED_CANONICAL_POTENTIAL_AND_COMPLETED_TRACE_20261022.md
[transport]: 05_ZERO_COUNTS_REAL_BIRTHS_AND_RELATIVE_TOPOLOGY_20261022.md

[rhe4]: ../../09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md
