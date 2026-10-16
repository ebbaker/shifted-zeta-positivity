# Ordered fourth-moment continuation and the refined arithmetic target

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model derivations and audits
are internal validation, not independent specialist review or formal verification.

The three tasks were pursued in the accepted order: source proof audit,
native arithmetic tests, then source-slot and simultaneous-witness
certification. The main constructive consequence is that a sufficiently
fine original source system lowers the common sufficient new fourth saving
from \(1/540\) to \(1/700\). That new moment remains unproved.
The native tests identify why two plausible extensions of the existing
proof do not supply it.

## 1 The refined sufficient theorem

Retain the original native physical rows, inverse and plain profiles,
selected high-conductor bin, and original whole prime slots. In the
operational region, choose the original source system by
[note 19](19_SOURCE_SLOT_WITNESS_CERTIFICATE_20261009.md), with its finite
mesh, global family, profile and witness hypotheses. Then the new theorem
\[
 \boxed{\sum_{u\in\mathcal C_+}
 |M_u|^2|S_u|^4|Q_J(u)|^2
 \ll_\varepsilon U^{1+dr-1/700+\varepsilon}H^b}               \tag{1}
\]
is sufficient for the direct selected-energy implication
\(E\ll_\varepsilon U^{1+dm-s+\varepsilon}H^b\).
This deduction uses the previous spectral Jensen/Cauchy criterion,
actual whole slots, and the witness loss budget; it is not a proof of (1).

The original system can be chosen with maximum slot width \(\ell/4\),
where \(\ell=10^{-6}\), before applying the theorem. Sorted whole inverse
slots give
\[
 \ell/2\le t_I\le3\ell/4,\qquad G_I\ge dx\,z_I.
\]
Choosing a fourth capacity decrement \(\ell/2\) from that same system
gives \(h_J\le3\ell/4\). The continuous budget therefore needs at most
\[
 0.001422030999790405\ldots<1/700,
\]
with exact spare saving \(563861960869/86211772920000000\).
The first inverse capacity has margin at least \(\ell\), and the fourth
capacity has margin at least \(9\ell/4\). The remaining combined witness
loss must be strictly below \(137\ell/200=6.85\times10^{-7}\).
Fixed buffer and upper-envelope costs must fit these real budgets;
they cannot be absorbed into every requested epsilon after being fixed.

No local evaluated slot manifest was found. The primary source does
provide an existential construction with disjoint windows and permitted
finite-ray coefficients. A uniform theorem can use that construction;
absence of a numerical manifest does not invalidate the source argument.

## 2 What the source replay establishes

The [audit](16_SOURCE_FOURTH_MARKED_BRIDGE_20261009.md) follows primary
Lemma 18.1 through both Poisson transforms and its finite induction.
The external envelope step
\(F_J\le\sup|M|^2\sum V_u\) is where the inverse response correlation is
lost. The source's first Gauss-norm interface exposes an actual
Möbius-inverse-plus-two-plain coefficient, which its two-plain theorem
does not cover. Artificial inverse-prime extraction also creates a
variable-specific deletion mask.

The source's equal-product plain cancellation can survive after an inverse
label is fixed. Its missing ingredient is control of the complete signed
inverse-label aggregation and its mixed children. Full positive enlargement
is legal for the original full mixed square, but cannot be applied as
positivity to a signed gcd-filtered remainder. The audit states a sufficient
marked Gauss estimate and all its scope conditions; it does not prove it.

## 3 The two native tests

The [coprime test](17_NATIVE_COPRIME_AND_RESPONSE_TEST_20261009.md) resums
the actual \(g=1\) inverse pair into two reciprocal \(L\)-functions and
an exact collision correction. For good Eisenstein primes that correction
is nonvanishing when both Mellin real parts exceed \(1/2\).
The permitted buffered contours reproduce the pointwise inverse exponent.
An absolute contour bound with a fixed saving would move below the bin
parameter, where a matching presentation may have a witnessed zero.
The correction cannot remove that pole. A signed selected average or
an oscillatory estimate is still needed.

The [annular test](18_NATIVE_ANNULAR_DIAGONAL_TEST_20261009.md) shows that
complete convolution cancellation does not improve the positive mixed
coefficient norm. Products of one prime of norm comparable to \(D\) and
two distinct primes of norm comparable to \(N\) have only one admissible
inverse divisor and coefficient \(-2A_0B B\). The inherited prime ideal
theorem gives squared coefficient norm
\(\gg DN^2/(\log U)^3\). The standard equal-product plain comparison is
zero on that subset.

Thus the unchanged separate positive second-diagonal majorant cannot
close even the refined target: its budget gap is greater than
\(363/1750\). This is a majorant obstruction, not a lower bound for the
full Gauss norm or selected energy. It is a no-prime-slot prototype for
the uniform coefficient class and zero-slot children; specialized
nonempty slot arguments require their own analysis.

## 4 The next arithmetic task

Keep the controlled high-gcd reduction and completion from notes 14–15.
With \(G_0=cU^{1/125}\), the remaining signed selected form still has
\(Ng<G_0\), original balanced annuli, and
\(Nf>U^{2r-2/125}\). Its positive part now needs the exponent in (1).
The old removals have more reserve against this weaker target.

A useful direct proof should preserve the entire artificial coprimality
Möbius combination in the first transformed bilinear kernel before the
Cauchy/absolute-label step creates separate positive Gauss norms.
A proof only for \(g=1\) is an initial test, not a bound for the full
low-gcd aggregate. The exact coefficient norm test rules out expecting a
power gain merely from complete \(\mu*\mathbf1*\mathbf1\) cancellation
inside each separated annular coefficient.

The positive alternative is the weighted inverse-response tail from
note 17, with \(\chi=1/700\). In the source's arbitrarily small-loss
ordering, it suffices to show
\[
 \sum_{\substack{u\in\mathcal C_+\\
       |M_u|^2>U^{dr-2/700}}}|S_u|^4|Q_J(u)|^2
       \ll U^{1-1/700+\varepsilon}H^b.
\]
At an already fixed inverse buffer \(\rho=12e\), its required mass saving
is instead \(1/700+\rho r\), with any additional allocation margin.
The exact integrated-tail criterion is weaker than this single-cutoff
condition. Existing unweighted moments do not prove either correlation.

Complete bin coverage and the global family-boundary reuse remain separate
after a mixed theorem closes. A zeta-only strip does not supply the
native family package.

## 5 Saved evidence

The [checker](../../numerics/check_mixed_marked_bridge.py) and
[small record](../../numerics/mixed_marked_bridge_record_20261009.json)
contain 215 exact assertions for local Euler algebra, complete versus
annular coefficient identities, contour and diagonal ledgers, layer
integration, prefix margins, and the refined sufficient saving. They
hash the checker and earlier operational record. They do not prove
native reciprocity, the prime ideal theorem, source analytic lemmas,
the mixed correlation, or a new zero-free boundary.

The primary source was read in memory, with SHA-256
8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.
No third-party PDF or large derived output was saved in the repository.

