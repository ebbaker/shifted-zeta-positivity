# Review of the energy-port continuation and fixed-support limit

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Scope: same-agent adversarial review of the existing CCM operator-realizations investigation and the [third continuation](../notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md), including its proofs, source definitions, numerical program, and records. This is LLM-assisted research for Edward Baker, not independent peer review or interval certification.

## Verdict

The earlier finite mechanics/string construction is consistent with its stated hypotheses. The new port experiment completes its proposed preliminary test at fixed support, with increased cutoff and precision. It does not establish spatial tightness, and no tested smoothing is shown to solve that problem.

The strongest new analytic result is that the integrated mass operator is trace class at fixed support, followed by a conditional trace-norm determinant limit on the original Fourier space. The latter requires a positive limiting odd-sector gap. The gap is not proved and is not certified by the computations. This is a useful reduction of the common-space problem; it is not a resolution of the continuum simple-even question, support growth, or Xi identification.

## 1. Review of inherited work

The mass metric in \(M=J^*T_+J\) is retained, and the quotient-to-string transformation is a congruence of both forms. The anchored incidence matrix and its graph Dirac map have the correct dimensions and no constant null mode. The lost scalar shift is explicitly recorded, so the construction is not offered as a proof of unshifted Weil positivity.

The earlier passive-bath obstruction is confined to one port and the specified unchanged free poles; it is not a general obstruction to passive realizations. Its mixed-residue argument and finite min--max control have the stated scope. The common-strain-space determinant criterion explicitly assumes weak mass convergence and uniform first-moment tails. Its escaping-mass counterexample correctly explains why a bounded trace alone is insufficient for that particular representation.

No correction to those central finite claims was needed. This continuation instead acts on two limitations: an arbitrary inverse-spectral port can obscure the arithmetic, and a sufficient geometric criterion should not be mistaken for a necessary determinant-convergence condition. Historical notes and code remain unchanged.

## 2. Port identities and numerical design

With \(v=A^{-1}b/\beta\), \(H^{-1}=A^*K^{-1}A\) gives exactly
\[
r_1=(b^*K^{-1}b)/\beta^2,\qquad
\|r\|^2=(b^*K^{-1}MK^{-1}b)/\beta^2.
\]
The two formulas for first position and total mass follow with \(h_1=1\). An overall force amplitude cancels. The inequality for total mass uses a positive inverse operator, so its direction is correct. It does not bound the first-moment spatial tail.

The new generator does not alter either preserved source program. It supplies a general force to a separate reconstruction routine, shares the Cholesky whitening across the four ports, and reorthogonalizes Lanczos twice. At the smallest cutoff it compares both historical ports with the earlier implementation. Both mass and stiffness congruences, not just frequencies, are checked for every port.

The smooth profile is fixed by \(f_n=2^{1-n}\) before the experiment. The inverse-energy profile is explicitly cutoff dependent and derived from the positive pencil; it is not mislabeled as a fixed smooth limiting function. All spatial comparisons keep the first mass one. Port-dependent renormalization after inspecting the tails would invalidate this comparison, and is not used.

The N=32 spatial tails are about 0.9532, 0.1381, 0.1375, and 0.1987 of the inverse trace for the force, displacement, smooth-displacement, and inverse-energy ports. They justify the narrow conclusion that the tested smoothing has not demonstrated tightness. They do not justify an assertion that any port fails the supremum-over-all-cutoffs tail condition.

The very long strings can have modest total mass because remote masses are very small. The code retains positions and masses together with their products. No conclusion is drawn solely from the last bead's position. The 90% trace quantiles provide a less extreme geometric diagnostic and also continue to move.

## 3. Audit of the trace-class mass proof

The limiting Weil operator is unbounded. Equation (1) must be read as a form composition, and the note constructs it in that way through \(Z=(W_+-\varepsilon_\infty)^{1/2}J\). It does not multiply arbitrary unbounded operators on an unspecified domain.

The archimedean multiplier is \(2\theta'\), not \(\theta'\). This normalization was checked against the source's (3.8), (3.9), and (3.19). Its continuous logarithmic growth permits the global upper bound used in (5); the proof does not need an uncertified numerical maximization of that symbol. The bounded prime and pole contributions are bounded in absolute value, so possible negative terms do not undermine the upper estimate.

Crucially, \(Je_n\) has zero endpoint values. Its zero extension has an ordinary square-integrable weak derivative, with no boundary delta contributions. Therefore Plancherel and the concavity of \(\log(1+s)\) apply in (7). The identities \(\|Je_n\|^2=3/d_n^2\) and \(\|(Je_n)'\|^2=1\) give a summable \(O_L(\log n/n^2)\) bound. The extension from columns to arbitrary odd vectors uses convergence under J in \(H^1_0\) and the closed shifted form, which supplies the required domain justification.

The infinite ground energy exists and is finite by the semibounded compact-resolvent Weil-form result. The proof needs neither its sign nor a simple eigenvalue to make \(B\) positive and trace class. Its tail estimate concerns B in Fourier coordinates. It does not establish the spatial-tail hypothesis of the previous string theorem.

## 4. Audit of the conditional determinant proposition

The finite-to-infinite shift is \(\delta_N=\varepsilon_N-\varepsilon_\infty\ge0\). Thus \(B_N=P_NBP_N-\delta_NP_NJ^*JP_N\), with a minus sign. This agrees with the earlier finite-cutoff identities. The trace-norm compression bound follows from two Hilbert--Schmidt products and the explicit \(\operatorname{tr}(J^*J)=L^2/8\).

The nontrivial additional hypothesis is \(\inf\sigma(W_-)>\varepsilon_\infty\). A continuum simple even ground state would imply it, since compact resolvent gives an isolated ground eigenspace. Finite simple-even behavior does not imply this uniform gap. The recorded finite odd Ritz gaps decrease by over 25 orders of magnitude over the experiment, and provide no certified positive lower bound on their continuum limit. The note states this limitation prominently.

Under that hypothesis, Galerkin inverses converge strongly by energy projection onto the odd form core. The changing scalar shift is a norm-small resolvent correction once \(\delta_N<\kappa_L/2\). The inverse square roots converge strongly by continuous functional calculus for uniformly bounded positive operators. Their products with \(B^{1/2}\) converge in Hilbert--Schmidt norm by finite-rank approximation, giving trace-norm convergence of the sandwiched operators. Strong resolvent convergence alone is not being used to assert determinant convergence.

The common-space finite operators have an infinite-dimensional kernel outside the finite Fourier range. Only their nonzero eigenvalues are identified with reciprocal squared mechanical frequencies. No assertion about a full limiting spectral triple, transported algebra, or first-order Dirac domain is made.

The result is not advertised as independent of existing conditional ground-state approximation arguments. Connes--van Suijlekom's Theorem 5.11 is acknowledged; the added content for this project is the explicit integrated trace-class factor and determinant realization. The fixed-support Fourier tail tends to one. Joint support/cutoff limits and their possible Gaussian remain separate.

## 5. Why stable port moments do not finish the string argument

The normalized counterexample \(\mu_R=\delta_1+(2/R)\delta_R\) has first mass and position one, bounded convergent total mass, and cyclic finite first-bead port. It nevertheless loses two units of inverse trace at spatial infinity. Its determinant tends to \((1-t)(1-2t)\), while its first-port response tends, away from the limiting poles, to \(1/(1-t)\). The second factor becomes invisible in that limiting response.

The printed two-by-two determinant and resolvent formulas were checked by exact rational arithmetic at R=10,100,1000. The formulas themselves prove the assertion for every R>1. Positivity follows from positive masses and positive springs, or the positive leading principal minor and determinant. This is a synthetic control, not an alleged CCM counterexample. It shows why a limiting observability/cyclicity input deserves attention if the string route is pursued.

## 6. Reproducibility and preservation

Both complete runs use mpmath 1.3.0, at 120 and 160 decimal digits. All 1,177 saved numerical observables agree at their 45 retained significant digits. Maximum scaled reconstruction residuals are below 7.76e-76 and 1.11e-115. Those are identity residuals, not interval enclosures or independently bounded quadrature errors. Both runs share the same builder and arithmetic implementation.

The comparison program verifies all three generator-source hashes before reading results and excludes precision-dependent residuals from the observable comparison. A deliberately stale generator hash is rejected with a regeneration instruction. The two-bead reconstruction and noncyclic controls test conventions that numerical agreement alone would not establish. The exact rational tail control has its own source hash and reproduction command.

Records contain small coefficient lists and diagnostics; the largest new record is below 105 KB. Dense matrices are regenerated in memory, no third-party papers are copied into the repository, and the large-file policy is respected. The older notes, reviews, programs, and records are preserved byte-for-byte. The investigation and numerical indexes are extended, and a concise DRAFT_HISTOR.md records the milestones without new manuscript snapshots. No commit or release is made by this continuation.

The proposed next task is a rigorous low/high-block estimate for the limiting odd sector, with the small-energy modes treated explicitly. It directly tests the remaining hypothesis in the new theorem. Selecting still more smooth ports without an estimate would currently add less mathematical information.
