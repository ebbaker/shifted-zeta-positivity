# GNP-BB-E01 r1 return — complete outer estimate

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent per-turn backend and usage metadata
were unavailable.

**Disposition: complete at the fixed E01 r1 scope, proved in-note from the
named inherited inputs; proof-author assessment only.** The
[frozen request](GNP-BB-E01-r1.md) matches its committed bytes. The
[execution record](../../numerics/03_GNP_BB_E01_INPUTS_AND_CHECKS_20261113.json)
confirms all 17 frozen inputs by size and SHA-256.

The [proof](../../notes/06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md)
uses HDA Note04 CS2–6 on recentered \(r=1,b=9\) charts, HDA Note03
CB4, and the parent transition section's normalization. It accounts
for the complete finite arms, fixed cutoff, corrected term, remainder
and Gaussian tails. It derives finite \(A,B\) and a uniform finite
onset from the inherited buffer and geometry gates together with
\(L_X\ge288A\), \(X-1\ge(288B)^{128/3}\). The ordinary shifted zeta
is independently analytic and nonzero on the closed rectangle's
neighborhood, with \(|1/Z_\lambda|\le9\) on the rectangle.

For every sufficiently large center \(X\) on the prescribed
\(\lambda_X=1/L_X\) curve, the proof acquires
\[
 \sup_{\overline D_X}|H_{\lambda_X}/C_- -Z_{\lambda_X}|
 \le A/L_X+B(X-1)^{-3/128},\qquad
 \sup_{\overline D_X}|F_{\lambda_X}-1|\le1/16 .
\]
On the exact field, Cauchy gives \(m=1/2, M=2,h=1/8>\eta=1/16\) with
floor \(1/4\). Polymath Theorem 3.2 and conjugation then give
\[
 H_{\lambda_X}(X+iy)=0\ \Longrightarrow\ |y|<a_X-1/16 .
\]
This implies the frozen weak bound. The same data give the complete
Green comparison \(\log(17/15)<\log(19/16)\), and already imply
nonvanishing throughout the rectangle.

The [assessment](../../reviews/02_GNP_BB_E01_SELF_ASSESSMENT_20261113.md)
reviews the frozen acceptance tests. No allowance remains unpaid
within their scope. The numerical onset, compact heights,
common-time global coverage and additional inward steps have not
been obtained. HDA's provider retains the evidence level “proved
in-note from named classical inputs; same-model internal assessment
only.” A further step requires its own classified contract in the
[sole register](../01_GNP_BB_RESEARCH_PROGRESS_20261113.md).

