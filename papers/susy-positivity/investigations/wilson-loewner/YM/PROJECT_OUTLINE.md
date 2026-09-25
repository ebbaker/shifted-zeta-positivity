# YM realization of the Weil form: project outline and background

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model: GPT-6 (Codex). Reasoning effort: not exposed; not inferred.  
Status: working research outline. OS positivity is an allowed assumption; the arithmetic realization is an open objective. No RH proof is claimed.

## 1. Overall goal

Investigate whether a specified Yang–Mills theory contains an admissible family of sources whose reflected inner product is exactly the Weil form for the Riemann zeta function. An existence proof is a valid endpoint; an explicit formula for every source is not required. Under assumed Osterwalder–Schrader (OS) positivity, such an identification would imply the Riemann Hypothesis (RH).

The project seeks one global source law, valid for every smooth compactly supported arithmetic input. The support length \(L\) is a property of an input, not a parameter used to redesign the model. Success at a few values of \(L\), or a small family of positive numerical matrices, does not establish this objective. A uniform strictly positive gap is not required either: an exact nonnegative pairing is sufficient.

The current physical starting point is pure four-dimensional \(SU(N)\) YM at theta zero, with the finite Wilson slab below as a concrete regulator. The rank, coupling, lattice, and state must be fixed once for any proposed theorem. No particular rank or coupling has yet been selected as the arithmetic realization. A continuum formulation is permitted if its existence and source-domain hypotheses are stated. Adding dynamical matter or a new defect theory would be a change of model, to be discussed explicitly.

A second goal remains in scope: a native causal YM preparation/evolution/readout system realizing the parent's shifted-zeta transfer and its ordinary energy balance. That requires additional identities beyond the reflected Weil pairing. Neither goal is to be discarded merely because an abstract arithmetic positivity route is weaker or easier to state.

## 2. Arithmetic background: zeta, RH, and a quadratic form

For \(\operatorname{Re}s>1\),
\[
\zeta(s)=\sum_{n\ge1}n^{-s}=\prod_p(1-p^{-s})^{-1}.
\]
Its analytic continuation has a pole at \(s=1\). The completed entire function
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
satisfies \(\xi(s)=\xi(1-s)\). RH says that all its zeros have real part \(1/2\).

The explicit formula relates these zeros to prime powers and the gamma factor. Weil's criterion expresses RH as nonnegativity of the associated quadratic form on every compactly supported smooth test. This is useful here because a physical Hilbert-space norm is automatically nonnegative. The hard step is proving it is the same form, with the correct signed arithmetic terms and normalization.

### 2.1 Conventions and exact target

Use the logarithmic coordinate \(x\in\mathbb R\), complex tests \(f\in\mathcal D=C_c^\infty(\mathbb R)\), and
\[
\widehat f(\tau)=\int_{\mathbb R}e^{-i\tau x}f(x)\,dx,
\qquad U_a f(x)=f(x-a),
\qquad \langle f,g\rangle=\int\overline f g.
\]
For a test supported in \(I_L=(-L/2,L/2)\), define
\[
\begin{aligned}
Q[f]={}&K_\Gamma[f]+w_0\|f\|_2^2+P[f]\\
&-2\sum_{\substack{p\text{ prime},\ m\ge1\\m\log p<L}}
(\log p)p^{-m/2}\operatorname{Re}\langle f,U_{m\log p}f\rangle,
\end{aligned}
\tag{1}
\]
where
\[
\begin{gathered}
w_0=\psi(1/4)-\log\pi,\qquad \psi=\Gamma'/\Gamma,\\
K_\Gamma[f]=\frac12\iint_{\mathbb R^2}|f(x)-f(y)|^2 n_\Gamma(|x-y|)\,dx\,dy,\\
n_\Gamma(r)=\frac{e^{-r/2}}{1-e^{-2r}},\qquad r>0,\\
P[f]=2\left|\int f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int f(x)\sinh(x/2)\,dx\right|^2.
\end{gathered}
\tag{2}
\]
All tests are zero outside their support. Near \(x=y\), the smooth difference cancels the kernel singularity. The prime sum is finite at any fixed support length because sufficiently large shifts have disjoint supports. Different choices of an enclosing interval produce the same form: additional shift terms vanish. Polarization defines the Hermitian pairing \(Q(f,g)\), antilinear in its first argument.

For a Fourier description,
\[
K_\Gamma[f]=\frac1{2\pi}\int b(\tau^2)|\widehat f(\tau)|^2\,d\tau,
\quad b(\tau^2)=\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).
\tag{3}
\]
The gamma term is positive, but the contact \(w_0\), prime cross terms, and pole term cannot be omitted. Independent positive models for the gamma and prime sectors do not by themselves prove positivity of their completed signed combination.

### 2.2 A smaller test class that is still sufficient for RH

The immediate target can use the global pole-neutral class
\[
\mathcal D^0=\left\{f\in\mathcal D:
\int e^{x/2}f(x)\,dx=\int e^{-x/2}f(x)\,dx=0\right\}.
\tag{4}
\]
Then \(P[f]=0\). Positivity of (1) for every test in this class is still RH-equivalent. These constraints correspond to Mellin vanishing at 0 and 1; the normalization and restricted criterion are recorded in [Connes–Consani, Appendices B–C](https://arxiv.org/html/2006.13771v1).

An exact way to generate these tests is
\[
f=(-\partial_x^2+1/4)h,\qquad h\in C_c^\infty(\mathbb R).
\tag{5}
\]
Every pole-neutral test has such an \(h\) without enlarging its enclosing support interval. This avoids treating the moment constraints approximately.

The gamma/contact multiplier is
\[
a_\Gamma(\tau)=\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi
\sim\log\frac{|\tau|}{2\pi}.
\tag{6}
\]
Consequently the source topology matters: a smooth-test or suitable logarithmic-form topology is appropriate. An ordinary \(L^2\)-bounded source map cannot realize the target at arbitrarily high frequency.

### 2.3 The additional shifted-transfer target

For a positive arithmetic shift \(\omega\) and complex Laplace variable \(z\), the parent program specifies
\[
K_\omega(z)=\frac{\xi(1/2+z-\omega)}{\xi(1/2+z+\omega)}.
\]
A native causal realization would obtain this function from actual YM preparation, evolution, and readout, so that the transformed output equals \(K_\omega(z)\) times the transformed input on a suitable half-plane. Its energy estimate would have to use the ordinary physical source/output norm and imply the arithmetic contraction criterion in the required support and shift limits. Writing the ratio into an auxiliary filter does not establish this physical identification.

The shift \(\omega\), logarithmic support length \(L\), physical time, and Loewner contour capacity are separate parameters. No identification among them is assumed. The [arithmetic source note](../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) derives the ratio's source equation and explains why its relation to a geometric Loewner evolution does not yet supply the physical realization.

## 3. Physical background: lattice YM and OS positivity

On a finite lattice, put an \(SU(N)\) matrix \(U_\ell\) on each oriented link. The reverse link has matrix \(U_\ell^\dagger\). A plaquette holonomy \(U_p\) is the ordered product around an elementary square. The Wilson action and measure are
\[
S(U)=\beta\sum_p\left(1-\frac1N\operatorname{Re}\operatorname{tr}U_p\right),
\qquad d\mu(U)=Z^{-1}e^{-S(U)}\prod_\ell dU_\ell,
\tag{7}
\]
with Haar link measures. A Wilson loop is the normalized trace of a holonomy around a closed contour; based matrix loops also retain reference color indices for subsequent gauge-invariant contraction.

OS reflection \(\Theta\) reflects physical Euclidean time and includes the appropriate complex/matrix adjoint. For a stated half-space observable domain \(\mathcal A_+\), the assumption is
\[
\omega_{\mathrm{YM}}((\Theta A)A)\ge0,\qquad A\in\mathcal A_+.
\tag{8}
\]
This defines a nonnegative sesquilinear form. Quotienting null vectors and completing gives the OS Hilbert space. Sources and operators must descend through this quotient; positivity does not automatically make arbitrary interior multiplication admissible. A complete relativistic reconstruction requires further conditions beyond (8). For the immediate arithmetic implication, the source pairing and its positivity are sufficient.

### 3.1 The concrete boundary realization already available

The existing finite regulator has a spatial three-torus and Euclidean-time sites \(-T,\ldots,T\), with open outer boundaries. Write \(U\) for central-slice spatial links and \(X_\pm\) for the half-slab interiors. The action splits as
\[
S=S_0(U)+S_+(U,X_+)+S_-(U,X_-).
\]
Define
\[
\Omega(U)=e^{-S_0(U)/2}\int e^{-S_+(U,X_+)}dX_+,
\quad d\nu(U)=Z^{-1}\Omega(U)^2dU.
\tag{9}
\]
This is the actual finite-slab boundary state. It is smooth and strictly positive on the compact link manifold. It has not been identified with an infinite-time vacuum.

For based covariant matrix-valued boundary functions \(B,C\), gluing gives
\[
\langle B,C\rangle_{\mathrm{OS}}
=\int\frac1N\operatorname{tr}(B^\dagger C)\,d\nu.
\tag{10}
\]
Boundary multiplication preserves the reflected null space; unitary loop multiplication is unitary in this space. In particular a matrix loop \(Q_C\) has norm one. The reference endomorphism fiber retains singlet and adjoint channels and adds no dynamical bulk matter; it is more than the ordinary scalar singlet sector and must be stated as such.

This provides a genuine YM setting in which to ask an existence question. It does not identify a family indexed by arithmetic tests, supply prime weights, or establish a continuum theorem. See the [finite-slab derivation](notes/FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md).

## 4. The desired global theorem

Fix the YM model and state, physical reflection, admissible observable sector or completion, and an independently specified arithmetic action on sources. Assuming (8), prove that there exists one continuous linear map
\[
J:\mathcal D^0\longrightarrow\mathcal H_{\mathrm{YM}}
\]
with the required source interpretation and intertwining properties, such that
\[
Q(f,g)=\langle Jf,Jg\rangle_{\mathrm{OS}}
\qquad \text{for every }f,g\in\mathcal D^0.
\tag{11}
\]
Then \(Q[f]\ge0\) and the criterion in §2 implies RH, conditional on the stated physical hypotheses. Realizing the full \(\mathcal D\) form, including \(P\), is an optional stronger endpoint.

| Item | Current role |
|---|---|
| OS positivity on the stated source domain | Allowed assumption; not the research bottleneck |
| A fixed finite Wilson slab and its boundary Hilbert space | Explicitly available |
| Existence of a chosen continuum YM state, if used | Additional hypothesis or separate theorem |
| Continuous arithmetic source map in the allowed observable class | Main open existence problem |
| Global identity (11), with exact coefficients | Main open identification problem |
| Native causal preparation, evolution, readout, energy balance | Additional physical target |

Abstract GNS, dilation, or Hilbert-space embedding arguments applied to \(Q\) would require its positivity as input. They do not prove the desired bridge. A nonconstructive proof must obtain occurrence and the pairing from independent YM/source structure. Existence inside a prescribed observable class can be stronger than RH-equivalent abstract positivity.

## 5. Proposed proof routes and their obligations

### A. Occurrence of a source module plus uniqueness of its pairing

A source module means a vector space of allowed sources together with specified operations and relations. Find one inside the YM sector; an existence theorem may suffice. Derive global Ward or intertwining identities for its reflected pairing. Prove that these identities and normalizations determine a unique continuous Hermitian pairing, allowing forms of unknown sign. Verify independently that \(Q\) obeys them. The identity with the positive YM pairing then follows.

The two central unknowns are whether the arithmetic module occurs in YM and whether its relations are sufficiently restrictive. Uniqueness only among already positive forms would leave the sign of \(Q\) unproved. Simply postulating all its known coefficients as positive moments restates the target.

### B. Compatible approximation in a fixed YM source space

Prove the existence of approximate sources for arbitrary finite sets of tests and source identities, together with estimates that produce a compatible global limit. Ordinary weak Hilbert-space compactness is insufficient because norm can be lost.

The [current audit](notes/GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md) proves a sufficient replacement: uniformly bounded maps into a stronger source Hilbert space compactly embedded in the fixed OS space have a strongly convergent subsequence on all tests, provided the bounds use local smooth-test seminorms and the pairings converge on a dense family. Strong convergence preserves the pairings. Finite boundary Sobolev spaces provide concrete candidate stronger norms.

The unresolved part is obtaining the approximants and uniform bounds from YM/arithmetic relations. Approximation only for a few supports does not supply them. An approach based instead on free moments must also prove that its limiting state is the intended YM state, rather than another positive theory.

## 6. Results and obstructions obtained so far

| Finding | What it accomplishes | What remains open |
|---|---|---|
| Exact finite-slab reflected boundary norm | Gives admissible YM loop vectors and null-space descent | Arithmetic source identification |
| Continuous storage/memory identities and discrete residual bounds | Distinguishes exact norm conservation from loss under finite compression | An accurate useful small hierarchy and a stationary arithmetic action |
| First interacting SU(2) experiment on a \(6^3\)-by-5 slab, \(\beta=1.6\) | Tests actual Wilson-measure correlations; small trial families leave large residuals | Controlled enlargement; no arithmetic match or global conclusion follows |
| Fixed-support high-frequency probe | Shows \(Q[f_\lambda]\sim\|h\|_2^2\log\lambda\) for bounded-amplitude pole-neutral tests | A generalized source reproducing that growth |
| Ordinary bounded-loop smearing exclusion | Rules out \(Jf=\int f(x)Q_xdx\) and locally norm-integrable variants | Distribution-valued/insertion sources remain possible |
| Euclidean-semigroup exclusion | Arithmetic translations cannot equal positive-Hamiltonian Euclidean decay on an exact source image | A native unitary arithmetic action or another causal correspondence |
| Full finite-lattice integration-by-parts uniqueness | Identifies the Wilson state without assuming a density first | Selection of the arithmetic source map |
| Compact source-control criterion | Supplies a sufficient nonconstructive limit preserving norms and pairings | Global approximants, uniform stronger bounds, and retained source relations |
| Native translation-generator audit | Requires an unbounded two-sided nonperiodic generator; rules out semibounded Hamiltonians and periodic link rotations in that role | A specific admissible generator with arithmetic determining relations |
| Generalized source via spectral calculus | Gives a continuous global source class from a generator and finite-order generalized vector | Native YM occurrence and equality of its spectral pairing with the Weil form |

The analytic entries are proved or scoped in the [global source and Ward-identity audit](notes/GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md) and its [native-generator continuation](notes/NATIVE_TRANSLATION_GENERATORS_AND_GENERALIZED_SOURCES_20260924.md). They are research-note results, not independently reviewed claims of novelty. The first interacting test remains a finite statistical diagnostic.

The source coordinate must be treated carefully. Common logarithmic translations preserve \(Q\), so an exact source image carries a unitary translation action. Physical Euclidean decay is contractive, and Loewner capacity labels contour growth. These are distinct operations until an actual intertwining statement is proved. Keeping this distinction does not remove the causal realization objective.

## 7. Immediate work and decision points

The next phase should test a global mechanism before expanding the list of finite support certificates.

1. **Specify the source core and arithmetic action.** Start with the existing boundary completion, covariant loop functions, and properly adjointed link/field insertions. The arithmetic generator must be unbounded in both spectral directions and nonperiodic. The native-generator note gives the concrete source class \(Jf=[\widehat f(\lambda)(1+\lambda^2)^{s/2}](G)\eta\). The next obligation is a native choice of \(G\), an admissible seed \(\eta\), and determining relations; choosing their spectrum from presumed RH would be circular. State the source topology and reference-color sector.
2. **Derive a mixed identity from the model.** Compute the relevant Ward/intertwining relations with their domains and adjoints. The sought relation must couple the source's archimedean behavior to its arithmetic shifts; separate positive sectors and translation symmetry alone do not do this.
3. **Test determination globally.** Calculate which continuous Hermitian pairings satisfy the relation set. Translation/reflection symmetry, leading logarithmic growth, and finitely many normalizations leave infinitely many possibilities. A successful next result must eliminate that freedom or identify exactly which additional relation is missing.
4. **Choose the existence proof.** Pursue occurrence plus uniqueness if a sufficiently restrictive module appears. Pursue compact approximation if the source hierarchy supplies uniform stronger bounds and an extension principle. Prove the needed property for arbitrary finite collections, not only displayed examples.
5. **Use computation to check those statements.** Appropriate calculations test exact candidate identities, source-domain estimates, or a concrete finite obstruction. Further loop-family Monte Carlo work remains useful for the physical hierarchy, but is not by itself progress on the global arithmetic match.
6. **Return to the causal target with a precise dictionary.** Specify physical preparation, time evolution, readout, and storage; prove how the already-defined shifted transfer arises. Reflected positivity alone does not supply this dictionary.

A decisive negative result about one source class should lead to a stated class change, not repeated adjustment of \(L\). A decisive positive result should be an all-support identity, representation theorem, or compatible extension/bound, not merely another positive finite matrix.

## 8. Organization and reading order

- This file is the maintained project-level outline; it is intended to be readable without earlier discussion.
- [Global existence under assumed OS positivity](notes/YM_EXISTENCE_ASSUMED_OS_AND_GLOBAL_SCOPE_20260924.md) records the agreed scope and nonconstructive objective. It was moved into this investigation from the parent notes directory.
- [Global source and Ward-identity audit](notes/GLOBAL_SOURCE_AND_WARD_IDENTITY_AUDIT_20260924.md) is the first analytical continuation under that scope.
- [Native translation generators and generalized sources](notes/NATIVE_TRANSLATION_GENERATORS_AND_GENERALIZED_SOURCES_20260924.md) tests natural operators, derives the exact weighted-flow generator, and formulates the next global source class. A fixed flow's weighted adjoint is conjugate to its unweighted generator, so the YM density alone does not determine its spectrum.
- [Notes index](notes/README.md) links the finite-slab, hierarchy, and interacting-test records.
- [Numerics index](numerics/README.md) contains reproduction details and the existing small records.
- The parent [arithmetic bridge sweep](../notes/ARITHMETIC_BRIDGE_SWEEP_AFTER_YM_20260924.md) and [bootstrap design discussion](../notes/ARITHMETIC_BOOTSTRAP_DESIGN_AND_OPEN_GAPS_20260924.md) remain background. Their recommendation to lead with isolated support windows is superseded by the global scope here.

Save incremental analysis in `notes/`, numerical code and small results in `numerics/`, and independent assessments in `reviews/`. Follow the repository's large-file policy. Future manuscript milestones should be indexed concisely in a draft-history file with commit/tag references rather than copied manuscript snapshots. Every new note or review records its model and exposed effort setting and acknowledges LLM assistance.
