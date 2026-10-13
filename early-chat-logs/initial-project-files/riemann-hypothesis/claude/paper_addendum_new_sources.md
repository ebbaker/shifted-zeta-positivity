# Addendum to paper handoff: review of YM_sym, Quat_Exp, RigidityThms (2026-08-17)

Reviewed the three newly uploaded manuscripts against the paper plan in `claude/paper_handoff.md`.
Decisions confirmed with the author (Teddy) in session on 2026-08-17.

## Quat_Exp.pdf — "The quaternion-regular exponential and the three dimensional Clifford-Fourier kernel" (2016, unpublished)

**Decision: fold in fully.** This closes handoff proof-obligation #4 (the "E_ℓ tags = spherical-harmonic
content" claim). Key machinery to import into paper §§6–7:

- Maps Q_ℓ = B₊^ℓ Q₀ with raising/lowering operators B± on sector spaces S_ℓ^{R,C,H}; the axial
  decomposition F(q) = Σ_{ℓ,m} Q_ℓ^m f_ℓ^m(q) gives a complete local (ℓ,m)-sector decomposition of
  Fueter-regular functions (with quaternionic spherical harmonics Y_ℓ^m(e_q) = G + jH built from
  ordinary Y_ℓ^m; Γ_q eigenvalues −ℓ / ℓ+2).
- Eq. (6.2): E_ℓ(λ,z) = 2λ^{−(2+ℓ)} Q_ℓ(e^{λz}) = i^ℓ (j_ℓ(λy) + i j_{ℓ+1}(λy)) e^{λx}, with
  ∂_{z,ℓ} E_ℓ = λ E_ℓ. This is the origin of the j_ℓ sector tags: they are the ℓ-components of the
  quaternionic exponential/plane wave. Use to make the positivity-hierarchy tags (§6) and the
  j_ℓ ↔ i_ℓ Wick rotation (§7) precise.
- Mellin/Laplace inversion on S_ℓ^C (Lemma 6.1) and full quaternionic Mellin inversion (Thm 6.2 via
  plane-wave expansion eq. 6.4/7.3, addition theorem Thm 7.1) — transform-side justification for the
  ℓ-decomposition of the EF bridge; the sinh(2z)/2z = Σ(2ℓ+1)i_ℓ(z)² identity is the Wick-rotated
  shadow of its completeness relation.
- CAVEAT for the paper: Quat_Exp is in the Fueter (CRF) setting, the paper's main line is slice
  regular. Present E_ℓ machinery on the Fueter side (Q_ℓ of Baker 2015), connect via the
  intrinsic-function dictionary already used in Theorem D.
- Cite via the Zenodo program-archive placeholder alongside Quat_Riemann (author will deposit).
- Clifford-analysis positioning: user-supplied DOI 10.1002/mma.1238 is almost certainly
  Bory Reyes & Shapiro, "Clifford analysis versus its quaternionic counterparts", MMAS 33(9)
  1089–1101 (2010) — already ref [9] of Quat_Exp. VERIFY DOI at citation pass. Also remark on the
  3D Clifford–Fourier kernel closed form (relates to Brackx–De Schepper–Sommen 2005; De Bie–Xu 2010).

## RigidityThms.pdf — "Rigidity theorems for generalized conformal symmetries" (Oct 2024, unfinished draft)

**Decision: use the idea, cite the classical classification literature directly, do NOT cite the draft.**
- Useful idea for paper §3 maximality (Theorem B options): holomorphic immersions
  CP¹×CP¹ → CP³ are classified as g = p∘⊗∘q (p ∈ PGL₄, q a pair of Möbius maps). The incidence
  quadric Q is the Segre CP¹×CP¹ ⊂ CP³, so this rigidity constrains holomorphic extensions of the
  lift off Q and strengthens fallback (ii) alongside Tconffinal Prop 3.1.
- ATTRIBUTION WARNING: the draft cites "Li–Peterson, Immersions of n-manifolds into (2n−2)-manifolds,
  Proc. AMS 97 (1986)" — a smooth-topology paper. The correct source for the *holomorphic*
  classification must be found during the citation pass (likely classical algebraic geometry:
  degree/linear-system argument on the Segre quadric).

## YM_sym.pdf — arXiv:2301.00029, "Generalized conformal maps as classical symmetries of Yang-Mills fields"

**Decision: provenance/framing only.** Introduction positioning: the author's broader program
(arXiv 2203.07952, 2301.00029) of generalized conformal maps that become holomorphic
contact-preserving maps on a twistor correspondence space; Theorem B is that phenomenon in
Euclidean signature for ℍ with the incidence quadric as correspondence space. Cite both arXiv
papers in the provenance paragraph. Its Liouville-type (1,1)-degree linearity argument matches
memo 2's style (classical; no import needed).

## Net changes to the outline

- §1 provenance paragraph: add the YM/causal-morphism arc.
- §3: maximality discussion gains the quadric-immersion rigidity citation (verified source, not draft).
- §6–7: sector tags founded on Quat_Exp machinery; gap #4 upgraded from "fence with a remark" to
  "close via cited theorem + short bridge lemma"; keep the safe remark as fallback if the bridge
  lemma resists rigor.
- References: + Bory Reyes–Shapiro 2010 (verify DOI 10.1002/mma.1238), + Brackx–De Schepper–Sommen,
  + De Bie–Xu, + arXiv 2203.07952 & 2301.00029, + Zenodo archive now includes Quat_Exp.
