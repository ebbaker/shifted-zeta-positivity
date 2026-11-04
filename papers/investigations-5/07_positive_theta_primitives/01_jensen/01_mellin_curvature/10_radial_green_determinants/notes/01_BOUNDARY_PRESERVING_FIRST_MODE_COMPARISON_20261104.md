# RGD-B01: preserve the theta boundary before a first-mode comparison

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual recorded **gpt-6-astra (Codex), effort
max**. Research chat0002, thread `01a1a75a-0fb3-7e02-a1a5-092d309ba58a`,
turn `01a1a75a-1205-71a1-a2ed-5a1cfd44d617`.

**RGD-B01 / overview r1: completed bounded conceptual return.** This note
selects one direct joint comparison, proves explicit complete-source
error bounds, works the boundary-sensitive k=1 and pure-volume k=4
structures, and exposes a finite, discriminating residual test. It does
**not** establish that either determinant comparison passes that test.
The proofs below have proof-author checking only; RGD-E04 is ready for
separate internal assessment. No numerical implementation or new scan was
performed. No optional Mellin or moment-inequality alternative was pursued.

The concrete gain is at the coefficient level: preserving the exact
theta boundary reduces the absolute first-mode error in c0 by a factor
strictly greater than **2200**, compared with retaining only the first
mode of the differentiated source. This factor is proved below, not
measured, and is not a determinant gain or a runtime claim.

Read with the [overview and B01 contract][overview], [result index][results]
(especially [theta identities][theta] and [controls][controls]), and
[avoid index][avoid] (especially [reformulations][a01], [scoped claims][a07]
and [joint signed estimates][a12]).

## 1. Fixed source, consumer and baseline

Use the complete time-zero source and ordinary coefficient convention
from overview (1)–(13). Write
\[
p_n(u)=\exp(u-\pi n^2e^{4u}),\qquad
p=\sum_{n\ge1}p_n,\qquad m_j(u)=\frac{u^{2j}}{(2j)!},
\]
\[
x_j=\frac18\int_0^\infty p_1m_j\,du,\qquad
y_j=\frac18\int_0^\infty\sum_{n\ge2}p_nm_j\,du.
\tag{1}
\]
All negative-index quantities are zero. These are scaled primitive
moments: d_j/8=x_j+y_j. With the **unchanged** b=1/16, put
\[
C_j(b,z)=b\delta_{j0}+z_{j-1}-z_j\quad(j\ge0),\qquad C_j=0\ (j<0).
\tag{2}
\]
Thus c_j=C_j(b,x+y). The reference coefficients are
c_j^*=C_j(b,x). The reference is an algebraic approximation using the
complete theta boundary; it is not a claim that p1 itself satisfies
theta reflection.

Let F_l(c)=det[c_{l+j-i}] for i,j=0,1,2, and define the **collected joint
polynomial**
\[
\mathscr P_k(b,z)=F_k(C(b,z))^2-F_{k-1}(C(b,z))F_{k+1}(C(b,z)).
\tag{3}
\]
It has total degree six in b,z, and
\[
Q_{3,k}=\mathscr P_k(b,x+y)=D_{4,k}D_{2,k}.
\tag{4}
\]
Equation (4) is the inherited target identity, not a sign argument.
The additional information selected here is the explicit canonical
mode-tail bound (6) and its propagation through the *combined* polynomial.

The [accepted Jensen assessment][lowerreview] and [parent balance note,
Section 1][parentbalance] supply D2,k>0 and D3,k>0 for the same complete
source at integer k>=0. Their status is internal LLM assessment with
shared premises, not specialist review. A verified L_k>0 with Q3,k>=L_k
would give D4,k>=L_k/D2,k and eta_k=L_k/D3,k^2 in overview (20).
No such positive L_k is asserted here.

Known finite-order coefficient positivity already covers this pilot:
[Katkova, Theorem 1][katkova] gives PF44. Her (4)–(5) use b_j=8*4^j*c_j;
positive geometric scaling preserves minor signs. The local purpose is
to test a quantitative method and its losses, not to add a new positivity
range. Only these source passages were rechecked; see the [source record][refs].
The Gaussian Mellin comparison is neither assumed nor proved, and no
noninteger Toeplitz identity is used.

## 2. An explicit tail for every primitive moment

For u>=0, e^(4u)>=1+4u, so
\[
p_n(u)\le e^{-\pi n^2}e^{-(4\pi n^2-1)u}.
\tag{5}
\]
For n>=2, n^2>=4+5(n-2). Let a=16*pi-1 and q=exp(-5*pi).
Integrating (5), including the factorial in m_j, gives for every integer
j>=0
\[
\boxed{0<y_j\le E_j:=
\frac{e^{-4\pi}}{8(1-e^{-5\pi})(16\pi-1)^{2j+1}}.}
\tag{6}
\]
Indeed, the integral of u^(2j)e^(-lambda*u)/(2j)! is
lambda^(-2j-1); bound each denominator below by a^(2j+1) and sum the
remaining geometric majorant. Tonelli applies to the positive summands.
This is an infinite-source bound, not a finite-mode measurement. It is
deliberately conservative: it keeps no correlations between different y_j.

For reference, the stronger spatially varying *pointwise relative*
envelope is
\[
0<\frac{p-p_1}{p_1}
\le\frac{e^{-3\pi e^{4u}}}{1-e^{-5\pi e^{4u}}}.
\tag{7}
\]
Equation (6), not a rounded uniform constant from (7), is the selected
payment in this attempt. Small relative source error alone is not small
relative determinant error.

All fixed polynomial moments and boundary transfers converge: each
derivative of p_n is p_n times a polynomial in pi*n^2*e^(4u), and the
complete Gaussian mode tail dominates these factors. No outer boundary
or mode remainder is omitted.

## 3. Why preserving b matters quantitatively

Define the natural first-mode endpoint constants
\[
\beta_n=-p_n'(0)/8=(4\pi n^2-1)e^{-\pi n^2}/8>0.
\tag{8}
\]
Complete theta reflection gives sum beta_n=b=1/16. The reflection
normalization agrees with [DLMF 20.7.32][dlmf] at z=0, tau=i*R^2;
differentiating gives p'(0)=-1/2 as in the inherited derivation.
Put tau=b-beta_1=sum_(n>=2) beta_n>0.

For each individual mode, p_n''-p_n=8*Phi_n, where
Phi_n=p_n[2(pi*n^2*e^(4u))^2-3*pi*n^2*e^(4u)]>0 on u>=0.
The even-probe Green identity therefore gives
\[
\int_0^\infty\Phi_1m_j\,du
=\beta_1\delta_{j0}+x_{j-1}-x_j.
\tag{9}
\]
Consequently c^* is the moment sequence of the positive half-line
measure Phi_1(u)du+tau*delta_0 (delta_0 evaluates a probe at zero).
This describes the reference exactly; the canonical source remains the
complete smooth source. Positivity of that reference measure does not
imply its Toeplitz minors are positive.

Let c0^(1)=integral Phi_1. The two approximation errors are exactly
\[
c_0^*-c_0=y_0,\qquad c_0-c_0^{(1)}=\tau-y_0>0.
\tag{10}
\]
The second inequality also follows from positivity of all omitted Phi_n.
Since tau>=beta_2=a*exp(-4*pi)/8 and y0<=E0,
\[
\boxed{\frac{|c_0-c_0^{(1)}|}{|c_0-c_0^*|}
=\frac{\tau-y_0}{y_0}
\ge a^2(1-e^{-5\pi})-1>2200.}
\tag{11}
\]
For the final strict inequality, pi>3 gives a>47 and
e^15>1000 (already 15^5/5!>1000); hence the preceding expression is
greater than 47^2*(999/1000)-1=2205.791.
The substantial endpoint contribution from the omitted source modes is
already present in b. Dropping it and then bounding it separately loses
this cancellation.

For j>=1, no scalar endpoint survives in (9), and
\[
c_j-c_j^*=y_{j-1}-y_j
=\int_0^\infty\sum_{n\ge2}\Phi_nm_j\,du>0.
\tag{12}
\]
Thus the improvement (11) specifically concerns c0. It is not assigned
to the k=4 comparison, whose coefficients start at c1.

## 4. Keep the full joint polynomial before taking a bound

For k=1 or 4 put J=k+3. Expand the already collected polynomial at the
one-mode reference, with b fixed:
\[
\mathscr P_k(b,x+z)-\mathscr P_k(b,x)
=\sum_{1\le|\alpha|\le6}t_{k,\alpha}(x)z^\alpha,
\quad
t_{k,\alpha}(x)=\frac{\partial_x^\alpha\mathscr P_k(b,x)}{\alpha!}.
\tag{13}
\]
Here alpha has J+1 entries, indexed from zero. Zero coefficients are
omitted. This is an exact finite Taylor identity with no remainder.
Define
\[
q_k^*=\mathscr P_k(b,x),\qquad
\mathcal R_k(x,E)=\sum_{1\le|\alpha|\le6}
|t_{k,\alpha}(x)|\prod_{j=0}^J E_j^{\alpha_j}.
\tag{14}
\]
Substitute z=y and use (6) to obtain the proved absolute error estimate
\[
\boxed{|Q_{3,k}-q_k^*|\le\mathcal R_k(x,E),\qquad
Q_{3,k}\ge L_k:=q_k^*-\mathcal R_k(x,E).}
\tag{15}
\]
The remaining finite question is **whether L1 and L4 are positive for
these fixed definitions**. Their signs have not been evaluated here.
Unlike (4), (15) compares the canonical expression with explicit
one-dimensional first-mode integrals and a paid full-source error. It
is a sufficient robustness test, not an equivalent rewriting of Q>=0.
A negative L_k would only reject this payment as a proof of positivity.

Taking absolute values occurs after subtracting the two neighboring
products and collecting all mixed terms. This avoids paying for terms
that cancel algebraically. It still discards correlations among the
tail moments y_j and can therefore fail despite Q3,k>0. The diagnostic
must measure that loss; (7) alone cannot decide it.

### k=1: explicit boundary-sensitive check

Let A=c0, B=c1, C=c2, D=c3, E=c4, just in this paragraph. Direct
3-by-3 expansion gives
\[
F_0=A^3,\quad F_1=B^3-2ABC+A^2D,
\quad F_2=C^3-2BCD+AD^2+B^2E-ACE.
\]
Thus the complete joint expression is
\[
\begin{aligned}
F_1^2-F_0F_2={}&B^6-4AB^4C+4A^2B^2C^2+2A^2B^3D\\
&-2A^3BCD-A^3C^3-A^3B^2E+A^4CE\\
={}&(B^2-AC)(B^4-3AB^2C+A^2C^2+2A^2BD-A^3E).
\end{aligned}
\tag{16}
\]
The A^4*D^2 terms cancel exactly. Bounding the two original products
separately would pay for them twice. Substituting A=b-x0-y0 and
C_j=b*delta_(j0)+x_(j-1)+y_(j-1)-x_j-y_j retains every endpoint-volume
mixed term. The inherited face ranges are q=0,...,3 for F0; q=1,...,3
for F1; q=2,3 for F2. None is deleted. Only x0,...,x4 and E0,...,E4 are
needed. The final factorization is an algebra check, not an assumed
positive D4,1.

### k=4: explicit pure-volume check

For l=3,4,5,
\[
F_l=c_l^3-2c_{l-1}c_lc_{l+1}
+c_{l-2}c_{l+1}^2+c_{l-1}^2c_{l+2}
-c_{l-2}c_lc_{l+2}.
\tag{17}
\]
All coefficients in F4^2-F3*F5 lie in c1,...,c7. Hence every coefficient
is a primitive difference and b is absent. The three determinants all
have only q=3 volume terms, as required by overview (14). The residual
test uses x0,...,x7 and E0,...,E7; it remains degree six. It cannot be
replaced by positivity of the positive primitive measure.

## 5. Finite acquisition and the actual remaining obligation

The selected expression now needs only eight elementary one-dimensional
integrals, shared between the two cases, and exact polynomial algebra.
There is no six-dimensional absolute-value quadrature. For a spatial
cutoff U>=0, let a_U=4*pi*e^(4U)-1. The same exponential tangent bound
gives the following entire exterior payment for each first-mode moment:
\[
0\le x_j-\frac18\int_0^U p_1m_j\,du\le B_j(U):=
\frac{e^{U-\pi e^{4U}}}{8(2j)!}
\sum_{h=0}^{2j}\binom{2j}{h}
\frac{U^{2j-h}h!}{a_U^{h+1}}.
\tag{18}
\]
To prove it, set u=U+v, use e^(4v)>=1+4v, expand (U+v)^(2j), and
integrate each nonnegative monomial. This pays the complete spatial
tail; it does not pay numerical quadrature error on [0,U].

For execution define x^U by the exact integrals over [0,U]. The direct
application of (13) to x^U, with residual (x-x^U)+y, gives
\[
Q_{3,k}\ge L_{k,U}:=\mathscr P_k(b,x^U)
-\mathcal R_k(x^U,E+B(U)).
\tag{19}
\]
This is the precise compact-reference diagnostic to freeze at U=2.
Both the infinite mode tail and spatial exterior are paid in the same
joint residual. No Green identity on a truncated spatial domain is used,
so no artificial U-boundary term is silently deleted. Numerical errors
in acquiring x^U remain separate. Equation (11) concerns the exact
infinite first-mode reference; it is not a quadrature-error claim.

**Decision:** retain this one primary candidate for one bounded
feasibility diagnostic. The sufficient test is L_(k,2)>0 from (19) at exactly
k=1,4, with the fixed conservative E in (6). No sign of the reference polynomial, no
positive gap, and no numerical feasibility is presumed. A fixed
[E03 request r1][packet] supplies U=2, moments 0,...,7, precision and
work caps, and actions for pass, fail or inconclusive outcomes. A
floating pass will require a separately issued rigorous E02 acquisition
before (15) can be called a positive bound. The packet first requests
E04's analytical assessment; execution belongs to Sol under the
[model workflow][workflow].

The k=2,3 transition, all k>=5, quantitative behavior as k grows, and
all higher determinant orders remain unassessed. At order r the same
algebra has degree 2r, and boundary ranks and conditioning change. No
uniform ratio of the error to the determinant margin is supplied.
Accordingly B03 is not ready merely because the tail moments are small.

## 6. Claim-specific controls and evidence limits

| Claim or control | What this attempt actually uses or establishes |
| --- | --- |
| Tail estimate (6), gain (11), polynomial payment (15) | Proved estimates in this note, proof-author checks only. The scalar gain has an explicit number; the determinant lower bound has no established positive sign. |
| Canonical source | Complete unit square coefficients and exact reflection-normalized b. The joint polynomial theorem itself is generic; the input reference and error vector are source-specific. |
| Weighted-square collision controls | Unit coefficients are changed; the reference, endpoint sum and E must be recomputed. No uncalculated failure of their finite-order L test is asserted. |
| Euler-factor controls | Shifted source is not this literal canonical square expansion. Generic Green transfer survives, but these canonical input bounds cannot be imported unchanged. |
| Reflected and smooth positive-primitive controls | They lack the literal complete unit-square expansion used in (5)–(8); positive primitives and endpoint normalization alone do not provide (6). |
| A control that happens to meet the same quantitative input box | Estimate (15) applies to it as well. Finite-order time-zero positivity can coexist with a positive-time collision; that is no contradiction. |
| Failure of the finite sufficient test | Would reject this conservative first-mode residual payment for the specified cases, not the actual determinant sign, all correlated estimates, or the radial program. |

No existing collision certificate was rerun: this is a premise screen for
a time-zero finite-order comparison, not a claim to reject their
positive-time events. The inherited 25-case [exact record][record] was
read and its recorded [checker][checker] hash matches the current script.
It checks normalization only and was not counted as a new result.
Equations (11), (16), (17) and (18) received direct analytical checks by
the proof author; no separate review or interval calculation has occurred.

**Return disposition:** B01 completes with an explicit surviving
obligation and a fixed diagnostic, not an unsupported positivity
conjecture. No global result-summary or avoid entry is added before a
qualifying assessment; no investigation closure or manuscript milestone
is claimed. Continue using the [model-change note][continuation] and the
[sole live register][progress].

## Input versions

All hashes are SHA-256 of the files read on 4 November 2026; these include
working-tree files, so no clean committed snapshot is implied.

| Input | SHA-256 |
| --- | --- |
| Overview / issued B01 r1 | `597255ffe3edc41e6f35705ed6337d8e07e9281931bc3acbf645a2d2dcfdfa9f` |
| Inherited brainstorm Note06 | `84eb64db229bf679ca7530cfa41bf97eafe382a4462fad18c83509a0d30af452` |
| Exact checker | `135601240e921764839f1791fee3261b43f96c4f68ce95da2770821b073bb6b3` |
| Exact 25-case record | `5cca5e1a614028a64217f703133b97aa87bcbb445d23f100ee1085182aaa7d49` |
| Jensen accepted Review01 | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
| Parent initial balance note | `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` |

[overview]: ../research-overview/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_OVERVIEW_20261104.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[packet]: ../research-progress/handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md
[continuation]: ../research-progress/handoffs/02_RGD_CONTINUATION_AND_MODEL_CHANGE_20261104.md
[refs]: ../references/README.md
[lowerreview]: ../../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[parentbalance]: ../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[record]: ../../brainstorm/numerics/RADIAL_GREEN_DETERMINANT_CHECK_20261104.json
[checker]: ../../brainstorm/numerics/radial_green_determinant_check.py
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[workflow]: ../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[katkova]: https://arxiv.org/html/math/0505174v1
[dlmf]: https://dlmf.nist.gov/20.7.E32
