# Normalization and transfer contract for the Dirichlet Newman family

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is the coordination note for the contract phase of the
[initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md),
written after the [portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md)
and the [portfolio setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md),
whose changes C4–C6, C8 and C12 bear on this project and are answered in
Section 6. Edward supplied Hakimoglu-Brown's preprint arXiv:2610.12803v1
during the session; Sections 3.5 and 4.6 are built on it. This note is not
independent review: the setup review and this note are both Claude models,
and the proposal assigns the audit of this phase to Codex.

Claim status is marked throughout: **proved** (a complete short proof
here, or a classical fact with its source), **proof sketch** (steps named
but not written in full), **conditional** (proved from a named unproved
input), **numerical** (floating point, with a record), **planning**
(arithmetic under a stated hypothesis; not a bound), and **open**. No
de Bruijn–Newman constant of any Dirichlet \(L\)-function is bounded here
except conditionally on a preprint claim (Corollary 3.2).

**Summary.**

1. *Normalization.* The family is fixed in Dobner's normalization, with an
   explicit kernel \(\Phi_\chi\) and the conjugate-pair relation
   \(H_{t,\bar\chi}(z)=\overline{H_{t,\chi}(-\bar z)}\), so that
   \(\Lambda_{\bar\chi}=\Lambda_\chi\) and "both height directions" means
   \(x\ge0\) for \(\chi\) and for \(\bar\chi\) (Section 1). Checked on
   sixteen characters of both parities, real and complex, against an
   independent Hurwitz-zeta evaluation (relative agreement
   \(4\cdot10^{-9}\) or better) and LMFDB zeros (\(3\cdot10^{-13}\)).
2. *Transfer.* Polymath's barrier criterion has a two-sided version for
   every primitive character (Proposition 3.1, proof sketch); for complex
   characters the zero dynamics gains only a real drift. Its time-zero
   hypothesis needs only \(L(s,\chi)\ne0\) for
   \(\operatorname{Re}s\ge\tfrac12+\tfrac12\sqrt{2\lambda}\) below the
   barrier, not GRH.
3. *A sibling result neither the proposal nor the review used.* The
   quasi-RH half-planes claimed in preprints that the repository has
   already audited give, by Dobner's Theorem 3, bounds uniform over all
   primitive characters: \(\Lambda_\chi\le25/72\) from the audited
   \(11/12\) chain, \(9/32\) from the claimed \(7/8\), and
   \(0.28118560\ldots\) from Liu's \(B_{\rm new}\) (Corollary 3.2,
   conditional on those claims).
4. *First bounded test, first mechanism.* Platt's verification gives the
   effective log conductor \(L\in[16.58,17.02]\) at the verified height for
   every \(q\le400{,}000\), confirming the setup review's benchmark. The
   consistent transfer of Polymath's parameter row, which keeps the
   leading-order first-term-dominance budget fixed, scales \(t_0\) **and**
   \(y_0\) and gives the planning value \(\lambda\approx0.30\), not the
   review's \(0.28\)–\(0.29\) with \(y_0\) fixed. That is above the
   conditional baseline \(0.2812\): the preregistered stopping answer
   demotes first-term dominance at existing verification heights.
5. *Correction that reorders the routes.* The analytic conductor of
   \(L(s,\chi)\) does not fall to zero at height zero: the effective log
   conductor there is \(\log(q/215)\) for even and \(\log(q/9.3)\) for odd
   characters. So for conductors above a threshold, an exterior estimate
   proved uniformly down to height zero (open: Lemma A or Lemma \(A_p\))
   covers every zero at once, and neither verification, a barrier nor a
   density estimate is needed. Section 2.3 of the setup review used the
   exterior height \(A/q\) without this floor; its density crux concerns
   only an intermediate range of \(q\).
6. *Second mechanism: the strip comparison.* Hakimoglu-Brown's paired-zero
   inequality \(Q'\le-2-(4Q/p)S+8Q/(p^2-Q)\) for the squared height \(Q\)
   of the highest zero holds verbatim for every primitive character
   (Proposition 3.3, proved), and its input \(S(x,p,t)\) has an exact
   time-zero floor at **every** height,
   \(\tfrac14\bigl(\log\tfrac q\pi+\psi(\tfrac{1+p+2\mathfrak a}4)\bigr)-\tfrac12\bigl(-\tfrac{\zeta'}\zeta\bigr)(\tfrac{1+p}2)\),
   because \(S\) at height \(p\) is half the real part of \(\xi_\chi'/\xi_\chi\)
   at \(\operatorname{Re}s=\tfrac{1+p}2>1\) (Lemma 3.4, proved). If the
   floor persists along the comparison and the nonreal zeros stay
   confined at positive times, the planning values, with no half-plane
   input (only \(|\operatorname{Im}z|<1\) at time zero), are
   \(\Lambda_\chi\le0.38\)–\(0.39\) (odd–even) for every primitive \(\chi\)
   with \(q=10^4\), \(0.31\)–\(0.32\) at \(10^6\), \(0.25\)–\(0.26\) at
   \(10^8\) and \(0.19\) at \(10^{12}\); and \(0.26\) per character at Platt's heights, below the
   conditional baseline (Section 4.6). These are planning numbers, not
   bounds.
7. *Proposed staging.* Target A (every primitive \(\chi\) above an explicit
   conductor; qualitatively \(\Lambda_\chi\to0\)) by the strip comparison
   first, with two open inputs: Lemma \(A_p\), that the time-zero floor of
   \(S\) persists, up to an explicit loss, along the comparison interval,
   uniformly in \(x\) and in \(q\); and H12, that the nonreal zeros are
   confined to a bounded set uniformly on every interval \([t',t_*]\),
   \(t'>0\) (Section 3.5). Target B (small conductors, per character, no
   half-plane input, planning value \(0.26\)) second; Target C
   (intermediate conductors) dormant. First-term
   dominance near the real axis (Lemma A, Section 3.4) is kept as the
   alternative route. A search found no prior upper bound below \(1/2\)
   for any Dirichlet \(L\)-function and no conductor-uniform statement;
   that is a search result, not a priority claim.

## 0. Conventions

\(s=\tfrac12(1+iz)\), \(z=x+iy\). A zero \(\rho=\beta+i\gamma\) of
\(L(s,\chi)\) corresponds to \(z=2\gamma+i(1-2\beta)\), so heights in \(z\)
are twice ordinates and \(|\operatorname{Im}z|=|2\beta-1|\). The heat flow
is \(H_t(z)=\int_{\mathbb R}e^{tu^2}\Phi(u)e^{izu}\,du\), with
\(\partial_tH_t=-\partial_z^2H_t\). This is Dobner's normalization
(arXiv:2005.05142v2, equations (5)–(6)); it agrees with Polymath's and
Hakimoglu-Brown's for zeta up to the constant factor \(8\) (Dobner's
\(\Phi\) for zeta is four times Polymath's, and Polymath integrates the
cosine over the half line), so de Bruijn–Newman constants agree.
Stopple's normalization for quadratic characters (arXiv:1301.3158) uses
\(e^{2u}\) in the kernel and the ordinate as variable, so his \(u\) is twice
ours and his time a quarter of ours; his family lower bound
\(-1.13\cdot10^{-7}\) is \(-4.5\cdot10^{-7}\) here, and both are superseded
by Dobner's Theorem 2. Parity \(\mathfrak a\in\{0,1\}\),
\(\chi(-1)=(-1)^{\mathfrak a}\). \(M(t)=\sup\{(\operatorname{Im}z)^2:H_t(z)=0\}\),
and \(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\), as in arXiv:2610.12803.

## 1. The family and its normalization

Let \(\chi\) be primitive modulo \(q>1\), with Gauss sum
\(\tau(\chi)=\sum_{a\bmod q}\chi(a)e^{2\pi ia/q}\) and root number
\(\varepsilon(\chi)=\tau(\chi)/(i^{\mathfrak a}\sqrt q)\). Put
\[
\xi_\chi(s)=\alpha_\chi\,(q/\pi)^{s/2}\,\Gamma\!\bigl(\tfrac{s+\mathfrak a}2\bigr)L(s,\chi),
\qquad \alpha_\chi^{2}\,\varepsilon(\chi)=1,
\]
\[
\Phi_\chi(u)=4\alpha_\chi\,(\pi/q)^{\mathfrak a/2}\,e^{(1+2\mathfrak a)u}\sum_{n\ge1}\chi(n)\,n^{\mathfrak a}\exp\!\bigl(-\pi n^2e^{4u}/q\bigr),
\qquad
H_{t,\chi}(z)=\int_{\mathbb R}e^{tu^2}\Phi_\chi(u)e^{izu}\,du .
\]

**Lemma 1.1 (proved; classical inputs named).**
(a) \(|\varepsilon(\chi)|=1\), \(\varepsilon(\bar\chi)=\overline{\varepsilon(\chi)}\),
and \(\varepsilon(\chi)=1\) for real \(\chi\).
(b) \(\xi_\chi\) is entire and \(\xi_\chi(s)=\overline{\xi_\chi(1-\bar s)}\);
with \(\gamma(s)=\alpha_\chi(q/\pi)^{s/2}\Gamma(s/2+\mathfrak a/2)\), so
\(m=0\), \(Q=\sqrt{q/\pi}\), \(\omega=\tfrac12\), \(\mu=\mathfrak a/2\),
\(L(\cdot,\chi)\) lies in Dobner's class \(\mathcal S^\sharp\).
(c) \(\xi_\chi(\tfrac12(1+iz))=\int_{\mathbb R}\Phi_\chi(u)e^{izu}du=H_{0,\chi}(z)\),
\(\Phi_\chi(-u)=\overline{\Phi_\chi(u)}\), and \(\Phi_\chi\) decays like
\(\exp(-\pi e^{4|u|}/q)\) in both directions.
(d) \(H_{t,\chi}\) is real on \(\mathbb R\), \(H_{t,\chi}(\bar z)=\overline{H_{t,\chi}(z)}\),
and, choosing \(\alpha_{\bar\chi}=\overline{\alpha_\chi}\),
\(H_{t,\bar\chi}(z)=\overline{H_{t,\chi}(-\bar z)}\). Hence the zeros of
\(H_{t,\bar\chi}\) are the reflections \(-\bar z\) of those of
\(H_{t,\chi}\), and \(\Lambda_{\bar\chi}=\Lambda_\chi\).

*Proof.* (a) and the functional equation
\(\Lambda(s,\chi)=\varepsilon(\chi)\Lambda(1-s,\bar\chi)\) for
\(\Lambda(s,\chi)=(q/\pi)^{(s+\mathfrak a)/2}\Gamma(\tfrac{s+\mathfrak a}2)L(s,\chi)\)
are classical (Davenport, *Multiplicative Number Theory*, Ch. 9, cited
from memory and checked numerically below; LMFDB uses the same
\(\varepsilon\)). Since \(\Lambda(1-s,\bar\chi)=\overline{\Lambda(1-\bar s,\chi)}\),
\(\xi_\chi(s)=c\,\alpha_\chi\varepsilon\,\overline{\Lambda(1-\bar s,\chi)}\)
and \(\overline{\xi_\chi(1-\bar s)}=c\,\overline{\alpha_\chi}\,\overline{\Lambda(1-\bar s,\chi)}\),
\(c=(q/\pi)^{-\mathfrak a/2}\); they agree when
\(\alpha_\chi\varepsilon=\overline{\alpha_\chi}\), that is when
\(\alpha_\chi^2\varepsilon>0\), which \(\alpha^2\varepsilon=1\) satisfies
for either root. This is (b), and Dobner's axioms (i)–(iii) (arXiv v2,
Section 2, equation (4)) are then immediate. For (c), Dobner's equations
(7)–(8) give \(\Phi_F(u)=2\alpha e^u\sum_na_n\psi(ne^{2u}/Q)\) with
\(\psi(v)=\frac1{2\pi i}\int\Psi(w)v^{-w}dw\); here
\(\Psi(w)=\Gamma(\tfrac{w+\mathfrak a}2)\), so \(\psi(v)=2v^{\mathfrak a}e^{-v^2}\),
which is the displayed kernel. The symmetry is the Fourier form of
reality on the line (Dobner, proof of Theorem 1), and the decay at
\(-\infty\) follows from it. (d) follows from (c):
\(\Phi_{\bar\chi}=\overline{\Phi_\chi}\) when \(\alpha_{\bar\chi}=\overline{\alpha_\chi}\),
and \(\overline{\int e^{tu^2}\Phi(u)e^{-i\bar zu}du}=\int e^{tu^2}\overline{\Phi(u)}e^{izu}du\). \(\square\)

| | real \(\chi\), even | real \(\chi\), odd | complex \(\chi\), even | complex \(\chi\), odd |
| --- | --- | --- | --- | --- |
| \(\varepsilon(\chi)\), \(\alpha_\chi\) | \(1\), \(\pm1\) | \(1\), \(\pm1\) | unit, \(\pm\varepsilon^{-1/2}\) | unit, \(\pm\varepsilon^{-1/2}\) |
| \(\Phi_\chi\) | real, even | real, even | \(\Phi(-u)=\overline{\Phi(u)}\), not even | same |
| \(\Phi_\chi(u)\), \(u\to+\infty\) | \(4\alpha e^{u}e^{-\pi e^{4u}/q}\) | \(4\alpha\sqrt{\pi/q}\,e^{3u}e^{-\pi e^{4u}/q}\) | as even | as odd |
| \(H_{t,\chi}\) on \(\mathbb R\) | real, even | real, even | real, not even | real, not even |
| symmetries of the zero set | \(z\mapsto\bar z,\,-z\) | \(z\mapsto\bar z,\,-z\) | \(z\mapsto\bar z\); \(\bar\chi\) has \(-\bar z\) | same |
| heights to be covered | \(x\ge0\) | \(x\ge0\) | \(x\ge0\) for \(\chi\) and \(\bar\chi\) | same |
| Gamma factor near height zero | \(\Gamma(s/2)\), pole at \(s=0\) | \(\Gamma((s+1)/2)\), pole at \(s=-1\) | as even | as odd |

**Numerical check** (numerical;
[record](../numerics/CHECK_CHARACTER_NORMALIZATION_CLAUDE_20261017.json),
[script](../numerics/check_character_normalization_claude_20261017.py)).
Sixteen characters: 3.2, 4.3, 5.2, 5.3, 5.4, 7.2–7.6, both real characters
modulo 8, 11.2, 11.6, 13.4 and 13.10 (Conrey labels where they apply).
\(H_{0,\chi}\) by full-line trapezoid quadrature of the kernel agrees with
\(\xi_\chi((1+iz)/2)\) computed independently from Hurwitz zeta values
(Euler–Maclaurin) and Stirling's series, at nine real and four complex
points with \(|\operatorname{Re}z|\le40\), \(|\operatorname{Im}z|\le0.9\), to
relative \(3.7\cdot10^{-9}\) at worst (cancellation at \(x=40\)); the
kernel symmetry holds to \(8\cdot10^{-13}\) by direct series at negative
\(u\); the Hermitian functional equation to \(3\cdot10^{-14}\);
\(|\varepsilon|=1\) to \(2\cdot10^{-15}\); the computed \(\varepsilon\)
agree with the LMFDB signs of 5.2 (\(0.850+0.525i\)) and 7.2
(\(0.895-0.444i\)) to the three digits shown there. For five independently
constructed conjugate pairs (separate tables, Gauss sums and kernels),
\(H_{t,\bar\chi}(z)=\overline{H_{t,\chi}(-\bar z)}\) holds at \(t=0\) and
\(t=0.2\) to \(10^{-12}\) with branch sign \(+1\), and the real zeros are
mirror images. The real zeros of 3.2, 5.2 (including the negative
ordinate \(-4.1329037052\)), 5.4 and 7.2 (including \(-6.2012300428\))
agree with LMFDB to \(3\cdot10^{-13}\); the first zero of 4.3 is
\(6.020948904698\) (its LMFDB page did not load). These heights lie far
inside verified GRH; they test the normalization, not any zero statement.

## 2. Hypothesis ledger

Each imported statement is quoted from the source text read on 17 October
2026, with its location; the status column says how it was read.

| No. | Statement used | Source and location | Hypotheses as stated | Status | Used in |
| --- | --- | --- | --- | --- | --- |
| H1 | For every \(F\in\mathcal S^\sharp\) there is a real \(\Lambda_F\) such that all zeros of \(\xi^F_t\) lie on the critical line iff \(t\ge\Lambda_F\) | Dobner, arXiv:2005.05142v2, Theorem 1; Acta Arith. 201 (2021) 29–62, doi:10.4064/aa200603-23-7 | \(F\in\mathcal S^\sharp\): Dirichlet series absolutely convergent on \(\operatorname{Re}s>1\); \((s-1)^mF\) entire of finite order; \(\xi^F=\gamma F\), \(\gamma(s)=\alpha s^m(s-1)^mQ^s\prod\Gamma(\omega_is+\mu_i)\), \(\alpha\ne0\), \(Q,\omega_i>0\), \(\operatorname{Re}\mu_i\ge0\), and \(\xi^F(s)=\overline{\xi^F(1-\bar s)}\) (equation (4)) | published; printed arXiv v2 read in the browser (pages 1–9); journal numbering not checked | definition of \(\Lambda_\chi\) |
| H2 | \(\Lambda_F\ge0\) | Dobner, Theorem 2 | as H1 | published | lower end of every range |
| H3 | If \(\varphi(u)=\overline{\varphi(-u)}\), \(\varphi(u)=O(e^{-\lvert u\rvert^b})\) for some \(b>2\), and all zeros of \(G=\int\varphi e^{izu}\) lie in \(\lvert\operatorname{Im}z\rvert\le\Delta\), then all zeros of \(G_t=\int e^{tu^2}\varphi e^{izu}\) lie in \(\lvert\operatorname{Im}z\rvert\le\max(\Delta^2-2t,0)^{1/2}\), \(t>0\) | Dobner, Theorem 3 (de Bruijn [Thm. 13], cf. Pólya [Thm. 1]); Polymath, Theorem 3.2, from a time \(t_0\) | as stated | classical | Corollary 3.2, both mechanisms |
| H4 | Upper-bound criterion: (i) no zeros of \(H_0\) with \(0\le x\le X\), \(\sqrt{y_0^2+2t_0}\le y\le1\); (ii) none of \(H_{t_0}\) with \(x\ge X+\sqrt{1-y_0^2}\), \(y_0\le y\le\sqrt{1-2t_0}\); (iii) none of \(H_t\) with \(X\le x\le X+\sqrt{1-y_0^2}\), \(\sqrt{y_0^2+2(t_0-t)}\le y\le\sqrt{1-2t}\), \(0\le t\le t_0\); then no zero of \(H_{t_0}\) has \(y\ge y_0\) | Polymath, arXiv:1904.12438v2, Proposition 3.3 (Theorem 1.2 is the version with (i) replaced by RH verification for \(\sigma\ge(1+y_0)/2\), \(T\le X/2\)); Res. Math. Sci. 6 (2019), doi:10.1007/s40687-019-0193-1 | zeta: \(H_t\) even, real, \(\Phi>0\) | published; Theorem 1.2 read in the printed PDF; Proposition 3.3 and its proof in the HTML rendering, cross-checked against the paper's remark that 1.2(i) implies 3.3(i) | Proposition 3.1 |
| H5 | GRH for primitive characters of modulus \(q\le400{,}000\) to height \(t_0(q)=\max(10^8/q,\,7.5\cdot10^7/q+200)\) (even \(q\)), \(\max(10^8/q,\,3.75\cdot10^7/q+200)\) (odd \(q\)) | Platt, arXiv:1305.3087 (abstract); Math. Comp., doi:10.1090/mcom/3077 | rigorous interval computation | published | Target B, Section 4.1 |
| H6 | Effective approximation \(H_t/B_t=f_t+O_\le(e_A+e_B+e_{C,0})\) for \(0<t\le\tfrac12\), \(0\le y\le1\), \(x\ge200\), with \(f_t=\sum_{n\le N}b_n^t n^{-s_*}+\gamma\sum_{n\le N}n^yb_n^tn^{-\bar s_*-\kappa}\), \(b_n^t=e^{(t/4)\log^2n}\), \(s_*=\tfrac{1+y-ix}2+\tfrac t2\alpha(\tfrac{1+y-ix}2)\), \(N=\lfloor\sqrt{x/4\pi+t/16}\rfloor\) | Polymath, Theorem 1.3 and Corollary 1.4 | zeta only | published; HTML rendering | template for Lemmas A and \(A_p\) |
| H7 | For \(x\ge e^{C/t}\) every zero of \(H_t\) is real; for all \(X\ge0\), \(N_t(X)=g(X,t)+O(\log(2+X))\) | Polymath, Theorem 1.5(i), (iv) | zeta, constants not evaluated | published | template for H12 |
| H8 | Every Dirichlet \(L\)-function is zero-free in \(\operatorname{Re}s>11/12\) | OpenAI preprint of 5 October 2026, pinned in the [arithmetic-source audit](../../../investigations-2/inactive/arithmetic_source_audit/README.md); Dirichlet norm-lift in that audit's base-change note | classical imports | **claimed**; complete scoped internal LLM audit of the main chain; not refereed | Corollary 3.2 |
| H9 | The same in \(\operatorname{Re}s>7/8\); in \(\operatorname{Re}s>34999/40000\); and in \(\operatorname{Re}s>B_{\rm new}=(1507-2\sqrt{921})/1653\) | OpenAI preprint of 30 September 2026, Theorem 1.1, as restated in Liu, arXiv:2610.12234v1, Theorem 1.1 and Corollary 14.1; Liu, Theorems 15.1 and 21.1 | as stated there | **claimed**; not refereed; Liu read in full from the project copy; Lean scope as recorded in [result summary 10](../../../../result-summaries/10_quasi_rh_audits_and_amplification.md) | Corollary 3.2, conditional rows of Section 4.6 |
| H10 | No upper bound on \(\Lambda_D\) for Dirichlet \(L\)-functions; \(\Lambda_{D_{p_n}}\to0\) only for reductions of cubic curves over function fields | Andrade–Chang–Miller, arXiv:1310.3477 (abstract) | — | published | precedent search |
| H11 | At a highest simple zero \(x+ih\), \(q=h^2\): \(q'\le-2-\frac{4q}pS(x,p,t)+\frac{8q}{p^2-q}\) for \(p^2\ge5q\) (from \(K_h\ge(h/p)K_p\) for \(v\le h\)); stepped comparison Theorems 9 and 12; under \(\operatorname{Re}\rho\le7/8\) for zeta, \(\Lambda\le0.13963\) (Theorem 1), one-step \(0.1797275414\ldots\) (equation (18)) | Hakimoglu-Brown, arXiv:2610.12803v1 (working draft 7 October 2026), Sections 4, 6–7 and Remark 5; uses Polymath's boundary computation (its Lemma 2) | zeta; finite region from Polymath's Section 8.4; approximation band \(3\le\operatorname{Im}z\le6\), \(t\le1/5\) | unrefereed working note, conditional for its zeta bound; read in full (26 pages, PDF supplied by Edward, SHA-256 `960a06dc…d3a`); the comparison inequality re-derived here (Proposition 3.3) | Section 3.5, 4.6 |
| H12 | For a fixed primitive \(\chi\) and every \(t'>0\) there is \(X(t')\) such that, for all \(t\in[t',t_*]\), every nonreal zero of \(H_{t,\chi}\) has \(\lvert x\rvert\le X(t')\) (uniform confinement, which gives the upper semicontinuity of \(M(t)\) that the first-contact argument needs) | the analogue of Polymath, Theorem 1.5(i), which Hakimoglu-Brown uses "uniformly on \(t\in[t_0,1/5]\)" | — | **open** for characters (expected from the large-height part of Lemma A at fixed \(q\)) | Target A |

The precedent search covered Dobner, Stopple, Andrade–Chang–Miller,
Chang–Mehrle–Miller–Reiter–Stahl–Yott (arXiv:1411.2071), Newman–Wu's
survey (arXiv:1901.06596), Ki–Kim–Lee (zeta only, per their abstract and
the survey), Basak–Thorner–Zaharescu (arXiv:2404.16003), Hakimoglu-Brown
(zeta only: "Only the zeta case is used"), and four web searches. It found
no upper bound below \(1/2\) for the de Bruijn–Newman constant of any
Dirichlet \(L\)-function and no statement uniform in the conductor. This
is a search, not a priority audit.

## 3. The transfer contract

### 3.1 The two-sided barrier criterion

**Proposition 3.1 (proof sketch).** Let \(\chi\) be primitive modulo
\(q>1\), \(0<y_0\le1\), \(t_0>0\) with \(y_0^2+2t_0\le1\), and
\(X_-,X_+>0\). Put \(Y(t)=\sqrt{y_0^2+2(t_0-t)}\) and \(w=\sqrt{1-y_0^2}\).
Suppose:

1. (time zero) \(H_{0,\chi}(x+iy)\ne0\) for \(-X_-\le x\le X_+\) and
   \(Y(0)\le y\le1\); equivalently \(L(s,\chi)\ne0\) for
   \(\operatorname{Re}s\ge\sigma^*=\tfrac12+\tfrac12\sqrt{y_0^2+2t_0}\),
   \(-X_-/2\le\operatorname{Im}s\le X_+/2\);
2. (exterior at the final time) \(H_{t_0,\chi}(x+iy)\ne0\) for
   \(x\ge X_++w\) and for \(x\le-X_--w\), when \(y_0\le y\le\sqrt{1-2t_0}\);
3. (two barriers) \(H_{t,\chi}(x+iy)\ne0\) for \(X_+\le x\le X_++w\) and for
   \(-X_--w\le x\le-X_-\), when \(Y(t)\le y\le\sqrt{1-2t}\), \(0\le t\le t_0\).

Then \(H_{t_0,\chi}\) has no zero with \(|y|\ge y_0\), and
\(\Lambda_\chi\le t_0+y_0^2/2\).

*Sketch.* Polymath's proof of their Proposition 3.3 applies with three
changes. First, the region is \([-X_-,X_+]\times[Y(t),\infty)\) with a
barrier on each side instead of \([0,X]\) with evenness, so the side
\(x=0\), which they exclude using \(\Phi>0\) on the imaginary axis, is no
longer a boundary; that positivity, false in general for characters (a
real zero of \(L(s,\chi)\) in \((\tfrac12,1)\) is a zero on the imaginary
axis), is not used. Second, the Hadamard factorization of a non-even
\(H_{t,\chi}\) of order one carries a factor \(e^{a+bz}\), and at a simple
zero
\[
\dot z_j=\frac{H''_t}{H'_t}(z_j)=2\Bigl(b_t+\sum_k\frac1{z_k}\Bigr)+2\sum_{k\ne j}\frac1{z_j-z_k},
\]
with each \(z_k\) paired with \(\bar z_k\). Reality on the line makes
\(b_t\) real and the paired sum \(\sum_k1/z_k\) real, so the extra drift is
horizontal and \(\operatorname{Im}\dot z_j\) is given by Polymath's
formula, whose paired terms are \(O(|x_k|^{-2})\). Third, their step 7
comparison \(y_k^2\le(x-x_k)^2+Y^2\) for any zero with \(y_k>Y\) uses only
\(|x-x_k|\ge\sqrt{1-Y^2}\), which the two barriers give for every
\(x\in[-X_-,X_+]\), and \(y_k<1\) (H3 from \(|\operatorname{Im}z|<1\) at
time zero). The repeated-zero case uses the Hermite-root expansion, which
does not need evenness. The conclusion is H3 from time \(t_0\). \(\square\)

A written proof must check the Hadamard form and convergence for every
\(t\in[0,t_0]\), and the minimal-failing-time argument when zeros may cross
\(x=0\), which evenness excluded in the original. The time-zero hypothesis
depends on \((t_0,y_0)\) only through \(\lambda=t_0+y_0^2/2\), since
\(y_0^2+2t_0=2\lambda\): any certificate of \(\Lambda_\chi\le\lambda\) of
this shape needs \(L(s,\chi)\ne0\) for \(\operatorname{Re}s\ge\tfrac12+\tfrac12\sqrt{2\lambda}\)
below its barrier: \(0.875\) for \(\lambda=9/32\), \(0.854\) for
\(\lambda=1/4\), \(0.832\) for \(\lambda=0.22\)
([benchmark record](../numerics/BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json), section D).

### 3.2 The conditional uniform bound

**Corollary 3.2 (proved, conditional on the half-plane).** If no Dirichlet
\(L\)-function vanishes in \(\operatorname{Re}s>B\), \(\tfrac12\le B<1\),
then \(\Lambda_\chi\le(2B-1)^2/2\) for every primitive \(\chi\).

*Proof.* The zeros of \(\xi_\chi\) are \(\rho\) and \(1-\bar\rho\) together,
so \(1-B\le\beta\le B\) and \(|\operatorname{Im}z|=|2\beta-1|\le2B-1\). H3
applies to \(\varphi=\Phi_\chi\) by Lemma 1.1(c). \(\square\)

With \(B=1\) this is the unconditional \(\Lambda_\chi\le\tfrac12\). The
claimed half-planes give:

| Half-plane \(B\) | Status | Bound on every \(\Lambda_\chi\) |
| --- | --- | --- |
| \(11/12\) | claimed; main chain internally audited | \(25/72=0.347222\) |
| \(7/8\) | claimed (30 September preprint) | \(9/32=0.28125\) |
| \(34999/40000\) | claimed (Liu, Theorem 15.1) | \(224970001/800000000=0.2812125\) |
| \(B_{\rm new}=(1507-2\sqrt{921})/1653\) | claimed (Liu, Theorem 21.1) | \((1867057-10888\sqrt{921})/5464818=0.2811856084\ldots\) |

The zeta case of this deduction is the
[prime-variance bridge note](../../../quasi-rh/prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md);
for zeta it is weaker than the published \(0.2\), for the Dirichlet family
it is the best bound below \(\tfrac12\) known to this search, and it is
uniform in \(q\). Every unconditional result below is read against
\(0.2812\) as well as against \(\tfrac12\).

### 3.3 Routes and what each needs

| Route | Characters covered | Time-zero input | Finite region | Exterior input | Density | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Strip (Corollary 3.2) | all | a uniform half-plane | none | none | none | conditional on H8/H9 |
| **A**, large conductor, strip comparison | all with \(q\ge q_0\) | \(M(0)\le1\) (free) | none | Lemma \(A_p\) at **every** height; positivity of \(g\); H12 | none | open |
| A, alternative: first-term dominance | all with \(q\ge q_0\) | none | none | Lemma A at every height | none | open |
| **B**, finite set | one \(\chi\) at a time, small \(q\) | GRH to height \(X/2\) (H5) | barrier over the comparison interval | Lemma \(A_p\) (or A) above \(X\) | none | open; per-character computation |
| **C**, intermediate \(q\) | all but an exceptional set modulo \(q\) | zero-free in \(\operatorname{Re}s\ge\sigma^*(\lambda)\) below \(T_*(q)\) | per character, or a replacement | as B | explicit family density at \(\sigma^*(\lambda)\) | dormant |

The proposal's inclusion
\(\{\Lambda_\chi>\lambda\}\subseteq\{Z_\chi(\sigma_*,T_*)\ge1\}\cup E_{\rm barrier}\cup E_{\rm approximation}\)
is Proposition 3.1 read contrapositively with \(\sigma_*=\sigma^*(\lambda)\),
\(T_*=X/2\) and \(E_{\rm approximation}=\varnothing\) once the exterior input
holds above \(T_*\); the localization the proposal says must not be
assumed is exactly what the barriers supply. Route C therefore still
needs a barrier for every non-exceptional character, which is the setup
review's first crux.

### 3.4 First-term dominance near the axis (the alternative route)

**Lemma A (open).** Explicit \(N(q,x,t)\), \(B_{t,\chi}\), \(\gamma_\chi\),
\(\kappa_\chi\) and an explicit error \(e(q,\mathfrak a,x,y,t)\) such that,
for every primitive \(\chi\) modulo \(q\), \(0<t\le\tfrac12\), \(0\le y\le1\)
and every real \(x\ge0\),
\[
\frac{H_{t,\chi}(x+iy)}{B_{t,\chi}(x+iy)}
=\sum_{n\le N}\frac{\chi(n)\,b^t_n}{n^{s_*}}
+\gamma_\chi\sum_{n\le N}\frac{\overline{\chi(n)}\,n^y\,b_n^t}{n^{\bar s_*+\kappa_\chi}}
+O_\le(e),
\]
with \(s_*=\tfrac{1+y-ix}2+\tfrac t2\alpha_\chi(\tfrac{1+y-ix}2)\),
\(\alpha_\chi(s)=\tfrac12\log\tfrac q\pi+\tfrac12\psi(\tfrac{s+\mathfrak a}2)\),
and \(e\to0\) as \(q\to\infty\) uniformly in \(x\ge0\). With a dominance
lemma at the effective log conductor
\(L_{\rm eff}=2\operatorname{Re}\alpha_\chi(\tfrac{1+y-ix}2)\), which is
smallest at \(x=0\) because \(\operatorname{Re}\psi(\sigma+i\tau)\) increases
with \(|\tau|\), it gives \(\Lambda_\chi\le t_0+y_0^2/2\) for
\(q\ge q_0(t_0,y_0,\mathfrak a)\) by H3 from time \(t_0\), both height
directions coming from \(\chi\) and \(\bar\chi\). The new work against
Polymath's Theorem 1.3: the approximation is needed down to \(x=0\),
where \(|s|\approx\tfrac12\) and, for even characters, the pole of
\(\Gamma(s/2)\) at \(s=0\) lies within two widths of the Gaussian average
that produces \(M_t=e^{(t/4)\alpha^2}M_0\) (\(\psi'(0.3)\approx12.2\) against
\(\psi'(0.8)\approx2.30\) for odd characters); the Riemann–Siegel-type
correction carries the Gauss sum and must be explicit in \(q\) and \(x\)
jointly; and the dominance lemma must be uniform in the sum length
\(N\approx\sqrt{q(x+1)/4\pi}\). Section 3.5 avoids the first two.

### 3.5 The strip comparison for the family

Hakimoglu-Brown (H11) compares the squared height of the highest zero with
an ordinary differential inequality whose coefficient is
\(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\), evaluated at a reference
height \(p\) above all zeros. For zeta, \(S\) is controlled only beyond
Polymath's verified region, so the comparison stops at squared height
\(1/25\), where Polymath's barrier keeps the remaining zeros. For the
family the same comparison needs no finite region once \(q\) is large.

**Proposition 3.3 (proved).** Let \(H\) be an entire function of order
one, real on \(\mathbb R\), with \(H(\bar z)=\overline{H(z)}\), let \(H_t\)
solve \(\partial_tH_t=-\partial_z^2H_t\), and suppose that at time \(t\)
the highest zero \(x+ih\), \(q=h^2>0\), is simple and \(p^2\ge5q\). Then
\[
q'(t)\le-2-\frac{4q}p\,S(x,p,t)+\frac{8q}{p^2-q}.
\]
In particular this holds for \(H_{t,\chi}\), every primitive \(\chi\).

*Proof.* As in Proposition 3.1, \(\operatorname{Im}\dot z\) at
\(z_1=x+ih\) is \(2\operatorname{Im}\sum_{k\ne1}(z_1-z_k)^{-1}\); the real
drift of a non-even \(H\) does not enter, and the same holds for \(S\),
since \(-\operatorname{Im}\) of a real constant vanishes. With zeros in
conjugate pairs \(x_k\pm iv_k\) (real zeros at half weight) and
\(K_h(d,v)=\frac{h-v}{d^2+(h-v)^2}+\frac{h+v}{d^2+(h+v)^2}\), this gives
\(h'=-1/h-2\sum'K_h(d_k,v_k)\) and
\(S=\sum K_p(d_k,v_k)\), the second sum including \(K_p(0,h)=2p/(p^2-q)\).
Put \(D=d^2\), \(A=h^2\), \(B=p^2\), \(r=v^2\le A\), \(v_0=D+A-r\),
\(w=D+B-r\). Then \(K_h=2hv_0/(v_0^2+4Dr)\), \(K_p=2pw/(w^2+4Dr)\), and
\[
\frac{K_h}h-\frac{K_p}p=\frac{2(w-v_0)(v_0w-4Dr)}{(v_0^2+4Dr)(w^2+4Dr)},\qquad
v_0w-4Dr=D^2+(A+B-6r)D+(A-r)(B-r),
\]
which is nonnegative when \(B\ge5A\), since then \(A+B-6r\ge B-5A\ge0\).
Hence \(\sum'K_h\ge\frac hp\bigl(S-\frac{2p}{p^2-q}\bigr)\), and
\(q'=2hh'=-2-4h\sum'K_h\) gives the claim. The paired sums converge
absolutely, their terms being \(O(d_k^{-2})\). \(\square\)

**Lemma 3.4 (proved; the exact time-zero floor).** For every primitive
\(\chi\) modulo \(q\), every \(p>1\) and every real \(x\),
\[
S(x,p,0)=\tfrac12\operatorname{Re}\frac{\xi_\chi'}{\xi_\chi}\Bigl(\frac{1+p+ix}2\Bigr)
\;\ge\;C_{q,\mathfrak a}(p):=\tfrac14\Bigl(\log\tfrac q\pi+\psi\bigl(\tfrac{1+p+2\mathfrak a}4\bigr)\Bigr)-\tfrac12\Bigl(-\tfrac{\zeta'}\zeta\Bigr)\bigl(\tfrac{1+p}2\bigr).
\]

*Proof.* \(H_{0,\chi}'(z)=\tfrac i2\xi_\chi'(\tfrac{1+iz}2)\), so
\(S(x,p,0)=-\tfrac12\operatorname{Re}(\xi_\chi'/\xi_\chi)(\tfrac{1-p+ix}2)\);
the Hermitian functional equation gives
\((\xi'/\xi)(s)=-\overline{(\xi'/\xi)(1-\bar s)}\), which is the equality.
Then \(\xi'_\chi/\xi_\chi=\tfrac12\log\tfrac q\pi+\tfrac12\psi(\tfrac{s+\mathfrak a}2)+L'/L(s,\chi)\);
\(\operatorname{Re}\psi(\sigma+i\tau)\ge\psi(\sigma)\) because each term
\(\operatorname{Re}(n+\sigma+i\tau)^{-1}\) of the series for \(\psi\) decreases
in \(|\tau|\); and \(|L'/L(s,\chi)|\le\sum\Lambda(n)n^{-\sigma}=-\zeta'/\zeta(\sigma)\)
for \(\sigma>1\) by the Euler product. \(\square\)

For zeta the same identity gives Hakimoglu-Brown's normalizer term
\(\tfrac12\operatorname{Re}\alpha(w)\); for the family the floor is
uniform in \(x\), so the comparison may run at every height at once.

**Target A by the strip comparison (open).** Suppose, for some \(p\) with
\(p^2\ge5a\), \(a\in\{1,9/16\}\), and some \(\delta\ge0\):

- (Lemma \(A_p\), open) \(S(x,p,t)\ge C_{q,\mathfrak a}(p)-\delta\) for every
  real \(x\) and \(0\le t\le t_*\);
- (positivity) \(g(Q)=2+\tfrac{4(C_{q,\mathfrak a}(p)-\delta)}pQ-\tfrac{8Q}{p^2-Q}>0\)
  on \((0,a]\), the analogue of \(k_i>0\) in Hakimoglu-Brown's Theorem 9
  (at \(a=1\), \(p=\sqrt5\) it is \(C-\delta>0\); with \(\delta=0\) the
  floor \(C_{q,\mathfrak a}(\sqrt5)\) is positive only above conductor about
  \(36\) for odd and \(79\) for even characters; it holds at every optimum
  tabulated in Section 4.6);
- (H12, open) uniform confinement of the nonreal zeros on every
  \([t',t_*]\), \(t'>0\).

Then, comparing with \(Q'=-g(Q)\), \(Q(0)=a\), as in Hakimoglu-Brown's
Theorem 9 but with no finite region, \(M(t_*)\le b\) for every \(b>0\)
reached by \(t_*\), and \(\Lambda_\chi\le t_*+b/2\); since \(g(0)=2\) the
limit \(b\to0\) is harmless, and \(p^2\ge5Q\) persists because \(Q\)
decreases. With \(a=1\) no half-plane or other time-zero zero-location
input is used beyond \(|\operatorname{Im}z|<1\); H12 is a qualitative
statement at positive times. \(a=9/16\) is the claimed \(7/8\) half-plane.
The proof structure (strict barrier perturbation, backward Hermite
splitting at multiple contacts, \(M(t)\le a-2t\) on the initial phase,
first contact) is that of Hakimoglu-Brown's Theorem 9, with H12 replacing
his use of Polymath's Theorem 1.5(i).

Lemma \(A_p\) is the input to prove. It is easier than Lemma A in the ways
that matter here: at height \(p\ge\sqrt{5a}\) the Dirichlet series is in
its region of absolute convergence (\(\operatorname{Re}s_B\ge\tfrac{1+p}2+\tfrac t4L_{\rm eff}\),
and \(\tfrac{1+p}2\ge1.34\)),
the Gamma factor is evaluated at real part at least \(\tfrac{1+p}4\)
(\(\ge0.81\) when \(a=1\), \(\ge0.67\) when \(a=9/16\)), away from its
poles even for even characters, the reflected sum carries
\(|\gamma_\chi|\approx e^{-pL_{\rm eff}/2}\), and at \(t=0\) the bound is
exact with \(\delta=0\). What it must supply is the persistence of the
floor along \(0\le t\le t_*\): the heat-weight perturbation of the Euler
product (Hakimoglu-Brown's Proposition 8 is the zeta model) and the
normalizer's time term \(\tfrac t4\operatorname{Re}(\alpha_\chi\alpha_\chi')\),
which is positive at \(x=0\) for large \(q\).

## 4. The first bounded test

The setup review asked for its Section 2 computations before the
normalization table (change C6). The stopping answer was fixed before the
computation: if the consistent transfer of a published zeta row gives a
planning value above the conditional baseline \(0.2812\) at every modulus
Platt covers, the per-character route at existing verification heights is
not a route to a better number and is demoted. All numbers are in the
[benchmark record](../numerics/BENCHMARK_FAMILY_CONTRACT_CLAUDE_20261017.json)
([script](../numerics/benchmark_family_contract_claude_20261017.py)); except
for Section 4.1 they are planning arithmetic.

### 4.1 Platt's budget in the analytic conductor (numerical)

Over all \(q\le400{,}000\) with primitive characters, the verified height
\(t_0(q)\) of H5 gives \(q\,t_0(q)\in[1.000\cdot10^8,\,1.550\cdot10^8]\) and
\(L=\log(q\,t_0/2\pi)\in[16.583,\,17.021]\) (even \(q\); odd \(q\) stop at
\(16.744\)). The exact form
\(\log(q/\pi)+\operatorname{Re}\psi(\tfrac{1/2+\mathfrak a+it_0}2)\) differs by
less than \(10^{-6}\). This confirms Section 2.1 of the setup review (its
upper end \(17.1\) is \(17.02\)): the budget is fixed in the analytic
conductor, and every modulus gets the same \(L\).

### 4.2 First mechanism: transferring a zeta row (planning)

The scaling hypothesis: in first-term dominance the parameters enter at
leading order through \(tL\) (the exponent shift \(tL/4\) of both sums of
H6) and \(yL\) (the ratio \(|\gamma|\approx e^{-yL/2}\)), so a row
\((t_0,y_0,L)\) maps to \((t_0L/L',\,y_0L/L',\,L')\). The unmollified
leading-order components (the tail \(\sum_{n\ge2}b_n^tn^{-(1+y)/2-tL/4}\)
and the \(B\)-part \(|\gamma|(1+\sum_{n\ge2}b_n^tn^{-(1-y)/2-tL/4})\)) test
whether a transfer keeps the budget; they are not the published criteria,
which use mollifiers.

| Row | \(L\) | \(tL\), \(yL\) | At \(L'=16.58\) | At \(L'=17.02\) | Tail, \(B\)-part: at the row; scaled to 16.58; \(y_0\) fixed at 16.58 |
| --- | --- | --- | --- | --- | --- |
| Polymath, \(\Lambda\le0.22\) | 22.287 | 4.457, 4.457 | \(t=y=0.2688\), \(\lambda=0.3050\) | \(t=y=0.2619\), \(\lambda=0.2962\) | 1.84, 0.68; 1.74, 0.69; 1.96, 1.05 |
| Platt–Trudgian, \(\Lambda\le0.2\) | 26.709 | 4.968, 4.469 | \(t=0.2996\), \(y=0.2696\), \(\lambda=0.3360\) | \(t=0.2919\), \(y=0.2626\), \(\lambda=0.3264\) | 1.28, 0.42; 1.32, 0.50; 1.54, 0.97 |

The scaled transfer of Polymath's row keeps both components at their
calibration values, so \(\lambda\approx0.30\) is the consistent value;
Platt–Trudgian's row, whose components grow under the transfer but stay
below Polymath's, gives the conservative \(0.33\). Holding \(y_0\) fixed
while scaling \(t_0\), as the setup review did, raises \(|\gamma|\) from
\(0.11\) to \(0.19\) and the \(B\)-part from \(0.68\) to \(1.05\); that
variant does not preserve the budget, and its \(0.28\)–\(0.29\) should not
be quoted. Reaching \(9/32\), \(1/4\) or \(0.22\) this way per character
needs verified heights about \(3.5\), \(26\) or \(300\) times Platt's
(record section F).

### 4.3 Against the baselines

By first-term dominance at Platt's budget the per-character value is
about \(0.30\): below \(\tfrac12\) and \(25/72\), above \(0.2812\). The
stopping answer applies to that mechanism. The strip comparison, which
entered from the preprint Edward supplied after the stopping answer was
written, gives \(0.26\) at the same budget (Section 4.6): below the
baseline, at the planning level. Target B is therefore kept, with the
strip comparison as its mechanism. Its work is explicit (record section
G): conductors up to \(100\) carry \(1{,}815\) primitive characters and
\(938\) distinct values of \(\Lambda_\chi\) after pairing conjugates; up to
\(1000\), \(184{,}829\) and \(92{,}718\). Each needs its own barrier at
height about \(10^8/q\), now over the longer comparison interval.

### 4.4 The analytic conductor at height zero (correction to the setup review)

Section 2.3 of the setup review placed the exterior height of conductor
\(q\) at \(T_*\approx A/q\), with \(A\) the zeta exterior's analytic
conductor, and concluded that the almost-all theorem needs an explicit
family density estimate at analytic conductor \(A\), with logarithmic
losses exceeding the family size "for every modulus anyone would compute
with". The exterior estimates depend on
\(L_{\rm eff}(q,\mathfrak a,x)=\log(q/\pi)+\operatorname{Re}\psi(\tfrac{1+y-ix}4+\tfrac{\mathfrak a}2)\)
near the axis, and on \(C_{q,\mathfrak a}(p)\) at height \(p\). These behave
like \(\log(qx/4\pi)\) and \(\tfrac14\log(qx/4\pi)\) only for large \(x\),
and are bounded below by their values at \(x=0\): \(L_{\rm eff}\) there is
\(\log(q/215)\) (even) or \(\log(q/9.3)\) (odd) at \(y=0\), and
\(\log(q/104)\) or \(\log(q/8.3)\) at \(y=0.2\). Once \(q\) is large
enough for that floor to exceed the threshold, an exterior estimate
proved down to height zero (Lemma A or \(A_p\), both open) covers every
height, \(T_*(q)=0\), and the density step is empty. The review's crux is real for the intermediate range
between Platt's moduli and the large-conductor threshold (Route C) and
does not concern Route A.

### 4.5 First mechanism: planning values for Target A

With the scaled Polymath row, \(\lambda(L)=c_1/L+c_2^2/(2L^2)\),
\(c_1=c_2=4.457\); \(L^*(\lambda)\) solves \(\lambda(L^*)=\lambda\) and
\(q_0=\pi\exp(L^*-\psi(\tfrac{1+y+2\mathfrak a}4))\) with \(y=c_2/L^*\).

| \(\lambda\) | \(L^*\) | \(q_0\), odd \(\chi\) | \(q_0\), even \(\chi\) |
| --- | --- | --- | --- |
| 0.40 | 13.05 | \(3.5\cdot10^6\) | \(3.3\cdot10^7\) |
| 0.3046 | 16.60 | \(1.3\cdot10^8\) | \(1.4\cdot10^9\) |
| \(9/32\) | 17.83 | \(4.4\cdot10^8\) | \(5.0\cdot10^9\) |
| 0.25 | 19.83 | \(3.3\cdot10^9\) | \(4.0\cdot10^{10}\) |
| 0.22 | 22.29 | \(3.9\cdot10^{10}\) | \(5.0\cdot10^{11}\) |

These assume Lemma A with negligible error and the Stirling form of
\(|\gamma_\chi|\) at height zero, which for even characters is about
\(10\%\) optimistic at \(y=0.2\). Section 4.6 does better at every \(q\).

### 4.6 Second mechanism: the strip comparison (planning)

The planning hypothesis is Lemma \(A_p\) with \(\delta=0\): the exact
time-zero floor \(C_{q,\mathfrak a}(p)\) of Lemma 3.4 is held over the
comparison interval. The comparison ODE is integrated exactly, from
\(Q=a\) to \(Q=b\), and \(p\ge\sqrt{5a}\) is optimized. The calibration:
with Hakimoglu-Brown's constants \(C=21/4\), \(p=4\), \(a=9/16\),
\(b=1/25\), the script's one-step formula returns \(0.179727541426\), his
equation (18); the exact ODE with the same constants gives \(0.17963\).

Large conductor, every height, \(b\to0\) (no finite region):

| \(q\) | odd \(\chi\), \(a=1\) | even \(\chi\), \(a=1\) | odd, \(a=9/16\) | even, \(a=9/16\) |
| --- | --- | --- | --- | --- |
| \(10^3\) | 0.416 | 0.423 | 0.252 | 0.255 |
| \(10^4\) | 0.377 | 0.385 | 0.236 | 0.240 |
| \(10^5\) | 0.340 | 0.349 | 0.220 | 0.224 |
| \(10^6\) | 0.307 | 0.316 | 0.204 | 0.208 |
| \(10^8\) | 0.254 | 0.262 | 0.176 | 0.181 |
| \(10^{10}\) | 0.216 | 0.222 | 0.154 | 0.158 |
| \(10^{12}\) | 0.190 | 0.194 | 0.136 | 0.139 |

Finite region, as in Hakimoglu-Brown's Lemma 2, stopping at
\(b=1/25\), with \(S\) floored at large height by \(L/4-\tfrac12(-\zeta'/\zeta)(\tfrac{1+p}2)\):

| \(L\) | Meaning | \(a=1\) | \(a=9/16\) |
| --- | --- | --- | --- |
| 16.58 | Platt's budget, every \(q\le400{,}000\) | 0.261 | 0.180 |
| 17.02 | its upper end | 0.256 | 0.178 |
| 22.29 | zeta at Polymath's \(X\) | 0.214 | 0.153 |
| 26.71 | zeta at Platt–Trudgian's \(X\) | 0.189 | 0.136 |

Three readings, all conditional on Lemma \(A_p\) with \(\delta=0\) and on
H12. First, the \(a=1\) large-conductor columns, which use no half-plane
input, fall below \(\tfrac12\) already at \(q=10^3\) and below the conditional baseline
\(0.2812\) between \(10^6\) and \(10^8\), and they tend to zero like
\((p\log L)/L\); this is the shape of Target A, with no computation per
character. Second, at Platt's budget the per-character value is \(0.26\),
below the baseline. Third, the zeta rows are a check on the model, not a
claim about zeta: at Polymath's height the model's conditional \(0.153\)
lies between Hakimoglu-Brown's certified \(0.164\) (Euler steps) and
\(0.1396\) (derivative kernel), and the model's \(a=1\) value \(0.189\) at
Platt–Trudgian's height is a planning number that would concern Projects
02–03 (a barrier over the longer interval and \(S\) at \(p\approx2.24\),
below his band \(3\le\operatorname{Im}z\le6\), would both be needed). He
writes that his formula "may not be extrapolated to \(\sigma=1\)", and the
table does not do that: it assumes Lemma \(A_p\) at heights and times his
paper does not cover.

## 5. Premises and controls

Target A by the strip comparison uses: a Hermitian degree-one functional
equation with gamma factor \((q/\pi)^{s/2}\Gamma(\tfrac{s+\mathfrak a}2)\);
the Euler product, only through \(|L'/L(s,\chi)|\le-\zeta'/\zeta(\sigma)\) at
\(\sigma=\tfrac{1+p}2>1\) (Lemma 3.4) and its heat perturbation (Lemma
\(A_p\)); a large conductor; and nothing about zeros except
\(|\operatorname{Im}z|<1\). First-term dominance (Lemma A) uses \(|a_n|\le1\)
in place of the Euler product. The controls of
[summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
fail these premises. The Euler-factor controls \(\Phi_{c,p}\) have
Dirichlet series \(\zeta(s)(1+(2\sqrt p/c)p^{-s}+p^{1-2s})\): the
coefficient of \(p^{-s}\) in their \(-F'/F\) is \((1+2\sqrt p/c)\log p\),
so the bound by \(-\zeta'/\zeta\) of Lemma 3.4 fails, and for
\(c=\tfrac12\), \(p\le13\) the factor even vanishes to the right of
\(\operatorname{Re}s=1\) (its zeros have
\(\operatorname{Re}s=\tfrac12+\log(1/c+\sqrt{1/c^2-1})/\log p\)); their
coefficients reach \(2\sqrt p/c\), their conductor is \(p^2\le2209\), and
their collisions lie below height \(9.1\), where the floor is small; they
are also not primitive Dirichlet \(L\)-functions. The weighted-square, reflected and
primitive-compatible theta controls have no Dirichlet series with a
degree-one functional equation of large conductor. None meets every
premise, so none tests Target A.

Davenport–Heilbronn-type combinations of \(L(s,\chi)\) and
\(L(s,\bar\chi)\) with a self-dual functional equation of conductor \(q\)
meet every premise of Lemma A (bounded coefficients; at most \(1\) for the
classical example modulo 5) but not Lemma 3.4: without an Euler product nothing
bounds \(f'/f\) by \(-\zeta'/\zeta\), and such functions can vanish to the
right of \(\operatorname{Re}s=1\), where \(f'/f\) is unbounded. So the strip
comparison distinguishes them where first-term dominance does not, and
Target A by first-term dominance would assert \(\Lambda_f=O(1/\log q)\) for
them too. Either way Target A is a smoothing
statement in the conductor aspect, the analogue of Ki–Kim–Lee and of
Polymath's Theorem 1.5(i), not evidence for GRH. A real zero of
\(L(s,\chi)\) near \(s=1\) is a pair at \(z\approx\pm i\); Target A says it
is pulled to the real axis within the stated time, as every other zero is.

## 6. Decisions and proposed amendments

Recommendations to Edward and to Codex as the auditor of this phase; the
proposal and the plan are not edited here.

1. **Staging (answers C4).** Replace the almost-all exponent as the
   headline, as C4 proposes, but stage the targets as A (every primitive
   character of conductor at least an explicit \(q_0\), by the strip
   comparison), then B (a finite set of small conductors, per character,
   by the strip comparison with Platt's data and no half-plane input;
   planning value \(0.26\)),
   with C dormant and first-term dominance kept as A's alternative.
2. **Baseline.** Record Corollary 3.2 in the proposal as the conditional
   baseline, with the status of H8 and H9 stated each time it is quoted.
3. **Lemma \(A_p\) and Project 03 (answers C5).** C5 is right that one
   conductor-parametrized remainder analysis is needed. The analysis this
   project needs first is at a fixed height \(p\in[\sqrt{5a},5]\) for every
   \(x\) (the optima of Section 4.6 fall from \(p\approx4.4\)–\(5\) at \(q=10^3\) to
   \(\sqrt{5a}\) or just above it at \(q=10^{12}\)), not near
   the axis; it shares Hakimoglu-Brown's Lemma 3 and
   Propositions 7–8 as templates with \(q\) as a parameter, and \(q=1\),
   \(x\ge X\) is the zeta case. One owner should write it; which model is
   for Edward and Codex. This project states the consumer contract: the
   loss \(\delta\) of Lemma \(A_p\) against the margins of Section 4.6.
4. **Project 06 (answers C8 here).** Neither mechanism of Target A needs a
   zero count; the counts belong to Route C, which is dormant.
5. **Sources (C12).** Dobner is cited with the journal data and the arXiv
   v2 theorem numbers; Platt with the formula of his abstract; Polymath's
   Theorem 1.2 from the printed text and Proposition 3.3 from the HTML
   rendering, which a review should compare with the printed page;
   Hakimoglu-Brown from the full PDF.
6. **Stopping rules for Target A.** Stop, and record the failed input, if
   Lemma \(A_p\) cannot be proved with \(\delta\le C_{q,\mathfrak a}(p)/4\) on
   the comparison interval for any \(q\le10^{12}\), or if H12 cannot be
   proved for characters. If the loss is acceptable only for one parity,
   that subfamily is a complete result on its own.
7. **Next bounded task.** Write Lemma \(A_p\): the heat-flowed
   approximation of \(H_{t,\chi}\) at height \(p\), for all real \(x\),
   \(0\le t\le\tfrac12\) and \(q\ge q_0\), with \(q\) explicit, modelled on
   Hakimoglu-Brown's Lemma 3 and Propositions 7–8; then H12; then one
   certified comparison table for one conductor range, as his Section 8
   does for zeta. No conductor sweep, barrier computation or density
   estimate before that.

## 7. Coverage, provenance and what was not done

Read in full for this note: the portfolio README and plan, the portfolio
setup review, this project's proposal and READMEs, the twenty files of
[`avoid/`](../../../../avoid/README.md) and the sixteen of
[`result-summaries/`](../../../../result-summaries/README.md), the
brainstorm reply's Section 8, the
[quasi-RH Newman bridge note](../../../quasi-rh/prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md),
the arithmetic-source audit's README and its base-change note (Sections
4–6), Liu's preprint (project copy), and Hakimoglu-Brown's preprint (26
pages, supplied by Edward during the session). Dobner's arXiv v2 was read
in the printed PDF for equations (4)–(8) and Theorems 1–3; Polymath's
Theorem 1.2 in the printed PDF and its Section 3 in the HTML rendering;
Platt's, Andrade–Chang–Miller's and Stopple's statements from their
abstracts or HTML renderings; LMFDB pages for 3.2, 5.2, 5.4 and 7.2 (the
page for 4.3 did not load). The Davenport reference in Lemma 1.1 is from
memory and is covered by the numerical check rather than a reading.
Gordon's and Gomila's preprints, cited by Hakimoglu-Brown, were not read.

A same-model check was run before filing: a Claude subagent of this
session, with its own code (mpmath 1.4.1, 40-digit quadrature), confirmed
the kernel formula and conjugate relation (Lemma 1.1, to about
\(10^{-41}\) for character 5.2), the kernel identity of Proposition 3.3
(199,999 exact rational cases, sharp at \(B<5A\)) and the inequality for
\(q'\) on synthetic zero sets, the identity and sign of Lemma 3.4 at
\(p=3\), the strip constants of Corollary 3.2, and every planning number
in Sections 4.1–4.6. It found three things, now corrected: the
Platt–Trudgian components at the row had been computed with a capped sum
length; H12 had been stated as attainment at each time, weaker than the
uniform confinement the first-contact argument uses; and the positivity
of \(g\) was missing from Target A. It also asked for the status words
"unconditional" in Section 4.6 to be qualified, which they now are. This
is not independent review.

Not done: no written proof of Proposition 3.1 beyond the sketch; no part
of Lemma A, Lemma \(A_p\) or H12; no mollified dominance computation; no
barrier or exterior computation for any character. The two check
programmes are standard-library Python with deterministic JSON output;
they are floating-point diagnostics and planning arithmetic, not
certificates. Nothing was committed.
