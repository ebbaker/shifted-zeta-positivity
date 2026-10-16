# Local heat-flow geometry at a collision, and why the observation criteria are RH-equivalent

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

For a real analytic backward-heat field \(H_t=-H_{xx}\) with an exact
spatial zero of order \(m=2r+j\) at \((T,a)\):

- **Local structure (22 §2).** The even-order stationary predecessor
  \(\chi(s)\) with \(W(T-s,\chi(s))=\tfrac A{r!}s^r+O(s^{r+1})\); the
  physical stationary pole \(\mathcal L_j/E=-r/s+O(1)\); the complete
  local backward stationary locus is one analytic curve; the scalar factor
  \(E=W^2Q(s)\).
- **Exclusion theorems and sharpness (22 §7).** Signed stationary
  exclusion; the fixed-endpoint chord law \(\mathcal C_j/\sqrt E\to-d_\delta<0\);
  starting-energy exclusion with \(o(\sqrt E)\) loss and sharpness of the
  exponent \(1/2\); the exponential average with its endpoint-only cutoff
  error \(\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E\); quarter-turn concentration
  and the scaled profiles.
- **Spacetime index and winding (22, Note 01/04).** The real index of
  \((H,H_x)\) at an \(m\)-fold collision is \(-\lfloor m/2\rfloor\), so zero
  boundary winding on a compact spacetime region excludes every interior
  collision; the four-dimensional local degree of the holomorphic pair is
  \(\binom m2\), so a tube certificate is never more permissive than the
  rectangle one (Reply 18, Proposition 5.1, checked exactly for \(m\le9\)).
- **The observation criteria are RH-equivalent (Review 16, Prop. 1;
  Reply 18 §1).** Under RH every slice is Laguerre–Pólya with simple zeros,
  so each criterion holds with zero loss; combined with the exclusion
  theorems, every loss-type criterion on \((0,\tfrac12]\) is equivalent to
  RH, and on \([t_0,\tfrac12]\) to \(\Lambda\le t_0\) (the strict pointwise
  sign needs \(\Lambda<t_0\)). A prescribed trace certificate is
  RH-equivalent when its scalar coefficient is locally bounded on both
  sides (Reply 18, Prop. 2.1).
- **The classification rule.** A proposal that implies RH and is implied
  by it is a reformulation, to be stated once; one that does not imply RH is
  a milestone, judged by its number (\(\Lambda\le t_0\), an effective
  height, a certified box, a certification cost).

## Status

All proved; exact replays pass on polynomial germs (22's checkers); the
Laguerre–Pólya argument is classical. Hand-verified in the cross-model
review and partly corrected in the second round (endpoint table).

## Caveats

These are statements about general backward-heat fields and carry no
information about theta; every identity here is shared by the controls of
[12](12_collision_controls_and_screening.md). The geometric apparatus
(self-dual forms, jet surfaces, hyperkähler lifts, theta bundle with ASD
connection; 21's Fueter and octonionic lifts) is correct and sign-blind by
the manuscripts' own sections.

## Reusable for

The exact local model of a collision for any certificate; the winding
certificate language (and its cost accounting against the published
proofs, Review 19 §2); the classification rule as the first test on any
new criterion.

## Where

- 22 manuscript: [`theta_manifold_geometry.tex`](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex) (§2 predecessor, pole, locus; §7 chord laws; §11 trace proposition and cone transfer); [spacetime index note](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md); [Jensen surfaces](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md).
- 21: [criteria baseline](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md); [Cauchy–Fueter boundary note](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md) (eq. (15), the real Jacobian of the lift).
- Reviews: [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §4; [Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md); [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md) §§1, 2, 5 with its [check programme](../papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_heat_germ_degrees_claude_20261015.py); [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md).
- Earlier statement of the same facts: [external review of project 17](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) (transport certificate \(\equiv\) first-jet test; S0/S1 are Laguerre's inequality); [17's index lemma](../papers/investigations-2/inactive/17_spacetime_collision_degree/notes/INITIAL_RESEARCH_PROGRAM_20261013.md).
