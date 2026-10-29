# CTF-B02 R7: same-assistant check of the cosine jet estimate

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra / actual recorded effort max**,
Investigation05 **chat0026**.

**Verdict: the displayed proof supports Note55's one-mark supporting-energy
gain.** This is checking by the same assistant that derived and wrote
[Note55][note], with inherited Note28/40 premises. It is not the separate
CTF-E08 assessment, a formal proof check or independent specialist review.
No subagents, numerical quadrature, PDE simulation or new certificate
were used. [Progress05][progress] owns status.

## Fixed analytical checks

1. **Complete source and moment ratio.** For every positive theta square
   term, x'=4x gives exactly the two logarithmic derivatives in (4).
   Multiplying the proposed curvature inequality by (x-3)^2 and setting
   y=x-6 gives 8y^3+21(y-1)^2+24. The initial-slope bound is 5/26<1/5.
   Summing q_n'<=q_n(1/5-74u) is valid; summing log-concavity statements
   would not be. The endpoint identity is
   0=3M2+integral u^3 q'; thus 74M4<=3M2+M3/5, in the required direction.
   At z=1/24, 74z-sqrt(z)/5>91/30>3, which proves M4/M2<1/24.

2. **Actual cosine and operator order.** 2F2-F1 has sign and factor
   rho u[sin(2u)-2u cos(2u)]. The integral remainder gives 8 rho u^4/3.
   The exact combination is prepared before propagation. No replacement
   by a multiplier on the evolved U was made. The R6 polynomial class
   does not inherit this sine/cosine estimate from its finite prefix.

3. **Gaussian normalization and full tail.** ||K1||2=(8pi)^(-3/4),
   K1*K1=K2, and the radial Jacobian gives precisely (11). The three
   tail intervals give I>=(1/6)M2-(10/9)M4>=13M2/108. In particular I
   is positive even after all negative tail contributions are paid.
   The upper numerator is M2/9; its ratio to 13M2/108 is 12/13.
   The comparison is between prepared norms, not raw norms.

4. **Homogeneous propagation and no extra feedback.** C=2J2-V solves
   the same L_s equation because the mark and alpha path are fixed.
   Its energy derivative retains negative diffusion and uses d<=6
   for the sufficient upper bound. ||V||2<=sqrt(E0) then gives (15).
   The weak Young coefficient is 72/169; the sharper allowance ratio
   tends algebraically to 36/169. These are different bounds, not a
   factor-of-two ambiguity.

5. **Comparison threshold and consumer.** Both the sharp Q comparison
   and the sharper triangle baseline for Theta cross at
   X/E0=169/196, with X=Q0 exp(6B). The initial norm relation and U0!=0
   give E0>196Q0/169, so Bc>0. A trajectory's reaching Bc is not assumed.
   The exterior forcing use is compared with the same whole-space
   Theta payment. It does not automatically reduce R5's compact maximum
   or improve a bound on G, alpha or B.

6. **Preserved residual and boundaries.** The proof adds no spatial
   integrations involving the source operator, and therefore deletes
   none of its full commutator. Its genuine nonzero preparation defect,
   cutoff terms, sphere cancellation and whole inner ball remain as in
   Notes31/40/47. The input-u partitions in the Gaussian test create
   no physical or auxiliary boundary.

7. **Direct comparison and controls.** Integrating sin(x)>=x-x^3/6 gives
   -Ha>=2M2-4M4/3>=35M2/18 at this mark. Thus no new collision-free region
   or independent dynamical separation is supported. For the exact
   Gaussian-polynomial control, the saved M2 and Gaussian moment formula
   give M4=123 sqrt(pi)/256 and ratio41/56, which fails the sufficient
   moment input. Positive weighted-square sources can pass that input
   at A=2; their registered high-frequency collisions are not excluded.
   The other controls retain their individual premise/domain qualifiers.

## Scope and disposition

The acceptance target recorded before testing was ||C0||2<=||J20||2
at (1/4,2); the proved coefficient12/13 is strictly stronger. The note
also proves a smaller same-B second-jet allowance after the explicit
threshold, rather than claiming a useful identity without a number.
There is no uniform-in-frequency statement or deadline control. The
source moment bound is a sufficient quantitative premise, not a unique
arithmetic characterization of theta.

**B02 R7 complete in-note; parent B02 partial. Next: [E] CTF-E08 R7 — Sol**,
assess the [fixed packet][packet]. Keep the manuscript and companion
unchanged during that bounded assessment. E03/B03 remain gated.
The [continuation][next] records model-change and chat-history instructions.

[note]: ../notes/55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_COSINE_JET_CORRELATION_ASSESSMENT_REQUEST_R7_20261029.md
[next]: ../notes/56_COSINE_JET_CORRELATION_AND_MODEL_CONTINUATION_20261029.md
