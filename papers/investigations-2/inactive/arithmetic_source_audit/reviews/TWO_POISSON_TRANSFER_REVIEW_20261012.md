# Two Poisson transfer proposition review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel internal reviews used the inherited configuration. These are
not independent specialist validation or formal verification.

## Result and scope

The full two-Poisson transfer proposition closes in this internal audit
under the stated classical Poisson, Gauss-sum, CRT, and reciprocity
inputs. No unresolved defect was identified across the permitted
shared factors, repeated row prime powers, principal frequencies,
short ranges, or smooth kernels. The returned energies remain in the
special coefficient class, with the required child scales.

This extends the earlier [single nonempty branch review](FIRST_BRANCH_REVIEW_20261012.md)
to every permitted transfer index. The [completed mean-square review](COMPLETED_MEAN_SQUARE_REVIEW_20261012.md)
is a separate input to cube removal. Combining these audited inputs also
checks the finite canonical induction, including its base case and
derivative recurrence. The full zero-free theorem has not received an
end-to-end assessment.

Source: the [October 5 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
openai/math revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb,
SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d.
Physical source lines 1487–1512 state the transfer; 2217–2683 give its
proof. The canonical induction is at 1515–1609, and exclusion removal
at 962–994. No upstream source correction was needed for these steps.

## Proposition and hypotheses

Assume
\[
1\le H,L,F,\Sigma\le D^{C_0},\qquad
\max\{H,LF\}\le\Sigma,\qquad C_0\ge1.
\]
The target scale \(\Sigma\) is independent of \(LF\).
Let \(W\) be smooth on a fixed compact support \(I=[u,v]\subset(0,\infty)\),
\(\xi\) a character of the fixed ray group, and \(\mathcal A(W)\)
the smoothed energy with the special coefficients
\(a_\xi=\overline\alpha\gamma_2\xi\), squarefree primary columns, and
zero-extended twists \(\chi_n(k)\chi_n(f)^4\).
The fixed radial majorant \(\Phi\) is nonnegative and Schwartz,
at least one on \([0,1]\), with Fourier support \([0,C_\Phi]\).

For every integer \(m\ge0\) and \(\varepsilon>0\), the audited estimate is
\[
\mathcal A(W)\ll
D^\varepsilon\Sigma\|W\|_{C^{4m+12}(I)}^2
(1+S_m),
\]
where \(S_m\) is the supremum of
\(\mathcal E(H',X',F';\xi',U)/(X'F')\), over
\[
H',X',F'\ge1,\qquad
H'\le\frac{HL}{\Sigma F},\qquad
\frac{H'}{X'F'}\le\frac H\Sigma,\qquad
X'F'\le L.
\]
The tests are supported in \(I'=[u/16,4v]\), with
\(\|U\|_{C^m(I')}\le1\); an empty supremum is zero. The implied
constant has only the source's fixed dependencies on
\(m,C_0,\varepsilon,I,\nu,S\) and the fixed arithmetic data.

| Obligation | Checked conclusion | Derivation |
| --- | --- | --- |
| First transformation | Full masks, normalization, fixed ray expansion, diagonal, and divisor-bounded map \(y=hf^2\) | [Arithmetic ledger](../notes/TWO_POISSON_ARITHMETIC_LEDGER_20261012.md) |
| Second transformation | Original coefficient class restored; residual exclusion exactly \(r=tg/e\); all principal modes retained | [Arithmetic ledger](../notes/TWO_POISSON_ARITHMETIC_LEDGER_20261012.md) |
| Signed preimages | Common kernel and exact coefficient for every preimage; total \(\tau(r)\mathbf1_{f'\mid k'}\) | [Arithmetic ledger](../notes/TWO_POISSON_ARITHMETIC_LEDGER_20261012.md) |
| Smooth and short ranges | Arbitrary positive intermediate scales, common Mellin majorant, support rescaling, both zero modes and divisor budget | [Smooth and short ranges](../notes/TWO_POISSON_SMOOTH_AND_SHORT_RANGES_20261012.md) |
| Child admissibility | Exclusion removal preserves product and gap, and all resulting lengths stay at least one | [Return and termination](../notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md) |
| Recursion | Strict row contraction, direct short-cube bounds, finite base case, and finite derivative order | [Return and termination](../notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md) |

## Decisive cancellation and all returned branches

The first Poisson calculation is enlarged to a positive form with its
entire declared \(C,t,d\) domain. The original Fourier restrictions
are not retained as new outer restrictions. The second calculation then
sets \(r=tg/e\), \(f'=Cew\), and \(k'=deh\). Every preimage of these
fixed return variables has the same column scale, Fourier parameter,
and exact exterior coefficient. This permits signed regrouping before
taking absolute values.

At \(p\mid f'\), write \(\delta_p=\mathbf1_{p\mid k'}\).
Placements in \(C,e,w\) contribute respectively
\(1+\delta_p,-\delta_p,-(1-\delta_p)\). Their sum is
\(\delta_p\), while choices \(t\mid r\) contribute \(\tau(r)\).
Thus only \(f'\mid k'\) survives. The universal preimage bijection
allows \(k'\) to share primes with \(r\), have repeated prime powers,
contain fixed \(S\)-primes, or be a unit. It introduces no restriction
\((d,h)=1\), \((e,h)=1\), or valuation at least two.

For a dyadic block \(R,F'\), put
\[
X'=L/(RF'),\quad \Sigma'=L/R,\quad
H'=HL/(\Sigma FR^2).
\]
Retain only \(r\)'s with an actual surviving term. The divisibility
\(f'\mid k'\) and Fourier support then give, for every \(j\mid r\),
\[
X'/N(j)\ge\Sigma F/H\ge1.
\]
Removing the exclusion sends
\((X',F')\) to \((X'/N(j),F'N(j))\), preserving \(\Sigma'\)
and the row range. Only after retaining these \(r\)'s may positivity
enlarge the other ranges. Taking absolute values earlier would destroy
the divisibility and can leave formal children of length below one.

The second zero mode sums with exact weight
\(w_{C,d}Y_{C,d}\ell=c_I\Sigma/[N(C)^2N(t)]\).
The \(C\)-sum converges and the \(t\)-sum costs a logarithm.
The first zero mode is \(O(H)\). Both are within the target \(\Sigma\);
principal nonzero frequencies remain in the transfer. No estimate of
a principal Möbius sum is assumed.

The positive intermediate row scale \(Y_{C,d}\) may be below one.
Poisson remains valid there, and its zero-mode bound uses \(Y\ell\),
not an assumed nonempty row annulus. Uniform coupled-kernel bounds
require \(2m+4\) derivatives at the second stage and \(4m+12\) at
the first. Each dyadic block has exact normalization
\((\Sigma R/L^2)R(L/R)^2=\Sigma\).

## Exact diagnostics and their scope

The [full-transfer checker](../numerics/check_full_transfer_bookkeeping.py)
and [verified-source record](../numerics/full_transfer_bookkeeping_record_20261012.json)
pass **4,186,781 exact assertions**, with **zero floating comparisons**
and eleven negative-control families. They cover 62,208 signed
regrouping cases and 438,012 actual Eisenstein preimages, including
repeated row powers, all six units, and fixed excluded primes in the row.
An independent forward enumeration checks the inverse preimage formula.

Further checks cover sextic zero extensions, first-map fibers,
normalization and common Fourier parameters, 271 retained scale cases,
309 divisor-shifted children, and 1,311 eligible cube-tail parameter
cases. The latter are checks of parameter eligibility; they do not
claim nonzero Möbius coefficients or actual Fourier kernels. The
below-one intermediate scale is tested in an admitted outer-domain
example, and the unit-cube and direct short-column cases are included.

The checker adapts the earlier finite [regrouping diagnostic](../numerics/check_transfer_regrouping.py)
and extends its coverage; it is not an independent mathematical review.
Counts include repeated checks inside enumerations. The finite tests
evaluate no Gauss sum, smooth kernel or Poisson/theta transformation,
and do not prove unbounded estimates or uniform derivative norms.
The [CLI validation record](../numerics/full_transfer_bookkeeping_cli_validation_20261012.json)
confirms source-mismatch rejection before arithmetic/output and a
successful portable run without the source. The [replay guide](../numerics/README.md#full-two-poisson-transfer-bookkeeping)
records the command, source verification, exact arithmetic and limitations.

## Canonical termination and remaining scope

For the canonical range \(\Sigma=XF\), \(H/\Sigma\le D^{-\kappa}\),
a nonempty long cube satisfies \(N(b)^3>X^2/H^2\) and \(L_b>1\).
Using the original target \(\Sigma\) at column scale \(L_b\) gives
\[
H'<H(H/\Sigma)^2\le D^{-2\kappa}H.
\]
The child keeps the same gap condition and a product at most \(\Sigma\).
Short columns and an empty cube supremum are bounded directly; the
unit long cube when the cutoff is below one also obeys the contraction.
The triangle bound supplies the base case \(H\le1\), and
\(\lceil C_0/\kappa\rceil\) induction levels suffice. The derivative
order grows by a finite recurrence with multiplier four and additive
term twelve; its size does not depend on a row or dyadic block.

These findings close the transfer and canonical-recursion bookkeeping
under the stated audited inputs. The earlier theta and quadratic-sieve
imports retain their [recorded scope](COMPLETED_MEAN_SQUARE_REVIEW_20261012.md);
this transfer audit supplies no independent proof of them. The next
bounded target is the final assembly from canonical energy to the
original mean square, fixed-character extraction, and the zero-free
implication, with one matched ledger of parameters and constants.
