# Boundary-tail selection in two derivative trial directions

28 September 2026. Drafted for Edward Baker with LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed.
Status: analytic working derivation, no numerical sweep. The conclusions concern explicitly stated trial subspaces. They do not identify the full Weil ground state or prove RH. No novelty claim is made.

## 1. Main result

Let k be the real even kernel from the preceding null-kernel note, using its literal displayed h coefficient. Its Fourier transform is Xi/4; rescaling k by four gives the standard Xi normalization and leaves all generalized eigenvalues and coefficient ratios below unchanged. Set

\[
I_b=[-b,b],\qquad A=\pi e^{2b},\qquad K=k(b),\qquad
h_b=\frac{K^2\log A}{A},\quad b\longrightarrow\infty.
\]

Let the arithmetic form Q be the full unshifted Weil form, and define the two-dimensional trial space

\[
S_b^{(2)}=\operatorname{span}\{1_{I_b}k,1_{I_b}k''\}.
\]

The form restricted to this space is positive definite for sufficiently large b, unconditionally. Its smallest generalized Rayleigh eigenvector can be represented, up to a scalar, by

\[
1_{I_b}(k+c_bk''),\qquad
\boxed{c_b=-\frac1{4A^2}-\frac9{8A^3}
+O\!\left(\frac1{A^3\log A}\right).}                       \tag{1}
\]

Its smallest trial eigenvalue is

\[
\boxed{\lambda_{\min}^{(2)}(b)=
\frac{K^2\log A}{2A^3\|k\|_2^2}
\left[1+O\!\left(\frac1{\log A}\right)\right].}             \tag{2}
\]

For comparison,

\[
\frac{Q(1_{I_b}k,1_{I_b}k)}{\|1_{I_b}k\|_2^2}
=\frac{K^2\log A}{2A\|k\|_2^2}
\left[1+O\!\left(\frac1{\log A}\right)\right].              \tag{3}
\]

Thus the optimal second-derivative correction reduces this trial energy by a factor asymptotic to `A^(−2)`, while its normalized trial vector tends to the normalized k in L2 at order `A^(−2)`. This is a concrete selection calculation within a prescribed two-dimensional arithmetic space. It is not selection against the full orthogonal complement.

The proof works in a cancellation-adapted basis and controls the entire small matrix relatively. Estimating the original nearly rank-one entries separately to fixed relative precision would not justify (2).

## 2. Exact tail identity and domains

The previous note `CCM_XI_ANNIHILATOR_AND_BOUNDARY_RESIDUAL_20260928.md` proves the distributional identity `Q(f,k)=0` without RH. Differentiation multiplies Xi by a polynomial, so `k''` and `k''''` are annihilators as well. For any of these profiles g, write `f_g=1_(I_b)g` and `r_g=1_(R\I_b)g`. Polarization gives

\[
Q(f_g,f_j)=Q(r_g,r_j).                                    \tag{4}
\]

All hard restrictions have finite jumps and rapidly decreasing piecewise-smooth extensions. Their Fourier transforms decay as O(1/|t|), enough for the logarithmic multiplier to map them into L2. They belong to the compressed Weil operator domain. In (4), `r_(k'')` means the hard restriction of the ordinary smooth derivative `k''`; it is **not** the distributional second derivative of `r_k`, which would introduce endpoint deltas.

The ordinary L2 Gram matrix of the two restricted interior functions converges to

\[
G=\begin{pmatrix}\|k\|_2^2&\langle k,k''\rangle\\
\langle k,k''\rangle&\|k''\|_2^2\end{pmatrix}>0.             \tag{5}
\]

Strict positivity follows because k and k'' are linearly independent: their Fourier transforms are Xi/4 and `−t²Xi/4`, which cannot be constant multiples on an interval where Xi is nonzero.

## 3. Boundary profiles in a basis that retains the cancellation

On the positive tail put `x=b+y/A`, `y≥0`. Introduce the two even tail functions

\[
r_{0,b}=1_{|x|>b}k,\qquad
r_{1,b}=1_{|x|>b}\left(\frac{k''}{4A}-Ak\right).
\]

Their scaled positive-side profiles satisfy

\[
\frac{r_{0,b}(b+y/A)}K=q_0(y)+O(A^{-1}),\qquad
q_0(y)=e^{-2y},
\]
\[
\frac{r_{1,b}(b+y/A)}K=q_1(y)+O(A^{-1}),\qquad
q_1(y)=(4y-11/2)e^{-2y}.                                  \tag{6}
\]

Here and below the profile O terms hold in L1, L2, and total variation on the half-line, with an exponentially weighted pointwise envelope. In particular they are strong enough to control a logarithmic Fourier form uniformly. They do not mean a uniform unweighted relative error where a limiting polynomial vanishes.

For verification, the leading n=1 theta summand is

\[
k_1(x)=\pi^2e^{9x/2}\left(1-\frac3{2t}\right)e^{-t},
\qquad t=\pi e^{2x}.
\]

It has the exact ratio

\[
\frac{k_1''}{k_1}=4t^2-22t+\frac{33}4+\frac6{2t-3}.         \tag{7}
\]

The remaining theta summands and their fixed-order derivatives are exponentially smaller relative to the first one, uniformly for x≥b. Also

\[
\frac{k(b+y/A)}K
=e^{-2y}\left[1+\frac{(9/2)y-2y^2}{A}\right]
+O(A^{-2})
\]

in the same weighted profile norms. Inserting `t=Ae^(2y/A)` into (7) gives

\[
\frac{k''(b+y/A)}{4A^2k(b+y/A)}
=1+\frac{4y-11/2}{A}
+\frac{8y^2-11y+33/16}{A^2}+O(A^{-3}).                     \tag{8}
\]

The expansions are obtained by Taylor's formula with remainder. Their uniform norm interpretation follows from the explicit Gaussian expression: on `0≤y≤A` the remainders are bounded by `C A^(−j)(1+y)^m e^(−c y)` after the common tail factor is included; on `y>A`, the term `exp[-A(e^(2y/A)−1)]` bounds the polynomial and derivative prefactors by a faster exponential. The fixed-order derivative of each error has the same type of bound, which supplies total variation control. The n≥2 terms are bounded by a polynomial in A times `e^(−3A)` after normalization. These facts give (6) with rate O(1/A), including the cancellation defining r1.

## 4. Uniform leading form on this boundary space

For a fixed finite family of even tails whose positive-side scaled profiles converge in the norms just specified, the archimedean form has

\[
Q^{\rm arch}(r_i,r_j)
=\log A\,\langle r_i,r_j\rangle_{L^2(\mathbb R)}
+O(K^2/A).                                               \tag{9}
\]

The O bound is uniform over bounded coefficient vectors in that family. To see this, let `a_Γ(t)=Re ψ(1/4+it/2)−log π`. The known logarithmic growth and boundedness on compact frequency intervals give

\[
|a_\Gamma(A\xi)-\log A|\le C+|\log|\xi||.
\]

The scaled half-line profiles have uniformly bounded L1 norms and variations, so their Fourier transforms are bounded by `C min(1,1/|ξ|)`. The last display is integrable against the product of these envelopes. Scaling frequency by A proves (9). Both endpoint packets are included. Their phase factors do not affect this remainder bound, while their ordinary L2 cross term is exactly zero because their supports are disjoint.

The pole and prime pieces are smaller:

\[
|Q^{\rm pole}(r_i,r_j)|+|Q^{\rm prime}(r_i,r_j)|
\le C(1+b)e^{-b}K^2/A.                                   \tag{10}
\]

One can use the explicit tail bounds in Section 6 of the null-kernel note with a fixed multiple of A in place of its decay rate. Every profile here obeys `|r_i(b+s)|≤CKe^(−cAs)` for a fixed c>0. The equal-ray prime correlations have the extra factor `e^(−cA log n)`; opposite-ray correlations begin at `log n=2b` and are bounded by an exponentially decaying function of `A(log n−2b)`. Replacing `Λ(n)` by `log n` and comparing the decreasing tail sum to its first value and integral gives the bound in (10). The pole functional is bounded by `CKe^(b/2)/A`, whose square is of order `e^(−b)K²/A`. These estimates control absolute values, so sign changes in a cancellation profile cause no difficulty.

Consequently, with `h_b=K²log A/A`,

\[
\frac1{h_b}\big(Q(r_i,r_j)\big)_{i,j=0,1}
=M+O(1/\log A),
\]
\[
\boxed{M=2\left(\int_0^\infty q_i(y)q_j(y)dy\right)_{i,j}
=\begin{pmatrix}1/2&-9/4\\-9/4&85/8\end{pmatrix}.}         \tag{11}
\]

Its determinant is 1/4, so M is strictly positive definite. This is the needed relative control after cancellation, and it proves eventual positivity on the two-dimensional trial space.

## 5. Generalized eigenvalue calculation

Let `H_b` be the form matrix in the original interior basis `{1_I k,1_I k''}`. The transformation from the adapted basis to this basis is

\[
T_A=\begin{pmatrix}1&-A\\0&1/(4A)\end{pmatrix},\qquad
T_A^tH_bT_A=h_b E_b,\quad E_b=M+O(1/\log A).               \tag{12}
\]

Write `E_ij` for the entries. Undoing the transformation gives

\[
H_{00}=h_bE_{00},
\]
\[
H_{02}=4A^2h_b(E_{00}+E_{01}/A),
\]
\[
H_{22}=16A^4h_b(E_{00}+2E_{01}/A+E_{11}/A^2).              \tag{13}
\]

In particular the energy Schur complement has the exact expression

\[
H_{00}-H_{02}^2/H_{22}
=\frac{h_b}{A^2}
\frac{\det E_b}{E_{00}+2E_{01}/A+E_{11}/A^2}
=\frac{h_b}{2A^2}[1+O(1/\log A)].                         \tag{14}
\]

The generalized L2 Gram matrix remains uniformly positive definite by (5). A candidate with coefficient `−H02/H22` has bounded nonzero norm and energy O(h_b/A²), so the smallest generalized eigenvalue is O(h_b/A²). In its eigenvalue equation, replacing `H−λG_b` by H changes the coefficient ratio by O(A^(−6)). Thus

\[
c_b=-\frac{H_{02}}{H_{22}}+O(A^{-6})
=-\frac1{4A^2}\left[1-\frac{E_{01}}{AE_{00}}+O(A^{-2})\right].
\]

Since `E01/E00=−9/2+O(1/log A)`, this proves (1). The denominator of its Rayleigh quotient is `||k||²+O(A^(−2))`, with an additional negligible truncation error. Equation (14) proves (2). Equation (3) follows from `H00`.

The optimized leading omitted-tail profile is proportional to

\[
\frac K A e^{-2y}(1-4y),                                 \tag{15}
\]

whose weighted L2 mean against the leading `e^(−2y)` profile vanishes. The derivative correction therefore cancels an endpoint boundary layer; it need not be large in the ordinary interior L2 norm to change an extremely small Rayleigh energy substantially.

## 6. Adding the fourth derivative changes the optimized energy again

This optional extension demonstrates a limitation of fixing the trial dimension at two. Put

\[
S_b^{(3)}=\operatorname{span}\{1_I k,1_I k'',1_I k''''\}.
\]

Consider the explicit field

\[
F_A=(1+4/A)k-\frac{k''}{2A^2}+\frac{k''''}{16A^4}.          \tag{16}
\]

It tends to k in L2. Differentiating (7) gives

\[
\frac{k_1''''}{k_1}=16t^4-240t^3+934t^2+O(t).
\]

Consequently

\[
\frac{k''''(b+y/A)}{16A^4k(b+y/A)}
=1+\frac{8y-15}A
+\frac{32y^2-90y+467/8}{A^2}+O(A^{-3}).                    \tag{17}
\]

Combining (8), (16) and (17) cancels both the constant and order-1/A profiles. In the same weighted norms,

\[
\frac{A^2F_A(b+y/A)}K
\longrightarrow e^{-2y}(16y^2-68y+217/4).                  \tag{18}
\]

The preceding form estimate therefore gives

\[
Q(1_I F_A,1_I F_A)=O(h_b/A^4).
\]

Moreover the three adapted tail profiles from k, `k''/(4A)−Ak`, and `A²F_A` have linearly independent polynomial factors of degrees 0,1,2. Their leading boundary L2 Gram matrix is positive definite. The same argument as (9)–(11) proves eventual positive definiteness on the full three-dimensional trial space. Hence

\[
0<\lambda_{\min}^{(3)}(b)\le C h_b/A^4,
\qquad
\boxed{\lambda_{\min}^{(3)}(b)/\lambda_{\min}^{(2)}(b)
\longrightarrow0.}                                      \tag{19}
\]

This is an optimized-energy statement. It does not assert that the Schur correction evaluated on the old two-dimensional Ritz eigenvector equals its old energy: those spaces have increasingly anisotropic energy scales, so a small change of the interior direction can matter. It does show that ignoring further derivative directions is unjustified for a **relative approximation to the optimized lowest energy**, even though the tested low-space vectors all tend toward k in ordinary L2.

## 7. Every fixed derivative rank is eventually positive

The same boundary argument extends to any fixed rank m; no constants below are uniform as m grows. Write

\[
S_b^{(m)}=\operatorname{span}\{1_I k^{(2j)}:0\le j<m\},
\qquad
B_{j,A}(x)=\frac{k^{(2j)}(x)}{(2A)^{2j}k(x)}.
\]

For fixed j and derivative order r, the theta expansion gives

\[
\partial_x^r B_{j,A}(b)=(4j)^r+O_{j,r}(A^{-1}),            \tag{20}
\]

with `0^0=1` and the j=0 derivatives of positive order equal to zero. Indeed the leading derivative ratio is `(2πe^(2x))^(2j)`, while its lower terms have successively lower powers of `πe^(2x)`. Fixed derivatives preserve that expansion; the remaining theta summands are exponentially smaller.

Thus the m-by-m jet matrix with rows r=0,...,m−1 converges to a Vandermonde matrix on the distinct numbers `0,4,...,4(m−1)`. It is invertible for large A. For each `0≤ℓ<m`, choose a linear combination `p_(ℓ,A)` of the B functions with jets

\[
\partial_x^r p_{\ell,A}(b)=r!A^r\delta_{r\ell}
\quad(0\le r<m).
\]

Its coefficients are O_m(A^ℓ). Taylor's formula at b then gives

\[
p_{\ell,A}(b+y/A)=y^\ell
+O_m\!\left(A^{\ell-m}y^m e^{C_m y/A}\right).
\]

This remainder description is used after multiplication by the decaying kernel profile. The explicit theta bounds from Section 3, including derivatives, give

\[
\frac{k(b+y/A)p_{\ell,A}(b+y/A)}K
=y^\ell e^{-2y}+O_m(A^{-1})                              \tag{21}
\]

in the weighted L1/L2/BV profile norms. For example, on bounded `y/A` the displayed Taylor remainder proves the rate because `ℓ≤m−1`; outside that range the superexponential theta factor dominates the fixed-rank coefficient growth and all `e^(C_m y/A)` factors. Each `k p_(ℓ,A)` is an exact scalar linear combination of the annihilator derivatives.

Applying the common form lemma gives, in this invertible trial basis,

\[
\frac{H_b^{(m)}}{h_b}=M_m+O_m(1/\log A),\qquad
(M_m)_{rs}=2\int_0^\infty y^{r+s}e^{-4y}dy
=\frac{2(r+s)!}{4^{r+s+1}}.                              \tag{22}
\]

The moment matrix M_m is positive definite because a nonzero polynomial has a strictly positive square integral against `e^(−4y)dy`. Consequently **every fixed derivative rank m gives a positive-definite arithmetic trial form for all sufficiently large support**, without RH. The threshold support and all estimates may deteriorate with m.

Together with the fixed-support derivative form-core theorem in [the complement note](CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md), this gives a sharp warning. If RH fails, then at every sufficiently large fixed b some finite derivative rank detects a negative direction, but the smallest such rank must tend to infinity as b grows. Thus no fixed-rank eventual-positivity theorem can settle the sign of the full operator. A joint rank/support estimate remains indispensable.

## 8. Scope and next obligation

This supplies a noncircular restricted selection mechanism: the exact arithmetic null identity converts the finite-window form into a boundary-tail form; its leading logarithmic energy selects a k-like vector within the prescribed derivative space. The prime and pole contributions are quantitatively lower order on that space, rather than discarded globally.

No lower bound on the entire orthogonal complement has been proved. In particular:

- Eventual positive definiteness on these two or three trial directions does not prove positivity on the full interval.
- Their Ritz values are upper bounds for the corresponding full low levels, not lower bounds or certified gaps.
- The actual ground may lie outside these spaces. The third direction already changes the optimized energy by another vanishing factor.
- The trial ground profiles' convergence to k is not the required theorem about the actual Weil ground profile.
- These are continuum trial-space results. Transferring their tiny relative energies to finite Fourier matrices requires separately quantified approximation in the relevant form/operator topology.

A useful continuation should either control an increasing derivative/annihilator space with uniform conditioning and an exterior estimate, or find a direct low-space overlap/selection invariant. The fixed two-dimensional theorem does not supply that final comparison, and the third-direction calculation explains why a fixed-dimensional complement cannot simply be assumed harmless.

## Verification/provenance

The derivatives, scaled profiles, Gram constants, and Schur formula are explicitly derived above. The two-dimensional leading Gram determinant is positive, and the three-dimensional argument uses independence of the degree-0,1,2 polynomial factors. A separate agent reading checked the main two- and three-dimensional calculations, the multiplier estimate and their scopes; this is additional machine review, not independent human verification. The fixed-rank extension was also checked in a separate agent reading before this version was saved. There are no inferred signs from floating-point experiments. The multiplier and explicit-formula conventions are those checked in the preceding null-kernel note and the repository's 26 September CCM audit.
