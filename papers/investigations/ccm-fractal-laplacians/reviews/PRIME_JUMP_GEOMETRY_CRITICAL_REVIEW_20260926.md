# Critical review: prescribed prime-jump geometry

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact deployed model variant and configured reasoning-effort level are not exposed.

Scope: same-agent adversarial review of the [new continuation](../notes/CCM_PRIME_JUMP_GEOMETRY_OBSTRUCTIONS_20260926.md), its numerical programs and records, and the preceding resistance-form investigation. This is not independent peer review.

## Verdict and scope

The proposed next experiment has been completed at \(L=\log13\), \(N=4,8,16\). A specified, spectrum-independent nodal/harmonic interpretation fails both stiffness and mass tests, as well as refinement compatibility. A separate pointwise mass identity fails in the unchanged sine representation. The continuation also proves an analytic violation of the Markov property in the folded odd coordinates, independent of the numerical signs.

These conclusions are properly limited. They reject a prescribed arithmetic interpretation, not all possible fractals, all linear maps, or arbitrary non-harmonic Galerkin realizations. In particular, the original note's conditional realization criterion is not refuted; its hypotheses have not been supplied by the tested construction.

No material error was found in the earlier compact-star control or the two conditional resistance propositions. The exact historical control program reproduced its saved JSON record. The new obstruction clarifies a missing arithmetic step that the earlier note already left open.

## 1. Was the geometric map specified before seeing the spectrum?

Yes. The function map is the real sine representation of the original odd coefficients. Vertices are the first \(N\) binary radical inverses on the half interval, independent of Weil eigenvalues. These sets are nested even though the usual uniform interior grids of dimensions \(4,8,16\) would not be. The sine evaluation matrix is invertible by the Chebyshev/Vandermonde argument, and its recorded condition products are modest.

Both required nodal Gram matrices are computed by congruence, and the inverse congruences are checked. No eigenvector-derived coordinate change, diagonal clipping, conductance fitting, or mass fitting is performed.

The finite graph sign criterion requires vertex values with harmonic lifts, not merely some basis of a Galerkin subspace. A Fourier cardinal function can change sign, and a positive resistance energy on a subspace can have positive off-diagonal matrix entries in such a basis. The note explicitly retains this distinction. Its stronger measure test does not depend on choosing the dyadic grid, but still depends on retaining the specified sine functions.

## 2. Arithmetic signs, prime offset, and parity

The source formulas were checked against [CCM, equations (3.13)–(3.18), (4.2)–(4.3), and Theorem 5.10](https://arxiv.org/html/2511.22755v1). The prime term is negative correlation; the positive jump Gram adds \(2\sum c_a\) times the original \(L^2\) identity. The zero-overlap endpoint prime power is retained in that offset. The pole is a signed rank-two contribution, and the archimedean remainder includes the regularized tail in the preserved full Weil builder.

Passing positivity of the full-line jump Gram is an essential control. It is compatible with failure of the Markov property in the odd sector. A jump crossing the midpoint couples a field to the **negative** of its reflected value and produces a plus sign inside the squared difference after folding. Absolute-value contraction on the folded field is not the restriction of absolute-value contraction on the unfolded odd field.

Finite nodal witnesses are not all attributed to the prime contribution: the saved decomposition shows different dominant signed components at different cutoffs. The analytic tent witness is a separate construction that isolates the prime \(2\) exactly.

## 3. Audit of the analytic Markov obstruction

For a Markov form, disjoint nonnegative \(f,g\) must satisfy \(\mathcal E(f,g)\le0\), by comparing \(f-g\) and \(|f-g|=f+g\). This remains a necessary condition with a Dirichlet boundary or a nonnegative killing term.

The chosen tents are interior to \((0,L/2)\), disjoint, and their odd lifts are disjoint as well. Their direct separations are \(0.2\pm0.02\); their reflected separations are \(\log2\pm0.02\). Therefore exactly one prime-power delay contributes to the cross form. Its sign is positive and its normalization is \((4/3)(\log2/\sqrt2)h\), because both reflected cross correlations occur and \(\int_{-1}^1(1-|u|)^2du=2/3\).

The pole/archimedean cross kernel is smooth on both separation intervals. No divergent kernel is estimated at zero. The zero-correlation regularization and tail terms, as well as any scalar ground shift, vanish on these disjoint lifts. The bound \(|A|<8\) on \([0.18,0.72]\), the two factors from folding, and the two tent integrals give the stated \(32h^2\) error bound. The rational lower bound \(46/16875\) is strictly positive and does not use floating-point sign decisions.

Piecewise-linear interior tents have finite Weil form energy: they are zero-extended \(H^1\) functions and the short-translation difference controls the archimedean singularity. Smooth approximation provides the same strict inequality if a smooth test core is preferred. Thus the argument has an explicit domain, not just a distributional picture.

The result is for the natural pointwise folded odd form, for every scalar shift. It does not assert that an arbitrary positive finite pair is non-realizable after a different transport of functions and order. It also does not promote the prime-only two-sheet picture to a realization of the full pair.

## 4. The mass obstruction is independent and map-specific

The identity \(\sin^2(2\theta)=\sin^2\theta+\sin\theta\sin3\theta\) forces \(M_{22}-M_{11}-M_{13}=0\) for any measure with the fixed sine field. This is a necessary linear identity, not an assumption of diagonal mass and not a least-squares fitting residual. An atomic positive-measure control satisfies it.

The CCM defect is approximately \(-2.8491\times10^{-7}\) in all three cases, or \(2.178\%\) relative to the largest involved entry. The separate order-one arithmetic contributions nearly cancel; independent multiprecision agreement is therefore necessary. The sign is numerically compelling but is not labeled interval certified.

The exact shift identity \(D(M_N)=D_0+35\varepsilon_N/(12d_1^2)\) and Rayleigh–Ritz monotonicity are correct. A certified negative sign at one cutoff would propagate to all larger cutoffs in this representation. The current note explicitly leaves that certification undone and does not turn precision agreement into a rigorous infinite-cutoff mass theorem.

The proposed next test in the even integrated coordinates uses a different product identity. Its formula follows by writing \(x=\cos\theta\), factoring \(\cos(n\theta)-1\), and checking the resulting polynomial relation. The current records do not claim to test it.

## 5. Compatibility and spectral diagnostics

The Schur minimizer is unique because each fine stiffness is positive definite. Although not a positive-network harmonic map, it is the correct algebraic test for the selected nodal trace proposal. Both coarse forms fail, the maps fail composition, and the coefficients violate the maximum principle. These failures are reproduced at both precisions. A grounded path with a consistently pulled-back mass passes all three identities using the same routine.

Conversely, the finite inverse traces increase and the compression-interlacing inequalities pass. These passing tests must not be suppressed to make the negative conclusion sound broader. They leave open other simultaneous form embeddings. The original Fourier inclusion defects also pass their separate exact formulas; their tiny scalar ground changes do not explain away the order-one nodal compatibility defects.

The recorded traces exclude the untouched Fourier tail, which is saved separately. The continuation neither asserts determinant convergence nor drops that tail from the CCM problem.

## 6. Reproducibility and remaining limitations

The main program rebuilds the arithmetic matrix at 80 and 120 decimal digits, uses no zeta-zero evaluations, and records both its own SHA-256 and the preserved builder's SHA-256. The comparator checks those source hashes, binds the two input files by hash, and fails closed on missing files or mismatched sources. No full matrix archive is retained.

All 153 serialized numerical observables agree to the generator's 45-significant-digit output and pass a relative \(10^{-25}\) check; all 119 discrete observables agree. Numerical control residuals, which are precision-dependent, are intentionally excluded from that equality comparison and are checked separately against \(10^{-35}\). Their observed maxima are below \(7.4\times10^{-58}\) and \(4.7\times10^{-98}\).

An independent one-dimensional quadrature checked the smooth tent cross term by convolving the two tents. Its convolution density is \(w(v)=2/3-v^2+|v|^3/2\) for \(|v|\le1\), and \((2-|v|)^3/6\) for \(1\le|v|\le2\). Evaluating \(2h^2\int_{-2}^2w(v)[A(1/5+hv)-A(\log2+hv)]\,dv\) at 60 digits differed from the saved two-dimensional value by less than \(3.3\times10^{-49}\). Deliberately missing and source-mismatched records were also confirmed to make the comparator fail without writing an output record.

These are exploratory multiprecision computations, not ball-arithmetic certificates. The very small ground gaps and mass eigenvalues make that distinction material. The analytic folded Markov obstruction, however, uses an explicit rational bound and does not depend on those eigenvalue computations.

The appropriate next step is to specify and test a different map or a nonlocal mass before requesting resistance trace estimates. Simple-even hypotheses in general, the unshifted ground-energy sign, arithmetic convergence, Xi identification, and the full spectral triple remain unresolved.
