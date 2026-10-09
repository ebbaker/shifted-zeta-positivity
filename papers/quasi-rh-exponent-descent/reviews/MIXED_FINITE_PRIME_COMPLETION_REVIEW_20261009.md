# Review of the high gcd reduction and finite prime completion

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex). Reasoning effort: inherited configuration, not
exposed; the exact serving variant is not inferred. Same-model internal
review, not independent specialist validation or formal verification.

Reviewed the staged mixed notes 14 and 15, `check_mixed_signed_gcd.py`,
and the source-scope paraphrase and derivation in `agent-signed-blocks`,
including the final fixed-buffer clarification and the compatible
finite-prime completion extension. I replayed the gcd checker and the
updated finite-prime completion checker: 2,161 and 153,705 assertions passed,
respectively. I did not independently
audit the deep proof of the primary source's Lemma 8.2.

**Assessment.** The new high-gcd removal is a valid conditional deduction
from the explicitly stated uniform all-length input (3), legal selected
fourth mass and elementary ideal counting. The joint near-maximal core
remainder is correctly identified. No sign, mask, normalization or cutoff
error was found. The original ratio-shell completion is correctly kept at
the original half-power edge; the new fixed-gcd boundary completion is
compatible with the stronger joint remainder. The source-buffer issue
raised in the first review is resolved by note 14's explicit literal
\(d+\rho\) allocation and the corresponding extension below.

## The deletion convolution and source scope

The identity
\((\mu_F\psi_u)\mathbf1_{(\,\cdot\,,q)=1}
 =(\mu_F\psi_u)*b_q\)
is correct prime by prime, including physical zeros. At a prime of \(q\),
the local coefficient at exponent \(j\ge1\) is
\(\psi_u(p)^j-\psi_u(p)\psi_u(p)^{j-1}=0\).
It requires all \(q\)-smooth powers in \(b_q\), not just squarefree
divisors; the note and checker both retain those powers.

The resulting inner inverse uses the original profile and original
character at scale \(X/Nk\). No new row, prime-annulus deletion or
frequency variable is introduced. The all-length input is essential;
the mixed manuscript's original-length envelope alone does not justify
this extension. The enclosing bounded nonnegative range of source lengths,
uniform profile derivatives, pure norm twists, cumulative Mellin frequency
budget, buffered row hypotheses and admissible height choice must all apply
to these shorter sums before (8) is asserted.

The \(q\)-smooth coefficient norm costs only the Euler product
\(\prod_{p\mid q}(1-(Np)^{-a})^{-1}\). For \(a\ge17/25\) and polynomial
\(Nq\), its arbitrary small power bound is uniform. Bounded scales below
one have a fixed positive lower endpoint \(1/C\) and are handled by finite
ideal counting, so they do not create a singular endpoint.

**Source-buffer clarification resolved:** note 14 now says explicitly that
the literal \(d+\rho\) contour power must be retained at an already fixed
buffer. It pays \(\rho(r-1/125)\) in the high-gcd bound and verifies that
\(\rho\le1/100000\) leaves a reserve above \(1/1000\). The source order
for choosing a buffer, finite height orders and final height is retained;
availability of a suitable buffer is explicitly not inferred from the
single original-length pointwise input. If the local hypotheses or buffer
choice are unavailable, the stated global \(\kappa=3/4\) fallback remains
the appropriate conditional deduction. An already fixed positive buffer
is not absorbed into every arbitrarily small loss.

## Fixed gcd inversion and the joint remainder

Inserting coprimality inversion before the ratio cutoff gives exactly
\[
 T_g(u)=\sum_{(h,g)=1}\mu_F(h)|\psi_u(h)|^2
       |Z_{gh}(u;D/(Ng\,Nh))|^2.
\]
The signs from the two original columns at \(h\) square away, leaving
the inversion sign. Their phases leave \(|\psi_u(h)|^2\); the exterior
\(|\psi_u(g)|^2\) remains. The h-sum converges at exponent \(1+d\)
uniformly over the working d-range. Thus the complete high-gcd aggregate
costs \(U D^dG_0^{-d}\), with the original \(D^{-1}\) normalization.

Restoring the strict ratio cutoff by subtracting the old small-core part
is legal: the absolute original pair-count estimate bounds every subset
of that part. This is not an application of the source inverse lemma to
a sharply ratio-filtered square.

For \(G_0=cU^{1/125}\), the new power reserve is exactly
\(d/125-1/540\ge347/337500>1/1000\). If \(Ng<G_0\), both original
annuli force \(Na,Nb>U^{r-1/125}\), hence
\(N(ab)>U^{2r-2/125}\). The simultaneous gcd/core restriction in (18)
is therefore valid, and the old half-power cut is automatic. Enlarging
this remainder to every large core would lose the equality, as the note
correctly emphasizes.

The signed-square reindexing by \(q=gh\) also checks out. In particular
the \(q=1\) term is the original moment; applying the pointwise inverse
envelope to the other terms alone cannot prove the missing final gain.
The \(g=1\) sector remains, and no selected weighted correlation estimate
for that sector has been established.

## Finite prime completion and the Euler diagnostic

Note 15 states the actual new joint cut and correctly declines to combine
the original ratio-shell completion with it without a joint boundary
estimate. At the
old edge its crossing terms obey
\(Y<Nf\le YNP\), so \(NP\le U^{1/250}\) leaves the claimed positive
reserve. At the new edge, the elementary cap cost already exceeds the
target, and allowing a prime on both columns can cross the gcd boundary.
Both limitations are material and are explicitly recorded.

The new compatible extension supplies a different boundary estimate. With
\(K=G_0/NP\), filtering the \(P\)-free pair by \(N(e,e')<K\) permits
every finite-prime state because the actual gcd is
\((b,b')(e,e')\), whose norm is less than \(NP\,K=G_0\). Original annuli
then force the full new ratio cutoff automatically. The complementary
terms are exactly those actual gcds satisfying
\(Ng<G_0\) and \(Ng^{(P)}\ge K\). This depends only on g and therefore
retains whole fixed-gcd forms \(T_g\), including all cofactor partitions.
Taking absolute values over those g after applying the source-compatible
\(T_g\) estimate gives \(UD^dK^{-d}\). The exact reserve for
\(NP\le U^{1/25000}\) is \(17107/16875000>1/1000\).

At a fixed buffered exponent \(d+\rho\), the extension correctly retains
the additional cost \(\rho(r-1/125+1/25000)\). For
\(\rho\le1/100000\), its uniform reserve is
\(67940623/67500000000>1/1000\). No source inverse estimate is applied
to the row-dependent completed profile \(\Delta_{P,u}A_0\): it is applied
only to the original profiles inside each \(T_g\) in the boundary.
The completed correlation itself remains open. The updated checker passes
153,705 exact assertions, including nonzero completed and boundary forms,
the original-gcd-only membership predicate, strict joint membership and
both rational buffer reserves.

The four local states and their common-prime zero mask are correct.
The three-variable Euler product has exactly the four choices
\(1,-\psi(p)p^{-s-z},-\overline\psi(p)p^{-t-z},
|\psi(p)|^2p^{-s-t}\). At \(z=0\), it factors into the two reciprocal
good-Euler-factor L-functions. At other z the displayed collision correction
is their quotient factor, so no gcd state has been dropped. The initial
absolute convergence conditions suffice; the note does not claim analytic
continuation from that calculation.

The finite-mask Mellin multiplier bounds are uniform \(U^{\pm o(1)}\)
for fixed positive real part. They correctly rule out obtaining a fixed
power from the isolated multiplier alone, while leaving possible oscillatory
or selected cross-core cancellation open. Neither the Euler diagnostic nor
the finite phase checks implies a lower bound for actual selected energy.
