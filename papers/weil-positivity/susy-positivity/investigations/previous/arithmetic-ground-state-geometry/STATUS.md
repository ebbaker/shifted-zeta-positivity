# Status: arithmetic ground-state geometry

This ledger records the investigation through note 20, integrated into the manuscript on 13 September 2026. The detailed conclusions and source attributions are in [REPORT.md](REPORT.md) and the linked notes. “Established” below means derived within the stated model and hypotheses, with internal review; it does not mean independent specialist validation.

## Manuscript

A self-contained [working manuscript](manuscript.pdf) now presents all findings through note 20, with [editable TeX source](manuscript.tex), fifteen section files, external references and a [build guide](BUILD.md). The [coverage map](MANUSCRIPT_COVERAGE.md) locates every new result. The preceding versions, including the live 48-page draft before note 20, have complete [dated snapshots](archive/drafts/README.md). Its introduction states the complete positivity objective and an overview before the detailed calculations. The manuscript fixes the differential normalization explicitly: D=(Q1−iQ2)/2=bar∂+(∂W/2)∧, so the canonical Higgs operator is half the displayed superpotential variation. This does not change the earlier nonscalar/zero-class conclusions.

## Constructive results

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Four real supercharges on a cylinder | Explicit operators, common-core algebra, physical adjoints and self-adjointness argument; [note 01](notes/01_EXTENDED_THEORY_CONSTRUCTION.md). | Changes the original Morse Hamiltonian and scalar state. |
| One physical cylinder vacuum | Noncompact Morse index at positive real parameter, Fredholm continuation, and exclusion of even-degree zero states; nonzero complex parameter handled as a real closed-one-form twist. | Gamma is retained as a holomorphic period; its physical source-frame metric is not identified. The ordinary one-vacuum Berry curvature is locally zero. |
| Quadratic physical Euler metric | Two complex prime fields give \(|1-q|^{-2}\) in an explicit holomorphic frame. | The factor is locally removable by a frame change; positivity alone does not fix the source. |
| Interacting nine-vacuum prime theory | Quartic cross-coupled polynomial with nonzero mass and nondegenerate leading form; strong tameness gives the physical middle-degree/Jacobi identification. | The vacuum count and positive metric do not determine the arithmetic observable. |
| Interacting exact Euler dependence | With \(M=1-q\), \(g=cM^2\), \(\lambda=cM^2/2\), transported identity period is \(C_c/M\) and physical identity-class metric is \(H_c/|M|^2\); [note 05](notes/05_QUARTIC_PERIOD_TEST.md). | \(C_c>0\) and \(H_c>0\) are separate reference constants. The mass class vanishes in the Jacobi ring, so the mass direction has zero ordinary chiral curvature. |
| Positive semisimple matrix-metric control | Explicit local rank-two \(tt^*\) solution reproduces the real arithmetic norm with a changed complex extension; [note 02](notes/02_NONABELIAN_METRIC_TEST.md). | No microscopic realization or original arithmetic state/observable identity is supplied. |
| Abelian vector-parameter compatibility | Explicit Bogomolny extension of the old Berry connection; [note 04](notes/04_VECTOR_PARAMETER_GEOMETRY.md). | Works for general suitable holomorphic functions; does not select arithmetic normalization or construct a quantum parameter multiplet. |

## Scoped exclusions

| Excluded repair | Essential hypotheses and reason |
|---|---|
| Fixed quartic coupling, different ordinary cycle | Identity insertion, flat rapid-decay cycles, vanishing integration-by-parts boundary terms. All such periods satisfy a differential equation that excludes any nonzero constant multiple of \(1/M\) on an open region. |
| Elementary gamma-dependent prime mass | Replacing \(M\) by \(M+\lambda e^Y\) changes the required period and produces a non-isolated classical critical locus. This is not a general quantum-gap theorem. |
| Finite enlargement holomorphic in one fixed ambient Hilbert space | Nonnegative trace curvature together with ordinary finite-rank chiral \(tt^*\) forces a constant vacuum subspace; it cannot contain the entire Morse coherent family. Intrinsically holomorphic bundles with nonholomorphic ambient dependence are not excluded. |
| Prescribed reciprocal rank-two metric with the tested companion Higgs operator | Its required holomorphic modulus fails the exact compatibility condition. General matrices or changed complex extensions are not excluded. |
| Scalar reversible ground-state completion | With a pointwise scalar source, disjoint nonnegative inputs have the wrong cross-term sign once \(L>\log\rho\), \(\rho^3-\rho-1=0\). A triangle excludes scalar phase gauges for \(L>2\log\rho\), already before prime two enters. |
| Two pole states or an assumed-positive Schur complement | The missing diagonal remains infinite dimensional. A block energy positive exactly when the unknown target is positive is circular. |
| Curvature alone fixing the contact | A flat source/gauge change shifts the first logarithmic derivative without changing curvature. |

These restrictions leave genuine matrix or fermionic mechanisms, nonlocal source maps, periodic/flavor structures, and relative boundary pairings open. They do not rule out all interacting supersymmetric theories.

## First results after saving the draft: notes 06–09

The following results were developed in notes 06–09 and are now integrated into sections 7–10 of the manuscript. This chronological ledger preserves the limitations at that stage; the next section records the resolutions in notes 10–13, which the integrated manuscript incorporates directly.

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Exact rank-three physical symmetry sector | Identity volume and its shape insertions close on \(1,s,t\); explicit Jacobi, canonical Higgs and residue matrices in [note 06](notes/06_SHAPE_DEFORMATION_GEOMETRY.md). | The full theory still has nine vacua; a source or boundary preparation is needed. |
| Radial physical metric equation | Exact fermion phase symmetry and field dilation yield a radial three-by-three \(tt^*\) problem. | Necessary equations alone admit a constant positive control and do not select the physical solution. |
| Physical strong-interaction endpoint | Li–Wen's non-Morse comparison, uniform confining forms and continuous fixed-source representatives justify the pure-quartic limit. The rescaled metric has positive limiting diagonal and \(H(c,c)\sim a_0/c\); notes 06 and [07](notes/07_PHYSICAL_PAIRING_TEST.md). | Excludes the constant control in the specified frame. Endpoint constants, opposite endpoint and global metric are not evaluated. |
| Nonconstant physical-to-period ratio | Radial physical norm versus holomorphic nonconstant real-cycle period excludes constant ratio on every complex-open shape region; note 07. | Does not prove ratio variation or monotonicity on the positive real axis alone. |
| Scalar simultaneous-preservation obstruction | No common scalar source adjustment preserves both fixed Euler period and physical Euler metric during nonconstant holomorphic shape variation, with the specified source, cycle and flat target. | Does not exclude physical mixing, different boundaries or a different full pairing. |
| Exact shape-period differential equation | Homogeneity and mass-period identities give a third-order equation; nine independent Gaussian-moment coefficients check it in [note 09](notes/09_SHAPE_PERIOD_AND_NORMALIZATION.md). | Local expansion is asymptotic; the period is not thereby a physical norm. |
| Boundary Gram decomposition | A physically supplied boundary covector has a Riesz normalization and an orthogonal residual; multiple covectors yield a positive Gram reconstruction in [note 08](notes/08_BOUNDARY_SOURCE_REQUIREMENTS.md). | No physical realization of the chosen identity period as such a covector is established. |
| Unbounded source requirement | Fixed-support modulation gives \(Q_L[f_N]=\|\phi\|^2\log N+O(1)\), excluding every bounded \(L^2\) source map, including square-integrable Hilbert-valued source families and uniformly bounded regularizations. | Leaves unbounded/distributional sources, energy insertions and controlled singular boundary limits open. |
| Positive resolvent architecture | Independent self-adjoint bulk dynamics and a specified boundary coupling yield a positive operator Gram kernel, also for interacting theories. | No arithmetic spectral identification, contact normalization or complete Weil pairing is supplied. |

## Physical boundary and source milestone: notes 10–13

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Actual cohomological boundary caps | Explicit compact Koszul–Dolbeault sources, Euclidean projection, Hilbert adjoint and opposite-twist reflection; [note 10](notes/10_REFLECTED_BOUNDARY_PAIRING.md). | This constructs wavefunctional caps, not a geometric brane or the earlier exponential period. |
| Calibrated physical residue covectors | \(\ell_p(q)=4\pi^2\operatorname{Res}_f(pq)\), \(b_p=\Theta h_f(p)\), and \(\mathcal B=PG^{-1}P^\dagger=G^T>0\), with \(P=4\pi^2\eta_E\). | The Gram identity characterizes the physical pairing; it does not evaluate all global metric entries. |
| Explicit invisible state component | The reflected identity cap has \(\ell_1(1)=0\) and positive Riesz norm. A zero invariant Jacobi class has nonzero raw exponential period, proving failure of that insertion rule to descend. | Different boundary cohomology and derived period lifts remain possible. |
| Evaluated homogeneous interacting norm | The middle-source norm is \(\lambda=256\pi^2/3\), and \(a_0a_4=\lambda^2\). An explicit homogeneous source has norm squared \(\lvert1-q\rvert^{-2}\) with known normalization. | Changes the original identity source; mass insertion is still Jacobi-trivial. \(a_0\) is not evaluated. |
| All-nine-vacuum massive endpoint | Source-normalized local closed representatives and matching duality bounds give \(G_{\rm orb}\to4\pi^2\operatorname{diag}(16,64,48)\); [note 12](notes/12_MASSIVE_ENDPOINT.md). | No derivative expansion or Stokes matrices are computed. The identity limit is eight times the different rank-one Gaussian norm. |
| Unique radial metric selection | A direct trace-distance inequality and both physical endpoints force equality of positive solutions; [note 13](notes/13_RADIAL_METRIC_SELECTION.md). | Application to the Hodge metric uses the inherited exact \(tt^*\) identification. Uniqueness fixes \(a_0\) implicitly, not numerically or in closed form. |
| Closed positive gamma preparation | Explicit massive residual source, zero-extension logarithmic domain, compact-support core, maximal interval adjoint, and massive/heat singular limits; [note 11](notes/11_CLOSED_ARITHMETIC_SOURCE.md). | Exact positive norm identity covers the gamma kinetic term. Contact, poles and active primes remain an explicit bounded signed addition. |
| Finite-vacuum closability exclusion | Every densely defined closable map with finite-dimensional range is bounded, so finite vacua cannot hide the full unbounded arithmetic source. | Finite channels coupled to infinitely many excited states are not excluded. |

The raw Euclidean source convention now fixes the previously unevaluated universal residue factor to \(4\pi^2\). The opposite endpoint is resolved, and the endpoint class uniquely selects a positive metric under the stated equation. Earlier notes are preserved as historical derivations; their statements that these data were open describe the earlier stage.

## Coherent arithmetic gluing milestone: notes 14–17

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Local exact pole absorption | Attractive Robin Green kernel \(A_{\rm R}^{-1}(x,y)=-e^{\lvert x-y\rvert/2}\) gives \(K_{0,L}+P_L=4I-A_{\rm R}^{-1}\); [note 14](notes/14_POLE_BOUNDARY_GLUING.md). | Its auxiliary action has one negative even mode for every support length and is a saddle. |
| Exact reduced Robin threshold | The lowest gamma-plus-pole pairing is positive for \(L<4\), has kernel spanned by \(x\) at \(L=4\), and one negative odd direction for \(L>4\). A specified projected source isolates a rank-one residual. | This is not a sign conclusion about full \(Q_L\). The projection lacks a local physical derivation; a supersymmetric shift changes infinitely many response coefficients. |
| Signed poles inside a positive norm | Two coherent remote injections in the lowest massive mode yield \(K_L+P_L+e^D I\), \(D\ge L\), with physical unit cap, explicit adjoint and closed logarithmic domain; [note 15](notes/15_COHERENT_DELAY_DEFECT.md). | The positive contact \(e^D\) is optimal only within the stated two-shift ansatz; the matched amplitude is prescribed source data. |
| Finite raw delay obstruction | A fixed finite delay alphabet with square-summable cap injections, even in infinitely many massive modes, cannot produce negative contact while preserving the continuous gamma and pole kernels. | Resolvent filters, infinitely many distinct delays and changed bulk constraints are not excluded. |
| Conservative prime-return source | An explicit nonnegative graph Laplacian, orthogonal coupler and observed output produce every prime repetition with its exact negative translation coefficient; [note 16](notes/16_PRIME_RETURN_CHANNELS.md). | The necessary positive contact is \(c_p=2\log p/(\sqrt p-1)\). Input scale and prime parameters are prescribed. |
| Sharp stationary prime contact | Arbitrary coherent positive channels with exactly the prescribed whole-line prime Gram require contact at least \(\sum_p c_p\). | Fixed-support compressions can have a smaller contact; the support scope is explicit. Unrenormalized all-prime norm still diverges. |
| Positive completion of the complete form | A stable response of the known positive \(T_0=T_L+P_L+e^DI\) gives a closed source with \(\|\Gamma_Lf\|^2=Q_L[f]+\langle f,C_{\kappa,\mu}f\rangle\); [note 17](notes/17_COLLECTIVE_FEEDBACK_AND_COMPACT_DEFECT.md). | \(C_{\kappa,\mu}>0\) is compact, infinite rank and nonzero for every parameter. Neither exact target positivity nor compatibility of completed sources across supports follows. |
| Regularity threshold for coherent repair | Corrections in any finite Schatten class, including Hilbert–Schmidt and finite rank, cannot turn the gamma or assembled pole-and-prime reference into full \(Q_L\). | Arbitrary compact corrections remain possible. The displayed feedback is compact but outside all finite Schatten classes and still leaves the explicit error. |

That stage's identity is a positive **completion**, not a positive factorization of the target. The feedback uses an inverse of an independently positive reference, never a square root or unknown spectrum of \(Q_L\). Its arithmetic gain is matched after derivation, not forced by a bulk normalization law. These qualifications are part of the result.

## Review and joint-response continuation: notes 18–19

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Review of notes 10–17 | All 39 prior checks reproduced; no invalidating error found in the central source, endpoint, comparison and feedback arguments; [note 18](notes/18_REVIEW_AND_NEUMANN_COMPARISON.md). | Internal review only. The physical chiral-equation identification remains conditional, and prescribed gains are not a derived arithmetic law. |
| Two-sided gamma comparison | \(b(H_{\rm N})\le T_L\le b(H_{\rm D})\) gives the eigenvalue asymptotic with \(O(n^{-1})\) error and an explicit high-mode cutoff. | The Neumann and Dirichlet preparations are comparison models, not replacement boundary conditions. |
| Exact positive high-sector gluing | A joint response and a convergent binomial series factor the compression where its positive gap has already been proved; [note 19](notes/19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md). | This does not assume or establish positivity on the remaining low modes. |
| Finite-rank completion | A closed source on the full logarithmic domain has \(\|\Phi_Lf\|^2=Q_L[f]+\langle P_Nf,D_NP_Nf\rangle\), \(D_N>0\), with all mixed terms and the unused low output retained. | The error has rank \(N\) but is nonzero. The source correction remains outside every finite Schatten class. |
| Explicit finite comparison | \(Q_L\ge0\) iff \(G-D_N\ge0\), where \(G\) is an independently positive low-output Gram. At \(L=1\), a rational proof permits \(N=4,\delta=1/16\). | No sign or numerical enclosure of this finite matrix is supplied. This is not a new full-form positivity interval. |
| Compatibility within a support envelope | One constructed source restricts consistently to every smaller interval. | Rebuilding on a larger envelope need not preserve its compressed finite-rank error. No all-support limit is constructed. |

The present construction is a general Hilbert-space completion mechanism, now with an explicitly controlled finite-rank remainder. The rational counterexample in the new checks demonstrates that such a completion can exist even when its target has a negative direction.

## Arithmetic sign and boundary-response continuation: note 20

| Result | Scope and evidence | Remaining limitation |
|---|---|---|
| Reduction audit and reference invariance | Live sections 10–15 and notes 18–19 assessed; no invalidating domain or normalization gap found under their hypotheses. The scalar reference shift cancels from \(S_N\). | Generic completion still does not correlate primes and archimedean data. Physical chiral identification remains conditional. |
| Exact gamma boundary correction | \(T_L=b(H_{\rm N})+\mathcal K_L\), with positive bounded \(\mathcal K_L\); exact form/operator domain equality and finite cosine operator core. | This is a gamma structure theorem, not an arithmetic sign. |
| Noncompact boundary obstruction | Essential norm exactly \(\pi/2\) for every \(L>0\); finite mass tails never converge in operator norm, including after finite-codimension compression. | It does not exclude finite-input or weighted approximation. It concerns a different operator from note 19's compact source correction. |
| Explicit finite-input gamma tails | Endpoint exponential columns and parity coefficients, with a tail bounded by \(\sqrt{2(2N-1)/L}(a_J^{-1/2}+a_J^{-3/2})\). | The bound depends on length and input dimension; it does not control the full operator tail. |
| Full mixed-response residual certificate | Positive high-sector Galerkin responses give \(S_N\ge PW_LP-B^*Y_K-d_K^{-1}R_K^*R_K\), with mass/mode tail and enclosure-error rules. | The arithmetic lower matrix has no established all-length sign. Finite-certificate completeness is stated only for a strictly positive fixed-length Schur matrix. |
| Inverse-tail and physical-gluing tests | Rational negative examples at every finite inverse order; abstract defect-contraction existence is equivalent to the remaining sign. | Ordered tails cannot be dropped; a physical proof needs an independent arithmetic intertwining identity. |
| Exact discrepancy formulation and density obstruction | Retaining all gamma, pole and contact data but replacing primes by \(e^rdr\) yields \(Q_2^{\rm dens}[\cos(\pi x/2)]<-2979/6125\); the entire gamma tail is controlled. | This is a negative non-arithmetic control, not a negative Weil input. Methods using additional signed prime information remain open. |
| Cofinal support criterion | Independent signs for \(L_j\to\infty\) suffice by zero extension, with varying dimensions and gaps. | No signs are proved here; physically compatible sources across all envelopes remain a separate problem. |

[Note 20](notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md) gives self-contained proofs, four candidate mechanisms, the exact missing lemmas, counterexamples and primary inputs. The mature results appear in the live manuscript. The outcome is new intermediate operator structure and rigorous obstructions, not full positivity.

## Verification and storage

Ten standard-library programs pass fifty-nine labelled exact checks: the previous forty-nine and ten arithmetic-sign/boundary-response checks. Historical records are unchanged. The validator checks hashes, file sizes, links and record replay. Algebra replay does not prove analytical self-adjointness, Hodge comparison, source domains, compactness or convergence. Earlier passes recorded subtask review of notes 10–17; the current derivation received single-agent internal review. No external specialist validation is claimed.

No floating-point experiment, sampled positivity claim, new certified positivity interval or large numerical dataset was produced. [ARCHIVES.md](ARCHIVES.md) specifies `szp-archive` for future large regenerable data. Every current deliverable is below the repository's approximate 1 MiB limit.

## Open target and next step

The complete Weil form still has no independently established positive norm on all supports. The strongest completion now leaves the finite-rank form \(P_ND_NP_N\), with
\[
D_N=\alpha I+B^*(H^{-1}-T_H^{-1})B>0.
\]
Proving a signed arithmetic estimate for the complete mixed-response residual is the next task; missing lemma B of note 20 states a sufficient target. A proof separately at every length would suffice without a uniform gap or compatible physical sources. The old one-parameter feedback cannot erase its own compact error; note 19 changes the response and mode treatment. See [CONTINUATION.md](CONTINUATION.md).
