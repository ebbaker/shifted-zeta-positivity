# Adaptive depth and shift investigation

Start with [the research note](critical_path_research.md). It derives a relative generator inequality, a central-form depth recursion carrying an energy norm, and a conservative local extension bound. It identifies the missing requirement that successive allowed depth increments have divergent sum.

There is one new numerical sign result, within the v0.3 normalization: an enclosed negative generator witness at total horizon log 7 and shift 1e-11. It does not show failure of cumulative contraction. The same vector bounds the central coordinate-energy norm from below by 2.32e11.

| File | Role |
|---|---|
| `critical_path_research.md` | Definitions, analytic deductions, proofs, limits, next target |
| `generator_witness_log7.json` | Rational polynomial vector and ball sign record |
| `generator_witness_log7_replay.json` | Replay at increased precision |
| `local_extension_check.json` | Coarse constants for the analytic local extension example |
| `diagnostics_N64.json`, `diagnostics_N128.json` | Exploratory finite-input energy norms and shifted heads; not full-norm upper bounds |
| `certify_generator_witness.py` | Witness construction and replay, including the analytic profile error |
| `check_local_extension.py` | Exact/ball checks of the coarse local-extension constants |
| `explore_path.py` | Diagnostic head and generalized-eigenvalue calculations |
| `reference_certify_arb.py` | Unmodified v0.3 numerical routines used by the scripts |

The reference file is copied from `papers/weil-depth/numerics/certify_arb.py` in repository commit `a566944dc1be2899e37fce3d0e857516ced33d8f`: [source permalink](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944dc1be2899e37fce3d0e857516ced33d8f/papers/weil-depth/numerics/certify_arb.py). Its licensing is preserved in `REFERENCE_LICENSE`. No synced project source or repository manuscript was edited.

The analytic work awaits independent review and uses the author's current normalization while the normalization check proceeds separately. A passing numerical witness certifies the stated form calculation with the supplied analytic error bound; it does not audit that normalization.
