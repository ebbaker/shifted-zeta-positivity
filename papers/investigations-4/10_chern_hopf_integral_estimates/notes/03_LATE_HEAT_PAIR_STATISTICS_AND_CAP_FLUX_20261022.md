# Late heat pair statistics and complete cap flux

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Root verification and delegated same-model
analytic checks; no independent specialist review.

**Classification:** assessment of a proposed large-real-heat-time boundary
estimate, with an exact cap control and a finite-cluster interaction
identity. The complete-charge exclusion condition is a conditional target,
not a new theta estimate or a weaker simplicity theorem. No CHB task or
parent exclusion status changes.

The proposed limit is **real heat time T tending to positive infinity**:
prove a late-time zero-statistics theorem, use it to estimate the distant
cap, and combine the cap with the connecting boundary to constrain a
possible time-zero event. It does not assume PCC at time zero. A theorem
of this kind could be useful; root statistics must first be connected to
the full, unnormalized three-form flux.

Read the [result index][results] and [avoid index][avoid], particularly
[heat geometry][geometry], [collision controls][controls],
[target classification][a01], [control premises][a02] and [scope][a07].
The inherited analytic setting and mass normalization are in
[local Note 01][n1].

**Dedicated continuation, 22 October 2026:** new execution now belongs to
[home 11](../../11_late_heat_caps_and_charge_transport/README.md) and its
sole LHCT register. This founding assessment retains its original path,
mathematical scope and provenance.

## 1 The limit and the cap

Write tau=t+is, z=x+iy, G=(H,H_z), E=|G|^2 and

\[
 \mathcal A=\frac{\operatorname{Im}(G^*dG)}{E},\qquad
 \mathcal C=\frac{\mathcal A\wedge d\mathcal A}{4\pi^2}.
\]

A physical late cap is the three-dimensional set

\[
 M_T=\{t=T\}\times[-Y,Y]_s\times\Omega_z,\qquad
 I_T=\int_{M_T}\mathcal C.
\]

It includes an imaginary-time direction. Real root locations at t=T do
not, by themselves, specify this phase and spatial jet flux.

The actual inherited [late-time theorem][saddle] proves, for each fixed
finite collection of positive root ranks,

\[
 L_Tx_j(T)\longrightarrow(j-\tfrac12)\pi,\qquad
 L_T(x_{j+1}(T)-x_j(T))\longrightarrow\pi,
 \qquad L_T\sim\tfrac14\log T.
\]

This is a local cosine or clock limit. It is not a growing-population
sine-kernel theorem, and it has no stated uniformity in growing ranks or
event heights. The [large-time reconstruction analysis][n12] explicitly
retains compatibility with an endpoint double.

Montgomery's usual PCC instead concerns the limit of large zero height.
Its implication is density-one simplicity, rather than simplicity of every
zero; see [Montgomery, printed page 184][montgomery] and
[Goldston et al., Theorem 1][glss]. This distinction clarifies terminology
but does not settle the proposed late-heat-time cap estimate.

## 2 An exact nonzero cap with regular root statistics

Consider the heat field

\[
 H(\tau,z)=e^\tau\cos z,\qquad H_\tau=-H_{zz}.
\]

Its zeros are real, simple and exactly equally spaced at every real heat
time. Since

\[
 G=e^\tau(\cos z,-\sin z),\quad
 E=e^{2t}\cosh(2y),
\]

direct substitution gives

\[
 \mathcal A=ds-\tanh(2y)\,dx,\qquad
 d\mathcal A=2\operatorname{sech}^2(2y)\,dx\wedge dy,
\]
\[
 \boxed{\mathcal C=
 \frac{\operatorname{sech}^2(2y)}{2\pi^2}
       ds\wedge dx\wedge dy.}
\]

On the rectangular cap with s in [-Y,Y] and
Omega=[-X,X]+i[-B,B], in the positive late-face orientation,

\[
 \boxed{I_T=\frac{2XY\tanh(2B)}{\pi^2}>0.}
\]

The value is independent of T. Each connecting-side pullback vanishes
because the displayed three-form needs all three ds, dx and dy
directions. The early and late cap integrals are equal, and their oriented
difference is zero, consistent with the absence of any joint zero of
(H,H_z).

Thus even perfect late-time separation and vanishing connecting sides do
not imply that an individual cap integral vanishes. The common
imaginary-time phase survives normalization. This is an exact even,
positive-atomic-source heat control, not the canonical theta field and not
a sine-kernel PCC counterexample. It screens only the generic inference
from simple or clock-like roots to zero cap flux.

## 3 A bridge from root pairs to discriminant evolution

For a proper finite cluster at a regular time, write

\[
 H(\tau,z)=U(\tau,z)\prod_{i=1}^m(z-z_i(\tau)),\quad
 b_i=\frac{U_z}{U}(\tau,z_i),\quad
 \Delta=\prod_{i<j}(z_i-z_j)^2.
\]

The unit U is nonvanishing on the cluster domain. Differentiating a root
and applying H_tau=-H_zz gives

\[
 z_i'=2\sum_{j\ne i}\frac1{z_i-z_j}+2b_i.
\]

Let S_i=sum_{j ne i}(z_i-z_j)^(-1). Every triple of distinct roots
cancels in sum_i S_i^2, leaving
sum_i S_i^2=2 sum_{i<j}(z_i-z_j)^(-2). Differentiating log Delta therefore
proves

\[
 \boxed{\frac{\Delta'}{\Delta}
 =8\sum_{i<j}\frac1{(z_i-z_j)^2}
  +4\sum_{i<j}\frac{b_i-b_j}{z_i-z_j}.}
\]

A pair-statistics theorem could constrain the first term, but must control
its unbounded inverse-square weight, the physical gap scale and the
exterior-unit term. Weak convergence of pair measures alone does not give
inverse-square uniform integrability: exceptional tiny gaps can have
vanishing statistical weight but dominate that moment. For normalized gap
measures mu_T, a relevant additional small-gap condition is

\[
 \lim_{\eta\downarrow0}\sup_{T\ge T_0}
 \int_{0<|v|<\eta}|v|^{-2}\,d\mu_T(v)=0,
\]

with the applicable population normalization, outer tails and scale
specified. No such new theta estimate is proved here. On the real slice,
the identity gives the evolution of log|Delta|; complex winding also needs
control away from that real slice. This finite-cluster identity is not an
unregularized global sum over every theta zero.

## 4 The complete flux required for exclusion

The inherited [transport identity][n18] is

\[
 \boxed{I_T-I_{-\varepsilon}+I_{\rm sides}
       =Q_W=\sum_{p\in W}\binom{m_p}{2}.}
\]

All imaginary-time faces and the physical spatial wall belong to the side
term. The [complete-boundary assembly][full] states that the spatial wall
generally has nonzero flux; cancellation of selected chart terms is not
its separate vanishing. The event sum cannot be dropped when transporting
the cap through a hypothetical collision.

A candidate endpoint event must be interior: use an early cap at
-epsilon, or retain its small linking three-sphere. A boundary through the
candidate joint zero does not define the normalized charge.

An independently proved complete bound

\[
 |I_T-I_{-\varepsilon}+I_{\rm sides}|<1
\]

on an admissible window would force its nonnegative integer charge to
zero. This is a sufficient complete-window target and can exclude more
than endpoint events if the window contains other complex-time events.
It is not counted as an analytic advance. With a fixed early cap, late-cap vanishing and side
vanishing alone give lim_{T to infinity} Q_{W_T}=-I_{-epsilon},
not a zero charge.
A late reference profile can instead be retained with its explicit cap
flux and a source-derived signed remainder.

A separate expanding-contour control also shows why pointwise decay is
insufficient. This example expands a complex-time contour and its spatial
window, rather than taking the proposed real-time cap limit:
H=z^2-2tau has Delta=8tau and

\[
 \frac{\Delta'}{\Delta}=\frac1\tau,\qquad
 \frac1{2\pi i}\oint_{|\tau|=R}\frac{d\tau}{\tau}=1.
\]

The contour length compensates for its decaying integrand. With a spatial
radius exceeding sqrt(2R), the same double remains inside every window.
This polynomial heat control lacks canonical theta arithmetic.

## 5 Scope and the next analytic question

The inherited [collision-control register][controls] retains its separate
preservation lists. Euler-factor controls change the arithmetic;
weighted-square and finite-prime controls fail the specified full
reflection or unchanged coefficients; reflected super-Gaussian and
positive-primitive controls lack the canonical integer-square expansion;
close RH-conditional endpoint controls fail ordinary Dirichlet-series
arithmetic. The generic degree and transport identities apply whenever
their local hypotheses hold. None of these controls is assigned a new
large-heat PCC theorem or identical canonical late-cap data.

The useful unresolved question is whether the actual late theta profile,
possibly with a controlled pair-statistics remainder, gives a sharper
estimate for the full cap and its connectors relative to an explicit
reference. It must retain imaginary-time phase, exterior-root influence,
normalization, geometry and any initial or linking cap. The present
assessment establishes no theta-specific flux gain and does not rule out
such an estimate.

## 6 Explicit bounds with moving zero sides

Follow-up, 22 October 2026. Prepared for Edward Baker with substantial
LLM assistance; recorded gpt-6.1-sol, effort ultra. These are elementary
conditional consequences of the inherited charge law, with root and
same-model delegated checks. They do not supply the asymptotic theta cap
bound or change the classification above.

If an admissible complete enclosing three-boundary decomposes as
M_T=C_T union S_T, with every closing piece included, and the side flux
vanishes, then

\[
 Q_T=I_{C_T}\in\mathbb Z_{\ge0}.
\]

A source-derived upper bound I_{C_T}<1 therefore gives Q_T=0. An
unnormalized limit I_{C_T}->0 is sufficient; a bound strictly below one
at a finite T is already enough. This directly implements the proposed
cap method when the complete-boundary geometry really has that form.

For the usual early-to-late tube, the closing piece includes an early
cap. With forward-oriented cap fluxes, the exact identity is instead

\[
 Q_T=I_T-I_-+S_T.
\]

If I_T lies in [a_T,b_T], I_- lies in [a_-,b_-], and |S_T|<=s_T, then

\[
 \boxed{Q_T\in[a_T-b_--s_T,\ b_T-a_-+s_T]
                 \cap\mathbb Z_{\ge0}.}
\]

In particular b_T-a_-+s_T<1 forces zero charge. A known nonzero late
baseline is usable: if |I_T-c|<=epsilon_T and |I_--c|<=epsilon_-, then
Q_T<=epsilon_T+epsilon_-+s_T. Individual cap positivity is not assumed.
Only a late upper bound and the vanished sides leave the early term to
be bounded. All windows must have a regular complete boundary and retain
the event whose exclusion is sought.

There is also a linking-sphere formulation. Under a hypothetical
ordinary double, a small regular linking three-sphere has flux one.
If a swept event-free region in the complement connects that sphere to
a distant cap and all connecting faces, Stokes gives
1=I_far+I_connectors. A proved upper bound below one on the right is a
contradiction. This requires the full far boundary and all connectors;
no event may be lost across the swept boundary. A collision on a proposed
initial boundary must be replaced by this regular linking construction
or placed in the interior using a negative initial cap.

The [projective side lemma][projective] gives a genuine vanishing-side
construction. On H_z!=0 put q=H/H_z. A regular three-face |q|=epsilon>0
maps projectively into one fixed circle, so the pulled-back curvature
vanishes and hence its C integral is zero. This can form a tube around
simple zero branches. By contrast, H=0 itself has real dimension two,
and an arbitrary spatial tube following z_j(tau) need not have zero
projective curvature. Following the roots alone is not the needed
rank condition.

At a double, both H and H_z vanish and the q chart fails. Complementary
charts, joining faces or a linking cap must be retained. The exact
[projective shell][projective] has side zero and oriented cap values
+kappa and -kappa; its inner cap retains -kappa as its radius tends to
zero. Completing the angular sectors restores the full linking charge
one. Thus exact side cancellation is useful, but it does not justify
discarding the closure at the candidate event. This is a generic local
control; the canonical arithmetic and quantitative cap estimate remain
the substantive theta inputs.

[projective]: ../../notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[n1]: 01_ESTABLISHED_MASS_TRACE_AND_AMPLITUDE_RESULTS_20261022.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[n12]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[n18]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[full]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[montgomery]: https://websites.umich.edu/~hlm/paircor1.pdf
[glss]: https://arxiv.org/html/2503.15449v4
