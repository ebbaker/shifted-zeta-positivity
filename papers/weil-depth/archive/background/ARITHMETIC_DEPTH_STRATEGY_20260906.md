# Increasing arithmetic depth: structural assessment and a small-shift continuation lemma

6 September 2026. Working research note for author review, not a manuscript or an independent audit of the inherited computer-assisted proofs.

## Main assessment

The most useful generalization is to separate two tasks:

1. Prove coercivity of the **central, prime-active Weil form** at increasing finite depth, and convert it to small-shift contraction by a general analytic lemma.
2. Develop **cumulative storage inequalities** for larger shifts and for a bulk realization with memory. Positivity of the instantaneous generator throughout a fixed shift interval is unnecessary and already fails in the second slab.

This change of organization has an immediate consequence. The existing second-slab endpoint certificate implies, by the analytic argument below,

\[
\boxed{\|V_{\omega,L}\|\le \exp(-2\times10^{-10}\omega)<1,
\qquad 0<\omega\le4\times10^{-5},\quad 0<L\le\log3.}
\]

This is a new **analytic corollary of the existing working certificate**, with the same inherited numerical and analytic qualifications. It enlarges the endpoint cutoff by about 286, with a weaker displayed contraction margin. It does not connect to the interior interval beginning at 0.05, increase the certified depth, or prove RH.

A second useful deduction concerns the ultimate target: a sequence of exact finite-horizon contractions with **depths tending to infinity and shifts tending to zero** is sufficient for RH through the central Weil criterion. A depth-independent shift interval or positive gap is not necessary for this implication.

## 1. What the supplied work establishes

| Component | Present role | Qualification |
|---|---|---|
| Shifted string paper | Identifies the Stieltjes/Weyl and positive-string interpretation of shifted zeta data | The positivity hypotheses have not been removed |
| Screw-function margin paper | Quantifies the margin and how a hypothetical forbidden zero becomes visible | A long positive time window is not an all-time criterion |
| Spectral defect-depth paper | Gives finite-resolution diagnostics and explains delayed detection in controlled defect models | Moment/string depth is not automatically the logarithmic arithmetic horizon |
| First slab, total length at most log(2) | Supplies the generator/energy mechanism, archimedean structure, and finite-tail techniques | The supplied audit leaves a corrected primary-Arb rerun unresolved; its conditional numerical repairs are not a completed independent certificate |
| Second slab, total length at most log(3) | Demonstrates positive cumulative contraction despite an indefinite instantaneous generator | Supplied exact-operator working coverage is (0, 1.4e-7] and [0.05, 0.3] |
| Endpoint parity pencils | Expose the weak directions and preserve the complete omitted-output Gram | Pencil positivity through 0.05 is not exact-operator positivity there |

The first-slab preprint states a result throughout 0 < omega <= 1/2. Its audit qualifications must accompany that statement. The second-slab norm certificates reconstruct their own matrices and do not depend on the disputed archived central first-slab matrix enclosures.

The second-slab obstruction is particularly informative: at omega = 1/4 and L = 1 a certified polynomial direction has negative generator form, while the contraction/storage theorem holds at that same shift and horizon. Thus the failure of a stronger proposed mechanism is compatible with success of the desired finite-depth positivity.

## 2. Exact arithmetic algebra at arbitrary finite depth

Let the total interval be (0,L), let

\[
(T_a f)(x)=\mathbf1_{x>a}f(x-a),\qquad T_aT_b=T_{a+b},
\]

and take T_a = 0 when a >= L. Write V^gamma for archimedean causal convolution. Suzuki's coefficients give the exact finite-horizon factorization

\[
V_{\omega,L}=B_{\omega,L}V^\gamma_{\omega,L},\qquad
B_{\omega,L}=\sum_{\log n<L}b_\omega(n)T_{\log n},
\]

\[
b_\omega(n)=\frac{n^\omega}{\sqrt n}
\prod_{p\mid n}(1-p^{-2\omega}),\qquad b_\omega(1)=1.
\]

The following identities are direct deductions from that coefficient formula. They do not use zero locations or a positive spectral measure. The source normalization is [Suzuki, equations (2.1)-(2.4) and Section 3.1](https://arxiv.org/pdf/1204.1827).

### 2.1 Finite Euler factors

On every finite horizon,

\[
B_{\omega,L}=
\prod_{\log p<L}
(I-p^{-1/2-\omega}T_{\log p})
(I-p^{-1/2+\omega}T_{\log p})^{-1}.
\]

Every inverse is a finite geometric series: sufficiently long products of positive delays vanish. Likewise B-I is nilpotent, so log(B) is a finite polynomial. Consequently

\[
\log B_{\omega,L}
=2\sum_{\substack{n\ge2\\\log n<L}}
\frac{\Lambda(n)}{\sqrt n\log n}
\sinh(\omega\log n)T_{\log n}.
\]

The transfer contains all integers, but its logarithm contains only prime powers. This is the natural distinction between arithmetic interactions and their generators.

### 2.2 General generator

With the convention partial_omega V = -A V,

\[
\boxed{
A_{\omega,L}=A^\gamma_{\omega,L}
-2\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
\cosh(\omega\log n)T_{\log n}.}
\]

Therefore the symmetric generator form is

\[
\boxed{
Q_{\omega,L}=Q^\gamma_{\omega,L}
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
\cosh(\omega\log n)(T_{\log n}+T_{\log n}^*).}
\]

Here Lambda is the von Mangoldt function. Differentiating the finite arithmetic factor, commuting causal factors, and using its bounded inverse proves the identity on the inherited core and form domain. No bounded inverse of the smoothing operator V^gamma is assumed.

At omega = 0 this is precisely the prime-active compact-window Weil form in the project's normalization. Both the gamma form and the symmetric delays commute with midpoint reflection. The generator remains parity diagonal at every depth, although H = VR need not preserve parity away from zero.

The arithmetic perturbations are bounded, generally indefinite, and generally **infinite rank**. Only the gamma shift difference is automatically compact. Neither positive scalar arithmetic coefficients nor parity makes a delay update positive.

### 2.3 The first genuinely different tests

| Newly active integer | New structure just beyond its threshold |
|---|---|
| 3 | A second independent delay; up to L = log(4), every product of two active delays still vanishes |
| 4 | First repeated delay: T_log(2)^2 = T_log(4) |
| 5 | Another primitive prime delay |
| 6 | First product of distinct prime delays: T_log(2) T_log(3) = T_log(6); no new term in the logarithmic generator because Lambda(6) = 0 |

Endpoint delays vanish almost everywhere when log(n) = L. Thus “newly active” means immediately beyond that endpoint.

For example, b_omega(6) = b_omega(2)b_omega(3) exactly. More generally, if r is the number of distinct prime divisors of n,

\[
b_\omega(n)=\frac{2^r}{\sqrt n}
\left(\prod_{p\mid n}\log p\right)\omega^r+O(\omega^{r+1}).
\]

This explains why prime powers appear at first order and mixed-prime products first appear at higher order. A general implementation should derive these identities once instead of treating each slab as an unrelated kernel.

Individual Euler factors do not provide an immediate passive cascade. Already I+bT with b>0 and T^2=0 has norm greater than one: its action on the final member and its preimage of a two-step delay chain produces a two-dimensional triangular matrix of norm greater than one. Contractivity must involve the gamma response and arithmetic interactions together.

## 3. A general central-form continuation lemma

Define

\[
r(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.
\]

The first-slab analytic gamma identity extends to every finite horizon. Combining it with the exact arithmetic formula above gives

\[
Q_{\omega,L}-Q_{0,L}
=C^\gamma_{\omega,L}
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
[\cosh(\omega\log n)-1](T_{\log n}+T_{\log n}^*),
\]

where C^gamma has kernel

\[
[\cosh(\omega|x-y|)-1]r(|x-y|).
\]

In particular, for any fixed finite L and fixed positive bar(omega),

\[
\|Q_{\omega,L}-Q_{0,L}\|\le C_L\omega^2,
\qquad 0\le\omega\le\bar\omega,
\]

where the norm refers to the bounded difference of forms, not either unbounded generator separately. One explicit choice is

\[
C_L=\cosh(\bar\omega L)\int_0^L t^2|r(t)|\,dt
+\frac12\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
(\log n)^2\cosh(\bar\omega\log n)
\|T_{\log n}+T_{\log n}^*\|.
\]

The integral is finite because r(t) = -1/(2t)+O(1). Schur's row bound and

\[
\cosh(\omega t)-1\le\tfrac12\omega^2t^2\cosh(\bar\omega t)
\]

prove the estimate. The delay norms are at most two and can be sharper on short horizons.

**Continuation lemma.** Suppose the complete central form satisfies Q_0,L >= m_L I with m_L > 0, and the generator/strong-limit identities hold for the causal family. Then

\[
\boxed{
\|V_{\omega,L}\|\le
\exp\!\left(-m_L\omega+\frac{C_L\omega^3}{3}\right),
\qquad 0\le\omega\le\bar\omega.}
\]

**Proof.** For positive shift, put u(s) = ||V_s,L f||^2. The energy derivative and bounded form difference give

\[
u'(s)=-2Q_{s,L}[V_{s,L}f]
\le-2(m_L-C_Ls^2)u(s).
\]

Integrate this scalar differential inequality from epsilon to omega, use V_epsilon,L f -> f strongly, and take square roots. The smoothing estimates justify differentiation away from zero; density extends the result to all inputs. No operator-norm derivative at zero is asserted. This is Gronwall's inequality and does not require Q_s to remain nonnegative at every intermediate shift. The common form domain and bounded finite arithmetic factors supply the same regularity mechanism as in the existing energy proof.

For example, if C_L > 0, then

\[
0<\omega\le\min\{\bar\omega,\sqrt{3m_L/(2C_L)}\}
\quad\Longrightarrow\quad
\|V_{\omega,L}\|\le e^{-m_L\omega/2}<1.
\]

Thus one central coercivity certificate gives an explicit interval of positive shifts. Its width may depend strongly on depth. Proving central coercivity remains the difficult arithmetic step; the lemma does not supply it.

## 4. Immediate application to the second slab

### 4.1 Extract the central floor from the existing norm theorem

The supplied endpoint theorem gives

\[
\|V_{\omega,\log3}\|\le1-10^{-9}\omega
\quad(0<\omega\le1.4\times10^{-7}).
\]

For f in a smooth compactly supported core, the weighted-Laplace derivative at zero gives

\[
Q_{0,L}[f]
=\lim_{\omega\downarrow0}
\frac{\|f\|^2-\|V_{\omega,L}f\|^2}{2\omega}.
\]

The norm bound makes the right side at least 1e-9 ||f||^2. Closure in the logarithmic form norm therefore gives

\[
Q_{0,\log3}\succeq10^{-9}I.
\]

The limit is first taken on the core: log-frequency derivative growth is harmless against the rapidly decaying transform of a smooth compactly supported input. The full operator is not norm differentiable at zero. Extending the inequality by form closure avoids that false inference.

This is not circular. The old small-shift norm result was proved by finite matrices and an analytic infinite-dimensional tail. We extract a central inequality from it and then use a different analytic estimate to extend its range.

### 4.2 An elementary uniform perturbation constant

Put L = log(3), d = log(2), and bar(omega) = 1/2. Only n=2 is active and ||T_d+T_d*|| = 1. Since

\[
\frac{e^{-5t/2}}{1-e^{-2t}}\le\frac1{2t},
\]

we have

\[
\int_0^L t^2|r(t)|dt
\le e^{L/2}\frac{L^3}{3}+\frac{L^2}{4}.
\]

Using e^(L/2) = sqrt(3), cosh(L/2) = 2/sqrt(3), and cosh(d/2) = 3/(2 sqrt(2)), this gives

\[
C_L\le\frac{2L^3}{3}+\frac{L^2}{2\sqrt3}+\frac{3d^3}{8}
<\frac{6619}{4800}<\frac32.
\]

The rational comparison uses only L<11/10, d<7/10, and 1/sqrt(3)<3/5. These elementary bounds were checked with exact rational arithmetic; finite lower Taylor sums for exp(11/10) and exp(7/10) suffice to prove the logarithm inequalities.

### 4.3 Resulting range

The continuation lemma yields

\[
\|V_{\omega,\log3}\|
\le\exp\!\left(-10^{-9}\omega+\tfrac12\omega^3\right).
\]

For 0<omega<=4e-5, the exponent is at most -2e-10 omega. Compression gives the same bound on all shorter horizons. Therefore

\[
\boxed{\|V_{\omega,L}\|\le e^{-2\times10^{-10}\omega}<1,
\quad0<\omega\le4\times10^{-5},\quad0<L\le\log3.}
\]

The generator itself is positive at least through 2e-5, since there Q_omega >= 4e-10 I. The larger displayed contraction interval uses the integrated bound. This gives a simple example of using cumulative control analytically.

With the separate inherited interior theorem, the resulting working coverage is

\[
(0,4\times10^{-5}]\ \cup\ [0.05,0.3].
\]

The gap (4e-5,0.05) remains. On the original tiny interval the preceding 1-1e-9 omega estimate is stronger and should be retained. This argument inherits the original certificate's error budgets; it is not a fresh reconstruction or audit of the entire operator certificate.

## 5. The RH-directed target can be diagonal in depth and shift

**Sufficient condition.** Suppose there are L_j -> infinity and omega_j -> 0+, with

\[
\|V_{\omega_j,L_j}\|\le1
\quad\text{for every }j.
\]

Then the central Weil form is nonnegative on every compactly supported smooth test function, and hence RH follows from Weil's criterion.

**Proof.** Fix a finite horizon L and a smooth input f supported inside it. For all sufficiently large j, causal compression gives

\[
\|V_{\omega_j,L}f\|\le\|f\|.
\]

Divide the resulting nonnegative norm defect by 2 omega_j and take j -> infinity. The fixed-L core derivative from Section 4 gives Q_0,L[f] >= 0. Every compactly supported test can be translated into some such interval, and the Weil form is translation invariant through autocorrelation. Thus the full compact-test Weil criterion applies. See [Connes and Consani, introduction and Appendix C](https://arxiv.org/html/2006.13771v1) for the compact-support formulation.

No relation between the rates L_j -> infinity and omega_j -> 0 is needed: the derivative limit is always taken after fixing a test function and its finite horizon. There is also no need for a depth-independent coercivity constant or for strict contraction in this sufficient condition.

This clarifies the research priorities. Closing the full second-slab interval in omega is a useful finite-depth theorem, but it is not a logical prerequisite for studying greater depth or for this route to RH. Proving the entire infinite sequence is, of course, still RH-level work. A finite list of successful slabs does not supply it.

For the stronger physical goal of an explicit global positive bulk with identified boundary response, compatible realizations and their limiting behavior still deserve separate study. The diagonal argument proves a positivity criterion; it does not itself construct that bulk.

## 6. What a storage induction would have to preserve

For a spatial split into an old interval and a new interval, causality always gives

\[
V=\begin{pmatrix}X&0\\Y&Z\end{pmatrix}.
\]

Assume ||Z||<1. Exact contraction is equivalent to

\[
\mathcal S=I-X^*X-Y^*(I-ZZ^*)^{-1}Y\succeq0.
\]

Thus the second-slab Schur formula is already an arbitrary-depth structural identity. For successive integer thresholds, the newly appended interval has length less than log(2), so its diagonal operator Z contains only the gamma kernel. All arithmetic memory of the past appears in Y.

If D_X = I-X*X is strictly positive, define

\[
\mathcal C=(I-ZZ^*)^{-1/2}Y D_X^{-1/2}.
\]

Then

\[
\mathcal S=D_X^{1/2}(I-\mathcal C^*\mathcal C)D_X^{1/2}.
\]

The natural induction target is a bound on this **normalized coupling**, with enough information to form the next update. Keeping only the smallest eigenvalue of D_X is likely to discard the cancellations needed by Y. A useful invariant would retain an explicit factor or an operator-valued storage bound and the associated input/output maps.

The inverse formula is used only at strictly contractive positive shifts. It is singular at omega = 0 and must be rescaled or replaced by the central-form approach there.

This is a candidate proof architecture, not a positivity theorem: neither the block identity nor the Euler product proves ||C||<=1. Such a theorem must exploit specific prime-gamma relations. Reconstructing a positive storage factor only after assuming contraction would return to the original inverse-spectral circularity.

## 7. Which computational patterns are likely to scale

**Retain the complete output Gram.** The identity E = PH^2P-(PHP)^2 = J*J is one of the most valuable reusable features of the present method. It records leakage into every omitted output mode. Positive compressions without this information can miss a negative direction in the full operator.

**Use relative error in the weak directions.** If a positive finite reference G is already certified, a target such as

\[
\|G^{-1/2}\mathcal R(\omega)G^{-1/2}\|<1
\]

is better aligned with positivity than comparing one global absolute remainder against the smallest eigenvalue of G. The inverse-square-root/congruence and its error amplification must themselves be controlled. The current parity pencils give a concrete finite setting in which to test this idea.

**Separate the few weak collective directions from the coercive tail.** Track their eigenvectors, parity, delay correlations, and Schur couplings as depth changes. Candidate eigenvectors can come from ordinary numerics; all final form, basis-change, and tail errors need enclosing bounds. Phase-space or Sonin/prolate-inspired bases are worth testing against Legendre bases, but they are not yet a proven improvement for this operator.

**Avoid adding absolute prime norms as the main induction.** The central arithmetic correction contains a growing sum of indefinite delays. A scalar triangle bound loses their interaction with admissible autocorrelations. Moreover ||T_d|| jumps from zero to one when a horizon first exceeds d, however short the new interval is. Small spatial width is therefore not a small operator-norm perturbation of the central generator. Localized coercivity or a relative form estimate is needed to exploit that width.

**Expect shrinking margins.** Zhu's current compact-window preprint reports central positivity for total support 1.6 and identifies a doubly exponential cost barrier for its particular pointwise-envelope reduction. Its variable L is a half-width, so compare its L=0.8 with this project's total horizon L=1.6. This provides a useful potential source of central estimates and a warning about that method, not an independently audited input here or a barrier theorem for every storage approach. [Zhu, v2, Theorems 1.2 and 1.4 and Section 6](https://arxiv.org/html/2608.24827v2).

For higher Taylor models, the evenness of A_omega also supplies a formal coefficient recurrence on a common smooth core. If V_omega = sum_j omega^j U_j and A_omega = sum_r omega^(2r) A_(2r), then

\[
(j+1)U_{j+1}=-\sum_{r=0}^{\lfloor j/2\rfloor}A_{2r}U_{j-2r}.
\]

In particular U_1=-A_0, U_2=A_0^2/2, and U_3=-A_0^3/6-A_2/3. These are core/coefficient identities, not a bounded-operator Taylor expansion on arbitrary L2 inputs or permission to neglect the infinite output. They may organize independent checks of the explicit logarithmic-moment calculations.

## 8. Recommended next research sequence

1. **Consolidate the general generator and continuation lemma.** Review the core derivative and closure argument carefully; record the new 4e-5 endpoint as a corollary with inherited certificate status.
2. **Make central coercivity the next depth target.** At total horizon log(4), include n=2 and n=3. Obtain a complete lower bound for Q_0,L, then apply the analytic lemma. Audit the normalization and certification of existing external central-window results before deciding how much to recompute.
3. **Test a storage invariant at log(4), then just beyond log(4).** The latter activates the first repeated delay, n=4. Later, test just beyond log(6), where mixed-prime compositions first enter. These are more discriminating tests of a general rule than many similar shift boxes at L=log(3).
4. **Use the second-slab gap as a secondary test of relative remainders.** A solution would strengthen the finite-depth paper and assess the proposed numerics, but a connected interval through 0.05 should not block the depth investigation.
5. **Test proposed structural positivity against perturbed arithmetic data.** Increasing a delay coefficient can make a finite-horizon operator expansive while leaving much of the Volterra algebra intact. Any claimed general proof must identify which special arithmetic relation excludes such examples. Keep spectral-defect tests as separate diagnostics unless a rigorous map to arithmetic horizon has been derived.

The mathematical bottleneck has become more specific: find a prime-gamma inequality that controls central weak modes, or normalized cumulative coupling, at unbounded depth. The present algebra and finite-tail machinery make that question concrete. They do not yet answer it.

## 9. Verification performed for this assessment

All eight supplied items were inspected: the overview, first-slab paper, second-slab summary, continuation guide, the extracted supporting archive, and the three foundational PDFs. The first-slab generator page was also rendered to check the kernel and normalization against the extracted text.

From the archive's `supplement/leakage_remainder` directory, the following were rerun successfully using the supplied coefficient and trace files:

```bash
OPENBLAS_NUM_THREADS=1 python3 validate_taylor.py
python3 validate_leakage.py
```

All four pencil congruence checks passed. The smaller validated row gap was approximately 8.2731e-9 after the prescribed matrix shift and error allowances. The direct leakage validator reproduced ||W2||<96, remainder constant 954147, and normalized Schur margin 1.12987188e-8 at the inherited cutoff 1.4e-7.

This was a validator rerun from supplied coefficients, **not** a new run of `build_leakage.py`, an independent derivation of every error allowance, or a rerun of the interior or primary first-slab certificates.

SHA-256 of the inherited numerical inputs used:

```text
decimal_coefficients.json
c43d31f8756fc6a0111c5c01f4cb902372b481153b25e7d0ba6224bc77d2e277

gamma_trace_bounds.json
65325e7d51f89b0cf69d0549e685dbab3f2dbc3f5235d1a24df9e735b1818903
```

The elementary constants for the new analytic corollary were separately checked with exact rational arithmetic:

```python
from fractions import Fraction as F

def exp_lower(x, n):
    term = out = F(1)
    for k in range(1, n + 1):
        term *= x / k
        out += term
    return out

assert exp_lower(F(11, 10), 6) > 3
assert exp_lower(F(7, 10), 4) > 2
assert F(5, 3)**2 < 3

C = (F(2, 3)*F(11, 10)**3
     + F(3, 10)*F(11, 10)**2
     + F(3, 8)*F(7, 10)**3)
assert C == F(6619, 4800) < F(3, 2)

m, B, h = F(1, 10**9), F(3, 2), F(4, 10**5)
assert m - B*h*h/3 == F(2, 10**10)
```

For continuation, retain this note together with `SECOND_SLAB_WORKING_SUMMARY_20260906.md` and `SECOND_SLAB_SUPPLEMENT_20260906.zip`. The older summary remains a record of the preceding endpoint cutoff; this note states the additional analytic deduction separately.
