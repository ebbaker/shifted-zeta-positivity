# Whole-cluster Poisson transfer and acquisition requirements

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Status.** Opening research note. Proposition1 is an elementary conditional
finite-polynomial transfer derived here from explicit inputs; no novelty
claim is made for the quotient, norm or tail inequalities. Canonical
acquisition and a favorable collision-excluding inequality are unproved.
This is a baseline for HCB-01/02, not an RH or simplicity result.

Inputs are the [Book](../../01_heat_density_asymptotics/book/main.tex),
[Summary76](../../01_heat_density_asymptotics/notes/76_CHAT0028_RESEARCH_SUMMARY_20261026.md),
[application targets](../../02_heat_flow_rh_applications/rh_simple_zeros/notes/02_TARGET_BOUNDS_FOR_RH_TO_SIMPLICITY_20261026.md)
and [Review51](../../01_heat_density_asymptotics/reviews/51_RH_TARGET_GAP_ANALYSIS_AND_RESEARCH_PRIORITIES_20261026.md).
Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md),
[control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[coupled payments](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The [input record](INITIAL_INPUTS_20261026.json) identifies source bytes;
[Review01](../reviews/01_OPENING_TRANSFER_ASSESSMENT_20261026.md) records the bounded internal check.

## 1. Consumer and conventions

Use \(H_t=-H_{zz}\). At a fixed positive time let \(a_1,\ldots,a_n\)
be a complete selected real population, with repeated labels for
multiplicities. Define
\[
 P(z)=\prod_{i=1}^n(z-a_i),\qquad
 p_P(x)=-\frac1\pi\Im\frac{P'(x+iy)}{P(x+iy)}
       =\sum_i\frac{y}{\pi((x-a_i)^2+y^2)}.
\]
The target note supplies the exact identity
\[
 \mathscr D_P(y)=2\pi y\|p_P\|_{L^2(\mathbb R)}^2-n
 =\sum_{i\ne j}\frac{4y^2}{(a_i-a_j)^2+4y^2}. \tag{1}
\]
Under RH, when this population includes all descendants of any proposed
multiple endpoint in the target core, \(y=\sqrt t\) forces
\(\mathscr D_P\ge2/3\). The full zero dynamics bound an adjacent descendant
squared gap by \(8t\). A fully paid upper bound below \(2/3\) at one
admissible time therefore excludes that endpoint within this population.
Membership over the interval and the bounded-height remainder remain
separate obligations. This implication is imported from the target note.

In microscopic coordinates \(u=L(z-X)\), \(\tau=tL^2\), the same
dimensionless statistic uses width \(\sqrt\tau\). Coefficient bounds below
must use one declared coordinate system. The count \(n\) is cluster roots,
not the number of arithmetic modes in \(F_N\).

## 2. Transfer without internal separation

**Proposition1.** Fix \(n\ge1\), \(A\ge0\), \(r>0\), \(y>0\).
All roots of monic \(P\) lie in \([-A,A]\), counted with multiplicity.
Let \(Q\) be monic of degree \(n\) with complex coefficients; its roots
need not be real. Write
\[
 P(z)=z^n+\sum_{j=0}^{n-1}c_jz^j,\qquad
 Q(z)=z^n+\sum_{j=0}^{n-1}\widetilde c_jz^j,\qquad
 |c_j-\widetilde c_j|\le d_j.
\]
Put \(I=[-A-r,A+r]\), \(W=2(A+r)\), \(Z=\sqrt{(A+r)^2+y^2}\), and
\[
 \delta_0=\sum_{j=0}^{n-1}d_jZ^j,\qquad
 \delta_1=\sum_{j=1}^{n-1}j d_jZ^{j-1}. \tag{2}
\]
Assume \(\delta_0\le\theta y^n\) for a declared \(0\le\theta<1\).
Define
\[
 e_p=\frac{\delta_1+(n/y)\delta_0}{\pi(1-\theta)y^n},
 \qquad p_Q(x)=-\pi^{-1}\Im(Q'/Q)(x+iy). \tag{3}
\]
Then \(Q\) has no zero on \(I+iy\), and
\[
 \|p_P-p_Q\|_{L^\infty(I)}\le e_p,\qquad
 \|p_P-p_Q\|_{L^2(I)}\le\sqrt W\,e_p. \tag{4}
\]
For any proved or certified \(M_Q\ge\|p_Q\|_{L^2(I)}\), including the
entire continuous-integration error,
\[
 \boxed{\mathscr D_P(y)\le
 2\pi y(M_Q+\sqrt W\,e_p)^2-n+
 \frac{4n^2y^3}{3\pi r^3}.} \tag{5}
\]
No internal gap, root-slope floor, simplicity assumption or favorable sign
for \(p_Q\) is used. Coefficient enclosures, complete population, real-root
premise and continuous \(M_Q\) bound are inputs.

**Proof.** For \(z=x+iy\), every \(|z-a_i|\ge y\). Hence
\(|P(z)|\ge y^n\) and \(|P'/P|\le n/y\), also at repeated roots.
Formula(2) bounds \(P-Q\) and \(P'-Q'\) on \(I+iy\), so
\(|Q|\ge(1-\theta)y^n>0\). The exact correlated identity
\[
 \frac{P'}P-\frac{Q'}Q
 =\frac{(P'-Q')+(P'/P)(Q-P)}Q
\]
gives(3)–(4). The triangle inequality gives
\(\|p_P\|_{L^2(I)}\le M_Q+\sqrt W\,e_p\).
For \(|x|>A+r\), positivity of the true real-root Poisson sum gives
\[
 0\le p_P(x)\le\frac{ny}{\pi(|x|-A)^2},\qquad
 \int_{\mathbb R\setminus I}p_P(x)^2\,dx
 \le\frac{2n^2y^2}{3\pi^2r^3}.
\]
Multiply by \(2\pi y\), subtract the exact self term \(n\), and use(1).
The norm step does not require \(p_Q\) to be positive. QED.

To apply P, the complete right side of(5) must be below \(2/3\) by a
declared positive margin. A sampled integral or a relative second-moment
estimate is insufficient. Source, coefficient, integration and tail
errors cannot each consume the same margin.

## 3. Shrinking-scale loss and a sharpness calibration

At fixed \(n,A,r,\theta<1\), for \(y\le1\) and
\(\delta_0,\delta_1\le\varepsilon\), (3) gives
\(e_p=O(\varepsilon y^{-n-1})\). If \(M_Q=O(y^{-1/2})\), the extra
transfer terms beyond \(2\pi yM_Q^2\) have sufficient order
\[
 O(\varepsilon y^{-n-1/2}+
   \varepsilon^2 y^{-2n-1}). \tag{6}
\]
Thus \(\varepsilon=o(y^{n+1/2})\), equivalently
\(\varepsilon=o(\tau^{n/2+1/4})\) at \(y=\sqrt\tau\), suffices for
\(o(1)\) transfer in this coarse bound. Constants are fixed-population
and fixed-window constants, not uniform in growing \(n\). The assumed
bound for \(M_Q\) must also be paid, not inferred for arbitrary \(Q\).

This rate is not sharp. For \(P(u)=u^2-2\tau\) and
\(Q(u)=u^2-2\tau-\varepsilon\), \(\varepsilon>0\), at width \(\sqrt\tau\),
\[
 \mathscr D_P=\frac23,\qquad
 \mathscr D_Q=\frac{2\tau}{3\tau+\varepsilon},\qquad
 \mathscr D_P-\mathscr D_Q
 =\frac{2\varepsilon}{3(3\tau+\varepsilon)}. \tag{7}
\]
The actual statistic needs \(\varepsilon=o(\tau)\) for \(o(1)\) change,
whereas(6) with \(n=2\) asks for \(\varepsilon=o(\tau^{5/4})\).
This quarter-power loss suggests estimating the integrated correlated
quotient difference more accurately than its uniform bound over a fixed
window. It is not a general multiplicity-uniform improved exponent.

The existing \(O(X^{-3/4})\) field error is not automatically an equally
sized monic-coefficient error. Wall acquisition must pay conversion,
normalization and unit conditioning first. The quadratic
\(\varepsilon\ll\tau\) and equally spaced reference \(n\tau\ll1\)
calibration in Review51 cannot substitute for that theorem.

## 4. Canonical acquisition contract

Use a holomorphic regional arithmetic model with complete modes and
remainder. A nonholomorphic spatial join needs its own correction.
For \(H=UP\), the cluster quotient is \(H'/H-U'/U\); omitting the
exterior unit changes the statistic.

Acquire an enclosing wall over the declared time interval, prove its
lower margin dominates the complete field error, and certify the count.
Contour logarithmic moments and existing HDC transport can then supply
monic coefficient enclosures \(d_j\). Charge contour integration,
moment-to-coefficient conversion, unit normalization, source cancellation
and all residual terms used by time transport. Avoiding individual root
slopes does not make the wall margin free.

Start from [HDC coefficient transport](../../../investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md),
retaining its correlated source numerator and whole-wall assumptions.
The [forest-filter note](../../../investigations-4/12_height_dependent_heat_contours/notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md)
is a comparator: its complex coefficient quotient can have a nonremovable
denominator problem from multiplicity three onward. Proposition1 avoids
that quotient but pays the explicit \(y^n\) denominator.

An acquired \(M_Q\) encloses the continuous integral on \(I\), including
evaluation, quadrature and rounding errors. No useful algorithm/cost for
obtaining it is claimed here. Inequality(5) is the consumer against which
such a provider should be designed.

## 5. Controls, scope and next task

The polynomial double passes the heat, whole-wall and coefficient
premises. It has \(\mathscr D=2/3\), so a valid upper bound(5) cannot be
strictly below \(2/3\) there. The nearby simple polynomial
\(u^2-a^2-2\tau\) has \(\mathscr D=2\tau/(a^2+3\tau)\), arbitrarily
close to \(2/3\) when \(a^2\ll\tau\). Qualitative simplicity or average
spacing therefore does not supply a convenient universal clock.

Proposition1 is generic finite-polynomial analysis; it allows every
control meeting its real-population/data premises. No theta premise is
hidden in its proof. For future canonical arithmetic claims, Euler-factor
controls change canonical coefficients; weighted-square/finite-tail
controls lack full reflection/completion; reflected and positive-primitive
controls lack full theta arithmetic; finite-prime/profile controls retain
only their specified constraints; RH-conditional theta-close controls lack
ordinary Dirichlet arithmetic. Absent premises are not automatic failure
of every derived inequality. Check actual events against any proposed
strict bound. No control certificates or research numerics were rerun.

**Next: HCB-02.** Freeze one microscopic canonical family and acquire
(2)–(5)'s inputs, or return the first unproved wall/coefficient/integration
payment and its required size. Keep HCB-03's sharpening question explicit
and compare total demands with J. Interface completion alone does not
supply favorable arithmetic or global endpoint coverage.
