# Bounded implementation of the sharp strip transfer gate

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**. Same-model subagents assisted with geometry and a separate
arithmetic check; this is internal LLM work, not cross-model or specialist
review.

**Status: the four-leg transfer gate is certified by outward arithmetic
and the analytic cases below.** The first bounded pass completed three
legs and part of the largest. A second bounded pass completed exactly the
missing sectors, with the same per-run limits. This proves the transfer
specified in [Note 01, equation (2)](01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md).
Complete finite-row floors remain open, so no new bound for \(\Lambda\)
is established.

This continues the quantitative milestone at \(t_*=157/1000\), not an
RH-equivalent criterion. The governing references are the
[result-summary index](../../../../../result-summaries/README.md),
[heat-flow cluster 11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control cluster 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[04](../../../../../avoid/04_counts_and_precision_as_evidence.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../../avoid/08_normalization_and_constant_slips.md) and
[10](../../../../../avoid/10_numerics_ahead_of_the_question.md).

## 1. Certified statement

Keep the coefficients, frozen scalars and normalization of Note 01. For
\(y_0=\sqrt{87677/2500000}\), \(y_1=\sqrt{343/500}\), and every integer
\(N\) in the following legs, each nonleading term
\[
 y\longmapsto U_{g_N(y)}(B_{N,n},A_{N,n}(y))n^{-\sigma_N(y)}
 \tag{6}
\]
is nonincreasing on \([y_0,y_1]\). Terms with no active divisor vanish
identically. Consequently their finite sum \(V_N(y)\) is nonincreasing.

| Indices \(N\) | Euler primes | Gcd and active-sector types | Coverage |
| --- | --- | ---: | --- |
| 690988 through 728999 | 2, 3, 5, 7, 11 | 243 | First-pass complete prefix 0–171; completion 172–242 |
| 729000 through 818999 | 2, 3, 5, 7 | 81 | Complete first pass |
| 819000 through 1027999 | 2, 3, 5 | 27 | Complete first pass |
| 1028000 through 3840000 | 2, 3 | 9 | Complete first pass |

The [engine](../../numerics/round-1/check_sharp_y_transfer_gate.py),
[first record](../../numerics/round-1/SHARP_Y_TRANSFER_GATE_RECORD_20261017.json),
[completion wrapper](../../numerics/round-1/complete_sharp_y_transfer_gate.py)
and [completion record](../../numerics/round-1/SHARP_Y_TRANSFER_COMPLETION_RECORD_20261017.json)
carry this computation. The first record intentionally retains its
incomplete largest-leg status. The completion record is required for the
four-leg conclusion; the first record alone does not establish it.

## 2. Integer coverage without freezing the heat coefficient

Let \(D\) be the product of the leg's primes and
\(G=\gcd(n,D)\). Order the divisors of \(G\) as
\(1=d_0<\cdots<d_{r-1}=G\). For sector zero, \(2\le n\le N\)
and all divisors are active. For \(j\ge1\),
\[
 d_{j-1}N<n\le d_jN,
\]
and precisely \(d_j,\ldots,G\) are active. Write \(n=Gk\) and impose
\(\gcd(k,D/G)=1\). When \(n>GN\) there are no active divisors, hence
\(B=A=A'=0\) exactly. Summing the number of sectors gives
\(\sum_{G\mid D}\tau(G)=3^{|P|}\), explaining the coverage table.

The interval coordinates are
\[
 h=\log N,\qquad v=\log(n/N),\qquad L=h+v,
\]
\[
 \delta(h)=-\tfrac12\log(1-(t_*/16)e^{-2h}),\quad
 \ell=\tfrac1{50}-h+\delta(h),\quad
 g=e^{y\ell},\quad F=ge^{yL}=e^{y(v+1/50+\delta(h))}.
 \tag{7}
\]
Thus \(N\) remains variable over its full leg. In particular, the old
plain-gate substitution of the smallest feasible \(N\) is not used.
The closed \(v\)-sector hulls contain the strict/inclusive integer
sectors; every root includes the full \(h\)- and \(y\)-ranges.

The engine discards a cell only after necessary integer conditions fail.
It obtains possible integer \(N\) and \(n\) by outward exponentiation,
intersects the leg and sector bounds, and requires a possible multiple
\(n=Gk\) with the correct gcd. When at most 33 candidate \(k\)'s remain,
it tests each against the exact sector inequalities and outer ratio
bounds. If only one possible \(n\) remains, its logarithm tightens the
cell. These tests may retain infeasible points, but cannot remove a
feasible integer pair. Bisection uses closed children sharing their
boundary, so it leaves no gaps. A positive interval upper bound is treated
as unresolved and subdivided; it is never a counterexample by itself.

## 3. Gate evaluation with both kinds of kink

Use the divisor factors \(C_0,C_y\) of Note 01 and put
\[
 c=C_0,\qquad Q=FC_y,\qquad
 T=F[(v+1/50+\delta)C_y+\partial_y C_y].
\]
After removal of the positive \(b_t(n)\), the two branches are
\(u_e=|c+eQ|/(1+eg)\), \(e=\pm1\). Their exact activity comparison is
\[
 u_-\ge u_+\quad\Longleftrightarrow\quad
 (gc-Q)(c-gQ)\ge0.
\]
A strictly positive interval selects minus, a strictly negative one selects
plus, and a zero-containing interval retains both. For every possibly
active branch, the code encloses the bracket in (2), multiplied by the
positive denominator:
\[
 (1+eg)\mathcal D(c+eQ,eT)
 -\left[\tfrac L2(1+eg)+e\ell g\right]|c+eQ|. \tag{8}
\]
For a zero-containing numerator interval, the upper absolute-value
right derivative is bounded by \(|T|\). No zero is deleted or replaced
by a sign chosen at its midpoint. The entire signed interval product in
(8) is retained: the coefficient of the plus absolute value can be
negative for small \(n\).

A second exact expression reduces overestimation near branch ties. Set
\[
 R=c-gQ,\quad S=Q-gc,\quad R'=-g(\ell Q+T),\quad S'=T-\ell gc.
\]
Since
\[
 \max(u_-,u_+)=\frac{|R|+|S|}{1-g^2},
\]
an equivalent sufficient sign test is
\[
 \mathcal D(R,R')+\mathcal D(S,S')
 -\left[\tfrac L2-\frac{2g^2\ell}{1-g^2}\right](|R|+|S|)\le0.
 \tag{9}
\]
Both expressions are evaluated with outward intervals. A cell passes if
all possibly active brackets (8) pass, or if (9) passes. Equality of the
underlying one-sided derivative formulas means that (9) also proves every
actually active branch of (2), including ties. The positive-part kink in
\(\sigma_N\) is handled by its global right-slope bound
\(\sigma'_{N,+}\ge1/2\), proved in Note 01; no numerical derivative of
that kink is assumed.

## 4. Analytic cells and exact coefficient zeros

Two classes need no interval subdivision beyond establishing membership.

**A single active divisor.** Write \(m=n/d\), \(a=\log m\). Then
\(A=B e^{ay}\), \(B\ne0\), and
\[
 0\le a\le\log N<-2\ell.
\]
The strict final inequality follows from
\(q_N/N=N-t_*/(16N)>e^{0.04}\), checked at the smallest \(N\), since
its left side increases. For \(a>0\) only plus is active. Its logarithmic
rate is
\[
 \frac{d}{dy}\log u_+
 =\frac a2+\frac12\left[(\ell+a)\tanh\frac{y(\ell+a)}2
 -\ell\tanh\frac{y\ell}2\right]\le\frac a2,
\]
because \(x\tanh(yx/2)\) is even and increases with \(|x|\), while
\(|\ell+a|\le|\ell|\). After multiplication by \(n^{-\sigma}\), the
rate is at most \(-\tfrac12\log d\le0\). At \(m=1\), both branches
equal \(|B|\) identically and their weighted derivatives are also
nonpositive. The other possible branch tie \(a=-2\ell\) is excluded
by the strict feasible bound.

**The exact prime zeros.** The shortcut applies only to a full-active
\(G=p\in P\) cell whose sole possible integer \(n\) is \(p\).
Then
\[
 B=0,\qquad A=b_t(p)(p^y-1)>0,
\]
and minus is the unique active branch. Its weighted logarithmic rate is
at most
\[
 \frac{\ell}{1-g}+\frac{\log p}{1-p^{-y}}-\frac{\log p}{2}
 \le\ell+\frac{\log p}{2}+\frac1y
 <0.52-13+1.5+\frac{1000}{187}
 =-\frac{52663}{9350}<0.
\]
Here \(q_N>N^2/2\), \(\log N>13\), \(\log p<3\), and
\(y>0.187\). No other simultaneous coefficient zero is assigned a
structural shortcut. Other zeros remain under (8)–(9).

## 5. Bounded runs and arithmetic checks

The [first run plan](../../numerics/round-1/GATE_RUN_PLAN_20261017.md)
fixed 45 seconds and 30,000 evaluated boxes per leg, depth 36, 40-digit
Decimal arithmetic and 512 MiB. The three smaller legs completed. The
largest stopped at its box cap after completing patterns 0–171, with no
depth-limit unresolved leaf. Pattern 172 had pending subtrees and the
remaining patterns were unopened. The record preserves that stop.

The [completion plan](../../numerics/round-1/GATE_COMPLETION_PLAN_20261017.md)
then fixed the suffix 172–242 under the same limits. Pattern 172 was
restarted from its full original root; none of its incomplete first-pass
work was needed. The completion wrapper checks the original engine hash,
records the first record's hash, verifies its complete prefix and the three
completed legs, and checks that prefix and completed suffix form the exact
243-pattern partition. The suffix completed in 34.45 seconds with no
pending or unresolved cell. Total interval evaluation time across both
runs was 91.06 seconds, and peak memory was below 22 MiB. These are measured
execution costs, not an optimality claim.

Arithmetic uses directed rounding for addition, subtraction, multiplication
and division. Correctly rounded nearest-mode \(\exp,\log,\sqrt{\cdot}\)
are padded outward by \(10^{-38}\). Exact rational derivative identities
exercise branch ties and zero numerators. A separate
[same-model arithmetic checker](../../numerics/round-1/check_gate_arithmetic.py)
and [record](../../numerics/round-1/GATE_ARITHMETIC_CHECK_RECORD_20261017.json)
compare the implemented expressions with 110-digit direct evaluations on
actual integer terms, and test that feasible toy pairs survive trimming
and bisection. No false pass, missing active branch or false pruning was
found. This is a separate implementation check by the same model, not an
independent validation of the theorem. Accepted-leaf hashes identify the
execution; every sign decision comes from an interval comparison or the
written analytic arguments above. No global extremal slack is inferred
from acceptance thresholds or leaf counts.

The preceding [floating scout](../../numerics/round-1/scout_sharp_y_transfer_gate.py)
and [record](../../numerics/round-1/FLOAT_GATE_SCOUT_RECORD_20261017.json)
found no sampled violation at the selected leg endpoints. Its samples
played no role in the coverage proof. The exact generic counterexample
from Note 01 is an adverse control: both branches tie, the minus bracket
(8) encloses \(\tfrac12\log2>0\), and the implementation correctly
refuses to certify it. Thus a failed generic inheritance implication has
not been silently built into this computation.

## 6. Consequence and remaining work

Combining this transfer with the analytic monotonicity of \(M_N\) and
\(K_N\) in Note 01 gives
\[
 L_N^\sharp(y)\ge L_N^\sharp(y_0)
 \quad(y_0\le y\le y_1)
\]
whenever \(V_N(y_0)<1\). The existing sharp pilot has a positive
numerator. Therefore its complete margin now extends through the whole
strip in \(W_{690988}\):
\[
 \left|\frac{H_{t_*}(x+iy)}{B_{t_*}(x+iy)}\right|
 >0.0017752269101384707,
 \quad x\in W_{690988},\quad y_0\le y\le y_1. \tag{10}
\]
Here \(B_t\) is the nonzero carrier from the inherited approximation
theorem. Equation (10) pays the full \(3\times10^{-7}\) allowance;
no corrected-center residual is substituted. The other finite windows
still require new sharp floors or a rigorously justified amortized
coverage method at \(t_*\). Neither the historical plain rows nor a
monotonicity assumption in \(N\) supplies them.

The collision-family screen is unchanged from Note 01 section 6.
Euler-factor controls change the coefficients and conductor;
weighted-square, reflected, primitive and earlier positive-source controls
do not supply the complete theta approximation with its stated error
budget. The generic sharp algebra still applies to their own paired
coefficients when such a representation is provided. These computations
are not a shape-only collision exclusion and make no claim about a
control region containing its collision without that control's full inputs.

The next bounded task is a floor-and-coverage design at the first row and
leg seams, retaining all producer and amortization errors. A full row
campaign remains subject to the portfolio's round-level cross-model
review gate. No manuscript, snapshot folder or global Newman bound is
created by completing this transfer calculation.
