# Open boundaries, zero flux and a larger backward width

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Analytical assessment and elementary finite derivation by this chat; no independent specialist review or new theta computation.

**Status: finite flux extension and proposed estimation strategy; no acquired negative-time theta flux bound, larger certified backward width, or new simplicity proportion.** The author's suggestion is to allow zeros to enter a bounded region and estimate their contribution, rather than requiring a population to remain fixed. This is a useful relaxation, particularly for the RH-conditional density-one objective. Its benefit must be measured after including the flux allowance.

This continues the [progress review](03_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_AND_OBSTACLES_REVIEW_20261023.md) and [moving-collar discussion](../../../brainstorm/notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md). The [result index][results], [avoid index][avoid], [local heat geometry][geometry], [collision controls][controls], and patterns [01][a01], [02][a02], [07][a07] and [12][a12] govern its scope. It is a finite conditional tool, not a new RH criterion. Boundary corrections already occur in the repository's [real zero-transport manuscript][transport] and [height-boundary note][height]. The extension below makes the appropriate correction explicit for [HDC Note 05's earlier-time consumer][earlier].

## 1. Which no-crossing requirement is being relaxed?

Use the canonical convention H_t=−H_zz and backward real time a=−ε<0. Three boundary quantities have different consumers:

| Quantity | What it measures | What it can support |
| --- | --- | --- |
| Signed change in the total complex zero count | All inward crossings minus all outward crossings, with multiplicity | Conservation of the divisor |
| Nonreal-root inflow, or a sufficiently accurate signed nonreal flux | Nonreal labels available to become real at collision events | Earlier-time bounds on endpoint multiplicity |
| The physical first-jet side integral | Transport of the cap form constructed from (H,H_z) | The complete cap identity |

These quantities cannot be substituted for one another merely because each can be called flux.

The physical cap requires E=|H|²+|H_z|²>0 on its boundary. At an ordinary simple wall zero, H=0 but H_z≠0, so E remains positive. Such a crossing is already admissible in the chart-free cap formulation. The complete side integral must remain, and a multiple boundary zero H=H_z=0 still requires a separate event link or an excision. See the [current contour section][contours].

The coefficient construction H=UP with a fixed-degree prepared polynomial P has the stronger requirement H≠0 on its spatial wall over the time track. An entry changes its degree. Across a simple entry at z_c, the one-sided population update multiplies P by z−z_c; an exit divides it by that factor. Its power sums jump by ±z_c^k. Thus one can use separate fixed-population intervals and explicit transfer maps, but cannot insert a time-dependent degree into the existing fixed-dimensional commuting propagator. A crossing also changes all pair interactions involving that label; a root-count correction is not automatically an additive correction of the same size to q. See [coefficient transport][coefficients].

## 2. A finite nonreal-flux extension

Let Ω be a bounded conjugation-invariant domain. Assume H is a real-type holomorphic heat solution near [a,0]×closure(Ω), no slice is identically zero, the interior multiple events and boundary crossings are finite, and every spatial boundary crossing is simple and transverse. No zeros lie on the spatial boundary at a or 0, and no multiple zero lies on the spatial boundary during the track. Interior multiple zeros, including at t=0, are allowed. These assumptions separate ordinary entry from a simultaneous boundary collision.

Write N_nr(t) for the nonreal zeros in Ω at time t, counted with multiplicity. Let J_in^nr and J_out^nr be the numbers of nonreal labels crossing inward and outward during (a,0), counted at every crossing; a conjugate pair contributes two. Define the real-birth mass

\[
 B_{\rm real}(a,0)=
 \sum_{\substack{a<t\le0,\ x\in\Omega\cap\mathbb R\\
                  H(t,x)=H_z(t,x)=0}}
                  2\lfloor m(t,x)/2\rfloor.
\]

The exact balance is

\[
 \boxed{N_{\rm nr}(0)=N_{\rm nr}(a)
       +J_{\rm in}^{\rm nr}-J_{\rm out}^{\rm nr}
       -B_{\rm real}(a,0).} \tag{1}
\]

To prove it, split the time interval at the finitely many crossings and events. An inward or outward nonreal crossing changes N_nr by its signed multiplicity. An off-real collision preserves nonreal multiplicity. At a real event of order m, the local heat/Hermite law loses exactly 2 floor(m/2) nonreal labels as time increases. The event at 0 is included, and the event at a, if present, is excluded, exactly as in HDC Note 05. Summing the jumps proves (1). No individual labels need to be continued uniquely through a collision.

Let M_0^real be the multiplicity mass at the real multiple endpoint sites, and D_0^real their multiplicity excess. Since m≤3 floor(m/2) and m−1≤2 floor(m/2) for m≥2,

\[
 \begin{split}
 M_0^{\rm real}
 &\le\tfrac32 B_{\rm real}(a,0)\\
 &\le\tfrac32\bigl(N_{\rm nr}(a)+J_{\rm in}^{\rm nr}
                            -J_{\rm out}^{\rm nr}\bigr)\\
 &\le\boxed{\tfrac32\bigl(N_{\rm nr}(a)+J_{\rm in}^{\rm nr}\bigr)},
 \end{split} \tag{2}
\]

and D_0^real≤N_nr(a)+J_in^nr. The number of real multiple endpoint sites is at most half that same quantity. These statements count real endpoint sites without assuming RH. Under RH, the endpoint zeros of the canonical field are real, so (2) controls the entire nonsimple multiplicity mass M_0 in the chosen region.

This is the concrete replacement for no entry: charge incoming nonreal labels to the error allowance. It is permissible to bound J_in^nr by the total number of inward crossings if distinguishing real and nonreal labels is difficult, though that can be much less sharp. An accurately bounded signed *nonreal* flux can retain the favorable exit term. Merely approximating the net *total* complex count does not provide it: real exits can cancel nonreal entries in the total count.

## 3. The density-one and projected-pair consumers

Suppose a prescribed, source-derived ε and a specified band admit certified bounds

\[
 N_{\rm nr}(-\epsilon)\le A_\epsilon,
 \qquad J_{\rm in}^{\rm nr}\le\widehat J_\epsilon+E_\epsilon.
\]

Then

\[
 \boxed{M_0\le\tfrac32
       (A_\epsilon+\widehat J_\epsilon+E_\epsilon)} \tag{3}
\]

under endpoint reality. If the total right-hand input over the bands is o(N(T)), and the uncovered endpoint labels also number o(N(T)), the usual density-one conclusion follows. Nonzero flux is therefore compatible with this objective. Excluding every multiple zero would require an integer-scale estimate; a vanishing relative error alone does not do that.

The earlier projected-pair formulation survives as well. For a given band normalize its complete earlier-slice projected-pair measure by its *endpoint* count N_0:

\[
 \mu_{a,0}=\frac1{N_0}\sum_{i\ne j}
       \delta_{\nu(\Re z_i(a)-\Re z_j(a))}.
\]

Every nonreal label has a distinct conjugate label in Ω, so N_nr(a)/N_0≤μ_{a,0}({0}). Consequently

\[
 \frac{M_0}{N_0}\le\frac32\left(
       \mu_{a,0}(\{0\})+\frac{J_{\rm in}^{\rm nr}}{N_0}\right). \tag{4}
\]

A nonconcentration estimate at zero plus sublinear inward flux now suffices. Complete earlier populations and the specified normalization matter; the numbers of roots at the two times need not agree. Allowing ε to be chosen after learning the endpoint multiplicities still risks the reformulation identified in HDC Note 05. The flux identity does not resolve that circular choice.

## 4. A larger ε is a tradeoff, not an automatic sharper bound

For a fixed Ω define the conservative exact resource

\[
 R(a)=N_{\rm nr}(a)+J_{\rm in}^{\rm nr}(a,0).
\]

For a_1<a_2<0 satisfying the boundary assumptions, (1) on the prefix gives

\[
 R(a_1)-R(a_2)
 =J_{\rm out}^{\rm nr}(a_1,a_2)
       +B_{\rm real}(a_1,a_2)\ge0. \tag{5}
\]

Thus going farther backward cannot improve this *exact* conservative count bound on a fixed region. Even retaining the exact signed nonreal flux gives N_nr(0)+B_real(a,0), which accumulates earlier births. A larger width could nevertheless improve a *certified estimate*: the source approximation, regularized evaluation or conditioning may improve enough to offset the larger exact resource and the flux uncertainty. That is the comparison to test. Changing the region also changes the comparison and its coverage cost.

The physical cap has a parallel caution. Its complete relation is I_0=I_−ε−S_ε+Q_− with Q_−≥0, under its own regular boundary hypotheses. It already keeps S_ε. For nested cells, admitting more interior event charge can lower the exact deformed representative I_−ε−S_ε=I_0−Q_−. More allowable width does not by itself certify a better cap estimate. An ordinary zero-crossing count is not a replacement for S_ε.

## 5. A smooth window can remove the zero-free-wall bottleneck

A useful implementation starts with a target core and a surrounding buffer. Choose 0≤ψ≤1, ψ∈C_c², equal to one on the core and transitioning to zero in the buffer. The exact weighted divisor count is

\[
 N_\psi(t)=\sum_{H(t,z)=0}m_z\psi(z)
     =\frac1{2\pi}\int\log|H(t,z)|\,\Delta\psi(z)\,dA.
\]

The logarithmic singularities are locally integrable. To make source-error estimates stable, use a field regularization ρ>0, distinct from the time width ε:

\[
 u_\rho(H)=\tfrac12\log(|H|^2+\rho^2),\qquad
 N_{\psi,\rho}=\frac1{2\pi}\int u_\rho(H)\Delta\psi\,dA.
\]

The [existing logarithmic-regularization note][regularization] gives

\[
 \partial_tN_{\psi,\rho}
 =-\frac1{2\pi}\int
   \frac{\operatorname{Re}(\bar H H_{zz})}{|H|^2+\rho^2}
          \Delta\psi\,dA, \tag{6}
\]

and, when |H−H_ref|≤η on the support of ψ,

\[
 |N_{\psi,\rho}(H)-N_{\psi,\rho}(H_{\rm ref})|
 \le\frac{\eta}{4\pi\rho}\|\Delta\psi\|_1. \tag{7}
\]

No lower bound on |H| along a hard wall is needed for (6)–(7). The constants follow from max_r r/(r²+ρ²)=1/(2ρ). They retain the complete heat numerator and permit simple zeros to pass through the transition region.

This is stable weighted *total-zero* transport, not yet the nonreal inflow in (2). Returning to a sharp count costs the regulator bias and the transition-region mass. Returning to a one-sided nonreal inflow requires further information about the zero current and its relation to the real axis. Neither the signed weighted change nor its time variation automatically bounds all inward crossings: simultaneous entry and exit can cancel. Collisions preserve the total divisor, so smoothing that divisor does not create a simplicity detector. A velocity estimate also is not free: at a simple root z'(t)=H_zz/H_z, and H_z can be small near a collision.

## 6. What is already known at high height

The [existing height-boundary analysis][height], using [Polymath's high-height theorem][polymath], provides an encouraging but restricted precedent. For fixed 0<δ<T≤1/2 and sufficiently large R relative to δ, its signed real net entry at the right wall satisfies

\[
 \mathsf W_{\delta,T}(R)
   =\frac{T-\delta}{16}\log\frac R{4\pi}+O(1),
 \qquad
 \frac{\mathsf W_{\delta,T}(R)}{N_T(R)}
   =\frac{\pi(T-\delta)}{4R}+o(R^{-1}). \tag{8}
\]

Boundary transport can therefore be small relative to the population in an established canonical regime. But (8) is a *signed real* flux at *positive* times. It bounds neither gross nonreal entry on [−ε,0], nor the physical first-jet side integral. Its onset R≥exp(C/δ) is also part of the input. Extending a useful estimate into the negative-time or near-zero regime remains the substantive missing work; (8) is not that extension.

## 7. Collision controls and self-check

For Ω the unit disk and a=−1, H=z²−2t has no nonreal roots inside initially. Its two nonreal roots enter at t=−1/2, and produce a double zero at 0. Thus N_nr(a)=0, J_in^nr=2 and M_0=2. Discarding the entry term would give a false conclusion.

For H=z³−6tz on the same track, the nonreal pair enters at t=−1/6 and produces a triple endpoint with the already present real root. Here J_in^nr=2 and M_0=3, so the factor 3/2 in (2) remains sharp with open boundaries. Both crossings are simple and transverse. These examples permit a multiple zero on the final time slice as required by the count consumer; they are not examples of a physical cap regular through that endpoint event.

The real-type solution exp(κz+(k²−κ²)t) sin(k(z−2κt)), for real κ≠0 and k>0, has simple roots moving at speed 2κ. A rectangle of real width an integer multiple of π/k, with endpoints chosen off the roots at the initial and final times, can exchange roots across both vertical walls while its total count has zero net change. This tests the distinction between signed total flux and one-sided entry. It supplies no collision example and is not the canonical theta source.

The broader [control register][controls] is screened at the level actually claimed here: all generic finite identities remain valid wherever their hypotheses hold; **none of those controls is excluded by this note**. Euler-factor modifications fail the unchanged canonical coefficients/source. Weighted-square and finite-prime substitutes fail the recorded full reflection or complete arithmetic data; one cannot grant them a complete globally real heat system. Reflection-completed, super-Gaussian and smooth positive-primitive controls still alter the exact theta source. Close normalized endpoint controls show why shape and a fixed error tolerance alone do not exclude collisions. Their collisions must be paid through the nonreal resource or another defect-sensitive term, just as in the polynomial controls. A future theta estimate must use and quantify the relevant source information rather than treating these failures as an acquired bound.

Self-check of the proposed extension: (1) includes the upper endpoint event; (2) keeps multiplicity rather than only distinct sites; (4) uses a conjugation-invariant complete earlier population; (5) limits the claimed gain; (6) is a regularized total-divisor identity, not a proof of a small one-sided flux; and the positive-time result (8) is not continued through zero without new input.

## 8. A focused next calculation

Specify a core, buffer, coverage rule and a source-derived range of ε before inspecting endpoint multiplicities. Compare the current fixed-population method against an open-boundary calculation on the same target. For the earlier-time consumer, acquire a certified upper bound on N_nr(−ε) and one-sided nonreal inflow, including approximation errors. For the physical-cap consumer, acquire the full first-jet side integral and its error instead. The best width is the one giving the strongest completed estimate at comparable source information and cost, rather than simply the largest admissible ε.

The practical opportunity is replacing a potentially tiny pointwise wall margin by a controlled aggregate boundary contribution. The current obstacles are the lack of a negative-time theta estimate for that contribution, possible recrossings or near-collision speeds, conversion from a smooth count to the intended defect statistic, and propagation of all errors across growing-height bands. No manuscript or progress ledger is advanced by this brainstorm note.

The discussion remains uniquely registered as [brainstorm chat 0002][chat].

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[transport]: ../../../manuscript/zero_count_heat_transport/sections/04_zero_transport.tex
[height]: ../../../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md
[earlier]: ../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[contours]: ../../manuscript/contours.tex
[coefficients]: ../../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[regularization]: ../../../11_late_heat_caps_and_charge_transport/notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md
[polymath]: https://arxiv.org/html/1904.12438v2
[chat]: ../chat-histories/0002_2026-10-23T20-20-56Z_review-curved-contour-manuscript.json
