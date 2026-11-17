# Assessment of the physical-time quadrature error extension

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Reviewer dispatch selected
**gpt-6.1-sol / ultra**, the same selection as for the E01 proof.
Separate backend attestation and actual recorded lead settings are
unavailable. The reviewer authored the parallel E02 note. This is a
separate internal assessment of E01 with shared inherited sources,
without independent specialist review.

**Accepted within the frozen E01 scope without mathematical correction.**
Both note hashes in the [E05 assessment request][e05] and all seven
source hashes in the [E01 execution request][e01] match. This assessment
reviews only the pinned E01 note, SHA-256
76f97cb49b1571b911e5bd3a9484a10802138ced63b1c4681bdbad79a5c999dd.
[Reviewed proof][proof] [Result index][results] [Avoid index][avoid]
[Shared-premise review pattern][shared]

## Uniform law and constants

The heat tilt stays in the normalized measure, and orthogonal
polynomial normalization cancels from the coefficient ratios and the
law \(P_N^2\,d\mu_\lambda/h_N^*\). The normalization at site zero
gives \(h_0^*=1\), so \(h_N^*=\prod_{j=1}^N\beta_j\).
The doubled-node remainder integrates against this probability law
with coefficient \((iz)^{2N}h_N^*/(2N)!\). The simplex probability
moment contributes \((2N)!\prod k_i!/(2N+\sum k_i)!\), agreeing
with the Laurent leading-coefficient calculation at repeated knots.
Agreement of the spectral rule and full moment walks through order
\(2N-1\) makes the interpolant integrate exactly. The first missing
walk uses every link from 1 through \(N\) twice in its square-root
Jacobi form. The stated tail domination makes the compact-\(z\)
interchanges valid for every fixed degree, jointly on the physical
time interval. At \(\lambda=0\) the probability measures, spectral
rules, and normalizations recover the pinned parent laws.
[E21 law][law] [E22 constants][phase]

The inherited weighted score bound is uniform on
\(0\le\lambda\le1/2\). Integration by parts gives \(2n+1\), and
the confinement slack 11 yields \(2n+12\). Applying Jensen to
\(u^2\mapsto\cosh(4\sqrt{u^2})\) and the recurrence therefore gives
the same \(B_n\) for the full physical time range. For \(N\ge2\),
\(\beta_j\le B_{N-2}\) on the retained links bounds every node
modulus by \(2\sqrt{B_{N-2}}\), and \(T_2=2\sum_{j<N}\beta_j\)
bounds the fourth trace through \(T_4\le\bar L_N^2 T_2\).
The \(U\) variance and fourth-moment allowances follow from one and
two recurrence steps. In (5) each of the three summands in \(m_4\)
is at most \(B_{N+1}^2\), and its factor of 24 gives the 72.
For \(N=1\) the node is 0 and \(S_0\) has second and fourth moments
\(1/6\) and \(1/15\). These identities give the displayed special
cases including \(\mathcal Q_1=B_2^2/5\).
[Parent score and envelope][envelope] [Reviewed proof §§1–3][proof]

For (6), the conditional node law has paired weights of parameter
2 and all odd moments vanish. Its moment denominator \((2N)_k\)
is at least \((2N)^k\). The paired-node product estimate keeps the
two occurrences of each positive node and its reflected partner;
the resulting exponent at \(t=2Y\) is bounded by
\(Y^2\bar T_N/[N^2(1-Y^2\bar L_N^2/N^2)]\). The denominator is
strictly positive for \(Y\in[0,1]\) by \(\bar L_N<N\), including
\(\bar L_1=0\). Concavity at the source argument supplies
\((2N+12)^{Y/2}\) before its weight \(1/(2N+1)\).
Cauchy–Schwarz applied to the second-order exponential
remainder uses \(\mathbb E e^{2Y|X|}\le2\mathcal A_N(Y)\).
This accounts for the factor \(1/2\) and the factor 2 under the
square root in (7). The stated growing disks make that
allowance vanish uniformly in heat time. The sign and sector
tests have their respective real-axis and \(\epsilon_N<1\)
requirements. No heat-time derivative estimate is used.
[Reviewed proof §3][proof] [Parent phase estimate][phase]

## Directed clearance, collar logarithm, and model cost

At nonzero \(z\), scaling the unit disk by the variable nonnegative
amplitude gives exactly the hull of 0 and the terminal disk.
For \(v=-G/q_N\), excluding each disk is equivalent to
\(|v-a|^2-a^2\varepsilon^2>0\) for every \(a\) in the compact
amplitude interval. Its minimum is the clamped vertex for
\(\varepsilon<1\) and can be taken at an endpoint for
\(\varepsilon\ge1\). This is a strict clearance test, distinct
from the angle bound for the actual positive amplitude. The
homotopy in the original value plane stays in the scaled hull
for all parameters, including 0. Positive distance therefore
gives a common winding count, with the count itself acquired
separately from the model. The real half-plane test alone can
hold when the model vanishes, which blocks this homotopy test.
[Reviewed proof §4][proof] [Parent directed consumer][directed]

In the stated paid collar, the full homotopy is nonvanishing and
the auxiliary-parameter integral is holomorphic in \(z\).
Integrating \((\partial_b H_b)/H_b\) exponentiates to \(F/G\)
without any heat-time equation for the model. The clearance is a
lower bound for every homotopy denominator, so the ratio in (10)
pays an actual logarithm, including its choice of branch.
A collar estimated by the strip inequality requires that strip
payment at its points. For the E02 interface, only the boundary
log bound and existence of an analytic collar are used. If a
uniform positive clearance is already verified on \(\Gamma\),
continuity of the actual homotopy on the compact set of
\(\lambda,z,b\) there gives nonvanishing on some open collar
even when \(\Gamma\) touches a strip edge. The integral then
defines the logarithm on that collar and (10) bounds it on
\(\Gamma\). This observation supplies no directed clearance
estimate across the strip edge or on a prescribed wider collar.
[Reviewed proof §4][proof] [E02 frozen contract][e02]

The coefficient accounting is exact at each fixed time. The
first \(N-1\) links suffice for \(G_N\) and for the upper amplitude
in (8), with \(B_0/2\) at \(N=1\). The exact correction needs
\(\beta_N\). The exact variance and fourth moment respectively
require through \(\beta_{N+1}\) and \(\beta_{N+2}\), while the
degree-only allowances require no acquired link. After buying
\(\beta_N\), the next physical head is available with the same
prefix. The consecutive factorial ratio is
\(1/[(2N+1)(2N+2)]\), and combining it with the variance in
(3) gives the stated actual error quotient at zero. The
near-zero actual ordering and uniform bound comparison have
their separate scopes. Neither claims an all-strip ordering.
[Reviewed proof §5][proof] [Parent comparison][directed]

## Scope and controls

The three- and four-square controls share the weighted cosh and
adjacent coefficient bounds in their own physical probability
laws. The factor \(u\) removes any integration-by-parts junction
term, so the uniform time extension retains their collision
examples without imposing the missing complete reflection or
equal arithmetic coefficients. The specified finite positive
square changes and bounded positive finite-prime orbits share
the same basis for confinement and fail full canonical
identities. These premises permit the asserted approximation
estimate on colliding sources. The Euler \(c=1/2,p=23\) failure
is only the inherited \(B_0\) test at time zero. The reflected
super-Gaussian fails the exponential confinement argument,
and the smooth or positive-primitive controls lack the exact
summand score. There is no inferred failure of every weaker
moment bound. The atomic envelope failure is at the named
three-atom event, and the probability law has the stated
positive-norm degree limit for finite support. The RH-conditional
controls retain their RH premise and lack ordinary arithmetic.
Changed observation kernels fail the literal Fourier readout,
and the profile relaxation supplies no actual field of that
type. No control witness was recomputed.
[Reviewed proof §6][proof] [Controls catalog][controls]
[Parent internal assessment][parent-review]

Canonical boundary geometry, paid clearance values and a usable
signed cost relative to the incoming gap remain open application
inputs. The checks support the fixed quadrature transfer and
do not establish the branch's collision-exclusion objective.

[e05]: ../research-progress/handoffs/VCD-GT-E05-r1.md
[e01]: ../research-progress/handoffs/VCD-GT-E01-r1.md
[e02]: ../research-progress/handoffs/VCD-GT-E02-r1.md
[proof]: ../notes/03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[envelope]: ../../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[law]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[phase]: ../../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[directed]: ../../notes/22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md
[parent-review]: ../../reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[shared]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
