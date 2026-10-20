# Topological boundary information beyond the three profile relaxation

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from this chat's recorded metadata.

**Status: brainstorm and elementary diagnostic, with author self-checks.**
The proposals below have no acquired new theta boundary certificate.
The concrete diagnostic shows that the three auxiliary atoms in the
displayed actual-profile witness have noninteger logarithmic-derivative
residues. This excludes that particular witness as an entire-function
zero divisor, but does not establish feasibility or infeasibility of an
integer replacement. The earlier positive-measure dual obstruction remains
valid in its stated class.

The project can return to its original target: obtain arithmetic boundary
information incompatible with a collision's required index. The fourth-order
quantity \(Q_L\) is one possible intermediate estimate, not a mandatory
invariant. The most relevant information missing from the profile relaxation
is integer contour counts, the phase of the actual function, and compatibility
between different points and times of the same heat flow.

The [result index][results], [control cluster][controls], [topological
results][topology-summary], and [avoid index][avoid] govern this discussion.
In particular, [target classification][avoid01], [control premises][avoid02],
[scoped conclusions][avoid07], and [signed recombination][avoid12] apply.
An exhaustive positive-time noncollision statement is RH-strength.
A bounded contour count, a quantitative boundary estimate, or a precise
failure of a specified information class is the appropriate milestone.
The [active register][progress] retains all existing task statuses.

## 1 Why the fourth order target was selected

At a hypothetical ordinary double event of the unchanged flow,
\[
 H_t=-H_{xx},\qquad H(T,a)=H_x(T,a)=0,\qquad h_2\ne0,
 \qquad h_j=\partial_x^jH(T,a),
\]
deflate only the double zero at \(+a\):
\[
 G(z)=\frac{H(T,z)}{(z-a)^2},\qquad
 S_2=-(\log G)''(a)
     =\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}.
\]
A local logarithm suffices, even when \(G(a)<0\). The all-real product and
the complete theta imaginary-axis estimate give the inherited strict
bound \(S_2>L_2(a)>0\). Fix \(0<L\le L_2(a)\), uniformly on the event
domain under consideration. Multiplication by the positive factor
\(18h_2^2\) gives
\[
 \boxed{Q_L=2h_3^2-3h_2h_4-18Lh_2^2
              =18h_2^2(S_2-L)>0.}                     \tag{1}
\]

This choice has three practical reasons. It expresses an already proved
necessary restriction; it needs only derivatives through order four at
the event; and its polynomial form avoids dividing by a curvature that
can be arbitrarily small. It also retains the mixed signed interaction
\(h_2h_4\), which separate absolute estimates can lose. The [all-height
bound][all-height] and [complete Schur consumer][schur] supply these
interfaces. Equation (1) is not a winding number, and \(Q_L>0\) is not
sufficient for a collision.

Its connection to boundary data comes through the critical curve
\(H_x(t,c(t))=0\). With \(v(t)=H(t,c(t))/h_2\), the [time-face
calculation][critical] gives
\[
 v(T)=0,\quad v'(T)=-1,\quad
 v''(T)=\frac{h_4}{h_2}-\left(\frac{h_3}{h_2}\right)^2
       =-\frac13\left(\frac{h_3}{h_2}\right)^2-6S_2.
                                                               \tag{2}
\]
Thus the lower bound on \(S_2\) forces a quantitative negative symmetric
pair of critical values on the two time faces, after the stated
sixth-derivative remainder is paid. That pair is compatible with the
ordinary collision and its winding \(-1\). It does not by itself give
an opposing boundary degree.

An independently proved \(Q_L\le0\) would contradict (1) directly, so no
additional winding computation would be necessary. Conversely, an
independent zero-winding certificate can exclude an event without ever
estimating \(Q_L\). The latter is the natural primary target when the
investigation is specifically about topological boundary contradictions.

## 2 Keep the three boundary counts distinct

| Boundary object | Integer it determines | What the hypothetical event forces |
| --- | --- | --- |
| Physical real spacetime loop \((H,H_x)\) on \(\partial D\) | \(W_D=-\sum_D\lfloor m/2\rfloor\), oriented by \(dt\wedge dx\) | At most \(-1\) if any collision lies inside |
| Complex spatial contour \(C\), with \(H(T,z)\ne0\) on \(C\) | Number of enclosed spatial zeros, with multiplicity | At least two if it encloses the designated double zero |
| Complex-time loop for the discriminant of an isolated two-zero group | Number of discriminant zeros inside, with multiplicity | One on a sufficiently small loop around an ordinary double event |

The first row is the [physical index theorem][index]; it already handles
all finite spatial multiplicities. The third row is related to the
[existing complex discriminant calculation][complex-index], not an
identification of complex degree with physical degree. For higher
multiplicity their weights differ.

An independently obtained spatial count of exactly two buys isolation
of a double event; it does not exclude that event. A physical boundary
value \(W_D=0\), by contrast, contradicts any enclosed collision because
all its local indices have the same negative sign.

## 3 A concrete topological defect of the displayed profile witness

The [actual-profile study][profile] retains three observations at
\(b=20,40,80\), for \(T=0.1\pm10^{-6}\) and \(a\in[1001,1002]\).
After removing a hypothetical double pair at \(\pm a\), its positive
weighted measure satisfies
\[
 \int\frac{y+400}{y+b_i^2}\,d\mu(y)
 =\frac{D_T(b_i)}{b_i}-\frac4{a^2+b_i^2}.
                                                               \tag{3}
\]
The constructed measure has three auxiliary nodes
\(y_j=900,1600,25000\), with weights \(w_j>0\), and a neighboring
unit-count atom at \(y_*=(a+d)^2\), \(0<d\le1/2\).

For a genuine zero pair at \(\pm\sqrt y\), the multiplicity is
\[
 \nu=\frac{y+400}{2}\mu(\{y\}).
                                                               \tag{4}
\]
This is also the residue at either zero of the corresponding
logarithmic derivative. Using the source note's rounded outward profile
intervals and its exact rational inverse matrix, the
[exact diagnostic][diagnostic] proves the following strict bounds
uniformly over that entire parameter domain:

| Squared auxiliary node | Required residue \(\nu_j=(y_j+400)w_j/2\) |
| --- | --- |
| \(900\) | \(1.1429<\nu_1<1.1433\) |
| \(1600\) | \(1.9438<\nu_2<1.9444\) |
| \(25000\) | \(82.5224<\nu_3<82.5235\) |

All three intervals exclude every integer. Explicitly, the candidate
full logarithmic derivative would be
\[
 \ell_\mu(z)=\frac{4z}{z^2-a^2}
       +\sum_{j=1}^3\frac{2\nu_jz}{z^2-y_j}
       +\frac{2z}{z^2-y_*}.                              \tag{5}
\]
It reproduces the three samples, since \(D_T(b)=i\ell_\mu(ib)\) there.
But its period on a small positively oriented loop around
\(+\sqrt{y_j}\) is \(2\pi i\nu_j\). For \(H'/H\) of a single-valued
entire function, the same period must be \(2\pi i\) times an integer
zero multiplicity. Exponentiating a local primitive of (5) instead
produces nontrivial monodromy at these nodes.

The relevant classical input is the logarithmic-derivative form of the
[argument principle][argument-principle]. The numerical conclusion here
uses only exact rational arithmetic on existing certified enclosures;
it is not a new acquisition of theta values.

There is also a direct source distinction: the auxiliary node \(y_1=900\)
would require a zero at \(x=30\), whereas the [validated source
interface][interface] already gives \(|H(T,30)|>9.07\,10^{-5}\)
throughout the same time interval.

These observations reject the displayed witness, not every replacement.
Because its original weights are strictly positive and its observation
matrix is invertible, small changes of the auxiliary nodes preserve an
exact positive fit by continuity. Forbidding just the three particular
locations does not close the relaxed class. Similarly, integrality
alone needs a new feasibility analysis: ordinary colliding entire
functions already have integer multiplicities.

## 4 Integer contour counts and known zero locations

One way to retain the missing topology is to supplement (3) with
actual-source counts on selected complex contours. A certified count
fixes an integer amount of zero mass in a region; a count of zero removes
that region from the permitted support. Under the event's all-real
hypothesis, counts in contours enclosing real intervals translate to
integer constraints on the residual positive zeros.

This is stronger than requiring arbitrary weighted masses to be positive.
It can also be stronger than imposing integrality at preselected atoms:
the atoms may move, but the total count in a certified region is fixed.
One should subtract already located zero groups, with their location
uncertainties, before allowing the remaining source to absorb the
profile constraints. Their contributions must be enclosed jointly with
the observation errors and infinite tail.

For a contour around \(a\) that excludes \(-a\), a count of exactly two
would forbid the witness's extra unit-count atom anywhere inside that
contour. This provides a quantified gap if the contour encloses a
specified disk about \(a\). It does not give a contradiction by itself;
the double root is still consistent with the count.

**Bounded question.** On one declared parameter box, can a small number
of acquired contour counts and zero-location enclosures make the
three-profile constraints incompatible with any extra unit-count root
within a specified distance of \(a\)? Compare the feasible class before
and after adding those counts. A failed integer feasibility search is
not a proof of infeasibility; a proposed bound needs a complete
certificate over the permitted locations and tails.

**Stopping condition.** If only the three displayed atom sites are
removed, or the replacement integer class remains unexamined, record
that limited distinction. Do not report a zero gap. The local source
nonvanishing and contour counts must be proved, not chosen to fit a
desired root configuration.

## 5 Direct physical winding from phase and wall flux

This is the most direct continuation within boundary winding. Retain
the actual loop
\[
 {\cal J}(t,x)=H(t,x)+iH_x(t,x)
\]
on a complete spacetime boundary. The field must be analytic near the
closed region and \({\cal J}\) must be nonzero on the whole boundary
before a winding is assigned. \(H\) itself may vanish on that boundary.
For the wall formula below, retain the source note's regular time faces,
nonzero corner values and analytic wall hypotheses. The phase form is
\[
 d\arg{\cal J}
 =\frac{(H_xH_{xx}-HH_{xxx})\,dt+
             (HH_{xx}-H_x^2)\,dx}{H^2+H_x^2}.             \tag{6}
\]
The temporal part matters. A sign on the spatial Laguerre expression
alone does not determine the loop's winding, as the repository's cubic
heat control already demonstrates.

The extra information is the cyclic order and signed change of the
actual first-jet direction around the boundary. Imaginary-axis samples
of a single time slice supply none of this loop data. Boundary phase
estimates can be useful even when one cannot give a useful interior
lower bound for \(|{\cal J}|\).

For moving spatial walls \(\alpha(t)<\beta(t)\), the [wall-flux
identity][wall-flux] gives
\[
 W_D=\frac{N_- -N_+ -Q_\alpha+Q_\beta}{2},\qquad
 K(D):=-W_D=\frac{N_+-N_-+Q_\alpha-Q_\beta}{2}.           \tag{7}
\]
Here \(N_\pm\) count real zeros on the regular time faces, and \(Q\)
denotes signed wall crossings, including the correct local degrees
at tangencies. These wall terms are unrelated to \(Q_L\).
Arithmetic boundary data giving \(K(D)<1\) forces \(K(D)=0\), since
the index theorem makes it a nonnegative integer. Equivalently, a
rigorous lower winding bound \(W_D>-1\) is enough.

There are two concrete acquisition strategies:

- Certify a cyclic sequence of half-plane or angular enclosures for
  \({\cal J}\) on whole boundary segments. Preserve common endpoints
  and count all phase crossings. The existing implementation already
  supports half-plane homotopy and exact polygon winding.
- Bound the signed combination in (7), keeping correlations between
  the two time faces and the walls. It may be possible to determine
  its integer value without resolving every crossing separately.

The comparison must retain the complete theta approximation and its
shared analytic errors on the boundary. A new representation of
independent pointwise error disks alone supplies no established gain.
Any normalizer or rotating frame must return its own orientation and
winding contribution explicitly. Real projective data retain twice
the physical winding; an unrestricted complex-projective filling
does not retain this obstruction, as the [projective note][projective]
explains.

**Bounded question.** Can one previously uncovered region be assigned
only winding zero from its paid boundary enclosures, while the strongest
same-source interior test remains unresolved or demonstrably costs more?
An interval enclosing the winding with radius less than \(1/2\) about
zero would suffice. A strict lower bound above \(-1\) can be weaker
still when the physical index sign is used.

**Control and stopping condition.** For \(H=x^2-2t\) on
\([-1,1]^2\), both time faces have zero real roots inside the spatial
interval, but \(Q_\alpha=1,Q_\beta=-1\), so \(W_D=-1\).
Equal endpoint counts alone would give a false exclusion. The fresh
wall-flux replay retained in [the diagnostic record][diagnostic] passes
all 88 inherited polynomial domains. A local approximation that merely
recovers this negative degree has not produced an arithmetic contradiction.

## 6 A contour count followed by a signed boundary modulus estimate

This combines a topological gap certificate with an optional return to
\(S_2\), while avoiding division by \(h_2\) in the boundary observation.
It also identifies a potentially useful observable beyond additional
imaginary-axis samples.

Assume a paid contour \(C_r=\{z:|z-a|=r\}\), \(0<r<a\), has no boundary
zero and encloses exactly two zeros counted with multiplicity. At the
hypothetical double event, \(G=H(T,z)/(z-a)^2\) is then zero-free on the
closed disk. Its logarithm is analytic there. Consequently
\[
 S_2=-\frac{1}{2\pi i}\oint_{C_r}
            \frac{G'(z)/G(z)}{(z-a)^2}\,dz.              \tag{8}
\]
The zero-free disk is an input of this identity, supplied by the count,
not inferred from small profile error.

A real-symmetric version uses boundary modulus alone. Expand
\(\log G(a+w)=c_0+c_1w+c_2w^2+\cdots\); the nonconstant coefficients
are real. Orthogonality of the cosine modes gives
\[
 \boxed{S_2=-\frac{2}{\pi r^2}
     \int_0^{2\pi}\log|H(T,a+re^{i\theta})|
                                  \cos(2\theta)\,d\theta.}       \tag{9}
\]
Indeed the integral for \(\log|G|\) is \(\pi r^2c_2\), while
\(S_2=-2c_2\). The difference
\(\log|H|-\log|G|=2\log r\) integrates to zero.
A constant amplitude normalization also cancels. A nonconstant analytic
normalizer contributes its second logarithmic derivative and must be
restored.

Equation (9) selects one signed Fourier component of boundary data.
It suggests combining the contour contributions before absolute
estimation. It does not justify estimating only their favorable part;
the repository's [circle-cancellation analysis][circle-loss] records
the losses caused by that operation.

There is a concrete error contract. Let the complete approximant \(P\)
be holomorphic near the closed disk and nonzero on its boundary. If it
satisfies, on the whole circle,
\[
 |H-P|\le\varepsilon |P|,\qquad 0\le\varepsilon<1,
\]
then \(|\log|H|-\log|P||\le E_{\log}:=-\log(1-\varepsilon)\).
The resulting error in (9) is at most
\[
 E_{S,\mathrm{source}}\le\frac{8E_{\log}}{\pi r^2},       \tag{10}
\]
because \(\int_0^{2\pi}|\cos(2\theta)|\,d\theta=4\).
The same strict boundary comparison transfers a known zero count of
\(P\) to \(H\) by [Rouché's theorem][rouche].
Quadrature, parameter variation, contour geometry and all source
omissions remain separate complete payments.

**Bounded question.** Can a source-informed signed evaluation of (9),
with the count-two certificate and all errors, yield a better upper
bound than the existing jet/Schur estimate? An upper bound at most
\(L\) would contradict the inherited \(S_2>L\). No uniform curvature
floor is required merely to state that contradiction.

**Control and stopping condition.** For
\(H(T,z)=(z^2-a^2)^2\), (9) returns the surviving mirror contribution
\(1/(2a^2)\), not zero. Adding a nearby real zero outside or inside
the contour must respectively change the boundary harmonic or the
enclosed count. A count-two certificate alone is not a sign result.
If the paid log error divided by \(r^2\) overwhelms the target, the
new observation has failed its budget; decreasing the radius is not
automatically an improvement.

## 7 A two-zero discriminant determined from spatial boundary data

The [complex multiplicity note][complex-index] already supplies the
local discriminant theory. A possible estimating interface is to
recover the discriminant directly from contour moments.

Suppose a fixed complex spatial contour \(C\) stays zero-free for
all complex times in a neighborhood of the closed time disk \(U\),
and encloses exactly two zeros there. Define
\[
 p_k(t)=\frac{1}{2\pi i}\oint_C z^k\frac{H_z(t,z)}{H(t,z)}\,dz,
 \quad k=0,1,2,\qquad p_0=2.
\]
These functions are holomorphic in \(t\), and the two enclosed zeros
\(z_1,z_2\), counted with multiplicity, satisfy
\[
 \Delta(t)=2p_2(t)-p_1(t)^2=(z_1(t)-z_2(t))^2.           \tag{11}
\]
Individual zero labels can interchange; the symmetric quantity
\(\Delta\) remains single-valued.

At an ordinary real collision \((T,a)\), locally write
\[
 H(t,z)=A(t,z)\big((z-u(t))^2-v(t)\big),\qquad A(T,a)\ne0.
\]
At the event the heat equation gives
\(-A(T,a)v'(T)=-2A(T,a)\), hence \(v'(T)=2\).
Since \(\Delta=4v\),
\[
 \Delta(T)=0,\qquad \Delta'(T)=8.                       \tag{12}
\]
Thus its winding is one on a sufficiently small positive time loop.
More generally any such disk containing the event has at least one
discriminant zero, provided the stated holomorphic packet and boundary
nonvanishing conditions hold.

The desired contradiction would be an independent arithmetic
calculation of winding zero for \(\Delta(\partial U)\). One explicit
sufficient estimate is
\[
 |\Delta(t)-c|<|c|\quad(t\in\partial U),\qquad c\ne0.
\]
The argument principle then excludes a discriminant zero inside.
This is a proposed arithmetic estimate, not something supplied by
the universal local expansion \(8(t-T)+O((t-T)^2)\).

**Why this is relevant to the witness.** The contour count prevents
an extra neighboring zero from being inserted inside the group, and
the contour moments must come from the same holomorphic function at
every time. Fractional slack measures and unrelated single-time fits
do not supply those data. The discriminator is the acquired contour
information; the discriminant identity itself is shared by colliding
heat controls.

**Bounded question and stopping condition.** Compare the complete cost
and error budget for \(p_1,p_2,\Delta\) with direct physical winding
on the corresponding real region. The current real-time fourth-order
validation is not a certified complex-time contour contract.
The subtraction in \(2p_2-p_1^2\) should retain correlations, or use
moments centered at a fixed reference height to avoid unnecessary
large cancellations. Stop if only the local discriminant is recovered,
or if root-group isolation and complex-time payments cost more without
an improved bound. For \(m>2\), use the actual degree-\(m\) discriminant;
its weight is \(m(m-1)/2\), not the physical \(\lfloor m/2\rfloor\).

## 8 Compatibility across the boundary is additional information

The profile witness fits three values separately at each fixed
parameter point. A boundary argument should require all observations
to be restrictions of one analytic heat solution. Where \(H\ne0\),
its logarithmic derivative \(\ell=H_z/H\) obeys
\[
 \ell_t=-\ell_{zz}-2\ell\,\ell_z.                        \tag{13}
\]
This follows by differentiating
\((\log H)_t=-(\ell_z+\ell^2)\).
It can constrain jointly observed contour values and their time
variation. It does not itself distinguish theta from other heat flows.

For a coherent physical approximant \(H=P+r\), the residual satisfies
\[
 r_t+r_{zz}=-(P_t+P_{zz}),
\]
not necessarily the homogeneous heat equation: the truncated polynomial
used in the existing interface is not an exact heat solution.
Overlapping analytic neighborhoods, one common residual, and this
known forcing are possible means of retaining information lost by
independent interval fits.

The useful question is whether those relations eliminate a nonzero
winding class still admitted by independent boundary enclosures.
No gain follows merely from rephrasing them as gluing, a bundle
extension, or monodromy. A global phase cannot be assumed around a
collision, and a regular phase maximum principle cannot be applied
through the point where \(H=H_x=0\).

## 9 Controls and a bounded next comparison

| Control class | What the proposed topological information does and does not exclude |
| --- | --- |
| Displayed actual-profile measure | Its three noninteger residues fail entire-function realizability; its atom at \(x=30\) also fails acquired theta value data. Other integer measures remain an open feasibility question. |
| Polynomial and Hermite heat events | They satisfy the PDE, integer counts, heat splitting and discriminant laws. Their own boundary data must retain the correct negative physical index. Complete theta arithmetic is absent. |
| Positive atomic and continuous threshold controls | They have genuine entire functions and integer zeros. The known finite-profile families match their own constructed vectors, not the specified theta data; they lack unchanged theta arithmetic, full profile growth and eventual simplicity at threshold as recorded in their sources. |
| Euler-factor controls | They satisfy generic heat and entire-function topology, and can have positive thresholds. They change the complete theta coefficients and their own quantitative boundary data. Their failure of a source identity does not imply failure of every derived inequality. |
| Weighted-square and finite-prime controls | Local events and selected arithmetic constraints remain. Full normalized theta source information fails; finite weighted-square controls have no all-real heat time, and no such threshold is assigned to finite-prime constructions. The physical index screen still applies to their local events. |
| Reflected, smooth and positive-primitive controls | Reflection, positivity and generic topological laws can coexist with a collision. These controls lack the unchanged normalized theta square expansion; source-specific boundary estimates are the missing premise. |
| Earlier counter-kernels and smooth-density or two-channel constructions | Apply only their documented source and product hypotheses. Positivity or an auxiliary realization cannot replace actual theta boundary data; their scoped obstructions do not determine a theta contour count. |

The broader families receive the analytical premise screen in
[result-summary 12][controls] and [result-summary 04][positive-obstructions].
No uncomputed event, threshold or theta error budget is assigned to them.
The new [exact checker][checker] makes 201 rational checks of the
residue bounds, boundary-harmonic factors and finite algebraic fixtures; the inherited wall-flux
replay has 2,122 checks on 88 domains. These are consistency checks and
a diagnosis of one witness, not evidence for an RH-equivalent assertion.

For a next bounded comparison, prioritize **physical boundary winding**
with shared theta data and complete wall flux. It is already matched
to the project's contradiction and covers all multiplicities.
Use **integer spatial counts** as additional observations where they
can be acquired independently. If a useful count-two contour becomes
available, compare the **signed boundary-modulus estimate** and the
**two-zero discriminant** with the existing direct methods.

The decision should turn on one measured outcome: removal of an
admissible nonzero winding class, a paid count/gap margin, a better
signed upper bound with its remaining deficit, or an explicit failed
budget. Neither another formulation of the index theorem nor the
rejection of the displayed fractional witness alone meets the
event-exclusion target.

[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[topology-summary]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[positive-obstructions]: ../../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[avoid]: ../../../../../avoid/README.md
[avoid01]: ../../../../../avoid/01_restating_the_target.md
[avoid02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[avoid07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[progress]: ../research-progress/02_THRESHOLD_SIGNED_ARITHMETIC_PROGRESS_20261020.md
[all-height]: ../threshold_routes/08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[critical]: ../threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[schur]: ../../02_threshold_jet_sign/notes/05_EXACT_EVENT_CONDITIONED_FOURTH_ORDER_SCHUR_CONSUMER_20261020.md
[profile]: ../threshold_routes/08_deflated_jet_hierarchy/notes/06_ACTUAL_PROFILE_OBSERVATIONS_AND_RELAXED_DUAL_FAILURE_20261020.md
[interface]: ../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/15_COMPLETE_FOURTH_ORDER_INTERFACE_20261020.md
[index]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[wall-flux]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[projective]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md
[complex-index]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[circle-loss]: ../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md
[checker]: ../numerics/check_profile_witness_topology.py
[diagnostic]: ../numerics/PROFILE_WITNESS_TOPOLOGICAL_SCREEN_20261020.json
[argument-principle]: https://dlmf.nist.gov/1.10#E9
[rouche]: https://dlmf.nist.gov/1.10#iv
