# Physical reflection, the reference junction, and a first bulk response

19 September 2026, third calculation. OpenAI GPT-6 (Codex), for Edward Baker.

**Status:** exact classical reflection and color-gluing identities; a
conditional regulated Gram construction; free endpoint and Gaussian bulk
calculations; 67 new finite diagnostics. Ordinary time reflection gives
the two branches different constant supercharges. An R rotation restores
the bulk scalar map but fails positivity on the elementary endpoint
doublet. A modified contour meets the reference smoothly and has a finite,
nonzero direct bulk-exchange response. The full interacting response,
quantum reflection-positive regulator and arithmetic realization remain
open. This is not a positivity theorem for the interacting defect theory.

This carries out the task in [the second continuation](CONTINUATION_20260919_SESSION2.md),
using [its endpoint calculation](DEFECT_PROJECTORS_AND_ENDPOINT_POLARIZATIONS_20260919.md).
The important distinction is between an ordinary adjoint pairing, which
can be positive without a common charge, and an internally rotated pairing,
whose positivity must be tested separately.

## 1. Choose a reflection compatible with physical time

Keep the defect at \(x^3=0\), and reflect a **defect time direction**:

\[
\vartheta x=Rx,\qquad R=\operatorname{diag}(-1,1,1,1),\qquad
b=0\in\{x^0=0\}\cap\{x^3=0\}.
\tag{1.1}
\]

The positive half-space is \(x^0>0\). In the bosonic adjoint convention,
the gauge field is a one-form, all six Hermitian scalar fields are even
under geometric time reflection, and complex conjugation exchanges the
defect scalar with its antifundamental adjoint. Fermionic reflection and
a full regulator are additional ingredients in an interacting OS theorem.

For the isometric scalar map from the second note, use

\[
M e_0=-e_7,\quad M e_1=e_8,\quad M e_2=e_9,\quad M e_3=e_6,
\qquad M^TM=1.
\tag{1.2}
\]

Let \(C:a\to b\) lie in \(x^0>0\) except at \(b\), with \(a\) on
the defect, and let

\[
U_M(C)=P\exp\int_C(iA_\mu+\Phi_\mu)dx^\mu,
\qquad \Phi_\mu=M^A{}_{\mu}X_A.
\tag{1.3}
\]

For Hermitian regulated matrix backgrounds, the actual reflected adjoint is

\[
\Theta_0 U_M(C)=U_N(\vartheta C^{-1}),\qquad N=-MR.
\tag{1.4}
\]

*Derivation.* Pulling the fields back by \(\vartheta\) turns (1.3) into
\(U_{MR}(\vartheta C)\). The dagger reverses matrix order and replaces
the scalar map by its negative on the reversed contour, as proved in
the second note. This gives (1.4). In particular,

\[
N e_0=-e_7,\quad N e_1=-e_8,\quad N e_2=-e_9,\quad N e_3=-e_6.
\tag{1.5}
\]

The time component retains its scalar map, while the three spatial
components reverse it. This is more specific than plain contour reversal.

The ordering and scalar-reflection rule agree with
[Dorn--Pershin, (4)--(7), printed p. 2](https://arxiv.org/pdf/hep-th/9906073).
Their ordinary-reflection argument and the distinction from an internal
rotation are in (11)--(16), printed p. 3. Those printed equations were
visually checked. Their result is not a construction of this defect
theory's fermionic measure.

## 2. Color gluing and exactly what positivity would require

Define a color vector at the common reference by

\[
F_i^\alpha=[U_M(C_i)]^\alpha{}_{\beta}\,q_2^\beta(a_i).
\tag{2.1}
\]

Its reflected row is

\[
(\Theta_0 F_i)_\alpha=
\bar q_{2,\gamma}(\vartheta a_i)
[U_N(\vartheta C_i^{-1})]^\gamma{}_{\alpha}.
\tag{2.2}
\]

The candidate kernel is therefore the specific observable

\[
K_{ij}=\left\langle
\bar q_{2,\gamma}(\vartheta a_i)
[U_N(\vartheta C_i^{-1})]^\gamma{}_{\alpha}
[U_M(C_j)]^\alpha{}_{\beta}
q_2^\beta(a_j)\right\rangle .
\tag{2.3}
\]

There is an identity color contraction at \(b\), not an extra defect
field there. Under a gauge transformation, \(F_i\mapsto g(b)F_i\)
and \(\Theta_0F_i\mapsto(\Theta_0F_i)g(b)^{-1}\). Thus the paired
observable is gauge invariant, even though a single \(F_i\) is not.

**Conditional Gram statement.** Suppose a regulator admits OS positivity
for these half-space functionals with their reference color fiber, and
the regulated endpoint and junction operators belong to that domain.
Then (2.3) is positive semidefinite. For example, in a bosonic regulator
with a positive boundary factorization, the two half-integrals give
vector wavefunctions \(\psi_i^\alpha(B)\) and

\[
K_{ij}=\int d\nu(B)\sum_\alpha
\overline{\psi_i^\alpha(B)}\psi_j^\alpha(B),\qquad d\nu\ge0.
\tag{2.4}
\]

Summing against coefficients gives the integral of a squared norm.
Boundary gauge transformations act unitarily on the displayed color
fiber. This is the precise location of the reference color sector in
the construction; it cannot be erased when imposing Gauss law.

Equation (2.4) proves the conditional statement, not its hypotheses for
interacting supersymmetric defect matter. The full fermionic theory is
not represented here by an asserted positive bosonic density. Gauge
invariance of (2.3) alone proves no OS inequality. A physical realization
of the reference charge sector, a compatible regulator and any junction
counterterms must still be supplied.

## 3. The free kernel changes with the reflection

Strip the positive color and propagator normalization. At free order,
\(U=1\), and for \(a_i=(\tau_i,\mathbf z_i,0)\), \(\tau_i>0\),

\[
K^{(0)}(a_i,a_j)=
\frac1{\sqrt{(\tau_i+\tau_j)^2+|\mathbf z_i-\mathbf z_j|^2}}.
\tag{3.1}
\]

Its standard free-scalar Fourier representation is a positive integral
of products \(e^{-|\mathbf k|\tau_i+i\mathbf k\cdot\mathbf z_i}\).
In particular, on the positive time ray \(a_r=(r,0,0,0)\),

\[
K^{(0)}(r,s)=\frac1{r+s}
=\int_0^\infty e^{-\lambda r}e^{-\lambda s}\,d\lambda.
\tag{3.2}
\]

This is a finite positive kernel for \(r,s>0\). The reflected points
are separated even on its diagonal. After the usual radial weights,

\[
\sqrt{rs}\,K^{(0)}(r,s)
=\frac1{2\cosh((\log r-\log s)/2)}=G_o(\log r-\log s).
\tag{3.3}
\]

Thus ordinary time reflection gives the parent's **opposite-ray** kernel,
not its even average \(n_\gamma\). It is Hankel in \(r,s\), but becomes
translation invariant in their logarithms; these two coordinate statements
should not be confused.

The [parent Poisson-smearing profile](../../wilson-lines/notes/ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md)
has support on the entire defect sphere, including both signs of \(x^0\).
It is not a positive-time state preparation. A profile supported strictly
inside the positive hemisphere is admissible at free level, but its
covariance must be recomputed; the old equal even-mode weights do not
follow. This does not alter the parent's valid regulated *ordinary*
free covariance calculation. It prevents calling that same construction
an instance of (2.3) without a new argument.

## 4. The reflected branches and their supercharges

Use \(\chi=D=+1\) and the matrices of the second note. For this section,
\(\widetilde K_\mu=i\Gamma_{M e_\mu}\Gamma_\mu\) uses the signed map
(1.2), and \(K_n=i\Gamma_6\Gamma_3\). The conditions are

| Operator | Ket eigenvalue | Ordinary reflected-bra eigenvalue |
|---|---:|---:|
| \(\widetilde K_0\) | \(-1\) | \(-1\) |
| \(\widetilde K_1\) | \(-1\) | \(+1\) |
| \(\widetilde K_2\) | \(-1\) | \(+1\) |
| \(K_n\) | \(-1\) | \(+1\) |

Each complete family has one complex chiral defect-compatible charge.
In just the \((x^0,x^3)\)-plane each has two. Their intersection is zero
because of the opposite normal conditions. This conclusion applies to
families whose tangents independently sample time and normal directions,
including the curved family below. It is not inferred merely from a cusp.

The normal conditions select opposite H weights. Accordingly the ket
uses \(q_2\) with its constant charge, and the physical bra uses
\(\bar q_2\) with the conjugate-weight charge. Both endpoint conditions
are now accounted for. The identity tensor at \(b\) has no local variation
that could compensate incompatible branch conditions.

As a bulk positive control, a straight time-directed contour needs only
\(\widetilde K_0=-1\), common to both maps, and its chiral defect solution
space has dimension four. This is a control of the *bulk* intersection;
it does not assert that a constant charge annihilates the physical
adjoint pair of scalar endpoints.

## 5. An R rotation aligns the connection but changes the metric

Consider rotations by \(\pi\) about the H axis 4 and the V axis 7:

\[
S_H=\operatorname{diag}(1,-1,-1),\qquad
S_V=\operatorname{diag}(1,-1,-1).
\tag{5.1}
\]

They are proper rotations in the actual \(SU(2)_H\times SU(2)_V\)
R symmetry. With \(S=S_H\oplus S_V\), direct substitution gives

\[
SN=M.
\tag{5.2}
\]

The rotated reflected line can therefore obey the ket's bulk projectors.
But \(S_H\) acts on the endpoint doublet as \(\pm i\sigma_1\), up to
basis conventions. It sends the adjoint of \(q_2\) to a phase times
\(\bar q_1\). The diagonal pairing is then the zero off-diagonal
contraction already found in the second note.

On the full free endpoint doublet the inserted metric has opposite
eigenvalues. With a phase making it Hermitian it is \(\sigma_1\):

\[
\frac1{\sqrt2}(1,-1)\,\sigma_1\,
\frac1{\sqrt2}\binom{1}{-1}=-1.
\tag{5.3}
\]

Without that phase the \(\pi\)-rotation has eigenvalues \(\pm i\),
so the form is not even real on all states. No overall phase makes both
eigenvalues positive. Ordinary adjoint pairing instead inserts the
identity and is the positive control.

More generally, on a positive Hilbert space a unitary insertion can give
a nonnegative form on every vector only if it is the identity on that
space: nonnegativity makes it a positive self-adjoint operator, and
unitarity then forces all spectral values to be one. A projection onto
one rotation eigenspace is a different, potentially positive operation;
here it mixes the two H polarizations and does not preserve the same
fixed-weight endpoint condition.

This explicit endpoint counterexample does not contradict the restricted
large-rectangle conjecture in Dorn--Pershin. It tests our doublet state
space. Their distinction between ordinary reflection positivity and an
unproved internally rotated inequality is exactly the distinction needed
here.

## 6. A free test of the older odd-H normal reflection

The parent normal-reflection proposal assigned odd parity to the H
scalars. Its [review](../../wilson-lines/reviews/review_codex_2026-09-18.md)
already distinguished that proposed discrete symmetry from a positive
adjoint. The necessary free test is decisive for an unrestricted scalar
algebra with the canonical bulk covariance: a real mode of frequency
\(\omega>0\), inserted a distance \(a>0\) from the reflection plane,
has ordinary OS norm \(e^{-2\omega a}/(2\omega)>0\); making it odd
reverses the sign.

The issue need not be hidden in a gauge-variant field. For a non-Abelian
gauge group with \(\operatorname{tr}T_aT_b=\delta_{ab}/2\), take the
Hermitian Wick polynomial

\[
\mathcal O=i\operatorname{tr}\bigl(H[V_1,V_2]\bigr),
\tag{6.1}
\]

with one H scalar and two distinct V scalars. It is gauge invariant and
odd under H sign reversal with V even. In the canonical free bulk limit,
Wick contraction at separated reflected points gives

\[
\langle\Theta_{\rm even}\mathcal O(x)\,\mathcal O(x)\rangle
=\frac14\sum_{abc}f_{abc}^2\,D(\vartheta x-x)^3>0.
\tag{6.2}
\]

The odd-H choice gives its negative. The ordinary-even choice is again
the positive control. Thus this parity assignment cannot define a
positive reflection on the full canonical free bulk observable algebra.
A restricted observable sector or a different reflected theory would
require a separate definition. We have not classified all possible
normal-reflection actions on the interacting defect; no uniqueness of
the parent's proposed parity assignment is assumed.

## 7. A smooth reference junction is available

Let \(v\) be the incoming unit tangent of a ket at \(b\). The outgoing
tangent of its reflected reverse is \(-Rv\). A smooth geometric join
therefore requires

\[
v=-Rv,
\tag{7.1}
\]

so \(v\) must be normal to the reflection plane, i.e. parallel to
\(e_0\). The scalar directions also agree there, since
\(N(-Rv)=Mv\). For a multi-contour kernel every ket should share this
reference tangent. In contrast, the inherited semicircles arrive along
\(-e_3\); under time reflection they turn back along \(+e_3\),
reproducing the backtracking geometry identified in the earlier review.

Contour freedom lets us impose (7.1). An explicit dimensionally consistent
family in the \((x^0,x^3)\)-plane is

\[
X_{T,\eta}(t)=\bigl(Tt,\eta T f(t)\bigr),\qquad
f(t)=t^2(1-t),\qquad 0\le t\le1,\quad T>0,\quad\eta\ge0.
\tag{7.2}
\]

The ket traverses it from \(t=1\) to zero. Both ends are on the defect,
the interior is in positive Euclidean time and above the defect for
\(\eta>0\), and its incoming tangent is \(-e_0\). The reflected return
gives a regular join with a continuous scalar direction, even when the
two branches have different \(T,\eta\). Curvature need not match.

This removes the constant-angle geometric and internal-coupling cusp
from the direct one-loop bulk exchange. It does not prove that touching
the defect at \(b\) needs no counterterm in the full interacting theory.
That local defect problem remains part of the operator definition.

## 8. The first nonzero direct bulk-exchange term

Here compute a specified subset of the perturbative response: free
Feynman-gauge bulk propagators
\(\langle A_\mu A_\nu\rangle\propto\delta_{\mu\nu}/|x-y|^2\) and
\(\langle X_A X_B\rangle\propto\delta_{AB}/|x-y|^2\), with equal
normalization. Endpoint self-energy, endpoint-to-line interactions and
defect diagrams are **not** included. Only their sum can be the full
gauge-independent interacting response.

On each separate branch, the gauge/scalar numerator cancels because
\(M^TM=N^TN=1\). Across the branches, if \(v_i,v_j\) are the original
ket tangents, reflection and reversal give

\[
-(-Rv_i)\cdot v_j+
[N(-Rv_i)]\cdot Mv_j
=v_i\cdot(R+1)v_j
=2\,v_{i,\mathrm{sp}}\cdot v_{j,\mathrm{sp}}.
\tag{8.1}
\]

Here \(\mathrm{sp}\) means the three directions unchanged by time
reflection, including the defect normal. Cancellation is lost only in
those components. At a reference tangent \(-e_0\), they vanish linearly
with distance. Near a regular join the denominator is of order
\((s+t)^2\), while the numerator is \(O(st)\). Hence the local double
integral is finite. This statement is about the displayed bulk term.

For the self-pairing of (7.2), scale invariance removes \(T\) and the
stripped cross term is

\[
I(\eta)=2\eta^2\int_0^1\!\int_0^1
\frac{f'(s)f'(t)}{(s+t)^2+\eta^2[f(s)-f(t)]^2}\,ds\,dt.
\tag{8.2}
\]

With propagator \(g^2/(4\pi^2|x-y|^2)\), its contribution relative to
the free endpoint propagator is \(g^2C_F I(\eta)/(4\pi^2)\).
No factor of one-half is needed for an exchange between two distinct
ordered branches.

**Proposition 8.1.** For this direct bulk term,

\[
I(\eta)=\bigl(\tfrac32-2\log2\bigr)\eta^2+O(\eta^4),
\qquad \tfrac32-2\log2\simeq0.1137056388801094>0.
\tag{8.3}
\]

*Proof.* The quadratic coefficient is \(2A\), where

\[
A=\int_0^1\!\int_0^1
\frac{(2s-3s^2)(2t-3t^2)}{(s+t)^2}\,ds\,dt.
\]

Set \(r=s/(s+t)\), \(u=s+t\), whose Jacobian is \(u\). By symmetry
restrict \(0\le r\le1/2\) and integrate \(0\le u\le1/(1-r)\).
The polynomial \(u\) integral simplifies to

\[
A=\frac12\int_0^{1/2}\frac{r^2}{(1-r)^2}\,dr
=\frac34-\log2.
\tag{8.4}
\]

Since \(|f'|\le1\), \(|f(s)-f(t)|\le s+t\); and since
\(|f'(s)|\le2s\), the corner is dominated by an integrable bounded
function. Expanding the denominator is justified, and the elementary
bound \(|I(\eta)-2A\eta^2|\le2\eta^4\) follows directly. \(\square\)

For reference, \(I(0.3)\simeq0.0102220294387\) and
\(I(0.7)\simeq0.0553790171219\). The straight-time control has
\(I(0)=0\). Thus a shape dependence is explicitly present in this
sector; it is not a change in the free endpoint propagator.

The cross-response matrix of several curves is nonnegative in this
Gaussian sector. Equation (8.1) reduces it to twice the sum of ordinary
reflected scalar norms of their spatial line currents. Equivalently,
the four-dimensional massless propagator across the time plane factors as

\[
\int\frac{d^3k}{(2\pi)^3}\frac1{2|k|}
e^{-|k|(s+t)}e^{ik\cdot(\mathbf x_i(s)-\mathbf x_j(t))}.
\tag{8.5}
\]

After integrating each spatial current, this is a positive momentum-space
inner product. For (7.2), the near-reference current vanishes, making
the displayed cross norm finite. This positivity belongs to this
Feynman-gauge Gaussian subset and does not replace the full calculation.

## 9. Shape variation and the missing Ward identity

For the one-form \(B_\mu=iA_\mu+\Phi_\mu\), fixed endpoints and
constant \(M\) reduce the first note's variation to

\[
\delta U_M(C)=\int_C U(b,x)\,\mathcal F_{\nu\mu}(x)
\eta^\nu\dot x^\mu\,U(x,a)\,ds,
\tag{9.1}
\]

\[
\mathcal F_{\nu\mu}
=\partial_\nu B_\mu-\partial_\mu B_\nu-[B_\nu,B_\mu]
=iF_{\nu\mu}+D_\nu\Phi_\mu-D_\mu\Phi_\nu-[\Phi_\nu,\Phi_\mu].
\tag{9.2}
\]

The sign follows the convention \(\dot U=BU\). A moving endpoint
would add \(B_\nu\eta^\nu U\) at the final end and its corresponding
initial term. Our bulge variations vanish at both endpoints and preserve
the reference tangent. In the reflected kernel they give

\[
\delta K_{ij}=
\langle\Theta_0(\delta F_i)F_j\rangle+
\langle\Theta_0F_i\,\delta F_j\rangle.
\tag{9.3}
\]

No sign or vanishing statement follows from this identity alone. Even
if a variation of a state were \(\delta\psi=Q\lambda\), its norm obeys

\[
\delta\|\psi\|^2=2\operatorname{Re}\langle Q^\dagger\psi,\lambda\rangle.
\tag{9.4}
\]

The condition \(Q\psi=0\) does not set this to zero. For example,
\(Qe_2=e_1\), \(Qe_1=0\), \(\psi=e_1\), \(\lambda=e_2\) gives
derivative two. A state in \(\ker Q\cap\ker Q^\dagger\) gives zero
first variation as a control. An all-orders protection statement needs
an actual Ward identity and its endpoint/junction terms. The subset
(8.3) might still cancel against other physical diagrams; no contrary
claim is made.

## 10. What this supplies and the next calculation

There is now a concrete ordinary-reflection network, an explicit color
contraction, a half-space support condition, a smooth reference join,
and a computable nonzero bulk contribution to contour response. Its
ordinary pairing is compatible with a conditional positive-state
construction. It does not carry the old even free kernel automatically,
and one constant Poincare charge does not annihilate the whole network.
Aligning the charges by the displayed R rotation fails the endpoint
positivity test.

The next bounded calculation is the **complete first interaction-order
shape response** for (7.2): include endpoint-to-line gauge and scalar
terms, endpoint renormalization and the required defect/junction terms,
in one stated gauge and scheme. Start at a positive bulge \(\eta_0>0\).
The straight-time reference lies entirely on the defect, so its relation
to the limit \(\eta\downarrow0\) is itself a question about boundary
contact terms and the order of limits. Subtract that reference only after
specifying the normalized observable. Determine whether the coefficient
in (8.3) survives or cancels, and whether the complete answer has additional
nonanalytic or regulator-dependent terms. It would be misleading to feed
this bulk subset directly into an arithmetic generator.

Even a positive nontrivial answer would still need a derivation of the
arithmetic transfer and its pole and prime contributions, and an
independent contraction statement for all support lengths. The change
from \(n_\gamma\) to \(G_o\) is already a concrete matching requirement.
Nothing here proves RH or identifies Loewner capacity with the shift.

## 11. Checks and statement ledger

[check_reflected_junction.py](../numerics/check_reflected_junction.py) and
its [record](../numerics/records/reflected-junction-checks.json) add 67
passing cases, bringing the package to 268. The checks cover reflected
ordered transport, the reference color contraction, independent Clifford
nullspaces, free positive and twisted negative forms, a gauge-invariant
odd-H control, reference tangents, bounded local exchange, the exact
quadratic coefficient, independent quadrature and a nilpotent-charge
norm counterexample. Direct-square quadrature was refined from 320 to
640 points per axis to control its corner error; transformed quadrature
uses 32 and 64 Gauss points. These are diagnostics, not quantum proofs.

| Statement | Status |
|---|---|
| Reflected map is \(-MR\), with the color gluing (2.3) | Exact classical identities; ordered-matrix and gauge-frame checks |
| Regulated pairing is positive | Conditional on an OS-positive regulator in the stated color sector and admissible operators |
| Free positive-time endpoint kernel is (3.1), giving \(G_o\) on a ray | Derived free-field result |
| Ket and ordinary reflected branch have no common constant charge for this curved family | Written projector argument; straight-time bulk control |
| Displayed R rotation restores the map but not endpoint positivity | Exact free endpoint counterexample with ordinary-adjoint control |
| Odd-H normal reflection fails on the full canonical free bulk algebra | Explicit Gaussian and gauge-invariant cubic counterexamples; not a classification of defect reflections |
| Time-normal reference tangent gives a regular leading bulk join | Classical geometry and local integrability; full defect renormalization open |
| Direct bulk response has coefficient \(3/2-2\log2\) | Derived analytically; independent finite quadrature |
| Full first-order quantum response and protection | Open |
| Arithmetic realization, all-length contraction, RH | Not obtained |
| Independent review of this package | None recorded |

See [the third continuation](CONTINUATION_20260919_SESSION3.md) for the
current handoff. Parent manuscripts and their historical claims have not
been rewritten.
