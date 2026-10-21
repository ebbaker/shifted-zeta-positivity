# Internal review of the resolved curvature-disk comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this research chat's metadata.
**Same-assistant analytic review; no independent or specialist review.**

[Note 01][note] gives an event-conditioned, finite curvature diagnostic.
Its inner bounds are derived from complete-source normal-form errors;
the source constants are specified but have not been numerically
acquired for theta. The result is not an endpoint-exclusion theorem.
The [result index][results] and [avoid index][avoid], particularly
[control matching][a02] and [scope][a07], govern this assessment.

## Analytic checks

- **Inherited versus new work.** BW10 Note 12 already gives all real
  stationary centers and the width \(2t/m\). Note 22 supplies the
  complete-source errors; Note 24 supplies the total concentration and
  outer flux error. The added result is the finite complex-disk
  enclosure G9 and the simultaneous growing-window estimate G11–G14.
  The note attributes those inputs and does not count their rederivation
  as an arithmetic gain.
- **Original physical jet.** For \(y=x_i+\tau q/m\),
  \(H_z/H=p_\tau'/(\tau p_\tau)\), whereas
  \(z=c_i+\tau^2q/m\). Differentiating in \(q\) therefore gives
  \((p_\tau''/p_\tau-(p_\tau'/p_\tau)^2)/m\), exactly G10.
  The area Jacobian cancels the same \(\tau^2/m\) scale. The
  pair is \((H,H_z)\), including at odd multiplicity.
- **Critical points and denominators.** Rouché on \(P'\) isolates one
  simple critical point in each inner polynomial disk. The larger
  disks have \(|p_\tau|\ge g-\delta_0>0\). The segment estimates
  stay in those convex disks. Neither a small physical energy floor
  at the endpoint nor global real-root information is inserted.
- **Area is counted once.** The estimate \(|F_i'+1|\le\eta<1\)
  proves injectivity by chord integration. Image containment and
  Rouché then place its image between two concentric disks. Without
  injectivity, an upper area bound from image containment would be
  invalid; the proof supplies the needed premise.
- **Growing windows.** With \(C=\tau^{-1/2}\), the scaled radius is
  \(\sqrt\tau/m\), and the physical radius is \(\tau^{3/2}/m\).
  G8 gives \(\eta\le L_1\sqrt\tau+L_2\tau\) under the displayed
  finite restrictions. Thus G11 does not exchange a fixed-window
  limit with an uncontrolled infinite window. Disjoint parent disks
  justify adding the masses and the Euclidean areas.
- **Outer accounting.** G14 follows by subtracting the actual inner
  masses from GA7's whole-disk bound. Its residual contains the
  regular endpoint area and the entire moving complement. GA7's
  boundary floor and simple-splitting range remain explicit
  conditions, not evaluated theta constants. The product-surface
  conversion is \(2\operatorname{Area}(B)\), not a new exclusion.
- **Same-information conclusion.** The condition \(h>0\) required
  before forming \(H_z/H\) already certifies scalar nonvanishing
  on larger positive-time sets. Hence this particular curvature
  monitor cannot improve nonvanishing coverage over that direct
  reference. This is not a universal computational dominance claim.

## Exact finite replay and its limits

The [checker][checker] passed with standard-library exact rational
arithmetic. It independently constructs Hermite polynomials by recurrence
and heat polynomials by the heat operator, checks their normalization and
equations for orders 2–16, and checks the Riccati identity and original
complex area scaling at 42 Gaussian-rational samples of asymmetric heat
germs. These finite checks catch transcription and normalization errors;
they do not prove the universal analytic statements.

The double and cubic controls at \(\tau=1/8\) give respectively
\(\eta=1/18\) and \(131/1587\). An independent rational square-root
enclosure for the exact quadratic area lies strictly between
\(0.5000076\pi\) and \(0.5000077\pi\), within G9's enclosure.
The whole-disk control at \(R=1,t=1/128\) contains two simple roots
but has area greater than \(\pi\); increased precision cannot make
that specified small-area test pass.

The [receipt][receipt] binds the checker, research note, and inherited
source notes. No theta quadrature, source-tail evaluation, timing
comparison, high-ordinate experiment, or specialist validation occurred.
The control-family screen is analytic substitution of recorded local
event germs, with each family's own bounds and failed theta premise;
no common numerical constants or all-real heat slices are assigned to
the finite-source controls.

## Status recommendation

Record GPJ-01 as an event-conditioned comparison contract completed.
Record GPJ-02 as a completed diagnostic subtask with its opposing
theta estimate still open. Stop the **leading-mass/direct-exclusion
comparison using G3–G9** as an exclusion improvement; retain it as a
quantitative diagnostic. Leave GPJ-03's different-observable benefit
question open and GPJ-04 gated.

The next step must change the source estimate or compensated observable,
not merely evaluate the same normal-form constants more accurately.
No evidence in this round excludes a hypothetical multiple theta zero
or upgrades the inherited HMC status.

[note]: ../notes/01_RESOLVED_CURVATURE_DISKS_AND_DIRECT_COMPARISON_20261021.md
[checker]: ../numerics/check_resolved_curvature_disks.py
[receipt]: ../numerics/RESOLVED_CURVATURE_DISK_CHECKS_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
