# J-B02 global tail proof and compact certificate decision

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**.

**Decision:** keep the original global pair \(R'>0,K\ge0\). An explicit
analytical bound below proves both signs for \(t=\pi e^{4u}\ge128\),
which includes every \(u\ge1\). The remaining interval is assigned a
finite certificate using complete joint numerators, exact removal of
the origin zeros, and amplitude normalization. All truncation and
Taylor remainders are specified. **The compact signs have not been
certified, so the global signed-averaging application remains conditional.**

This completes J-B02's present proof-strategy decision under
[Continuation08][continuation08]. The [owning register][progress] holds
status. The tail proof and certificate design are in-note analytical
work, awaiting execution audit; they have no independent specialist
review. Neither the source nor the sufficient condition has changed.

| Next task | Type | Recommended model and reason | Readiness | Output |
| --- | --- | --- | --- | --- |
| **J-E02 r1, Section 7** | E | Sol; fixed algebra, bounds and finite certificate | Ready, issued and unstarted | Full sign certificate, a certified counterpoint, or a precisely unresolved bounded return |
| J-E03 | E | Sol; assess a completed fixed claim | Gated by a complete E02 sign proof | Assessment of bounds, coverage, controls and transfer |
| Return to J-B02 | B | Astra; a failed sign or exhausted allowance needs a decision | Only on E02 failure or unresolved coverage | Scoped disposition without automatic enlargement |

Read with the [result index][results], [theta identities][theta] and
[controls][controls], and the [avoid index][avoid]:
[target classification][reformulations], [joint bounds][joint],
[numerics before a question][numerics-first], [scoped exclusions][scopes]
and [status strength][status]. This is a fixed-order structural target.
The prospective gain is the normalized index comparison in [Return07][r2],
not a new order-three coefficient range or an increasing-order/RH result.

## 1. Fixed target and choice of method

Retain the complete canonical even source at physical heat time zero:
\[
\phi_j(u)=\Phi^{(j)}(u)=e^u\sum_{n\ge1}P_j(n^2t)e^{-n^2t},
\quad t=\pi e^{4u},\quad P_0(t)=2t^2-3t,
\quad P_{j+1}=4tP_j'+(1-4t)P_j.
\tag{1}
\]
Keep \(b_k=\int_0^\infty u^{2k}\Phi(u)du\), \(c_k=b_k/(2k)!\),
\(\gamma_k=k!c_k\), and the original definitions
\[
R=\phi_2/\phi_0,\quad T=\phi_4/\phi_0,\quad
C=R'T''-T'R'',\quad K=R'C'-3CR''.
\]
The source is positive on the closed real half-line, since \(t\ge\pi>3\)
and every summand of \(\phi_0\) is positive. The r1 negative origin
\(C\) and r2 positive origin/tail \(K\) remain unchanged.

| Route considered | Remaining difficulty | Decision |
| --- | --- | --- |
| Positivity of the 579-term Jacobi numerator on an invariant orbit region | A suitable invariant region and its sign certificate have not been supplied; source identification alone does not sign that polynomial | Retain as an alternative; no impossibility claim |
| Complete theta series with joint numerators, explicit tail and a compact certificate | Two scalar signs on a specified finite interval, with stated analytic errors | Selected; keeps the actual canonical coefficients and directly tests the unchanged pair |

The second route is not a point-sampling argument. Each accepted cell
must cover a closed interval with rigorous errors. An uncovered cell
prevents a global conclusion.

## 2. Joint numerators and exact removal of origin zeros

For a jet vector \(q=(q_0,\ldots,q_7)\), define
\[
\begin{aligned}
\mathcal A(q)&=q_0q_3-q_1q_2,&
\mathcal B(q)&=q_0q_4-q_2^2,\\
\mathcal W(q)&=\det\begin{pmatrix}q_0&q_1&q_2\\q_2&q_3&q_4\\q_4&q_5&q_6\end{pmatrix},&
\mathcal W_1(q)&=\det\begin{pmatrix}q_0&q_1&q_3\\q_2&q_3&q_5\\q_4&q_5&q_7\end{pmatrix},\\
\mathcal N(q)&=q_0\mathcal A(q)\mathcal W_1(q)
 -3\{q_0\mathcal B(q)-q_1\mathcal A(q)\}\mathcal W(q).
\end{aligned}
\tag{2}
\]
For actual source jets, \(\mathcal A'=\mathcal B\) and
\(\mathcal W'=\mathcal W_1\): differentiating either of the first two
columns of the determinant creates a repeated column. Quotient
algebra then gives
\[
R'=\frac{\mathcal A(\phi)}{\phi_0^2},\qquad
C=\frac{\mathcal W(\phi)}{\phi_0^3},\qquad
K=\frac{\mathcal N(\phi)}{\phi_0^6}.
\tag{3}
\]
In particular, this is the same \(K\), not a replacement sign condition.
The coefficient absolute sums of \(\mathcal A,\mathcal B,\mathcal W,
\mathcal W_1\) are at most \(2,2,6,6\). Hence that of \(\mathcal N\)
is at most \(2\cdot6+3(2+2)6=84\). Its monomials have ordinary degree
six and weighted degree thirteen when \(q_j\) has weight \(j\).
\(\mathcal A\) has degree two and weight three.

Full evenness of \(\Phi\), together with the regular identities in r2,
makes
\[
\mathcal U(u)=\frac{\mathcal A(\phi(u))}{u},\qquad
\mathcal V(u)=\frac{\mathcal N(\phi(u))}{u^5}
\tag{4}
\]
analytic even functions at zero. Their values are
\[
\mathcal U(0)=2\Phi(0)^2\widehat R'(0)>0,\qquad
\mathcal V(0)=32\Phi(0)^6J(0)>0.
\tag{5}
\]
Thus the coefficients below degree five in \(\mathcal N(\phi(u))\)
vanish identically. These cancellations are imposed as exact identities
before interval evaluation. They are justified for the full even source;
**a finite theta sum is not itself even and cannot be treated that way.**
For \(u>0\), positivity of (4) proves the original pair through (3).

## 3. Explicit tail with a complete error payment

Write \(M_j\) for the coefficient absolute sum of \(P_j\). Since
\(\deg P_j=j+2\),
\[
M_0=5,\qquad M_{j+1}\le(4j+13)M_j,
\qquad M_j\le5\,64^j\quad(0\le j\le7).
\tag{6}
\]
A convenient common arithmetic bound is
\[
\mathcal S=\sum_{n\ge1}n^{18}e^{-(n^2-1)}<2^{23}.
\tag{7}
\]
Here is an elementary rational verification. Replace \(e\) by its lower
bound 2. The terms \(n=1,\ldots,7\) are bounded above by
\(1,2^{15},2^{21},2^{21},2^{18},2^{12},2^3\).
The \(n=8\) term is \(2^{-9}\); all subsequent ratios are at most
\((9/8)^{18}2^{-17}<2^{-13}\). The resulting geometric tail is less
than \(2^{-8}\), and the whole bound is less than \(2^{23}\).
Consequently the constants in Return07's differentiated remainder obey
\[
B_j=\sum_{n\ge2}n^{2j+4}e^{-(n^2-4)}<e^3\mathcal S<2^{28}
\quad(0\le j\le7).
\tag{8}
\]

Let \(f_j=\phi_j/\phi_0\), \(f_{j,1}=\phi_{j,1}/\phi_{0,1}\), where
subscript 1 means the first theta summand. From the differentiated
series, for \(t\ge3\),
\[
|\phi_j-\phi_{j,1}|\le e^u M_jB_jt^{j+2}e^{-4t},\qquad
\phi_0\ge\phi_{0,1}\ge e^ut^2e^{-t}.
\]
Set \(\eta_j=f_j/(64t)^j\) and \(\eta_{j,1}=f_{j,1}/(64t)^j\).
The quotient error, including its denominator contribution, satisfies
\[
|\eta_{j,1}|\le5,\qquad
|\eta_j-\eta_{j,1}|\le30\,2^{28}e^{-3t}<2^{33}e^{-3t}.
\tag{9}
\]
For \(t\ge128\), both vectors have absolute coordinates below 6.

For clarity, a complete polynomial bound for \(K\) can be written using
\[
\begin{aligned}
a&=f_3-f_1f_2,\quad
b=f_4-2f_1f_3-f_2^2+2f_1^2f_2,\\
c&=f_5-3f_1f_4-4f_2f_3+6f_1^2f_3+6f_1f_2^2-6f_1^3f_2,\\
d&=f_5-f_1f_4,\quad
e=f_6-2f_1f_5-f_2f_4+2f_1^2f_4,\\
f&=f_7-3f_1f_6-3f_2f_5-f_3f_4
 +6f_1^2f_5+6f_1f_2f_4-6f_1^3f_4.
\end{aligned}
\]
Then \(K=a^2f-adc-3abe+3db^2\). The polynomial has weighted degree
13, ordinary degree at most 8 and coefficient absolute sum at most
\(104+104+216+216=640\). On the coordinate box of radius 6 its
Lipschitz constant for the maximum norm is at most
\(8\cdot640\cdot6^7<2^{31}\). The corresponding constant for \(a\)
is 13. Apply these identities before factoring out the common weighted
scale \(64t\). Equation (9) gives
\[
|R'-R_1'|<2^{55}t^3e^{-3t},\qquad
|K-K_1|<2^{142}t^{13}e^{-3t}.
\tag{10}
\]
This coarser tail power is sufficient at the chosen cutoff; no derivative
of an unspecified remainder is used.

Use the exact first-summand formula from [Return07, (9)][r2]:
\[
R_1'=128t^2-352t-\frac{192t}{(2t-3)^2},\qquad
K_1=\frac{3\cdot2^{26}t^5p(t)}{(2t-3)^7}.
\]
For \(t\ge128\), discarding the positive lower coefficients of its
recorded degree-nine \(p\) gives
\[
\frac{p(t)}{t^9}\ge2048-\frac{32768}{t}
-\frac{1034304}{t^3}-\frac{5589360}{t^5}
-\frac{6180300}{t^7}-\frac{654885}{t^9}
>2048-256-4>1024.
\]
Thus \(R_1'>64t^2\) and \(K_1>3\cdot2^{29}t^7\).
The functions \(te^{-3t}\) and \(t^6e^{-3t}\) decrease for \(t\ge128\).
Since \(e>2\), (10) implies
\[
\frac{|R'-R_1'|}{t^2}<2^{-322},\qquad
\frac{|K-K_1|}{t^7}<2^{-200}.
\]
We obtain the explicit analytical conclusion
\[
\boxed{t\ge128\ \Longrightarrow\ R'(u)>63t^2,\quad K(u)>2^{30}t^7.}
\tag{11}
\]
In particular this covers \(u\ge1\): \(\pi>3\) and the Taylor sum
for \(e^4\) through degree six gives \(e^4>43\), so \(\pi e^4>128\).
The remaining proof domain can therefore be fixed as \(0<u\le1\).

## 4. Origin polynomial with an explicit analytic remainder

Fix
\[
\varepsilon=1/64,\qquad \rho=1/8,\qquad m=63.
\]
For every real center \(c\in[0,1]\), the source is holomorphic on a
neighborhood of \(|z-c|\le1/4\). Indeed, writing \(t=\pi e^{4z}\),
\[
|t|>1,\quad \Re t\ge|t|/2,\quad |e^z|<4.
\]
The inequalities follow from \(\pi>3\), \(e<3\),
\(\cos(4\Im z)\ge1/2\), and \(e^{5/4}<4\).
For \(y=n^2|t|\),
\((2y^2+3y)e^{-y/4}\le76\), so normal convergence and
\[
|\Phi(z)|\le4\cdot76\sum_{n\ge1}e^{-n^2/4}
\le4\cdot76\cdot4=1216<2^{11}
\tag{12}
\]
hold. Cauchy's derivative bound then gives, on \(|z-c|\le\rho\),
\(|\phi_j(z)|\le2^{11}j!\rho^{-j}\).
Using the degrees and coefficient sums in (2), together with
\(\prod j_i!\le(\sum j_i)!\), gives
\[
|\mathcal A(\phi(z))|<2^{35},\qquad
|\mathcal N(\phi(z))|<2^{145}.
\tag{13}
\]
Let \(A_{\le63},N_{\le63}\) be their full-source Taylor polynomials
at zero. Exact parity and the vanishing below degree five make
\(A_{\le63}/u\) and \(N_{\le63}/u^5\) polynomials in \(x=u^2\), of
degrees at most 31 and 29. For \(0\le u\le\varepsilon\), Cauchy's
geometric remainder yields
\[
\left|\mathcal U(u)-\frac{A_{\le63}(u)}u\right|
\le\frac{2^{35}\rho^{-1}(\varepsilon/\rho)^{63}}{1-\varepsilon/\rho}
<2^{-150},
\tag{14}
\]
\[
\left|\mathcal V(u)-\frac{N_{\le63}(u)}{u^5}\right|
\le\frac{2^{145}\rho^{-5}(\varepsilon/\rho)^{59}}{1-\varepsilon/\rho}
<2^{-16}.
\tag{15}
\]
At zero the quotients and errors mean their analytic continuations.
These are absolute bounds, not assertions that either polynomial is
positive on this interval.

**Coefficient acquisition.** Retain exactly 24 theta summands. On
\(|z|\le1/4\), the omitted source satisfies
\[
|\Phi(z)-\Phi_{24}(z)|
\le304\sum_{n\ge25}e^{-n^2/4}<2^{-146}.
\tag{16}
\]
The first term is less than \(2^{-156}\), successive ratios are less
than \(2^{-12}\), and \(304<2^9\), proving the displayed bound.
For the full Taylor coefficient \(a_j=[u^j]\Phi(u)\), the error after
using \([u^j]\Phi_{24}\) is less than \(2^{-146+2j}\). Acquire only
\(a_0,\ldots,a_{70}\), using (1) and division by \(j!\). Set odd
coefficients to their exact full-source value zero. These suffice for
\([u^{\le63}]\mathcal N(\phi)\), which uses derivatives through seven.
Coefficient balls include (16) and rounding. Form the full polynomials
before bounding their ranges. Remove only the symbolically proved
zero coefficients; do not set a small computed coefficient to zero.

The origin proof obligation is now a finite pair of polynomial lower
bounds on \(x\in[0,1/4096]\), exceeding (14)–(15). It has not been
executed. The derivative order 70 serves this fixed Taylor approximation;
it introduces no new source-curvature condition and requires no Q70
Jacobi polynomial generation.

## 5. Normalized compact interval and all omitted terms

On \(\varepsilon\le u\le1\) use normalized jets
\[
\nu_j(u)=\frac{e^{t-u}\phi_j(u)}{64^jt^{j+2}}
=\frac1{64^j}\sum_{n\ge1}e^{-(n^2-1)t}
 \sum_{\ell=0}^{j+2}p_{j\ell}n^{2\ell}t^{\ell-j-2},
\quad P_j(t)=\sum_\ell p_{j\ell}t^\ell.
\tag{17}
\]
Here \(j\le7\). The common source amplitude and weighted scaling are
positive on the real axis. Homogeneity gives
\[
R'=(64t)^3\frac{\mathcal A(\nu)}{\nu_0^2},\qquad
K=(64t)^{13}\frac{\mathcal N(\nu)}{\nu_0^6},\qquad \nu_0>1.
\tag{18}
\]
This removes the very small factor \(\Phi^6\) before compact evaluation.
The normalized jets are not ordinary derivatives of \(\nu_0\); (18)
uses polynomial homogeneity, not a substituted derivative recurrence.
Do not first compute a high Taylor jet of \(\Phi\) and then multiply
by \(e^{t-u}\): that would reintroduce the cancellation removed in (17).
Compute Taylor series directly from the right-hand side, with
\(t(c+s)=t(c)e^{4s}\). In particular the first summand is a finite
combination of exponentials in \(s\).

For \(c\in[\varepsilon,1]\), \(|z-c|\le\rho\) gives
\(|t|>3/2\) and \(\Re t>1\), since \(\cos(1/2)\ge7/8\).
Equations (6)–(7) therefore imply
\[
|\nu_j(z)|<5\mathcal S<2^{26}.
\]
The same bound holds for the 24-term truncation \(\nu^{[24]}\), and
\[
|\mathcal A(\nu^{[24]})|<2^{53},\qquad
|\mathcal N(\nu^{[24]})|<2^{163}.
\tag{19}
\]
The omitted normalized source jets satisfy uniformly on these disks
\[
|\nu_j-\nu_j^{[24]}|
\le5\sum_{n\ge25}n^{18}e^{-(n^2-1)}<2^{-530}.
\tag{20}
\]
For (20), the first term before multiplying by 5 is less than
\(2^{90-624}=2^{-534}\); successive ratios are less than \(2^{-33}\).
The degree/coefficient bounds in (2) give Lipschitz constants at most
\(2^{28}\) and \(6\cdot84\cdot2^{130}<2^{139}\). Thus
\[
|\mathcal A(\nu)-\mathcal A(\nu^{[24]})|<2^{-502},\qquad
|\mathcal N(\nu)-\mathcal N(\nu^{[24]})|<2^{-391}.
\tag{21}
\]
This pays for the infinite theta tail after the complete signed
expression has been formed; no summand sign is inferred.

Partition \([\varepsilon,1]\) initially into the 126 closed cells
\([m/128,(m+1)/128]\), \(m=2,\ldots,127\). Their half-width is
\(h=1/256\). Use the degree-63 Taylor polynomials of the two truncated
numerators at each cell center. Cauchy's bound (19) gives respective
Taylor errors
\[
E_A(h)=\frac{2^{53}(h/\rho)^{64}}{1-h/\rho}<2^{-266},\qquad
E_N(h)=\frac{2^{163}(h/\rho)^{64}}{1-h/\rho}<2^{-156}.
\tag{22}
\]
Use the actual half-width in this formula after subdivision. Rounding
is carried in the polynomial coefficient balls. The full lower bounds
are the polynomial lower bounds minus (22) and (21). Bernstein
coefficients on each real cell provide a sufficient polynomial lower
bound: the Bernstein basis is nonnegative and sums to one. All
coefficient conversion and comparisons must be outward rounded.

The joins are exact: the origin interval ends at \(1/64\), these cells
start there and end at 1, and (11) covers \([1,\infty)\). The signs on
both finite pieces remain unpaid until a certificate is returned.

## 6. Scope and controls

The new analytical result is the effective tail (11), together with a
finite, explicit certification route. It is not yet the global estimate.
If the compact proof succeeds, [Return07][r2] transfers it to
\(A_{k+\ell}\ge A_k\ge48c_0^3/Z_0>0\) for all finite integer
\(k,\ell\ge0\), at determinant order three. Its order-three positivity
is already known; the proposed additional structure is normalized index
monotonicity. No novelty claim or induction in determinant order is made.

The analytical control screen remains scoped to that claim:

| Control | Actual premise affected |
| --- | --- |
| Euler-factor sources | Changed translates and weights do not have the exact canonical expansion (1); the numerical constants and remainder payment here cannot be imported unchanged |
| Weighted-square and finite-prime perturbations | Changed coefficients fail (1); finitely matched endpoints do not supply the full evenness needed in (4) and (16) |
| Reflected super-Gaussian sources | Evenness permits formal origin cancellation, but the canonical series, first-mode formula and tail bounds used here are absent |
| Smooth shape and positive-primitive sources | Their shape/primitive data supply neither the canonical series nor these quantitative bounds |
| Gaussian | The generic polynomial identity gives \(\mathcal N=0\), consistent with the equality case of the conditional transfer; it is not required to satisfy the strict canonical certificate |

No uncomputed control sign is asserted. This finite-order argument may
accept a source with other nonreal zeros; it is not a universal collision
exclusion. No collision numerics, source grid, or compact certificate was
run in this B round. No new external theorem is imported: the new bounds
use the existing exact theta series, elementary polynomial algebra,
Cauchy's coefficient bound and geometric sums.

## 7. Frozen execution request J-E02 r1

**Parent:** J-B02. **Type:** E. **Recommended model:** Sol; the target,
source, formulas, errors, domain and finite limits are fixed. Issued
1 November 2026 for Edward Baker by **gpt-6-astra / max**. This request
is issued, not dispatched or executed. The actual executor records its
own model and effort. The original J-E01 requests and records stay frozen.

**Inputs.** This note and [Return07][r2], [Continuation08][continuation08],
[Note05][decision], its [r2 exact record][record] and program; the live
register, root model workflow and large-file policy. Record this note's
hash at execution. Preserved input hashes are:

| Input | SHA-256 |
| --- | --- |
| Note05 | `32f8289741bac117b45399855558b554e1f1430adc7169a8229bfd69448e3cf2` |
| Return07 | `202a37845f602efd56c8d11935cb8256c665edbaaae421b1b2fed14c186e97d2` |
| Continuation08 | `511ea166478a7904e978fd5b62f2c2b132fc479c549a72510c621904afb183ff` |
| j_e01_r2_audit.py | `aefcae5a3b0f9ea2ef6033c5daeb70396becdb47262eb01859a23554616900cc` |
| J_E01_R2_EXACT_RECORD_20261101.json | `9d2c6b008cebda9138537011295aa167d4c6e21d57edb491a89751e95452d5f4` |

**Fixed work in order.**

1. Audit (2)–(22), including every constant, polynomial homogeneity,
   complex disk, omitted tail and join. Check (3) against the r2 K
   expression and check the Gaussian identity \(\mathcal N=0\).
   Reproduce the effective tail (11) as an exact analytical proof.
   Reuse r2's accepted signed-averaging proof; do not rederive unrelated
   coefficient baselines. A bounded correction preserving the source,
   target and declared limits is permitted and must be documented.
2. With outward-rounded ball arithmetic, acquire the origin coefficient
   balls from exactly 24 terms through \(a_{70}\), using (16), full
   evenness and the exact low-order cancellations. Generate at most
   P0–P70; no Q beyond the preserved Q10 is needed. Form the two
   polynomials in \(x\) and bound them on \([0,1/4096]\), paying
   (14)–(15). Check (5) against the inherited origin formulas.
3. On the specified 126 initial cells, form degree-63 Taylor series
   directly from (17), using only P0–P7 and exactly 24 terms. Form the
   complete numerators (2), convert their interval coefficient
   polynomials to Bernstein form, and pay (21)–(22). Certify strict
   positivity on every cell, or retain its unresolved status.
4. Assemble coverage, normalization and the conditional consumer.
   If all cells pass, state precisely the resulting global pair and
   normalized index comparison. No theta-minor or Z_k quadrature is
   needed. If a negative value is suspected, only a rigorous full-source
   upper bound below zero at a tested dyadic center is a counterpoint.

**Arithmetic and finite limits.** Use an available outward-rounded ball
library such as Arb, recording its version, or exact rational enclosures
of the same functions. Floating values alone cannot accept or reject a
sign. Start at 128-bit precision; one refinement to 256 bits is allowed
for unresolved cells or coefficient acquisition. No precision above 256,
Taylor degree above 63, retained term beyond 24, or P order above 70 is
part of r1. The origin polynomial interval may be bisected to at most 64
leaves and depth six. Middle cells may be bisected to depth at most eight
from their initial cells, with at most 4096 current leaves in total.
Recompute Taylor coefficients at new centers as needed within these caps.
Allow at most 30 minutes of arithmetic execution, recording actual time;
stop earlier on a certified failed required sign. Audit and write-up are
separate from that execution limit. If outward rounding is unavailable,
report the dependency rather than substituting uncertified arithmetic.

**Acceptance and stop.** A complete global certificate requires both
finite pieces and the audited infinite tail, with strictly positive
lower bounds after all errors. A certified negative K or nonpositive
R' witness rejects the corresponding original premise only when the
stated inequality is rigorously established; an interval containing zero
is unresolved. A zero K is compatible with K>=0 and may defeat this
strict certificate without refuting the original hypothesis. Reaching
any cap, losing a required identity, or leaving any cell unresolved is
a bounded return, not permission to widen the campaign. Return those
cases to **[B] J-B02 — Astra**. A complete global proof proceeds to
**[E] J-E03 — Sol** for assessment; mandatory Astra approval is not added.

**Outputs and allowed changes.** Save one return in `01_jensen/notes/`, new
programs and small records in `01_jensen/numerics/`, and any assessment in
`01_jensen/reviews/`. Preserve all prior notes, programs and records. Record
actual model/effort, input/code hashes, arithmetic, precise cell cover,
error budgets, positive margins, failed/unresolved cells, corrections and
runtime. The replay record must distinguish algebra, interval proof and
unresolved observations. Keep individual repository files below the
large-file limit; place bulky regenerable coefficient payloads outside
Git with a small receipt and replay instructions. Update only the owning
J register, relevant navigation and this chat's uniquely registered
history. Model change does not confer independent review.

**Next: [E] J-E02 r1 — Sol.** The [continuation note][handoff] supplies
reading order and a pasteable model-change prompt. No research execution
has been performed under this new contract.

[continuation08]: 08_CONTINUATION_FOR_ASTRA_GLOBAL_SIGNED_AVERAGING_20261101.md
[r2]: 07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md
[decision]: 05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md
[record]: ../numerics/J_E01_R2_EXACT_RECORD_20261101.json
[handoff]: 10_CONTINUATION_FOR_SOL_GLOBAL_SIGN_CERTIFICATE_20261101.md
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[reformulations]: ../../../../../avoid/01_restating_the_target.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[numerics-first]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[status]: ../../../../../avoid/06_status_stronger_than_the_evidence.md
