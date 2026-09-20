# Open directions: everything not consolidated into the manuscript

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Written at the point
where [manuscript 0.1](../manuscript.pdf) closed this investigation's first
round. It collects every thread that was opened and not finished, with an honest
status and an assessment of each, so that nothing has to be rediscovered.

Threads are grouped by how close they are to being actionable. Within each
group they are ranked. Where a claim is second-hand from a literature sweep it
is marked; where it is mine it is marked.

---

## A. Ready to work on now

### A1. Suzuki's de Branges paper, arXiv:2301.00421 --- **the top item**

Reportedly proves that the Hilbert space `H_W` of the Weil distribution *is* a de
Branges space, produces a **totally ordered family** of de Branges subspaces
indexed by `t >= 0`, and --- the part that matters --- **converts the RH criterion
from inequalities into equalities**.

Why it is first. Our central structural problem is that the criterion is an
inequality critical to more than twenty digits: no method that supplies a margin
can prove it, no finite computation can certify it, and the disproof test
accordingly came back with a fixed gap. An equality formulation sidesteps that
entirely. It is also the cheapest item here --- one session of reading, no new
machinery --- and the one verified contact we have with Suzuki's work (his
Theorem 1.4 in arXiv:2606.09096 reproducing our density identity at the
interval's own frequency scale, constant included) suggests the rest connects.

*Status: second-hand. I have read arXiv:2606.09096 directly, not this one.*

### A2. The spectral gap of the jump form

`lambda_2(S_L)` sits near `2e-4` and is roughly constant over `3/2 <= L <= 4`.
That is a spectral gap statement about the explicit jump Dirichlet form of
manuscript (4.1), it is where the criticality of the target originates --- the
pole supplies only a rank-one cancellation --- and it is well posed. The spectral
theory of nonlocal Dirichlet forms on an interval is developed and untouched
here.

An explanation would do two things: give the collapse of the margin a mechanism
rather than a measurement, and supply the ingredient the necessary condition is
missing (§7.4 of the manuscript shows the insufficiency is exactly a `lambda_2`
deficit).

*Status: the numbers are ours and reproducible; the question is open.*

### A3. Why is the ground state `cosh(x/2)`?

The ground state of `S_L` --- an operator assembled from the archimedean density
and the prime atoms --- has cosine `0.9844` rising to `0.9998` with the pole
form's positive direction `cosh(x/2)`. Nothing proved forces this. A proof would
make the rank-one cancellation structural rather than numerical and would very
likely sharpen Proposition 7.1. Of everything here this is the most concrete
"there is a theorem behind this number" item.

*Status: mine, numerical, unexplained.*

### A4. Port two computations into registered checks

The manuscript labels three computations as outside the checks. Two should be
brought in:

- **The smooth-basis saturation values** (`6.4e-10` at `L = 1` down to `1.2e-24`
  at `L = 3`). Currently `mpmath` with 80 zero ordinates. A standard-library
  port needs `decimal`, half-integer Bessel functions (elementary), and zero
  ordinates either self-computed or hard-coded as labelled published input, as
  `check_explicit_formula.py` in the companion investigation already does.
- **The near-null band edge.** Measured once in a brainstorm note: the
  near-null eigenvectors of the compression carry more than 99.9% of
  `|F^|^2` below `gamma_1 = 14.1347`, generic directions a few per cent, and the
  in-band count tracks `L gamma_1 / pi` to about 25%. This is selection rule 7's
  other half and it is not written down anywhere reproducible.

---

## B. Open with a named obstruction

### B1. A cone adapted to the pole directions

Manuscript §6 closes the *pointwise* cone and gives the reason (Sherman--Morrison:
a positive rank-one addition drives the inverse's entries negative). It does not
close a cone adapted to the two pole directions, nor Rugh's complex-cone theory
for indefinite forms (*Cones and gauges in complex spaces*, Ann. Math. 171
(2010) 1707--1752). The prize is named precisely: a **Collatz--Wielandt pointwise
supersolution**, which would convert the operator inequality into a pointwise
one.

Note the asymmetry that makes this worth trying: `N_L` itself is entrywise
positive off the diagonal, so Birkhoff's theorem *does* apply to it, and
Birkhoff bounds `|lambda_2|/|lambda_1|` --- which is exactly the gap of A2. The
cone is useless on `Q_L` and possibly useful on `N_L`. That connection is mine
and untested.

### B2. The sharp form of the necessary condition

`P_L` has rank two, so the exact criterion is a condition on the two scalars
`<cosh, S_L^{-1} cosh>` and `<sinh, S_L^{-1} sinh>`. Exact, small, and in the
same language. But `S_L^{-1}` is dominated by the near-null direction of A2, so
the two scalars are delicate in precisely the way the original problem is: this
relocates the difficulty rather than reducing it. Cheap to write down; I do not
expect it to open anything. *(The companion investigation already has a
two-scalar parity reduction of the same shape for its prime-free form.)*

### B3. Selection rule 6 for infinite prime sums

The exclusion of Bloch-lifted circle weights is proved for **finite** sums
(bounded periodic multipliers with purely atomic off-diagonal kernels, against an
unbounded symbol with a continuous kernel). The infinite case is open, because
`union_p (log p) Z` is dense, so atomic kernels can converge weakly to
continuous ones. That is Guinand--Weil duality and it is the only route left
inside that family. Settling it either way is a real result, and it stands
directly in the path of the physics-side programme (B4).

### B4. The spherical-vector correspondence

Gaiotto--Teschner reportedly give a one-to-one correspondence between positive
traces on the algebras `A_q` and unitary representations of `D_q` containing a
spherical vector, cut out by a `q`-difference system. This converts existence of
the positive pairing into **normalizability of a solution of a difference
system** --- genuinely self-consistent, and the strongest existence handle found
anywhere on the physics side. Section 5.2 of the companion manuscript works with
that difference equation and treats it as an obstacle rather than a handle.

I would hold this until B3 is settled: rule 6 sits directly in its path.

*Status: second-hand.*

---

## C. Closed, with the reason recorded

These are not to be redone. Each was pursued and settled this round.

- **Non-constructive existence of a realization** is exactly RH, and abstract
  operator theory applied to the target alone returns its input: Corollary 7.9
  of the companion manuscript manufactures the dilation the moment `||Pi|| <= 1`,
  which *is* the criterion. What remains available is rigidity (three results in
  hand), family exclusion by invariants, and finite-moment determination.
- **Krein--Rutman** adds nothing to the spectral theorem for a self-adjoint form;
  **Birkhoff** bounds a spectral gap and never a spectral radius; **Vandergraft**
  makes the existence of *some* invariant cone automatic and therefore
  uninformative. Manuscript §6.3.
- **Knaster--Tarski on operator intervals** is blocked by Kadison's antilattice
  theorem. It is *not* blocked on de Branges chains, which is part of why A1
  matters.
- **The RG fixed point.** Any RG fixed point is scale invariant; the Weil form
  fixes an absolute scale twice over (dilation destroys the prime atoms and
  shifts the density symbol). Ambrosino--Gaiotto's spectrum generator is
  *equivariant under* the flow, not a fixed point *of* it, which confirms this
  from a second direction.
- **Krein--Langer screw continuation.** The best-looking item of the whole
  literature sweep --- a local positive-definite kernel extends to a global
  spectral measure, non-constructively --- **is** Remark 3.3 of the companion
  manuscript: the extension is not unique and the arithmetic lives in the
  compatibility as `L` grows. The general theorem now has a name; the conclusion
  is unchanged.
- **De Branges' own RH route** is dead as stated: Conrey--Li exhibit the 34th zero
  violating the required positivity by `-5.4e-69`. Lagarias has only the
  converse, RH implies the structure function.
- **Nyman--Beurling as a fixed-point or cone problem.** Both the target and the
  subspace are explicit; it is not self-consistent, and no link between `d_N` and
  the localized form's least eigenvalue is known.
- **Transfer operators.** The Ruelle--Perron--Frobenius machinery attaches to the
  Selberg and Ruelle zetas; the Riemann zeros enter the modular surface only
  through the scattering determinant, which the cone machinery does not single
  out. No transfer operator with the Riemann zeros as spectrum was found.
- **A prime budget from the twisted-trace classification.** Retracted. The prime
  parameters are not roots of `P`: the elementary Schur algebra of Section 6.1 of
  the companion manuscript is the generalized `q`-Weyl algebra with
  `P(y) = 1 + y`, verified in exact rational arithmetic, so `n = 1` and its
  twisted-trace space is one dimensional. The algebra carries no arithmetic
  parameter at all; all of it lives in the chosen dressing state, which Section
  6.5 shows is unconstrained. What the classification does supply is a
  **localization of the unjustified step**: the Bloch lift uses infinitely many
  orthogonal copies, which is exactly where the classification's bound is evaded
  and exactly what the companion manuscript flags as lacking a field-theoretic
  interpretation.

---

## D. External work to track

### D1. Zhu, arXiv:2608.24827

**Worth borrowing:** Theorem 1.1, a reduction that drops the symbol's tail past a
threshold using the total prime-comb mass `A_L = sum_{log n < 2L} 2 Lambda(n)/sqrt n`
as an envelope, leaving a finite Legendre block with errors below `1e-100`. The
idea is good and independent of everything else about the paper.

**Worth knowing:** its certified upper bounds (`2.27e-17` at `L = 0.8`,
`3.19e-283` at `L = 2`, unconditional, interval arithmetic, sine-basis trial
functions) are far stronger than ours, in a different normalization --- against
`||f||_2^2`, not `K_+` --- so not directly comparable, but they show our trial
spaces are weak by hundreds of orders of magnitude.

**Worth discounting:** the barrier bounds only *its own* envelope method, as its
Remark 1.5 concedes; the `2 pi^2` Landau--Widom decay law is **fitted on four
points** and fails badly at `L = 0.8`; the paper is an unrefereed preprint whose
author name changed between versions, with single-author `mpmath` certificates
and a replication attempt of unknown outcome.

### D2. Suzuki, arXiv:2607.24830

The numerical companion to the screw-function paper: `lambda_1(a)` strictly
positive and superexponentially decaying, smooth through the first prime
threshold, with an archimedean law `lambda_k(a) = log(1/a) + log(k - 1/2) + B_0 + O(a)`
to 30 digits. Bears directly on selection rule 7. Not read directly.

### D3. Bombieri's index argument

Rendiconti Lincei 11 (2000), Theorem 8: the number of negative eigenvalues of
the truncated form equals the number of conjugate pairs of zeros off the line,
proved by continuous deformation with symmetries preserved. An index is an
**integer**, hence immune to the collapsing margin --- which is the main
attraction and the reason to keep it on the list. His Theorems 3 and 4
(attainment of the infimum by weak compactness) are the published precedent for a
non-constructive object-producing step in this subject.

---

## E. Method notes worth keeping

- **Never assemble `Q_L` from the term-by-term form in double precision.** At
  `L = 1` in a five-dimensional smooth basis the direct and spectral assemblies
  differ by `1.6e-6` while the entries themselves are `~1e-7`. Build it from
  `sum_rho |F^(gamma_rho)|^2`, which is a sum of positive terms.
- **Choose the basis for the direction of the bound.** Rayleigh quotients are
  upper bounds on `lambda_min` and lower bounds on `alpha_L`; a better-adapted
  basis strengthens whichever direction you are after. Cells are poor for
  anything involving the zeros, because their transforms decay like `1/tau`.
- **Exploit the Toeplitz structure.** `S_L`, `N_L` and the archimedean energy are
  all Toeplitz in the cell basis; with FFT matrix-vector products and Lanczos on
  the *nonnegative* operator, `alpha_L` at 4000 cells costs 0.2 s. The adaptive
  sum for the archimedean column needs a `psi'` tail correction at offset one,
  without which every value is off by a constant `0.0125`.
- **Say which direction a one-sided value certifies, every time.** Saturation
  quotients certify only failure; Galerkin values of `alpha_L` certify only the
  lower bound. Half of the work of this round was keeping those straight.
