# A sharper explicit radius for the degree-one payment

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra**, effort **max**, same Investigation05 **chat0048**. This is a short refinement within B03 R5, with proof-author self-checking only and no numerical acquisition.

[Note26](26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md)(19) is valid, but its added unit denominators can unnecessarily dominate small source values. Preserve that issued proof. For the numerical radius comparison, solving its already proved quadratic payment directly gives a better specified rule, without a tuning search or unknown regional minimum.

Use the same
\[
 D=|D_0|>0,\quad L_0=2b^2+|h_1h_3|,\quad M=M_G(R;U),
 \qquad d_1(r)\ge D-L_0r-\frac{8M}{R^2}r^2.
\]
Define
\[
 r_{\rm quad}=\min\left\{\frac R2,\frac\tau2,
 \frac{D}{L_0+\sqrt{L_0^2+16MD/R^2}}\right\}.
 \tag{1}
\]
If \(M=L_0=0\), take the third entry to be \(+\infty\). Otherwise its denominator is positive. Indeed, the last entry is the positive root of
\[
 L_0r+(8M/R^2)r^2=D/2,
\]
written in a form avoiding subtraction of nearby square roots. This formula also gives \(D/(2L_0)\) when \(M=0,L_0>0\). Therefore every \(0<r\le r_{\rm quad}\) has \(d_1(r)\ge D/2>0\). It is the largest radius licensed by this particular quadratic payment and the two caps, not the largest true collision-free radius or the optimal coefficient radius.

For the theta envelopes of Note26, \(U_3,U_4>0\): the moment integrals are positive, the IBP majorant contains the positive \(2R\) term, and the phase-window exterior is positive. Thus \(D>0\) forces \((b,h_1)\ne(0,0)\) and \(M>0\). The denominator is nonzero without a jet-minimum hypothesis. The explicit zero-case convention retains the more general algebraic result.

The older radius satisfies both payments individually by D/4, so it is no larger than (1). The new rule also respects positive source rescaling: D, L0 and M scale by the same source-amplitude square, leaving (1) unchanged. Lowering M weakly increases (1), with strict improvement when the quadratic root, rather than an unchanged cap, controls the result. This makes the B-versus-C radius comparison sensitive to the actual remainder gain instead of an arbitrary unit added for denominator protection.

The [frozen R2 amendment A1](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_A1_RADIUS_RULE_20261030.md) replaces only the optional data-derived radius rule in the execution request. All fixed centers, radii, degrees, source bounds, work limits and comparison requirements stay as issued. No source evaluation or empirical benefit is claimed. [Note27](27_CONTINUATION_ADAPTIVE_RADIUS_IBP_AND_MODEL_HANDOFF_20261030.md) provides the model handoff; [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) alone owns live status.
