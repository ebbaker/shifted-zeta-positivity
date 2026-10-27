# Assessment of the aspirational simplicity bounds

26 October 2026. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. **Same-assistant checking only**, with no independent specialist review.

## Scope and outcome

The [new note](../notes/02_TARGET_BOUNDS_FOR_RH_TO_SIMPLICITY_20261026.md) answers the clarified request to work backward from RH-conditional simplicity to bounds that might be pursued in 01_heat_density_asymptotics. It keeps [Note01](../notes/01_RODGERS_TAO_REVIEW_AND_RH_SIMPLICITY_20261026.md) intact.

The canonical estimates J/P/V/E are **unproved research targets**. The note establishes their conditional implications, necessary accounting and selected transfer constants. No theta lower margin, favorable second-moment bound, regulator-uniform negative-time estimate, or subcritical canonical energy bound was acquired.

The most direct fit to the current approximation theorem is J. P supplies a density/energy application with a strict absolute threshold and an explicit finite error budget. V specifies a signed weak-potential target and its regulator/accuracy tradeoff. E records the direct integrated-energy requirement motivated by Rodgers–Tao.

## Checked calculations

| Calculation | Verification |
| --- | --- |
| First-jet scaling | On \(z=X+u/L\), derivatives divide by \(L\). A frozen positive carrier is comparable to the Book envelope on the microscopic chart. Thus the signed-crossover \(X^{-3/4}\) allowance at zero gives a joint-jet error \(CX^{-3/4}\), rather than requiring the coarser long-band logarithmic loss. |
| J margin | A model norm \(cX^{-\beta}\), \(\beta<3/4\), exceeds the error eventually. The example squared bound \(cX^{-1}\) gives the onset comparison \(X>(C/\sqrt c)^4\), in addition to the analytic onset. |
| Integral-to-margin conversion | At any target point the unit subinterval lies inside \([-2,2]\). The Lipschitz bound gives \(I(r)\ge(2/M)\log(1+M/(v+r))\); inversion yields the stated lower margin. With \(r=\varepsilon\), the strict condition uses \(2\varepsilon\) in the logarithm. |
| Poisson convolution | \(\int k_y(x-a)k_y(x-b)\,dx=2y/[\pi((a-b)^2+4y^2)]\). In particular the diagonal is \(1/(2\pi y)\), so subtracting \(n\) after multiplying by \(2\pi y\) is exact. |
| Collision threshold | A full-system adjacent descendant gap has \(g^2\le8t\). Its two ordered terms contribute at least \(2\kappa/(2+\kappa)\) when \(y^2=\kappa t\), giving \(2/3\) at \(\kappa=1\). This applies inside any higher-multiplicity cluster too. |
| Simple-pair clock control | For \(z^2-a^2-2t\), the gap squared is \(4a^2+8t\) and the Poisson excess at \(y^2=t\) is \(2t/(a^2+3t)\). A close simple pair can approach the collision threshold at an unsuitable time. |
| Regular-spacing calibration | The ordered off-diagonal sum is \(8y^2\sum_{k=1}^{n-1}(n-k)/(k^2d^2+4y^2)\), bounded by \((4\pi^2/3)n(y/d)^2\). This is a reference calculation, not an actual-theta spacing premise. |
| Finite tail | The two omitted rays give \(2n^2y^2/(3\pi^2R^3)\) before multiplication by \(2\pi y\), hence \(4n^2y^3/(3\pi R^3)\). |
| P transfer | The \(L^2\) triangle inequality gives the exact complete upper budget \(2\pi y(\|p_*\|+\epsilon_p)^2-n+T_{\rm tail}\). It retains the count and exterior unit. |
| Weak density normalization | \((4\pi)^{-1}\Delta\log(|H|^2+\eta^2)=\eta^2|H_z|^2/[\pi(|H|^2+\eta^2)^2]\) for a constant regulator. The limiting zero measure counts multiplicity. |
| Negative-time moment | Heat splitting gives imaginary displacements \(i\sqrt{2s}\lambda_i+O(s)\), and \(\sum\lambda_i^2=m(m-1)\). The weighted vertical moment therefore has coefficient \(2m(m-1)\), with first nonzero value four. |
| Log-potential error | The real gradient norm of \(\log(|w|^2+\eta^2)\) is at most \(1/\eta\). This gives \(\|\Delta\psi\|_1\delta/(4\pi\eta)\) without a denominator floor on \(H\). |
| Microscopic cutoff scale | For \(\psi=y^2\chi(L(x-X),Ly)\), \(\|\Delta\psi\|_1=L^{-2}\|\Delta(v^2\chi)\|_1\). The sufficient one-event transfer condition is \(\delta/\eta=o(sL^2)\). |
| Energy and density thresholds | Ordered raw energy has first collision coefficient \(1/4\). The bound \(\mathscr D(t,\sqrt t)\le4tE(t)\) is correct but loses threshold: P would require \(tE<1/6\); E's direct endpoint argument retains \(1/4\). |

These are analytic derivation checks, not tests offered as evidence for the unproved targets. No new zero computation or collision-control numerical replay was performed.

## Quantifiers retained

- All positive-time population estimates require complete endpoint membership, including whole multiple sites, and actual coverage of every target core.
- The polynomial cutoff \(N\) in the finite arithmetic model is distinct from the number \(n\) of zero labels.
- A high-height asymptotic result needs bounded-height coverage. An averaged \(o(n)\) exception allowance does not exclude every multiple zero.
- P2's time range is uniform down to zero at fixed \(X\). A direct finite-clock P1 theorem is an alternative, but its clock must be acquired from stated source data.
- The constant \(A_X\) in P2 may grow with height. Regular spacing alone does not give an adequate universal clock in the presence of arbitrarily close simple pairs.
- V takes the regulator limit at fixed negative time first. A joint schedule must pay its approximation accuracy, multiplicity and normalized unit coefficient.
- The V regulator is an auxiliary consumer parameter. The Book's physical regulator and fixed averaging kernel are not redefined.
- No first-jet or logarithmic-derivative nonvanishing is silently supplied by absolute field accuracy.

## Source and control review

The [source record](../notes/02_TARGET_BOUNDS_INPUTS_20261026.json) pins the inspected files. The present review reread the Book crossover and physical definitions, the retained-arithmetic theorem, the earlier BW10 second-moment and Poisson-resolution work, and the HDC simplicity-target/coefficient-transport interfaces. The elementary consumers also use the complete root law and Hermite splitting already examined in Note01. Primary Polymath v2 and Rodgers–Tao v5 HTML were reopened; this is not a new full audit of those papers.

BW10 Note06 already contains the full-window second-moment method and its one-event resolution warning; the new note credits it. The spectral threshold \(q<1/2\) and gap-free coefficient machinery are likewise inherited. No priority claim is made for the Poisson identity, moment detector or integral-to-margin inequality.

The [registered controls](../../../../../result-summaries/12_collision_controls_and_screening.md) are screened by premise. Hermite births and RH-conditional theta-close endpoint controls fail the desired strict bounds while satisfying the shared heat dynamics; their missing canonical arithmetic must be used in a successful proof. The close simple pair separately screens overly optimistic clock choices. Finite-tail controls lack the required complete all-real interval. These are scoped checks, not a universal exclusion of the research routes.

The note classifies final-strength tests honestly under [avoid/01](../../../../../avoid/01_restating_the_target.md), while carrying out the user's requested task of specifying them. Attainability is a research question. A new favorable canonical estimate or a measurable improvement in its complete transfer budget would be the next mathematical result.
