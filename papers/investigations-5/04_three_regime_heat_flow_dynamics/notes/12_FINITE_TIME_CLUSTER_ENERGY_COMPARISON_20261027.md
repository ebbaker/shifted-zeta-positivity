# Finite-time cluster energy comparison with the full exterior

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, **Continue heat-flow research**, thread
`01a17e41-99d3-79c1-b932-2bae84ad0d47`.

**Status: proved in-note conditional finite-time lower bounds; internal
same-model checks. No collision exclusion or improved Newman upper bound.**
The gain over [Note10][n10] is an inequality on an entire isolating
right-time interval, rather than an asymptotic with an unsigned remainder.
The logarithmic coefficient is still exactly the universal coefficient.
The full exterior has a compressive sign at an all-real threshold.

This continues [Note08][assignment] after [Note11][n11]'s stop on further
bounded local jet refinements. Read the [result index][results],
[control register][controls], and [avoid index][avoid], especially
[target classification][a01], [premise screening][a02],
[scoped conclusions][a07], and [coupled estimates][a12]. These elementary
deductions carry no literature-priority claim. [Review06][review] describes
the checks and [Note13][n13] supplies a separate source-acquisition gain.

## 1. Domain and normalization

Fix a hypothetical canonical threshold t_c=Lambda>0 and a real zero a
of exact finite multiplicity m>=2. Choose a fixed isolating wall as in
[Note09][n09]. On 0<u<=u_0, t=t_c+u, assume the m resulting roots stay
inside that wall and are real and simple. All exterior zeros are real.
For the canonical threshold these properties follow on a sufficiently
small interval from the all-real slice and Hermite unfolding. No numerical
wall, uniform interval, or positive source margin is acquired here.

Write H=UP for the complete preparation and retain Note09's b=U_z/U.
To avoid a factor-of-two ambiguity define the **exterior velocity**
B(t,x)=2b(t,x). Put

\[
 f_i=\sum_{j\ne i}\frac1{x_i-x_j},\quad
 x_i'=2f_i+B(t,x_i),\quad y_i=x_i-\bar x,\quad
 V=\sum_i y_i^2,\quad E=\sum_{i<j}(x_i-x_j)^{-2},
 \quad p=\frac{m(m-1)}2,\quad\kappa=\frac p8.                 \tag{1}
\]

The root equation, order-one paired product, and local unfolding are the
imported inputs in [Polymath v2, Proposition 3.1][poly], rechecked in this
turn. Differentiating the exterior product gives

\[
 B_x(t,x)=-2\sum_{\lambda\ \text{exterior}}(x-\lambda)^{-2}\le0.
                                                                    \tag{2}
\]

The series, with multiplicity, converges locally uniformly away from
exterior zeros: order one implies convergence of the inverse-square tail.
An allowed linear exponential contributes a common drift only. No quadratic
exponential factor is available in this order-one class. The cluster hull
contains no exterior zero. Formula (2) is a consequence of the **global
all-real hypothesis**, not of a bare local event or source positivity.

## 2. Exact variance and shape defects

Pair symmetrization and cancellation over each distinct triple give

\[
 \sum_i f_i=0,\qquad \sum_i y_i f_i=p,\qquad
 \sum_i f_i^2=2E.
\]

Expanding a square therefore proves, at every such simple slice,

\[
 \boxed{E=\frac{p^2}{2V}
    +\frac12\sum_i\left(f_i-\frac pV y_i\right)^2.}           \tag{3}
\]

This is stronger than using an arbitrary minimum gap. Equality in its
first term means a translated and scaled Hermite root configuration.
Indeed the centered monic polynomial Q then satisfies
Q''-2(p/V)y Q'+2(pm/V)Q=0; the left side has degree at most m-1
after its leading terms cancel and vanishes at all m roots. Conversely
that equation implies equality. For m=2 the shape defect always vanishes.

Keep the exterior jointly by defining

\[
 S=-\sum_i y_i B(t,x_i)
  =-\frac1m\sum_{i<j}(x_i-x_j)(B(t,x_i)-B(t,x_j))\ge0.
\]

Differentiating V cancels the center velocity and gives the exact identity

\[
 \boxed{V'=4p-2S,\qquad
 V(u)=4pu-2\int_0^u S(v)\,dv\le4pu.}                       \tag{4}
\]

The extension to u=0 uses V(0)=0. B_x is bounded on the fixed local
neighborhood, so S=O(V)=O(u) by the inherited local unfolding. Thus the
integral at zero is legitimate; no individual infinite root velocity
is integrated across the event. Combining (3) and (4) proves

\[
 \boxed{E(t_c+u)\ge\frac\kappa u,\qquad 0<u\le u_0.}       \tag{5}
\]

## 3. A quantitative exterior floor and its integrated bound

If a constant lambda>=0 satisfies B_x<=-lambda on every cluster hull
throughout the interval, then S>=lambda V and

\[
 V'\le4p-2\lambda V,\qquad
 V(u)\le\frac{2p}{\lambda}(1-e^{-2\lambda u}),
\]
\[
 \boxed{E(t_c+u)\ge
 \frac{p\lambda}{4(1-e^{-2\lambda u})}.}                    \tag{6}
\]

Use continuous limits for lambda=0. For lambda>0, integration yields

\[
 \int_\epsilon^{u_0}E(t_c+u)\,du
 \ge\kappa\log\frac{e^{2\lambda u_0}-1}
                         {e^{2\lambda\epsilon}-1}.         \tag{7}
\]

In particular on [r^2,4r^2], within the same interval,

\[
 I_r\ge\kappa\log\frac{e^{8\lambda r^2}-1}
                              {e^{2\lambda r^2}-1}
 =\kappa\log4+3\kappa\lambda r^2+O(r^4).                  \tag{8}
\]

Evenness provides a concrete floor. Source positivity implies a!=0.
If the cluster stays in |x_i-a|<=rho<|a|, its reflected m-root cluster
is exterior and stays in |lambda_j+a|<=rho. For every x in the first
cluster hull its distance to a reflected root is at most 2(|a|+rho).
Consequently one may take

\[
 \lambda_{\rm ref}=\frac{m}{2(|a|+\rho)^2}>0.              \tag{9}
\]

This proves a strictly stronger finite-time lower bound than (5).
The elementary inequality (1-e^{-z})^{-1}>=z^{-1}+1/2 gives also
E>=kappa/u+kappa lambda_ref. These are lower bounds, with no independent
upper bound with which to contradict them.

At the event gamma=(log U)_zz(t_c,a) from Note10 gives
-B_x(t_c,a)=-2gamma. By continuity, on sufficiently small shrinking
neighborhoods the allowable lambda approaches -2gamma. The constant
term kappa lambda in (6) then matches -2kappa gamma in Note10.
The reflection-only limit matches kappa m/(2a^2).

## 4. Full nonlocal identity and scale audit

Set q(u)=S(u)/V(u)>=0 and Q(u)=integral_0^u q(v)dv. Equations (3)-(4)
give without discarding the signed exterior

\[
 V(u)=4p e^{-2Q(u)}\int_0^u e^{2Q(v)}dv,
\]
\[
 \boxed{E=\kappa(\log V)'+2\kappa q
       +\frac12\sum_i\left(f_i-\frac pV y_i\right)^2.}     \tag{10}
\]

Here q(u)->-2gamma. In fact this follows by the mean-value formula for
B_i-B_j as all roots tend to a. Thus bounded exterior curvature changes
V by O(u^2); its energy contribution per logarithmic annulus is O(r^2).
The shape defect is nonnegative, not a source of an upper saving.
The residue in (7) remains kappa. This exact nonlocal calculation confirms
the first return's scoped failure without adding higher local jet orders.

Subtracting kappa/u from E leaves the finite correction already computed
in Note10. Bounding that renormalized integral alone cannot contradict
the logarithmic divergence. Enlarging a real-root window that contains
the entire cluster adds nonnegative pairs. A moving window that cuts or
exchanges members needs new crossing and population payments; the fixed
cluster identities do not supply them.

## 5. Controls, quantifiers, and disposition

| Control | Outcome under the actual premises |
| --- | --- |
| Free heat polynomial; exponential unit | Attain (5); a common drift disappears. These lack the theta source and global canonical growth. |
| Positive atomic thresholds | Satisfy the monotone exterior comparison; actual collisions remain possible. They fail theta arithmetic and eventual simplicity at the threshold. |
| Euler-factor thresholds | Pass (2)-(8) at their all-real thresholds; no derived inequality here distinguishes them. Ordinary theta coefficients/completion fail. |
| Weighted-square / finite-tail controls | Their event slices have no all-real heat time, so the global premise for (2) fails; do not impose this comparison on them. |
| Reflected, smooth-shape, positive-primitive controls | Local collision formulas alone do not establish the all-real global premise. Apply (2) only if that separate premise is verified. Their unchanged theta arithmetic fails. |
| Finite-prime controls | Their local events do not supply an all-real threshold, so (2) cannot be inferred. Full reflection and unchanged theta coefficients fail. |
| Exact finite-profile threshold controls | Their documented order-one all-real threshold models pass the comparison, including the continuous compact-source extension. Unchanged theta coefficients, full profile growth and eventual simplicity at the threshold fail. |
| RH-conditional endpoint controls | Use this geometry only on slices with the verified all-real/growth hypotheses; they are not unconditional positive-threshold counterexamples. |

These statements hold at each fixed finite event of arbitrary finite m.
No uniform lower bound for |c|, isolating wall, event time, or multiplicity
is needed for (5), but the common interval and reflection floor depend on
the event. A positive-slab application still requires a canonical input
incompatible with the event. CE-04 gains a finite-time geometric lower
bound, not an arithmetic exclusion. CE-06 remains open. See
[the progress register][progress] and [the next calculation][next].

[n09]: 09_COMPLETE_SOURCE_AND_SCALED_ENERGY_TRANSFER_20261027.md
[n10]: 10_COUPLED_CURVATURE_AND_ENERGY_BUDGET_20261027.md
[n11]: 11_COLLISION_ENERGY_FIRST_RETURN_CONTINUATION_20261027.md
[n13]: 13_UNCONDITIONED_SOURCE_ACQUISITION_AT_COLLISION_SCALE_20261027.md
[assignment]: 08_COLLISION_ENERGY_CONTINUATION_20261027.md
[review]: ../reviews/06_FINITE_TIME_COMPARISON_AND_SOURCE_ACQUISITION_REVIEW_20261027.md
[progress]: ../research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md
[next]: 14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
