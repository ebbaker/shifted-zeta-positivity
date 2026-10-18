# 12: The fixed Dirichlet beta function and its eta kernel — exploratory research proposal

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

**Status: outlined; research round not yet begun.**

## Research question and intended advance

Keep one primitive character fixed throughout: \(\chi_{-4}\), of conductor
four. Can its complete eta-product source supply a signed heat-transform
estimate that positivity, reflection and generic decay do not provide?
The research objective is a structural restriction for this particular
L-function. A varying-character result needs a proved transfer to serve this
objective; inducing the same character to a larger modulus does not increase
its primitive conductor.

The exact product offers a concrete way to organize arithmetic derivatives.
It does not establish real Fourier zeros, and this proposal does not assume
that the fixed beta problem is easier than the fixed zeta problem. A transfer
back to zeta would require an additional theorem.

## Classical normalization to use

Write

\[
\beta(s)=L(s,\chi_{-4})=\sum_{n\ge0}\frac{(-1)^n}{(2n+1)^s},
\qquad
C_\beta(s)=(4/\pi)^{(s+1)/2}\Gamma((s+1)/2)\beta(s).
\]

The [theta Fourier series][thetafourier], [Jacobi product][jacobiproduct]
and [eta identity][etaidentity] give, for \(y>0\),

\[
A(y)=\eta(iy)^3
=\sum_{n\ge0}(-1)^n(2n+1)e^{-\pi(2n+1)^2y/4}
=e^{-\pi y/4}\prod_{n\ge1}(1-e^{-2\pi ny})^3.
\]

Define the complete source and physical heat transform by

\[
\Psi_\beta(u)=e^{3u}\eta(ie^{4u})^3,
\qquad
H_\beta(t,x)=\int_0^\infty e^{tu^2}\Psi_\beta(u)\cos(xu)\,du.
\]

The product is positive. The [eta modular transformation][etatransform]
gives \(\Psi_\beta(-u)=\Psi_\beta(u)\). Termwise Mellin integration first
in \(\Re s>1\), followed by \(y=e^{4u}\) and analytic continuation, gives

\[
H_\beta(0,x)=\tfrac18 C_\beta(\tfrac12+ix/2).
\]

This fixes both the spectral scale and the physical multiplier \(e^{tu^2}\).
It is the classical calculation already recorded in the [candidate note][candidates],
not a new milestone. The even source has the decay needed for the displayed
heat transform at finite real time; any subsequent integration by parts,
differentiation of infinite products or exchange of series must state the
specific domination required.

## The new product-to-observation problem

The useful premise would be the complete eta product together with its
modular and differential relations. Merely replacing \(\Psi_\beta\) by
an arbitrary positive even rapidly decaying source would discard the feature
this project is meant to test.

Start from one signed two-source expression for the physical derivatives of
\(H_\beta\). Use logarithmic differentiation of the product to organize the
complete source derivatives, then ask whether the resulting relations impose
a signed bound after the heat weight and Fourier phase are inserted. The
factorwise signs of the product do not directly give the sign of that
oscillatory bilinear integral. This transfer is the unresolved step.

The source's positive product and alternating series are complementary
representations. The complete expression must remain fixed while estimates
move between them. A factorwise absolute bound or a termwise sign assertion
that loses cancellation needs to be compared with the exact paired form.

## Opening research round

1. **Make a normalization and import ledger.** Record the completed beta
   function, source, Fourier scale, physical heat sign and conductor. List
   which local heat statements are generic, which zeta estimates use its
   particular primitive or coefficients, and which global Newman statements
   need a separate beta import.
2. **Write the exact signed form.** Select \(\mathcal L_0\) initially, or
   another already justified observation, and derive its complete beta
   two-source formula. Record all endpoint terms and growth estimates.
   This is setup for the inequality, not proof of its sign.
3. **Use the complete product.** Derive one explicit differential relation
   or integral identity retaining the product's arithmetic structure. Prove
   convergence for each derivative and any modular pairing used. Identify
   a cross term whose size or sign is not determined by generic positivity.
4. **Attempt one estimate and screen it.** Bound that term on a declared
   domain using the beta-specific relations. State the remainder scale
   near degeneracy and compare with appropriate colliding controls. If only
   a restricted source inequality follows, state exactly what physical
   transfer remains.

The proposed first output is the normalization ledger and one substantive
product-to-observation estimate attempt within a coherent round. This setup
has not performed the calculation, initiated a numerical search or claimed
a beta collision theorem.

## Which imports need separate checking

The local analytic heat laws apply to a field satisfying their local
hypotheses. Their global use to locate a finite event requires additional
threshold, confinement and endpoint statements. [Dobner's work][dobner]
provides the broader extended-Selberg-class Newman setting, but any theorem
used here must be matched to the present completed function and time scale.
Do not infer a beta version of every zeta endpoint or primitive bound from
the existence of a general Newman constant.

In particular, a lower bound or positive primitive specific to the zeta
source is not automatically a bound for \(\Psi_\beta\). Nor does a uniform
estimate for a varying family in [01][p01] or [03][p03] become arbitrarily
strong for this fixed character. Any such application must display the
actual fixed-function estimate or comparison map.

## Control screen

The beta source has an alternating odd-index series and an exact eta product.
The zeta unweighted-square control table is useful guidance, not a completed
audit of a beta-specific premise. Use [summary 12][s12] and [Reply 18][reply18]
to test generic steps, then construct or identify controls for the precise
finite subset of beta identities actually used.

| Proposed input | Required screen |
| --- | --- |
| Positivity, even reflection and decay | Existing smooth reflected collision controls test these generic assumptions; none supplies the complete eta product |
| Local heat equations, multiplicity or a positive Gram form | Generic heat controls test the claimed analytic implication independently of beta arithmetic |
| A finite set of product derivatives or coefficient conditions | Determine whether a colliding source can preserve that exact list; no such beta-specific construction is asserted here |
| The complete eta product and modular law | These specify the arithmetic source, but a separate signed consequence still has to be proved |

State which identity a control fails, and which step requires that identity.
Do not treat an unconstructed beta analogue as an established counterexample.
Equally, source uniqueness or failure to find a control is not a positivity
proof.

## Success, useful failure and connections

A first positive result could be a quantitative relation among the complete
product derivatives that restricts the signed physical form on a stated
domain, or a transfer lemma that makes an estimate from [08][p08], [09][p09]
or [10][p10] applicable to beta. The theorem should name the actual extra
arithmetic input and the range in which it helps.

A useful negative result could show that a specified finite product-derivative
ansatz reduces to generic shape assumptions, or produce a colliding source
meeting those exact finite assumptions. Such a conclusion is confined to
that ansatz and class. It does not settle the effect of the full product.

[11][p11]'s collision-scale matching may later be repeated for beta once a
complete nonlocal identity and the necessary global hypotheses are available.
Any comparison with zeta must preserve the heat normalization and prove the
needed sign or zero-location transfer. Neither averaging fixed functions nor
enlarging an imprimitive modulus supplies that transfer automatically.

The specialist brief should show the normalized source, its exact product,
one new differential relation being sought, the signed observation and the
nearest generic control. Dirichlet L-functions, theta products and modular
differential identities are the relevant areas. Continue after a coherent
round when a new restriction, transfer or informative scoped obstruction has
emerged; routine recomputation of the classical Mellin identity is preparation.

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

[thetafourier]: https://dlmf.nist.gov/20.2.E1
[jacobiproduct]: https://dlmf.nist.gov/20.4.E2
[etaidentity]: https://dlmf.nist.gov/23.15.E9
[etatransform]: https://dlmf.nist.gov/23.18.E5
[candidates]: ../../brainstorm/notes/03_NEW_FIXED_FUNCTION_PROJECTS_CODEX_20261018.md
[dobner]: https://arxiv.org/abs/2005.05142
[p01]: ../../01_dirichlet_newman_families/README.md
[p03]: ../../03_effective_outer_remainders/README.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[reply18]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md
[p08]: ../../08_modular_oscillator_estimates/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p09]: ../../09_coupled_arithmetic_dilations/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p10]: ../../10_modular_auxiliary_functions/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p11]: ../../11_arithmetic_collision_rigidity/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[overview]: ../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
