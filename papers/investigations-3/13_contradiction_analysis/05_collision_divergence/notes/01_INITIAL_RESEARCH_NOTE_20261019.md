# Initial research questions for collision divergence and arithmetic bounds

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

## Research status and standards

This is an initial exploration note, not a completed research program,
progress tracker, new theorem, or numerical acceptance record. The
[living brainstorm][brainstorm] supplies the common RH context. Read the
[result summaries][results] and [patterns to avoid][avoid], especially
[target classification][classification], [collision controls][controls],
[control premises][control-rule], [scoped exclusions][scope], and
[signed recombination][pairing]. Existing results keep their source status;
the required new estimates below are proposed work.

Before quantitative work, identify the exact source versions, domain,
normalization, derivative orders, cutoff conventions, and complete error
norm. Any control run must use the control's own source and errors on a
domain containing its event or relevant witness. Analytic existence results
must not be assigned invented numerical event locations. The analytic
screens below select premises; they are not new numerical validations.

## Hypothetical event and exact contradiction

Use \(h_k=\partial_x^kH\), physical energy \(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\). For an event of exact finite
order \(m=2r+j\), with \(r\ge1\) and \(j\in\{0,1\}\), the existing
local theory identifies the appropriate stationary predecessor branch.
Along that branch, as \(s=T-t\downarrow0\),

\[
\frac{\mathcal L_j}{E}=-\frac r{s}+O(1).
\]

The [local-law sources][local-laws] and [summary 13][laws] specify the
branch and multiplicity assumptions. The desired contradiction is an
independently established arithmetic lower bound that remains finite
near the positive-time event, or permits strictly slower negative
divergence than this pole. The ratio is considered where \(E>0\) before
the event; it is not evaluated as a quotient at the zero itself.

For example, a proved bound \(\mathcal L_j/E\ge-C\), with \(C\)
finite in the relevant neighborhood, would contradict the pole. More
generally, a bound \(\mathcal L_j/E\ge-B(s)\) with
\(B(s)\ge0\) and \(sB(s)\to0\) would suffice. A lower bound with the
same or faster allowed divergence need not contradict anything. These
are formulations of the desired estimate, not estimates proved here.

## Existing inputs and the main transfer difficulty

The [earlier priority note][priorities] already identifies this arithmetic
boundedness target. The generic pole law and its related chord/turning
laws are inherited local geometry. Re-expressing them in another set of
coordinates does not supply the arithmetic lower bound.

The denominator tends to zero at the event. A small absolute tail error
or an error relative to a positive carrier can therefore overwhelm the
physical energy after division. The [carrier and collision analysis][carrier]
explains why accurate approximation of a positive tail does not settle
the complete signed quantity. All endpoint cancellations and the actual
normalization conversion must be retained.

An equivalent finite-bound formulation is
\(\mathcal L_j+C E\ge0\) on the specified predecessor branch. This
may be easier to estimate without division, but it is still the same
unproved inequality. Calling it a nonnegative form does not prove its sign.

## Questions for the first deeper discussion

1. Which complete source or paired arithmetic expression represents
   \(\mathcal L_j+C E\) without destroying its cancellation? What
   quantitative mechanism might bound it on the correct stationary set?
2. Can an independently specified neighborhood or family of stationary
   points support a bound whose constants remain finite at every covered
   positive-time event? Do not choose constants by assuming noncollision.
3. Is the weaker goal of ruling out a particular rate or multiplicity
   accessible? The first useful estimate need not cover both parity
   branches or all positive times, but the excluded class must be stated.
4. Can the retained-sum or source-reflection routes provide a relative
   estimate at the vanishing-energy scale, rather than another fixed
   absolute allowance?

An event-dependent scale can be used in a contradiction argument under a
hypothetical event, but any arithmetic estimate invoked on that scale must
be proved uniformly for the required parameters. An adaptively chosen
plot or shrinking window is not by itself an independent certificate.

## Control screen

The pole law applies to generic analytic heat collisions, including the
appropriate polynomial models. Such a model therefore defeats a finite
lower bound derived solely from the heat equation and local smoothness.
Its failed premise is the complete theta source and arithmetic contract.
The quartic threshold model further shows that threshold real-rootedness
alone cannot remove the ordinary collision pole.

Weighted-square and finite-prime controls retain positive carriers or
selected arithmetic constraints but fail full normalized reflection or
unchanged coefficients. Reflected smooth and positive-primitive controls
lack the theta square expansion. Euler modifications change arithmetic
data. Any claimed source estimate must identify the relevant distinction,
and must not silently apply the genuine theta error constants to a control.

## Useful first results and remaining scope

A useful first result could bound the negative growth rate on a specified
stationary set, prove a relative error estimate compatible with \(E\),
or show that a chosen absolute-payment rule necessarily loses too much
near an event. Record the exponent, constants, norm, multiplicity class,
and parameter range. An averaged energy lower bound does not produce the
needed pointwise ratio bound without a quantitatively compatible transfer.

If both appropriate parity branches were controlled near every possible
positive-time event, the inherited reduction would yield RH. That universal
claim is the existing equivalent target, not a new intermediate theorem.
A bound on a compact positive-time subdomain remains a restricted result;
the approach to time zero and unbounded heights cannot be omitted. This
route concerns local rates before the event, whereas the threshold-jet
route concerns a sign at the event itself. Neither is presumed to dominate
the other before an arithmetic estimate is selected.

[brainstorm]: ../../../brainstorm/notes/04_SMALL_JET_OBSTRUCTION_AND_RH_CONTRADICTION_TARGETS_ASTRA_20261019.md
[local-laws]: ../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[carrier]: ../../../11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/04_modular_collisions.tex
[priorities]: ../../../brainstorm/notes/02_FIXED_CHARACTER_GOALS_AND_ARITHMETIC_COLLISION_RESEARCH_CODEX_20261018.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[laws]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[control-rule]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
