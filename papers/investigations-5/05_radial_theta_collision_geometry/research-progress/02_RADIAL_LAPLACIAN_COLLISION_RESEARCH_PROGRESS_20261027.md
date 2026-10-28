# Radial Laplacian collision research progress

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0004, **Explore 3D Laplacian collision rules**.

**Current priority.** This is the authoritative register for the new RLC program in the [overview][overview]. It supersedes the earlier [RTC register][old-progress] for selecting and reporting current work. The old register remains the historical source for its tasks and results; no earlier completion is erased or counted again. [The handoff][handoff] is the current continuation entry point.

**Current mathematical position.** [Note16][n16] completes the first bounded RLC-01/RLC-02 comparison. It proves complete canonical flux/shell/tail bounds and the necessary collision restriction a^4 P4(t)>24 P0(t), with an explicit conservative bounded range free of simultaneous zeros. The matched direct-u proof has the same constants and tails; separately majorizing the boundary and flux integral enlarges the nonnegative-remainder allowance. No improvement over previously covered theta regions or over the matched direct estimate, global collision exclusion, Newman bound or all-height endpoint-simplicity result is established. Broad RLC-01/02 remain open. Analytic results lead; no new numerics were needed.

**Further exploration.** [Note17][n17] constructs a family of forced radial Darboux equations with exactly the same H and spectral multiplicities, including an invariant integral and full time/forcing terms. Its complete energy identity transports the existing cancellation; no stronger estimate or new exclusion range is acquired. This is an exploratory RLC-04 input, separately assessed in [Review10][r10].

Latest research: 27 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0006 **Review radial collision progress**.

## Task ledger

The overview defines each task's full proof contract. Status words here describe work actually recorded, not the hoped-for output.

| ID | Current status | Available input | Required next output | Dependency |
| --- | --- | --- | --- | --- |
| RLC-01 | First bounded return complete; broader source estimates open | Note16, Sections 2–3 and 5: complete square-mode remainder, arbitrary finite time slab, shell correlation, joint weighted tails and boundary transfer | A different source correlation or demonstrated acquisition-cost gain if pursuing radial improvement | Common source input acquired for this return |
| RLC-02 | First bounded return complete; theta-specific improvement open | Note16: coupled fourth-moment restriction, explicit bounded exclusion, exact direct equality and separate-flux loss | Decide the actual moment-radius comparison on a declared time slab, or choose a new theta-specific estimate | RLC-01; RLC-03 only for an identified consumer |
| RLC-03 | Conditional support; no localized consumer selected | Note14 radial Hardy identity and short-annulus constant | One complete localized estimate with forcing, cutoff and interface costs; gain or scoped failure | A specified RLC-02 or RLC-04 consumer |
| RLC-04 | Exact deformation family recorded; stronger collision estimate open | Note01 forced system/control; Note05 source system; Note17 radial Darboux family preserving H and complete energy comparison | One stronger complete estimate in the transformed system, or another source-dependent event restriction | Common source setup; may proceed independently of success in RLC-02 |
| RLC-05 | Deferred; no characteristic candidate constructed | Note01 source-coefficient/spectral distinction; earlier transfer obstructions | Explicit operator, domain, homogeneous boundary map and nonvanishing observation factor, or candidate-specific obstruction | A concrete construction from source data |
| RLC-06 | Bounded multiplicity scope recorded; global transfer open | Note16 excludes all multiplicities at least two in its explicit bounded range | Cover the actual remaining heights and times before any threshold or all-height simplicity application | Further RLC-02, RLC-04 or RLC-05 coverage |
| RLC-07 | First-return analytic/control assessment recorded; ongoing | Review09 and same-model subagent checks; exact Gaussian-polynomial control passes the restriction | Preserve scoped conclusions and assess each new analytic return; no numerical campaign needed for this return | Accompanies all tasks |

Priority order: the first bounded RLC-01/RLC-02 comparison is recorded below. Continue only with a distinct analytic question; the coordinate-only shell variant and separate-absolute-value flux variant are stopped at their proved scopes. Use RLC-03 only to answer an identified estimate question. RLC-04 is the main structural alternative, not a reward unlocked only by a successful shell argument. RLC-05 remains exploratory until its candidate exists. RLC-06 assembles actual results and cannot fill missing estimates by extrapolation.

## Inherited results and their limits

| Item | Recorded source and status | Permitted use | Remaining limitation |
| --- | --- | --- | --- |
| Radial theta, Kelvin symmetry and normalized evolved potential | [Note01][n01], exact in-note analysis; historical RTC-01 | Fix Q_t, T_t, M_t, origin charge and exterior observation | No collision sign follows from this geometry alone |
| Forced boundary system and Wronskian | Note01, exact in-note analysis; historical RTC-02 | Use B=-8H and the complete norm-plus-forcing identity | Still inhomogeneous; positive source/response can collide |
| Circle transfer obstruction | [Note03][n03], proved in-note with same-assistant checking | Retain nonzero commutator and physical point-observation costs | It excludes the tested transfer, not all nonlinear or nonlocal mechanisms |
| Gaussian deformation and event transport | [Note04][n04], exact transport and a scoped control | Preserve full physical boundary accounting and all finite multiplicities | Positive changed-source endpoint does not force zero original degree |
| Nonlinear canonical source and modular multiplier test | [Note05][n05], exact source system and scoped canonical sign obstruction | Source equations may enter new coupled estimates | Finite source variables do not close physical spectral jets; the tested scalar multiplier is not a sign mechanism |
| Positive tail flux and positive-time correction | [Note14][n14], direct same-assistant derivations | S_0 positive Gaussian sum; S_t includes its full time correction | No independent review or strict observation margin recorded |
| Joint shell observation and radial energy identity | Note14, direct same-assistant derivations | Form an analytic comparison; retain the inverse-square term and endpoint conditions | Generic shell convexity and local coercivity alone do not distinguish theta from colliding controls |

Notes06–12 and their seven historical RTC-03 returns remain valid at their stated representation and obstruction scopes. They are background, not default next tasks. This register does not reopen the tested bounded collision-energy correction in the sibling investigation.

## Setup scope before the first return

The following records the program setup. Current acquired results and next work are in the first-return record below.

- S_t(r)=integral_r^infinity s^2 Q_t(s) ds is positive and decreasing for real t. In Note14's explicit time formula, both displayed terms are nonnegative for t>=0 and r>=1, the first is strictly positive, and the correction vanishes at t=0. This sign assertion is not made for all negative times or for radii below one.
- Q_t evolves by multiplication by log^2 r/4. The potential has the time-dependent charge M_t=16H(t,i). The boundary relation is 2S_t(1)=T_t(1); S_t(1) is not the full charge M_t.
- The joint observation uses the complete exterior integral. The inversion-related interior is not an additional copy to be added to it.
- The mode's inverse-square coefficient exceeds the radial Hardy threshold for a!=0. The positive annular constant pi^2/L^2-a^2/4 requires the stated Dirichlet test class, not the unrestricted physical response.
- The first analytic comparison has no chosen numerical rectangle, shell partition, cutoff, source truncation or precision. Its domain is to be specified symbolically before any numerical support is requested.
- No improved two-observation bound, source-sensitive event identity, homogeneous characteristic determinant, effective all-height cutoff or t-down-to-zero transfer has been acquired by this program setup.

## First bounded return: contract and completed record

**Work package: RLC-01 into RLC-02.** Read the current handoff and use the exact formulas from Note14 without treating their rederivation as a new result. Choose a symbolic compact time-frequency domain and one complete flux-based estimate for the pair (H,H_a). Derive the canonical shell/tail information and the observation transfer analytically, then compare the resulting allowance with direct u integration under the same information and domain.

The return must contain:

1. The proposition being attempted and the domain on which it is intended to hold.
2. The full derivation, including the r=1 contribution, the outer tail and the time-weight correction.
3. The actual source-dependent inequality or the exact obstruction to obtaining it by the selected method.
4. The matched direct comparison, with any gain or loss quantified analytically where possible.
5. The relevant control test and the premise distinguishing theta, if one is used; a generic identity shared by controls must remain compatible with their events.
6. A concise assessment separating proof, inherited input, finite algebra, certified constants, exploratory values and unresolved obligations.

An analytic source-balance restriction or an explicit failed-estimate comparison can complete this bounded return without excluding a collision. Merely specifying a convex enclosure, a positive energy, an unevaluated sufficient criterion or a numerical sampling plan cannot.

### Completed record — chat0005

27 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, chat0005 **Begin radial collision research**.

[Note16][n16] and [Review09][r09] are the deliverables. The domain is 0<=t<=T<infinity and 0<a_-<=a<=A<infinity, selected symbolically. The proof covers the entire integer-square sum and positive time correction; no numerical shell partition, precision or sampled rectangle was selected.

- **Acquired source input:** explicit Gaussian remainder bounds for the complete source or an omitted square tail; flux and shell differences retaining shared endpoints; weighted tails for both observations; correct r=1 boundary and uniform differentiation justifications.
- **Acquired restriction:** for Pj(t)=integral u^j exp(tu^2)Phi(u)du, every simultaneous zero requires a^4 P4(t)>24 P0(t). Since P4/P0 increases with time, no simultaneous zero occurs for 0<=t<=T and 0<a<=(24 P0(T)/P4(T))^(1/4). Note16 also specifies positive constants L0 and U4(T) giving the entirely explicit conservative range a^4<=24 L0/U4(T). This covers all multiplicities at least two in that bounded range only.
- **Matched comparison:** changing to u gives the identical projection, moments and tail allowance. For a nonnegative omitted source, the separate flux allowance exceeds the direct absolute allowance by exactly 2 integral over {phi phi'<0} E abs(phi'). The loss is strict for omitted canonical modes and a nonzero direction at a>0. No radial margin or evaluation-cost gain is established.
- **Control and review:** the Gaussian-polynomial collision has a^4 P4/P0=123>24, so it passes. Other controls are screened by their actual premises. Derivations and constants received separate same-model internal checks; no specialist review or new interval certificate is claimed.
- **Remaining condition:** improvement over the ordinary second-moment positivity radius occurs precisely when P0(T)P4(T)<6 P2(T)^2. This canonical comparison remains unproved here. The coarse explicit range is not claimed to enlarge existing coverage. Global heights, threshold transfer and all-height t=0 simplicity remain open.

**Decision:** record one bounded RLC return without marking either broad task complete. Stop the same-information coordinate rewrite and the separate absolute flux implementation as routes to a better allowance. A next bounded task can prove or disprove the actual moment comparison on a declared time slab before numerical evaluation. RLC-04 remains available for a distinct theta-specific event-conditioned relation. RLC-03 and RLC-05 received no new result; RLC-06 has no global transfer input. No manuscript milestone or new snapshot is created.

## Rules for supporting numerics

No numerical campaign is currently justified by an identified analytic consumer. A later calculation is appropriate only after a written analytic task specifies what uncertainty it resolves. Typical uses are an exact algebra check, a control replay, or an interval enclosure of an explicit finite constant in a derived theorem. A bounded diagnostic may help reject a candidate, but does not prove a sign for unsampled parameters.

Record the computation's hypothesis, domain, error sources and consumer in the same research return. A larger grid, higher precision or more checks are not independent evidence for an RH-equivalent statement. A fully validated finite constant remains supporting evidence for its particular analytic estimate, not a substitute for the proof's uniformity and transfer.

## Relation to the previous task register

| Previous work | Treatment in the RLC program |
| --- | --- |
| RTC-01 and RTC-02 | Retained foundations for RLC-01 and RLC-04; not counted as new completions |
| RTC-03 radial and source relations | Reused where they inform RLC-01/04; lattice-kernel optimization is lower priority |
| RTC-04 characteristic question | Continued at the explicit-candidate scope of RLC-05 |
| RTC-05 global index question | Retained only when RLC-06 has complete boundary information; the Gaussian inference stays stopped at its stated scope |
| RTC-06 signed estimates | Made concrete in RLC-01/02, with RLC-03 as targeted support |
| RTC-07 multiplicity and range transfer | Carried into RLC-06 without inheriting an exclusion that was never proved |
| RTC-08 review and provenance | Continued through RLC-07 |

## How to update this register

Update the relevant row only after saving its actual deliverable. Record the date, source path, hypotheses and domain, proved gain or scoped obstruction, verification status and next unresolved condition. Link to detailed notes rather than accumulating derivations here. Do not mark a broad task complete because one attempted estimate failed; name the closed variant and the remaining class.

Keep [result summaries][results] and [avoid patterns][avoid] aligned at an actual research closeout or manuscript milestone, preserving the sources' status words. The [collision-control register][controls] governs premise screening. The historical RTC files and chat registrations remain unchanged. Do not create snapshots or claim independent review from same-assistant checks.

## Update log

27 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0006 **Review radial collision progress**. User-proposed deformation direction made concrete in [Note17][n17], with [same-assistant assessment][r10]. An added radial potential and transformed source preserve the exact physical observation, all positive-frequency multiplicities and an explicit integral. The ordinary complete energy identity supplies no further event condition. This records an exploratory RLC-04 construction; it does not close that task or change the bounded exclusion of Note16. No numerical work or manuscript milestone.

27 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, chat0005 **Begin radial collision research**. First bounded RLC-01/RLC-02 analytic return saved in [Note16][n16], with [assessment][r09], explicit source-balance restriction, and exact direct comparison. No numerics were needed. Chat0005 is registered uniquely in this investigation; current capture metadata remain in the registry.

27 October 2026 — program established at Edward Baker's request in chat0004. New overview, progress register, handoff and current-program entry were created as separate files, reusing relevant earlier definitions and results. The new program takes research priority, with analytic results leading and numerical work supporting. Previous program documents remain intact. No new mathematical return, manuscript milestone, computation or collision exclusion is recorded by this setup. Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra, actual recorded effort max.

The [setup and chat-history verification record][verification] documents file preservation, navigation and the archive verification snapshot. It assesses this documentation change, not the validity of all inherited mathematical arguments. Current chat capture counts and hashes remain authoritative in the [registry][history-index].

[overview]: ../research-overview/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_OVERVIEW_20261027.md
[handoff]: ../notes/15_RADIAL_LAPLACIAN_COLLISION_PROGRAM_HANDOFF_20261027.md
[old-progress]: 01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[n01]: ../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n03]: ../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[n04]: ../notes/04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[n05]: ../notes/05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[n14]: ../notes/14_RADIAL_FLUX_AND_COLLISION_RESTRICTIONS_BRAINSTORM_20261027.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[verification]: ../reviews/08_RADIAL_PROGRAM_SETUP_AND_HISTORY_VERIFICATION_20261027.md
[history-index]: ../chat-histories/index.json

[n16]: ../notes/16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[r09]: ../reviews/09_FLUX_MOMENT_AND_DIRECT_COMPARISON_ASSESSMENT_20261027.md
[n17]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[r10]: ../reviews/10_RADIAL_DARBOUX_DEFORMATION_SELF_ASSESSMENT_20261027.md
