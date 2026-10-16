# Continuation after rough-core parity and the squarefree discrepancy bridge

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model audits and finite checks are internal validation, not independent
specialist review or formal proof verification.

Continue in the current local checkout at
`/Users/ebbaker/Documents/shifted-zeta-positivity`. The session began from
commit `6c343e8` with a clean working tree; the manuscript matched the
source hash recorded in note 20. The present additions are uncommitted.
Do not create a worktree solely from HEAD and thereby omit them.

## Read first

1. [Note 21](21_SHORT_FAMILY_ROUGH_PARITY_20261008.md): the complete
   squarefree coefficient split, the new growing signed sector, its
   conductor restriction, and the retained generic budget.
2. [Note 22](22_SHORT_FAMILY_SQUAREFREE_DISCREPANCY_20261008.md): the exact
   masked mixed-discrepancy bridge at the same buffer, with both edges,
   low/low, density, endpoints, prime powers and added modulus retained.
3. [Scoped review](../../reviews/SHORT_FAMILY_ROUGH_PARITY_REVIEW_20261008.md),
   the [existing manuscript](../short_family_reductions.tex), and the
   [dependency ledger](../../notes/RESEARCH_LEDGER_20261008.md).
4. [Previous continuation](20_SHORT_FAMILY_SESSION_CONTINUATION_20261008.md)
   for the earlier squarefree reduction, source qualifications and wider
   research tasks. Its handoff Git state is historical, not the new HEAD.

## What changed

Keep \(H=D^{2/5}\), \(\theta=11/20\), and \(Y_u=D^{9/20}/L_u\).
For each squarefree total ideal and \(Y\ge1\), let \(b_Y\) contain
exactly the prime factors of norm at most \(Y\), and let \(r_Y=n/b_Y\).
Then exactly

\[
 t_Y(n)=\mu_K(b_Y)(1+\mu_K(r_Y))
       -\sum_{d\mid b_Y,\,Nd>Y}(-2)^{\omega(d)}.
\]

When the whole norm \(Nb_Y\le Y\), an odd rough core cancels and an
even rough core has coefficient \(2\mu_K(b_Y)\). The overflow sum is
essential when \(Nb_Y>Y\). Individual small primes being below \(Y\)
does not imply their product is below it.

For total ideals \(n=bq_1q_2q_3\), \(Nb\le D^{1/40}\),
\(Nq_j\ge\kappa D^{13/40}\), the actual response restricted to
\(L_u\ge D^{1/8+\delta}\), fixed \(0<\delta<11/40\), has energy
\(O_N(D^{-N})\) for every \(N\). On \(Nu\le D^{33/80}\) it is
zero by the complete cofactor identity; the exterior rows are paid by
Schwartz decay. This includes nonempty signed tails and growing nonunit
cofactors. Fixed prime windows give \(\asymp D/\log^4D\) columns,
so this is not merely a sparse-support estimate.

This sector theorem is incorporated, with proof, in the existing manuscript.
The native editor compiler returned success for saved source SHA-256
`628700359d78202fae5137fafbf4667a73df208c7f738a517f6bc35aebd16e22`.
Read any newer source and reconcile its changes; do not restore this hash
over subsequent edits.
Its generic retained-response bound still costs \(D^{16/15+\epsilon}\).
There is no improved full moment, scalar bound, or zero-free strip.

## The precise remaining response

Define \(G_u\) to retain saturated even rough cores, and \(R_u\) to
retain the entire unsaturated coefficient; retain the \(Y_u<1\) unit
exception in \(R_u\) until its Schwartz estimate is invoked. Note 21
gives exactly \(T_{u,\mathrm{sf}}=G_u+R_u\). The open estimate is

\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})|G_u+R_u|^2
                    \ll_{\epsilon,W}D^{4/5+\epsilon}
\]

for every required derivative profile, with all fixed arithmetic data
retained. The new algebra identifies an additional actual zero sector
and gives no improved estimate for the remaining nonzero response. The
power deficit remains \(16/15-4/5=4/15\).

Balanced semiprimes retain \(+2\) on every significant row. Balanced
triples retain \(-6\) on coherent inner rows, since
\(L_u\ll D^{1/15}\) gives \(Y_u\gg D^{23/60}>D^{1/3}\).
Thus the next estimate must explain compensation across these products
and other total products, especially at low conductor. It cannot promote
the high-conductor zero sector to an all-row triple bound.

## Next bounded research task

Seek a bound for a **nonzero signed combination** in \(G_u+R_u\), rather
than another coefficient-zero sector. A concrete test is to pair the
surviving saturated-even semiprime response with its unsaturated or
low-conductor odd-product compensation before any absolute value.
Retain all product and divisor cutoffs and specify where a power saving
enters the weighted energy.

Note 22 gives a second exact interface. For fixed squarefree coprime
outer factors \(c,m\), put \(h=cm\) and add \(h\) to the inner
deletion mask. Then \(\mu\lambda_{u,h}*\Lambda\lambda_{u,h}\) is
squarefree-supported after complete prime-power recombination. This
restores a genuine product-convolution identity, but the deletion
modulus can grow to \(L_{u,h}\le L_uNh\), with \(Nh\) between
order \(D^{1/2}\) and order \(D\). Neither the Möbius nor the von
Mangoldt factor is a free-character sum. A proposed completion argument
must pay this cost and cannot reuse the original \(L_u\) unchanged.
At this buffer the previous support criterion for deleting low/low fails.
Semiprimes can lie wholly in the low/high edge; retaining an opposing
edge does not itself cancel them.

If the next attempt yields only another equivalent expression with the
same generic budget and no bound for a nonzero signed combination,
record that fact and reassess the parallel mixed-character route. Do not
claim contraction from a positive single-cofactor kernel or from a finite
sample.

## Verification and saving

The new standard-library checkers and small records are indexed in the
[numerics guide](../../numerics/README.md). The parity checker reports
32,815 assertions, including 420 nonempty canceled tails and the nonunit
36-tuple witness. The squarefree discrepancy checker covers the masked
full-prime-power bridge and its direct projection. These validate finite
algebra, not physical reciprocity, conductor comparison, Poisson, sieve
inputs, prime asymptotics, or an unbounded moment.

Use the next unused numbered note after 23, keep sources and records
small under the root `LARGE_FILES.md` policy, and update the concise
history and ledger for substantive results. Follow-up manuscript edits
belong in the same `.tex` file and native editor, with a successful native
compilation check. Preserve the author's acknowledgement and preparation
metadata. No commit, tag, snapshot folder or separate PDF was created in
this session.
