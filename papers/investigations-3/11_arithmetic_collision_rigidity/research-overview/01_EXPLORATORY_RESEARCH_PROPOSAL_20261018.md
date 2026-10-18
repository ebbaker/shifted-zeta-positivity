# 11: Arithmetic constraints at collision scale — exploratory research proposal

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

**Status update, 18 October 2026:** the opening round is complete, with
[exact packet matching](../notes/02_COMPLETE_PACKET_MATCHING_CODEX_20261018.md)
and a [scoped finite-prime control theorem](../notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md).
The [self-review](../reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md)
records its limits. The continuation proves [positive arithmetic packets, uniform relative bounds and a bounded carrier energy payment](../notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md), with a [second self-review](../reviews/02_POSITIVE_PACKET_AND_MODULAR_CANCELLATION_SELF_REVIEW_CODEX_20261018.md). The complete signed theta residual estimate remains open. The [self-contained working manuscript](../manuscript/README.md) now consolidates the results and their background, with [same-assistant manuscript review](../reviews/03_MANUSCRIPT_SELF_REVIEW_CODEX_20261018.md). The initial exploratory proposal is retained below.

**Execution-plan successor:** [Updated overview and Sol plan](02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md)
now controls future work. The proposal below is retained as historical
context. Successor added with LLM assistance, **gpt-6-astra, ultra**.

## Central question

The current task establishes the proposal and its scope before the research round.
The directory name records a hoped-for rigidity mechanism. No arithmetic
rigidity theorem is presently claimed.

Can a hypothetical collision of the fixed theta heat transform force a
restriction on complete nonlocal arithmetic data that can be proved
independently of the collision criterion? The local germ alone is universal.
The proposed new information must come from matching that germ to the global
modular and coefficient relations of the same source.

The proposal has two tasks: derive a correct matching formula,
then prove an arithmetic restriction on the exterior term it exposes. The
first makes the problem precise. Only the second, or a meaningful scoped
obstruction to it, would give the intended structural advance.

## A deliberately narrow opening event

Begin conditionally with one real event \((T,x_*)\), \(T>0\), satisfying

\[
H(T,x_*)=H_x(T,x_*)=0,\qquad
c=\tfrac12H_{xx}(T,x_*)\ne0,
\qquad H_t=-H_{xx}.
\]

This is an exact double collision. Write \(s=T-t\) and
\(x=x_*+\sqrt{s}\,y\). The known local heat expansion gives, on bounded
\(y\)-sets,

\[
\frac{H(T-s,x_*+\sqrt{s}\,y)}{cs}\longrightarrow y^2+2,
\qquad
\frac{H_x(T-s,x_*+\sqrt{s}\,y)}{c\sqrt{s}}
\longrightarrow 2y.
\]

These are specializations of the established [local collision laws][s13],
not new conclusions. The stationary predecessor is
\(x=x_{\rm stat}(s)=x_*+O(s)\), defined by \(H_x=0\); it need not be the
vertical line \(x=x_*\). The existing ratio on that branch is
\(\mathcal L_0/E=-1/s+O(1)\).

An opening uniform statement may restrict \(T\) to a compact interval
\([T_-,T_+]\subset(0,\infty)\) and \(x_*\) to a bounded interval. Compactness
alone does not control division by \(c\). Record either event-dependent
constants or explicit lower bounds for \(|c|\) and bounds for the normalized
higher derivatives. Such assumptions are part of a restricted theorem;
they cannot silently be extended to every possible theta event. Higher
multiplicity and \(T\downarrow0\) remain later extension problems.

## First global relation: the complete d=2 packet

Use the [exact half-line relation][packets] with \(a=\tfrac12\log2\):

\[
\mathcal P_2(t,z)=2^{-1/2}e^{ta^2-iza}
\bigl[F(t,z+2ita)-L_2(t,z)\bigr].
\]

Here \(F(t,z)=\int_0^\infty e^{tu^2+izu}\Phi(u)\,du\), and \(L_2\) is
the entire lower-interval integral from the packet note, with its shifted
frequency. The change-of-variable formula is generic. Its identification
with extraction of the even square indices uses the exact theta coefficients;
compatibility with the reflected source uses additional global information.
The first note must separate these inputs explicitly.

The physical entire function is

\[
H(t,z)=\tfrac12\bigl[F(t,z)+F(t,-z)\bigr].
\]

For real \(z\) this is \(\Re F(t,z)\), but at complex \(z\) the symmetrized
formula is essential. The conditions \(H=H_x=0\) do not imply
\(F=F_z=0\). Keep both half-line observations and their derivative signs
when matching packets to the collision. Reflection does not license dropping
either lower interval.

Under the local rescaling, the shifted argument has rescaled coordinate

\[
\frac{(x_*+\sqrt{s}\,y+i(T-s)\log2)-x_*}{\sqrt{s}}
=y+\frac{i(T-s)\log2}{\sqrt{s}}.
\]

The imaginary displacement approaches \(T\log2\) in physical coordinates
and diverges in the local rescaled coordinates. A finite Taylor polynomial
valid on bounded \(y\)-sets cannot be substituted at that point without a
separate remainder estimate. This is where the exterior arithmetic data
must remain visible.

## Opening research round: match, expose, then constrain

1. **Write the exact matched system.** Combine the \(d=2\) relation, its
   correctly reflected half-line observation, and the physical symmetrization
   before rescaling. Keep the prefactors, source insertion, lower intervals,
   and derivatives. Separate local physical jets from all observations at
   fixed complex displacement.
2. **Choose a meaningful exterior quantity.** Name the complete combination
   of shifted integrals or modular traces that the matching formula actually
   uses. Specify its norm, parameter domain and dependence on the source.
   Its definition must not encode the desired sign or divide by the unknown
   vanishing jet. An arithmetic identity residual can be used, but its
   vanishing for theta is only an identity until an independent estimate
   connects it to the collision.
3. **Prove the matching remainder at the required scale.** Keep a fixed
   bounded \(y\)-domain for the local expansion and a separate domain for
   exterior data. Establish a remainder after the multiplicity normalization,
   with all dependence on \(c\), derivatives, source cutoffs and complex
   shifts stated. A small absolute remainder need not be small compared with
   \(s\), \(\sqrt E\), or \(E\).
4. **Seek an independent restriction.** Use the complete coefficient and
   modular relations to bound or constrain the exterior quantity on the
   stated domain. Explain why that statement is not simply a rewritten
   collision exclusion. It may initially impose only a nontrivial necessary
   condition on a hypothetical event. A contradiction is a stronger goal,
   not a premise of the work.
5. **Carry the same construction through controls.** At an actual control
   event, use the same scaling and matching procedure, recording precisely
   which global arithmetic relation fails and where that defect enters the
   proposed estimate. Agreement of the local double-collision profile is
   expected and should be preserved.

The opening output should be a short exact setup and matching note, followed
by an estimate attempt or a sharply scoped failure analysis within one
research round. It is not necessary to settle all five projects or to obtain
a numerical Newman improvement before this work becomes worthwhile.

## Second route: full modular compatibility

If the single packet merely moves the unknown to a shifted observation,
compare it with the complete [oscillator/modular relation][oscillator].
Retain the source insertion and physical heat weight, then ask what trace
data the modular reflection couples across the local and exterior domains.
The problem is again an estimate on that complete relation, not an assumption
that the auxiliary oscillator normal form constrains physical collisions.

This route may use a new trace estimate from [08][p08] or an auxiliary
functional from [10][p10]. It need not wait for those projects if a direct
integral relation is accessible. The choice between the two routes should
follow the first matching calculation and its identified uncontrolled term.

## Control screen and what a defect would mean

| Control | Local information it shares | Distinction the global argument must actually use |
| --- | --- | --- |
| Weighted-square sources | The same heat collision law at a matching multiplicity | Missing full reflection and complete coefficient-excision relations |
| Reflected smooth or positive-primitive controls | Reflection and the local heat law, with the source properties proved for each example | Missing the normalized theta square expansion; see [the stronger primitive control][primitivecontrol] |
| Euler-factor modifications | Reflection and unmodified arithmetic factors | Changed coefficients, level or lattice; one d=2 test alone cannot be assumed to detect a modification at another prime |
| Generic heat germs and the shifted-field example | Local multiplicity and heat identities | No complete theta arithmetic; [the shifted example][e8] also prevents bounding arbitrary exterior amplitudes by a vanishing physical energy |

Use the actual hypotheses in [summary 12][s12] and [Reply 18][reply18]. A
defect must measure a specified failed identity, coefficient condition or
quantitative compatibility. Giving the name “arithmetic defect” to the
collision equation, the unknown sign, or an arbitrary nonzero control
quantity does not make it a distinguishing theorem.

## Possible outcomes and limits of the opening scope

**Positive structural outcome:** a relation that forces quantitatively restricted
exterior data for a hypothetical double collision, together with a proved
arithmetic bound or compatibility law for those data. A theorem could cover
only a declared time-height region or a nondegenerate event class. State
that scope and its constants; do not advertise all-event rigidity.

**Useful negative outcome:** prove that a named finite measurement list,
with a specified topology and tail norm, admits colliding sources obeying
all of its tested constraints. That requires an actual construction or proof
within the declared class. It would identify information that the list loses;
it would not exclude infinitely many measurements, a different norm, or the
complete modular relation. A failed Taylor truncation alone is not such a
theorem.

**Preparation only:** an exact rescaling identity, the universal Hermite
profile, source uniqueness, or a reformulation whose independent arithmetic
estimate is still the full original target. Record these honestly and use
them to choose the next estimate, without counting them as the promised
advance.

[09][p09] is the natural supplier of complete-packet estimates; this project
owns their collision-scale interpretation and any new arithmetic restriction
it proves. The collaborator-facing question should include the exact double
event, one complete global relation, the exterior quantity, its required
remainder scale, and a matched control. Singular perturbation, analytic PDE
and analytic number theory are the relevant areas. Review the coherent round
before making stronger status claims; broader multiplicities and endpoint
regimes require explicit subsequent work.

## Shared scope and research practice

This is an exploratory proposal, not a new theorem, completed experiment or
reviewed research result. The [shared overview][overview] states the common
collision target and classifies its all-event strength. Begin with the
[result summaries][summaries] and [patterns to avoid][avoid]; in particular,
use [criterion classification][a01], [premise-based control screening][a02],
[scoped negative results][a07] and [preservation of paired cancellations][a12].

Save incremental derivations in notes, computations and small records in
numerics, and separate assessments in reviews. Review a coherent research
round, which may contain several notes. Record the actual model, effort,
sources and status in subsequent work. Source links below point to canonical
records; existing results retain the review scope stated in those records.

[Project home](../README.md) · [Proposal index](README.md) · [Source guide](../source-documents/README.md).

[s13]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[packets]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md
[oscillator]: ../../brainstorm/03_PROJECT_MERGER_AND_OCTONIONIC_METHODS_CODEX_20261018.md
[p08]: ../../08_modular_oscillator_estimates/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p10]: ../../10_modular_auxiliary_functions/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[primitivecontrol]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md
[e8]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[reply18]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md
[p09]: ../../09_coupled_arithmetic_dilations/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[overview]: ../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
