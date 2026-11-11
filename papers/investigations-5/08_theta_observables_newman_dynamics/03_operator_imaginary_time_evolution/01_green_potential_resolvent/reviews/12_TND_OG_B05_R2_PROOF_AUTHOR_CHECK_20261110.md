# B05 r2 proof-author and scope check

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort are absent from accessible
chat0009 metadata. **Same-assistant proof-author checking only**, with
inherited E07 premises; no independent specialist review or canonical run.

The checked source is [Note14](../notes/14_TND_OG_B05_R2_CONTOUR_CONDITIONING_AND_COST_20261110.md).
Disposition: retain its conditional design and issue the bounded E08
pilot. The canonical input and cost gates are untested. No correction to
the accepted E07/r1 claims is asserted.

| Claim | Check and exact limitation |
| --- | --- |
| Actual root census | Strict Rouché margins are required on the outer circle and every disjoint inner circle. Equality of the total counts establishes completeness. Repeating a cluster center m times gives matching data for m root labels; it does not prove a single zero of order m. |
| Reciprocal floor | On the outer boundary, all factors have distances in [A-s,A+s]. Apply maximum modulus to both U and 1/U only after completeness establishes that U has no zeros in the disk. The omitted-root polynomial explicitly defeats the inference without this premise. |
| Uniform polynomial deflation | Note12's convex-domain simplex estimate works also for complex evaluation points. The polynomial has the complete error epsilon_k; the physical source is unchanged. Exact synthetic division subtracts the interpolation value at every step, including repeated/nonroot knots. |
| Curvature | Fourier extraction of the holomorphic logarithm gives coefficient bound log(V/mu)/t^k and hence the factor 2 for k=2. A real-line floor alone is insufficient. The complex-disk floor is explicitly acquired by the proposed certificates. |
| Gamma factor | Differentiating log D0 gives -1/(2s^2)+psi'(s/2)/16. The trigamma series at Re(s/2)=1/4 gives 20, so 13/4 bounds the real curvature. The half-length/endpoint interpolation term is 13/128. |
| Source and coefficient errors | Positive-half-line cosine uses the correct normalization after reflection. For k<=7,b<=2 the omitted-source moments are bounded by the inherited e^(9u) moment. Taylor remainder uses order 65 with denominator (65-k)!, and coefficient radii carry the falling factorial (j)_k. |
| Source integration | The degree-15 midpoint rule integrates even terms through order 14; the absolute degree-16 remainder integrates to 2 h^17/17!. Interval differentiation stays on the analytic positive-half-line formula. The reflection join is not differentiated across zero. |
| Design arithmetic | S<=35970 and B_*<=4109/4 imply C<34933/320<110. There are exactly 67584 panels, with no patch-rounding omission. The root-label count 1056 includes repeated use across patches. |
| Complete error | Four local/numerical allowances are each <=1/2000; inherited tails remain charged. Note12's symmetric-radius factor two is retained. The <17/1000 number is an upper-endpoint error, not a value of J. |
| Direct comparison | D lies in |z-30|<3/2. The same literal-source polynomial procedure and source errors pay a direct winding-zero test. Patch-disk data only prove direct exclusion on their covered portion unless coverage of all D is checked. No general timing or signed-method dominance theorem is claimed. |

[Exact Record08](../numerics/08_TND_OG_B05_R2_EXACT_DESIGN_RECORD_20261110.json)
was produced by [the rational bookkeeping script](../numerics/check_b05_r2_design.py).
It checks constants and polynomial examples, and uses the actual directed
E06 endpoints for the conditional final-error comparison. It makes zero
theta evaluations and acquires zero root certificates. Algebra checks
are not evidence for the canonical floor gates.

The local controls were checked before accepting the design:
H=z(z-1/4) has positive modulus on the unit circle but H/z has a zero;
the count mismatch blocks the reciprocal-floor proof. H=z-1 fails the
strict boundary condition. H_eta=z^2+eta retains square-root root motion
even with exact regular factor one. n=0 and repeated/nonroot polynomial
knots have no division by a root gap. The full repository-family premise
screen is in Note14 section 8, following [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).

Unresolved costs include source interval-jet subdivision, polynomial
root-candidate convergence, strict small-contour margins, cancellation
in polynomial deflation, gamma evaluation, and ultimately singular
primitive rounding. Their finite caps can fail. In particular a panel
allowance is not a bound on acquisition operations or measured runtime.
The local three-patch experiment cannot certify the remaining cover or
justify a linear runtime extrapolation. Direct success would already
resolve the finite D exclusion, leaving Green as calibration/reuse.

**Next: [E] TND-OG-E08 — GPT-6.1 Sol**, [Request26](../research-progress/handoffs/26_TND_OG_E08_LITERAL_SOURCE_ACQUISITION_PILOT_REQUEST_20261110.md).
Its first stage checks this new interface before a bounded field pilot.
Its failure can complete the request. A changed source, geometry or
mathematical method requires a separately activated B05 r3; no full
integration run or investigation closure follows from this author check.
