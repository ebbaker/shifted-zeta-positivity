# Hamiltonian auxiliary dynamics and collision constraints

8 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual recorded model and effort are unavailable in the current chat. This is the author-requested TND-A-E06 priority and documentation renewal; it adds no mathematical result.

## 1. The question this branch should answer

**Can the Hamiltonian auxiliary construction make an independent estimate
about the canonical Newman field easier to obtain, and can that estimate
constrain a specified collision?** This is now the leading research
question. A useful first result may restrict an event's location, a
pair's lifetime or an explicitly bounded region. It need not settle
global realness.

Three accomplishments must remain distinct:

| Accomplishment | What it provides | What a collision application still needs |
| --- | --- | --- |
| Physical response representation | A precise supplied-apparatus model whose calibrated observation recovers H | An additional inequality about the canonical field |
| Recovery or acquisition diagnostic | The accuracy or cost of obtaining a field value and its derivatives | Acquired information strong enough to give a positive margin |
| Collision constraint | A source-derived estimate with a stated consequence for an event | Only the further coverage, time or multiplicity extensions explicitly claimed |

The accepted representation remains valuable at its original scope.
The pending recovery diagnostic remains available as supporting work.
Neither should be the automatic next step merely because its formula is
tractable. The next conceptual task chooses the estimating job first.

The author's generalized-marginal program remains a separate, high-risk
avenue in [localized zero correlations](../../03_operator_imaginary_time_evolution/02_localized_zero_correlations/README.md).
This auxiliary branch does not depend on its success, and it does not
require that project to produce an immediate collision theorem. The
[recent program-fit diagnosis](../../03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md)
motivates this distinction. Revision of the operator program is deferred
until the author incorporates the parallel direct-branch brainstorm.

## 2. What has actually been established

The fixed complete cylinder construction uses
\[
C=\mathbb R_v\times S^2_{1/2},\qquad
A=D^2,\qquad L_0=-\partial_v^2+4A.
\]
All angular shells, both Dirac signs and the continuous radial spectrum
are retained. The prepared amplitude contains the complete canonical
source \(F_\lambda(v)=e^{\lambda v^2}\Phi(v)\), with a supplied calibrated
angular reference bank. Auxiliary proper-time heat acts on the left:
\[
S_{\lambda,\tau}=e^{-\tau L_0}S_{\lambda,0},\qquad \tau\ge0.
\]

The [E01 proof, §§6–8](../notes/01_TND_A_E01_R1_COMPLETE_SPECTRUM_RESPONSE_20261106.md)
and [E02 assessment, §§5–6](../reviews/01_TND_A_E02_REALIZATION_ASSESSMENT_20261106.md)
establish, within their supplied-apparatus scope,
\[
\mathcal O_{\lambda,\tau}(z)=m_\tau(z)H_\lambda(z),\qquad
m_\tau(z)=q(\tau)e^{-\tau z^2},\qquad
q(\tau)=\frac{Q_1(\pi+4\tau)}{Q_1(\pi)}>0,
\quad Q_1(\beta)=\sum_{n\ge1}e^{-\beta n^2}.
\tag{1}
\]
E02 accepted all six obligations without a required correction. Its
assessment was internal, in the proof-author chat/model, with shared
premises; it was not independent specialist verification.

For every fixed admitted \(\tau\), the multiplier in (1) is nonvanishing.
The response has exactly H's zeros and multiplicities. Varying this
auxiliary time at fixed lambda therefore does not move those zeros.
Their collisions as lambda varies are preserved as well. Equivalently,
the extra term in \(\log|\mathcal O|=\log|H|+\log|m_\tau|\) is harmonic
in z, so it makes no contribution to the zero measure. Any zero-position
marginal with the same observation convention is consequently unchanged
by this particular auxiliary heat evolution.

The equations for the two parameters also differ:
\[
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda,\qquad
\partial_\lambda\mathcal O_{\lambda,\tau}
=-(\partial_z+2\tau z)^2\mathcal O_{\lambda,\tau},
\qquad
\partial_\tau\mathcal O=(q'/q-z^2)\mathcal O.
\tag{2}
\]
Newman time lambda, auxiliary Euclidean time tau and unitary laboratory
time are distinct. No clock identification is part of the result.

The calibrated source placement, its complete arithmetic scan, passive
reference bank, absolute gains and phase-sensitive readout are supplied
premises. The free Hamiltonian does not itself derive them. An intrinsic
source-preparation or laboratory theorem would be another objective.

## 3. Where theta and the primitive enter

The arithmetic is already present in the prepared amplitude. On the
half-line,
\[
p(u)=e^uQ_1(\pi e^{4u})
=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad
\Phi=(p''-p)/8,\quad p'(0)=-\tfrac12,
\]
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du.
\tag{3}
\]
With \(\mathcal P_\lambda(z)=\int_0^\infty
p(u)e^{\lambda u^2}\cos(zu)\,du\), the inherited primitive identity is
\[
8H_\lambda=\tfrac12+(2\lambda-1-z^2)\mathcal P_\lambda
+4\lambda z\mathcal P_\lambda'-4\lambda^2\mathcal P_\lambda''.
\tag{4}
\]
See the [parent source construction](../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md)
and the [operator primitive derivation, §3](../../03_operator_imaginary_time_evolution/notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md).
Their existing evidence levels are retained.

The operational chain is therefore: complete arithmetic source;
supplied state preparation; auxiliary evolution; calibrated observation;
recovery or estimation of H. Equation (1) completes the representation
part of this chain. An estimate must still exploit the unchanged theta
coefficients or another independently justified property strong enough
to constrain the signed oscillatory transform. Positivity of p,
positivity of the Hamiltonian and decay of the auxiliary norm do not
themselves prevent H and H' from vanishing together.

The integers in a source expansion, the physical angular channels,
reference columns and zero positions have different roles. No zero
correlation law follows simply by interpreting one of these indices
probabilistically.

## 4. A concrete collision consumer and its missing input

For a real collision at \((\lambda_*,k_*)\),
\[
H_{\lambda_*}(k_*)=H'_{\lambda_*}(k_*)=0.
\]
Fix derivative units \(s>0\) and define the value-and-derivative pair
\[
X_\lambda(k)=\binom{H_\lambda(k)}{sH_\lambda'(k)}.
\]
On a stated compact real parameter domain \(\mathcal D\), a validated
approximation and error bound would give the elementary implication
\[
\|X-\widehat X\|_2\le\eta,\qquad
\inf_{\mathcal D}\bigl(\|\widehat X\|_2-\eta\bigr)>0
\quad\Longrightarrow\quad
\text{no real multiple zero in }\mathcal D.
\tag{5}
\]
The bound must hold throughout the region; values at isolated probes do
not establish the infimum. This is a finite-region verification consumer,
not a new estimate or an RH claim. Saying merely that the exact pair is
nonzero restates the finite target. The substantive work is to acquire
and compare the two sides with complete errors.

An alternative consumer may bound a collision-conditioned jet, the
influence of exterior zeros, or a time-integrated approach to a pair.
Such an intermediate estimate can be useful without directly proving
(5). Its implication, event class and time/height range must be stated
before selecting an auxiliary equation.

The existing [B02 decision](../brainstorm/notes/02_TND_A_B02_FIRST_JET_CONDITIONING_DECISION_20261106.md)
and [E03 request](../research-progress/handoffs/07_TND_A_E03_R1_FROZEN_REQUEST_20261106.md)
address only the recovery error in this interface. The exact pair map is
\[
Y=\binom{\mathcal O}{s\partial_k\mathcal O}
=m_\tau(k)
\begin{pmatrix}1&0\\-2s\tau k&1\end{pmatrix}X.
\tag{6}
\]
E03 is to prove sharp inverse-error constants for the specified additive
error class on a finite real window. It has not been executed. Even a
completed sharp inverse norm would need an independently acquired error
radius and a favorable canonical value to make (5) positive.

Matched source uncertainty must remain matched: the exact forward image
and inverse return the same uncertainty set. Covariant post-processing
changes its shape and correlations, not the information by itself.
A practical advantage requires a new justified acquisition/error model
or lower complete cost at the same accuracy. The scalar inverse
amplification \(e^{\tau k^2}/q(\tau)\) is already known to be unbounded
as real |k| grows for fixed positive tau.

## 5. The next conceptual choice

**TND-A-B03** asks for one collision-relevant target and compares at most
two ways the auxiliary branch could contribute:

1. **Use additional canonical information within the accepted model.**
   Identify a coupled source estimate, localized form or acquisition
   advantage with a specified consequence for H. Compare it with direct
   analysis using exactly the same source information, error correlations,
   units and complete costs. A useful direct bound may be the outcome;
   credit it without attributing a gain to the multiplier.
2. **Propose at most one controlled auxiliary extension.**
   Explain what independent estimate a modification of the preparation,
   observation or dynamics might make accessible, and how it transfers
   back to the original canonical H. Specify the changed premise and
   mathematical domain. A nontrivial deformation is not itself a collision
   bound; avoiding collisions on an auxiliary slice does not settle the
   physical slice.

No extension is selected by this overview. A changed physical construction
requires a new B01 revision before any dependent execution; B01 r1 and its
accepted result remain intact. A new estimate is not required before the
brainstorm can begin, but a plausible route and explicit transfer are
required before issuing a substantial execution task.

The [earlier auxiliary-flow lessons](../../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md)
must inform this choice: generic response, visible splitting and
positivity after discarding cancellation were insufficient in the tested
classes. Those scoped failures do not exclude other complete-source
estimates or controlled deformations. Do not repeat their tests merely
under Hamiltonian notation.

The [Green branch](../../03_operator_imaginary_time_evolution/01_green_potential_resolvent/README.md)
and [collision-constraint alternatives](../../03_operator_imaginary_time_evolution/03_collision_constraints/README.md)
are useful comparators. They keep their own tasks. This branch's distinctive
question is what the Hamiltonian auxiliary construction contributes.
The forthcoming operator brainstorm is neither presumed complete nor a
blocking prerequisite for this documentation.

## 6. Evidence and the control screen

Read the [result index](../../../../../result-summaries/README.md), especially
[theta14](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md), especially
[classification01](../../../../../avoid/01_restating_the_target.md),
[premise02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [volume20](../../../../../avoid/20_volume_without_a_gain.md).

The following is the inherited premise-level planning screen, not a new
collision computation:

| Control | Shared mechanism and failed canonical premise |
| --- | --- |
| Euler-factor sources | Applicable smooth source/Fourier/heat response survives; unchanged canonical theta arithmetic fails. A nonvanishing multiplier preserves their collisions. |
| Weighted-square / finite-prime sources | The pair-map algebra survives where the transforms exist; full unit weights or full normalized reflection fail as specified by each source. Finitely matched endpoints do not supply the complete canonical field. |
| Reflected super-Gaussian / smooth positive-primitive sources | Applicable positivity, reflection, regularity and response operations survive; the complete integer-square theta expansion fails. Generic energy positivity cannot separate them. |
| Atomic / finite-profile controls | Finite moments and algebraic observations can survive; smooth prepared-state and full operator-domain premises need not. No full realization is asserted for these controls. |

A new exclusion estimate must fail on a relevant colliding control when
applied to a domain containing its witness, or name the specific premise
that control lacks. A finite collision-free box of a control need not be
rejected. Naming canonical arithmetic without estimating it supplies no
separating inequality.

The [new plan](../research-plan/02_TND_A_COLLISION_PRIORITIES_RESEARCH_PLAN_20261108.md)
bounds the next work. The
[new sole register](../research-progress/02_TND_A_COLLISION_PRIORITIES_RESEARCH_PROGRESS_20261108.md)
owns TND-A status. The [previous overview](01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_OVERVIEW_20261105.md)
and the existing manuscript preserve the full physical background;
[reference-use06](../references/06_TND_A_E06_PRIORITY_RENEWAL_SOURCE_USE_20261108.md)
maps the inputs used here. No manuscript expansion or source-status
promotion accompanies this priority change.
