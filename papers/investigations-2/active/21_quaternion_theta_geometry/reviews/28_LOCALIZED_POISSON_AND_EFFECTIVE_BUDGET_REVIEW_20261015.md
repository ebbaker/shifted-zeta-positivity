# Localized Poisson, subpower transfer, and explicit weighted-budget review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, verified from the current conversation’s session metadata. Separate parallel derivations, a coordinating proof audit, and independent checker executions support this internal LLM review. This is not external peer review or formal proof verification.

The reviewed continuation establishes admissible localization, stronger nonintegrability obstructions, an extended conditional cutoff transfer, and explicit elementary remainder constants. It supplies no new theta signed-energy estimate, effective full sign threshold, or enlarged sign domain. No material gap remains in the scoped claims below.

## 1. Poisson modes, joint escape, and localized integration

[Note 42](../notes/05_theta_correlation_kernels/42_LOCALIZED_POISSON_MODE_OBSTRUCTIONS_20261015.md) preserves the complete source differential operator and exact heat. Its smooth window is applied after the differential operator, so no integration by parts, cutoff commutator, or boundary term has been omitted. Summing the differentiated lattice absolute values gives a bound by a constant times (e^{2|s|}+e^{18|r|}). The negative quartic window dominates this bound and every polynomial weight uniformly for a positive lower window parameter and bounded heat ceiling. This covers simultaneous escape, including diagonal tubes where one original coordinate stays bounded. The unsplit complete exterior has the stated (O(\varepsilon)) moment allowance; it has no energy factor.

The modewise expansion was derived independently using (z=e^{-4r}). The first two orders are annihilated, and the leading differentiated coefficient is ((9/4)\pi^2p^2k^2-9/8). It is nonzero for every mode. Summing over a finite centered rectangle gives the exact nonzero coefficient in (16a). Hence neither individual modes nor finite rectangular packets may be globally heat-integrated at positive time. The asymptotic is nonuniform in lattice indices, explaining its different sign from the infinite summed axis sector.

The additional diagonal expansion after the (+f) addback was checked independently in (u=s+r,v=s-r). For every modular Taylor profile, ((F_n''-F_n)(0)) has the stated nonzero common sign. Every fixed-order subtraction in that specified class leaves a nonzero exponential tube tail. The conclusion is limited to this class, not arbitrary exact resummation.

The smooth-window and expanding-box lower bounds concern **absolute sector budgets**. The final radial strip has width (1/R), giving the precise power (R^{2j+1}). The box cost at (R=(\log N)/2) exceeds every fixed polynomial in (N) at every fixed positive time. These statements do not provide lower bounds for signed sector integrals or rule out cancellation in the combined expression.

The [mode/cutoff checker](../numerics/check_poisson_mode_cutoff_obstructions.py) passes **260 exact rational assertions**, including 49 mode expansions, 49 rectangle sums, cutoff scaling, and diagonal differential symbols. A separate execution produced identical [receipt](../numerics/POISSON_MODE_CUTOFF_OBSTRUCTIONS_20261015.json) bytes. The global conclusions use the analytic proofs, not finite samples.

## 2. Larger cutoff costs and analytic collision exclusion

[Note 44](../notes/02_signed_cusp_control/44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md) conditionally transfers an all-cutoff signed bound with cost (N^p\exp\{a(\log N)^2\}) and a Gaussian tail to an (E\exp\{C[\log(2+\log_+(M/E))]^2\}) loss. The audit checked the explicit cutoff ceiling, constants (D,d,K,C), (B=0), (E=0), and (E\ge M). Local boundedness of the inverse Gaussian rate is retained. Cutoff optimization occurs only after the entire family is proved.

The full-amplitude transfer uses the full stationary condition and Young’s inequality, and preserves the imported (N\ge8) staircase range. The new gauge is subpower in (1/E), so the universal analytic predecessor pole dominates it for every finite multiplicity. The analytic curve-selection proof extends the earlier local rigidity lemma without assuming that the gauge itself is analytic. Both proofs retain the coverage requirement and do not construct the missing arithmetic coefficient.

A raw absolute norm has no (E) factor and therefore supplies none of this conditional theorem’s missing signed premise. This distinction prevents a false inference from the new integrability formula or its sector growth to collision exclusion. No finite numerical sampling is represented as validation of an all-cutoff or all-arc theorem.

## 3. Explicit weighted-remainder package

[Note 43](../notes/01_weighted_outer_remainders/43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md) was independently checked for shrinking-disc geometry at (L\ge100002), the uniform low-index sum, exact Abel payment, shifted convex dyadic sum, and isolated terminal block. The surviving exponent is (2324691/31840000000>1/14000); the improved exponent comes from elementary bookkeeping on the same five assigned pairs.

The audit reopened [Polymath Theorem 1.3, (23)–(24)](https://arxiv.org/html/1904.12438v2#S1) and checked the new numerical majorants against its complete errors. The derived bounds (e_A+e_B\le8\ell^2e^{-3\ell/4}) and (e_{C,0}\le3e^{-2\ell/5}) preserve both branches. The carrier comparison and nonzero zeta lower bound give the stated analytic replacement budget and Cauchy factor 1728; the discontinuous floor cutoff is never differentiated.

The actual exponent-pair constant (C_{\rm EP}) and any supplied theorem thresholds remain explicit unresolved inputs. The separate differentiation error between the analytic comparison and its phase vector is also still needed for a numerical full sign threshold. The note does not take an imported constant to be one, remove the five-halves majorant obstruction, or claim an effective finite bridge.

The [weighted checker](../numerics/check_explicit_weighted_budget.py) passes **50 exact rational assertions**. Independent replay produced identical final [receipt](../numerics/EXPLICIT_WEIGHTED_BUDGET_CHECKS_20261015.json) bytes. Those checks support the arithmetic, while the infinite sums, complex-disc bounds, and imported theorems retain their analytic proof obligations.

## 4. Scope and repository verification

The 260 and 50 assertions check different finite algebraic budgets. They are not a count of formal proofs or new stationary observations. No fresh stationary pilot was run because no new signed arithmetic coefficient family has passed the analytic gate. The prior height-112 finite cover, eventual threshold (61/24), and explicit theta-five outer result retain their previous scope. The manuscript source, PDF, and build record were not changed.

The [final validation receipt](../numerics/LOCALIZED_POISSON_CONTINUATION_VALIDATION_20261015.json) records final script/receipt hashes, deterministic independent replay, local links, file sizes, manuscript identity, and the live history registration. [Note 45](../notes/00_research_coordination/45_LOCALIZED_POISSON_AND_CONSTANT_PACKAGE_CONTINUATION_20261015.md) states the next admissible task.
