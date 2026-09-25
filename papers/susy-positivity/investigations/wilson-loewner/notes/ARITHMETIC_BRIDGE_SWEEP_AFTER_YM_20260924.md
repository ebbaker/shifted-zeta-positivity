# Arithmetic bridges after the Yang–Mills lattice investigation

Date: 24 September 2026 (America/New_York; literature checked through this date).
Prepared for Edward Baker.
Model: GPT-6 (Codex). The runtime does not expose the configured reasoning-effort label; no label is inferred.
Repository baseline: 520a859b7f73fea9e314debdecabd45439b3fcb1.
Status: research-direction assessment and brainstorm, not a proof, implementation plan already approved for execution, or priority claim.

This note was drafted with LLM assistance from local research notes and primary literature. Established results, elementary deductions, and proposed investigations are distinguished below. Recent preprints are used with their stated hypotheses; their availability is not an independent verification of every proof.

## 1. Recommendation and scope

For an RH-directed continuation, start with arithmetic operators and a precise sufficient positivity statement. Use the YM work for its methods: honest adjoints, complete state spaces, Gram matrices, dynamical identities, and controlled projection errors. The current SU(2) slab supplies those methods but does not supply prime lengths, their exact weights, or the archimedean comparison.

The best near-term continuation remains an actual semilocal Sonin comparison, sharpened in two ways:

1. Work first on a fixed, RH-sufficient class of tests that annihilates the two pole amplitudes. An unrestricted same-window physical realization is a stronger objective.
2. Seek a signed estimate for the explicit comparison remainder. Constructing another positive ambient metric, or certifying another isolated finite window, does not establish continuation.

The most interesting extension of the YM methodology is an **arithmetic positivity bootstrap**: positivity together with exact arithmetic/Fourier identities. The most distinct alternative physical mechanism found in the sweep is **Lee–Yang zero localization**, which would reach RH through real-zero entire approximants and only then imply Weil positivity. Both need an independently derived arithmetic construction before extensive numerics.

Several leading routes are already present in the repository. This sweep supports and narrows them; it does not claim to have discovered Sonin spaces, canonical systems, spectral triples, odd-test criteria, arithmetic Hodge structures, or the pole-vanishing criterion.

Local background reviewed includes the four recent YM notes, the updated reflection/hierarchy assessment, the arithmetic-storage continuation and prime-rigidity notes, the brainstorm assessment and failure inventory, the arithmetic landscape, the inverse-bulk notes, and the 14 September semilocal comparison stored in the local project output directory. The latter comparison is internally checked work and still needs an independent normalization/domain audit.

## 2. State exactly what must be bridged

Let \(I_L=(-L/2,L/2)\), let \(F\) be the zero extension of \(f\in C_c^\infty(I_L)\), and put \(U_dF(x)=F(x-d)\). In the repository normalization,

\[
Q_L[f]=K_\Gamma[F]+w_0\|F\|_2^2+P_L[f]
-2\sum_{m\log p<L}c_{p,m}\operatorname{Re}\langle F,U_{m\log p}F\rangle,
\]

where

\[
c_{p,m}=(\log p)p^{-m/2},\qquad
w_0=\psi(1/4)-\log\pi,
\]

\[
K_\Gamma[F]=\frac12\iint |F(x)-F(y)|^2
\frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}\,dx\,dy,
\]

\[
P_L[f]=2\left|\int f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int f(x)\sinh(x/2)\,dx\right|^2.
\]

The archimedean Fourier multiplier, including its contact, is
\(\operatorname{Re}\psi(1/4+i\tau/2)-\log\pi\). Positivity for all compactly supported smooth inputs is equivalent to RH.

Three different achievements would suffice or contribute:

- **Exact norm identity:** \(Q_L[f]=\|A_Lf\|^2\), with \(A_L\) constructed without assuming the positivity to be proved.
- **Comparison:** \(Q_L[f]=B_L[f]+R_L[f]\), where \(B_L\ge0\) is independently constructed and \(R_L\ge-B_L\) is proved.
- **Alternative RH criterion:** prove a sufficient real-zero, approximation, or restricted-test statement; RH then gives the complete Weil positivity statement.

Only the first two directly identify the arithmetic quadratic form with a positive object. The third can still be the better research route. None requires that the original scalar causal zeta transfer function be literally a Wilson expectation. Likewise, a square root obtained by first assuming \(Q_L\ge0\) is not a construction.

Unconditionally, zeros in the explicit formula need not have real ordinates in the centered variable. A sum of absolute squares at real ordinates cannot be used as an unconditional definition of the target. The sesquilinear continuation must retain the possible complex locations.

## 3. Remove pole sectors without losing the RH implication

**Literature.** Connes–Consani's Appendix C allows finitely many prescribed Mellin zeros away from the zeta zeros, including 0 and 1, in an RH-equivalent criterion. [Source](https://arxiv.org/html/2006.13771v1).

**Project coordinates.** Use
\[
\mathcal D_L^0=\left\{f\in C_c^\infty(I_L):
\int e^{x/2}f(x)dx=\int e^{-x/2}f(x)dx=0\right\}.
\]
Both pole amplitudes vanish. Positivity on this class for every \(L\) still implies RH. The correspondence is \(g(u)=u^{-1/2}f(\log u)\).

The same-support parametrization is
\[
f=(-\partial_x^2+1/4)h,\qquad h\in C_c^\infty(I_L).
\]
Integration by parts gives the constraints; conversely the Green kernel \(e^{-|x|/2}\) has zero tails when both moments vanish.

One can also impose \(\int f=0\), since \(\zeta(1/2)\ne0\), without extending the published short-support comparison to larger supports.

**Strategic consequence.** An RH-first bridge can avoid constructing signed pole sectors. An unrestricted physical norm identity still needs them. The odd-test criterion is a separate narrowing; arbitrary intersections of sufficient classes require justification.

## 4. Route A: canonical Sonin pairing on the restricted source class

**Existing input.** Semilocal Fourier theory supplies arithmetic maps and compatible Sonin spaces. Its Hilbertian isomorphisms have place-dependent metrics; they are not automatically isometric or monotone. [Connes–Consani–Moscovici, semilocal adelic operators, Theorem 4.13 and §4.8](https://arxiv.org/html/2310.18423v1). Quasi-inner local factors control an off-diagonal block, not its sign or its disappearance. [Connes–Consani, quasi-inner functions](https://arxiv.org/abs/2008.10974).

The local 14 September comparison uses the actual archimedean Sonin projection \(\Pi\), and

\[
D_S=\prod_{p\in S_f}(I-p^{-1/2}U_{\log p}),\quad
A_S=\left.\Pi D_S^*D_S\Pi\right|_{\operatorname{Ran}\Pi},
\]

\[
\Pi_S=D_S\Pi A_S^{-1}\Pi D_S^*,\qquad
B_{S,L}[f]=\|C_F\Pi_S\|_{\mathrm{HS}}^2,
\]

where \(C_F\) is convolution by \(F\). The inverse compressed metric is essential. It retains the actual adjoint under transport.

**Proposal.** Audit the existing identity \(Q_L=B_{S,L}+R_{S,L}\), then restrict it to \(\mathcal D_L^0\), or the further zero-mean class. Seek an estimate on the complete signed remainder. An adequate target is

\[
R_{S,L}[f]\ge-\eta_L B_{S,L}[f],\qquad \eta_L\le1,
\]

with null directions handled explicitly. A fixed positive margin independent of \(L\) is unnecessary and may be unavailable. A remainder that is itself nonnegative would be stronger than required.

**First test.** Compute the actual projection and error on a stated small source family generated by \((-\partial_x^2+1/4)h\). Use exact prime weights and controlled tails. First prime 2, then primes 2 and 3, then the return at \(2\log2\). Compare the signed residual with the positive pairing on the same inputs.

**Promote if:** the canonical Fourier/Poisson geometry gives a signed relation or a relative estimate absent from generic Gram positivity.

**Stop this particular comparison if:** a controlled negative direction disproves the proposed domination. That would exclude the comparison, not RH. Replacing \(\Pi\) by a fitted finite positive matrix would not test the proposal.

**Assessment:** closest to the existing mathematics, most informative bounded next task, but still a serious inequality problem. Its value is the explicit arithmetic structure, not an expectation of an easy proof.

## 5. Route B: import the bootstrap method into an arithmetic operator algebra

**Physical precedent.** Lattice bootstraps combine positive Gram matrices with loop equations and algebraic identities. Finite-\(N\) SU(2) relations simplify trace types without closing the infinite family of loop shapes. Recent work also obtains indirect equations by eliminating longer loops. [Kazakov–Zheng](https://arxiv.org/abs/2404.16925), [Liu–Yang](https://arxiv.org/abs/2601.04316).

**Proposal, not an existing RH theorem.** Build the analogous hierarchy from arithmetic operators whose relations are independently known. A transparent starting representation on \(\ell^2(\mathbb N)\) is

\[
V_n|m\rangle=|nm\rangle,\qquad H|m\rangle=(\log m)|m\rangle,
\]

\[
V_mV_n=V_{mn},\quad V_n^*V_n=I,\quad
V_m^*V_n=V_{n/d}V_{m/d}^*,\quad d=(m,n),
\]

\[
[H,V_n]=(\log n)V_n
\]

on the finite-sequence core. This gives the logarithms from arithmetic dynamics rather than assigning unrelated geometric lengths.

These relations alone are insufficient: they contain neither the real-place Fourier constraint nor the desired critical state. A serious proposal must adjoin a precisely defined Fourier/Poisson or co-Poisson structure and specify its domain and state. Do not infer a Gibbs vector at inverse temperature \(1/2\) by analytically continuing a convergent thermal trace.

For actual observables \(A_i\), their matrix \(\varphi(A_i^*A_j)\) is positive. The objective is to use independently valid relations to derive a dual certificate for the restricted Weil form, schematically

\[
Q_L[Th]=\sum_j\|A_jh\|^2+\text{controlled remainder},
\qquad T=-\partial_x^2+1/4.
\]

The signed coefficients must emerge from the relations. Inserting the entries of \(Q_L\) as already-positive moments would assume the conclusion.

**First test.** Use the two prime generators \(V_2,V_3\), their adjoints, and a small real-place test family. Derive an exact identity that explains a compulsory contact, a repeated-prime coefficient, or cancellation of a forbidden mixed-ratio term. Only then enlarge a semidefinite hierarchy.

**Promote if:** an arithmetic relation produces a nontrivial improvement over all constraints obtainable from positivity alone, preferably as an exact symbolic identity.

**Stop if:** the state is free to fit the target, the Fourier constraint is merely named, or every finite certificate reproduces the same unresolved Schur positivity.

**Assessment:** best conceptual bridge from the YM work, more exploratory than Route A. The first deliverable should be an identity, not a large numerical optimization.

## 6. Route C: an arithmetic jump model and a sharp constrained inequality

**Elementary deduction.** For any unitary translation,

\[
-2c\,\operatorname{Re}\langle F,U_dF\rangle
=c\|F-U_dF\|^2-2c\|F\|^2.
\]

Consequently, on the pole-neutral class,

\[
Q_L[f]=\mathcal E_L[F]-\kappa_L\|F\|^2,
\]

\[
\mathcal E_L[F]=K_\Gamma[F]
+\sum_{m\log p<L}c_{p,m}\|F-U_{m\log p}F\|^2,\qquad
\kappa_L=2\sum_{m\log p<L}c_{p,m}-w_0.
\]

Every term in \(\mathcal E_L\) is a positive jump energy. It combines a continuous symmetric jump kernel with jumps of lengths \(m\log p\), using zero extension outside the interval. A lattice approximation designed around this energy has the correct arithmetic coefficients from the beginning.

The necessary result is the sharp two-constraint inequality

\[
\mathcal E_L[F]\ge\kappa_L\|F\|^2
\quad(f\in\mathcal D_L^0,\ L>0).
\]

**What this does and does not buy.** It converts the indefinite target into a Poincaré-type question for an independently positive energy. It does not prove the required gap. It exposes exactly the contact deficit that defeated earlier independent delay-square constructions. The two exponential moment constraints are not an ordinary stationary zero-mean condition, and their subspace is not automatically invariant under the jump semigroup.

**Possible new ingredient:** a sharp uncertainty or co-Poisson estimate on the constrained class that couples continuous Fourier localization to arithmetic jumps. A generic lower bound depending only on total jump mass is unlikely to retain the needed arithmetic cancellations.

**First test.** Compare the constrained gap and its minimizing response with the Sonin remainder on the same windows. Derive the Euler–Lagrange equation with both Lagrange multipliers retained. Test any proposed inequality against the repository's smooth-density replacement control.

**Stop if:** all that has been proved is positivity of \(\mathcal E_L\), or the contact \(\kappa_L\) is reduced to a fitted constant.

**Assessment:** a useful exact model-selection reformulation and a possible bridge to probabilistic methods; less evidence of a new inequality than Route A. It should not become another simulation campaign without a proposed sharp estimate.

## 7. Route D: screw functions, covariance, and exclusion of a first zero mode

**Literature.** Suzuki expresses arithmetic in a continuous screw-function kernel. With the paper's \(g\),

\[
G_g(t,u)=g(t-u)-g(t)-g(-u)+g(0),
\]

and positivity of this kernel is equivalent to RH. This integrates the distributional arithmetic data into a continuous object. [Suzuki, 2023](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.12785).

The 2026 operator treatment relates the Weil form to that kernel through differentiation and studies finite-interval ground eigenvalues, including continuity in the interval size. Small-interval positivity is established; global positivity and the proposed limiting spectral realization remain additional problems. [Suzuki, 2026](https://arxiv.org/html/2606.09096v2).

**Two proposals.** First, construct \(G_g\) as a covariance of an independently defined arithmetic process. Second, use continuity from short intervals and exclude a first zero eigenvalue by a specific nonlocal uniqueness or boundary identity.

The latter asks for an obstruction to a nonzero null solution at a first crossing. It may be more focused than proving a quantitative uniform gap. Ordinary local unique continuation cannot simply be imported into a nonlocal equation containing translated values.

**First test.** Translate the existing first-prime Schur equation into the screw-function variables and derive the exact null equation. Look for a conserved boundary quantity or an arithmetic identity that a null vector would violate.

**Stop if:** “it is a covariance” is merely a renamed positive-definiteness assumption, or the no-crossing assertion is just the original positivity statement without a new estimate.

**Assessment:** attractive analytic coordinates and a potentially sharper lemma; not a new source of positivity by itself.

## 8. Route E: spectral triples and entire-function convergence

**Literature.** Theorem 5.10 of the 2025 zeta-spectral-triples preprint assumes a simple lowest finite Weil-matrix eigenvalue and an even normalized eigenvector. It constructs a self-adjoint quotient operator using the metric obtained after subtracting that lowest eigenvalue. Its regularized determinant is, up to a nonvanishing phase, the Fourier transform of the eigenvector and has real zeros. [Connes–Consani–Moscovici](https://arxiv.org/html/2511.22755v1).

The subtraction is crucial: self-adjointness does not establish that the original lowest eigenvalue was nonnegative. Related real-zero results for ground-state transforms are studied by [Connes–van Suijlekom](https://arxiv.org/abs/2511.23257).

**Proposal.** Identify a normalization and a joint cutoff regime in which the real-zero entire approximants converge locally uniformly on the complex plane to \(\Xi(z)=\xi(1/2+iz)\), or to a known nonvanishing entire multiple of it. Hurwitz's theorem would then exclude nonreal zeros of the limit.

Agreement with many real zeros, weak convergence of spectral measures, or strong resolvent convergence alone does not establish this entire-function conclusion. The normalization cannot discard unwanted zeros.

**First test.** Audit the precise conjectured limit and isolate a compact-set error bound in terms of independently estimable arithmetic quantities. Use existing certified matrix information to assess those bounds, rather than extending a plot of real eigenvalues.

**Stop if:** the convergence proof assumes the positivity of the unshifted Weil form, ignores off-line zeros, or replaces a complex-plane bound with agreement on selected real points.

**Assessment:** a serious arithmetic spectral alternative, already known to the project. It is appropriate only if the user wants to reconsider a spectral-convergence program; it is not the default recommendation here.

## 9. Route F: Lee–Yang systems and real-zero approximants

**Literature.** The theta-kernel Fourier representation of \(\Xi\) connects RH to statistical-mechanical zero-location problems. Newman–Wu review the de Bruijn–Newman deformation and its relation to Lee–Yang measures. [Newman–Wu](https://arxiv.org/abs/1901.06596). Rodgers–Tao prove the de Bruijn–Newman constant is nonnegative; RH would place the threshold exactly at zero. [Rodgers–Tao](https://arxiv.org/abs/1801.05914).

**Proposal.** Seek a sequence of finite ferromagnetic systems, or another rigorously Lee–Yang class, whose normalized magnetization transforms converge to the completed theta transform. Positivity of the Gibbs measure is insufficient: the interaction and single-site measures must satisfy an actual zero-location theorem.

For a source-independent partition function \(Z_N(h)\), a relevant construction would make
\[
Z_N(iz)/Z_N(0)\longrightarrow \Xi(z)/\Xi(0)
\]
locally uniformly, after any explicitly justified fixed coordinate scaling. A weak limit of probability measures needs adequate exponential-moment control to imply this entire-function convergence.

**First test.** Examine whether the theta density admits a representation or approximation using operations that preserve a verified Lee–Yang class. Check structural closure conditions and tail estimates before fitting moments or zeros. A finite moment fit can falsify a proposed ansatz; it cannot verify all-degree real-rootedness.

The Jensen-polynomial approach is a related algebraic test. Existing results establish eventual hyperbolicity for each fixed degree, which is not all-degree, all-index control. [Griffin–Ono–Rolen–Zagier](https://arxiv.org/abs/1902.07321).

**Stop if:** the argument uses only a positive theta density, requires antiferromagnetic couplings outside its zero theorem, or controls only finitely many derivatives.

**Assessment:** the clearest different physical mechanism in this sweep. It would reach Weil positivity through RH, not by a direct norm identity. Higher construction risk, but worth a bounded feasibility study if a fresh physical route is desired.

## 10. Other routes screened

| Route | What is already available | Missing ingredient and useful first test | Assessment |
|---|---|---|---|
| Arithmetic reflection on an adelic space | Positive Haar/Fourier Hilbert structures and arithmetic scaling | Define the reflection, half-space algebra, and source map; compute one full two-point pairing, including contacts | Potential geometric realization of A/B, not a positivity argument by naming a reflection |
| Local conductor operators | A place-by-place operator description of explicit-formula terms | An independently derived global Fourier/Poisson constraint controlling their signed sum | Useful exact dictionary; sign problem remains |
| Canonical systems | A zeta-related construction in an unconditional parameter range | Derive positive Hamiltonians toward all small positive shifts without assuming innerness | Focused reserve branch, close to existing shifted-zeta program |
| Li coefficients and moment matrices | RH-equivalent positivity sequences and conditional norm formulas | Prove an independent recurrence, integral representation, or norm identity for the whole sequence | Smaller interface, not automatically easier |
| Nyman–Beurling/co-Poisson approximation | A criterion in a positive ordinary Hilbert space | Construct arithmetic approximants with a vanishing residual and proved rate/control | Distinct RH route; useful comparison for errors |
| Polarized arithmetic cohomology | Finite-field examples with a positive arithmetic adjoint; number-field trace frameworks | Construct the number-field pairing and prove adjoint compatibility, rather than assume it | Best conceptual explanation, largest construction burden |
| Arithmetic dynamics and periodic orbits | Candidate spaces with arithmetic periods | Exact repetition weights, completed trace identity, and positive physical/cohomological metric | Long-range structural work |
| Determinants and connected loops | Log determinants naturally organize primitive repetitions | Preserve an ordinary positive pairing while producing the required signs and all-place completion | Algebraically suggestive; connected quantities need not be positive |
| Bost–Connes/KMS or arithmetic Toda | Exact arithmetic spectra or positive local-factor measures | Relate the required first derivative and residues to an actual positive norm | Existing obstruction still central |
| Larger YM, WZW, or supersymmetric sectors | More observables, richer positive Gram spaces, sometimes exact equations | An arithmetic operator action and full source/readout identity | Do not enlarge solely for RH relevance |

Primary anchors for these shorter assessments:

- Burnol's conductor operator identifies local explicit-formula contributions through logarithms of position and Fourier variables. This is an operator identity, not positivity of the global form. [Burnol, explicit formula](https://arxiv.org/abs/math/9902080).
- Suzuki constructs canonical systems unconditionally for a restricted shift range; extension toward all positive shifts is tied to the unresolved positivity problem. [Suzuki, canonical systems](https://arxiv.org/abs/1204.1827).
- Li coefficients can be represented as norms of certain explicit functions precisely under an RH-equivalent condition. The word “norm” in such a criterion does not remove that condition. [Suzuki, Li coefficients](https://arxiv.org/abs/2301.05779).
- Báez-Duarte's strengthening makes arithmetic dilates central to the Nyman–Beurling approximation criterion. The Hilbert norm is positive independently; approximating the target is the hard step. [Báez-Duarte](https://arxiv.org/abs/math/0202141).
- Co-Poisson constructions connect arithmetic with Fourier-vanishing Sonine spaces, offering a concrete common language for A and approximation approaches. [Burnol, complete and minimal systems](https://jtnb.centre-mersenne.org/item/JTNB_2004__16_1_65_0/).
- Adelic cyclic-homological formulations give an arithmetic trace pairing whose needed positivity remains an RH-equivalent issue. [Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392).
- Dynamical constructions related to arithmetic schemes supply candidate orbit geometry; they are not an already established number-field positive Hodge realization. [Deninger](https://arxiv.org/abs/1807.06400).
- Semilocal local-factor moment measures and Jacobi operators are already developed; a generic positive moment/Toda construction is not a new Weil comparison. [Connes–Consani–Moscovici, local-factor moments](https://arxiv.org/html/2403.01247v1).

An especially useful finite-field control would derive the Frobenius adjoint relation from a polarization, rather than starting with zeros on a circle. It demonstrates what an arithmetic positivity law must actually accomplish. It is not a proposal to solve number-field cohomology by analogy.

## 11. Tests that distinguish a bridge from an analogy

These are research discrimination tests, not new prerequisites for unrelated mathematical-physics work.

1. **Arithmetic is derived.** Explain why the translation lengths are \(m\log p\) and the primitive weight remains \(\log p\) at every repetition.
2. **Repeated primes and mixed primes differ correctly.** The central form has a coefficient at \(\log4\), but none at \(\log6\), since \(\Lambda(6)=0\). A shared amplitude may generate a spurious \(\log(3/2)\) correlation. The construction must explain its cancellation or legitimate location outside the target.
3. **The full diagonal is retained.** Positive delay squares add contacts. A positive thermal or moment normalization can change contacts. These cannot be silently discarded.
4. **The source class is explicit.** Decide between the unrestricted physical form and an RH-sufficient restricted criterion. Preserve all inputs in the chosen class, not just favorable probes.
5. **The adjoint is physical or mathematically specified.** Inverse transport, reflection, and metric adjoint are different operations unless a relation is proved.
6. **The limiting statement has a topology and domain.** Compact support, critical-line boundary values, trace ideals, and complex-plane convergence cannot be interchanged casually.
7. **There is a mechanism for arbitrary support.** A uniform gap is not required, but an unbounded sequence of independently certified short windows is not by itself a continuation theorem.
8. **An arithmetic-blind control fails where it should.** Apply the proposed principle to the existing smooth-density replacement. If it proves positivity there too, identify the missing arithmetic hypothesis.

Useful finite windows for algebraic tests are \(L=1\) (only prime 2), \(L=1.25\) (2 and 3), and \(L=1.5\) (2, 3, and 4). A test beyond \(\log6\) must also include prime 5. At the transfer-function level integer labels can occur even when they are absent from the central logarithmic derivative, so the two coefficient dictionaries must remain separate.

## 12. Two corrections to keep in view

### 12.1 Existing scalar-norm estimates can miss cancellation

In the YM projection experiment, bounding an omitted pairing by the product of two residual norms can remain large when the pairing itself cancels. This is a reason to retain correlations and equations in an arithmetic hierarchy. It is not evidence that those cancellations occur in an arbitrary interacting slab or arithmetic state.

### 12.2 Prime-log support is not dense

Section 6 of the 16 September note
`brainstorm/inverse-bulk-brainstorm/NONCONSTRUCTIVE_EXISTENCE_AND_THETA_SYMBOL_20260916.md`
states that the union of \((\log p)\mathbb Z\) over primes is dense in \(\mathbb R\). That statement is false.

For fixed \(R\), every nonzero point in that union with absolute value at most \(R\) is \(\pm\log(p^m)\) with \(p^m\le e^R\), so there are only finitely many. The union is closed and locally finite, with no point in \((0,\log2)\). A distributional limit of kernels all supported on this same closed set remains supported there. Merely adding more prime lattices in a fixed logarithmic coordinate cannot produce the continuous off-diagonal gamma kernel.

Rescalings or convolutions generating new differences can change the support; for example log-rational differences can be dense. Those are different operations and introduce terms that must be reconciled with the target. The correction strengthens a scoped obstruction to the stated Bloch-lift limit; it does not exclude arithmetic Fourier duality or a coupled construction.

The historical note has not been edited as part of this sweep.

## 13. Recommended decision before further calculations

Choose one main objective:

- **Direct bridge with maximum reuse:** audit and test the canonical Sonin remainder on the pole-neutral class. This is my recommendation.
- **Develop the YM-inspired method:** derive one new arithmetic identity suitable for a positivity bootstrap, using two prime generators and a real-place constraint.
- **Try a different physical principle:** screen the theta kernel for a rigorous Lee–Yang approximation mechanism.

The arithmetic jump-energy reformulation is a useful analytic companion to the first two. The screw-function null equation is another candidate coordinate system. Neither should trigger a separate large computation before a discriminating lemma is identified.

A bounded next assignment for the first choice would be:

> Re-derive the actual semilocal Sonin comparison in the repository's normalization on the range of \(-\partial_x^2+1/4\). Retain the exact remainder, adjoints, contacts, support restrictions, and trace/domain hypotheses. Determine whether canonical Fourier/Poisson structure supplies a signed estimate beyond generic positivity. Use the first-prime and two-prime settings as diagnostic cases. Report a precise candidate lemma or a scoped obstruction; do not substitute an arbitrary positive finite matrix or launch an all-window computation.

For the second:

> Specify an independently defined arithmetic operator algebra and positive state with a real-place Fourier constraint. Derive an exact identity involving \(V_2,V_3\) that contributes to the restricted Weil form and explains either the repeated-prime coefficient or mixed-term cancellation. Identify exactly what remains missing before formulating an optimization hierarchy.

For the third:

> Determine whether the completed theta kernel lies in, or can be approximated locally uniformly in transform by, a verified Lee–Yang class. Track interaction signs, single-site hypotheses, and exponential tails. Give an explicit construction or rule out a precisely stated ansatz. Positive density and finite zero matching are insufficient.

The sweep provides no established path to a proof of RH. Its practical conclusion is narrower: there are several concrete, falsifiable bridge problems worth considering, and further generic lattice enlargement is currently less informative than solving one of them.
