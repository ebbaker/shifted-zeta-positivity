# Barrier theorem and ladder conjecture — draft note (11 September 2026)

Claude (Fable 5.1), for Teddy. Draft statements with proofs or proof sketches, the numerical evidence behind them, and an assessment of what each accomplishes. Everything is in the working Weil-depth v0.3 normalization. Numerics in this note are double-precision Galerkin computations (illustrative, not certified); the scripts are `ladder_fit.py`, `barrier_numerics.py`, `twisted.py`, `farband.py` beside this note.

## 0. Short answers

**Barrier theorem.** The arithmetic operator `T_L = sum_{n<e^L} Lambda(n) n^{-1/2} (T_{log n} + T_{log n}^*)` on `L^2(0,L)` has purely essential spectrum: no isolated eigenvalue of finite multiplicity. Hence on the orthogonal complement of *any* finite-dimensional head the supremum of its Rayleigh quotient is exactly `lambda_max(T_L)`. Every certificate that bounds the complement by "gamma tail floor minus arithmetic bound" (as v0.1–v0.3 do) therefore needs a head of dimension `N > pi L e^{lambda_max(T_L)}` just to have a positive floor, and `lambda_max(T_L) >= rho^+_L ~ 8 e^{L/2}/L`. Computed values: `lambda_max(T_L) = 1.78, 1.91, 1.96, 2.96, 4.29, 5.94, 7.97` at `L = log 7, L_q, L_2, 2.5, 3, 3.5, 4`, so `N > 36, 42, 45, 152, 689, 4170, 36400`. The v0.3 weight bounds `rho = 1.9492` (at `L_q`) and `2.0269` (at `L_2`) exceed the true `lambda_max` by only 2–4 %: there is nothing left to gain from sharper arithmetic norm bounds.

**Ladder conjecture.** Using all nine two-sided enclosures now available (Weil-depth `log 2 … log 7` and `9/5`, storage-depth `L_q`, `L_2`), `-ln lambda_min(Q_{0,L})` is linear in `e^L` to within `±1` over `0.69 <= L <= 2.01`: `-ln lambda_min = 11.4 e^L - 17`. Each new integer under the horizon divides `lambda_min` by about `e^{11.4} ~ 10^5`, whether or not it is a prime power. The zero-count variable `e^L (L-1) ~ N(2 pi e^L)` that I suggested earlier is the *worst* of the candidate laws over this range; that remark is withdrawn. The conjecture is stated below in a weak form (`e^L <~ -ln lambda_min <~ L e^L`) and a sharp form (`-ln lambda_min ~ kappa e^L L^theta`, `theta` in `[0,1]`, data favouring `theta ~ 0`, `kappa ~ 11.4`), with a decisive test at `L = log 11`.

**Is the ladder conjecture a reformulation of RH?** No. `lambda_min(Q_{0,L}) > 0` for every `L` *is* RH (Weil's criterion in finite-horizon form). The conjecture's lower-bound half (`lambda_min(L) >= e^{-C L e^L}` for all `L`) implies RH and is strictly stronger; RH gives positivity but no rate. Under RH the weak form is plausibly provable from sampling theory (sketch in Section 3.4), in which case the weak form is an *effective* Weil criterion, equivalent to RH. The sharp form — the power of `L` and the constant — carries information beyond RH about the extremal problem "how small can the transform of a function supported on an interval of length `L` be at all zeros of zeta", i.e. about the sampling constant of the zeros in Paley–Wiener spaces. What it accomplishes is listed in Section 4.

## 1. Setting: `Q_{0,L}` as a compressed Fourier multiplier

For real `f` in `L^2(0,L)` write `fhat(tau) = int_0^L f(x) e^{-i tau x} dx` and `(T_u f)(x) = f(x-u) 1_{(0,L)}(x)`. Because `f` vanishes outside `(0,L)`, the truncation in `T_u` is automatic in the quadratic form:

    <f, T_u f> = int_R f(x) f(x-u) dx = (1/2pi) int_R |fhat(tau)|^2 cos(u tau) dtau.

So with `P_L` the projection of `L^2(R)` onto `L^2(0,L)` and `M_w` the Fourier multiplier by `w`,

    T_L = P_L M_{w_L} P_L,   w_L(tau) = 2 sum_{n<e^L} Lambda(n) n^{-1/2} cos(tau log n) = 2 Re sum_{n<e^L} Lambda(n) n^{-1/2-i tau},

the sharp-cutoff partial sum of `-2 Re zeta'/zeta(1/2 + i tau)`. Likewise the archimedean part is `G_L = P_L M_g P_L` with `g(tau) = Re psi(1/4 + i tau/2) - log pi = log(tau/2pi) + O(tau^{-2})`, increasing on `tau > 0`, `g(0) = -5.37`; the pole term `2|C|^2 - 2|S|^2` has rank two. Hence

    Q_{0,L} = P_L M_{m_L} P_L + (rank two),   m_L = g - w_L,

a truncated Wiener–Hopf operator on a finite interval with an almost-periodic symbol. The symbol is negative near `tau = 0` (`m_L(0) = -5.37 - W_L`, `W_L := w_L(0) = 2 sum_{n<e^L} Lambda(n) n^{-1/2} ~ 4 e^{L/2}`) and at every "Kronecker return" of `w_L` below `2 pi e^{W_L}`; positivity of `Q_{0,L}` is a compression phenomenon (uncertainty principle), which is what Weil positivity is in this language. Under RH the explicit formula gives `Q_{0,L}[f] = sum_gamma |fhat(gamma)|^2` (all zeros with multiplicity; `= 2 sum_{gamma>0} |fhat_c(gamma)|^2` in the paper's notation). Since `g -> +infinity`, `Q_{0,L}` has compact resolvent and discrete spectrum; `lambda_min(L) := min spec Q_{0,L}` is an eigenvalue.

Useful constants: `rho^+_L := <1, T_L 1>/L = (2/L) sum_{n<e^L} Lambda(n) n^{-1/2} (L - log n)` (the Fejér average of `w_L`, `~ 8 e^{L/2}/L`), and `lambda_max(T_L) := sup spec T_L`, with `rho^+_L <= lambda_max(T_L) <= W_L`.

## 2. The barrier theorem

### 2.1 Statement

**Theorem A (arithmetic operator has purely essential spectrum).** Let `L > 0` and `T_L` as above.

1. `sigma(T_L)` is contained in `[-W_L, W_L]` and `lambda_max(T_L) >= rho^+_L`.
2. `sigma_ess(T_L) = sigma(T_L)`: `T_L` has no isolated eigenvalue of finite multiplicity.
3. For every finite-dimensional subspace `V` of `L^2(0,L)`,
   `sup_{0 != f in V^perp} <f, T_L f>/||f||^2 = lambda_max(T_L)` and `inf_{0 != f in V^perp} <f, T_L f>/||f||^2 = lambda_min(T_L)`.
4. The same holds for the real form, with real modulations `cos(omega x)` in place of `e^{i omega x}`.

Only the linear independence of `{log p : p prime}` over `Q` enters; nothing else about zeta.

### 2.2 Proof

*Modulation identity.* For `omega` real let `M_omega f = e^{i omega x} f` (unitary on `L^2(0,L)`). Since `M_omega` is a pointwise multiplication it commutes with restriction to `(0,L)`, so `T_u M_omega = e^{-i omega u} M_omega T_u` and `T_u^* M_omega = e^{i omega u} M_omega T_u^*`. Hence

    T_L M_omega = M_omega T_L^{(omega)},   T_L^{(omega)} := sum_{n<e^L} Lambda(n) n^{-1/2} (n^{-i omega} T_{log n} + n^{i omega} T_{log n}^*),

and `||T_L^{(omega)} - T_L|| <= 2 sum_{n<e^L} Lambda(n) n^{-1/2} |n^{i omega} - 1| <= 4 pi sum_{n<e^L} Lambda(n) n^{-1/2} ||omega log n / 2pi||`, with `||.||` the distance to the nearest integer.

*Return frequencies.* Let `p_1 = 2 < p_2 < ... < p_k` be the primes below `e^L` and `theta_j = log p_j / log 2` (irrational for `j >= 2`). By Dirichlet's simultaneous approximation theorem, for every integer `Q > 1` there is an integer `1 <= q <= Q^{k-1}` with `||q theta_j|| <= 1/Q` for all `j`. Put `omega = 2 pi q / log 2`; then `omega log 2 / 2pi = q` is an integer and `||omega log p_j / 2pi|| <= 1/Q`, hence also `||omega log p_j^m / 2pi|| <= m/Q`. Because the `theta_j` are irrational, `q` is unbounded as `Q -> infinity`, so there is a sequence `omega_k -> infinity` with `||T_L^{(omega_k)} - T_L|| -> 0`. (For `L <= log 3` only `n = 2` occurs and `omega_k = 2 pi k / log 2` gives `T_L^{(omega_k)} = T_L` exactly.)

*(2).* Suppose `lambda` in `sigma(T_L)` is not in `sigma_ess(T_L)`. Then `lambda` is an isolated eigenvalue of finite multiplicity: there is an eigenvector `phi` (`T_L phi = lambda phi`, `||phi|| = 1`) and, for some `eps > 0`, the spectral projection `E` of `T_L` onto `(lambda - eps, lambda + eps)` has finite rank. Put `f_k = M_{omega_k} phi`. Then `||f_k|| = 1`, `f_k -> 0` weakly (Riemann–Lebesgue, `phi` fixed), and `||(T_L - lambda) f_k|| = ||M_{omega_k}(T_L^{(omega_k)} - lambda) phi|| = ||(T_L^{(omega_k)} - T_L) phi|| -> 0`. Since `E` has finite rank, `||E f_k|| -> 0`, so `||(1-E) f_k|| -> 1` and `||(T_L - lambda) f_k|| >= eps ||(1-E) f_k|| - ||T_L - lambda|| ||E f_k|| -> eps > 0`, a contradiction.

*(3).* Given `V` and `delta > 0` pick `phi` with `<phi, T_L phi>/||phi||^2 > lambda_max(T_L) - delta` and put `f_k = M_{omega_k} phi`. Then `<f_k, T_L f_k> = <phi, T_L^{(omega_k)} phi> -> <phi, T_L phi>`, while `||P_V f_k|| -> 0` (finitely many inner products `<v_j, M_{omega_k} phi> -> 0`). So `g_k := P_{V^perp} f_k` satisfies `||g_k - f_k|| -> 0` and `<g_k, T_L g_k>/||g_k||^2 -> <phi, T_L phi>/||phi||^2`. The reverse inequality is trivial; the infimum is the same argument.

*(1)* is immediate from the multiplier representation and the constant function. *(4):* with `f = cos(omega x) phi`, `T_u f = [cos(omega x) cos(omega u) + sin(omega x) sin(omega u)] T_u phi`; along the return sequence `cos(omega_k log n) -> 1`, `sin(omega_k log n) -> 0` for the finitely many `n`, so `T_L f_k = cos(omega_k x) T_L phi + o(1)` and `||f_k||^2 -> ||phi||^2/2`, giving the same limit of the quotient. ∎

### 2.3 Consequence for certificates

**Corollary B (dimension barrier for separated complement floors).** Suppose a certificate controls `Q_{0,L}` on `V^perp` by `inf_{V^perp} G_L - sup_{V^perp} T_L` (with or without cross-term budgets). Then the arithmetic bound used must satisfy `rho >= lambda_max(T_L)`, and the certified floor is at most `g_V - lambda_max(T_L)`, where `g_V` is the gamma floor over `V^perp`. For the Legendre head `V_N` on `(0,L)`, `g_{V_N} <= <P_N, G_L P_N> = H_N - gamma - log(pi L / 2) + o(1)` (the diagonal Rayleigh quotient of the `N`-th normalized Legendre mode; numerically `H_N - gamma - log(pi L) + 0.69` at `N = 32 … 256`, `L = log 7` and `3`), and the proven v0.3 tail floor is `H_N - gamma - log(pi L) - (correction)`. Hence a positive separated floor needs

    N > N_sep(L) := pi L e^{lambda_max(T_L)}   (with the proven floor; `(pi L/2) e^{lambda_max}` even with the sharpest conceivable one),

and since `lambda_max(T_L) >= rho^+_L ~ 8 e^{L/2}/L`, `N_sep` grows doubly exponentially in `L/2`. Passing the v0.3 leakage tests has cost a further factor 4–6 (`N = 256` at `L_q`, where `N_sep = 42`).

Equivalently: `N_sep = (L/2) tau^*_L` with `tau^*_L := 2 pi e^{lambda_max(T_L)}`, the frequency beyond which the gamma symbol exceeds every compressed arithmetic quotient. A separated certificate must resolve all frequencies below `tau^*_L`.

### 2.4 Numbers

Galerkin in normalized shifted Legendre modes, `K = 768` (lower bounds for `lambda_max`, converged to three digits between `K = 512` and `768`):

| `L` | terms `n` | `W_L` | `rho^+_L` | `lambda_max(T_L)` | v0.3 bound `rho` | `tau^*_L` | `N_sep` |
|---|---|---|---|---|---|---|---|
| `log 7 = 1.946` | 2,3,4,5 | 4.38 | 1.632 | 1.778 | — | 37 | 36 |
| `L_q = 1.979` | 2,3,4,5,7 | 5.85 | 1.703 | 1.915 | 1.9492 | 43 | 42 |
| `L_2 = 2.013` | 2,3,4,5,7 | 5.85 | 1.772 | 1.958 | 2.0269 | 45 | 45 |
| 2.5 | …,11 | 8.52 | 2.797 | 2.959 | — | 121 | 152 |
| 3.0 | …,19 | 13.02 | 4.085 | 4.292 | — | 459 | 689 |
| 3.5 | …,32 | 18.12 | 5.647 | 5.939 | — | 2380 | 4170 |
| 4.0 | …,53 | 24.38 | 7.538 | 7.974 | — | 18200 | 36400 |

Two checks. The v0.3 arithmetic weight bounds are valid (`rho > lambda_max`) and within 0.035 and 0.07 of the truth, so the arithmetic side of the separated certificate is already essentially sharp. And the constant-function value `rho^+_L` underestimates the barrier constant by only 6–9 %, so the dimension estimates of storage-depth v0.3 §6 (which used `rho^+_L`) were slightly optimistic; the corrected law is `N_sep = pi L e^{lambda_max(T_L)}` with the values above.

### 2.5 What the theorem does not say, and where the wall really is

*It says nothing about `Q_{0,L}` itself.* `Q_{0,L}` has compact resolvent, so `inf_{V_N^perp} Q_{0,L} -> +infinity` as `N -> infinity` for any exhausting sequence of heads, and it becomes positive far earlier than `N_sep`. In the `K = 768` Galerkin space the top of the *arithmetic* quotient over the complement of the first `N` Legendre modes is

| `L` | `lambda_max(T_L)` | `N=32` | `N=64` | `N=128` | `N=256` |
|---|---|---|---|---|---|
| 3.0 | 4.29 | 3.21 | 3.20 | 3.14 | 2.91 |
| 3.5 | 5.94 | 3.67 | 3.66 | 3.63 | 3.50 |
| 4.0 | 7.97 | 3.83 | 3.82 | 3.75 | 3.68 |

i.e. within the frequency range the Galerkin space resolves (`|tau| <~ 2K/L`), functions orthogonal to a few dozen Legendre modes have arithmetic quotient about 3.2–3.8, nearly independent of `L`, instead of `lambda_max(T_L) = 4.3–8.0`. The joint complement floor `g_N - (this)` is positive at `N ~ 250` for `L = 3` and `N ~ 600` for `L = 4`. The gap between this and `N_sep` is the price of rigour on an infinite-dimensional complement: by Theorem A the near-maximizers of `T_L` in `V_N^perp` exist, but they live at return frequencies, which the finite Galerkin space does not see.

*The two available analytic handles both fail beyond `N_sep`.* The compressed norm of `T_L` on the complement is exactly `lambda_max(T_L)` (Theorem A). The pointwise symbol is worse: `g(tau) >= w_L(tau)` holds for all `tau >= Omega` only when `Omega` is close to `2 pi e^{W_L}` — the last violation is at `tau = 1550` for `L = 2` (`2 pi e^{W_L} = 2200`), `19852` for `L = 2.5` (`3.3e4`), and `1.42e6` for `L = 3` (`2.8e6`), where `w_L` reaches `12.53` out of `W_3 = 13.02` at `tau = 5.5e5`. Returns are not rare, and any band-limited (spectral-cutoff) decomposition of the complement inherits the pointwise symbol and loses the compression. So neither "sharper norm bounds" nor "check the symbol pointwise" can move the wall.

*What could: a frequency-resolved certificate (Proposal C).* The only route past `N_sep` that is consistent with Theorem A is to keep every piece of the decomposition supported in `(0,L)` (so that the compression bound `lambda_max(T_L)` applies to the far band) while resolving the middle band with functions of `L^2(0,L)` that are frequency-concentrated: time-limited prolate spheroidal functions on `(0,L)` for the band `[-tau^*, tau^*]`, or modulated prolates for sub-bands. Then: the far remainder (mass fraction inside the band bounded by Slepian's eigenvalues) has `G`-quotient `>= g(tau^*) - O(eps W_L)` and `T`-quotient `<= lambda_max(T_L)`, hence positive `Q` for `tau^* = 2 pi e^{lambda_max + delta}`; the head `V_N` is exact; the middle band `[2N/L, tau^*]` is covered by sub-band blocks whose arithmetic tops are computed (they are the 3.2–3.8 of the table, rising towards `lambda_max` only near returns, where `g` is already large), with off-diagonal blocks bounded by leakage. The total number of degrees of freedom is still `~ L tau^*_L / pi = 2 N_sep`, but the dense head only needs to reach the frequency where the sub-band tops fall below `g`, roughly `2 pi e^{3.8} ~ 300`, i.e. `N ~ 600` at `L = 4`; the rest is many small blocks. Cost estimate for `L = 4`: dense head ~600, about 900 blocks of ~25 modes up to `tau^* = 1.8e4`, plus the leakage bookkeeping. For `L = 5` (`tau^* = 6e9`) the block count is `3e8`: out of reach with rigorous arithmetic. So a complete redesign buys `L = 4`, perhaps a heroic `L = 5`, and the height a certificate at horizon `L` sees is `~ e^{2L} ~ 3000` to `2e4`, far below the `3e12` already verified. This is method development, not information about zeros.

## 3. The ladder conjecture

### 3.1 The data

Nine two-sided enclosures of `lambda_min(Q_{0,L})` (even sector = bottom of the spectrum at every horizon). Point estimates are the ball Rayleigh quotients (upper bounds); floors are within a factor 1.01–1.6 of them except at `log 7` (factor 5, a lossy certificate) and within 10 % at `L_q`, `L_2`.

| horizon | `L` | floor | upper bound | `-ln lambda` | `-ln lambda / e^L` | increment per unit `e^L` |
|---|---|---|---|---|---|---|
| `log 2` | 0.6931 | 1.32e-3 | 1.33e-3 | 6.62 | 3.31 | — |
| `log 3` | 1.0986 | 5.52e-8 | 5.54e-8 | 16.71 | 5.57 | 10.09 |
| `log 4` | 1.3863 | 7.48e-13 | 7.57e-13 | 27.91 | 6.98 | 11.20 |
| `log 5` | 1.6094 | 8.95e-18 | 9.30e-18 | 39.22 | 7.84 | 11.31 |
| `log 6` | 1.7918 | 5.93e-23 | 7.33e-23 | 50.97 | 8.49 | 11.75 |
| `9/5` | 1.8000 | 3.38e-23 | 4.14e-23 | 51.54 | 8.52 | (11.5, inside a window) |
| `log 7` | 1.9459 | 1.37e-28 | 6.81e-28 | 62.56 | 8.94 | 11.59 |
| `L_q` | 1.9793 | 2.99e-29 | 3.29e-29 | 65.59 | 9.06 | (12.7) |
| `L_2` | 2.0127 | 1.69e-30 | 1.89e-30 | 68.44 | 9.15 | (11.6) |

Least-squares fits of `-ln lambda_min` (rms residual in `ln lambda`, i.e. in natural-log units of the eigenvalue):

| law | fit | rms | max residual |
|---|---|---|---|
| `c e^L + b` | `11.37 e^L - 17.05` | 0.47 | 0.94 (at `log 2`) |
| `c L e^L + b` | `4.47 L e^L + 2.06` | 0.94 | 1.64 |
| `c e^L (L-1) + b` (`~ N(2 pi e^L)`) | `7.34 e^L (L-1) + 14.6` | 1.82 | 3.47 |
| `c e^L (L - a) + b` | `1.47 e^L (L + 5.2) - 10.8` | 0.12 | 0.24 |

The single-variable law in `e^L` fits nine points spanning 27 orders of magnitude to within a factor `e^{0.94} = 2.6`, with a shallow U-shaped residual; the three-parameter fit shows the `e^L` term dominates with a small `L e^L` admixture. The increments per unit of `e^L` (per new integer under the horizon) drift slowly upward, `10.1, 11.2, 11.3, 11.75, 11.6`, and the passage `log 6 -> log 7`, which adds no arithmetic term (`Lambda(6) = 0`; `n = 7` enters only above `log 7`), costs the same as the others: the decay is driven by the growth of the domain, not by new primes. Within one arithmetic window the local slope is steeper right after a prime power enters (`d ln lambda/dL = -91` on `(log 7, L_q)`, `-86` on `(L_q, L_2)`, against `-81` to `-84` for the smooth law), a kink structure the smooth law averages over.

### 3.2 Statement

Let `T_L := 2 pi e^L`, the height at which the density of zeros of zeta, `(1/2pi) log(t/2pi)`, equals the zero density `L/2pi` of entire functions of exponential type `L/2`, i.e. of transforms of functions supported on an interval of length `L`. Below `T_L` a function of `PW_{L/2}` can vanish at every zero; above it cannot.

**Conjecture L (ladder).**

*(weak form)* There are constants `0 < c_1 <= c_2` such that for all `L >= 1`
    c_1 e^L <= -ln lambda_min(Q_{0,L}) <= c_2 L e^L.

*(sharp form)* There are `kappa > 0` and `theta` in `[0,1]` such that
    -ln lambda_min(Q_{0,L}) = kappa e^L L^theta (1 + o(1)),   L -> infinity.
The enclosures at `0.69 <= L <= 2.01` are consistent with `theta = 0`, `kappa ~ 11.4` (`lambda_min ~ e^{17} exp(-1.81 T_L)`), with a residual drift that a small power of `L` or a `log L` factor would absorb; the best fit with `theta = 1` leaves residuals up to 1.6, and the zero-count law `e^L (L-1)` residuals up to 3.5.

*(spectral ladder, observation)* At fixed `L` the lowest even-sector eigenvalues form a geometric ladder: `ln(lambda_1/lambda_0), ln(lambda_2/lambda_1) = 14.7, 13.5` at `log 7`, `13.2, 11.5` at `log 5`, `10.2, 6.2` at `log 3` (head diagnostics), the spacing growing slowly with `L`; the odd sector interlaces (`4.8e-25` at `log 7`). Under RH each further dimension of a trial subspace forces one more unannihilated constraint at the zeros; the spacing is the cost of one such constraint.

*(test)* Predictions for the next horizons: at `log 8` the `e^L` law gives `-ln lambda_min = 73.9` (`lambda ~ 8e-33`) and the `L e^L` law `76.4` (`6e-34`); at `log 11` they give `108.0` (`1e-47`) against `120.0` (`8e-53`). The storage-depth march to `log 8` is a weak test (2.5 in the log, resolvable with 10 % enclosures), `log 11` a decisive one. Intermediate horizons inside a window (as `9/5` inside the `log 6` window) map the kinks.

### 3.3 Sampling form and heuristic

Under RH, `lambda_min(L) = 2 pi inf { sum_gamma |F(gamma)|^2 / ||F||^2_{L^2(R)} : 0 != F in PW_{L/2} }`, the lower sampling constant of the zero set `Gamma = {gamma}` for the Paley–Wiener space of type `L/2` (positive for every `L`: a nonzero function of exponential type `L/2` cannot vanish on a set whose density exceeds `L/2pi`, and `Q_{0,L}` has discrete spectrum). The extremal function vanishes at the zeros below about `T_L`, spending `2 N(T_L) ~ 2 e^L (L-1)` of the `T_L L / pi = 2 L e^L` degrees of freedom a type-`L/2` function has on `[-T_L, T_L]`, and pays with its mass beyond `T_L`, where the zeros are denser than it can follow. Slepian's concentration asymptotics make the leakage of a type-`L/2` function built from a fraction `1 - eps` of the Nyquist number of modes on `[-T, T]` decay like `exp(-T L psi(eps))`; with `eps = 1 - log(T/2pi e)/L` and `T` optimized this gives `-ln lambda_min ~ const · e^L`, the height scaling, with logarithmic corrections coming from the edge behaviour of the Slepian spectrum (`psi(eps) ~ pi eps / log(T L)` near the edge) that would show up as the `L^theta` or `log L` factor. This is the reason to write the conjecture in the height variable `T_L` rather than the count `N(T_L)`; it also matches the observation that a new integer under the horizon costs the same whether or not it is a prime power. It is a heuristic for the upper bound on `lambda_min`, not a proof of anything.

### 3.4 Relation to RH

1. `lambda_min(Q_{0,L}) > 0` for all `L > 0` is equivalent to RH. (Weil's criterion needs positivity of `W(g * g~)` for `g` in `C_c^infty(R)`; autocorrelation is translation invariant, so `g` may be taken supported in `(0,L)`, and `Q_{0,L}[f] = W(f * f~)`. Conversely RH gives the sum-of-squares representation.)
2. The lower-bound half of Conjecture L — `lambda_min(L) >= e^{-C L e^L}` for all `L` — implies RH and is strictly stronger: it is a *quantitative* Weil positivity. The upper-bound half — `lambda_min(L) <= e^{-c e^L}` — is an unconditional statement about `Q_{0,L}` (interesting only under RH, and probably provable by the Slepian construction above, which uses only the count of zeros below `T_L`).
3. RH does not imply any rate by itself. But under RH the weak form looks provable: the upper bound by the construction in 3.3; the lower bound because a `PW_{L/2}` function that is small at all zeros must (Remez/Turán-type inequalities for entire functions of exponential type vanishing at `~ (1 - 1/L)` of the Nyquist number of points in `[-T, T]`) have most of its mass beyond `T`, where the zeros oversample and a Plancherel–Pólya inequality with Riemann–von Mangoldt density bounds returns a fixed fraction of the mass; the constants give `e^{-C L e^L}`. If that argument goes through, the weak form is equivalent to RH — an effective form of it — and only the sharp form (`theta`, `kappa`) says something RH does not.
4. In particular the conjecture is not a route to RH: its lower half contains RH, and what the numerics measure is the rate, i.e. the part beyond RH. Positivity for all `L` remains exactly as hard as before; the finite-horizon certificates are lower bounds for `L <= L_2` and, by the conjecture, should track `e^{-11.4 e^L + 17}` — a consistency check on certificate quality (the inserted `1e-33` at `L_q` was four orders below the ladder, the bisected `2.99e-29` sits on it).

## 4. What the two statements accomplish

**Barrier theorem.** (i) It turns the empirical dimension wall of storage-depth §6 into a theorem about certificate architecture, with the exact constant `lambda_max(T_L)` in place of the lower bound `rho^+_L`. (ii) It shows the wall is not a defect of Legendre heads, of the spatial split, or of the arithmetic norm bound (which is within 4 % of sharp): any finite-dimensional head and any separated complement bound hit it. (iii) It identifies the mechanism — Kronecker returns of the almost-periodic symbol, i.e. simultaneous Diophantine approximation of the `log p` — and hence what a certificate must do to pass it (keep pieces supported in `(0,L)`, resolve the middle band with prolates, Proposal C), together with the cost: `L = 4` with a redesign, `L = 5` at the edge, nothing beyond. (iv) It closes the question "can theory push the depth of *this* method": only by the redesign, and only to a horizon whose zero-height reach (`~ e^{2L}`) stays nine orders below what is verified.

**Ladder conjecture.** (i) It explains the ladder (factor `~ 20` per quarter step, factor `e^{11.4}` per integer) as the decay of a sampling constant governed by the height `2 pi e^L`. (ii) It proves, if true even in the weak form, that no uniform step lemma can exist: `lambda_min(L+h)/lambda_min(L) -> 0` for every fixed `h`, so the direct-floor recurrence must lose a factor `exp(-c h e^L)` per step and `||J_j||` must grow like `exp(c h e^{L_j}/2)`; the conditional continuation theorem's hypotheses are, as the paper says, Weil positivity itself. (iii) It reframes the finite-horizon numerics as measurements of a well-defined analytic quantity — the sampling constant of the zeros in `PW_{L/2}` — so the enclosures have scientific content independent of any progress on RH, and the certificate quality can be judged against the ladder. (iv) It connects the programme to sampling theory (Beurling–Landau, Seip), Slepian concentration, and de Branges/Krein spaces built on `xi`, where such constants are studied. (v) It gives sharp analytic targets: prove the upper bound under RH (constructive), prove the weak lower bound under RH (which would make the weak form an effective Weil criterion), and determine `theta` and `kappa`.

Neither statement helps prove RH. The barrier theorem says the certificates cannot go deep; the ladder conjecture says positivity gets exponentially more delicate with depth, which is why they cannot.

## 5. Cheap next steps

1. Ladder test: the planned step to `log 8` (weak test), then `log 11` if the recursion or a global rebuild reaches it (decisive). Record `lambda_min` estimates (ball Rayleigh quotients) at every horizon, including intermediate ones inside windows.
2. Replace `rho^+_L` by `lambda_max(T_L)` in storage-depth §6 (Galerkin lower bounds are rigorous in Arb; the weight argument gives upper bounds), and state Corollary B there; it also documents that the arithmetic weight bound has no slack worth pursuing.
3. Decide whether Proposal C (frequency-resolved certificate, `L = 4`) is worth a redesign; the numbers above say it is a method paper, not a zero-information paper.
4. Analytic: write out the Slepian construction for the upper bound of Conjecture L under RH and check its constant against `11.4`; then attempt the lower bound via Turán-type inequalities. Both are self-contained problems in Paley–Wiener theory.
5. Cheap diagnostic: compute the twisted-quotient function and the sub-band arithmetic tops at `L = 3, 4` with prolate bases (double precision) to confirm the 3.2–3.8 plateau and locate the first return that exceeds `g`; this decides the dense-head size for Proposal C.
