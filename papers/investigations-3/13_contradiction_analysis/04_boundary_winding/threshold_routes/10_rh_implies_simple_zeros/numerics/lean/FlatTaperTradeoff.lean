import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic

/-!
# The finite-dimensional core of the flat-taper tradeoff

Prepared for Edward Baker, 20 October 2026, with substantial LLM assistance.
Model: gpt-6-astra. Reasoning effort: ultra.

Scope: the implications from the stated real inner-product hypotheses only.
No integration, Mellin transform, taper approximation, zeta theorem, or
Riemann-hypothesis-to-simplicity conclusion is formalized here.
-/

set_option autoImplicit false

open scoped RealInnerProductSpace InnerProductSpace

namespace BW10

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

theorem flatTaperResidualIdentity
    (δ : ℝ) (e r v : E)
    (hδ : 0 < δ)
    (he : ‖e‖ ^ 2 = 1)
    (hr : ‖r‖ ^ 2 = δ)
    (her : ⟪e, r⟫_ℝ = 0)
    (hve : ⟪v, e⟫_ℝ = -1)
    (hvr : ⟪v, r⟫_ℝ = (1 - δ) / 2) :
    ‖v + e - ((1 - δ) / (2 * δ)) • r‖ ^ 2 =
      ‖v‖ ^ 2 - 1 - (1 - δ) ^ 2 / (4 * δ) := by
  have hev : ⟪e, v⟫_ℝ = -1 := by
    rw [real_inner_comm]
    exact hve
  have hre : ⟪r, e⟫_ℝ = 0 := by
    rw [real_inner_comm]
    exact her
  have hrv : ⟪r, v⟫_ℝ = (1 - δ) / 2 := by
    rw [real_inner_comm]
    exact hvr
  rw [← real_inner_self_eq_norm_sq]
  simp only [inner_sub_left, inner_sub_right, inner_add_left, inner_add_right,
    real_inner_smul_left, real_inner_smul_right]
  simp only [real_inner_self_eq_norm_sq, he, hr, her, hre, hve, hev, hvr, hrv]
  field_simp [ne_of_gt hδ]
  ring

theorem flatTaperNormBound
    (δ : ℝ) (e r v : E)
    (hδ : 0 < δ)
    (he : ‖e‖ ^ 2 = 1)
    (hr : ‖r‖ ^ 2 = δ)
    (her : ⟪e, r⟫_ℝ = 0)
    (hve : ⟪v, e⟫_ℝ = -1)
    (hvr : ⟪v, r⟫_ℝ = (1 - δ) / 2) :
    1 + (1 - δ) ^ 2 / (4 * δ) ≤ ‖v‖ ^ 2 := by
  have hres := flatTaperResidualIdentity δ e r v hδ he hr her hve hvr
  have hnonneg := sq_nonneg ‖v + e - ((1 - δ) / (2 * δ)) • r‖
  linarith

theorem flatTaperCostBound
    (δ : ℝ) (e r v : E)
    (hδ : 0 < δ)
    (he : ‖e‖ ^ 2 = 1)
    (hr : ‖r‖ ^ 2 = δ)
    (her : ⟪e, r⟫_ℝ = 0)
    (hve : ⟪v, e⟫_ℝ = -1)
    (hvr : ⟪v, r⟫_ℝ = (1 - δ) / 2) :
    4 + (3 * δ - 1) ^ 2 / (4 * δ) ≤ 2 * (1 + δ) + ‖v‖ ^ 2 := by
  have hbound := flatTaperNormBound δ e r v hδ he hr her hve hvr
  have hid :
      4 + (3 * δ - 1) ^ 2 / (4 * δ) =
        2 * (1 + δ) + (1 + (1 - δ) ^ 2 / (4 * δ)) := by
    field_simp [ne_of_gt hδ]
    ring
  rw [hid]
  linarith

theorem flatTaperCostFloor
    (δ : ℝ) (e r v : E)
    (hδ : 0 < δ)
    (he : ‖e‖ ^ 2 = 1)
    (hr : ‖r‖ ^ 2 = δ)
    (her : ⟪e, r⟫_ℝ = 0)
    (hve : ⟪v, e⟫_ℝ = -1)
    (hvr : ⟪v, r⟫_ℝ = (1 - δ) / 2) :
    4 ≤ 2 * (1 + δ) + ‖v‖ ^ 2 := by
  have hbound := flatTaperCostBound δ e r v hδ he hr her hve hvr
  have hterm : 0 ≤ (3 * δ - 1) ^ 2 / (4 * δ) := by positivity
  linarith

#print axioms flatTaperResidualIdentity
#print axioms flatTaperNormBound
#print axioms flatTaperCostBound
#print axioms flatTaperCostFloor

end BW10
