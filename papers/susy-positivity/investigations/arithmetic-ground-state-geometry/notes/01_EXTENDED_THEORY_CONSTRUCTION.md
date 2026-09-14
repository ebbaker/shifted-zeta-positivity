# An actual four-supercharge enlargement of the gamma–one-prime benchmark

This note constructs positive enlarged quantum theories, computes their holomorphic boundary periods, and tests elementary interactions. The complete finite-interval Weil form has not been obtained. The constructions below are new deductions for this investigation; the cited references supply the supersymmetric and analytic frameworks.

## 1. Result and distinctions

There is an explicit four-real-supercharge enlargement of the Morse control: replace its real coordinate by a flat complex cylinder. Its positive Hamiltonian has an added angular boson and an enlarged fermion sector. Its physical vacuum is a middle-degree differential form, not the old scalar Morse wavefunction. A noncompact Witten-complex argument gives one normalizable vacuum at nonzero coupling, but does not identify its Hermitian norm with a gamma function.

Adding two complex quadratic fields gives an exact one-prime gamma/Euler **holomorphic period**. Their physical oscillator vacua also give the Euler metric |1-q| to the minus two in an explicitly specified holomorphic frame. This is a genuine four-supercharge theory on an enlarged field space, not a formal Clifford doubling of the old Hamiltonian. It remains a benchmark: the full gamma/Euler period is not the physical ground-state pairing, and the Euler metric alone has flat curvature away from its singular point.

A natural interaction between the gamma coordinate and the prime mass fails two analytic tests. It changes the complete period and produces a noncompact critical manifold. A different quartic prime sector is a viable interacting replacement with nine isolated vacua and a well-defined positive matrix geometry. Its simplest boundary period also changes, so a new physically specified boundary state or metric identity is required. These results select a concrete next theory rather than establishing arithmetic positivity.

## 2. Four charges on the flat cylinder

Let Y=y+i theta with theta identified modulo 2pi, and use the complete flat metric dy squared+dtheta squared. The physical Hilbert space is

\[
\mathscr H=L^2\Omega^*(\mathbb R\times S^1),
\]

with its ordinary positive metric on differential forms. Exterior multiplication by dy and dtheta is denoted by Ey,Etheta; their Hilbert adjoints are Iy,Itheta. Start with

\[
\mathcal W_a(Y)=\frac12(e^Y-aY),\qquad h=\Re\mathcal W_a.
\]

For real a,

\[
h(y,\theta)=\frac12(e^y\cos\theta-ay),\qquad
\Delta h=0.
\]

Define the two complex charges on compactly supported smooth periodic forms by

\[
\begin{split}
Q_1&=E_y(\partial_y+h_y)+E_\theta(\partial_\theta+h_\theta),\\
Q_2&=-E_y(\partial_\theta-h_\theta)+E_\theta(\partial_y-h_y).
\end{split}
\]

Thus Q1=d+dh wedge and Q2=d^c-d^c h wedge, with d^c=Etheta partialy-Ey partialtheta. Their adjoints use the same physical metric:

\[
\begin{split}
Q_1^\dagger&=I_y(-\partial_y+h_y)+I_\theta(-\partial_\theta+h_\theta),\\
Q_2^\dagger&=I_y(\partial_\theta+h_\theta)+I_\theta(-\partial_y-h_y).
\end{split}
\]

An exact exterior-algebra calculation gives

\[
Q_1^2=Q_2^2=0,\qquad
\{Q_1,Q_2\}=-2(\Delta h)E_yE_\theta,\qquad
\{Q_1,Q_2^\dagger\}=0,
\]

\[
\{Q_1,Q_1^\dagger\}-\{Q_2,Q_2^\dagger\}
=2(\Delta h)(N-1),\qquad N=E_yI_y+E_\theta I_\theta.
\]

Harmonicity therefore gives a common Hamiltonian H and four real charges

\[
R_1=Q_1+Q_1^\dagger,\quad R_2=i(Q_1-Q_1^\dagger),\quad
R_3=Q_2+Q_2^\dagger,\quad R_4=i(Q_2-Q_2^\dagger),
\]

\[
\{R_i,R_j\}=2\delta_{ij}H,\qquad H\ge0.
\]

In particular

\[
H=-\partial_y^2-\partial_\theta^2
+\frac14|e^Y-a|^2
+e^y\!\left[\cos\theta(E_yI_y-E_\theta I_\theta)
-\sin\theta(E_yI_\theta+E_\theta I_y)\right]
\]

for real a; for complex a the same formula holds with the displayed absolute-square potential. The exponential and Yukawa couplings are nonlinear. Positivity follows from the supercharges, without estimates of the desired arithmetic form.

The associated Euclidean coherent-state action, in the Hamiltonian normalization above, is

\[
S_E=\int dt\left[
\frac14(\dot y^2+\dot\theta^2)+|\nabla h|^2
+\bar c_i\dot c_i+2\bar c_i h_{ij}c_j\right].
\]

The fermion expression uses normal ordering and Delta h=0. Equivalently this is the quantum-mechanical Kähler/Landau–Ginzburg realization of a holomorphic superpotential. Fermionic path-integral weights need not be pointwise positive; the Hilbert adjoint and the Hamiltonian square provide the positivity relevant here.

### Closed realization

The algebra just displayed is first an identity on the common smooth compact-support core. It admits a positive self-adjoint realization, rather than relying only on formal integration by parts.

Each real charge is a Dirac-type first-order operator plus a smooth Hermitian multiplication potential on a complete flat manifold. Choose real cutoffs chiR approaching one with compact support and |dchiR| bounded by C/R. Multiplication potentials commute with chiR, and the commutator of a real charge with chiR is bounded by C/R. If Rstar psi=plus or minus i psi, elliptic local regularity permits the usual cutoff identity. Taking its imaginary part gives

\[
\|\chi_R\psi\|^2
\le \frac C R\|\chi_R\psi\|\,\|\psi\|.
\]

The limit forces psi=0, so the deficiency spaces vanish. This proves essential self-adjointness of each real charge. On the core their squared graph norms coincide; taking closures gives identical closed quadratic forms and hence the same nonnegative H. The same argument applies to real linear combinations of the charges. Their squared-form identities recover the standard algebra on the common Hamiltonian domain. The argument also applies on cylinder times a finite-dimensional complex vector space with the complete flat metric.

For the original real-a cylinder, these domain conclusions also fall within the noncompact Witten-operator framework of [Dai and Yan](https://arxiv.org/abs/2005.04607).

## 3. Why this is not the old Morse Hamiltonian

Along theta=0, h has the old real Morse function (e^y-ay)/2. This is only a real slice of the superpotential. It is not a quantum reduction of H.

On zero-forms the cylinder Hamiltonian contains no negative scalar Hessian term because Delta h=0. The old real-line Morse Hamiltonian instead contains minus e^y/2. On one-forms the full cylinder Hessian has eigenvalues plus or minus e^y, not minus e^y/2. Freezing theta is not an invariant Hilbert subspace; a delta-supported angular wavefunction is not an L2 state.

The trial scalar zero state exp(-h) also fails globally. Near theta=pi and y tending to plus infinity, h tends to minus infinity exponentially, so exp(-h) is not square integrable. The top-degree candidate exp(h) diverges near theta=0. A physical zero state must be a one-form

\[
\alpha=P(y,\theta)dy+Q(y,\theta)d\theta
\]

satisfying

\[
\partial_yQ-\partial_\theta P+h_yQ-h_\theta P=0,
\]

\[
-\partial_yP-\partial_\theta Q+h_yP+h_\theta Q=0.
\]

These are coupled equations on the full cylinder. Their solution's norm has not been evaluated in this note.

### Existence and count are separate from the norm

For real a>0, h has exactly one critical point, at y=log a, theta=0, with one positive and one negative Hessian eigenvalue. It is well tame in the sense needed for noncompact Witten deformation:

\[
\liminf_{|y|\to\infty}|dh|=a/2>0,
\qquad
\frac{|\operatorname{Hess}h|}{|dh|^2}\longrightarrow0
\]

at both ends. The cylinder has bounded geometry. The strong Morse inequalities of [Dai and Yan](https://arxiv.org/abs/2005.04607), including their equality for the alternating sum, therefore give graded Dirac index minus one for sufficiently large T. This uses their well-tame Morse hypotheses; it does not require their additional Thom–Smale identification or a gradient-flow transversality argument.

This count extends to every T>0. At the negative end the squared operator tends to a Laplacian plus T squared a squared/4; at the positive end T squared |dh| squared dominates the Hessian. The graded Dirac operator is consequently Fredholm throughout T>0. On compact T intervals away from zero these end estimates are uniform and the graph domains are equivalent, so its Fredholm index is constant. The degree-zero and degree-two Hamiltonians are both

\[
-\Delta+T^2|dh|^2.
\]

They have no zero states, since zero energy would require both a constant L2 function and |dh| times that function to vanish. There is therefore exactly one normalizable one-form vacuum. This is an existence/counting argument, not an evaluation of its metric and not an arithmetic positivity argument.

## 4. Global parameter type and the gamma period

For a=aR+i aI, h is only locally defined on the cylinder:

\[
h=\frac12(e^y\cos\theta-a_Ry+a_I\theta),\qquad
h(y,\theta+2\pi)-h(y,\theta)=\pi a_I.
\]

Nevertheless the real closed one-form alpha=dh is globally smooth and periodic. Both charges use alpha and its complex-structure rotation, so the physical Hamiltonian remains well defined on periodic forms. The deformation is not globally conjugation by a single-valued exp(h). For complex a the same Fredholm end estimates hold when a is nonzero. Varying a changes alpha by a bounded constant one-form, so index continuation from positive real a gives the same one-vacuum count on C excluding zero. Even-sector kernels remain absent. At a=0 the end gap closes and this continuation argument does not apply.

Locally a is a holomorphic superpotential parameter. Globally, the proposed chiral insertion partiala W=-Y/2 is multivalued. Consequently this is periodic Landau–Ginzburg data, not automatically an ordinary rank-one chiral tt* system. One can instead work on the covering plane, record deck translations and Bloch data, or include the corresponding flavor/monodromy structure. The periodic model studied by [Cecotti, Gaiotto, and Vafa](https://arxiv.org/html/1312.1008v1#S3.SS1) is the relevant literature precedent; their physical metric and their limiting brane amplitudes are different objects.

There is also a direct local constraint on the particular Hilbert realization chosen here. Its Hamiltonian has real coefficients on differential forms for every complex a. A unique isolated vacuum therefore admits a real normalized representative locally in parameter space. For that representative, its ordinary Berry connection is zero: reality and differentiation of unit norm give inner product of psi with dpsi equal to zero. Thus the one-line connection P d has zero local curvature, although global sign holonomy is possible. A gamma-dependent scalar metric would require a specified nonunit holomorphic/source frame; it cannot be inferred as nonzero ordinary Berry curvature of this line. Additional deck/flavor data or a different parameter connection would be extra structure requiring a new derivation.

The real integration path theta=0 does define a convergent holomorphic period for Re a>0:

\[
\mathcal P_\gamma(a)=\int_{\mathbb R}e^{-2\mathcal W_a(Y)}dY
=\int_0^\infty t^{a-1}e^{-t}dt=\Gamma(a).
\]

Here the factor two in the exponent is part of the specified period normalization. For complex a, the real path is a convergent relative cycle and need not itself be a steepest-descent thimble. Such holomorphic periods are the topological/asymmetric brane quantities described by relative cycles; this integral is not the finite-coupling physical Hermitian overlap of the one-form vacuum. Gamma therefore survives the enlargement in a precisely identified observable, while the physical metric remains a new calculation.

## 5. An exact four-supercharge gamma/Euler period

Fix one prime p and independent parameters a and q with Re a>0 and |q|<1. Add two complex fields U,V with flat Kähler metric and set M=1-q. On cylinder times C squared take

\[
\mathcal W_{a,q}(Y,U,V)
=\frac12\left[e^Y-aY+\frac M2(U^2+V^2)\right].
\]

The same construction with h=Re W in six real dimensions gives four real supercharges. In higher dimension the needed condition is pluriharmonicity, or equivalently the Hessian anticommuting with the flat complex structure; it holds because W is holomorphic. The bosonic potential is explicitly

\[
|\nabla h|^2
=\frac14|e^Y-a|^2
+\frac{|M|^2}{4}(|U|^2+|V|^2).
\]

The quadratic complex factors each have a unique middle-degree oscillator vacuum. Combined with the cylinder this gives one vacuum with the periodic form boundary condition already specified around the cylinder. Unlike the old control, this uses six real bosons and their differential-form fermions; the positive-energy multiplets genuinely have the field content for four charges.

Specify the integration cycle by real Y,U,V and normalize its U,V measure by 1/(2pi). Since Re M>0, direct Gaussian integration gives

\[
\frac1{2\pi}\int_{\mathbb R^3}
e^{-2\mathcal W_{a,q}}dYdUdV
=\frac{\Gamma(a)}{1-q}.
\]

On the arithmetic parameter locus a=z/2, q=p to the minus z, include the explicit source prefactor pi to the minus z/2. The result is

\[
\mathcal P_p(z)=
\pi^{-z/2}\Gamma(z/2)(1-p^{-z})^{-1},\qquad \Re z>0.
\]

Every integral converges in this domain. The relation is an exact holomorphic-period identity. The source prefactor and integration cycle are specified, rather than inferred from positivity. The parameter q is an ordinary chiral mass parameter of the quadratic sector; a retains the periodic subtlety above. Im z, or the arithmetic Fourier variable tau, is not thereby identified with a physical Euclidean time or a single ordinary chiral coordinate of the full global model.

### The Euler factor also occurs in a specified physical vacuum metric

The oscillator calculation can be completed exactly. For one complex field U=x+iy with superpotential M U squared/4, write M=r exp(i phi), r>0, and rotate U to U'=exp(i phi/2)U=x'+iy'. Then

\[
h_U=\frac r4(x'^2-y'^2),\qquad
\psi_M=e^{-r|U|^2/4}\,dy'
\]

is a normalizable one-form annihilated by Q1 and its adjoint. The scalar Gaussian contribution is r to the oscillator energy; the occupied negative Hessian direction contributes minus r. Its squared norm in the ordinary flat measure is 2pi/r. This also proves the claimed uniqueness, since the other oscillator states have positive energy.

To specify the parameter frame rather than only its norm, set

\[
s_M=(2\pi)^{-1/2}e^{-i\phi/2}\psi_M
=\frac{e^{-r|U|^2/4}}{2i\sqrt{2\pi}}
\left(dU-\frac{\bar M}{|M|}d\bar U\right).
\]

This formula is single valued for M nonzero. If P is the physical ground-state projector, its induced anti-holomorphic connection obeys P partialbarM sM=0. Indeed the normalized real ground state proportional to sqrt(r) psiM has zero local Berry connection, while its coefficient in sM is M to the minus one-half. Thus sM is a holomorphic ground-line frame for the projected connection, and

\[
g_U=\langle s_M,s_M\rangle=|M|^{-1},\qquad
g_{UV}=|M|^{-2}=|1-q|^{-2}.
\]

The coefficient of dU in the displayed harmonic representative and the constant 1/sqrt(2pi) fix our frame normalization explicitly. The tensor-product theory consequently has a physical vacuum metric ggamma(a,bar a) times |1-q| to the minus two in the tensor frame, where ggamma has not been calculated. Its holomorphic period is instead Gamma(a)/(1-q). No equality between these two full quantities has been established.

There is a decisive limitation. Log gUV is pluriharmonic for M nonzero, so this Euler metric has zero local curvature. Multiplying the two-field holomorphic frame by M gives unit metric on this domain. Therefore the displayed denominator is meaningful relative to its specified source/frame normalization; positivity alone does not select that normalization. At M=0 the oscillator confinement and normalizable vacuum disappear, so the excluded singular point also has a physical meaning. The projected chiral mass operator is zero in the one-vacuum Jacobi ring, consistently with the scalar flat tt* equation.

This elementary construction is deliberately a benchmark. Its external parameters are prescribed jointly, but its sectors do not interact dynamically. Its periods and oscillator metric produce local factors without a new theorem converting their logarithmic derivative into a positive norm. In particular it does not address the contact normalization or the poles of the Weil form.

## 6. A natural gamma–prime interaction fails two exact tests

The simplest holomorphic mass coupling is

\[
\mathcal W^{\lambda}_{a,q}
=\frac12\left[e^Y-aY+
\frac{M+\lambda e^Y}{2}(U^2+V^2)\right].
\]

For real a>0, 0<q<1 and lambda>0 its real-cycle period is still convergent. Integrating U,V exactly gives

\[
\mathcal P_\lambda(a,q)
=\int_0^\infty\frac{t^{a-1}e^{-t}}{M+\lambda t}\,dt
<\frac{\Gamma(a)}M.
\]

The strict inequality is an analytic identity test on the positive real locus, not a numerical estimate. The first derivative at lambda=0 is

\[
\left.\partial_\lambda\mathcal P_\lambda\right|_0
=-\frac{\Gamma(a+1)}{M^2}.
\]

Thus even the full elementary boundary amplitude changes immediately.

There is a separate physical failure invisible on that real cycle. In the complex field space the mass vanishes at t0=-M/lambda. The critical-point equations then allow

\[
e^Y=t_0,\qquad
U^2+V^2=\frac{2(a-t_0)}{\lambda t_0}.
\]

This is a noncompact complex quadric, not isolated massive vacua. Its existence is exact; for example write (U+iV)(U-iV) equal to the displayed constant and let one factor become arbitrarily large. A standard finite-rank massive vacuum bundle cannot be assumed for this coupling. The real contour's convergent Gaussian integral does not repair the physical critical manifold elsewhere in the complex target.

A broader period statement is also available. Suppose M(t,q) is a nonvanishing mass on the positive contour, with sufficient growth conditions for Mellin inversion. If one requires

\[
\int_0^\infty t^{a-1}e^{-t}M(t,q)^{-1}dt
=\frac{\Gamma(a)}{1-q}
\]

throughout an open Mellin strip for independent a and q, uniqueness of the Mellin transform forces M(t,q)=1-q almost everywhere on that contour. Thus a nontrivial Y-dependent quadratic mass cannot preserve this entire factorized period in that class. This argument does not cover matching only on the linked arithmetic locus q=p to the minus 2a, other boundary insertions, or nonquadratic prime fields.

## 7. A viable interacting prime sector with room for matrix tt* geometry

The preceding critical-manifold failure suggests replacing the quadratic prime sector by a controlled polynomial interaction rather than merely making its mass depend on Y. Consider

\[
F_{M,g,\lambda}(U,V)
=\frac M2(U^2+V^2)+\frac g4(U^4+V^4)
+\frac\lambda2U^2V^2,
\]

and

\[
\mathcal W=\frac12[e^Y-aY+F_{M,g,\lambda}(U,V)].
\]

Take M nonzero, g>0 and lambda=g/2 as a definite starting model. The cross quartic is an interaction between the two complex prime fields. It is not a Gaussian mass replacement.

The critical equations of F are

\[
U(M+gU^2+\lambda V^2)=0,\qquad
V(M+gV^2+\lambda U^2)=0.
\]

They have exactly nine points: the origin; two points on each coordinate axis with the nonzero coordinate squared equal to minus M/g; and four points with

\[
U^2=V^2=-M/(g+\lambda).
\]

All are nondegenerate. At an axis point the Hessian determinant is minus 2M squared times (1-lambda/g). At a both-nonzero point it is

\[
4(g^2-\lambda^2)U^2V^2,
\]

which is nonzero for the chosen parameters.

The degree-four homogeneous part has no gradient zero on the complex unit sphere when g squared differs from lambda squared. Therefore its gradient has a positive minimum there, implying

\[
|\nabla F|\ge cR^3-CR,\qquad
|\operatorname{Hess}F|\le C(1+R^2).
\]

This proves strong tameness: the gradient square dominates any fixed multiple of the Hessian at infinity. The prime-sector twisted Laplacian has discrete spectrum, and its middle-degree vacuum space has dimension nine by the strongly tame Kähler/Stein Hodge theorem of [Fan](https://arxiv.org/abs/1107.1290). This is precisely the setting where the Jacobi-ring representation and its positive physical metric have an analytic foundation; it is not an index count substituted for that metric.

For the stated superpotential normalization, the projected operator associated with M is multiplication by partialM W=(U squared+V squared)/4. Its values in the critical-point basis are zero, minus M/(4g), and minus M/[2(g+lambda)], with multiplicities one, four, and four. It is therefore not forced to be scalar. The earlier rank-one commutator obstruction no longer applies. Under admissible deformations the ground-state metric can satisfy a nontrivial matrix tt* system, as in the general four-supercharge framework of [Sonner and Tong](https://arxiv.org/abs/0810.1280).

This model does not preserve the simple Euler period. For positive real M,g,lambda,

\[
\frac1{2\pi}\int_{\mathbb R^2}e^{-F_{M,g,\lambda}}dUdV
<\frac1M.
\]

The real-cycle suppression is strict. Nor is the g tending to zero limit uniform on the vacuum space: eight critical points escape to infinity. It is not a fixed-rank protected deformation from the quadratic theory. These are constraints on any proposed arithmetic boundary state.

The cylinder is still dynamically independent in this first controlled model. Its role is to retain a known gamma period and the necessary periodic parameter structure while a genuine multi-vacuum prime sector is studied. Coupling the sectors is a subsequent problem; the failed affine mass coupling shows why it should not be done without checking the full complex critical geometry.

## 8. What has been achieved and the next construction test

This pass supplies an actual positive four-supercharge cylinder theory, an existence argument for its normalizable vacuum, an exact gamma/one-prime holomorphic period in an enlarged theory, and an exact Euler physical metric in a specified holomorphic oscillator frame. It also gives two analytic exclusions for a simple coupling and a concrete interacting replacement with a nine-dimensional physical vacuum metric. It does not compute the cylinder or quartic metric, identify a boundary norm with the Weil form, fix the arithmetic contact, or supply the poles.

The next useful analytical task is to derive the Jacobi-ring matrices, allowed physical boundary states, and full tt* equations for the nine-vacuum prime sector, retaining the periodic gamma factor. Determine whether a physically fixed combination of boundary states has an arithmetic meaning and whether its Hermitian pairing supplies more than the already known holomorphic period. A boundary combination fitted from the desired answer would not count.

A successful proposal must eventually retain an infinite-dimensional input space. Nine vacua alone cannot represent all test functions; the full periodic/boundary-field construction must supply that space and the prime-return singularities. Numerical calculations are best used after such a complete pairing has been specified, as checks on the resulting structural identities.
