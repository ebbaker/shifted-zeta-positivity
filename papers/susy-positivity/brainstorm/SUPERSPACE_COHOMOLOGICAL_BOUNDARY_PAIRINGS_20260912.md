# Superspace, cohomological bulk symmetry, and positive arithmetic boundary pairings

**Companion brainstorming and continuation note · 12 September 2026**

**Status:** a proposed direction for the SUSY positivity research program. This note develops a possible combination of superspace fields, cohomological symmetry, and a positive boundary state pairing. It states conditional mathematical mechanisms and derives several elementary design constraints. It does not construct a superspace action or topological theory realizing the full Weil form, prove its all-length positivity, or establish RH.

This is a companion to [Topological bulk theories and exact boundary positivity](TOPOLOGICAL_BULK_BOUNDARY_POSITIVITY_20260912.md), especially its §§6–9. That note distinguishes extension independence, constrained energies, saturation, and positive gluing. The present note concentrates on how supersymmetry might make the pairing route useful, what a candidate theory would need, and how it could connect to the established gamma kinetic construction.

The authoritative normalization and form domains remain in the [shared background source](../background_section.tex) and [background PDF](../background.pdf). Other starting points are the [program overview](../PROGRAM_OVERVIEW.md), the [earlier superspace continuation](continuation-notes/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md), and the [positive-factorizations manuscript](../attempts/positive-factorizations/manuscript.tex). The continuation note was moved into `brainstorm/continuation-notes/`; use the links here for the current locations of its background references.

## 1. Where the discussion stands

The original proposal was to explain a quadratic form of a boundary input by a nonnegative bulk energy. If the bulk variables adjust to the fixed input, the boundary energy is their constrained minimum. The user then suggested that the bulk could be a superspace, and subsequently that a topological mechanism might make the relevant quantity independent of the bulk extension.

These suggestions fit together most naturally in the following proposed architecture:

> A supersymmetric bulk has an observable whose boundary pairing is unchanged by specified auxiliary bulk deformations. The pairing is an ordinary positive Hilbert pairing. Its dependence on the boundary coordinate retains the arithmetic data, and an independent calculation identifies it with the full Weil form.

Here “protected” will mean unchanged by those specified deformations as a consequence of a proved symmetry identity. It does not mean positive, independent of every variable, or already evaluated.

The preferred first investigation is this **positive boundary pairing route**. A **saturation route** is a useful second track, closer to the gamma auxiliary-field construction. Demanding equal classical energy for every unrestricted interior extension is a stronger requirement and is not the default proposal.

This preference is a research judgment, not a theorem that a particular field theory exists or that one approach will succeed.

## 2. The arithmetic problem to be represented

Fix a support length \(L>0\), set \(I_L=(-L/2,L/2)\), and take a possibly complex input \(f\in C_c^\infty(I_L)\). Its extension by zero to the real line is \(\widetilde f\). Use inner products conjugate-linear in the first argument, and define

\[
\widehat f(\tau)=\int_{I_L} f(x)e^{-i\tau x}\,dx,
\qquad
(T_a f)(x)=\widetilde f(x-a)\quad(x\in I_L, a>0).
\]

The linear pole amplitudes and the gamma multiplier are

\[
C(f)=\int_{I_L}f(x)\cosh(x/2)\,dx,
\qquad
S(f)=\int_{I_L}f(x)\sinh(x/2)\,dx,
\]

\[
m_\gamma(\tau)
=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi,
\qquad \psi=\Gamma'/\Gamma.
\]

With \(\Lambda\) the von Mangoldt function, the central form is

\[
\begin{aligned}
Q_{0,L}[f]={}&\frac1{2\pi}\int_{\mathbb R}
m_\gamma(\tau)|\widehat f(\tau)|^2\,d\tau
+2|C(f)|^2-2|S(f)|^2\\
&-\sum_{\substack{n\ge2\\\log n<L}}
\frac{\Lambda(n)}{\sqrt n}
\langle f,(T_{\log n}+T_{\log n}^*)f\rangle.
\end{aligned}
\]

Only prime powers contribute. The sum is finite for fixed \(L\); a delay of exactly \(L\) acts as zero. The subscript zero fixes the zeta shift at \(\omega=0\).

The associated Hermitian form, denoted \(q_{0,L}(g,f)\), is

\[
\begin{aligned}
q_{0,L}(g,f)={}&\frac1{2\pi}\int_{\mathbb R}
m_\gamma(\tau)\overline{\widehat g(\tau)}\widehat f(\tau)\,d\tau\\
&+2\overline{C(g)}C(f)-2\overline{S(g)}S(f)\\
&-\sum_{\substack{n\ge2\\\log n<L}}
\frac{\Lambda(n)}{\sqrt n}
\langle g,(T_{\log n}+T_{\log n}^*)f\rangle.
\end{aligned}
\]

Thus \(Q_{0,L}[f]=q_{0,L}(f,f)\). We reserve the different symbol \(\mathsf q\) below for an odd symmetry operator.

The background gives the classical criterion

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
Q_{0,L}[f]\ge0
\quad\text{for every }L>0\text{ and every }f\in C_c^\infty(I_L).
\]

Unboundedly many covered lengths suffice because every fixed compact support eventually fits. Nonnegativity is enough; a uniform positive gap is not required. The natural finite-interval form domain is

\[
\mathcal D_{\log,L}
=\left\{f\in L^2(I_L):
\int_{\mathbb R}\log(2+|\tau|)|\widehat f(\tau)|^2\,d\tau<\infty\right\}.
\]

The form is closed and semibounded there independently of the desired sign, and the smooth test functions are a core. A candidate should first state its identity on that core, then justify any domain extension. The program's shifted transfers offer a separate contraction route; this proposed first construction needs only the central form.

## 3. Distinct jobs for superspace, symmetry, and positivity

| Ingredient | Proposed job | What it does not establish by itself |
|---|---|---|
| Superfields and their component transformations | Specify even and odd degrees of freedom and how a chosen supersymmetry acts. | A positive energy, a physical Hilbert space, or an arithmetic identity. |
| Cohomological bulk symmetry | Prove invariance of a specified observable under allowed auxiliary changes. | Equality of energies on every classical field configuration. |
| A positive physical pairing | Turn a boundary state into a nonnegative quadratic functional. | The kernel, normalization, or prime weights of that functional. |
| Gluing and reflection | Compute a pairing by composing a preparation with its adjoint. | Positivity unless the pairing and adjoint operation satisfy the needed axioms. |
| Arithmetic labels and dynamics | Select the gamma spectrum, pole terms, and prime-delay couplings. | Positivity unless their joint realization has already supplied it. |

These jobs can interact without being identical. In particular, the operator whose expectation measures bulk excitation energy need not be the observable that represents the Weil form.

## 4. Geometry, superfields, and the meaning of the boundary input

### 4.1 Coordinates and the symmetry algebra

A schematic bulk has ordinary coordinates \(x\in\mathbb R\), \(y\ge0\), and odd coordinates \(\theta,\bar\theta\). One illustrative even superfield is

\[
\mathcal U(x,y,\theta,\bar\theta)
=u(x,y)+\theta\chi(x,y)+\bar\theta\widetilde\chi(x,y)
+\theta\bar\theta\,b(x,y).
\]

The components \(u,b\) are even and \(\chi,\widetilde\chi\) are odd. This is not a specified irreducible multiplet. The number of odd coordinates, conjugation, spin or form degrees, component transformations, and algebra must be chosen. A complex arithmetic input requires a compatible complex field or two real components with the correct Hermitian polarization.

An actual candidate must say whether its symmetry squares to zero, a gauge transformation, an ordinary translation, or a combination. If it uses a topological twist of a physical supersymmetry, it must specify the original algebra and the twist. Merely adjoining Grassmann coordinates does not make the dynamics supersymmetric. Superspace and component descriptions provide the general language for these choices. [Tong, *Superspace and superfields*, §3.1](https://www.damtp.cam.ac.uk/user/tong/susy/susy3.pdf)

The coordinates have separate roles:

- \(x\) carries the arithmetic translation structure.
- \(y\) is a proposed auxiliary direction.
- \(L\) limits the support of the input, not necessarily the physical size of the bulk.
- A channel index \(k\) can replace or supplement \(y\).
- Hamiltonian time, if needed, is another ordinary coordinate, denoted \(t\).
- The zeta shift \(\omega\) is an arithmetic family parameter. Identifying it with \(y\) or \(t\) would require a separate derivation.

Odd coordinates are algebraic directions. They do not provide an ordinary distance from the interval.

### 4.2 Prescribed component versus smeared insertion

There are two different uses of the same test function.

**Prescribed-component formulation.** Impose \(u(x,0)=\widetilde f(x)\). The trace selects this component on the full lower boundary. Other components, other edges, and infinity require additional conditions. A strip with lower edge \(I_L\) also needs side conditions. Arbitrary boundary forcing need not preserve supersymmetry; any symmetry used in the proof must survive the actual conditions or have its boundary variation explicitly accounted for.

**Insertion formulation.** Keep a specified background boundary condition and let \(f\) smear a boundary insertion. If \(\mathcal O_L(x)\) is an operator-valued distribution and \(\Omega_L\) is a reference state, set

\[
\Psi_L(f)=\mathcal O_L(f)\Omega_L,
\qquad
\mathcal O_L(f)=\int_{I_L} f(x)\mathcal O_L(x)\,dx.
\]

The integral is distributional; point operators need not create finite-norm states. The map \(f\mapsto\Psi_L(f)\) must be defined on every required test input and be linear. Here \(f\) specifies the amplitude of an insertion, rather than the boundary value of \(u\). The two formulations could be related in a specific model, but their equality is not assumed.

A general source-dependent path integral or normalized state is usually nonlinear in its source. The single smeared insertion is attractive because its linearity is explicit. An interacting theory can still have a quadratic norm of this linear state map; one does not need the entire generating functional to be Gaussian. Conversely, a Hessian of a complex effective action is not automatically this norm.

## 5. The primary target: an independently positive boundary pairing

For each \(L\), independently construct a positive Hilbert space \(\mathcal H_L\) and a linear map \(\Psi_L:C_c^\infty(I_L)\to\mathcal H_L\). Begin with a fixed input:

\[
f\longmapsto\Psi_L(f),
\qquad B_L[f]=\|\Psi_L(f)\|_{\mathcal H_L}^2.
\]

For two inputs define

\[
Z_L(g,f)=\langle\Psi_L(g),\Psi_L(f)\rangle_{\mathcal H_L}.
\]

The research target is the polarized identity

\[
\boxed{Z_L(g,f)\stackrel{\mathrm{target}}{=}q_{0,L}(g,f)
\quad\text{for all }f,g\in C_c^\infty(I_L).}
\]

This formulation tests cross terms as well as diagonal energies. Once it holds, \(Q_{0,L}[f]=\|\Psi_L(f)\|^2\ge0\). If it holds at unbounded lengths, the criterion in §2 applies. This is an elementary conditional implication, not an existence theorem for \(\Psi_L\).

If one writes \(A_L f=\Psi_L(f)\), then \(A_L\) is the boundary factor. Only after establishing a densely defined closed factor on the chosen input Hilbert space may one write the associated response operator as \(A_L^*A_L\). On its operator domain,

\[
q_{0,L}(g,f)=\langle g,A_L^*A_Lf\rangle.
\]

Here the original input has become implicit in the operator notation. The norm identity on test functions is the essential positivity statement; the operator realization carries further domain requirements.

### 5.1 What the two-point calculation must produce

In an insertion realization, the distributional kernel is schematically

\[
W_L(x,x')=\langle\Omega_L,
\mathcal O_L(x)^\dagger\mathcal O_L(x')\Omega_L\rangle,
\]

so that \(Z_L(g,f)\) is its pairing with \(\overline{g(x)}f(x')\). This is an ordinary Hilbert adjoint pairing, with the operator order shown. A Euclidean time-ordered correlator, supertrace, or holomorphic bilinear pairing requires an additional identification before it can replace it.

Let \(\kappa_\gamma\) denote the inverse Fourier transform of \(m_\gamma\), as a distribution. On \(I_L^2\), the desired kernel is

\[
\begin{aligned}
W_L^{\mathrm{target}}(x,x')={}&\kappa_\gamma(x-x')
+2\cosh((x-x')/2)\\
&-\sum_{\substack{n\ge2\\\log n<L}}\frac{\Lambda(n)}{\sqrt n}
\bigl[\delta(x-x'-\log n)+\delta(x-x'+\log n)\bigr].
\end{aligned}
\]

The pole kernel follows from the hyperbolic subtraction formula. The gamma term includes its exact normalization; its singularity is interpreted distributionally. This expression is a target for calculation, not a proposed positive kernel by definition.

Signed pieces do not preclude positivity of the complete pairing. But identifying only the separated-point kernel misses contact terms, and identifying only its high-frequency behavior misses finite terms. A regularization must fix the finite contact terms through independently stated rules. Choosing a counterterm because it makes the final answer match would leave that part of the arithmetic selection unexplained.

## 6. What a cohomological symmetry would actually protect

Let \(\mathsf q\) be an odd symmetry, nilpotent on the observables under consideration or closing onto a specified symmetry that acts trivially there. An observable is \(\mathsf q\)-closed if its variation vanishes, and \(\mathsf q\)-exact if it is the variation of another observable.

The field-theory precedent is that a stress tensor or deformation can be \(\mathsf q\)-exact, causing suitable correlation functions to be insensitive to that deformation by a Ward identity. Witten's topological theory supplies this mechanism; it does not assert equality of classical energies for every field. [Witten, *Topological Quantum Field Theory*, equation 2.33 and §3](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf)

For the proposed pairing, let \(\lambda\) label a chosen auxiliary deformation and suppose, schematically, an action satisfies

\[
\partial_\lambda S_\lambda=\mathsf q V_\lambda,
\]

where \(V_\lambda\) is odd. Write \(X_{g,f}\) for the full observable whose expectation represents the pairing; in the insertion formulation its operator product is \(\mathcal O_L(g)^\dagger\mathcal O_L(f)\), with the specified reference state or preparation understood. If this observable has no explicit \(\lambda\)-dependence, differentiation of a normalized Euclidean expectation would give

\[
\partial_\lambda\langle X_{g,f}\rangle_\lambda
=-\langle X_{g,f}\,\mathsf q V_\lambda\rangle_\lambda
+\langle X_{g,f}\rangle_\lambda
\langle\mathsf q V_\lambda\rangle_\lambda.
\]

A valid Ward identity and closure of the whole insertion can make these terms vanish. This is a conditional diagnostic formula. In a candidate one must justify differentiation, the integration measure and contour, the boundary conditions, zero modes, and the absence of uncancelled symmetry variations. If the operators, reference state, or identifications of state spaces vary with \(\lambda\), their derivatives must also be included. An unnormalized gluing amplitude additionally retains its normalization factors.

Localization may then make the pairing calculable by a deformation to a simpler limit. The remaining determinants, residual integrations, and boundary contributions must still be evaluated. Localization supplies an exact-computation strategy under its hypotheses, not a general statement that a path integral is a classical minimum. [Pestun–Zabzine, *Introduction to localization in quantum field theory*](https://arxiv.org/abs/1608.02953)

### 6.1 Preserve arithmetic geometry along the boundary

The initial proposal should protect changes of auxiliary thickness, bulk gauge representative, or some specified interior geometry while retaining the structure along \(x\). A rescaling of \(x\) changes the delays \(\log n\). Boundary backgrounds and defect labels must remain fixed during the claimed invariance.

There is a sharper test. Suppose tangential translation were \(\mathsf q\)-exact, so that a boundary operator obeyed \(\partial_x\mathcal O(x)=[\mathsf q,R(x)]_{\mathrm{gr}}\) for some \(R\), and all relevant Ward identities held without contact or defect terms. Correlators of closed insertions would then be locally independent of insertion position away from collisions. That cannot by itself provide the required general dependence on separation. A viable model must retain nontrivial boundary translations, or specify backgrounds and defects that supply the missing terms. “Topological in the bulk” should not silently impose topological invariance on every boundary displacement.

### 6.2 Arbitrary smearing and adjoint compatibility

For an even insertion, the schematic conditions

\[
\mathsf q\Omega_L=0,
\qquad [\mathsf q,\mathcal O_L(x)]=0
\]

imply \(\mathsf q\Psi_L(f)=0\) for arbitrary test \(f\), provided the distributional smearing and operator domains justify the calculation. This can avoid imposing a differential equation on \(f\). If closure holds only modulo an \(x\)-derivative, integration by parts introduces derivatives of \(f\), and arbitrary-input closure no longer follows.

Closure of the ket insertion alone is insufficient to protect its norm. Taking an adjoint of \([\mathsf q,\mathcal O]=0\) gives a relation with \(\mathsf q^\dagger\), not automatically \([\mathsf q,\mathcal O^\dagger]=0\). The full reflected or adjoint insertion, vacuum, and pairing must obey the relevant Ward identity. This is one reason to specify the real structure and the boundary algebra before invoking protection of \(Z_L\).

Supersymmetric theories with boundary conditions have concrete precedents, including Dirichlet examples evaluated by localization, but their boundary conditions do not establish arbitrary arithmetic input coverage here. [Sugishita–Terashima, *Exact Results in Supersymmetric Field Theories on Manifolds with Boundaries*](https://arxiv.org/abs/1308.1973)

## 7. Zero supersymmetric energy, positive norms, and cohomology

On a positive Hilbert space with an actual adjoint, the quadratic form of

\[
H_{\mathrm{aux}}=\{\mathsf q,\mathsf q^\dagger\}
\]

is \(\|\mathsf q v\|^2+\|\mathsf q^\dagger v\|^2\) on the common form domain. Here the normalization has no factor \(1/2\). A harmonic state means a vector \(v\) annihilated by both operators. Such a state has zero \(H_{\mathrm{aux}}\)-energy, but it can have a nonzero Hilbert norm. Supersymmetric quantum mechanics and its relation to harmonic forms provide the standard example. [Tong, *Supersymmetric Quantum Mechanics*, §§1.1 and 3.1.2](https://www.damtp.cam.ac.uk/user/tong/susy/susyqm.pdf)

Thus it is consistent in principle to seek

\[
H_{\mathrm{aux}}\Psi_L(f)=0,
\qquad
Q_{0,L}[f]\stackrel{\mathrm{target}}{=}\|\Psi_L(f)\|^2,
\]

with the appropriate operator domain for the first expression. The Weil form would be a state norm, not the expectation of this auxiliary Hamiltonian. Boundary dynamics could give a different energy interpretation, but it would require another identity.

### 7.1 A quotient needs a specified positive pairing

In a finite-dimensional positive complex with \(\mathsf q^2=0\), physical classes might be \(\ker\mathsf q/\operatorname{ran}\mathsf q\). Each class has a unique representative in \(\ker\mathsf q\cap\ker\mathsf q^\dagger\), obtained by orthogonal projection. Its norm defines a positive quotient norm.

For a densely defined closed Hilbert-space differential satisfying \(\operatorname{ran}\mathsf q\subseteq\ker\mathsf q\), the analogous reduced quotient uses \(\overline{\operatorname{ran}\mathsf q}\). Its orthogonal representatives lie in \(\ker\mathsf q\cap\ker\mathsf q^\dagger\). Identifying this reduced quotient with an unreduced cohomology, or obtaining stronger decompositions without closures, requires additional range and domain information. A gauge theory starting with an indefinite ghost space does not meet the positive-Hilbert hypotheses merely by having a nilpotent differential.

The original representative norm generally does not descend: adding \(\mathsf q w\) can change it. One must use a specified quotient norm, harmonic representative, or separately proved physical pairing. That choice can itself involve a projection or an infimum, so cohomological language does not automatically eliminate every variational step.

### 7.2 A topological vector space need not have a topological norm

An elementary example makes this distinction concrete. On a circle with coordinate \(s\in\mathbb R/\mathbb Z\), choose metric \(r^2ds^2\), with \(r>0\). The class represented by \(ds\) has period one and is independent of \(r\). Its representative is harmonic for each metric, but

\[
\|ds\|_r^2=\int_0^1r^{-2}\,r\,ds=\frac1r.
\]

Thus the cohomology and zero-energy condition can remain unchanged while the positive norm changes. This calculation is an illustration derived here. It shows why protection of the vector space of states is weaker than protection of the required Hermitian pairing.

A candidate must provide an isometric identification of the relevant states across the auxiliary deformations, or prove invariance of the pairing directly. A bilinear topological pairing is not automatically the positive Hermitian one required by the arithmetic form.

## 8. Why the existing factorization supercharge is not already the topological answer

There is an elementary distinction worth preserving in future work. Let \(A:\mathcal H_{\mathrm B}\to\mathcal H_{\mathrm F}\) be a densely defined closed factor. On the graded direct sum define

\[
\mathsf q_{\mathrm{fac}}(v,w)=(0,Av),
\qquad
\mathsf q_{\mathrm{fac}}
=\begin{pmatrix}0&0\\A&0\end{pmatrix}.
\]

Its domain is \(\operatorname{Dom}(A)\oplus\mathcal H_{\mathrm F}\), and its square is zero. Together with its adjoint it gives the familiar partner Hamiltonian with blocks \(A^*A\) and \(AA^*\), on their operator domains.

For any input in the domain of the factor, every amplitude state of the form

\[
(0,Af)=\mathsf q_{\mathrm{fac}}(f,0)
\]

is exact under this differential. Passing to its cohomology identifies that amplitude with zero, even when \(\|Af\|^2>0\). If an actual adjoint applies to the amplitude, a nonzero exact state also cannot be harmonic: harmonic states are orthogonal to the range of the differential.

The same observation applies when \(A\) is the bulk amplitude map \(\mathcal C\) and \(f\) in the last display is replaced by an admissible bulk configuration \(U\). In particular, the gamma energy amplitudes are exact under the standard graded differential built from their own amplitude map.

**Design consequence:** a protected-state construction cannot be obtained simply by calling the existing factorization amplitudes the cohomology of that same supercharge. It could use a different symmetry acting on auxiliary redundancies, a relative boundary complex, or a different boundary observable. Each option needs an explicit construction. The symbols \(\mathsf q_{\mathrm{fac}}\) and a proposed topological symmetry \(\mathsf q_{\mathrm{top}}\) should remain distinct until a model relates them.

This does not invalidate the existing positive factorization or require a topological quotient for every approach. It identifies what additional structure is needed if cohomology is intended to explain the nonzero boundary pairing.

## 9. Gluing, reflection, and a boundary space large enough for the input

The proposed state preparation assigns \(\Psi_L(f)\) to one bulk region. Gluing a second region with the appropriate reflected conjugate should produce \(Z_L(g,f)\). The reflection must implement the physical adjoint, including fermionic conventions and boundary orientation.

For any finite list of inputs \(f_1,\ldots,f_N\), an ordinary positive pairing gives

\[
\sum_{i,j=1}^N\overline{c_i}c_j Z_L(f_i,f_j)
=\left\|\sum_{j=1}^N c_j\Psi_L(f_j)\right\|^2\ge0
\]

for all complex coefficients \(c_j\). This Gram positivity is the relevant sign statement. A formal topological gluing rule or a signed index is not a substitute.

Reflection positivity is additional structure in topological field theory; Freed–Hopkins give a treatment in the invertible setting. Their results are a precedent for the distinction, not a realization theorem for the infinite boundary space required here. [Freed–Hopkins, *Reflection positivity and invertible topological phases*](https://arxiv.org/abs/1604.06527)

Gauge-theoretic gluing must also retain boundary modes and global sectors. The BV–BFV framework supplies methods for organizing bulk and boundary gauge data and their composition; a positive physical Hilbert pairing remains an additional requirement for this proposal. [Cattaneo–Mnev–Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*](https://arxiv.org/abs/1507.01221)

A finite-dimensional protected sector alone cannot carry this linear factorization. At fixed \(L\), the gamma multiplier grows logarithmically at high frequency while the other terms are bounded forms. Modulating any fixed finite-dimensional smooth subspace to sufficiently high frequency gives positive subspaces of arbitrarily large dimension. Consequently the target cannot be a finite-rank Gram form. Boundary fields, infinitely many channels, or another infinite-dimensional state space must survive the proposed reduction.

One must also track exact states that become physical at a boundary. A gauge transformation trivial on the boundary can be quotiented, while one acting on boundary data may generate an edge mode. A relative complex could express this difference, but the boundary trace and allowed transformations have to be specified; a bulk quotient must not erase the data \(f\) carries.

## 10. The gamma construction as a controlled nonlocal example

The program already has an independently positive auxiliary-field realization. Define \(a_k=2k+1/2\) for integers \(k\ge0\). Its energy is

\[
\mathcal E^{\mathrm{kin}}[\widetilde f,(u_k)]
=\sum_{k\ge0}\frac2{a_k}\int_{\mathbb R}
\left(|\widetilde f-u_k|^2+a_k^{-2}|u_k'|^2\right)dx,
\]

with \(u_k\in H^1(\mathbb R)\) and finite total energy. The input component is fixed; the channels vary on the whole line. Their minimizers satisfy

\[
(1-a_k^{-2}\partial_x^2)u_k=\widetilde f,
\qquad
\widehat u_k(\tau)=\frac{a_k^2}{a_k^2+\tau^2}\widehat f(\tau).
\]

Let \(\mathcal P f=(\widetilde f,(u_k))\) be this extension and let the amplitude map be

\[
\mathcal C(\widetilde f,(u_k))
=\left(\sqrt{2/a_k}(\widetilde f-u_k),
\sqrt{2/a_k^3}\,u_k'\right)_{k\ge0}.
\]

Its target is the positive Hilbert direct sum of the displayed \(L^2(\mathbb R)\) components. The kinetic state map \(\Psi^{\mathrm{kin}}_L(f)=\mathcal C\mathcal P f\) obeys

\[
\|\Psi^{\mathrm{kin}}_L(f)\|^2
=K[\widetilde f]
=\frac1{2\pi}\int_{\mathbb R}
\left(\sum_{k\ge0}\frac2{a_k}\frac{\tau^2}{a_k^2+\tau^2}\right)
|\widehat f(\tau)|^2\,d\tau.
\]

The summed multiplier is \(\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4)\). The factor, minimizing extension, and infinite-channel domain are supplied by Section 5 of the [existing manuscript](../attempts/positive-factorizations/manuscript.tex).

### 10.1 One channel already tests nonlocality and exact normalization

For a single parameter \(a>0\), the solution is convolution with

\[
r_a(x)=\frac a2 e^{-a|x|},
\qquad u=r_a*\widetilde f.
\]

The two-component amplitude has squared norm

\[
K_a[f]=\frac1{2\pi}\int_{\mathbb R}
\frac2a\frac{\tau^2}{a^2+\tau^2}|\widehat f(\tau)|^2\,d\tau.
\]

Equivalently, its whole-line distributional kernel is

\[
\frac2a\delta(x-x')-e^{-a|x-x'|}.
\]

This follows from \(\frac2a\frac{\tau^2}{a^2+\tau^2}=\frac2a-\frac{2a}{a^2+\tau^2}\). It displays a positive form with a negative nonlocal kernel contribution and a compensating contact term. It is a precise test of diagonal accounting. The decomposition is for one channel; the separate contact coefficients cannot be summed over all \(k\) because \(\sum_k2/a_k\) diverges. The full tower must retain the combined multipliers or an equivalent convergent formulation.

### 10.2 What a superspace reformulation would have to add

The tower is not extension-independent: a nonzero channel variation with zero input can have positive energy. Its minimizing solutions do not make the unrestricted system topological. Nor does its standard graded supercharge protect the amplitude as a nonzero cohomology class, by §8.

A useful additional theory would supply explicit component transformations and a boundary pairing whose calculation recovers this kernel through an independently meaningful symmetry or gluing identity. One should first do that for a single channel or a finite tower, then justify the infinite limit. Arbitrarily assigning trivial symmetry to the answer or adding decoupled supersymmetric fields would verify no new arithmetic mechanism.

The full central form still contains

\[
Q_{0,L}[f]=K[\widetilde f]
+w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
\langle f,(T_{\log n}+T_{\log n}^*)f\rangle,
\]

where \(w_0=\psi(1/4)-\log\pi<0\) and the sum is over integers \(n\ge2\). These contributions require a common construction. A superspace version of the kinetic tower alone is not a completion of the gamma form, let alone of the full Weil form.

## 11. The secondary route: a saturating bulk solution

If a candidate naturally supplies a real nonnegative component energy rather than a state pairing, seek

\[
\mathcal E_L[U]=\|\mathcal D_LU\|_{\mathcal Y_L}^2+B_L[\operatorname{Tr}U],
\]

where \(U\) is a component configuration, \(\mathcal D_L\) is a specified bulk operator, and \(\mathcal Y_L\) is a positive Hilbert space. For fixed input \(f\), a finite-energy solution

\[
\operatorname{Tr}U_f=f,
\qquad \mathcal D_LU_f=0
\]

would give \(B_L[f]=\mathcal E_L[U_f]\ge0\) and attain the infimum. Matching \(B_L[f]\) with \(Q_{0,L}[f]\) is still required. Calling the solutions BPS additionally requires an actual supersymmetry algebra connecting these equations to preserved charges.

The companion note's §6.1 shows the danger precisely. In this finite-dimensional illustration, take an invertible Hermitian matrix \(M\) on \(\mathbb C^m\). Here the boundary input \(f\) is a vector in \(\mathbb C^m\), and \(u\in H^1([0,\infty);\mathbb C^m)\) has trace \(u(0)=f\) and tends to zero at infinity. The positive half-line energy satisfies

\[
\int_0^\infty(\|u'\|^2+\|Mu\|^2)\,dy
=\int_0^\infty\|u'+Mu\|^2\,dy+\langle f,Mf\rangle
\]

has a decaying saturating solution \(u=e^{-yM}f\) only for the positive spectral part of the input. Its true minimum for general \(f\) is \(\langle f,|M|f\rangle\). Thus all-input solvability can conceal the whole sign question. This example is an algebraic diagnostic, not a proposed choice of arithmetic \(M\).

Approximate saturation with the exact same trace can suffice: if \(\|\mathcal D_LU_j\|\to0\) and \(\operatorname{Tr}U_j=f\), the positive energies converge to \(B_L[f]\). Approximate traces instead require a justified limit in a topology controlling the boundary form.

The primary pairing route avoids this particular requirement of a classical saturating solution for every \(f\), but replaces it with the obligation to construct every state \(\Psi_L(f)\) with finite norm. It does not remove the all-input problem.

### 11.1 Why unrestricted extension independence is not the default

Suppose a quadratic bulk energy is independently given by a squared amplitude norm. Exact independence from every allowed interior variation would require

\[
\mathcal E[U]=\|\mathcal C U\|^2,
\qquad
\ker\operatorname{Tr}\subseteq\ker\mathcal C.
\]

The companion note proves this criterion: zero energy on all zero-trace variations forces their cross terms to vanish by positivity. It is much stronger than gauge invariance along selected variations or invariance of a quantum observable under selected deformations. In an unconstrained positive finite block system it eliminates both the interior energy block and its coupling to the boundary.

This route remains possible if an independently derived constraint, quotient, or identity explains the descent. It should not be imposed on the unrestricted gamma energy, which has energetic interior variations. A cohomological boundary pairing can pursue a different invariance statement without claiming this null-space condition.

## 12. How arithmetic might constrain the bulk and boundary couplings

### 12.1 Translation labels and composition

For \(n\ge2\), the displacement \(\log n\) suggests a labeled operation whose boundary action is translation by that amount. On the whole line, forward translations compose according to \(\log(mn)=\log m+\log n\). The corresponding compressed forward delays on \(I_L\) also have this semigroup property, but their adjoints and mixed products include endpoint restrictions. A model must use the actual finite-interval operators in its Gram calculation.

For example, if a candidate amplitude were formally

\[
A f=\sum_j v_j T_{a_j}f,
\]

where \(a_j\ge0\), \(T_0=I\), and \(v_j\) are channel vectors, then its squared norm contains terms

\[
\sum_{i,j}\langle v_i,v_j\rangle
\langle T_{a_i}f,T_{a_j}f\rangle.
\]

On the whole line these involve differences of displacements. On a finite interval they also have truncation effects. A composition or symmetry rule must explain unwanted mixed delays, desired prime-power coefficients, and diagonal contributions together. The logarithm identity alone supplies none of the weights \(\Lambda(n)/\sqrt n\).

Possible data carriers include labeled defects, a representation of arithmetic operations, a channel spectrum, or boundary background fields. These are alternatives to specify and test, not already defined parts of a theory. A topological rule for deforming a labeled network would be useful only after its independent labeling and evaluation rules were given.

### 12.2 Positive components must account for signed arithmetic collectively

The existing manuscript's obstructions to its specified independent pairwise-square models remain relevant. Simply adding isolated positive prime channels generally introduces positive diagonal terms and cannot reproduce an indefinite prime correction without a joint accounting. The first prime can stabilize a direction in which the gamma form is negative while acting differently on another direction.

A candidate might evade those restricted models through coherent multicomponent couplings, additional constraints, or a different positive pairing. It must demonstrate that escape in its actual algebra. Topological labels do not change the sign constraints of an otherwise identical pairwise model.

The pole contribution also contains both reflection parities. A construction preserving only odd, even, chiral, or zero-mean inputs does not cover the criterion. Free finite-rank boundary couplings must be fixed independently rather than selected after comparing with the target.

### 12.3 Cutting the interval must retain cross terms

For inputs \(f_1,f_2\) whose sum lies in \(I_L\),

\[
Q_{0,L}[f_1+f_2]
=Q_{0,L}[f_1]+Q_{0,L}[f_2]
+2\operatorname{Re}q_{0,L}(f_1,f_2).
\]

Linearity of a correctly matched state map retains this through the overlap of the two states. A gluing construction that places the two pieces in orthogonal summands loses their interaction. Interface variables must carry the gamma interaction and prime delays crossing the cut.

Exact matching on separate unbounded lengths is already enough for the RH implication. A coherent family of state spaces and isometric embeddings under support inclusion would be additional explanatory structure, not a prerequisite to that elementary implication.

## 13. Analytical and physical conditions a candidate must settle

| Condition | What must be specified or proved |
|---|---|
| Positive object | An ordinary positive Hilbert pairing or independently nonnegative real component energy, before arithmetic matching. |
| Physical space | Which states are retained, which null or gauge states are quotiented, and why the resulting pairing is positive. |
| Odd symmetry | Fields, transformations, algebra, domains, and the treatment of gauge closure; distinguish it from the factorization supercharge. |
| Boundary input | Whether \(f\) is a prescribed component or a smearing function, with every required complex test input represented. |
| Boundary conditions | A consistent choice of prescribed variables, remaining responses, other edges, infinity, zero modes, and global sectors. |
| Adjoint and reflection | The conjugation and gluing operation producing the ordinary Hermitian norm, including the reflected insertion's symmetry. |
| Protected quantity | Exactly which pairing or observable is invariant, under which deformations, with fixed arithmetic data. |
| Arithmetic selection | Independent rules for gamma parameters, prime labels and weights, pole terms, and finite contact terms. |
| Linearity and polarization | A linear state map or an exactly quadratic reduced energy, with the full identity on arbitrary pairs \(g,f\). |
| Regularization and limits | Finite norms on test inputs, convergent channel sums, preserved symmetry and positivity where used, and controlled contact terms. |
| Support growth | Exact matching at unbounded lengths, with interface interactions if a gluing law is used. |
| Appropriate input topology | Finite-interval form domains or another stated topology; no unwarranted whole-line \(L^2\) closability assumption. |

The last condition is substantive. Section 9 of the existing manuscript gives a restriction on a single closable factor on ordinary whole-line \(L^2\) containing all compactly supported smooth inputs and reproducing the full form. It does not exclude finite-interval factors or maps on appropriate test-function spaces. A global boundary operator-valued distribution should not silently be assumed to extend to an \(L^2\)-bounded or closable smearing map. The manuscript's results retain the review status recorded in its [status file](../attempts/positive-factorizations/STATUS.md).

For limits of regularized positive pairings, a sufficient sign argument is convergence of \(Z_{L,\varepsilon}(f,f)\) to the desired finite value for each fixed test \(f\). Convergence on arbitrary pairs gives the polarized identity as well. Convergence in the form topology is an appropriate route when approximating inputs in the unbounded finite-interval form. Ordinary \(L^2\) convergence alone does not control those energies.

If divergences are removed by subtracting terms, positivity of the unsubtracted regulator does not automatically pass to the renormalized answer. The selected finite pairing must have its own positive realization or a limit argument that actually preserves positivity. This is particularly relevant to the gamma tower's cancellation between contact and nonlocal terms.

## 14. A staged investigation with definite outcomes

1. **Choose one boundary interpretation.** For the primary route, start with a linear insertion map and an ordinary pairing. For the secondary route, start with prescribed component data and a nonnegative energy. State which quantity is claimed to be protected.
2. **Specify a minimal symmetry model.** Give its multiplets or component fields, odd transformations, real structure, boundary conditions, physical space, and the relation between bulk and boundary symmetries. Check explicitly that nonzero target states survive any quotient.
3. **Derive a nonlocal toy pairing.** The one-channel kernel in §10.1 supplies a known answer with nontrivial contact accounting. A useful model should explain its pairing through the chosen mechanism, rather than define that kernel as a boundary coupling.
4. **Prove arbitrary-input coverage.** Include complex inputs with nonzero mean, both reflection parities, and separated supports. Determine whether symmetry closure introduces hidden equations on \(f\).
5. **Test the claim of protection.** Identify an actual auxiliary deformation and prove invariance of the full Hermitian pairing, including the bra, normalization, boundary modes, and any changing inner product.
6. **Recover the full gamma kinetic tower.** Derive its spectrum and weights or clearly state which are external input. Control the infinite-channel limit without separating divergent pieces. Then address the fixed normalization and both pole amplitudes.
7. **Introduce arithmetic interactions jointly.** Compute the first prime and at least two interacting translation labels, including mixed delays and diagonal terms. Compare with the existing restricted no-go results.
8. **Establish an arbitrary-length rule.** Prove matching and positivity under support growth or an explicit composition rule with all cross terms. A finite numerical certificate is a diagnostic, not this rule.

A successful early deliverable would be a fully specified nonlocal toy model with a positive pairing, a nontrivial symmetry identity, and all-input coverage. A useful negative deliverable would identify a precise obstruction, such as failure of adjoint closure, collapse of the boundary states in cohomology, or inability to preserve the arithmetic translations. Neither should be overstated as an all-length arithmetic result.

## 15. Continuation instructions and unresolved choices

The next discussion should start from the primary pairing route and keep the saturation route available as a controlled alternative. No particular gauge group, supersymmetry algebra, twist, spacetime dimension, action, or arithmetic defect rule has been selected.

The most consequential unresolved choices are:

- What independent data define the physical positive pairing and the arithmetic boundary operator?
- Is the topological symmetry a bulk redundancy with surviving boundary states, a symmetry of an insertion algebra, or a symmetry producing saturation equations?
- How does that symmetry act on the adjoint insertion and on the physical norm?
- Which auxiliary deformations become invisible, while the scale and translations along \(x\) remain visible?
- What supplies a sufficiently large boundary sector and arbitrary complex input coverage?
- Can the nonlocal gamma pairing be recovered through a meaningful symmetry mechanism, and can that same mechanism constrain the remaining terms collectively?

Useful opening prompt for a continuation:

> Read this companion note, the topological brainstorm, and the current shared background. Develop one concrete candidate for a positive boundary pairing from a supersymmetric or cohomological bulk. Begin by defining its positive space, boundary input map, symmetry, adjoint, and boundary conditions. Explain which auxiliary changes it protects and why its nonzero boundary states survive the symmetry reduction. Use the one-channel gamma kernel as a first nonlocal check, while keeping the full arithmetic matching and arbitrary-length questions explicit. Show each map acting on \(f\) before giving its operator notation.

The distinction introduced in §8 is particularly important to retain: the factorization differential makes its own amplitudes exact. A proposed protected pairing must explain its relationship to that construction rather than equate their cohomologies by notation. The metric example in §7.2 likewise prevents confusing invariance of a state space with invariance of its positive pairing.

## 16. Sources and scope of the deductions

The arithmetic formulas, gamma tower, and existing model restrictions are drawn from the local program background and manuscript. The companion brainstorm supplies the descent criterion, saturation template, and half-line sign diagnostic. The exact-amplitude observation in §8, circle norm calculation in §7.2, one-channel kernel calculation, and the project-specific design tests are elementary deductions developed in this note.

The external sources below provide precedents for the field-theory mechanisms. They do not establish an arithmetic realization.

| Source | Use in this note |
|---|---|
| [Tong, *Superspace and superfields*](https://www.damtp.cam.ac.uk/user/tong/susy/susy3.pdf) | Superspace coordinates, component fields, and the need for specified transformations. |
| [Tong, *Supersymmetric Quantum Mechanics*](https://www.damtp.cam.ac.uk/user/tong/susy/susyqm.pdf) | Positive partner Hamiltonians, zero-energy states, and the harmonic/cohomological picture. |
| [Witten, *Topological Quantum Field Theory*](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf) | Cohomological symmetry and metric-independent observables. |
| [Pestun–Zabzine, *Introduction to localization in quantum field theory*](https://arxiv.org/abs/1608.02953) | Localization as a conditional exact-computation method. |
| [Sugishita–Terashima, *Exact Results in Supersymmetric Field Theories on Manifolds with Boundaries*](https://arxiv.org/abs/1308.1973) | Concrete supersymmetric boundary-condition precedents. |
| [Freed–Hopkins, *Reflection positivity and invertible topological phases*](https://arxiv.org/abs/1604.06527) | Reflection positivity as added structure, within that work's invertible-theory scope. |
| [Cattaneo–Mnev–Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*](https://arxiv.org/abs/1507.01221) | Organizing gauge-theoretic boundary data and gluing. |

Sources were consulted in the discussion and preparation on 12 September 2026. This is a conceptual continuation document, not an exhaustive literature survey, priority review, or independent specialist validation of the program's existing results.
