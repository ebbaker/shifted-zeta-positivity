# Continuation after the complete-cofactor test and mixed-probe reassessment

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model audits and finite checks are internal validation, not independent
specialist review or formal proof verification.

Continue in the current local checkout at
`/Users/ebbaker/Documents/shifted-zeta-positivity`. This continuation and
notes 21--23 remain uncommitted on the session's base commit `6c343e8`.
Preserve the working tree; a fresh worktree from HEAD would omit the results.

## 1. The bounded task and its outcome

[Note 23](23_SHORT_FAMILY_PARITY_CONTINUATION_20261008.md) requested a
nonzero signed combination of surviving semiprimes and odd products, then
a reassessment if the pairing supplied no power gain. That task is complete.

[Note 24](24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md) sums every
divisor cofactor of a squarefree ideal \(M\), with \(NM\le D^\beta\),
fixed \(\beta<1/20\), before taking absolute values, for the permitted
trivial fixed twist \(\nu=1\). Its actual products
are \(bqr\), \(b\mid M\), two distinct primes of norm at most
\(z=\sqrt{CD}\), and \((qr,M)=1\). It includes semiprimes, negatively
signed triples, and all higher cofactor signs. This is a nonzero signed
response, not another vanishing coefficient sector.

On coherent rows \(u=v^6\), \(Nv\le D^{1/15}\), \((v,M)=1\),
its coefficient is \(2\mu_K(b)\). The prime-pair continuum has the
essential rescaling Jacobian \(1/Nb\); the signed cofactor inverse is
therefore \(P_-(M)=\prod_{p\mid M}(1-1/Np)>0\). Uniform prime ideal
theorem errors, Taylor remainders, Euler factors and coprime-row counting
give the selected energy lower bound

\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})|\mathcal B_{u,M}|^2
 \gg \frac{D^{16/15}}
 { (\log D)^{2k_0+2}(\log\log D)^3},
\]

for every fixed nonzero complex zero-integral profile, where \(k_0\ge1\)
is its first nonzero logarithmic moment. This particular complete pairing
cannot be assigned a separate \(D^{4/5+\epsilon}\) budget. Its cross
term with all remaining products is uncontrolled. **No lower bound for
the full tail follows.** Balanced triples with all prime norms near
\(D^{1/3}\) lie outside this block.

[Note 25](25_SHORT_FAMILY_PAIRING_REMAINDER_20261008.md) gives an exact
finite-prime resummation of the saturated projection. The auxiliary free
response has arbitrary power decay after both mask/dilation costs
\(L_u(NM)^2/D\) are paid. Its explicit arithmetic complement and the
remaining total products stay inside the same square. The balanced-triple
test is decisive: the actual coefficient is \(-6\), whereas a naive
single-prime pairing gives \(-2\) and misses \(-4\) from the other
singleton prefixes. Nonsquarefree terms of this auxiliary complement have
different coefficients from note 17 and cannot inherit its budget.

The short-family full-moment exponent remains \(16/15\); its \(4/5\)
target and deficit \(4/15\) remain open. No scalar or zero-free improvement
has been obtained.

## 2. A weaker mixed-family sufficient target

The prescribed reassessment is in
[mixed-family note 3](../../mixed_character_families/notes/3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md).
Keep that family's actual sixth-power-free rows, masks and selectors;
they are not the unrestricted short-family rows. For the selected positive
frame \(\mathcal A=\operatorname{diag}(\sqrt w)T\), set
\(G=\mathcal A\mathcal A^*\), \(C=\mathcal A^*\mathcal A\),
\(f=\mathcal A\mathbf1\), and \(E=\|f\|^2\). If \(L_N\ll N=U^m\)
is the number of original columns, then

\[
 J=f^*G^2f=\mathbf1^*C^3\mathbf1\ge0,\qquad
 E^3\le L_N^2J,\qquad J\le L_N\operatorname{Tr}(G^3).
\]

Thus \(J\ll U^{h_3+m+\epsilon}\mathcal H^a\), where
\(h_3=3[1-(1-d)m-s]\), suffices for the original energy target.
It is strictly weaker as an algebraic requirement than the earlier
full cyclic-trace target, because it retains the actual plain vector.
Its exact expansion is the open chain

\[
 J=\sum_{u,v,h}w_uw_vw_h\overline{S_m(u)}
                        K(u,v)K(v,h)S_m(h).
\]

The existing conditional buffered plain hypothesis supplies
\(|S_m(u)|^2\ll N^dU^\epsilon\mathcal H^a\) on these rows.
Together with the imported nonprincipal kernel bound \(N^{-1/8}\),
the selected inverse mass and bounded primitive fibers, it controls all
repeated-character chains. Exact minimum exponent reserves are
\(0.540594\) for all-equal, \(0.19376\) for adjacent-equal, and
\(0.24376\) for endpoint-equal character patterns. The endpoint input
is a substantive existing hypothesis, not a consequence of arbitrary
bounded coefficients.

The pairwise-inequivalent chain \(J_{\ne}\) remains unproved. Only its
real upper bound is required; it is real by reversal but need not be
nonnegative. Positivity of the full \(J\) does not give a sign for
this restricted part. The short-family obstruction does not prove that
the mixed target is easier to estimate arithmetically.

## 3. The next bounded task

Work on the specific distinct-character open chain of mixed note 3,
equation (10). Let \(c(u)\) denote the inducing primitive character and
write it as

\[
 J_{\ne}=\sum_{c(u)\ne c(h)}w_uw_h\overline{S_m(u)}S_m(h)
 \sum_{c(v)\notin\{c(u),c(h)\}}w_v K(u,v)K(v,h).
\]

Test a conductor-resolved or reciprocity-based bound for this coupled
middle-row sum and its actual endpoint form. Start with one precisely
specified conductor regime and calculate its available exponent against
\(h_3+m\). Retain every original weight, physical deletion zero and
derivative/height profile. A useful result must give a new arithmetic
estimate for a nonzero part or a quantified obstruction to that proposed
estimate. Another formal expression alone does not supply cancellation.

Do not replace endpoint sums by arbitrary coefficients, infer an unmasked
primitive family, or remove a conductor selector inside the positive
frame. Bounds on individual kernel moduli give only
\(N^{d-1/4}A^3\), which does not meet the target. Either prove a coupled
gain in a stated range with the complementary budget tracked, or record
the exact unresolved loss and reassess that proposed bound. The old
cyclic trace remains a stronger sufficient alternative; the full short
tail remains a separate open arithmetic target.

## 4. Saved verification and manuscript state

The [scoped review](../../reviews/SHORT_FAMILY_COFACTOR_PAIRING_REVIEW_20261008.md)
audits the uniform obstruction, the free/complement split and the mixed
actual-probe criterion. Two fresh runs of each standard-library checker
match its small record byte for byte:

| Checker and record | Finite scope | Record SHA-256 |
| --- | --- | --- |
| [Cofactor pairing](../../numerics/check_short_family_cofactor_pairing.py), [record](../../numerics/short_family_cofactor_pairing_record_20261008.json) | 3,289 assertions, 27 actual pairing cases, phases/zeros, weighted Euler identities, free/complement partition, true \(-6\) versus naive \(-2\) | `ea54f5736dce0ab5358ff588b6df1715925f94fb7f74d0aa137951e5a59b083d` |
| [Mixed actual probe](../../numerics/check_mixed_actual_probe.py), [record](../../numerics/mixed_actual_probe_record_20261008.json) | 2,368 exact assertions, 34 rational Gaussian frames, Jensen, open-chain partitions, negative-group witnesses and rational reserves | `e7b21e05cdcca176a4e6493cbd3b7bc26d23227db519c0e746b119ee17068bfc` |

The cofactor obstruction and proof are in the existing
[manuscript](../short_family_reductions.tex), whose native compiler returned
success for saved source SHA-256
`3c8ee8ee95b9afd2a4d16400ebead075207e38e38e8ede29ca5c7242b52c2219`.
The added subsection was separately audited against note 24. Reconcile any
newer source; do not restore this hash over subsequent edits.

Finite checks certify the stated finite algebra and arithmetic, not prime
ideal or lattice asymptotics, imported family estimates, physical
reciprocity or an unbounded moment. The analytic source qualifications in
the [dependency ledger](../../notes/RESEARCH_LEDGER_20261008.md) persist.
