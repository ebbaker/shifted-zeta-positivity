# Discussion: finding a useful connection between Jacobi readouts

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are
unavailable in this chat's recorded configurations. Chat0004,
**Find Jacobi readout connections**.

**Discussion and limited reference orientation; no B07 activation or E25
dispatch.** The author asked to discuss the contribution invited in
[synthesis23 §4](23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md)
before continuing research. This note explains possible search targets;
it acquires no canonical slope, phase, contour margin or zero count.
Explanatory deductions below have no separate assessment.

Read the [result index](../../../../result-summaries/README.md),
[cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[avoid index](../../../../avoid/README.md),
[classification01](../../../../avoid/01_restating_the_target.md),
[control pattern02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The [overview](../research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md)
and [live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md)
retain their statuses. The unspecified exhausting shrinking-strip claim
retains the overview's RH-equivalence classification.

## 1. The object a reference must address

At time zero,
\[
 G_N(z)=e_0^{\mathsf T}e^{izJ_N}e_0
       =\sum_{j=1}^N\omega_{j,N}e^{izx_{j,N}},
 \qquad \omega_{j,N}>0,\quad\sum_j\omega_{j,N}=1.
\]
Increasing degree changes both Gauss nodes and weights. The zeros of
\(\det(uI-J_N)=P_N(u)\) are source-coordinate nodes. The zeros of
\(G_N(z)\) are cancellations in Fourier height. A Sturm or
Christoffel–Darboux theorem about the first object requires a new bridge
before it controls the second.

The existing [Gaussian example](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md#4-what-must-be-preserved-to-pass-a-zero-statement-to-the-limit)
has \(G_3(z)=2/3+\cos(\sqrt3z)/3\), with nonreal zeros even though the
Gaussian transform is zero-free. This rejects a generic zero-preservation
inference, not a theta-specific estimate; Gaussian coefficients do not
satisfy the theta logarithmic envelope.

## 2. A degree relation is already present, but does not locate zeros

Subtract B06's two exact error laws. With its \(L_N,E_N\),
\[
 G_{N+1}-G_N
 =L_NE_N-L_{N+1}E_{N+1}
 =L_N\left(E_N+
 \frac{\beta_{N+1}z^2}{(2N+1)(2N+2)}E_{N+1}\right).
\]
This is bookkeeping from the existing law, not a new predictive closure:
the error factors still contain unresolved information. On a common real
interval where the two proved error factors are positive, and \(x\ne0\),
\(G_{2m}(x)<F(x)<G_{2m+1}(x)\) for the corresponding adjacent pair.
Equivalently \(G_{N+1}-G_N\) has strict sign \((-1)^N\).

At any two real zeros of \(G_N\) in this common range,
\(G_{N+1}\) consequently has the same nonzero sign. It cannot have
exactly one simple zero and no other zeros between those endpoints.
Thus ordinary strict interlacing of the consecutive readouts is not the
appropriate automatic consequence of B06. This observation is conditional
on the proved common sign range and the existence of those endpoints;
it does not assert the number or location of canonical readout zeros.

## 3. Two bounded questions to discuss

**Local zero displacement.** Can the canonical source give a quantitative
slope or cluster-separation estimate that makes the known degree
correction small relative to local zero geometry? For orientation, if
\(G_N(r)=0\), \(r\) is real, and on \(|z-r|\le\rho\) one has
\[
 |G_N'(r)|\ge s>0,\quad |G_N''(z)|\le M,\quad
 |G_{N+1}(z)-G_N(z)|\le D,\quad
 D+M\rho^2/2<s\rho,
\]
then comparison with \(G_N'(r)(z-r)\) gives exactly one zero of
\(G_{N+1}\) in the disk by Rouché. Conjugation symmetry makes it real.
This elementary conditional local test is not the missing result. Its
unpaid source-derived ingredient is the quantitative lower slope and
separation relative to the correction, with useful degree/domain
dependence. Multiple-zero clusters would instead need a multiplicity
count; simplicity of all zeros is not assumed or required by the program.
One disk does not exclude additional zeros elsewhere.

**A source-controlled phase system.** Can the complete score
\(V'=-\Phi'/\Phi\), or its exact adjacent identities, yield a relation
for the actual Fourier readouts and a justified companion observable
whose phase has a useful local comparison law? Ladder operators and
canonical systems are possible sources of ideas. The exact readout
identification and all nonlocal residual terms must be retained. E08's
full-score characterization already identifies the source; repeating it
does not supply this phase estimate.

These are search questions, not selected B07 mechanisms. A general theorem
can be useful without mentioning theta, provided its actual hypotheses
can be proved for the unchanged source. A finite local estimate is an
intermediate target, judged by its paid constants and domain. Merely
requiring successful contours on an exhausting family would restore the
unpaid global objective.

## 4. Premise screen for this discussion

The [full catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and synthesis23's family-specific screen were applied as a logical premise
comparison; no numerical certificates were rerun. The local Rouché
statement is generic and can hold near isolated real zeros of controls.
That is consistent with their having nonreal zeros elsewhere. No new
source-specific lower bound has been proposed or tested.

| Control class | What the present discussion establishes or leaves untested |
| --- | --- |
| Weighted-square and E07 finite canonical-score controls | Share the applicable B06 error structure/rate. E07 can preserve a fixed head while having nonreal zeros; their locations are not prescribed. No new local slope or global placement premise is known to fail. |
| E10/E12 smooth compact multipliers | Share the relevant confinement/finite-information premises in their stated classes; complete arithmetic structure fails. Their zero locations remain unestablished. No new slope test has run. |
| Euler-factor translates | The inherited envelope fails in the checked c=1/2, p=23, time-zero example. This does not establish failure of the generic local disk test or cover all parameters. |
| Reflected super-Gaussian | Fails the inherited exponential confinement premise; generic local analytic zero stability remains available. |
| Smooth shape/primitive and finite-prime controls | Their recorded canonical arithmetic/reflection failures remain distinct. No proposed quantitative phase or slope inequality has been evaluated on them. |
| Atomic/finite-profile and triangular extensions | Lack the unchanged positive full-line theta density/score assumptions; their entire Fourier readouts can still satisfy local analytic tests. |
| RH-conditional endpoint constructions | Keep their RH hypothesis and lack ordinary unchanged theta arithmetic. They provide no unconditional canonical phase input. |
| Fixed source with altered readout; actual-profile measure relaxation | Fail the literal readout or full physical-source identification respectively. No new comparison of their quantitative local data is claimed. |

Absence of the canonical formula is not evidence that a proposed derived
inequality fails. A future candidate needs its own actual control
comparison on the stated domain, especially if that domain contains a
known counterexample zero or collision.

## 5. Author contribution and reference disposition

The useful contribution can be recognition of a theorem, analogy or
tractable local relation. The author is not being asked to assume the
missing global zero claim. A candidate can be evaluated by specifying
its functions and variable, hypotheses available from the complete
source, quantitative conclusion, and exact connection to B06's margin
or count.

[Reference05](../references/05_READOUT_PHASE_SEARCH_PASSAGES_20261116.md)
records checked Teschl and Romanov passages, a secondary Dimitrov–Xu
Fourier-Wronskian analogy, and a bibliographic Chen–Ismail lead whose
primary text was inaccessible. These initial checks did not acquire a
theorem connecting successive canonical readouts. No claim about the
absence of such a theorem in the literature is made. B07 remains ready
and unactivated; E25 remains unissued. No manuscript, reviewed milestone,
numerical campaign or result-summary update follows from this discussion.
