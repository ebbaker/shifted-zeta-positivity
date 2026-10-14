# Matched stationary test: the complete remainder allowance is too large

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex), reasoning effort **ultra**.
This is a bounded internal research comparison, not independent validation.

**Outcome.** The retained complete A+B−C approximation does not certify
either stationary target at the tested disk radii. For the second target,
the associated separate Cauchy jet boxes necessarily contain zero at every
allowed radius `0<r<=1`, even after exact elimination of the leading
correction using physical stationarity. This is an obstruction to the
present error-allowance architecture, not a lower bound on the actual
approximation error or an adverse sign of the genuine function. The shared
direct-source baseline certifies both genuine stationary signs.

No new signed Riemann–Siegel/Mordell remainder inequality was obtained.
The finite approximation is reasonably accurate at the test points; the
available complete upper bounds are too conservative to exploit that fact.
This negative screen does not pass 01's reopening gate.

## 1. Common cells and admissibility

The fixed time is `t=1/20`. The preselected cells are

| Target | Initial real-height cell | Physical stationary equation |
| --- | --- | --- |
| j=0 | `[204.087,204.089]` | `H_x=0` |
| j=1 | `[205.556,205.558]` | `H_xx=0` |

The [shared baseline record](../../../brainstorm/numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json)
certifies one stationary root in each cell. This calculation uses its
retained narrow rational root brackets, rather than confusing the range
of physical values across the initial cells with numerical error.
The baseline record is hash checked before use.

The originally suggested range `40<=x<=100` is outside the retained
complete A+B−C theorem's `x-r>=200` domain. It was not used by extrapolation.
The revised cells have natural cutoff `N=4`, unchanged on each expanded
real interval for all tested radii `r=1/4,1/2,3/4,1`. The physical disk
requirements `x-r>=200`, `0<t<=1/2`, and `0<r<=1` all hold. The old exact
reciprocal-block centers are not being imposed: this pilot tests the
complete physical source interface, not the earlier block-tail diagnostic.

The common numerical budget was 256-bit ball arithmetic, at most one
million primitive evaluations and a target of 60 seconds per cell. The
01 screen needs four finite terms per cell and four error ledgers, with
no source quadrature. Primitive ball operations are not instrumented;
its recorded runtime is about six milliseconds, excluding interpreter
startup. The comparison still fails: its analytic allowances do not meet
the shared `1e-40` absolute jet-error target or `1e-72` stationary-form
accuracy. A fast unsuccessful bound is not a cost improvement.

## 2. Complete physical approximation and error payment

Use the existing [holomorphic correction theorem, Note 20](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md)
and [cutoff ledger, Note 22](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md).
Their analytic input is the [Polymath approximation, Corollary 6.4 and Proposition 6.6](https://arxiv.org/html/1904.12438v2#S6.SS3).
The paper also supplies an exact contour remainder at general nonreal
spectral arguments, but this pilot does not newly enclose that contour
integral. It evaluates the retained complete approximation theorem.

At each real center `X`, set `s=(1+iX)/2`,

\[
\begin{split}
M_0(s)&=\frac{s(s-1)}{16}\pi^{-s/2}\sqrt{2\pi}
 \exp\{(s/2-1/2)\log(s/2)-s/2\},\\
\alpha(s)&=\frac1{2s}+\frac1{s-1}+\frac12\log\frac{s}{2\pi},\qquad
M_t(s)=M_0(s)e^{t\alpha(s)^2/4},\\
G_{t,N}(X)&=2\Re\left\{M_t(s)\sum_{n=1}^N
 \exp\left(\frac t4\log^2n-[s+t\alpha(s)/2]\log n\right)\right\}.
\end{split}
\]

The fixed positive normalizer is `A_t(X)=|M_t(s)|`. It is held constant
when taking the physical derivatives. Ball power-series evaluation of the
complete finite formula retains all carrier and normalization derivatives.
Write `f_j=G^(j)(X)/A_t(X)`, `k=pi/8`, `d=-k`, and
`c=C(t,X)/A_t(X)`, with the full correction `C` of Note 20. Then

\[
 h_j:=H_t^{(j)}(X)/A_t(X)=f_j-cd^j+\delta_j,
 \qquad |\delta_j|\le E_j:=j!\eta_r/r^j.
\tag{1}
\]

The complete disk allowance is

\[
 \eta_r=K\{E_{AB}+Z[B_C+2rWJ_{\rm all}]\}.
\tag{2}
\]

Every quantity uses Notes 20–22's definitions. In particular

\[
 B_C=\frac{1.24(3^r+3^{-r})}{N-0.125}+\frac{6.92}{x_- -12},
 \qquad
 J_{\rm all}=\frac3{\tau_-}+\frac1{\tau_-^2}
 +\frac{17+17/\tau_-}{4\pi a_-}.
\]

The all-phase profile bound is necessary: the selected `p` values are
not within `0.01` of 1. No sharper near-endpoint constants are substituted.
The source remainder, both finite source channels and the comparison of
the nonholomorphic printed correction with its holomorphic exponential
surrogate are all paid. There is no cutoff jump on these disks. The
complete source theorem, rather than a truncated theta sum, pays the
infinite remainder. No shared Poisson endpoint is deleted.

## 3. Physical stationarity eliminates the leading correction exactly

On `h_(j+1)=0`, equation (1) gives

\[
\begin{aligned}
h_j&=f_j-f_{j+1}/d+\delta_j-\delta_{j+1}/d,\\
h_{j+2}&=f_{j+2}-df_{j+1}+\delta_{j+2}-d\delta_{j+1}.
\end{aligned}
\tag{3}
\]

Thus the conditional error allowances are

\[
 B_{\rm lower}=E_j+E_{j+1}/k,
 \qquad B_{\rm upper}=E_{j+2}+kE_{j+1}.
\tag{4}
\]

The tested sign is `-h_j h_(j+2)`. This conditions on the genuine physical
stationary equation, not a stationary point of the finite model. The
unknown correction amplitude cancels, but the two residual payments do
not. Both conditional signs fail the separate interval test at each
radius below. Rounded midpoints are only a summary; the checker and record
use outward balls throughout.

| Target | r=1/4: eta | r=1/2: eta | r=3/4: eta | r=1: eta |
| --- | ---: | ---: | ---: | ---: |
| j=0 | 0.58712130 | 0.92593393 | 1.44386302 | 2.22932323 |
| j=1 | 0.58521592 | 0.92293872 | 1.43947858 | 2.22325387 |

At `r=1`, the four derivative allowances are respectively
`[eta,eta,2eta,6eta]`. Their scale already explains the loss of the
stationary reserve. Smaller radii improve the value allowance but increase
the higher-derivative payments.

## 4. An allowance floor for every permitted radius

This part removes any need for a denser radius sweep. Let `X_+` be the
right endpoint of the initial cell and `q_max=X_+/(4pi)`. Since `K>=1`,
`E_AB>=0`, `3^r+3^(-r)>=2`, and the omitted exponential factor in `Z` is
positive, monotonicity of `q^(-1/4)exp(-t log^2(q)/16)` for `q>1` gives

\[
 \eta_r\ge\eta_{\min}:=
 q_{\max}^{-1/4}e^{-t\log^2q_{\max}/16}
 \left\{\frac{2.48}{4-0.125}+\frac{6.92}{X_+-12}\right\}
 \quad(0<r\le1).
\tag{5}
\]

This is a lower bound on the size of the theorem's **upper-error
allowance**. It is not a lower bound on the true approximation error.
For the j=1 cell the outward evaluation gives

\[
 \eta_{\min}>0.32791095.
\]

Using `r<=1` in (4) yields

\[
 B_{\rm lower}\ge(1+2/k)\eta_{\min}>1.99794,
 \qquad
 B_{\rm upper}\ge(6+2k)\eta_{\min}>2.22500.
\tag{6}
\]

On the retained genuine stationary-root bracket, the conditional finite
centers are enclosed near

\[
 f_1-f_2/d=-1.35407642459\ldots,
 \qquad f_3-df_2=0.89925360312\ldots.
\]

Both separate conditional jet boxes therefore contain zero for **every**
permitted radius. Refining the radius alone cannot make this architecture
certify the j=1 sign. This does not exclude a stronger joint analytic
constraint on the residual or an independently bounded signed remainder.
The analogous all-radius floor does not, by itself, rule out j=0; only
the four specified radii were tested for that target.

## 5. Comparison with the complete source baseline

The shared baseline gives strictly positive conditional values

\[
 L_0(H)=1.15071737608519\ldots\times10^{-64},\qquad
 L_1(H)=2.08000102453508\ldots\times10^{-65},
\]

with full outward enclosures in its record. The normalizers here are
approximately `7.279225178e-33` and `4.140203774e-33`; the baseline values
of `L_j/A^2` are approximately `2.171692656` and `1.213445052`.

Subtracting the finite corrected model from those already certified
physical jets gives the following signed residual diagnostics, themselves
enclosed using the baseline:

| Target cell | delta0 | delta1 | delta2 | delta3 |
| --- | ---: | ---: | ---: | ---: |
| j=0 | -0.00539166 | -0.00296951 | 0.00395771 | -0.00402002 |
| j=1 | -0.00143119 | -0.00447124 | 0.00298127 | -0.00221217 |

Their smallness illustrates the conservatism of (2), but it was obtained
by computing the full source first. These are **not** independent signed
Mordell remainder bounds and do not reduce certification cost.
Some smaller-radius bounds also exclude a joint zero using the value
alone. This easy consequence at stationary extrema is not an improvement
over the baseline and does not meet the matched accuracy target.

**Decision.** Stop this instance of the complete-error comparison. A useful
next 01 continuation needs a signed contour/remainder bound or a genuinely
stronger joint residual estimate that can be certified without first
computing the same physical answer. Increasing precision, repeating the
radius search, or using the old reflected Fourier-tail residual as a
replacement for the complete source payment would not address this failure.

## Reproduction and retained outputs

The [checker](../numerics/check_matched_remainder_01.py) and
[small record](../numerics/MATCHED_REMAINDER_01_RECORD_20261014.json) use
Python with `python-flint 0.9.0`. From the repository root, with that
package available:

```sh
python3 papers/investigations-2/active/01_complete_cutoff_reflection/numerics/check_matched_remainder_01.py \
  --baseline-record papers/investigations-2/brainstorm/numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json \
  --record /tmp/MATCHED_REMAINDER_01_RECORD_20261014.json
```

The checker pins the shared baseline hash and records its own and the
retained source notes' hashes. Binary64 midpoint fields are explicitly
labelled diagnostics and never decide the interval signs. All arrays and
records remain small; no external large-data archive is needed.
