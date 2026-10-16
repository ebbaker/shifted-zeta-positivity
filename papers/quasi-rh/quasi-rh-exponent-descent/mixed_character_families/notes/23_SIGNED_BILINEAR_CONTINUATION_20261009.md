# Signed bilinear continuation: controlled cofactor and remaining theorem

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model internal audits and
finite checks are not independent specialist review or formal verification.

Follow-up: [Note 24](24_ADAPTIVE_COFACTOR_AND_DYADIC_KERNEL_20261009.md) enlarges the cutoff to U^(r/2−1/4), completes the literal dyadic and algebraic extraction interface, and bounds the smooth zero contributions. The nonzero-frequency moment remains open. The fixed-cutoff results below retain their original scope.

The signed bilinear investigation produces one new conditional analytic
removal and two useful exact transform facts. The short combined cofactor
in an exact truncated inverse decomposition, together with every cross
term, is controlled beyond the saving required by the current program.
The signed joint transform cancels its artificial nonunit zero-frequency
diagonal and restricts nonzero-frequency coprimality labels to divisors of
the new frequency. A bound for the remaining correlation is still needed.

## 1 The new removal

Keep the actual original row/bin, native zero-extended character, inverse
and plain annuli, whole slots and selected positive weight
\[
 V_u=1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2,
 \qquad F=\sum_uV_u|M_u|^2.
\]
Under the source all-length bin bounds and selected fourth mass,
[note 22](22_TRUNCATED_INVERSE_BILINEAR_REMOVAL_20261009.md) gives the exact
decomposition
\[
 M_u=-D^{-1/2}\sum_{\mathfrak t}c_Z(\mathfrak t)\psi_u(\mathfrak t)
                  P_u(D/\mathrm N\mathfrak t),
 \qquad Z=\sqrt{CD},\quad c_Z=(\mu_F1_{\mathrm N\le Z})^{*2}.
\]
Remove the part with \(\mathrm N\mathfrak t\le U^{1/10}\), and call the
remaining inverse \(M_{L,u}\). The removed response square has unbuffered
saving at least \(1/125\). Applying weighted Cauchy to the **full** original
inverse and that short part controls all its cross terms. With the literal
source buffer \(0<e\le1/1200000\),
\[
 \left|F-\sum_uV_u|M_{L,u}|^2\right|
 \ll_\varepsilon
 U^{1+dr-7979/2000000+\varepsilon}H^b.                    \tag{1}
\]
The bound on \(e\) must also satisfy the source's own smallness condition
and the tighter witness budget; a fixed buffer is not an epsilon loss.
The source frequency/height schedule likewise follows the permitted
small-loss ordering; any fixed positive power cost is deducted from the
margin in (1).
The exact margin in (1) beyond the required \(1/700\) is
\(35853/14000000\). The removal also fits the older \(1/540\) target.

Consequently the new sufficient theorem can now be stated as
\[
 \boxed{\sum_uV_u|M_{L,u}|^2
       \ll_\varepsilon U^{1+dr-1/700+\varepsilon}H^b.}     \tag{2}
\]
It is equivalent at this target exponent to the original full mixed
theorem, under the stated imported inputs. This is a smaller correlation
support, not a proof of (2).

The exact coefficient remains \(c_Z\); it is not multiplicative beyond
\(\mathrm N\mathfrak t\le Z\), and its product may have prime valuation
two. The large product condition does not make both factors large. Its
plain quotient can also be short. These facts matter for every subsequent
dyadic or gcd decomposition. The old signed near-gcd/large-ratio remainder
from notes 14–15 is an alternative original-inverse representation; its
filters do not pass through this regrouping without a new exact identity.

## 2 What the signed transform now supplies

[Note 21](21_SIGNED_JOINT_TRANSFORM_20261009.md) follows the exact source
first Gauss-pair expression before Cauchy, including its conjugations,
common primitive Gauss factor, complementary row mask and fixed twists.
The artificial all-pairs kernel is
\[
 Q_j(a,b)=R(a,b)\overline{\chi_b(-1)}F_{13.3}(a,b;j).
\]
Its zero-frequency kernel is \(1_{a=b}\varphi(a)\). Restoring the complete
coprimality projector kills every nonunit diagonal. An active common
primitive character kills even the possible unit/unit term; otherwise
that exception needs an actual residual-support check. The source's
earlier first-Poisson zero row is a separate term and is not removed by
this argument.

For \(j\ne0\), the kernel vanishes unless \((a,b)\mid j\), and its
magnitude is at most \(\mathrm N(a,b)\). Thus an individual Möbius label
can contribute only when \(s\mid j\), giving a divisor-bounded list at
each physical new frequency. Its noncoprime correlations remain intact;
one cannot replace them by the genuine coprime factor on individual
label terms. This arithmetic refinement has no proved fixed exponent gain.

Keeping the common Gauss factor is essential. If \(K_0\) is the nominal
first frequency length and \(K\) the actual retained dyad, the correct
joint row-plus-column width is
\[
 M_{\mathrm{joint}}=M+(K_0-K).
\]
At the main dyad it returns the original width. The common character
\(\xi_r(j)\) remains a signed row factor with possibly growing conductor;
its removal from column support does not certify a recursive source class.
The exact sixth-power replacement likewise retains a sublattice mask.
Its larger row ball and Fourier modulus cancel one another. Coprimality
does eliminate two-sided prime extraction branches, but a new signed
operator estimate is needed to turn the remaining one-sided branches
into a saving.

These transform statements apply to fixed smooth row problems, with an
appropriately proved marked coefficient class. They do not authorize
Poisson on a sharply selected amplitude bin or positive enlargement of
the old signed near-gcd remainder. Using the positive full form as a
sufficient stronger smooth problem still requires its actual profiles,
masks and coefficient normalizers. Applying this machinery to (2) needs
the coefficient extension proved afresh.

## 3 The next proof task

The most useful next task is a dyadic signed kernel estimate for the
literal form (2), beginning with the exact expansion in note 22, (19).
The first partition should retain both truncated squarefree factors,
their product cut \(\mathrm N\mathfrak t>U^{1/10}\), and the original
inverse annulus through the plain quotient. It must include the
unbalanced and short-quotient pieces. A proof for one balanced rectangle
alone is an initial subcase.

For a smooth sufficient row problem, keep the complete artificial
coprimality combination through the joint transform and use the
frequency-divisor support before any absolute label summation. The
remaining target is cancellation in the nonzero-frequency aggregate
with its actual marked coefficient and common Fourier kernel. Source
positive diagonal estimates lose exactly the correlation that must be
controlled. The weighted inverse-response tail in note 17 remains an
alternative sufficient route to the original full moment.

No new mixed fourth theorem, native-family boundary reuse, complete bin
coverage or stronger zero-free strip is established by this continuation.
Those are separate obligations after (2) is proved. The original-slot
and simultaneous-witness construction in note 19 remains conditional
on its imported global native-family assumptions.

## 4 Saved evidence and provenance

The [checker](../../numerics/check_mixed_signed_bilinear.py) and
[record](../../numerics/mixed_signed_bilinear_record_20261009.json) contain
62,822 exact assertions; two fresh runs reproduced the record byte for
byte. They test the
truncated inverse identity, squareful and higher-power cancellation,
physical zero masks, original normalization, selected weighted cross
terms, endpoints and exact rational gains. The source-kernel projector
checks are finite arithmetic models, not native selected-row estimates.
The record states their precise scope and binds the checker by hash.

The [joint-transform review](../../reviews/MIXED_SIGNED_JOINT_TRANSFORM_REVIEW_20261009.md)
and [truncated-inverse review](../../reviews/MIXED_TRUNCATED_INVERSE_BILINEAR_REVIEW_20261009.md)
are separate same-model audits. The primary PDF was read in memory and
cited by URL and hash in the linked notes; no third-party PDF, large
derived output, manuscript snapshot or commit was created.
