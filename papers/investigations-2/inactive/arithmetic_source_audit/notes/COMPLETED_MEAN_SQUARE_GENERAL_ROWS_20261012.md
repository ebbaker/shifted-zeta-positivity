# General rows in the completed mean square

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical review, not independent specialist
validation or formal verification.

## Source, hypotheses, and finding

Source: the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
openai/math revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`,
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Physical lines 2188–2215 prove `prop:R` from
`lem:squarefree-completed`; the proposition is at lines 1317–1333.

The squarefree-row estimate allows any nonzero auxiliary twist \(g\),
including repeated prime factors, primes in \(S\), and nonprimary chosen
generators. With a fixed unit \(u_0\), it gives

\[
\sum_{\substack{0<N(s)\le H_0\\s\ {\rm squarefree}}}
 |T(X;u_0s,g)|^2
 \ll D^\varepsilon\|W\|_{C^J(I)}^2
 \left(H_0+\frac{H_0^2N(g)}X\right)
\]

when \(1\le H_0,X,N(g)\le D^{C_0'}\), with constants depending on
\(I,\xi,S,\varepsilon,C_0'\). The [local ledger](COMPLETED_MEAN_SQUARE_LOCAL_LEDGER_20261012.md)
and [sieve and summation note](COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md)
audit this input under the stated theta and quadratic-sieve imports.

**Finding:** the passage to general rows preserves all character zero
extensions and gives exactly the summable factor \(N(v)^{-2}\).
There is no coprimality condition between the squarefree part and the
square part, and no extra conductor or counting loss is needed.

## Unique decomposition, including shared primes

Use the source's multiplicative choice of one generator for each integral
ideal of the Eisenstein field. At each prime, write the valuation uniquely
as \(r=\epsilon+2a\), with \(\epsilon\in\{0,1\}\) and \(a\ge0\).
Every nonzero element then has the unique expression

\[
k=u_0sv^2,\qquad s\text{ squarefree},\quad u_0\in\mathcal O^\times,
\]

with \(s,v\) chosen ideal generators. The six units are counted only in
\(u_0\). If a prime has valuation three, it divides both \(s\) and \(v\).
Imposing \(\gcd(s,v)=1\) would therefore discard valid rows.
This decomposition includes the fixed excluded primes and the ramified
prime above three; no primary residue-symbol formula at those primes is
required for the decomposition itself.

For a column \(n\) away from \(S\), complete multiplicativity and
\(8\equiv2\pmod6\) give

\[
\chi_n(u_0sv^2)\chi_n(f)^4
=\chi_n(u_0s)\chi_n(fv^2)^4.
\]

This identity also holds at zero values. If a prime of \(n\) divides
\(s\), \(f\), or \(v\), the appropriate factor makes both sides zero;
otherwise all relevant factors are sixth roots of unity and the exponent
congruence applies. No division by a vanishing value is used. For a column
meeting \(S\), both completed twists are zero by their prescribed
extension. Thus the identity allows \(v\) and \(g=fv^2\) to meet \(S\)
and to have nonprimary chosen generators.

The defining twists agree on every column. Their completed theta sums
therefore agree, including any multiplicative cube factors in that
definition:

\[
T(X;u_0sv^2,f)=T(X;u_0s,fv^2).
\]

## Parameter ranges and exact normalization

Assume the proposition's hypotheses:
\(1\le H,X,N(f)\le D^{C_0}\), \(f\) squarefree and primary with
\((f,S)=1\), fixed ray character \(\xi\), and smooth \(W\) supported
in the fixed compact interval \(I\subset(0,\infty)\).
For a fixed \(v\) occurring among \(N(k)\le H\), set

\[
H_v=H/N(v)^2,\qquad g=fv^2.
\]

Then \(H_v\ge1\), \(N(g)=N(f)N(v)^2\le HN(f)\le D^{2C_0}\),
and \(H_v,X\le D^{2C_0}\). Apply the squarefree-row lemma with
\(C_0'=2C_0\), which changes only the permitted fixed constants and
derivative order. Its main term is precisely

\[
H_v+\frac{H_v^2N(g)}X
=\frac{1}{N(v)^2}
 \left(H+\frac{H^2N(f)}X\right).
\]

Summing over \(v\) gives

\[
\sum_{0<N(k)\le H}|T(X;k,f)|^2
\ll D^\varepsilon\|W\|_{C^J(I)}^2
 \left(H+\frac{H^2N(f)}X\right)
 \sum_v N(v)^{-2}.
\]

The sum uses one chosen generator per ideal. Eisenstein lattice counting
gives \(O(R)\) ideals of norm at most \(R\). In the norm annulus
\([2^j,2^{j+1})\), the weighted sum is consequently \(O(2^{-j})\).
Hence \(\sum_vN(v)^{-2}<\infty\); it is \(\zeta_K(2)\).
The six units contribute a fixed factor. A row cutoff \(N(k)\ll H\)
is handled by replacing \(H\) by its fixed constant multiple in the
same estimate. This proves the proposition's general-row conclusion
once the audited squarefree-row input is granted.

The auxiliary length remains polynomial during that input's proof:

\[
Y\ll H_0^2N(\operatorname{rad}(tg))^2/X
\le H^2N(g)^2/X.
\]

For its generic range \(H,N(g)\le D^{C_0'}\), this is at most a
fixed constant times \(D^{4C_0'}\). The general-row substitution uses
\(C_0'=2C_0\); it does not require a uniform constant for twists outside
the declared polynomial range.

## Exact diagnostic record

[check_completed_bookkeeping.py](../numerics/check_completed_bookkeeping.py)
uses only the Python standard library. The [verified-source record](../numerics/completed_bookkeeping_record_20261012.json)
passes **198,323 exact assertions**, with **zero floating comparisons**
and eleven negative-control families. Coverage includes:

- 7,776 actual Eisenstein elements, all six units and valuations 0–5 at
  primes of norms 7, 13, 4, and 3; actual sextic characters for denominator
  norms 7, 13, and 91; and the explicit \(S\)-column zero extension.
- 40 exact finite \(j=4\) reindexing sums at norms 7, 13, 19, 25, and 121,
  with a fixed nonconstant rational coefficient profile and a rational test weight. Square
  norms use canonical rational arithmetic; the other norms use
  \(\mathbb Q(\sqrt q)\).
- Every local branch for \(t\)-valuation 0/1 and \(g\)-valuations 0–18 at
  four norms, 216 simultaneous three-prime worst-case products, the
  polynomial length bound, and the inverse-square normalization.

Negative controls detect omitted collision masks or attenuation,
incorrect length updates, the erroneous restriction \((s,v)=1\), use of
\(fv\) instead of \(fv^2\), discarded character zeros, and a spurious
\(N(v)^{-1}\) factor. Assertion totals include repeated enumerations;
they are not counts of independent theorem validations.

The [CLI validation record](../numerics/completed_bookkeeping_cli_validation_20261012.json)
also records rejection of a supplied source with the wrong hash before
any arithmetic or output, and successful portable execution without a
source file. A no-source run explicitly records
`source_hash_verified=false`. See the [replay guide](../numerics/README.md#completed-mean-square-bookkeeping).

These diagnostics check finite identities and normalization. The
unbounded row identity and inverse-square convergence are the analytical
arguments above; theta automorphy, reflection uniformity, transformed
weight bounds, and the quadratic large-sieve theorem remain the stated
imports. The [combined review](../reviews/COMPLETED_MEAN_SQUARE_REVIEW_20261012.md)
records the resulting scoped conclusion and next obligation.
