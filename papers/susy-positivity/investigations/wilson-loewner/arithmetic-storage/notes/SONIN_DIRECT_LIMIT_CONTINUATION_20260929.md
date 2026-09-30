# Continuation of the direct positive approximation program

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is a continuation handoff, not a
new mathematical result or independent specialist review.

Continue the search for independently positive forms converging to the
complete arithmetic Weil form. The immediate task is to derive a usable
trace representation for the regularized Sonin family, with its boundary
correction retained. This note records the current state, a bounded next
assignment, and a recommendation to use Codex with the local repository for
the main research continuation.

## Objective and required context

The target is one specified, source-independent family satisfying

\[
P_j[F]\geq0,\qquad P_j[F]\longrightarrow Q[F]
\]

for every fixed compact smooth pole-neutral source, with arbitrarily large
supports admitted. Source preparation is
\(F=(-d^2/dx^2+1/4)h\), with \(h\in C_c^\infty\).
Positivity must follow from the construction without a zero-location
assumption. Identifying the limit with the complete arithmetic expression is
a separate obligation.

The user explicitly chose this direction over making constrained domination
of the odd source the next prerequisite. Do not resume finite-stage
domination, higher moments, or greater numerical precision by default.
Those tools remain available when a specified limiting argument needs them.

Read these first:

1. [Project overview](../PROJECT_SUMMARY.md), especially the active plan and
   decision criteria.
2. [Direct positive approximation program](SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md).
3. [Regularized positive family](SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md)
   and its [internal crosscheck](../reviews/SONIN_DIRECT_LIMIT_REVIEW_20260929.md).

Use the [topology analysis](SONIN_POSITIVE_LIMIT_TOPOLOGY_20260929.md),
[place addition criteria](SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md), and
[canonical comparison audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md)
for proofs and conventions. The
[program meta analysis](../../../../../investigations/program-meta-analysis/README.md)
supplies the broader context. Older continuation notes are historical;
their scalar and first-moment tasks have already been addressed.

## Results and limits to carry forward

The current research notes establish the following internally checked
statements. Their same-model review is not independent human refereeing.

- The raw prime-cutoff candidate is
  \(P_R[F]=\|C_F\Pi_{S_R}\|_{\mathrm{HS}}^2\), using the actual orthogonal
  projection onto the transported Sonin space, including its inverse
  compressed metric. For pole-neutral sources its exact discrepancy is
  \(P_R-Q=E_\infty+\Delta_{S_R}+W\). The complete active prime-power sum
  \(W\) is finite on each fixed source; further geometric places can still
  change the positive trace.
- Replacing prime weights by \(p^{-\sigma}\), for fixed \(\sigma>1\),
  gives bounded invertible infinite-place transport and a positive form
  \(B_\sigma\). Source-smoothed trace operators converge in trace norm as
  the prime cutoff grows. These estimates do not reach the critical line.
- A bounded phase continuation defines actual intersection projections
  \(\Pi_\sigma\). The functional equation gives
  \(\Pi_\sigma\to0\) strongly as \(\sigma\downarrow1/2\).
  Strong convergence alone does not determine the smoothed trace limit:
  positive frequency measures can concentrate while the projections tend
  strongly to zero.
- For fixed source-independent finite-rank projections \(E_N\uparrow I\),
  \(P_{\sigma,N}[F]=\|C_F\Pi_\sigma E_N\|_{\mathrm{HS}}^2\) is always
  finite and positive. Fixed \(N\) gives zero at the critical endpoint.
  A nonzero arithmetic limit needs growing resolution and a justified
  limiting prescription common to the source class.
- A single fixed bounded compression on ordinary logarithmic \(L^2\)
  cannot realize \(Q\) on the full admissible all-support class. This
  restricts the endpoint realization; it does not rule out singular limits
  of positive forms. Conditional moving-tail and signed-covariance criteria
  also exist for the raw prime sequence, but their growing-family hypotheses
  remain unproved.

No arithmetic limit or RH proof has been obtained. Full phase-family
smoothed trace finiteness for \(1/2<\sigma\leq1\) is open here. The raw
critical prime sequence and the analytically continued phase family are
distinct candidates, with no theorem identifying their limits.

## First assignment for the next session

**Derive a projection trace formula with an independently represented
boundary correction, initially for \(\sigma>1\).** This is a proposed
bounded step toward arithmetic identification, not a claim that this family
will succeed or a replacement for the broader construction search.

The known positive quantity is

\[
B_\sigma[F]=\|C_F\Pi_\sigma\|_{\mathrm{HS}}^2
=\int |\widehat F(t)|^2\,d\nu_\sigma(t).
\]

Seek an actual kernel or compressed-resolvent representation for
\(\nu_\sigma\), or directly for the smoothed trace. Use it to expose how
the gamma/contact contribution and the prime coefficients enter. A useful
target decomposition on prepared sources is

\[
B_\sigma[F]=\Gamma[F]-W_\sigma[F]+K_\sigma[F],
\]

where \(W_\sigma\) retains every active prime power with weight
\(p^{-m\sigma}\). The correction \(K_\sigma\) must be given by an
independently derived operator or kernel expression. Simply defining it as
the difference of the two sides adds no information. Likewise, the existing
compressed-metric formula is a starting point; merely renaming that formula
as a density is not the requested advance.

The phase derivative has the expected prime coefficients, but has not been
proved equal to the positive projection's frequency density. The
archimedean calibration detects an omitted correction: as
\(\sigma\to\infty\),

\[
B_\sigma[F]\longrightarrow
B_\infty[F]=\Gamma[F]+E_\infty[F],\qquad
W_\sigma[F]\longrightarrow0.
\]

Thus a valid correction must recover \(E_\infty[F]\), which is not
identically zero. A formula that discards it already fails this test.
Also, \(\Gamma-W_\sigma\) is the useful artificial arithmetic deformation
defined in the regularization note; it is not the full shifted
completed-zeta form.

The session should deliver one checked representation or a precise
obstruction to deriving it, with:

1. Exact Fourier normalization, domains, cutoff conventions, and the actual
   orthogonal projection or compressed metric.
2. A justified kernel or resolvent formula, with the needed trace and
   interchange arguments, and the archimedean calibration above.
3. Identification of the specific estimate or domain issue that blocks
   continuation toward \(\sigma=1/2\). If full traces become unavailable,
   state what survives for the finite-rank positive forms.
4. One resulting concentration or discrepancy lemma to pursue next, or a
   reason to revise the candidate family.

Do not assume half-plane innerness or absence of off-line zeros. Do not infer
trace convergence from strong projection convergence. Keep arithmetic
identification separate from existence of an unknown positive limit.
Choose numerical work only if the representation yields a specific
asymptotic claim it can discriminate. No large numerical run is needed to
complete this first assignment.

## Recommended working environment

**Use Codex with the local repository for the main continuation.** This is
a workflow recommendation: the next assignment depends on exact conventions
across several notes, reusable projection tools, reproducible calculations
if needed, and durable records of what was proved. Keeping that work in the
repository makes the reasoning and changes easier to inspect.

OpenAI's current documentation says ChatGPT Work and Codex have overlapping
capabilities; Codex exposes more developer detail and review views. It does
not establish that one interface reasons better about this mathematical
problem. ChatGPT Work with access to the same local files is also a suitable
choice if its presentation is preferable.
[Official product comparison](https://learn.chatgpt.com/docs/use-chatgpt).

Use a separate ChatGPT discussion when useful for conceptual criticism,
alternative constructions, or explanation. Give that discussion the current
note and the specific argument to challenge, then reconcile any findings
into the repository. A different interface or another LLM review alone
does not constitute independent mathematical verification.

For a new session, use the actual repository
`/Users/ebbaker/Documents/shifted-zeta-positivity` as the working project,
and begin with this note. Verify access to the current files rather than
assuming a shared conversation transfers the repository. Official guidance
distinguishes conversation history from local project-file access.
[Projects and chats](https://learn.chatgpt.com/docs/projects).

## Repository handoff

Preserve existing working-tree changes. Keep incremental research in
`notes/`, reviews in `reviews/`, and small reproducible numerical code and
records in `numerics/`. Follow the root `LARGE_FILES.md` policy. Synced
ChatGPT project files under `sources/` remain read-only references. Record
the actual model and reasoning effort when available; do not infer missing
metadata. No new manuscript snapshot, commit, or push is requested.

Suggested opening instruction for the next session:

> Continue from this note and the linked project overview. Carry out the
> bounded projection trace representation assignment for the regularized
> positive Sonin family, starting at sigma greater than 1. Preserve the
> independently derived boundary correction and verify the archimedean
> limit. Save the derivation and a separate critical review. State exactly
> what is proved and what blocks arithmetic identification. Keep direct
> positive approximation as the objective; do not make odd-source domination
> or a new numerical campaign a prerequisite.
