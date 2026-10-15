# Joint source current experiment and the next signed estimate

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. This continuation executes the experiment recommended in [handoff 09](09_MANUSCRIPT_RECURRENCE_INTEGRATION_AND_NEXT_CHAT_20261015.md). It establishes no new theta sign domain or RH conclusion.

## Outcome of the bounded experiment

The [joint coefficient and source calculation](../03_theta_bundles_and_connections/09_JOINT_SOURCE_CURRENT_AND_POLYNOMIAL_OBSTRUCTION_20261015.md) produces an explicit identity with both lower boundaries, both finite upper boundaries, and an error of order \(L^{-1/2}\). A bounded coefficient chosen from the known primitive endpoint cancels the source lower edge. The remaining coefficient lower edge tends to the original physical residual. The construction therefore gives approximation and a stopping rule, not the needed sign.

For \(p_n=e^u e^{-\pi n^2e^{4u}}\), \(r_n=\phi_n w_n\), set

\[
K_n=(p_n'w_n-p_nw_n')/8,\qquad
g_n=p_n(w_n''-w_n)/8,\qquad
J^{[L]}=-\tfrac12\sum_{k<L}T^kg.
\]

Here \(T\) is killed averaging on the positive integers. Then

\[
r_n=\Delta_nJ_n^{[L]}+\partial_uK_n+T^Lg_n.
\]

For the endpoint residual \(V_N-AH-BH_x-CS\), source integration gives

\[
V_N=AH+BH_x+CS+B_{\rm src}+B_L(G)+R_L(G),
\quad G_n=\int_0^\infty g_n(u)\,du,
\]

\[
B_{\rm src}=\frac{\mathbf1_{j=0}\sum_{n\le N}\beta_n-A/2}{8},
\qquad |R_L(G)|\le c_L\sum_n n\int_0^\infty|g_n(u)|\,du.
\]

Choosing \(A=2\mathbf1_{j=0}\sum_{n\le N}\beta_n\) removes precisely \(B_{\rm src}\). The surviving \(B_L(G)\) still tends to \(V_N-AH-BH_x-CS\). All starting fields and stationarity conditions remain complete. The source error bound is locally uniform on compact real time intervals and bounded parameter/coefficient sets; an upper bound on arbitrary real time alone is insufficient after source differentiation.

## What the obstruction now excludes

The earlier pointwise no-inverse theorem omitted source divergence. The new theorem includes it: if the coefficient current and source current each use finitely many neighboring square modes, polynomial amplitudes in \(u,e^{4u}\), and finitely many real spectral frequencies, an exact joint identity cannot reconstruct a nonzero physical mode beyond the coefficient current's lower-boundary range.

The source differential reduction leaves \(w''-w\). For \(w=e^{tu^2+i\omega u}a(u)\), with real \(t,\omega\) and nonzero polynomial \(a\), this cannot vanish. Extracting each square mode and taking the discrete first moment reduces the joint identity to this obstruction. The imaginary anchor \(t=0,\omega=\pm i\) is an explicit exception to the real-frequency class.

This stops the search for an exact solution by merely enlarging this finite polynomial ansatz. It does not exclude approximate inequalities, bilocal identities, nonlocal currents, or nonpolynomial primitives with independently controlled boundaries. An unrestricted antiderivative alone puts the original unknown in the source lower boundary.

## A more permissive signed criterion

The [signed observation quotient](../01_physical_jet_geometry/02_SIGNED_OBSERVATION_QUOTIENT_AND_COEFFICIENT_SINGULARITIES_20261015.md) supplies a positive refinement. In the complete reconstruction above, the sufficient coefficient payment can be replaced by

\[
q_0=A_+,\qquad q_1=\frac{B+\sqrt{A^2+B^2}}2.
\]

If the complete boundary satisfies

\[
\frac{W}{\sqrt E}B_\partial\le C_0\sqrt E+\varepsilon_0,
\]

then on full stationarity

\[
WV\le(q_j+C_0)E+(\varepsilon+\varepsilon_0)\sqrt E.
\]

It suffices that \(q_j,C_0\) remain locally bounded; separate boundedness of \(A,B\) is stronger than necessary. On branch one, \(q_1\le M\) is exactly

\[
B\le M,\qquad A^2\le4M(M-B).
\]

An explicit analytic matrix example has bounded signed payment despite an absolute reconstruction norm diverging through a rank drop. This is a result about the criterion, not an arithmetic construction for theta. Singular coefficients still require independent, uniform control of every remainder: the joint source norm above can diverge even when \(q_j\) stays bounded.

## Recommended next decision

Do not continue exact polynomial current inversion within the excluded class. For a proposed arithmetic identity, test its complete signed trace directly, preserving the favorable negative contribution and using \(q_j\) instead of an unnecessary absolute coefficient norm. Accept the proposal only if it supplies an independent sign or vanishing-order estimate and a uniform error bound through the candidate event. No such theta identity has yet been found.

For a concrete secondary experiment with a finite success criterion, use the positive tail-cone task already specified in [strategy 07, section 3](07_RESEARCH_PATHS_AFTER_COUPLED_PRODUCT_20261015.md): enclose the complete tail vectors \((H_n,H_{n,x})/\beta_n\), including their limit \((1/8,0)\), and test a prescribed separator on one small parameter box. Compare its cost with the existing finite certificates before building broader machinery. A successful box would be a finite-domain noncollision certificate, not the missing all-event inequality. The practical outer-bridge task in that strategy remains separate.

The order of limits remains: fix a sufficiently small spatial length, choose one sufficiently accurate cutoff/current depth, then approach the event. Both stationary branches and every positive-time finite-height event still need coverage.

## Saved research and verification

The [exact checker](../../numerics/check_joint_source_current.py) passes **3,803 overlapping rational assertions**, with an independently replayed [receipt](../../numerics/JOINT_SOURCE_CURRENT_CHECKS_20261015.json). It checks finite boundary identities, source reduction, lower-edge normalization, and signed quadratic certificates. The [review](../../reviews/10_JOINT_SOURCE_CURRENT_AND_SIGNED_QUOTIENT_REVIEW_20261015.md) separately assesses the analytic arguments. The [manifest](../../numerics/JOINT_SOURCE_CONTINUATION_CHECKS_20261015.json) binds the delivered research files and the unchanged manuscript source and PDF.

The manuscript remains the 43-page version identified by its existing build record. No new manuscript snapshot, commit, or tag was created. This conversation is registered, under the explicit local standing instruction, as **formal replay history 21**, “Continue theta manifold geometry,” thread `01a14066-e48e-7fa1-b488-deb17ea0448f`. Its [canonical archive](../../../../formal_replay_crosswalk/chat-histories/0021_2026-10-15T16-30-47Z_continue-theta-manifold-geometry.json) retains its identity on refresh; preceding history 20 is unchanged. Use the relevant investigation for other chats unless their instructions or existing registration specify otherwise.
