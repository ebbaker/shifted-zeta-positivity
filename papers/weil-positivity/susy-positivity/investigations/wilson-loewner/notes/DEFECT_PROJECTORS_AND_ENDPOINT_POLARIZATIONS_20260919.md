# Defect-compatible contour freedom and the endpoint pairing

19 September 2026, second calculation. OpenAI GPT-6 (Codex), for Edward Baker.

**Status:** written classical supersymmetry and endpoint-polarization
derivations, with 99 finite matrix and polarization checks. A nonzero common
complex charge exists for the tangent-coupled contours, including a family
over all defect directions. The two scalar endpoints annihilated by that
same charge have zero mutual free contraction. Their complete Wilson
bilinear has nonzero residual R charge, so its expectation vanishes in an
invariant vacuum with a symmetry-preserving definition of the operator.
This solves a restricted endpoint test; it supplies neither a nonzero
positive quantum kernel nor an arithmetic evolution.

**Subsequent calculation:** [the reflection note](REFLECTION_JUNCTION_AND_BULK_RESPONSE_20260919.md)
now derives the ordinary reflected map and a smooth reference join, with
a first direct bulk response. This note retains its second-calculation
status and scoped endpoint conclusions.

This continues [the first calculation](SMOOTH_VARIATION_AND_CONSTANT_DRIVER_20260919.md),
Section 6, and carries out [its proposed next calculation](CONTINUATION_20260919.md).
The conclusion concerns a constant real scalar map, a constant Poincare
charge, ordinary fundamental/antifundamental scalar endpoints and a single
bosonic Wilson connection. It does not classify superconnections, extra
junction matter, conformal Killing spinors, or reflected state networks.

## 1. The defect and the ansatz

Use Euclidean spacetime coordinates \(x^0,x^1,x^2,x^3\), with defect
\(x^3=0\). The internal directions \(4,5,6\) form the \(SU(2)_H\)
scalar triplet, and \(7,8,9\) form the \(SU(2)_V\) triplet. Write
the corresponding scalar fields as \(X_A\). Work in the complexification
of the physical supersymmetry algebra, with

\[
\{\Gamma_A,\Gamma_B\}=2\delta_{AB},\qquad
\chi=-i\Gamma_0\Gamma_1\cdots\Gamma_9,\qquad
D=\Gamma_3\Gamma_4\Gamma_5\Gamma_6.
\tag{1.1}
\]

Our chirality and defect conventions are

\[
\chi\epsilon=\epsilon,\qquad D\epsilon=\epsilon.
\tag{1.2}
\]

The second condition is the unfluxed D3-D5 supersymmetry projector. Its
definition and brane derivation are in
[Gaiotto--Witten, (2.7), (4.1)--(4.3), and (4.9)](https://arxiv.org/pdf/0804.2902).
The brane derivation applies to the intersection before their subsequent
specialization to terminating D3-branes. We use that common supersymmetry
projector, **not** the terminating-brane boundary conditions or Nahm pole.
Wick rotation leaves \(D\) unchanged; (1.1) fixes the Euclidean chirality
sign. Complex dimensions below are not counts of real Euclidean
Majorana--Weyl spinors.

For a regular contour in the \((x^1,x^3)\)-plane, take

\[
\mathcal A=iA_1\,dx^1+iA_3\,dx^3+X_8\,dx^1+X_6\,dx^3.
\tag{1.3}
\]

Thus the scalar unit vector is
\(n=(\dot x^1 e_8+\dot x^3 e_6)/|\dot x|\).
The scalar coupling changes sign with the oriented tangent. It is not
the old coupling \(X_6|dx|\). The local bulk condition is

\[
\bigl[\dot x^1(i\Gamma_1+\Gamma_8)
       +\dot x^3(i\Gamma_3+\Gamma_6)\bigr]\epsilon=0.
\tag{1.4}
\]

We ask for one constant nonzero \(\epsilon\), independent of position,
tangent and contour. Endpoints lie on the defect. A Loewner trace stopped
at an interior tip still requires an additional color state there; this
calculation does not make a defect scalar available in the bulk.

## 2. Compatibility with the defect

Define

\[
K_1=i\Gamma_8\Gamma_1,\qquad K_n=i\Gamma_6\Gamma_3.
\tag{2.1}
\]

Both are involutions. Equation (1.4) holds for every planar tangent if

\[
K_1\epsilon=-\epsilon,\qquad K_n\epsilon=-\epsilon.
\tag{2.2}
\]

The four involutions \(\chi,D,K_1,K_n\) commute, and their common projector is

\[
P_{\rm plane}=\frac1{16}(1+\chi)(1+D)(1-K_1)(1-K_n).
\tag{2.3}
\]

**Proposition 2.1.** The image of (2.3) has complex dimension two.
Every spinor in it satisfies the chiral defect condition and the bulk
line condition for every regular planar contour with coupling (1.3).

*Proof.* The factors are commuting Hermitian involution projectors. In the
32-dimensional complex Clifford module, every nonidentity monomial in
the expansion of (2.3) has zero trace, and no nonempty product of these
four generators is a scalar. Thus \(\operatorname{tr}P_{\rm plane}=32/16=2\).
Multiplying (2.2) by the appropriate internal gamma matrix gives
\((i\Gamma_1+\Gamma_8)\epsilon=(i\Gamma_3+\Gamma_6)\epsilon=0\).
Linearity proves (1.4). \(\square\)

The triplet assignments matter. \(D\) commutes with a spacetime tangent
gamma and with a V gamma, and anticommutes with the normal gamma and
with an H gamma. Consequently a tangent paired to an H scalar, or a
normal paired to a V scalar, gives a BPS involution anticommuting with
\(D\); it cannot have a nonzero simultaneous eigenspinor with \(D\).

More generally, for an independently variable defect tangent in a
constant real scalar map, split its scalar vector into H and V parts.
The wrong H part of its BPS equation lies in the opposite \(D\)-eigenspace
from the other terms and must annihilate \(\epsilon\) separately. Its
gamma matrix squares to the squared Euclidean norm of that real vector,
so it is invertible unless the vector is zero. The normal-direction
argument exchanges H and V. Thus the respective pure V and pure H
assignments are necessary in this ansatz. Complex null scalar vectors
and couplings required only along one constrained tangent are outside
this argument.

The nonzero projector (2.3) is the positive control for these exclusions.

## 3. One charge for all defect directions

The angular family in the parent investigation motivates a stronger
test. Put

\[
K_\mu^{(s)}=i s_\mu\Gamma_{7+\mu}\Gamma_\mu,
\qquad\mu=0,1,2,\qquad s_\mu\in\{+1,-1\}.
\tag{3.1}
\]

These are the tangent projectors for the V-valued isometry
\(M=\operatorname{diag}(s_0,s_1,s_2)\). All commute with each other,
\(D,\chi\), and \(K_n\). Direct Clifford multiplication gives

\[
K_0^{(s)}K_1^{(s)}K_2^{(s)}=(\det M)\chi D.
\tag{3.2}
\]

For conventions \(\chi\epsilon=c\epsilon\), \(D\epsilon=d\epsilon\),
requiring all three tangent eigenvalues to be \(-1\) therefore requires

\[
\det M=-cd.
\tag{3.3}
\]

With this sign, only two of the three tangent conditions are independent.
Together with chirality, defect and normal conditions, there are five
independent commuting projections. Their common image has complex
dimension \(32/2^5=1\). With the opposite determinant it is zero.
Orthogonal changes of frames extend the statement to an arbitrary real
isometry between the two oriented three-dimensional spaces. The determinant
condition depends on the displayed chirality and frame conventions; the
existence of a suitable map does not.

For \(c=d=+1\), one explicit choice is

\[
\mathcal A=iA_\mu dx^\mu+iA_3dx^3
             -X_7dx^0+X_8dx^1+X_9dx^2+X_6dx^3,
\qquad \mu=0,1,2.
\tag{3.4}
\]

The same nonzero complex charge works for every tangent in four-dimensional
Euclidean space with this coupling, and hence for contours in every
normal plane indexed by \(\Omega\in S^2\). This includes the Euclidean
continuation of the time direction. It is not a claim about arbitrary
real Lorentzian trajectories with real scalar couplings.

The correct determinant is the positive control for the zero-rank
opposite-orientation choice. There is no angular-family obstruction at
this classical projector level.

## 4. The normal projector fixes one H weight

Let

\[
T_H=i\Gamma_4\Gamma_5.
\tag{4.1}
\]

It is twice a Cartan generator, up to the choice of generator versus
spinor-parameter convention. The exact matrix identity

\[
D=K_nT_H
\tag{4.2}
\]

implies \(T_H\epsilon=-\epsilon\) under (1.2) and (2.2).
The tangent projectors reduce the remaining spacetime/V spinor freedom
but never introduce the other H weight. Thus every surviving charge
has a fixed H factor. Since the charge is Poincare, that factor is the
same at both endpoints.

Label the preserved generator by \(Q_{i2}\) for the normal combination
\(iA_3+X_6\), matching Baker's generator labels. The conjugate orientation
exchanges 1 and 2. The corresponding spinor parameter and generator are
paired by charge conjugation; their index placement should not be inferred
from the gamma-matrix eigenvalue alone.

## 5. Endpoint conditions and the vanishing pairing

The physical hypermultiplet has fundamental scalars \(q_m\) and their
antifundamental conjugates \(\bar q_m\), with \(m=1,2\) an H index.
The starting transformations and conjugation convention are
[Baker, Appendix C, (79), (81)--(84), printed pp. 24--25](https://arxiv.org/pdf/1102.4948).
In his final choice for the plus normal coupling, the endpoints are
\(q_2\) and \(\bar q_1\); the conjugate orientation gives
\(q_1\) and \(\bar q_2\). The off-diagonal distinction is essential.

Here is the polarization calculation with spinor and V indices suppressed.
For a charge with H factor \(a=(a_1,a_2)^T\ne0\), define

\[
q(v)=v_mq_m,\qquad \bar q(w)=w_m\bar q_m,\qquad
E=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\tag{5.1}
\]

The H-invariant transformation tensors, in the generator convention just
specified, give

\[
Q(a)q(v)\ \propto\ (a^TEv)\Psi,\qquad
Q(a)\bar q(w)\ \propto\ (a^Tw)\widetilde\Psi.
\tag{5.2}
\]

The suppressed nonzero spinor/V coefficient does not change these scalar
annihilator conditions. Each must vanish as an operator, for arbitrary
fermion components. Equation (5.2) follows equivalently by starting with
\(Q_{i2}q_2=Q_{i2}\bar q_1=0\) and using the invariant antisymmetric
tensor for two fundamentals and the evaluation tensor for a fundamental
and its dual. Complexification does not make the actions on \(q\) and
\(\bar q\) independently adjustable: both are fixed by the same physical
superalgebra.

The two one-dimensional nullspaces are

\[
v=\lambda a,\qquad w=\mu Ea.
\tag{5.3}
\]

Since the free propagator has H tensor \(\delta_{mn}\), its endpoint factor is

\[
v^Tw=\lambda\mu\,a^TEa=0.
\tag{5.4}
\]

**Proposition 5.1.** For a nonzero constant charge of the fixed H weight
in Section 4, ordinary nonzero fundamental and antifundamental scalar
endpoints individually annihilated by that charge have zero mutual free
contraction. They cannot be a physical adjoint pair.

*Proof.* Equations (5.2)--(5.4) prove the first assertion. Physical
conjugation instead sets \(w=v^*\), giving
\(v^Tw=\|v\|^2>0\). For \(v=\lambda a\),
\(a^Tv^*=\lambda^*\|a\|^2\ne0\), so that antifundamental endpoint is
not annihilated by the same charge. \(\square\)

In the representative basis this reads

\[
Q_{i2}q_2=Q_{i2}\bar q_1=0,\qquad
\langle q_2\bar q_1\rangle_0=0,\qquad
\langle q_2\bar q_2\rangle_0\ne0,
\quad Q_{i2}\bar q_2\ne0.
\tag{5.5}
\]

The last two statements are the positive control. They demonstrate that
nonzero endpoint covariance is available, at the cost of this particular
common-charge condition. They do not by themselves prove positivity of a
dressed Wilson expectation.

For distinct endpoints, the two endpoint variations contain independent
fermion fields, so they cannot cancel each other as bare operator
identities. In our ansatz the line variation already vanishes separately.
An added boundary term, junction field, or fermionic superconnection could
change this argument and would need its own transformation law.

## 6. The complete bilinear is R charged

All the fields in (1.3) or (3.4) are neutral under the H rotation fixing
\(X_6\). Assign \(q_1,q_2\) the usual weights \(+\tfrac12,-\tfrac12\).
Then \(\bar q_1\) also has weight \(-\tfrac12\), and

\[
\mathcal O_C=\bar q_1(b)\,U_C\,q_2(a)
\quad\hbox{has H charge }-1.
\tag{6.1}
\]

Color index placement fixes the orientation of \(U_C\); it does not affect
this H charge. If the vacuum and regulator preserve this U(1),

\[
\langle\mathcal O_C\rangle
=e^{-i\alpha}\langle\mathcal O_C\rangle
\quad\hbox{for every }\alpha,
\qquad\therefore\quad\langle\mathcal O_C\rangle=0.
\tag{6.2}
\]

This is a symmetry selection rule, beyond the free cancellation (5.4).
It assumes a well-defined symmetry-covariant operator; it is not a proof
of its ultraviolet construction. A broken-symmetry vacuum, compensating
charged insertion or additional endpoint degrees of freedom changes the
problem. Fixed-endpoint shape variations of this same neutral connection
carry no compensating H charge and therefore cannot make (6.2) nonzero.

The ray endpoint selection is already present in Baker's Section 3.1.
Our calculation applies it to the defect-compatible tangent-coupled
contour family; no novelty claim is made for the selection rule.

## 7. Why the original semicircle is a successful control

For the upper semicircle parametrized as in the first note, (1.3) gives

\[
n_8(\theta)=-\sin\theta,\qquad n_6(\theta)=\cos\theta.
\tag{7.1}
\]

At the two endpoints, both the normal tangent and its scalar coefficient
reverse. Their relative sign stays fixed; so does the selected H weight.

The original constant-scalar semicircle instead uses \(X_6|dx|\).
Its normal tangent reverses while its scalar coefficient stays positive.
The local H weight can therefore change between the two ends through a
position-dependent conformal Killing spinor. Baker's (29)--(30) realizes
a same-polarization endpoint pair, with leading normalized expectation
\(g^2/(4\pi|a-b|)\). This is a nonzero supersymmetric open-line control,
outside the constant-Poincare, constant-map hypotheses of Proposition 5.1.

| Construction | Contour condition established here or in the first note | Endpoint outcome |
|---|---|---|
| Inherited constant scalar and common special charge | Semicircles or their degenerate rays in one normal plane | The familiar conformal endpoint construction has a nonzero free contraction; a common positive network still needs its own proof |
| Constant tangent-to-scalar map and constant Poincare charge | Arbitrary smooth contours with the displayed projectors | Same-charge scalar endpoints are off-diagonal and their vacuum bilinear vanishes |
| Physical adjoint of a tangent-coupled endpoint state | No complete glued observable derived yet | Free endpoint overlap is nonzero; the bra is naturally closed by the conjugate charge |

This explains exactly what was traded for contour freedom. Supersymmetry
of each tangent survives, but the elementary same-charge two-endpoint
expectation cannot furnish the desired nonzero kernel.

## 8. Consequence for the Wilson--Loewner and RH programs

Loewner-generated smooth contour deformations can use (1.3) or (3.4)
without losing the common classical charge. That is a genuine improvement
over the fixed-scalar rigidity calculation. It is insufficient for the
program's positive kernel: the most direct same-charge scalar bilinear
is zero, and its shape response remains zero under the symmetry assumptions.

A more promising next calculation is to retain a \(Q\)-closed endpoint
state and pair it with its **physical adjoint**, whose natural charge is
\(Q^\dagger\). Derive the reflected connection and the color junction at
the reference point before claiming a Gram interpretation. The scalar
part of a Euclidean Wilson connection makes its ordered exponential
nonunitary, so reversal alone cannot be substituted for Hermitian adjoint.
One must determine which scalar signs and endpoint polarizations the
actual adjoint/reflection requires.

There is already a useful classical identity. For Hermitian matrix
backgrounds \(A,X\), real \(M\), and smooth regulated transport,

\[
U_M(C)^\dagger=U_{-M}(C^{-1}).
\tag{8.1}
\]

Taking the dagger reverses matrix order and changes \(iA+MX\) to
\(-iA+MX\). Traversing the reversed contour with scalar map \(-M\)
does exactly the same. Plain reversal with \(M\) unchanged instead
gives \(U_M(C)^{-1}\), generally different from the dagger. Equation
(8.1) is not yet an Osterwalder--Schrader reflection law: spacetime
reflection, field reflection, state support and the reference junction
must still be specified. In particular, the two branches need not be
one globally constant-map line covered by Proposition 5.1.

If that construction gives a positive state pairing, test whether the
smooth displacement insertion is exact for a compatible charge after
gluing, or whether it has a nontrivial unprotected response. A common
charge on the ket is not a protection theorem for the paired observable.
An R-twisted pairing is another possible definition, but its positivity
cannot be inherited from the physical adjoint without proof.

The parent free angular kernel has a nonzero adjoint polarization factor;
replacing it by the same-charge factor (5.4) would multiply it by zero.
Keeping the adjoint instead retains a free kernel independent of the
interior contour. Thus neither choice yet generates the arithmetic
transfer, its prime terms, the pole correction, or contraction for all
support lengths. Those remain the proof obligations recorded in the
[opening note](OPENING_NOTE_20260919.md).

## 9. Checks, sources and statement ledger

[check_defect_endpoints.py](../numerics/check_defect_endpoints.py) constructs
32-by-32 Jordan--Wigner gamma matrices and independently row-reduces the
simultaneous linear conditions. Its
[record](../numerics/records/defect-endpoint-checks.json) has 99 passing
cases: Clifford relations, chiral/defect projectors, wrong-triplet controls,
all eight orientation sign choices, one common charge across angular
directions, endpoint nullspaces, physical-adjoint controls and R-charge
phases, plus four adjoint/reversal checks with noncommuting matrix
backgrounds and a zero-scalar control. Together with the first note's 102 cases, the package has 201.

The finite checks support the displayed algebra. They do not numerically
establish a quantum Ward identity, reflection positivity or an RH theorem.
Primary printed equations were visually checked in Gaiotto--Witten,
pp. 7 and 74, and Baker, pp. 12--14 and 25; the brane derivation on
Gaiotto--Witten pp. 72--73 was also read. Third-party PDFs remain outside
this repository. This note continues the tangent prescription already
referenced to Zarembo in the first calculation; it claims no new general
classification of supersymmetric Wilson lines.

| Statement | Status |
|---|---|
| Planar tangent prescription has two complex chiral defect-compatible charges | Proved by the projector calculation under the displayed conventions |
| All defect directions share one complex charge for the required map orientation | Proved by (3.2)--(3.3); independent rank checks and wrong-orientation controls |
| Same-charge scalar endpoint pairing has zero free contraction | Proved from the physical hypermultiplet transformation tensors |
| Its complete bilinear has zero expectation | Exact symmetry implication, conditional on an invariant vacuum and a symmetry-preserving operator definition |
| Physical adjoint endpoint overlap is nonzero | Established at the free endpoint level; not a dressed-kernel positivity theorem |
| Reflected Wilson network, renormalization and compatible Ward identities | Open; next calculation |
| Arithmetic generator, all-length contraction, RH | Not obtained |
| Independent human or model review | None recorded for this package |

The [second continuation note](CONTINUATION_20260919_SESSION2.md) records
the next calculation and the limits that must be preserved.
