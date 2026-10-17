# Coupled theta products, preserved cancellations and the next signed target

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [19](../../chat-histories/0019_2026-10-15T13-36-13Z_review-research-paths.json) now use this investigation's [local registry](../../chat-histories/index.json), as recorded in the [relocation receipt](../../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. This is the additional continuation requested after the coefficient-core research cycle. The existing formal-replay conversation remains history **19**; its integrity and prior final capture have been verified. The manuscript remains unchanged.

## What the leading-priority experiment established

The coupled arithmetic experiment has now been carried out. It supplies an exact theta product identity at **independent** source parameters, the complete double source operator, a coefficient-rigidity statement, and concrete reasons the natural positive-Gram interpretation fails. Two further notes identify which cancellations an admissible estimate must retain. No theta signed-core bound has been proved.

| New note | Main result | Consequence |
| --- | --- | --- |
| [Coupled theta product and parity sectors](../03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md) | Mixed theta addition, full double fourth-jet operator, Gaussian-weight rigidity, and indefinite parity source matrices | The simplest positive-Gram construction is false, even with a zero-sum coefficient constraint |
| [Parity strip and complete starting factor](../03_theta_bundles_and_connections/07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md) | Exact endpoint-cutoff geometry, finite-box correction, and actual-theta algebraic parity tails | Keep the complete starting direction and recombine both parity sectors before measuring the error |
| [Reflected source and mixed exchange sectors](../05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md) | Exact full/cutoff center-separation identity and an explicit reflected positive-source collision | The odd exchange sector is essential; reflection and generic source/Fourier positivity do not supply the missing sign |

## 1. The genuinely coupled identity

Let `q=e^(4u)`, `r=e^(4v)`, `p=n+m`, `k=n−m`, `X=z+w`, `Y=z−w`. The two-source lattice has `p≡k (mod 2)` and quadratic form

\[
Q_{q,r}(p,k)=\frac{q+r}{4}(p^2+k^2)+\frac{q-r}{2}pk.
\]

The full product is the mixed-heat operator

\[
\exp\!\left(\frac{q-r}{2\pi}\partial_X\partial_Y\right)
\sum_{\epsilon=0}^1\vartheta_\epsilon(X,i(q+r))
                       \vartheta_\epsilon(Y,i(q+r)).
\]

The derivative series converges under the explicit Gaussian margin `q+r−|q−r|=2min(q,r)>0`. The mixed derivative cannot be dropped: equal parameters mean only the diagonal u=v of the physical double integral.

The complete physical source insertion produces the coefficient

\[
M_{p,k}(u,v)=\tfrac14
\phi_{|(p+k)/2|}(u)\phi_{|(p-k)/2|}(v),\qquad\phi_0=0.
\]

Its same-parity source matrices have zero diagonal and positive off-diagonal entries. The even block on indices `{0,2}` and odd block on `{1,3}` have negative determinants. Each block also has both signs on its zero-sum subspace, as shown by explicit three-index witnesses and uniform source-mode ratio bounds. Adding a scalar multiple of the all-ones matrix cannot repair these witnesses. A physical stationarity constraint is a different condition; it is not ruled out by this calculation.

There is useful arithmetic content before source projection. For positive even polynomial-growth weights with a_0=1, rank one of

\[
C_0(a,b)=a_{a+b}a_{a-b}
\]

forces `a_n=c^(n²)`, `0<c≤1`. The normalized primitive endpoint forces c=1. Finite positive square controls fail this relation. The zero-mode coefficients used in the rigidity proof are annihilated by the source operator, so this argument must not be silently inferred from the projected matrix alone. Input rigidity remains distinct from output sign.

## 2. Two independent cancellations must survive the calculation

The endpoint cutoff `|m|≤N` becomes the **infinite strip** `|p−k|≤2N`, with the complete starting direction left unbounded. A rectangular parity cutoff additionally imposes `|n|+|m|≤M` and computes

\[
Q_{j,N,M}=\sum_{m=1}^N\ell_{j,m}(t,x+\delta)W_{M-m}(t,x).
\]

Its omitted term is a sum of incomplete-start tails. An absolute bound is Gaussian but lacks √E. The exact correction must be retained, or a separate pure-tail theorem must pay that cost. The earlier mixed-error theorem does not apply automatically.

The arithmetic parity split introduces a difference observation `W_-=W_e−W_o` in addition to the physical `W_+=W_e+W_o`. Its two amplitude sectors are `(A+B)/2` and `(A−B)/2`, where `B=W_-²−e^(−δ)W_-V_-`. Only recombination removes B.

For actual theta, this cancellation is quantitatively substantial. Define β=−Φ_e′(0)>0. At fixed heat time,

\[
h_{j,e}(t,x)=(-1)^j(j+1)!\beta x^{-j-2}+O(x^{-j-4}),
\qquad h_{j,o}=-h_{j,e}+O(x^{-M})
\]

for every fixed M, because the complete reflected source has Schwartz Fourier decay. For fixed δ>0 and complete endpoints,

\[
B\sim4[(j+1)!\beta]^2(1-e^{-\delta})x^{-2j-4}.
\]

Separate polynomial-height absolute sector bounds by √E are therefore impossible. This does not forbid coefficients merely locally finite at each finite event, or prove an impossibility for all coupled methods.

There is a second, different parity distinction in **physical** center/separation coordinates `a=(u+v)/2`, `b=(u−v)/2`. For a complete starting source and truncated endpoint, the exchange-even cosine–cosine sector and exchange-odd sine–sine sector are both required. They equal

\[
\tfrac12\{W(x)W_N(y)+W_N(x)W(y)\},\qquad
\tfrac12\{W(x)W_N(y)-W_N(x)W(y)\}.
\]

Dropping the second sector introduces an incomplete starting factor. At a complete starting zero the sectors can be nonzero and cancel exactly. These exchange sectors are not the arithmetic even/odd lattice sectors; both kinds of cancellation matter.

## 3. A precise control for reflection-only arguments

Set T=1/4 and

\[
\Phi_*(u)=c e^{-u^2/4}
\left(e^{-u^4}+\frac{e^{-(u-4)^4}+e^{-(u+4)^4}}2\right),
\]

with the positive constant c chosen to normalize the decaying Green primitive to ψ′(0)=−1/2. This source is positive, even and entire, has super-Gaussian real decay, and satisfies every odd primitive endpoint and every generic positive source/Fourier Gram constraint. At time T,

\[
H_*(T,x)=cF(x)(1+\cos4x),\qquad
F(x)=\int_0^\infty e^{-u^4}\cos(xu)\,du.
\]

The moment bound `F(x)≥M_0(1−x²/4)>0` for |x|<2 proves an exact double collision at x=π/4, with positive H_xx. The fixed-δ averaged defect has a strictly negative √E limit. The validated δ=1/4 value is approximately −0.011546502002.

This source cannot have a nonzero polynomial-growth integer-square source expansion: its logarithmic decay is quartic in u, while any such expansion is dominated by its first nonzero double-exponential mode. Thus it does not contradict the theta reflection-rigidity theorem. Its role is to rule out arguments that discard the arithmetic coefficients after obtaining reflection and ordinary Gram positivity. Investigation 21 Note 56 already supplies a different control with stronger additional shape properties; the new control's benefits are its exact time and its explicit mixed-sector cancellation.

## 4. The next bounded research task

The unconditional addition-basis Gram ansatz is now closed. Increasing its finite matrix size cannot remove a negative principal block. A scalar normalization correction is also insufficient. Source reflection, ordinary positive Gram forms, or omission of a mixed sector are not replacements for the missing arithmetic estimate.

The next test should use **one arithmetic correction tied to the full stationary constraint**, acting on the combined physical observation rather than on separate parity matrices. A useful exact target has the form

\[
\mathcal A_{j,1/N,N}+K_NE
=\mathcal P_N+\Lambda_N h_{j+1}(t,x)+R_N,
\]

where P_N has a justified nonnegative sign from coefficient relations not shared by the saved controls, the complete stationarity term vanishes, and `R_N≥−ε_N√E` with Gaussian or comparably sufficient ε_N. K_N and any required multipliers must remain locally finite through hypothetical finite events. This is a proposed certificate format, not an identity or sign result established in this cycle.

Keep the complete affine primitive endpoints or the corresponding unprojected coefficient data wherever the arithmetic correction uses them. Use the infinite endpoint strip and retain both exchange sectors. Reject a proposed correction if it merely returns the reindexed identity, assumes a positive matrix already disproved above, uses truncated stationarity, or pays a newly introduced error by an absolute source norm without an admissible transfer argument.

A certified stationary-point pilot becomes worthwhile after an explicit coefficient rule and remainder are derived. A larger numerical parity-matrix sweep is not the next step: the bounded Gram question has an analytic negative answer. No claim is made that the proposed constrained format must succeed.

## 5. Verification and chat history

The [internal review](../../reviews/07_COUPLED_PRODUCT_AND_REFLECTION_CONTROL_REVIEW_20261015.md) records independent analytic audits and replays. The [manifest](../../numerics/COUPLED_PRODUCT_CONTINUATION_CHECKS_20261015.json) binds the three new notes, checkers and receipts. The new replay passes **3,278 exact assertions** and **38 mixed or validated assertions**. Exact algebra and validated control integrals are distinguished from general analytic proofs and from the unproved theta sign.

The [history verification receipt](../../numerics/COUPLED_PRODUCT_CHAT_HISTORY_VERIFICATION_20261015.json) verifies the sole formal-replay registration, identity **19**, original creation and first-capture provenance, stored and canonical hashes, and the unchanged public-message prefix. It confirms that the preceding turn's real final answer was captured by its deferred worker and that its turn completed. The current turn's final answer is not claimed captured before it exists; the bounded exact-turn follow-up is arranged after the last refresh. Later legitimate refreshes change snapshot hashes without invalidating this checkpoint.

The unchanged manuscript is identified by SHA-256 `114611f06f0928827045399561d2f83ca6ca9abc1d35a9d5cd7d406c845aa417`. Its PDF and existing build record remain untouched. The new work is saved as research notes, with no new draft snapshot, commit, or RH conclusion.
