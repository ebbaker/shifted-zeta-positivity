# A finite spectral target at cofactor bandwidth

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the serving variant and
configured effort are not inferred. Internal same-model analysis and cross-review, not independent specialist
refereeing. No new global exponent or mathematical priority is claimed.

This continues the localized one-sided target with a proved bound for an
entire discarded frequency range. For the illustrative kappa=0.01, only
frequencies up to X^(1/1400) times a logarithmic factor remain; the tail
is already within O(X^(-1/200)). The central signed integral still needs
an arithmetic estimate. This is an unconditional reduction, not a proof
of that estimate.

Two parallel attempts are recorded in the
[short-interval dispersion note](SHORT_INTERVAL_DISPERSION_GATE_20261004.md)
and [arithmetic closure note](ARITHMETIC_CLOSURE_ATTEMPT_20261004.md).
The first identifies a stronger-strip assumption hidden in an uncentered
variance shortcut. The second retains exact arithmetic edge terms and
makes the deterministic zero-mode boundary error affordable, including
multiple zeros. Neither closes the target.

## Exact scalar reduction

Retain the definitions and hypotheses of the
[aggregated-kernel continuation](AGGREGATED_KERNEL_CONTINUATION_20261004.md)
and [mixed-discrepancy derivation](MIXED_DISCREPANCY_FEEDBACK_20261004.md). Put

\[
H=X/U^2,\qquad V=CX/U=CUH,\qquad
K_0(v)=\sum_{k\ge1}\ell(kv),\qquad
L(z)=\int_A^C\ell(v)v^{z-1}\,dv.
\]

The seventh-order Poisson estimate already established for ell gives
\(K_0(v)=O_w(v^6)\) at zero; K_0 is zero for v>=C. Its Mellin transform
is therefore holomorphic for Re z>-6, and continuation from Re z>1 gives

\[
\int_0^C K_0(v)v^{z-1}\,dv=\zeta(z)L(z).
\tag{1}
\]

In particular the pole at z=1 is removable, since L(1)=0. Write
\(W(\tau)=\zeta(1+i\tau)L(1+i\tau)\), with its continued value
\(W(0)=L'(1)=q c_w\).

Because the compactly supported function r->exp(r)ell(exp(r)) has seventh
distributional derivative a finite measure, its Fourier transform obeys
\(L(1+i\tau)=O_w((1+|\tau|)^{-7})\). Euler summation gives
\(\zeta(1+i\tau)=O(\log(2+|\tau|))\) for |tau|>=1. One elementary
proof takes N=ceil(|tau|) in

\[
\zeta(z)=\sum_{n\le N}n^{-z}+\frac{N^{1-z}}{z-1}
+O_\sigma(N^{-\sigma}+|z|N^{-\sigma}),\qquad\sigma=\Re z>0,
\]

where the last term comes from integrating the bounded first periodic
Bernoulli function. It follows that

\[
|W(\tau)|\ll_w(1+|\tau|)^{-7}\log(2+|\tau|).
\tag{2}
\]

Thus Mellin inversion on Re z=1 is an absolutely convergent integral.
No contour passes through any zero pole: W is the regular product zeta*L.

Let Q=J_0-R be the exact centered scalar in the mixed-discrepancy note;
R=O_w(H^{-8}) is its retained density remainder. Using A_U=mu_(>U)*1
before any estimate gives

\[
Q=\frac1{qX}\sum_{d>U}\mu(d)
\int_{(U,\infty)}K_0(dt/X)\,dE(t).
\tag{3}
\]

This is the original high-divisor grouping with d in (U,V], not the
complementary localized divisor interval (D,U]. The latter returns only
through the proved comparison with the original centered scalar.

The exact product support permits both variables to be capped at V.
Strict lower cutoffs and the right-continuous Stieltjes convention are
unchanged. Any term with d=V or t=V has dt/X>=C, so K_0=0; in particular
there is no unaccounted atom at the upper cap.

Define the finite arithmetic transforms

\[
\begin{aligned}
D_M(\tau)&=\sum_{U<n\le V}\frac{\mu(n)}n
(n/U)^{-i\tau},\\
D_E(\tau)&=\sum_{U<p\le V}\frac{\log p}p
(p/U)^{-i\tau}-\int_0^{\log(V/U)}e^{-i\tau r}\,dr.
\end{aligned}
\tag{4}
\]

The density term at tau=0 is log(V/U). Inserting Mellin inversion in
(3), permitted by (2) and finite total variation of dE on (U,V], gives

\[
\boxed{\quad
Q=\frac1{2\pi q}\int_{\mathbb R}
W(\tau)e^{i\tau\log H}D_M(\tau)D_E(\tau)\,d\tau.
\quad}
\tag{5}
\]

This expression uses a product, not an absolute square or a Hermitian
quadratic form. The negative-frequency summand is the conjugate of the
positive-frequency summand, so the integral is real. Formula (5) retains
all product endpoints and arithmetic signs. It is not an explicit
formula or a zero expansion.

## An elementary spectral-tail estimate

For U>=2, V>U, T>=1, put

\[
\Lambda=1+\log V,\qquad \mathcal L=1+\log(V/U).
\]

If |c_n|<=b, then

\[
\int_T^{2T}\left|\sum_{U<n\le V}\frac{c_n}n
(n/U)^{-i\tau}\right|^2\,d\tau
\ll b^2\left(T/U+\Lambda\mathcal L\right).
\tag{6}
\]

For completeness, the diagonal terms contribute O(b^2 T/U). Each
unordered pair m<n contributes at most O(b^2/(mn log(n/m))), since the
integral of its exponential is at most 2/log(n/m). The inequality
log(n/m)>=(n-m)/n gives

\[
\sum_{U<m<n\le V}\frac1{mn\log(n/m)}
\le\sum_{U<m\le V}\frac1m
\sum_{1\le h\le V-m}\frac1h
\ll\Lambda\mathcal L.
\]

This deliberately elementary estimate requires no deep mean-value theorem
and preserves all off-diagonal terms by a bound sufficient for the tail.

Apply (6) with c_n=mu(n), and with c_n=log n for primes and zero
otherwise. Cauchy--Schwarz gives

\[
\int_T^{2T}|D_M(\tau)D_P(\tau)|\,d\tau
\ll\Lambda\left(T/U+\Lambda\mathcal L\right),
\tag{7}
\]

where D_P is the prime sum in (4). The density transform is at most
2/|tau|. Its contribution to (7), with D_P replaced by that transform,
is bounded by

\[
O\left((T/U+\Lambda\mathcal L)^{1/2}T^{-1/2}\right),
\]

which is absorbed by the right side of (7). Thus (7) holds for D_E.
Combining it with (2) and summing dyadic frequency intervals proves

\[
\boxed{\quad
\left|Q-\frac1{2\pi q}\int_{-T}^T
W(\tau)e^{i\tau\log H}D_M(\tau)D_E(\tau)\,d\tau\right|
\ll_w\log(2T)\left\{
\frac{\Lambda}{U}T^{-6}+\Lambda^2\mathcal L T^{-7}
\right\}.
\quad}
\tag{8}
\]

No stronger hypothesis on M or E is used. This is a tail bound for the
actual arithmetic scalar, not only for deterministic test inputs.

For the balanced admissible cutoff

\[
U=X^{1/2-\kappa/28},\quad H=X^{\kappa/14},
\quad 0<\kappa<14/29,
\]

set

\[
T=H[\log(2X)]^{4/7}.
\tag{9}
\]

Since Lambda, mathcal L, and log(2T) are O_kappa(log(2X)), the second
term in (8) is O_(w,kappa)(H^{-7}). The first has, relative to H^{-7},
an extra factor O_(kappa)((H/U)[log(2X)]^{-10/7}), hence is smaller.
Consequently the finite signed transform

\[
\mathcal C_T(X)=\frac1{2\pi q}\int_{-T}^T
W(\tau)e^{i\tau\log H}D_M(\tau)D_E(\tau)\,d\tau
\tag{10}
\]

satisfies

\[
\boxed{\quad Q=\mathcal C_T(X)+O_{w,\kappa}(X^{-\kappa/2}).\quad}
\tag{11}
\]

Combining the existing centering and divisor-deletion estimates gives
\(\mathcal I_{(D,U]}=-q\mathcal C_T+O_{w,\kappa}(X^{-\kappa/2})\).
Specifically, the lower bound on localized I in (18) corresponds to an
upper bound on mathcal C_T, while the upper bound on localized I corresponds
to a lower bound on mathcal C_T; allowed constants change by q and the
comparison error. Either eventual one-sided target for the complete signed
transform (10), at scale X^(-kappa/2), is separately equivalent to the
original admissible target. For kappa=.01 its frequency cap is
X^(1/1400)[log(2X)]^(4/7).

The result removes all frequencies above this cap at an already affordable
error. It does not bound the remaining finite-band signed integral at the
required scale, and therefore does not prove an exponent improvement.
The kernel value W(0)=q c_w is nonzero, and every fixed real frequency
eventually lies in [-T,T]. Neither the finite bandwidth nor the
logarithmic buffer in the cap removes a fixed coherent spectral mode.

## What ratio-variable coherence says, and does not say

Let R_*=log H, L_*=log(CH), and define on [0,L_*]

\[
m(x)=M_U(Ue^x)/(Ue^x),\qquad e(y)=E_U(Ue^y)/(Ue^y).
\]

The exact mixed integral can alternatively be written

\[
Q=\frac1q\int_0^{L_*}\int_0^{L_*}
m(x)e(y)\,k(x+y-R_*)\,dx\,dy,
\quad k(r)=e^{2r}\mathscr F(e^r).
\tag{12}
\]

With Fourier convention hat k(tau)=int k(r) exp(-i tau r) dr, one has
hat k(-tau)=mathscr A(1+i tau). The multiplier appearing after Fourier
inversion and the replacement tau->-tau is therefore mathscr A(1+i tau).
Integration by
parts in each finite profile would produce both arithmetic transforms
in (4) and endpoint terms. Those endpoint terms cancel only after the
complete frequency integral is evaluated, because their product arguments
lie outside the support. The direct cofactor-kernel proof of (5) implements
that support fact before truncation and avoids losing this cancellation.

For elementary uncentered power modes with a common real part beta and
frequencies gamma, eta, the ratio-variable integral at fixed product
v=st/X contains exactly

\[
\int_0^{\log(Hv)}e^{i(\gamma-\eta)x}\,dx,
\qquad
\left|\int_0^{\log(Hv)}e^{i\Delta x}\,dx\right|
\le\min\{\log(Hv),2/|\Delta|\}.
\tag{13}
\]

For v bounded away from zero the natural coherence width is therefore
1/log H. A fixed separation only gains a reciprocal logarithm relative
to the diagonal bound. It supplies no power of H. Formula (13) concerns
explicit test inputs, not an expansion of M or E; lower-cutoff increments
add the already identified boundary terms, which must also be retained.

One must also avoid throwing away the low-product end on this heuristic.
The crude bounds |M_U(s)|<<s and |E_U(t)|<<t, together with
mathscr F(v)=O(v^3), give on 1/H<=v<=b/H, for any fixed b>1, only

\[
O_w\left(\int_{1/H}^{b/H}v^4\log(Hv)\,dv\right)
=O_{w,b}(H^{-5}).
\tag{14}
\]

This upper bound is larger than the target H^{-7}; it is not a lower
bound or an obstruction theorem. It says that the full arithmetic and
endpoint cancellation is still needed if that corner is removed.
The finite-spectrum target (10) keeps it automatically.


## Verification and the remaining analytic target

The [internal review](../../../reviews/01_signed_arithmetic_covariance/LOCALIZED_TARGET_ATTEMPT_REVIEW_20261004.md)
records independent same-model checks of the Mellin inversion, elementary
mean-square estimate, logarithmic cutoff budget, endpoints, and both
companion attempts. The [exact checker](../../../numerics/01_signed_arithmetic_covariance/check_localized_target.py)
passed 2,592 finite algebra comparisons; its
[record](../../../numerics/01_signed_arithmetic_covariance/localized_target_record_20261004.json)
includes source hashes and explicit limits. It does not numerically certify
Fourier inversion, tail bounds, derivative constants, or an asymptotic
arithmetic saving.

The next estimate to attempt is one sign of the actual complete central
integral (10). The elementary mean-square argument in (6) was sufficient
only where the fixed multiplier decays at high frequency. Applying its
absolute-value bound to the central range does not establish the target.
A useful next proof must estimate the signed product D_M D_E with its
phase and density term retained, or control the coherent mean together
with the centered term in the short-interval representation. No such
estimate has been obtained in this continuation. The manuscript and
existing certificate records remain unchanged; no commit or snapshot is
created.
