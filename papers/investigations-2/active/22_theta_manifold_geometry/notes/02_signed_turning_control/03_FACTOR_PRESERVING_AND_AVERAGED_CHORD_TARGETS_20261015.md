# Factor preserving cutoff bounds and averaged chord criteria

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This note proves two conditional local collision criteria, a complete-source tail bound and exact averaged kernels. The coordinating review and collaborating readers checked the arguments. No theta-specific signed-core bound is proved. The manuscript remains unchanged.

## 1. A cutoff target that preserves the amplitude

Put

\[
W=h_j(t,x),\quad D=h_j(t,y)-h_{j+1}(t,y),\quad
\mathcal C_j=WD,\quad e=H(t,x)^2+H_x(t,x)^2,
\qquad j=0,1.
\]

The starting point has **complete** stationarity `h_(j+1)(t,x)=0`, and `h_j` is nonzero on the entire rightward interval `[x,y]`. In both branches `|W|<=sqrt(e)`. At a finite collision of multiplicity `2r+j`, the established full predecessor and fixed-endpoint theorem give, for a sufficiently small fixed `delta>0`,

\[
x=\chi(s),\quad t=T-s,\quad y=a+\delta,\qquad
e\longrightarrow0,\quad
\frac{\mathcal C_j(T-s;\chi(s),a+\delta)}{\sqrt e}
\longrightarrow-d_\delta<0.
\tag{1}
\]

Here the energy is always the physical energy at the starting point. In particular, branch 1 does not replace it by `h_1^2+h_2^2`.

**Mixed-remainder exclusion lemma.** Suppose that on the admissible intervals one has, for every integer `N>=N_0`,

\[
\boxed{\mathcal C_j\ge-K_N e-\varepsilon_N\sqrt e,}
\qquad K_N\ge0,\quad\varepsilon_N\ge0,\quad\varepsilon_N\to0.
\tag{2}
\]

For each fixed N, `K_N` must have a finite local upper bound through the candidate event, uniformly in the covered endpoints. The error `epsilon_N` is a source-prescribed local bound, independent of the approaching energy. There must be a fixed positive spatial endpoint reach for arbitrarily large N, so that the same fixed endpoint in (1) is covered. A common event neighborhood and allowed length suffice. The time threshold can depend on N, provided every fixed N eventually covers the predecessor and this endpoint.

Then every covered finite collision is excluded. No growth-rate restriction on `K_N` is needed.

**Proof.** Fix N before taking `s` to zero. Divide (2) by `sqrt(e)` along (1). Local boundedness gives `K_N sqrt(e)->0`, and hence `-d_delta>=-epsilon_N`. This holds for arbitrarily large N, contradicting `epsilon_N->0`. The argument applies to both branches using the established physical-energy asymptotic in (1). It does not interchange two limits or require a jointly uniform bound on all `K_N`.

If the admissible spatial length shrinks to zero with N, the same fixed endpoint need not remain available and this argument fails. A shrinking-length version would require additional quantitative comparison with `d_delta`; none is claimed here.

This is a distinct target from a pure-tail family `C_j>=-K_N e-beta_N`. Dividing that family by `sqrt(e)` does not permit the fixed-N limit, because `beta_N/sqrt(e)` diverges. Preserving the starting amplitude can therefore remove a cutoff rate-gap requirement. The existence of (2), however, remains substantive and unproved for theta.

## 2. An exact endpoint-only theta cutoff and its tail

Use the complete physical modes already defined in the manuscript:

\[
\phi_n(u)=e^u(2\pi^2n^4e^{8u}-3\pi n^2e^{4u})e^{-\pi n^2e^{4u}},
\quad
H_n(t,z)=\int_0^\infty e^{tu^2}\phi_n(u)\cos(zu)\,du.
\]

Define

\[
D_N(t,y)=\sum_{n=1}^N
\{\partial_y^jH_n(t,y)-\partial_y^{j+1}H_n(t,y)\}.
\]

Keep `W=h_j(t,x)` **complete**, including every theta coefficient. Then the identity

\[
\boxed{\mathcal C_j=W D_N+W(D-D_N)}
\tag{3}
\]

holds exactly. This definition uses the source directly and does not drop any primitive endpoint or replace the physical heat factor.

Here is one explicit uniform tail. Fix a finite real upper time bound `T_*` and put

\[
S_4=\sum_{n\ge1}n^4e^{-\pi n^2/4},\qquad
B_j(T_*)=2\pi^2S_4\int_0^\infty
(u^j+u^{j+1})e^{T_*u^2+9u-(\pi/2)e^{4u}}\,du.
\tag{4}
\]

Both positive quantities are finite and prescribed independently of the observed energy. For every real y, `t<=T_*`, and `N>=0`,

\[
\boxed{|D-D_N|\le B_j(T_*)e^{-\pi(N+1)^2/4}.}
\tag{5}
\]

Indeed `0<phi_n(u)<=2 pi^2 n^4 exp(9u-pi n^2 e^(4u))` on the half-line. For `n>=1`, `u>=0`,

\[
\pi n^2e^{4u}\ge\frac\pi2n^2+\frac\pi2e^{4u},
\]

and

\[
\sum_{n>N}n^4e^{-\pi n^2/2}
\le e^{-\pi(N+1)^2/4}S_4.
\]

The absolute spectral derivatives are bounded by the extra factors `u^j` and `u^(j+1)`. Integrating these inequalities proves (5), and also justifies the complete tail exchange. The constant requires no spectral-height bound because all spectral arguments here are real.

Consequently, the following **unproved finite-core certificate** would suffice:

\[
\boxed{h_j(t,x)D_N(t,y)\ge-K_NE(t,x)}
\tag{6}
\]

on the complete stationary, zero-free domain, with the local coverage and fixed-N boundedness specified above. Combining (3), (5), and `|W|<=sqrt(e)` gives (2) with `epsilon_N=B_j exp(-pi(N+1)^2/4)`.

The easy tail bound is not the missing sign theorem. In particular, (6) cannot be established by defining `K_N` as a quotient with denominator E and assuming that quotient remains bounded. Nor may complete stationarity be replaced by stationarity of the truncated source. Any proof must identify the coefficient relation that supplies the finite-core lower bound independently of the desired collision exclusion.

## 3. Optional quantitative rate, including integer rounding

Suppose a proposed proof gives the more specific common-domain family

\[
\mathcal C_j\ge-Ae\exp(aN^2)-B\sqrt e\exp(-cN^2),
\quad A,B,a\ge0,\ c>0,\ N\ge N_0,
\tag{7}
\]

with fixed local constants. Set `kappa=a+c`, `D_0=N_0+1`, and

\[
p=\frac{a+2c}{2(a+c)}>\frac12,\quad L=\log(1/e),\quad
N=\left\lceil\max\left(N_0,\sqrt{\frac L{2\kappa}}\right)\right\rceil
\quad(0<e\le1).
\]

Since `sqrt(L/(2 kappa))<=N<=D_0+sqrt(L/(2 kappa))`,

\[
\boxed{\mathcal C_j\ge-e^p\left[
A\exp\left(aD_0^2+2aD_0\sqrt{\frac L{2\kappa}}\right)+B
\right].}
\tag{8}
\]

This is `o(sqrt(e))`; for each fixed `1/2<gamma<p` it is bounded below by `-K_gamma e^gamma` near zero. The rounding factor is retained. Unlike the corresponding pure-tail estimate, (7) needs no inequality between a and c. If a is zero, the same formula holds with p=1. The qualitative lemma remains valid even for growth of `K_N` faster than Gaussian; a power improvement is then not asserted.

## 4. Exact stationarity subtraction and the remaining calculation

For `c_j(z,u)=u^j cos(zu+j pi/2)` and `d_j(y,u)=c_j(y,u)-c_(j+1)(y,u)`, complete stationarity gives, for any real scalar alpha and beta,

\[
\mathcal C_j=\beta W^2+
W\int_0^\infty e^{tu^2}\Phi(u)
\{d_j(y,u)-\beta c_j(x,u)-\alpha c_{j+1}(x,u)\}\,du.
\tag{9}
\]

This is an identity, not a favorable sign representation. It is a useful starting form for inserting the full elliptic coefficient recurrence or modular reflection before estimating the remainder. A successful construction must produce a one-sided estimate such as (6), or a direct version of (2), while preserving the complete starting factor.

Truncating both factors usually loses this advantage. If `W=W_N+r_N` and `D=D_N+s_N`, a bound for `W_N D_N` introduces the term `r_N D_N`, whose absolute estimate has no small complete starting factor. Reorganizing as (3) avoids that term, but the certificate for `W D_N` must actually retain complete W; merely relabeling a doubly truncated calculation does not suffice.

The bounded next calculation is therefore to derive one coefficient-coupled expression for the complete-start, truncated-endpoint core in (6), state the sign mechanism and its local domain, and test that same rule against the existing collision controls. The arithmetic finite-core estimate, rather than the Gaussian tail or its rate, is the unresolved part.


## 5. Positive averages retain the collision obstruction

Let `H_t=-H_xx` be jointly real analytic, with no identically zero spatial slice. Write `h_j=∂_x^j H`, `E=H²+H_x²`, and `W=h_j`, for `j=0,1`. Fix once and for all a nonnegative smooth function `ρ` compactly supported in `(0,1)`, normalized by `∫₀¹ρ(v)dv=1`, and a prescribed sequence `δ_k>0` with `δ_k→0`. These choices are independent of any hypothetical collision.

Define the averaged endpoint factor and averaged chord by

\[
 B_{j,\delta}(t,x)
 =\int_0^1\rho(v)\{h_j(t,x+\delta v)-h_{j+1}(t,x+\delta v)\}\,dv,
 \qquad
 \overline{\mathcal C}_{j,\delta}(t,x)
 =h_j(t,x)B_{j,\delta}(t,x).
\]

Suppose `H` has exact spatial multiplicity `2r+j` at `(T,a)`, with `r≥1`, and let `χ(s)` be the full stationary predecessor of `W`: `W_x(T-s,χ(s))=0`. Put

\[
 a_0=\frac{\partial_x^{2r}W(T,a)}{(2r)!}\ne0,
 \qquad k=\frac{\partial_x^{2r}W(T,a)}{r!}.
\]

For every sufficiently small fixed `δ>0`,

\[
 \frac{\overline{\mathcal C}_{j,\delta}(T-s,\chi(s))}
 {\sqrt{E(T-s,\chi(s))}}
 \longrightarrow-D_\delta<0,
\]

where

\[
 -D_\delta
 =\operatorname{sgn}(a_0)
 \int_0^1\rho(v)\{W(T,a+\delta v)-W_x(T,a+\delta v)\}\,dv
 =-2r|a_0|\delta^{2r-1}m_{2r-1}+O(\delta^{2r}),
\]

and `m_q=∫₀¹ρ(v)v^q dv>0`.

**Proof.** The manuscript's stationary-predecessor calculation gives

\[
 W(T-s,\chi(s))=ks^r(1+O(s)),\qquad
 E(T-s,\chi(s))=k^2s^{2r}(1+O(s)).
\]

This uses physical starting energy on both branches. For `j=0`, `E=W²` exactly on the predecessor; for `j=1`, `H(T-s,χ(s))=O(s^{r+1})`, so `E=W²(1+O(s²))`. Consequently `W/√E→sgn(k)=sgn(a₀)`. At each fixed `δ`, continuity is uniform in `v∈[0,1]`, so the averaged endpoint factor tends to its value at `(T,a)`. The expansions

\[
 W(T,a+z)=a_0z^{2r}+O(z^{2r+1}),\qquad
 W_x(T,a+z)=2ra_0z^{2r-1}+O(z^{2r})
\]

give the displayed asymptotic as `δ→0`; its leading moment is strictly positive. This proves the negative limit. The positive leading heat polynomial in the manuscript additionally proves that the entire interval `[χ(s),χ(s)+δ]` is `W`-zero-free for sufficiently small `s`, after choosing `δ` sufficiently small. Thus an optional zero-free-window restriction in a candidate estimate is automatically met near the event. ∎

It follows that **bounds only for the prescribed countable family of scales are sufficient**. Near each candidate event, suppose for both branches and every sufficiently large fixed `k` there is a prescribed modulus

\[
 \overline{\mathcal C}_{j,\delta_k}(t,x)
 \ge-\omega_{j,k}(E(t,x)),\qquad
 \omega_{j,k}(e)=o(\sqrt e),
\]

at full stationary starts, uniformly through the event on the declared covered neighborhood. The neighborhood must contain the sufficiently close full predecessor and its fixed-`k` windows. Then there is no covered finite multiple real zero: choose `k` first so that `D_{δ_k}>0`, and then let `s→0`. **No uniformity as `k→∞` and no estimate for every individual endpoint is needed.** One cannot instead select a single scale `δ=δ(s)→0` while taking the collision limit; that changes the argument.

A useful factor-preserving sufficient hypothesis is, for each such fixed `k`,

\[
 \overline{\mathcal C}_{j,\delta_k}
 \ge-K_{j,k,N}E-\varepsilon_{j,k,N}\sqrt E
 \quad\text{for every sufficiently large integer }N,
\]

where each fixed-`N,k` coefficient is locally uniformly finite through the event and `ε_{j,k,N}→0` as `N→∞`, uniformly over the declared starts. There is **no required growth bound on `K_{j,k,N}` as `N→∞`**. Choose `k`, then choose `N` with `ε_{j,k,N}<D_{δ_k}/2`, then let `s→0`; division by `√E` gives a contradiction. The spatial window at this fixed `k` must remain admissible for those `N`. An `N`-dependent sufficiently-small-time threshold is harmless because `N` is fixed before `s→0`. A shrinking `N`-dependent spatial reach is not automatically harmless.

## 6. The exact averaged source kernel

Write `μ_t(u)=e^{tu²}Φ(u)` for the complete source and

\[
 c_j(x,u)=\Re[(iu)^j e^{ixu}],\qquad
 M_\rho(\zeta)=\int_0^1\rho(v)e^{i\zeta v}\,dv.
\]

Then, directly by differentiation and Fubini,

\[
 B_{j,\delta}(t,x)
 =\int_0^\infty\mu_t(u)b_{j,\delta}(x,u)\,du,
 \qquad
 \boxed{b_{j,\delta}(x,u)
 =\Re[(iu)^j(1-iu)e^{ixu}M_\rho(\delta u)].}
\]

The full symmetric bilocal kernel is

\[
 \overline T_{j,\delta}(x;u,v)
 =\tfrac12\{c_j(x,u)b_{j,\delta}(x,v)
             +c_j(x,v)b_{j,\delta}(x,u)\},
\]

so

\[
 \overline{\mathcal C}_{j,\delta}
 =\int_0^\infty\!\int_0^\infty
 \mu_t(u)\mu_t(v)\overline T_{j,\delta}(x;u,v)\,du\,dv.
\]

This is an identity, with the full starting factor and complete physical stationarity retained. The manuscript's covariant insertion can replace `Φ(u)Φ(v)` without any change in its normalization.

For the primitive variables `8h_j=I_j+δ_{j0}/2`, put

\[
 \overline I_{j,\delta}(t,x)
 =\int_0^1\rho(v)\{I_j(t,x+\delta v)-I_{j+1}(t,x+\delta v)\}\,dv.
\]

The complete affine endpoint formula is

\[
 \boxed{64\overline{\mathcal C}_{j,\delta}
 =\bigl(I_j(t,x)+\tfrac12\delta_{j0}\bigr)
  \bigl(\overline I_{j,\delta}(t,x)+\tfrac12\delta_{j0}\bigr).}
\]

Thus averaging does not dispose of the lower endpoint or corner terms.

## 7. Endpoint truncation for the averaged probe

If `B_{j,δ,N}` approximates **only the endpoint factor** with a proved uniform error `|B_{j,δ}-B_{j,δ,N}|≤ε_{j,δ,N}`, then

\[
 |\overline{\mathcal C}_{j,\delta}-h_j(t,x)B_{j,\delta,N}(t,x)|
 \le\varepsilon_{j,\delta,N}|h_j(t,x)|
 \le\varepsilon_{j,\delta,N}\sqrt{E(t,x)}.
\]

No Young inequality is needed. A finite-core signed estimate `h_j B_{j,δ,N}≥-K_{j,δ,N}E`, with the required local coverage, would therefore yield the mixed-tail criterion above regardless of the cutoff growth of `K`. This estimate remains unproved for theta. A separately truncated starting factor can destroy this useful exact error structure, and the stationary start must remain a zero of the complete `h_{j+1}`.

For each fixed `δ>0`, smooth compact support gives `|M_ρ(δu)|≤C_{m,ρ}(1+δ|u|)^{-m}` for every integer `m≥0`, by integration by parts. Thus averaging supplies explicit source-frequency decay and freedom to shape the endpoint test. This does **not** prove a favorable sign, does not provide decay in the starting spectral coordinate `x` by itself, and does not establish the missing arithmetic inequality. Its usefulness is a research hypothesis; the local exclusion implication and displayed identities are the proved results of this note.


## Sources and scope

The [integrated manuscript](../../manuscript/theta_manifold_geometry.tex) supplies the full stationary predecessors, fixed-endpoint collision law, complete source conventions and primitive affine terms. See also the [starting-energy chord note](02_CENTRAL_ENERGY_CHORD_AND_CUTOFF_TRANSFER_20261015.md), [complete signed bridge](../03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md), and [reflection-rigidity note](../05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md). The earlier chord note already records a full-amplitude tail followed by Young's inequality; Sections 1–3 keep that factor through the collision limit. Sections 5–7 add the prescribed averaged probes.

These are analytic proofs and exact identities, not deductions from finite numerical tests. The remaining arithmetic core estimate is unproved. The [research assessment](../../reviews/05_RESEARCH_PROGRESS_AND_PRIORITY_PATHS_20261015.md) explains the proposed coefficient-translation experiment and the competing research paths.
