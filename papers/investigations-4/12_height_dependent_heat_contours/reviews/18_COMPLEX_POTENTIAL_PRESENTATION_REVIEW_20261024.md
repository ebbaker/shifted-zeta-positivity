# Complex-potential presentation review

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning effort max**. This is the revising assistant's own review, not an independent review.

The author requested that [book.tex](../manuscript/book.tex) favor the complex presentation derived in [Note 20](../notes/20_COMPLEX_POTENTIAL_AND_WIRTINGER_FORMULATION_20261024.md). The revised setup defines both Wirtinger derivatives, S=log D and W=2 S_zz. The main field theorem now leads with the complex amplitude equation and first-order complex-potential constraint; the original `eq:SP` label remains attached to its real-coordinate equivalent.

The density proof, phase velocity, current, field proof, Fourier potential selection, normalized-state equation and evolution residual now use the complex notation directly. The proof uses S_z A_z=S_zz A and the scalar heat identity for S, without dividing by H_z. The potential section states the local converse, simply connected domain condition, holomorphic ambiguity and the same global selection obligations. The complex DS-II comparison is normalized to Taimanov's introductory equation (1); the real-coordinate Klein–Stoilov comparison remains available. Real momentum, Hamiltonian and boundary calculations retain their useful geometric form. The old external real forcing W was renamed V_ext to avoid collision with the new complex potential.

The changed residual convention was propagated through both continuity and the final smoothed-observable source, which now uses 2 h^2 Re(conjugate(A) r). The normalized field retains the complete-field potential W; substituting K|psi|^2 would change the evolution. The polynomial proof now verifies agreement of both selected potentials with their explicit lifted expressions.

The [exact checker](../numerics/20_check_complex_potential.py) returns fourteen zero residuals, including the new proof identities, cutoff commutator and arbitrary-amplitude evolution defect. The jet checks allow H and H_z to vanish. [Execution record](../numerics/20_COMPLEX_POTENTIAL_CHECKS_20261024.json). No collision hypothesis or positivity property was added.

Both the desktop compiler and the local PDF build succeed. The final reading copy has 16 pages, no unresolved references, no compilation warnings and no overfull or underfull boxes. All pages were visually inspected at 95 dpi, including the complex theorem, potential selection, localization formulas and bibliography. An almost-empty acknowledgement page was removed by tightening prose. [Build receipt](../manuscript/BOOK_COMPLEX_POTENTIAL_BUILD_RECORD_20261024.json) records source/PDF hashes and the preceding version.

**Disposition:** the requested presentation revision is complete. Mathematical claims, finite-mass restrictions and open theta estimates retain their earlier scope. No new manuscript snapshot or Git commit was created.
