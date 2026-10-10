# Character-channel controls

26 September 2026. Prepared for Edward Baker by Claude (Anthropic). Model line: claude-fable-5-1 (Fable 5.1) per the runtime environment, session configured as claude-opus-5-5; the serving model may differ. Reasoning effort not exposed.

Floating diagnostics only; nothing here proves GRH, a limiting theorem, or positivity. They accompany the [research note](../notes/CHARACTER_CHANNELS_AND_THE_DIRICHLET_FAMILY_20260926.md).

## Program and records

- [`check_character_channels_family.py`](check_character_channels_family.py) — NumPy and SciPy (Si function for the exact angle moments); Part C also needs mpmath for Dirichlet $L$-functions. Run from this directory:

  ```sh
  OPENBLAS_NUM_THREADS=1 python3 -B numerics/check_character_channels_family.py --output /tmp/character-channels.json
  ```

  About 2.5 minutes with the cached zeros; `--refresh-zeros` recomputes them (about 25 minutes). `--part A|B|C` runs one part.
- [`records/character-channels-20260926.json`](records/character-channels-20260926.json) — 207 controls, all passing (Python 3.11.15, NumPy 2.4.4); script sha256 `e519756d…`.
- [`records/dirichlet-zeros-T320.json`](records/dirichlet-zeros-T320.json) — ordinates of the zeros of $L(s,\chi)$ up to height 320 for the six real primitive characters of conductor 3, 4, 5, 7, 8, found as sign changes of the real completed function $\Lambda(\tfrac12+it,\chi)$ on a grid of step 0.04 and refined by the secant method (mpmath, 15 digits); sha256 `720ae8a6…`. Counts against the main term of $N(T,\chi)$: 206/205.2, 220/219.8, 231/231.2, 248/248.4, 255/255.2, 255/255.2. First ordinates: 8.0397 ($\chi_{-3}$), 6.0209 ($\chi_{-4}$), 6.6485 ($\chi_5$), 4.4757 ($\chi_{-7}$), 4.9000 ($\chi_8$), 3.5762 ($\chi_{-8}$).

## Part A — character limits in the class sector (168 controls)

Multiplicative packets $M^\chi_R f$ (note, Definition 3.1) in the class sector with the Gram matrix $t_{n-m}-t_{n+m}$, for $q=5$ (real character $\chi_5$ and the character of order 4 with $\chi(2)=i$; opposite parity) and $q=7$ (the two cubic characters; same parity), $N = 1024, 4096$, windings $a = 2,\dots,7$, Haar and the five-harmonic marginal $\rho \propto 1+0.3\cos\theta+0.25\cos2\theta+0.1\cos3\theta-0.05\cos5\theta$. Each control compares a norm limit or a mixed winding pairing with Theorem 3.3 of the note, including the Gauss-sum ratio and the state Gram matrix $G_{\chi\chi'}$. Haar errors $\le 2.5\cdot10^{-13}$ at $N=1024$ and $\le 10^{-16}$ at $N=4096$; interacting-marginal errors $\le 5.2\cdot10^{-7}$ at $N=1024$ and $\le 3.3\cdot10^{-8}$ at $N=4096$ ($O(N^{-2})$). The cubic pair mod 7 mixes under the interacting marginal with $G = 0.07467 - 0.00474\,i$ (Haar: $1.6\cdot10^{-16}$); the opposite-parity pair mod 5 does not, as Corollary 3.5 predicts. $\bar\rho_5 = 0.9$, $\bar\rho_7 = 1.02857$.

## Part B — the class-sector archimedean insertion on character packets (3 controls)

For $\chi_{-3}$ and $\chi_5$ (Haar picture), $\langle M^\chi_R f, C M^\chi_R f\rangle/\|M^\chi_R f\|^2 - R$ with $C = \log D + B^*M_{\log(\theta/2\pi)}B$; the angle term is computed exactly through $\int_0^\pi\log(\theta/2\pi)\cos n\theta\cos m\theta\,d\theta = \tfrac12[J_{|n-m|}+J_{n+m}]$, $J_k = -\mathrm{Si}(k\pi)/k$. Results (note, Proposition 4.1):

| $\chi$ | $N=256$ | $N=1024$ | $N=4096$ | predicted $\langle f,xf\rangle/\|f\|^2 + \varphi(q)^{-1}\sum_j\log\frac{\min(j,q-j)}{q}$ |
|---|---|---|---|---|
| $\chi_{-3}$ | $-0.986902$ | $-0.986895$ | $-0.986895$ | $-0.986895$ ($= 0.111717 - \log 3$) |
| $\chi_5$ | $-1.151160$ | $-1.151148$ | $-1.151147$ | $-1.151147$ ($= 0.111717 + \tfrac12\log\tfrac{2}{25}$) |

Errors at $N=4096$: $2.8\cdot10^{-8}$, $4.9\cdot10^{-8}$. Control: the same code on the identity packet ($q=1$) at $N=1024$ reproduces the archimedean limit of the manuscript's Theorem 5.2 to $2.2\cdot10^{-16}$.

## Part C — the family Weil form against the zeros of $L(s,\chi)$ (36 controls)

$C_\chi(t) = Q_\chi(f_*,U_tf_*)$ from the definition (note, eq. (5.1): parity-dependent digamma multiplier plus $\log(q/\pi)$, twisted von Mangoldt sum; no pole term) versus $\sum_{\gamma>0}2|\hat f_*(\gamma)|^2\cos\gamma t$ over the cached zeros, for the manuscript's probe $f_*$:

| $\chi$ | $\kappa$ | $C_\chi(0)$ | max $|$definition $-$ zeros$|$ over $t\in\{0,\tfrac12,1,2,3,5\}$ |
|---|---|---|---|
| $\chi_{-3}$ | 1 | 76.6194850 | $1.3\cdot10^{-9}$ |
| $\chi_{-4}$ | 1 | 65.4898146 | $1.4\cdot10^{-9}$ |
| $\chi_5$ | 0 | 81.0067319 | $1.5\cdot10^{-9}$ |
| $\chi_{-7}$ | 1 | 131.6844109 | $1.6\cdot10^{-9}$ |
| $\chi_8$ | 0 | 140.5745130 | $1.6\cdot10^{-9}$ |
| $\chi_{-8}$ | 1 | 184.7891541 | $1.7\cdot10^{-9}$ |

The residual at $t=0$ is the weight of the zeros above height 320 (the crude envelope estimate in the record, $\approx10^{-6}$, is loose by three orders); it decreases at the other translates. A normalization error in the parity factor, the conductor term, or the sign of the twisted prime sum would appear at the $10^{-1}$–$10^{2}$ level. The $\zeta$ case ($q=1$) is the YM folder's `check_probe_against_zeros.py`.
