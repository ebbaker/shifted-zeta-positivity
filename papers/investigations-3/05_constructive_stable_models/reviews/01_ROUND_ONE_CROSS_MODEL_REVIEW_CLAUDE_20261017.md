# Round-one cross-model review of constructive stable models

17 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier
`claude-opus-5-5`), Claude Cowork, reasoning effort max; the serving model
may differ from the configured identifier. This is a cross-model LLM review
of [round one](../notes/round-1/README.md) of Project 05, recorded by
**gpt-6.1-sol (Codex)**, effort **ultra**: Notes 01–03, the four replay
programs and their records, and the requested
[working manuscript](../manuscript/constructive_stable_models.tex), as
committed at `74eb892` and unchanged at HEAD `001aaeb`. It is not
independent specialist review, and no subagents were used.

One caveat on independence. The opening gate that this round answers was
written into the [proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
from a Claude reply ([Reply 03](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md)
§3, Claude Fable 5.1), and the [setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md)
§6 expected "a short disposition rather than a candidate". On the overall
disposition this review is same-family with that prediction
([avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md)),
so the findings below come with proofs or with checks that can fail.
Every statement is labelled as a verification of the round's text, a
proof sketch by the reviewer, a floating computation, an interval
computation, a literature reading, or a recommendation. Nothing here bears
on the zeros of zeta.

**Summary.** I found no mathematical error in Notes 01–03 or in the
manuscript, and every finite computation reproduces. The four programs
replay with their recorded hashes and identical enclosures; an
independent mpmath program that shares no code, and uses different
formula routes where one exists, agrees with all of them (§2). The
claims are carefully scoped and honestly labelled, and the certificate
contracts are a model of the repository's conventions. Three findings
change how the round should be read:

1. **The main obstructions also exclude a known stable target (§3).** The
   odd-dilation, persistent-site and independent-array theorems apply
   verbatim to the Bessel seed \(e^{-2\pi\cosh4u}\), whose transform has
   only real zeros. They are limits on what the tested families can
   express, not information about theta. Only Note 02's source tests
   separate theta from that stable control, and they do so for
   de Bruijn's classical reason.
2. **Two extensions (§4), proved here in sketch for the reconciliation to
   check.** For stable approximants, weak convergence already implies
   complex-compact convergence and Laplace convergence at every real
   field, so the persistent-site theorem holds under weak convergence,
   which closes the gap stated in the manuscript's Remark 2.5. And every
   heat-type construction from stable seeds at a base time bounded away
   from \(0\) and \(-\infty\) is excluded unconditionally by Rodgers–Tao
   (\(\Lambda\ge0\)); with the odd-dilation theorem this closes Note 01's
   family at every bounded base time.
3. **Literature (§5).** Cardon's Theorem 1 (Proc. AMS 133, 1349–1356) is
   built on the same laws as Note 01, limits of normalized Rademacher
   sums, multiplied by real-zero entire factors, and is motivated by
   \(\Xi\); the round cites that paper only for Pólya's Proposition 1.
   Newman's papers that founded this viewpoint, Ginibre's GKS theorem,
   Pólya's \(\Xi^*\) and Hejhal's study of it, Khintchine's theorem and
   Rodgers–Tao belong in the record; with them, Section 3 of the
   manuscript has a short classical proof.

**Disposition (§8).** Confirm the round's negative results, with the
scope edits of §6. Round one answers the opening gate negatively: no
qualifying family. I recommend closing the opening phase and making the
project dormant with the reopening input stated in §8. The manuscript
should stay an unreviewed working record; in its present framing I do not
think it passes the portfolio's Manuscript gate.

## 1. Scope, artifacts and method

**Read in full.** Notes 01–03 and the round README; the manuscript source,
README and build record; the four programs, their records and the two
replay guides; the project README, draft history, proposal and folder
READMEs; the project chat record (history 1). For context: all of
[`avoid/`](../../../../avoid/README.md) and
[`result-summaries/`](../../../../result-summaries/README.md), the
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md)
and README, the predecessor
[program 13](../../../investigations-2/active/13_stability_jensen_lee_yang/notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
and the [10 October spin scout](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/15_lee_yang/notes/1_THETA_MOMENT_ENCLOSURE_AND_FERROMAGNETIC_SPIN_SCREEN_20261010.md),
the brainstorm's §3 exchange, and the setup review's §6.

**Replays.** All four programs were rerun in the cloud workspace with
python-flint 0.9.0 and FLINT 3.6.0, as recorded, under Python 3.13.16.
Each exits 0; script hashes equal the recorded ones; the regenerated JSON
equals the committed JSON field by field except the Python version, the
runtime and the two printed strings of one row, discussed in §7. The
manuscript recompiles with latexmk to the same 11 pages without warnings,
and the build record's source and PDF hashes match the committed files.

**Independent checks.** [`claude-review/`](../numerics/round-1/claude-review/README.md)
holds one program (mpmath; python-flint only for the optional Acb signs of
its section H) and its record. It imports nothing from the round. Routes
differ from the round's where possible: \(H_0\) through the
Riemann–Siegel \(Z\) function instead of \(\zeta\); moments by quadrature
of \(\Phi\) instead of the scout's Decimal cell sum; cumulants and
convolution coefficients by quadrature and numerical Taylor expansion;
the Chebyshev discriminant in exact rational arithmetic. Floating results
are evidence about implementation, not independent certificates.

**Literature fetched today** (statements quoted below were read in the
fetched text): Fröhlich–Rodriguez, Theorem 1 (arXiv text); Simon–Griffiths,
Theorems 1 and 3 and the GKS remark on p. 145 (scan, OCR); de Bruijn 1950,
Theorem 1 and p. 221 (scan, OCR); Cardon, Proposition 1 and Theorem 1
(author's preprint); Newman–Wu (arXiv); the abstracts of Newman 1975 and
1976, of Shi 2014 and 2017, and Hejhal's bibliographic record. Per
[avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md),
the two OCR readings are quoted only where the words survived extraction,
and Newman 1974 and Ginibre 1970 are cited from memory (Ginibre also as
Simon–Griffiths' reference [4]), not fetched.

## 2. What was verified

N01–N03 are the round's notes and MS the manuscript; equation numbers are
those of the cited file.

| Claim | Where | Check |
| --- | --- | --- |
| Quadratic heat weight gives couplings \(2tb_ib_j\); Lee–Yang applies with Fröhlich–Rodriguez's hypotheses (even law, \(\int e^{b\sigma^2}<\infty\), \(\cosh h\ne0\) on \(\Re h>0\), \(J\ge0\)) | N01 (2)–(4) | Verified; hypotheses read in the fetched Theorem 1 |
| \(\kappa_4=-2P_2\), \(\kappa_6=16P_3\); \(N\ge2/(3-m_4/m_2^2)\) | N01 (5)–(6) | Verified; independent value \(9.57409\), inside the stated \((9.5687,9.5795)\) |
| (7) in moment form | N01 (7) | Verified symbolically; theta's left side is \(+3.1\cdot10^{-9}\) (floating), so (7) excludes nothing, as the note says it does not need it |
| Heat laws (8)–(9) | N01 | Verified |
| Odd-dilation lemma, Hurwitz closure, floor (10) | N01 §4, MS Prop 4.1 | Verified. Acb record replayed; Riemann–Siegel route agrees to 20 digits at \(a,b\); on 61 points of \(B\), \(H_0\in[-3.67370,-3.67364]\cdot10^{-13}\), and \(|B|\max|H_0'|\approx6\cdot10^{-18}\) |
| Sub-Gaussian tail bound (11) and domain \(\Re t<125/3\) | N01 §5 | Verified |
| Pair example (\(\cos3\theta=23/27\)) and pair kurtosis \(\le1/p\le2\) | N02 §2 | Verified (derivative \(2p(1-p)(r-1)/D^3\)); generalizes the scout's equal-amplitude pair |
| Quartic seeds are Lee–Yang | N02 §3 | Verified as cited: Simon–Griffiths Thm 1 (p. 148) and Thm 3 (p. 151) |
| Cone (5) gives \(\Delta_h^3W(0)\ge0\); de Bruijn's class has nonnegative coefficients | N02 §3 | Verified (third differences of \(x^k\) are \(3!\,S(k,3)h^k\); the rotated odd Laguerre–Pólya argument) |
| (6) and (9) | N02 (6), (9) | Replayed; recomputed: \(-4.3499819129152\cdot10^{-4}\), \(-5.231189313578\cdot10^{-7}\) |
| Single-quartic weak limits; fixed-Bessel normal family | N02 §§3–4, MS Props 4.2–4.3 | Verified |
| Bessel transform, energy identity, Pólya's Proposition 1 hypotheses | N02 §4 | Verified; identity to \(10^{-40}\) at three \(z\); Proposition 1 read in Cardon's preprint |
| \(c=\pi-3/(2\pi)\); \(p_c\); \(\operatorname{disc}=2^{24}D(c)\), \(D(2+s)\) with negative coefficients | N02 §4 | Verified in exact arithmetic at 25 rational points (degree 5, so an identity) |
| Two-quartic marginal, \([s^6]=\tfrac92\kappa_3(W)\), \(\kappa_3(W)=-0.005059254092\) | N02 (11)–(14) | Verified; also \([s^4]=-1.112\), \([s^2]=2.177\) |
| Binomial envelope, \(c_N^4=1/(12N^3)\), heat bookkeeping | N02 (13), MS §5.3 | Verified analytically and for all even \(N\le400\) |
| Normalized ferromagnetic comparison (3) by duplication | N03 §1, MS Lemma 2.1 | Verified; Ginibre's GKS for arbitrary even single-site laws (Simon–Griffiths p. 145, ref. [4]) |
| Single-site monotonicity (5) | N03 §2 | Verified |
| Theta growth (8) | N03 (8), MS Lemma 1.1 | Verified: \(\log M_\theta(h)-\) asymptotic \(\to-0.4011900\) (at \(h=10^5\)) |
| Quartic saddle (9), lower bound (10) | N03 | Verified |
| No persistent site; (11a) | N03 §2, MS Thm 2.3, Cor 2.4 | Verified; witness fields in §4.1 |
| Independent quartic arrays, weak corollary (\(\kappa_4(X)=\tfrac14-3v^2<0\), Paley–Zygmund \(1/12\)) | N03 §3, MS Thm 3.1, Cor 3.2 | Verified; classical route in §5 |
| \(X+Y/4\) coefficients | N03 §6, MS §3 | Exact record replayed; closed forms agree with quadrature to 12 digits: \(0.975091599\), \(-0.164093918\) |

## 3. Finding 1: the obstructions also exclude a stable target

Let \(B(u)=e^{-2\pi\cosh4u}\). Its cosine transform is
\(\tfrac14K_{iz/4}(2\pi)\), which has only real zeros (Note 02 §4, by the
Dirichlet energy identity). It is a positive, even, double-exponentially
decaying source with real-zero transform: a **stable control** in the tail
class of theta.

**(a) Odd dilation.** *Interval computation (Acb, 160 bits).*
\(K_{iz/4}(2\pi)\) is positive at \(r_B-10^{-6}\) and negative at
\(r_B+10^{-6}\), where \(r_B=39.0750803340\); on the ball
\(3(r_B\pm10^{-6})\) it lies in \([-2.0368\cdot10^{-21}\pm7.8\cdot10^{-26}]\).
*Floating:* its real zeros below 125 are \(39.08,49.79,\dots,112.32,118.02,123.60\),
and \(3r_B=117.23\) is not among them. So the proof of Proposition 4.1,
word for word, shows that independent Bernoulli cosine products cannot
converge complex-compactly to this stable function.

**(b) Field growth.** *Floating:* \(\log M_B(10^4)=14201.6\), against
\(h^{4/3}=215443\); analytically \(\log M_B(h)=\tfrac h4\log h\,(1+o(1))\),
since the tail is \(e^{-\pi e^{4u}}\) as for theta. The proofs of
Theorem 2.3, Corollary 2.4 and Theorem 3.1 use only
\(\log M=o(h^{4/3})\) and, for Theorem 3.1, a non-Gaussian limit. They
apply verbatim with \(B\) in place of theta.

**(c)** The single-quartic and one-pair exclusions are likewise statements
about the family's shape: \(B\) is neither quartic nor Gaussian, and its
kurtosis is \(2.877>2\) (floating).

By contrast, \(B\) **passes** Note 02's tests: \(-\log B=2\pi\cosh4u\) has
nonnegative even coefficients, so \(B\) lies in the cone (5) and in
de Bruijn's class, and \(U\equiv1\) lies in Proposition 4.3's multiplier
class. Those two tests are the round's only theta-discriminating
statements, and their content is classical. A source \(e^{-f}\) with \(f\)
in de Bruijn's class, or \(B\,U\) with \(U\) entire, continues to an entire
function of \(u\); \(\Phi\) does not continue across \(|\Im u|=\pi/8\).
De Bruijn makes exactly this argument against universal-factor
approximation on p. 221: "We must not expect that the function
\(\Phi(t)\) can be approximated by functions" of that form, because
factors converging in a small circle give a limit that continues to the
whole plane, which \(\Phi\) does not (OCR reading; the scan loses the
symbol \(\Phi\)). Note 02's normal-family step is the same argument, and
the finite differences (6) and (9) are finite diagnostics of that fact.

**Consequence (reviewer's reading).** The round's main obstructions say
that zero sets of independent Bernoulli products lie in odd-multiple
progressions, and that a ferromagnetic network keeping a non-negligible
diffuse site has tails no thinner than that site's. Both would equally
reject any construction of a known stable function in theta's tail
class. They prune families correctly, and they carry no information about
whether theta is stable. This is the mirror image of
[avoid 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md):
an obstruction whose premises a stable control also satisfies is a
statement about the family.

**Recommendation.** Add the Bessel seed (or Pólya's \(\Xi^*\), §5) to the
project's controls as a *stable* control, run in the reverse direction: a
family excluded for a reason that also excludes the stable control is a
family-expressiveness result, and any future nomination should first show
that its family can approximate the stable control. The forward control
tables in Notes 01–03 and manuscript §6 cannot fail: by Hurwitz, no
function with a nonreal zero is a complex-compact limit of real-zero
functions, whatever its source properties
([avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)).
One sentence can replace them.

## 4. Finding 2: two extensions

### 4.1 Weak convergence suffices for stable approximants

**Lemma (reviewer's proof sketch; please check in the reconciliation).**
Let \(\mu_n\) be symmetric probability laws whose characteristic functions
\(f_n\) are entire and in the Laguerre–Pólya class, so that
\(f_n(z)=e^{-a_nz^2}\prod_k(1-z^2/x_{n,k}^2)\) with \(a_n\ge0\). If
\(\mu_n\to\mu\) weakly and \(f\ge\tfrac12\) on \([-\delta,\delta]\), where
\(f\) is the (real) characteristic function of \(\mu\), then:

1. \(\operatorname{Var}\mu_n\le(8\log4)/\delta^2\) for all large \(n\);
2. \(f_n\to F\) locally uniformly on \(\mathbb C\), with \(F\) entire and
   \(F=f\) on \(\mathbb R\); in particular \(F\) is Laguerre–Pólya;
3. \(\int e^{hu}\,d\mu_n\to F(-ih)=\int e^{hu}\,d\mu\) for every real \(h\).

*Proof.* By Lévy's theorem \(f_n\to f\) uniformly on \([-\delta,\delta]\),
so \(f_n\ge\tfrac14\) there for large \(n\). Hence every \(|x_{n,k}|>\delta\),
and for \(0\le x<\delta\) each factor satisfies
\(0<1-x^2/x_{n,k}^2\le e^{-x^2/x_{n,k}^2}\). Therefore
\(f_n(x)\le e^{-\sigma_nx^2/2}\) with
\(\sigma_n=2a_n+2\sum_kx_{n,k}^{-2}=\operatorname{Var}\mu_n\), and
\(x=\delta/2\) gives (1). The same product gives
\(|f_n(z)|\le e^{\sigma_n|z|^2/2}\), so the family is locally bounded on
\(\mathbb C\), and Vitali's theorem gives (2). For (3),
\(f_n(-ih)=\int e^{hu}d\mu_n\to F(-ih)\); Fatou makes \(\int e^{hu}d\mu\)
finite, so \(f\) is entire and equals \(F\). \(\square\)

The bound \(|f(z)|\le e^{\sigma|z|^2/2}\) is immediate from the product
representation in Newman–Wu §3 (their eqs. (27)–(28)); Newman (1975)
proves the corresponding Gaussian domination of moments for Lee–Yang
fields. *Floating sanity check* on the two-quartic seed:
\(\log\mathbb E e^{hS}\le\tfrac12\operatorname{Var}(S)h^2\) at
\(h=\tfrac12,1,2,4\) (\(0.70\le0.86\), \(2.01\le3.44\), \(4.88\le13.8\),
\(11.0\le55.1\)).

**Consequences.**

- Readout laws of finite ferromagnetic quartic or Ising networks have
  entire Laguerre–Pólya characteristic functions (Simon–Griffiths
  Theorem 3; order at most \(4/3\)). So **Theorem 2.3 and Corollary 2.4 hold
  with "\(M_n(h)\to M_\theta(h)\) for every real \(h\ge0\)" replaced by weak
  convergence of the readout laws.** The limitation stated in Remark 2.5
  and at the end of Note 03 §2 can be removed, and Corollary 3.2 becomes a
  special case.
- A weak limit of stable laws is stable. Section 1's sentence "would imply
  RH by Hurwitz's theorem" can say that weak convergence already suffices,
  so the target is RH-strength in the weakest natural mode.

**Where Theorem 2.3 acts.** *Floating, exact quartic transform.* For a unit
quartic site \(e^{-x^4}\) read out with weight \(\ell\), GKS makes the
readout variance at least the isolated site's, \(\ell^2v\) with
\(v=\mathbb EX^2=0.33799\). So sites with \(\ell^2v>m_2\), that is
\(\ell>\sqrt{m_2/v}=0.18488\), are excluded already by the second moment.
Below that, the theorem acts in the far tail:

| \(\ell\) | site variance | first field with \(m(\ell h)>M_\theta(h)\) |
| --- | --- | --- |
| \(\ge0.2\) | \(\ge0.0135\) | \(0^+\) (variance) |
| \(0.18\) | \(0.0110\) | \(5.8\cdot10^4\) |
| \(0.15\) | \(0.0076\) | \(1.9\cdot10^5\) |
| \(0.10\) | \(0.0034\) | \(1.9\cdot10^6\) |
| \(0.05\) | \(0.00084\) | \(7.3\cdot10^7\) |

At these fields the tilted theta law sits near
\(u\approx\tfrac14\log(h/4\pi)\approx2.1\)–\(3.9\), where
\(\Phi<e^{-10^4}\). This supplies the \(h_*\) that the manuscript declines
to quantify, and it shows that the theorem is a far-tail statement for
thin sites.

### 4.2 Heat-type constructions from a negative base time

**Proposition (reviewer's proof sketch).** Let \(\mu_n\) be stable seeds
(symmetric, entire Laguerre–Pólya characteristic functions), let
\(\lambda_n\ge0\) with \(\int e^{\lambda_nu^2}d\mu_n<\infty\), and let
\(\nu_n\propto e^{\lambda_nu^2}\mu_n\) be their forward heat evolutions.
If \(\nu_n\to\mu_\theta\) weakly and \(\lambda_n\to\lambda\in(0,\infty)\), we
reach a contradiction.

*Proof.* \(Z_n=\int e^{\lambda_nu^2}d\mu_n\) satisfies
\(Z_n^{-1}=\int e^{-\lambda_nu^2}d\nu_n\to\int e^{-\lambda u^2}d\mu_\theta>0\),
since \(e^{-\lambda_nu^2}\to e^{-\lambda u^2}\) uniformly on \(\mathbb R\).
Hence \(\mu_n=Z_ne^{-\lambda_nu^2}\nu_n\) converges weakly to the law
\(\propto e^{-\lambda u^2}\Phi(|u|)\,du\), whose characteristic function is
\(H_{-\lambda}/H_{-\lambda}(0)\). By the lemma this is Laguerre–Pólya, so
\(H_{-\lambda}\) has only real zeros, contradicting \(\Lambda\ge0\)
(Rodgers–Tao): \(H_t\) has a nonreal zero for every \(t<0\). \(\square\)

If \(\lambda_n\to0\), the same untilting gives \(\mu_n\to\mu_\theta\): the
seeds face the time-zero problem themselves. Applied to Note 01's family,
with independent seeds at base time \(-\tau_n\) and \(\tau_n\) bounded,
every subsequential limit \(\tau>0\) is excluded by Rodgers–Tao, and
\(\tau=0\) by the floor (10), because Lévy's theorem makes the seeds' cosine
products converge to \(H_0/I_0\) uniformly on \(K\). Approximating \(H_{t_0}\)
by \(Q_N(t_0,\cdot)\) at a positive time untilts to the same time-zero
statement. So the items Note 01 §6 leaves open ("constructions based at
changing negative times or positive-time approximation without a
controlled limit to zero") are closed for that family **except base
times tending to \(-\infty\)**. There the couplings \(2\tau_nb_ib_j\) need not
vanish; that is the mean-field regime, which belongs with the interacting
networks. The proposition turns Reply 03's remark that a heat-type
creation step only moves the problem to the seed's earlier time into a
theorem-backed rule.

## 5. Finding 3: literature and classical framing

- **Cardon, *Fourier transforms having only real zeros*, Proc. Amer. Math.
  Soc. 133 (2005), 1349–1356**, Theorem 1 (author's preprint): for \(G\)
  real entire of order \(<2\) with only real zeros, nonincreasing
  \(a_k>0\), independent \(\pm1\) variables \(X_k\), \(F_n\) the law of
  \((a_1X_1+\dots+a_nX_n)/s_n\) and \(F=\lim F_n\), the transform \(H\) of
  \(G(it)\,dF(t)\) is entire and, if not identically zero, "H has only
  real zeros"; §1 motivates it by \(\Xi\). These are Note 01's time-zero laws, in the limit
  of normalized sums, extended by multipliers. The odd-dilation
  obstruction covers \(G\equiv\) const only. For a fixed even \(G\) with
  \(G(0)>0\), so that \(G(iu)\ge G(0)\), untilting as in §4.2 shows that
  the multiplied family approximates \(\Phi\) only if the Rademacher laws
  approximate \(\Phi(u)/G(iu)\), whose transform must then be a limit of
  cosine products, hence closed under odd dilation: a finite test for each
  \(G\), and the natural first test if this family is ever nominated. The
  paper says its exponential-sum lemma is proved like the Lee–Yang circle
  theorem; see also Cardon, *Sums of exponential functions having only
  real zeros*, Manuscripta Math. 113 (2004), 307–317.
- **Newman.** *Fourier transforms with only real zeros*, Proc. AMS 61
  (1976), 245–251, which introduced the constant and the measure-theoretic
  viewpoint; *Inequalities for Ising models and field theories which obey
  the Lee–Yang theorem*, Comm. Math. Phys. 41 (1975), 1–9 (Gaussian
  domination); and, not fetched today, *Zeros of the partition function
  for generalized Ising systems*, CPAM 27 (1974). With Wu, *Constants of
  de Bruijn–Newman type in analytic number theory and statistical
  physics*, Bull. AMS 57 (2020), no. 4 (arXiv:1901.06596), whose
  Definition 15 class (even, sub-Gaussian, real-zero characteristic
  function) is the natural home of every family in this round.
- **Ginibre (1970)**, GKS for arbitrary even single-site laws, which
  Lemma 2.1 re-proves; the manuscript cites only Simon–Griffiths' mention
  of it.
- **Pólya (1926)** and his \(\Xi^*\): de Bruijn p. 221 records that Pólya's
  approximant "has real roots only, since cosh 9t/4 is a universal
  factor" (OCR reading). Note 02 §4 is this construction; \(\Xi^*\) is also
  a second stable control for §3. **Hejhal**, *On a result of G. Pólya
  concerning the Riemann \(\xi\)-function*, J. Analyse Math. 55 (1990),
  59–95. **Y. Shi**, arXiv:1502.06844 (real-rooted Pólya-like
  approximations anchored at both ends of the kernel), and
  arXiv:1706.08868 (math.GM, which claims RH by convergence of stable
  approximants on the strip; unrefereed, abstract read only). A project in
  this lane should know where such arguments fail before repeating them.
- **Classical probability.** Theorem 3.1 has a short classical route.
  Characteristic functions of infinitely divisible laws never vanish,
  while \(H_0\) has real zeros (Note 01's certified bracket suffices), so
  theta's law is not infinitely divisible. By Khintchine's theorem it is
  therefore not a weak limit of any infinitesimal independent array, of
  any single-site laws, quartic or not. Only arrays with non-negligible
  summands remain, and for the round's two classes these are excluded by
  the growth argument (quartic) and by odd dilation (Bernoulli), under
  weak convergence by §4.1. An infinitely divisible law with a
  Laguerre–Pólya characteristic function is Gaussian, since that function
  has no zeros; this is the manuscript's "the limit must be Gaussian".
- **Rodgers–Tao**, *The de Bruijn–Newman constant is non-negative*, Forum
  Math. Pi 8 (2020), arXiv:1801.05914, for §4.2. **Dimitrov–Rusev**, *Zeros
  of entire Fourier transforms*, East J. Approx. 17 (2011), 1–108, is the
  survey of this literature.

**Recommendation.** The manuscript's "No literature priority is claimed"
is right; it should also say which statements are classical: Proposition
4.3 (de Bruijn), Theorem 3.1 (Khintchine plus field growth), Lemma 2.1
(Ginibre), the odd-dilation lemma (elementary), and that Note 01's family
is Cardon's at \(G\equiv1\).

## 6. Smaller mathematical and expository points

1. **Lemma 1.1.** "The \(\log h\) coefficient is \(2-1/4\)": the
   contributions are \(+2\) from \(s(s-1)\), \(+\tfrac14\) from
   \((s/2)\log(s/2)\) with \(s/2=(h+1)/4\), and \(-\tfrac12\) from
   Stirling. The constant term is \(-0.40119\) (floating), if wanted.
2. **Scale of (10).** \(\delta=3.6\cdot10^{-13}\) is \(5.8\cdot10^{-12}H_0(0)\)
   and \(0.98\min_B|H_0|\). The statement reads more naturally as: either the
   error on \([a,b]\) is at least \(2.4\cdot10^{-11}\) or the error on \(B\) is at
   least \(3.67\cdot10^{-13}\), that is, essentially all of \(|H_0|\) there.
3. **Note 02 §5.** That test (6) "cannot exclude" the coupled seed follows
   from the \(s^6\) sign only for small steps. *Floating:* the seed's own
   third difference at \(h=1/100\) is \(-1.27\cdot10^{-7}\), and that of
   \(X+Y/4\) is \(-9.76\cdot10^{-7}\); both carry theta's sign. State the values.
4. **Proposition 4.3.** Once the normal-family step produces an entire
   \(U\) with \(B_0U=\Phi\), de Bruijn's continuation argument (§3) finishes
   the proof; the five-node certificate is then an optional finite
   diagnostic. Quantitative readings of both finite tests: the weights of
   \(\Delta^3\) sum to 8 and those of \(\Delta^4\) to 16, so for every normalizer
   some node has log-density error at least \(5.4\cdot10^{-5}\) for the cone,
   and multiplier error at least \(3.3\cdot10^{-8}\) (against values near
   240) for the Bessel class.
5. **Theta's potential.** *Floating:* the Taylor coefficients of
   \(-\log\Phi(\sqrt x)\) begin \(0.8059,\ 37.45,\ 95.34,\ -137.67,\ 1549.9,\ -15221,\ 150530\),
   so the \(u^6\) coefficient is already negative. The series converges
   slowly at the test nodes (radius about \(0.1\) in \(x\)), which is why the
   finite difference, needing only four real evaluations, is the
   convenient certificate.
6. **Cone (5)** allows either sign of the quartic coefficient (the
   coupled seed's marginal has \([s^4]=-1.112\)); say so where (4) requires
   \(\alpha>0\), to avoid confusion.
7. **Bibliography.** Complete the Cardon entry (Proc. AMS 133,
   1349–1356) and add the references of §5.

## 7. Records, reproducibility and conventions

1. **Certificate practice is good.** Budgets are declared, scouts are
   separated from retained runs, tails are paid analytically, and one ball
   covers the whole tripled interval. One portability point: the
   tripled-interval row prints 65 digits of a ball of radius
   \(6.5\cdot10^{-17}\). On Python 3.13 the digits below the radius differ
   from the committed string, while the enclosures agree. Print
   radius-limited digits, or compare enclosures rather than strings, in
   any future replay test.
2. **Compiled PDF.** The 305 KB PDF is tracked. [LARGE_FILES.md](../../../../LARGE_FILES.md)
   permits small PDFs, but the [16 October changelog entry](../../../../CHANGELOG.md)
   untracked the reading copies and pointed READMEs to the `.tex`, and
   Edward's stated convention keeps only the source. Project 07 does the same, so
   this is a portfolio decision for Edward.
3. **Draft history.** The three entries name sources but no commit. The
   round is commit `74eb892`, whose message says "investigation 4"; record
   the hash there.
4. **Status files lag** ([avoid 19](../../../../avoid/19_status_files_that_lag_the_findings.md)).
   The portfolio README still lists 05 as "Gated on a qualifying explicit
   family"; the research-overview README says "Current opening plan; not
   executed". Besides this review and its `claude-review/` folder, I
   changed only the reviews README (its index row) and, by the standing
   project instruction, this session's chat record.
5. **Process.** The proposal gave the nomination to Claude and the audit
   to Codex, with a cross-model review at each phase. Round one was Codex
   throughout, extended twice and written up at Edward's explicit request
   before any review. That was his call, and the notes record it; the
   README should also say that phases 0–2 ran without their cross-model
   gates and that this review is the first cross-model check.
6. **Volume** ([avoid 20](../../../../avoid/20_volume_without_a_gain.md)).
   About 51 KB of notes and an 11-page draft record what the setup review
   expected, and what the mathematics is: a short disposition. Its content
   fits in two pages: the odd-dilation floor, the persistent-site theorem,
   the classical exclusions, and the open regime.
7. **Chat record.** History 1 is registered. It notes that Note 01's
   opening was accidentally truncated and restored before the commit; the
   committed Note 01 is complete (sections 1–6 read).

## 8. Disposition and recommendations

1. **Accept as correct**, with the edits of §6: the odd-dilation
   obstruction and floor; the pair bound; the single-quartic, cone and
   fixed-Bessel exclusions; the coupled seed, its coefficient and its
   Ising realization; the normalized GKS comparison; the persistent-site
   theorem; the independent-array theorem.
2. **Adopt the two extensions** of §4 after Codex checks them in the
   reconciliation. One reconciliation, as the portfolio plan asks.
3. **Read the outcome correctly.** The tested families cannot express
   theta's tail class or zero arithmetic. The same obstructions exclude
   the stable Bessel seed, and the round's only theta-specific statements
   are de Bruijn's. Round one answers the opening gate negatively: no
   qualifying family.
4. **Close the opening phase and make Project 05 dormant.** This follows
   the proposal's stopping rule (a useful exact obstruction completes the
   phase; reopen only for a different construction or a new inequality),
   the plan's rule after one derivation-and-review cycle, and the
   intention in the commit message. Reopening input: a named family in
   the remaining regime (infinitesimal interacting sites, mean-field
   coupling with base time
   tending to \(-\infty\), or Cardon-type multiplied Rademacher laws with
   non-Gaussian \(G\)), together with (i) a proof or certified bound that
   the family approximates the stable Bessel seed or \(\Xi^*\), and (ii) the
   theta-specific mechanism by which the family sees what the stable
   control lacks: the boundary of \(\Phi\) at \(|\Im u|=\pi/8\), or the
   arithmetic of the zeros. Without (i) the family fails on
   expressiveness. Without (ii), success would be an RH-equivalent
   restatement ([avoid 01](../../../../avoid/01_restating_the_target.md)).
5. **Manuscript.** Keep it as an unreviewed working record, not a
   milestone. In my judgment it does not pass the plan's Manuscript gate
   ("substantial precise obstruction") in its present framing: its main
   theorems are short consequences of classical results, and its
   obstructions are theta-agnostic. If a citable record is wanted, an
   accurate four-to-five-page note would be built around the lemma of
   §4.1, the persistent-site theorem under weak convergence, the
   Rodgers–Tao exclusion of negative base times and the reverse-control
   observation, with the attributions of §5. That is a judgment for Edward,
   not a finding.
6. **Proposed file changes, not made here** (one writer per file): the
   §6 edits in Notes 01–03 and the manuscript; Remark 2.5 and Note 03 §2
   (weak convergence); Note 01 §6 (closed base-time items); the control
   tables reduced to one sentence; draft history (commit hash); portfolio
   README row and research-overview README (status); project README
   (dormancy and process note); the PDF decision.
7. **After the reconciliation.** Add evidence lines to
   [avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
   (Cardon's Theorem 1 contains the family studied, and the round cites
   the same paper for another statement) and to
   [avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
   (forward control tables that Hurwitz makes automatic). Add a short
   result-summary entry, in a cluster of Edward's choosing, stating the
   obstructions with the reverse-control caveat.

## Appendix A. Artifact digests at review (SHA-256, first 16 hex digits)

| Artifact | Digest |
| --- | --- |
| Note 01 | `e096830eb1320de9` |
| Note 02 | `fd7ccbb0554f3d47` |
| Note 03 | `26f4076600d4192d` |
| Round-one README | `da47c409324668d5` |
| `constructive_stable_models.tex` | `39eeebf0b7712e60` (matches build record) |
| `constructive_stable_models.pdf` | `cddec940f7d7757b` (matches build record) |
| `BUILD_RECORD.json` | `a1a095e6ac673940` |
| `certify_harmonic_obstruction.py` | `39e8c1dfba3e8e9b` (matches its record) |
| `certify_source_alternative_obstructions.py` | `537c77181cad592c` (matches) |
| `certify_two_quartic_seed.py` | `29f4f6d8cdf924ec` (matches) |
| `certify_unequal_quartic_convolution.py` | `9b033c8990be14ad` (matches) |
| `HARMONIC_SIGN_CERTIFICATE.json` | `7a1345a6fcba54e0` |
| `SOURCE_ALTERNATIVE_OBSTRUCTIONS.json` | `cec4cc6db2944540` |
| `TWO_QUARTIC_SEED_CERTIFICATE.json` | `fc97ec24859002cb` |
| `UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json` | `ece5156053662266` |

## Appendix B. Computations

The [review-check program](../numerics/round-1/claude-review/review_checks_claude_20261017.py)
and its [record](../numerics/round-1/claude-review/REVIEW_CHECKS_CLAUDE_20261017.json)
contain the computed numbers quoted above, in nine sections: A digests and hash
matches; B \(H_0\) by Riemann–Siegel; C moments by quadrature; D the
source differences and Taylor coefficients; E the coupled seed and
\(X+Y/4\); F exact checks (Chebyshev polynomial and discriminant, binomial
envelope, Bessel identity, pair example); G the theta growth constant and
crossover fields; H the Bessel seed as a stable control, with Acb signs;
I the sub-Gaussian check. The full run takes about three and a half
minutes on one core. The record was produced in the cloud workspace with
Python 3.13.16, mpmath 1.3.0 and python-flint 0.9.0; see the folder README
for the run on Edward's machine.
