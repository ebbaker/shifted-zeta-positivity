# Adaptive EMA: corrected limiting lemmas and the L = 1/2 pilot

20 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex), the identity exposed by the system; a more specific deployment ID was not exposed. **Reasoning effort:** Extra High, as reported by Baker in this task; not independently read from runtime configuration. **Status:** bounded mathematical audit, full-output finite-input diagnostics, and one exact rational bound for a deliberately over-smoothed operator. No independent mathematical review, all-depth continuation, physical Wilson construction, localization theorem, or arithmetic Loewner driver.

## 1. Result and decision

The auxiliary EMA interpretations are mathematically controllable, but this pilot does **not** demonstrate a new positivity margin for the arithmetic transfer after accounting for the filter's contribution. The strongest useful outcome is a clarified set of lemmas and an explicit identification of the missing input-complement estimate.

- Output smoothing preserves the central real form on fixed smooth interior tests if `ell^2/omega -> 0`. The trace and fixed-window hypotheses matter. The two missing plus signs in the earlier note's (3.3) and (4.1) must be supplied. Full first operator variation needs the stronger `ell=o(omega)` condition.
- Input smoothing on **both** sides has an additional useful property: by causal commutation, **any** `ell -> 0` preserves the fixed-test central limit. No `ell^2/omega` condition is needed for this congruence. At fixed positive shift its all-input positivity is equivalent to the original question. This is the most defensible interpretation to retain as a numerical change of test space, although no computational speed or certification advantage has yet been established.
- Shift-path averaging has the stated limit only with correct initialization and normalization by the mean shift. Its positive output variance is measurable. At equal mean shift the unaveraged transfer was a better estimate of the finite central minimum in all 15 comparisons in the refined N=24 run. Averaging also weakens the high-frequency decay of the prime-free symbol.
- A complete norm calculation on 24 and 40 sine inputs is positive in every tested construction. These are restrictions in the **input**, with full output functions integrated over the target interval. Their positive minima do not bound the omitted input directions from below.
- An explicit rigorous complement bound is derived below. It becomes useless at the smaller shifts for every tested admissible output-removal schedule at these dimensions. The offending terms are proportional to `(N ell)^(-1/2)` and `(N ell)^(-1)`. This remains a failure even if the finite matrices were known exactly.
- To illustrate what an easy certificate can and cannot mean, exact rational arithmetic proves `||S V||^2 <= 0.987339385394 < 1` at `L=1/2, omega=1/10, ell=sqrt(omega)`. This is a certificate for an auxiliary operator at one deliberately contaminating schedule point. It supplies no certificate for the original transfer or for admissible removal.

**Single next calculation:** at this same L=1/2 and omega=0.001, obtain a rigorous bound for the omitted **input** directions of the original defect, retaining the signed pole cancellation, and compare it with the correctly weighted input-smoothed congruence. Use a low/high-frequency Schur complement of the defect, with an endpoint-adapted low block; test the explicit gamma EMA tail estimate in Section 9 as part of the high-block analysis. This retains the mixed block instead of requiring the transfer itself to be tiny on the complement. Do this before crossing log 2 or attempting spatial continuation.

## 2. Inputs, preservation, and the exact arithmetic target

This audit starts from the [continuation note](EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md), treating its new derivations as claims. That original note and its numerical record are preserved. This note supplies its corrections and extensions.

Local sources consulted:

- Wilson–Loewner v0.4 [main Section 5](../../wilson-loewner/sections/05_fixed_window.tex), [SI S10](../../wilson-loewner/sections/s_fixed_window.tex), [SI S11](../../wilson-loewner/sections/s_localization.tex), [SI continuation](../../wilson-loewner/sections/s_continuation.tex), and [shift evolution](../../wilson-loewner/sections/03_shift_evolution.tex).
- The [shared background](../../../background_section.tex), especially its right-Laplace-line derivative bounds.
- Parent Loewner [decomposition](../../loewner/sections/03_decomposition.tex), [registered assembly discussion](../../loewner/notes/REGISTERED_ASSEMBLY_AND_THE_HORIZONS_20260918.md), and [transfer/Weil-form assembler](../../loewner/numerics/check_contraction_margin.py).

For `0 < L < log 2` the complete finite-window transfer is convolution by

\[
 k_\omega=h_\omega-2\omega e^{(1/2-\omega)\cdot}*h_\omega,
 \quad
 h_\omega(t)=\frac{(2\pi)^\omega}{\Gamma(\omega)}
 t^{\omega-1}\left(\frac{\sinh t}{t}\right)^{\omega-1}e^{-3t/2}.
 \tag{2.1}
\]

Its right-half-plane symbol is

\[
 K_\omega^<(p)=\pi^\omega
 \frac{\Gamma((p+5/2-\omega)/2)}{\Gamma((p+5/2+\omega)/2)}
 \frac{p-1/2-\omega}{p-1/2+\omega}.
 \tag{2.2}
\]

The computation actually reuses the parent's equivalent original kernel
`kGamma - 4 omega b J_{-b} - 4 omega a J_a`, with both pole terms. Equation (2.1) is an independent evaluation check and supplies the bound in Section 8. No contact term or gamma tail is tuned away. The independent central matrix uses the parent's full `WeilForm`, including the local constant and poles. On this interval the absorbed generator is

\[
 G_0=(w_0+4)I+\sum_{n=1}^\infty\frac2{a_n}(I-S_{1/a_n})+2R_{-1/2},
 \quad a_n=2n+\tfrac12,
\]
\[
 w_0=-\gamma-\pi/2-3\log2-\log\pi,
 \qquad R_{-1/2}f(x)=\int_0^x e^{(x-y)/2}f(y)\,dy.
 \tag{2.3}
\]

The gamma and beta identities are consistent with the primary references [DLMF 5.9](https://dlmf.nist.gov/5.9) and [DLMF 5.12](https://dlmf.nist.gov/5.12). All operator estimates below are derived here from the stated kernels.

The arithmetic factorization `k = khat - 2 S_{1/b} khat`, `b=1/2+omega`, is a **different** EMA. Its rate is fixed by cancellation of the growing `exp(bx)` component. Replacing it with rate c leaves a growing coefficient `(b-c)/(b+c)`. The built-in length tends to 2, not zero. Every adjustable ell below belongs to an additional smoother; neither the internal pole cancellation nor the fixed local normalization changes.

## 3. Energy, boundary conditions, and the removal lemma

### 3.1 Exact energy identity

On H=`L^2(0,L)` let

\[
 S_\ell f(x)=\ell^{-1}\int_0^x e^{-(x-y)/\ell}f(y)\,dy.
\]

For every complex L2 input, h=S_ell f belongs to H1, has trace h(0)=0, and satisfies `f=h+ell h'` almost everywhere. Conversely that equation and trace uniquely determine h. Expanding the square and using the H1 integration-by-parts identity gives

\[
 \boxed{\|f\|^2-\|h\|^2=\ell^2\|h'\|^2+\ell|h(L)|^2.}
 \tag{3.1}
\]

The plus sign between the terms is missing in the continuation note's displayed (3.3). No differentiability of f is required for (3.1). Both endpoint traces of h exist. With an inherited initial state h(0)=z, the correct identity instead is

\[
 \|f\|^2+\ell|z|^2=\|h\|^2+\ell^2\|h'\|^2+\ell|h(L)|^2.
 \tag{3.2}
\]

Thus zero history is part of the contraction statement. Dividing the kernel by `1-exp(-x/ell)` changes the operator and this balance.

The resolvent `S_ell=(I+ell d/dx)^(-1)` on H1 with zero left trace is a contraction, is compact at positive ell, and tends strongly to I. Norm convergence to I is impossible: I minus a compact operator has essential norm 1. The resolvent identity in the continuation note correctly proves monotonic decrease of every filtered norm as ell increases.

For `W=S_ell V`, the other missing plus sign, in its (4.1), is essential:

\[
 \boxed{I-W^*W=(I-V^*V)+V^*(I-S_\ell^*S_\ell)V.}
 \tag{3.3}
\]

The second term is precisely filter storage, not arithmetic storage.

### 3.2 Regularity and traces of the evolving input

Fix a **finite** interval (0,R) and f in `C_c^infinity(0,R)`. Put `g_omega=V_{omega,R}f`. Here is the missing regularity argument in a form that specifies what it uses. On a fixed Laplace line `p=sigma+i t`, sigma>1, the absolutely convergent zeta series, rational factors and gamma-ratio estimates give, uniformly for small nonnegative omega,

\[
 |\partial_\omega K_\omega(\sigma+it)|\le C_\sigma(1+\log(2+|t|)).
\]

Multiplying by the transform of the zero extension F gives

\[
 \int_{\mathbb R}(1+t^2)(1+\log(2+|t|))^2
 |\widehat{e^{-\sigma x}F}(t)|^2\,dt<\infty.
 \tag{3.4}
\]

Weighted Plancherel and integration in omega now prove, on (0,R),

\[
 \|g_\omega-f\|_{H^1}=O_{f,R}(\omega).
 \tag{3.5}
\]

The factor for converting the weighted norm to the local unweighted norm depends on R. We do not bound it uniformly as R grows. Causality makes g identically zero before the input begins, so its left trace vanishes. Continuity of the H1 trace map and f(R)=0 give `g_omega(R)=O(omega)`.

Condition (3.4), together with zero endpoint traces, is a sufficient larger test class. Merely saying f is in H1 is insufficient to obtain (3.5) from this multiplier argument. The sine inputs used below satisfy (3.4): their zero extensions lie in `H^(1+epsilon)` for every `epsilon<1/2`. Thus the numerical inputs are covered even though they are not interior compactly supported smooth functions.

### 3.3 Quantitative removal

For any g in H1 with g(0)=0, differentiation gives `(S_ell g)'=S_ell g'`, and

\[
 S_\ell g(R)=g(R)-\ell(S_\ell g')(R),\qquad
 |\ell(S_\ell g')(R)|\le\sqrt{\ell/2}\,\|g'\|.
\]

Use contraction on g' and the square bound in (3.1):

\[
 0\le\|g\|^2-\|S_\ell g\|^2
 \le 2\ell^2\|g'\|^2+2\ell|g(R)|^2.
 \tag{3.6}
\]

For the evolving fixed test this is `O_f,R(ell^2+ell omega^2)`. Consequently

\[
 \ell^2/\omega\longrightarrow0
 \quad\Longrightarrow\quad
 \frac{\|f\|^2-\|S_\ell V_\omega f\|^2}{2\omega}
 \longrightarrow Q_0[f].
 \tag{3.7}
\]

This implication entails ell->0 and ell omega->0. It is a fixed-test statement, not uniform on the L2 unit sphere or on a growing-dimensional test space.

The endpoint assumptions cannot be removed silently. If g(0)=0 but g(R) is fixed nonzero, the loss is generally order ell at the right endpoint. For f=1, direct integration gives
`||1||^2-||S_ell 1||^2 = 2 ell(1-e^(-R/ell)) - (ell/2)(1-e^(-2R/ell)) ~ 3 ell/2`.
Thus ell^2=o(omega) alone would not control that test. Initial-history errors likewise require their own estimate.

For smooth interior f, at the threshold `ell/sqrt(omega)->c`, one can sharpen the calculation to

\[
 \frac{\|V_\omega f\|^2-\|S_\ell V_\omega f\|^2}{2\omega}
 \longrightarrow\frac{c^2}{2}\|f'\|^2.
 \tag{3.8}
\]

Indeed `(S g)'->f'` in L2. To control the endpoint more sharply, split `g'=f'+O(omega)` in L2, use bounded f', and obtain `ell|Sg(R)|^2=O(ell omega^2+ell^3+ell^2 omega^2)`. Dividing by omega makes this vanish in the threshold regime. The threshold therefore contaminates the limiting form for every nonconstant such test.

### 3.4 Growing intervals require a fixed smaller interval

Suppose all-input contractions of `S_{ell_j,L_j}V_{omega_j,L_j}` were established with `L_j->infinity`, `omega_j->0`, and `ell_j^2/omega_j->0`. Fix f in `C_c^infinity(0,R)`, extend it by zero to every larger interval, and restrict the output to (0,R). Causality identifies this restriction with `S_{ell_j,R}V_{omega_j,R}f`. Its norm is no larger than the full contracted output norm. Now apply (3.7) with R fixed. No uniform H1 or trace constant in L_j is required. Translation handles arbitrary compact supports. This conditional implication survives the audit; the hypotheses are not constructed here.

## 4. Real forms, full variations, and the stronger input lemma

On a fixed smooth test,

\[
 S_\ell V_\omega f=f-\omega G_0f-\ell f'+o(\omega)+o(\ell).
 \tag{4.1}
\]

This follows from `Sg=g-ell Sg'`, (3.5), and strong convergence of S on f'. Therefore `ell=o(omega)` preserves the full first vector derivative. If `ell/omega->c`, the derivative becomes `-G_0f-c f'`. Its real pairing with an interior test is unchanged because `Re <f,f'>=0`. If ell/omega->infinity and f' is nonzero, the vector difference quotient diverges in norm after its leading `-ell f'` term. The schedules `omega^(3/4)`, `omega`, and `omega^(5/4)` all preserve the real form; only the last preserves the full variation. This does not produce a physical transfer match.

For input smoothing, define

\[
 d^{\rm in}_{\omega,\ell}[f]=\|S_\ell f\|^2-\|V_\omega S_\ell f\|^2.
\]

**Input-removal lemma.** If `V_omega f=f+omega A f+o(omega)` on a fixed test, causal convolution commutes with S, and ell(omega)->0, then

\[
 d^{\rm in}_{\omega,\ell}[f]/(2\omega)\longrightarrow-\Re\langle f,Af\rangle.
 \tag{4.2}
\]

**Proof.** Write `r_omega=(V_omega-I)f/omega -> Af`. Exactly,

\[
 \frac{d^{\rm in}_{\omega,\ell}[f]}{2\omega}
 =-\Re\langle S_\ell f,S_\ell r_\omega\rangle
   -\frac\omega2\|S_\ell r_\omega\|^2.
\]

Contraction and strong convergence of S suffice. This avoids assuming form-norm convergence for arbitrary varying tests. It gives Q0 with A=-G0. Division additionally by `||S_ell f||^2` gives the normalized limit for nonzero f. Even the output-contaminating schedule sqrt(omega) is admissible for this **two-sided** comparison.

At each fixed positive omega, `S* D S >= 0 iff D >= 0` follows from the dense range `ran S={h in H1:h(0)=0}` and boundedness of D. However S* D S is compact, so in infinite dimension it cannot have a strictly positive lower bound against the original input norm, even if D is coercive. Numerics must use its natural metric `S* S`, not treat smaller unnormalized defects as better bounds. Changing to finitely many smoothed inputs also changes the tested subspace.

For increasing support, all-input positivity of this congruence first implies original contraction by dense range; then apply original causal restriction. Simply restricting **both** smoothed norms would not by itself preserve their difference, since input tails are discarded as well.

## 5. Shift-path averaging: initialization, clock, and variance

Let V0=I, and let mu_epsilon be probability measures on `[0,epsilon]`, with positive mean m and epsilon->0. For a fixed smooth f write

\[
 V_s f=f+sAf+r_s,\qquad \|r_s\|\le s\eta_f(\epsilon),\quad\eta_f(\epsilon)\to0.
\]

Bochner integration (or strong integration on each input) gives

\[
 \overline V f=f+mAf+\bar r,\quad \|\bar r\|\le m\eta_f(\epsilon),
\]
\[
 \frac{\|f\|^2-\|\overline V f\|^2}{2m}\longrightarrow Q_0[f].
 \tag{5.1}
\]

Local uniform boundedness of V suffices for the integrals; no operator-norm continuity at s=0 is assumed. No positive lower bound on m/epsilon is required analytically. Numerical errors must be o(m), so very small means are costly.

The initialization rules in the earlier note are correct, with these qualifications:

- For constant tau>0 and initial value I, `bar V=e^(-omega/tau) I + int_0^omega e^(-(omega-s)/tau) V_s ds/tau`. The atom at zero is **I**, and `m=omega-tau(1-e^(-omega/tau)) ~ omega^2/(2tau)`. The defect divided by 2omega tends to zero on smooth tests. Initializing at zero instead destroys this limit. More generally a wrong initial operator B contributes `e^(-omega/tau)(B-I)f`; it must be o(m) for the vector argument to survive.
- The differential equation with `tau(omega)=c omega` has the unique bounded solution with strong limit I
  `bar V=(1/c) omega^(-1/c) int_0^omega s^(1/c-1) V_s ds`, and `m=omega/(1+c)`. The homogeneous term proportional to `omega^(-1/c)` is excluded by bounded initialization. Substituting c omega into the **constant-tau solution formula** would be a different operator.
- With a fixed positive tau the identity atom remains at positive omega, preventing exact equality to compact V_omega. With c omega there is no atom and the average is compact (truncate the small s tail in operator norm). Its derivative is `-G0/(1+c)`; only the first derivative is corrected by the mean clock, not the complete finite transfer.

Shrinking history means more than the probability mass concentrating near zero. For example `(1-delta) delta_0 + delta delta_{s0}` has mean delta s0->0 and almost all mass at zero, but its normalized first response is `(V_{s0}-I)/s0`, not A. A sufficient extension beyond shrinking support is uniform boundedness on a fixed shift interval, the local expansion above, and

\[
 \int_{s>\eta}s\,d\mu(s)=o(m)\quad\hbox{for every fixed }\eta>0.
 \tag{5.2}
\]

On a bounded shift interval these hypotheses control the relative remainder; a corresponding second-moment condition `int s^2 dmu=o(m)` follows. A chronological EMA descending from shift 1/2 must verify such relative-history estimates, including its initial state. Vanishing old probability alone is inadequate. The same mu must be used under interval restriction.

Exactly, for every input,

\[
 I-\bar V^*\bar V=\int(I-V_s^*V_s)\,d\mu(s)
 +\int(V_s-\bar V)^*(V_s-\bar V)\,d\mu(s).
 \tag{5.3}
\]

No adjoints or products are commuted in this identity. On a fixed smooth test the variance is at most `C_f int s^2 dmu <= C_f epsilon m`, hence disappears after division by 2m. Averaged transfers and averaged defects share a central limit but differ at finite shifts. Neither is a contraction principle for arbitrary expanding families.

There is also a high-frequency cost specific to the prime-free target. Put beta=1/c and fix omega>0. The uniform gamma-ratio asymptotic on a right vertical line gives `K_s^<(p)=(2pi/p)^s(1+O(1/|p|))` for `0<=s<=omega`. Integrating the density `beta s^(beta-1)/omega^beta` yields

\[
 \overline K_\omega^<(p)\sim
 \frac{\Gamma(1+\beta)}{[\omega\log(p/(2\pi))]^\beta},\qquad |\Im p|\to\infty.
 \tag{5.4}
\]

To verify it, extend the exponential integral in s to infinity; its main term is `Gamma(beta) log(p/(2pi))^(-beta)`, and the omitted fixed-upper-end tail is exponentially smaller in the real part of that logarithm. The gamma-ratio error is uniform over the compact s interval. This is a derived consequence of [DLMF 5.11(iii)](https://dlmf.nist.gov/5.11#iii). It concerns the prime-free right-line symbol, not an unweighted whole-line zeta multiplier. Averaging thus replaces a power decay at fixed positive shift by inverse-logarithmic decay. It should not be presumed to improve a high-frequency complement estimate.

## 6. Pilot design and complete output accounting

The [pilot program](../numerics/adaptive_ema_pilot.py) imports the existing parent `Kernel`, `kernel_nodes`, `transfer_matrix`, and `WeilForm`. It accelerates the same Golub–Welsch recurrence with NumPy and vectorizes `Kernel.Ghat`. Tests compare the vectorized kernel to the original scalar method, to (2.1), and compare integrated matrix entries to the parent's assembler. All arithmetic factors and the `n=1` comb atom remain; no later atom can act at L=1/2.

Inputs are the first N orthonormal sines `e_j=2 sin(2 pi j x)`, N=24 and 40. The program evaluates

\[
 (V_\omega f)(x)=x^\omega\int_0^1v^{\omega-1}\widehat G_\omega(xv)f(x(1-v))\,dv
\]

at output quadrature nodes throughout (0,L). It integrates products of these full functions to form the output Gram matrix. No `P_N V f` replaces V f. The full interval here is the output space of the compressed target V; no infinite-line norm is substituted.

For sine inputs the auxiliary filter is evaluated exactly before applying V:

\[
 S_\ell\sin(kx)=\frac{\sin(kx)-\ell k\cos(kx)+\ell k e^{-x/\ell}}{1+(\ell k)^2}.
\]

Causal commutation makes this **exactly** the output-filtered function as well. Its derivative and endpoint give a second evaluation of the filter storage. The two input/output comparisons consequently share complete outputs but use different input metrics.

The shifts are `0.1, 0.03, 0.01, 0.003, 0.001`. Schedules are `ell=omega^0.75, omega, omega^1.25`, and the contaminating `ell=sqrt(omega)=2L sqrt(omega)`. Path EMAs use `c=0.5,1,2`; records include m, the averaged defect, output variance, and original V_m for an equal-clock comparison. For every row the tests include e1, e8, eN, the central matrix's weakest direction and the original finite-shift defect's weakest direction.

There are three runs: N=24 with output/delay/inner/path orders `(48,64,24,8)`, refined N=24 `(72,96,32,12)`, and N=40 `(96,128,32,12)`. Output quadrature uses five panels with edges `L*(0,0.0001,0.001,0.01,0.1,1)`. This resolves the left endpoint without discarding it. The largest checked N=24 normalized refinement difference is `2.383e-9`. In the refined N=24 run the full filter-energy matrix residual is at most `1.53e-14`; the absorbed-kernel check is below `7e-17`, and the parent projected-entry check below `8e-15`. These are floating refinements and identities, **not rigorous quadrature enclosures**.

The 57 earlier EMA diagnostics were replayed successfully without overwriting their record. Full parameters, versions, timings, scalar controls, and checks are in the [pilot record](../numerics/records/adaptive-ema-pilot-20260920.json).

### 6.1 The original central scale and output projection error

| omega | N=24 full-output minimum / 2omega | N=40 full-output minimum / 2omega |
|---:|---:|---:|
| 0.1 | 0.03540103156 | 0.03460184281 |
| 0.03 | 0.03575534188 | 0.03482717702 |
| 0.01 | 0.03592454874 | 0.03494947345 |
| 0.003 | 0.03599200861 | 0.03499938566 |
| 0.001 | 0.03601210249 | 0.03501435713 |
| central matrix | 0.03602228812 | 0.03502196336 |

Increasing the input dimension lowers the apparent minimum by about 0.001; that unresolved input effect is much larger than the refined quadrature differences. At omega=0.1, projecting the output back to the N=24 input space would add `0.000849341688` to the normalized defect **on its actual weakest direction**. At omega=0.001 it would still add `0.000011182721`, comparable to the original finite-shift error in the central estimate. Complete output accounting is consequential even here.

The oscillatory controls also converge to their independent central values: at omega=0.001 the normalized defects on e1, e8 and e24 are `0.04982182, 2.01569602, 3.14757420`, versus `Q=0.04984481, 2.01981606, 3.15754181`. The central limit is a fixed-test limit; higher frequencies have larger errors.

### 6.2 Output smoothing and the two-sided input comparison

At omega=0.001 in the refined N=24 run:

| ell schedule | ell^2/omega | output minimum / 2omega | after subtracting full filter energy | two-sided input minimum, relative to S* S, / 2omega |
|---|---:|---:|---:|---:|
| omega^0.75 | 0.0316228 | 0.66153238 | 0.03601210 | 0.03622996 |
| omega | 0.001 | 0.06029474 | 0.03601210 | 0.03601850 |
| omega^1.25 | 0.0000316228 | 0.03694115 | 0.03601210 | 0.03601258 |
| sqrt(omega) | 1 | 17.16009722 | 0.03601210 | 0.03694343 |

Subtraction is performed on the full matrices **before** taking their minimum eigenvalues. Subtracting two unrelated minimum eigenvalues would not be valid. On e1, for example, the admissible omega^0.75 schedule adds `0.61641860` to an arithmetic value `0.04982182`: asymptotic admissibility does not imply small finite-shift contamination.

The two-sided column uses the generalized eigenvalue problem for `(S*DS,S*S)`. It compares a different finite test subspace, ran(S P_N), so its increase over the original column is not an improvement of an all-input lower bound. The original defect is already positive on the tested inputs. No recovered arithmetic margin or reduction in normalized error is attributable to the added output filter after exact loss subtraction.

### 6.3 Shift averaging at equal mean shift

For c=1 (uniform history), omega=0.001, m=0.0005, N=24:

| quantity | normalized minimum |
|---|---:|
| original V_omega, divide by 2omega | 0.03601210249 |
| original V_m, divide by 2m | 0.03601718371 |
| averaged defect, divide by 2m | 0.03601549129 |
| defect of averaged transfer, divide by 2m | 0.03604563175 |
| central matrix | 0.03602228812 |

The output variance matrix has norm `0.001032002625` after division by 2m. Its contribution to any particular direction must be evaluated in that direction; the difference of the two minima is not a variance eigenvalue. The average-transfer minimum has crossed above the central value, while original V_m is closer. Across c=0.5,1,2 and all five shifts, original V_m is closer to this finite central minimum than either averaged estimator. The averaging costs 8 or 12 transfer evaluations per c and provides no demonstrated estimate or speed advantage in this pilot. This is a finding on these data, not an impossibility theorem for averaging.

## 7. Expanding control and false positivity

For the nonarithmetic `V_omega=exp(omega) I`, the exact original and input-relative normalized defects are both

\[
 (1-e^{2\omega})/(2\omega)\to-1.
\]

Uniform-history transfer averaging also expands: its multiplier is `(exp(omega)-1)/omega>1`, so its normalized defect remains negative. At omega=0.00001 the refined e1 results are:

| schedule | output-smoothed normalized defect | after exact loss subtraction |
|---|---:|---:|
| omega^0.75 | -0.93761017 | -1.00001000 |
| omega | -0.99981261 | -1.00001000 |
| omega^1.25 | -1.00000938 | -1.00001000 |
| sqrt(omega) | +18.60705808 | -1.00001000 |

Since e1 is unit norm with derivative norm squared 4pi^2, the last limit is `-1+2pi^2=18.7392088...`, exactly (3.8). The admissible schedules return to -1. At moderate shifts even an admissible schedule can mask expansion; it is the limiting rate that distinguishes them.

The earlier all-input toy bound also checks the effect without any finite matrix:

\[
 \|S_\ell\|^2\le\frac1{1+2\ell^2/L^2},\qquad
 \|S_{\sqrt\omega}e^\omega I\|^2\le\frac{e^{2\omega}}{1+8\omega}<1
 \quad(0<\omega\le0.1).
\]

The Poincare estimate used here is elementary: `||h||^2<=L^2||h'||^2/2` for h(0)=0. Thus false positivity is present even at the **all-input** level if output smoothing is removed too slowly.

## 8. Rigorous bounds and the exact obstruction to certification

### 8.1 A complete-kernel majorant and a genuine, limited certificate

For `0<omega<=1/2`, (2.1) and `sinh(t)/t>=1` give

\[
 \int_0^L h_\omega(t)dt\le M_h:=\frac{(2\pi L)^\omega}{\Gamma(1+\omega)},
\quad
 \|k_\omega\|_{L^1(0,L)}\le C_\omega:={ (2\pi L)^\omega\over\Gamma(1+\omega)}
 [1+2\omega L e^{(1/2-\omega)L}].
 \tag{8.1}
\]

Young's inequality bounds ||V|| by C_omega. It is deliberately conservative because it takes absolute values after preserving the pole contribution. Together with the preceding Poincare bound it proves

\[
 \|S_\ell V_\omega\|^2\le C_\omega^2/(1+2\ell^2/L^2).
 \tag{8.2}
\]

For L=1/2, omega=1/10, ell^2=1/10, logarithmic convexity of Gamma gives `Gamma(1+omega)>=exp(-gamma omega)`. Using `pi<22/7`, `gamma<H_1000-log(1000)`, and rational series bounds for log and exp yields

\[
 \|S_\ell V_\omega\|^2
 \le \frac{987339385394}{10^{12}}<1.
 \tag{8.3}
\]

The [certificate program](../numerics/certify_ema_coarse_bound.py) makes the final comparisons in exact Python Fraction arithmetic; its [small record](../numerics/records/ema-coarse-certificate-20260920.json) gives the outward rational bound. This certificate applies to all L2 inputs and retains the complete arithmetic kernel. It establishes only this broadly filtered contraction. Here ell^2/omega=1, and the same schedule contracts the expanding toy; it cannot be used in the central implication (3.7).

### 8.2 An explicit omitted-input bound

Let P_N project onto the first N sines. For any g in H1 with g(0)=0, integration by parts in each sine coefficient and Bessel's inequality for its derivative in the cosine basis give

\[
 \|(I-P_N)g\|
 \le\frac{\sqrt{2L}}{\pi\sqrt N}|g(L)|
   +\frac L{\pi(N+1)}\|g'\|.
 \tag{8.4}
\]

The same estimate applies to g(L)=0 with the other endpoint. Indeed the boundary coefficients have squared tail bounded by `2L |g(L)|^2/(pi^2 N)`, and the derivative coefficients have squared tail bounded by `L^2 ||g'||^2/(pi^2(N+1)^2)`. This accounts for the output endpoint that a sine projection misses.

For `W=S_ell V`, its convolution kernel w is in L2 and

\[
 \|w\|_2\le C_\omega/\sqrt{2\ell},\qquad
 \|W'\|\le2C_\omega/\ell.
\]

The first follows by convolving the L1 kernel k with the L2 EMA kernel. The second follows from `ell W'=V-W`. Reflection gives the corresponding adjoint derivative bound; W* f has right trace zero and left trace bounded by `||w||_2 ||f||`. Applying (8.4) to W* and taking adjoints proves the **all-input** estimate

\[
 t_N:=\|W(I-P_N)\|
 \le C_\omega\left[\frac1\pi\sqrt{\frac L{N\ell}}
              +\frac{2L}{\pi(N+1)\ell}\right].
 \tag{8.5}
\]

It may be capped by `C_omega/sqrt(1+2ell^2/L^2)`. If a_N is a rigorous upper bound for ||W P_N||, then

\[
 \|W\|\le\sqrt{a_N^2+t_N^2}.
 \tag{8.6}
\]

This follows by decomposing an arbitrary unit input, bounding the two outputs, and applying the scalar Cauchy–Schwarz inequality. No block orthogonality is assumed.

At omega=0.001 and N=24 the capped t_N values for the three admissible schedules are all about 1.003. Combining them even with the **diagnostic** finite-block norms gives upper estimates between 1.4158 and 1.4164, far above 1. The finite defect would allow t_N only approximately `0.0364, 0.0110, 0.00860` for powers `0.75,1,1.25`, respectively. N=40 does not close the estimate. Therefore the omitted-input bound, not numerical noise, blocks certification at the small shifts.

For a margin of order omega, this sufficient estimate would require its first term to be o(sqrt(omega)), hence at least `N ell omega -> infinity`, as well as control of the derivative term. Fixed N cannot meet this under removal. This is a limitation of this estimate, not a necessary complexity theorem for every method. Replacing sines by an endpoint-adapted representation could remove the first term; the derivative bound still grows as ell shrinks.

At some broader, larger-shift points the diagnostic finite block plus (8.5) is below 1 (for example ell=omega at omega=0.1). Those are **not** certificates: a rigorous quadrature/eigenvalue enclosure for a_N is still missing. Only the rational result (8.3), which bypasses the finite block, is certified here.

### 8.3 Explicit approximation bounds also expose the filter's cost

For a fixed sine-space f with zero endpoints, differentiation commutes with V, so `||g'||<=C_omega ||f'||`. Also `|f(L-t)|<=t||f'||_infinity`. Applying (2.1) gives

\[
 |g(L)|\le\omega\|f'\|_\infty M_h
 [L/(1+\omega)+2L^2e^{(1/2-\omega)L}].
 \tag{8.7}
\]

Equations (3.6), (8.1), and (8.7) are a rigorous explicit bound for the added filter loss. For unit f in the first N sines, use `||f'||<=pi N/L` and `||f'||_infinity<=sqrt(2/L)(sum_{j<=N}(pi j/L)^2)^(1/2)`. The program records this bound separately from the measured loss. At omega=0.001, N=24, ell=omega^1.25 the resulting normalized uniform loss bound is about 0.9032, already much greater than the detected arithmetic minimum 0.0360. Exact measured subtraction works numerically, but this coarse uniform subtraction cannot certify a new margin.

These are analytic inequalities with explicit constants. Except for (8.3), their decimal evaluations and all finite matrix values in the pilot are binary64 diagnostics. No claim of directed rounding or interval quadrature is made.

## 9. What merits continuation, and what must remain visible

Input smoothing on both sides merits further work as a change of test space because (4.2) removes a rate restriction and dense range preserves the exact positivity question. The pilot gives no license to call its finite generalized eigenvalues operator lower bounds. Output smoothing remains a possible auxiliary positivity route only if a substantially sharper complement bound and an admissible removal schedule can be proved together. The measured extra margin itself is accounted for by filter energy. Shift averaging has a correct mean-clock limit, but this pilot shows neither better central estimates at equal clock nor faster evaluation; (5.4) adds a reason to be cautious about its complement.

The inherited gamma EMA representation may help calculate the next rigorous complement without changing the transfer. For f in H1 with zero left trace,

\[
 \left\|\sum_{n>M}\frac2{a_n}(I-S_{1/a_n})f\right\|
 \le 2\|f'\|\sum_{n>M}a_n^{-2}
 \le\frac{\|f'\|}{2M+1/2}.
 \tag{9.1}
\]

The last inequality is the integral test. It is a core/derivative estimate, not a uniform bound on unrestricted high-frequency inputs. The negative local coefficient, remaining growing exponential, and subsequent arithmetic delays still have to be estimated with their signs. A finite EMA tower cannot simply replace the logarithmic generator on all of L2.

Any eventual construction must still establish unbounded support length, vanishing shift, and the appropriate smoothing removal. For output smoothing that includes `ell_j^2/omega_j->0` on every fixed smaller interval; full first-variation matching requires more. Path averages must lose old shifts relative to their mean, and use compatible measures under spatial restriction. For input congruences use all-input dense-range equivalence before restricting intervals.

EMA memory must also cross a spatial join. If the old length is L and a new slab has coordinate z, the filter's cross block is

\[
 (Bf)(z)=e^{-z/\ell}(S_{\ell,L}f)(L).
\]

Consequently for arithmetic blocks `(X,0;Y,Z)` the new filtered cross block is **BX+CY**, not CY. Resetting the EMA deletes stored state and changes the global operator. The stored endpoint terms in (3.2) cancel at a constant-ell join only when that state is carried. Changing ell between steps changes the old block too. For a spatially varying length, the additional bulk term `-int ell'(x)|h(x)|^2 dx` remains; arbitrary adaptation is not automatically contractive. The cumulative Schur test must keep the new slab's **output** defect and signed parameter changes.

Nothing here assumes a Wilson realization, a localizing charge, a physical origin for the EMA states, or a Loewner driver. Wilson–Loewner version 0.4 and all manuscript snapshots remain the baseline. This bounded audit ends before the first-delay experiment and before all-depth continuation.

## 10. Reproduction and records

From the repository root, with Python 3 and NumPy:

```sh
OPENBLAS_NUM_THREADS=1 python3 papers/susy-positivity/investigations/critical-path/numerics/adaptive_ema_pilot.py
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_coarse_bound.py
python3 papers/susy-positivity/investigations/critical-path/numerics/check_ema_controls.py
```

The pilot requires NumPy only; the rational certificate and earlier controls use the standard library. The recorded run used Python 3.10 and NumPy 1.25.1. The pilot's three runs took approximately 3, 10, and 23 seconds on this host; these are reproducibility data, not a controlled timing comparison of smoothing methods. The persisted record contains scalar summaries and weak-vector coefficients, not regenerable large matrices.

The [audit provenance record](../numerics/records/adaptive-ema-audit-provenance-20260920.json) hashes the note, scripts, records, source inputs, and preserved v0.4 baseline. Hashes identify files; they do not certify mathematics. Existing uncommitted research and manuscript files were checked against their pre-task hashes, with only the specifically listed index files intentionally updated. The earlier `RESEARCH_RECORD.json` remains a historical record of the prior session; its index hashes refer to that earlier index state. All new files are below the LARGE_FILES.md size threshold; no large derived data or manuscript rebuild is introduced.
