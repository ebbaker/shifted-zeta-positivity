# Moving collar and material energy self review

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Same-assistant review; no independent specialist assessment.

The [brainstorm note](../notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md) gives exact finite-cluster identities and a conditional collision-free radius. It does not give a new theta exclusion, an all-height gap bound, or a demonstrated advantage over the existing scalar discriminant method.

| Item | Assessment |
| --- | --- |
| Geometry | The right face is a fixed positive \(\delta_{H_{\max}}\) at each finite height cutoff; the left face may vary with height. Zero remains inside the domain before any limit. |
| Subdivision | Shared physical faces cancel exactly. Each complete cell has integer nonnegative charge when its boundary is regular. Root-tube regularity is not assumed as evidence of its own existence across a proposed event region. |
| Refined cap objective | The correct equality is \(I_0=I_{-\epsilon}-S_\epsilon+Q_-\). Event-freeness gives equality with the complete deformed representative. A lower bound transfers without event exclusion, provided the boundary is regular; endpoint events need excisions. |
| Material velocity | Differentiating \(H/H_z\) with \(H_\tau=-H_{zz}\) gives the stated velocity. Its denominator is \(H_z^2-HH_{zz}\), which can vanish away from an event. Other charts and joining complements are retained. |
| Material derivative | The same velocity gives \(D_\tau\log H_z=(H_{zz}^2-H_zH_{zzz})/(H_z^2-HH_{zz})\). At a zero it reduces to the derivative of the complete cap source. |
| Interaction coefficient | Direct finite-product derivatives and cancellation of distinct-triple terms give coefficient \(8\) on the unordered-pair inverse-square sum. The remainder is \(2\sum_{j<k}(a_k-a_j)/(z_k-z_j)+\sum_j(a_j^2-3a'_j)\). No time-independent-unit assumption is made; the heat equation supplies the time derivative. |
| Renormalization | Real positivity is kept separate from analytic continuation. The complex remainder has the displayed absolute bound only in a verified strain disk. A real all-height conditional theorem is not imported into the proposed collar. |
| Transfer from real energy to a cap | On the stated regular real-symmetric band, \(I_t=(k_\rho/\pi)\int_0^Y\Re K_{\mathscr D}(t+i\sigma)d\sigma\). The first transverse variation has zero real part at real time, so the error after its leading value is at most \(k_\rho Y^3\sup|K_{\mathscr D}''|/(6\pi)\). Connecting faces remain. |
| Two-root radius | The analytic coefficient is defined on an isolating wall and remains meaningful at a collision. The integrating-factor proof bounds an integral by \(8(e^{Kr}-1)/K\); comparison with \(|\Delta_0|\) gives \(r<K^{-1}\log(1+K|\Delta_0|/8)\). |
| Imaginary thickness | A rectangle requires \(r=\sqrt{(\delta+\epsilon)^2+Y^2}\). A real-time gap estimate alone is insufficient for the complete complex charge. |
| Sharp control | For \(H=z^2-2\tau\), the right-cap discriminant is \(8\delta\). The radius is exactly \(\delta\), so no positive left width crosses the event under the criterion. |
| Meaning of charge zero | Simple off-real roots can remain in an event-free region. Reality requires an anchor and population control. Event-freeness near zero also does not exclude an event at a later positive time. |
| Novelty and comparison | Root dynamics and inverse-square energies are classical. The two-root scalar equation is already in the repository. The radius is an elementary consequence used as a benchmark; no priority or competitive theta improvement is asserted. |

The [diagnostic script](../numerics/check_material_jet_energy_20261023.py) uses exact rational arithmetic for the local and summed identities, including nonconstant analytic units and a close-pair configuration. Its [record](../numerics/MATERIAL_JET_ENERGY_CHECKS_20261023.json) states the test counts. These checks support algebraic consistency; the proofs and their hypotheses carry the mathematical claims.

The [registered collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) satisfy the generic identities. Their missing canonical-source premises are stated in the note. On an event-containing domain the sufficient radius condition or a required isolation/wall premise must fail. This is a logical screen, not an unperformed numerical claim about those source families.

The next useful result would establish independent full-source bounds in one specified theta window and compare the physical material estimate with the coupled scalar radius at the same information accuracy. Until that is done, the present contribution is a precise formulation and finite local bound.
