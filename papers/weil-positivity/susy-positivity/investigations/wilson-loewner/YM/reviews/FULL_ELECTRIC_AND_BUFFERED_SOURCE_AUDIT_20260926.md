# Audit of full-electric point sources and strict-half preparation

26 September 2026. Substantive self-audit of the [new research note](../notes/FULL_ELECTRIC_AND_BUFFERED_SOURCE_OBSTRUCTIONS_20260926.md) and live manuscript Section 12. Drafted for Edward Baker with substantial GPT-6 (Codex) assistance. Exact deployed variant and reasoning effort unavailable. This is not independent human or second-system verification.

## Findings and assumptions

Two candidate mechanisms were investigated. Both stay in the fixed SU(2) slab at coupling $8/5$ and its actual reflected state. Neither uses a continuum limit, RH, physical mass gap, or a postulated arithmetic spectral measure. No old research result is retracted.

The strongest new conclusion is the fixed-smoothing exclusion. It applies to the actual half-slab descent of any continuous finite-order distributional observable family in strict-half variables that does not depend on central spatial links. This is stronger than the previous ordinary-input-norm exclusion, but still excludes a specified source class. General finite-lattice distributional sources are not ruled out.

## A. Local electric source audit

1. **Dimensions and sectors.** The spatial lattice has 216 sites and 648 positively oriented links. The link manifold has dimension 1944. At an irreducible connection the gauge orbit has dimension 648, so the local quotient dimension is 1296. The common center is ineffective and acts trivially on the reference endomorphism fiber. Scalar and traceless sectors have orthogonal, gauge-covariant physical norms; the full summed electric form preserves both. This is not the earlier radial compression.
2. **Source and domains.** The coefficient of the point distribution is the fiber pairing with the actual eigenfunction value. The combined source series uses a fixed real Sobolev power and compact smooth Fourier smearing. Polynomial point spectral growth and Schwartz decay prove norm convergence and continuity. The diagonal and mixed sums converge absolutely. All spectral cutoffs therefore retain the actual pairing strongly.
3. **External mathematical input.** The local Weyl law is an established theorem, not a new YM assumption. Its application is confined to a fixed point of the principal quotient, where the reduced operator has scalar elliptic leading symbol and a smooth positive density. The bundle heat-kernel leading term is a scalar multiple of the fiber identity. Weight conjugation does not change the principal symbol. [Ramacher, Theorem 4.3](https://arxiv.org/abs/1512.02193) supplies the equivalent fixed-isotypic formulation; [Hörmander](https://doi.org/10.1007/BF02391913) supplies the underlying local law. No estimate uniform toward singular gauge orbits is needed. These primary sources were checked during this continuation; their PDFs were not added to the repository.
4. **Scaling exponent.** For $p=d-2s>0$, weighted cumulative mass is $dC R^p/p$. The source Fourier factor squared contributes $R^{-1}u^4|\widehat h(u)|^2$. Hence the exponent is $p-1$, and the integral is $\int_0^\infty u^{p+3}|\widehat h(u)|^2du$. The factor is $dC$, not $pC$. At $p=1$ the result is a constant, not a logarithm. At $p=0$ the weighted mass itself has a logarithm, but the source norm has the additional $R^{-1}$ suppression and tends to zero. This critical-case distinction is essential.
5. **Target comparison.** Neutral shrinking tests make every diagonal prime term identically zero for large $R$. Rescaling the full multiplier, including its $2\pi$ convention, gives $\|h''\|^2\log R+O(1)$. The note rederives the asymptotic used from the previous continuation. It does not appeal to zeros or RH. A fixed contact constant adds only a bounded quantity.
6. **Scope.** The proof does not give an eigenvalue spacing law for the full electric operator. It excludes fixed Sobolev powers of regular-point evaluation, including the distributional cases, rather than all generalized seeds. Logarithmic filters, other singular supports and singular-orbit sources are outside the theorem; matching a leading logarithm would still not establish the full prime/contact pairing.

## B. Uniform test-space and rank audit

The key new step is uniformity over an entire $N$-dimensional space, not just individual packets.

- Disjoint translated profiles $h_R$, with $R=aN$, give exact norm orthogonality after application of $R^{-2}T$, since their supports remain disjoint. Each test is individually globally pole neutral.
- Choosing the enclosing interval shorter than $\log2$ removes **all** prime mixed terms for every linear combination, not only its diagonal terms in the packet basis.
- Possible Fourier interference is handled by $\|P_{\le\epsilon R}f\|\le(\epsilon^2+1/(4R^2))\|H\|$. The low-frequency fraction can be made uniformly less than one quarter of squared norm. No unsupported claim of an approximately diagonal Weil Gram matrix is needed.
- The lower multiplier bound then yields $Q[f]\ge c\log N\|c\|^2$ uniformly. Ordinary derivatives give $C^m$ growth $N^{m+1/2}$; $H^s$ growth is $N^s$ by disjointness for integer orders and interpolation for other nonnegative orders.
- The count $\operatorname{rank}P_L\le C(1+L)^{972}$ follows from Haar product multiplicities and the bounded positive weight by the min-max principle. The gauge-covariant sector is smaller than the full matrix-valued space. The proof deliberately does not use the optimal quotient Weyl exponent.
- With rank less than $N$, a unit coefficient vector annihilates $P_LJ$. The exact pairing supplies a norm lower bound $\sqrt{c\log N}$. Electric regularity supplies the contradictory upper bound $C_rN^{m+1/2-r/1944}$ when $r>1944(m+1/2)$. All bounds are uniform in the coefficient vector chosen after $J$ is fixed.

The argument uses exact source linearity and pairing. It does not require that source translations be implemented by any specified physical generator. The large ambient dimension makes the rate weak but does not affect the asymptotic contradiction.

## C. Physical half-slab preparation audit

The central-link dependence is the decisive domain boundary.

For $\mathcal Af$ depending only on strict-half variables $X$, the normalized boundary vector is $I_f(U)/h(U)$, with $I_f=\langle\mathcal Af,e^{-S_+(U,\cdot)}\rangle$. In the physical norm the factors $h^2$ cancel, leaving precisely

\[
Z^{-1}\int e^{-S_0(U)}\operatorname{tr}(I_f^*I_g)/2\,dm(U).
\]

This is the actual reflected pairing, not a constructed target kernel. The full action remains in $I_f,I_g$. For every fixed distribution order $s$ on $X$, smoothness of the finite Wilson kernel bounds all output derivatives by the **same** $H^{-s}(X)$ norm. Continuity of $\mathcal A$ on a fixed compact arithmetic support gives one finite arithmetic order $m$, independent of output regularity $r$. Constants may depend on $r$, which is harmless: the rank proof fixes a sufficiently large $r$ before taking $N$ to infinity.

Smooth gauge-compatible regularizations converge in $H^{-s}(X)$, and the descent map is bounded into the physical Hilbert space (indeed into every electric Sobolev space). This proves strong retention and positivity of the completed limit. No subtraction or cutoff coefficient is chosen. Neither this construction nor the point-source construction uses the winding module, so no rational phase has been silently discarded. Finite winding operations in $X$ preserving the domain remain included; central-link operations need a different source relation.

If an observable depends explicitly on $U$, differentiating the output can differentiate the source itself. The common-order smoothing bound no longer follows. Boundary sources $F(U)$ are an elementary example. Therefore the theorem must not be called a general finite-slab distributional no-go theorem. Likewise, mere smoothness of every $Jf$ is insufficient: input seminorm order may increase with output regularity. The original one-fixed-$r$ compact-occurrence theorem remains valid.

## D. What the necessary preparation estimate does and does not prove

An exact source in $\mathcal K_r$ must satisfy

\[
\sup_{\|c\|=1}\|Jf_{N,c}\|_{\mathcal K_r}
\ge c_rN^{r/1944}\sqrt{\log N}.
\]

It follows that a fixed-support $H^s$ input bound requires $s>r/1944$, including exclusion at equality. For a $C^m$ bound the present proof only requires $m+1/2>r/1944$; it does not claim the sharper Sobolev threshold for a supremum norm. These are necessary conditions and no physical feasibility theorem is inferred from them.

The fixed electric heat example is an instance of the same smoothing mechanism, not a third candidate and not a claim that the electric operator is the physical time Hamiltonian. A continuum limit may destroy uniformity in the smoothing constants, link count, state bounds or preparation orders. The finite proof does not automatically extend to a continuum theory, with or without a mass gap.

## E. Reproducibility and preservation

The new arguments are analytical. They require no new zero data, finite Gram-matrix experiment, or numerical estimate. The previously recorded exact infinite-tail bound and diagnostic labels remain unchanged. No numerical program or record was edited in this continuation.

The live manuscript, indexes, draft history and build record are updated in place. Existing notes, review exchange, numerical records and the preceding continuation are preserved. Build and rendering results are recorded in [BUILD_RECORD.json](../BUILD_RECORD.json); hashes identify content rather than proof validity. No commit, tag, model change, large dataset or snapshot directory is part of this work.

Verification of the maintained draft: 45 pages, no overfull boxes, unresolved citations/references or duplicate labels; three pre-existing minor underfull warnings. All pages were rendered for layout review, with detailed inspection of the new section and changed front/back matter. The running-header date was corrected during that review. All 54 pre-existing non-index files in notes, reviews, replies and numerics matched the pre-continuation fingerprints. Local-link checks found no broken Markdown links (two apparent matches were mathematical functional-calculus notation, not links). Temporary renderings and the baseline fingerprint file remain outside the repository.

The remaining mathematical gap is an independently motivated source relation outside these excluded classes with strong physical realization and the complete mixed Weil identity. Neither a power-law exclusion nor a preparation cost proves RH or closes the program.
