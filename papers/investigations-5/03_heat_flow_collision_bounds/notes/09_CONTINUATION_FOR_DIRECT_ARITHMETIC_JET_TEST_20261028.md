# Continuation: a direct arithmetic first-jet test

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.

**Status: continuation prepared; HCB-05 remains open.** This specifies the
next bounded analytical task. It proves no new arithmetic lower bound,
changes no inherited result's status, and launches no computation or chat.
The originating conversation retains its unique Investigation05/chat0016
registration, *Identify equation 2.1 Mellin form*.

## 1. Decision and ownership

Continue **Investigation03, HCB-05**, using Investigation01's complete
arithmetic approximation and Investigation02's existing J specification.
Test a direct joint value-and-derivative estimate before expanding the
whole-cluster P machinery. P remains the main alternative; HCB-02's finite
wall/count results and its unfinished uniform acquisition are preserved.
There is no need for a sixth investigation or another transform.

The motivation is the [portfolio assessment][portfolio]: higher-dimensional
heat geometry supplies faithful representations, but has not supplied the
independent arithmetic estimate needed to exclude collisions. The next
question is whether the actual arithmetic contributions to the field and
its derivative can cancel simultaneously within the complete model error.
Naming that question is not progress on its answer.

Read, in this order:

1. The [result index][results], especially [heat-flow results][r11] and
   [collision controls][controls], and the [avoid index][avoid], especially
   [target classification][a01], [control premises][a02], [scoped failures][a07]
   and [complete signed estimates][a12].
2. [Target J, §§1–2][target], for its normalization, transfer and scope.
3. [Ansatz Note04, CS2–CS7 and CS24][cross] and [Ansatz Note26, RA1–RA5][long],
   for the complete frozen-cutoff model and the distinct time domains.
4. The [HCB register][register] and [Note08][handoff], for acquired results
   and outstanding payments; [04 Review08][review04] for the same bounded
   arithmetic recommendation and the limits of local-energy corrections.

The source approximation statements are recorded as proved in-note from
named inputs, with same-model internal assessment. Their constants/onsets
are finite but uninstantiated. This continuation supplies no independent
validation of that chain.

## 2. Freeze the first test and keep the physical derivative

Use the canonical normalization
\[
H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]
For the **first analytical comparison**, take
\[
L=\log(X/(4\pi)),\quad N=\lfloor\sqrt{X/(4\pi)}\rfloor,
\quad z=X+u/L,\quad |u|\le1,\quad 4\le tL\le8,
\tag{1}
\]
with the buffered core \(|u|\le2\), the upstream fixed complex buffers,
and sufficiently large \(X\) (in particular \(L\ge16\)). This is a
specified asymptotic band, not a selection of numerical sample heights.
It lies in both source theorems and has \(0<t\le1/2\). It is a calibration
for approaching smaller \(tL\), not an assertion of new coverage there.

At each fixed time set \(A_{X,t}=\mathcal E_o(t,X)>0\), constant in \(u\),
and write
\[
f_{X,t}(u)=F_N(t,X+u/L)/A_{X,t},\qquad
V_{X,t}=\left(f_{X,t},\partial_u f_{X,t}\right)
=\frac1{A_{X,t}}\left(F_N,L^{-1}F_{N,z}\right).
\tag{2}
\]
Freeze \(X,L,N,A_{X,t}\) in spatial differentiation. Retain all derivatives
of the arithmetic arms, their carriers, and the completion. A logarithmic
derivative is not interchangeable with the physical derivative through a
zero. If time evolution is used, also retain the derivative of the chosen
time-dependent normalization.

Use the sharper nonnegative-time crossover allowance on (1). After paying
envelope comparability on the buffered chart, the exact normalized jet
differs from (2) by at most \(C X^{-3/4}\). Track the constants separately
before combining the two components. On a later extension to
\(4/L\le t\le1\), Note26 instead supplies the allowance
\((1+\log X)^2X^{-3/4}\), with the stated spatial derivative scales.
Do not carry the sharper allowance beyond its theorem's domain.

The model generally has \(F_{N,t}+F_{N,zz}\ne0\). Direct spatial jet
comparison needs no evolution argument; any use of heat transport must
pay that residual and the needed derivatives. An upper envelope is not a
lower jet margin.

## 3. The actual calculation to attempt

Use precisely Note26's two arms \(P_{+,n},P_{-,n}\) and its completion:
\[
F_N=\sum_{n=1}^{N}(P_{+,n}+P_{-,n})
       +e^{-\pi^2t/64}\mathcal R_N.
\tag{3}
\]
First form the two-component contribution of the **paired \(n=1\) arms**,
then the contribution of every \(2\le n\le N\) and the Riemann–Siegel
completion. Derive their joint dependence on \(u,tL,X\). In particular,
determine whether the paired field and derivative supply complementary
control near a cancellation of the leading field.

The first deliverable is an actual lower estimate for the complete vector
on a stated subrange of (1), or the explicit inequality where the proposed
estimate fails. A triangle comparison of the paired vector against the
complete remainder is a useful baseline. If it loses the margin, identify
the offending modes, derivative contribution or completion payment before
attempting a correlated estimate. In a squared expansion retain all mixed
terms: the positive diagonal alone is not a lower bound. A larger paired
block is permissible only with its full remaining sum accounted for and
the reason for changing the block recorded.

Record the model floor, both approximation errors, constants/onsets, and
the resulting **net exact-field margin**, all on the same domain. Do not
divide by the oscillating field or by \(\mathcal R_N\), either of which
may vanish. If finite evaluation later becomes necessary, specify a
bounded protocol and total cost first; no sweep, extra saddle orders or
new source evaluations are part of this handoff.

## 4. What would count as a useful return

Compare against [Polymath v2, Theorem1.5][polymath]: for \(0<t\le1/2\),
the known exterior real/simple-zero regime starts at sufficiently large
height of size \(\exp(C/t)\). This is precisely the scale on which (1)
must be assessed. The theorem statement was checked on 28 October; the
[existing reference records][references] preserve the limited inspection.
Do not infer a numerical value of \(C\) from an unspecified constant.

Accept one of these bounded outcomes:

- A proved stronger time-height domain, or a useful explicit onset,
  net-margin or complete-cost improvement over a stated comparator.
- A full estimate recovering the classical range, clearly marked as
  calibration, together with the exact new obstacle to extending it.
- A precise failure of the tested decomposition or allowance, identifying
  what correlated information would be needed to improve it.

The second and third outcomes can close this comparison without claiming
new zero exclusion. A known-simple finite sample, a positive diagonal,
or another conditional transfer does not establish the missing arithmetic
bound. If the first test only reproduces the exterior argument and offers
no new estimate, stop that variant; do not broaden its failure to all J
methods. Return to P only with a specific integrated arithmetic quantity
that appears more accessible and an absolute error budget below one event.

## 5. Keep the two eventual applications distinct

The original time-zero HCB-05 target remains
\[
\|(f_{X,0},\partial_u f_{X,0})\|_2\ge cX^{-\beta},
\qquad \beta<3/4.
\tag{4}
\]
This is a strong quantitative arithmetic target, not a consequence known
to follow from qualitative simplicity. With every high chart covered and
the bounded remainder checked, its existing transfer proves **RH implies
simple zeros**. Merely writing (4), or restating nonvanishing of the exact
jet, earns no new result.

An RH-directed positive-threshold argument instead concerns
\(H(T,\cdot)\) for every possible \(T>0\), without assuming RH. It needs
coverage of every possible event height, including the bounded region
left by a fixed-positive-time exterior theorem and its changing size as
\(T\downarrow0\). The first band (1) does not provide this coverage or
settle the threshold argument's remaining hypotheses. A time-zero result
under RH cannot be relabeled as that argument. Nor may the arithmetic
endpoint information in Rodgers–Tao be moved to time \(T\) by a clock shift.

## 6. Controls and the stopping rule

The relevant analytical premise screen is inherited from [cluster12][controls]:

| Control | Premise unavailable to the proposed canonical arithmetic argument |
| --- | --- |
| Euler-factor source | Unchanged canonical arithmetic coefficients and factors |
| Weighted-square source | Full normalized theta reflection; moreover these finite-source controls have no all-real heat time, so their local events are not finite global thresholds |
| Reflected super-Gaussian and positive-primitive sources | The canonical integer-square expansion; reflection and positivity alone do not distinguish them |
| Finite-prime-compatible perturbations | Full reflection and unchanged infinite arithmetic data; selected-prime identities and finite measurements are insufficient |
| RH-conditional close-source endpoint controls | Ordinary Dirichlet-series arithmetic; close sources and preserved completion alone do not force simplicity |

A free heat double also satisfies the generic local collision laws, and
Investigation05's carrier controls retain the relevant generic positivity
on their stated domains. Therefore the proposed gain must use an actual
arithmetic estimate, not just heat geometry or carrier positivity. The
event-domain qualification matters: a valid bound on a collision-free box
of a control need not reject that control elsewhere.

This is a premise screen for the existing strategy, not a successful test
of an unproved inequality; no controls were numerically rerun. Before
claiming a new bound, identify the exact line at which each relevant
control loses a used premise or fails the quantitative estimate. If no
such line exists for a control whose collision is covered, return the
failure instead of adding assumptions that encode the desired conclusion.

## 7. Handoff and records

Save the analytical return in this investigation's `notes/`, any later
numerics in `numerics/`, and review in `reviews/`. Update the sole HCB
register without upgrading HCB-02 or the inherited source proofs. Keep
the complete failed estimate if the bounded test stops. No manuscript
milestone or draft snapshot is created by this planning note.

A fresh research chat should register its own identity in Investigation03.
This conversation stays in [Investigation05's history archive][history];
writing a note here does not relocate or duplicate that registration.

**Suggested opening request:** Continue HCB-05 from Note09. Carry out the
paired-leading-arm comparison against the complete arithmetic and
derivative remainder on the declared \(4\le tL\le8\) band. Retain the
physical derivative, completion and full error payments; compare the
result with Polymath's exterior theorem. Return a quantitative gain,
an explicitly classical calibration with its extension obstacle, or a
precisely scoped failure. Do not begin a numerical sweep.

[portfolio]: ../../reviews/01_PORTFOLIO_ROUTE_ASSESSMENT_20261028.md
[results]: ../../../../result-summaries/README.md
[r11]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[target]: ../../02_heat_flow_rh_applications/rh_simple_zeros/notes/02_TARGET_BOUNDS_FOR_RH_TO_SIMPLICITY_20261026.md
[cross]: ../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[long]: ../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md
[register]: ../research-progress/01_COLLISION_BOUNDS_RESEARCH_PROGRESS_20261026.md
[handoff]: 08_CHAT0001_RESULTS_AND_HANDOFF_20261026.md
[review04]: ../../04_three_regime_heat_flow_dynamics/reviews/08_PROGRESS_ASSESSMENT_AND_NEXT_STEPS_20261027.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1
[references]: ../../04_three_regime_heat_flow_dynamics/references/README.md
[history]: ../../05_radial_theta_collision_geometry/chat-histories/README.md
