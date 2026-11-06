# TND-A-E01 r1: complete-spectrum supplied-apparatus response

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, verified in local turn metadata. Auxiliary branch chat0002, thread `01a1af5d-9e4a-78c2-afad-04dc3a245679`. **E — execution**, frozen request r1. Root is sole artifact writer; two read-only same-model derivation supports contributed within this single proof-author pass.

**Return: all six obligations proved in-note for the conditional supplied-apparatus model, with proof-author checks only.** The complete response is
\[
\boxed{\mathcal O_{\lambda,\tau}(z)
=q(\tau)e^{-\tau z^2}H_\lambda(z),\qquad
q(\tau)=\frac{Q_1(\pi+4\tau)}{Q_1(\pi)}>0.}
\tag{1}
\]
The preparation, passive bank, source placement and absolute phase-sensitive detector law remain supplied. Intrinsic preparation and laboratory implementation are not derived. No collision exclusion or recovery advantage follows. The [request][request] remains unchanged; [activation/input identities][activation], [return record][return], [sole register][progress] and [continuation/model-change guidance][continuation] retain scope and routing. Branch E02 and the shared TND-E03 assessment have not been performed here.

## 1. Theorem, evidence and fixed conventions

For every fixed finite \(M,T,Z,b\ge0\), real \(|\lambda|\le M\), \(0\le\tau\le T\), and complex \(|\Re z|\le Z,\ |\Im z|\le b\), (1) holds with the literal source and readout in [B01 Decision01 §§1–4][decision]. Every finite tuple of nonnegative integer derivative orders in \(\lambda,\tau,z\), and every finite spatial derivative and left graph norm used below, has the stated continuous integral identity and a complete order-dependent majorant. Time derivatives at zero are right derivatives. There is no assertion uniform in order, of an infinite derivative expansion, negative/complex proper time, or all-height inverse stability.

We inherit the geometric factorization, signed blocks and source estimates from [parent E01 Note02 §§1–4,6–7][parent], at its proof-author level pending shared TND-E03. MC11 [Note05][mc05], [fixed Note06][mc06], [source Note08][mc08] and [Review05][mc-review] retain their accepted internal scopes and shared premises. No pending Note13-only preparation or measurement assertion is used. The local pairing/calibration proof is §6 below.

The primary-source uses are limited: [Camporesi–Higuchi v1, (3.40), (3.54), (5.35)–(5.36)](https://arxiv.org/html/gr-qc/9505009v1) fixes the inherited angular spectrum and slash convention; [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) fixes complete theta inversion; [Rodgers–Tao v5, Introduction (1)–(4) and following heat-sign paragraph](https://arxiv.org/html/1801.05914v5#S1) fixes the canonical source, \(H_0(z)=\xi((1+iz)/2)/8\), and Newman sign. These selected passages were checked, not the papers' main theorems. [Source-use receipt02][source-use] records exact use and canonical bibliography homes. The new amplification and heat estimates below are local derivations.

Keep \(K=L^2(S^2,\Sigma;d\Omega)\), unit-sphere self-adjoint \(D=-i\,\mathrm{slash}\nabla\), \(A=D^2\), parallel chirality \(\Gamma\), and cylinder metric \(dv^2+g_{S^2}/4\). Then
\[
\mathcal D_C=-i\Gamma\partial_v+2D,\qquad
L_0=\mathcal D_C^2=-\partial_v^2+4A.
\tag{2}
\]
No curvature term is added to this accepted square. The supplied energy convention is \(H_{\rm kin}=\varepsilon L_0\), \(\varepsilon=\hbar^2/(2m\ell_0^2)\), \(m,\ell_0>0\). Metric volume is \(dv\,d\Omega/4\); the unitary product-to-metric-volume spinor map is multiplication by 2.

## 2. Complete amplified realization and core — obligation 1

Let \(K_{\rm ref}\) be the passive copy and \(J:K_{\rm ref}\to K\) the fixed matched unitary. Via
\[
\operatorname{HS}(K_{\rm ref},K)\simeq K\otimes\overline{K_{\rm ref}},
\quad \mathscr H=L^2(\mathbb R;\operatorname{HS}(K_{\rm ref},K)),
\]
all differential and angular operators act on the left, amplified by the identity on the conjugate reference space. Write \(L=L_0^{\rm left}\).

Take \(D\chi^+_{n,a}=n\chi^+_{n,a}\), \(\chi^-_{n,a}=\Gamma\chi^+_{n,a}\), \(1\le a\le2n\), \(n\ge1\). The physical projection \(P_n\) has rank \(4n\). The full-line unitary transform is
\[
\widehat S(k)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-ikv}S(v)\,dv.
\tag{3}
\]
In each physical pair and every reference column the first-order multiplier and its projectors are
\[
M_n(k)=\begin{pmatrix}2n&k\\k&-2n\end{pmatrix},\quad
E_n(k)=\sqrt{k^2+4n^2},\quad
\Pi_\pm(n,k)=\tfrac12(I\pm M_n(k)/E_n(k)).
\tag{4}
\]
Thus \(M_n^2=\omega_n I\), \(\omega_n=k^2+4n^2\). Hermitian matrix multiplication on its maximal weighted domain is self-adjoint: testing its adjoint on compact spectral sets in finitely many channels/columns forces the same weighted square-integrability. Consequently
\[
\begin{split}
\operatorname{Dom}\mathcal D_C^{\rm left}
=\operatorname{Dom}L^{1/2}
&=\{S\in\mathscr H:\sum_n\int\omega_n\|P_n\widehat S(k)\|_{\rm HS}^2dk<\infty\},\\
\operatorname{Dom}L^p
&=\{S\in\mathscr H:\sum_n\int\omega_n^{2p}\|P_n\widehat S(k)\|_{\rm HS}^2dk<\infty\},\quad p\ge0.
\end{split}
\tag{5}
\]
The first equality is also the form domain of \(L\). There is no right-energy weight.

The complete-shell projections \(P_{\le N}=\sum_{n\le N}P_n\) and finite-reference projections commute with these operators and converge in every displayed graph norm by dominated convergence. After these projections, the first-order graph norm is equivalent to a finite sum of \(H^1(\mathbb R)\) norms; the \(L^p\) graph norm is equivalent to \(H^{2p}(\mathbb R)\). Smooth radial cutoff and mollification are dense in those Sobolev norms. Hence finite sums of
\(f(v)|\chi_{n,\sigma,a}\rangle\langle e_j|\), \(f\in C_c^\infty(\mathbb R)\), form a core for the first-order operator and every finite power in (5). Their closures are the realizations just given; no boundary condition is selected.

The spectra are
\[
\sigma(\mathcal D_C^{\rm left})=(-\infty,-2]\cup[2,\infty),\qquad
\sigma(L)=[4,\infty).
\tag{6}
\]
At fixed \(k\), each first-order sign has physical multiplicity \(2n\) per reference column; the square has physical multiplicity \(4n\). The reference adds countable apparatus multiplicity, without another energy or physical-angular weight. Both radial directions and all \(k\in\mathbb R\) are retained. On each open radial half-line the dispersions are smooth monotone maps with nonzero derivative. Their threshold preimages have measure zero, so pushforwards of the integrable spectral densities are absolutely continuous. Countable sums and reference amplification preserve this conclusion. Threshold singularities are integrable; there are no normalizable radial plane/cosine modes or threshold eigenstates. Plain radial evenness reduces the square but not the first-order operator, whose derivative changes parity.

Functional calculus gives the left-only semigroup
\[
\widehat{e^{-\tau L}S}_n(k)=e^{-\tau\omega_n(k)}P_n\widehat S(k),
\quad \|e^{-\tau L}\|=e^{-4\tau},\quad \tau\ge0.
\tag{7}
\]
Dominated convergence proves strong continuity, including zero. For \(r\ge0\) and \(\tau>0\),
\(\|L^r e^{-\tau L}\|=\sup_{x\ge4}x^r e^{-\tau x}<\infty\).
This is positive-time left-energy smoothing; it gives no uniform arbitrary-data smoothing as \(\tau\downarrow0\), and no right-reference regularization. Infinite radial volume and passive amplification do not yield a trace-class or compact heat operator. For initial data in \(\operatorname{Dom}L\), the semigroup is a strong solution of \(\partial_\tau S=-LS\). A difference of strong solutions with zero initial data has nonincreasing squared norm, since \(L\ge4I\); this proves uniqueness in the strong-solution class. Prepared data below lie in every finite domain.

## 3. Angular bank and exact prepared graph norms — obligation 2

Set \(Q=Q_1(\pi)\). The inherited complete radial Green integral gives
\[
\int_{\mathbb R}\frac{dk}{2\pi(k^2+4n^2)}=\frac1{4n}.
\]
It is this full integral, not \(k=0\), that calibrates the supplied bank. With
\[
R=\sum_{n\ge1}r_nP_n,\quad r_n=\frac{e^{-\pi n^2}}{4nQ},
\quad B=R^{1/2}J,\quad
\mu_s=\frac1Q\sum_{n\ge1}n^{2s}e^{-\pi n^2},
\tag{8}
\]
we have \(R>0\), \(\operatorname{Tr}R=\mu_0=1\), \(BB^*=R\), \(B^*B=J^*RJ\), and \(\|B\|_{\rm HS}=1\). In particular this normalizes the angular bank only, not the radial source. Every finite \(\mu_s\) is finite by Gaussian summability. Moreover
\[
\operatorname{Tr}(A^sR)=\mu_s,\qquad
\|A^sB\|_{\rm HS}^2=\mu_{2s},\qquad
\|A^s(I-P_{\le N})B\|_{\rm HS}^2
=\frac1Q\sum_{n>N}n^{4s}e^{-\pi n^2}\longrightarrow0.
\tag{9}
\]
These are left moments; no right generator is assigned. Even \(B\) is nuclear between the two spaces, since \(\sum_n4n\sqrt{r_n}<\infty\), but it has no asserted trace-one normalization.

Let \(f_{a,\lambda}(v)=v^{2a}F_\lambda(v)\), \(F_\lambda=e^{\lambda v^2}\Phi(v)\). Section 4 proves uniform Schwartz seminorms for each finite \(a\) on \(|\lambda|\le M\). Since \(\|P_nB\|_{\rm HS}^2=e^{-\pi n^2}/Q\), Plancherel and a finite binomial expansion give the useful exact formula
\[
\boxed{\|L^p(f_{a,\lambda}^{(h)}B)\|_{\mathscr H}^2
=\sum_{j=0}^{2p}\binom{2p}{j}4^{2p-j}\mu_{2p-j}
\|f_{a,\lambda}^{(h+j)}\|_2^2.}
\tag{10}
\]
Thus \(S_{\lambda,0}=F_\lambda B\) and every finite \(\lambda\)/spatial derivative belong to every requested left domain, uniformly on compact \(\lambda\) intervals. Differentiability in those graph norms follows from the same source majorants, including their next finite derivative.

For all finite \(a,c,h,p\ge0\),
\[
\partial_\lambda^a\partial_v^h\partial_\tau^cS_{\lambda,\tau}
=(-1)^ce^{-\tau L}L^c(f_{a,\lambda}^{(h)}B),
\quad
\|L^p\partial_\lambda^a\partial_v^h\partial_\tau^cS_{\lambda,\tau}\|
\le e^{-4\tau}\|L^{p+c}(f_{a,\lambda}^{(h)}B)\|.
\tag{11}
\]
Strong continuity in each graph space and extra finite powers give continuous right-time limits at zero. Compactness of the parameterized source family in each graph norm makes these limits uniform for \(|\lambda|\le M\). This uses the prepared domain rather than an arbitrary-data smoothing estimate at zero.

## 4. Complete source and radial tails — obligation 3, prepared part

For \(u\ge0\) put \(x=\pi e^{4u}\). Keep the source index \(m\) independent of physical field channel \(n\). Rename the inherited source polynomials \(\mathsf H_j\) to distinguish them from the Newman functions:
\[
\mathsf H_0(x)=2x^2-3x,\quad
\mathsf H_{j+1}=(1-4x)\mathsf H_j+4x\mathsf H_j',\quad
\Phi^{(j)}(u)=e^u\sum_{m\ge1}e^{-m^2x}\mathsf H_j(m^2x).
\tag{12}
\]
They have degree \(j+2\). For a polynomial \(P\), let \(A_P\) be its absolute coefficient sum. Reusing [parent (27)–(34)][parent] and [MC11 Note08 (6)–(14)][mc08],
\[
C_d(N)=\sum_{m>N}m^{2d}e^{-\pi(m^2-1)}\to0,\quad
B_j=A_{\mathsf H_j}C_{j+2}(0),
\]
\[
 e^u\sum_{m>N}e^{-m^2x}|\mathsf H_j(m^2x)|
\le A_{\mathsf H_j}C_{j+2}(N)e^u x^{j+2}e^{-x}.
\tag{13}
\]
Indeed \(x\ge\pi>1\) bounds the polynomial by \(A_{\mathsf H_j}m^{2(j+2)}x^{j+2}\), and the remaining exponent by \(e^{-x}e^{-\pi(m^2-1)}\). This pays the sum of absolute values, not only a signed tail.

Complete canonical theta inversion gives smooth even reflection of \(\Phi\); hence (13) bounds its full-line finite derivatives with \(u=|v|\) and \(x=\pi e^{4|v|}\). The identity uses the zero-mode correction and complete unit weights, as in [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) and [parent §4][parent]. Reflected finite prefixes generally have derivative jumps at zero. Their one-sided derivative tails are not global graph-core approximations. We use the exact smooth source and the operator core of §2, so no such approximation is needed.

For finite \(r,d\ge0\),
\[
J_{r,d}(M,b)=\int_{\mathbb R}|v|^r
 e^{Mv^2+(b+1)|v|}x^d e^{-x}\,dv<\infty.
\tag{14}
\]
The substitution \(x=\pi e^{4|v|}\) gives
\[
\frac{2}{4^{r+1}}\int_\pi^\infty
 [\log(x/\pi)]^r(x/\pi)^{(b+1)/4}x^{d-1}
 \exp\{M\log^2(x/\pi)/16-x\}\,dx.
\]
The \(-x\) exponent dominates all displayed powers and the log-square. Its remaining tail tends to zero, giving a complete radial integral payment.

Define \(\mathsf R_0=1\), \(\mathsf R_{j+1}=\partial_v\mathsf R_j+2\lambda v\mathsf R_j\); then \(\partial_v^j e^{\lambda v^2}=e^{\lambda v^2}\mathsf R_j(\lambda,v)\). Finite Leibniz expansion yields
\[
|f_{a,\lambda}^{(h)}(v)|
\le C_{a,h,M}(1+|v|)^{2a+h}
 e^{Mv^2+|v|}x^{h+2}e^{-x}.
\tag{15}
\]
An explicit finite \(C\) is obtained by summing over \(i+j+\ell=h\), \(i\le2a\), the multinomial coefficient, \((2a)!/(2a-i)!\), \(B_\ell\), and the absolute \(v\)-coefficient sum of \(\mathsf R_j\) with \(|\lambda|\) replaced by \(M\). Since \(x\ge1\), each \(x^{\ell+2}\le x^{h+2}\). No order-uniform bound is used.

For \(w_{r,b}(v)=(1+|v|)^r e^{b|v|}\), let
\[
\mathcal N_{a,h;r,b}(M)
=\sup_{|\lambda|\le M}\|w_{r,b}f_{a,\lambda}^{(h)}\|_1.
\]
Then (15) gives the controlled bound
\[
\mathcal N_{a,h;r,b}(M)
\le C_{a,h,M}\sum_{\ell=0}^{2a+h+r}
\binom{2a+h+r}{\ell}J_{\ell,h+2}(M,b).
\tag{16}
\]
Squaring the right side of (15) and integrating gives the finite uniform \(L^2\) derivative bounds needed in (10): the exponent \(-2x\) dominates the resulting \(2Mv^2\) and all powers. Supremum-weighted versions likewise prove every fixed Schwartz seminorm. Continuity in \(\lambda\) into each weighted space follows by domination using the next insertion \(v^2\).

For clarity, source-prefix value tails, with \(\Phi_N\) the reflected finite value sum, obey
\[
\|w_{r,b}v^{2a}e^{\lambda v^2}(\Phi-\Phi_N)\|_1
\le A_{\mathsf H_0}C_2(N)\sum_{\ell=0}^r\binom r\ell
J_{2a+\ell,2}(M,b)\to0.
\tag{17}
\]
This is a value/moment tail bound, not a spatial-domain assertion for \(\Phi_N\).

The full radial Fourier integral is also controlled: for finite \(d,l\ge0\),
\[
|\partial_k^d\widehat f_{a,\lambda}(k)|
\le \frac{(1+k^2)^{-l}}{\sqrt{2\pi}}
\|(1-\partial_v^2)^l[(-iv)^df_{a,\lambda}]\|_1.
\tag{18}
\]
The right side is uniformly finite by (15)–(16). Taking \(l\) sufficiently large pays any finite polynomial-weighted radial spectral tail, in \(L^1\) or \(L^2\). Angular energy tails are paid separately by (9). A finite-reference cutoff converges in Hilbert–Schmidt norm since the squared column norms sum to that norm; with the matched reference basis, it can be exhausted by complete shells and has exactly the same Gaussian bank tails. These limits do not identify the source index, physical channel, passive reference column or radial momentum with one another.

## 5. Evolved exponential moments and zero time — obligation 3, heat part

For \(\tau>0\) set
\[
K_\tau(y)=(4\pi\tau)^{-1/2}e^{-y^2/(4\tau)},\quad
h_{\lambda,\tau}=K_\tau*F_\lambda,\quad
B_\tau=e^{-4\tau A}B.
\]
Use \(K_0*f=f\) and \(B_0=B\). The commuting direct multipliers in §2 give
\[
S_{\lambda,\tau}(v)=h_{\lambda,\tau}(v)B_\tau.
\tag{19}
\]
This factorization follows in \(\mathscr H\) first, and below in its paid weighted classes.

The weight is submultiplicative: \(w_{r,b}(x+y)\le w_{r,b}(x)w_{r,b}(y)\). For a standard real Gaussian \(X\), put
\[
\gamma_{r,b}(T)=\mathbb E[(1+\sqrt{2T}|X|)^r e^{b\sqrt{2T}|X|}],\qquad \gamma_{r,b}(0)=1.
\tag{20}
\]
This is finite and dominates \(\|w_{r,b}K_\tau\|_1\) for all \(0<\tau\le T\). For an explicit finite-order bound, with \(m_j=\mathbb E|X|^j=2^{j/2}\Gamma((j+1)/2)/\sqrt\pi\), Gaussian exponential tilting and \(e^{b|y|}\le e^{by}+e^{-by}\) give
\[
\gamma_{r,b}(T)\le
2e^{b^2T}\sum_{j=0}^r\binom rj
\sum_{l=0}^j\binom jl(2bT)^{j-l}(2T)^{l/2}m_l.
\tag{21}
\]
Zero powers use \(0^0=1\); this upper bound need not be sharp at zero. Tonelli and submultiplicativity therefore prove
\[
\|w_{r,b}(K_\tau*f)\|_1\le\gamma_{r,b}(T)\|w_{r,b}f\|_1,
\quad 0\le\tau\le T.
\tag{22}
\]
In particular every polynomial/exponential radial moment requested for the evolved field is uniformly paid, without preservation of double-exponential spatial decay.

Move finite derivatives onto exact prepared data. For \(a,c,h\ge0\),
\[
\partial_\lambda^a\partial_\tau^c\partial_v^hS_{\lambda,\tau}
=\sum_{j=0}^c\binom cj(-4)^{c-j}
(K_\tau*f_{a,\lambda}^{(h+2j)})
 A^{c-j}e^{-4\tau A}B.
\tag{23}
\]
For \(\tau>0\), differentiation and integration by parts follow first from the paid source derivatives and Gaussian kernel. No singular derivative-kernel bound at zero is used. From (9), (16), (22),
\[
\|w_{r,b}\partial_\lambda^a\partial_\tau^c\partial_v^hS\|_{L^1(\mathrm{HS})}
\le\gamma_{r,b}(T)\sum_{j=0}^c\binom cj4^{c-j}
\sqrt{\mu_{2(c-j)}}\,\mathcal N_{a,h+2j;r,b}(M).
\tag{24}
\]
An additional finite left power \(L^p\) has the same absolute bound with \(c\) replaced by \(c+p\). A spatial or generator derivative on a vanishing angular/reference bank tail replaces the corresponding \(\mu\) moment by its vanishing tail from (9).

These are continuous weighted limits at zero, not just bounds. Translation is continuous in each \(L^1(w_{r,b}dv)\): approximate by compactly supported continuous functions and use submultiplicativity to control translations. With \(y=\sqrt{2\tau}X\),
\(K_\tau*f-f\) is the Gaussian average of the translation difference. Its weighted norm tends to zero by translation continuity and domination by \((1+w_{r,b}(\sqrt{2T}X))\|wf\|_1\). For the family \(f_{a,\lambda}^{(j)}\), compactness of its image in each weighted space, proved after (16), makes this convergence uniform in \(|\lambda|\le M\). Also \(A^s e^{-4\tau A}B\to A^sB\) in HS by (9) and dominated convergence. Thus every expression (23) has a continuous right limit. Integrating the positive-time identity \(\partial_\tau K_\tau*f=K_\tau*f''\) down to zero, and then iterating on the paid derivatives, proves that these limits are the actual right derivatives. The same argument gives mixed-derivative interchanges in these weighted Banach spaces. Finite positive times are continuous by the same estimates.

## 6. Local source, pairing and absolute readout — obligation 4

For every \(X\in\operatorname{HS}(K_{\rm ref},K)\), \(B^*X\) is trace class and
\[
\|B^*X\|_1\le\|B\|_{\rm HS}\|X\|_{\rm HS},\qquad
|\operatorname{Tr}_{K_{\rm ref}}(B^*X)|\le\|X\|_{\rm HS}.
\tag{25}
\]
This is the conjugate-linear-first-slot HS pairing. It is basis independent. The matched \(J\) fixes the preparation/readout relative phase; a reference basis change transforms both together. An altered relative physical phase would change the supplied experiment. No right heat factor arises from taking this pairing.

By (24), the pointwise Bochner Fourier transform of the prepared family exists and is continuous for every real \(k\). Its complex extension is paid in §7. Fixed-\(k\) evaluation is not a bounded functional on arbitrary radial \(L^2\), and no such claim is needed. In the metric-volume convention put \(U\psi=2\psi\), \(B_{\rm geom}=UB\), \(S_{\rm geom}=US\). The metric-volume adjoint gives
\(B_{\rm geom}^*S_{\rm geom}=B^*S\): the two factors 2 cancel the angular measure factor \(1/4\). There is no additional factor 4 in (25) or the readout.

The supplied source is \(F_\lambda\) itself, not its square root; \(\|S_{\lambda,0}\|=\|F_\lambda\|_2\) is not normalized away. Evenness and (3) give the full-line/cosine conversion
\[
\widehat F_\lambda(k)
=\frac{2}{\sqrt{2\pi}}\int_0^\infty F_\lambda(v)\cos(kv)\,dv
=\sqrt{2/\pi}\,H_\lambda(k).
\tag{26}
\]
Thus the readout's \(\sqrt{\pi/2}\) factor has a fixed absolute scale. The canonical \(H_0=\xi((1+iz)/2)/8\) is retained from [Rodgers–Tao v5 (1)–(4)](https://arxiv.org/html/1801.05914v5#S1); no gain is fitted to a zero or signal value.

In the assumed physical amplitude units, \(S^{\rm phys}=gS\), fixed known \(g>0\), and the raw complex signal is \(y=\eta\operatorname{Tr}(B^*\widehat S^{\rm phys})\), fixed known \(\eta\ne0\) including phase. Therefore
\(\sqrt{\pi/2}\,y/(\eta g)=\sqrt{\pi/2}\operatorname{Tr}(B^*\widehat S)\).
This checks the stipulated law's mathematical consistency and sign/phase convention. It derives neither a Born detector law nor hardware existence. Unknown phase/gains would leave only proportional recovery and fail this exact absolute-calibration premise.

## 7. Response, entire continuation and finite derivatives — obligation 5

For real \(k\), (7), (19) and the complete Fourier integral give, for every physical shell and reference column,
\[
P_n\widehat S_{\lambda,\tau}(k)
=e^{-\tau k^2}e^{-4\tau n^2}\widehat F_\lambda(k)P_nB.
\tag{27}
\]
The trace can be evaluated by the matched basis, or cyclically using the trace-class product in (25):
\[
\begin{split}
\operatorname{Tr}_{K_{\rm ref}}(B^*\widehat S(k))
&=e^{-\tau k^2}\widehat F_\lambda(k)
\operatorname{Tr}_K(e^{-4\tau A}R)\\
&=e^{-\tau k^2}\widehat F_\lambda(k)
\frac1Q\sum_{n\ge1}e^{-(\pi+4\tau)n^2}.
\end{split}
\tag{28}
\]
All \(4n\) physical states contribute; their degeneracy cancels \(1/(4n)\) in the bank weight. The single heat factor is on the left. In particular no density-matrix doubling of \(4\tau\) occurs. Equations (26) and (28) prove (1) first for real \(k\), including \(\tau=0\).

Now define for complex \(z\)
\[
\widehat S(z)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-izv}S(v)\,dv.
\tag{29}
\]
For every compact strip rectangle, (24) pays this HS-valued integral and all its finite \(z\) derivatives. Difference quotients are dominated using one extra moment and a slightly wider finite strip; hence it is entire. The same source argument gives the entire \(\widehat F\) and \(H\). Both sides of (27), with \(k\) replaced by \(z\), are entire HS-valued functions after (29) has been established; pairing with every continuous linear functional and the scalar identity theorem extends the real identity to \(\mathbb C\). Equivalently Gaussian Fourier Fubini in the paid weighted classes gives it directly. This is continuation of an actual integral, not evaluation of an unrestricted \(L^2\) transform at complex momentum. Evenness in (26) also holds for complex \(z\).

Every mixed derivative has the integral form
\[
\partial_\lambda^a\partial_\tau^c\partial_z^d\mathcal O_{\lambda,\tau}(z)
=\frac12\operatorname{Tr}_{K_{\rm ref}}
\left[B^*\int_{\mathbb R}(-iv)^d e^{-izv}
\partial_\lambda^a\partial_\tau^cS_{\lambda,\tau}(v)\,dv\right].
\tag{30}
\]
Its absolute value is bounded uniformly on the admitted parameter rectangle by one half of (24) with \(r=d\), \(h=0\). The factor \(1/2=\sqrt{\pi/2}/\sqrt{2\pi}\) is exact. This gives one complete majorant for every tuple, including continuous right-time limits at zero, using no formal derivative series.

For an explicit scalar recursion, let \(h_a=\partial_\lambda^aH_\lambda\) and
\[
q^{(s)}(\tau)=\frac{(-4)^s}{Q}\sum_{n\ge1}n^{2s}e^{-(\pi+4\tau)n^2},\quad
|q^{(s)}|\le4^s\mu_s,
\]
\[
P_{0,r}(\tau,z)=(-z^2)^r,\qquad
P_{j+1,r}=\partial_zP_{j,r}-2\tau zP_{j,r}.
\tag{31}
\]
Then finite Leibniz differentiation of the established (1) gives
\[
\partial_\lambda^a\partial_\tau^c\partial_z^d\mathcal O
=e^{-\tau z^2}\sum_{s=0}^c\sum_{j=0}^d
\binom cs\binom dj q^{(s)}(\tau)P_{j,c-s}(\tau,z)
\partial_z^{d-j}h_a(z).
\tag{32}
\]
The source bound is
\[
\partial_z^l h_a(z)=\tfrac12\int_{\mathbb R}(-iv)^lv^{2a}F_\lambda(v)e^{-izv}dv,
\quad |\partial_z^lh_a|\le\tfrac12B_0J_{2a+l,2}(M,b).
\tag{33}
\]
For \(\rho=\sqrt{Z^2+b^2}\), let \(P^\#_{j,r}(T,\rho)\) be the finite absolute coefficient sum of \(P_{j,r}\) evaluated with \(\tau=T, |z|=\rho\). Since \(|e^{-\tau z^2}|\le e^{Tb^2}\), (32) has the explicit majorant
\[
\frac12e^{Tb^2}B_0\sum_{s=0}^c\sum_{j=0}^d
\binom cs\binom dj4^s\mu_s P^\#_{j,c-s}(T,\rho)
J_{2a+d-j,2}(M,b).
\tag{34}
\]
All constants/recursions depend only on the stated finite orders and compact parameters. Source tails are paid by (13), (17), physical angular derivative tails by the Gaussian tails of \(\mu_s\), and radial integrals by (16), (24). The independent indices have not been collapsed. The inherited scalar \(G\) integral is unnecessary; its initial \(|\Im z|<1\) strip is not extended or used in this proof.

## 8. Exact consequence, changed Newman equation and limits — obligation 6

For every finite real \(\tau\ge0\), the positive convergent series gives \(q(\tau)>0\), and \(e^{-\tau z^2}\) is entire and nowhere zero. Thus
\[
H_\lambda(z)=q(\tau)^{-1}e^{\tau z^2}\mathcal O_{\lambda,\tau}(z).
\tag{35}
\]
The positive source gives \(H_\lambda(0)>0\), so the entire function is not identically zero. Multiplication by this nonvanishing entire factor preserves every zero and its multiplicity at fixed \(\lambda\). The zero sets agree throughout the family, so pre-existing collisions in \(\lambda\) are preserved rather than excluded. At \(\tau=0\), \(q=1\) and \(\mathcal O_{\lambda,0}=H_\lambda\), retaining the absolute \(H_0\) normalization.

The canonical source gives \(\partial_\lambda H=-\partial_z^2H\), consistent with the [Rodgers–Tao v5 heat-sign paragraph](https://arxiv.org/html/1801.05914v5#S1). For fixed \(\tau\), differentiate the Gaussian prefactor when translating this equation:
\[
\boxed{\partial_\lambda\mathcal O
=-(\partial_z+2\tau z)^2\mathcal O
=-\partial_z^2\mathcal O-4\tau z\partial_z\mathcal O
 -(2\tau+4\tau^2z^2)\mathcal O.}
\tag{36}
\]
More generally, for each finite \(a\),
\(\partial_\lambda^a\mathcal O=(-1)^a(\partial_z+2\tau z)^{2a}\mathcal O\).
The operator is repeated composition, including product-rule derivatives of \(z\), not a commuting-binomial abbreviation. The unchanged Newman PDE is recovered only at \(\tau=0\). As a separate consistency check,
\(\partial_\tau\mathcal O=(q'/q-z^2)\mathcal O\); this is the proper-time response equation, not a Newman clock law.

At real frequency the exact inverse amplification is
\[
|q(\tau)^{-1}e^{\tau k^2}|=\frac{Q_1(\pi)}{Q_1(\pi+4\tau)}e^{\tau k^2}.
\tag{37}
\]
For fixed \(\tau>0\) it is unbounded as \(|k|\to\infty\). On any fixed rectangle (35) is bounded, but this is not an all-height recovery theorem or an optimal stability result. No negative proper-time evolution is inferred from recovery of this known family.

The four roles remain distinct: Newman \(\lambda\) labels externally prepared \(e^{\lambda v^2}\Phi\); \(\beta\) is the angular damping/scan parameter; proper time is \(\tau=\varepsilon t_E/\hbar\ge0\); laboratory kinetic unitary time appears in \(e^{-i\varepsilon t_{\rm lab}L_0/\hbar}\). Positive heat/resolvent proper time is not an asserted relativistic clock. No physical law identifies these variables.

## 9. Six-obligation disposition, controls and proof boundary

| Request obligation | Disposition at this return | Evidence and remaining premise |
| --- | --- | --- |
| 1. Complete realization | **Proved in-note, proof-author** | §§2–3, (3)–(7): all signs/channels, continuous radial integral, maximal domains/core, strong heat evolution. Geometric parent input retains its pending shared assessment. |
| 2. Prepared domains | **Proved in-note, conditional preparation** | §§3–4, (8)–(16): trace/HS normalization, every finite left moment/domain and mixed graph derivative, including zero time. The actual source/bank remains supplied. |
| 3. Complete tails/integrals | **Proved in-note, proof-author** | §§4–5, (12)–(24): independent source/angular/reference/radial limits; all finite-order weighted moments and zero-time continuity. No reflected-prefix graph approximation or evolved double-exponential claim. |
| 4. Local source/readout | **Proved in-note under supplied detector law** | §6, (25)–(26): trace-class pairing, fixed relative phases, factor 2 metric conversion, paid pointwise Fourier class and absolute gains. No hardware/Born theorem. |
| 5. Response/derivatives | **Proved in-note, conditional apparatus** | §7, (27)–(34): complete real-frequency identity, actual entire integral continuation and every finite mixed derivative. |
| 6. Consequence/limits | **Proved in-note, proof-author** | §8, (35)–(37): nonvanishing/recovery and multiplicity preservation, changed Newman PDE, explicit inverse amplification and distinct times. No collision or stability gain. |

No obligation failed and no construction-changing correction was needed. All mathematical claims are conditional on the explicitly supplied construction; their proofs do not establish physical availability. All new results remain proof-author work awaiting branch E02 and its shared TND-E03 prerequisite.

Classification under [avoid/01][a01] is a **conditional physical response representation**, not an RH criterion or a new sign estimate. Consult the [result index][results], specifically [collision controls][controls] and [theta/source cluster][theta], and [patterns index][avoid], especially [re-realizations][a03] and [scoped exclusions][a07]. Carry [Decision01 §5][decision]'s existing control screen without new experiments:

| Inherited control family | Retained machinery and failed canonical premise |
| --- | --- |
| Euler-factor | Applicable smooth positive even source, Fourier and heat operations persist. Exact unchanged theta arithmetic fails; the representation rejects none of its recorded collisions. |
| Weighted-square / finite-prime | Applicable positive half-line and square-response formulas persist. Complete unit coefficients/full canonical reflection fail. Finitely matched endpoints do not prove global smooth domains. |
| Reflected super-Gaussian / smooth positive primitive | Applicable smoothness, positivity, reflection and exponential-moment operations persist. Exact canonical theta expansion fails; whenever these analytic hypotheses apply, the multiplier also preserves their collisions. |
| Atomic / finite profile | Applicable Fourier/moment observations can persist. Smooth source and full field-domain hypotheses need not hold. No smooth-field realization or universal exclusion is inferred. |

Naming canonical input identifies the supplied source but supplies no quantitative separation; applicability of this generic multiplier to colliding controls is compatible with the theorem. No new control witness or exclusion was claimed. Investigation05/06 and MC11 external statuses were not changed.

One proof pass and one local correction/check pass were used. Read-only supporting derivations checked disjoint domain/readout and weighted-heat/PDE details; root integrated and checked the formulas. Local checks retained (10)'s finite binomial indices, (21)'s Gaussian scaling, the left-only \(4\tau\) factor, \(\sqrt{\pi/2}\sqrt{2/\pi}=1\), the metric adjoint cancellation, the \(\tau=0\) weighted limit, and both product-rule terms in (36). The local wording clarification specifies complete-shell angular cutoffs, which commute with the first-order operator; arbitrary signed-subspace selections need not. No mathematical correction to the frozen candidate was needed. This is same-model proof-author support, not branch E02, shared TND-E03, specialist review or formal verification. No numerics, fit, manuscript or successor activation occurred.

**Continuation:** the default ready prerequisite is **[E] TND-E03 r2 — Sol**, the existing shared parent assessment; no new shared audit is invented here. Then **[E] TND-A-E02 — Sol** can audit this return after both dependencies are available. The [continuation/model-change note][continuation] gives reading order and prompts. B02 remains pending the branch assessment; it owns any later choice of a consequential estimate or representation-only stop.

[request]: ../research-progress/handoffs/02_TND_A_E01_R1_FROZEN_REQUEST_20261106.md
[activation]: ../research-progress/handoffs/04_TND_A_E01_R1_ACTIVATION_INPUTS_20261106.json
[return]: ../research-progress/handoffs/04_TND_A_E01_R1_RETURN_RECORD_20261106.json
[continuation]: ../research-progress/handoffs/04_TND_A_E01_R1_RETURN_AND_MODEL_CONTINUATION_20261106.md
[progress]: ../research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[decision]: ../brainstorm/notes/01_TND_A_B01_R1_SUPPLIED_PROPER_TIME_RESPONSE_DECISION_20261106.md
[parent]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[mc05]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md
[mc06]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md
[mc08]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[mc-review]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[source-use]: ../references/02_TND_A_E01_R1_SOURCE_USE_20261106.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
