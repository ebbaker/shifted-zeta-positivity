# Exact signed place addition and accelerated first-prime returns

29 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed to this agent. This is an independent same-model derivation within the current audit, not human refereeing.

## Scope

These results use the actual Sonin smoothing and calibration established in the [companion audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md). They retain the compressed metric and establish no residual sign. No numerical approximation to the Sonin projection is used. The scalar return-tail comparison is reproducible with [the standard-library script](../numerics/sonin_return_tail_bounds.py) and its [small exact-arithmetic record](../numerics/records/sonin-return-tail-bounds-20260929.json).

The starting reference is `papers/investigations/program-meta-analysis/notes/SONIN_RESIDUAL_CONTINUATION_20260928.md`, especially Sections 4–7. Let `P` be the ordinary orthogonal projection onto the already transported Sonin space `D_S K`. Work in the ambient scaling Hilbert space, with inner products antilinear in the first slot. Let `U=U_log(p)` be the unitary translation, `r=p^(-1/2)`, `d=I-rU`, and let bounded convolution operators `C_F,C_G` commute with `U,U*`. Assume

\[
V_F=C_FP,\qquad V_G=C_GP
\]

are Hilbert–Schmidt as maps `Ran P -> H`. Set `K=C_F* C_G`. The assumption propagates to the new projection because `C_F dP=d C_FP`.

## 1. Compressed trace proof, valid at every finite-place step

On `Ran P`, define

\[
M=P d^*dP,\qquad
P'=dP M^{-1}P d^*.
\]

Here `(1-r)^2 I <= M <= (1+r)^2 I`; thus its inverse is bounded. The actual new positive pairing is

\[
B'[f,g]=\operatorname{Tr}\bigl(M^{-1}V_F^*d^*dV_G\bigr).
\]

This formula follows from the isometry `dP M^(-1/2)` and Hilbert–Schmidt factorization; it does not need the stronger assertion that `KP` is trace class. With `B[f,g]=Tr(V_F* V_G)`,

\[
\delta_p^P[f,g]=B'[f,g]-B[f,g]
=\operatorname{Tr}\bigl(M^{-1}P d^*d(I-P)KP\bigr).
\tag{A1}
\]

The off-diagonal expression in (A1) is trace class because

\[
P d^*d(I-P)KP
=V_F^*d^*dV_G-MV_F^*V_G.
\tag{A2}
\]

All cyclicity used here has a bounded factor and a trace-class factor. This argument applies with `P=P_S` directly. There is no need to recompress against the original `Pi` at every addition; doing so would require keeping both old and new compressed metrics.

## 2. Exact resolvent and a signed covariance measure

Put

\[
Z=U+U^*,\qquad A=Z/2,\qquad T=(PAP)|_{\operatorname{Ran}P},
\qquad \beta=\frac{2r}{1+r^2}<1,
\]
\[
X=PZ(I-P)KP.
\]

Then `A,T` are selfadjoint contractions,

\[
M=(1+r^2)(I-\beta T),\qquad
\boxed{\delta_p^P[f,g]
=-\frac{r}{1+r^2}\operatorname{Tr}\bigl((I-\beta T)^{-1}X\bigr).}
\tag{A3}
\]

In particular the inherited first-prime factor and sign are correct: `r=1/sqrt(2)` gives `r/(1+r^2)=sqrt(2)/3`.

For diagonal inputs set

\[
W=V_F^*V_F,\qquad H_F=V_F^*AV_F.
\]

Both are trace class, `W>=0`, and `-W<=H_F<=W`. Also

\[
X=2(H_F-TW).
\tag{A4}
\]

Although `X` need not be selfadjoint, `Tr q(T)X` is real for every bounded real Borel function `q`: its two terms in (A4) are traces of products of selfadjoint operators. In particular no unjustified real-part deletion is hidden in (A3).

Let `E_T` be the spectral measure of `T`, and define finite measures on `[-1,1]` by

\[
\mu_F(E)=\operatorname{Tr}(E_T(E)W),\qquad
\eta_F(E)=\operatorname{Tr}(E_T(E)H_F).
\]

The first measure is positive, has mass `B[f]`, and `-mu_F <= eta_F <= mu_F`. Hence `eta_F=h_F mu_F` for a real measurable `h_F` satisfying `|h_F|<=1`. Equation (A3) becomes the exact signed identity

\[
\boxed{\delta_p^P[f]
=-\beta\int_{-1}^1\frac{h_F(t)-t}{1-\beta t}\,d\mu_F(t),}
\tag{A5}
\]
\[
\boxed{B'[f]=\int_{-1}^1
\frac{1-\beta h_F(t)}{1-\beta t}\,d\mu_F(t).}
\tag{A6}
\]

This makes the sign-bearing object explicit: the difference between the compressed translation coordinate `t` and the translation average `h_F(t)` after applying the source convolution. It does not assert that this difference has a sign for actual Sonin sources.

The only bounds following from `|h_F|<=1` alone are the condition-number bounds

\[
\left(\frac{1-r}{1+r}\right)^2 B[f]
\le B'[f]\le
\left(\frac{1+r}{1-r}\right)^2 B[f].
\tag{A7}
\]

Their deterioration with the number of places prevents treating them as all-prime control. They imply no arithmetic positivity.

There is also an exact compressed double-commutator version on the diagonal:

\[
X+X^*=-P[Z,[P,K]]P,
\]
\[
\delta_p^P[f]
=\frac{r}{2(1+r^2)}\operatorname{Tr}
\left((I-\beta T)^{-1}P[Z,[P,K]]P\right).
\tag{A8}
\]

The **compressed** double commutator in (A8) is trace class by (A4); no claim is made that its uncompressed counterpart is trace class.

## 3. The complete residual law and the arithmetic bookkeeping

For the handoff's complete residual, which contains **all** prime powers active at support length `L`, the arithmetic form is independent of the chosen finite set of transported places. Therefore, at fixed `L`,

\[
\boxed{R_{S\cup\{p\},L}[f]
=R_{S,L}[f]
+\beta\int\frac{h_{S,p,F}(t)-t}{1-\beta t}\,d\mu_{S,p,F}(t).}
\tag{A9}
\]

All objects in the integral use `P=P_S`. Equation (A9) is a signed formula for the exact change, including the metric inverse. If `p` is inactive at `L`, the same change still occurs, and it cancels the change in `B_S` exactly.

There is **no additional new prime term in (A9)**: such a term would double-count arithmetic already present in the handoff's complete residual. To formulate a prime-by-prime induction with an explicit arithmetic increment, define the auxiliary *partial* arithmetic form `Q_{S,L}` containing only prime-power summands for `p in S`, and its residual `R_tilde_{S,L}=Q_{S,L}-B_S`. Write the full contribution of the newly included prime as

\[
\mathfrak a_{p,L}[f]
=(\log p)\sum_{m\log p<L}p^{-m/2}
\bigl(\kappa_f(m\log p)+\kappa_f(-m\log p)\bigr).
\]

Then the correct auxiliary law is

\[
\boxed{\widetilde R_{S\cup\{p\},L}[f]
-\widetilde R_{S,L}[f]
=\beta\int\frac{h_{S,p,F}(t)-t}{1-\beta t}\,d\mu_{S,p,F}(t)
-\mathfrak a_{p,L}[f].}
\tag{A10}
\]

Once `S` contains every active prime, the auxiliary form and residual equal the complete ones. All powers of the new prime are included. Mixed metric shifts are already in `P_S` and its newly compressed metric; they are not extra Weil labels.

For a fixed source supported in `I_L`, changing the nominal larger support interval does not create further nonzero correlations outside its actual difference support. For a family of sources whose supports grow, the arithmetic increments from powers of old primes and intervening new primes must still be handled explicitly. A formal place-addition law does not address them by itself.

## 4. A faster, rigorously bounded first-prime return expansion

Let `T_n` denote Chebyshev polynomials of the first kind, with `T_0=1`. The Poisson-kernel identity, valid in operator norm for every selfadjoint contraction `T`, is

\[
(I-\beta T)^{-1}
=\frac{1+r^2}{1-r^2}
\left(I+2\sum_{n\ge1}r^nT_n(T)\right).
\]

Consequently

\[
\boxed{\delta_p^P[f,g]
=-\frac{r}{1-r^2}
\left(\operatorname{Tr}X+
2\sum_{n\ge1}r^n\operatorname{Tr}(T_n(T)X)\right).}
\tag{A11}
\]

For truncation after degree `M>=0`,

\[
\boxed{|\delta_p^P-\delta_{p,M}^P|
\le\frac{2r}{1-r^2}\frac{r^{M+1}}{1-r}\|X\|_1.}
\tag{A12}
\]

This uses `||T_n(T)||<=1`; it is valid for mixed inputs as well. The trace-class bound inherited from the handoff is correct:

\[
X=V_F^*ZV_G-2T V_F^*V_G,\qquad
\|X\|_1\le4\|V_F\|_{\rm HS}\|V_G\|_{\rm HS}.
\tag{A13}
\]

For `p=2`, the new convergence ratio is `r=1/sqrt(2)`, compared with the Neumann ratio `beta=2sqrt(2)/3`. Explicitly the prefactor in (A12) is `4(1+sqrt(2))=9.656854...`, multiplying `2^(-(M+1)/2)||X||_1`. The inherited Neumann prefactor is `4+3sqrt(2)=8.242640...`, multiplying `(2sqrt(2)/3)^(M+1)||X||_1`.

On a diagonal test the crude tails relative to `B[f]` are therefore at most

\[
16(1+\sqrt2)\,2^{-(M+1)/2}\,B[f]
\]

and

\[
(16+12\sqrt2)(2\sqrt2/3)^{M+1}\,B[f],
\]

respectively. For example the Chebyshev bound is below `10^(-8) B[f]` by degree `M=63` (64 trace terms); the inherited Neumann bound needs degree `M=372` (373 trace terms). These are truncation bounds only. Neither controls the actual Sonin projection, its trace calibration, the computed return moments, or source preparation. A numerically computed projection should preserve selfadjoint contractivity of `T` before these bounds are applied.

## 5. No universal place monotonicity follows from this algebra

Consider the finite-dimensional control `H=C^2`, `U=diag(1,-1)`, and `P` the projection onto `(1,1)/sqrt(2)`. Let `K=C* C=diag(k_1,k_2)`, with `k_1,k_2>=0`; all relevant convolutions in this abstract control are replaced by commuting diagonal operators. Then

\[
B=(k_1+k_2)/2,\qquad
B'=\frac{(1-r)^2k_1+(1+r)^2k_2}{2(1+r^2)},
\]
\[
\delta_p^P=\frac{\beta}{2}(k_2-k_1).
\tag{A14}
\]

The exact increment has either sign. This is **not a counterexample for the actual Sonin projection** or the pole-neutral source class. It proves that unitary translations, bounded invertible place transport, commuting source smoothing, positivity of the compressed metric, and Gram positivity alone cannot supply a monotonicity theorem. A new inequality must use actual Sonin geometry and/or the arithmetic source structure.

A sufficient sign condition for the complete residual increment is `h_{S,p,F}(t)>=t` almost everywhere; an arithmetic induction would instead need the weighted integral in (A10) to dominate the explicit prime-power form. Neither assertion is established here. Simply requiring the latter without further kernel information restates the hard comparison and is not itself progress.

## 6. Check of the parallel Galerkin error lemma

The root agent proposed a useful independent error-control statement. Let `A=Pi G_S Pi` on the original Sonin space, `W=(C_F D_S Pi)*:H->K` be Hilbert–Schmidt, and let `E_N` be an orthogonal finite-rank projection on the actual `K`. Define

\[
A_N=(E_N A E_N)|_{E_NK},\quad
Y_N=E_N A_N^{-1}E_NW,\quad
B_N=\operatorname{Tr}(W^*Y_N),\quad
\mathcal R_N=W-AY_N.
\]

Since `E_N R_N=0`, Galerkin orthogonality yields the exact energy identity

\[
B_S[f]-B_N
=\|A^{-1/2}\mathcal R_N\|_{\rm HS}^2
\le\ell_S^{-2}\|\mathcal R_N\|_{\rm HS}^2.
\tag{A15}
\]

For nested `E_N` converging strongly to `I_K`, the variational characterization gives `B_N` increasing to `B_S[f]`. This does not require operator-norm convergence of finite-rank projections. It is a meaningful fixed-test smoothing result and error certificate, provided one can construct actual-Sonin trial spaces and enclose the **full** Hilbert–Schmidt residual. Computing only its finite observed rows is not an enclosure. This controls `B_S` alone and supplies no inference that its limit is `Q`.

## 7. Making the Galerkin bound concrete

An actual-Sonin dense trial family exists without a finite cosine surrogate.
Choose a countable dense set of smooth compact functions in the positive-axis
space `R H=L²(1,infinity)`, apply the exact projection (11) of the audit,
discard dependent vectors, and orthonormalize. Their spans are nested and
dense in `K`, because `Pi(R H)=K`. This is a construction of the exact spaces,
not a claim that their matrix entries have already been enclosed.

The full residual norm in (A15) has a useful finite-matrix reduction. Let
`Q_N:C^N->K` be the isometry for one such trial basis, and put

\[
\mathsf H=WW^*,\quad h_0=\operatorname{Tr}\mathsf H,\quad
A_N=Q_N^*AQ_N,\quad H_N=Q_N^*\mathsf H Q_N,
\]
\[
J_N=Q_N^*\mathsf H A Q_N,\qquad K_N=Q_N^*A^2Q_N.
\]

Then `B_N=tr(A_N^{-1}H_N)` and direct expansion gives

\[
\boxed{\|\mathcal R_N\|_{\rm HS}^2
=h_0-2\Re\operatorname{tr}(A_N^{-1}J_N)
+\operatorname{tr}(A_N^{-1}K_NA_N^{-1}H_N).}
\tag{A16}
\]

The scalar `h_0=||C_F D_S Pi||²_HS` is an archimedean smoothed trace.
It is evaluated by the audit's calibration with the compact smooth kernel
`D_S F`; its support is the finite union of the translated supports. This
use of shifted kernels is allowed: the trace calibration holds for every
compact smooth kernel, without the short-support dominance hypothesis.
The matrix entries still use the actual `Pi` and full integrals. Thus (A16)
identifies finitely many quantities to enclose and retains the unseen tail.
It does not license dropping the part of the Hilbert–Schmidt norm outside
a computational box. Cancellation in (A16) requires outward error control.

The lower bound in (A15) is also available:
`u_S^{-2}||R_N||²_HS <= B_S-B_N`. At prime 2 alone, the upper error
multiplier is `(1-1/sqrt(2))^{-2}=6+4sqrt(2)`, about 11.657.
Neither this nor (A16) is uniform in all primes.

## 8. Specified first-prime family and total error gate

Fix `L=1`, `b=9/20`, and define

\[
\phi(x)=\begin{cases}
\exp[-1/(1-(x/b)^2)],&|x|<b,\\0,&|x|\ge b,
\end{cases}\quad
h_0^{\rm src}=\phi,\quad h_1^{\rm src}=x\phi,
\]
\[
f_j=\frac{(-\partial_x^2+1/4)h_j^{\rm src}}
{\|(-\partial_x^2+1/4)h_j^{\rm src}\|_2},\qquad j=0,1.
\tag{A17}
\]

These are exact smooth compact moment-zero sources, respectively additive
even and odd, orthonormal in ordinary `L²`. Their two-dimensional complex
span is admissible. The support diameter is `9/10>log 2`, so the family
can probe the first-prime correlation. No optional mean-zero constraint
is imposed. This family is a specified starting diagnostic, not a claim
to attain the constrained minimum or reproduce the old unrestricted
Table 2 weak vectors. No normalized source energies have been evaluated.

For one normalized source, a meaningful numerical report must separately
enclose `B_2`, `E_infinity`, `Delta_2`, and
`a_2=(log 2)/sqrt(2)(kappa(log 2)+kappa(-log 2))`. Then

\[
R_{2,1}=-E_\infty-\Delta_2-a_2,\qquad
Q_1=B_2+R_{2,1}=\Gamma_1-a_2.
\tag{A18}
\]

Do not obtain `Delta_2` solely by subtracting a direct value of `Q_1`.
The direct right side is a cross-check of independently evaluated pieces.
The required error budget can now be stated precisely:

1. **Positive trace.** Enclose `B_N` and the full residual in (A16), yielding
   `B_2 in [B_N, B_N+ell_2^{-2}||R_N||²_HS]`, with outward matrix-entry
   and inverse errors included.
2. **Prolate error.** A bound `||e-e_approx||_infinity<=epsilon_e` gives
   an integral error at most `||F||_1² epsilon_e <= L epsilon_e` on
   a unit `L²` source. Include spectral truncation, computed eigenvectors,
   eigenvalues, their evaluation quadrature, and conditioning in this bound.
   Add a separate enclosure for quadrature of the final `kappa e` integral.
3. **Return moments.** For enclosures
   `|x_n-Tr(T_n(T)X)|<=epsilon_n`, the Chebyshev evaluation error is at most
   \[
   \frac r{1-r^2}\left(\epsilon_0+
       2\sum_{n=1}^M r^n\epsilon_n\right)
   +\frac{2r}{1-r^2}\frac{r^{M+1}}{1-r}\,4 B_\infty^{\rm upper}.
   \tag{A19}
   \]
   Each `epsilon_n` must include the actual projection and full trace
   error. Selfadjoint contractivity of a finite numerical matrix alone
   does not bound its difference from the actual return moment.
4. **Sources and arithmetic.** Enclose normalization, source derivatives,
   and the prime correlation. If using an approximate source, control it
   in the logarithmic form norm and enforce or enclose both moments. A
   nonneutral numerical replacement also needs an enclosure for its pole
   term and the error of replacing the exact source in (A18).
   The exact sources in (A17) require no moment correction analytically.

The total absolute error for the first expression for `Q_1` in (A18) is
the sum of these four contributions; the residual error omits the positive
trace contribution. The direct check has its own gamma and prime error.
To test a sign at a proposed scale `tau`, the corresponding total enclosure
must resolve that scale. The script's `10^{-8} B_infinity` bound is only
the return-series component: it is not an absolute `10^{-8}` trace error
or a resolution of either old Table 2 benchmark.

The numerical stage is **not passed in this session**. In particular, no
certified actual-Sonin trial matrix, Hilbert–Schmidt residual, or return
moment enclosure has been computed. Formula (A16) isolates the next
single implementable lemma: give certified enclosures of its scalar and
matrix entries, including the infinite spatial tails, for a nonzero trial
space generated by the actual projection and the two sources (A17).
Establishing that lemma would permit a bounded trace diagnostic. It would
still leave the signed arithmetic covariance estimate in (A10) open.

## 9. Rechecked small-cutoff obstruction

The recovered non-Hilbert–Schmidt claim is correct for its stated operator.
For one prime let `F_p=d F_infinity d^{-1}` and let `B_n` on `L²(0,1)`
have kernel `2 cos(2 pi p^n xy)`, including `n=-1`. The geometric series
for `d^{-1}` and Fourier reversal of dilation give

\[
\chi\mathcal F_p\chi
=(1-p^{-1})\sum_{n\ge0}B_n-p^{-1}B_{-1},\qquad
\|B_n\|\le p^{-n/2}\ (n\ge0).
\tag{A20}
\]

This converges in operator norm to a compact operator. With
`j(z)=Si(z)/z`, `j(0)=1`, direct integration yields

\[
\langle B_m,B_n\rangle_{\rm HS}
=2j(2\pi(p^m-p^n))+2j(2\pi(p^m+p^n)).
\tag{A21}
\]

The diagonal is `2+O(p^{-n})`; for `0<=m<n` each off-diagonal entry is
`O_p(p^{-n})`, and the double off-diagonal sum is absolutely convergent.
Entries involving `B_{-1}` are summable as well. If `Y_N=sum_{n<N}B_n`,
then `||Y_N||²_HS=2N+O_p(1)` and
`Tr((chi F_p chi)Y_N)=2(1-p^{-1})N+O_p(1)`.
Each `Y_N` is trace class, so operator-norm convergence justifies this
trace calculation. Were `chi F_p chi` Hilbert–Schmidt, Cauchy–Schwarz
would bound the second trace by `O(sqrt N)`, a contradiction.
This proves compactness without Hilbert–Schmidt regularity for the exact
cutoff operator and prohibits copying an unsmoothed prolate-square trace.
It leaves the correctly smoothed comparison and (A15) intact.

## Assessment

The advance is the exact signed covariance/place-addition law (A5), (A9),
and (A10), the faster return expansion (A11), and the one-sided actual-trace
approximation certificate (A15)–(A16). These are usable lemmas, not a
residual-sign theorem. For this bounded continuation, the next task is the
actual-Sonin enclosure lemma specified after (A19). The RH-directed missing
ingredient remains a Sonin-specific signed estimate in (A10), or a proved
arithmetic fixed-test limit. The positive approximants in (A15) converge
to `B_S`, not to `Q`; this distinction prevents a circular positivity claim.
The finite-dimensional control (A14) refutes only a generic monotonicity
inference and implies no impossibility result for the Sonin program.
