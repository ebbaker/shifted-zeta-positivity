# Assessment of collision scale estimates and proof mechanisms

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.
Chat0003, thread `01a17da8-4a84-7df3-b309-ec18e0535f1e`.

**Same-assistant assessment of [Note07][note].** The elementary scaling,
transfer and Hermite-energy deductions were checked algebraically against
the canonical normalization and the cited source records. This is an
analytical synthesis and brainstorm, with no new canonical inequality,
numerical certificate, independent review or upgrade of TRD status.

## Mathematical checks

1. **Heat orientation and source shift.** With H_t=-H_zz, the event
   polynomial is exp(-s partial_w^2)w^m. A double has w^2-2s, real
   roots for s>0 and nonreal roots for s<0. The Gaussian identity
   propagates from t_c to t_c-epsilon. The source at t_c is explicitly
   exp(t_c u^2)Phi(u). No negative-time canonical approximation is
   imported at a positive base by a change of labels.

2. **Normal-form amplitude.** The coefficient c=H_z^(m)/m! is nonzero
   only under the stated exact-multiplicity assumption. Cauchy's series
   bound after division by c r^m gives 2M r/(|c|rho^(m+1)). Spatial
   derivative bounds use a unit scaled buffer, not a fixed physical
   buffer. The argument adapts the previously recorded complete-source
   normal form and does not acquire a canonical lower bound for |c|.

3. **Kernel scaling.** Under u=a+rv, the factor r from du cancels the
   r^-1 Gaussian normalization. On fixed scaled rectangles and a compact
   positive theta interval, exp((Im w)^2/(4theta)) and every specified
   weighted Gaussian derivative integral are independent of r. Physical
   derivatives retain r^-j, and physical time derivatives retain r^-2.

4. **Local error and remote tail.** C10 assumes an actual normalized
   error bound, including |c|r^m. For theta in [1/2,2] and V>=2A+2,
   the outside Gaussian is bounded by exp(-v^2/32); splitting it once
   more pays polynomial derivatives and yields C11 with exp(-V^2/64).
   Locality does not remove the outside amplitude D/(|c|r^m).

5. **Weak response and regulator.** For psi_r=r^2 psi((z-a)/r),
   Delta_z psi_r=Delta_w psi and its physical L1 norm gains r^2.
   The response normalization cancels exactly that factor. The gradient
   norm of log(|v|^2+eta^2) is at most 1/eta, proving C15 with its
   stated 1/(4pi) convention. Regulator bias and root/no-entry gates
   remain separate. A dimensionless eta corresponds to physical field
   regulator eta |c|r^m. This is an auxiliary diagnostic, not the
   unchanged Book measurement prescription.

6. **Hermite energy constant.** P_m(1,w) solves
   P''-(w/2)P'+(m/2)P=0. At its roots the reciprocal-gap sum is h_i/4.
   Squared sums cancel triple cross terms; sum h_i^2=2m(m-1) gives
   the unordered-pair coefficient m(m-1)/16. In particular m=2 gives
   1/8 and m=3 gives 3/8. No ordered/unordered factor is omitted.
   The stated O(s^-1/2) remainder follows from the usual O(s) root
   errors and is integrable. C18's error is O(r); C19's error is O(1)
   as epsilon tends to zero with s_0 fixed.

7. **Energy implication.** Nonnegative E_W dominates the collision
   cluster. A coefficient theta<1/8 independent of the artificial
   lower cutoff contradicts every m>=2. The proposed upper bound is
   unproved. Energy dissipation, smooth H, a gap-dependent constant,
   a weight vanishing at the event, or a subtraction of the 1/s term
   cannot be substituted for it.

8. **Explicit positive control.** For C22, division by e^t and q=cos z
   gives 2bq^2+q-b with b=e^(3(t-t_c)). Its positive root belongs to
   (0,1), while the negative root enters [-1,0) exactly at b=1.
   Hence the stated threshold is t_c. At z=pi the curvature is
   -3e^(t_c), confirming a double. This control has positive atomic
   source but infinitely many threshold events and lacks canonical
   exterior asymptotics. It tests the universal and positivity claims
   only; no stronger preservation list is inferred.

## Source scope and classification

The [positive-threshold note][positive] already formulates the 1/s
endpoint energy problem. [BW-10 Note22][profile] already proves a
quantitative heat-scale profile and shows that matching controls share
it. Their contributions are explicitly attributed. The exact energy
coefficient and dyadic presentation here are elementary deductions,
not a new endpoint upper bound or a novelty claim.

Polymath Proposition 3.1(ii) was rechecked in the v2 primary HTML for
normalization, multiplicity and the O(|t-t_c|) root remainder. The
Rodgers--Tao v5 energy discussion and interval orientation were rechecked;
its infinite energy needs truncation/renormalization and is not identified
with an unqualified finite-cluster energy. No full proof audit is claimed.

The controls in [cluster12][controls] and the warnings in
[avoid01][classification], [avoid02][screen] and [avoid07][scope] are
applied before proposing exclusion. Naming the literal theta identity
as a missing control premise does not establish that a derived bound
would reject the control. The smooth-density and two-channel entries
are information-class screens, not additional claimed heat-collision
examples. The leading-profile obstruction is limited to its stated class.

C20 and the source-side response bound are final-strength targets, not
evidence that RH holds. C7--C15 are conditional resolution statements.
The next useful return must acquire a numerical coefficient or rate in
an actual source-dependent inequality, or demonstrate a scoped failure
of a specified estimate. No field evaluator, zero search, manuscript
milestone, new scheduled work or Git commit is part of this note.

[note]: ../notes/07_COLLISION_SCALE_RESOLUTION_AND_PROOF_MECHANISMS_20261027.md
[positive]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[profile]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../avoid/01_restating_the_target.md
[screen]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

## Follow-up assessment: fixed positive slabs and shifted sources

27 October 2026. Same assistant, **gpt-6-astra, actual effort max**.
The Section 9 addition to [Note07][note] is a conditional clarification.
Checked that the known anchor Lambda<=B and the canonical finite-event
reduction make exclusion on (b,B] sufficient for Lambda<=b; exclusion
only in a finite height range would not suffice without the exterior.
C23 compares unordered-pair energy with the minimum coefficient 1/8,
allows fixed-event constants, and forbids hidden cutoff/gap dependence.
Summable annulus errors affect only its bounded term; persistent annulus
errors can affect its logarithmic coefficient. No such source upper bound
or certified improved numerical value has been supplied.

The shift G(tau,z)=H(t_c+tau,z) is exact, but the source retains
exp(t_c u^2); at tau=-r^2 its combined weight is exp((t_c-r^2)u^2).
The old negative-time remainder theorem is not imported. The inherited
Section 7 controls and their stated failed premises remain unchanged.
Neither the fixed-slab criterion nor a second coordinate description is
counted as a new research result. No independent review is claimed.
