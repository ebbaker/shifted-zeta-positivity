# CCM and fractal Laplacians

Started: 26 September 2026.

This investigation asks whether resistance forms, fractal mass distributions, or geometry that changes with scale can realize the finite Connes–Consani–Moscovici mass–stiffness pair
\[
M_{L,N}=J^\dagger(W_+-\varepsilon I)J,\qquad K_{L,N}=W_--\varepsilon I,
\qquad Kq=\omega^2Mq.
\]
It starts from the original geometric-realization question in [CCM operator realizations](../ccm-operator-realizations/README.md), with the simple-even ground-state and nonzero boundary-value hypotheses explicit. It does not start from a reconstructed isospectral string.

The initial round constructs a compact weighted resistance tree with frequency count of order \(T\log T\), a finite inverse-frequency-square trace, and compatible finite-branch approximations. It defeats a blanket spectral-growth objection to changing-scale geometry. The tree is a control, not the CCM arithmetic realization.

The next proposed experiment has now been completed at \(L=\log13\), \(N=4,8,16\). **The tested direct logarithmic-coordinate construction fails:** the required nodal stiffness is not a positive-conductance graph trace, the nodal mass cannot come from nonnegative harmonic coordinates, and the prescribed refinement maps fail both form identities and composition. A separate sine-product identity rejects a measure interpretation of the mass in the unchanged sine field. The inverse traces and necessary spectral-interlacing tests do pass, so this does not exclude other geometric maps.

The continuation also proves an analytic obstruction: odd folding turns a crossing positive prime jump into a sign-reversing coupling. Explicit disjoint nonnegative half-interval tents have positive cross energy even after the pole and archimedean contributions are included. No scalar ground shift repairs that violation of the Markov property in these coordinates. The finite diagnostics agree at 80 and 120 digits; the analytic sign proof uses a rational bound independently of those computations.

The resistance identity
\[
\operatorname{tr}\mathcal L^{-1}=\int R(x,o)\,d\mu(x)
\]
remains a conditional quantitative target. Applying it to CCM still requires a different arithmetic map identifying **both** geometric energy and mass, with compatible refinements. Exact frequency-dependent elimination must also retain its interior spectral factor; a constant reduced mass–stiffness pencil is generally only a low-frequency approximation.

## Research record

- [Initial continuation: resistance forms and changing fractals](notes/CCM_RESISTANCE_FORMS_AND_CHANGING_FRACTALS_20260926.md).
- [Continuation: prescribed prime-jump geometry and its obstructions](notes/CCM_PRIME_JUMP_GEOMETRY_OBSTRUCTIONS_20260926.md).
- [Exact controls, arithmetic computations, and precision checks](numerics/README.md).
- [Initial critical review](reviews/RESISTANCE_REALIZATION_CRITICAL_REVIEW_20260926.md).
- [Critical review of the new construction test](reviews/PRIME_JUMP_GEOMETRY_CRITICAL_REVIEW_20260926.md).
- [Concise research/milestone index](DRAFT_HISTOR.md).

The simple-even Weil ground-state hypothesis in general, its original energy sign, an arithmetic geometric embedding, Xi identification, and a full spectral-triple realization remain unresolved. Support length \(L\), Fourier cutoff \(N\), and geometric refinement parameters remain distinct. The untouched Fourier tail remains part of the full CCM determinant.

## Next investigation

Test a different prescribed map before building another geometry: use the even integrated field \(q\mapsto J_Nq\), whose basis is proportional to \((\cos(n\theta)-1)/n\). Its mass must satisfy
\[
M_{22}-\tfrac34M_{13}-M_{12}+\tfrac14M_{11}=0.
\]
If this necessary identity fails, record that obstruction before considering a nonlocal transport or mass. A two-sheet interpretation explains the prime-only signs but does not supply the full arithmetic energy or mass. A separate useful certification task is to enclose the already observed sine-mass defect at \(N=4\); the derived monotonicity would propagate a certified negative sign to all larger cutoffs in that representation.

Incremental notes, code and small records, and reviews belong in their respective folders. Earlier dated research is preserved. The repository's [large-file policy](../../../LARGE_FILES.md) applies; no third-party PDFs or large derived matrices are stored here. Milestones should refer to Git commits or tags rather than new snapshot folders.
