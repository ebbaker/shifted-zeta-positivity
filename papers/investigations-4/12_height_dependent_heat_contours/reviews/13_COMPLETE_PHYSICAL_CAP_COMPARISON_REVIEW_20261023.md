# Independent audit of the bounded complete-cap range replay

23 October 2026. Prepared for Edward Baker with substantial LLM assistance. Reviewer: **gpt-6-astra (Codex)**, reasoning effort **ultra**. Same-model independent agent inspection; no external refereeing.

**Accepted as a bounded interval enclosure, not as a positive cap lower bound.** I inspected `hdc15_complete_cap_pilot.py` against equations (4)–(5) of Note 02 and the complete source core. I did not perform another cap experiment or change its mesh budget.

The first-jet denominator is re-acquired on the loaded exact spatial partition, rather than trusting a numeric floor from its receipt. Exact area, containment and disjoint-interior checks cover the entire rectangle. The replayed floor holds for the whole original complex-time square, hence every cap and side time cell used here. The stronger volume floor legitimately gives no joint zero in the interior and thus the exact identity \(B_\epsilon=I_0\), with \(Q_-=0\), on this finite box.

`inverse_E` constructs reciprocal endpoint bounds after clipping the lower endpoint by the independently proved positive floor. It never inverts an interval whose radius representation has accidentally reached zero. Reconstructing an outward Arb ball can enlarge that reciprocal interval, but only multiplication and squaring follow; such enlargement weakens the bound without invalidating it. Using the clamped positive enclosure in the paired identities remains valid: interval dependencies are discarded only by outward enlargement.

The paired sigma-face difference retains the exact factor \(2iY\) in the finite heat-polynomial difference. Its full-source remainder and spatial Taylor remainder are paid. The identities for \(\Delta E,\Delta L,\Delta N\) are correct. With \(n=\Im(L\overline N)\), the code evaluates
\[
 p_+-p_-=
 \frac{\Delta n\,E_-^2-n_-\Delta E(2E_-+\Delta E)}
      {2\pi^2 E_+^2E_-^2},
\]
which preserves the subtraction before separate absolute bounds.

All three side sums have the signs and physical measures in Note 02: the sigma pair, the right-minus-left spatial pair, and the upper-minus-lower spatial pair. The left cap uses forward orientation, and the final combination is \(I_{-\epsilon}-S_\epsilon\). The spatial meshes cover full faces without root disks, omitted complement pieces, or mismatched physical interfaces. Floating scores choose refinement order only; all bounds remain Arb intervals.

The recorded intervals contain zero and do not certify a positive lower bound. The report correctly says so and claims no computational advantage. Agreement of the independently enclosed direct and deformed quantities is a consistency check; it is not a substitute for the analytic geometric identity or a sharpened quadrature.


Installed artifacts: [Note 15](../notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md), [checker](../numerics/08_enclose_complete_physical_cap_20261023.py), and [receipt](../numerics/08_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.json). The parent independently checked every face sign, coupled heat-polynomial difference, delta-numerator identity, and positive denominator intersection before the installed replay.
