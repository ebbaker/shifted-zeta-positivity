# Completed mean-square estimate review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel internal reviews used the inherited configuration. They are not
independent specialist validation or formal verification.

## Result and exact scope

The completed mean-square estimate `prop:R` closes in this internal audit
under the stated theta and quadratic large-sieve inputs. No unresolved
defect was identified in the exceptional local terms, moving-row
coefficient independence, sieve-family hypotheses, infinite recombination,
or passage from squarefree rows to all rows.

The audited conclusion is

\[
\sum_{0<N(k)\ll H}|T(X;k,f)|^2
\ll_{I,\xi,S,\varepsilon,C_0}
D^\varepsilon\|W\|_{C^J(I)}^2
\left(H+\frac{H^2N(f)}X\right),
\]

where \(1\le H,X,N(f)\le D^{C_0}\), \(f\) is squarefree and primary
with \((f,S)=1\), \(\xi\) is a fixed ray character, and \(W\) is
smooth and supported in a fixed compact interval
\(I\subset(0,\infty)\). \(T\) is the source's completed theta family;
this is not an estimate for arbitrary sextic coefficient sequences.

Source: the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
openai/math revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`,
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
All line references below are physical source lines. The proposition is
at 1317–1333; the quadratic interface and squarefree/general-row proof
are at 1886–2215. The local reflection, uniformity, and coefficient
inputs are at 1734–1868 and 3438–3451.

| Obligation | Checked conclusion | Derivation |
| --- | --- | --- |
| Every fixed-prime branch | \(a^2\le1\), \(a^2Y\ll H_0^2N(t)^2N(g)/X\), including \(t,g\) overlap | [Local branch ledger](../notes/COMPLETED_MEAN_SQUARE_LOCAL_LEDGER_20261012.md) |
| Primitive quadratic family | Unit correction, fixed-class reciprocity, product conductor, and finite \(S\)-column splitting meet the imported interface | [Sieve and summation](../notes/COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md) |
| Smooth row dependence | Common pointwise Mellin majorant; column squared norm \(O(a^2)\); no surviving cube-block length factor | [Sieve and summation](../notes/COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md) |
| Infinite blocks and ramified exponents | Summable dyadic and \(m\ge-4\) norms for every \(Y>0\), including \(Y<1\) | [Sieve and summation](../notes/COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md) |
| General rows | \(k=u_0sv^2\), \(g=fv^2\), exact \(N(v)^{-2}\) factor and convergent ideal sum | [General rows](../notes/COMPLETED_MEAN_SQUARE_GENERAL_ROWS_20261012.md) |

## Why the difficult terms fit the bound

For a \(j=4\) prime, the large local value splits into a constant term,
a squarefree-column collision, and a cube-factor collision. Reindexing
\(n=pn'\) changes the length from \(q^2Y\) to \(qY\); reindexing
\(b=pb'\) changes it to \(Y/q\) and leaves a factor \(q^{-1/2}\).
Their costs in \(a^2Y\) are \(q,q,q^{-2}\). The column mask
\(p\nmid n'\) preserves squarefreeness, and \(p\nmid n\) in the
cube branch ensures that simultaneous \(p\mid n,b\) is counted once.
The same substitutions commute at distinct exceptional primes, provided
all other coefficients are evaluated at the original substituted pair.
No multiplicativity of the cusp coefficient is assumed.

A prime dividing both \(t\) and \(g\) has odd exponent
\(1+4v_p(g)\pmod6\), so it has no exceptional zero or fourth-power
branch. It is charged once in the sharper local budget. A zero-exponent
prime has an inactive branch with scalar \(1-q^{-1}\) and no dual-column
exclusion, or an active branch with \(q^{-1/2}\) attenuation. Restoring
the original column exclusion after Fourier transformation would alter
the reflected expression.

After fixing the ray class, the cusp coefficient and additive phase are
independent of the moving squarefree row \(k_0\). Extracted quadratic
row phases remain bounded exterior scalars. This distinction permits
the sieve with arbitrary fixed column coefficients. Dual columns can
contain fixed \(S\)-primes, including the norm-4 prime above two; a
finite factorization of those column primes gives the required sieve
interface. The cubic theta coefficient at that prime does not extend
the original sextic denominator notation there.

The source's analytic cancellation input is
[Goldmakher–Louvel, arXiv:1112.1642v2](https://arxiv.org/html/1112.1642v2),
Definition 1 and Theorem 1.1. The primitive quadratic Hecke family is
obtained by the unit correction
\(\Xi_k(x)=(x/k)_2\kappa_\lambda(x)^{e_k}\), with
\(e_k=0,1\) according as \(N(k)\equiv1,3\pmod4\). Its conductor is
\(k\lambda^{e_k}\). For coprime indices in the same fixed ray class,
the primitive inducing product has conductor \(k_1k_2\), matching
the external paper's explicit Section 2 convention. That theorem's
proof remains imported; the audit checks its applicability here.

The Mellin bound is a common pointwise majorant over all rows, which
allows weighted Cauchy before summing the row energies. Both its decay
factors survive that step. Ideal counting gives
\(\sum_{N(n)\asymp U}|A(n,b)|^2/N(n)\ll a^2\) and
\(\sum_{N(b)\asymp B}N(b)^{-1}\ll1\). Dyadic recombination gives
\(O(\log^2(2+Y))\) for the row part and \(O(\sqrt Y)\) for
the column part. For \(Y<1\), direct large-argument decay closes the
same sums. The lower support bound \(m\ge-4\) makes the remaining
ramified sum geometric.

The raw length satisfies \(Y\ll H^2N(g)^2/X\ll D^{4C_0'}\)
in a generic squarefree-row range \(H,N(g)\le D^{C_0'}\), with \(C_0'=2C_0\) for the general-row application. Thus the sieve exponent, fixed-prime
branch counts, and logarithms consume a finite reserved \(D^\varepsilon\)
budget. A sufficient derivative order for this portion is \(J\ge18\),
using decay order three and two logarithmic derivatives in the earlier
theta kernel bound. No order increases with a dyadic block or moving row.

Finally, the decomposition \(k=u_0sv^2\) allows shared primes between
\(s\) and \(v\). The zero-extended identity moves the square part into
\(g=fv^2\). Applying the squarefree-row result with parameter range
\(2C_0\) produces exactly
\([H+H^2N(f)/X]/N(v)^2\). The ideal sum \(\sum_vN(v)^{-2}\)
converges; there is no additional count of \(v\).

## Reproducible finite checks

The [standalone checker](../numerics/check_completed_bookkeeping.py) and
[verified-source record](../numerics/completed_bookkeeping_record_20261012.json)
pass **198,323 exact assertions**, **zero floating comparisons**, and
eleven negative-control families. They include 7,776 actual Eisenstein
rows, 40 exact local reindexing sums, all valuation cases through 18 in
the local ledger, simultaneous three-prime products, polynomial length
bounds, and inverse-square normalization. Square norms are handled with
canonical rational arithmetic.

These are finite diagnostics of identities and bookkeeping. They do not
prove the theta transformation, the large sieve, or an unbounded estimate.
The assertion count includes repeated enumeration. The [CLI record](../numerics/completed_bookkeeping_cli_validation_20261012.json)
confirms source-mismatch rejection before output and portable execution
without a third-party file. The [replay guide](../numerics/README.md#completed-mean-square-bookkeeping)
gives the command, source verification, coverage, and limitations.

## Imports and next bounded obligation

This closes the completed mean-square audit within the stated imported
theta transformation, moving-prime uniformity, coefficient and weight
bounds, reciprocity, and quadratic large sieve. Earlier [theta](THETA_TRANSFORMATION_REVIEW_20261012.md)
and [initial Poisson/arithmetic](INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md)
reviews retain their original scopes and access limitations. No source
correction was needed for the inspected mean-square proof.

The canonical energy estimate and full quasi-RH theorem remain
unvalidated. The next bounded target is the full two-Poisson transfer
proposition beyond the [selected nonempty cube-tail branch](FIRST_BRANCH_REVIEW_20261012.md).
Cover every occupied branch and short-range case, preserving the
coefficient class, zero masks, diagonal/coherent terms, and coupled smooth
norms. Record the exact parameter decrease and terminating base case for
every admitted child. A successful completed-family estimate alone does
not validate that transfer or its final descent.
