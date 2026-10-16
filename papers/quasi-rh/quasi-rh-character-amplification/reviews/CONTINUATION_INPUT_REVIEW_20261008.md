# Scoped review of inputs for the selector-feasibility continuation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This is a fresh same-model review of the elementary ideal-pair argument and
the source hypotheses relevant to the selector test. It is not specialist
refereeing or formal verification. The reviewed September 30 companion
[preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
has verified PDF SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Its deep analytic results and global assertion `beta_* <= 7/8` remain
assumptions here. No Lean proof was replayed.

## Elementary pair count: no defect found

The argument at manuscript label `lem:pair-count` proves the stated
`O_epsilon(X V^(1/2+epsilon))` bound. After removing the ideal gcd, the
residual ideals are coprime. Extracting their sixth powers uniquely leaves
at each prime of the ratio conductor two possible sides and five possible
nonzero exponents. For a fixed conductor and allocation, the ideal gcd
count is bounded by

\[
\frac{C X}{\max\{\mathrm N a_0(\mathrm N a)^6,
                         \mathrm N b_0(\mathrm N b)^6\}}
\le \frac{C X}{\sqrt{\mathrm N(a_0b_0)}(\mathrm N(ab))^3}.
\]

The two unrestricted sixth-power-label sums converge at exponent three.
Also `N(a_0 b_0) >= N f`, and
`10^omega(f) <<_epsilon (N f)^epsilon`. Ideal counting and partial
summation give the claimed conductor sum. This includes `f = 1` and
requires no positive lower norm bound on the columns. If the permitted
gcd norm is below one, its actual count is zero. Dropping coprimality
conditions only enlarges the positive majorant. The additional zero mask
at primes of canceled phase does not change this count and is correctly
retained elsewhere in the manuscript.

## Imported statements: hypotheses that remain necessary

- **Lemma 17.1, PDF pp. 114–115:** the marked inverse norm is over all
  element rows, so restriction of this positive norm is legal. Its common
  presentation, common orientation, row-independent prime supports and
  coefficients, fixed slot count, smooth profiles, and both strict width
  inequalities match the stated manuscript setting. Appending an arbitrary
  plain polynomial is not licensed by this theorem.
- **Lemmas 8.1–8.2, PDF pp. 55–58:** the primitive conductor factor before
  replacing it by the physical row scale is
  `Q_psi^(a-1/2+6e)`. On the manuscript's box, the reflected line remains
  strictly in `Re s > 0`, so Lemma 4.10 bounds the actual deleted Euler
  product by an arbitrarily small power of its polynomial-size radical.
  The conductor-sensitive plain estimate is therefore a valid conditional
  refinement, with the original buffered height allowance and finite-height
  tails. Nonprincipality is essential for that plain contour shift.
- **Lemma 18.3, PDF pp. 176–177:** a plain smooth sum with a fixed ray
  character and polynomial-size squarefree coprimality mask has its stated
  scale-independent residue coefficient and absolute error
  `O_epsilon(U^epsilon (1+|t|)^J)`. This evaluates the plain factor in the
  sixth-power test. It says nothing about a prime-slot main term and does
  not turn an inverse/plain rectangle into the source's two-plain-sum
  cancellation.

Numbering precaution: the global reciprocal estimate in this PDF is
**Lemma 4.9**, together with deleted Euler factors in **Lemma 4.10**.
Lemma 4.6 is the Gaussian annular decomposition.

## The masked principal inverse bound is available conditionally

In the principal-twist case, let `R` be the squarefree radical containing
the fixed exclusions and the primes dividing the sixth root `a`. For
`N R <= U^B`, with fixed `B`, define

\[
M^{(a)}(D)=D^{-1/2}
 \sum_{(d,R)=1}\mu_F(d) A(\mathrm N d/D).
\]

For `Re s > 1` its Dirichlet series is exactly

\[
F_R(s)=\zeta_F(s)^{-1}
           \prod_{p\mid R}(1-(\mathrm N p)^{-s})^{-1}.
\]

Assume the source's global `beta_* <= 7/8`. For any fixed positive `v`,
Lemma 4.9 bounds the reciprocal on `Re s >= 7/8+v`, and Lemma 4.10 bounds
the inverse deleted product by `(N R)^epsilon`, uniformly in height.
The reciprocal has a zero, not a pole, at the principal pole `s = 1`.
Smooth Mellin inversion can therefore be shifted to `Re s = 7/8+v`.
After choosing the subsidiary losses and `v` sufficiently small, it gives

\[
|M^{(a)}(D)|^2
 \ll_\epsilon D^{3/4+\epsilon}U^\epsilon(1+T_1)^{A_0}.
\]

This is uniform for the manuscript's uniformly smooth annular profiles,
including the actual smooth truncated-inverse cutoff when it has those
seminorm bounds. Pure norm twists have a fixed polynomial height cost;
the required derivative profiles must satisfy the same finite seminorm
conditions. A sharp nonsmooth cutoff or arbitrary arithmetic coefficients
cannot be inserted under this assertion. In the sixth-power dyad
`N a \asymp U^(1/6)`, the moving radical has the required polynomial bound.

## What this does and does not settle for enlargement

There is exactly one row `a^6` for each nonzero integral ideal `(a)` in
this class-number-one field: the six unit choices of generator have the
same sixth power, and equality of sixth powers identifies precisely those
choices. Thus the extracted subfamily is an ideal sum, with no extra
factor six. Its size is `O(U^(1/6))`.

For these rows Lemma 18.3 gives the normalized plain factor

\[
S_m^{(a)}
=c_{\mathcal S}\prod_{\substack{p\mid a\\p\notin\mathcal S}}
 (1-(\mathrm Np)^{-1})\,N^{1/2}\int_0^\infty B(y)\,dy
 +O_\epsilon(N^{-1/2}U^\epsilon(1+T_1)^J),
\]

where the positive fixed constant `c_S` incorporates the ideal-density
normalization and fixed exclusions. The integral includes the actual norm
twist and may vanish. Each prime factor remains its exact masked finite
sum. Its actual coefficients and support may cancel; a positive principal
main term cannot be asserted merely because the row is a sixth power.

Using only the uniform upper bounds `|S|^2 << U^m` and
`|Q_I|^2 << U^z`, the conditional inverse estimate above bounds this
subfamily by

\[
U^{1/6+3r/4+m+z+\epsilon}(1+T_1)^{A_0}.
\]

At `z=(1-r)/2-rho`, its excess over the requested exponent
`K=1+delta*m-1/5000` is

\[
\frac r4+(1-\delta)m-\frac13+\frac1{5000}-\rho.
\]

The expression before `-rho` ranges from `19/375` to `1289/7500` on
the full rectangular box. Thus this available bound does not close the
near-capacity sixth-power test. This is an upper-bound budget deficit,
not a lower bound for the actual norm, and not a disproof of either the
restricted target or a complete-family estimate. Actual vanishing or
small profile factors could improve this diagnostic. A principal main
term claim for the prime slots would require their actual data and a
justified distribution statement. Controlling this one subfamily alone
would also not control every row introduced by a complete-family
enlargement.

The elementary input and the conditional principal inverse estimate pass
this scoped check. Specialist validation of the imported machinery remains
outstanding; the new mixed saving remains unproved.

## Additional scoped review: moving the live divisor into the label

Reviewed [LIVE_DIVISOR_TRANSFORM_20261008.md](../notes/LIVE_DIVISOR_TRANSFORM_20261008.md)
against source equations (17.72), (17.74)–(17.85), and the coefficient
conditions of Lemma 17.2. No algebraic error was found in the squarefree,
mutually coprime calculation. The following checks are specific to that
formal complete-family branch; they do not settle the selector gate.

1. Set the other character arguments in source (17.72) to one. On
   coprime squarefree arguments it gives exactly
   `A_*(qe)=A_*(q)A_*(e) chi_e(q)^4`. Multiplicativity of the
   zero-extended symbols then proves the note's (8). The scalar
   `chi_q(y)` retains its numerator zeros, while `chi_e(gq)^4` excludes
   overlap of the new residual column with both factors of the enlarged
   label. The fixed puncture remains at `t`.
2. The canonical coefficient can be recovered at a **fixed common
   separating mode**. Because the plain divisor is coprime to all
   physical prime slots, every still-live slot lies in `e`, with its
   original coefficient and support. Its sign `mu(P_n)` factors into
   the individual prime coefficients. The residual polynomial can thus
   have the form

   \[
   R_{\widetilde g}(y)=\sum_{e\ {\rm sf}}
   A_*(e)1_{(e,t)=1}\chi_e(y)\chi_e(\widetilde g)^4
   d_\xi(e)\omega_e(\mathrm Ne/U^{R-\lambda})
   (\mathrm Ne/U^{R-\lambda})^{i\xi_e},
   \]

   where the product-form mark `d_xi` and smooth profile are independent
   of the current `g,q,y`. This requires a joint compact profile in the
   independent normalized coordinates, including `q,e,k_0` and the
   individual slot norms, chosen before their arithmetic values are
   evaluated. The original coupled cutoffs must remain in that profile.
   Their inversion restores the identity before positive enlargement;
   selecting a new measure for each `g,q` would invalidate this argument.
3. In the positive Cauchy inequality, counting possible `q` costs
   `U^(lambda+epsilon)` once. Thereafter `(g,q) -> gq` has at most a
   divisor number of preimages, not another independent length count.
   The previously frozen divisor choices also divide `t*gq` and only
   alter fixed divisor powers. Bounded scalar phases and zeros may be
   dropped at this positive stage. No second `U^lambda` cost is justified.
4. Source (17.82) has unnormalized squared energy `H=U^F E`, and its
   claimed baseline is `E << U^(F+epsilon)`. Moving `q` from the residual
   column to the averaged label leaves `F` unchanged. The normalized
   inverse roots stay in the common smooth profile and are not additional
   powers of `U`. Source (17.83)–(17.86) give
   `kappa+beta+2F=1`, so the hypothetical bound after the live-divisor
   Cauchy step has exponent `1+lambda`. For unequal sides the geometric
   mean gives `1+(lambda_1+lambda_2)/2`.
5. The resulting first canonical margin is `1-L-z_n`, independent of
   `lambda`, and is at most `1-r-m <= -3/50` on the box. Thus recovering
   the coefficient class does not make Lemma 17.2 applicable. The endpoint
   excess `(1-delta)m+1/5000` ranges from `209/1000` to `1601/5000`.

The recovered coefficient structure is a useful partial identity. Neither
the common-profile separation, the divisor reindexing, nor these width
calculations prove cancellation, control the full broadened canonical
family, or transport the original exceptional-row selector through
Poisson summation. They do not upgrade the unproved mixed saving.
