# Analytical scope and potential of the relative charge

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. The derivations and [review][review] are by the
same assistant; no independent mathematical review or novelty claim.

**Status:** analytical assessment, with a proved-in-note finite-cluster
discriminant formula and an elementary symmetry screen. These organize
standard facts and inherited local results. No new theta exclusion,
arithmetic charge bound, or numerical experiment is claimed.

The user asks whether the previous comparisons make the method
mathematically uncompetitive, or only numerically uncompetitive, and what
could still be gained. The answer is more precise than either alternative:
two specified numerical constructions lost their comparisons, and one
particular analytic reference mechanism supplies no stronger uniform
margin than its direct consequence. Neither result excludes a different
analytic way of determining or bounding the charge. **Computational speed
is not the sole criterion for continuing this research.**

Read with the [result index][results], [local-geometry cluster][local] and
[avoid index][avoid]. The relevant rules are [classification][a01],
[matching control premises][controls], [scope of negative results][a07]
and [question before numerics][a10]. The current problem is to identify an
independent analytic estimate made accessible by the charge, not to count
an equivalent reformulation as progress.

## 1. What the comparisons establish

| Finding | What it establishes | What it does not establish |
| --- | --- | --- |
| First theta ellipsoid, [Note 01][note01] | The implemented charge certificate uses more source integrals and gives a weaker margin than direct derivative exclusion. | A lower bound on the cost of every boundary method. |
| Two-zero theta box, [Note 03][note03] | With identical source data, direct tensor interpolation gives a stronger margin and a cheaper consumer than the implemented boundary triangulation and degree count. | That direct pointwise estimates always beat global analytic identities. |
| Holomorphic reference transfer, [Note 02][note02] | For a supplied degree-zero square holomorphic reference with boundary floor b and uniform boundary error e<b, the same proof/data give the direct interior floor b−e. | That every way of proving degree zero is a uniform perturbation argument, or that proving degree zero is free. |

The third row is a genuine analytic limitation, not a timing observation.
But its hypotheses matter. It is a comparison of conclusions from one
certificate. If an independent argument first determines the degree,
using that degree to deduce an interior floor does not retroactively
replace the argument by a cheaper direct proof.

In the bounded holomorphic setting, charge zero and absence of a joint
zero are equivalent. Equivalence says that the conclusions have the same
strength; it says nothing by itself about the difficulty of obtaining
them from the available information. The ordinary argument principle is
the useful analogy: a contour count can organize a proof without locating
every zero individually. An appropriate comparison must allow direct
analysis to use all the same analytic information.

## 2. What the invariant could buy analytically

Let B be a bounded domain in complex (t,z)-space, with piecewise smooth
boundary, and H holomorphic near its closure. Assume (H,H_z) is nonzero
on the entire boundary. The compact-fiber argument in Note 02 makes the
joint zeros finite. For the heat equation H_t=−H_zz, inherited local
intersection theory gives
\[
 Q_B=\sum_{p\in B:\,H(p)=H_z(p)=0}\binom{m_p}{2}
       \in\mathbb Z_{\ge0},                                      \tag{1}
\]
where m_p is spatial multiplicity at the event. Simple zeros of H are
not events of this square map and contribute nothing.

**An integer gap.** An independently established estimate Q_B<1 forces
Q_B=0. More generally, Q_B<3 rules out a triple or higher event, while
allowing up to two ordinary double events. If a collection of already
accounted events contributes K, then Q_B<K+1 excludes any additional
event. These are consequences of positivity and integrality, not new
theta estimates. They show what a quantitative global bound could buy
even before it is strong enough to prove full simplicity.

**Aggregation.** Degree is additive over subregions whose separating
boundaries avoid the jet zero set. Internal boundary integrals cancel
with opposite orientations. The resulting outer boundary can encode the
total multiplicity of many events without resolving their locations.
Interior holomorphic event charges themselves never cancel: they are
positive. Signed cancellation is available in the boundary expression,
not in the sum in (1).

**Deformation.** A continuous homotopy of nonzero boundary maps preserves
the degree. This need not be a short straight homotopy justified by a
single error e<b, and its intermediate extensions need not be holomorphic.
Holomorphicity of the final map supplies positivity of its local counts.
An explicit analytic deformation to a map of known degree could therefore
have proof value outside Note 02's reference-transfer class. The missing
work is to prove boundary avoidance throughout that deformation without
assuming the desired interior exclusion. Homotopy invariance and degree
composition are standard; see [Hatcher, §2.2, pp. 134–136][hatcher].

**Separation from absolute size.** On Note 02's box with T=1/10 and R=3/2,
the heat family
\[
 H_\varepsilon(t,z)=\varepsilon(z^2-1-2t),\qquad \varepsilon>0,
\]
has charge zero for every epsilon and exact joint floor 4epsilon/5.
Thus a qualitative charge statement has no universal amplitude floor.
This example illustrates the information retained by degree; it does
not demonstrate a theta advantage, since direct algebra also handles it.
Likewise, multiplying H by a nonvanishing holomorphic unit preserves the
local ideal (H,H_z), hence its charge, but generally does not preserve the
heat equation. No heat-invariance claim is made for that operation.

The boundary must still be nonzero to define Q_B. An analytic identity or
qualitative nonvanishing proof could establish this without a numerical
mesh. A small denominator in numerical evaluation is not, by itself, an
obstruction to such a proof; conversely, topology does not automatically
provide the proof or remove its denominator.

## 3. A concrete analytic interface: finite-cluster discriminant winding

The local discriminant interpretation is already in [BW10 Note 25,
MC4][n25]. The following packages a whole finite cluster into a scalar
analytic object. It is a standard consequence of preparation,
intersection multiplicity and the argument principle, recorded here with
the boundary assumptions needed in this program.

Let D be a bounded disk in the complex time plane and Omega a bounded
disk in the spatial plane. Suppose H is holomorphic on a neighborhood of
the closed product, and
\[
 H(t,z)\ne0\quad\text{on }\overline D\times\partial\Omega,        \tag{2}
\]
\[
 (H,H_z)(t,z)\ne(0,0)\quad\text{on }\partial D\times\overline\Omega.
                                                               \tag{3}
\]
Condition (2) prevents spatial roots from escaping through the side
wall. Condition (3) excludes collisions on the time caps. Neither
asserts absence of an interior collision.

The number N of spatial roots in Omega, counted with multiplicity, is
constant. For k>=1 the symmetric root sums are holomorphic in time:
\[
 S_k(t)=\frac1{2\pi i}\int_{\partial\Omega}
                  z^k\frac{H_z(t,z)}{H(t,z)}\,dz.                 \tag{4}
\]
Newton identities construct the monic polynomial P(t,z) of these N
roots, with holomorphic coefficients, without choosing root labels.
The quotient U=H/P is holomorphic and nonvanishing on the product.
The contour construction and invertible quotient follow the preparation
argument in [Demailly, Chapter II, §2.A, pp. 79–80][demailly].

Define
\[
 \Delta(t)=\operatorname{Disc}_zP(t,z)
          =\prod_{i<j}(z_i(t)-z_j(t))^2.                          \tag{5}
\]
It is single-valued and holomorphic even where individual roots branch;
for N=0 or 1 set Delta=1. It is nonzero on the time boundary by (3).
The usual discriminant/resultant normalization is described in
[the TU Eindhoven resultant notes, §2][resultant].

**Proposition.** With complex orientations,
\[
 \boxed{\quad Q_{D\times\Omega}
       =\frac1{2\pi i}\int_{\partial D}\frac{\Delta'(t)}{\Delta(t)}\,dt
       =\operatorname{wind}(\Delta(\partial D),0).\quad}          \tag{6}
\]

**Proof.** Since U is a unit,
(H,H_z)=(UP,UP_z+U_zP) and (P,P_z) generate the same local ideal.
Fix a time t_0 and let R=C{t−t_0}. The R-module A=R[z]/(P) is free of
rank N. Multiplication by P_z on A has determinant Res(P,P_z), which
differs from Delta by the constant sign (−1)^{N(N−1)/2}. This follows
by evaluating at the distinct roots at generic time, and then by analytic
continuation. The determinant is not identically zero by (3).
Over the discrete valuation ring R, its vanishing order equals the
length of its cokernel A/(P_z), by diagonal reduction over R. That
length is the sum of the local complex lengths of (P,P_z) over t_0:
locally the distinct root clusters split, and preparation identifies
each polynomial quotient with its analytic local quotient. Thus
ord_{t_0} Delta equals the sum of the local jet intersection numbers
over that time. Summation over D and the scalar argument principle
give (6). For N<=1 both sides vanish. Square-map boundary degree
equals the same intersection sum by Note 02. \(\square\)

For a heat event of order m, the inherited Hermite splitting gives local
discriminant order binomial(m,2), recovering (1). The proposition itself
does not need the heat equation or real-rootedness. It extends the
inherited local formula to a fixed finite spatial window; it is not an
infinite discriminant product for all theta zeros.

The heat equation also gives an explicit boundary differentiation rule:
\[
 S_k'(t)=\frac{k}{2\pi i}\int_{\partial\Omega}
                     z^{k-1}\frac{H_{zz}(t,z)}{H(t,z)}\,dz.
                                                               \tag{7}
\]
Indeed partial_t(H_z/H)=partial_z(H_t/H), integration by parts on the
closed contour supplies −k, and H_t=−H_zz supplies the other minus
sign. Equations (4), (7) and the finite coefficient discriminant give
an exact interface from the complete source to (6). They are identities;
the ratios in them have not been estimated for an exhaustion of theta.

One sufficient analytic mechanism would be to derive, from that source,
a holomorphic a(t) near the closed time disk and a constant phase theta
such that
\[
 \Re\{e^{-i\theta}e^{-a(t)}\Delta(t)\}>0\quad(t\in\partial D).
                                                               \tag{8}
\]
The normalized boundary curve lies in a half-plane and has zero winding;
the exponential factor has zero winding too. Equation (6) then gives
charge zero. This is a **conditional sufficient test**, not an established
theta inequality, and it may be harder than direct exclusion. Its value
as a research specification is that a proof would exploit correlated
analytic information about a whole cluster instead of merely repackaging
independent jet error balls. Other signed integral or deformation bounds
could serve the same purpose; (8) is not asserted to be necessary.

## 4. The discriminant does not remove the endpoint difficulty

This interface connects to existing work rather than starting an
independent energy program. On a simple-root time interval write H=UP
as above and b=2U_z/U. The exact root motion is
\[
 z_i'=2\sum_{j\ne i}\frac1{z_i-z_j}+b(t,z_i),
\]
and, writing b_i=b(t,z_i),
\[
 \frac{\Delta'}{\Delta}
 =8\sum_{i<j}\frac1{(z_i-z_j)^2}
   +2\sum_{i<j}\frac{b_i-b_j}{z_i-z_j}.                          \tag{9}
\]
To verify (9), differentiate the squared root differences. The mutual
pair terms give 8/(z_i−z_j)^2; the terms involving three distinct
indices cancel. The remaining term retains the holomorphic unit, hence
the influence of the exterior roots. On a real simple-root interval this
is exactly −2 times the log-gap energy identity in [BW10 Note 12,
§3, H5][energy]. Dropping b would silently replace the actual theta
cluster by an isolated polynomial heat flow.

At an order-m heat event, Delta(t)=(t−t_0)^M d(t) with
M=binomial(m,2) and d(t_0) nonzero. Hence Delta'/Delta has residue M.
Subtracting M/(t−t_0) regularizes the expression while retaining, not
excluding, the event. The elementary heat control H=z^2−2t has
Delta(t)=8t: its real roots are distinct for every t>0, its discriminant
is positive there, and it nevertheless has charge one at t=0. Forward
positivity or monotonicity alone cannot prove endpoint simplicity.

A zero-free source normalization also leaves the discriminant roots
unchanged. One must prove a restriction on the actual winding or its
residues; changing the representation is insufficient. The existing
endpoint energy obstruction is not being claimed as a new result here.

## 5. Symmetry screen and collision controls

Suppose a domain symmetry sigma and a target symmetry tau satisfy
n∘sigma=tau∘n for n=(H,H_z)/||(H,H_z)|| on the boundary. If their
orientation degrees are s and r, degree composition gives
\[
                       sQ_B=rQ_B.                              \tag{10}
\]
Opposite signs would force Q_B=0. The standard theta symmetries do
**not** have opposite signs:

- Reality: sigma(t,z)=(conjugate(t),conjugate(z)) and simultaneous
  conjugation of both target components each reverse two real axes in
  R^4, so s=r=+1.
- Spatial parity: sigma(t,z)=(t,−z), with target action (w_1,w_2)
  mapped to (w_1,−w_2), is complex linear on both sides, so s=r=+1.

These statements apply on domains invariant under the symmetry in
question; an asymmetric box is instead mapped to a different domain.
The symmetries organize equal positive contributions, rather than cancel
them. For example, on a parity-invariant region avoiding z=0, events
occur in equal-charge pairs and Q is even. This imposes a divisibility
condition but does not by itself improve an additive upper bound. No
additional symmetry capable of forcing theta charge zero is established.

The algebraic screens are exact, with no new numerical acquisition:

| Control | Response of the analytical framework; premise missing from a prospective theta exclusion |
| --- | --- |
| H=z^2−2t | Delta=8t and Q=1 on a small event domain. Heat evolution, parity, reality and flat/trivial ambient geometry do not imply charge zero. It lacks the theta source. |
| H=z^3−(4+6t)z+2 | Delta=4(4+6t)^3−108 has three simple complex-time roots, agreeing with three positive charges. Only one event has real time and position. It lacks the theta source; physical forward simplicity does not imply zero global complex charge. |
| RH-conditional close positive sources in [BW10 Note 05][close] | Exact endpoint doubles retain positive local charge despite closeness and forward real simplicity. They fail unchanged ordinary Dirichlet-series arithmetic. |
| Euler-factor controls | Their certified collision witnesses prevent an upper charge estimate below one on an isolating event domain. Their Euler factor/coefficient data differ from theta's; use each control's stated parameter regime. |
| Weighted-square and finite-prime controls | Shared selected support, moment or prime constraints cannot alone give the proposed exclusion. They fail the complete normalized reflection/unchanged coefficient conjunction. |
| Reflected, smooth and positive-primitive controls | Their listed reflection, positivity or primitive properties can coexist with collision; they lack the canonical full theta square expansion. Preservation lists are not merged. |

The last four rows use the existing [control register][controls] and its
source witnesses. They are logical premise checks, not fresh numerical
certifications. The identities (1), (6) and (9) are expected to remain
valid for a control wherever their holomorphic and domain hypotheses
hold. A future theta upper estimate must fail a control's quantitative
or source premise on a domain containing its event; identities alone do
not distinguish theta.

Trivial absolute c_2 also supplies no zero-charge argument: the relative
class includes the nonzero boundary section. That distinction is already
proved and screened in BW10 Note 25. Applying Stokes to a connection
assumed regular throughout B would likewise assume away its possible
interior defect. No new consequence follows from either shortcut.

## 6. Research decision

Keep the numerical comparisons as scoped evidence and stop routine
enlargement of their meshes. Broaden RCH-07 from a cost-separation gate
to an **independent analytical estimate** gate. Computational advantage
is one possible payoff; a useful global theorem, multiplicity budget or
source-dependent obstruction is another.

The next analytical target is a finite-window, source-dependent bound
on (6), or a justified boundary deformation that determines its value.
Equations (4) and (7) specify where the complete theta information can
enter. A successful result must say which analytic information constrains
the winding, why the collision controls do not satisfy that premise,
and how spatial escape, complex-time events and eventual height extension
are handled. Equation (8) is one concrete sufficient form to investigate,
not an assertion that such a form exists or is easier to prove.

The attractive possibility is to replace many local separation tasks by
one controlled global invariant. The present limitation is that we have
the invariant and its analytic interfaces, but no independent arithmetic
estimate restricting it for the required theta domains. This leaves a
legitimate analytical research direction, with its main difficulty now
stated more accurately. HMC-05 remains open and HMC-06 remains gated.

[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[results]: ../../../../../../../result-summaries/README.md
[note01]: 01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[note02]: 02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md
[note03]: 03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md
[n25]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[energy]: ../../10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[review]: ../reviews/04_ANALYTICAL_SCOPE_AND_DISCRIMINANT_REVIEW_20261021.md
[hatcher]: https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf
[demailly]: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
[resultant]: https://aeb.win.tue.nl/2WF02/resultant.pdf
