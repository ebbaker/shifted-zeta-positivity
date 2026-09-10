# Review of *Cumulative storage and residual-controlled depth extension for shifted-zeta transfer operators*, research draft v0.2 (10 September 2026)

Reviewer: Claude (Fable 5.1, Cowork session), 10 September 2026.
Object reviewed: `papers/storage-depth/` at repository commit `dffb5e2` (branch `critical_path`, working tree clean): `manuscript/storage_depth.tex` and `spatial_recursion.tex` (read in full), `README.md`, `STATUS.md`, `ARCHIVES.md`, `CLAIMS.json`, `BUILD_RECORD.json`, `SHA256SUMS.txt`, all of `numerics/recursion/*.py`, `numerics/metric_comparison.py`, every small record under `numerics/records/`, the inherited `central_residual.py`, `relative_closure.py`, `reference_certify_arb.py` (the analytic routines actually called), and the four external matrix archives in `shifted-zeta-positivity-archive/storage-depth/numerics-archives/` (SHA-256 sums verified; the second-step and first-step spatial archives were loaded and used). Not reviewed line by line: the four background packets under `archive/background/`, the remaining v0.1 history scripts, and the inherited Weil-depth v0.3 lemmas, which I take as reviewed in that paper's own cycle. The author's normalization audit remains pending and everything below is inside the working normalization, as the manuscript itself insists.

Companion files: `numerics/RESULTS.md` in this folder logs every number quoted here, and the scripts that produced them are alongside it. A separate note, `NOTE_improvements_and_next_steps_20260910.md`, develops the constructive side.

## 0. Summary

The manuscript does what it says at the level of its analytic reductions and its recorded arithmetic. I rederived by hand the residual identity, the Cayley congruence and the coupling identity, the graph-scaled Schur test with its two-Gram leakage decomposition, the disjoint-window arithmetic cross bound, the old-energy comparison, the multi-interval comparison matrix, and the conditional continuation theorem; all are correct as stated. I recomputed the analytic constants independently with mpmath (the gamma tail floors, the new-slab floor `f_0`, the smooth cross bound, `beta`, `beta_theta`, `C_{L_q}`, the slab exponent's Gamma-function inequality) and they agree with the manuscript to between ten and seventeen digits where I used the same bounds, and to four digits for `beta` and `beta_theta`, where I used a cruder derivative bound of my own. Most importantly, I wrote an independent loader and validator for the stored 6144-bit ball matrices and replayed every recorded sign test at the first and second step: every outcome, failing pivot index, failing pivot value and minimum-pivot diagnostic in the records is reproduced, to eleven or more digits where a value is printed. So the validators, not only the matrices, have now been checked by a second implementation, which the manuscript correctly says had not happened.

Three findings go beyond confirmation and materially change what the paper should claim.

First, the certified floors are understated by four orders of magnitude. The absolute Schur test on the stored first-step matrices passes with an inserted floor of `2e-29` (it fails at `3e-29`), not merely the `1e-33` the paper reports; the compressed lowest eigenvalue of the 288-mode head is `3.28e-29`, so the certificate is essentially sharp. The spatial floor is therefore two hundred times *stronger* than the global `1.98` certificate R6 (`1e-31`), reversing the manuscript's assessment, and the shift interval at `L_q` widens from `5e-18` to about `7e-16`.

Second, the scalar bookkeeping of the conditional induction, which carries the floor through the comparison `H_J >= mu A`, loses about six orders of magnitude per quarter-step relative to the truth (`mu` is about `1e-7` while the lowest eigenvalue actually shrinks by a factor of about twenty per step). It is unnecessary: the relative test with an inserted floor `m` certifies `M_theta >= m`, and a one-line convex-combination argument then gives `Q_{0,L_q} >= m / tau^2` with no `(1 - sqrt(theta))` and no `mu` at all. On the first-step matrices this passes at `m = 2e-29`.

Third, the second-step failures are entirely an artifact of the three-interval complement floor. Replacing the certified floor `0.4109` (absolute) or `0.2931` (`theta = 0.9`) by an oracle value, with every matrix and error term unchanged, both tests pass once the floor reaches about `0.55`; the stored matrices even support a floor of `1e-30` at `L_2`. Raising the two short slabs to 64–96 Legendre modes is projected to supply that floor. The same projection shows that the appended-slab recursion degrades: the analytic floor decreases roughly linearly in the number of slabs and becomes negative after about five 32-mode slabs.

Recommendation: a major revision that is mostly re-running and restating rather than new mathematics, together with a reorganization that matches title and abstract to what is actually proved. Details follow, then itemized recommendations in Section 8.

## 1. What is claimed, and the logical shape of the argument

In the working v0.3 normalization the paper studies the central form `Q_{0,L}` on `L^2(0,L)` and its spatial split at `a = log 7` with a new slab of length `h = log(8/7)/4`. The key device is a bounded continuation `J` from the old to the new space; the graph congruence turns `Q` into `[[H_J, R*],[R, F]]` with `H_J = A + B*J + J*B + J*FJ` and `R = B + FJ`, and the residual identity `S = A - B*F^{-1}B = H_J - R*F^{-1}R` converts control of the Schur complement into a relative bound `R*F^{-1}R <= theta H_J`. The infinite-dimensional complements of the 256-plus-32 verification space are handled by an analytic floor (gamma tail floors, Carleman cross bound, a certified continuum arithmetic norm) and a full-output leakage Gram, exactly as in Weil-depth, but now also for the graph-scaled form `M_theta`. Records R7, R8 and R10 give, at the first quarter-step, a floor `1e-33`, the factor `theta = 0.9`, and the comparison `H_J >= 1e-7 A`. At the second quarter-step (three intervals, 256+32+32) only the comparison `H_{J_2} >= 1e-8 A_2` is certified; the absolute and residual sufficient tests fail. A conditional theorem states which per-step inequalities would yield divergent depth with vanishing shift.

The dependency map in Appendix B is accurate. In particular R8 does not use R7 or R6, and neither spatial result uses the global method. I checked this against the code paths (`relative_closure.py` reads only the spatial archive and the rational continuation).

## 2. Accuracy of the analytic content

**Framework (Section 2).** The definitions match v0.3. The assertion that a spatial split gives the direct sum of the two local form domains with a bounded cross block is supported by a one-sentence sketch. The cross block is bounded (the singular kernel `-1/(2|x-y|)` across the join is a Hilbert-type kernel of norm at most `pi/2`, which the paper uses), and multiplication by an interval indicator is bounded on `H^s` for `|s| < 1/2`, so the claim is right; but a working draft that will be reviewed by others should either write out the closure argument or cite where it is done. The hypothesis on `J` (bounded into the operator domain of `F`, with `FJ` bounded) is satisfied by finite-rank polynomial continuations because `F` applied to a polynomial on the slab is a polynomial plus endpoint logarithms, which is in `L^2`.

**Generator geometry (Section 3).** The hyperbolic identity, the norm criterion and the `cos(2 omega kappa_L)` bound are correct; the Taylor-majorant step needs the coefficients of `tanh` and `sech` to be dominated in absolute value by those of `tan` and `sec`, which holds because `tanh(x) = -i tan(ix)` and `sech(x) = sec(ix)`. The local extension estimate and the remark that it can force `h` of order `exp(-const/m_L)` are correct and, in my view, the clearest statement in the paper of why a naive induction is hopeless. The finite-input diagnostics (the `2.1554e13` cancellation, the coupling lower bound `1 - 1.84e-17`) are labelled as diagnostics, which is right.

**Proposition 5.1 (uniform short-slab storage).** The reduction to `log z(omega)/omega` is correct. The Gamma-function step deserves one comment: the displayed constant `pi^2/4 - 2` is not what `log(1+t) <= t` gives (that gives only `gamma`); it is a valid but unexplained constant. I checked numerically that `-log Gamma(1+omega)/omega <= gamma - (pi^2/4 - 2) omega` on `(0, 1/2]` (the defect is at most `-3.5e-4`, and the sharp slope at zero is `-zeta(2)/2 = -0.822`), so the statement is true; the proof should say where the constant comes from. The near-coincidence `pi^2/4 - 2 = 0.46740` versus `-G_1 h_max = 0.46736` is presumably accidental but worth a footnote so a reader does not suspect a typo.

**Cayley storage (Section 4).** I verified the identity `D = (omega/2)(I+V*)P(I+V)`, the three block formulas, and the unitarity of `U` and `W`; the proof of `||F_omega^{-1/2} B_omega A_omega^{-1/2}|| = c_D` is complete and does not need commuting factors, as claimed. The formal expansion of `a_cum,omega` is stated on a core and the paper is careful not to claim operator convergence; I did not verify the coefficient `a_0''/6 - a_0^3/12` and it plays no role in any result. This whole section, together with the finite depth-shift step (4.1), is not used by Theorem 1.1 or by any certificate; see Section 5 below.

**Residual and continuation (Section 6).** Lemma 6.1 is correct (I expanded it). The new-slab floor `f_0 > 1.73617237627376657` follows from the ground-state identity with `G_0 > 0` on `[0,h]`; I recomputed the displayed lower bound to seventeen digits. The all-new residual result R5 with `theta = 0.004` on 128 old modes is correctly described as covering only those modes.

**Complements (Section 7).** The joint arithmetic bound via a positive weight, `Tw <= rho w` giving `||T|| <= rho`, is the standard Schur test and the partition verifier covers the 2,152 intervals; I did not re-run it but I did confirm that the recorded weights and `rho = 1.9492` are consistent with the constant function's Rayleigh quotient `1.70` as a lower bound. The tail floors `g_{a,256}`, `g_{h,32}`, `b_sm`, `beta` recompute correctly. The corrected variation hypothesis on `K_ell` in Section 10 is right: for causal convolution `S_{w_0} = (w_0(0) I + S_{w_0'}) I_1`, the primitive estimate needs `|w_0(0)| + ||w_0'||_{L^1}`, and the historical `K_ell = sum |g_j| ell^{j-1} + remainder` bounds exactly that. Good catch, and no constant changes.

**Direct all-old residual test (Section 8).** I rederived the leakage decomposition `E_theta = D_o E_o D_o + D_n E_n D_n` from first principles (the old-tail output of `M_theta` on a head input `(f,v)` is `K_o Pi_o Q T (f, lambda v)` because `K_o J* = 0`; the new-tail output is `K_n Pi_n Q T (lambda f, v)`), the head scaling `||X_theta|| <= lambda ||X||` (the paper's factor `2 lambda` is conservative), the modified complement floor `beta_theta` with the `(lambda - 1) b_ar` correction, and the disjointness of the arithmetic source windows (the smallest gap among `log n` for `n` in `{2,3,4,5,7}` is `log 5 - log 4 = 0.223`, far above `2h = 0.067`). All correct.

**Old-energy comparison (Section 10).** Correct, including `J K_o = 0`, the exact tail compression `(1 - mu) K_o A K_o`, and the error bookkeeping. My replay reproduces the minimum-pivot diagnostic `2.4638394e-5` exactly.

**Conditional continuation (Section 11).** The theorem is correct; `tau_j` is the largest singular value of `[[1,0],[q,1]]` and the shift schedule does what is claimed. My objection is not to its truth but to its usefulness, see Finding 2.

**Partition step (Section 12).** The Hilbert–Schmidt bound for separated intervals, the choice `min(pi/2, HS)`, the `b^sm_ij` formula and the 3-by-3 comparison matrix are correct; my own evaluation of the comparison matrix gives `0.4108` against the recorded `0.41090`. The inherited-error bookkeeping `e_s`, `b_out`, `e_G`, `e_E` is conservative and valid. The exact identity `q(t) = 2 cosh(t/2) - sum_k e^{-(1/2+2k)t}` is right, and the separated-interval remainder bound follows from the geometric tail. This subsection is a proposal, correctly labelled.

I found no mathematical errors. The items that need attention are (i) the unexplained Gamma constant, (ii) the direct-sum sketch, and (iii) a dangling reference: the manuscript pins Weil-depth v0.3 to commit `a566944d...`, which no longer exists in the repository (the branch was squash-merged as `76b0d32`). The v0.3 source is preserved under `archive/drafts/v0.1_2026-09-10/reference/weil-depth-v0.3/`, so the dependency is pinned by content, but the citation and the hyperlink should point there and to the v0.4 commit, with a sentence saying that the v0.4 corrections (a local step in the proof of Lemma 3.3) change no constant used here.

## 3. Independent numerical verification

I installed python-flint 0.9.0 on the review machine, wrote a streaming loader for the gzipped JSON ball archives (the 635 MB decompressed second-step archive cannot be `json.load`ed in 3 GB of RAM), and re-implemented the validators' reductions with my own LDL. Working precision 2048 bits on the stored 6144-bit balls, as in the recorded replays.

| Test (record) | Recorded | Replayed |
|---|---|---|
| R7 absolute, `m = 1e-33` | PASS, min pivot `2.584e-5` | PASS, `2.58405266699e-5` |
| R8 relative, `theta = 0.9` | PASS, min pivot `1.051e-5`, `beta_theta 0.7616605490419337` | PASS, `1.05134657539e-5`, `0.7616605490` |
| R10 comparison, `mu = 1e-7` | PASS, min pivot `2.4638394e-5` | PASS, `2.46383943638e-5` |
| R11 absolute, `m = 1e-36` | FAIL, pivot 182, `-0.71634722381234840513` | FAIL, pivot 182, identical value |
| R11 comparison, `mu = 1e-8` | PASS, min pivot `2.2736098e-5` | PASS, `2.27360977442e-5` |
| R11 comparison, `mu = 1e-7` | FAIL, pivot 263 | FAIL, pivot 263 |

Analytic constants: `L_q`, `L_2`, `g_{a,256}`, `g_{h,32}`, `f_0`, `C_{L_q}`, `beta`, `beta_theta`, `b_ar`, the check `C_{L_q}(5e-18)^2 < 4.135e-34` and `1 - sqrt(0.9) >= 1/20` all reproduce (RESULTS.md). One presentation point: the 2048-bit and 4096-bit "replays" print identical pivot values and identical radii (for example `9.21e-37` on the failed absolute pivot), because the radii are inherited from the stored 6144-bit balls and the analytic error terms, not from the working precision. Re-evaluating stored balls at a second precision is a useful consistency check but it is not the "second precision" of the original construction; the manuscript's phrase "reproduced at 2,048 and 4,096 bits" should say so.

## 4. Findings

### 4.1 The spatial floors are understated by four orders of magnitude

Inserting larger floors into the first-step absolute test, everything else unchanged:

| `m` inserted in `(beta - m)(H - m) - E - budget` | result |
|---|---|
| `1e-33` (paper), `1e-31`, `1e-30`, `1e-29`, `2e-29` | PASS |
| `3e-29` | FAIL (pivot 263) |

The compressed lowest eigenvalue of the 288-mode head is `3.284e-29` (midpoint diagnostics), so `2e-29` is within a factor 1.6 of the best any test on this head can give. Consequences if confirmed through the repository's own code path: `Q_{0,L_q} >= 2e-29 I`; with `C_{L_q} < 16.5362`, `C_{L_q}(7e-16)^2 = 8.1e-30 < 1e-29`, so `||V_{omega,L}|| <= exp(-1e-29 omega)` for `0 < omega <= 7e-16` and all `L <= L_q`, and `D_{omega,L} >= (1 - exp(-2e-29 omega)) I`. This is two hundred times stronger than R6 at `1.98` and fourteen times wider in shift, so the sentence "the spatial floor `1e-33` is weaker numerically than R6" and the staircase discussion in Section 9 need rewriting. The Weil-depth paper already adopts the right practice ("floors are the largest three-significant-figure rationals passing the sector tests"); storage-depth should do the same, with a recorded bisection.

At the second step the analogous statement is conditional on the tail floor (4.3): with an oracle joint floor of `0.65` the stored matrices certify `Q_{0,L_2} >= 1e-30` and fail at `1e-29`; the compressed lowest eigenvalue there is `1.884e-30`.

### 4.2 The `mu` bookkeeping is lossy and unnecessary

The comparison `H_J >= mu A` is sharp at `mu = 1e-7` (the test fails at `1.2e-7`; the generalized eigenvalue `min H_J/A` on 256 modes is `1.218e-7`), and at the second step at about `6e-8` (passes `5e-8`, fails `7e-8`; generalized minimum `6.04e-8`, so the recorded `mu = 1e-8` can be raised fivefold). But `mu` measures the *worst* direction of `H_J/A`, which is not the weak direction of `A`: the compressed lowest eigenvalue falls only from `6.56e-28` (`log 7`) to `3.28e-29` (`L_q`) to `1.88e-30` (`L_2`), a factor of 17–20 per quarter-step, while the recurrence `m_{j+1} = (1 - sqrt(theta)) min(mu m_j, f_j)/tau^2` charges a factor of about `2e-9` per step. After three steps the scalar floor would be `1e-25` below the truth and the shift schedule `omega_j = sqrt(m_j/(2C_{L_j}))` correspondingly absurd.

The remedy is already inside the paper's machinery. Run the relative test with an inserted floor, `(beta_theta - m)(H_theta - m) - E_theta - budget > 0`. Passing certifies `M_theta >= m I`. Then, since

    T*QT = (1/lambda) M_theta + (1 - 1/lambda) diag(H_J, F),

and both `H_J >= m` and `F >= f_0 >= m` follow from `M_theta >= m`, one gets `T*QT >= m I` and hence `Q_{0,L_q} >= m / tau^2` directly, with no `(1 - sqrt(theta))` loss and no comparison with `A`. On the first-step matrices this passes at `theta = 0.9` for `m = 2e-29` (fails at `3e-29`), and at `theta = 0.8` for `m = 1e-29`. The conditional theorem's hypotheses can then be reduced to "at each step, `M_{theta_j} >= m_j' I` is certified and `F_j >= f_j`," with `m_{j+1} = m_j'/tau_j^2`. The old-energy comparison remains a good diagnostic of continuation quality and a clean statement (`S >= 1e-8 A`), but it should stop being the carrier of the floor.

Two smaller sharpenings on the same matrices: `theta = 0.8` passes (`0.75` fails), so `1 - sqrt(theta)` doubles to `0.1056` if one keeps the paper's formulation; and the residual identity is best stated as an operator identity followed by the convex-combination inequality above, which is shorter than the `2ab <= a^2 + b^2` route.

### 4.3 The second-step failure is the three-interval complement floor, and the recursion as designed does not scale

Replacing the certified complement floors by oracle values, with the head, the leakage Grams, the continuation and the error budgets unchanged:

| test at `L_2` | certified floor | oracle floor needed | outcome with oracle |
|---|---|---|---|
| absolute, `m = 1e-36` | `0.4109` | `0.5` FAIL, `0.55` PASS | passes up to `m = 1e-30` at `beta = 0.65` |
| residual, `theta = 0.9` | `0.2931` | `0.5` FAIL, `0.55` PASS | `theta = 0.8` also passes at `0.65` |

So the operator and the verification space are fine; the analytic floor is short by about `0.15` (absolute) and `0.26` (residual). Where does the shortfall come from? The 3-by-3 comparison matrix has diagonal `(3.71, 5.73, 5.73)` before the uniform subtraction of `rho_2 = 2.027`, two adjacent `pi/2` couplings, and the eigenvector `(1, 0.69, 0.45)`; the middle slab is coupled on both sides. Recomputing the floor with different parameters (numpy, RESULTS.md):

| verification space | joint floor | `theta = 0.9` floor |
|---|---|---|
| 256 + 32 + 32 (record) | `0.411` | `0.293` |
| 256 + 48 + 48 | `0.562` | — |
| 256 + 64 + 64 | `0.654` | `0.547` |
| 256 + 96 + 96 | `0.768` | — |
| 256 + 128 + 128 | `0.837` | `0.737` |
| 384 + 32 + 32 | `0.637` | — |
| 384 + 64 + 64 | `0.924` | — |

Sixty-four modes on both slabs should certify the absolute test and is borderline for the residual test; ninety-six is comfortable. This is STATUS.md's experiment 1, now with a target. Two things will not work: the separate-tail weight search of R12 (with the Perron weights all three floors equal the joint floor, and other weights only move floor from one interval to another; the recorded searches confirm this), and replacing the uniform `rho_2` by blockwise arithmetic norms (`rho_1` on the long interval, `b_ar` across, zero on the slabs), which the triangle inequality makes worse, giving `-0.61`.

The same computation exposes a structural problem with appending slabs. A chain of `k` 32-mode slabs behind the 256-mode head has joint floor `0.41, 0.13, -0.26, -0.74` for `k = 2, 3, 5, 9`; with 64-mode slabs `0.65, 0.45, 0.16, -0.23`; with 128-mode slabs `0.84, 0.69, 0.48, 0.19`. The analytic floor of the incremental partition decays roughly linearly with the number of slabs and becomes negative after a handful of steps, because each new slab adds an adjacent `pi/2` coupling while the long interval keeps its small diagonal `g_{a,256} - rho`. The recursion therefore cannot simply keep appending; it must either grow the slab dimension with each step or periodically merge the old intervals into one interval with a fresh global basis (the two-interval invariant, whose floor is `0.91` at the first step). The note discusses the trade-off.

### 4.4 Smaller points

The compressed lowest eigenvalue ladder `6.56e-28, 3.28e-29, 1.88e-30` at `log 7, L_q, L_2` is a useful quantity for the paper: it is the truth the floors are chasing, it fixes the shift schedule, and its per-step ratio (about 17–20 at these depths) is what the storage discussion should be measuring rather than `mu`. The 32-mode Galerkin continuation reproduces the lowest eigenvalue of the full head to four digits at both steps, which is strong evidence that the continuation is not the bottleneck anywhere.

## 5. Interest and positioning

The genuinely new idea relative to Weil-depth is the graph transformation with a Galerkin continuation and the relative residual test, and the reason it works deserves to be said explicitly: the cross output of an old input onto the new slab carries an endpoint logarithm with coefficient `[sqrt(h/a) phi(1) - (J phi)(0)]/2`, so a continuation that matches the join cancels the singularity and the leakage of the transformed operator into the new complement becomes tiny. The manuscript records this coefficient but treats it as a technicality; it is the mechanism. With the inserted-floor version of 4.2, the relative test also becomes the better way to certify floors, so the idea has more value than the paper claims for it.

By contrast, the title, abstract and Sections 4 and 5 promise a theory of cumulative storage at positive shift, but no certificate in the paper lives in the Cayley metric; every result is a zero-shift central-form statement plus the inherited perturbation bound, and Section 9 says so in one sentence ("the factor 0.9 is a central-form factor"). The two vector witnesses (negative generator, positive storage on one input at `omega = 1e-11`) and the coupling lower bound `1 - 1.84e-17` are interesting diagnostics but not results. I would move Sections 3–5 into a motivational section or an appendix, retitle the paper around the residual-controlled spatial extension, and state in the abstract that the positive-shift programme is open. The negative results at the second step are valuable and should stay, now with the diagnosis of 4.3.

The paper is honest about scope everywhere and the dependency map is exemplary. The biggest strategic gap is one it names but does not quantify: nothing bounds the verification dimension with depth. The note estimates it; the short version is that the tail floor needs `H_N` to exceed the arithmetic norm `rho_L` plus `gamma + log(pi L)`, and `rho_L` grows at least like the constant function's Rayleigh quotient, so `N` grows like `exp(rho_L)`: roughly a thousand modes at `L = 3` and tens of thousands at `L = 4`. That is the number a reader wants to see next to "no theorem bounds verification dimensions".

## 6. Presentation

The manuscript reads as a consolidated laboratory record rather than a paper: thirteen record identifiers, three tables of record paths, and a theorem in Section 1 whose floor turns out to be twenty thousand times below what the same computation supports. Suggestions: open with one table stating each certified inequality, its scope (which inputs, which normalization), its record, and its dependency; move the record inventory to the reproducibility section; put the working-normalization hypothesis inside each computer-assisted theorem statement rather than in a preamble; give the reader the compressed eigenvalue ladder next to the certified floors so the sharpness of each certificate is visible; and cut the repetition of "this is not a proof of RH", which appears in some form in nearly every section and can be said once, forcefully, in the status block.

Specific text corrections: the dangling commit `a566944d...` (Section 2 and bibliography); "reproduced at 2,048 and 4,096 bits" (Section 12 and records); the sentence comparing the spatial floor unfavourably to R6 (Section 9); the unexplained `pi^2/4 - 2`; `papers/README.md`, `MANIFEST.md`, `CHANGELOG.md`, the root `README.md` and `.zenodo.json` do not mention `storage-depth` at all although the folder is committed. The PDF (25 pages) was not checked visually here; the build record says no clipped material.

## 7. Reproducibility and repository hygiene

Strengths: dual hashes on every archive, fail-closed loaders, exact rational continuations, source hashes bound into the records, pinned dependencies, and a clear LARGE_FILES policy followed to the letter. All six external files verify.

Weaknesses. (i) There is no archive-based replay of the first-step *absolute* test with a chosen floor (the only way to change `m` there is the 21-minute rebuild in `close_complement.py`), and at the second step the floor is read from the build record, so it can only be changed by editing a copy of that record; this is why nobody noticed that `2e-29` passes. Add a `--floor` replay to `certify_step.py`-style validators and record a bisection. (ii) `json.load` of the 635 MB second-step archive needs more than 3 GB of RAM; a streaming reader (mine is 70 lines) or a compact binary encoding of the balls would let a laptop replay it. (iii) `requirements.txt` pins mpmath 1.4.1 but the review machine had 1.3.0 and everything ran; either relax the pin or say why it matters. (iv) The records store only the inserted floor and the sign; storing the largest passing floor from a bisection, and the compressed lowest eigenvalue as a diagnostic, would make each certificate's sharpness visible.

## 8. Recommendations

Must, before the draft is shown to anyone as v0.3: re-run the first-step absolute test with a bisection on the floor (expect about `2e-29`), the path corollary with the new floor (expect `omega <= 7e-16`), the relative test with an inserted floor and with `theta = 0.8`, and the second-step comparison with a bisection on `mu` (expect about `5e-8`); restate Theorem 1.1 and Sections 9–11 accordingly; replace the `mu` recurrence by the direct floor via `M_theta >= m` and the convex-combination inequality; fix the dangling commit; register the paper in the repository indices.

Should: enlarge both slabs to 64 or 96 modes and re-run the second step (this is the experiment that closes the residual premise, per 4.3); report the compressed eigenvalue ladder; state the endpoint-log cancellation as the mechanism; move the cumulative-storage material to a motivational section and retitle; add the dimension estimate to the scope discussion; add archive-based `--floor` replays and a streaming loader.

Could: derive the Gamma constant; write out the direct-sum closure; add a two-interval "re-globalized" second step for comparison with the three-interval one; state the detection question for finite-horizon positivity (see the note) so that the programme's milestones have a stated meaning.

I would be glad to run the repository's own validators with the new floors, or to draft the restated theorem, in a follow-up session.
