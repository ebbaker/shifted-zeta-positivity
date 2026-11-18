# E15 r1 — Assessment of the B03 r2 quantitative decision

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Assessor settings are inherited; actual model
and effort are unavailable and are not inferred from the recommended Sol
routing. This assessor supplied neither route's analytical advice and did
not author Note13. This is a separate-agent **internal shared-premise
assessment**, not independent specialist review.

**Accepted within the stated identity, transfer and scoped-screen domains.
No required mathematical correction.** All seven [input pins][pins] match.
The fixed [E15 request][request] was assessed in one pass. No new route,
numerical campaign, canonical estimate or manuscript change was introduced.
[Result index][results] · [Avoid index][avoid] · [Shared-premise rule][shared]

## 1. Joint hierarchy and time normalization

[Note13][note] uses `s_n=ell^(2n)S_n`, `v_n=ell^(2n−1)T_n` and
`d/dsigma=ell² d/dt` with fixed ell. These scales preserve every term in
the accepted fixed-order [Note09][hierarchy] rows. The n=3 row has
`12m s_3+6s_2²+12v_2v_3+12delta s_2s_3−60s_4−72delta s_5`.
Differentiating `F=12s_2+16delta s_3` gives

    F'−8mF=48v_2²+192delta v_2v_3+144delta s_2²
             +192delta²s_2s_3−352s_3−1440delta s_4−1152delta²s_5.

The s_3 coefficient is `−384+32`, the delta s_2² coefficient is
`48+96`, and the delta s_4 coefficient is `−480−960`; the m terms
combine to `8mF`. These checks use the complete accepted moments, not a
newly differentiated finite divisor truncation. Only finitely many fixed
orders occur, so the cited complete passage and merger regularity suffice.

The odd bound follows from
`|w/ell| |mu|^(1/2)≤sqrt(16/15)` and `|mu|≤gamma` before summing.
It gives the displayed `sqrt(q0) gamma^(n−3/2) B_1 L` bound.
The termwise use of these existing bounds produces an `O(L²)` allowance
for the remainder. This does not prove a lower bound for its actual size
and is not a no-go theorem for all joint estimates.

The manuscript defines `W(x,y)=exp(−4 integral_x^y m)`. The integrating
factor for `F'−8mF=R` is `W(x,sigma)²`; division at y gives exactly

    F(y)=W(x,y)^(−2)F(x)+integral_x^y W(u,y)^(−2)R(u)du.

There is no sign reversal in Note13's formula (4). It remains an identity
with an unacquired signed integral and entry value. Direct residues have
the same information, as the note states.

For the finite quartic `P(0,z)=z²(z²+b²)`, the displayed finite heat
exponential has the correct negative spatial-heat sign. Its double target
and simple exterior pair persist as a separated count-two tube locally.
At zero, `s_3=−2/b⁶`, `v_2=0`, so `R=704/b⁶`; adding `8mF` gives
`F'=320/b⁶`. The exterior `±b` instead gives `R=−704/b⁶`. The control
excludes the proposed remainder sign only from finite hierarchy,
conjugation and collar information. Its missing canonical source,
nonzero value at the origin and growing complete population are explicit.

## 2. Gap energy and scalar limitation

Differentiation of `delta'=2−4m delta`, followed by `m'=2m²−F`, gives
`delta''=8m²delta−8m+4Fdelta`. Therefore
`2delta delta''−(delta')²+4=8Fdelta²` holds without dividing by delta.
Its integral has the boundary term `2[delta delta']` and coefficient
`−3` on `integral (delta')²`, as written. Merger values and interval
endpoints require no additional singular operation.

The constant triple `m=−h`, `F=2h²`, `delta=−1/(2h)` solves both scalar
consumer equations. It saturates the weighted integral at `(y−x)/2`
while giving the exact exponential multiplier and inhomogeneous cost in
Note13 (7). The stated d>0 restriction covers the negative constant gap.
The choice `h=sqrt(C_F L/2)` retains the baseline forcing scale for
large L; it is not a full-hierarchy realization. This distinction is
repeated in the note and is essential to the accepted scope.

The warning about unweighting a signed integral is correct even away from
zero: absent a sign for F or a paid negative part, an upper bound with a
variable positive weight cannot be divided by its minimum to bound the
unweighted signed integral. The boundary data also retain m. Finally,
`q'=−2mq` and the Riccati law give `q''=2Fq` and the displayed W ratio;
linearization does not supply a new estimate.

## 3. Deflation, infinite series and the external source

Removing the exact two target occurrences makes G entire in w and
zero-free inside the exterior collar, including at D=0. The complete
genus-one logarithmic product has no contribution from its linear
regularizers after n≥2 derivatives, giving Note13 (8) with its negative
sign and `(n−1)!` denominator. Integer powers have no logarithm-branch
ambiguity in this formula.

The first series in (9) is the binomial expansion of
`w^(−2n)(1−D/w²)^(−n)`. The uniform ratio bound `|D/w²|≤1/16`, the
collar and the complete count bound pay its absolute double sum on the
fixed compact time tube for each n. Combining n=2 and n=3 yields the
coefficient `12(k+1)+8k(k+1)=4(k+1)(2k+3)` in the forcing series.
The geometric-polynomial tail (10) follows by taking absolute values only
in the omitted tail. At D=0, `(n−1)!=6` gives the factor `−2ell⁴` in
(11). This is a convergent representation, not a signed gain.

The time-zero mapping checks against the [framework][framework]:
`s_c−rho=i w_j/2`, so the full first-kind sum is multiplied by `(i/2)^n`
before the target powers are subtracted. For n=2r the target term is
`2D^(−r)`. Retaining the deflated combination is necessary near the
merger. The note correctly conditions this transfer on the tube containing
time zero. Independently, `z=i(2s−1)` gives
`partial_s² Xi_t=−32H_zz` and `partial_t Xi_t=−8H_zz`, hence the heat
factor `1/4` in (13).

I inspected the version-pinned [Voros source][voros], definitions (16)–(19),
the first-kind continuation (20)–(23), its positive-integer log-derivative
formulas and the second-kind setup. They concern zeros of the fixed
completed zeta function and an auxiliary shift. They do not provide the
heat-interval signed estimate asserted missing in Note13. The statement
about that missing transfer is an assessment of these inspected passages,
not a claim that no such theorem can exist. The source's normalization of
its completed function differs by a constant from the manuscript's xi;
the zero set and logarithmic derivatives used here are unaffected.

## 4. Decision, controls and limits

The [controls12][controls] premise replay follows the inherited CM screen:
generic heat identities and local deflation need not fail on colliding
controls. The table instead names absent or unpaid canonical application
premises, without inferring the missing theta bound from those failures.
The new polynomial screen is finite and local; the equilibrium screen is
scalar only; the previously accepted surgery obstruction remains static.
None is promoted to a counterexample to the complete canonical heat field.
[Classification01][classification] · [Scope07][scope] · [Joint12][joint]

The accepted disposition is precisely: **B03 r2 supplies no improved
canonical signed forcing or transport bound.** The joint remainder,
weighted-energy limitation and exact deflated-derivative transfer locate
unpaid quantities; they do not acquire them. The decision not to issue a
numerical E07 or a proof packet for a presently unspecified stronger
estimate follows the frozen scope. This assessment does not close the
canonical dynamics problem or exclude other source-specific inequalities.

[request]: ../research-progress/handoffs/VCD-GT-CM-E15-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E15-inputs-r1.json
[note]: ../notes/13_VCD_GT_CM_B03_JOINT_TRANSPORT_AND_SUPERZETA_20261118.md
[hierarchy]: ../notes/09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[framework]: ../manuscript/sections/01_framework.tex
[voros]: https://arxiv.org/pdf/1403.4558v2
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
