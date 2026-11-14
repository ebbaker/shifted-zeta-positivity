# Same-assistant assessment of the B06 short-window packet test

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Current actual model and reasoning
effort are unavailable in recorded configurations. This is checking by
the author of the argument, not an additional-agent or specialist review.

**Disposition: the bounded B06 failure is supported by the written
estimates, conditional on the inherited accepted E09 localization.**
[Note25](../notes/25_GNP_BB_B06_SHORT_WINDOW_AND_ACTUAL_PACKET_20261113.md)
does not establish or refute the full short-center witness. Its definite
conclusion is that the specified actual-phase quartic packet has
vanishing energy and vanishing effect on the complete averaged moment.
[E11 r1](../research-progress/handoffs/GNP-BB-E11-r1.md) is the fixed
request for a distinct review; it remains unstarted.

## Analytical checks

- **Consumed norm and moving endpoints.** The triangular measure has
  mass one; P has mass2/5. E09's bound can therefore be integrated in
  the joint norm without a window-length loss. The real cutoff
  movements have powers -59/64 and -21/32; at most one integer per
  cutoff changes eventually. Their amplitudes have powers -771/16384
  and -75/256. Common weights and the exact correction in tau cost
  O(U^(-243/256)), uniformly in v. The statement is a square-root
  moment transfer. In particular the crude product of the localization
  norm with the full norm allowance has exponent31/8192>0, so it would
  not justify an additive moment o(1) claim. Note25 does not make one.
- **Complete quadratic.** Convolution of two interval probability
  densities yields the triangular profile. The center frequency is
  log(n/m)/2, giving sinc²(H log(n/m)/4); the spatial frequency gives
  P_hat(log(n/m)/2). The actual center phase and every pair are retained.
  Nonnegativity comes from the norm, not separate cross-term signs.
- **Cell estimates.** The logarithmic cells are narrower than the
  entire middle band but contain O(D/H) integers, with the usual +1
  absorbed because D/H tends to infinity uniformly at the lower edge.
  The cell-distance row has summable inverse-square decay. Its
  geometric amplitude sum gives F=O(U^(1/128)); square-root transfer
  gives the same allowance for A. No small upper constant follows.
  The separate r-cell estimate and the full deletion estimate have
  different thresholds,3/128 and1/64 respectively. Both are stated
  with their correct scope.
- **Actual center and lower construction.** tau is strictly increasing
  eventually; its equation defines actual Y_D~48pi D^4. U=2Y_D/3
  places that center inside the permitted window. The selected indices
  D through D+floor(D^(1/5)/4) are in the middle band uniformly over
  the window. The four Taylor coefficients divided by2pi are the
  integers12,-6,4,-3. The next integrated geometric-series remainder
  is bounded by3pi/640<1/32, and the remaining relative phase over the
  physical window and |v|<=1 tends to zero. Positivity of the restricted
  P mass provides the lower norm bound; the triangle inequality provides
  the upper. Their common order is U^(-241/640).
- **Full background payment.** The original complete tail, including
  both discarded middle-band complements, has joint norm O(U^(1/256)).
  Pairing it with the actual packet of norm O(U^(-241/1280)) costs
  O(U^(-59/320)); the packet's own squared norm decays faster. Thus
  every background cross term is included. The remainder's own moment
  remains unknown; no lower estimate on the selected packet is
  substituted for the full moment.

## Recorded checks and limitations

The [small record](../numerics/21_GNP_BB_B06_INPUTS_AND_CHECKS_20261113.json)
replays19 exact rational powers and the integer Taylor coefficients.
E09's actual hash still matches its E10 review. These checks cover
finite arithmetic and provenance, not the analytical argument. No field
evaluation, sampled large value, interval certificate, support scan,
new exponent-pair search or numerical onset is supplied.

The [source-use record](../references/06_GNP_BB_B06_SOURCE_USE_20261113.md)
distinguishes direct derivations, inherited accepted input and limited
primary-source reinspection. Note25's control table states the failed
canonical premise for each listed source class. The norm lemmas also
apply outside theta and do not independently exclude collisions.

The B06 completion is the exact failure of the tested mechanism,
not a negative answer to A_U(Y)>=5/66². Every-center4/66², conditional
9/16, compact heights, near-zero time, global Newman conclusions and
iteration remain open. Existing accepted width567/1000 retains its
domain and symbolic onset. The [results index](../../../../../result-summaries/README.md),
[heat-flow cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[avoid index](../../../../../avoid/README.md) and
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
govern those status distinctions.
