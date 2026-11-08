# Opening-round proof-author self-check

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**,
chat0001. Same assistant as the proofs. **This is not the separate E02
assessment**, cross-model validation, or specialist review.

Sources: [Note01](../notes/01_TND_OC_REFLECTION_AND_CONFIGURATION_REDUCTION_20261107.md),
[Note02](../notes/02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md), the fixed
[E01 request](../research-progress/handoffs/01_TND_OC_E01_REQUEST_20261107.md),
and its input manifest. This check recalculates the material constants
and edge cases analytically; no numerical or interval campaign was run.

| Claim | Check and disposition |
| --- | --- |
| Note01(3) and (5) | Conjugate copies have identical x and w, so every odd transverse measure vanishes before convolution. Extending to self-pairs is valid because the original difference power vanishes there. For multiplicity m at each conjugate location, the two orders give \(2m^2(2d)^2=8m^2d^2\). For order four and one pair, both sides give \(32d^4\). This is an algebraic normalization check, not evidence for an RH criterion. |
| Product recurrence and order bounds | Logarithmic differentiation gives the alternating power-sum recurrence. The factorial majorant retains repeated-index terms only in its upper comparator. The two inequalities in Note01(11) pay both the \(e^t\) factor and the desired remainder; no fixed-order limit is substituted at growing order. |
| Jensen/Blaschke part | \(R/\rho=27/26\), \(R+r=26/3\), and \((\rho+r)/(\rho-r)=51\). The quotient has no poles in the R-disk and no zeros in the rho-disk. Its center modulus is at least m; the maximum principle supplies its upper bound. Zeros on the intermediate circle do not invalidate the interior-radius Harnack limit. |
| Sublevel and logarithm constants | For \(q<1\), \(k\le n\) gives \(kq^{2/k}\le nq^{2/n}\); for \(q\ge1\), the full disk area is dominated. The zero-free case is handled separately. Integrating \(t^{2/n}/t\) gives \(n/2\), and applying the bound to both functions cancels the half. The split \(\tau=\epsilon^{n/(n+2)}\) gives the common exponent \(2/(n+2)\). |
| Canonical normalization | Xi reflection gives \(H_0=\xi(s)/8\). Cancelling \((s-1)/s\) yields \(D=16\pi^{s/2}/(s^2\Gamma(s/2))\). The disk has \(\Re s\in[1/4,19/4]\), so D is nonzero there and the cancelled zeta pole adds no zero. |
| Safe anchor and disk size | \(\lvert s-1\rvert\le X/2+6\) and \(1/\sigma\le4\) give \(2X+25=M_X-1\). The center Euler lower bound is \(c_0\); \(\delta\le c_0/2\) pays the approximant's anchor. Dividing both functions by the same \(M_X\) cancels their normalization in the logarithm difference. |
| Weak planar tests | Their support fits because \(\sqrt{17}<25/6\). Value and normal first derivative vanish at y=0; there is no boundary delta. Mollification preserves bounded second derivatives, and locally integrable logarithms permit the limit. The factor two counts both conjugate halves; real multiple zeros contribute zero. Approximate zeros above y=1 are retained up to the actual cutoff, not silently discarded. |
| Complete source tail | The half-line cosine integral has no extra half factor. At \(b=17/2\), substitution \(r=\pi e^{4u}\) gives gamma parameter \(35/8\) and prefactor \(\pi^{-19/8}/4\). The arithmetic-tail ratio is at most \(16e^{-\pi(2J+3)}<1\). |
| Compact multiplier bound | \(8/\lvert s\rvert\le32\), \(\Re(s/2)\le19/8\), and \(\lvert s\rvert^2/48\le(361+4V_X^2)/768\) reproduce Note02(32). It is a compact, height-dependent bound, not a full-line uniform conversion. |
| Consumer and scope | The approximation error can be made smaller than any declared positive budget at each arbitrary height. The finite-source value has no proved small signed bound. Height-dependent cutoffs, the deteriorating exponent, shrinking d, h costs and future quadrature costs are all retained. No HDA negative-time result is used at zero. |

No mathematical correction to the issued target was needed in this
author check. The statement is deliberately weaker than a useful signed
canonical estimate: it establishes controlled acquisition, including
near-zero logarithmic conditioning. It does not establish that the
finite comparison has an easier uniform sign theorem.

The inherited collision controls are screened analytically in Note01;
they remain compatible with the generic comparison lemma. In particular,
accurate finite-source approximation does not imply that the approximant
is all real. The simple amplitude-scaling control in Note02 isolates
why the safe anchor must be paid.

**Disposition:** E01 has a complete written comparison at its stated
scope, subject to a separate E02 assessment. Recommend **Sol6.1/ultra**
for [E02 r1](../research-progress/handoffs/02_TND_OC_E02_REQUEST_20261107.md).
The only numerical quantities claimed here are explicit analytical
constants and exponents. Proof-author checking is not independent
evidence; see [avoid05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md).
