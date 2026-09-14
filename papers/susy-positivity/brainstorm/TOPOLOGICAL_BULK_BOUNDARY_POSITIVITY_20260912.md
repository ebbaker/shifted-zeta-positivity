# Topological bulk theories and exact boundary positivity

**Brainstorming note · 12 September 2026**

**Status:** a proposed research direction, with elementary implications proved below and field-theory precedents cited where used. No topological bulk realizing the full Weil form has been constructed here. The arithmetic matching and arbitrary-length existence problems remain open.

This note develops Edward Baker's suggestion that a bulk theory might be topological in a sense that makes its energy depend only on the boundary data. In that case, the infimum in the background's bulk–boundary formula could be replaced by evaluation on an extension. The formula is equation **1.14** in the current background; its stable TeX label is `eq:rh-bulk-target`.

The shared definitions remain in the [background source](../background_section.tex) and [background PDF](../background.pdf). See also the [program overview](../PROGRAM_OVERVIEW.md), [superspace continuation](continuation-notes/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md), and [positive-factorizations manuscript](../investigations/positive-factorizations/manuscript.tex). This note records a possibility within that program, rather than revising those documents.

## 1. The idea and the distinctions that matter

Suppose a bulk configuration is denoted by \(U\), its boundary profile by \(f\), and the map extracting that profile by \(\operatorname{Tr}U=f\). The current proposal is

\[
Q_{\omega,L}[f]\stackrel{\mathrm{target}}{=}
\inf_{\operatorname{Tr}U=f}\mathcal E_{\omega,L}[U],
\qquad \mathcal E_{\omega,L}[U]\geq0.
\]

The infimum allows the additional degrees of freedom to adjust while the boundary input stays fixed. Baker's suggestion asks for a stronger structure: changing the interior might never change the energy in the first place.

Three mechanisms should be investigated separately.

| Mechanism | Precise content | What happens to minimization |
|---|---|---|
| Extension independence | Every admissible \(U\) has \(\mathcal E[U]=B[\operatorname{Tr}U]\). | Every extension has the same energy; the infimum is redundant. |
| Boundary energy on a constrained space | The same identity holds after imposing specified bulk constraints. | One solves constraints and evaluates the boundary energy. Equality with an infimum over a larger, unconstrained space needs an additional argument. |
| Saturation of an energy bound | \(\mathcal E[U]=\|\mathcal D U\|^2+B[\operatorname{Tr}U]\), and appropriate solutions satisfy \(\mathcal D U=0\). | A saturating solution attains the infimum. Existence for every required input is essential. |

In all three cases the boundary functional \(B\) must still be computed and proved equal to the arithmetic target. Topological terminology does not establish that equality or the required positivity.

“Depends only on the boundary” means dependence on the **entire function** \(f(x)\). It does not mean dependence only on the endpoints of its support, a few moments, or the topology of that support. Nor must the extension be unique: many interior configurations may have the same boundary profile and energy.

## 2. The arithmetic target and the roles of the coordinates

Let \(I_L=(-L/2,L/2)\). The direct target is

\[
Q_{0,L}[f]\geq0
\quad\text{for every }L>0
\quad\text{and every }f\in C_c^\infty(I_L;\mathbb C).
\]

The background states the equivalence of this all-length condition with RH. An unbounded sequence of covered lengths suffices. No positive lower bound uniform in \(L\) is required. A finite collection of successful lengths is insufficient.

For reference, with the background's normalization,

\[
\begin{aligned}
Q_{0,L}[f]={}&\frac{1}{2\pi}\int_{\mathbb R}
\left(\operatorname{Re}\psi\left(\frac14+\frac{i\tau}{2}\right)
-\log\pi\right)|\widehat f(\tau)|^2\,d\tau\\
&+2|C(f)|^2-2|S(f)|^2\\
&-\sum_{\substack{n\geq2\\\log n<L}}
\frac{\Lambda(n)}{\sqrt n}
\langle f,(T_{\log n}+T_{\log n}^*)f\rangle .
\end{aligned}
\]

Here \(\widehat f(\tau)=\int f(x)e^{-i\tau x}\,dx\), \(\psi=\Gamma'/\Gamma\), and \(\Lambda\) is the von Mangoldt function. The amplitudes are

\[
C(f)=\int f(x)\cosh(x/2)\,dx,
\qquad S(f)=\int f(x)\sinh(x/2)\,dx.
\]

The operator \(T_a\) shifts the zero extension of \(f\) by \(a\) and restricts it back to \(I_L\). Only prime powers contribute to the finite sum, and a delay of length exactly \(L\) acts as zero.

The natural closed form domain at fixed \(L\) is

\[
\mathcal D_{\log,L}=
\left\{f\in L^2(I_L):
\int_{\mathbb R}\log(2+|\tau|)|\widehat f(\tau)|^2\,d\tau<\infty\right\}.
\]

The smooth test functions form a core. The full form is closed and semibounded on this domain independently of the desired nonnegativity, as explained in the background.

In a proposed field theory:

- \(x\) labels the arithmetic input. Its translation structure matters because delays occur at \(\log n\).
- \(L\) limits the support of that input. It need not be a physical size of the entire bulk.
- \(y\), if introduced, is an auxiliary bulk coordinate; a discrete channel index could serve instead.
- \(t\), if introduced, is physical or auxiliary Hamiltonian time. It is a new variable.
- \(\omega\) remains the zeta shift. It is not automatically \(y\) or \(t\).

A sensible initial objective is a construction at \(\omega=0\). Requiring positivity of every shifted form at every length would add a condition absent from the direct RH criterion. A construction available only for positive shifts would need a proved central limit or the separate contraction route in the background.

## 3. Exact extension independence: an elementary criterion

Suppress the parameters. Let \(\mathcal X\) be a complex linear space of admissible finite-energy fields. Let \(\operatorname{Tr}:\mathcal X\to\mathcal B\) be linear and onto the required boundary space. Suppose

\[
\mathcal E[U]=e(U,U)\geq0,
\]

where \(e\) is Hermitian and conjugate-linear in its first argument. All variations below belong to \(\mathcal X\).

**Elementary equivalence.** The following conditions are equivalent:

1. There is a quadratic functional \(B\) on \(\mathcal B\) with \(\mathcal E[U]=B[\operatorname{Tr}U]\).
2. \(\mathcal E[U+h]=\mathcal E[U]\) for every \(U\in\mathcal X\) and every \(h\in\ker\operatorname{Tr}\).
3. \(\mathcal E[h]=0\) for every \(h\in\ker\operatorname{Tr}\).

**Proof.** Conditions 1 and 2 express the same independence from the choice of lift. Condition 2 implies condition 3 by setting \(U=0\). Conversely, the Cauchy–Schwarz inequality for a nonnegative sesquilinear form gives

\[
|e(h,U)|^2\leq e(h,h)e(U,U)=0.
\]

Thus the cross term vanishes and \(\mathcal E[U+h]=\mathcal E[U]\). Defining \(B[f]\) by any lift is consequently well-defined. This also proves \(B[f]\geq0\). No minimizer theorem is needed for this algebraic implication.

In particular, for any admissible lift \(U_f\),

\[
\boxed{
\inf_{\operatorname{Tr}U=f}\mathcal E[U]
=\mathcal E[U_f]=B[f].
}
\]

If the bulk energy is independently given by \(\mathcal E[U]=\|\mathcal C U\|_{\mathcal K}^2\) in a positive Hilbert space, the criterion becomes

\[
\ker\operatorname{Tr}\subseteq\ker\mathcal C.
\]

The amplitude map itself descends to the boundary: \(A f=\mathcal C U_f\) is independent of the lift and linear, and \(B[f]=\|Af\|^2\). This is exactly the type of positive factor sought in the program, now obtained without optimizing over the interior. Continuity, completion, and closability of the resulting maps remain separate analytical questions.

### 3.1 What this implies for a proposed local bulk

The condition is strong. For a finite-dimensional unconstrained quadratic system with boundary vector \(f\), interior vector \(u\), and nonnegative energy matrix

\[
H=\begin{pmatrix}H_{bb}&H_{bi}\\H_{ib}&H_{ii}\end{pmatrix},
\]

independence from all changes of \(u\) forces \(H_{ii}=0\). Nonnegativity then forces \(H_{bi}=H_{ib}=0\). In these coordinates the energy is already \(f^*H_{bb}f\); there is no energetic interior coupling left to eliminate.

Likewise, if a continuum energy is a positive integral of local differential amplitudes, demanding zero energy for every freely allowed smooth interior variation forces those amplitudes to annihilate all such variations. An ordinary positive gradient energy does not have this property. This observation applies to the energy, not to a separate first-order action that imposes constraints or defines a symplectic structure.

**Design implication:** the strongest mechanism is most informative if a symmetry, quotient, or independently derived identity explains why the energy descends. Merely writing \(\mathcal E[U]=Q_{0,L}[\operatorname{Tr}U]\) assumes the desired sign when one calls \(\mathcal E\) positive.

## 4. Boundary energy after imposing topological constraints

Let \(\mathcal F(U)=0\) denote explicitly chosen bulk constraints. They may be flatness equations, conservation equations, or equations obtained from multiplier fields. Define

\[
\mathcal S_f=
\{U:\mathcal F(U)=0,\ \operatorname{Tr}U=f,\ U\text{ obeys all other domain conditions}\}.
\]

The required statement is that \(\mathcal S_f\) is nonempty for every test input and that an independently defined physical energy takes one common value \(B[f]\) throughout \(\mathcal S_f\). If that energy is nonnegative on physical configurations, then \(B[f]\geq0\).

This supplies a direct positivity route whether or not there is a useful energy on unconstrained fields. If an unconstrained energy does exist, its infimum need not equal the constrained value: that requires a bound or a proof that an unconstrained minimum lies in \(\mathcal S_f\).

### 4.1 Gauge equivalence is helpful but not enough by itself

Gauge transformations that act trivially on the prescribed boundary data should leave the physical energy unchanged. If all elements of \(\mathcal S_f\) are related by such transformations, extension independence follows. This is sufficient, not necessary: distinct gauge classes could still have equal energy.

However, gauge invariance does not say that every variation with zero boundary trace is gauge. A topological theory can retain global holonomies, fluxes, or other residual data. Either these must be fixed as part of a stated sector, included in the boundary specification, or shown not to affect the energy. Choosing a sector separately for each \(f\) requires a consistent selection rule and full boundary coverage.

In abelian BF theory, for example, the bulk action is \(S_{\mathrm{BF}}=\int_M B\wedge dA\), with \(A\) a one-form and \(B\) an \((\dim M-2)\)-form. Its equations are \(dA=dB=0\); quotienting by exact-form gauge transformations can leave cohomology classes. Thus the absence of local propagating modes is compatible with residual global fields. The BV–BFV framework organizes gauge data in the bulk together with compatible boundary structures and gluing. It does not supply a positive Hilbert norm merely by doing so. [Cattaneo–Mnev–Reshetikhin, especially §§5.4 and 7](https://arxiv.org/pdf/1201.0290).

### 4.2 An action, an energy, and a boundary response are different objects

A metric-independent action is not automatically a nonnegative energy. A symplectic form determines pairings and brackets, not a preferred positive Hamiltonian. An on-shell action may be a phase or a signed functional. A boundary response obtained from that action may also have an indefinite quadratic part.

For every candidate, identify the actual positive object: a classical Hamiltonian, a quadratic energy, a norm of a state, or a positive operator expectation. Then identify the map from \(f\) to that object. The positivity proof must concern the same quantity that is matched to \(Q_{0,L}\).

### 4.3 What a Stokes-type identity would and would not establish

An especially direct mechanism would be an identity expressing an energy density as a total derivative, \(\mathscr L(U)=d\mathscr J(U)\), so that its integral reduces to an integral of \(\mathscr J(U)\) over the boundary. This gives the desired descent only if the boundary current is determined by the prescribed data. If it also involves an undetermined normal derivative, one still needs a bulk equation relating that derivative to \(f\). Ordinary harmonic extension already illustrates the latter situation; boundary evaluation on solutions does not itself establish topological invariance.

There is a further global distinction. A closed differential form need not be globally exact. Integrals over two fillings of the same boundary can differ by an integral over the closed manifold obtained by joining the fillings. Independence of an exponentiated action modulo a phase period would not make a real quadratic energy single-valued. A proposed exact boundary energy must resolve that dependence, not just show invariance of its exponential.

## 5. Chern–Simons theory as a concrete source of inspiration

For abelian Chern–Simons theory, take a gauge one-form \(a\) and action

\[
S_{\mathrm{CS}}[a]=\frac{k}{4\pi}\int_M a\wedge da.
\]

On a half-space with coordinates \((t,x,y)\), a suitable boundary condition \(a_t-v a_x=0\), followed by the flatness constraint and gauge reduction, yields the boundary scalar action

\[
S_{\partial}[\phi]=\frac{k}{4\pi}\int dt\,dx\,
\bigl(\partial_t\phi\,\partial_x\phi-v(\partial_x\phi)^2\bigr).
\]

Here \(\phi\) is a real edge field; conventions fix orientation and chirality. Its Hamiltonian is

\[
H_{\partial}[\phi]=\frac{kv}{4\pi}\int(\partial_x\phi)^2\,dx,
\]

which is nonnegative when \(kv>0\). The velocity \(v\) is specified through boundary data, not fixed by the topological bulk alone. [Tong, *Lectures on the Quantum Hall Effect*, §6.1.2, equations 6.4–6.10](https://www.damtp.cam.ac.uk/user/tong/qhe/six.pdf).

The useful pattern is a constrained bulk with genuine boundary degrees of freedom. The boundary Hamiltonian contains additional information. Geiller and Jai-akson make that freedom explicit in constructions with edge modes and chosen boundary Hamiltonians, including Chern–Simons and BF examples. [*Extended actions, dynamics of edge modes, and entanglement entropy*, §4](https://arxiv.org/pdf/1912.06025).

**Project-specific deductions from this example:**

- A topological bulk can organize a nontrivial boundary theory; an energetic boundary is compatible with the proposal.
- A candidate must explain the selection of the boundary Hamiltonian. Choosing its kernel to be the Weil kernel simply relocates the original problem.
- The simple scalar Hamiltonian above has a second-derivative kinetic operator, whereas the Weil form has logarithmic high-frequency growth and arithmetic delays. It is a structural example, not a matching candidate as written.
- The identification of \(f\) matters. If \(f=\phi\), the displayed energy is a derivative energy. If \(f=\partial_x\phi\), reconstruction of \(\phi\) requires endpoint and zero-mode choices. In particular, on a circle the derivative of a single-valued periodic scalar has zero integral, so this identification alone would miss inputs with nonzero mean.
- The input functions may be complex. A real-field construction must be complexified through its Hermitian quadratic form, or two real components must be combined with the correct polarization.

## 6. Saturation: a precise route suggested by supersymmetry

Instead of requiring independence from every interior variation, seek a decomposition

\[
\boxed{
\mathcal E_L[U]=\|\mathcal D_L U\|_{\mathcal Y_L}^2
+B_L[\operatorname{Tr}U].
}
\]

Here \(\mathcal Y_L\) is a positive Hilbert space, \(\mathcal D_L\) is a specified bulk operator, and \(\mathcal E_L\) is independently nonnegative. The equations \(\mathcal D_L U=0\) describe the configurations that saturate the bound. For a quadratic linear model, take \(\mathcal D_L\) and the trace linear. A nonlinear field theory could be considered, but its reduced functional would still need to be proved exactly quadratic in arbitrary input amplitudes.

**Sufficient theorem template.** For every required \(L,f\), suppose:

1. The displayed identity holds with all boundary and infinity terms accounted for.
2. The total energy \(\mathcal E_L[U]\) is nonnegative by its independent construction.
3. There is a finite-energy field \(U_f\) with \(\operatorname{Tr}U_f=f\) and \(\mathcal D_LU_f=0\).
4. Computing the boundary term gives \(B_L[f]=Q_{0,L}[f]\).

Then

\[
Q_{0,L}[f]=B_L[f]=\mathcal E_L[U_f]\geq0,
\]

and the square decomposition also proves

\[
\inf_{\operatorname{Tr}U=f}\mathcal E_L[U]
=\mathcal E_L[U_f]=Q_{0,L}[f].
\]

This is a Bogomolny-type completion-of-squares mechanism. Calling it a BPS mechanism would additionally require an actual supersymmetry algebra relating the equations to preserved supercharges. The algebraic theorem above does not require that terminology or a physical model.

The boundary contribution could resemble a charge in an energy bound. However, a bound \(\mathcal E\geq B\) does not establish \(B\geq0\). Even if supersymmetry establishes positivity of \(\mathcal E-B\), positivity of the total energy and saturation for the required inputs remain essential. A boundary-dependent charge also need not be invariant under all changes of the function \(f\).

### 6.1 A worked example: where solvability can hide the sign problem

This elementary model is an illustration, not an arithmetic construction. Let \(A\) be an invertible Hermitian matrix on \(\mathbb C^m\), with no sign assumption. For fields \(u:[0,\infty)\to\mathbb C^m\) in \(H^1\), set \(u(0)=f\) and

\[
\mathcal E[u]=\int_0^\infty
\bigl(\|u'(y)\|^2+\|Au(y)\|^2\bigr)\,dy\geq0.
\]

These fields tend to zero at infinity. Integration of
\(\frac{d}{dy}\langle u,Au\rangle=2\operatorname{Re}\langle u',Au\rangle\)
gives

\[
\mathcal E[u]
=\int_0^\infty\|u'+Au\|^2\,dy+\langle f,Af\rangle.
\]

The proposed saturating solution is \(u(y)=e^{-yA}f\). It has finite energy and decays exactly when \(f\) belongs to the positive spectral subspace of \(A\). Negative eigencomponents grow. Therefore a saturating extension for **every** \(f\) exists if and only if \(A\) is positive definite.

Without that sign condition, the actual minimizer is

\[
u_{\min}(y)=e^{-y|A|}f,
\qquad
\inf_{u(0)=f}\mathcal E[u]=\langle f,|A|f\rangle.
\]

This follows by completing the square with \(|A|\), since \(|A|^2=A^2\). For \(A=\operatorname{diag}(1,-1)\) and \(f=(0,1)\), the candidate boundary term is \(-1\), but the true positive minimum is \(+1\). The alleged saturating field grows like \(e^y\) and is inadmissible.

**Lesson:** positive bulk energy plus an attractive boundary identity is insufficient. The all-input extension theorem can contain the entire difficult sign question. An arithmetic proposal must prove that theorem from its own structure, rather than assuming the spectral positivity it is intended to establish.

## 7. What cohomological topological field theory contributes

A different meaning of “topological” uses an odd symmetry \(\mathsf q\). Write \(\mathsf q\), rather than \(Q\), to distinguish this symmetry from the Weil quadratic form. Typically \(\mathsf q^2=0\) on the relevant gauge-invariant observables, or closes onto a specified gauge or geometric symmetry. A quantity is \(\mathsf q\)-closed when its variation vanishes, and \(\mathsf q\)-exact when it is the variation of another quantity.

In Witten's topological gauge theory, the stress tensor is a \(\mathsf q\)-commutator. Ward identities then motivate metric independence of suitable correlation functions. This is a statement about a protected sector and its expectation values, not equality of classical energies for every field configuration. [Witten, *Topological Quantum Field Theory*, §2.2, equation 2.33, and §3](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf).

Supersymmetric localization similarly studies deformations schematically written

\[
S_t=S_0+t\,\mathsf q V.
\]

For suitable observables and symmetry-preserving measures, domains, and contours, with \(\mathsf q^2V=0\) in the relevant sense, the integral is independent of \(t\). A suitable bosonic deformation concentrates the calculation on a special locus; fluctuation determinants and residual integrations generally remain. [Pestun–Zabzine, *Introduction to localization in quantum field theory*](https://arxiv.org/pdf/1608.02953). The construction of supersymmetric boundary conditions is an additional part of applying localization on manifolds with boundary. [Sugishita–Terashima, *Exact Results in Supersymmetric Field Theories on Manifolds with Boundaries*](https://arxiv.org/abs/1308.1973).

The following are deductions for this project, not consequences supplied by those papers:

- A useful symmetry would make changes of auxiliary bulk geometry invisible to the chosen boundary quadratic functional, while preserving the arithmetic structure along \(x\).
- The boundary conditions and the rule inserting arbitrary \(f\) must preserve the symmetry actually used in the argument, with no uncancelled boundary variation or quantum anomaly. A symmetry valid only at zero source does not establish the desired identity for arbitrary inputs.
- A localization locus could give the equations \(\mathcal D_LU=0\) in Section 6. Its boundary trace must cover all required inputs.
- Cancellation of bulk fluctuations might help compute a boundary pairing exactly. One must still evaluate the remaining determinants, phases, zero modes, and boundary terms, and show that the answer is the intended quadratic form.
- An equality of partition functions is not by itself an equality of classical energies. Likewise, a second variation of a complex effective action is not automatically a nonnegative form. The route from the protected observable to \(Q_{0,L}[f]\) must be stated explicitly.

### 7.1 Superspace and positivity

Fields could be organized schematically into

\[
\mathcal U(x,y,\theta,\bar\theta)
=u+\theta\chi+\bar\theta\widetilde\chi+\theta\bar\theta\,b,
\]

where \(\theta,\bar\theta\) anticommute, \(u,b\) are even components, and \(\chi,\widetilde\chi\) are odd components. This is packaging; a particular multiplet, reality structure, transformation law, and boundary condition have not been chosen.

A Berezin integral selects components and is not an ordinary positive measure. A supertrace such as \(\operatorname{Tr}((-1)^F e^{-tH})\), with \((-1)^F\) the fermion-parity sign, is a signed index rather than a norm. Ghost and auxiliary spaces are not automatically the physical positive Hilbert space.

There is a separate elementary positivity identity: on a positive Hilbert space, with an actual adjoint and appropriate domains,

\[
\langle\Psi,\{\mathsf q,\mathsf q^\dagger\}\Psi\rangle
=\|\mathsf q\Psi\|^2+\|\mathsf q^\dagger\Psi\|^2\geq0.
\]

This requires identifying both the state \(\Psi\) associated with \(f\) and the operator expectation that equals the arithmetic form. If one restricts entirely to states annihilated by both operators, this particular energy vanishes. A nonzero Weil form would need boundary dynamics, a different observable, or a carefully specified boundary contribution to the algebra.

## 8. Positive gluing: a second way to avoid minimization

There is another possible use of topological field theory: construct a state from a bulk region, then pair it with its reflected conjugate. Reflection positivity is extra structure beyond topological invariance; Freed and Hopkins formulate it in the setting of invertible topological theories. Their work provides a precedent for distinguishing the two properties, not an arithmetic construction or a general realization theorem for the present boundary space. [*Reflection positivity and invertible topological phases*](https://arxiv.org/abs/1604.06527).

Here is the proposed mathematical architecture. For each \(L\), construct a positive Hilbert space \(\mathcal H_L\) and a **linear** boundary insertion map

\[
\Psi_L:C_c^\infty(I_L)\longrightarrow\mathcal H_L.
\]

Suppose a gluing calculation produces the Hermitian pairing

\[
Z_L(g,f)=\langle\Psi_L(g),\Psi_L(f)\rangle_{\mathcal H_L}.
\]

If an independent arithmetic evaluation proves that \(Z_L(g,f)\) is the polarization of \(Q_{0,L}\), then

\[
Q_{0,L}[f]=Z_L(f,f)=\|\Psi_L(f)\|^2\geq0.
\]

This construction would require neither a classical minimum nor a unique interior solution. Its difficult step is the exact evaluation of the glued pairing.

Linearity is substantive: preparing a path-integral state using a general boundary source usually depends nonlinearly on that source. A possible linear map is a smeared insertion \(\Psi_L(f)=\int f(x)\mathcal O(x)|\Omega\rangle\,dx\), provided the operator-valued distribution, reference state, and norm are independently defined. Its two-point kernel would then have to reproduce the Weil distribution, including contact terms. This formula is a candidate specification, not an existing model.

A formal gluing rule does not ensure a positive pairing. Orientation reversal must act as the appropriate adjoint or conjugation, and the physical pairing must be positive after any quotient by null states. The BV–BFV perturbative gluing framework addresses consistency of gauge-theory composition; positive Hilbert-space realization is an additional demand here. [Cattaneo–Mnev–Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*](https://arxiv.org/abs/1507.01221).

## 9. Which directions should be topological?

For this problem, a promising interpretation is **topological or cohomologically invariant in auxiliary bulk directions, with a boundary that retains arithmetic geometry**. This is a proposed design choice, not a theorem about the existence of such a theory.

The positions \(\log n\), the factors \(n^{-1/2}\Lambda(n)\), and the gamma multiplier distinguish specific translations and frequencies. A theory that forgets all scale and positional information along \(x\), without any replacement structure, has no supplied means of selecting those data. The missing information could be carried by labeled defects, background fields, a representation of arithmetic operations, or a specified boundary geometry.

One should therefore state exactly which deformations are meant to leave the energy unchanged. Changing the auxiliary thickness while keeping the arithmetic boundary structure fixed is different from rescaling \(x\): rescaling \(x\) changes the arithmetic delays. Similarly, invariance under deformations of a labeled bulk does not imply invariance under changing the labels themselves.

A useful model could have topological transport in \(y\) and nontrivial evolution in \(t\). Neither is automatically the shifted-zeta evolution in \(\omega\), which has its own parameter-dependent generator in the background. Any such identification would require a separate identity.

One should also avoid reducing the boundary input to finitely many topological labels. For example, if a proposed boundary amplitude depended only on \(r\) moments, its Gram form would have rank at most \(r\). The Weil form at fixed \(L\) has infinitely many independent directions from its logarithmic kinetic term. More concretely, for any prescribed finite number of linearly independent smooth test functions, modulating their span to sufficiently high frequency makes the gamma multiplier grow like \(\log|\tau|\), while the remaining terms stay bounded at that \(L\). This produces positive subspaces of arbitrarily large dimension, incompatible with a finite-rank Gram representation.

Consequently, a finite collection of topological states alone cannot be the whole amplitude space for a linear factorization. Boundary fields, infinitely many channels, or a comparably rich state space would be needed. This does not exclude a topological bulk with a richer boundary theory.

## 10. Necessary and desirable features of a candidate

“Necessary” below means necessary for the indicated proof route. It does not claim that every conceivable proof of Weil positivity needs a field theory, supersymmetry, or topology.

| Feature | Role and status for this proposal |
|---|---|
| Independently positive object | **Necessary for these positivity routes.** Specify a nonnegative physical energy or positive Hilbert pairing without assuming positivity of the target form. |
| Exact arithmetic identity | **Necessary.** Compute the full form, including its constant, pole amplitudes, gamma contribution, and every active prime delay. Agreement with only a kernel away from the diagonal is insufficient. |
| Coverage of boundary inputs | **Necessary.** Every complex smooth compactly supported \(f\) must be represented in the stated construction, at arbitrarily large support lengths. |
| Appropriate trace and domain | **Necessary.** Define finite energy, the trace, conditions at infinity and other edges, and convergence of all channel sums. Extend from the test core only with a justified form argument. |
| Independence from interior representatives | **Necessary for exact descent.** Prove constancy on each trace fiber, or on each constrained trace fiber, rather than only gauge invariance along a subset of variations. |
| Existence of saturating extensions | **Necessary for equality by saturation.** Show that the first-order equations can be solved for all required \(f\). Uniqueness is optional. An approximation variant is described below. |
| Control of global sectors and zero modes | **Necessary whenever present.** Explain which variables are fixed, summed, quotiented, or invisible to energy. Retain boundary zero modes that carry required inputs. |
| Boundary dynamics compatible with the symmetry | **Necessary if symmetry is used.** Include boundary terms and the allowed gauge transformations; arbitrary boundary forcing must not invalidate the identity. |
| A rule selecting the boundary Hamiltonian | **Necessary to make the arithmetic mechanism explanatory.** Free boundary couplings must be specified independently, with a derivation of why they give the Weil form. |
| Positive adjoint-compatible gluing | **Necessary for the state-pairing route; desirable otherwise.** Composition must preserve the relevant positive pairing and control all interface terms. |
| Auxiliary deformation invariance | **Desirable.** It could make a computation independent of bulk thickness, triangulation, or other auxiliary choices, provided the arithmetic data remain fixed. It does not alone prove positivity. |
| Collective arithmetic coupling | **Desirable and constrained by existing results.** The model must escape the excluded classes of independent pairwise squares if it falls within their hypotheses. |
| Exact quadratic dependence on \(f\) | **Necessary for the proposed matching.** In a nonlinear or quantum model, higher powers of source amplitude must cancel or be absent for a proved reason. A small-source approximation alone is insufficient. |
| Compatibility across support lengths | **Desirable for a unified theory.** Exact matching separately at unbounded lengths already suffices for RH; an explicit extension or gluing law could explain why those matches persist. |
| A controlled treatment of degeneracy | **Desirable and sometimes necessary.** Near-zero boundary energies and null states must be compatible with all positive components; a uniform spectral gap should not be imposed without reason. |

### 10.1 Boundary polarization and the danger of overconstraint

In a first-order field theory, one normally chooses which boundary variables to prescribe; fixing every member of a conjugate pair can overdetermine the equations. A boundary polarization is such a choice of prescribed variables. In this project it must leave room for an arbitrary input function, with the remaining boundary response determined by the bulk.

Similarly, a holomorphic, chiral, or harmonic constraint may admit only a proper subspace of boundary profiles. A proof for that subspace cannot silently be promoted to all \(C_c^\infty(I_L)\). One can add complementary components or prove that a different boundary variable covers all inputs, but the coverage statement must be explicit.

### 10.2 Approximate saturation can still prove positivity

Exact attainment is stronger than necessary for a sign argument. If the identity in Section 6 holds and, for each \(f\), there are admissible fields \(U_j\) with the **same** trace \(f\) and

\[
\|\mathcal D_LU_j\|\longrightarrow0,
\]

then \(\mathcal E_L[U_j]\to B_L[f]\). Nonnegativity of the energies gives \(B_L[f]\geq0\), and the lower bound gives \(\inf\mathcal E_L=B_L[f]\). There need not be a limiting bulk field. This retains an infimum rather than replacing it by evaluation on an actual solution, but may provide a more flexible proof route.

If only approximate boundary traces are available, one needs a limit argument that transfers the boundary energies to \(B_L[f]\), for example convergence in the form topology. Ordinary \(L^2\) convergence alone does not ensure convergence of an unbounded form. Lower-semicontinuity alone also does not transfer nonnegativity in the required direction: it bounds the energy at the limit from above by a liminf, rather than from below.

## 11. Arithmetic structure a topological proposal would have to explain

### 11.1 Defects and arithmetic labels are possibilities, not a derivation

Labeled lines, interfaces, or channels could represent translations by \(\log n\). Multiplicative arithmetic has a natural additive expression in this coordinate:

\[
\log(mn)=\log m+\log n.
\]

One could therefore seek a composition rule for labeled operations whose boundary action realizes arithmetic translation. This observation does not determine the weights \(\Lambda(n)/\sqrt n\), explain why only prime powers occur, or supply positivity.

The first useful computation would identify the operator assigned to a label, its adjoint, and the composition of two labels. Squaring amplitudes involving multiple translations can generate unwanted mixed delays, including differences of their displacements. A successful algebra must derive the desired cross terms and cancel or explain the unwanted ones, while accounting for the positive diagonal terms introduced by the same squares.

Topological invariance of a defect network could then make equivalent compositions give the same answer. That would be valuable only after an independent arithmetic labeling and evaluation rule has been supplied.

### 11.2 The gamma term needs more than a simple boundary gradient

The existing gamma kinetic realization has infinitely many channels with

\[
a_k=2k+\tfrac12,
\qquad
\mathcal E^{\mathrm{kin}}[\widetilde f,(u_k)]
=\sum_{k\geq0}\frac2{a_k}
\int_{\mathbb R}
\left(|\widetilde f-u_k|^2+a_k^{-2}|u_k'|^2\right)dx.
\]

Its minimization produces the multiplier

\[
\sum_{k\geq0}\frac2{a_k}\frac{\tau^2}{a_k^2+\tau^2}
=\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).
\]

This is a concrete positive ingredient, described in the background and Section 5 of the attempt. It is **not** extension-independent: at zero boundary input, a nonzero finite-energy channel variation generally has positive energy. Restricting to its equilibrium configurations gives equality by minimization, without making the unrestricted system topological.

A topological or cohomological reformulation would need to add a useful structural explanation, such as a boundary identity, protected pairing, or constraint algebra. Repackaging the existing equilibrium equations in new notation would not establish the missing completion.

The full form also contains \((\psi(1/4)-\log\pi)\|f\|^2\), the pole terms, and the prime terms. They cannot be discarded or inserted as unsigned corrections to a positive energy.

### 11.3 Existing restrictions remain applicable

The [positive-factorizations manuscript](../investigations/positive-factorizations/manuscript.tex) contains working results that any new candidate should respect:

- **Independent pairwise squares:** Section 6 excludes its precisely defined class of positive two-point representations already at a prime-free length. Finite positive networks assembled from such squares retain comparison positivity after the specified Schur eliminations. Calling hidden nodes topological does not change this algebra. Singular continuum limits require their own analysis; the finite result is not a theorem excluding every continuum model.
- **Joint gamma and prime accounting:** Sections 7–8 show why adding isolated prime channels with a simple diagonal debit fails in the demonstrated case. The first prime can stabilize a negative gamma direction while acting with the opposite sign on another channel. A common energy must account for both effects.
- **The global input norm:** Section 9 proves a restriction on a single closable factor defined on ordinary whole-line \(L^2\) and containing all smooth compactly supported inputs. Separate finite-interval realizations remain possible, as do appropriate other input topologies. A topological Hilbert-space proposal should specify which setting it uses before claiming a global closed factor.

These are restrictions at their stated scopes, not exclusions of topological or supersymmetric methods as a whole. The manuscript's review status remains as recorded in the program; this note does not constitute a new independent review of those results.

### 11.4 Gluing must preserve interactions across the interface

The source form agrees on a fixed input when that input is regarded as lying in a larger interval. A model that matches it must reproduce this fact. If a long input is split into \(f_1+f_2\), its energy includes the polarized interaction

\[
Q_{0,L}[f_1+f_2]
=Q_{0,L}[f_1]+Q_{0,L}[f_2]
+2\operatorname{Re}q_{0,L}(f_1,f_2),
\]

where \(q_{0,L}\) is the Hermitian form associated with \(Q_{0,L}\). A gluing construction must retain the interface variables or pairing that generates this cross term, including prime delays crossing the cut. Adding nonnegative energies of isolated short pieces does not address it.

## 12. A focused investigation sequence

The next investigation should aim to identify a mechanism valid at arbitrary length, using small cases to test a specified mechanism rather than treating a longer numerical certificate as the main objective.

1. **Choose the mathematical route.** Decide between exact descent, constrained energy, saturation, or a positive glued pairing. State which object is positive and what it means for the bulk to be topological in that route.
2. **Specify one candidate completely.** Give its fields, symmetry, boundary variables, trace, sectors, energy or pairing, and arithmetic labels. If using superspace, specify the component transformations and the physical positive space.
3. **Derive its boundary functional.** Calculate the polarization on arbitrary pairs of test functions. Check the constant and diagonal terms as well as the visible nonlocal kernel. Determine whether free boundary choices have merely encoded the target.
4. **Prove boundary coverage.** For a constrained or saturating construction, analyze existence for all complex test inputs, including nonzero mean and both reflection parities. For a state construction, establish linearity, finite norm, and the relevant domains.
5. **Test the mechanism where it can fail.** Check the gamma contribution, the first-prime coupling, and a composition with at least two interacting arithmetic labels. Include a separated-support polarization test to expose missing cross terms. Compare with the known pairwise and global-domain restrictions.
6. **Establish the arbitrary-length rule.** Prove that extending support or composing regions preserves exact matching and positivity with all interface terms. Separate any approximation or regularization limit from formal identities.

A useful first deliverable would be an explicitly defined positive boundary pairing or an energy identity with a proved trace-coverage statement in a toy model that has at least one genuinely nonlocal coupling. Its value would be to expose how the mechanism selects a boundary kernel and where arithmetic could enter. It should not be presented as progress on full Weil positivity unless the arithmetic matching is actually established.

## 13. Questions that would distinguish a substantive proposal

- What makes the bulk energy independent of interior choices: a null-space identity, gauge equivalence, field equations, or a Ward identity for a specified observable?
- Where is positivity proved, and does that proof apply before the arithmetic matching is assumed?
- Which boundary datum is the test function \(f\), and why does every required \(f\) occur?
- Does the topological structure determine the boundary Hamiltonian, or only its phase space and symmetry? What independent rule supplies the remaining data?
- What retains the scale and arithmetic information in \(\log n\), \(\Lambda(n)\), and the gamma factor?
- If a protected sector is used, why does it produce an ordinary positive quadratic form rather than an index, phase, or pairing with indefinite sign?
- How do boundary modes and global sectors participate in gluing, especially when a prime delay crosses an interface?
- Is a claimed simplification removing the variational problem, or moving it into an unproved all-input solvability or spectral assertion?

The strongest potential contribution of topology would be an identity or composition principle explaining why one independently positive construction reproduces the complete arithmetic form at arbitrary length. Boundary reduction alone is a useful organizing idea, but that selection principle is the unresolved mathematical objective.

## 14. Reading guide and provenance

The elementary descent criterion, theorem template, matrix half-line example, and project-specific deductions are derived in this note. The following sources supply field-theory precedents, with their use limited to the claims cited in the text. They are not cited as evidence for a Weil-form realization.

| Source | Suggested entry point |
|---|---|
| [Tong, *Lectures on the Quantum Hall Effect*](https://arxiv.org/abs/1606.06687) | [Chapter 6, §6.1.2](https://www.damtp.cam.ac.uk/user/tong/qhe/six.pdf): the explicit Chern–Simons boundary example. |
| [Geiller–Jai-akson, *Extended actions, dynamics of edge modes, and entanglement entropy*](https://arxiv.org/abs/1912.06025) | Section 4: edge fields and choices of boundary dynamics. |
| [Cattaneo–Mnev–Reshetikhin, *Classical BV theories on manifolds with boundary*](https://arxiv.org/abs/1201.0290) | Sections 5.4 and 7: BF and Chern–Simons examples with boundary structures. |
| [Witten, *Topological Quantum Field Theory*](https://www.ias.edu/sites/default/files/sns/%5B109%5DCommMathPhys117-1988.pdf) | Sections 2.2–3: the cohomological meaning of metric independence. |
| [Pestun–Zabzine, *Introduction to localization in quantum field theory*](https://arxiv.org/abs/1608.02953) | An entry point to localization and its mathematical setting. |
| [Sugishita–Terashima, *Exact Results in Supersymmetric Field Theories on Manifolds with Boundaries*](https://arxiv.org/abs/1308.1973) | Examples where boundary conditions are part of the supersymmetric construction. |
| [Freed–Hopkins, *Reflection positivity and invertible topological phases*](https://arxiv.org/abs/1604.06527) | Reflection positivity as added structure; the invertible-theory scope is essential. |
| [Cattaneo–Mnev–Reshetikhin, *Perturbative quantum gauge theories on manifolds with boundary*](https://arxiv.org/abs/1507.01221) | Gauge-theory quantization compatible with cutting and gluing. |

Online sources checked 12 September 2026. This is a targeted conceptual reading, not an exhaustive literature or priority review. The local background remains authoritative for the program's normalization and existing results.
