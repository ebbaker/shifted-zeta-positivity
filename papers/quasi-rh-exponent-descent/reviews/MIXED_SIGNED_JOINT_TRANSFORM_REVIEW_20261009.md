# Scoped review of note 21: the native joint second transform

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact runtime variant and reasoning-effort
configuration are unavailable. This is same-model internal source and
algebra review, not independent specialist or formal proof certification.

Reviewed [mixed note 21](../mixed_character_families/notes/21_SIGNED_JOINT_TRANSFORM_20261009.md).
Source comparison: printed pp. 89 and 161 of the
[30 September companion manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
including rendered inspection of the Gauss conjugations. Source SHA-256:
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
No source quotations or source PDF are retained in this review.

**Finding: no substantive algebraic error found in the reviewed note.**
Its scope is correctly restricted to an exact fixed smooth-envelope
transformation and arithmetic cancellations. It does not claim a signed
bilinear moment estimate or a strict induction drop.

1. **Common character and conjugations, equations (8)--(11).**
   Reduction of the triple congruence modulo \(r\) fixes
   \(z=(ab)^{-1}j\), giving
   \(\xi_r(j)\overline{\xi_r(ab)}\). Scaling both remaining residues
   by \(r^{-1}\) gives
   \(\overline{\chi_a(r)}\chi_b(r)F^+(a,b;j)\), including on artificial
   noncoprime pairs. The source definition
   \(\tau_D(b)=\tau(b)\chi_b(er)\overline{\xi_r(b)}\) means its conjugate
   contributes \(\xi_r(b)\); together with \(\xi_r(a)\), it cancels
   \(\overline{\xi_r(ab)}\) exactly. The \(r\)-Euler twists also cancel.
   This verifies (9), including the surviving native row factor
   \(\xi_r(j)\). The plus-congruence sign is
   \(\overline{\chi_b(-1)}\), as in (5). On the genuine coprime locus,
   the residues are \(x=jb^{-1}\), \(y=-ja^{-1}\), so sextic reciprocity
   and \(\chi_b(-1)^2=1\) give (11). That formula must not be used on
   individual noncoprime divisor terms.

2. **Radial Poisson normalization, equations (12)--(14).**
   The finite Fourier coefficient of the Gauss product is
   \(F_r^+(a,b;j)/\sqrt{q_rq_aq_b}\). A radial dyad of norm length \(T\)
   contributes \(T\) and Fourier argument \(Tq_j/(q_rq_aq_b)\) in the
   source's self-dual two-dimensional lattice normalization. Multiplying
   by the first prefactor and column inverse root gives precisely
   \(HT/(Xq_eq_r)\) times \(1/(q_aq_b)\), as in (13).
   With the entire first kernel, its radial inverse has scale
   \(B=q_eq_rq_aq_b/H\); the factors cancel to \(1/X\) and yield
   \(\Phi_1(q_eq_j/H)\). This checks the involution in (21), with its
   stated first-\(h=0\) subtraction when appropriate.

3. **Zero frequency and nonzero divisor support.**
   The source diagonal \(F(a,b;0)=1_{a=b}\varphi(a)\), together with
   \(R(a,a)=\chi_a(-1)\), gives (15) exactly. If \(r>1\), the primitive
   zero-extended \(\xi_r\) makes the zero frequency vanish immediately.
   If \(r=1\), the complete divisor sum kills every nonunit diagonal.
   The note correctly retains the possible residual unit/unit column;
   an outer full-column annulus need not exclude that residual sector.
   Since \((a,b)\mid j\) is necessary for the actual congruence,
   \(s\mid a,b\) forces \(s\mid j\). Thus (18) is exact, including old
   zeros and both whole physical column profiles. It is not a saving
   merely from counting divisors: the local correlations and their
   signed sum still require an analytic estimate.

4. **Frequency and conductor scope.**
   The formal triple period is \(rab\), so the raw transformed width is
   \(m-E+(K_0-K)\). After the column cancellation in (9), its column
   support allowance is \(q+E\). The total is exactly
   \(M+(K_0-K)\). The note explicitly retains \(\xi_r(j)\) as a possibly
   moving native row character and does not identify it with fixed
   arithmetic data in the source recursion. Hence this calculation
   proves no strict smaller-width induction step and no automatic
   membership in the source's positive child coefficient class.

5. **Sixth-power replacement and surviving errors.**
   For a \(p\)-free residual modulus and common support, multiplication
   of the Gauss frequency by \(p^6\) is exactly periodic because every
   character has order dividing six. The full coprimality projector kills
   every two-sided extracted \(p\) branch. The surviving one-sided
   central moduli in (22) follow directly from the normalized local
   Gauss sums at valuations \(1,6,7\): after the column inverse roots,
   their factors are \(P^{-1/2},1-P^{-1},P^{-1/2}\).
   Squarefreeness removes only inverse ownership above the first power;
   it does not eliminate plain sixth powers. The inverse-owned first
   power has exactly the sign and quotient puncture in (23).
   In (24), the enlarged row ball retains the \(p^6\)-sublattice.
   Its finite Fourier average loses \(P^6\), cancelling the enlarged
   radial scale. The resulting Fourier argument and effective width are
   unchanged. A row-dependent eligible pool additionally requires its
   actual lattice mask and normalization; the note keeps this caveat.

6. **Selected norm and signed restriction.**
   The note properly distinguishes the original selected positive moment
   from a sharp signed near-ratio remainder. Positive enlargement of the
   former to a smooth full mixed moment is a sufficient stronger task.
   It gives no monotonicity or positivity for the latter. The complete
   coprimality sum, original common Fourier kernel, inverse-labelled
   annulus, native zeros, and all extracted masks remain prerequisites.

The separate [truncated-inverse review](MIXED_TRUNCATED_INVERSE_BILINEAR_REVIEW_20261009.md) records the controlled short-cofactor proof. It validates an actual
removable small-product sector, with correlated fixed-buffer saving
\(7979/2000000\) before arbitrary small losses. It does not establish a
balanced bilinear theorem for the complementary product sector.
