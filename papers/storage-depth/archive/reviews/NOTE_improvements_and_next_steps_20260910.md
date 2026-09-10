# Storage-depth v0.2: improvements to the results and a view of the next steps

Claude (Fable 5.1, Cowork session), 10 September 2026. Companion to `REVIEW_storage-depth_v0.2_claude_20260910.md`; numbers are logged in `numerics/RESULTS.md`. Everything is inside the working Weil-depth normalization, and every "passes" below was obtained with an independent diagnostic replay of the stored ball matrices, not with the repository's hash-bound validators; it should be confirmed through those before being stated in the manuscript.

## 1. Improvements available now, on the existing archives

### 1.1 Report the floors the matrices actually support

The first-step absolute Schur test passes with `m = 2e-29` inserted and fails at `3e-29`; the compressed lowest eigenvalue of the 288-mode head is `3.28e-29`, which is an upper bound on the true `lambda_min(Q_{0,L_q})`, so the certificate is within a factor 1.6 of the best possible from this verification space. The paper's `1e-33` should become `2e-29` (or the largest three-figure rational a bisection returns), and the derived statements follow with `C_{L_q} < 16.5362`:

    Q_{0,L_q} >= 2e-29 I,
    Q_{s,L} >= 1e-29 I           for 0 <= s <= 7e-16,  L <= L_q   (16.5362 * (7e-16)^2 = 8.1e-30 < 1e-29),
    ||V_{omega,L}|| <= exp(-1e-29 omega),   D_{omega,L} >= (1 - exp(-2e-29 omega)) I,   c_D(omega)^2 <= exp(-2e-29 omega).

The staircase in Section 9 then runs `(log 7, 4e-15) -> (L_q, 7e-16)` with the spatial certificate alone, and R6 at `1.98` (floor `1e-31`, shift `5e-17`) is no longer the strongest all-input statement in the package. The comparison threshold is also sharp at `mu = 1e-7` (fails at `1.2e-7`; generalized minimum `1.218e-7`), and the residual factor improves to `theta = 0.8` (fails at `0.75`).

At the second step the comparison passes at `mu = 5e-8` and fails at `7e-8` (generalized minimum `6.04e-8`), so `1e-8` can be raised to `5e-8`.

### 1.2 Carry the floor directly through the relative test

Certifying `(beta_theta - m)(H_theta - m) - E_theta - budget > 0` gives `M_theta >= m I` on the whole space. Two consequences, neither of which is in the paper.

*Lemma (direct floor).* If `M_theta >= m I` with `0 < m <= f_0`, then `T*QT >= m I` and `Q >= m tau^{-2} I`, where `tau = (q + sqrt(q^2 + 4))/2` and `q >= ||J||`.

*Proof.* `M_theta >= m` forces `H_J >= m` and `F >= m` (restrict to `(f,0)` and `(0,v)`). Since `lambda = theta^{-1/2} >= 1`,

    T*QT = (1/lambda) M_theta + (1 - 1/lambda) diag(H_J, F) >= (m/lambda + (1 - 1/lambda) m) I = m I,

and `Q[u] = (T*QT)[T^{-1}u] >= m ||T^{-1}u||^2 >= m ||u||^2 / ||T||^2` with `||T|| <= tau`.

So the `(1 - sqrt(theta))` factor of Lemma 6.1 is not needed for the floor, and neither is the comparison `H_J >= mu A`. On the first-step matrices `M_{0.9} >= 2e-29` passes (fails at `3e-29`) and `M_{0.8} >= 1e-29` passes, giving `Q_{0,L_q} >= 2e-29/2.5508 = 7.8e-30` by this route alone; the absolute test gives `2e-29` directly, so at the first step the absolute test is the better of the two, but at later steps (Section 2) the relative test is the one that tolerates a weaker complement floor, and it should carry `m`.

The conditional continuation theorem then simplifies. Its per-step hypotheses become: a bounded continuation `J_j`, a certified `M_{theta_j} >= m_j' I`, and the slab floor `F_j >= f_j`; the recurrence is `m_{j+1} = m_j' / tau_j^2`, and the shift schedule is unchanged. The `mu_j` disappear. This matters because the scalar recurrence `m_{j+1} = (1 - sqrt(theta)) min(mu m_j, f_j)/tau^2` loses a factor of about `2e-9` per quarter-step, while the compressed lowest eigenvalue actually falls by a factor 17–20 per quarter-step (`6.56e-28 -> 3.28e-29 -> 1.88e-30` at `log 7, L_q, L_2`). After three steps the scalar floor would be `1e-25` below the truth and the shift schedule `omega_j = sqrt(m_j/(2C))` would be uselessly small. The old-energy comparison should stay as a diagnostic of continuation quality (and the clean statement `S >= 1e-8 A` is worth keeping), but it should not carry the floor.

### 1.3 Name the mechanism

The reason the relative test works is the endpoint-logarithm coefficient `[sqrt(h/a) phi(1) - (J phi)(0)]/2` in Section 6: the Galerkin continuation approximately matches the join, the log singularity of the new-slab output cancels, and the leakage of the transformed operator into the new complement collapses. The 32-mode continuation reproduces the lowest eigenvalue of the full head to four digits at both steps, so the continuation is not a bottleneck anywhere. This deserves a paragraph, and it is also the design principle for any later variant (local gamma profiles, exponential modes): whatever basis is used on the slab, the continuation must be able to match the join.

### 1.4 Proposed restatement of the main theorem

Pending the repository re-runs: in the working framework, on the entire old form domain, `R*F^{-1}R <= 0.8 H_J`; `M_{0.9} >= 2e-29 I`, hence `H_J >= 2e-29 I`; `H_J >= 1e-7 A` and `A - B*F^{-1}B >= 2e-8 A`; directly `Q_{0,L_q} >= 2e-29 I`; and the shift statements of 1.1. At the second step, `H_{J_2} >= 5e-8 A_2`; the residual and absolute premises are not certified, for the reason in Section 2. Add the compressed eigenvalue ladder as the diagnostic that shows each floor's sharpness.

## 2. Closing the second step

The second-step tests fail only because the three-interval complement floor is too small. With everything else unchanged and an oracle floor in place of the certified `0.4109` (absolute) or `0.2931` (`theta = 0.9`), both tests pass once the floor reaches `0.55`; with `0.65` the stored matrices certify `Q_{0,L_2} >= 1e-30` (failing at `1e-29`; compressed lowest eigenvalue `1.88e-30`) and `theta = 0.8`. So the task is purely to raise the analytic floor by about `0.15` (absolute) or `0.26` (residual). From the comparison matrix, with `rho_2 = 2.027` subtracted uniformly:

| verification space | joint floor | `theta = 0.9` floor | verdict |
|---|---|---|---|
| 256 + 32 + 32 (current) | 0.411 | 0.293 | fails both |
| 256 + 48 + 48 | 0.562 | 0.450 | absolute only |
| 256 + 64 + 64 | 0.654 | 0.547 | absolute yes, residual marginal |
| 256 + 96 + 96 | 0.768 | 0.665 | both, with margin |
| 256 + 128 + 128 | 0.837 | 0.737 | both, comfortable |
| 384 + 32 + 32 | 0.637 | 0.513 | absolute yes, residual marginal |
| 384 + 64 + 64 | 0.924 | 0.810 | both, comfortable |

Recommended experiment (this is STATUS.md's item 1 with a target attached): rebuild the first step with a 256 + 96 head (the `old_256_320_6144` cache supplies the old/old blocks; the cross and slab blocks scale with the slab dimension, so expect a build of the order of an hour), extend with `--new 96`, and run the absolute test, the relative test with an inserted floor, and the comparison, each with a bisection. Expected outcome: `Q_{0,L_2}` between `1e-30` and `1.9e-30`, `theta` between `0.8` and `0.9`, `mu` about `5e-8`, and a shift interval near `sqrt(1e-30/(2 C_{L_2}))`, of order `1.7e-16`. Two things not to spend time on: the separate-tail weight search (with the Perron weights all three floors equal the joint floor, so the search can only redistribute, which the recorded attempts confirm), and blockwise arithmetic bounds in place of the uniform `rho_2` (the triangle inequality makes the floor negative).

## 3. The recursion needs a different invariant

Appending a 32-mode slab per step does not scale. With the constants at hand, a chain of `k` slabs behind the 256-mode head has analytic floor `0.41, 0.13, -0.26, -0.74` for `k = 2, 3, 5, 9`; with 64-mode slabs `0.65, 0.45, 0.16, -0.23`; with 128-mode slabs `0.84, 0.69, 0.48, 0.19`. Each appended slab adds an adjacent `pi/2` coupling to a path whose long-interval diagonal stays at `g_{a,256} - rho`, and the smallest eigenvalue of the comparison matrix decreases roughly linearly in `k`. Enlarging the slabs only delays this.

Two invariants are viable. The first is the two-interval invariant: at every step the old interval `(0, L_j)` is treated as one interval with a fresh global Legendre basis of `N_j` modes, and the analytic floor is the first-step value (`0.91` for `N = 256`, `M = 32` at `L_q`) for as long as `g_{L_j,N_j} - rho_{L_j}` stays near `1.8`. Its cost is the old/old Gram rebuild at every step (21 minutes at 256 modes, scaling roughly like `N^2 M` in 6144-bit operations), and its benefit is that the head, leakage and continuation are all freshly certified against a clean two-block complement. The second is a hybrid: append slabs while the analytic floor stays above the threshold the tests need (about `0.55` here), then merge all intervals into one global basis and continue. With 96-mode slabs the merge would be needed every three or four quarter-steps. A comparison run of the two-interval second step (global basis on `(0, L_q)`, `N = 288` or `320`, new slab 32 or 64) against the three-interval one is the experiment that decides this; expected cost about forty minutes for the rebuild.

Whichever is chosen, the state carried between steps should be what the paper already recommends: the head, the two (or more) full-output Grams, the exact rational continuation, and now the certified `m_j'` from the relative test plus the compressed eigenvalue ladder as the sharpness diagnostic.

## 4. How far can the method go? A dimension estimate

The joint complement floor requires the gamma tail constant to beat the arithmetic norm, roughly `H_N - gamma - log(pi L) > rho_L`. The bound `rho_L` cannot be much improved: high-frequency functions `phi(x) cos(omega x)` with `omega log n` near `2 pi Z` for every active `n` are orthogonal to any fixed polynomial space and realize essentially the positive Rayleigh quotient of the arithmetic operator, so `||K T K||` is at least the constant function's quotient `rho^+_L = (2/L) sum_{log n < L} Lambda(n) n^{-1/2} (L - log n)`, and the certified `rho` is already within 15 percent of it at `L = 2`. On such a function the central form is about `(log(omega) - c - rho_L) ||k||^2`, so the tail is positive only above frequency `e^{rho_L + c}`, and the head must reach that frequency: `N` grows like `L e^{rho_L}`.

| `L` | `e^L` | `rho^+_L` | `N` for a positive floor (`pi L e^gamma e^rho`) | observed / projected `N` for the tests to pass |
|---|---|---|---|---|
| 1.98 | 7.2 | 1.70 | 61 | 256 (128 failed) |
| 2.5 | 12.2 | 2.80 | 230 | about 1000 |
| 3.0 | 20.1 | 4.09 | 1000 | 3000–4000 |
| 3.5 | 33.1 | 5.65 | 5500 | 15000–20000 |
| 4.0 | 54.6 | 7.54 | 42000 | more than 100000 |

The last column scales the first-step experience (a factor of about four between "floor positive" and "leakage test passes"). Dense 6144-bit Grams at `N = 3000` are about 7 GB each and the build time scales like `(3000/256)^2` times the current 21 minutes, roughly two days on one core; this is a workstation job but feasible. `L = 3.5` is not feasible with this code, and `L = 4` not with this method. Precision is not the barrier: the ladder decays by about `e^{-88}` per unit depth at `L = 2`, so certifying floors at `L = 3` needs ball radii below about `1e-70`, which 6144-bit arithmetic with a larger profile degree can supply.

The honest summary for the manuscript is that the polynomial-complement method as implemented has a practical horizon near `L = 3` (arithmetic support up to `n = 20`), and that reaching it is a matter of engineering; going beyond it needs a different idea for the tail, and the paper's Section 12.4 proposal (local profiles, exponential modes) removes the `L < 3` representation limit but not this one.

## 5. Two strategic questions worth settling before more computation

### 5.1 What does finite-horizon positivity at horizon `L` say about zeros?

The Weil-depth review verified numerically that `Q_{0,L}[f] = sum_rho |f_c^hat(gamma_rho)|^2` in the working normalization. For a hypothetical off-line pair `1/2 +- delta + i t` (with its conjugates), the same explicit formula gives a contribution

    2 ( |<f, cosh(delta X) e^{itX}>|^2 - |<f, sinh(delta X) e^{itX}>|^2 ),

(up to the normalization constants of the explicit formula, with `X` the centered coordinate), a difference of two squares whose negative part is at most `L sinh^2(delta L/2) ||f||^2` in size, hence of order `(delta L)^2 L ||f||^2 / 4` when `delta L` is small. Meanwhile the certificates show that the near-null vectors of `Q_{0,L}` at `L` near 2 are very smooth functions (well represented by a few hundred Legendre modes) whose transforms are negligible at large heights; and the high-frequency part of the space is handled unconditionally by the tail argument. My reading, which I have not made rigorous, is that finite-horizon positivity at horizon `L` is insensitive to off-line zeros with `delta L` well below one, that the near-null space of `Q_{0,L}` for `L` near 2 is governed by the first few dozen zeros, all classically known, and that consequently the certificates at `L <= 3` are consistency checks of the framework rather than information about zeros. This is not an objection to the programme, whose stated goal is an all-depth argument; but it fixes what the milestones mean, and it argues for putting effort into the analytic recursion rather than into pushing `L` numerically.

Two cheap experiments settle the reading. First, compute the lowest eigenvalue of the truncated zero-sum form `sum_{|gamma| < T} |f_c^hat(gamma)|^2` on the 288-mode head with the first `K` zeros (`K` up to a few thousand, using the Fourier-side code from the Weil-depth review) and compare with `3.28e-29`; if the two agree once `K` is a few hundred, the near-null space is a low-zero phenomenon. Second, for the hypothetical pair, compute the largest `delta` at height `t` for which the sinh-term can make the 288-mode compression indefinite; this gives a detection threshold `delta(L, t)`, and comparing it with the classically verified region says what any finite-horizon certificate at that `L` could ever exclude.

### 5.2 Is the positive-shift (storage) programme still the right frame?

Every certified statement in the paper is a zero-shift statement plus the perturbation bound `||Q_s - Q_0|| <= C_L s^2`, and this is enough for the diagonal criterion: the conditional theorem needs `Q_{0,L_j} >= m_j > 0` and a shift `omega_j <= sqrt(m_j/(2C_{L_j}))`. The Cayley storage identities are correct and elegant, and the finite depth-shift step (4.1) is the right formulation if one ever wants to certify at fixed positive shift, but nothing currently requires it. Unless a positive-shift certificate is planned, I would move that material to a motivational section and keep the paper's spine as: spatial split, graph continuation, relative test with inserted floor, conditional theorem with the direct-floor recurrence. If a positive-shift certificate is planned, the natural first target is the bounded Cayley block form at `omega = 1e-11` on the existing 288-mode head, where the `P_omega = (2/omega) I + compact` structure makes the tail trivially positive for large `N` but, as the paper notes, offers no uniformity as `omega -> 0`.

## 6. Suggested order of work

1. Add archive-based replays with a `--floor` bisection (first-step absolute and relative, second-step all three) and a streaming loader; re-run; restate Theorem 1.1 and Sections 9–11; fix the dangling commit and the repository indices. Hours.
2. Rebuild 256 + 96 and extend to 256 + 96 + 96; certify the second step. Half a day of compute.
3. Run the two-interval second step for comparison and choose the recursion invariant. One day.
4. Fourier-side check of the near-null space against the first `K` zeros, and the detection-threshold computation. One to two days of analysis and light computation.
5. Decide, with the dimension table in hand, whether `L = 2.5` and `L = 3` are worth the workstation time, and what the manuscript should say about the horizon of the method.
