# Assessment of the evolution-first manuscript rewrite

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0002, thread `01a17600-b15f-7f52-8713-31fa13599341`.

**Disposition:** the requested manuscript integration and planning
revision are complete at editorial/synthesis scope. This is the same
assistant's consistency and production assessment, not an independent
mathematical review. No new asymptotic theorem is accepted here.

## Scope and preserved evidence

The [manuscript](../manuscript/main.tex) now leads with controlled
large-height asymptotics for all times, uses the exact evolution/error
equations as its organizing method, and retains the fine t=64 transition
as supporting work. It distinguishes fixed times, compact-time uniformity
and joint time-height limits. [Note09](../notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
records the source map and the one additional product-rule display for
carrier-normalized error.

Text-identity checks retained all 54 original equation, align and
proposition environments verbatim. These include the compact-positive,
buffered crossover, two negative-time accuracy scales, joined estimates
and regulator center/rounding displays. The 11 research-note inputs in
the rewrite manifest are unchanged. These checks confirm editorial
preservation, not correctness of the inherited proofs.

The old Note03 bibliography wording left its complex-buffer gap open;
the rewrite now explicitly records that Note04 closed it at the stated
bounded scope. All statements retain the same-model, proved-in-note
qualification and unevaluated constants/onsets. No parent HDA status
changes.

## Mathematical consistency checks at synthesis scope

1. The original-time residual is r_F=F_t+F_zz. E=H-F obeys
   E_t+E_zz=-r_F, so the direct time error uses spatial error and the
   actual residual rather than differentiation of a bound.
2. T=-t changes the sign: d=f_T-f_zz=-r_F(-T), and the Duhamel error
   formula subtracts the integrated d. Its direction is T>=T0. The
   manuscript does not assert stable backward recovery for arbitrary
   data or carrier-relative contraction from an absolute norm.
3. The carrier-normalized equation retains the drift -2 A_x/A and
   zeroth-order coefficient (A_T-A_xx)/A, and spatial localization
   retains both commutators. Required tails and complex-strip losses
   are explicit proof obligations.
4. The amplitude/phase and product-residual identities apply to named
   nonvanishing arms. Canonical initial matching, all modes and the RS
   correction remain required; no global nonvanishing form of H is used.
5. The negative-time modal expression preserves the damping, phase drift
   and correction multiplier. Fixed-mode damping and relative-weight
   scales are separated from the growing cutoff population and the
   signed total. The natural-to-outer conversion still pays exp(T L²/16).
6. The observable equations retain the actual covariance, physical q,
   residual forcing, regulator curvature and current defect. Zero spatial
   regulator curvature at negative time does not remove its time forcing.
   A new physical-transfer theorem is not inferred from these identities.

**A residual identity alone does not establish a carrier-relative field
error.** The next packet's o(|G|X^-3/4) objective and illustrative
|G|X^-5/4 logarithmic rate remain targets. Neither is reported as a
result of this rewrite.

## Planning and archive checks

[Overview02](../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
and [Progress02](../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
are the current planning pair. The old pair carries explicit supersession
notices. A02-AN03 is primary next, Analysis — Sol; A03-AN01 is retained as
deferred supporting work. The frozen mathematical request and return
text in both pending packets is unchanged byte-for-byte from its frozen
request heading onward. A08 assigns the already documented positive-time
coverage gap; it is not an additional claimed result.

Both ansatz chats are uniquely registered, and the repository capture
helpers verify their stored/canonical hashes, counts, original identities,
first-capture provenance and public-source prefixes under the shared lock.
The [verification receipt](../chat-histories/VERIFICATION_20261025_EVOLUTION_REWRITE.json)
records the snapshot. The current final is captured after it is actually
sent; no transcript is hand-edited or synthesized in advance.

## Production checks and limitations

The final manuscript compiles to **26 pages**, with no overfull/underfull
boxes, LaTeX/package warnings or unresolved references reported by the
build. All pages were rendered and inspected in contact sheets; the new
evolution, negative-time mode, physical-forcing and coverage-map pages
were also inspected at readable resolution. A long definition display was
split into two lines; the table of contents fits on one page and the
coverage table is kept together. No clipping, overlapping text or missing
glyphs was seen. Local documentation links and Markdown table structure
were checked after the final records were written.

The [build record](../manuscript/BUILD_RECORD_20261025_EVOLUTION_REWRITE.json)
pins the final source/PDF hashes and production scope. Generated PDFs and
compiler intermediates stay in the ignored root output tree; temporary
page renders remain outside the repository. No numerical, symbolic or
interval research was executed. Compilation, hashes, layout and internal
algebra checks do not independently validate the inherited mathematics.

The next analytical deliverable remains [HDA-A02-AN03 r1](../research-progress/handoffs/HDA-A02-AN03.md),
**Analysis — Sol**, prepared and not dispatched. Wider all-time estimates,
physical transfer, useful cost and independent review remain open.
