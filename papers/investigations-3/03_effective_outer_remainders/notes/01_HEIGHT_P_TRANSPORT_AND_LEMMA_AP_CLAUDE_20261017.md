# Height-p transport and Lemma A_p: an exterior budget for the strip comparison

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is the coordination note for the first phase of the
[initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
(consumer and baseline) and the opening of its second (a new analytic
estimate). The proposal assigns the remainder budget to Codex and the audit
of imports and losses to Claude; Edward asked Claude to begin the project on
17 October 2026, so this is a Claude draft and the Codex audit becomes this
phase's cross-model check. The note answers change C5 of the
[portfolio setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md)
and the request of Project 01's
[contract note](../../01_dirichlet_newman_families/notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md)
(its Section 6, items 3 and 7) for Lemma \(A_p\), with \(q=1\) as the zeta
case.

Claim status is marked as in that note: **proved** (a complete proof here,
or a classical fact with its source), **proof sketch**, **conditional**,
**numerical** (floating point, with a record), **planning** (arithmetic under
a stated hypothesis) and **open**. The one check programme is
[`height_p_transport_claude_20261017.py`](../numerics/height_p_transport_claude_20261017.py),
with its [record](../numerics/HEIGHT_P_TRANSPORT_CLAUDE_20261017.json);
"record A" to "record H" below are its sections.

**Summary.**

1. *Consumer and contract.* The exterior statement Project 03 was opened to
   make effective is replaced, for the strip comparison of Project 01
   (Proposition 3.3 there, after Hakimoglu-Brown, arXiv:2610.12803), by a
   lower bound for \(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\) at a fixed
   height \(p\ge\sqrt5\), where the Euler product converges absolutely.
   That is a weaker sufficient statement than a zero-free region near the
   axis at the final time (Section 1). The inherited four-jet budget (21
   Note 58, 22 outer Note 01) is stopped by its own unavoidable costs: at
   the attainable height \(L\approx27\) they exceed its sign margin \(1/8\)
   by a factor of about \(10^6\) (Section 2).
2. *Exact transport identity* (proved, Lemmas 3.1–3.3). \(S(x,p,t)\) is half
   the real part of the logarithmic derivative of the Gaussian average
   \(\mathcal G(w)=\mathbb E\,F(w+\tau N)\), \(\tau=\sqrt{t/2}\), of the
   completed function \(F=\xi_\chi\) (or \(\xi\)) at
   \(w=\tfrac12(1+p+ix)\). Moving the contour to the saddle of the Gamma
   factor, \(s_*=w+\tfrac t2\alpha(s_*)\), gives
   \((\mathcal G'/\mathcal G)(w)-(F'/F)(s_*)=\int(G'-c_1G)\varphi_\tau/\int G\varphi_\tau\)
   for an explicit entire \(G\) with \(G(0)=1\), \(G'(0)=c_1\).
3. *Transport law with an explicit remainder* (proved, Proposition 4.5 and
   Theorem 4.6). \(|(\mathcal G'/\mathcal G)(w)-(F'/F)(s_*)|\le E\), where
   \(E\) is written with \(\zeta\), \(-\zeta'/\zeta\) and its derivatives at
   real arguments, \(\psi\) and \(\log\Gamma\), and a partial-summation bound
   in the critical strip. No Riemann–Siegel formula, truncated Dirichlet
   series, mollifier or zero-free region enters. Hence
   \[
   S(x,p,t)\ \ge\ \tfrac14\ell_*-\tfrac12\kappa(\sigma_*)-\tfrac12E,\qquad
   \sigma_*=\tfrac{1+p}2+\tfrac t4\ell_*,\quad \ell_*=2\operatorname{Re}\alpha(s_*),
   \]
   with \(\kappa=-\zeta'/\zeta\): the time-\(t\) floor is the time-zero floor
   of Project 01's Lemma 3.4 at a point moved right by \(t\ell_*/4\) and up
   by about \(\pi t/8\) (the mean-field drift of the zeros toward the
   origin). For the family,
   \(E\) depends on \(x\) only through \(\ell_*\).
4. *Lemma \(A_p\) with no loss, on a grid* (numerical evaluation of the
   proved bound, record F, H). At each of 20 times
   \(0.001\le t\le\tfrac12\) the gain
   \(\tfrac12(\kappa(\sigma_0)-\kappa(\sigma_*))\) exceeds \(E/2\) once
   \(\ell_*\ge\ell_1(p)\): \(\ell_1=10.6\) (even) and \(10.1\) (odd) at
   \(p=\sqrt5\), \(6.7\) and \(6.2\) at \(p=3\), \(9.6\) and \(5.6\) for zeta.
   Consequently, at those times, \(S(x,p,t)\ge C_{q,\mathfrak a}(p)\),
   Project 01's time-zero floor, at every real \(x\) for every primitive
   \(\chi\) of conductor \(q\ge1.1\cdot10^5\) (even) or \(4.9\cdot10^4\)
   (odd) when \(p=\sqrt5\), and \(q\ge1.3\cdot10^3\) or \(6.6\cdot10^2\) when
   \(p=3\); and for zeta \(S(x,p,t)\ge\tfrac14\ell_X-\tfrac12\kappa(\tfrac{1+p}2)\)
   at every \(x\ge X\) of Polymath's and Platt–Trudgian's certificates,
   \(\ell_X=\log(X/4\pi)\). Three things separate this from a statement for
   every \(t\): \(E\) is evaluated in floating point, its decrease in
   \(\ell_*\) is sampled (12 settings) rather than proved, and below
   \(t=0.001\) only the leading order is controlled.
5. *Validation* (numerical, record B–D). The Gaussian representation agrees
   with the kernel integral to \(10^{-15}\); at 124 points (zeta at
   \(x=10^3,10^4\); six characters of conductor \(10^4\) to \(10^6\) at
   \(x\in\{0,2,10\}\); \(p\in\{\sqrt5,3\}\); \(0.02\le t\le\tfrac12\)) the
   measured deviation from the main term is at most \(0.12\) and never
   exceeds \(E\); the ratio \(E/|\varepsilon|\) runs from \(1.6\) to about
   \(1300\), median \(22\).
6. *Consequence for Project 01's Target A* (planning, record G). Rerunning
   Project 01's comparison with the time-dependent floor lowers its planning
   values by \(1.4\)–\(4.8\%\), for instance from \(0.262/0.254\) to
   \(0.252/0.245\) (even/odd) at \(q=10^8\). These remain conditional on
   H12, on a written comparison theorem and on the certification of item 4.
7. *What remains.* H12 and the comparison theorem for the family; for
   zeta, the finite-region logic of the comparison; an outward-rounded
   evaluation of \(E\) with a proof of its monotonicity in \(\ell_*\) and of
   the small-time limit; the Codex audit.

## 0. Conventions

As in Project 01's note: \(s=\tfrac12(1+iz)\), \(z=x+iy\), so a zero
\(\rho=\beta+i\gamma\) sits at \(z=2\gamma+i(1-2\beta)\); physical height
\(x\) is twice the ordinate, \(T=x/2\).
\(H_t(z)=\int_{\mathbb R}e^{tu^2}\Phi(u)e^{izu}du\),
\(\partial_tH_t=-\partial_z^2H_t\), with Dobner's kernel \(\Phi=\Phi_\chi\)
for a primitive character \(\chi\) modulo \(q\ge3\) of parity
\(\mathfrak a\), and Polymath's kernel for zeta (which differs from Dobner's
by the factor 8). \(F=\xi_\chi=\Gamma_F\mathcal L\) with
\(\Gamma_F(s)=\alpha_\chi(q/\pi)^{s/2}\Gamma(\tfrac{s+\mathfrak a}2)\),
\(\mathcal L=L(\cdot,\chi)\); for zeta \(F=\xi=\Gamma_F\zeta\),
\(\Gamma_F(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\), \(q=1\),
\(\mathfrak a=0\). In both cases \(H_0(z)=c\,F(\tfrac12(1+iz))\) with a
constant \(c\ne0\), and \(F(s)=\overline{F(1-\bar s)}\). Put
\(\alpha=\Gamma_F'/\Gamma_F\):
\(\alpha(s)=\tfrac12\log\tfrac q\pi+\tfrac12\psi(\tfrac{s+\mathfrak a}2)\)
for the family and
\(\alpha(s)=\tfrac1s+\tfrac1{s-1}-\tfrac12\log\pi+\tfrac12\psi(\tfrac s2)\)
for zeta.

\(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\) as in arXiv:2610.12803;
\(p>1\), \(\sigma_0=\tfrac12(1+p)\), \(w=\sigma_0+\tfrac i2x\),
\(\tau=\sqrt{t/2}\), \(\varphi_\tau\) the centred Gaussian density of
variance \(\tau^2\), \(N\) a standard normal variable. For \(\sigma>1\):
\(\kappa(\sigma)=-\zeta'/\zeta(\sigma)=\sum\Lambda(n)n^{-\sigma}\),
\(K_2=-\kappa'=\sum\Lambda(n)\log n\,n^{-\sigma}\),
\(K_3=\kappa''=\sum\Lambda(n)\log^2n\,n^{-\sigma}\). For a function \(f\) of
a real variable, \([\![f]\!]_v=f(\sigma_*+v)-f(\sigma_*)-vf'(\sigma_*)\) is
its Taylor remainder at \(\sigma_*\).

Project 01's time-zero floor (its Lemma 3.4, proved there) is
\[
S(x,p,0)\ \ge\ C_{q,\mathfrak a}(p)=\tfrac14\bigl(\log\tfrac q\pi+\psi(\tfrac{\sigma_0+\mathfrak a}2)\bigr)-\tfrac12\kappa(\sigma_0),
\]
and for zeta at height \(x\) the same argument gives
\(S(x,p,0)\ge\tfrac12\operatorname{Re}\alpha(w)-\tfrac12\kappa(\sigma_0)\),
about \(\tfrac14\log\tfrac x{4\pi}-\tfrac12\kappa(\sigma_0)\).

## 1. The consumer and the contract

**1.1 The inherited consumer.** Polymath's criterion (Project 01, ledger
H4) concludes \(\Lambda\le t_0+y_0^2/2\) from (i) a verification below
height \(X\), (ii) an exterior statement at the final time,
\(H_{t_0}(x+iy)\ne0\) for \(x\ge X+\sqrt{1-y_0^2}\),
\(y_0\le y\le\sqrt{1-2t_0}\), and (iii) a barrier. In zeta coordinates (ii)
concerns ordinates \(T\ge\tfrac12(X+\sqrt{1-y_0^2})\) and real parts
\(\tfrac12(1+y_0)\le\operatorname{Re}s\le\tfrac12(1+\sqrt{1-2t_0})\), the
strip next to the critical line. Investigation 21's four-jet budget (Note
58) and its refinement (22 outer Note 01) asked for Laguerre-type sign
conditions on four derivatives there, which is stronger than (ii) needs;
Polymath's own route to (ii) is a mollified first-term dominance (their
Theorem 1.3 and Section 6), which Project 01's Section 4.2 has measured for
the family.

**1.2 The strip comparison.** Project 01's Proposition 3.3 (proved there for
every entire \(H\) of order one, real on \(\mathbb R\)) reproduces
Hakimoglu-Brown's inequality for the squared height \(Q\) of the highest
zero, \(Q'\le-2-\tfrac{4Q}pS(x,p,t)+\tfrac{8Q}{p^2-Q}\) for \(p^2\ge5Q\),
\(x\) the zero's real part. Its exterior input is a floor
\[
\textbf{(E)}\qquad S(x,p,t)\ \ge\ C(t)\quad\text{for }0\le t\le t_*\text{ and every }x\text{ where the highest zero can lie,}
\]
at one fixed \(p\in[\sqrt{5a},5]\), \(a=Q(0)\). Project 01 called this Lemma
\(A_p\), with stopping rule \(\delta\le C/4\) for \(C(t)=C-\delta\). For the
family at large conductor the region is the whole line (Target A, no
finite region); for zeta and for small conductors it is \(x\ge X\), the
rest being covered by a verification and a barrier as in Hakimoglu-Brown's
Lemma 2 (Project 01, ledger H11; not re-read here, see Section 10). The
comparison also needs H12, uniform confinement of the nonreal zeros at
positive times, and a written first-contact argument.

**1.3 Why (E) is the consumer for this project.** (E) is a statement at
height \(p\ge\sqrt5\), where the Dirichlet series of \(L\) converges
absolutely: it bounds a Poisson-smoothed density of zeros from below and
says nothing directly about zeros near the axis, which the comparison
turns into confinement. It needs no derivative of \(H_t\) beyond the
first, no zero-free region and no first-term dominance. The proposal names
"direct complex nonvanishing that avoids unnecessary differentiation" and
"a weaker sufficient consumer statement" as openings for this project;
(E) is both. The contract adopted here:

| Consumer | Region of (E) | \(p\) | Times | Floor wanted | Comparison height |
| --- | --- | --- | --- | --- | --- |
| Target A (family) | every real \(x\) | \(\sqrt5\le p\le5\) | \(0<t\le\tfrac12\) | \(C_{q,\mathfrak a}(p)\) (\(\delta=0\)) | none needed: every height |
| Target B (one character) | \(\lvert x\rvert\ge X_\chi=2t_0(q)\) (Platt) | same | same | \(\tfrac14\ell-\tfrac12\kappa(\sigma_0)\), \(\ell=\ell_*(X_\chi)\) | \(\ell\approx16.6\) |
| zeta | \(x\ge X\): \(6\cdot10^{10}\) (Polymath), \(5\cdot10^{12}+194858\) (Platt–Trudgian) | \(\sqrt5\le p\le6\) | same | \(\tfrac14\ell_X-\tfrac12\kappa(\sigma_0)\) | \(\ell_X=22.29\), \(26.71\) |

Here \(\ell_X=\log(X/4\pi)\) up to \(10^{-6}\) (Polymath's \(X\) is
\(6\cdot10^{10}+83952-\tfrac12\); the record rounds it down to
\(6\cdot10^{10}\), which moves \(\ell_X\) by \(1.4\cdot10^{-6}\)); physical height \(x\)
corresponds to the ordinate \(T=x/2\), so Platt–Trudgian's
\(X=5\cdot10^{12}+194858\) is the ordinate \(2.5\cdot10^{12}\), inside their
verified height \(3\cdot10^{12}\). For zeta the floor wanted is the constant
\(\tfrac14\ell_X-\tfrac12\kappa(\sigma_0)\), which Project 01's
finite-region rows assumed; the \(x\)-dependent floor
\(\tfrac14\log\tfrac x{4\pi}-\tfrac12\kappa(\sigma_0)\) is larger.

## 2. Unavoidable positive costs

The proposal's first instruction is a table of the costs that no
reallocation can remove, with the margin they must fit.

**2.1 The inherited budget (stopped).** Its margin is a normalized phase
error at most \(1/8\). Two of its terms are nonnegative and intrinsic to the
four-jet carrier design:

| Term (22 outer Note 01, eq. (6)) | Value at \(L=26.9\) (\(x\approx6\cdot10^{12}\)) | Against \(1/8\) |
| --- | --- | --- |
| carrier differentiation \(409/L\) | \(15.2\) | \(\times122\) |
| low-index \(1728\cdot4A_*/(L-1)\), \(A_*=218227/384\) | \(1.5\cdot10^5\) | \(\times1.2\cdot10^6\) |

Each alone exceeds the margin, and the budget's analytic setup needs
\(L\ge100002\). By the proposal's rule the budget stops here; 22 outer
Note 01 reached the same verdict ("a practical finite-to-asymptotic bridge
demands a different nonasymptotic error architecture"). Extracting its
exponent-pair constant would not change this.

**2.2 The chosen estimate.** For (E) the margin is not fixed: at \(t=0\) the
floor holds exactly (Project 01, Lemma 3.4), and for \(t>0\) the transport
of Section 3 moves the evaluation point to \(\sigma_*>\sigma_0\), which
raises the floor by
\[
g(t)=\tfrac12\bigl(\kappa(\sigma_0)-\kappa(\sigma_*)\bigr)\quad(+\ \tfrac14(\psi(\tfrac{\sigma_*+\mathfrak a}2)-\psi(\tfrac{\sigma_0+\mathfrak a}2))\ \text{for the family at }x=0).
\]
Any proof that bounds the heat-flow perturbation through majorants of the
Euler product pays the following, and \(E\) of Proposition 4.5 is their
sum:

| Cost | Order | Source |
| --- | --- | --- |
| C1 curvature of \(\log L\) | \(\tfrac12\tau^2(K_2\kappa+\tfrac12K_3)(\sigma_*)\) | second-order transport; attained in the worst case of the majorants |
| C2 curvature of \(\log\Gamma_F\) (family, small height) | \(\tfrac12\tau^2(A_1\kappa+\tfrac12A_2)(\sigma_*)\), \(A_1=\tfrac14\psi'\), \(A_2=-\tfrac18\psi''\) at \(\tfrac{\sigma_*+\mathfrak a}2\) | Gamma factor away from Stirling's range |
| C3 leakage into the critical strip | \(\exp(-(\sigma_*-1)^2/2\tau^2)\) times a power of \(q\lvert s\rvert\) | Gaussian mass left of \(\operatorname{Re}s=1\) |
| C4 the reflected term | \(e^{-p\ell_*/2}\) | functional equation (Polymath's \(B\)-term) |

As \(t\to0\), \(g/\tau^2\to\tfrac14K_2(\sigma_0)\ell\) and the sum of C1 and
C2 over \(\tau^2\) tends to \(\tfrac12(k\kappa+\tfrac12k_2)(\sigma_0)\),
\(k=K_2+A_1\), \(k_2=K_3+A_2\); so the small-time test passes once
\(\ell>2(k\kappa+\tfrac12k_2)/K_2\): \(6.40\) (even) and \(5.99\) (odd) at
\(p=\sqrt5\), and \(5.67\) for zeta; with the \(\psi\) part of \(g\) at
\(x=0\), \(5.22\) and \(5.38\) (record H). C3 and C4 are exponentially small
in \(\ell\). No cost exceeds the margin at the heights of the contract, so
the budget proceeds to Section 4.

## 3. The exact transport identity

**Lemma 3.1 (Gaussian form; proved).** For \(t\ge0\) and \(z\in\mathbb C\),
\(H_t(z)=\mathbb E\,H_0(z+i\sqrt{2t}\,N)\). With
\(\mathcal G(s)=\mathbb E\,F(s+\tau N)\) one has
\(H_t(z)=c\,\mathcal G(\tfrac12(1+iz))\),
\(\mathcal G(s)=\overline{\mathcal G(1-\bar s)}\), and for \(p>1\)
\[
S(x,p,t)=\tfrac12\operatorname{Re}\frac{\mathcal G'}{\mathcal G}(w),\qquad w=\sigma_0+\tfrac i2x .
\]

*Proof.*
\(\mathbb E\,H_0(z+i\beta N)=\int\Phi(u)e^{izu}\,\mathbb E\,e^{-\beta Nu}\,du=\int e^{\beta^2u^2/2}\Phi(u)e^{izu}du\)
by Fubini (\(\Phi\) decays like \(\exp(-\pi e^{4\lvert u\rvert}/q)\)), and
\(\beta=\sqrt{2t}\) gives \(H_t\). Substituting \(H_0(z)=cF(\tfrac12(1+iz))\)
and using \(N\stackrel d=-N\) gives \(H_t(z)=c\,\mathcal G(\tfrac12(1+iz))\)
with \(\tau=\beta/2\), and the functional equation of \(F\) passes to
\(\mathcal G\). Then \(H_t'(z)=\tfrac i2c\,\mathcal G'(\tfrac12(1+iz))\); at
\(z=x+ip\), \(\tfrac12(1+iz)=1-\bar w\), and differentiating
\(\mathcal G(s)=\overline{\mathcal G(1-\bar s)}\) gives
\((\mathcal G'/\mathcal G)(1-\bar w)=-\overline{(\mathcal G'/\mathcal G)(w)}\).
So
\(S=-\operatorname{Im}\bigl(\tfrac i2(\mathcal G'/\mathcal G)(1-\bar w)\bigr)=\tfrac12\operatorname{Re}(\mathcal G'/\mathcal G)(w)\);
\(\mathcal G(w)\ne0\) because every zero of \(H_t\) has
\(\lvert\operatorname{Im}z\rvert<1<p\) (Project 01, ledger H3). \(\square\)

**Lemma 3.2 (the Gamma saddle; proved).** *Family.* Let \(p>1\),
\(t\le\tfrac12\) and \(\ell_0=\log\tfrac q\pi+\psi(\tfrac{\sigma_0+\mathfrak a}2)>0\).
Then \(\mu\mapsto\tau^2\alpha(w+\mu)\) maps the closed half-plane
\(\{\operatorname{Re}\mu\ge0\}\) into itself and is a contraction there, so
it has a unique fixed point \(\mu_*\). Put \(s_*=w+\mu_*\),
\(\ell_*=2\operatorname{Re}\alpha(s_*)\), \(\sigma_*=\operatorname{Re}s_*\).
Then \(\sigma_*=\sigma_0+\tfrac12\tau^2\ell_*=\sigma_0+\tfrac t4\ell_*\) and
\(\ell_*\ge\ell_*^{(0)}\ge\ell_0\), where \(\ell_*^{(0)}=2\alpha(\sigma^{(0)})\)
and \(\sigma^{(0)}\) is the unique real solution of
\(\sigma=\sigma_0+\tau^2\alpha(\sigma)\) (the saddle at \(x=0\)).
*Zeta.* For \(x\ge40\) and \(p>1\) the same map has a unique fixed point in
\(D_x=\{\mu:0\le\operatorname{Re}\mu\le R_x,\ \lvert\operatorname{Im}\mu\rvert\le\tfrac12\}\),
\(R_x=\tfrac18\log x+1\); there \(\operatorname{Im}s_*\ge\tfrac x2-\tfrac12\) and
\(\ell_*\ge\log\bigl((\tfrac x2-\tfrac12)/2\pi\bigr)-2c(\tfrac12s_*)\), with
\(c\) as in Lemma 4.3. (\(S\) is even in \(x\) for zeta.)

*Proof.* Family: for \(\operatorname{Re}\mu\ge0\),
\(\operatorname{Re}(w+\mu)\ge\sigma_0\). For \(\operatorname{Re}z>0\),
\(\operatorname{Re}\psi(z)\ge\psi(\operatorname{Re}z)\) (each term of
\(\psi(z)=-\gamma+\sum_{n\ge0}(\tfrac1{n+1}-\tfrac1{n+z})\) has real part
increasing in \(\lvert\operatorname{Im}z\rvert\); Project 01, Lemma 3.4) and
\(\lvert\psi'(z)\rvert\le\psi'(\operatorname{Re}z)\) (termwise from
\(\psi'(z)=\sum(n+z)^{-2}\)). So
\(\operatorname{Re}\tau^2\alpha(w+\mu)\ge\tfrac12\tau^2\ell_0>0\), and
\(\lvert\tfrac d{d\mu}\tau^2\alpha(w+\mu)\rvert\le\tfrac14\tau^2\psi'(\tfrac{\sigma_0+\mathfrak a}2)\le\tfrac1{16}\psi'(\tfrac12)=\tfrac{\pi^2}{32}<0.31\)
(below \(0.15\) when \(p\ge\sqrt5\)). Banach's theorem gives \(\mu_*\), and
\(\operatorname{Re}\mu_*=\tau^2\operatorname{Re}\alpha(s_*)=\tfrac12\tau^2\ell_*\).
Next \(\ell_*\ge2\alpha(\sigma_*)\) and
\(\sigma_*\ge\sigma_0+\tau^2\alpha(\sigma_*)\); since
\(h(\sigma)=\sigma-\sigma_0-\tau^2\alpha(\sigma)\) is strictly increasing
(\(\tau^2\alpha'<1\)) with \(h(\sigma^{(0)})=0\le h(\sigma_*)\),
\(\sigma_*\ge\sigma^{(0)}\ge\sigma_0\), and \(\alpha\) increases on the real
axis. Zeta: for \(\mu\in D_x\), \(s=w+\mu\) has
\(\operatorname{Re}s\in[\sigma_0,\sigma_0+R_x]\) and
\(\operatorname{Im}s\ge\tfrac x2-\tfrac12\ge19\). There
\(\lvert\alpha'(s)\rvert\le2/\operatorname{Im}s\le0.11\) (Lemma 4.2), so the
map is a contraction. With \(z=s/2\), \(\operatorname{Im}\psi(z)=\sum_{n\ge0}\operatorname{Im}z/\lvert z+n\rvert^2\in(0,\tfrac\pi2+\tfrac1{2\operatorname{Re}z}]\)
and \(\lvert\operatorname{Im}(\tfrac1s+\tfrac1{s-1})\rvert\le2/\operatorname{Im}s\),
so \(\lvert\operatorname{Im}\tau^2\alpha(s)\rvert\le\tfrac14(\tfrac\pi4+\tfrac12+0.11)<\tfrac12\).
Lemma 4.3 and \(\operatorname{Re}(\tfrac1s+\tfrac1{s-1})>0\) give
\(\tfrac12\log\tfrac{\lvert s\rvert}{2\pi}-c(z)\le\operatorname{Re}\alpha(s)\le\tfrac12\log\tfrac{\lvert s\rvert}{2\pi}+\tfrac1{12\operatorname{Re}z\lvert z\rvert}+\tfrac2{\operatorname{Im}s}\)
(the upper bound from \(\operatorname{Re}\psi(z)\le\log\lvert z\rvert+\lvert I(z)\rvert\) in
Lemma 4.3's notation). The lower bound is positive, and since
\(\lvert s\rvert\le x\) on \(D_x\), \(\tau^2\operatorname{Re}\alpha(s)\le\tfrac18\log\tfrac x{2\pi}+0.01<R_x\).
So \(D_x\) is mapped into itself; the bound on \(\ell_*\) is the lower bound
at \(s_*\). \(\square\)

**Lemma 3.3 (the shifted representation; proved).** Let
\(G(v)=F(s_*+v)e^{-\alpha(s_*)v}/F(s_*)\), an entire function of \(v\) of
order one with \(G(0)=1\), and \(c_1=(\mathcal L'/\mathcal L)(s_*)\)
(\(\operatorname{Re}s_*>1\), so \(F(s_*)\ne0\)). Then
\[
\frac{\mathcal G'}{\mathcal G}(w)-\frac{F'}{F}(s_*)=\frac{\int_{\mathbb R}(G'-c_1G)\varphi_\tau}{\int_{\mathbb R}G\varphi_\tau},\qquad
\int_{\mathbb R}(G'-c_1G)\varphi_\tau=\int_{\mathbb R}\Bigl(\frac v{\tau^2}-c_1\Bigr)G\varphi_\tau .
\]

*Proof.* \(h\mapsto F^{(k)}(w+h)\varphi_\tau(h)\) is entire, and on
\(\operatorname{Re}h=\pm R\), between \(0\) and \(\operatorname{Im}\mu_*\),
it is \(O(e^{R^{1+\epsilon}-R^2/2\tau^2})\); so the line of integration in
\(\mathcal G^{(k)}(w)=\int F^{(k)}(w+h)\varphi_\tau(h)dh\) moves to
\(\mu_*+\mathbb R\). Since \(\mu_*/\tau^2=\alpha(s_*)\),
\(\varphi_\tau(\mu_*+v)=\varphi_\tau(v)e^{-\alpha(s_*)v-\mu_*^2/2\tau^2}\), so
\(\mathcal G(w)=\kappa_0F(s_*)\int G\varphi_\tau\) and
\(\mathcal G'(w)=\kappa_0F(s_*)\int(G'+\alpha(s_*)G)\varphi_\tau\) with
\(\kappa_0=e^{-\mu_*^2/2\tau^2}\), because
\(F'(s_*+v)e^{-\alpha(s_*)v}/F(s_*)=G'(v)+\alpha(s_*)G(v)\). Subtract
\((F'/F)(s_*)=\alpha(s_*)+c_1\). The second identity is Gaussian integration
by parts, \(\varphi_\tau'=-(v/\tau^2)\varphi_\tau\), valid because \(G\) has
order one. \(\square\)

So the question is how far the complex weight \(G\varphi_\tau\) is from the
pure tilt \(e^{c_1v}\varphi_\tau\), for which the right side vanishes. Where
\(\operatorname{Re}(s_*+v)>1\), \(G=e^{c_1v+D(v)}\) with
\(D(v)=[\log\mathcal L(s_*+v)-\log\mathcal L(s_*)-c_1v]+[\log\Gamma_F(s_*+v)-\log\Gamma_F(s_*)-\alpha(s_*)v]\),
and \(G'-c_1G=\Delta G\) with
\(\Delta(v)=(F'/F)(s_*+v)-(F'/F)(s_*)\).

## 4. Majorants and the bound

**Lemma 4.1 (Euler-product majorants; proved).** For
\(\operatorname{Re}s=\sigma>1\) and \(j\ge0\),
\(\lvert(\mathcal L'/\mathcal L)^{(j)}(s)\rvert\le(-1)^j\kappa^{(j)}(\sigma)\),
\(\lvert\log\mathcal L(s)\rvert\le\log\zeta(\sigma)\) and
\(\zeta(2\sigma)/\zeta(\sigma)\le\lvert\mathcal L(s)\rvert\le\zeta(\sigma)\).
Hence, for real \(v\) with \(\sigma_*+\min(v,0)>1\),
\[
\lvert(\mathcal L'/\mathcal L)(s_*+v)-c_1\rvert\le\lvert\kappa(\sigma_*+v)-\kappa(\sigma_*)\rvert,\qquad
\lvert(\mathcal L'/\mathcal L)(s_*+v)-c_1-v(\mathcal L'/\mathcal L)'(s_*)\rvert\le[\![\kappa]\!]_v,
\]
\[
\lvert\log\mathcal L(s_*+v)-\log\mathcal L(s_*)\rvert\le\lvert\log\zeta(\sigma_*+v)-\log\zeta(\sigma_*)\rvert,\qquad
\lvert\log\mathcal L(s_*+v)-\log\mathcal L(s_*)-c_1v\rvert\le[\![\log\zeta]\!]_v .
\]

*Proof.* \(\mathcal L'/\mathcal L=-\sum\chi(n)\Lambda(n)n^{-s}\) and
\(\log\mathcal L=\sum\chi(n)\Lambda(n)(\log n)^{-1}n^{-s}\) with
\(\lvert\chi(n)\rvert\le1\); the bounds on \(\lvert\mathcal L\rvert\) are the
Euler product. Each difference is an integral along the horizontal segment
from \(s_*\) to \(s_*+v\) of a derivative bounded by a majorant of fixed
sign, whose integral is the corresponding difference or Taylor remainder
of \(\kappa\) or \(\log\zeta\), both convex. \(\square\)

**Lemma 4.2 (Gamma majorants; proved).** *Family.* For
\(\operatorname{Re}z>0\), \(\lvert\psi'(z)\rvert\le\psi'(\operatorname{Re}z)\)
and \(\lvert\psi''(z)\rvert\le-\psi''(\operatorname{Re}z)\) (termwise). With
\(\gamma(\sigma)=-\tfrac12\psi(\tfrac{\sigma+\mathfrak a}2)\) and
\(\lambda(\sigma)=\log\Gamma(\tfrac{\sigma+\mathfrak a}2)\), for
\(\sigma_*+\min(v,0)>-\mathfrak a\):
\(\lvert\alpha(s_*+v)-\alpha(s_*)\rvert\le\lvert\gamma(\sigma_*+v)-\gamma(\sigma_*)\rvert\),
\(\lvert\alpha(s_*+v)-\alpha(s_*)-v\alpha'(s_*)\rvert\le[\![\gamma]\!]_v\),
and
\(\lvert\log\Gamma_F(s_*+v)-\log\Gamma_F(s_*)-\alpha(s_*)v\rvert\le[\![\lambda]\!]_v=:\vartheta(v)\).
*Zeta.* If \(\lvert\operatorname{Im}s\rvert\ge T\ge10\), at any real part,
\(\lvert\alpha'(s)\rvert\le2/T\) and \(\lvert\alpha''(s)\rvert\le3/T^2\); put
\(\vartheta(v)=v^2/T\).

*Proof.* The family bounds are integrals along the segment, as in Lemma
4.1, since \(\lvert\alpha'\rvert\le-\gamma'\),
\(\lvert\alpha''\rvert\le\gamma''\) and \(\lambda''=-\gamma'\). For zeta, with
\(z=s/2=x+iy\), \(\sum_{n\ge0}\lvert z+n\rvert^{-2}\le y^{-2}+\pi/y\) and
\(\sum_{n\ge0}\lvert z+n\rvert^{-3}\le y^{-3}+2y^{-2}\) (unimodal summands:
the sum is at most the integral plus the maximum), so
\(\tfrac14\lvert\psi'(z)\rvert\le\tfrac{\pi}{2T}+\tfrac1{T^2}\) and
\(\tfrac18\lvert\psi''(z)\rvert\le\tfrac2{T^3}+\tfrac2{T^2}\); add
\(\lvert s\rvert^{-2}+\lvert s-1\rvert^{-2}\le2T^{-2}\) and
\(2\lvert s\rvert^{-3}+2\lvert s-1\rvert^{-3}\le4T^{-3}\). \(\square\)

**Lemma 4.3 (a Stirling inequality; proved).** For
\(\operatorname{Re}z=x>0\),
\(\log\lvert z\rvert\le\operatorname{Re}\psi(z)+\tfrac x{2\lvert z\rvert^2}+\tfrac1{12x\lvert z\rvert}=:\operatorname{Re}\psi(z)+c(z)\).

*Proof.* Binet's formula for \(\psi\) (DLMF §5.9(ii); quoted from memory,
its equation number not checked; the subagent check of Section 10
confirmed it to \(10^{-29}\)) is
\(\psi(z)=\log z-\tfrac1{2z}-I(z)\), \(I(z)=\int_0^\infty\beta(u)e^{-zu}du\),
\(\beta(u)=\tfrac1{e^u-1}-\tfrac1u+\tfrac12\). Since \(\beta(0)=0\),
\(I(z)=z^{-1}\int_0^\infty\beta'(u)e^{-zu}du\), with
\(\beta'(u)=\tfrac14f(u/2)\), \(f(v)=v^{-2}-\sinh^{-2}v\). Here \(f>0\)
because \(\sinh v>v\), and \(f\le\tfrac13\): for \(v\ge\sqrt3\) because
\(v^{-2}\le\tfrac13\), and for \(v<\sqrt3\) because
\(\sinh^2v\,(3-v^2)=\sum_{n\ge1}(3a_n-a_{n-1})v^{2n}\) with
\(a_n=2^{2n-1}/(2n)!\), \(a_0=0\), whose coefficients are \(3\), \(0\) and
then \(a_{n-1}(\tfrac{12}{2n(2n-1)}-1)<0\), so
\(\sinh^2v\,(3-v^2)\le3v^2\). Hence \(0\le\beta'\le\tfrac1{12}\),
\(\lvert I(z)\rvert\le1/(12x\lvert z\rvert)\), and real parts give the claim.
\(\square\)

For the family put \(c_*=\tfrac1{2x_*}+\tfrac1{12x_*^2}\) with
\(x_*=\tfrac12(\sigma_*+\mathfrak a)\), which bounds \(c(z_*)\),
\(z_*=\tfrac12(s_*+\mathfrak a)\), at every height. Then, for
\(0<u\le\sigma_*\) at the height of \(s_*\),
\[
q\lvert u+i\operatorname{Im}s_*\rvert\le2q\lvert z_*\rvert\le Q_*:=2\pi e^{\ell_*+c_*},
\]
since \(\log\lvert z_*\rvert\le\operatorname{Re}\psi(z_*)+c_*=\ell_*-\log\tfrac q\pi+c_*\);
for zeta the same \(Q_*\), with \(c_*=c(\tfrac12s_*)\), bounds \(\lvert s\rvert\).

**Lemma 4.4 (partial summation in the strip; proved).** For \(\sigma>0\),
\(s=\sigma+iT\) and every integer \(N\ge1\):
\(\lvert L(s,\chi)\rvert\le1+\int_1^Nu^{-\sigma}du+q\lvert s\rvert N^{-\sigma}/(2\sigma)\)
for \(\chi\) primitive modulo \(q\ge3\), and
\(\lvert\zeta(s)\rvert\le1+\int_1^Nu^{-\sigma}du+N^{1-\sigma}/\lvert s-1\rvert+\tfrac12N^{-\sigma}+\lvert s\rvert N^{-\sigma}/(2\sigma)\).

*Proof.*
\(L(s,\chi)=\sum_{n\le N}\chi(n)n^{-s}+s\int_N^\infty(A(u)-A(N))u^{-s-1}du\)
with \(A(u)=\sum_{n\le u}\chi(n)\); a sum of \(\chi\) over consecutive
integers equals a sum over \(r<q\) of them, which is also minus the sum
over the other \(q-r\) of a period, so \(\lvert A(u)-A(N)\rvert\le q/2\). For
zeta,
\(\zeta(s)=\sum_{n\le N}n^{-s}+\tfrac{N^{1-s}}{s-1}-\tfrac12N^{-s}-s\int_N^\infty(\{u\}-\tfrac12)u^{-s-1}du\).
Both identities hold for \(\sigma>1\) and extend to \(\sigma>0\). \(\square\)

The minimum over \(N\) is taken near \(N=Q/2\); for zeta
\(\lvert s-1\rvert\ge\lvert\operatorname{Im}s\rvert\ge T\) is used. This is
weaker than the convexity bound by about \((q\lvert s\rvert)^{(1-\sigma)/2}\);
Rademacher's explicit convexity bound would improve the small-conductor
rows and is not used, so nothing here depends on an unread import.

**Proposition 4.5 (the bound; proved).** Fix the hypotheses of Lemma 3.2,
\(t\in(0,\tfrac12]\) and \(V\in(0,\sigma_*-1)\). Write
\(k=K_2(\sigma_*)+A_1(\sigma_*)\) (zeta: \(K_2(\sigma_*)+2/T\)),
\(\kappa_*=\kappa(\sigma_*)\), \(\mathfrak M=\kappa+\gamma\) (zeta:
\(\mathfrak M=\kappa\)), and define, for \(v\ge-V\),
\[
r(v)=[\![\mathfrak M]\!]_v\ \bigl(\text{zeta: }[\![\kappa]\!]_v+\tfrac32v^2/T^2\bigr),\qquad
g(v)=\exp\bigl(\lvert\log\zeta(\sigma_*+v)-\log\zeta(\sigma_*)\rvert+\vartheta(v)\bigr),\qquad
D_m(v)=[\![\log\zeta]\!]_v+\vartheta(v),
\]
and, for \(v<-V\) with \(\sigma=\sigma_*+v\) and
\(z_\zeta=\zeta(\sigma_*)/\zeta(2\sigma_*)\),
\[
g_*(v)=\begin{cases}z_\zeta\,\Lambda(\sigma)\,e^{\vartheta(v)},&\tfrac12\le\sigma<\sigma_*-V,\\
z_\zeta\,\Lambda(1-\sigma)\exp\bigl(\tfrac12\ell_*(1-2\sigma)+\vartheta(1-\sigma-\sigma_*)\bigr),&\sigma<\tfrac12,\end{cases}
\]
where \(\Lambda(u)=\zeta(u)\) for \(u\ge\sigma_*\); for \(1<u<\sigma_*\) the
smaller of \(\zeta(u)\) and Lemma 4.4's bound with \(q\lvert s\rvert\)
(zeta: \(\lvert s\rvert\)) replaced by \(Q_*\); and that bound alone for
\(u\le1\). Put
\[
M_\rho=\int_{-V}^\infty rg\varphi_\tau,\quad B_V=g(-V)\varphi_\tau(V),\quad P_1=\int_{-V}^\infty e^{\kappa_*\lvert v\rvert}(e^{D_m}-1)\varphi_\tau,
\]
\[
D_L=\int_{-\infty}^{-V}g_*\varphi_\tau,\quad N_L=\int_{-\infty}^{-V}g_*\Bigl(\frac{\lvert v\rvert}{\tau^2}+\kappa_*\Bigr)\varphi_\tau,\quad P_2=\int_{-\infty}^{-V}(g_*+e^{\kappa_*\lvert v\rvert})\varphi_\tau,
\]
and \(d_0=e^{-\tau^2\kappa_*^2/2}-P_1-P_2\). If \(\tau^2k<1\) and
\(d_0>0\), then
\[
\Bigl\lvert\frac{\mathcal G'}{\mathcal G}(w)-\frac{F'}{F}(s_*)\Bigr\rvert\le E:=\frac{\tau^2k\kappa_*}{1-\tau^2k}+\frac{M_\rho+B_V+\tau^2k\kappa_*D_L+(1+\tau^2k)N_L}{(1-\tau^2k)\,d_0}.
\]

*Proof.* Write \(\mathcal N\) and \(\mathcal D\) for the numerator and
denominator of Lemma 3.3. On \([-V,\infty)\), Lemmas 4.1–4.2 give
\(\lvert G\rvert\le g\), \(\lvert D\rvert\le D_m\), and, with
\(\Delta_1=\Delta'(0)=(F'/F)'(s_*)\), \(\lvert\Delta_1\rvert\le k\) and
\(\lvert\rho\rvert\le r\) for \(\rho(v)=\Delta(v)-\Delta_1v\). For \(v<-V\),
\(\lvert G(v)\rvert\le g_*(v)\): when \(\sigma\ge\tfrac12\),
\(\lvert G\rvert=\lvert\mathcal L(\sigma+i\operatorname{Im}s_*)/\mathcal L(s_*)\rvert\exp\operatorname{Re}[\log\Gamma_F(s_*+v)-\log\Gamma_F(s_*)-\alpha(s_*)v]\),
and Lemmas 4.1–4.4 apply, with
\(\lvert\mathcal L(s_*)\rvert\ge\zeta(2\sigma_*)/\zeta(\sigma_*)\); when
\(\sigma<\tfrac12\), \(\lvert F(\sigma+iT)\rvert=\lvert F(1-\sigma+iT)\rvert\),
and the Gamma ratio from \(s_*\) to \(1-\sigma+i\operatorname{Im}s_*\)
contributes \(\exp(\tfrac12\ell_*(1-\sigma-\sigma_*)+\vartheta(1-\sigma-\sigma_*))\),
which with \(e^{-\operatorname{Re}\alpha(s_*)v}=e^{\ell_*(\sigma_*-\sigma)/2}\)
gives the stated exponent. Gaussian integration by parts on
\([-V,\infty)\),
\(\int_{-V}^\infty v\varphi_\tau G=\tau^2\varphi_\tau(V)G(-V)+\tau^2\int_{-V}^\infty\varphi_\tau G'\),
turns Lemma 3.3 into \(\mathcal N=\varphi_\tau(V)G(-V)+X+\mathcal N_L\) with
\(X=\int_{-V}^\infty\Delta G\varphi_\tau\) and
\(\mathcal N_L=\int_{-\infty}^{-V}(v/\tau^2-c_1)G\varphi_\tau\), and, applied
once more to \(\Delta_1\int vG\varphi_\tau\),
\[
(1-\tau^2\Delta_1)X=\tau^2\Delta_1\bigl(\varphi_\tau(V)G(-V)+c_1\mathcal D_E\bigr)+\int_{-V}^\infty\rho G\varphi_\tau,\qquad
\mathcal D_E=\int_{-V}^\infty G\varphi_\tau .
\]
Hence, with \(\mathcal D=\mathcal D_E+\mathcal D_L\),
\[
\mathcal N-\frac{\tau^2\Delta_1c_1}{1-\tau^2\Delta_1}\mathcal D=\frac{\varphi_\tau(V)G(-V)+\int_{-V}^\infty\rho G\varphi_\tau-\tau^2\Delta_1c_1\mathcal D_L+(1-\tau^2\Delta_1)\mathcal N_L}{1-\tau^2\Delta_1},
\]
whose modulus is at most \(d_0\) times the second fraction of \(E\),
because \(\lvert c_1\rvert\le\kappa_*\). Finally
\(\mathcal D=e^{\tau^2c_1^2/2}+\int_{-V}^\infty e^{c_1v}(e^{D}-1)\varphi_\tau+\int_{-\infty}^{-V}(G-e^{c_1v})\varphi_\tau\)
and \(\lvert e^{\tau^2c_1^2/2}\rvert\ge e^{-\tau^2\kappa_*^2/2}\), so
\(\lvert\mathcal D\rvert\ge d_0\). Divide. \(\square\)

**Theorem 4.6 (transport law and floor; proved).** Under the hypotheses of
Proposition 4.5,
\[
\Bigl\lvert S(x,p,t)-\tfrac12\operatorname{Re}\tfrac{F'}F(s_*)\Bigr\rvert\le\tfrac12E,\qquad
S(x,p,t)\ge\tfrac14\ell_*-\tfrac12\kappa(\sigma_*)-\tfrac12E .
\]
For the family every quantity in \(E\) is a function of
\((\ell_*,\tau,p,\mathfrak a,V)\), so the bound at \(x\) is
\(\mathfrak F(\ell_*(x))\) with
\(\mathfrak F(\ell)=\tfrac14\ell-\tfrac12\kappa(\sigma_0+\tfrac12\tau^2\ell)-\tfrac12E(\ell)\);
for zeta \(E\) depends on \(\ell_*\) and on the height through \(T\).

*Proof.* Lemma 3.1, Proposition 4.5, and
\(\tfrac12\operatorname{Re}(F'/F)(s_*)=\tfrac14\ell_*+\tfrac12\operatorname{Re}c_1\ge\tfrac14\ell_*-\tfrac12\kappa_*\).
In the family case \(Q_*\), \(\Lambda\), \(\vartheta\), \(r\), \(g\) and
\(D_m\) are functions of real arguments fixed by
\(\sigma_*=\sigma_0+\tfrac12\tau^2\ell_*\) and \(\ell_*\). \(\square\)

*Reading.* To second order in \(\tau\) the deviation is
\(\tau^2(\Delta_1c_1+\tfrac12\Delta''(0))=\tfrac12\tau^2(\mathcal L''/\mathcal L)'(s_*)+\tau^2(\alpha'c_1+\tfrac12\alpha'')(s_*)\),
which record C confirms for zeta (Section 6). So, to that order, the heat
flow at height \(p\) is evaluation of the time-zero quantity at
\(s_*=w+\tfrac t2\alpha(s_*)\): at height \(p+t\ell_*/2\) instead of \(p\),
and at real part \(x+t\operatorname{Im}\alpha(s_*)\approx x+\pi t/4\). The
second shift is the drift of the zeros toward the origin at speed about
\(\pi/4\) that the zero dynamics \(\dot z_j=2\sum_{k\ne j}(z_j-z_k)^{-1}\) of
\(\partial_tH=-\partial_z^2H\) give in the mean-field approximation: the
Hilbert transform of the density \(\tfrac1{4\pi}\log\tfrac{\lvert x\rvert}{4\pi}\)
contributes \(-\pi/8\) to the sum at \(x>0\) (a heuristic, not used in any
proof here).

## 5. Evaluation (numerical)

\(E\) is evaluated in floating point (record D–H): \(\zeta\) and
\(\zeta^{(j)}\) by Euler–Maclaurin at real and complex points; \(\psi\),
\(\psi'\), \(\psi''\) by recurrence and asymptotic series, all checked in
record A; the real-variable majorants tabulated on logarithmic grids
(relative interpolation error below \(4\cdot10^{-5}\)); composite Simpson
rules; \(V=\sigma_*-1-\eta\) with the better of \(\eta\in\{0.03,0.08\}\);
Gaussian tails beyond \(40\tau\) dropped. None of this is outward-rounded,
and an independent implementation (Section 10) differs from the programme
by up to \(4\cdot10^{-5}\) relative, in both directions.

**5.1 Thresholds** (record H). The smallest \(\ell\) with \(g(t)\ge E/2\) at
every \(t\) of the grid \(\{0.001,0.002,0.005,0.01,\dots,0.5\}\) (20 points),
counting only the \(\kappa\) part of \(g\), by bisection to \(0.03\):

| Case | \(p=\sqrt5\) | \(p=2.5\) | \(p=3\) | \(p=4\) | small-time threshold at \(p=\sqrt5\) |
| --- | --- | --- | --- | --- | --- |
| family, even | 10.65 | 8.77 | 6.74 | 4.40 | 6.40 |
| family, odd | 10.12 | 8.22 | 6.19 | 3.92 | 5.99 |
| zeta (Gamma constants of height \(10^4\)) | 9.62 | 7.67 | 5.56 | 3.29 | 5.67 |

Just above \(\ell_1\) the binding time is near \(t\approx0.2\) (record E: at
\(\ell=10\), \(p=\sqrt5\), the even family fails at \(t=0.2\) by \(0.09\));
from \(\ell=11\) on, the margin is smallest at the smallest time of the
grid, where it is \(\tau^2\) times the small-time coefficient of Section
2.2. Below \(t=0.001\) the next order is not bounded here. \(E\) is
nonincreasing in \(\ell\) at all 12 sampled \((t,p,\mathfrak a)\) settings
(record H, \(\ell\) from 10 to 40); that monotonicity, which turns the
evaluation at the smallest \(\ell_*\) into a bound at every height, is
checked, not proved. With the zeta row, (E) holds at every grid time from
\(x\approx4\pi e^{9.62}\approx1.9\cdot10^5\) at \(p=\sqrt5\), and from
\(x=2\cdot10^4\) at \(p=3\), the height where the Gamma constants were taken.

**5.2 Lemma \(A_p\) for the family** (record F, H). At \(x=0\) the saddle is
real and \(\ell_*=\ell_*^{(0)}\); Lemma 3.2 gives \(\ell_*(x)\ge\ell_*^{(0)}\)
at every \(x\). With \(\mathfrak F\) increasing (Section 5.1),
\(S(x,p,t)\ge\mathfrak F(\ell_*^{(0)}(t))=:H(t)\) for every real \(x\). The
smallest conductor with \(H(t)\ge C_{q,\mathfrak a}(p)\) at every time of the
grid (bisection in \(\log_{10}q\) to \(0.006\)):

| Parity | \(p=\sqrt5\) | \(p=3\) |
| --- | --- | --- |
| even | \(q\ge1.08\cdot10^5\) (\(\ell_0=9.50\)) | \(q\ge1.32\cdot10^3\) (\(\ell_0=5.46\)) |
| odd | \(q\ge4.89\cdot10^4\) (\(\ell_0=9.49\)) | \(q\ge6.6\cdot10^2\) (\(\ell_0=5.39\)) |

The conductor thresholds sit below the \(\ell_1\) of Section 5.1 because the
\(\psi\) part of the gain counts at \(x=0\). At \(q=10^6,10^8,10^{10},10^{12}\)
the excess \(\min_t(H(t)-C_{q,\mathfrak a}(p))\) is positive for both
parities and \(p\in\{\sqrt5,3\}\) (record F, \(0.0014\) to \(0.0077\),
attained at \(t=0.001\)), and at \(t=\tfrac12\) it is \(0.37\) to \(0.97\).
So on the grid Lemma \(A_p\) holds with \(\delta=0\), and the floor rises
with \(t\).

**5.3 Zeta beyond \(X\)** (record F). At Polymath's \(X=6\cdot10^{10}\)
(\(\ell_X=22.29\)) and Platt–Trudgian's \(X=5\cdot10^{12}+194858\)
(\(\ell_X=26.71\)), the excess
\(\min_t\bigl(H(t)-(\tfrac14\ell_X-\tfrac12\kappa(\sigma_0))\bigr)\) over the
grid, with \(H\) sampled at \(\ell_X+\{0,1,3\}\), is:

| \(p\) | \(\sqrt5\) | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- |
| Polymath \(X\) | 0.0051 | 0.0021 | 0.00088 | 0.00044 | 0.00025 |
| Platt–Trudgian \(X\) | 0.0064 | 0.0026 | 0.0011 | 0.00054 | 0.00030 |

all attained at \(t=0.001\). They are thin at large \(p\) only because
\(\tau^2\) is small there; the floor at those times is
\(\tfrac14\ell_X-\tfrac12\kappa(\sigma_0)\) to within the small-time
coefficient. So (E) holds on the grid at every \(x\ge X\) with the floor
Project 01's finite-region rows assumed.

## 6. Validation (numerical)

**6.1 The Gaussian representation** (record B). For zeta at
\((x,p,t)=(3,\sqrt5,0)\), \((10,\sqrt5,0.1)\), \((20,3,0.3)\),
\((25,\sqrt5,0.5)\), \(S\) from Polymath's kernel integral and \(S\) from
the Gaussian average of \(\xi\) agree to \(9\cdot10^{-16}\). The two routes
share no formula beyond the definition of \(\xi\).

**6.2 The transport law** (record C, D). Zeta at \(x=10^3\) and \(10^4\)
(\(\ell_*=4.38\), \(6.68\)), \(p\in\{\sqrt5,3\}\),
\(t\in\{0.02,0.1,0.3,0.5\}\): \(S\) by the Gaussian average of \(\xi\), the
main term \(\tfrac12\operatorname{Re}(F'/F)(s_*)\) and the second-order term
of Section 4. Characters: real characters modulo 10007 (odd), 10009 (even),
100003 and 1000003 (odd) and 1000033 (even), and a cubic character modulo
10009; \(x\in\{0,2,10\}\), \(p\in\{\sqrt5,3\}\), \(t\in\{0.05,0.2,0.5\}\); \(S\)
by the kernel integral with Gauss-sum root numbers, the main term as the
kernel's \(S\) at time zero at \((2\operatorname{Im}s_*,2\operatorname{Re}s_*-1)\).
Findings:

- the deviation \(\lvert\varepsilon\rvert\) (zeta: of
  \(\mathcal G'/\mathcal G\); characters: of its real part) is at most
  \(0.044\) for zeta and \(0.117\) for the characters, the largest at
  \(x=0\) for the even character modulo 10009 at \(t=\tfrac12\);
- for zeta the second-order term accounts for most of it (at \(x=10^3\),
  \(p=\sqrt5\): \(0.0048\) against \(0.0047\) at \(t=0.02\));
- \(E\ge\lvert\varepsilon\rvert\) at all 124 points; the ratio runs from
  \(1.6\) (even character modulo 1000033, \(x=0\), \(p=3\), \(t=\tfrac12\))
  to about 1300, median 22, and is largest at \(p=\sqrt5\) and moderate
  \(\ell_*\);
- \(S(x,p,t)\) exceeds the time-zero floor at the same \(x\) at every point,
  including those below the thresholds of Section 5.

These test the identity and the size of \(E\) at moderate heights. They do
not test the high-height regime of Section 5.3, where the theorem rather
than a computation is the evidence.

## 7. What this gives the consumers

**Target A** (planning, record G). With \(H(t)\) in place of the constant
\(C_{q,\mathfrak a}(p)\), the comparison
\(Q'=-2-\tfrac{4H(t)}pQ+\tfrac{8Q}{p^2-Q}\), \(Q(0)=a\), run to \(Q=0\) and
optimized over \(p\) (heat floor: \(p\) within \(0.45\) of the constant
optimum, step \(0.15\)), gives:

| \(q\) | Parity | Start | Constant floor: \(\lambda\) (\(p\)) | Heat floor: \(\lambda\) (\(p\)) | Change |
| --- | --- | --- | --- | --- | --- |
| \(10^6\) | even | \(a=1\) | 0.3161 (2.85) | 0.3076 (2.70) | −2.7% |
| \(10^6\) | odd | \(a=1\) | 0.3073 (2.69) | 0.2990 (2.54) | −2.7% |
| \(10^6\) | even | \(a=9/16\) | 0.2084 (2.79) | 0.2055 (2.64) | −1.4% |
| \(10^6\) | odd | \(a=9/16\) | 0.2041 (2.63) | 0.2011 (2.48) | −1.4% |
| \(10^8\) | even | \(a=1\) | 0.2618 (2.37) | 0.2519 (2.37) | −3.8% |
| \(10^8\) | odd | \(a=1\) | 0.2541 (2.27) | 0.2447 (2.27) | −3.7% |
| \(10^8\) | even | \(a=9/16\) | 0.1807 (2.31) | 0.1761 (2.16) | −2.6% |
| \(10^8\) | odd | \(a=9/16\) | 0.1765 (2.21) | 0.1719 (2.06) | −2.6% |
| \(10^{10}\) | even | \(a=1\) | 0.2217 (2.24) | 0.2129 (2.24) | −4.0% |
| \(10^{10}\) | odd | \(a=1\) | 0.2162 (2.24) | 0.2088 (2.24) | −3.4% |
| \(10^{12}\) | even | \(a=1\) | 0.1936 (2.24) | 0.1868 (2.24) | −3.5% |
| \(10^{12}\) | odd | \(a=1\) | 0.1897 (2.24) | 0.1839 (2.24) | −3.1% |
| \(10^{12}\) | even | \(a=9/16\) | 0.1394 (1.86) | 0.1328 (1.71) | −4.8% |
| \(10^{12}\) | odd | \(a=9/16\) | 0.1362 (1.81) | 0.1306 (1.81) | −4.1% |

(The \(a=9/16\) rows at \(10^{10}\) are in record G.) The constant-floor
column reproduces Project 01's Section 4.6. The heat-floor column uses
\(H(t)\) at \(\ell_*^{(0)}(t)\) on nine times, linearly interpolated, and the
floating evaluation of \(E\); at \(p<\sqrt5\) (the \(a=9/16\) rows) the
thresholds of Section 5 were not computed, and those rows use \(H(t)\) as
evaluated. At \(q=10^8\) the unconditional \(a=1\) values are now
\(0.245\)–\(0.252\), further below the conditional baseline \(0.2812\) of
Project 01's Corollary 3.2. All of these are conditional on H12, on a
written comparison theorem and on the certification of Section 9.2.

**Target B.** Platt's verification heights give \(\ell\approx16.6\) for every
\(q\le400{,}000\) (Project 01, Section 4.1), above every \(\ell_1\) of Section
5.1, so on the grid the exterior floor holds with \(\delta=0\) beyond the
verified height of every such character. Target B still needs the
per-character barrier over the comparison interval and the finite-region
argument.

**Zeta.** Section 5.3 supplies the floor beyond \(X\) for \(p\) from
\(\sqrt5\) to 6 at every grid time \(t\le\tfrac12\), which covers the band
\(3\le\operatorname{Im}z\le6\), \(t\le\tfrac15\) of Hakimoglu-Brown's
approximation (Project 01, ledger H11). Whether his comparison then
improves, and how its finite region is closed, belongs to this project's
next phase once his Lemma 2 and Theorem 9 are read against this note.

## 8. Premises and controls

Theorem 4.6 uses: the Hermitian functional equation with a degree-one Gamma
factor; the Euler product, only through Lemma 4.1 (coefficients of
\(\log\mathcal L\) dominated by those of \(\log\zeta\)); bounded
coefficients, through Lemma 4.4; and nothing about zeros except that
\(H_t\) has none with \(\lvert\operatorname{Im}z\rvert\ge1\). The controls of
[summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
fail the second premise: the Euler-factor controls have \(-F'/F\)
coefficient \((1+2\sqrt p/c)\log p>\Lambda(p)\) at their prime, and for
\(c=\tfrac12\), \(p\le13\) vanish to the right of \(\operatorname{Re}s=1\)
(Project 01, Section 5); the weighted-square, reflected and
primitive-compatible theta controls have no Dirichlet series with this
functional equation; Davenport–Heilbronn combinations satisfy the first
and third premises and fail Lemma 4.1. This is not a claim that the
estimate distinguishes theta from its controls in any sense relevant to
RH: (E) is a smoothing statement at height \(p>1\), true for every member of
the class, and its consumer converts it into confinement only with H12 and
the comparison theorem. It is a milestone of the kind the portfolio plan
asks for, judged by the heights and floors of Section 5, not a
reformulation.

## 9. Decisions and next bounded tasks

Recommendations to Edward, and to Codex as the auditor of this phase.

1. **Status of Lemma \(A_p\).** Record it as: proved with an explicit
   remainder (Theorem 4.6); \(\delta=0\) shown by floating evaluation on the
   20-point time grid, for the family at \(q\ge1.1\cdot10^5\) (even) and
   \(4.9\cdot10^4\) (odd) at \(p=\sqrt5\), at every \(x\), and for zeta at
   \(x\ge X\) (and from \(x\approx1.9\cdot10^5\) at \(p=\sqrt5\)); pending
   item 2. Project 01's Target A then rests on H12, the comparison theorem
   and item 2.
2. **Certification** (the next bounded task here). Re-evaluate \(E\) with
   outward rounding, with monotone majorants on intervals of \(\sigma\) and
   interval Riemann sums; cover all \(t\in(0,\tfrac12]\) by monotonicity or
   Lipschitz bounds between grid times; prove the decrease in \(\ell\) piece
   by piece (each Euler-region majorant is monotone in \(\sigma_*\) at fixed
   \(v\); the strip and reflected terms need the exponent argument of
   Section 2.2); and bound the \(O(\tau^3)\) term for \(t<0.001\). Stopping
   rule: if outward rounding moves \(\ell_1(\sqrt5)\) above \(12\), report the
   certified threshold and recompute the conductor thresholds.
3. **Sharpening, only if a consumer needs smaller conductors.** Rademacher's
   convexity bound in place of Lemma 4.4, read from the printed source,
   and the exact second-order term in place of its majorant would lower
   \(\ell_1\). Target A at \(q\ge10^6\) does not need it.
4. **H12 and the comparison theorem** belong to Project 01 (Claude lead).
   This note supplies their exterior input and does not touch them.
5. **Audit request to Codex.** Check Lemma 3.3's contour shift and
   integration by parts, the left-region bound of Proposition 4.5
   (including the reflected exponent and the range of \(\Lambda\)), Lemma
   3.2's zeta domain, Lemma 4.4, the majorant bookkeeping of the check
   programme against the definitions above, and replay the record.
6. **Hakimoglu-Brown's input.** Compare Theorem 4.6 with his Lemma 3 and
   Propositions 7–8, and read his Lemma 2 and Theorem 9 for the zeta finite
   region, once the PDF is available in the session; it could not be
   fetched today (Section 10). Done later the same day in
   [note 02](02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md),
   after Edward added the preprint to the project.

## 10. Coverage, provenance and what was not done

Read in full for this note: the portfolio README, plan, draft history and
setup review; Project 03's proposal and READMEs; Project 01's README,
proposal, note 01 (SHA-256 `8e6ea157…7b4e`), source-document and numerics
READMEs and Section H of its benchmark programme; the twenty files of
[`avoid/`](../../../../avoid/README.md) and the result summaries
[README](../../../../result-summaries/README.md), 08–16 in full and 01–07
in part; 21 Note 58, 22 outer Note 01 and
[Review 20](../../../investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md).
Hakimoglu-Brown's preprint was not available: the arXiv page was refused
by the web proxy (rate limit), and the PDF read in Project 01's session is
not in the repository, so every statement about it here is Project 01's
reading (its ledger H11), and the comparison asked for in item 9.6 is open
here; [note 02](02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md)
carries it out.
Binet's formula for \(\psi\) (DLMF §5.9(ii)) is quoted from memory and was
checked numerically; every other ingredient is proved here or in Project
01's note.

A same-model check was run before filing. A Claude subagent of this
session, with its own mpmath code, confirmed Lemma 3.1 at four points to
\(10^{-30}\) (zeta and an odd complex character modulo 5), the three forms of
Lemma 3.3 to \(4\cdot10^{-31}\), Lemmas 4.1–4.4 in about 23,000 randomized
cases with no violation, the identity in the proof of Proposition 4.5 to
\(4\cdot10^{-42}\) for random entire \(G\) and to \(8\cdot10^{-28}\) for zeta's
\(G\), the programme's \(E\) at five parameter points against its own
implementation (relative differences at most \(4\cdot10^{-5}\), two of them
with the programme's value below its own), the threshold behaviour near
\(\ell_1\), and the planning value \(0.26176\). It also found the following,
now corrected: the status words of the summary and of Sections 5, 7 and 9
were stronger than a grid evaluation supports; Lemma 3.2 misquoted its
contraction constant and its zeta part lacked an invariant domain; the
crude strip bound was allowed where \(Q_*\) is not justified (\(u>\sigma_*\),
numerically harmless, now excluded in the programme); several numbers in
the text disagreed with the record; and Lemma 4.3's bound
\(\beta'\le\tfrac1{12}\) was only sampled. This is not independent review.

Not done: no outward-rounded evaluation; no proof of the monotonicity of
\(E\) in \(\ell_*\) or of the margin between grid times; no bound on the
\(O(\tau^3)\) term below \(t=0.001\); no H12, comparison theorem or
finite-region argument; no use of Rademacher's bound or of any explicit
convexity estimate. The check programme is standard-library Python with
deterministic JSON output. Its record regenerates byte for byte with
Python 3.13.16 on x86_64 Linux; a replay with Python 3.10.12 on aarch64
Linux agrees in records A and E–H and differs in 24 floats of records B–D,
by at most \(4\cdot10^{-11}\) relative apart from three rounding-level
identity differences (numerics README). Nothing was committed to git.
