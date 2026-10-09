# Review of the mixed middle sieve estimate and direct energy budget

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate derivations by same-model agents are internal validation, not
independent specialist review or formal proof verification.

The reviewed [mixed note 6](../mixed_character_families/notes/6_WEIGHTED_MIDDLE_SIEVE_AND_DIRECT_ENERGY_20261009.md)
adds a conditional actual-chain sector estimate. The good part of the
middle row supported outside both endpoint supports has full physical norm
at most \(U^{103/200}\). The uniform reserve below the probe target is
\(4031/1500000\). The earlier sharp counting family is controlled by this
different averaged-kernel argument. The full seven-cut remainder and the
direct correlation estimates remain open.

## 1 Operator scope and retained masks

The new input to the mixed lane is the already imported physical sextic
operator from `cor:physical-operator` in the
[short-family manuscript](../short_families/short_family_reductions.tex).
The [primary theorem](https://arxiv.org/html/2610.04045v1#Thmtheorem1.1)
was checked for its index class and parameter dependence. The index bound
is the physical norm of a power-free ideal. Neither that source theorem
nor the repository's native character presentation is reproved here.

The fixed factors in \(K(u,at)\) produce a bounded fixed column vector,
including their original zeros. The operator's arbitrary-coefficient
quantifier makes its constant independent of these growing factors. This
does not extend a theorem for a fixed analytic twist to growing twists.
The arithmetic unit and bad-prime presentation classes must be split
finitely as in the existing physical transfer.

For \(k=\lambda^6k_0\), the exact character identity is
\[
 \chi_k(t)=\chi_{k_0}(t)\mathbf1_{(t,\lambda)=1}.
\]
For a fixed \(\lambda\), the extra zero factor is independent of
\(k_0\). It is removed only after the positive row square is formed.
The column norm bound is \(O(N^{-1}(\mathrm N\lambda)^{-6})\);
Minkowski then costs the convergent ideal series
\(\sum_\lambda(\mathrm N\lambda)^{-3}\). This proves the stated
kernel average with \(N^{-1}\mathscr B(H,N)\), including nonsquarefree
plain columns and every zero before positive enlargement.

## 2 Actual middle factors and endpoint summation

For fixed endpoints, their good radical has polynomial norm in \(U\).
The sixth-power-free middle row has only six possible valuations at each
endpoint-supported prime. Enumerating these fixed factors costs
\(6^{\omega(\operatorname{rad}_{\rm good}(uh))}\ll U^\varepsilon\),
along with bounded unit/bad-prime factors.

The exterior factor retains its full valuations. A physical cap on its
norm permits the low-row operator directly; squarefreeness is not required.
Squarefreeness is needed only when deducing that cap from the primitive
conductor ratio. Confusing the exterior radical with its physical norm
would invalidate the generalization to all comparable conductors.

The actual row weight is bounded by \(W\) on its selected subset before
either square sum is enlarged. Cauchy retains the two complete kernels.
The endpoint weights sum to at most \(A^2\), with no additional endpoint
or common-factor count. The exterior predicate is invariant under endpoint
reversal. Assigning it outside the six prior sectors gives a real disjoint
sector, without asserting that sector positivity follows from the Gram
matrix.

## 3 Exponent checks

For \(H=U^{103/200}\) and the operational plain lengths, the dominant
term in \(\mathscr B(H,N)\) is \(H^{5/6}N^{1/3}\). The exact reserve is
\[
 1-\frac{103}{240}-g-(4/3-2d)m-3s+2\mu.
\]
The lower envelope uses \(g\le d(1+r)/2\), \(\mu\ge0\),
\(d\le21/50\), \(r<73/100\), \(m<207/500\), and
\(s<101/500000\). Its derivative in \(d\) is
\(2m-(1+r)/2<0\), and it decreases with the other variables. The
coarse corner gives \(4031/1500000>0\).

At note 5's exact point, the reserve is
\(7362652673/507450000000\). For the original four-prime geometry,
its sharper exterior radius \(U^{1/2}\) gives
\(13705777673/507450000000\). The old \(0.2253834\) deficit was for
a different entrywise majorant; there is no contradiction with the new
operator bound or with sharpness of the old unweighted count.

The new uniform reserve exceeds the old smallest reserve \(19/12500\),
so the seven-cut error exponent remains \(T-19/12500\). Every prior
inequality remains in the exact complement, now with exterior norm
strictly exceeding \(U^{103/200}\). The displayed higher-valuation
support pattern checks that these algebraic restrictions do not force
an empty raw range. It makes no selected-bin or weight lower-bound claim.

## 4 Direct energy comparison

The direct marginal Hölder optimization has four vertices, not an
additional interpolated saving. Its envelope reproduces the existing
count, pair and count-plus-fourth estimates. At ideal continuous slot
capacity, the remaining deficit is
\(88651/1321484375\), approximately \(0.00006708441\). Whole-slot shortfall reduces the combined branch until the mass
branch dominates; the ideal value is not a claim
about the original mesh.

The scalar amplitude model saturates that envelope while respecting the
listed marginal inequalities. It is not an arithmetic character frame.
The high-response tail-mass criterion and the inverse-weighted fourth
criterion are correctly marked as sufficient new estimates. The fourth
criterion uses \(E^2\le A\sum w|S_m|^4\) and asks for extra saving
\(177302/1321484375\) at the ideal displayed point. No such arithmetic
correlation saving is proved.

## 5 Finite verification and remaining dependencies

The [checker](../numerics/check_mixed_middle_sieve.py) prints a deterministic
[small record](../numerics/mixed_middle_sieve_record_20261009.json).
Two fresh replays match byte for byte: **141,413 exact assertions**.
Its formal cyclotomic frames retain nontrivial sixth-power deletion masks.
It checks exact column decomposition, the fixed-coefficient expansion,
positive mask removal and Hilbert Cauchy, exterior valuation factorization,
cut complements and reversal, and rational sector/direct budgets.

These finite tests do not certify the infinite ideal sums, physical
reciprocity, presentation transfer, the source sieve theorem, selected-bin
population, analytic plain/inverse/family inputs, or the seven-cut signed
correlation. Analytic use requires the same fixed-parameter ordering and
uniform profile derivatives and polynomial height costs as the preceding
mixed notes. The present result remains a conditional sector estimate.
