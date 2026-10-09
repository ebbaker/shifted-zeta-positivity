# Short family continuation after the squarefree reduction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The recorded audits and finite checks are internal validation, not
independent specialist review or formal proof verification.

The next session should seek cancellation in the **remaining squarefree
signed response**. The latest theorem controls the whole nonsquarefree
part of an adaptive convolution tail, but gives no improved exponent for
the full moment. The first useful next milestone is a signed estimate
for a new substantial sector of the squarefree residual, with its exact
compensating terms and remainder budget retained.

## Start with the current local files

The authoritative repository is
`/Users/ebbaker/Documents/shifted-zeta-positivity`.
The investigation is `papers/quasi-rh-exponent-descent/` within it.
The ChatGPT project mirror under `.codex/.chatgpt-projects/` is a separate
workspace; its `sources/` files are read-only reference material.

Read these in order, following additional references only as needed:

1. [The manuscript](../short_family_reductions.tex), especially “A
   nonsquarefree tail bound and a squarefree residual,” the adaptive
   factorization, and the imported physical operator.
2. [Note 17](17_SHORT_FAMILY_SQUAREFREE_TAIL_REDUCTION_20261008.md), which
   supplies the complete proof, cutoff tradeoff and precise residual.
3. [The latest scoped review](../../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md),
   including its validation limits.
4. [Note 18](18_SHORT_FAMILY_COFACTOR_COMPENSATION_20261008.md) and
   [note 19](19_SHORT_FAMILY_EDGE_COMPENSATION_20261008.md), which record
   actual compensated blocks and the need to retain opposing edges.
5. [Note 16](16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md),
   [note 15](15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md), and
   [note 14](14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md), for the
   earlier product barrier, packet geometry and logarithmic bridge.

The [dependency ledger](../../notes/RESEARCH_LEDGER_20261008.md) distinguishes
imported inputs, new deductions and open estimates. The earlier
[program assessment](../../reviews/SHORT_FAMILY_PROGRAM_ASSESSMENT_20261008.md)
is useful strategically, but predates notes 14–19 and is not the latest
statement of the controlled sectors.

At handoff, repository HEAD is
`480581447dcd3e93c9c2f9c22a050d9c5100ff9d`. The latest research package,
including the manuscript, has uncommitted and untracked files. Start in
the existing local checkout; a worktree created solely from HEAD will
omit those results. Inspect current changes and preserve them.
No commit, tag or manuscript snapshot was created in this continuation.

The manuscript's last checked SHA-256 is
`373014701a7fa9cdc1562f60c8d10aedc01b2147031c1a0fda4a1453808813dc`.
The desktop editor's native compiler returned success for that source.
If the hash changes, read the newer version and reconcile the changes;
do not restore the recorded version over subsequent work.

## What has been proved

Use the good ideal monoid, fixed finite-order twist \(\nu\), physical
sextic characters with their zero extensions, and
\(\lambda_u(n)=\nu(n)\chi_n(u)\). For an annular profile \(W\),
\(\int W=0\), put

\[
 z=\sqrt{CD},\qquad c_z=m_z*m_z,\qquad
 m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},\qquad
 Y_u^{(\theta)}=D^{1-\theta}/L_u,
\]
\[
 S_u(X)=\sum_m\lambda_u(m)W(Nm/X),\qquad
 T_u^{(\theta)}=-\sum_{Nd>Y_u^{(\theta)}}
           c_z(d)\lambda_u(d)S_u(D/Nd).
\]

Here \(L_u=Q_uNE_u\) combines the inducing primitive conductor and
extra deletion modulus; it is comparable to the good radical of the row.
The full response is \(A_{u,W}=I_u^{(\theta)}+T_u^{(\theta)}\).
The small-product response \(I_u^{(\theta)}\) has arbitrarily rapid
decay in normalized mean square under the complete Schwartz row weight.

For the projection of \(T\) onto nonsquarefree total ideals, note 17 proves

\[
 \mathcal E_{\rm nsq}^{(\theta)}(D,H)
 :=D^{-1}\sum_{u\ne0}\Phi(Nu/H)|T_{u,\rm nsq}^{(\theta)}|^2
 \ll_\varepsilon D^\varepsilon
 \min\{HD^{1-\theta},D^{-\theta/2}B(D,H)\},
\]
\[
 B(D,H)=H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6},
 \qquad 0<\theta<1,\quad 1\le H\le D.
\]

The proof uses the existing masked completion, radical-weighted row mass,
and imported sixth-order physical operator. Square-divisor
inclusion–exclusion makes \(T_{\rm nsq}=-I_{\rm nsq}\) pointwise.
Small square roots are controlled by free completion. Large square roots
give sparse columns after removing sixth powers. Fixed binary intervals
handle the row-dependent divisor prefix before the operator is applied.

At \(H=D^{2/5}\), \(\theta=11/20\), this yields
\(\mathcal E_{\rm nsq}\ll D^{19/24+\varepsilon}\), with
\(4/5-19/24=1/120\). The elementary part alone would give \(17/20\),
which is too large for the proposed budget; the sparse operator step matters.

Two further results identify compensation without bounding the whole tail:

- Note 18 proves negligible full weighted energy for an actual
  selected-factor block with \(C_0D/z\le Na\le z\), when
  \(\operatorname{supp}W\subset[c,C_0]\), \(C_0<C\).
  Its complete cofactor inverse vanishes. The range has constant relative
  width and is equivalent to an asymmetric change of factor cutoffs.
- Note 19 proves exact opposing logarithmic-edge coefficients
  \(-2LJ_b(L)\) and \(+2LJ_b(L)\) for a nonunit divisor packet,
  where
  \[
   J_b(L)=\int_0^\infty e^{-Lt}
                 \prod_{p\mid b}(1-e^{-t\log Np})\,dt>0.
  \]
  Positivity concerns one packet; it gives no sign or contraction for
  the response across different total products. The unit exception survives.

## The exact open target

Fix \(H=D^{2/5}\) and \(\theta=11/20\). The full moment target
\(\mathfrak M_W(D,H)\ll_\varepsilon D^{4/5+\varepsilon}\)
is equivalent to

\[
 \boxed{D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})
             |T_{u,\rm sf}^{(11/20)}|^2
                \ll_{\varepsilon,W}D^{4/5+\varepsilon}.}
\]

This is open. For sufficiently large \(D\), the exact coefficient form is

\[
 T_{u,\rm sf}^{(11/20)}
 =\sum_{n\ \mathrm{squarefree}}
 \left[\mu_K(n)+
   \sum_{\substack{d\mid n\\Nd\le D^{9/20}/L_u}}
                        (-2)^{\omega(d)}\right]
                  \lambda_u(n)W(Nn/D).
\]

For zero detection the target must hold for every required derivative
profile \(W=(1+t\partial_t)V\), \(V\in C_c^\infty((0,\infty))\),
with the fixed arithmetic data and constants allowed by the manuscript.
A single convenient profile or finite numerical sample does not suffice.

| Quantity at \(h=a=2/5\) | Exponent | Status |
| --- | --- | --- |
| Generic full-moment upper bound | \(16/15\) | Proved under the imported sieve package |
| Entire nonsquarefree tail energy at \(\theta=11/20\) | \(19/24\) | New proved component bound |
| Proposed full or squarefree-residual moment | \(4/5\) | Open |
| Extracted scalar exponent if that target holds | \(13/15\) | Conditional; below the comparison benchmark \(7/8\) |

## First research tasks

Keep the short-family route as the main investigation for the next
proof-focused milestone. Concentrate on a new signed sector rather than
further shrinking an already negligible one. These are proposed tasks,
not additional proved reductions.

1. **Construct a complete signed cofactor decomposition of the squarefree
   residual.** Start from the displayed coefficient, using a canonical
   prime-factor ordering or exact divisor inversion. Retain coprimality,
   every cutoff and deletion zero. Test whether note 18's complete-cofactor
   cancellation extends to a range of factor norms with growing power
   width. A useful output is an exact identity plus a genuinely new
   sector estimate and a quantified remaining response. Merely changing
   asymmetric cutoffs or recovering an equivalent full moment is not
   that milestone.
2. **Rebuild the mixed-discrepancy bridge for the retained response.** Use
   note 14 and note 19 as algebraic guides, but derive the formula at
   \(\theta=11/20\) with the squarefree selector present. Keep the
   density, both low/high edges, low/low correction, prime powers and
   endpoint terms until recombination. Seek a bound for their signed
   combination. A positive kernel for one canceled packet does not
   control the surviving semiprimes.
3. **Audit a candidate estimate against the surviving coherent rows.**
   Balanced semiprimes have coefficient \(+2\) when
   \(1\le Y_u<\min(Nq,Nr)\); rough squarefree products also survive.
   Before investing in a proposed bound, check what compensates these
   terms and where its power saving enters. Explicitly budget every
   conductor range; fixed-character estimates do not automatically extend
   to growing conductors.

For additional techniques, consult the
[signed Mellin continuation](../../../prime-variance-exponents/notes/SIGNED_MELLIN_CONTINUATION_20261004.md)
for summing complete cofactors before absolute values, and the
[arithmetic closure attempt](../../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
for coupled discrepancy and renewal formulations. Their integer estimates
cannot be transferred to ideals or made conductor-uniform without proof.
Neither source proves the missing fixed power contraction.

If every attempted reformulation preserves the same unresolved moment and
exposes no new cancellation, record that conclusion and reassess the
parallel mixed-character route rather than declaring a power saving.

## Constraints that prevent false progress

The bound \(19/24\) is the energy of a difference vector. It permits
moment-target equivalence by the weighted triangle inequality; it is not
an additive identity
\(\mathfrak M=\mathcal E_{\rm sf}+O(D^{19/24})\), because a cross term
has not been bounded separately.

The earlier packet theorem's uniform sector estimate and coherent
illustrations use \(\theta=1/40\); its finite divisor identity holds
whenever its \(z,Y\) hypotheses hold. Full tails at two fixed buffers
are close, but their product projections need not be.
Do not combine projected estimates from the two cutoffs without a new
argument. Once \(n=abm\) is restricted to squarefree ideals, the factors
are squarefree and pairwise coprime; the \(m\)-sum is no longer free.

Do not replace the complete signed response by separately bounded prime
pieces, absolute Möbius envelopes or arbitrary bounded coefficients.
The coherent-row term \(DH^{1/6}\) survives such broad classes. The
selected-piece lower bounds in notes 15–19 illustrate required
compensation and are not lower bounds for the full tail. Their coherent
branch illustrations specialize to \(\nu=1\).

The deep native Poisson/reciprocity and de Faveri sieve inputs remain
imported. There is no new full-moment exponent, zero-free region, proof
that quasi-RH implies RH, or independent specialist validation.

## Checks and saving the next result

The three latest deterministic checkers and small JSON records are in
[`../../numerics/`](../../numerics/README.md):

- `check_short_family_squarefree_projection.py`: 594,360 exact assertions.
- `check_short_family_cofactor_compensation.py`: 18,442 exact assertions.
- `check_short_family_edge_compensation.py`: five packets, 52 triple terms,
  208 phase/deletion checks and 24 rational-log cases.

Two fresh runs reproduced each saved record byte-for-byte. These verify
finite algebra and rational budgets, not the analytic inputs or asymptotic
moment bounds. Recheck affected identities when an argument changes;
do not confuse a larger assertion count with a stronger theorem.

Save research as the next unused numbered note in `short_families/notes/`,
calculations in the shared `numerics/`, and scoped audits in `reviews/`.
Include author, LLM, model and effort metadata, reporting unavailable
configuration fields honestly. Follow the root `LARGE_FILES.md` policy.
Use small source files and records; do not create manuscript snapshot
folders. Update the concise `DRAFT_HISTOR.md` for substantive milestones.

When a new theorem is ready, add its proof to the existing
`short_families/short_family_reductions.tex`, preserve the author's and
LLM acknowledgement fields, keep that editor open, and check the saved
source with the built-in `compile_latex_document` tool. Notes 18–19
currently remain supporting notes; note 17 is incorporated in the manuscript.

## Codex or ChatGPT for the next session

Use **Codex in the current local checkout** as the main continuation.
This task repeatedly requires exact repository context, calculations,
proof audits and in-place manuscript edits. Codex supports direct local
file inspection, edits and execution; the desktop interface also provides
Git review controls. See the official
[Codex documentation](https://learn.chatgpt.com/docs/cli) and
[local environment documentation](https://learn.chatgpt.com/docs/environments/local-environment).

Use a separate ChatGPT session optionally for a focused conceptual
challenge: supply this note, the complete candidate proof and its stated
inputs, and ask for a counterexample or a missing hypothesis. Return any
proposed repair to the repository session for verification. This division
is a workflow judgment, not evidence that either interface is inherently
better at mathematics. Model capability and the exact supplied context
matter; a second LLM session is not independent mathematical refereeing.

Suggested opening instruction for the new session:

> Continue the short-family investigation in the existing local checkout
> at /Users/ebbaker/Documents/shifted-zeta-positivity. Read
> papers/quasi-rh-exponent-descent/short_families/notes/20_SHORT_FAMILY_SESSION_CONTINUATION_20261008.md
> and the files it prioritizes. Preserve all current changes. Seek the
> first new signed squarefree-sector estimate described there, retaining
> the actual cutoffs, masks and compensating terms. Distinguish every
> proposed argument from a proved bound. Save the derivation and scoped
> audit, and incorporate a proved milestone into the existing manuscript
> with a successful native compilation check.
