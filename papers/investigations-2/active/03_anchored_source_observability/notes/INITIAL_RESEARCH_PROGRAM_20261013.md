# Initial research program for anchored source observability

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort ultra, verified
from the recorded session configuration. Status: initialized, awaiting
Claude review. This initializes a bounded source-to-observation program;
no new research computation or global visibility theorem has run.

## State generator and readout

On a literal fixed cutoff, retain every coefficient
\(q_n=e^{i\theta}\exp(t\log^2n/4-\zeta\log n)\), including composites.
The heat-weight part has generator \(\mathsf H^2/4\), where
\(\mathsf H e_n=\log(n)e_n\). Physical evolution additionally moves
\(\zeta,\theta\), and the normalizer; the approximant has a known heat
residual and is not an exact invariant heat manifold.

For \(p n\le N\), the prescribed edge factor is
\[
r_{p,n}=e^{t(2\log p\log n+\log^2p)/4-\zeta\log p},
\qquad (B_pq)_n=q_{pn}-r_{p,n}q_n=0.
\]
The source anchor is \(q_1=e^{i\theta}\). With all edges stacked,
\(A_{\rm bulk}=B^*B+e_1e_1^*>0\) and
\(q=A_{\rm bulk}^{-1}e_1e^{i\theta}\). Its coordinate blocks admit regular
Schur elimination without assuming observation nonvanishing.

The physical finite pair is \(Cq_R=(F/2,F_x/(2L))\), with amplitude and
carrier drift included in \(C\). The nonvanishing normalizer and full
approximation interface relate it to \((H,H_x)\).

## Objective and exact certificate

Find an independently justified complete-source relation that makes the
anchor quantitatively visible through the two observations. Source
covectors satisfy \(b^Tq_R=1\), \(a^Tq_R=0\). An adjoint identity
\[
b=C^Ty+B_R^T\lambda+za+r
\]
gives \(1=y\cdot Cq_R+r\cdot q_R\). With
\(R=\sum_{n\le N}|q_n|\|r_n\|\), it implies
\(\|Cq_R\|\ge(1-R)/\|y\|\). A genuine joint zero satisfies the imported
\(\eta/2\) bound, so the paid exclusion predicate is
\(R+\eta\|y\|/2<1\).

## First bounded task

Select one independent complete angular or matched-boundary relation and
one closed shrinking-sector cell. Declare an exact finite pairing map or
pay a continuum-to-discrete interface. Retain every prime edge and compute
the resulting effective source map. Construct a regular prescribed
direction \(y\), its added relation, and the complete residual. Choose a
cell where separate coordinate bounds are inconclusive, so the proposed
correlation can be assessed directly. Deliver the identity, domain,
multiplier bounds, defect ledger, and a concrete decision on the paid gap.

## Validation and failure criteria

The existing unrestricted graph optimum is exactly
\(|1-y\cdot Cq_R|\). Further tree or Schur optimization of the same
constraints creates no independent source information. A useful gain must
come from a new source correlation or a uniformly controlled direction
established independently of nonvanishing. Dividing by the unknown joint
norm, value, slope, or collision determinant is inadmissible.

Validate block invertibility and all transported source terms before
elimination. Check finite identities exactly; prove claimed cell bounds
outward, with the full approximation payment. Approximate edge identities
require their defects multiplied by the actual multiplier sizes. Positive
bulk energy alone supplies no lower observation bound. A graph using only
primes 2 and 3 with the old absolute residual is already obstructed for
\(L\ge160\); a different correlated relation needs its own hypothesis.
Continue for a paid gap or a uniform growth improvement; otherwise save
the exact preventing term. A bounded gap is not global collision coverage.

## Starting records

- [Brainstorm card 3](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#3-anchored-source-identities-and-schur-elimination).
- [Source certificate, Heat Note 25 §§2–3](../../../../quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).
- [Sharp residual and restricted-prime scope](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/2_SHARP_ADJOINT_RESIDUALS_AND_RESTRICTED_PRIME_OBSTRUCTION_20261010.md).
- [Schur/Feshbach precedent](https://arxiv.org/html/2105.02058v1#S1).
