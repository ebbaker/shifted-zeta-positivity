# Research overview: arithmetic gap continuation

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI Codex LLM assistance. Founding-chat lead configuration: **gpt-6-astra, reasoning effort max**. Author-requested continuation effort: **ultra**; bounded **gpt-6.1-sol/ultra** subtasks expressly authorized. Requested future settings and observed lead provenance are distinct.

## Question and separation from the parent work

Can a structured error equation for the complete arithmetic approximation
of the Newman field yield a useful whole-time bound on gap motion, and
thereby extend a certified interval below the region supplied by direct
large-height localization? The immediate comparison is local and
quantitative. A global Newman-bound improvement is a later coverage
problem, not an asserted consequence of the representation.

The [existing analytical manuscript](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/README.md) owns the
moment hierarchy, common-time compatible approximations and contour
refinements. AGC owns the proposed arithmetic acquisition of a useful
continuation estimate. No parent task is moved, reclassified or closed.
The user chose a direct `investigations-6` child to keep navigation shallow.

Read [the result index](../../../../result-summaries/README.md) and [patterns index](../../../../avoid/README.md), with
[Cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [classification01](../../../../avoid/01_restating_the_target.md),
[premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate caution03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [joint bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [imports16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## Fixed field and observables

The source is the unchanged theta amplitude

\[
\Phi(v)=\sum_{n\ge1}(2\pi^2n^4e^{9v}-3\pi n^2e^{5v})e^{-\pi n^2e^{4v}},
\quad H(t,z)=\int_0^\infty e^{tv^2}\Phi(v)\cos(zv)\,dv,
\quad H_t=-H_{zz}.
\]

Backward time is `u=t_*-t`, so `H_u=H_zz`. For a counted pair use
`a=c-s`, `b=c+s`, `D=s²`; when the pair is real and ordered,
`g=b-a=2sqrt(D)`. For every exterior occurrence put
`Q_j=(rho_j-c)²-D`, `M=sum 1/Q_j`. The pair law is

\[
D_t=2-4DM,\qquad D_u=-\mathcal E,\qquad \mathcal E=2-g^2M.
\]

The full exterior is part of the observable. Along an all-real adjacent
chain, each exterior distance is a cumulative sum of actual neighboring
gaps. Its contribution is a dipole response `1/[r(r+g)]`; M sums those
responses without a normalization by the number of zeros. The canonical
reference spacing is `d≈4π/log(X/(4π))`, with local fluctuations. It is
not a uniform infinite lattice and is not identical to g.

Integer split-pole indices p,q are the natural home of the rational
hierarchy. The regular S/T moments encode it without selecting sqrt(D)
through a merger. A separate complex exponent acts on the quadratic
inverse denominator and gives a Mellin representation, with branch,
convergence and contour assumptions. Merely extending indices does not
create an estimate. The draft derives these facts locally rather than
requiring repeated consultation of the parent.

## Inherited evidence and limitations

| Input | Status carried forward | What it does not supply |
| --- | --- | --- |
| Pair, split-pole and complete moment equations | Existing internal analytical proofs, rederived in the draft | A favorable canonical sign or a finite closure from arbitrary moments |
| Common-time finite-product approximation and counted transfer | Proved at fixed supplied inputs; internal assessment in parent | Useful relative conditioning at arbitrary height or a new source acquisition |
| Joint V/K barrier | Conditional theorem for a stopped complete path | Its own whole-time forcing floor or protection of every gap |
| Canonical high-height moments on a fixed positive slab | Acquired using Polymath's individual zero localization | A second, independent proof of separation or uniform passage to time zero |
| Polymath full finite-sum approximation | Published theorem with stated error domain | Zeros of that approximant are not automatically separated outside clock dominance |
| Platt–Trudgian RH verification | Published finite-height input to the 0.2 bound | Fine separation data for every verified zero |
| Gomila 0.1787854 package | Author presents computer-assisted proof, peer review pending; selected prior internal audit | Full independent replay by this investigation, or all-real separated zeros at its t0 |

Point-of-use sources and exact inspection scopes are in
[references](../references/README.md) and the
[source crosswalk](../notes/02_AGC_SOURCE_AND_STATUS_CROSSWALK_20261119.md).
The blog's later 0.1782354 calculation remains an attributed, unreviewed
research report, not a replacement baseline certified here.

## The quantitative consumer

An upper drift allowance `mathcal E(u)<=epsilon(u)` gives
`D(u)>=D(0)-integral_0^u epsilon`. A signed allowance needs a bound on
every partial integral; a nonnegative allowance can use its final
integral. Strict positive margin protects the target pair only while
its count, chart and complete exterior inputs remain valid up to the
first event.

An alternative retains `V=1-2DM` and
`K=24D²S_2+32D³S_3`. Then `D_u=-2V` and
`V_u=(1-V²-K)/D`. A whole-time `K>=1-eta²` and initial `V<=v0`
give `D(u)>=D(0)-2 max(v0,eta)u` with eta>=0. At gap scale
`D(0)~L^-2`, the rate needed for useful fixed-duration control is much
more precise than the assertion that `K` tends to one.

These identities and conditional comparisons are not new criteria for
RH. The finite milestone is a smaller **complete** allowance or a longer
certified interval at matched information. New coverage and global
assembly are separately named outcomes.

## Candidate analytical mechanisms

1. Preserve the joint numerator `P E_zz-P_zz E` in the difference of
   logarithmic second-derivative quotients, rather than bound its two
   pieces independently. Common spatial multiplicative errors cancel
   there, but contour floors, center error and the heat defect of P remain.
2. Propagate the error through its forced heat equation with full spatial
   complement or boundary data, possibly pairing it with an adjoint
   functional for the time-integrated gap drift.
3. Retain the arithmetic correction and its phase in the actual reference
   field. A smaller remainder centered at `f-C/B` cannot use a lower bound
   proved only for `f`; the earlier Gomila audit is the relevant benchmark.

The mechanisms may be combined after their consumer is fixed. The plan
starts with that choice and proceeds through dependent analytical work
in the same research turn. A failed estimate identifies a scoped loss;
it does not close all other dependence-preserving methods.

## Controls and outstanding work

Apply [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md) on domains containing the relevant events.
The exact quadratic `H=P=z²-2(t-T)` has zero error and forcing defect yet
collides: the strict integrated gap margin fails. Euler-factor and
finite-source/score/prime perturbations change the full theta arithmetic;
finite-profile and atomic controls change its full profile. Reflected
super-Gaussian controls also fail the order-one product premise. Changed
observation kernels fail the physical Newman readout. The draft gives the
complete premise table, including endpoint and static-divisor controls;
no source-identity failure is itself claimed to defeat every coarse bound.

Open tasks are useful denominator/count acquisition, whole-time error
control outside first-term dominance, retaining shared divisor constraints,
and proving a same-information gain. Later global work must cover every
required height and interface, or discharge all three inputs of the
Polymath strip criterion with its `y0²/2` payment. The plan and
[sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
keep those stages distinct.
