# Assumption and source-domain audit of the OS/mass-gap continuation

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and reasoning effort: unavailable; not inferred.

Baseline: `12a39447c8ef41cfbf9ca1db60e73f78d5ef8c49` plus the preserved uncommitted investigation. This is a self-audit of the [new continuation](../notes/NATIVE_RECENTERING_AND_GAPPED_POSITIVE_COMPLETION_20260925.md), not independent human verification. No new physical assumptions are attributed to earlier finite-slab calculations without being stated.

## 1. Authorized assumptions and their actual use

The user permits the full OS axioms, a mass gap, and further natural physical assumptions. This broadens the conditional investigation; it does not authorize treating the desired arithmetic identity as an established physical law.

| Assumption or input | Where used | What it establishes | What it does not establish |
|---|---|---|---|
| Fixed finite SU(2) Wilson slab, smooth positive actual boundary density | Theorems 1–2 and finite-state application of Theorem 4 | Full current flow, actual packet limits, correct winding norms | A continuum vacuum or regulator-uniform estimates |
| Reflected boundary pairing and positivity | Actual source norms in Theorem 1 and each finite constrained-energy construction | Genuine Hilbert pairings in the stated physical representation | Positivity of the signed completed insertion |
| Full continuum OS reconstruction hypotheses | Sections 7–8 | Reconstructed vacuum Hilbert space, physical Hamiltonian, Euclidean preparation; the local observable-net formulation is stated | A continuum limit of the particular slab packet construction |
| Physical gap \(H\geq\Delta(1-P_{\rm vac})\) | Section 7; conditional physical interpretation of Theorem 4 | Bounded inverse energy on the excited sector and coercive energy bounds there | A gap on the vacuum line, ultraviolet compactness, or the arithmetic coefficients |
| Local phase-space compactness, or the stronger energy nuclearity assumption | Lemma 5 and its finite-compatibility application | Compact sets consisting of actual bounded local preparations | Arithmetic finite feasibility or uniform preparation costs for an arbitrary prescribed Gram matrix |
| Local vacuum separatingness, if used | Only the operator uniqueness refinement after Lemma 5 | Uniqueness and linearity of the local operator representatives | The vector existence step, which does not need it |
| Restricted Weil criterion and the explicit formula | Theorem 3 | Positivity would imply RH; its consequent atomic spectral form yields the domain obstruction | No RH assumption is used to construct any YM source |

The local phase-space hypothesis is a natural addition worth retaining. Its role is concrete: it preserves an actual bounded-observable preparation through a strong limit. The mass gap alone does not furnish that compactness. The original [Buchholz–Wichmann paper](https://doi.org/10.1007/BF01454978) motivates this phase-space condition; the new proof explicitly assumes the compactness map it needs rather than invoking every conclusion of nuclearity theory.

The [Jaffe–Witten formulation](https://www.claymath.org/library/monographs/MPPc.pdf#page=122) separates the continuum existence/gap statement from other expected physical properties. The new note follows that separation. The finite-state weighted electric operator is not relabeled as the continuum physical Hamiltonian.

## 2. Native recovery: normalization and full-state checks

The recovery operator is precisely \(\mathscr U_R=e^{iRA_\nu}\), with \(A_\nu=i[E_\nu,X]/(2\ell)\). It is not an arbitrary basis permutation or a target-dependent isometry.

The sign check is decisive. If \(Y=\nabla X/\ell\), then \(Y\theta=-\sin\theta\), so \(e^{itA_\nu}\) acts by pullback along the contracting angle flow and expands the support of a packet concentrated at zero. The inverse sign would not give the asserted recovered vector.

The full Haar divergence is \(-3\cos\theta\). Its Jacobian factor is \((\sin\theta_R/\sin\theta)^3\), and the state contributes \(w(\Phi_RU)/w(U)\). The square root of the geometric Jacobian cancels the packet's order-\(N^{3/2}\) amplitude at the identity. Formula (11) in the note verifies the surviving normalization explicitly.

The argument does not assume that the full weighted current leaves class functions invariant. The full link trajectory has finite remaining length, so \(w(\Phi_RU)\) has an almost-everywhere limit depending on the other links as well. The recovered physical source can consequently leave the original one-plaquette class subspace. The output is admitted in the already specified OS Hilbert completion, without a claim that it is a finite loop polynomial.

Strong convergence uses two proved ingredients: local Riemann-sum convergence to the sine transform, and equality of the limiting global norms by sine Plancherel. This avoids extending a fixed-time current approximation to times growing like R, which would not be justified by the earlier Duhamel argument.

The nonidentity phases converge only weakly after recentering. Their norm is not discarded: equation (13) gives the complete actual-state defect. Thus there is no conflict with the previous bounded winding-occurrence obstruction. The recovered source has ordinary L2 pairing and is explicitly excluded as the Weil source by the known high-frequency test.

## 3. The new closability obstruction is global and specifically scoped

Theorem 3 does not infer RH and then use it as an independent premise. Its contradiction has the following order:

1. Assume an isometric L2 source followed by a fixed closable operator realizes Q as a norm.
2. That norm supplies positivity, so the restricted criterion implies RH.
3. The consequent explicit formula gives an atomic zero-ordinate measure.
4. The exact pole-neutral profiles (17) tend to zero in L2 while their images are Cauchy with nonzero norm. This contradicts the originally assumed closability.

The growing supports in that sequence are essential. It neither disproves closability on every fixed support interval nor conflicts with continuity in the global smooth compact-test topology. Multiplicities cause no problem: one chosen ordinate has finite positive multiplicity, and the other distinct ordinates are isolated from it.

The excluded object is one fixed operator on the recovered Hilbert source vectors. This is not a prohibition of physical quantum fields as operator-valued distributions. A map \(f\mapsto\mathcal O(f)\Omega\) can be continuous in a test-function topology while not being closable in an unrelated larger L2 input norm; each individual smeared physical operator may still be closable on the physical Hilbert space. Future generalized-source proposals must keep these two notions of domain distinct.

This narrows the preceding recommendation of a positive completion: a fixed closable completion of an ordinary-L2 source is not the appropriate global target. It does not retract the earlier archimedean insertion, whose signed logarithmic multiplier is a different form.

## 4. Gapped Schur completion: why the finite positivity is genuine but insufficient

Every finite form \(\mathfrak q_A\) uses the actual weighted winding adjoints, a declared closed energy domain, and a fixed bounded readout. Its source norm is represented by \(K_A^{1/2}u_{A,y}\) inside the same physical class Hilbert space. It is not merely positivity of a numerical matrix or a norm in an unspecified auxiliary theory.

The divergent-limit proof does not assume compact resolvent or a joint diagonalization of energy and winding. Coercivity bounds the candidate source vectors. Weak compactness preserves the bounded readout. Lower semicontinuity of each finite positive prime form then forces any putative bounded-energy limit into the infinite form's zero domain. The contradiction already occurs before any arithmetic matching requirement.

The explicit coefficient-readout lower bound checks that distinct prime terms use distinct norm coordinates. It also explains why minimizing unresolved coefficients does not remove the divergence: they can partly cancel a prime difference only by accumulating coercive norm cost. Adding other nonnegative terms or fixed constraints cannot improve this conclusion.

A physical mass gap yields the needed norm control only after removing the vacuum component and identifying the energy and source sector. The note also gives a completely finite-slab application using the connected electric sector, whose elliptic gap is known. Neither application permits a formal negative counterterm to inherit the finite forms' positivity.

The inverse-energy alternative was checked as well: boundedness of \(K_A^{-1}\), the zero-domain argument, and \(\mathfrak q_A[K_A^{-1}v]=\langle K_A^{-1}v,v\rangle\) give strong convergence of the inverse to zero. Hence positive susceptibility sources \(K_A^{-1/2}v\) vanish. This conclusion concerns a fixed smeared input v and the specified increasing prime forms, not every susceptibility in a gapped theory.

## 5. What a conditional YM-to-RH theorem would still need

The OS and phase-space assumptions now provide a concrete occurrence framework: source vectors of the form \(e^{-\beta H}A_f\Omega\), with bounded local operators, smooth-test preparation bounds, and compact coordinate sets. The existing finite-intersection argument retains that physical preparation in the limit.

What remains unproved is the independent source relation that makes the finite assignments feasible and forces the separated-support gamma-plus-prime pairing, its symmetries, growth, and local anchors. Reeh–Schlieder density does not solve this: approximation of known Hilbert vectors does not produce a positive realization of an unspecified signed Gram form, and does not bound the necessary operator norms.

No claim is made that standard physical axioms are logically incapable of implying RH. Conversely, assuming that the completed signed response has a positive source realization would already insert the crucial arithmetic assertion. The continuation retains the user's broader conditional objective while making this distinction explicit.

Recommended next problem: specify a direct generalized source relation in the full YM observable sector, with the smooth-test topology and local preparation bounds stated from the outset, and derive a mixed arithmetic identity for it. The current recentering gives a controlled physical comparison; the two new obstruction theorems identify source completions that should not be retried under stronger generic assumptions.

## 6. Verification record

All current-flow factors, weighted-state transport, the global norm argument, the weak winding defect, the closability sequence, the coercive minimization proof, and the compact prepared-observable lemma were checked analytically in the order above. The [new script](../numerics/check_current_recentering.py) produced [19 passing floating controls and a small record](../numerics/records/current-recentering-20260925.json). Its weighted controls are a prescribed radial comparison, not the full interacting flow. No zero data or numerical eigenvalue claim enters the new proofs.

The two primary physical references were checked for their stated roles. The original nuclearity paper was available as author-uploaded text; its publisher/Euclid pages did not provide usable full text through the web interface. The source compactness statement is explicitly assumed and the needed image-closedness lemma is proved here, so no inaccessible theorem is a hidden proof premise. Research deductions remain subject to independent mathematical review.
