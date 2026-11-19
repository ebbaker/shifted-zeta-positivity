# Split poles, the gap observable and localization

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are
unavailable in this chat's recorded configuration; none is inferred.
Status: **explanatory correction and exploratory discussion, with
same-assistant source and algebra checking**. No new theorem,
certificate, task activation or manuscript milestone is claimed.

This follows Edward Baker's correction to [Discussion06][previous]:
the separate p,q powers and the square root of D deserve a central
place. He also requested a clearer account of estimating the gap itself
and suggested revisiting Pestun localization and index-theoretic
cancellation in light of the present results.

The [result index][results] and [avoid index][avoid] remain the routing
sources, particularly [Cluster18][cluster], [Controls12][controls],
[classification01][classification], [premises02][premises],
[scope07][scope] and [joint-errors12][joint-errors]. Classification here:
the formulas below explain existing identities; the localization
question is an unconstructed mechanism; any eventual computational
claim would need a measured improvement to a complete error or coverage
budget. There is no new global sign criterion.

## 1. The two exponents and the square-root geometry

Write the target pair as \(z_\pm=c\pm s\), \(s^2=D\). For an exterior
zero \(\rho_j\), set \(w_j=\rho_j-c\). [Manuscript §3][split] studies

\[
 P_{p,q}=\sum_j\frac{1}{(w_j-s)^p(w_j+s)^q},
 \qquad p,q\in\mathbb Z_{\ge0},\quad p+q\ge2.
\]

The two indices measure interaction with the two target poles
separately. Their diagonal is \(S_n=P_{n,n}\), and
\[
 T_n=\tfrac12(P_{n-1,n}+P_{n,n-1}),\qquad n\ge2.
\]
Conversely every integer split moment reduces to the complete S/T
tower. Thus using the complete regular tower does not discard q;
it changes coordinates. A truncation still needs its own error bound.
[§4][lattice] carries the two-index structure into the compatible
lattice for adjacent pairs sharing one zero divisor.

The square root matters because replacing s by -s exchanges p and q.
For example, the algebra in §3 gives
\[
 P_{2,0}+P_{0,2}=2S_1+4DS_2,\qquad
 \frac{P_{2,0}-P_{0,2}}{4s}=T_2.
\]
The divided expression has its regular continuation at s=0. More
generally an integer split moment has the form A+sB, with A and B
regular functions of time obtained from D and the regular moments.
Its symmetric and divided-antisymmetric parts remain regular even
when the labeled roots merge. The raw labeled derivatives can contain
1/s; the manuscript exhibits this behavior, rather than assuming it away.
The event D=0 remains possible: the exact law gives D'=2 there.

One distinction is essential. The current manuscript proves the
two-index recurrence at **integer p,q**, and separately proves
[§9's][complex] complex-power family
\[
 Z(p)=\sum_j \exp\{p[2\log\ell-\Log(w_j^2-D)]\},
 \qquad \Re p>\tfrac12 .
\]
This is the combined-denominator continuation, with specified local
branches. The checked manuscript does not establish a joint complex
p,q extension of the split recurrence. Such an extension is a natural
question, but would need two log choices, exchange and chart-transition
rules, and a complete time law. An integer finite-sum recurrence cannot
simply be asserted for noninteger indices. Any claimed advantage must
also explain what useful estimate this representation adds beyond the
equivalent complete regular tower.

## 2. What “estimate the final gap quantity” means

The intended target is \(D(t_*)=(z_+(t_*)-z_-(t_*))^2/4\), or a
certified lower bound for \(\min_{t\in I}D(t)\) if the claim concerns a
whole interval. “Final” meant the quantity the argument ultimately
needs. It did not mean that checking only the last time suffices.

Consider \(z_-=a-1,\ z_+=a+1\), with uncertain real a. Both individual
positions can be poorly known while the gap is exactly 2 and D exactly
1. Independent error intervals for the two roots can lose this
cancellation. The aim is to carry their common uncertainty into the
gap calculation before taking absolute bounds.

The same issue occurs in contour readouts. On a counted contour
enclosing exactly two zeros, fix a spatial reference \(\zeta\), put
\(u=z-\zeta\), \(B=H_z/H\), and define
\[
 I_k=\frac1{2\pi i}\oint u^k B\,dz,\qquad
 a=\frac{I_1}{2}=c-\zeta,\qquad D=\frac{I_2}{2}-a^2.
\]
If \(B=\widehat B+\delta B\), write
\(\delta I_k=(2\pi i)^{-1}\oint u^k\delta B\,dz\) and
\(\widehat a=\widehat I_1/2\). The exact difference is
\[
 D-\widehat D=
 \frac{\delta I_2}{2}-\widehat a\,\delta I_1
 -\frac{(\delta I_1)^2}{4}.
\]
The two moment errors come from the same field error. Keeping that
dependence, including the quadratic term, is the principle behind
[§20's][correlated] existing refinements. [§19][adjoint] supplies
another exact route that weights errors by their effect on D.

An especially simple cancellation occurs if
\(\widetilde H=H(1+\varepsilon)\) on a zero-free contour neighborhood:
\[
 \frac{\widetilde H_z}{\widetilde H}-\frac{H_z}{H}
 =\frac{\varepsilon_z}{1+\varepsilon}.
\]
Both quotients must be defined. A common nonzero scalar factor has
\(\varepsilon_z=0\), hence no effect on this readout. A useful bound
for a nonconstant error needs a denominator margin and an analytic
derivative estimate, together with complete evolution and tail costs.
The identity alone does not supply those estimates. The proposed
research target is a better complete bound for D or its path at fixed
source information, not merely a smaller field norm.

## 3. Instantaneous cancellation does not remove the exterior dynamics

For a counted disk, factor \(H=((z-c)^2-D)A\), where A is analytic
and nonzero throughout the disk. Polynomial-weighted contour integrals
of \(A_z/A\) vanish. Thus the fixed-time pair power sums ignore that
analytic factor. This does not make A irrelevant to heat evolution.

For an elementary finite illustration, evolve
\[
 H(0,z)=(z^2-d)(z^2-b^2),\qquad b^2>d>0,
\]
by \(H_t=-H_{zz}\), selecting the pair \(\pm\sqrt d\). The exterior
zeros give \(M(0)=2/(b^2-d)\); the established pair law yields
\[
 D'(0)=2-\frac{8d}{b^2-d}.
\]
At d=1, b=5 gives D'(0)=5/3, whereas b=9 gives D'(0)=19/10.
The initial target pair is identical; in both cases the exterior
distances exceed four times the target half-gap. The exterior changes
the pair's velocity. These are
direct substitutions in the existing law, not a numerical certificate
or a new theta-source result.

Consequently a possible localization identity must retain the
appropriate exterior contribution to a time-dependent gap. A freely
chosen time-dependent rescaling can also change the heat equation even
though its spatial logarithmic derivative is unchanged.

## 4. What the Pestun analogy offers now

The checked primary source is recorded in the [Pestun reading note][pestun].
In §4.4, a Q-complex pairs fluctuation modes; the surviving determinant
is governed by an equivariant kernel/cokernel character of a
transversally elliptic operator. This is richer than a single integer
index. The localization deformation also requires control of boundary
terms. These are substantive ingredients, beyond an observed scalar
normalization cancellation.

The [20 September discussion][old-localization] had already represented
the prime-free gamma/pole factor by auxiliary bosonic and fermionic
Gaussian factors. Its spectrum was prescribed to reproduce the desired
factor. It did not derive that spectrum from a supercharge, a
localization complex or a physical observable dictionary. That is the
specific unresolved bridge; the discussion does not exclude all
localization approaches.

There is also an existing [index-interface note][index-interface].
It records finite-regularization event-mass and bounded-weight estimates
for the jet map \((H,H_z)\). Unlike the ordinary contour root count,
which stays two when two roots merge, this event construction can detect
a double zero. The missing transfer includes an inverse Schur-complement
cost and the distinction between complex-time averaging and the physical
time slice. No theta improvement or analytic-index identification was
established there. Those limitations concern that interface, not every
possible equivariant construction.

The current work makes the localization question more specific:
we have an exact two-pole observable and its exterior force, a
compatible finite heat model, and demonstrated benefits from keeping
common errors. It is reasonable to ask whether some of those
dependencies come from a Ward identity that can be derived independently
of the desired answer. This is a structural motivation, not evidence
that such a charge exists.

The exchange \(s\mapsto-s\) already explains useful parity
cancellations. It supplies neither a continuous equivariant action nor
an elliptic complex by itself. Likewise, the two target poles are not
identified with the two S4 fixed points merely by counting them.
Physical heat time changes D; an auxiliary localization deformation
parameter must not be silently equated with physical time.

## 5. A bounded feasibility question and its controls

A useful first question is: **can a specified differential complex and
symmetry produce a Ward identity for the complete two-pole observable
or its error, in the compatible finite heat model?** The observable,
measure or pairing, domain and boundary conditions would have to be
given. The surviving term must represent the actual gap or its
complete forcing, including exterior contributions. Defining an
auxiliary spectrum solely to reproduce a desired factor repeats the
earlier unresolved construction.

If such a structure exists, its quantitative test is whether its
identity improves a complete D or transport bound using the same
information available to a direct method. The current short-tube
transport target or a larger certified interval would be concrete
consumers. An exact identity without a gain remains an identity;
a global no-collision conclusion is not a substitute for that test.
No new task is activated by this discussion.

The [full analytical control screen in Discussion06][previous] is
retained. For this proposal its implications are:

- Quadratic and strong-collar quartic heat controls satisfy the generic
  local quotient and split-pole algebra and can collide. They fail
  literal canonical theta-source identity, not those generic
  cancellation identities. A general error theorem must enclose their
  actual events, including zero error for an exact finite model.
- Euler-factor translates and finite-source, finite-score and
  finite-prime perturbations do not have the complete unchanged theta
  source. Preserved finite data cannot be declared a substitute for
  that premise. No proposed Q here has been shown to distinguish them.
- Shape-positive and reflected controls retain their separately
  documented source, order and kernel distinctions in Controls12.
  No inference from scalar positivity, an ordinary index or normalized
  quotient invariance excludes those classes.
- Static divisor surgery and arbitrary moment states fail the
  common-path or realizability premise. A legitimate complex must
  respect the admissible evolution; a definition on independent formal
  coordinates would not automatically transfer to it.

This is a premise screen, not a new numerical replay. Until a complex
is specified, further localization-specific controls cannot honestly
be claimed as passed. The proposed next conceptual gain is a derived
identity for the complete observable, followed by its fully paid
quantitative use.

[previous]: 06_VCD_GT_CM_RESEARCH_POSITION_AND_PATHS_DISCUSSION_20261118.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[cluster]: ../../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[classification]: ../../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint-errors]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[split]: ../../manuscript/sections/03_split_poles.tex
[lattice]: ../../manuscript/sections/14_coupled_lattice.tex
[complex]: ../../manuscript/sections/04_complex_powers.tex
[correlated]: ../../manuscript/sections/22_correlated_enclosures.tex
[adjoint]: ../../manuscript/sections/19_two_sided_refinement.tex
[pestun]: ../references/01_PESTUN_LOCALIZATION_READING_20261118.md
[old-localization]: ../../../../../../../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/notes/LOCALIZATION_AND_THE_POLE_CANCELLATION_20260920.md
[index-interface]: ../../../../../../../papers/investigations-4/notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
