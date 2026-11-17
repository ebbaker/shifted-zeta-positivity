# VCD-GT-E17 r1 — source-specific averaged transverse correction

17 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance, chat0006. Root actual model/effort unavailable.
Executor dispatch gpt-6.1-sol/ultra; report actual exposed settings separately.
Type E, fixed analytical execution of B09 Decision17. Root alone owns the
sole register, integration and chat history.

## Frozen question and route

Keep canonical H_t, 0<=t<=1/2, all integer zero multiplicities, no all-real
assumption. Fix T>=16, L=log T, ell=1/L, 1<=a<=L, 3<=R<=T/2. Define

    Xi_{a,R}(t,X)=ell^2 sum_{rho: |rho-X|>=a ell,
                               |Re rho-X|<=R}
                         (Im rho)^2 / |rho-X|^4, X in [T,2T].

No selected pair is needed for this aggregate. Prove, with C independent
of t,T,a,R,

    (1/T) integral_T^{2T} Xi_{a,R}(t,X)dX <= C/a^3.       (A)

Use accepted TND-O Note21(8): for U>=8, sum_{U<=Re rho<=2U}(Im rho)^2
<=C_b U/log U uniformly in t, with one fixed 0<b<1/2. Cover
[T/2,5T/2] by three dyadic bands and use Tonelli with the elementary
integral, to be proved including y=0 and cutoff endpoints,

    I(y,r0)=integral_{x^2+y^2>=r0^2} y^2/(x^2+y^2)^2 dx
       <= (pi/2) min(1/r0,y^2/r0^3).

Give the same Fubini argument only the complete count O(T L) to prove
the equally averaged comparator C0/a. Do not compare (A) with a pointwise
O(L) allowance as the source gain. For a=L^eta, fixed0<eta<1, compare
L^(-3eta) with L^(-eta). No sharpness or numerical onset claim.

For the selected-pair bridge take real c,D, |D|<=d ell^2 and a separately
paid exterior collar |rho-c|>=a ell, a^2>d. With w=x+iy=rho-c,
r^2=x^2+y^2, delta=d/a^2<1, prove

    q=1/(r^2-D)
       -2y^2(r^2+D)/[(r^2-D)((r^2-D)^2+4D y^2)],
    0<=1/(r^2-D)-q <= C_delta y^2/r^4,
    C_delta=2(1+delta)/(1-delta)^3.

Include both D signs and D=0; show denominator positivity. Sum to obtain

    ell^2 S_R >= ell^2 sum_near 1/(r^2-D) - C_delta Xi_{a,R}(t,c).

Target roots are inside a ell if d<a^2 and absent from Xi at such a
paid pair center. No averaging over selected-pair centers is allowed
without a separately specified conditioning measure and denominator.
Markov gives only exceptional Lebesgue measure <=C T/(a^3 h). A growing
collar is a premise, not an acquired count-two region. At fixed a both
bounds are O(1); no selected-pair o(1), radial lower mass, incoming anchor
or integrated cost follows. Give the direct comparator all inputs. Replay
controls, especially Note34: absence of theta alone does not show failure
of its actual second-moment inequality. Preserve scoped conclusions.

## Outputs, limits and evidence

Write only notes/37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md
and research-progress/handoffs/VCD-GT-E17-r1-return.md under this branch.
One fixed proof route and correction pass; no numeric experiment, new
source family, shared-ledger/history or manuscript edit. Success is
uniform a^-3, matched a^-1 and correct both-sign bridge. Cite result/avoid
indexes, inherited theorem/assessment, authorship and actual/dispatch
provenance. A proof failure returns to B09; E18 assesses separately.

## Frozen input identities

| Repository-relative input | SHA-256 |
| --- | --- |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/brainstorm/notes/17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md` | 2f207ecc12dd3e9c14c06b0bb9be352b5471532c4d90e07e2b29436702df7585 |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md` | d398589c8bae73dad530c8ffd9950fd778a0beabd0782b22a0efb7c37e06b2be |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md` | 2484cb1535de12848598be67ac66db6bb4a5e1f16934d9741d2c6320b679f92e |
| `papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md` | ee94e5c08ee793d927ca5afad7fbc86ddda559f39ec87623051e6f6d9ad4ee68 |
| `papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md` | 1d5b4babf1ddffc0d9ec0ec0c6e2cb6d1aa5eb8cd203bb91b95e7df495d89c66 |
