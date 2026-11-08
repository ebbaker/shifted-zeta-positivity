# B05 r4: a threshold lower bound without tracking a pair

6 November 2026 America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead tool-selected configuration: **gpt-6-astra, ultra**, not independently verified backend identity. The root coordinator independently identified this direct consumer of the completed E12 estimate. Assessment of this short corollary is assigned to the forthcoming assembled E13 review.

**Decision and quantitative result, derived in-note:** use the whole local moment at the all-real threshold, rather than continue or relabel the initial pair. If H0 has a conjugate pair X±id with X>=10 and 0<d<1, then

    Lambda >= 2d² / [344 A² ||chi||_(2) log²(2+X)],                 (1)

for any fixed nonnegative chi in C_c²([-1,1]), chi<=1, chi(0)=1. Here A is exactly the common absolute canonical unit-count/safe-line constant of Note18, and ||chi||_(2)=||chi||∞+||chi'||∞+||chi''||∞. A has not been numerically evaluated, so (1) is not advertised as a numerically explicit bound. No source margin, simplicity, isolated tube, maximal root or persistent labeling is required.

## Proof and the threshold endpoint

The canonical all-real set is [Lambda,infinity). De Bruijn's strip theorem applied to the time-zero critical strip gives Lambda<=1/2. If H0 has a nonreal zero, its nonreal neighborhood retains the same positive zero count for sufficiently small real lambda by local uniform convergence and Rouché's theorem. Thus Lambda>0. This argument does not need to import the Rodgers–Tao lower-bound theorem.

All zeros at lambda=Lambda are real: if a nonreal zero were present there, the same local persistence would give nonreal zeros for some lambda>Lambda, contradicting the all-real property above the threshold. Consequently Q_{X,1}(Lambda)=0, whereas the two initial copies give Q_{X,1}(0)>=2d². E12's proved full-time Lipschitz estimate (1), applied between 0 and Lambda in [0,1/2], gives

    2d² <= |Q_{X,1}(0)−Q_{X,1}(Lambda)|
          <=344 A²||chi||_(2) log²(2+X) Lambda.

This proves (1). The moment counts whichever zeros occupy the fixed window at each time; it does not claim that the initial pair remains there or reaches a particular collision. Multiplicities and all intervening collisions are covered by E12. For a zeta zero beta+i gamma, X=2gamma and d=2|beta−1/2|, so the corresponding numerator in (1) is 8|beta−1/2|².

## Scope and comparison

This is a conditional-on-an-off-line-zero **lower** bound for the global Newman threshold, equivalently an upper bound on transverse displacement in terms of Lambda and height. It is not an RH proof, a positive-time realness improvement, or a height-shrinking upper envelope for collision times. It remains compatible with Lambda=0 implying RH, and is not presented as independent evidence for Lambda=0.

The [recent-preprint receipt12](../references/12_TND_O_RECENT_COLLISION_PREPRINT_TRIAGE_20261107.md) records a related unreviewed claim with log(gamma)loglog(gamma) rather than log²(gamma) in the denominator and a stated numerical constant. That claim is stronger in its advertised height dependence; its theorem and numerical premise have not been validated or imported here. The present result uses the checked Polymath coarse constants and the assessed-to-date local calculus, with the E10/E12 assembly still awaiting E13. No priority or specialist-independence claim is made.

The used premises are genuinely canonical strip, count and safe-line estimates and the existence/closure of the canonical all-real threshold. A generic control with corresponding estimates and a threshold satisfies the same implication; positivity of a source alone is not a premise that yields (1). This is a quantitative consumer, not a new all-window vanishing criterion. [Result index](../../../../../result-summaries/README.md), [controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns](../../../../../avoid/README.md), [classification](../../../../../avoid/01_restating_the_target.md) and [scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) remain in force.

The precise sources are [E10 Note18](18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md), [E12 Note19](19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md), and the pinned Polymath2019 threshold/strip inputs already recorded there. The proof is finite and analytic; no numerical work, further source truncation or new worker is required. E13 is to check this exact corollary with the assembled package.
