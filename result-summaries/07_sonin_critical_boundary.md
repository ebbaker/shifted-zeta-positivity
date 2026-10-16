# Sonin critical boundary: trace limits, place addition, single-probe equivalence, finite certificates

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

- **Sonin critical limit (Thm 1.1, Cor 6.3).** Unit-window mass is
  \(\le M\log(2+|j|)\) uniformly in \(\sigma>\tfrac12\); \(\Pi_\sigma\to0\)
  strongly, while the traces of the majorant \(L_\sigma\) and of each fixed
  Abel approximant \(\Pi_{\sigma,r}\) converge to \(\int|f|^2d\mu_{\rm crit}\);
  every exact-projection limit has the form \(\sum c_\gamma\delta_\gamma\)
  with \(0\le c_\gamma\le m_\rho\). Full survival \(c_\gamma=m_\rho\) is not
  asserted, and by Cor 9.2 even full survival gives \(Z_{\rm crit}\), not
  \(Q\).
- **Return defect and projection loss (Thm 7.1, Cor 7.2, Thm 8.1).** Loss
  concentrates at cutoff spectral value one; the limit holds for \(g\)
  continuous at 1 and fails for the indicator; a rational family with a
  positive prelimit gap has \(\Pi\equiv0\). Local data cannot fix the exact
  weights.
- **Finite Euler identity and fixed-place obstruction (Props 3.4, 9.3).**
  \(\Pi_{S,\sigma}=D\Pi_\infty M^{-1}\Pi_\infty D^*\); once \(S\) contains all
  active primes, \(Q=B-K\) on prepared sources; for every fixed \(S\),
  dilated sources give \(K>B\ge0\). The support-adapted inequality
  \(K\le B\) is open and is exactly Weil positivity.
- **Signed place-addition laws.** \(\delta_p=-\beta\int(h_F(t)-t)/(1-\beta t)\,d\mu_F\),
  with complete- and partial-residual laws; a \(2\times2\) control shows
  either sign occurs generically. "Usable lemmas, not a residual-sign theorem."
- **Single-probe equivalence (Thm 10.3).** For one prepared probe \(g\):
  RH, all-window positivity, bounded \(M_g\), subexponential \(M_g\), and
  either one-sided envelope are equivalent; prime powers contribute
  \(o(1)\); the only unconditional envelope is \(O(e^{r/2-c\sqrt r})\).
- **Finite certificates.** \(|M_g|<1.48\) on \([2,500]\); seven-translate
  Gram \(>I/20\); \(\Theta_g<-5\) on \([100,225]\); \(Q\ge0.09\|F\|^2\) and
  \(Q\ge B/9000\) at \(L=1\), \(S=\{2\}\); \(Q\ge\tfrac3{2000}\|F\|^2\) at
  \(L=6/5\), \(S=\{2,3\}\); \(V_g<38X^2\) for \(e\le X\le10^{99}\).
- **Subpower reductions (Props 11.3–11.6).** RH \(\iff V_g(X)=O_\delta(X^{2+\delta})\)
  for all \(\delta\); one fixed \(\delta\) excludes zeros with
  \(\operatorname{Re}\rho>\tfrac12+\delta/2\).

## Status

"Proves" (README); two cross-model Claude rounds found "no mathematical
error" (1 October); certificates "certified", outward at 192/256 bits.
Since the 1 October rounds the manuscript grew from 1,782 to 3,874 lines
with only same-model checks, and the draft history ends on a working-tree
revision.

## Caveats

Critical-line mass in a majorant or Abel limit does not settle exact
projection mass survival or the contribution of off-line zeros; the
introduction was rewritten after review for describing "a phenomenon the
paper never exhibits for a projection". Mean-only and finite-rank penalty
bounds were retired (a translated resonance gives \(K>0\) with infinite
positive index). All four all-window strategies tested on 3 October fail
for stated reasons.

## Reusable for

Uniform Toeplitz–Hankel trace control; the finite Euler identity as the
exact form of the prepared-source target; the single-probe reformulation
of RH as growth of one function; the signed place-addition laws as lemmas.

## Where

- [README](../papers/investigations/sonin-critical-boundary/README.md); [manuscript](../papers/investigations/sonin-critical-boundary/manuscript.tex) (Thm 1.1, Cor 6.3, Thm 7.1, Thm 8.1, Props 3.4 and 9.3, Cor 9.2, Thm 10.3, Props 10.11–10.15, 11.1–11.6); [draft history](../papers/investigations/sonin-critical-boundary/DRAFT_HISTORY.md).
- Reviews: [Claude round 1](../papers/investigations/sonin-critical-boundary/reviews/MANUSCRIPT_REVIEW_CLAUDE_20261001.md), [response](../papers/investigations/sonin-critical-boundary/reviews/RESPONSE_TO_CLAUDE_REVIEW_20261001.md), [round 2](../papers/investigations/sonin-critical-boundary/reviews/MANUSCRIPT_REVIEW_ROUND2_CLAUDE_20261001.md), [finite Euler audit](../papers/investigations/sonin-critical-boundary/reviews/FINITE_EULER_BOUNDARY_AUDIT_20261003.md), [latest work assessment](../papers/investigations/sonin-critical-boundary/reviews/LATEST_WORK_ASSESSMENT_20261003.md).
- Notes: [finite Euler identity](../papers/investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md), [single-probe growth theorem](../papers/investigations/sonin-critical-boundary/notes/SINGLE_PROBE_GROWTH_THEOREM_20261003.md), [handoff with the bounds table](../papers/investigations/sonin-critical-boundary/notes/NEXT_SESSION_GLOBAL_GROWTH_HANDOFF_20261003.md), [non-bootstrap theorem](../papers/investigations/sonin-critical-boundary/notes/subpower-milestones/04_structural_nonbootstrap_20261003.md).
- Place addition: [Sonin place addition and error control](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md); [arithmetic-storage summary](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/PROJECT_SUMMARY.md); [program assessment](../papers/investigations/program-meta-analysis/reviews/ARITHMETIC_STORAGE_PROGRAM_ASSESSMENT_20260929.md).
