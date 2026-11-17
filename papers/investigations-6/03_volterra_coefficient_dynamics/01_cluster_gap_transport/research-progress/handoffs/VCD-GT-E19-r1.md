# VCD-GT-E19 r1 — exceptional isolated-pair interactions

17 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance. Root actual model/effort unavailable; executor
dispatch gpt-6.1-sol/ultra, serving attestation unavailable. Type E,
following B10's two-option selection recorded in the sole register before
execution. Decision18 preserves the conceptual rationale. Source, domain,
proof route and success tests are fully fixed here; root alone owns shared
registers, integration and history.

## Fixed pair class, packing and visibility

Canonical H_t, 0<=t<=1/2, integer multiplicities, strip width<=1,
T>=16, L=log T, ell=1/L. Fix d>=0, max(2,4sqrt(d))<=a<=L,
3<=R<=T/4. Count distinct unordered conjugation-invariant target pairs
with c∈[T,2T], real |D|<=d ell^2 and every exterior occurrence satisfying
|rho-c|>=a ell. Target positions are within sqrt(d)ell. No collar or pair
population is acquired; this defines the independently paid application class.

Prove distinct eligible pairs cannot share an occurrence; otherwise a
third occurrence lies within 3sqrt(d)ell<aell of the first center.
Then prove center separation at least (a-sqrt(d))ell>=3aell/4.
This pays disjoint intervals I_c=[c-aell/4,c+aell/4] and packing cap
1+4TL/(3a). Include doubles, multiplicities, both D signs and endpoints.

Using Note37's Xi, if Xi_{a,R}(t,c)>=h>0 then throughout I_c

    Xi_{a/2,R+aell/4}(t,X) >= beta h, beta=(4/5)^4.

Each original exterior contribution survives the shifted radial and
horizontal cutoffs and its new distance is at most 5/4 of its old one.
Target contributions are nonnegative. Integrate over the padded band
[T-aell/4,2T+aell/4]. All contributing zeros still lie in[T/2,5T/2].
Do not silently extend Note37's original center band; redo its same
Tonelli calculation using the common enlarged zero-band constants.
For Cs=11pi C_b^(moment)/6 and C0=3pi A as in Note37, obtain

    N{Xi>=h} <= (16 Cs/beta) TL/(a^4 h),
    matched count-only allowance <= (4 C0/beta) TL/(a^2 h).

Also pay the matched pointwise count/strip bound Xi<=C(L/a^2+1/L)
by unit windows and radial cutoff. It already excludes fixed h when
a/sqrt L→infinity. For the polynomial fixed-threshold gain advertise
only a=L^eta with0<eta<1/2; do not count known exclusion as progress.
Note37's C_delta<=8704/3375 converts ell²S_R<=-epsilon into a large-Xi
count, but the sharper signed-sign route below is primary.

## Selected stronger signed estimate: incidence plus source density

Inherit TND-O Note21(7), accepted by its Assessment07, for one fixed
0<b<1/2. Convert three dyadic bands to a common enlarged-band estimate

    N_t(v;[T/2,5T/2]) <= B_b^* TL exp(-bLv), 0<v<1,

with constants independent of t,T,v. Count multiplicities, closed real
endpoints and transverse strict inequality accurately. No b→1/2 limit.
For a negative individual q, prove

    y² > (r²-D)/2 >= (a²-d)ell²/2,
    |y| > (2/3)aell.

A given zero can have negative q for pair centers only within
sqrt(y²+D)<=|y|+aell/4 of its real part. The paid center separation
therefore bounds its number of incident eligible pairs by
5/3+8|y|/(3aell). Negative S_R requires at least one negative q.
Sum incidences over the complete broadband zeros with |y|>v0=2a/(3L),
then use layer cake to prove

    N{S_R<0} <= B_b^* [31/9+8/(3ab)] TL exp(-2ba/3)
               <= C_b' TL exp(-2ba/3).                      (A)

The far groups |x|>R are positive for R>=3, strip<=1 and
|D|<=d/L²<=1/16. Absolute divisor convergence thus gives
N{M<0}<=N{S_R<0}; do not assert the converse. This estimates slice-wise
negative-interaction pairs, not time events, gap signs, or incoming cost.

Give the equally informed direct comparator all density and geometry
inputs; its count-only baseline includes packing and the pointwise
fixed-threshold bound. For a=L^eta,0<eta<1, (A)/(TL) has exponential
rather than power decay in a and needs no fixed negative threshold.
At maximal a=L its stated upper allowance is proportional to
T^(1-2b/3)L and grows; the bound does not force one-exception exclusion.
This concerns the stated allowance, not the true number of exceptions.

## Controls, outputs and finite limits

Preserve Note37's new screen that Note34's opposite-sign fixed-slice
fields satisfy the broad second moment uniformly at time zero. They also
must not be declared to fail the full density inequality merely because
theta differs; any density verdict needs an actual check. No common heat
tube or theta event is supplied by those controls. Run the documentary
control table for all imported inputs and scope each negative statement.

Write only notes/38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
and research-progress/handoffs/VCD-GT-E19-r1-return.md under this branch.
One shared packing plus two fixed downstream estimates and one concrete
correction pass; no new mechanisms, numerical scans, source evaluations,
manuscript/shared-ledger/history edits. Verify pins, cite result/avoid
indexes and predecessor theorem, give proof status and author/model
provenance. A located failed step returns to B10; E18 assesses separately.

## Frozen input identities

| Repository-relative input | SHA-256 |
| --- | --- |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/brainstorm/notes/18_VCD_GT_B10_ISOLATED_PAIR_VISIBILITY_DECISION_20261117.md` | 0e88dcbf430414681687fc71b3d6e73b8113c7178b2921cb155d7a3c3af005fb |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md` | 8b78a4fc25dc8e671238210a61ea359c764427cd72a12f48ae2a38e1723f923b |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md` | d398589c8bae73dad530c8ffd9950fd778a0beabd0782b22a0efb7c37e06b2be |
| `papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md` | 2484cb1535de12848598be67ac66db6bb4a5e1f16934d9741d2c6320b679f92e |
| `papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md` | ee94e5c08ee793d927ca5afad7fbc86ddda559f39ec87623051e6f6d9ad4ee68 |
| `papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md` | 1d5b4babf1ddffc0d9ec0ec0c6e2cb6d1aa5eb8cd203bb91b95e7df495d89c66 |
