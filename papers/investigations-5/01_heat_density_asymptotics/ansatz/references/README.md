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
