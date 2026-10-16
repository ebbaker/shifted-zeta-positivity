# Internal review: prescribed heat-weight covariance

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex); configured reasoning effort: ultra, verified
from the parent chat's local turn context. This is an internal LLM review,
not independent mathematical validation.

The reviewed result is [Note 4](../notes/4_PRESCRIBED_HEAT_WEIGHT_COVARIANCE_AND_SIGNED_HIERARCHY_20261010.md).
Its new arithmetic information is the exact quadratic coefficient shape;
it yields a Gaussian coefficient decomposition, a complete signed
covariance, and a shifted signed-moment hierarchy. The bounded result is
a scoped failure of the explicit absolute covariance envelope to provide
a vanishing error or a free opposite threshold sign.

The centering formula is exact:
`b_n exp(t rho_n^2/4)=exp(-sigma log n+t log^2 n/4)`.
Gaussian completion of the square gives both its mean and the pair
covariance multiplier `exp(t rho_n rho_m/2)-1`. Finite `N` justifies all
Gaussian integrations and exchange with the sum. Expanding that multiplier
gives an absolutely convergent rank-one matrix series. Its contraction
with the indefinite dual is the exact signed hierarchy in equation (12).
The leading shifted coordinates are `X_1,Y_2+epsilon X_2`; setting them
to zero would impose new candidate conditions. Matrix covariance
positivity does not give a sign for its contraction with the dual.

The covariance multiplies the complete existing four-channel pair kernel.
The difference sine sign is `(C_mn-C_nm)/2`, the product sine sign is
`(C_nm+C_mn)/2`. The new factor is symmetric in `n,m`, so antisymmetric
difference sine coefficients still combine with their antisymmetric sine
phase. Ratio/product regrouping retains the multiplier inside each inner
coefficient sum. The ordered diagonal, product squares and every mixed
block/core contribution stay present. The checker verifies complete
recombination on one common rational phase generator, rather than with
independently chosen phases.

The asymptotic proposition concerns the positive envelope (15). Its upper
bound keeps the full natural cutoff and combines the two heat weights
with the covariance exponential. The pair log-density exponent is bounded
by `-(1/2-kappa/4-o(1))(y+z)`, retaining a uniform `1/8` reserve on the
stated kappa interval. Integer log bins pay the low-index endpoint
without discarding it. The lower bound uses a fixed macroscopic subblock
of at least constant times `N` indices, each of weight at least constant
times `w_N`. The feature norm bound is independent of both carrier and
individual phases. This proves `E_t asymp t(Nw_N)^2`, not a lower bound
for the signed contraction or its individual channels.

For all dual parameters `||mathbb Q||_op>=2` by its fixed `Y_3`
diagonal. Thus the selected norm/triangle covariance payment is always
at least constant times `t exp(2a/t)`; uniformly bounded dual matrices
make it exactly that order. This does not rule out a larger negative
margin, a different covariance estimate, or a theorem that uses the
prescribed weights without this mixture. The statement is a loss
calculation for the specified absolute-payment mechanism.

Physical raw jets remain those of the complete moving weights/carrier.
Freezing each auxiliary reweighting at the center preserves the raw Bell
multipliers if a local tilted control is differentiated. The finite sum
is not assigned an independent scalar heat equation. The exact
normalizer `gamma`, both lower-jet tolerances, raw residuals `E_2,E_3,E_4`,
and Cauchy payments `j! L^j eta_N` remain in the sufficient criterion.
Heat Note 18's correlated candidate domain can improve the actual dual
payment, but does not constrain the auxiliary tilt's shifted moments.

The [checker](../numerics/check_prescribed_heat_covariance.py) passes
**327 exact assertions**, including 203 ordered-pair identities. It uses
standard-library Fraction arithmetic and formal series through degree
12 in `sqrt(t/2)`, retaining the prescribed coefficient heat shape.
The [record](../numerics/prescribed_heat_covariance_record_20261010.json)
binds the final source hash. Two fresh replays, including one with
`--output` directed to a temporary record, match byte for byte.
The exact Gaussian and hierarchy formulas are proved for all finite
orders in the note; the checker verifies their finite series instances.
The uniform asymptotic proof is analytic, not inferred from the finite
models. No actual huge-height covariance sign is certified.

The remaining research input is an upper bound for the unconditioned
tilted average and a signed lower bound for the complete covariance,
or an equivalent prescribed-coefficient estimate directly on the
original four pair channels, beating both actual candidate and raw-jet
payments. No collision exclusion, new Newman bound, RH conclusion,
higher-multiplicity coverage, endpoint theorem, or priority claim follows.
Sources and records remain small under the repository storage rule.
