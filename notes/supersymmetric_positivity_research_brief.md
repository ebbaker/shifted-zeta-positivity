# Shifted zeta positivity and supersymmetric routes

Pedagogical research brief • 11 September 2026

## 1 Purpose and current assessment

The shifted zeta program seeks a physical or geometric reason for the positivity that is equivalent to the Riemann hypothesis. Its original motivation was to construct a positive bulk system whose boundary response reproduces the appropriate zeta data. The present proposal is to investigate whether supersymmetric quantum mechanics or a related Dirac or Hodge construction can supply that independent source of positivity.

The program already has exact reformulations, explicit operators built from gamma and prime data, and substantial finite depth positivity results. It does not yet have a global physical mechanism that forces positivity. Supersymmetry is being considered because it suggests how such a mechanism might be organized, not because an arithmetic supercharge has been found.

This brief preserves the reasoning behind that choice. Sections 2 through 5 explain the history, motivation, and selection of the proposed routes before introducing their detailed mathematical targets. Sections 6 through 10 specify the objects, constraints, and first investigations. Sections 11 and 12 provide a way to interpret outcomes and carry lessons into a different approach. The proposed investigations have not been carried out in this brief.

## 2 How the program arrived at positivity

### Higher dimensions and the search for an additional constraint

The initial idea was to extend the Riemann xi function into higher dimensions and use rotational symmetry to constrain its zeros. The research explored quaternionic and slice regular functions, twistor ideas, and related constructions. The recurring difficulty was that the extensions did not produce an additional usable restriction on the original complex zeros. The information recovered from the higher dimensional formulation was already encoded in the complex formulation. This account comes from the program history and the researcher's description of its motivation. [P1]

That experience teaches a specific lesson. An extra coordinate or symmetry is useful only if it brings a theorem or structure that can be applied to the original problem. Rewriting the same data is not inherently useless: a change of representation can expose an inaccessible argument. But the new representation must do more than restate the desired conclusion in a different language.

### Why the search remained connected to physics

The researcher's background is in physics, which makes questions about dynamics, energy, symmetry, and boundary observables natural sources of insight. The search consequently broadened to Yang–Mills theory, supersymmetric gauge theories, Chern–Simons theory, and ideas inspired by AdS/CFT. Earlier specific proposals encountered their own obstructions; their failure does not establish a general obstruction to every use of those subjects. The historical note index records those investigations, but an index entry should not substitute for reading the underlying argument when a route is reconsidered. [P1, P8]

The most useful surviving question was whether the zeta object could be realized as a response at the boundary of an independently specified physical system. Such a realization could change the source of the argument: positivity would follow from the physical system's structure, and the arithmetic consequence would follow from identifying its boundary response.

### The original bulk and boundary ambition

The August 31 overview states the organizing question explicitly: can RH be explained through a boundary theory induced by an independently positive radial bulk? The shifted screw functions, arithmetic Hankel operators, and inverse spectral constructions provided a concrete mathematical setting for asking it. [P2]

Here “bulk” initially means an auxiliary system with internal propagation, storage, or spectral structure. “Boundary” means a response or quadratic form seen by the external data. These words do not assert the existence of an AdS geometry, a conformal field theory, or an established holographic duality. A linear wave equation, a string, or a passive network could already be enough if its response had the required arithmetic identity.

The intended explanation has four stages. The global quantifiers belong to the final stage and cannot be supplied by a finite example.

```mermaid
flowchart LR
    A[Gamma and prime data] --> B[Independent positive bulk]
    B --> C[Exact zeta boundary response]
    C --> D[Global positivity and RH]
```

The unresolved task is to construct the middle stages in the required family and prove the global passage. A bulk reconstructed from a spectral measure already assumed positive does not reverse that dependency.

## 3 What the existing work has taught us

### A useful dictionary and finite results

The shifted setting connects several objects: zeta transfer functions, causal operators, Hankel forms, strings, and positive spectral measures. This dictionary matters because it makes a physical question precise enough to test. The first slab, before the arithmetic threshold at log 2, gives an independently specified gamma system whose positivity can be studied without assuming a zero free region. Later Weil depth and storage depth work extends finite positivity beyond that slab through rigorous bounds and computer assisted certificates, with verification status recorded separately in the project. [P3–P5]

These are mathematical accomplishments. They establish finite statements and reveal which estimates retain or lose the information needed for continuation. They do not establish positivity at every depth. A growing list of successful finite certificates also does not identify the mechanism that would make every subsequent case succeed.

### The source of the concern about a missing mechanism

In the current coordinates, the Weil form combines gamma terms with signed arithmetic couplings. Positivity is not visible term by term. The recent barrier analysis explains why a particular strategy, bounding the gamma and arithmetic parts separately on a complement, becomes expensive. Its essential spectrum argument prevents a finite dimensional head from removing the worst arithmetic Rayleigh quotient from that complement. The numerical decay laws for the smallest eigenvalue remain conjectural extrapolations. [P6]

This supports a change of emphasis toward structural questions. It does not prove that the full joint form lacks a useful factorization, nor that every possible bulk model must fail. In particular, a negative term in an expansion is not an obstruction to positivity of the complete operator.

The disagreement in the recent assessments is therefore best stated narrowly. There is strong reason to doubt that routine certificate refinement alone will become a proof strategy for RH. There is not yet a no-go theorem for an independent bulk mechanism. The original motivation was preserved in the overview and first-slab paper; the numerical branch increasingly addressed finite verification in place of the still unresolved explanatory step. [P2, P3, P7]

### A standard for conceptual progress

An explanatory advance would identify a structure that forces the relevant sign: a positive Hilbert space with a suitable operator, an energy identity whose density is independently nonnegative, or a composition rule with a proved positivity invariant. This is the useful aspiration behind comparisons with geometric proofs of the Weil conjectures. The comparison does not mean that all such proofs use the same positivity argument or that their geometry is already present here.

The practical test is dependency. Which assertion supplies the sign, and what was assumed to prove that assertion? A new vocabulary is helpful only if it exposes an independent step or makes an existing difficult step more accessible.

## 4 Why supersymmetry is a relevant next question

### Positivity from a defining operator

Supersymmetric quantum mechanics offers a simple model of the desired dependency. One begins with an operator and a positive inner product, forms its adjoint, and obtains a Hamiltonian as a square or anticommutator. Positivity then follows from a norm identity. The difficult problem can be the identification of that Hamiltonian or its boundary response with an object of interest.

This shifts attention from estimating the final quadratic form to discovering the operator that generates it. Witten's use of the exterior differential and its adjoint in Morse theory illustrates how a supersymmetric organization can be mathematically productive when the defining operators have independent geometric meaning. [E1]

For the zeta program, the hoped-for counterpart would be an operator defined from the actual gamma and prime data. Its square would reproduce the required joint form, or its dynamics would produce the required boundary response. Supersymmetry supplies a possible architecture for an explanation; arithmetic must still supply its content.

### The relationship to BRST

BRST quantization is a related but distinct construction. A nilpotent BRST charge organizes gauge redundancy, with physical states described through cohomology, roughly the kernel of the charge modulo its image at the relevant ghost number. Nilpotence by itself does not prove that this physical space has a positive inner product. A no-ghost or equivalent positivity argument is still required. Introducing an adjoint can produce a Hodge Laplacian, but that Laplacian is not automatically the physical Yang–Mills Hamiltonian. [E2]

Ordinary supersymmetric quantum mechanics can also use nilpotent complex supercharges. The distinction is not simply “nilpotent versus nonnilpotent.” The relevant questions are which adjoint is used, whether the inner product is positive, and which anticommutator is identified with the Hamiltonian. BRST has not by itself resolved the rigorous construction of four dimensional quantum Yang–Mills theory. [E3]

A BRST route would become specifically motivated here if a candidate bulk introduced a genuine gauge redundancy and a physical quotient that had to be controlled. At present, an ordinary supersymmetric or Hodge construction is the more direct way to investigate the square root idea without introducing a gauge system whose necessity has not been established.

## 5 Why we have selected two paths

The first proposed path works directly with the central Weil form. It asks for a factorization through an independently defined arithmetic operator. This is the shortest connection to the object already studied and makes comparison with existing kernels and certificates straightforward. It is also demanding: a global factorization would supply the RH-level positivity itself.

The second path begins with a larger positive bulk and derives its boundary response. This more closely follows the original physical motivation and permits auxiliary components, internal channels, and different coordinates. Its challenge is fidelity: a positive system is easy to construct in isolation, but its response must equal the required zeta object with the correct analytic properties and limits.

These paths are complementary. A direct factorization could suggest a bulk model. A bulk model could yield a factorization after eliminating internal degrees of freedom. Neither path requires a full interacting supersymmetric gauge theory at the outset.

| Path | Why it is being considered | What would make it substantive |
| --- | --- | --- |
| Direct arithmetic factorization | Uses the central form already available | Derive the full form from an independently defined operator |
| Supersymmetric bulk response | Restores the original physical explanation | Derive the exact zeta response from independently positive dynamics |
| BRST or gauge construction | Relevant if the model has gauge redundancy | Establish a positive physical quotient and the arithmetic identification |

The third row is a conditional extension rather than a coequal starting project. More finite depth numerics remain useful when they answer a structural question. They are not the proposed next objective by themselves.

## 6 The existing mathematical objects

### The shifted boundary family

Write the completed xi function and the shifted transfer as

$$
\xi(s)=\frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Theta_\omega(z)=\frac{\xi(\frac12-\omega-iz)}{\xi(\frac12+\omega-iz)}.
$$

The shift ω is positive. On the real frequency line, the functional equation gives unit modulus wherever the quotient is defined, and hence almost everywhere. This boundary unitarity is unconditional. The stronger condition is innerness: analyticity and boundedness in the upper half-plane together with unit modulus boundary values.

Suzuki's precise equivalence concerns a family: a zero free half-plane to the right of 1/2 + ω₀ corresponds to innerness for every shift ω > ω₀. RH corresponds to innerness for every positive shift. One should not silently replace this family statement by an unrestricted single-shift equivalence, because numerator and denominator cancellations must be accounted for. [E4, P3]

### Depth and the energy identity

On an interval of logarithmic length L, let V be the causal transfer and D its contraction defect. With the subscripts restored,

$$
D_{\omega,L}=I-V_{\omega,L}^{*}V_{\omega,L}
=2\int_0^\omega V_{s,L}^{*}Q_{s,L}V_{s,L}\,ds.
$$

The identity holds with the domain and limiting interpretation specified in the first-slab analysis. D is nonnegative exactly when V is a contraction. The form Q is the symmetric part of the logarithmic shift generator. At zero shift, Q becomes the finite-horizon Weil form. Nonnegativity of that central form on every compactly supported admissible test function is the global Weil positivity condition relevant to RH. [P3, P4]

When Q is already known to be nonnegative along the required shift interval, the formula defines a Gram factor:

$$
(G_{\omega,L}f)(s)=\sqrt{2}\,Q_{s,L}^{1/2}V_{s,L}f,
\qquad D_{\omega,L}=G_{\omega,L}^{*}G_{\omega,L}.
$$

This is a valid consequence of the finite positivity proof. It does not independently establish its premise. The supersymmetric search asks whether an operator defined before that sign is known can play the explanatory role currently played by the square root.

### The string and spectral response

The companion shifted Weyl function is

$$
q_\omega(z)=\frac{1}{\sqrt{-z}}\frac{\xi'}{\xi}
\left(\frac12+\omega+\sqrt{-z}\right),\qquad \Re\sqrt{-z}>0.
$$

Under the appropriate zero free condition it has a positive Stieltjes representation,

$$
q_\omega(z)=\int_0^\infty\frac{d\sigma_\omega(\lambda)}{\lambda-z},
\qquad d\sigma_\omega\geq0.
$$

A Stieltjes measure provides the string realization and a positive mixture of massive free-field covariances. With the usual distributional and integrability conditions, the latter gives reflection positivity in the generalized free-field setting. This construction is downstream of the positive measure. A new bulk argument must derive that measure or the equivalent analytic class from independently specified dynamics. Positivity of a plotted boundary density alone is insufficient if the candidate function has additional forbidden poles. [P3, P9]

### The two directions that must not be conflated

Increasing L includes additional logarithmic delays. In the transfer, integer layers enter at log n; in the logarithmic generator, the von Mangoldt weights select prime powers. Reducing ω moves the shifted family toward the critical line. These are different operations. The coordinate of an inverse Krein string is another construction again, and should not be identified with either parameter without a theorem.

Under RH, the shifted density is a Poisson smoothing of the zero ordinates, counted with multiplicity:

$$
\rho_\omega(u)=\sum_\gamma P_\omega(u-\gamma),\qquad
P_\omega(u)=\frac{\omega}{\pi(\omega^2+u^2)}.
$$

Consequently, increasing the shift corresponds to further smoothing, with ρ at ω + ε equal to the convolution of P at ε with ρ at ω. The analogous relation holds within a suitable common zero free region. This gives a precise RG-like intuition, but positivity preserving smoothing does not provide positivity preserving unsmoothing toward ω = 0. No Wilsonian coarse-graining procedure with the required reconstruction has yet been established here. [P9]

## 7 What a supersymmetric mechanism would require

### A genuine square root and a formal repackaging

Let A be a densely defined closed operator from a positive Hilbert space H₀ to a positive Hilbert space H₁. On the direct sum, the standard block construction is

$$
\mathcal S=\begin{pmatrix}0&A^*\\A&0\end{pmatrix},\qquad
\mathcal S^2=\begin{pmatrix}A^*A&0\\0&AA^*\end{pmatrix}\geq0.
$$

With domain Dom A ⊕ Dom A*, the block operator is self-adjoint. The block grading distinguishes its two sectors. Equivalently, a nilpotent operator that maps the first sector to the second has anticommutator with its adjoint equal to this Hamiltonian. These are elementary operator identities; the meaningful input is the independent definition of A and of the positive spaces.

If A is chosen to be the square root of the desired Weil operator, the construction assumes the sign that it was meant to prove. The same problem appears if an unknown inner product is defined using the Weil form: proving that the inner product is positive becomes the unresolved step. A finite Cholesky factor can be useful for discovery, but becomes explanatory only if it reveals an independently specified structure with proved scope beyond that matrix.

### Why signed contributions can still fit

For a simple example, take a real smooth function W and A = d/dx + W on compactly supported functions. Integration by parts gives

$$
A^*A=-\frac{d^2}{dx^2}+W^2-W',\qquad
\langle f,A^*Af\rangle=\int|f'+Wf|^2\,dx\geq0.
$$

For W(x) = x, the potential x² − 1 is negative near the origin, yet the full operator is nonnegative. The negative term is constrained by its relation to the other terms. On a finite interval, boundary conditions and boundary terms must be included before making the operator statement.

This example explains why signed arithmetic contributions do not settle the question against supersymmetry. It also explains why a factorization would have to reproduce the relations between gamma, arithmetic, and endpoint terms. Declaring the troublesome terms fermionic, or finding a cancellation in a supertrace, would not establish positivity of the required ordinary quadratic form.

### Positivity has several meanings

| Statement | What it controls | What must still be checked |
| --- | --- | --- |
| H is nonnegative on a positive Hilbert space | Energy expectations | Identification with the arithmetic target |
| D is nonnegative | Contraction of the specified transfer | Global depth and shift requirements |
| A covariance is reflection positive | Norms reconstructed through reflection | Correct covariance, reflection, and analytic assumptions |
| BRST cohomology is defined | Gauge equivalence classes | Positivity of the physical quotient |

These implications require maps and hypotheses; the words “positive” and “supersymmetric” do not supply them automatically. Likewise, nonnegativity does not imply a positive spectral gap, so very small positive eigenvalues are compatible with a factorization. A Witten index concerns a graded count of protected zero-energy states, not the location of the nontrivial zeta zeros by itself.

## 8 The two precise research targets

### Path A Factor the central Weil form

The strongest simple target is a single arithmetic construction whose restriction to supported tests satisfies

$$
Q_{0,L}[f]=\|A\widetilde f\|_{\mathcal K}^{2},
$$

where the tilde denotes the chosen extension or embedding of f and K is a positive Hilbert space specified independently of the Weil form. The norm must include the full output of A, including any output outside the input interval. Alternatively, a compatible family of operators could be used, provided its compatibility and domains are proved. A sum of such squared norms is equally acceptable, since the output spaces can be combined.

The factor could be differential, integral, or a combination involving delays. A local first-order Schrödinger ansatz is a useful lesson from supersymmetric quantum mechanics, not an assumption about this nonlocal arithmetic form. The logarithmic high-frequency behavior of the gamma contribution should be checked early against any proposed operator's behavior.

At all depths, an exact identity of this kind would establish the relevant Weil nonnegativity. If a remainder is present, its sign must have an independent proof; moving the entire original difficulty into the remainder does not constitute a mechanism. A finite norm identity would be useful if it exposed how the coefficients are forced or how the construction could extend.

### Path B Construct the bulk and derive the boundary response

Begin with a bulk supercharge and positive Hilbert space defined from arithmetic input. Form its nonnegative Hamiltonian, specify a boundary coupling, and derive the observable seen at the boundary. A basic spectral model illustrates the logic: for H ≥ 0 and a Hilbert-space vector b,

$$
m(z)=\langle b,(H-z)^{-1}b\rangle
=\int_0^\infty\frac{d\mu_b(\lambda)}{\lambda-z},\qquad d\mu_b\geq0.
$$

The measure is positive because it comes from the spectral projections of H. To use this mechanism for zeta, one must prove that the resulting response is q at the desired shift, with its normalization and analytic domain. Actual boundary traces may be unbounded and the zeta measure need not have finite total mass. The displayed vector formula is a pedagogical model; a rigorous boundary realization may require form methods or a boundary triple and explicit control of any subtraction terms.

The transfer version would instead derive the specified Θ or V and prove the required passivity. A positive Hamiltonian alone does not make an arbitrary chosen input-output function passive. The coupling, boundary conditions, and energy balance have to establish that implication.

This path permits a positive total bulk energy even when the observed subsystem does not have a nonnegative instantaneous shift generator. Eliminating internal variables can change the form of the reduced evolution. The physical model must explain that reduction rather than demand a sign already contradicted by the known generator examples.

## 9 Constraints inherited from the existing program

### Instantaneous generator positivity is too strong globally

The storage-depth manuscript records an explicit negative direction of a shifted generator while the cumulative defect remains positive on the same input. Therefore a proposal that identifies every existing Q at positive shift with A* A in the existing inner product cannot be correct. This observation concerns the instantaneous generator; it is not a negative direction of the central Weil form and is not a demonstration of noncontractivity. [P5]

The targets left open include the central form, cumulative storage, and an enlarged bulk realization. A change of metric is permissible as a mathematical proposal, but the new metric and the connection to the original boundary criterion must be proved independently.

### Formal arithmetic structure is not enough

The earlier arithmetic-depth notes report coefficient deformations that preserve the finite delay algebra and Euler-type factorization while producing negative central witnesses. Their verification status belongs to those records. They provide useful controls for a new proposal: a theorem depending only on features shared by those deformations cannot distinguish the desired arithmetic sign. [P10]

This is compatible with a supersymmetric explanation. The square-root relation might hold only for the actual coefficients, just as a perturbation of one term in a factorized Schrödinger operator can destroy the relation. The investigator must identify where that rigidity enters.

### Boundary terms and global limits carry mathematical content

Completing a square on compactly supported functions does not settle a boundary value problem unless the domain and endpoint contributions are accounted for. Similarly, integrating out a block of variables preserves positivity through a Schur complement only after the necessary positivity and invertibility hypotheses have been established. A Schur identity can expose the needed estimate without proving it.

A result for finitely many depths is not an all-depth theorem. A sequence of certified depths can also accumulate at a finite limit. For Path A, the natural endpoint is an identity on all admissible compactly supported tests. For Path B, the statement must specify the shifts, analytic domains, depth limits, and compatibility that actually recover an RH-equivalent criterion. Arbitrary limiting or compression operations must not discard the offending directions.

## 10 The proposed first investigations

### Establish the mechanism in a model whose answer is known

First reproduce a standard supersymmetric factorization with its domains and boundary conditions. Derive the bulk response as well as the positive Hamiltonian if Path B is being pursued. The point is to distinguish which part of the argument gives energy positivity and which part identifies a boundary observable. This model should expose any hidden assumption before arithmetic is introduced.

### Recover the gamma slab structurally

Use the exact first-slab data to ask whether its positivity has an operator or energy explanation more informative than its existing certificate. Retain the completed gamma contribution and the endpoint terms used by the target normalization. The gamma-only continuation is not known to stay positive at arbitrary depth; the first-slab paper already reports negative directions beyond its initial range. A proposal should not assume a globally passive gamma backbone. [P3]

An explicit gamma operator would be a useful result even if the first prime later defeats it. Conversely, failure of a particular local ansatz would identify a limitation of that ansatz, not refute all nonlocal or enlarged bulk constructions.

### Introduce the first arithmetic delay

The first arithmetic layer is the smallest place where the intended mechanism must do more than explain gamma positivity. Write the complete target form, propose an operator with specified coefficients, and expand its square symbolically before fitting numerical parameters.

One elementary identity shows both the attraction and the difficulty. For a delay T and real scalars a and b,

$$
(aI-bT)^*(aI-bT)=a^2I+b^2T^*T-ab(T+T^*).
$$

The negative off-diagonal coupling has the desired general shape. But the positive diagonal and endpoint projection terms have also been forced. On a finite interval, T is a truncated shift, so T* T is not generally the identity. Matching only the negative coupling would miss the main mathematical condition. This identity is an illustration of what to examine, not a proposed factorization of the actual zeta form.

With multiple delays, products generate additional mixed terms. Their coefficients and possible cancellations must follow from the proposed arithmetic structure. The initial deliverable should be either a complete identity in the chosen model or an explicit incompatible coefficient or boundary condition.

### Use controls that can falsify the proposed explanation

Compare the candidate with selected arithmetic deformations and with a tractable zeta analogue. The Ihara graph laboratory is useful because the relevant Ramanujan condition is true for some graphs and false for others. A function-field example can also test whether the proposed coordinates expose the structure that proves its known positivity. These are proposed comparison studies, not results asserted by this brief. [P7]

A candidate that predicts the desired positivity for a control known to violate the corresponding criterion has a missing hypothesis or a false identity. A candidate that passes only a finite matrix comparison has earned further analysis, not an all-depth conclusion.

### Assign numerics a deciding question

Use modest computations to locate a failed coefficient match, a boundary defect, an unstable domain approximation, or a falsifying witness. Escalate to expensive certification when the computation would settle a precise unresolved finite assertion relevant to the mechanism. Before each campaign, state what outcome would change the next mathematical step.

## 11 How to interpret progress and dead ends

| Outcome | What has been learned | Appropriate next step |
| --- | --- | --- |
| Exact identity in the gamma slab | A structural explanation in a known positive region | Determine which feature survives the first delay |
| Exact identity with the first delay | A nontrivial arithmetic compatibility relation | Test repeated and mixed delays and prove scope |
| Positive bulk with a different response | A physical system has been built, but the identification fails | Isolate the mismatched observable or coefficient |
| A finite fitted factor only | A numerical representation of finite positivity | Seek an independent coefficient rule before extending |
| A contradiction within a specified ansatz | That operator class or set of hypotheses fails | Record the obstruction and the smallest change that avoids it |
| Success obtained by assuming the target sign | The difficult step has been relocated | Rewrite the dependency chain and remove that assumption |

Tiny eigenvalues alone are not a reason to reject a factorization. They can reflect approximate null directions in a positive operator. They do become a reason to reject a proposed uniform coercivity estimate if that estimate contradicts validated upper bounds. Nonnegativity, strict positivity for individual tests, and a uniform positive lower bound should always be distinguished.

Likewise, a negative result must be stated at its actual scope. “This scalar local ansatz cannot match the first delay” is a useful conclusion. “Supersymmetry cannot help with RH” would require a much broader argument. A failed path can still explain which arithmetic information or boundary structure the next model must retain.

## 12 A reusable record for future explorations

For each new approach, preserve a short record before substantial computation. The following prompts are intended to be reused even if the supersymmetric routes are abandoned.

1. State the original mathematical target and all of its quantifiers. Identify the test space, shift range, depth range, and normalization.
2. Specify the proposed system independently. List its coefficients, Hilbert space or metric, operator domain, boundary conditions, and any auxiliary variables.
3. Name the assertion that forces positivity and give its proof or exact missing lemma. Separate a known theorem from an analogy or a conjecture.
4. Derive the map to the arithmetic object. Record whether it gives an identity, a one-sided bound, a compression, a limit, or only a spectral resemblance.
5. Identify where the actual arithmetic enters. Give a nearby control that preserves the generic formalism but should not inherit the conclusion.
6. Choose the cheapest deciding calculation or proof. State what success, failure, and inconclusive evidence would each mean.
7. Record the outcome at its precise scope. Preserve the counterexample, coefficient mismatch, or successful identity together with its assumptions.
8. Explain what transfers to the next idea. Identify the indispensable structure, the dispensable ansatz choice, and the evidence that would justify reopening the route.

The immediate objective is to discover whether the arithmetic admits an independently specified square-root or positive bulk construction. If that search fails, the durable result should be a clearer account of why it fails and which part of the original physical motivation remains untested. The guiding question remains the same: what structure forces positivity before the zeta boundary condition is imposed?

## 13 Notation and terminology for later use

| Symbol or term | Meaning in this brief |
| --- | --- |
| ξ | Completed Riemann xi function; its nontrivial zeros are those of ζ |
| ω | Positive shift away from the critical line |
| L | Logarithmic depth cutoff of the supported input space |
| Θ | Shifted transfer function whose full analytic class matters |
| V | Causal transfer on the specified finite interval |
| Q | Symmetric logarithmic shift generator; its central member is the Weil form |
| D | Contraction defect I − V* V, or cumulative storage |
| q | Shifted Weyl function used in the string formulation |
| A and S | Proposed arithmetic factor and associated supercharge; not the existing shift generator |
| Positive inner product | A genuine Hilbert norm, distinguished from a ghost or indefinite metric |
| Independent construction | A definition and proof that do not assume the target arithmetic positivity |
| Mechanism | A proved structure that forces the relevant sign, with the arithmetic identification supplied |

The distinction between Q and a supercharge is especially important. Q already names the Weil-related energy form in the project. This brief uses A and S for the proposed factor and supercharge to avoid confusing the desired Hamiltonian with the operator that would explain it.

## 14 Sources and the research record

The mathematical definitions and reported finite results should be traced to their manuscripts and verification records. Research notes contain proposals, diagnostic calculations, and assessments with narrower status. The historical account also incorporates the researcher's explanation of the original motivation in the September 11 discussion.

The code and paper repository is `/Users/ebbaker/Documents/shifted-zeta-positivity`. The external data archive is now `/Users/Shared/szp-archive`; older references to a differently named data archive should be resolved against that location. This brief does not require the large Fourier outputs to be copied into the archive. Their reported conclusions inform the motivation; the proposed factorization arguments must stand on their own mathematical identities.

### Project sources

[P1] [Root README and program background](/Users/ebbaker/Documents/shifted-zeta-positivity/README.md). Origins of the program and the transition from higher dimensional constructions to shifted screw functions.

[P2] [Project overview of the shifted zeta holographic program](</Users/ebbaker/.codex/.chatgpt-projects/g-p-6a90684bbcb881918a5a1f5740bfbc65/sources/PROJECT_OVERVIEW_shifted_zeta_holographic_program(1).md>). August 31, 2026. Original dependency diagram and the distinction between inverse reconstruction and an independently positive bulk.

[P3] [First-slab positivity manuscript](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/first-slab-positivity/first_slab_positivity.tex). Definitions, shift energy identity, finite Gram construction, modular endpoint, and the proposed passive network and PDE directions.

[P4] [Finite-horizon Weil manuscript](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex). Finite central forms, certified bounds, and global scope of the Weil criterion.

[P5] [Storage-depth manuscript](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/storage-depth/manuscript/storage_depth.tex). Spatial continuation, limits of the certificate method, and the appendix distinguishing negative instantaneous generators from cumulative storage.

[P6] [Barrier theorem and ladder conjecture note](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/storage-depth/archive/reviews/NOTE_barrier_theorem_and_ladder_conjecture_20260911.md). September 11, 2026. Keep its proposed spectral decay laws distinct from its theorem arguments and numerical evidence.

[P7] [Lessons learned and manifest positivity design guidance](</Users/ebbaker/Documents/shifted-zeta-positivity/Claude outputs/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md>). September 11, 2026. Strategic assessment and proposed comparison laboratories; its broad conclusions are assessments rather than general no-go theorems.

[P8] [Historical note index](/Users/ebbaker/Documents/shifted-zeta-positivity/notes/README.md). A guide to prior investigations, including earlier gauge and supersymmetry proposals. Consult the underlying notes before claiming that a new proposal has already been ruled out.

[P9] [Shifted zeta string manuscript](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/omega-string/omega_string.tex). Weyl function, Stieltjes representation, conditional Poisson smoothing, and spectral limits.

[P10] [Arithmetic-depth results and obstructions](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/shifted-zeta/weil-depth/archive/background/ARITHMETIC_DEPTH_RESULTS_20260906.md). September 6, 2026. Earlier generator and coefficient-deformation witnesses, with their original verification qualifications.

### External mathematical sources

[E1] Edward Witten, [Supersymmetry and Morse Theory](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf), Journal of Differential Geometry 17 (1982), 661–692. The differential, its adjoint, and a positive Hamiltonian with independent geometric meaning.

[E2] Hyun Seok Yang and Bum-Hoon Lee, [BRST Cohomology and Its Application to QED](https://arxiv.org/abs/hep-th/9502082). A concrete discussion of the positive auxiliary inner product, Hodge decomposition, and additional conditions for positivity of physical states.

[E3] Arthur Jaffe and Edward Witten, [Quantum Yang–Mills Theory](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf). The constructive existence and mass gap problem; a reminder of the distinction between a quantization formalism and a completed rigorous construction.

[E4] Masatoshi Suzuki, [arXiv 1204.1827](https://arxiv.org/abs/1204.1827), especially Proposition 1.2 and the Hankel/canonical-system framework, and [arXiv 2206.03682](https://arxiv.org/abs/2206.03682) for the screw-function setting. Use the precise family statements when translating between innerness and zero free regions.

[E5] Jean-François Burnol, [Spacetime causality in the study of the Hankel transform](https://arxiv.org/abs/math/0509619), Annales Henri Poincaré 7 (2006), 1013–1034. A precedent for deriving a classical Hankel transform from causal Klein–Gordon propagation. It supplies motivation for a bulk realization, not the missing arithmetic construction.
