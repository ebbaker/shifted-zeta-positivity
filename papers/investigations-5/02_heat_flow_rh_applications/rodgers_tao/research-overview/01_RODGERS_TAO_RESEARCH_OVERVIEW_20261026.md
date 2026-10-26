# Research overview: Rodgers–Tao methods and useful bound requirements

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**.

**Purpose:** systematically investigate which parts of Rodgers–Tao's
argument the new bounds can strengthen, and what additional estimates
would make a positive-threshold contradiction possible. A precise
missing-bound specification is an intended output while the parent
estimates are still developing.

The [initial-results note](../notes/01_INITIAL_RESULTS_AND_BOUND_REQUIREMENTS_20261026.md)
states the mathematical baseline. The
[progress note](../research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md)
alone owns current task status. This overview defines the research
contracts; it does not turn prepared work into completed results.

The first bounded return is now recorded in
[Note02](../notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
(source audit and conditional contour-force transfer). Use the progress
register for its scope and next request. Continuation pointer added
26 October 2026 for Edward Baker with LLM assistance, **gpt-6.1-sol,
actual recorded effort ultra**. The later
[r2 return](../notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md)
acquires actual compact canonical margins and an exterior budget. Its
direct comparator wins on the frozen known-covered pilot; no RH result
or high-height margin is claimed. Current task scopes stay in the progress
register.

## 1. Outcomes and their logical strength

| Outcome | What would count |
| --- | --- |
| Understanding the method | A checked dependency map, including the negative-threshold premise, normalization, all-real/simple-root assumptions, boundary payments, and time-zero arithmetic input |
| Guidance for intermediate bounds | A named consumer, its exact domain/norm, the required inequality or margin, and the parameter dependence currently missing |
| Quantitative improvement | A proved better error, rate, onset, complete margin, covered range, or cost against an explicit baseline on the same data and domain |
| A fixed positive Newman improvement | A complete certificate or theorem yielding a specified smaller positive upper bound; a method pilot on an already covered box is distinct |
| Positive-threshold exclusion | The existing RH-equivalent target: no common real zero of \(H,H_z\) at any positive time. A final-strength aspirational endpoint estimate must be labeled accordingly |
| RH implies simplicity | A separate conditional endpoint result at time zero, coordinated with BW-10 rather than duplicated here |

An effective negative-time witness or a moving-time geometry theorem is
also a useful outcome. No single route is assumed to succeed. A failed
comparison can be useful if it identifies the exact loss and the class
of estimates for which that loss was proved.

## 2. Normalize the problem before comparing estimates

Use \(\partial_tH=-H_{zz}\), \(H(0,z)=\xi((1+iz)/2)/8\),
\(L=\log(X/(4\pi))\), and heat-coordinate spacing \(d_X\sim4\pi/L\).
Keep the microscopic time \(d_X^2\asymp L^{-2}\), the arithmetic
parameter \(tL\), and late time \(t\to\infty\) distinct.
Reserve \(T\) for a possible threshold; write \(R\) for a large-height
parameter when translating the paper's notation.

The initial note records both unordered cluster pair energy and the
paper's ordered, renormalized energy. Every comparison must specify
the reference locations, weights, root labels, finite index interval,
buffers, and whether its boundaries move.

For \(\Lambda<0\), the real-root hypotheses belong to the contradiction
argument. For a hypothetical \(T=\Lambda>0\), they hold at \(t>T\),
but endpoint constants must be examined as \(t\downarrow T\).
For an unconditional bounded pilot, establish the relevant root
configuration independently. A known late-time real interval is useful
for calibration, with that limitation stated.

## 3. Systematic work packages

The following IDs are stable and shared with the progress note.
Dependencies refer to mathematical inputs, not authorization to run
agents, create chats, or send work elsewhere.

| ID | Question and required deliverable | Dependencies / acceptance |
| --- | --- | --- |
| RT-00 | Consolidate initial findings and source status | Opening synthesis only; preserve original notes and identify aspirational statements |
| RT-01 | Audit the corrected proof: list each selected lemma's inputs, outputs, and use of \(\Lambda<0\) | Start from v5 PDF Theorem 11, §7, Propositions 26–28, and §9; no positive-time extension by substitution |
| RT-02 | Choose the exact observable and reconcile normalizations | After RT-01's relevant definitions; write the finite sums, reference gaps, cutoffs, and ordered-pair factors; prove any link to a Book physical quantity |
| RT-03 | Derive field/jet-to-zero, quotient, and first-jet error requirements | RT-02 and current source domains; exhibit the needed lower margins and show how they can be obtained independently of the desired conclusion |
| RT-04 | Bound the exterior drift and localization boundary terms | RT-03; retain \(2U_z/U\), its variation across gaps, the zero tail, and every buffer loss; compare coupled versus separate absolute estimates |
| RT-05 | Assemble one complete localized energy comparison | RT-01–04; match the same energy on both sides, sum all errors, retain slow modes, and show a gain or a precisely scoped unpaid term |
| RT-06 | Compare a finite positive-time consumer with a direct certificate | RT-03 and RT-08; freeze a documented baseline and domain, include core/exterior coverage, and measure total margin or cost |
| RT-07 | Identify a theta-specific endpoint discriminator | RT-02 and the full control screen; name an arithmetic input capable of improving the \(1/s\) collision behavior, or state exactly why a proposed class cannot |
| RT-08 | Audit moving domains, resolution, onsets, and cost | Source inventory plus the chosen consumer; track \(X,t,M\), minimum separation, buffers, regulator widths, mode count, and precision together |
| RT-09 | Return the bound priorities to the parent program | Synthesize each completed comparison into one requirement or gain with evidence; update this register and the parent's eight-target summary |

RT-07 is exploratory and need not wait for all quantitative work to finish.
Any attempt to prove an endpoint inequality must first distinguish it
from a new formulation of the desired conclusion.

## 4. Bounds to ask for, and why

These requirements map to B1–B8 in the
[parent summary](../../summary/CURRENT_SUMMARY.md). The source
[Note 26](../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md)
now reports the high-height positive field contract through zero;
its status and limits are recorded in the initial note. Do not reopen
that domain task merely because the earlier Book review predates it.

| Bound family | Exact question for this investigation | What remains to be learned |
| --- | --- | --- |
| B1: complete small-positive field/jets | On the chosen domain, how small is the complete normalized error compared with the required model margin? | Reported high-height contract available; lower margins, instantiated onsets, finite core, and usable cost still need their own arguments |
| B2: microscopic comparison | At \(x=X+O(M/L)\), \(\lvert\Im z\rvert=O(1/L)\), \(\lvert t\rvert=O(L^{-2})\), what accuracy survives block summation? | Crossover supplies a baseline; stronger negative recurrence at this scale requires a new endpoint/buffer proof |
| B3: lower margins | Can field error pay a contour floor, a first-jet floor, or a simple-root derivative bound? | The lower bound must include arithmetic cancellations and must not presume noncollision |
| B4: exterior interactions | Can \(D(a_i)-D(a_j)\), with \(D=2U_z/U\), be controlled more accurately than separate drifts? | Common motion cancels from gaps; paid derivative/tail estimates and root/block isolation are required |
| B5: complete energy balance | What is the total boundary, arithmetic, approximation, and cutoff allowance for the selected energy? | Error size must be compared with that consumer's scale; no universal exponential relaxation rate is assumed |
| B6: shrinking resolution | Which spatial/regulator widths resolve the chosen observable, and what do their derivatives cost? | A fixed smoothing estimate is not uniform in shrinking widths; a leading resolved collision profile can still be universal |
| B7: RH-conditional endpoint arithmetic | Can a theta-specific estimate beat the \(1/t\) endpoint energy at zero under RH? | Final-strength simplicity target; coordinate with BW-10 and keep it distinct from the positive-threshold question |
| B8: joint effectiveness | What do the full input acquisition, modes, precision, onset, and margin cost together? | Fixed-data extra-accuracy complexity is insufficient for a complete consumer comparison |

RT-07 adds the positive-threshold application of B3–B5: seek an
independently justified arithmetic input that could force
\(sE_W(T+s)\to0\). B7 retains the original RH-conditional simplicity
target. Neither endpoint estimate is presently established.

### Two concrete sensitivity calculations

First, retain the parent's complete first-jet margin test. With
\(|H-F|\le\epsilon_0\), \(|H_z-F_z|\le\epsilon_1\), and a declared
positive length \(\ell\),

\[
 \bigl(|F|^2+\ell^2|F_z|^2\bigr)^{1/2}
 >
 \bigl(\epsilon_0^2+\ell^2\epsilon_1^2\bigr)^{1/2}
\]

excludes a common zero at the tested point. A slab theorem needs
continuous coverage, all propagation/evaluation errors, and an exterior
argument. A positive amplitude normalization may be applied to both
sides. This is a transfer interface, not the missing lower bound.

Second, suppose a positive gap \(g\) is approximated by \(\widehat g\)
with \(|g-\widehat g|\le r<\widehat g\). Direct algebra gives

\[
 |g^{-2}-\widehat g^{-2}|
 \le
 \frac{r(2\widehat g+r)}
      {(\widehat g-r)^2\widehat g^2}.
\]

Thus an \(O(r)\) position allowance becomes an \(O(r/g^3)\) gap-energy
allowance when \(r\ll g\). Near a collision \(g\asymp\sqrt s\),
resolving its leading \(1/s\) energy coefficient requires accuracy
small relative to \(\sqrt s\), before summing pairs. A logarithmically
small mean spacing is not a lower bound for the smallest gap.
The existence of such root enclosures itself needs an independent
margin; the calculation cannot assume the endpoint exclusion.

## 5. A bound requirement must be usable

For each candidate, record:

1. **Consumer and conclusion:** the precise energy term, certificate, or
   local event it controls; whether the target is incremental or final-strength.
2. **Domain and normalization:** height/time range, source, holomorphic
   chart, root configuration, reference gaps, buffers, and input norm.
3. **Complete payment:** analytic and arithmetic errors, lower margins,
   derivatives, exterior terms, localization, and any discretization.
4. **Required size and uniformity:** an explicit inequality after all
   summations; identify dependence on \(M,X,t-T\), cutoffs and resolution.
5. **Baseline and decision:** a matched old bound, the proposed new
   bound, and a measurable gain or the exact term preventing one.
6. **Evidence and controls:** source version, proof/inspection status,
   failed premise on each applicable control, and assessment link when available.

This specification can be completed before the desired bound is proved.
If it reveals that the current field error already suffices, prioritize
the missing margin or structural estimate instead of requesting
unnecessary extra approximation orders.

## 6. First sequence and decision points

Begin with RT-01's bounded audit of the corrected propagation step,
together with the observable definitions in RT-02. Then derive one
RT-03/RT-04 requirement using the actual available field contract.
Only after this comparison choose a numerical consumer or a broader
energy calculation.

For the positive-threshold aim, ask whether the proposed estimate sees
an individual finite event. If it only improves bulk regularity, retain
that useful result with its scope and identify the additional localization
step. For a threshold limit, expose any constant depending on a minimum
gap or lower time cutoff before attempting to let that cutoff vanish.

A fixed-slab pilot can succeed without lowering the global Newman bound.
An improved global bound requires complete finite and exterior coverage.
The parent's published \(0.2\) benchmark is not a current-record claim.
Do not infer descent to zero from finitely many positive improvements.

Use the
[BW-10 simplicity work](../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/README.md)
for its existing root-motion and endpoint-control arguments. Its endpoint
is \(T=0\) under RH, while this branch primarily studies hypothetical
\(T>0\). Preserve that distinction.

## 7. Controls, evidence, and maintenance

Apply the initial note's full control screen before claiming an exclusion.
The generic heat identities and transfer inequalities should hold on
controls within their stated domains. An exclusion premise must fail at
their collision, with the actual failed inequality identified. Retain
the distinctions between a local collision and a finite all-real threshold,
and between failure of the full theta identity and failure of a derived
bound.

The [result index](../../../../../result-summaries/README.md), especially
[11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md),
govern interpretation.

Save derivations in notes, assessments in reviews, and any necessary
computation in numerics. Update the progress note with the evidence and
next question; update the parent summary with the result's practical
implication. Keep the approximation proofs and their live task statuses
in their existing parent homes. Neither this plan nor same-model
checking provides independent specialist validation.
