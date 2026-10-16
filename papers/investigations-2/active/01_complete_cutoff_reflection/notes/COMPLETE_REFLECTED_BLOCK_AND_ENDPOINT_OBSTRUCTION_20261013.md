# A complete reciprocal block and its noncancelling shared endpoint

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex); reasoning effort **ultra**, inherited
from the parent session whose configuration was verified. Internal LLM
research, not independent mathematical validation.

## Result and decision

The literal pair `[N/2,N]`, `[N,2N]` can be completed at an actual physical
center with `P=N²`, including both endpoint half-weights, every retained
Fourier mode, the infinite excluded-mode integral remainder, the actual
carrier mismatch, and the raw first spatial derivative. It does **not**
automatically cancel its shared cutoff endpoint. For a common Fourier
ceiling `M=4N`, that contribution has magnitude greater than `w_N/20`
under the explicit hypotheses in Section 4. The ordinary cancellation of
a boundary between adjacent integrals becomes addition in the conjugated
reflection comparison.

This is a quantified obstruction to estimating that comparison by deleting
or cancelling its shared endpoint. It is not a lower bound for the complete
reflection defect: its retained oscillatory integrals and outer endpoints
can and do compensate much of the shared term. The bounded experiment finds
no substantial additional cancellation between the two *remaining Fourier
tails*. Their combined residual is much smaller than the existing analytic
absolute envelope, but its size is nearly the sum of the individual tail
sizes. Thus the small residual alone does not demonstrate a reflection gain.

**Gate:** this particular automatic boundary-cancellation mechanism fails.
Keep the complete formula as an interface; continue only if a new relation
controls the combined retained modes and endpoints, or an outward first-jet
calculation beats the existing *complete physical* error. No collision
exclusion, actual-source observation lower bound, or RH consequence is
established.

## 1. The physical preparation and one exact reciprocal center

Use the actual finite-source data in [Heat Note 22](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md),
not a freely adjusted carrier. At fixed `t`, put
\[
\begin{gathered}
L=\log(x/(4\pi)),\quad
\alpha_r=L/2+\tfrac14\log(1+x^{-2})-(1+x^2)^{-1},\\
\alpha_i=3x/(1+x^2)-\tfrac12\arctan x,\quad
U=(7x^2-5)/(1+x^2)^2,\quad V=x(x^2+5)/(1+x^2)^2,\\
T=(x-t\alpha_i)/2,\quad P=T/(2\pi),\quad
\sigma=\tfrac12+t\alpha_r/2,\\
c=\tfrac12+tU/4,\quad d=tV/4,\quad
\Omega=\tfrac12\Re\{(\alpha_r+i\alpha_i)(1+t(U+iV)/2)\},\\
\theta=-\pi+\tfrac14\arctan x+\tfrac x4(1-L)
 -\tfrac x8\log(1+x^{-2})+t\alpha_r\alpha_i/2,\\
w(v)=e^{-\sigma\log v+t\log^2v/4},\qquad
q(v)=w(v)e^{i(\theta+T\log v)}.
\end{gathered}\tag{1}
\]
Then `T_x=c`, `sigma_x=d`, `theta_x=-Omega`, and
\[
q_x(v)=h(v)q(v),\qquad h(v)=-i\Omega+(-d+ic)\log v.\tag{2}
\]
Every index derivative below is distinguished from this spatial derivative.

Fix an **even integer** `N>=4` and `0<t<=1/20`. Define `x=x_N(t)` as the
unique nearby root
\[
x-t\alpha_i(x)=4\pi N^2.\tag{3}
\]
For `x>=200` the left side is strictly increasing, and the root lies in
`(4 pi N²-pi t/4,4 pi N²)`. Thus `P=N²` exactly and the continuum reciprocal
map exchanges the compact blocks
\[
I=[N/2,N],\qquad E=[N,2N].\tag{4}
\]
The natural finite cutoff is `N`: indeed
\[
x/(4\pi)+t/16=N^2+t(\alpha_i+\pi/4)/(4\pi)>N^2,
\]
and the small positive addition is less than one. These centers are just
above the natural-cutoff crossing; an arbitrarily small neighborhood has
fixed cutoff. The wider cutoff-crossing ledger is in Section 6.

This special reciprocal scale is a chosen **physical point**, not an
integer-lattice permutation. Most integer `n` in `I` still have noninteger
`P/n`. The exterior below is the prescribed real-index chirp continuation
sampled at its own integers; it is not a new physical tail of `H`.

Write
\[
\delta=\sigma-\left(\tfrac12+\tfrac t4\log P\right),\quad
\vartheta=2\theta+T\log P-T-\pi/4+2\pi,
\quad w_*(v)=w(v)e^{\delta(2\log v-\log P)}.\tag{5}
\]
The extra `2 pi` chooses the small real branch; it changes no exponential.
The exact leading stationary *coefficient*, extended to real `v`, is
\[
B(v)=e^{i\vartheta}\overline{w_*(v)e^{i(\theta+T\log v)}}
=e^{-i(T+\pi/4)}\frac{\sqrt P}{v}q(P/v).\tag{6}
\]
Equation (6) does not replace any finite Fourier integral by a leading
saddle approximation.

For an integer-endpoint interval, use its literal half-weighted sum
\[
\Sigma_{a,b}(f)=\tfrac12 f(a)+\sum_{a<n<b}f(n)+\tfrac12 f(b).
\]
Our complete comparison is
\[
D_0=\Sigma_I(q)-e^{i\vartheta}\overline{\Sigma_E(q_*)},
\qquad q_*=w_*e^{i(\theta+T\log v)}.\tag{7}
\]
Neither endpoint half is discarded. In particular the true sum through `N`
is recovered exactly from
\[
\sum_{n=1}^Nq(n)
=\sum_{n<N/2}q(n)+\tfrac12q(N/2)+\tfrac12q(N)
  +e^{i\vartheta}\overline{\Sigma_E(q_*)}+D_0.\tag{8}
\]
The exterior and the complete defect enter together.

## 2. The raw first jet, including the moving carrier

Freeze both integer ranges in (7) when differentiating. Define
\[
\begin{gathered}
\delta_x=d-\frac{tc}{4T},\qquad
\vartheta_x=-2\Omega+c\log P,\\
\epsilon_x(v)=\delta_x(2\log v-\log P)-\delta c/T,\\
a_{I,0}=w,\quad a_{I,1}=wh,\quad
 a_{E,0}=w_*,\quad a_{E,1}=w_*\{h+\epsilon_x-i\vartheta_x\}.
\end{gathered}\tag{9}
\]
Then, with `Phi=theta+T log v`,
\[
D_j=\Sigma_I(a_{I,j}e^{i\Phi})
 -e^{i\vartheta}\overline{\Sigma_E(a_{E,j}e^{i\Phi})},
\qquad j=0,1,\quad D_1=\partial_xD_0.\tag{10}
\]
This keeps amplitude drift, reflected-weight drift, and the derivative of
the carrier multiplying the conjugated channel. Omitting the last term
`-i vartheta_x` would give the wrong derivative.

For reproducible index derivatives, every amplitude here has the form
`a(v)=C w_s(v)(A+B log v)`, with
`w_s=exp(-s log v+t log²v/4)`. If `p=-s+(t/2)log v` and `h_0=A+B log v`,
\[
a'=Cw_s(ph_0+B)/v,\qquad
a''=Cw_s\{(p^2-p+t/2)h_0+(2p-1)B\}/v^2.\tag{11}
\]
All these formulas are exact.

A qualification matters: away from the center, the geometrically reflected
continuum interval is `[P(x)/N,2P(x)/N]`, not the frozen `E`. A moving
continuum integral must add
\[
(2P_x/N)f(x,2P/N)-(P_x/N)f(x,P/N)\tag{12}
\]
to its differentiated integral. A sharp integer mask additionally has
entering/leaving terms as its endpoints cross integers; its half-weighted
value at the crossing is not a differentiable mask. We do **not**
differentiate that moving mask. Formula (10) differentiates the single
frozen comparison, whose exact defect retains all saddle/endpoint
transitions. This is the same fixed-cutoff principle as the inherited
physical approximation interface.

## 3. Complete Poisson identity and its current absolute envelope

For either amplitude in (9), set
\[
g_k(v)=T/v-2\pi k,\quad
I_k[a;a_0,b_0]=\int_{a_0}^{b_0}a(v)e^{i\Phi(v)-2\pi ikv}\,dv,
\qquad M=4N.
\]
Every stationary mode, including an endpoint saddle, is inside `|k|<=M`.
They remain exact finite integrals. At each integer endpoint `z`, let
`omega=P/z` and
\[
S_r(\omega,M)=\sum_{|k|>M}^{\rm sym}(\omega-k)^{-r},\qquad r=1,2,3.
\]
At our endpoints `omega=2N,N,N/2` is integer, and no tail denominator
vanishes. The functions have particularly simple complete expressions:
\[
\begin{aligned}
S_1&=-\sum_{k=M-\omega+1}^{M+\omega}k^{-1},\\
S_2&=\pi^2/3-H^{(2)}_{M-\omega}-H^{(2)}_{M+\omega},\\
S_3&=-\sum_{k=M-\omega+1}^{M+\omega}k^{-3}.
\end{aligned}\tag{13}
\]
These follow by pairing positive and negative tails; equivalently use the
[cotangent partial fractions, DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3).
The finite Poisson identity uses the endpoint-average Fourier convergence
in [DLMF 1.8(ii)](https://dlmf.nist.gov/1.8#ii), as proved directly by
periodization in [project 09 Note 8](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/notes/8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md).

Define the **entire excluded-mode endpoint contribution**
\[
\mathcal E_a(z)=e^{i\Phi(z)}\left\{
\frac{a(z)}{2\pi i}S_1+\frac{a'(z)}{(2\pi)^2}S_2
 +\frac{Ta(z)}{z^2(2\pi)^3}S_3\right\}.\tag{14}
\]
Two integrations by parts, with `L_k a=(a/g_k)'`, give the exact identity
\[
\Sigma_{a_0,b_0}(ae^{i\Phi})
=\underbrace{\sum_{|k|\le M}I_k+\mathcal E_a(b_0)-\mathcal E_a(a_0)}_{\mathcal T[a;a_0,b_0]}
+R[a;a_0,b_0],\tag{15}
\]
\[
R=-\sum_{|k|>M}\int_{a_0}^{b_0}
 e^{i\Phi-2\pi ikv}
 \left\{\frac{a''}{g_k^2}-\frac{3a'g_k'}{g_k^3}
 -\frac{ag_k''}{g_k^3}+\frac{3a(g_k')^2}{g_k^4}\right\}dv.\tag{16}
\]
The integral series is absolutely convergent. The first endpoint series is
symmetrically summed; its paired series is absolutely convergent. Thus no
unrecorded Fourier tail remains in (15).

Since `M>=2P/a_0` on both intervals, the proof of
[Heat Note 24, (16)](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/24_CURVATURE_CONES_SHARP_NULL_PAYMENTS_AND_LOCALIZED_POISSON_20261010.md)
applies equally to integer endpoints and gives the explicit analytic bound
\[
|R|\le\mathcal B[a;a_0,b_0]
:=\frac{2}{\pi^2M}\int_{a_0}^{b_0}
\left(|a''|+3|a'|/v+5|a|/v^2\right)dv.\tag{17}
\]
Indeed `|g_k|>=pi|k|`, `|g_k'|<=pi|k|/v`, and
`|g_k''|<=2pi|k|/v²`; summing `k^-2` gives (17).

The **complete reflected block identity** is therefore
\[
\boxed{D_j=\mathcal T[a_{I,j};I]
-e^{i\vartheta}\overline{\mathcal T[a_{E,j};E]}+R_{\rm pair,j}},
\qquad
R_{\rm pair,j}=R_{I,j}-e^{i\vartheta}\overline{R_{E,j}},\tag{18}
\]
\[
|R_{\rm pair,j}|\le\mathcal B_{I,j}+\mathcal B_{E,j}.\tag{19}
\]
This is exact for both coherent channels before real projection. The
transforms in (18) are applied separately to the two exact raw jets.
`R_pair,1` is not asserted to be the derivative of `R_pair,0`, because
differentiating a truncated integration-by-parts decomposition also changes
its phase denominators and endpoint decomposition. Both individual jet
identities are nevertheless exact. The real readout uses `2 Re` only after
all terms are combined.

## 4. A rigorous shared-endpoint obstruction

The contribution of the shared endpoint `N` in (18), for `j=0`, is
\[
\mathcal C_N=\mathcal E_w(N)
 +e^{i\vartheta}\overline{\mathcal E_{w_*}(N)}.\tag{20}
\]
There is a **plus** sign. The cancellation in the ordinary adjacent sum
`T[I]+T[E]` does not survive replacing the exterior by its conjugate and
subtracting it.

**Proposition.** Assume even `N>=4`, the physical definitions (1), `P=N²`,
and `|delta|<=1/2`. Then
\[
\left|\mathcal C_N-e^{i\vartheta/2}(-1)^{N-1}w_N
       \frac{\sin(\pi/8)}\pi S_1(N,4N)\right|
\le\frac{34w_N}{225\pi^2N^2},\tag{21}
\]
and in particular
\[
\boxed{|\mathcal C_N|>w_N/20.}\tag{22}
\]
The actual small-time centers in (3) satisfy `|delta|<=1/2`; alternatively
that explicitly printed hypothesis is sufficient for the proposition.
For example, from `|alpha_i|<pi/4` and `|alpha_r-L/2|<=x^-2` at `x>=200`,
\[
|\delta|\le t/(2x^2)+t^2\pi/(16x)<1/2.
\]

**Proof.** The carrier relation is exact:
\[
q(N)=(-1)^{N-1}w_N e^{i\pi/8+i\vartheta/2}.
\]
Also `w_*(N)=w_N`, and the logarithmic weight derivatives at `N` are
`p=-1/2-delta`, `p_*=-1/2+delta`, so `|p|+|p_*|=1`. Combining the
`S_1` terms in (20) gives the displayed main term of (21). For the rest,
\[
S_2(N,4N)\le\frac{8}{15N},\qquad
|S_3(N,4N)|\le\frac8{225N^2},\qquad T/N^2=2\pi.
\]
These follow by integral comparison with `k^-2` and `k^-3`. Equation
(14) bounds the two remaining contributions by respectively
`2w_N/(15 pi² N²)` and `4w_N/(225 pi² N²)`, proving (21).
Furthermore
\[
|S_1(N,4N)|\ge\log\frac{5N+1}{3N+1}.
\]
Hence
\[
|\mathcal C_N|/w_N\ge
\frac{\sin(\pi/8)}\pi\log\frac{5N+1}{3N+1}
 -\frac{34}{225\pi^2N^2}>\frac1{20}.\tag{23}
\]
For a purely rational verification of the final strict inequality, use
`sin(pi/8)>3/8`, `pi<22/7`, `pi²>9`, and
`log(21/13)>=2((21/13)-1)/((21/13)+1)=8/17`.
For `N>=4` the right side exceeds `21/374-34/32400>1/20`.
This proof uses no numerical quadrature. QED.

As `N` grows along even integers, its leading magnitude divided by `w_N`
tends to `sin(pi/8) log(5/3)/pi`, about `0.0622`. This statement concerns
one term of (18). It does **not** prevent cancellation against the finite
Fourier integrals, the two outer endpoints, or the literal endpoint halves
when reconstructing (8). No lower bound for `D_j` follows from (22).

## 5. A bounded diagnostic of the signed remainder

The [checker](../numerics/check_complete_reflected_block.py) and
[small record](../numerics/COMPLETE_REFLECTED_BLOCK_RECORD_20261013.json)
evaluate (18) at `t=0.05` and `N=8,12,16,32`. The approximate centers are
`804.2086670157`, `1809.5181952704`, `3216.9516617671`, and
`12867.9242527953`. The same physical data, endpoints, common `M=4N`, and
binary64 precision are used on both sides. Every finite Fourier integral
is retained through the exact Dirichlet kernel. Composite Gauss–Legendre
quadrature uses `M` panels per unit length and degrees 16 and 24; the
record stores both evaluations and their differences. Direct finite
differences of (7) with frozen ranges also check (9)–(10).

These are **floating-point diagnostics**, not outward bounds, certified
quadratures, or a genuine `H` calculation. Numbers labelled envelope below
are floating-point evaluations of the analytic expression (17), not
certified upper endpoints. The centers satisfy `x>=200`, but their
`kappa=t log(x/(4 pi))` is about `0.208` through `0.347`, below the inherited
asymptotic search sector `[1,3/2]`. No large-height extrapolation is made.

Define the pairing cancellation ratio at each jet by
\[
\chi_j=\frac{|R_{I,j}-e^{i\vartheta}\overline{R_{E,j}}|}
 {|R_{I,j}|+|R_{E,j}|}.\tag{24}
\]
The denominator is the sum of the two actual computed residual magnitudes,
not the much larger analytic envelope. Values rounded from degree 24 are:

| N | jet | `2 Re R_pair` | `B_I+B_E`, diagnostic | `chi_j` |
| ---: | ---: | ---: | ---: | ---: |
| 8 | 0 | `-1.93e-6` | `3.20e-3` | `0.974` |
| 8 | 1 | `+5.12e-7` | `1.63e-3` | `0.976` |
| 12 | 0 | `+3.15e-7` | `1.14e-3` | `0.962` |
| 12 | 1 | `+1.08e-8` | `5.77e-4` | `0.987` |
| 16 | 0 | `-6.11e-8` | `5.43e-4` | `0.961` |
| 16 | 1 | `+5.30e-8` | `2.76e-4` | `0.987` |
| 32 | 0 | `+3.63e-9` | `9.09e-5` | `0.957` |
| 32 | 1 | `+6.63e-10` | `4.62e-5` | `0.991` |

The value residual changes sign among these exact-source coefficient
samples. Pairing reduces its magnitude only a few percent relative to the
sum of separate residual magnitudes. The very large difference between
actual residuals and (17) mostly concerns the conservatism of the absolute
integration-by-parts envelope; it is not evidence for a special reflected
cancellation. At `N=32`, subtraction and floating-point phase errors already
limit meaningful tail digits, so only coarse ratios are used.

The complete reflection defects are also retained in the record. For
example at `N=8`, `D_0` is approximately
`0.000992+0.001726 i`, whereas the shared endpoint is approximately
`0.02058-0.00000959 i`. Their difference demonstrates why a bound for the
shared term must not be advertised as a bound for the entire defect.

Replay without overwriting the saved record:

```sh
python3 papers/investigations-2/active/01_complete_cutoff_reflection/numerics/check_complete_reflected_block.py --record /tmp/COMPLETE_REFLECTED_BLOCK_RECORD_20261013.json
```

Python and NumPy versions, input hashes, the checker hash, all finite
parameters and limitations are saved. The arrays are small and ephemeral;
no external derived archive is required.

## 6. Physical reconstruction and adjacent-cutoff ledger

Equations (8) and (18) are exact finite-source identities. They do not
replace the inherited source-to-`H` theorem. To make this distinction
explicit, write `F_N=2 Re sum_(n<=N) q(n)` and `G_N=A_t(x) F_N` with the
same positive real normalizer as in the source approximation. At a center
`X`, put `b=A_t'(X)/A_t(X)` and `c_N=C_N(t,X)/A_t(X)`. The paid
[holomorphic cutoff interface, Note 22](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md)
says for a frozen cutoff and its verified disk
\[
\frac{H_t(X)}{A_t(X)}=F_N-c_N+e_0,\qquad
\frac{H_t'(X)}{A_t(X)}=F_N'+bF_N+k c_N+e_1,\tag{25}
\]
where `k=pi/8`, `|e_0|<=eta_cross`, and
`|e_1|<=eta_cross/r`. Thus if (18)'s tails are omitted while all its
other terms and (8)'s complement are retained, the *additional* absolute
first-jet payments are at most
\[
2(\mathcal B_{I,0}+\mathcal B_{E,0}),\quad
2(\mathcal B_{I,1}+\mathcal B_{E,1})
 +2|b|(\mathcal B_{I,0}+\mathcal B_{E,0}).\tag{26}
\]
The signed payments before absolute estimation are respectively
`2 Re R_pair,0` and `2 Re(R_pair,1+b R_pair,0)`.
They are additive to, not replacements for, the complete source residual.
No `eta_cross`, `b`, genuine `H`, or joint-candidate separation was
numerically certified in this experiment.

For one adjacent natural-cutoff crossing through `m`, the same source
interface retains
\[
\Delta G=G_m-G_{m-1},\qquad
\Delta C=C_m-C_{m-1},\qquad
|\Delta G(z)-e^{-iky}\Delta C(t,x)|/A_t(X)
 \le KZ B_{\rm edge},\tag{27}
\]
with `B_edge=2(exp(Lambda_edge)-1)` and the explicit `Lambda_edge` of
that note. Its exact correction identity is
\[
C_0(p+2)+C_0(p)=e^{i\pi(p^2/2+p+3/8)},\tag{28}
\]
and neither the entering finite term nor this correction jump is zero.
The full uniform residual remains
\[
\eta_{\rm cross}=K\{E_{AB}+Z[B_C+B_{\rm edge}+2rW_\tau J_*]\}.\tag{29}
\]
Equations (27)–(29) are the imported, fully specified payment, not a newly
verified numerical estimate here. Applying (8), (18) separately with
either **frozen** integer cutoff changes no source term in this crossing
identity: it only re-expresses that same `G_N`. In particular a small
Poisson tail does not cancel `E_AB`, `B_C`, or the correction-amplitude
comparison. No derivative of a jumping approximation is taken.

The ledger is therefore complete:

| Effect | Term retained or paid |
| --- | --- |
| Preparation | Every integer and composite in (8), actual weight and carrier (1) |
| Reciprocal amplitude/carrier mismatch | `delta`, `vartheta`, and exact `w_*` in (5)–(6) |
| Physical derivative and projection | All terms in (9); `2 Re` after pairing; normalizer `b` in (25)–(26) |
| Literal interval boundaries | Both endpoint halves in (7)–(8); all three endpoint-tail terms (14) at both ends |
| Saddle transitions | Every integral `|k|<=M` in (15); no full-Gaussian substitution |
| Excluded Fourier modes | Exact signed integral series (16), or explicitly paid (17)–(19) |
| Moving reciprocal endpoints | Transport terms (12) if that different family is used; not differentiated away |
| Genuine source remainder and correction | Entire (25), (27)–(29), including the entering wave and both reflected channels |
| Finite evolution vs genuine heat equation | No autonomous finite heat equation is invoked; none of its residuals is declared zero |

The next useful result would control the *whole* retained expression in
(18), with (25)–(29), on a candidate-relevant cell. Another derivation of
unitary reflection, another scalar cutoff dictionary, or a wider binary64
sweep would not pass this gate.
