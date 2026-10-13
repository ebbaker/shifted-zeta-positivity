# Completed mean square local branch ledger

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical read-through, not independent specialist
validation or formal verification.

## Source, scope, and result

Source: the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
`build/paper2.tex` at openai/math revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The source hash
is `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
All source line numbers below use the physical lines of these exact bytes.

The audited part is the squarefree-row local calculation in
`lem:squarefree-completed`, lines 1934–2110, using the reflection local
factors (1734–1746), fixed-ray uniformity (1839–1855 and 3438–3451),
support/coefficient bounds (1859–1868), and the exact local Fourier
transform (3230–3279). The prior theta cusp and primary-source audits
were read as bounded input records, not blanket validation.

**Finding:** all active/inactive branches and simultaneous exceptional
prime collisions preserve the required quadratic-row form and give the
stated auxiliary-conductor bound. In particular, a prime dividing both
the squarefree bad row part \(t\) and \(g\) has odd local exponent and
never enters an exceptional \(j=0\) or \(j=4\) branch. The \(j=4\)
split correctly counts a prime dividing both the squarefree column and
the cube factor once. No arithmetic overlap error or moving coefficient
dependence was identified in these inspected steps.

This is conditional on the reflection identity, its fixed-family
uniformity and theta coefficient/kernel inputs. The quadratic sieve and
the [Mellin and dyadic summation](COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md)
are companion parts of the completed mean-square audit.

## 1. Row decomposition and local exponents

The lemma allows arbitrary \(g\ne0\) and a unit \(u_0\). For each
squarefree ideal row, choose its multiplicative generator and write

\[
s=tk_0,\qquad
t=\prod_{\substack{p\mid s\\p\mid g\text{ or }p\in S}}p,
\qquad \mathcal H_0=\mathcal H/N(t).
\]

Then \(k_0\) is squarefree, primary and prime to \(gS\). A nonempty
range has \(\mathcal H_0\ge1\). The choices of \(t\) lie among divisors
of \(\operatorname{rad}(g\prod_{p\in S}p)\), so their number is
divisor bounded in \(g\), with a fixed factor from \(S\).

For a prime \(p\notin S\), sextic reciprocity transforms the original
factor \(\chi_n(u_0tk_0)\chi_n(g)^4\) into a factor on the column
variable with exponent

\[
j_p\equiv v_p(u_0tk_0)+4v_p(g)\pmod6,
\qquad 0\le j_p\le5.
\]

Its zero extension survives even when this exponent is zero:
\(\chi_p^0(n)=\mathbf1_{p\nmid n}\). The reciprocity sign from the
fourth power of the \(g\)-factor is 1 because \(\mathcal R^4=1\).
The remaining reciprocity sign, factors at \(S\), and unit factors
form \(\Psi_0\). Exponents at \(S\) are relevant only modulo six.
The sign \(n\mapsto\mathcal R(n,\prod_{p\notin S}p^{v_p(k)})\)
depends on a fixed ray class. Thus \(\Psi_0\) lies in a fixed finite
family. A unit factor in \(g\) is absorbed here; it does not create a
moving prime in the fixed modulus.

There are three disjoint cases away from \(S\):

| Prime position | Local exponent | Activity and role |
| --- | --- | --- |
| \(p\mid k_0\) | \(j_p=1\) | Forced active; residual quadratic row factor |
| \(p\mid t\) | \(j_p=1+4r\), \(r=v_p(g)\ge0\) | Always odd, hence forced active and nonexceptional |
| \(p\mid g\), \(p\nmid t\) | \(j_p=4r\), \(r\ge1\) | \(0,4,2\) for \(r\equiv0,1,2\pmod3\) |

For the middle case, the exponents are \(1,5,3\) for
\(r\equiv0,1,2\pmod3\), respectively. This explicitly covers
\(p\mid t\) and \(p\mid g\); no second local factor for the same
prime should be introduced.

## 2. Active versus inactive zero-exponent branches

The local finite Fourier coefficient for \(j=0\) is
\(1-q^{-1}\) at frequency zero and \(-q^{-1}\) at nonzero frequency,
where \(q=N(p)\). Therefore a zero-exponent prime has exactly two
allowed branches:

- Inactive: scalar \(1-q^{-1}\), no prime in the reduced denominator,
  and no transformed column mask at this prime.
- Active: the prime enters the reduced denominator, contributing
  \(q^2\) to its squared norm, and
  \(B_{p,0}(x)=q^{-1/2}\chi_p(x)^{-2}\).

The active factor vanishes when \(p\mid x\). The inactive factor does
not retain an original \(p\)-coprimality restriction on the transformed
column: the Fourier transform has already redistributed that original
mask. Keeping such an extra exclusion would change the exact reflection
formula.

Every nonzero \(j\) is forced active, because its zero-frequency Fourier
coefficient vanishes. In particular there are no active/inactive choices
for primes dividing \(k_0\). After fixing the active subset of the other
primes, the denominator is \(c=c_*k_0\), with
\(c_*=c_0\prod_{p\in\mathcal A_{\rm fix}}p\).

The reflection uniformity input says that, after partitioning \(k_0\)
into finitely many fixed ray classes, \(d,\psi,c_0\) are fixed for each
index. Its proof does not replace the moving denominator by fixed data:
\(N(k_0)^2\) remains explicitly in the weight.

## 3. Quadratic row dependence and the base coefficient

The theta support uniquely writes a frequency as
\(\ell=u\lambda^mnb^3\), with \(u\) a unit, \(m\ge-4\),
\(n,b\) primary, and \(n\) squarefree. No condition \((n,b)=1\) is
imposed. The exponents away from \(\lambda\) are of the form
\(3v_p(b)\) or \(1+3v_p(b)\), so the representation is unique.

For a prime dividing \(k_0\), the transformed exponent is
\(-j-2=-3\equiv3\pmod6\). Thus

\[
B_{p,1}(u\lambda^{m+4}nb^3)
=\chi_p(u\lambda^{m+4})^3\chi_p(nb)^3.
\]

This equality also holds when \(p\mid n\) or \(p\mid b\): both
sides vanish. It uses \(9\equiv3\pmod6\) on the cube factor; it does
not erase its zero extension. Since \(k_0\) is prime to all fixed active
primes and \(\lambda\), the unit/ramified row factor has modulus 1.

Set

\[
A_{u,m}(n,b)=
\frac{d(u\lambda^mnb^3)\alpha(u\lambda^mnb^3)
\psi(u\lambda^{m+4}nb^3)}{3^{m/6}\sqrt{N(b)}}.
\]

The coefficient bound gives \(|A_{u,m}|\le27\), and it is independent
of \(k_0\) in the fixed sector. Dividing \(d\) by
\(\sqrt{N(\ell)}\) gives the exact remaining denominator
\(3^{m/3}\sqrt{N(n)}N(b)\). The prepared sum has form

\[
\mathscr S_m[A,Y](k_0)=
\sum_{n,b}
\frac{A(n,b)\chi_{k_0}(nb)^3}
{3^{m/3}\sqrt{N(n)}N(b)}
V_*^\sharp\!\left(
\frac{3^mN(n)N(b)^3\mathcal H_0^2}{YN(k_0)^2}\right),
\]

with base \(Y=N(c_0)^2\mathcal H_0^2/X\). The constant 27 is an
absolute coefficient bound and supplies no cancellation saving.

After reflection the columns may contain primes in \(S\). Restrictions
must be those actually present in \(d\) and the transformed factors.
The original \((nb,S)=1\) cannot simply be reimposed. The sieve permits
the resulting squarefree column coefficients with primes in \(S\),
after the fixed-prime factorization in its stated interface.

In particular, a squarefree \(n\) may contain the norm-4 prime above 2;
squarefree here refers to ideal prime exponents and does not require the
rational integer \(N(n)\) to be squarefree. The theta coefficient bound
uses a cubic Gauss sum at this prime, which is legitimate over the
residue field of size 4. It does not extend the original sextic residue
notation to that prime. Primary \(n\) is prime to the prime above 3, so
the only unavoidable exclusion from being primary is the ramified prime
above 3. The fixed-\(S\) factor splitting in the quadratic sieve handles
the remaining allowed \(S\)-primes. A growing prime dividing \(g\) is
never absorbed into \(S\); its explicit local factor and conductor cost
remain in the ledger.

## 4. A single exceptional \(j=4\) collision, including overlap

For \(p\notin S\), \(p\nmid k_0\), write \(q=N(p)\). Since
\(p\nmid u\lambda^{m+4}\),

\[
\begin{aligned}
B_{p,4}(u\lambda^{m+4}nb^3)
&=q^{-1/2}(-1+q\mathbf1_{p\mid nb})\\
&=-q^{-1/2}
  +q^{1/2}\mathbf1_{p\mid n}
  +q^{1/2}\mathbf1_{p\nmid n,\,p\mid b}.
\end{aligned}
\]

If \(p\mid n\) and \(p\mid b\), the second term applies and the
third does not. Its total is \(q^{-1/2}(q-1)\), which is exactly the
original Ramanujan value. This overlap is therefore counted once.

Let \(A^{(p)}\) contain the base coefficient and all other factors.
The \(p\mid n\) term uses \(n=pn'\), giving

\[
A^{(p,n)}(n',b)=\mathbf1_{p\nmid n'}A^{(p)}(pn',b).
\]

The mask \(p\nmid n'\) is necessary and sufficient to preserve
squarefreeness. There is no exclusion at \(b\) in this branch. The
factor \(q^{1/2}\) cancels \(\sqrt q\) in the denominator, the row
factor extracts \(\chi_{k_0}(p)^3\), and the scale changes from
\(q^2Y\) to \(qY\).

The \(p\nmid n,p\mid b\) term uses \(b=pb'\), giving

\[
A^{(p,b)}(n,b')=\mathbf1_{p\nmid n}A^{(p)}(n,pb').
\]

Here \(b'\) is unrestricted at \(p\): higher powers in the original
cube factor are allowed. The denominator \(N(b)\) leaves
\(q^{-1/2}\); the row phase is again \(\chi_{k_0}(p)^3\), and the
scale becomes \(Y/q\). The three terms are exactly

\[
\begin{aligned}
\mathscr S_m[A^{(p)}B_{p,4},q^2Y]
={}&-q^{-1/2}\mathscr S_m[A^{(p)},q^2Y]\\
&+\chi_{k_0}(p)^3\mathscr S_m[A^{(p,n)},qY]\\
&+q^{-1/2}\chi_{k_0}(p)^3
\mathscr S_m[A^{(p,b)},Y/q].
\end{aligned}
\]

The extracted row phases have modulus 1, because \((p,k_0)=1\).
They belong in the permitted bounded exterior scalar, rather than in a
coefficient sequence which is asserted independent of \(k_0\).

## 5. Simultaneous exceptional primes

Let \(E\) be the set of fixed active primes with \(j=4\). Choose a
partition \(E=E_C\sqcup E_N\sqcup E_B\), for constant, squarefree
column and cube-factor branches. Define primary products
\(P_N=\prod_{p\in E_N}p\), \(P_B=\prod_{p\in E_B}p\).
The simultaneous reindexing is

\[
n=P_Nn',\qquad b=P_Bb',\qquad
n'\text{ squarefree},\quad (n',P_NP_B)=1.
\]

There is no corresponding \((b',P_NP_B)=1\) restriction. A prime in
\(E_N\) can also divide \(b'\), allowing the overlap already assigned
to its \(n\)-branch; a prime in \(E_B\) can divide \(b'\) again,
allowing arbitrarily high cube exponents.

All other coefficient restrictions are evaluated at the original pair
\((P_Nn',P_Bb')\), not at the unreindexed pair. The coefficient is
therefore the original bounded function at that pair, times these
explicit zero masks and the remaining local character factors. Because
the primes are distinct, inserting one is a unit at every other prime.
Consequently divisibility masks commute with this substitution; a
nonexceptional local character gains only a fixed unit phase. The cusp
coefficient \(d\) need not be multiplicative for this argument: its
uniform magnitude bound still applies at the reindexed pair.

The row-dependent scalar acquires
\(\chi_{k_0}(P_NP_B)^3\), of modulus 1. It introduces no moving column
profile. If \(Y_0\) includes the nonexceptional active primes, the
exceptional primes contribute

\[
Y_{\rm new}=Y_0
\prod_{p\in E_C}q_p^2
\prod_{p\in E_N}q_p
\prod_{p\in E_B}q_p^{-1},
\]

and their squared coefficient bound contributes
\(\prod_{p\in E_C\cup E_B}q_p^{-1}\). The sign is
\((-1)^{|E_C|}\). These formulas follow by expanding the finite product
of the exact three-term local identities; absolute convergence of the
theta series permits their use inside the sum.

## 6. Complete coefficient and length ledger

Track \(|A|\le27a\) and scale \(Y\), starting with
\(a^2=1\), \(Y=N(c_0)^2\mathcal H_0^2/X\).

| Local branch | New \(a^2\) | New \(Y\) | Multiplier in \(a^2Y\) |
| --- | --- | --- | --- |
| Nonexceptional active \(j\in\{1,2,3,5\}\) | \(a^2\) | \(q^2Y\) | \(q^2\) |
| Inactive \(j=0\) | \(\le a^2\) | \(Y\) | \(\le1\) |
| Active \(j=0\) | \(a^2/q\) | \(q^2Y\) | \(q\) |
| \(j=4\), constant branch | \(a^2/q\) | \(q^2Y\) | \(q\) |
| \(j=4\), squarefree-column branch | \(a^2\) | \(qY\) | \(q\) |
| \(j=4\), cube-factor branch | \(a^2/q\) | \(Y/q\) | \(q^{-2}\) |

All coefficient bounds satisfy \(a^2\le1\). For \(p\mid t\), the
exponent is odd, so \(a^2Y\) costs \(q^2\). For \(p\mid g\) but
\(p\nmid t\):

- \(r\equiv0\pmod3\) gives \(j=0\). The cost is at most \(q\),
  or at most 1 in its inactive branch. Since \(r\ge3\), either is
  bounded by \(q^r\).
- \(r\equiv1\pmod3\) gives \(j=4\). Every branch costs at most
  \(q\le q^r\).
- \(r\equiv2\pmod3\) gives \(j=2\). The cost is \(q^2\), and
  \(r\ge2\), so it is again at most \(q^r\).

Hence, simultaneously at every prime and without assuming disjoint
supports of \(t\) and \(g\),

\[
\begin{aligned}
a^2Y
&\le C_{\xi,S}\frac{\mathcal H_0^2}{X}
\prod_{\substack{p\mid t\\p\notin S}}N(p)^2
\prod_{\substack{p\mid g\\p\nmid t,\ p\notin S}}N(p)^{v_p(g)}\\
&\le C_{\xi,S}\frac{\mathcal H_0^2N(t)^2N(g)}{X}.
\end{aligned}
\]

The primes dividing both \(t\) and \(g\) enter only the first product;
the final upper bound simply allows the unused extra factors from
\(N(g)\). Primes in \(S\) cause bounded fixed-denominator data and no
unbounded conductor cost. Their positive norm factors on the right cause
no difficulty.

Every scale update is independent of \(m\) and \(k_0\). The index
counts one fixed theta/Fourier sector, a unit, an active/inactive choice
at each zero-exponent fixed prime, and at most three branches at each
exceptional fixed prime. It is divisor bounded in \(tg\), hence
\(D^\varepsilon\) within the stated polynomial norm ranges. The
uniformity lemma ensures that the moving primes of \(k_0\) create no
additional binary choices. This is the required finite decomposition
into prepared sums with fixed coefficients and bounded row scalars.

## 7. What is imported and what remains to inspect

This calculation uses cubic/sextic reciprocity and the already scoped
theta reflection, cusp uniformity, support and kernel results. The local
branches and the conductor ledger above are algebraic checks of their
use, not proofs of theta automorphy. They require no independent Möbius
cancellation estimate. The favorable estimate beyond this ledger comes
from applying the imported quadratic large sieve to the squarefree
\(k_0\)-rows after removing smooth row dependence; that analytic
separation and its infinite sums are checked in the [companion note](COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md).

There is no corrective restriction or new assumption needed for the
inspected local overlaps. Helpful presentation expansions are the
inactive \(j=0\) row of the ledger, the explicit \(p\mid t\cap g\)
case, and the simultaneous-prime formula with \((n',P_NP_B)=1\) but
unrestricted \(b'\) at those primes. They explain why a generic bound on
the large \(j=4\) value cannot replace the reindexing.
