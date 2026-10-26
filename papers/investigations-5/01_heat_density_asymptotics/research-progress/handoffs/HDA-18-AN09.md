# HDA-18-AN09 r1 — an effective Gaussian-polynomial core ansatz

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
chat0022, thread 01a17572-5411-7f32-9a12-7d1ba46ad679.

Parent HDA-18, supporting HDA-17. Next owner **Analysis — Sol**.
Preparation phase READY_FOR_SOL, unexecuted; the existing progress
register owns live status. The author requested simpler solution
ansätze, permits different regimes and complicated error terms, and
created ansatz/notes/ as the home of this work. This packet does not
replace the existing weak-filter height-cost task or authorize dispatch.

## Read first and fixed inputs

Follow the repository AGENTS.md, LARGE_FILES.md, model workflow and
chat-history instructions. Read the current overview/progress register,
Summary62, Notes54–55 and 58–61, and
[Ansatz Note01](../../ansatz/notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md).
Save an input manifest before execution. Preserve the complete source,
heat sign, physical q, fixed K and actual covariance; do not silently
replace the original IC23 tuple. Existing parent completion statuses
are unchanged.

## One bounded analytical question

Can the finite-time source field be represented effectively as

\[
F_m(t,z)=[p_m(-\partial_z^2)]^2
\left[\frac{\sqrt\pi}{2\sqrt{a-t}}e^{-z^2/[4(a-t)]}\right],
\qquad a>b,\quad t\le b,
\]

with one real polynomial p_m fixed per target accuracy, while retaining
the same absolute four-jet tolerance for all real heights on the full
declared complex strip?

The underlying nonnegative source is exp(-au²)p_m(u²)². Ansatz Note01
A8 gives a Gaussian-weighted L² existence route; it does not give a
finite degree/coefficient constructor or useful cost. Note58 has a
proven compact-source constructor and is the comparison baseline.

1. Verify the heat/Hermite identities and the weighted L² argument
   analytically, correcting any normalization or domain issue openly.
2. Supply an explicit finite polynomial construction and a degree,
   coefficient and weighted four-jet error ledger in b, Y and epsilon,
   using the full canonical source. Routine choices of a, basis,
   truncation, coefficient rounding and weighted approximation method
   are delegated to Sol. Positivity must survive coefficient rounding.
3. Compare the proven sufficient degree/description bound with Note58
   at the same fixed-b target. Separate a simple formula from a
   genuinely low-degree or economical one; do not claim the latter
   from density of polynomials alone.
4. Identify precisely which unchanged compact-transfer inputs accept
   the new field and which new bounds would be needed before replacing
   the central IC23 field. No global replacement or positive endpoint
   conclusion is required by this packet.

## Evidence, limits and stop

Analytical only: no source/field samples, numerical fitting,
machine-symbolic checks, exact-arithmetic campaign or interval run.
Housekeeping hashes and file/link checks are allowed. Stop after one
effective construction with its degree/error ledger, or at the first
precise unpaid weighted-tail/coefficient/transfer estimate. Record a
failed method and its actual estimate; a bad majorant is not an
impossibility result. Escalate only a specifically identified resistant
structural issue.

Save mathematics in **ansatz/notes/**, an assessment in the investigation's
reviews folder, and any small analytical-only work record in numerics.
Append the actual-model/effort return and disposition here without
rewriting this request. Update the sole progress register and the chat's
unique history. No manuscript change, snapshot or commit is requested.

## Return and disposition

Pending. A bounded analytical result does not by itself change HDA-17
Partial, HDA-18 Gated or HDA-20 unfulfilled.


## Priority disposition — 25 October 2026, later in chat0022

Prepared for Edward Baker with LLM assistance, gpt-6-astra, actual effort
max. The author explicitly prioritized large-height formulas across all
real times and requested a dedicated ansatz manuscript/overview/progress
program. This frozen core request is **deprioritized and unexecuted**,
not rejected or completed. The next chat should follow
[HDA-A01-AN01 r1](../../ansatz/research-progress/handoffs/HDA-A01-AN01.md)
and the [ansatz branch register](../../ansatz/research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md).
Its bounded request and the original evidence above are preserved.
