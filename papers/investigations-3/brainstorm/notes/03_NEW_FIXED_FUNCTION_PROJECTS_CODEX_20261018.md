# Proposed projects for fixed function arithmetic and heat collisions

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from this turn's metadata.

**Status:** research proposals following the [fixed character priority
clarification][priority]. The classical beta-function normalization below is
included to make one proposal concrete. No new collision estimate, theorem
of arithmetic rigidity, or literature-priority claim is made.

## Recommendation

Add five candidate projects to the Investigations 3 discussion. Their common
purpose is to obtain an arithmetic estimate for one fixed function. The
most direct continuation is **09, coupled arithmetic dilation estimates**;
the most exploratory construction is **10, modular auxiliary functions**;
and **12, the fixed Dirichlet beta function**, supplies a distinct arithmetic
laboratory. **08** gives the geometric and differential route a concrete
analytic task, while **11** asks what global arithmetic information can
constrain a local collision.

These are proposed numbers and homes, not newly initialized investigations.
The five scopes reuse established machinery from 21–22. Their new work is
the missing estimate or transfer, not another derivation of that machinery.
The [result summaries][summaries] and [patterns to avoid][avoid] remain the
entry points; especially relevant are [arithmetic identities][s14],
[geometric realizations][s16], [control screening][s12],
[criterion classification][a01], and [preservation of cancellations][a12].

| Proposed project | Main question | First substantive result to seek |
| --- | --- | --- |
| 08 Modular oscillator estimates | Can the simultaneous theta recurrence and modular transformation control a signed physical observation? | A valid weighted trace or bilinear estimate with all boundary costs and a benefit from the arithmetic constraints |
| 09 Coupled arithmetic dilation estimates | Can the shifted field and its lower-interval correction be estimated together in the collision pairing? | A signed estimate for complete arithmetic packets, uniform in a stated cutoff or strip regime |
| 10 Modular auxiliary functions | Can modular identities construct a useful lower bound for the existing signed collision form? | One nontrivial admissible auxiliary functional with proved sign and tail control |
| 11 Arithmetic constraints at collision scale | Does a putative collision force a global arithmetic incompatibility that its universal local model cannot see? | A quantitative relation between the rescaled germ and an independently controlled arithmetic quantity |
| 12 Fixed Dirichlet beta function | Does the exact eta product provide more usable arithmetic structure for one fixed character? | A signed heat-transform estimate using the complete product or its modular differential relations |

The selection criterion is potential structural significance, as requested.
An initial phase can succeed through a new restriction or transfer theorem
without immediately improving a Newman bound. A failure is useful when it
identifies the precise estimate and function class that fail; the scope
corrections in [Reply 18][reply18] and [avoid 07][a07] apply throughout.

## Keep one collision target

Use the established notation

\[
h_j=\partial_x^jH,\qquad E=h_0^2+h_1^2,\qquad
\mathcal L_j=h_{j+1}^2-h_jh_{j+2},\qquad S_j=\{h_{j+1}=0\}.
\]

For an event of exact multiplicity \(m=2r+j\), the relevant predecessor
branch satisfies

\[
\mathcal L_j/E=-r/(T-t)+O(1).
\]

An arithmetic lower bound with locally finite loss on the required
predecessors would contradict the event. The all-event zeta assertion is
already RH-equivalent, with the endpoint qualifications in
[summary 13][s13] and [Reply 18][reply18]. This is the common destination of
the projects, not an additional deliverable.

Two distinctions determine whether a proposed intermediate result helps.
An absolute source-tail estimate does not automatically control an error
relative to \(E\) as \(E\) vanishes. Also, identifying the unique normalized
theta source does not establish a sign for its oscillatory transform. Each
project must bridge one of these gaps explicitly. Favorable finite checks
can validate calculations or compare methods; they do not support the
RH-equivalent universal assertion.

## 08 Modular oscillator estimates

Suggested home: `08_modular_oscillator_estimates`.

The [oscillator calculation][oscillator] already places the complete theta
jets in a common generating function satisfying

\[
\partial_u\mathscr U=(\partial_\eta^2-\eta^2)\mathscr U,
\qquad \mathscr U(u,\eta)=\mathscr U(-u,-i\eta),
\qquad \Phi=(U_4-3U_0)/16.
\]

The question is whether using the recurrence and the quarter-rotation law
*together* improves a bilinear estimate after the physical multiplier
\(e^{tu^2}\) and Fourier observation are included. The auxiliary coordinate
\(\eta\), the source coordinate \(u\), and physical heat time \(t\) have
different roles.

Start by specifying a contour or weighted space in which the actual
generating function is admissible. Derive its full integration-by-parts
identity for a two-source expression, retaining the source insertion,
modular pairing, and every contour and cutoff boundary. Then ask whether
the combined boundary form has a bound unavailable from separate absolute
estimates. A useful first theorem would provide that comparison on a
declared parameter range, including the behavior as a cutoff is removed.

This gives the transverse theta-bundle and octonionic constructions an
explicit role: they may organize the oriented bilinear current or improve
its estimate. The scalar form remains the comparison baseline. No ambient
dimension is preferred in advance.

The existing obstruction is specific. The generating function is not in
the usual oscillator \(L^2\) space on the real auxiliary axis, so a standard
spectral gap cannot simply be invoked. A finite jet hierarchy does not
close. The [earlier modular review correction][modularcorrection] also
leaves the transverse question open while excluding the named
moderate-growth completion of the bare heat multiplier. A deformation of
the complete decaying section must be assessed on its own terms.

**Control test:** weighted-square sources obey the local oscillator
recurrence but fail the full modular reflection; reflected smooth sources
lack the normalized theta expansion; the Euler-factor controls change the
level and coefficient data. A calculation using only the recurrence,
positive norms, or curvature has not used a distinguishing premise.

**Specialist audience:** automorphic forms, harmonic analysis, and geometric
analysis. The attractive question is an estimate for a specified section
and observation, rather than the existence of another geometric lift.

## 09 Coupled arithmetic dilation estimates

Suggested home: `09_coupled_arithmetic_dilations`.

This is the closest continuation of the exact arithmetic work. For the
complex half-line transform \(F\), the [complete packet note][packets] gives

\[
\mathcal P_d(t,z)=d^{-1/2}e^{ta_d^2-iza_d}
\bigl[F(t,z+2ita_d)-L_d(t,z)\bigr],
\qquad a_d=\tfrac12\log d,
\]

where \(L_d\) is the indispensable lower-interval integral. The bracket is
the transform of the divisible-index source. Its parts become enormous
relative to their difference; separated positive-time Möbius series fail
even the term test.

The new task is to estimate the **complete packet in a signed pairing**.
One concrete starting calculation is to combine a finite divisor block
with its reflected counterpart before estimating it, using the exact
boundary cocycle from the packet note. Determine whether a contour
representation or a joint quadratic form exposes cancellation that the
current separate majorants discard. Preserve the complete stationary
starting factor; only the endpoint approximation may be truncated under
the existing error lemma.

The first result should be a bound for such a paired block whose dependence
on time, strip width, divisor cutoff, and distance from degeneracy is
explicit. The important question is whether the estimate remains usable
when blocks are assembled. A small absolute remainder with an uncontrolled
main trace does not meet this objective. Nor does a coefficient defined by
dividing the desired observation by a vanishing physical jet.

The exact shifts \(z\mapsto z+it\log d\) remain part of the problem.
A general strip-contraction argument is already saturated by generic
collision models. Any improvement must use the arithmetic relation among
the shifted values and lower intervals. This is distinct from 03's existing
outer carrier estimates and from 04's Sonin mixed-prime operator.

**Control test:** for \(\Phi_a=\sum a_n\phi_n\), exact prime excision has
the extra terms \(a_{pn}-a_n\). The weighted-square controls fail the full
family of these identities. The reflected controls lack the square
expansion. An Euler modification at a prime outside a finite tested set
warns that finite-prime algebra alone is insufficient; its actual
coefficient or level defect must enter the proposed bound.

**Specialist audience:** analytic number theory and complex analysis.
The collaborator-facing question is a concrete cancellation estimate with
known exact terms and known divergent separations.

## 10 Modular auxiliary functions for signed collision forms

Suggested home: `10_modular_auxiliary_functions`.

Try to construct a test function or kernel that converts the exact modular
constraints into a lower bound for the existing signed form. The approach
is inspired by modular constructions of sharp Fourier inequalities, but
the theta collision problem needs its own auxiliary function and proof.

[Radchenko and Viazovska][rv] construct Fourier interpolation from weakly
holomorphic modular forms for the theta group. Their theorem reconstructs
an even Schwartz function from samples of it and its Fourier transform at
\(\sqrt n\). The [Cohn–Kumar–Miller–Radchenko–Viazovska theorem][ckmrv]
uses values and radial derivatives at \(\sqrt{2n}\) in dimensions 8 and 24.
These establish possible construction tools, not a theta collision bound.

Start with the exact bilinear source expression for \(\mathcal L_j\).
Choose a small, explicitly defined family of modular auxiliary kernels.
Use valid arithmetic identities to add terms that vanish for the complete
theta source, then ask whether the resulting expression has a useful
signed lower bound with controlled tails. A finite optimization may suggest
coefficients, but the output must be an analytic or interval-certified
functional valid on a stated domain with its infinite complement included.

The first substantive result would be one such functional, or an
obstruction for that declared auxiliary family. An interpolation formula
that merely reconstructs the same unknown sign is preparation, not the
result. A restricted-domain inequality is a milestone; its extension to
the common all-event target retains RH strength.

There are two immediate compatibility tests. The physical square-index
samples are not automatically the full \(\sqrt n\) interpolation data.
Also, the [finite E8 character bridge][e8] is anisotropic and contains
differential insertions and signed sectors, so a radial E8 inequality
cannot be imported directly. In the one-dimensional approach, the
[finite-source-cutoff test functions][nonlocal] are Schwartz, but their
positive-time limit cannot be taken through separately integrated dual
modes. Prove the relevant uniform admissibility before removing cutoffs.

**Control test:** the auxiliary identities must use exact coefficient and
modular data. Fourier positivity, interpolation, or a generic positive
Gram form alone is shared by colliding controls. A proposed universal
certificate that also signs an actual control event has a missing premise
or an invalid estimate.

**Specialist audience:** Fourier interpolation, extremal functions, and
modular forms. This is the most speculative construction project, with a
clear question to take to specialists.

## 11 Arithmetic constraints at collision scale

Suggested home: `11_arithmetic_collision_rigidity`.

The local collision germ is universal. Therefore its Hermite polynomial,
index, or multiplicity cannot distinguish theta from a control. The new
question is what happens when the germ is matched to the *global*
arithmetic identities of the same fixed source.

Set \(s=T-t\) and \(x=x_*+\sqrt{s}\,y\), with the appropriate
multiplicity normalization. Keep one complete modular or dilation relation
before this rescaling. For example, a fixed dilation samples an imaginary
displacement approaching \(T\log d\), which remains far outside the
shrinking collision scale. Its contribution cannot be replaced by a fixed
finite Taylor polynomial at the event.

The opening task is a matched relation between the rescaled physical germ
and that nonlocal contribution, with all cancellations and bounds uniform
in \(s\). It becomes a substantive result only if an independently proved
arithmetic estimate restricts the nonlocal term or forces a quantitative
defect. This would connect information absent from the universal germ to
the event. An exact matching identity alone leaves the original problem.

A useful negative result could show that one specified finite collection
of arithmetic measurements loses all its distinguishing content in this
limit, under stated norm and tail assumptions. It would identify what an
infinite or nonlocal estimate has to retain. Such a result would not rule
out all arithmetic constraints at collision scale.

**Control test:** carry the same rescaling through the weighted-square,
reflected, and Euler-factor controls at their actual events. Their local
normal forms should agree in the expected multiplicity class; the proposed
distinction must appear in an explicit global defect. A criterion that
rejects their generic local normal form also rejects any hypothetical
theta collision without having used arithmetic.

**Specialist audience:** singular perturbation, analytic PDE, and analytic
number theory. This has high structural upside but the least developed
estimating mechanism of the five candidates.

## 12 The fixed Dirichlet beta function and its eta kernel

Suggested home: `12_fixed_beta_eta_kernel`.

Take one character throughout: the real primitive character modulo four,
\(\chi_{-4}\), with

\[
\beta(s)=L(s,\chi_{-4})=\sum_{n\ge0}\frac{(-1)^n}{(2n+1)^s}.
\]

This choice has a concrete structural advantage for exploration. The
[theta Fourier series][thetafourier], [Jacobi product][jacobiproduct], and
[eta identity][etaidentity] give, for \(y>0\),

\[
A(y):=\eta(iy)^3
=\sum_{n\ge0}(-1)^n(2n+1)e^{-\pi(2n+1)^2y/4}
=e^{-\pi y/4}\prod_{n\ge1}(1-e^{-2\pi ny})^3.
\]

Define the complete source

\[
\Psi_\beta(u)=e^{3u}\eta(ie^{4u})^3.
\]

It is positive, and the [eta transformation][etatransform] gives
\(\Psi_\beta(-u)=\Psi_\beta(u)\). For

\[
C_\beta(s)=(4/\pi)^{(s+1)/2}\Gamma((s+1)/2)\beta(s),
\]

termwise Mellin integration first in \(\Re s>1\), followed by
\(y=e^{4u}\) and analytic continuation, gives

\[
\frac18 C_\beta(\tfrac12+ix/2)
=\int_0^\infty\Psi_\beta(u)\cos(xu)\,du.
\]

Thus the physical heat family can use exactly the source multiplier
\(e^{tu^2}\) and the same spectral scaling as the zeta collision setup.
The normalization is a classical calculation, not a research milestone.
[Dobner][dobner] supplies the broader setting of Newman constants for
the extended Selberg class; any particular imported threshold or
confinement statement must still be matched to this normalization.

The project would ask whether the complete eta product, its logarithmic
derivatives, and modular inversion yield a useful signed two-source
inequality after heat deformation. The initial calculation should keep the
infinite product intact long enough to expose relations among its
derivative terms, then prove convergence and estimate the complete paired
expression. The objective is a new structural restriction for this fixed
function. There is no claim that its GRH problem is easy or that source
product positivity forces real Fourier zeros.

**Control test:** positivity and reflection alone already fail the general
collision screen. The potential extra premise is the exact eta product
and its coefficient and modular relations. Its coefficient pattern differs
from zeta's, so zeta's unweighted-square control table cannot simply be
declared an audit of a beta-specific inequality. Check every proposed
generic step against the existing shape controls, and prepare controls
preserving whatever finite subset of beta identities the estimate uses.

**Specialist audience:** Dirichlet L-functions, theta products, and
modular differential identities. It directly satisfies the fixed-character
objective and could serve as a testing ground for 08–10; transfer back to
zeta would be a further theorem.

## What the existing controls require

The following is a premise screen using the established controls, rather
than a new numerical sign experiment. There is not yet a proposed
inequality to validate. The corrected sources are [summary 12][s12] and
[Reply 18 section 3][reply18].

| Control | Shared information that cannot suffice | Arithmetic information it fails to supply |
| --- | --- | --- |
| Three-square and four-square sources | Positive square weights, support-only moment inequalities, and the matched finite endpoint conditions | Full reflection and the complete constant-coefficient or exact prime-excision laws |
| Reflected super-Gaussian source | Full reflection, positive Fourier–Gram forms, and the stated primitive endpoints | The normalized integer-square expansion |
| Smooth shape and positive-primitive controls | Positivity, reflection, strong shape conditions; the stronger control also matches all algebraic primitive asymptotics | The complete theta arithmetic source specification |
| Euler-factor modifications for every prime p | Reflection and all unmodified Euler factors; finite-prime operator algebra can survive | The original coefficient data and conductor-one structure, with the finer lattice specified in Reply 18 |
| Generic heat germs, q and q(T,a), and the translated-field Gaussian example | Heat identities, local collision geometry, and the particular positivity or decay assumptions proved for each source | They do not provide the complete normalized theta arithmetic data; their properties must not be combined into one fictitious control |

The last row also warns against paying every auxiliary shifted amplitude
by \(E\): [the E8 bridge's Gaussian control][e8] has zero physical energy
at an event and a nonzero shifted amplitude. For any attempt that moves to
the Weil form, also retain the [smooth-density witness and two-channel
exclusion][s04]. Those are checks on the claimed transfer or factorization,
not assertions that the same sources lie in every theta class.

Different controls fail different arithmetic premises. This permits a
joint arithmetic argument; it does not prove that argument. A first
proposal should write its actual input list and identify where each
relevant control leaves that list.

## Selection and relationship to existing work

For an initial selection I favor **09 and 10 as two distinct zeta
approaches**, with **12 as the fixed-character alternative**. If the
preferred emphasis is geometric, choose **08** as a principal project,
with a function space and a specific trace estimate as its opening task.
Keep **11** as an exploratory question until a particular global relation
and independent estimate are chosen. This ranking reflects identifiable
mechanisms and the revised objective; it is not a success-probability
estimate or a short publication timetable.

Three related questions should retain existing homes instead of creating
duplicate projects:

- Exponentially accurate primitive reconstruction belongs with **03**
  unless it introduces a new arithmetic sign mechanism. Its connection to
  heat-deformed Riemann–Siegel estimates is already in the
  [earlier brainstorm][earlier].
- Infinite reflected stable approximation belongs with **05 and 07**.
  A new construction must respect their scoped obstructions; finite
  coefficient changes and the already excluded spin families do not
  provide a fresh starting point.
- Family-to-fixed-function transfer is a **possible extension of 01+03**,
  conditional on an actual construction or comparison map. An asymptotic
  bound for changing primitive characters does not bound a fixed one.
  Inducing a fixed character to larger moduli does not increase its
  primitive conductor. Averages of functions with real zeros need not
  preserve that property. A proposed recovery map must prove convergence,
  compatible heat normalization, and the required sign or zero-location
  transfer before it earns a separate project.

For collaborator recruitment, each selected project should produce a short
problem brief: the exact complete source, one existing collision observable,
the proposed estimate, its distinguishing arithmetic premise, and the
closest control. The technical record can remain in the linked notes.

[priority]: 02_FIXED_CHARACTER_GOALS_AND_ARITHMETIC_COLLISION_RESEARCH_CODEX_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[s04]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[s13]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[s16]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[reply18]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md
[oscillator]: ../03_PROJECT_MERGER_AND_OCTONIONIC_METHODS_CODEX_20261018.md
[modularcorrection]: ../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md
[packets]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md
[nonlocal]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md
[e8]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md
[earlier]: ../../../brainstorm/investigations-3/notes/03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md
[rv]: https://arxiv.org/html/1701.00265v2
[ckmrv]: https://annals.math.princeton.edu/2022/196-3/p03
[thetafourier]: https://dlmf.nist.gov/20.2.E1
[jacobiproduct]: https://dlmf.nist.gov/20.4.E2
[etaidentity]: https://dlmf.nist.gov/23.15.E9
[etatransform]: https://dlmf.nist.gov/23.18.E5
[dobner]: https://arxiv.org/abs/2005.05142
