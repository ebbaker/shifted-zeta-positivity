# References for the readout-connection discussion

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and reasoning effort are
unavailable in this chat's recorded configurations.

Limited passage inspection for [discussion24](../notes/24_VCD_READOUT_LEMMA_SEARCH_DISCUSSION_20261116.md),
not a full literature review or an acquired B07 lemma. Retrieval date for
all entries: 16 November 2026. Bibliography: [induction.bib](induction.bib).

## Teschl: the spectral-variable distinction

Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear
Lattices*, Mathematical Surveys and Monographs 72, AMS, 2000.
[Authorized author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf),
version 24 August 2017; [author's book page](https://radon.mat.univie.ac.at/~gerald/ftp/book-jac/index.html).
Checked §4.1, equations (4.1)–(4.4), printed p.75, and Theorem4.5,
equations (4.25)–(4.27), p.79. The former introduces Prüfer variables
for real solutions of the Jacobi eigenvalue equation, using negative
off-diagonal coefficients; the latter gives real, simple, interlacing
polynomial zeros and identifies finite spectra. The sign convention can
be changed by an alternating diagonal gauge. These are statements in the
spectral variable, not zeros of the exponential readout in Fourier height.
Useful background; no transfer theorem to the present readouts was found
in these inspected passages.

## Romanov: a precise phase-system hypothesis

Roman Romanov, *Canonical systems and de Branges spaces*,
[arXiv:1408.6022v1](https://arxiv.org/abs/1408.6022v1), 26 August 2014;
[PDF](https://arxiv.org/pdf/1408.6022v1).
Checked introduction and §3.2, equations (12)–(15) and Proposition4,
pp.14–15. A locally integrable positive semidefinite Hamiltonian generates
the displayed Hermite–Biehler property, except for the specified degenerate
rank-one Hamiltonian with the chosen initial column. The positive integral
identity explains the phase mechanism. No such canonical-system
realization of the actual Fourier readouts has been established here.
Representing the source Jacobi spectral problem does not establish that
identification. This is a possible tool after a faithful identification,
not an applicable theta zero theorem.

## Dimitrov–Xu: a Fourier-side analogy with an equivalence warning

Dimitar K. Dimitrov and Yuan Xu, *Wronskians of Fourier and Laplace
Transforms*, [arXiv:1606.05011v1](https://arxiv.org/abs/1606.05011v1),
16 June 2016; [PDF](https://arxiv.org/pdf/1606.05011v1).
Checked Theorem1.1, p.2, and §2.1, Theorems2.5–2.6, p.5.
These relate derivative Wronskians of a single transform to correlation
kernels, with integrability/moment hypotheses; Theorem2.6 states a
positive-definiteness conclusion. Positive definiteness is not pointwise
positivity. Theorem1.1 is explicitly an RH-equivalent translation-density
criterion. No normalization or theorem is imported into a proof here;
the paper has not been audited. The inspected passages do not compare
successive Gaussian-quadrature transforms. This is a secondary analogy,
not evidence for the missing degree step.

## Chen–Ismail: bibliographic lead only

Yang Chen and Mourad E. H. Ismail, *Ladder operators and differential
equations for orthogonal polynomials*, Journal of Physics A: Mathematical
and General 30(22) (1997), 7817–7829,
[DOI:10.1088/0305-4470/30/22/020](https://doi.org/10.1088/0305-4470/30/22/020).
Bibliographic data crosschecked in the references of the
[AMS article DOI:10.1090/proc/16348](https://doi.org/10.1090/proc/16348).
The publisher page was blocked by robots.txt. The primary paper's
passages and hypotheses were not inspected; no theorem is imported.
Retained as a lead for source-score/differential relations, whose
connection to the actual finite Fourier readout would still need proof.

## Reading-copy status

Online PDF passage inspection succeeded for Teschl, Romanov and
Dimitrov–Xu. Direct authorized downloads to the external temporary
directory `/private/tmp/szp-vcd-readout-references-20261116/` each failed
DNS resolution. No local PDF, byte count or hash is claimed. Third-party
PDFs were not placed in the repository. The Chen–Ismail access restriction
was not bypassed.
