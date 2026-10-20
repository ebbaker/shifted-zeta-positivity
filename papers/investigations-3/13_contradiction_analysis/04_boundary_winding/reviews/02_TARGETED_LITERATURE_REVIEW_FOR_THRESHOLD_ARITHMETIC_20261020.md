# Targeted literature review for threshold signed arithmetic

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from recorded turn metadata.

**The most useful additional reading is moment-bound optimization and
the conditioning of near-collision recovery. The established heat-flow
and Laguerre literature supplies important identities and approximation
theorems, but the sources checked here do not provide the missing
fourth-order opposing sign at a hypothetical positive theta threshold.**

This is a targeted source review for the [active program][program],
paired with the [repository capability map][capabilities]. It is neither
an exhaustive bibliography nor an independent referee report on every
cited paper. Searches and source checks were made on 20 October 2026.
Full primary-source passages were checked for items 1–6 and the stated
conditional theorem in item 8. Item 7 and item 9 were screened at the
primary abstract/version-record level. No third-party PDFs were stored
in the repository.

Repository context was read at
`574b658061c5144a78d44a805fe2c116d86f9397`, using the
[result summaries][results], especially [controls][controls] and
[arithmetic identities][arithmetic], and the [avoid index][avoid],
especially [unchecked imports][imports] and [scoped claims][scope].
“Additional” below means a potentially useful connection for this
program, not a claim of mathematical novelty.

## 1. Bertsimas–Popescu: optimize what the observations actually imply

Dimitris Bertsimas and Ioana Popescu, *Optimal Inequalities in Probability
Theory: A Convex Optimization Approach*, SIAM Journal on Optimization
15(3), 2005, 780–804. [Publisher DOI](https://doi.org/10.1137/S1052623401399903);
[full author-institution working paper](https://flora.insead.edu/fichiersti_wp/inseadwp2004/2004-62.pdf).

The paper formulates optimal bounds on mass in a specified set under
moment constraints. Section 2 gives primal/dual problems and weak
duality; strong duality has additional hypotheses. Section 3 treats
univariate polynomial moment bounds through semidefinite optimization.
The dual certificate is a pointwise majorant whose integral is determined
by the observations.

**Possible contribution:** use actual theta profile intervals to
majorize the number of nearby residual zeros, then bound their
inverse-square contribution after a gap is established. The capability
map spells out a finite weighted measure and rational observations.
That adaptation needs its own proof and certified inequalities.
The paper does not establish stability for this infinite zero set or
guarantee a useful bound for the theta data.

**Priority: high for a bounded feasibility study.** No Bertsimas or
Popescu reference was found in the searched research prose/bibliography
corpus.

## 2. Batenkov–Goldman–Yomdin: quantify the accuracy lost near collisions

Dmitry Batenkov, Gil Goldman and Yosef Yomdin, *Super-resolution of
near-colliding point sources*, [arXiv:1904.09186](https://arxiv.org/abs/1904.09186);
[author-hosted full text](https://dimabatenkov.info/pdf/batenkov2019a.pdf).

Definition 2.2 and Theorem 2.1 treat finitely many point sources with a
specified cluster, separated remaining nodes, bounded nonzero amplitudes,
and noisy Fourier observations. The theorem gives matching error scales
for recovering cluster nodes and amplitudes. Its permitted noise depends
strongly on the cluster width and bandwidth.

**Possible contribution:** design an accuracy-versus-gap test before
acquiring many profile samples. Recovery of nearly coincident zeros is
an ill-conditioned inverse problem even when the forward data are
accurate. These rates do not transfer automatically: our observations
are Stieltjes-type values of an infinite zero measure, not the paper's
finite Fourier data.

**Priority: high as an accuracy and failure-analysis reference; medium
as a source of a directly applicable theorem.** No Batenkov or Prony
reference was found in the searched corpus.

## 3. Stopple: relate inverse-square sums to derivative information

Jeffrey Stopple, *Lehmer Pairs Revisited*,
[arXiv:1508.05870v2](https://arxiv.org/html/1508.05870v2), 2015.

Section 4 expresses sums over other zeros through derivatives of the
pre-Schwarzian at simple zeros. Section 5 includes an explicit
logarithmic-derivative localization lemma, with errors \(30M/r\) and
\(90M/r^2\) under its contour-growth and zero-location hypotheses.

**Possible contribution:** a template for retaining a finite local zero
cluster while paying the rest analytically. This could complement the
repository's explicit zero-count bounds. However, the paper assumes RH
throughout and its Lehmer-pair conclusions concern lower bounds on
\(\Lambda\). They cannot be imported as an unconditional exclusion of a
positive threshold. Use at a multiple event requires deflation, and use
for \(H_T\) requires checking its own hypotheses and normalization.

**Priority: medium.** Stopple appears elsewhere in the repository, but
this paper's title/arXiv identifier was not found in the searched corpus.
The explicit local lemma is the most relevant part to inspect further.

## 4. Polymath: the main approximation source is already in use

D. H. J. Polymath, *Effective approximation of heat flow evolution of the
Riemann \(\xi\) function, and a new upper bound for the de Bruijn–Newman
constant*, [arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 2019.

Theorem 1.3 provides the effective Riemann–Siegel approximation; Section 6
gives the detailed error machinery. Theorem 1.2 separates initial
verification, the moving barrier, and final-time exterior nonvanishing.

**Contribution here:** this remains the primary source behind Project
11's arithmetic approximation and Project 06's counts. A higher-derivative
application must freeze a holomorphic cutoff model, verify the relevant
complex neighborhood and pay Cauchy losses. A small value error alone
does not certify four derivatives. The global criterion also explains
why finite noncollision coverage is insufficient.

**Priority: high, but already substantially absorbed.** Read it together
with the repository's corrected local interfaces and latest reviews;
reusing an old scalar error without those corrections would regress.

## 5. Rodgers–Tao: zero dynamics with a crucial direction of implication

Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is
non-negative*, [arXiv:1801.05914](https://arxiv.org/abs/1801.05914);
[full v5 text](https://arxiv.org/pdf/1801.05914v5).

The paper proves \(\Lambda\ge0\). It assumes \(\Lambda<0\) for a
contradiction, obtains increasingly strong control of the zeros in
the real simple regime, and derives local equilibrium incompatible
with known zeta-zero statistics. Section 4, Theorem 11, records the
principal-value zero-motion equations on \(\Lambda<t\le0\).

**Contribution here:** energy identities and interaction sums can guide
a proposed nonlocal mechanism. Their effective use must retain the
time interval and distance from the threshold used in the proof.
The theorem does not give a uniform gap or curvature lower bound
at \(t=\Lambda>0\), nor can its contradiction simply be reversed
to prove \(\Lambda\le0\).

**Priority: medium for a defined dynamics question; already foundational
in the repository.**

## 6. Csordas: complete correlated kernels, with positivity left open

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann \(\xi\)-function*,
[arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2), 2014 revision.

Theorem 3.7 represents generalized Laguerre expressions by Fourier
transforms of associated kernels and characterizes the Laguerre–Pólya
property by positive definiteness of all those kernels, under the stated
admissibility and logarithmic-concavity hypotheses. Open Problem 4.7
explicitly asks for the basic theta Laguerre inequality.

**Contribution here:** preserve complete two-source correlations when
rewriting a signed expression. Pointwise positivity of the source or
of an associated kernel is not positive definiteness of that kernel,
and the missing positivity is not a theorem of this paper. Applying
its formulation to a positively heat-weighted source also requires
checking its hypotheses.

**Priority: medium as an identity source; already used extensively.**
The arXiv identifier occurs in 15 searched repository files. Reintroducing
this characterization alone would not be an additional estimate.

## 7. Dobner: an arithmetic proof in the negative-time direction

Alexander Dobner, *A proof of Newman's conjecture for the extended
Selberg class*, [arXiv:2005.05142v2](https://arxiv.org/abs/2005.05142v2);
Acta Arithmetica 201 (2021), 29–62. The arXiv record was updated
10 January 2026 to match the published version.

The primary abstract describes a proof of nonnegativity using an
arithmetic approximation at \(t<0\), rather than information about
the original zeta zeros. Its Dirichlet series has weights
\(\exp(t\log^2 n/4)\).

**Possible contribution:** a source-specific arithmetic comparison worth
consulting if a concrete estimate calls for it. The sign of time is
essential: the reported argument produces off-line zeros for negative
time and does not supply a positive-threshold upper bound for \(Q_L\).
This review checked the current abstract/version record, not the full
proof. The repository already uses Dobner in the Dirichlet-family work.

**Priority: secondary for this particular consumer.**

## 8. Recent translated-probe comparisons: useful methods, conditional imports

Michel Planat, *A certified classical-strip comparison for the
de Bruijn–Newman constant*,
[arXiv:2610.18214v1](https://arxiv.org/html/2610.18214v1),
13 October 2026.

Theorem 1.1 states its numerical bound under explicit true-function
source, localization and uniform first-contact premises. Section 2
combines translated rational kernels before clearing denominators and
describes exact Bernstein certificates for the resulting polynomial
inequalities.

**Possible contribution:** the rational-kernel certification technique
is relevant to a profile-majorant experiment. Its source-to-function
premises and original comparison would require a separate audit before
use. The numerical bound is not treated here as an independently
validated unconditional result or as a fourth-jet estimate.

**Priority: method reference, with conditional status retained.**
Project 03 already records this paper in its October literature table.
This is therefore a clarified connection, not a newly discovered
repository omission.

## 9. Recent random-polynomial heat flow: a model reference only

Jonas Jalowy, *Heat flow and repeated differentiation of polynomials with
i.i.d. roots*, [arXiv:2609.24867v2](https://arxiv.org/abs/2609.24867v2),
1 October 2026 revision.

The abstract states limiting-zero-distribution results for random
polynomials, including small-time transport under a Lipschitz Stieltjes
transform assumption. The method uses leave-one-root recursions and
concentration.

**Possible contribution:** examples and ideas for a resolvent
calculation. An empirical limiting distribution does not resolve the
microscopic gap at one deterministic theta event; random independence
and concentration cannot be assigned to theta zeros. Only the primary
abstract/version record was screened here.

**Priority: low for the present sign problem.** No Jalowy reference or
this arXiv identifier was found in the searched corpus.

## What this changes in the brainstorming

The additional literature suggests a focused question: can actual theta
observations support a certified rational majorant strong enough to
exclude another zero near the assumed double event, with all error
amplification paid? This is distinct from a universal bound based on
source positivity or generic finite profile data. The
[capability map][capabilities] gives the proposed measure normalization,
the integer-count test, the subsequent \(S_2\) target, and its controls.

For the direct arithmetic route, the repository's own complete
approximation and correlated-residual work remain the more immediate
starting point. The literature reviewed here supplies no shortcut around
the missing estimate for the retained fourth-order expression.

Search scope for repository-presence statements: `.md`, `.tex` and `.bib`
files under `papers/`, `result-summaries/` and `references/`, excluding
directories named `chat-histories`, `archive` and `drafts`.
These are bounded text-search findings, not exhaustive absence claims.
Online searches covered effective theta heat flow, zero dynamics and
Lehmer pairs, Laguerre kernels, moment inequalities, near-collision
recovery and recent polynomial heat flow. Primary author, institutional,
journal or arXiv sources support the descriptions above; search-engine
summaries and third-party claimed RH proofs were not used as mathematical
inputs.

[program]: ../research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[capabilities]: ../brainstorm/02_REPOSITORY_CAPABILITIES_AND_RESEARCH_OPTIONS_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[arithmetic]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
