# Verification records

26 October 2026. Prepared for Edward Baker with substantial LLM assistance. Actual model **gpt-6-astra**, recorded effort **max**.

[RT_R2_REPLAY_20261026.json](RT_R2_REPLAY_20261026.json) records execution of the existing [canonical two-root program](../../rodgers_tao/numerics/certify_rt03_rt04_r2.py), exact agreement apart from timing fields, and rejection of an injected wall error. The original full certificate stays in its existing home. The program's embedded original authoring configuration is distinguished from this review's configuration.

Run the new finite algebra check with standard Python from the repository root:

    python3 papers/investigations-5/02_heat_flow_rh_applications/rh_simple_zeros/numerics/check_endpoint_energy.py --output /tmp/endpoint-energy-check.json

The [saved check record](ENDPOINT_ENERGY_EXACT_CHECKS_20261026.json) contains exact rational outputs. The check uses no root approximations or external package. It verifies normalization on six rational configurations and Hermite heat polynomials of multiplicities 2–8 at three rational times. It is not a simplicity test for zeta.

See the [assessment](../reviews/01_REVIEW_AND_ENDPOINT_CALCULATION_ASSESSMENT_20261026.md) for the mathematical and execution limits.
