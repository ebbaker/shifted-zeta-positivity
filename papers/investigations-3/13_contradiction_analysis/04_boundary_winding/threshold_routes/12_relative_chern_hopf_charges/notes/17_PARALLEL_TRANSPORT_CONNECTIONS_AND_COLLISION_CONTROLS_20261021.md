# Parallel transport in the heat jet and theta geometry

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**Classification:** geometric interpretation, elementary control
calculations and proposed estimating questions. Parallel transport is
already present in several objects used by the project. Identifying it
does not establish a new theta inequality or change the endpoint-exclusion
status. This note responds to the user's proposed connection with transport.

## 1 Which geometric object carries the transport

A connection tells us how to compare vectors in fibers above neighboring
points. Transport around a closed path can return a vector with a changed
phase or direction; that change is holonomy. A manifold by itself does
not specify a unique connection. A metric supplies a Levi-Civita
connection on its tangent bundle; a Hermitian holomorphic bundle supplies
a Chern connection. The choice must be tied to the theta observation.

Three relevant objects are already in the project:

| Object | What is transported | Relation to a collision |
| --- | --- | --- |
| Complex line spanned by the heat jet G=(H,H_z) | A complex phase, using the induced Hermitian connection | The projective direction and its normalized lift fail at a common zero; the complex boundary records its Hopf charge. |
| Isolated two-root discriminant Delta | The scalar homogeneous component, with an additional source term | Its affine transport equation stays regular through an ordinary double. |
| Spectral cover w^2=H(t,z) | Homology classes of cycles in regular fibers | A cycle collapses when two branch points meet; this is the setting for Gauss-Manin transport. |

The first two belong directly to BW12. The third is the neighboring
[BW13 investigation][bw13]. A separate arithmetic theta line bundle over
a marked elliptic family was developed in Investigations 21–22; its
physical restriction is discussed below. These connections are related
to the same source, but they are not interchangeable.

## 2 The Hopf charge already has a phase connection

On a region where G is nonzero, use the standard Hermitian norm and set

\[
 g=G/\|G\|,\qquad P=gg^*,\qquad
 \mathcal A=-i g^*dg.
 \tag{1}
\]

Here the star denotes Hermitian transpose and d differentiates the real
coordinates of complex heat spacetime. The line L=span(G) is the pullback
of the tautological line under [H:H_z] into CP^1. The induced connection
is P d. For a section g c it acts as

\[
 \nabla(g c)=g\{dc+i\mathcal A c\}.
\]

Thus horizontal transport has c'=-i A_gamma c, and holonomy is
exp(-i integral_gamma A) in this convention. Replacing the unit frame
g by exp(i chi)g changes A to A+d chi and leaves its curvature dA
unchanged. This is the usual geometry underlying Berry phase; see
[Simon's original holonomy interpretation][simon]. No adiabatic quantum
evolution or quantum Hamiltonian is being asserted for the theta field.

With the standard complex boundary orientation and Hopf normalization,
the [manuscript's charge formula][intro] is

\[
 Q_\Omega=\frac{1}{4\pi^2}
       \int_{\partial\Omega}\mathcal A\wedge d\mathcal A.
 \tag{2}
\]

This is a three-dimensional boundary invariant, not a phase acquired on
one chosen loop. In the manuscript's notation alpha=A/(2 pi). The pulled
back line has the global frame g on the boundary and can be topologically
trivial there while (2) is nonzero. The relative top Chern number of the
bulk rank-two section must not be confused with the first Chern class of
this boundary line.

There is a useful restriction on the literal physical plane. For real
t,z, both entries of G are real. Wherever G is nonzero, g is a global
real unit vector, so

\[
 g^*dg=g^Tdg=\tfrac12d(g^Tg)=0,
 \qquad \mathcal A|_{\mathbb R^2}=0.
 \tag{3}
\]

Consequently this particular phase connection has trivial holonomy on
closed real-plane paths avoiding the events. This does not remove the
integer winding of the real two-component vector, root-label monodromy,
or the Hopf charge on a boundary in complex spacetime. It identifies
which observation the connection retains. Complex transverse directions
are essential to its nonzero curvature contribution here.

## 3 The discriminant is already undergoing affine transport

[Note 05][n05] proves, on a proper isolated two-root window,

\[
 \Delta'=8+a(t)\Delta,
 \qquad
 a(t)=\frac{4}{2\pi i}\int_\Gamma
       \frac{H_z(t,\zeta)}{H(t,\zeta)P_2(t,\zeta)}\,d\zeta,
 \tag{4}
\]

where P_2 is the monic two-root polynomial. The coefficient a is
holomorphic through an interior collision because the outer denominators
stay nonzero. This does not assume a positive internal root gap.

Define the scalar covariant derivative D_t=partial_t−a(t). Then
D_t Delta=8. The homogeneous transport factor is

\[
 U(t,s)=\exp\!\left(\int_s^t a(v)dv\right),\qquad
 \Delta(t)=U(t,s)\Delta(s)+8\int_s^t U(t,v)dv.
 \tag{5}
\]

The source 8 is essential. A nonzero homogeneous parallel section
cannot become zero under regular transport; the forced section in (5)
can. Equivalently, the augmented vector satisfies

\[
 \frac d{dt}\binom{\Delta}{1}
 =\begin{pmatrix}a&8\\0&0\end{pmatrix}\binom{\Delta}{1}.
 \tag{6}
\]

This is homogeneous transport of a vector that never vanishes, while
its first component may vanish. A regular flat connection therefore
does not exclude a collision of its observed component.

Normalizing mu(t)=exp(-integral_0^t a), the proposed finite-time return is

\[
 \Delta(0)=\mu(T)\Delta(T)-8\int_0^T\mu(s)ds.
 \tag{7}
\]

This is precisely the invariant already analyzed in [Note 12][n12],
not an additional estimate. Its positivity remains the target. The
new work would have to control its two terms jointly from the complete
theta source. Note 12's large-time amplification concerns separately
bounded scalar data; it does not prohibit every source-correlated
transport estimate.

## 4 Exact collision control and the regularity question

Take H(t,z)=z^2−2t. Then

\[
 G=(z^2-2t,2z),\qquad a(t)=0,\qquad \Delta(t)=8t.
\]

It has an ordinary double at zero, simple real roots for t>0, regular
affine transport, and a charge-one Hopf boundary. The last assertion
follows directly because the complex Jacobian of G at zero has determinant
−4 and hence complex local degree +1. On a sufficiently small boundary
|G|=epsilon, (2) is the unit Hopf integral. Equations (3) and (7) also
hold: real-plane phase transport is trivial and the two terms in (7)
cancel exactly. These are analytic checks, not theta numerical data.

One possible stronger proposal would be a regular finite-dimensional
connection making the physical vector G itself parallel. That would be
substantive: along a path, y'=-B(s)y with integrable ||B|| gives, for s>=s0,

\[
 \|y(s)\|\ge\|y(s_0)\|
            \exp\!\left(-\int_{s_0}^{s}\|B(v)\|dv\right).
\]

A nonzero anchor could then yield a lower bound. But the actual heat
equation gives partial_t G=−(H_zz,H_zzz); it is not a closed homogeneous
equation on these two entries with an already controlled coefficient.
On G!=0 one can force the identity using the matrix-valued one-form

\[
 B=-(dG)G^*/(G^*G),\qquad dG+B G=0.
\]

Its denominator is exactly the missing jet floor. It cannot provide a
noncircular estimate through a common zero merely by definition. A
different connection with independently paid coefficients would be a
new mathematical input, not a consequence of calling the field parallel.
The full heat equation also has a function-space transport interpretation;
preserving a nonzero entire function does not preserve every pointwise
evaluation of that function.

## 5 Spectral and arithmetic transport

For the finite spectral family w^2=H(t,z), the fixed wall and regular
punctured time domain in [BW13 Note 01][period] allow transport of a
vanishing-cycle class. This is the local Gauss-Manin viewpoint: transport
homology or cohomology in regular fibers and integrate a varying
differential over the transported class. The standard meaning of this
connection and its monodromy is illustrated in [Seidel, Lecture 3,
pages 25–26][seidel]. No global finite-genus compactification of the
entire theta cover is being assumed.

BW13 already calculates the period and its first correction. That
correction uses only the existing event four-jet, so it supplies no
extra information under that comparison. A period or monodromy
constraint involving additional exact source data remains a possible
direction. Transporting a cycle near a node is itself compatible with
the node; a useful exclusion needs an independent constraint on its
period or admissible degeneration.

There is also a genuine Chern connection on the arithmetic theta line
bundle in Investigations 21–22. The [metric and restriction analysis][asd]
shows that its pullback to the physical source path tau=i exp(4u), z=0
can be zero in an adapted arithmetic frame, and its natural two-source
external product is flat. Source and observation covector connection
terms cancel in the physical pairing. Mixed transverse commutators
survive before restriction, but their appearance alone does not fix the
sign of the complete cosine transform. Thus ambient curvature cannot be
inserted as an extra favorable term without proving its physical
observation identity. The modular base coordinate is not automatically
the external spectral variable.

## 6 The next test of the idea

The most direct test stays with the already paid two-root window and
asks whether exact source reflection and the shared head-tail law impose
a quantitative constraint on the *complete affine return* (7), or on
the equivalent small response space of [Note 16][n16]. A successful
intermediate estimate improves the complete lower endpoint without an
internal-gap assumption. Calling the return positive is the target;
deriving a stronger source constraint is the work.

A second option is a global period relation for BW13 that is not fixed
by the already studied four jets. Before developing it, specify its
source data, finite domain, boundary terms, direct comparator and the
precise quantitative condition a colliding control would fail. Merely
recording universal monodromy, curvature or charge does not meet that
test. Neither does assuming the normalized direction extends regularly
through every candidate event.

This interpretation follows the [result index][results], the
[geometric summary][geometry], the [collision controls][controls] and
the [avoid index][avoid], especially [lifting without a new estimate][a03]
and [target classification][a01]. The polynomial model only screens
generic heat/connection arguments; it lacks the canonical theta source.
The arithmetic controls have their separate preservation lists. No
theta inequality has been proposed here with a newly verified failed
premise on those stronger controls. No new endpoint margin, numerical
exclusion or independent review is claimed. The [FTSR register][progress]
records this interpretive task without upgrading its existing statuses.

[intro]: ../manuscript/introduction.tex
[n05]: 05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[n12]: 12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[n16]: 16_HIGH_LEVEL_INTERPRETATION_AND_RESEARCH_DIRECTIONS_20261021.md
[bw13]: ../../13_spectral_covers_and_periods/README.md
[period]: ../../13_spectral_covers_and_periods/notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[asd]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[progress]: ../research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md
[simon]: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.51.2167
[seidel]: https://math.mit.edu/~seidel/texts/937-lecture-notes.pdf
