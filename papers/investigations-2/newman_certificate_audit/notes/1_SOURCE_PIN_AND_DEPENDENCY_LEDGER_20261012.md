# Pinned public certificate and dependency ledger

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Fable 5.1 (`claude-fable-5-1`), Cowork session. This is an
internal LLM-assisted audit record, not independent mathematical validation
or formal verification. Every number below is either copied from the pinned
package (marked **[package]**), recomputed in this investigation (marked
**[replay]**, with the tool and its limitations named), or read from the
cited published theorem (marked **[source]**).

## 1. Source selection and pin

The portfolio README proposed the Gomila package as the first target. It was
inspected on 12 October 2026 and selected because it (a) instantiates one
published criterion directly, (b) exposes every parameter as an exact
rational, (c) ships the per-row certificates and the barrier transcript in
the repository itself, and (d) separates numerical replay from the
mathematical audit in its own review scope.

| Item | Value |
| --- | --- |
| Repository | `https://github.com/judegomila/dbn-lambda-01787854-candidate-audit` |
| Pinned revision | `a74738deb6d5e0f76887cb36901da08b68dca705` (committer date 2026-08-21T14:26:54-07:00, "Add the Aristotle-formalized complete lemma layer under lean/aristotle (#29)") |
| Claimed bound | `Λ ≤ 893927/5000000 = 0.1787854` **[package]**, self-labelled "computer-assisted unconditional proof, not yet peer reviewed" |
| Seal | `SHA256SUMS` lists 443 files; `sha256sum -c` passes for all 443 in a fresh shallow clone **[replay]** |
| Hashes of the documents read | `README.md 72a1ebf7…4fb4`, `PROOF_NOTE.md eb669afe…51bf8`, `CANDIDATE_PARAMETERS.md b3595190…0374`, `BARRIER_CERTIFICATE.md 81bea050…7eac`, `NATIVE_BINDING.md c9eb17be…daa4`, `src/lemma_sweep_p235711.c 580d0b51…0808`, `verifiers/verify_prop410_arb.c 0d40f9b8…66d8` |
| Certificates used below | `certificates/p235711_690988_690995.log.gz d9a66e79…907db`; `barrier/certificates/barrier_target_closed.log 2d010f70…05f4` (matches the hash printed in `BARRIER_CERTIFICATE.md`) |
| Published inputs **[source]** | Polymath, arXiv:1904.12438v2, Theorem 1.2 (criterion), Theorem 1.3 with bounds (20)–(24), Section 6 refined bounds for `e_C`, `e_{C,0}`, Section 8.5 Euler mollifier and the "improved triangle inequality" lemma; Platt–Trudgian, arXiv:2004.09765, RH through `T = 3000175332800` |

Full-length hashes are in the [replay record](../numerics/README.md). No
file of the package is copied into this repository; the clone was made
outside the tree and discarded. The package's `references/dbn21a-main.pdf`
(a third-party PDF) was not copied either.

The three other public claims named in the brainstorms (Gordon `< 0.158`,
Planat `0.17795…`, Raymond `< 0.149396`) were not inspected in this
session. Nothing here validates or refutes them.

## 2. The exact row

**[package]** `X = 6000000185827`, `t_0 = 129/800 = 0.16125`,
`y_0^2 = 87677/2500000 = 0.0350708` (`y_0 = 0.187272…`),
`Λ ≤ t_0 + y_0^2/2 = 893927/5000000`. The Riemann–Siegel index at the
barrier and at the start of the final-time region is `N = 690988`.

## 3. Criterion and the four hypotheses

Polymath Theorem 1.2 **[source]**: if (i) RH holds for zeta zeros with
`(1+y_0)/2 ≤ σ ≤ 1`, `0 ≤ T ≤ X/2`; (ii) `H_{t_0}` has no zeros with
`x ≥ X + √(1−y_0^2)`, `y_0 ≤ y ≤ √(1−2t_0)`; and (iii) `H_t` has no zeros
with `X ≤ x ≤ X + √(1−y_0^2)`, `√(y_0^2 + 2(t_0−t)) ≤ y ≤ √(1−2t)`,
`0 ≤ t ≤ t_0`; then `Λ ≤ t_0 + y_0^2/2`.

The package discharges (ii) in two lanes (finite windows and an analytic
tail) and (iii) by a closed rectangular barrier; (i) is the imported
Platt–Trudgian theorem. Where the effective approximation Theorem 1.3
enters, and how much of each lane's margin it consumes, is the point of
this ledger.

| Lane | Domain certified **[package]** | Lower bound mechanism | Approximation error paid | Certified margin | Error / margin |
| --- | --- | --- | --- | ---: | ---: |
| (i) verified height | `0 ≤ T ≤ X/2 = 3000000092913.5` | Platt–Trudgian, surplus `350479773/2` | none | — | — |
| (ii-finite) windows `N = 690988 … 3840000` | `x ∈ [x_*, x_{3840001})`, `y ∈ [y_0, √(1−2t_0)]`, `t = t_0` (box `[129/800, 161250001/10^9]` on later legs) | Euler-mollified **plain triangle inequality** on `f_t` (Section 8.5 form, `NATIVE_BINDING.md`), per-window frozen constants, stored floors `T_N` | `E_max = e_A+e_B+e_{C,0} ≤ 2.33494905e-7` (Arb, 256/512 bits), of which `e_{C,0} = 2.3349285e-7` | `T_min − E_max ≥ 5.5787e-7` at `N = 690988` (`T_min = 7.91366e-7`) | **0.295** |
| (ii-tail) `N ≥ 3840000` | same `y`-range, `t`-box | contraction `D < 0.999721`, `M_max < 1.608290`, normalized flow `> 1.7353e-4` | `< 1.1671604e-8` | `> 1.7352e-4` | 6.7e-5 |
| (iii) barrier | `[X, X+1] + i[0.1809, 1]`, `0 ≤ t ≤ t_0` (the curved barrier of (iii) is contained) | argument principle on 883 closed time prisms, mesh evaluation of `f_t`, derivative allowances `D_z, D_t` (Lemma 8.4 majorants) | allowance `0.00125`; actual `e_A+e_B+e_{C,0} < 3.56523011600040e-4` | minimum prism margin `≥ 0.519849894613872543` (prism 882) | 0.0024 (allowance), 0.0007 (actual) |

Notes on the table.

- **[replay]** The barrier transcript parses to 883 prisms, all `PASS`,
  14,493,508 mesh evaluations in total (38,396 on the first prism at
  `t = 0`, 64 on the last), minimum boundary modulus `1.5432` and minimum
  margin `0.51985` on prism 882. The spatial allowance is held near `0.5`
  by the mesh choice; the time allowance is `0.41–1.89`. The approximation
  allowance `0.00125` is at most `0.24 %` of any prism's margin.
- **[replay]** The finite-lane floors reproduce. A float64/numpy
  reimplementation of the stored `L_N` (plain triangle weight,
  `(1−g−Σ(|B|+g|A|)n^{−σ})/M − g C`) gives `7.913667e-7` at `N = 690988`
  (stored floor `0.000000791366`), `9.740621e-7` at `690989` (stored
  `0.000000974062`) and `1.891133e-6` at `690991` (stored `0.000001891132`),
  i.e. agreement to the six stored digits at the first row of each
  producer run. Rows that are not first in their run (e.g. `690990`,
  stored `1.570095e-6`, replay `1.622941e-6`) are *below* the exact value,
  as expected from the producer's frozen sawtooth weights, which are
  conservative by construction. The replay is not interval arithmetic and
  certifies nothing; it establishes that the lane's formulas are the ones
  stated in `NATIVE_BINDING.md` and `src/lemma_sweep_p235711.c`.
- **[replay]** The pointwise error budget at `(x_{690988}, y_0, t_0)`
  recomputed from Theorem 1.3 (20)–(23) and the Section 6 refined bound
  gives `e_{C,0} = 2.334925e-7` and, at the barrier corner
  `(X, 0.1809, t = 0)`, `3.565218e-4`; the package's directed Arb values
  (`2.3349285e-7`, `3.565226e-4`) are slightly larger because they are
  taken over a `t`-box with directed endpoints. The transcription of the
  constants (`0.02`, `0.626`, `6.66`, `1.24`, `3.58`, `6.92`, `8.52`, `12`)
  agrees with the published formulas; the package's "weld" `10.50` is the
  elementary consequence `3.58 + 6.92` of the Section 6 bound after
  `1 + u ≤ e^u` and enlarging the denominator `x − 8.52` to `x − 12`, and
  is correct as stated in `ERROR_CONSTANT_WELD.md`.

## 4. Where the corrected interface could act

The repository's corrected interface (project 17, Notes 20–22) retains the
Polymath `C` term as a holomorphic surrogate `C_N(t,X)e^{−π(z−X)/8}` and
pays `e_A + e_B + e_C` plus the explicit matching and surrogate costs,
instead of `e_A + e_B + e_{C,0}`. By the Section 6 bounds **[source]**,

```
e_C / e_{C,0} = s / (1 + s),   s = 1.24(3^y + 3^{−y})/(N − 0.125) + 6.92/(x − 12),
```

so at `N = 690988` the ratio is `3.66e-6` **[replay]** and the retained-`C`
budget at the first window would be `e_A + e_B + e_C ≈ 1.6e-12`.

That reduction is real but it can act only where (a) the lane evaluates
`f_t` **pointwise**, so that `C_t/B_t` can be evaluated at the same point
and subtracted, and (b) the approximation error is a material part of the
margin. Neither lane of this certificate satisfies both.

- The **barrier** evaluates pointwise, so the correction is applicable
  there (with the Note 20–22 derivative payments replacing the Lemma 8.4
  allowances for the correction term), but the error is `0.07 %` of the
  smallest prism margin. Replacing it by `1e-9` changes no prism, no mesh
  count and no time step. The cost of the barrier is set by `D_z, D_t` and
  the mesh/prism counts, i.e. by the finite sum itself.
- The **finite lane** is uniform in `x` over each window of length
  `4π(2N+1) ≈ 1.7·10^7`: its lower bound is the triangle inequality on the
  coefficients and never evaluates `f_t` at a point. A term `−C_t/B_t`
  can only enter such a bound through `sup_x |C_t/B_t|`, which is the very
  quantity `e_{C,0}` already pays (the Section 6 bound is sharp up to the
  factor `1 + s`). Pointwise use would require a mesh in `x` with spacing
  of order `e_C/|∂_x f_t| ≈ 10^{−13}` over `10^7` units. So the
  `e_{C,0}` payment of this lane is **not removable by the corrected
  interface**; it is a structural cost of a uniform lane.
- The **tail** lane is also uniform in `x` and its error is `6.7e-5` of
  its margin.

Even if the finite-lane payment *were* removable, the benefit is bounded by
the lane's own sensitivity: see the [benchmark note](2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md)
for the numbers (about `1.2·10^{−8}` in `Λ`).

## 5. Domain contracts: package versus repository interface

| Contract | Package | Repository interface (Notes 20–22) | Status |
| --- | --- | --- | --- |
| time range | barrier uses `t ∈ [0, t_0]`, extended to `t = 0` by a dominated-convergence limit on the compact box (`BARRIER_CERTIFICATE.md` §"Effective approximation, including t = 0") | `0 < t ≤ 1/2`; `t = 0` not covered | the package's limit argument is elementary and looks correct for the fixed-`N` finite sum and the continuous majorant; it is not needed by the finite lane (`t = t_0`) |
| cutoff | `N = 690988` constant on the whole barrier box (certified by `verify_uniform_error_01787854.c`, `N^2 < x/(4π)` throughout) and frozen per window in the finite lane | adjacent natural cutoffs matched with an explicit `O(Z/N^2)` payment | no cutoff crossing occurs in the barrier box; the finite lane's window edges are exactly where `N` increments and are handled by the window-freeze theorem, not by matching |
| heights | barrier `y ∈ [0.1809, 1]`; finite `y ∈ [y_0, √(1−2t_0)] = [0.18727, 0.82310]` | disk radius `r ≤ 1` about a real center; physical derivatives at the center | the barrier's imaginary heights up to `1` are inside the source theorem's region (`0 ≤ y ≤ 1`); the repository's disk statements would need `r = 1` to cover the box |
| `C`-term | dropped (`e_{C,0}`) in all three lanes | retained with holomorphic surrogate | see §4 |

## 6. What this ledger establishes and what remains

Established (within the stated tools): the pinned package's parameters,
the criterion it instantiates, the domain and mechanism of each lane, the
error budgets as fractions of the certified margins, the reproduction of
the first-row floors by an independent floating implementation, and the
reproduction of the pointwise error-budget numbers from the published
formulas.

Not established here: the correctness of Polymath Theorems 1.2–1.3 and of
the package's handwritten reductions (`DERIVATIVE_BOX_LEMMA.md`,
`TAIL_LEMMA.md`, the Dini `y`-transfer, the window freeze); the
proof-to-code map of the C programs; the barrier's `D_z, D_t` majorants;
the Lean material. The package's own `OPEN_REVIEW_QUESTIONS.md` lists these
as the referee's tasks, and nothing in this session changes their status.

Remaining obligations for a complete audit, in order of leverage:

1. The Dini-derivative `y`-transfer and the window-freeze lemma (they
   carry the single weakest row to the whole `(x, y)` region).
2. The Lemma 8.4 derivative majorants and the prism gate in
   `TloopSinglemat_closed_cert.c` (they carry 883 prisms to hypothesis (iii)).
3. The tail lemma's monotonicity gates for all `N ≥ 3840000`.
4. A rigorous (interval) replay of the first-row floor, e.g. a direct
   non-amortized Arb run at `N = 690988`, which the package's own
   `OPEN_REVIEW_QUESTIONS.md` Priority 7 also requests.
