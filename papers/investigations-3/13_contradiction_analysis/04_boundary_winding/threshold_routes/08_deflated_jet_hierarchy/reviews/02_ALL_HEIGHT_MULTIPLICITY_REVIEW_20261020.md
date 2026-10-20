# Review of the all-height, finite-multiplicity jet bound

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. This is a separate subagent review within the
same-model research session, not independent specialist review.

**Assessment: the restricted analytic claim is supported.** The
[result note][note] proves a strictly stronger necessary condition than
the mirror bound at every a>0 and finite m>=2. Its all-multiplicity proof
does not rely on the finite controls. It does not exclude a theta
collision, force a later witness or supply a physical winding transfer
for m>2.

## Proof checks

1. Taylor division by (z-a)^m gives exactly
   S_m=h_(m+1)^2/((m+1)^2 h_m^2)
   -2h_(m+2)/((m+1)(m+2)h_m). The m mirror roots at -a contribute
   m/(4a^2). No factor of two is missing.
2. The paired root kernel dominates 2/(rho^2+b^2) when b>=a.
   The imaginary-axis sum counts the positive representative a with
   coefficient 2m/(a^2+b^2), so this is the correct subtraction.
   A pure paired power attains equality in this comparison.
3. The reused full-source floor for D_T has b>=5 and T>=0. The selected
   b=max(a,20m) is at least 40 and satisfies both conditions. The estimate
   log((b+1)/(4pi))>1/2 and 2m/(a^2+b^2)<=1/(10b) yields the strict
   improvement 1/(40b). This choice removes the earlier height restriction
   without claiming to optimize b.
4. The differentiated critical-value identity is
   v_G''=-(m/(2(m+1)))(h_(m+1)/h_m)^2
   -((m+1)(m+2)/2)S_m. Its constants, finite-curve hypotheses and K_m
   match the inherited order-six argument after shifting orders by m-2.
   The maximal original derivative order is m+4, not six.
5. Multiplying S_m>L by (m+1)^2(m+2)h_m^2 gives the displayed Q_L.
   Its product allowance contains both cross errors and square errors.
   The interval lower coefficient uses the conservative endpoints in
   the correct direction. These formulas are acquisition interfaces;
   no opposing arithmetic estimate has been obtained.

Two scope clarifications were requested and incorporated during review: the finite-pair
consumer with delta<T must explicitly assume **T>0**, while the slice
bound itself permits T=0; and the optional b=a corollary inherits
**a>=5** from the source floor. These clarify the domains of existing
proofs and do not change the main all-height theorem.

## Exact replay and control interpretation

The reviewer ran [check_all_height_multiplicity.py][checker] with the
repository's inherited exact routines and an output outside the checkout.
All **nine polynomial controls and seven outward coefficient rows**
passed. The selected multiplicities were 2,3,4,6, with negative
normalization, b=a and b>a, and additional real root pairs. The
coefficient rows are values at hypothetical parameters, not measured
theta events.

The pure paired-power controls attain the kernel comparison and fail
the selected scalar floor. Several controls with additional roots pass
that floor and still have the prescribed multiple event. This correctly
shows that the floor is not an exclusion criterion. The Euler-factor
screen is especially relevant: it preserves the positive-source
imaginary-axis lower estimate while changing the source, so this
necessary condition does not remove that positively colliding family.
No theta tails were assigned to the control polynomials, and no
existence-only source received an invented numerical event.

The [record][record] is small and binds source versions by hash. Replaying
it checks the finite arithmetic assertions and their coefficient
enclosures; it is not independent evidence for the theorem's universal
quantifiers or the missing opposing sign.

## Classification and remaining gap

The useful gain is the removal of the old a>=20 restriction and the
explicit extension of the unchanged source's necessary jet bound to
every finite multiplicity. The physical double-event consumer is paid.
For higher multiplicities the named consumer belongs to the derivative
field, as the note says, and [BW-07][bw07] audits that distinction.

The status is consistent with [local-law summaries][laws], [control
screening][controls], [target classification][a01], [same-model review
limits][a05] and [scoped conclusions][a07]. The remaining obstacle is an
independent signed arithmetic estimate incompatible with the necessary
bound, together with any required physical-jet transfer. Further
coefficient tables alone do not discharge it.

[note]: ../notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[checker]: ../numerics/check_all_height_multiplicity.py
[record]: ../numerics/ALL_HEIGHT_MULTIPLICITY_CONTROLS_20261020.json
[bw07]: ../../07_multiplicity_reduction/notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
