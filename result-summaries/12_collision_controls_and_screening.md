# Collision controls and the screening they impose

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

The controls are the most distinctive product of the second portfolio:
explicit sources that share named properties with the theta source and
nevertheless collide at positive heat time, so that any argument using
only those properties proves a false statement.

- **Euler-factor controls (Investigation 19).**
  \(\Phi_{c,p}=\Phi+\tfrac c2[\Phi(\cdot+a)+\Phi(\cdot-a)]\), \(a=\tfrac12\log p\).
  It is positive and even; \(H^{c,p}_0=H_0(1+c\cos ax)\) has, for
  \(0<c<1\), the same real zeros as \(H_0\); its Dirichlet series
  \(\zeta(s)(1+(2\sqrt p/c)p^{-s}+p^{1-2s})\) lies in the extended Selberg
  class with conductor \(p^2\), tempered iff \(c\ge1\); for \(c\ge1\),
  \(\Lambda_{c,p}\le0\iff\)RH, and for \(0<c<1\), \(0<\Lambda_{c,p}\le\max(1,\delta)^2/2\).
  Exact flow: \(H^{c,p}_t(z)=H_t(z)+\tfrac c2e^{ta^2}[e^{-iaz}H_t(z+2ita)+e^{iaz}H_t(z-2ita)]\).
  Witness: one real \(x_0\) with \(\mathcal L_0(H^{c,p}_t;x_0)<0\) proves
  \(\Lambda_{c,p}>t\). Certified: \(\Lambda_{1/2,p}>0.2\) for every prime
  \(p\le41\), \(>0.1787854\) for \(p\in\{43,47\}\), by two programs sharing
  no code. Asymptotic: \(\Lambda_{c,p}>t_m-S_2t_m^2-Q a^{-6}\) with explicit
  \(Q\), \(t_m=4\log(1/c)/(\log p)^2\). Screening corollary: a property
  list satisfied by some \(\Phi_{1/2,p}\), \(p\le41\), cannot imply
  \(\Lambda\le0.2\). Shared properties S1–S5 and unshared D1–D3 are listed
  in the manuscript; the controls fail direct evaluation already at height
  \(\pi/a\le9.1\).
- **Weighted-square controls (Investigation 22).** Three positive weights
  on the first three square nodes give a source positive on the half-line,
  satisfying every support-only moment and localizing inequality and the
  first reflection endpoint \(\Phi'(0)=0\), with a nondegenerate collision at
  \(T=1/4\), \(x_*\in(44.1303,44.1304)\); a four-square control at
  \(T=1/100\), \(x_*\approx83.5324\), matches two reflection endpoints and
  three primitive endpoints. Both validated with Arb and reproduced
  independently with mpmath.
- **Reflected super-Gaussian control.** \(\Phi_*=c\,e^{-u^2/4}g(u)\) with
  \(g\) built from \(e^{-u^4}\): strictly positive, even, entire, all odd
  primitive endpoints \(-\tfrac12\), every Fourier–Gram form positive, and
  an exact collision \(H_*(1/4,\pi/4)=H_{*,x}=0\) with \(H_{*,xx}>0\).
- **Reflection rigidity.** Within polynomially weighted integer-square
  combs, full source reflection plus the normalized endpoint forces
  \(a_n\equiv1\): the conjunction of square support and reflection is the
  theta source itself.
- **The per-control table.** No single listed property is absent from all
  four controls; \(\{A,B\}\) have square support without reflection,
  \(\{C,D\}\) reflection without integer-square support. Any certificate
  must reject all four; the premises on record that do are the complete
  source (conductor one, equivalently level-one modularity) and direct
  quantitative information about \(\xi\) (19's D2, D3).

## Status

19: proved and certified; the manuscript "awaits independent review" and
its tracked \(T_0\) table is not a bound (\(\Lambda\le T_0\) is explicitly
not proved). 22: validated (python-flint), hand-verified and reproduced.
Rigidity: proved.

## Caveats

The screening is a statement about tested premises, not an impossibility
theorem (Response 17, accepted in Reply 18). 19's manuscript in the tree at
commit `58871b3` still contains merge-conflict markers from commit
`bd8d0a9` and does not compile until they are resolved.

## Reusable for

The standing falsification screen for every proposal: run it on
\(\Phi_{c,p}\) for all \(p\), on the weighted-square and reflected controls,
and name the premise each fails. A template for raw-margin witness
certificates.

## Where

- 19: [manuscript](../papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex) (thm:structure, thm:flow, prop:witness, thm:certified, thm:asymptotic, cor:screen, §"What upper-bound proofs must use"); [certified witness](../papers/investigations-2/active/19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md); [initial program](../papers/investigations-2/active/19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md); [verification review](../papers/investigations-2/active/19_euler_factor_controls/reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md); [README](../papers/investigations-2/active/19_euler_factor_controls/README.md).
- 22 controls: [three-square control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md), [reflection rigidity](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md), [four-square control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md), [reflected control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md); [manuscript §9](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex); [independent recomputation](../papers/investigations-2/active/22_theta_manifold_geometry/numerics/recompute_controls_claude_20261015.py).
- The table and its scope: [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md) §3; [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §6 (superseded wording); [Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md).
- Earlier counter-kernels: [11](11_newman_heat_flow_reductions_and_certificates.md).
