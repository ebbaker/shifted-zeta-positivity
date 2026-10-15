# A bounded improvement to the effective outer budget

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an internally checked analytic budget refinement, not external refereeing or an evaluation of the imported exponent-pair constants.

The source documents are Investigation 21 [Note 43](../../../21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md) and [Note 58](../../../21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md). Their imported analytic and exponent-pair hypotheses remain in force. The original Investigation 21 notes remain unchanged.

## Outcome

The dominant explicit low-index constant can be reduced from

\[
A_0=\frac{36138917}{16}
\quad\hbox{to}\quad
A_* = \frac{218227}{384},
\]

a factor exceeding 3974, by splitting exactly the same low-index sum into four ranges. The remaining arithmetic input, outer domain, analytic branches, exact Riemann--Siegel endpoint, high-index assignments and carrier proof are unchanged.

Substituting this into Note 58's original six equal budget shares gives the sufficient conditional log-height

\[
L\ge1+\max\left\{188548128,
14000\log(663552G_0C_{\rm EP})\right\}.
\tag{A}
\]

A different budget allocation gives the sharper alternative

\[
L\ge1+\max\left\{32000000,
14000\log(14155776G_0C_{\rm EP})\right\}.
\tag{B}
\]

For both formulas retain the original optional condition
\(x-L^{-1}\ge3T_{\rm EP}\), and all other hypotheses below. Either sufficient formula may be used; (A) preserves the old logarithmic coefficient and improves its fixed term unconditionally relative to the old formula. Formula (B) gives a much smaller fixed term at the cost of a modest increase in the EP logarithm. No value is assigned to \(C_{\rm EP}\).

The old fixed term **749376582912 is a single integer**, not four separate entries. It is exactly \(48\cdot1728\cdot4A_0\). The new thresholds still correspond to astronomical spectral height \(x=4\pi e^L\). They do not furnish a feasible bridge from the existing finite certificate through \(|x|\le112\), and they do not bound the true onset of positivity from below.

## Retained hypotheses

Use Note 43's notation

\[
\rho=\eta=10^{-5},\quad
\theta_*={61\over24},\quad
\theta_0=\theta_*-\rho/100,\quad
G_0={962773\over671},
\]
\[
\lambda={21807\over254720000}-{63\over50}\rho>{1\over14000}.
\]

At real center \(x\), require \(L=\log(x/(4\pi))\ge100002\), \(0<t\le1/2\), \(tL\ge61/24\), and work on the same shrinking analytic discs \(|z-x|\le L^{-1}\). The underlying disc variables satisfy \(\ell\ge L-1\ge100001\), \(\theta_u=t\ell\ge\theta_0\), and the real-part allowance \(\delta<\rho/2\). The actual numerical EP package is exactly Note 43's arbitrary-interval package at positive loss \(\eta=10^{-5}\), including completion/A-process costs and any source validity threshold. This audit does not supply that package.

## 1. Where the old dominant constant comes from

The original low-index range is \(n\le Y=e^{\ell/5}\). The absolute discrepancy is bounded by

\[
{\theta_u\over4\ell}\sum_{2\le n\le Y}
(\log n)^2 n^{-1/2-\theta_u/4+\delta}
\exp\!\left({\theta_u(\log n)^2\over4\ell}\right).
\tag{1}
\]

Note 43 bounds \(\log n/\ell\) by \(1/5\) everywhere, making the effective exponent barely larger than \(1+1/121\). Integrating \((\log n)^2n^{-1-1/121}\) to infinity costs \(2\cdot121^3\), despite small indices having a substantially better exponent. This is the concrete source of \(A_0\); it is not an imported exponent-pair loss.

## 2. Four exact ranges

Split at

\[
b_0={1\over1024},\quad b_1={1\over64},\quad
b_2={1\over10},\quad b_3={1\over5},
\qquad n=e^{b_i\ell}.
\]

If \(\log n\le b\ell\), (1)'s summand is bounded using

\[
p_b={1\over2}+{\theta_u(1-b)\over4}-\delta.
\]

Put \(\theta_u=\theta_0+s\), \(s\ge0\). Since \((1-b)/4\ge1/5\) and \(5/e<2\),

\[
(\theta_0+s)e^{-s(1-b)\log n/4}
\le \theta_*+{2\over\log n}.
\tag{2}
\]

Direct rational checks give

| Upper relative log-index \(b\) | Uniform lower exponent \(p_b\) |
| --- | --- |
| \(1/1024\) | \(1+2/15\) |
| \(1/64\) | \(1+1/8\) |
| \(1/10\) | \(1+1/14\) |
| \(1/5\) | \(1+1/121\) |

All inequalities are strict after retaining \(\theta_0\) and \(\delta<\rho/2\). This argument remains uniform when \(\theta_u\) grows; no fixed-\(\theta_u\) substitution is made.

For the first range, extend its positive majorant to all \(n\ge2\). The same unimodal sum--integral comparison used in Note 43 gives, for \(d=15/2\),

\[
\sum_{n\ge2}(\log n)^k n^{-1-1/d}
\le k!d^{k+1}+k^k,\qquad k=1,2.
\]

Consequently this range contributes at most

\[
{1\over4\ell}\left[\theta_*(2d^3+4)+2(d^2+1)\right]
=\frac{217843}{384\ell}.
\tag{3}
\]

## 3. The three upper ranges cost less than \(1/\ell\)

For a range starting after \(X=e^{b\ell}\), with majorant exponent \(1+1/d\), bound its sum by the entire tail after \(X\). The functions \((\log y)^k y^{-1-1/d}\), \(k=1,2\), are decreasing for \(y\ge X/2\) on the present domain. Hence their sums are bounded by integrals from \(\lfloor X\rfloor\ge X/2\). Writing \(r=b\ell\) and using \(2^{1/d}\le2\) gives

\[
\sum_{n>X}(\log n)n^{-1-1/d}
\le2e^{-r/d}(dr+d^2),
\]
\[
\sum_{n>X}(\log n)^2n^{-1-1/d}
\le2e^{-r/d}(dr^2+2d^2r+2d^3).
\]

Thus the contribution to (1) is at most

\[
{e^{-b\ell/d}\over2\ell}P_{b,d}(\ell),\qquad
P_{b,d}(\ell)=
\theta_*[d(b\ell)^2+2d^2b\ell+2d^3]
+2[db\ell+d^2].
\tag{4}
\]

For the three ranges take

\[
(b,d)=\left({1\over1024},8\right),\quad
\left({1\over64},14\right),\quad
\left({1\over10},121\right).
\]

Since \(P\) has positive coefficients and degree two, \(e^{-b\ell/d}P(\ell)\) decreases once \(\ell>2d/b\), which holds throughout \(\ell\ge100001\). At the lower endpoint exact rational Taylor lower bounds for the exponential prove, respectively,

\[
\tfrac12 e^{-b\ell/d}P_{b,d}(\ell)
<\tfrac34,\quad <\tfrac18,\quad <\tfrac18.
\tag{5}
\]

These are rigorous upper shares; approximate values at the endpoint are about \(0.57434\), \(1.50\times10^{-41}\), and \(2.02\times10^{-26}\), included only for interpretation. Equations (4)--(5) bound the upper ranges together by \(1/\ell\). Combining with (3) proves the revised complete low-index bound \(A_*/\ell\).

## 4. Transfer through the existing complete budget

Only the low-index constant in Note 43 changes. Its complete weighted replacement bound becomes

\[
\left|\sum_{n\le N_{\rm RS}}e^{t\log^2n/4}n^{-w}-\zeta(w)\right|
\le {A_*\over\ell}+16e^{-\ell/40}+2G_0C_{\rm EP}e^{-\lambda\ell}.
\]

The same disc/carrier proof then gives, with \(\Lambda=L-1\),

\[
B_C^*(L)=\frac{4A_*}{\Lambda}+64e^{-\Lambda/40}
+8G_0C_{\rm EP}e^{-\lambda\Lambda}
+16\Lambda^2e^{-3\Lambda/4}+6e^{-2\Lambda/5},
\]
\[
d_C^*(L)=1728B_C^*(L)+\frac{409}{L}.
\tag{6}
\]

The same condition \(d_C^*(L)\le1/8\) yields Note 58's full signs and energy floor, without a stationary hypothesis:

\[
E\ge2|Q|^2\ge2\Gamma^2/81,\qquad
\mathcal L_0\ge\frac{31}{16}|Q|^2\omega^2,\qquad
\mathcal L_1\ge\frac{31}{16}|Q|^2\omega^4.
\]

For formula (A), retain each of Note 58's six \(1/48\) shares. The only changed fixed term is

\[
48\cdot1728\cdot4A_*=188548128.
\]

For formula (B), combine the low-index and carrier terms using

\[
\frac{1728\cdot4A_*}{\Lambda}+\frac{409}{L}
\le\frac{3928495}{\Lambda}
<\frac{63}{512}\qquad(\Lambda\ge32000000).
\]

The EP term is at most \(1/1024\) if
\(\Lambda\ge14000\log(14155776G_0C_{\rm EP})\).
The three remaining exponential terms together are at most \(1/1024\) already for \(\Lambda\ge100001\): each is bounded by \(1/3072\) using the elementary Taylor estimates checked in the companion script. The allocations sum to
\(63/512+1/1024+1/1024=1/8\).

## 5. Attainable-height assessment and next decision

This is a real improvement to the sufficient bound, not a claim about the true positivity threshold. Even after this refinement, the retained budget (6) itself cannot certify \(d_C^*\le1/8\) below \(\Lambda\approx31424688\), because its first nonnegative term alone is \(3928086/\Lambda\). This is an obstruction to this particular majorant, not to actual signs.

The untouched initial disc hypotheses already require \(L\ge100002\). Consequently a practical finite-to-asymptotic bridge demands a different nonasymptotic error architecture, not just sharper allocation or the extraction of \(C_{\rm EP}\). The present task has identified and reduced the largest elementary constant; it has not removed the remaining \(1728\) differentiation loss, the \(1/L\) comparison error, the imported constants, or the large preliminary disc threshold.

If the objective is an explicit asymptotic theorem, extracting the actual EP package is now the exact remaining imported task. If the objective is an overlap with finite certificates, first redesign the approximation/differentiated remainder and test a proposed numerical cutoff before undertaking a large sweep. The condition \(tL\ge61/24\) is unchanged, so neither version resolves the lower inner region or the small-time cusp.

## Verification

The companion [checker](../../numerics/check_theta_outer_budget_audit.py) verifies the exponent margins, exact new constants, monotonicity thresholds, tail shares via finite positive Taylor sums, both conditional height allocations and the unchanged \(\lambda>1/14000\) margin. The [receipt](../../numerics/THETA_OUTER_BUDGET_AUDIT_20261015.json) records all 35 passing exact assertions. These are finite rational checks supporting the analytic argument above. They do not evaluate \(C_{\rm EP}\), prove the imported arithmetic theorem, recertify the original complex-disc replacement, or supply a theta stationary-root certificate.
