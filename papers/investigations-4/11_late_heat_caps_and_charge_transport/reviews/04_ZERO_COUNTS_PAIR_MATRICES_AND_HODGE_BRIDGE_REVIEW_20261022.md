# Internal review: zero counts, pair matrices and reciprocal Hodge transport

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Parent integration review plus separate same-model subagent audits of the matrix and Hodge proofs; the statistics author's self-check and parent review are distinguished from those audits. **No independent specialist or cross-model validation.**

**Verdict: accept Notes 05–08 in their stated finite-domain, fixed-rank and information-class scopes.** The real transport result is credited consolidation, the Hodge count is an explicit refinement of the established area formula, and the canonical Hodge corollary reuses an existing certificate. The finite pair-matrix convergence has a paid canonical source rate. None proves endpoint simplicity, a new PCC theorem or a strict complete-charge bound.

## Mathematical checks

| Item | Assessment |
| --- | --- |
| [Note 05][n5]: all-zero cap balance | The earlier Investigation 22 theorem is cited rather than presented as a new invariant. With source orientation dt∧dx, β is minus the angular current of H+iH_x; its cap includes N/2 and endpoint arctangents. Both moving-wall crossings remain. Real event weight floor(m/2) differs from complex binom(m,2). |
| Complex divisor and endpoint | Holomorphic multiplicity count is constant with zero-free spatial boundary; its current is closed. Interior collisions are not sources of this count. A joint zero on the initial cap fails the boundary-jet hypothesis, so an indentation or link is necessary. |
| Reciprocal normalized cover | Only odd-multiplicity roots branch on the normalization. χ=2−B_odd includes disconnected even-multiplicity normalizations. The singular-fiber excess is N−B_odd=2Σfloor(m/2); both neighboring regular complex fibers still have χ=2−N. Reciprocal differential pole orders and energy divergences are correct. |
| [Note 06][n6]: matrix normalization | Quadratic-form comparison proves the Loewner bounds. The row-sum bound gives 16δΣ(d−2δ)⁻³ and the inherited O_K((L√κ)⁻¹) rate. This is fixed rank only. |
| Complete heat force and dissipation | Root velocity includes 2U_z/U. Triple cancellation gives ||S||²=2Σgap⁻²; the exterior divided difference has the correct sign and factor. The actual theta E′ is eventually positive. The physical/normalized weight ambiguity in (5) was corrected before installation. |
| Clock contraction and polynomial model | The mixed-denominator identity retains the centered full residual. Its lower graph weight yields the stated contraction rate. The √(2t) polynomial scaling gives probabilists' Hermite zeros and norm decay (t₀/t)^(1/2). This deterministic equilibrium is not a GUE distribution. |
| [Note 07][n7]: inverse-square constants | Ordered off-diagonal normalization gives Q_clock→π²/3 and Q_sine=2π²/3, and the discriminant pair term 4mρ²Q. The triangular Fourier representation proves the sine integral. |
| Sparse defects and PCC | The slow-diagonal/averaging proof changes only o(n) compact pair terms when one repeated or very close point is added. Weak pair laws therefore cannot exclude all exceptions or bound singular moments. These are point-array controls, not claimed theta realizations. |
| Tent-test threshold | R₂(s)≤π²s²/3 and the tent's second moment δ³/6 give π²δ³/18. A double contributes 2/m; a gap at most δ/2 contributes at least 1/m. The rate condition remains an unacquired conditional test. |
| Exact heat controls | e^τ cos z+1 has an ordinary event and late simple clock roots. z and e^(a²τ)sin(az)/a have the same tracked root but different root-derivative phases and cap fluxes. Both satisfy the PDE exactly. The scope is finite root data, not the complete global divisor. |
| [Note 08][n8]: low-value count | Rouché plus the area formula on the target disk gives W_<ε=4πεN on finitely connected domains. No separation or simplicity is used. Positive boundary orientation and all components are explicit. |
| Potential and approximation errors | The compact modulus/log potential is C¹ across the cutoff and C^{1,1} near that level, including critical points. There is no interface atom; local zero flux tends to zero at fixed ε. Its η/(2πε) source allowance, cubic-cutoff constant 16η/(9ε), smooth-kernel boundary bias and coefficient 9/(32√3πε) pass. The approximant is explicitly holomorphic. |
| Canonical corollary and continuation | RHE04's existing count two and boundary floor >6.6759×10⁻⁷ imply the exact low-value identity for ε≤6×10⁻⁷. The full moment M₂ controls time perturbation by 3×10⁻⁷ on |τ|≤h; the remaining floor >3.6759×10⁻⁷ permits ε≤3×10⁻⁷ throughout. This proves a source-defined positive disk, not an effective large-time range. No certificate is rerun. |

## Provenance and control screen

The root agent reviewed the integrated proofs. The transport agent separately checked the matrix note and identified the normalized-weight derivative correction. The matrix agent separately checked the Hodge count/regularization note, requested the holomorphic approximant and precise nonsmoothness language, and checked the subsequently added canonical corollary against RHE04. The statistics author supplied its own explicit audit, then the parent checked the constants, sparse-defect argument and exact heat controls. Small exact rational checks for m=2,…,8 support matrix algebra only; the analytical proofs are the evidence.

Montgomery's original pp.181–184 were checked for RH, height unfolding, the conjectured pair law and almost-all simplicity. Joyner–Smilansky, with Zagier's appendix, was checked for the stochastic Dyson equations and stationary density. The topology note cites primary mathematical lecture sources for the current and bordered Riemann–Hurwitz conventions; its relevant finite-domain formulas are also proved or routed to established repository proofs. No literature novelty claim is made.

Applicable generic collision controls pass the transport and Hodge identities. The explicit polynomial/atomic-cosine controls fail the unchanged canonical source; amplitude controls fail canonical normalization. Their purpose is to reject only implications based on those generic data. The actual finite-rank matrix result uses the complete theta source and is compatible with an earlier event. No negative claim is generalized to all pair-statistical, random-matrix or Hodge methods.

The latest RHE15 signed trace is positive on its declared window and its potential is already acquired. Integration preserves that stopped negative-witness status and makes no sibling ledger changes. The original LHCT closure calculation still retains the event charge. LHCT-05–07 and ZTP-05 remain open.

## Repository verification

The integration check validates all local Markdown targets and reference definitions in the seven new files, file-size compliance, and whitespace/diff cleanliness for touched files. Exact counts and any repaired link are added below after execution. No new manuscript, snapshot, numerical dataset or generated history file is edited by hand. The existing chat registration is refreshed by the authorized history tool.

[n5]: ../notes/05_ZERO_COUNTS_REAL_BIRTHS_AND_RELATIVE_TOPOLOGY_20261022.md
[n6]: ../notes/06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[n7]: ../notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md
[n8]: ../notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md

**Executed integration check:** 16 new/updated Markdown files (seven new analytical/program/review files), 465 local link targets, unique reference definitions, balanced display-math delimiters and all files below 1 MiB passed. `git diff --check` on the touched paths passed. The RHE README received a routing link only; its ledger and RHE15 status were preserved.
