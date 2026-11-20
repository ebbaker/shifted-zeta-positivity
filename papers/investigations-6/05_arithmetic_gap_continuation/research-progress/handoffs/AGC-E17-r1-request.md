# AGC-E17 r1: common dyadic phase envelope obstruction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Contract author explicitly dispatched
**gpt-6-astra / ultra**; serving-backend attestation and root settings
unavailable. **Type E; recommended Sol6.1 ultra.** Parent AGC-B05 r1.
This request is frozen. The [sole register](../01_AGC_RESEARCH_PROGRESS_20261119.md)
owns activation and status.

## Question and evidence standard

Complete the analytical proof that the strengthened common-phase
dyadic envelope in [Note19](../../notes/19_AGC_B05_PHASE_GROUP_DECISION_20261119.md)
still has complete allowance below−1/400 on the continuous boundary
segment F0. Its failure is a decision about that information reduction,
not a zero or failure of the exact direct margin. One proof pass and
one bounded correction pass; **no numerical scan, phase evaluation,
new rational-witness campaign or new source mechanism**.

Read repository instructions, GPT_RESEARCH_MODEL_WORKFLOW.md,
LARGE_FILES.md, the [result index](../../../../../result-summaries/README.md),
[pattern index](../../../../../avoid/README.md), Controls12, Cluster18,
patterns01/02/07/11/12, Notes14 and17–19, Review08 and Section11.
Reuse Note17's accepted parameters and Record08's exact eight-prime
witness; re-proving their transcendental bounds is unnecessary.
The retained source is Polymath v2 Corollary6.4 as normalized in
Notes14/17. No t=.2 numerical constant is imported at t=.1.

Prerequisite SHA-256 identities at freezing:

- Note14: `53fbba8135f853c54369b7bf1bddf862b3f49d8450d35ed4821450e41029d376`.
- Note17: `23fee20746272c467a0563d6090605f85bbafcbf86921c0d86421d51bdeb00c0`.
- Note18: `242d5456755cdd91f9841e433cb0fd48016457a0d9eb212466a9a8202c2ce1cb`.
- Review08: `fa9af35f64db79d0dfe85dafafbaa85d0f2a6094afbe5af27dca8c0ab4b5a59d`.
- Record08: `039f36497d5fed42603c727c8d964097229c2787006497b7a63e12b1cc286f95`.
- B05 r1 request: `9cf10c0ad1f00670ccb34f418b125f54366bd6f61f6a3a57d293ed8777a718a0`.

Keep the literal source, natural N, q=f−c and full v from Note17.
The proof domain is exactly

    F0: t=1/10, y=1/5, x0=14000+sqrt(24/25)<=x<=30000.

The intended eventual consumer remains the full final strip
x>=x0, .2<=y<=sqrt(.8). The present task does not acquire it.

## Frozen six proof targets

1. **Full source, finite convolution and phase identity.** Reproduce
the exact q=f−c and |H/B−q|<=v interface. v must contain both full
term-error sums and both entire retained delta payments; keep c and
the full D_kappa from Note17. Use unchanged E, lambda_d, beta_m,a_m
with indicator m/d<=N and all m<=30N. With rho=gamma E/conjugate(E)
=g exp(i theta), prove Note19's exact odd-core decomposition at
u=−tau log2, eta_r=−tau log r−theta/2. The r=1,j=0 term is the
separate anchor, not silently discarded. No multiplicativity of b_n.

2. **Exact group radius and the stronger common-phase consumer.**
For odd r<=30N, set I_1={j>=1:2^j<=30N}, I_r={j>=0:r2^j<=30N}
for r>=3 and

       B_r(u)=sum_(j in I_r)beta_(r2^j)2^(−j*sigma)e^(iju),
       A_r(u)=sum_(j in I_r)a_(r2^j)2^(−j*sigma)e^(iju),
       G_r(eta,u)=r^(−sigma)[e^(i eta)B_r+g e^(−i eta)conjugate(A_r)],
       R_r(u)=(1−g)sup_eta ||G_r(eta,u)||_g,
       C_dyad=sup_u sum_r R_r(u), C_sep=sum_r sup_u R_r(u).

   All phase suprema are over [0,2pi], with coefficients frozen at
   the actual observation. Prove the explicit 2 by2 real matrix
   formula in Note19. Derive

       K_dyad=1−g−C_dyad,
       ell_dyad=K_dyad/|E|−D_kappa−|c|<=|q|,
       m_dyad=ell_dyad−v.

   Show C_dyad<=C_sep<=C_ind, where C_ind is E16's individual cost.
   The exact positive divisor |E| stays in the signed definition.

3. **Independent Fourier-mean lower floor.** For every odd r>=3,
   the mean of M_r is the diagonal matrix

       diag((beta_r+g a_r)/(1+g),(beta_r−g a_r)/(1−g)).

   Use convexity of its operator norm to prove

       mean_u R_r(u)>=h_r r^(−sigma),
       C_dyad>=sum_(r odd,r>=3)h_r r^(−sigma).

   r=1 has zero constant matrix and nonnegative cost. The finite
   sums/integrals require no limiting argument. This is a mean
   bound on the relaxed envelope, not on R_r at the actual u(x).
   Establish the paid positivity threshold
   C_dyad<1−g−|E|(D_kappa+|c|+v)<=1−g, without assuming it.

4. **Quantitative failure from the accepted witness.** Reuse
   N>=33,.6<sigma<.8,0<g<.6,0<|E|<8 on F0 and

       P*={7,11,13,17,19,23,29,31},
       sum_(p in P*)b_p p^(−.8)>21/20.

   Each p has beta_p=b_p,a_p=p^.2 b_p, so h_p>=(1−g)b_p.
   Deduce C_dyad>(21/20)(1−g), K_dyad<−1/50 and
   ell_dyad,m_dyad<−1/400. Use |E|<8 only to upper-bound the
   already-defined negative allowance. A zero-clipped lower function
   cannot give a strict margin. Do not infer an upper bound on |q|.

5. **Equally informed comparator and honest phase scope.** Prove
   m_E<=m_dyad<=m_dir=|f−c|−v. Give direct evaluation all group
   polynomials, actual phases, correction, kappa and complete source
   information. It may use the same grouping. Explicitly distinguish
   C_dyad from sum_r R_r(u(x)); the latter's smaller actual-phase
   allowance may succeed and its sign is not decided. No common
   maximizer or simultaneously adverse core phases is claimed to
   occur at any actual x. No speed advantage or all-methods no-go.

6. **Exact cutoffs, remaining coverage and collision screen.**
   The natural indices on F0 are33,...,48 and its seams are
   x_j=4pi*j²−pi/40,j=34,...,48. A permissible rational endpoint
   proof uses25/8<pi<22/7 and x0<14001. Treat each half-open
   natural cell intersected with F0, its old one-sided seam limit,
   new included seam and the final included30000. Both references
   retain all eight primes. Fixed-reference transfers still pay
   Note14's signed jump and the full error. No floor differentiation.

   Keep the rest of the two-dimensional finite strip, effective
   infinite-tail onset/overlap, initial verification and full time-zero
   barrier separate and unacquired. Moving a join cannot rescue this
   envelope at the included x0. Screen Controls12 against source,
   actual arithmetic/phase and strict-margin premises, retaining
   each construction's domain/event/conditional qualifiers. The
   exact quadratic zero at t=.1,z=x_c+i sqrt(.3),x_c>=x0, is a
   generic complete-margin test, not theta arithmetic.

## Completion, limits and ownership

Completion is six passed analytical targets or the exact failed step
with its consequence. A scoped negative allowance theorem completes
E17. Routine notation or algebra corrections inside this class are
permitted. Changing the anchor, grouping, phase relaxation, source,
domain, or claimed constant requires return to B05 with the failed
evidence preserved; do not create a broader campaign.

Write `notes/20_AGC_E17_DYADIC_GROUP_OBSTRUCTION_20261119.md`,
`research-progress/handoffs/AGC-E17-r1-return.md` and the concise
`manuscript/sections/12_dyadic_group_obstruction.tex`. The manuscript
section should take roughly 2–3 pages: inherit Section11's source and
eight-prime witness, state the new grouped definition, and give a
self-contained proof of its mean/sup argument, comparator and scope.
Do not rederive inherited source estimates. Root alone changes
`main.tex`, the sole register, shared indexes/navigation, history and
production records. No new numerical receipt is needed. Preserve prior
evidence and let root route the separate assessment.
Record actual available settings and distinguish explicit dispatch
from backend attestation. A separate nonauthor internal assessment
is required before accepted or manuscript-milestone status.

The return should identify what a later **B06 / Astra ultra** decision
would need to escape this class: either actual-height joint phase
restrictions with coefficient variation and every seam paid, or a
signed group retaining the anchor/core/correction coupling. An actual
phase name or an unquantified correlation is insufficient. Require
an independently checkable bound and full-margin threshold, with an
equally informed direct comparator. Do not select or run a new phase
campaign, change the source, or claim that this list itself acquires
such a bound. Root's continuation will own the B06 specification.
