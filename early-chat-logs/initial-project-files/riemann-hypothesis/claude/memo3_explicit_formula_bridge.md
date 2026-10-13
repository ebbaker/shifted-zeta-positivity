# Memo #3 — The Explicit-Formula Bridge

*August 17, 2026. Continues `RH_program_synthesis.md` (memo 1) and `twistor_lift_computation.md` (memo 2).
Code: `lab/explicit_formula.py`; experiments reproduced by the session log; figure `bridge_results.png`.*

## 1. The certified explicit formula

Rotated coordinates throughout: $\rho = \tfrac12 + i\gamma$, zero multiset $\{\gamma\}$ closed under
$\gamma\mapsto-\gamma$ (functional equation) and $\gamma\mapsto\bar\gamma$ (reality). For $h$ even,
holomorphic in $|\mathrm{Im}\,r|\le\tfrac12+\varepsilon$, decaying, with
$g(u)=\tfrac{1}{2\pi}\int h(r)e^{-iur}dr$:

$$\sum_\gamma h(\gamma) \;=\; h(\tfrac i2)+h(-\tfrac i2)\;+\;\frac1{2\pi}\int_{-\infty}^\infty h(t)\Big[\mathrm{Re}\,\psi\big(\tfrac14+\tfrac{it}2\big)-\log\pi\Big]dt\;-\;2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n).$$

**Numerically certified** with the Gaussian-modulated family below: zero side (250 zeros) matches
pole + archimedean + prime side to $10^{-8}$–$10^{-10}$ at $(c,\lambda)\in\{(20,0),(20,1),(20,2),(20,3),(35,2)\}$, $\sigma=2$.

## 2. The linear building block

$$h_{c,\lambda}(r)=e^{i\lambda(r-c)}e^{-\frac{(r-c)^2}{2\sigma^2}}+e^{-i\lambda(r+c)}e^{-\frac{(r+c)^2}{2\sigma^2}},\qquad
Z(c,\lambda):=\sum_\gamma h_{c,\lambda}(\gamma).$$

Its prime side is a **Gaussian-windowed prime sum at scale $\log n\approx\lambda$**:
$g(u)=\tfrac{\sigma}{\sqrt{2\pi}}\big[e^{-iuc}e^{-\sigma^2(u-\lambda)^2/2}+e^{iuc}e^{-\sigma^2(u+\lambda)^2/2}\big]$,
so $Z(c,\lambda)$ is unconditionally computable from primes with $\log n\in[\lambda-O(1/\sigma),\lambda+O(1/\sigma)]$
plus explicit archimedean/pole terms. The frequency $\lambda$ *is* the logarithmic prime scale.

## 3. The quadratic form and the sphere anomaly

$\mathcal{Q}(c)=\int w(\lambda)|Z(c,\lambda)|^2 d\lambda$, or pointwise $|Z(c,\lambda)|^2$. Zero-side expansion:
diagonal + cross terms. **Diagonal anomaly lemma** (proved by direct computation): a real zero pair
$\{\pm a\}$ contributes to $|Z|^2$ a bounded oscillatory amount, uniformly in $\lambda$; a zero sphere
$(a,y_0)$ (quadruple $\pm a\pm iy_0$) contributes
$$2\cosh(2\lambda y_0)\,e^{-\frac{(a-c)^2-y_0^2}{\sigma^2}}\;+\;O(1),$$
i.e. **exponential growth in $\lambda$ at rate exactly $2y_0$**, weighted by the Gaussian distance of the
sphere's center from the window. Cross terms involving a sphere grow at most like $e^{\lambda y_0}$, so the
diagonal dominates. Consequently
$$\limsup_{\lambda\to\infty}\frac{\log|Z(c,\lambda)|}{\lambda}\;=\;\sup_\rho y_\rho\;=\;\Theta-\tfrac12,$$
($\Theta$ = supremum of real parts of $\zeta$ zeros), for every fixed window: **RH $\iff$ $Z(c,\lambda)$ grows
subexponentially in $\lambda$**, and the growth rate *reads off the largest sphere radius*.

**Numerics (real data).** With $\sigma=2$, $\lambda\le25$:

| zero set | $|Z|^2$ at $\lambda{=}25$ | fitted rate | true $y_0$ |
|---|---|---|---|
| $\zeta$ zeros (250, all real), $c=20$ | 3.2 | $-0.0003$ | 0 |
| same + implanted sphere $y_0=0.1$ | $4.7\cdot10^2$ | $0.0961$ | 0.1 |
| DH on-line zeros only (control), $c=85.7$ | 5.7 | $-0.009$ | 0 |
| **DH with its real sphere** | $2.1\cdot10^7$ | $\mathbf{0.3085}$ | **0.30852** |

(The implant fit is biased slightly low because $e^{2\lambda y_0}=e^5$ at the window edge barely clears the
oscillatory background; the DH sphere, with $e^{15.4}$, gives the rate to four digits.)

## 4. The graded decomposition of the anomaly

Verified to machine precision (Gegenbauer/Unsöld type):
$$\frac{\sinh(2z)}{2z}\;=\;\sum_{\ell\ge0}(2\ell+1)\,i_\ell(z)^2,$$
$i_\ell$ = modified spherical Bessel. So the sphere-anomaly kernel $\cosh(2\lambda y_0)$-type decomposes over
exactly the quaternionic $\ell$-sectors, with **modified** Bessel tags: the analytic twin of the unitary
sector family of the lab ($j_\ell\to i_\ell$; same $y_0^{2\ell}$ leading behavior at small radius, but
exponentially amplified once $\lambda y_0\gtrsim1$). The two graded families are the real and imaginary
slices of one complexified family — the same $j\leftrightarrow i$ Wick rotation that runs through the
quaternionic extension itself ($\cos(qu)$ on the sphere direction is $\cosh$).

## 5. The structural finding: two involutions

Why did the unitary sector energies resist a prime-side formula? Now answerable precisely. The zero
multiset carries two involutions: the **holomorphic** one $\gamma\mapsto-\gamma$ (i.e. $\rho\mapsto1-\rho$,
functional equation) and the **antiholomorphic** one $\gamma\mapsto\bar\gamma$ (i.e. $\rho\mapsto\bar\rho$,
reality — the real structure $\sigma$ of the twistor picture). The explicit formula computes sums of
functions *analytic* in $\gamma$ — it natively sees the holomorphic involution and is blind to the
antiholomorphic one. The unitary tags $j_\ell(\lambda y)e^{i\lambda a}$ are functions of the *conjugate pair*
$(\gamma,\bar\gamma)$ — e.g. $j_0(\lambda y)e^{i\lambda a}=\dfrac{e^{i\lambda\bar\gamma}-e^{i\lambda\gamma}}{-i\lambda(\gamma-\bar\gamma)}$, a divided
difference across the pair — i.e. **conjugate-paired sums** $\sum_\gamma F(\gamma,\bar\gamma)$, a class strictly
between Weil-linear and fully quadratic. The sharpest scalar instance:
$$\sum_\rho\frac{1}{\rho(1-\rho)}=2+\gamma_{\rm Euler}-\log4\pi\ \ (\text{computable — pairs by the functional equation}),\qquad
\sum_\rho\frac{1}{\rho\bar\rho}\ \ (\text{pairs by reality — not directly computable}),$$
and the termwise difference vanishes exactly on-line ($1-\rho=\bar\rho$) — it is a sphere detector. **RH is
the statement that the two involutions coincide on zeros** — the arithmetic-side restatement of the
twistor statement (memo 2) that the zero divisor is $\sigma$-invariant component-by-component. So Stage 3
has a name: *import the real structure into the explicit formula* — find identities for conjugate-paired
sums, or control the defect between the two pairings.

## 6. Honest accounting: what is new leverage vs. classical fact

At the crude exponential-rate level, §3 is a Gaussian-mollified form of the classical equivalence between
zero-free regions and prime-counting error ($\psi(x)-x\ll x^{\Theta+\epsilon}$): detecting a sphere of radius
$y_0$ via the growth of $Z$ requires windows $\lambda\gtrsim1/y_0$, i.e. primes up to $e^{1/y_0}$ — the
exponential wall is the old one, now with its geometry exposed (window length ↔ sphere radius; the lab
demo at $\lambda=25$ is zero-side; the prime-side at $\lambda=25$ would need $n\sim e^{25}\approx7\cdot10^{10}$ —
feasible; at $\lambda=40$, $n\sim10^{17}$ — the wall). The candidates for *genuinely new* leverage are below
the exponential scale:
1. **Graded positivity**: the $\ell$-decomposition (§4) splits the anomaly into a positive series; each
   truncation gives an inequality family interpolating between the Laguerre level ($\ell=1$, lab memo) and
   full Weil positivity. Whether the graded family has a better cone (test functions realizable from
   primes with controlled cross terms) than the classical Weil cone is the open question — it is *not* a
   relabeling of any inequality family we found in the literature.
2. **Cross-term structure**: $|Z|^2$'s off-diagonal is smoothed pair correlation; Montgomery's regime is
   the on-line part. A sphere contributes cross terms with a *coherent phase signature* ($e^{\pm\lambda y_0}$
   asymmetry) absent from GUE-like fluctuation — a matched-filter formulation ("sphere = coherent mode in
   the pair-correlation field") that may detect radii *below* the $\lambda\sim1/y_0$ wall statistically. Worth
   one focused attempt; failure modes informative.
3. **Conjugate-paired identities** (§5): any unconditional identity for $\sum F(\gamma,\bar\gamma)$ beyond
   trivial cases would be a new tool with consequences beyond this program.

## 7. Next steps

1. Prime-side computation of $|Z(c,\lambda)|^2$ up to $\lambda\approx23$ ($n\le10^{10}$, sieve in chunks) for a
   direct unconditional demonstration that the *prime side* reproduces the flat (no-growth) profile at
   $c=20$ — the first "sphere-free certificate from primes alone" at a real window. Cheap, satisfying.
2. Work out the cross-term calculus: expected size of off-diagonal $|Z|^2$ under (i) RH+GUE, (ii) RH only
   (unconditional bounds), to determine the minimal detectable radius at prime scale $e^\lambda$ — the
   quantitative form of the wall, and the precise gap any new idea must close.
3. Attempt the matched-filter/coherent-mode formulation (item 2 of §6).
4. Write up memos 1–3 + lab as the program paper draft; the two-involutions framing (§5) is its thesis.
