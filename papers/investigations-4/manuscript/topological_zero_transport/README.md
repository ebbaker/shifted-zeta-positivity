# Topological Zero Transport and the Phase of the Discriminant

23 October 2026. Drafted for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant derivation and self-review; no independent specialist validation.

**Maintained working manuscript:** [PDF](main.pdf), [main source](main.tex), [build record](BUILD_RECORD.json). This is the additional reader-oriented paper requested by the author. The existing [Zero Counts, Heat Transport, and Localized Hodge Energy](../zero_count_heat_transport/README.md) remains a separate catalogue; its files were preserved in this round. This directory is not a historical snapshot.

The central equation is **(1.2)** on the first page:

\[
I_0=\frac{k_\epsilon}{2\pi}\operatorname{Im}\int d\log(\Delta\mathscr U)
   +J_++J_-+R-Q.
\]

It relates a physical initial-cap integral to future collision charge and a complete set of boundary contributions. The terminal term is the phase of the squared Vandermonde times the analytic factor at the roots. Fixed projective walls following regular roots have zero flux. Theorem 1.1 gives growing-population asymptotics; Theorem 5.1 characterizes the surviving closures at a fixed event core.

The principal new estimate is uniform for K=o(L sqrt(kappa)), with L~log(T)/4 and kappa~8TL. The full terminal cap per root tends to r²Y/pi, while its Vandermonde contribution has a smaller controlled phase. Each imaginary-time face on [theta T,T] has flux per root O(1/log T). These statements concern large heat time, with ranks allowed to grow. They do not give a fixed-heat all-height theorem or close the early boundary starting at zero.

## Reading and source map

| File | Content |
| --- | --- |
| [main.tex](main.tex) | Abstract, organizing formula, headline quantitative theorem, literature and novelty scope. |
| [boundary.tex](boundary.tex) | Local heat charge, normalization, exact cap reduction, moving wall and complete transport. |
| [asymptotics.tex](asymptotics.tex) | Population-linear Vandermonde estimate, complete-source moments, growing complex disks and late edge asymptotics. |
| [closures.tex](closures.tex) | Fixed-core closure limits, exact controls, outstanding early-boundary estimate and acknowledgements. |
| [references.tex](references.tex) | Seventeen external references and the research archive. |

The [incremental Note 12](../../notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md) records what this continuation adds. The [literature and proof review](../../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) identifies classical overlap, actual source access, proof checks and the unresolved novelty question. The [shared progress register](../../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md) owns the task status; this manuscript adds no separate competing ledger.

## Research provenance

- [Home 11 Note 01](../../11_late_heat_caps_and_charge_transport/notes/01_FINITE_PROJECTIVE_TUBES_AND_COMPLETE_ATTACHMENTS_20261022.md): finite physical root tubes, exact walls and complete attachments.
- [Home 11 Note 02](../../11_late_heat_caps_and_charge_transport/notes/02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md): complete complex-time source and fixed-rank physical caps.
- [Home 11 Note 03](../../11_late_heat_caps_and_charge_transport/notes/03_FIXED_RANK_PAIR_CANCELLATION_AND_TUBE_CONTROLS_20261022.md): fixed-rank pair/unit cancellation and exact tube controls.
- [Home 11 Note 04](../../11_late_heat_caps_and_charge_transport/notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md): fixed-core closure allocation, reorganized here with an elementary comass bound.
- [Base Note 10](../../notes/10_GROWING_CLOCK_WINDOWS_20261022.md): growing real spatial clocks, preceding the new complex-time population estimate.
- [Base Note 11](../../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md): real initial angular integral and high-height birth budgets. That observable is not substituted for this paper's physical three-form cap.

The [result index](../../../../result-summaries/README.md) and [avoid index](../../../../avoid/README.md) retain the repository's scope discipline. The paper consolidates classical/inherited identities and adds the explicitly identified quantitative estimates. It claims no new invariant, no RH conclusion, and no verified priority. A specialist assessment of the narrower quantitative contribution remains appropriate before publication.

## Build and diagnostic checks

Open this directory in the built-in LaTeX editor, with `main.tex` as the main file. A local build can also use `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. The PDF is retained with the source; intermediate build files belong outside the repository or in an ignored build directory.

The [small numerical record](../../numerics/TOPOLOGICAL_CAP_CHECKS_20261023.json) and [reproducible script](../../numerics/check_topological_caps_20261023.py) support sign, winding and algebra checks. They neither evaluate canonical theta caps nor provide interval certification. The proofs are analytic. The exact generated-source/PDF hashes and preservation check are recorded in `BUILD_RECORD.json`.
