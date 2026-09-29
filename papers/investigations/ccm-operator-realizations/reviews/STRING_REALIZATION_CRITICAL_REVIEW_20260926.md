# Critical review of the string and graph Dirac continuation

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Scope: same-agent adversarial review of [continuation round 2](../notes/CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md), its new numerical program, and the relevant source equations. This is not independent peer review or interval certification. Earlier notes and records remain unchanged.

## Verdict

The strongest justified claim is an exact finite realization by positive point masses and springs, with an explicit unitary map of the CCM quotient to the string's graph Dirac operator and an exact inverse-frequency trace as a first mass moment. The common strain-space formulation gives a proved conditional determinant convergence criterion. It does not verify that criterion for CCM.

The main danger is interpreting universal inverse-spectral reconstruction as an arithmetic explanation. The note now specifies the forcing vector, the geometric normalization, the cyclicity condition, and the additional tightness assumptions. The large differences between two natural ports show why these qualifications matter.

## 1. Positivity and circularity audit

The starting hypotheses are still the simple-even least eigenvalue of the full finite Weil matrix, the nonzero boundary value of its eigenvector, and the CCM weighted-adjoint identity. Positivity of the string is deduced from the shifted positive pencil; it cannot be used to prove those inputs.

In particular:

- The ground vector of the Weil matrix is removed before the mechanical operator is constructed. Positivity and simplicity of the lowest string vibration concern a different object.
- The map \(W\mapsto W+cI\) leaves all constructed dynamics unchanged. The sign of the unshifted least eigenvalue is irretrievable from these dynamics alone.
- The selected port must be cyclic to obtain one connected scalar string. That is an additional condition, not a consequence asserted from the CCM hypotheses. A direct sum of strings covers the noncyclic case. The numerical program deliberately stops on Lanczos breakdown rather than discarding invisible modes.
- A bounded first moment is a useful geometric formulation of a trace bound, but asserting it without a separate estimate would simply restate the missing result.
- The code uses primes and the defining archimedean distribution. It does not evaluate zeta zeros, even for a diagnostic.

## 2. Checks of the strongest finite claim

The Cholesky transformation uses \(M=AA^\dagger\), \(H=A^{-1}KA^{-\dagger}\), and configuration map \(q=A^{-\dagger}UD_hu\). Both congruences were checked, so a mass metric has not been dropped.

For positive tridiagonal \(C\) with negative nonzero off-diagonals, the cofactor formula in (6) proves \(C^{-1}e_1>0\). The equation \(Ch=e_1/r_1\), with \(h_1=1\), fixes the left spring and leaves a free right end. The row identities, including the last row, verify the local energy exactly. No unproved positivity of a continuum density is used.

An independent two-bead hand control is
\[
C=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
r=(2/3,1/3)^t,\quad h=(1,1/2)^t,
\]
\[
m=(1,1/4),\quad k=(3/2,1/2),\quad x=(2/3,8/3),
\quad K_s^{-1}=\begin{pmatrix}2/3&2/3\\2/3&8/3\end{pmatrix}.
\]
Thus \(\sum m_ix_i=4/3=1+1/3=\operatorname{tr}C^{-1}\), and the normalized determinant is \((1-z^2)(1-z^2/3)\). This checks the endpoint, scaling, and inverse-kernel conventions without CCM data.

This example was also passed through the new implementation at 80 digits: the predicted masses and springs agree, with maximum scaled residual below \(1.62\times10^{-81}\). A diagonal two-mode pencil with port \(e_1\) correctly raises the noncyclic-seed error.

A primary-source sign issue was found on visual inspection: the isolated formula for \(l_M[u]\) on p. 13 of Mikhaylov--Mikhaylov has a positive slope jump, while the preceding integral definition and smooth formula on p. 12 imply its negative. Their negative matrix \(A\) in \(M u_{tt}=Au\) is consistent with the latter convention. Our equations (11)--(12) derive the jump sign from the positive spring energy, and do not use the inconsistent display as a premise.

The node/edge operator uses an anchored incidence matrix, not a periodic graph incidence matrix. It is invertible and has no null mode. In (14), the edge component includes \(d_s\); omitting it would lose the stiffness metric. Direct substitution verifies both norm preservation and intertwining with (4). Consequently the finite operator equivalence is stronger than bare frequency agreement. Adjoining the free tail only gives the full operator at a fixed cutoff, not its algebra representation or an infinite-cutoff limit.

## 3. Continuum and determinant audit

The ambient operator \(\mathcal C_\mu\) is a positive inverse-dynamics operator on a fixed strain space. At finite cutoff it has a large kernel, so it is not identified with the inverse CCM operator on that entire ambient space. Only its nonzero spectrum and its restriction to its finite range are used. The factorization \(ZZ^\dagger\), \(Z^\dagger Z\) proves the spectral and determinant claims.

The limiting proposition requires weak convergence of finite positive mass measures, a mass bound, and uniform first-moment tail control. The map \(x\mapsto|1_{(0,x)}\rangle\langle1_{(0,x)}|\) is trace-norm continuous on compact sets; the explicit tail hypothesis controls its unbounded norm. Those facts give trace-norm convergence without an unjustified convergence theorem for unbounded differential operators. The determinant argument then follows from convergence of positive eigenvalue lists in \(\ell^1\).

The counterexample \(j^{-1}\delta_j\) was checked: weak convergence to zero and a uniformly bounded trace do not force determinant convergence to the determinant of the weak limit. The determinant stays \(1-z^2\). Thus a weak-measure argument with no first-moment tail hypothesis would be false. Conversely, mass transport inside a common compact interval is genuinely controlled by (22); exact coincidence of moving atoms is not needed.

This proposition is sufficient, not necessary. It does not prohibit determinant convergence in other coordinates or under weaker hypotheses. It also supplies no arithmetic identification of the limit.

The full determinant includes the Fourier tail. The support and Fourier parameters remain separate: \(L=\log X\), \(N\), and the reconstructed string length \(x_N\) are three different quantities. The possible Gaussian in the joint limit is retained. None of the computed first frequencies can justify discarding it.

## 4. Obstruction audit and controls

Equation (23) follows directly from nested Fourier compressions at fixed \(L\). Its sign uses min--max for the original \(W\), not for the changing mechanical pencil. When the least energy drops strictly, the natural inclusion changes both mass and stiffness; claiming standard fixed-pencil Galerkin monotonicity would therefore be invalid. This rules out that inclusion as an exact fixed-energy embedding, not all conceivable embeddings. The numerical change in Jacobi coefficients similarly rules out exact principal nesting for the tested normalization, not future convergence.

The passive-bath obstruction uses residues of a specified rational function with specified free poles. Positive Hilbert-space couplings contribute squared amplitudes of a single sign. Mixed residues cannot be repaired by changing their phases. The separate min--max argument for a self-adjoint rank-one update gives the same finite exclusion when \(\omega_1>d_2\).

The program runs a positive update of \(\operatorname{diag}(1,4,9)\) and verifies its interlacing as a control. The actual small CCM case \(X=2,N=4\) has residues all of one sign. The note therefore does not claim a universal failure of passive boundary realizations. The mixed signs at the other tested cases are numerical observations; a rigorous instance would require sign enclosures. A changed bath, more ports, or a dense metric is outside the obstruction's scope.

The exact two-coordinate positive pencil displayed at the end of Section 9 has squared frequencies 9 and 16 against free poles 1 and 4, with residues of opposite signs. Its integer determinants verify positivity directly. It supplies a nonarithmetic control for coexistence of dense positive energy and failure of fixed-bath interlacing.

## 5. Numerical validation and precision

The two full runs use 120 and 160 decimal digits, for five \((X,N)\) pairs and two port choices. The [comparison program](../numerics/compare_string_precision.py) verifies the hashes of both the new reconstruction program and the unchanged Weil builder before comparing records. All **504 numerical observables** agree at all **45 saved significant digits**. The maximum scaled identity residual is less than \(8.85\times10^{-92}\) at 120 digits and \(2.20\times10^{-130}\) at 160 digits. These are reconstruction residuals, not certified error bounds on eigenvalues or coefficients.

Checks cover the mass and stiffness congruences, Lanczos orthogonality and intertwining, the explicit graph Dirac metric and intertwining, the Green kernel, the trace moment, determinant and boundary response, and the two cutoff-compression identities and their Rayleigh drift. Selected Weil matrix entries retain the earlier builder's direct-correlation cross-check.

For the main port at \(X=13\), the increasing trace fractions beyond \(10^6\) are a warning about the missing tightness input, not a proof of failure at all cutoffs. The alternative displacement port changes the geometry greatly; at \(N=16\) its fraction beyond \(10^6\) is about 0.045, compared with about 0.846 for the force port. It would be incorrect to treat the force-port geometry as a spectral invariant.

The two runs share their quadrature and linear-algebra implementation. Precision agreement does not detect a shared modeling or formula error; the source checks, explicit proofs, and synthetic controls provide different checks of those aspects. No external human review has been performed.

## 6. Remaining mathematical gap

The finite realization is complete within its hypotheses. What is missing is an arithmetically specified port and normalization with estimates proving mass control and first-moment tightness as \(N\) grows, followed by support-dependent control and identification of the resulting full entire function. The next proposed investigation isolates the first of these at fixed \(L=\log13\).

Research-history and storage check: the original derivations, review, builder, and numerical records were not altered. The added JSON files are small records of coefficients and diagnostics, not matrix archives; each is below 50 KB. Downloaded third-party PDFs and their renders remain in temporary storage outside the repository. No large-file archive, commit, or release was created.
