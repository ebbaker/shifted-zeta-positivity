# First arithmetic source branch review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Parallel model read-throughs are internal checks, not independent specialist
validation or formal verification.

## Finding and scope

The first audit identifies a specific source of the claimed saving and a
strictly decreasing return mechanism. In the inspected argument, the theta
transformation changes the residual sextic row twist into a quadratic
twist. The quadratic large sieve bounds the completed sums; cube inversion
and two Poisson transformations return the remaining sums to the original
energy class. The second return relies on a signed divisor cancellation
that must occur before taking absolute values.

The extraction and recurrence bookkeeping pass this internal check
conditional on the stated arithmetic and analytic identities. This does
**not** establish the manuscript's zero-free theorem, the September 30
family baseline, or a stronger strip. Outstanding inputs include the full
October 5 theta transformation and its uniformity, the imported theta and
sieve theorems, and complete validation of the arithmetic identities and
initial Poisson reduction used by the source. The earlier local
September 30 audit is relevant evidence, not a substitute for comparing
the pinned versions or validating those inputs.

The source is the [October 5 manuscript at commit
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).
The manuscript date is October 5; the pinned repository revision is dated
October 8. [The provenance record](../notes/source_provenance_20261012.json)
records the exact URL, hash, size, and physical-line convention. No source
PDF or full third-party manuscript has been added to this repository.

Read the [dependency map and extraction](../notes/DEPENDENCY_MAP_AND_EXTRACTION_20261012.md)
and [cube-tail branch ledger](../notes/CUBE_TAIL_BRANCH_AUDIT_20261012.md)
for hypotheses and the transformations. This review records the source of
the completed estimate and the decision about further work.

## Where the saving enters

The canonical energy uses the special coefficients
\(a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n)\), squarefree
primary columns, and the zero-extended factors
\(\chi_n(k)\chi_n(f)^4\). It is not an arbitrary-coefficient sextic
large-sieve norm. Its completed version includes cubes in the precise
theta-coefficient normalization.

The following is a check of the composition in source Section 6, assuming
its Appendix A identities and kernel bounds. It identifies the analytic
input; it is not an independent proof of theta automorphy.

1. Split a squarefree row as \(s=tk_0\), with the primes of \(t\)
   dividing the auxiliary twist or the fixed excluded set. The remaining
   \(k_0\) is squarefree and coprime to both. The reflection's local
   exponent is \(-j-2\); consequently \(j=1\) gives
   \(B_{p,1}=\chi_p^3\), a quadratic character. The zero at a column
   divisible by \(p\) is retained. Source labels
   `eq:theta-local-factors`, `eq:residual-quadratic-factor`, physical
   lines 1731–1746 and 2005–2011.
2. `lem:reflection-uniformity` fixes the cusp data after splitting the
   moving rows into finitely many fixed ray classes. Only with this
   uniformity does the resulting coefficient profile become independent
   of \(k_0\). A bounded scalar may still depend on \(k_0\), and the
   smooth weight may depend on its norm; neither is silently treated as
   a fixed coefficient. Lines 1841–1853 and 1982–1998.
3. Exceptional \(j=4\) factors are split into a constant term, a prime
   dividing the squarefree column, and a prime dividing only its cube
   factor. If \(q=N(p)\), their changes to coefficient bound and length
   are
   \[
   (a^2,Y)\mapsto(a^2/q,q^2Y),\quad(a^2,qY),\quad(a^2/q,Y/q).
   \]
   The large local value is paid for by reindexing and normalization.
   The mask preserving squarefreeness is retained. These updates give
   \(a^2\le1\) and
   \(a^2Y\ll\mathcal H_0^2N(t)^2N(g)/X\), with
   \(\mathcal H_0=\mathcal H/N(t)\). Lines 2039–2101. The fixed factor
   27 in the coefficient bound is harmless and is not counted as a
   saving.
4. Mellin separation removes the dependence of the smooth weight on
   \(k_0\) before applying the quadratic sieve. For a fixed cube index
   and Mellin parameter, the squared coefficient norm is \(O(a^2)\),
   since the coefficients contain \(N(n)^{-1/2}\) on a dyadic shell.
   Goldmakher–Louvel supplies the factor \(\mathcal H_0+U\). Summing
   the decaying dyadic and ramified pieces gives
   \(D^\varepsilon a^2(\mathcal H_0+Y)\), hence the squarefree-row
   completed bound. Lines 2110–2185. The separation has a common
   integrable majorant, as required by Appendix B; a different
   unconstrained coefficient sequence is not chosen for each row.
5. General rows have a unique factorization \(k=u_0sv^2\) with
   squarefree \(s\). The identity
   \(T(X;u_0sv^2,f)=T(X;u_0s,fv^2)\), including its zeros,
   follows from \(8\equiv2\pmod6\). The resulting bound has a factor
   \(N(v)^{-2}\) in both terms. Summation costs the convergent
   \(\zeta_K(2)\), yielding
   \[
   \sum_{0<N(k)\le\mathcal H}|T(X;k,f)|^2
   \ll D^\varepsilon\|W\|_{C^J}^2
       \left(\mathcal H+\frac{\mathcal H^2N(f)}X\right).
   \]
   Lines 2188–2214. No cancellation estimate for principal Möbius sums
   is used at this step.

The external sieve's [Definition 1 and Theorem 1.1](https://arxiv.org/html/1112.1642v2#S1)
require primitive quadratic Hecke characters of trivial infinite type, a
finite-class reciprocity law, and the specified product conductor for
coprime same-class indices. They permit arbitrary complex squarefree
column coefficients. The source matches these requirements in
`lem:quadratic`; the earlier [interface audit](../../../../quasi-rh/quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md)
gives more detail. The theorem's full proof is still an import. The
[Dunn–Radziwiłł theta reference](https://arxiv.org/html/2109.07463v3)
likewise supplies deep inputs; its existence alone does not validate the
source's extension to every fixed ray twist and moving local mask.

## Why the return needs signed cancellation

After the second Poisson transformation set
\(r=tg/e\), \(f'=Cew\), and \(k'=deh\). All preimages of a fixed
\((r,f',k')\) have the same column scale and coupled kernel. At a prime
\(p\mid f'\), putting \(\delta=\mathbf1_{p\mid k'}\), their signed
multiplicity is
\[
(1+\delta)-\delta-(1-\delta)=\delta.
\]
Thus the sum is supported on \(f'\mid k'\), with the remaining
factor \(\tau(r)\). The first parentheses count placements in \(C\),
the next term placements in \(e\), and the last placements in \(w\).
This uses the enlarged intermediate form's full domain; prematurely
retaining extra first-Poisson restrictions would require a new argument.

For a dyadic block \(R\le N(r)<2R\), the child parameters are
\[
X'=\frac L{RF'},\qquad \Sigma'=\frac LR,\qquad
\mathcal H'=\frac{\mathcal H L}{\Sigma F R^2}.
\]
The divisibility restriction and the true bound on \(N(k')\) give
\(X'/N(j)\ge F\Sigma/\mathcal H\ge1\) for every \(j\mid r\).
This justifies removing the residual column exclusion by the exact
scale change \((X',F')\mapsto(X'/N(j),F'N(j))\).
Only after retaining the eligible \(r\) can positivity enlarge the
other ranges. Source `lem:second-transfer`, lines 2539–2639.

The [exact regrouping checker](../numerics/check_transfer_regrouping.py)
and its [record](../numerics/transfer_regrouping_record_20261012.json)
test this finite arithmetic mechanism and its scale bookkeeping. The
negative control takes absolute values before regrouping; terms with
\(f'\nmid k'\) then survive. These tests do not certify Poisson
summation, theta automorphy, smooth estimates, or an unbounded induction.

The recorded run and a separate replay pass 729 regrouping cases, 4,913
preimage normalization checks, and 65 child exclusion checks. The checker
also verifies the selected norm-7 branch's rational scale and Fourier
support inequalities. The pinned source hash was verified on both runs.
The analytic nonzero-profile and cutoff arguments are in the branch
ledger; the checker does not replace them with floating-point sampling.

## Decision and remaining obligations

There is a justified next audit target: compare the October 5
`lem:reflection`, `lem:reflection-uniformity`, and `lem:theta-bounds`
against their complete Appendix A proofs and the primary theta formulas,
with explicit version correspondence to the September 30 checks. In
particular retain the active cusp denominator, the conjugated cusp
coefficients, zero-exponent masks, and prime-uniform kernel seminorms.
The full initial Poisson reduction also needs its own complete ledger
before promoting the whole theorem.

The selected branch does not require downstream exponent optimization.
Its return mechanism closes under the stated identities; no precise
proof defect has been established in this first audit. Further work should
address the remaining analytic inputs and other branches. An internal
successful branch is evidence about that branch, not independent
validation of the full claimed quasi-RH result.

Follow-up on 12 October 2026: the [theta transformation and uniformity
audit](THETA_TRANSFORMATION_REVIEW_20261012.md) now addresses the next
target identified above. Its version comparison, proof clarifications,
and remaining imports are recorded separately from this first branch audit.
