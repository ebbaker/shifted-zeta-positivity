# References and inspected scope

25 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), actual effort max**, chat0022.

These are primary references for the
[working draft](../manuscript/main.tex). The reusable entries are in
[references.bib](references.bib). Online text was inspected; no new PDF
download was needed. The parent catalog and its sibling provenance
remain the home of the existing Polymath reading copy.

## External primary sources

1. **D. H. J. Polymath**, *Effective approximation of heat flow evolution
   of the Riemann xi function, and a new upper bound for the de
   Bruijn–Newman constant*, arXiv:1904.12438v2, revised 4 August 2019.
   [Versioned primary HTML](https://arxiv.org/html/1904.12438v2).
   Rechecked normalization (1)–(4), exact domain (5), gamma/Stirling
   definitions (6)–(10), Theorem1.3 and (14)–(24), the retained-C
   correction discussion pointing to (69), Gaussian formula (35),
   and Proposition9.1's statement. The explicit early domain has
   0<t<=1/2, 0<=y<=1, X>=200; negative time is not imported. The
   large-height onset deteriorates toward zero time. Full proofs and
   a negative-time extension were not audited. The exact parent gamma
   factor is distinguished from this source's Stirling factor.
   [Existing parent catalog](../../references/README.md).

2. **NIST DLMF §5.11**, [Gamma asymptotics](https://dlmf.nist.gov/5.11).
   Rechecked equations 5.11.1–5.11.3, 5.11.9 and sectorial remainder
   hypotheses. Used to calibrate the elementary amplitude, phase and
   logarithmic derivative. No whole-chapter or differentiated theta
   error theorem is imported.

3. **NIST DLMF §25.10**, [Riemann–Siegel formula](https://dlmf.nist.gov/25.10).
   Inspected 25.10.1–25.10.3, the floor cutoff and O(r^(-1/4))
   remainder, and the displayed first correction 25.10.4. The opening
   draft uses only the real-axis leading finite sum and its remainder;
   the apparent quotients in finer correction formulas require their
   removable-singularity treatment before evaluated use.

4. **NIST DLMF §4.13**, [Lambert W](https://dlmf.nist.gov/4.13).
   Defining identity and real/complex branches inspected during Ansatz
   Note01. Used for the candidate saddle inversion, without importing
   a field comparison or a global fixed-branch prescription.

5. **NIST DLMF §18.18(i)**,
   [Hermite expansions](https://dlmf.nist.gov/18.18#i).
   Equations18.18.6–18.18.7 and the following Gaussian-weighted L²
   completeness paragraph inspected during Note01. Used only for
   existence of a polynomial approximation; no effective degree or
   source-construction complexity bound is imported.

DLMF was retrieved 25 October 2026; the inspected site identifies version
1.2.8, released 15 September 2026. No artificial PDF copies were created.

## Repository inputs and status

- [Parent manuscript](../../manuscript/main.tex), especially 01,
  10–13, 14, 22–24, through Notes54–55.
- [Summary62](../../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md)
  and its Notes58–61 dependencies; no claim that the opening draft
  re-audits their full proof chain.
- [Parent overview](../../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
  and [parent progress](../../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md).
- [Ansatz Note01](../notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md).
- [Result index](../../../../../result-summaries/README.md), clusters
  11–13, and [avoid index](../../../../../avoid/README.md), including
  normalization, shared-premise review, cutoff/remainder and scope cautions.

The build record hashes identify files, not mathematical validity.
Inherited in-note and internal-review qualifications are preserved.


## AN01 continuation source check — 25 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, ansatz chat0001. Reopened the
primary DLMF5.11 sectorial log-Gamma/digamma statements and
DLMF25.10.3--4 (real RS remainder, first correction and removable
quotient). Polymath's exact formula (35), fixed-cutoff contours
(36)--(38), Theorem1.3 (23)--(24) and retained-C equation (69) were
rechecked. Proposition9.1 explicitly allows -10<=y<=10 but requires
its eventual x>=exp(C/t) for the two-carrier statement; this does not
pay the bounded t log X crossover. The finite-sum theorem's inspected
effective domain remains 0<t<=1/2, 0<=y<=1, x>=200. No negative-time
error theorem or arbitrary-width buffer is imported from it.
Note03 derives its negative-time real-axis estimate separately.


## AN02 continuation source check — 25 October 2026

Prepared for Edward Baker with LLM assistance, **gpt-6.1-sol, effort ultra**.
Rechecked DLMF25.10.3--4 (real corrected RS), 25.2.1 and25.2.8
(ordinary Dirichlet tail and Euler summation), and5.11 sectorial bounds.
Note04 supplies its own complex extension by a paid rectangle argument.
Also inspected Polymath v2 equations36--38 and Proposition6.2, including
all-real-sigma coefficient bounds54--57 and K+sigma>=2 at negative sigma.
The restricted sigma interval belongs to evolved Proposition6.3; it is
not a restriction of6.2. The broader positive-time buffer estimate in
Note04 is proved directly from the exact Gaussian source identity,
not imported from that restricted evolved theorem. The original Arias
paper's PDF access returned403; only Polymath's inspected primary
restatement is used in the optional contour consistency check.

## HDA-A02-AN01 source check — 25 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**. Rechecked Polymath v2's exact
zero-time equations36--38 and Proposition6.2 equations54,56 at sigma=1/2.
Note05 imports the arbitrary-positive-integer-K coefficients and explicit
Gamma((K+1)/2)(1.1/a)^(K+1) remainder, retaining exact M and the real
initial-value formula. The K-dependent constants are paid, rather than
treated as fixed. Only real initial sigma=1/2 is used, so the negative-
sigma qualification is not invoked. No evolved positive-time theorem
is imported at negative time. DLMF5.11 sectorial bounds support the
separate n-independent gamma-curvature factor and its growing-order
Cauchy estimate. No independent audit of the original Arias PDF or new
PDF download is claimed. [Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
and [Assessment04](../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md)
give the complete imported/derived distinction.

## HDA-A02-AN02 input scope — 25 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
recorded effort ultra**. Note06 uses the exact source identity, classical
RS input and sectorial gamma bounds already checked and recorded in
Notes04--05. No new external theorem or extension of an evolved
positive-time estimate is imported. The moving-T kernel, derivative,
tail and joining estimates are derived in Note06 itself. In particular
the T>=1 constants of Note05 are not assumed to hold at the new lower
endpoint. The separate future regulator packet points to parent Note28
JT26--33, retaining its exact named linear-arm center and actual
b_t sensitivity; it is not an executed extension of that result.


## Evolution-equation discussion reference — 25 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, recorded effort max**, ansatz chat0002.

**Heat Equation**, Stanford University Math 220B course handout.
The author and issue date are not identified in the inspected copy.
[Primary PDF](https://web.stanford.edu/class/math220b/handouts/heateqn.pdf).
Checked selected passages in Section 2.7, printed pages 32--35, covering
Duhamel's principle, whole-space heat convolution, and the bounded-data
estimate. This is background for
[Note08 EV2--3](../notes/08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md);
no chartwise, complex-strip or outer-carrier-relative stability theorem
is imported. Full reading and independent source-proof audit were not
performed. Retrieved 25 October 2026; reusable entry StanfordHeatDuhamel.

The public reading copy is outside Git:
/Users/Shared/szp-archive/heat-density-asymptotics/references/stanford-math220b-heat-equation-retrieved-20261025.pdf.
Size 260914 bytes; SHA-256
ccc97d89c36337a3b11897b2efc51c1b2ef8b89ed659ddb3b1fa4ffbac8e2d8c.
This identifies the retrieved bytes, not mathematical validity; the
public source remains the portable reference.

## HDA-A02-AN03 checked scope — 25 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
recorded effort ultra**, chat0003. Reopened the existing version-pinned
Polymath v2 primary HTML, equations36--38 and Proposition6.2, especially
54/56 at sigma=1/2 and K=1. These give the two retained RS coefficients
and initial remainder used in Note10 EC4--5. The coefficient C1 is named
by that classical construction; its size bound is not used to infer
derivatives, analyticity or endpoint parity. Keeping the real RS data
inside the bounded correction integral bypasses those unacquired inputs.
No negative-time evolved theorem or positive-time error is imported.
DLMF5.11 sectorial gamma inputs were reopened; Note10 derives its own
evolution correction, all-mode error and tails. Existing PDF provenance
above and in the parent catalog is retained; no new PDF or new article.

## HDA-A02-AN05 reused input scope — 25 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
recorded effort ultra**, chat0003. Note12 reuses only the previously
inspected real K=1, sigma=1/2 RS import of Notes05/10 and their sectorial
gamma inputs. It derives the endpoint-dependent kernel, population,
residual and tail estimates directly. No new external theorem, C1
derivative/endpoint identity, negative-time literature bound or PDF is
imported. Existing primary-source links and reading-copy provenance
remain canonical above.


## AN06 discussion and next-step source check — 26 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6-astra,
recorded effort max**, ansatz chat0004. Reopened the existing pinned
Polymath v2 HTML: exact Gaussian identity35, contour decomposition36--38,
initial RS Proposition6.2, and positive-time Proposition9.1. The latter's
two-arm estimate requires 0<t<=1/2, |y|<=10 and eventual x>=exp(C/t);
it does not supply [1/2,1] or arbitrary larger buffers by substitution.
DLMF5.11's sectorial gamma/digamma expansions were also reopened.
[Review11](../reviews/11_CURRENT_ANSATZ_AND_NEXT_STEPS_REVIEW_20261026.md)
uses these checks for normalization and scope. No new article, PDF,
coefficient regularity input or independent source-proof audit.

## Generalized-transform discussion — 26 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6-astra, recorded
effort max**, ansatz chat0004. These sources support the comparisons in
[Note15](../notes/15_GENERALIZED_TRANSFORMS_AND_HEAT_COMPONENT_HIERARCHIES_20261026.md).
They are contextual references, not imports of new heat-density estimates.
The source inspections were selective; no complete literature survey,
novelty claim, or independent proof audit is implied.

- **R. S. Ward**, *Infinite-Parameter ADHM Transform*, arXiv:2006.01459v2,
  26 July 2020; published in *Quarterly Journal of Mathematics* 72(1–2),
  407–415 (2021), DOI [10.1093/qmath/haaa054](https://doi.org/10.1093/qmath/haaa054).
  [Pinned primary HTML](https://arxiv.org/html/2006.01459v2).
  Checked Introduction and selected Sections 2–3, including the stated
  transform analogy, ADHM constraints/reconstruction (5)–(8), and the
  boundary-data interpretation (12)–(13). The setting is self-dual gauge
  fields with the stated geometric conditions. No theorem transfers to
  xi heat evolution. The HTML rendering displays a later automatic date;
  the pinned arXiv v2 date is 26 July 2020. The Durham metadata verifies
  the publication identity. The reading copy is listed in the manifest.
- **M. J. Ablowitz, D. J. Kaup, A. C. Newell, H. Segur**,
  *The Inverse Scattering Transform–Fourier Analysis for Nonlinear
  Problems*, *Studies in Applied Mathematics* 53(4), 249–315 (December
  1974), [DOI](https://doi.org/10.1002/sapm1974534249).
  Publisher abstract and bibliography inspected: it explicitly presents
  inverse scattering as an extension of Fourier analysis for its
  integrable evolution classes. Full text and specific scattering-data
  normalizations were not checked. No public accessible PDF was
  established in this inspection; no copy retained.
- **C. S. Gardner, J. M. Greene, M. D. Kruskal, R. M. Miura**,
  *Method for Solving the Korteweg-deVries Equation*, *Physical Review
  Letters* 19, 1095–1097 (6 November 1967),
  [DOI](https://doi.org/10.1103/PhysRevLett.19.1095).
  Publisher-indexed abstract/discovery only. Its initial-value method
  assumes sufficiently rapid approach to a constant at spatial infinity;
  no unrestricted or periodic-data statement imported. No accessible
  public reading copy established here.
- **M. J. Ablowitz, D. J. Kaup, A. C. Newell, H. Segur**,
  *Method for Solving the Sine-Gordon Equation*, *Physical Review Letters*
  30, 1262–1264 (18 June 1973),
  [DOI](https://doi.org/10.1103/PhysRevLett.30.1262).
  Publisher-indexed abstract and authors' institutional bibliographic
  records inspected. Used only for the inverse-scattering example.
  Detailed hypotheses and formulas were not checked; no public
  accessible PDF established in this inspection.
- **John A. Pople**, *Nobel Lecture: Quantum chemical models*,
  *Reviews of Modern Physics* 71, 1267–1274 (1 October 1999),
  [DOI](https://doi.org/10.1103/RevModPhys.71.1267).
  Inspected publisher metadata and the indexed official Nobel lecture
  passage headed “Correlated models,” printed p.253, on reference
  determinants, virtual orbitals and correlation approximations.
  [Official lecture PDF](https://www.nobelprize.org/uploads/2018/06/pople-lecture.pdf).
  Used only for the interpretation of approximation choices; no
  convergence, monotonicity, or accuracy theorem imported. Full reading
  was not performed. Official Nobel and APS PDF retrieval returned403;
  no local copy retained.
- **Ali Akbari, Mohammad Javad Hashemi, Risto M. Nieminen, Robert van
  Leeuwen, Angel Rubio**, *Challenges in Truncating the Hierarchy of
  Time-Dependent Reduced Density Matrices Equations: Open Problems*,
  arXiv:1204.4395, first submitted 19 April 2012.
  [Primary record](https://arxiv.org/abs/1204.4395).
  Abstract inspected: coupled one-/two-body evolution, higher-order
  closure, and compatibility/positivity issues in the studied fermionic
  dynamics. The conclusions are scoped to that setting. A v1 PDF was
  retained, but its full text was not read. No universal statement that
  every closure fails and no quantitative closure bound imported.
- **Michael Updike and Joshua Burby**, *A BBGKY-like Hierarchy for
  Quantum Field Theories*, arXiv:2310.10940v1, 17 October 2023.
  [Primary record](https://arxiv.org/abs/2310.10940v1).
  Abstract-only contextual discovery: hierarchies and finite closures
  for reduced density matrices. No Hamiltonian or approximation theorem
  imported. A v1 reading copy is retained; full text not read.
- **NIST DLMF §18.12**, [equation18.12.15](https://dlmf.nist.gov/18.12.E15).
  Checked the physicists' Hermite generating function. Note15 obtains
  its Gaussian moments by elementary differentiation. No orthogonality,
  completeness, convergence rate, or global basis claim is imported.
- **S. K. Donaldson and P. B. Kronheimer**, *The Fourier Transform and
  ADHM Construction*, chapter3 of *The Geometry of Four-Manifolds*,
  Oxford University Press (1990), pp.75–125,
  [publisher record](https://academic.oup.com/book/52942/chapter-abstract/421958992),
  DOI10.1093/oso/9780198535539.003.0003. Publisher-indexed abstract and
  title discovered; direct chapter access failed. Contextual terminology
  only, not an inspected theorem or an attribution of exact words to
  Atiyah. No PDF retained.

External PDF provenance, retrieval26 October2026, is recorded in
[the small manifest](TRANSFORM_REFERENCE_RETRIEVAL_20261026.json).
Files live under /Users/Shared/szp-archive/heat-density-asymptotics/references/.
Their hashes identify bytes, not mathematical validity. No third-party
PDF is stored in Git; all canonical public links remain above.


## HDA-A04-AN01 rechecked source scope — 26 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, recorded
effort ultra**, ansatz chat0005. Reopened D. H. J. Polymath, *Effective
approximation of heat flow evolution of the Riemann xi function, and a
new upper bound for the de Bruijn–Newman constant*, arXiv:1904.12438v2
(4 August2019), [Section4, equation35](https://arxiv.org/html/1904.12438v2#S4).
Checked the Gaussian identity/Fubini derivation and xi/8 normalization for
every t>0 and complex z. This exact identity needs no RH; no restricted
evolved finite-sum approximation theorem or zero theorem is imported.
Existing v2 reading-copy provenance is retained; no new PDF was downloaded.

Reopened [DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv), especially2.4.14–15:
analytic phase/amplitude, an interior stationary point with nonzero
quadratic term, appropriate convergence/end behavior and sector/branch
conditions underlie the usual fixed-parameter simple-saddle expansion.
That passage supplies context and coefficient parity, not uniformity for
this moving saddle or the complete canonical arithmetic/contour budget.
[Note17](../notes/17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md)
derives those estimates directly on its actual contour.

Reopened [DLMF5.11](https://dlmf.nist.gov/5.11), equations5.11.1–2 and the
finite-truncation error discussion in(ii). The log-Gamma/digamma expansions
have a fixed sector |arg p|<=pi-delta; holomorphic remainder/Cauchy on a
larger sector gives the finite derivative bounds used through alpha^(5).
No shrinking sector or all-order uniform constant is assumed. Inspected
passages only, not full-source proof audits; DLMF remains an online source.
Retrieval/check date26 October2026. Existing canonical bibliography entries
remain in use; no duplicate article/reference record or third-party PDF
was added to Git.


## HDA-A04-AN02 finite-derivative source check — 26 October2026

For Edward Baker with LLM assistance, **gpt-6.1-sol, recorded effort ultra**,
same ansatz chat0005. Reopened [DLMF5.11](https://dlmf.nist.gov/5.11#ii)
and [DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv). The previously recorded
fixed-sector digamma remainder, with Cauchy's formula on a larger sector,
supplies the finite bounds through alpha^(7) needed in Note18; SC11
exposes one constructive finite constant choice. No order-uniform theorem
or new moving-parameter expansion is imported from DLMF. The finite
interpolation/Bell remainder and complete canonical contour estimates
are proved in Note18 using the exact source already checked in AN01.
Existing canonical bibliography/PDF provenance is retained; no new article,
PDF download or full-source proof audit is claimed.


## AN03–AN04 checked-source scope — 26 October2026

For Edward Baker with LLM assistance, **gpt-6.1-sol, recorded effort ultra**,
same ansatz chat0005. Reopened the recorded [Polymath1904.12438v2](https://arxiv.org/html/1904.12438v2#S4)
exact equation35 and [DLMF5.11](https://dlmf.nist.gov/5.11#ii), plus
[DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv) as simple-saddle context.
Note19 derives indexed finite constants by Cauchy on a fixed larger sector;
its coefficientwise Gaussian residual identity is proved in-note, not
imported as a convergent or growing-order expansion. Note20 rechecks the
canonical fixed-endpoint proof on each new fixed compact[32,T] and its
stronger arithmetic bound; no restricted evolved Polymath approximation
is extended by citation. Existing bibliography and PDF provenance remain;
no new PDF, article record or full-source proof audit is claimed.
