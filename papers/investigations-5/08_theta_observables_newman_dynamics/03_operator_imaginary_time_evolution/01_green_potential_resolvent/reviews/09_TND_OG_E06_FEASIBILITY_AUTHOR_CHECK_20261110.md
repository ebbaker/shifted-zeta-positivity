# E06 r1 proof and code-author check

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual backend and reasoning effort are
unavailable. This is internal proof/code-author checking with a separate
read-only formula subcheck under inherited model settings. The scalar
calculation uses the inherited E03/E05 bounds.

- **Identity.** The [return][return] records all frozen packet checks.
  The one E06 manifest difference is a dated appendix to avoid11. The
  original byte prefix matches exactly and the appendix does not change
  a bound. All formula and request bytes match. The older E03/E05
  differences affect history guidance or later catalogue entries.
- **Budgets and centers.** \(h=\sin(a)/(8\cosh(a))\),
  \(h_a=\eta_{\rm eval}=h/2\). Each of the four radii is
  \(\eta_{\rm eval}/8\), hence the resulting interval width is
  \(\eta_{\rm eval}\). F2 uses \(M_v=|2v|+26\),
  \(\log p_v=\log(2(26/3)n_v^3/(n_v-1))+51A_v/n_v\), and
  the directed ceiling of \(A_v/\kappa\) at all 132 centers. The maximum
  F2 exponent is enclosed below 4533. Every chosen dyadic satisfies
  the local per-cell bounds, and the actual sum of upper allowances
  is independently compared to \(h_a/3\).
- **Source.** The ratios in Note06 (15) use \(2N+3\) and are applied at
  \(N=0\) for \(B_0\). The two F4 tests are in log space. With the
  source factor \(1/2\), each majorant paying \(\delta/2\) gives
  \(\mathcal B\delta_H\le(\delta/2+\delta/2)/2=\delta/2\).
  Both source searches and the tail search reject all candidates before
  the first certified hit. \(Q=32\) uses the directed upper endpoint
  and the prime tail is tested separately.
- **Midpoint and nodes.** Retain Note06's conservative \(R L_g\Delta\)
  with \(\Delta=2R/N_{\rm pan}\), so F6 has \(2R^2\) even though
  Note07 gives a tighter Lipschitz cell estimate. \(K\le1/16\)
  and total integration length \(2R\) give weight at most \(R/8\).
  Thus \((R/8)(e_F/\delta)=e_{\rm node}\) for evaluations of the exact
  declared finite approximant. The source allocation is separate.
- **Decision.** The stable log-sum uses
  \(\max(x,y)+\log_2(1+2^{\min(x,y)-\max(x,y)})\).
  Exact rational comparison of the emitted dyadic endpoints verifies
  the coarse displayed intervals, budget separations and
  \(5252.8622>19.9316\). The kernel-only lower bound follows by
  adding the two stored lower endpoints for \(\log_2 L_1\) and
  \(\log_2 C\). The arithmetic uses 128-bit balls. No integer panel
  count above the cap is constructed.
- **One bounded reporting correction.** The first execution stored the
  exact lower endpoint for each closest rejected candidate under the
  label “gap.” The corrected code stores the full directed gap enclosure
  for that candidate and retains the minimum-lower-endpoint selection.
  No branch predicate, formula, allowance, cutoff or outcome changed.
  Both runs resolved at 128 bits and the combined scalar work took
  less than 0.007 seconds. The [return][return] preserves initial and
  corrected hashes and timing. The replay record is the corrected run.

The [research note][note] records the scoped stop and collision screen.
The directed lower bound is on the recipe's sufficient allowance.
The actual error or cost of integration, a favorable value and
a sharper method remain undetermined.

[return]: ../research-progress/handoffs/21_TND_OG_E06_FEASIBILITY_RETURN_20261110.json
[note]: ../notes/11_TND_OG_E06_SINGLE_TUPLE_FEASIBILITY_20261110.md
