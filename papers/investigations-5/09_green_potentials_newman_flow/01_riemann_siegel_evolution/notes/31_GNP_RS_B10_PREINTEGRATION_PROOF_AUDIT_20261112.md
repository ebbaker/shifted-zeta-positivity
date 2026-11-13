# B10 pre-integration proof audit

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Child chat0008, thread
`01a1d1aa-91c3-7d61-9a0e-0754a0091281`. Actual model and reasoning
effort are unavailable in the recorded configurations. Three separate
internal agents rederived the Mellin, source/mean and low-mode steps.
They inherited their settings and shared the named inputs.

The four checks requested in [Note30][handoff] support [Note29][proof]
(B10.3), with the exact same \(17/81\) window exponent and power remainder.
The Green corollaries use the block cutoff \(P_U=\lfloor L_U^2\rfloor\).
In the final paragraph of Note29 §5, read the shorthand \(R_P\) in the
\(C/L_U\) transfer as \(R_{P_U}\). For general \(P\) the termwise argument
can retain the separate omitted-prime allowance \(O(P^{-3/2})\).
[Review16][review] records the disposition and integration edits.

The result is an averaged quantitative milestone under [avoid01][a01].
The [result index][results], [heat-flow cluster11][cluster] and [avoid
index][avoid] route to the related results. [Controls12][controls],
[premise02][a02], [scope07][a07], [separate-bounds12][a12] and
[imports16][a16] govern the applicability and source checks below.

## 1. Cutoff, Mellin contour and tails

The two transition intervals in (B10.5) are \((Z+1/4,Z+3/4)\) and
\((B+1/4,B+3/4)\). Thus \(b(n)=\sqrt n\,w_n\,{\bf1}_{Z<n\le B}\)
including \(n=Z,Z+1,B,B+1\). Put \(A_*=U^{-1/18}\) and \(y=\log x\).
The lower support endpoint has log \(\tfrac13\log U+O(U^{-1/3})\)
and the upper log is \(\tfrac12\log U+O(1)\). Uniformly there,
\(\log a(U^\alpha)=-\alpha(1-\alpha)\log U/4+O(1)\), and the
endpoint minimum of \(\alpha(1-\alpha)\) is at least
\(2/9-O(1/\log U)\). Hence \(\sup a\ll A_*\).

In \(y\), the derivative of \(a(e^y)\) is \(Da(e^y)\) with
\(D=-1/4+y/(2L)\), and the second derivative is
\((D^2+1/(2L))a(e^y)\). At most one turn gives total variation
\(O(A_*)\). On a transition at \(x\asymp N\), \(N=Z,B\), its
logarithmic width is \(O(1/N)\) and the cutoff derivatives in \(y\)
are \(O(N)\) and \(O(N^2)\). The product rule yields
\(\|g\|_1\ll A_*\mathcal L,\ \|g'\|_1\ll A_*,\
\|g''\|_1\ll A_*(\mathcal L+Z+B)\ll A_* B\), where \(g(y)=b(e^y)\)
and \(\mathcal L=1+\log U\).

Integrating by parts gives the kernel envelope
\(C A_*\min(\mathcal L,|v|^{-1},B|v|^{-2})\).
Splitting at \(1/\mathcal L,B,U\) gives \(L^1\) cost \(O(A_*\mathcal L)\),
log-weighted cost \(O(A_*\mathcal L^2)\) and \((U+|v|)^\theta\)-weighted
cost \(O(A_*U^\theta\mathcal L)\). The contributions from \(|v|>U\)
are bounded by \(C A_* B(\log U+1)/U\) and
\(C A_*B U^{\theta-1}/(1-\theta)\) for the two weighted moments.
The long-frequency range therefore stays inside the stated budgets.

The inversion convention is \(b(n)=(2\pi i)^{-1}\int_{(1)}
\widetilde b(z)n^{-z}\,dz\). For \(s=1/2-i\tau(u)\), absolute
convergence at \(\Re(s+z)=3/2\) permits the Dirichlet sum. Moving to
\(\Re z=0\) adds \(+\widetilde b(1-s)\) from the simple pole.
For fixed \(U,u\), compact smooth support gives arbitrary vertical
decay in the closed contour strip. For example,
\[
 \zeta(w)=\frac{w}{w-1}-w\int_1^\infty\{x\}x^{-w-1}\,dx
\]
gives polynomial growth on the horizontal sides, away from the pole.
For the residue the \(y\)-weight \(e^{y/2}a(e^y)\) is increasing and
at most \(C A_*\sqrt B\) on the support. Multiplication by the cutoffs
preserves a total-variation bound of that order. One integration by
parts and \(|\tau(u)|\asymp U\) yield \(O(A_*U^{-3/4})\).

## 2. Cumulative input and signed high-mode sum

[Bourgain–Watt v1, Theorem 4][bw] gives the cumulative error
\(E(V)\ll_\epsilon V^{1515/4816+\epsilon}\) for \(V\ge1\).
For \(\epsilon=151/144480\) this is \(O(V^{19/60})\) after enlarging the
constant at bounded \(V\). For \(1\le a\le b\le R\), subtract the
two cumulative identities. The main term integrates
\(\log(t/(2\pi))+2\gamma\) over \([a,b]\) and the two errors cost
\(O(R^{19/60})\). Reflection handles negative heights and the
intersection with \([-1,1]\) has bounded cost. This proves (B10.4)
for intervals of length at most \(c_*\ell\) and \(\ell\ge1\), with
\(c_*\) fixed.

Write \(K_*=\int |k(v)|\,dv\). Cauchy–Schwarz in \(|k|\,dv\) and
Tonelli give
\[
 \mathcal Q_{Z,B}\ll A_*^2U^{-3/2}
 +K_*\int_{\mathbb R}|k(v)|
 \left[\log(2+U+|v|)+\frac{(U+|v|)^\theta}{\ell}\right]\,dv .
\]
The map \(u\mapsto v-\tau(u)\) has \(|du/dt|=2\) and the
\(\chi\)-support maps to an interval of length \(5\ell/2\) contained
in \([-C(U+|v|),C(U+|v|)]\). This is (B10.11), since
\(A_*^2=U^{-1/9}\) and \(\theta-1/9=37/180\).
The positive-sign Fourier convention and \(\int\chi=4\) give
\(2|\Re\mathcal S_{Z,B}|=|\mathcal Q_{Z,B}-4\sum w_n^2|
\le\mathcal Q_{Z,B}+4\sum w_n^2\), with diagonal \(O(A_*^2\mathcal L)\).
This yields (B10.12) for the sum of all real quadratic contributions,
including resonances. An individual complex block modulus is outside
the estimate.

## 3. Lower modes and complete arm norms

In the comparable block \(N\le m<2N\), \(n=m+h<2m\), write
\(t=\tau(U)/(2\pi)\). For the conjugate phase
\(f=-t\int_0^h(x+s)^{-1}ds\) compare \(\varphi=-th/x\).
For every derivative order \(j\ge1\), the relative difference is at
most \((j+1)h/(2x)\). Fix the exponent-pair derivative order and
tolerance first, then choose the fixed small-shift cap \(\delta_0\)
so the relative difference is at most half the tolerance.
[Montgomery–Vaughan, Ch. 16][mv] gives this phase class with derivative
parameter \(2\) and scale \(th\), including arbitrary subintervals.
The \(B,A,A,B\) operations on \((0,1)\) give \((2/7,4/7)\).
Consequently the partial sum is
\(O((Uh)^{2/7}+N^2/(Uh))\). This supplies a citation without the
inconsistent parameter list in the Robert author copy used by
[B08][b08].

The weights decrease for \(x\le B\), with \(|w_x'|\ll w_x/x\).
The two weights on the block have product at most \(w_N^2\).
The Fourier argument derivative is \(O(\ell h/N^2)\); after integration
over a block, one additional decay power pays \(\ell h/N\).
Abel summation and
\(\sum_{h\ge1}h^{2/7}(1+\ell h/N)^{-A}\ll (N/\ell)^{9/7}\) for fixed
\(A\ge4\) give \(U^{2/7}N^{-3/14}\exp((\log N)^2/(2L))\ell^{-9/7}\).
The exact quadratic \(2/7-3\alpha/14+\alpha^2/2\) is convex on
\([1/10,1/3]\); its endpoint values are \(377/1400\) and \(17/63\),
separated by \(1/1800\). Floors and dyadic factors shift the logarithm
by \(O(1)\), and the \(O(\mathcal L)\) block count is paid. The extra
\(N^2/(Uh)\) term summed with the coarser weights is
\(O(U^{-1}Z^{3/4}\mathcal L)\), which fits \(O(U^{-5/8}\mathcal L)\).
For the complementary pairs the log ratio is bounded below by a fixed
positive constant. Fourth-power Fourier decay and the square of the
absolute coefficient sum pay \(O(U^{3/8}\ell^{-4})\). The low diagonal
is at most \(16Y^{-1/4}\).

The exact split at \(Z\) uses \(|D_{\rm low}+D_{\rm high}|^2\le
2|D_{\rm low}|^2+2|D_{\rm high}|^2\), which includes the cross pairs in
the norm bound. The smooth \(\chi\) majorizes the exact \(\sigma\) measure
for nonnegative norm squares on \(r_*\le\ell\le\sqrt U\).
The [B07][b07] freezing allowance on the full \(\chi\)-support is
\(O(\ell U^{-13/16}+(1+\ell/\sqrt U)U^{-5/16})\) in amplitude. The
second term counts the changing integer cutoff, and the first pays
weight and small-phase drift. This yields \(O(U^{-5/8})\) in the
norm square. The head diagonal is bounded and its minimum distinct
log spacing \(1/Y\) gives \(O(Y^{11/4}/\ell^2)\) off-diagonal.
This last term is bounded on the theorem's short-window range
\(U^{17/81+\rho}\le\ell\le\sqrt U\). There, the head and tail bounds
give (B10.17)–(B10.19).

## 4. Residual comparison, onsets and Green transfer

The [B07 ledger][b07] (B07.26) equals (B08.14) and (B10.20).
The factor \(1/2\) in Fubini with \(d\sigma=2W\,dx/\ell\) gives
the stated reflected, arm-replacement and multiplier constants.
The mass deficit costs at most \((4/\pi)\mu_P U^{-4}\).
The coefficient diagonal uses \(L_0=L_{U-r_*}\asymp L_U\) and gives
\(D_0=O(\sqrt{\mu_P}/L_U+L_U^{-2}+U^{-1/80})\), uniformly in \(P\)
since \(0\le\mu_P\le 2P^{-1/2}\). Here the \(1/L_U\) diagonal
error has no Euler-product factor.

At \(\beta=17/81\), \(M=U^{1/10}\), \(Y=\lfloor U^{1/10}\rfloor\),
\(\eta=1/8\), put \(q_\rho=\min(7/3240,9\rho/14)\).
The entries below use \(\ell\ge U^{\beta+\rho}\) and suppress
logarithms and the indicated product factors.

| Ledger input or term | Bound |
| --- | --- |
| \(A_1\), low modes | \(U^{-9\rho/7}\) |
| \(A_1\), high modes | \(U^{-1/9}+U^{-7/1620-\rho}\) |
| \(A_1\), diagonal and other terms | \(U^{-1/40}+U^{-301/648-4\rho}+U^{-5/8}\) |
| \(8H^2\sqrt{A_0A_1}\) | \(H^2 U^{-q_\rho}\), once \(A_0\) is bounded |
| \(s_0\) and \(c_0/2\) | \(U^{-4/405-\rho}\) and \(H^4 U^{-437/3240-\rho}/L_0\) |
| \(4T_M\sqrt{A_0 b_0},2T_M^2 A_0,2HT_M b_0\) | \(T_M,T_M^2,HT_M\) respectively, with \(A_0,b_0=O(1)\) |
| Complete field and clock | \(H^2(U^{-1/32}+r_*U^{-9/16})\) |
| Mass deficit | \(O(U^{-4})\) |

The head auxiliary off-diagonal has exponent
\(-469/3240-2\rho\). The \(T_M\) power is \(-1/80\) before
\(\exp(CP^{3/8})\), and \(H\le\exp(CP^{1/4})\).
Both \(A_0,b_0\) are bounded at a finite \(\rho\)-dependent onset.
The fixed exponent margins in the table all dominate \(q_\rho\).
Thus (B10.21) follows, and
\(\log(G(L_U^2)\mathcal L^{C'})=O(L_U^{3/4}+\log\mathcal L)\)
allows (B10.22). The resulting remainder is \(O_\rho(U^{-q_\rho/2})\).
For the closed overlap \(\sqrt U\le\ell\le U\), B08 with
\(\rho_8=19/72\) gives \(O(U^{-1/144})\), with the same \(P\).
At \(\rho=47/162\) the short range consists of \(\ell=\sqrt U\).

The common onset keeps the inherited HDA/E01/E04 chart, buffer,
correction and tail gates on the declared field domains. On the
arithmetic side \(r_*\ll\log U\), \(J\subset[U/2,3U]\), the smooth
support stays in positive comparable heights, \(L_0\ge16\),
\(2\le Y<Z<B\) and \(Y\le N_{U-2\sqrt U}\) hold eventually.
The auxiliary \(\nu'(u)=1/2-\pi/(8uL_u^2)\) is in \([1/4,1/2]\)
and \(\nu''>0\). For each retained reflected frequency
\(\omega=\log(kle/d)\), \(|\omega|\le 2\log Y+3\log M\le
\tfrac12\log U\). This is eventually \(\le(7/8)L_0\).
The curvature gate has left side \(O(U^{-2}/L_U)\), below
\(1/(12U)\). The same-arm and reflected integration by parts use
the exact weight variation and mass. The source, fixed smoothing
and exponent-pair gates have fixed parameters.

For the clock, the physical residual first uses \(1/L_X\) throughout
its spatial integral. Only the auxiliary arm is compared along
\(\lambda\) between \(1/L_X\) and \(1/L_x\) at fixed \(x\).
The clock displacement is \(O(r_*/(UL_U^2))\), and the derivative
of the auxiliary relative square is \(O(H^2L_U^2 U^{7/16})\).
Here \(T_1(P)=O(P^{1/4}\log P)\le L_U^2\) eventually, uniformly
for \(P\le L_U^2\). The full-field error \(O(U^{-1/4})\) paired
with the \(O(H U^{7/32})\) relative-arm envelope, after division
by the Euler reference, costs \(O(H^2U^{-1/32})\) in the square.
This recovers both clock terms with the inherited field provider.
The Mellin translations concern an auxiliary zeta variable and
leave this comparison intact.

For the Green consequence use \(P_U\) and \(X\in[U,2U]\), so
\(P_U\le L_X^2\) and \(L_X=L_U+O(1)\). In [E06][e06] the
bounds for the first and second Euler phase derivatives are
\(O(L_X^{3/4}\log L_X)\) and \(O(L_X^{3/4}(\log L_X)^2)\),
both \(o(L_X)\). The window gate \(R_X^w/X\le L_X/8\), positive
cutoff and inherited chart/tail gates also hold. The omitted prime
allowance is \(O(P_U^{-3/2})=O(L_U^{-3})\); the reference exterior
cost is \(O(P_U^{3/8}U^{-4})\) and the true logarithmic tail is
\(O(U^{-3}\log^2 U)\). Termwise application of (E06.6), with
\(\log(1+x)\le x\), gives
\[
 0\le J_{1/L_X}(X)
 \le\delta/4+R_{P_U}(X,1)/(2\delta^2)+C/L_U .
\]
The residual mean is \(\mu_{P_U}+O_\rho(L_U^{-3/2})=O_\rho(L_U^{-1})\).
Use \(\delta=L_U^{-1/3}\) for the \(O_\rho(L_U^{-1/3})\) Green mean.
For a fixed \(h>0\), take \(\delta/4\le h/4\) and \(C/L_U\le h/4\).
Then \(J\ge h\) implies \(R_{P_U}\ge h\delta^2\); Markov gives
\(O_{h,\rho}(L_U^{-1})\) for the proportion. All onsets remain
finite and unevaluated. At the handoff test \(\ell=U^{11/48}\),
the low/high norm powers are \(-25/1008\) and \(-17/720\), and the
previous B08 leading allowance has exponent \(1/112\).

## 5. Ancillary source check and collision screen

For (B10.23), the **left** inequality of Bourgain–Watt (7.3) gives
\(N_{\rm BW}(R-1)^2<C_3M_{\rm BW}^3/(2T)\). The right inequality
gives the opposite-sided comparison for \(N_{\rm BW}R^2\).
The integer \(R\ge2\) follows from \(H\ge1\) and \(H/R^2\le B_1<1\).
Then \(R^2\le4(R-1)^2\) and the two caps in (7.5) give
\(TH^2/M_{\rm BW}^3\le 2C_3B_1^2\).
For the block \(M_{\rm BW}\asymp\sqrt T,\ H\asymp M_{\rm BW}/\ell\)
with \(T\asymp U\), the expression grows as \(U^{1/36}\) at the
old B08 endpoint and faster below it. This exclusion applies to
retaining those internal setup gates at that scale.

The analytical screen identifies which inputs of the actual proof
fail for the named [controls][controls].

| Control | Failed input of the canonical application |
| --- | --- |
| Euler-factor and translated heat sources, earlier heat counter-kernels | The full unmodified zeta coefficient identification and exact evolved theta arm used together |
| Weighted-square and finite-tail controls | The full coefficient sequence and reflection, beyond the retained square support and endpoint data |
| Finite-prime orbit controls | Full reflection and the coefficient identity beyond the fixed primes and prefix |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical arithmetic square expansion identifying the arm with the ordinary zeta Dirichlet series |
| Atomic, exact finite-profile and compact continuous controls | Complete canonical profile and coefficients outside the finitely imposed observations |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic of unmodified theta |
| Fixed amplitude with variable observation kernel | The true cosine oscillator and Newman equation for the readout |
| Relaxed positive-measure profiles | An integer zero configuration identified with the exact field |
| RSCT calibrated multiplicative models | Full phases along the actual common height trajectory and the complete Green window |

The reflection rigidity screen uses its domain and the conjunction of
square support, full reflection and endpoint normalization. The B09
quadratic controls fail the canonical log-ratio/zeta identification,
while actual canonical resonances are included in the estimate. The
screen concerns applicability of this arithmetic derivation. An
averaged inequality of this size can accommodate a localized defect,
since its permitted total mass grows on the available windows.

[handoff]: 30_GNP_RS_B10_RETURN_AND_MODEL_CHANGE_20261112.md
[proof]: 29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[review]: ../reviews/16_GNP_RS_B10_PREINTEGRATION_ASSESSMENT_20261112.md
[b07]: 23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md
[b08]: 25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md
[e06]: 17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[bw]: https://arxiv.org/pdf/1505.04161v1
[mv]: ../references/03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
