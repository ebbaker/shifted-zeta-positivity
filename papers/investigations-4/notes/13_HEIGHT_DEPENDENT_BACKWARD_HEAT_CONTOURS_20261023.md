# Height dependent backward heat contours

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant derivation and assessment.

**Status: exact signed collar balance and scale diagnostics, not a new zero-free estimate.** The proposed contour t=-epsilon(h), with epsilon shrinking with height, is geometrically legitimate. Negative-time events have a favorable sign when deriving a lower bound for the original cap. The analytic task is a coupled bound for the displaced cap and its complete connecting boundary.

This follows the [result index](../../../result-summaries/README.md), [collision controls](../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../avoid/README.md), and the rules on [reformulations](../../../avoid/01_restating_the_target.md) and [separate bounds](../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The comparison and utility assessment is [Review 05](../reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md). These identities specify a diagnostic, not an RH-equivalent criterion presented as a gain.

## The signed balance on a thin curved collar

Retain the physical jet G=(H,H_z), with H_tau=-H_zz, and its normalized Chern–Hopf form C from the [manuscript](../manuscript/topological_zero_transport/boundary.tex). Write tau=t+is and z=x+iy, oriented by dt wedge ds wedge dx wedge dy. Let epsilon(x)>0 be C¹ on a finite height interval [A,B]. For a compact rectangular base Omega in (s,x,y), define

\[
W_- =\{(t,s,x,y):(s,x,y)\in\Omega,
                    -\varepsilon(x)\le t\le0\}.
\tag{B1}
\]

Assume G is nonzero on the complete boundary. Let I_0 be the upper cap integral and I_epsilon the lower graph integral, both parameterized with the forward orientation ds wedge dx wedge dy. Let S_epsilon be the sum of **all other outward boundary integrals**, including imaginary-time faces, spatial faces and any exposed joining pieces. The positive holomorphic local degree gives

\[
\boxed{I_0=I_\varepsilon-S_\varepsilon+Q_-\ge
                   I_\varepsilon-S_\varepsilon,}
\qquad
Q_- =\sum_{p\in W_-:\,G(p)=0}\binom{m_p}{2}\ge0.
\tag{B2}
\]

**Proof.** The complete boundary is the upper cap, minus the forward-oriented lower graph, plus the remaining outward faces. Thus its integral is I_0-I_epsilon+S_epsilon. Degree additivity identifies this with Q_-, proving (B2). The graph need not be a complex submanifold: the map G is holomorphic on the ambient domain, which supplies the positive local degrees.

This addresses the concern about creation in negative time. A lower bound I_epsilon-S_epsilon>=L implies I_0>=L without an upper bound on Q_- and without assuming an all-real negative-time slice. If the positive-time event domain has Q_+=I_T-I_0+S_+, then

\[
Q_+\le I_T+S_+-(I_\varepsilon-S_\varepsilon).
\tag{B3}
\]

This is a one-sided consumer, not a favorable numerical estimate. Negative-time charges can still make the available lower bound weaker: exactly, I_epsilon-S_epsilon=I_0-Q_-. For a nested family of collars with fixed upper cap and regular boundaries, this combined quantity is constant between event crossings and decreases by their positive degrees when the collar grows across them. Topology cancels regular deformations; it does not give a free strict improvement from smoothing.

Q_- counts all enclosed complex joint events with their degrees; it is not merely the number of real pair births. If G vanishes on the original t=0 cap, the stated regular-boundary argument does not apply without explicit excisions and their local contributions. The formula has not silently assumed simplicity at time zero. An all-height limit also requires bounds uniform in the finite height cutoffs.

## A curved cap has a slope contribution

The lower graph has dt=-epsilon'(x) dx, which must be substituted into the full three-form. A flat-cap formula cannot simply be evaluated pointwise at t=-epsilon(x). Even inside a regular root chart, tilting time across a disk changes its fiber integral; chart existence alone does not justify the old Vandermonde formula for that disk. Uncovered graph and joining pieces also remain part of the boundary.

The real angular observable makes the same issue explicit. Set

\[
E=H^2+H_x^2,\qquad \mathcal L=H_x^2-HH_{xx}.
\]

On a real patch with E>0, direct differentiation and H_t=-H_xx give

\[
-d\arg(H+iH_x)=\frac{\mathcal L\,dx-\mathcal L_x\,dt}{E}.
\]

Consequently the lower graph carries the exact density

\[
\boxed{-\frac d{dx}\arg[H(-\varepsilon(x),x)+iH_x(-\varepsilon(x),x)]
=\left.\frac{\mathcal L+\varepsilon'(x)\mathcal L_x}{E}
  \right|_{t=-\varepsilon(x)}.}
\tag{B4}
\]

This follows from the chain rule; in particular dH(-epsilon(x),x)/dx=H_x+epsilon'H_xx. The physical partial derivative H_x must not be replaced by that derivative of the trace. Equation (B4) is a real one-form identity, distinct from the three-dimensional cap in (B2). A small epsilon' alone does not bound its correction near a small first jet.

## A first height dependent scale to examine

Use h for height in the H variable, twice the zeta ordinate, and put

\[
\ell(h)=\tfrac14\log\frac{h}{4\pi},\qquad
\varepsilon(h)=\frac{c(h)}{\ell(h)^2},\qquad h>4\pi.
\tag{B5}
\]

The classical-location density is ell(h)/pi, giving mean spacing pi/ell(h); see [Rodgers–Tao, equations (38)–(39)](https://arxiv.org/html/1801.05914). This is a density normalization, not an individual-gap lower bound. Their conditional negative-time real-zero estimates are not imported here, and no RH assumption is made for this choice of scale.

Freeze h within a local chart and rescale X=ell(h)(x-h) and s=nu/ell(h)². The reversed-time equation becomes U_nu=U_XX. Thus c is the dimensionless smoothing duration, and the Gaussian standard deviation is sqrt(2c)/ell(h). A small fixed c gives a small fraction of the mean-spacing scale. Taking c(h) to zero tests still smaller increments. For constant c,

\[
\varepsilon'(h)=-\frac{c}{2h\ell(h)^3}.
\tag{B6}
\]

For variable c, add c'(h)/ell(h)². These are exact scale calculations, not yet uniform theta estimates. The scale ell(h) here depends on spatial height and is different from the manuscript's large-real-time saddle L_T.

Two controls delimit the interpretation. For U(s,x)=x²-a²+2s, an initial gap g=2a collides at s=g²/8. Therefore a mean-spacing choice for epsilon does not guarantee survival of every smaller gap. For U(s,x)=e^(-s ell²) cos(ell x), smoothing only changes a positive scalar amplitude, so the normalized jet and its phase are unchanged at fixed s. After local rescaling, an increment with c(h) tending to zero changes a uniformly C²-bounded profile by O(c(h)); such a normalized theta bound is not assumed. Infinitesimal increments could still matter through a proved sign or monotonicity, but the sign must be acquired.

## The same-information comparison

The full source gives, for epsilon>0 and complex z,

\[
H(-\varepsilon,z)=\frac1{\sqrt{4\pi}}
\int_{\mathbb R} e^{-r^2/4}H(0,z+\sqrt\varepsilon\,r)\,dr.
\tag{B7}
\]

The Gaussian Fourier transform proves this by multiplying each source frequency by e^(-epsilon u²); superexponential source decay justifies interchange. This is the classical formula used in [Rodgers–Tao, equation (15)](https://arxiv.org/html/1801.05914). It remains valid pointwise for epsilon=epsilon(h). The variable-time trace is not generally holomorphic in z and cannot be assigned an argument-principle count without returning to the original spacetime domain.

The earlier [imaginary-spatial note](../../investigations-2/active/20_constrained_operator_squares/notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md) had a different increasing-time equation and an unsigned forcing obstacle. Literal imaginary heat time gives a Schrödinger equation; the user's clarified proposal instead uses reversed real time. The [local endpoint-window note, Section 5](../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md) already allows negative widths depending on height and local jets. The new focus here is the complete curved collar and its one-sided sign, not the logical necessity of one common negative time.

The [scalar-current pilot](../03_heat_transport_and_charges/notes/03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md), Section 3, already loses to direct estimation when both use the same absolute source moments and terminal floors. A new comparison must retain signed correlations before estimating I_epsilon-S_epsilon, and give the direct method the same Gaussian formula, source data and boundary information. An epsilon rule defined by the unknown distance to a collision would not supply an independent estimate.

The immediate test is one height window with a prescribed shrinking rule, complete cap and connecting-face costs, and a comparison at the same source accuracy. A useful outcome would be a stronger certified lower bound for I_0, a better relative event bound, or a genuine zero-free-region improvement after the additional transfer to zeta. The present identities do not yet establish any of these.

## Control screen and assessment

Heat evolution and the collar identity also hold for the repository's Euler-factor, weighted-square, reflected and positive-primitive collision controls. None is rejected by changing the contour. Their failures of the full canonical-source requirement differ: Euler-factor controls alter the source and arithmetic coefficients; finite weighted-square examples lose full reflection and the complete normalized coefficients; reflected and positive-primitive controls lack the unchanged arithmetic square expansion. The quadratic and cosine scale controls lack the complete theta source as well. This is a premise-level screen; there is no newly proved theta inequality to evaluate on event-containing domains.

The scoped positive conclusion is that negative-time event exclusion is unnecessary for the lower-bound consumer (B2). The scoped limitation is that neither smoothing nor a shrinking time width supplies the needed coupled bound. These are consequences of established degree and heat identities, with no novelty claim. Both manuscripts remain intact while this quantitative comparison is unresolved.
