# MC11-E01 r1 — separate assessment of the starting results

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), effort ultra**, MC11 chat0001, thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`.

**Disposition: accepted within the requested scope; E01 r1 complete, no correction.** The [proof/replay note][note] supplies the rederivation; the [exact record][record] and [checker][code] supply arithmetic evidence. This assesses the originating Astra/xhigh derivation with a different model, assisted by one read-only Sol/ultra proof pass. It shares the inherited acquisition and source premises. The new checker has coordinator implementation checks. This is internal LLM assessment, not independent specialist review or revalidation of the integration library.

## Frozen versions and method

All five request-r1 hashes match, with no version substitution:

| Frozen input, relative to the parent Mellin-curvature folder | SHA-256 |
| --- | --- |
| `08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md` | `96ffcc2943608870d5b8426fd217ce5ad515a05f06ff73f97c1d1295b71eec5a` |
| `10_radial_green_determinants/manuscript/sections/01_green.tex` | `0822d1d731da513ff62c6c7fa4ec8dfcd794c7212847dc2e39256efcfc015a60` |
| `10_radial_green_determinants/brainstorm/notes/02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md` | `7b1cfcf6bdc9edd3e09b8143e70491c795f8d1cf011a7acec104f8a416824a10` |
| `10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md` | `6a54482efcf3e586df878b097a450bb2584e75b5888a77c214105ec1f63ac928` |
| `10_radial_green_determinants/numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json` | `9ddc5881df258c3dbdfe611bf0c620c74cbd1292e0628d0e00dbca30a4e06e9a` |

One analytical proof pass and one exact-rational replay were used. No local correction, numerical acquisition, finite-energy sampling, E02 calculation, or source change occurred. The trusted numerical inputs are the inherited compact primitive balls and energy/spatial tail balls from the accepted acquisition. The replay reconstructs the derived coefficients and ratios from serialized dyadics rather than trusting recorded PASS strings or displayed readings. The analytical energy/spatial tail formulas are checked in the Green comparison; their saved constant enclosures are inherited.

## Claim-by-claim disposition

| Claim | Disposition | Premises and evidence |
| --- | --- | --- |
| Filter and positive source | Accepted | Positive effect \(W_s\), amplitude \(W_s^{1/2}\), unnormalized heat trace, direct differentiation of \(p_E\), and \(X\ge\pi>3/2\). |
| Hilbert orbitals and diagonal determinant | Accepted | Finite-order smoothness/decay, positive ground density, ordered exterior convention; no normalization factors are discarded. |
| Endpoint cancellation | Accepted for the used diagonal indices | Origin derivatives of \(m_\ell\) vanish through order \(2i-1\); infinity terms decay. The compensating atom vanishes for coefficient indices \(\ge1\). Canonical reflection is not needed. Arbitrary filtered blocks are outside this conclusion. |
| Whole-path coefficient boxes | Accepted, inherited integration premises | \(r_j=x_j-A_j+s y_j\in[0,T_j]\), giving \(c_j(s)-c_j^*=r_{j-1}-r_j\). Exact reconstruction verifies \((T_{j-1}+T_j)/\operatorname{lower}(c_j^*)<1/40000\), \(j=1,\ldots,5\). |
| Excited-tail coefficient allowance | Accepted | \(h_j>0\) by source positivity and \(h_j=y_{j-1}-y_j\le E_{j-1}+E_j\le T_{j-1}+T_j\); same saved payment applies. |
| Two-orbital sign for every excited level, all \(s\) | Accepted | Slope \(>40\), \(a_2/a_1\le1/1600\), and exact \(c_3/c_2>359991/233005825>1/700>1/800\). The final exchange term is strictly negative. |
| Full-half-line \(D_2(0)>0\) | Accepted | The compact reference is distinguished from \(b_j=a_j(\pi)\). Scaled floor \(\ge5069269683169/13838400000000>7/20\). |
| Strict fractional loss \(0<\mathrm{loss}<10^{-4}\) | Accepted | Exact common-path derivative integrated with all mixed terms; upper bound \(5480137/60543000000<40001/437500000<10^{-4}\). No measured loss is claimed. |
| Cofactor indexing and energy limit | Accepted for fixed order and fixed \(s\) | Unique index-one entry bottom left; cofactor \((-1)^{q-1}D_{q-1,q+1}\). Dominated-convergence moment asymptotic; no determinant inverse used. |
| Three-orbital limiting cofactor positive | Accepted | Permutation minor \(c_4^2-c_3c_5\); positive scale \((c_1^*)^8/(c_0^*)^6\) and exact lower factor \(158282480099/1600000000000000>0\), using boxes through moment five. |
| Sum/integration of level response | Accepted at fixed order | Absolute convergence of each moment sum and bounded cofactors on the compact path; determinant entries are affine. |

The replay reports 87 passed checks, zero integrand evaluations, zero new moments, and no failed/corrected attempt. Its 12,487-byte record retains exact fractions and input/code hashes. These checks verify the fixed arithmetic deductions, not the mathematical truth of imported numerical enclosures by themselves.

## Consequence and retained limits

E02 may use every accepted row above, with the same source, path, half-line and unnormalized observable. **No E01 premise blocks E02.** The signs of the finite first excited contribution, higher-level contribution and net three-orbital restoration remain unassessed. No numerical \(D_3(0)>0\) floor or fractional three-orbital effect has been acquired. The high-energy statement supplies no explicit finite cutoff and no growing-order or neighboring-shift estimate.

The [control discussion in the note][note] checks the named source premises against weighted-square, Euler-factor, reflected and positive-primitive families. It does not assert an uncomputed control-margin failure. The claims remain fixed-order directional comparisons in a known positivity range; they establish no RH conclusion or universal obstruction. Preserve the shared-premise qualification when changing models.

**Next: [E] MC11-E02 — Sol**, under the [continuation packet][handoff]. E03 stays conditional on E02 showing a specific resolvable input-width deficit; E04 reviews the finished three-orbital return before B01 interprets it. No B01 structural escalation arises from this assessment.

[note]: ../notes/01_MC11_E01_R1_PROOF_AND_RATIONAL_REPLAY_20261104.md
[record]: ../numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json
[code]: ../numerics/mc11_e01_r1_exact_replay.py
[handoff]: ../research-progress/handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md
