# Sources, normalization checks, and verification ledger

12 September 2026. This is an AI-assisted targeted primary-source review and mathematical check, not independent specialist validation or an exhaustive priority search. The sources listed below provide specific mechanisms or normalization checks; no source is cited as a proof of an arithmetic bulk theory.

## Repository instructions and source state

No `AGENTS.md` was found in the repository ancestors or under `papers/`. `CONTRIBUTING.md` supplied the applicable verification rules: run controls for impossibility claims, search before claiming novelty, inspect printed equations, verify mathematical object types, and record what was checked. `LARGE_FILES.md` was read and applied. No claim of priority is made.

The four requested sources were read, together with the positive-factorizations status, round-4 review and even-sector report. The later review supersedes the manuscript's older statement that a shift-uniform odd factor is open; the even scalar and joint arithmetic completion remain open. This package does not edit that historical status.

Repository HEAD at the initial inspection was `12899d9b2bac0225a2c6e9316e7526a92c40c123`. There were pre-existing deletions of two top-level SUSY notes and untracked `archive/` and `brainstorm/` content. Those changes were preserved. The new package directory was absent at the initial inspection. Input file hashes and the exact downloaded PDF versions are recorded in [results/source-record.json](results/source-record.json).

## Primary literature actually consulted

| Source | Checked material | What it contributes; what it does not |
|---|---|---|
| [Witten, *Supersymmetry and Morse theory*, JDG 17 (1982)](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf) | Printed pp. 662 and 665, especially (9)–(12), rendered and inspected | Actual adjoint SUSY/Hodge algebra and deformed differentials. The relative channel differential, injection and metric in this package are independently specified adaptations, not attributed to Witten. |
| [Brüning–Lesch, *Hilbert complexes*, JFA 108 (1992), 88–132](https://doi.org/10.1016/0022-1236(92)90147-B) | Publisher abstract and bibliographic record; full paper not audited | Framework for closed complexes. No unexamined theorem from this paper is needed: closed range, quotient norm and adjoint properties used here are proved directly. |
| [Kwaśnicki–Mucha, *Extension technique for complete Bernstein functions of the Laplace operator*](https://arxiv.org/pdf/1707.02475) | arXiv v1, printed p. 28, Appendix A, (A.2)–(A.3), Theorems A.2–A.3, rendered and inspected; surrounding exposition searched | Positive measure-valued string extensions and orthogonal zero-trace/harmonic decomposition. Its Fourier transform is unitary; this package uses $1/(2\pi)$ with the background transform. The one-atom model is solved explicitly here. No inverse string coefficient for the full target is claimed. |
| [Tong, *Quantum Hall Effect*, chapter 6](https://www.damtp.cam.ac.uk/user/tong/qhe/six.pdf) | PDF page 5, printed p. 205, (6.7)–(6.11), rendered and inspected; current propagator discussion located | Explicit CS flatness reduction and chiral boundary action. The velocity is boundary data. A position-space scalar logarithm is not the target Fourier logarithm. |
| [Geiller–Jai-akson, *Extended actions, dynamics of edge modes, and entanglement entropy*](https://arxiv.org/pdf/1912.06025) | PDF page 15, printed p. 14, (4.14) and Hamiltonian/velocity discussion, rendered and inspected | Edge modes and the independent choice of boundary dynamics. No positive Weil norm or SUSY boundary Ward identity is supplied by this result. |
| [Kottos–Smilansky, *Periodic Orbit Theory and Spectral Statistics for Quantum Graphs*](https://arxiv.org/pdf/chao-dyn/9812005) | arXiv v2 header, printed pp. 8–9, (26), (27), (32), (35), (36), rendered and inspected; p. 10 convergence discussion read | Determinant/logarithm, primitive repetitions, and distinction between smooth density and orbit terms. The finite transport/residence model and its endpoint identities here are adaptations. The paper does not choose zeta's arithmetic graph. |
| [DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6), [DLMF 5.11](https://dlmf.nist.gov/5.11) | Partial-fraction formula and gamma asymptotic used with the background convention | Digamma differences and asymptotic normalization; no positivity of the full arithmetic form follows. |
| [Suzuki, *Weil's quadratic form via the screw function*, v2](https://arxiv.org/pdf/2606.09096v2) | Printed pp. 1–2 rendered and inspected: Weil functional, smooth-test criterion, and finite-interval operator formulation. Header says 17 August 2026; internal date says 18 August | Primary normalization/criterion check. The later report's broader reading of §§3–5 was consulted as local context, not treated as a fresh audit of every result in those sections. |

Searches followed the brainstorm's references into Hilbert-complex theory and quantum-graph primitive-orbit formulas. The related Connes–Consani spectral-triples paper was located through its publisher record and the later progress report; no numerical statement from it is used as a premise. This avoids treating mere shared vocabulary about cohomology or spectral triples as a positive-boundary construction.

The web screenshot endpoint was unavailable for the PDFs. Public primary PDFs were downloaded into a temporary audit directory, rendered locally with Poppler, and inspected. Third-party PDFs and page images are not included in the repository, in accordance with `LARGE_FILES.md`.

## Independent normalization check against the printed Weil functional

Suzuki's printed functional has the same prime weights and $j(t)=e^{-t/2}/(1-e^{-2t})$, but displays its contact normalization as $-(\log4\pi+\gamma_E)$, with the subtraction $e^{-t/2}$ inside the archimedean integral. For an autocorrelation with value $\|f\|^2$ at zero, converting that subtraction to the jump normalization changes the contact by

\[
2\int_0^\infty j(t)(e^{-t/2}-1)dt=\psi(1/4)-\psi(1/2).
\]

Since $\psi(1/2)=-\gamma_E-2\log2$, the resulting constant is exactly $\psi(1/4)-\log\pi=w_0$. The pole integrals of the autocorrelation are

\[
2\operatorname{Re}\left[\left(\int f(x)e^{x/2}dx\right)
\overline{\left(\int f(x)e^{-x/2}dx\right)}\right]
=2|C(f)|^2-2|S(f)|^2.
\]

The paired evaluations at $\pm\log n$ give the background's $T+T^*$ term. Thus no scale, pole, prime, or contact factor is imported from a paraphrased equation. Different conventions for which argument is conjugate-linear are reconciled by Hermitian polarization.

## Existing results materially used: what was verified

**Gamma tower and domain.** Re-completed the square at each frequency and derived (7)–(10) of the relative-complex note independently from the local differential. Rechecked the $a_k$ conversion using the digamma partial fractions. The summands are nonnegative; monotone convergence gives the diagonal tower and Cauchy–Schwarz its polarization. $B(\tau^2)$ differs from $\log(2+|\tau|)$ by a bounded function. Finite primes and pole amplitudes are bounded at fixed $L$, so the natural finite-interval domain is unchanged. The original weighted auxiliary-space closedness/density argument was read. New constructions state their own domains, including the failure of the raw infinite source to be a Hilbert vector.

**Pairwise obstruction.** Rechecked the grouped two-point Gram inequality $|c|^2\le\alpha\beta$, which permits replacing $c$ by $-|c|$. For the unit constant on $I_L$, direct overlap integration yields

\[
Q^\gamma[f]=w_0+{2\over L}\sum_{k\ge0}{1-e^{-a_kL}\over a_k^2}
+{32\over L}\sinh^2(L/4).
\]

Replacing the off-diagonal $R=2\cosh(t/2)-j(t)$ by $-|R|$ subtracts $(4/L)\int_0^L(L-t)R_+(t)dt$. The rational checker encloses the weaker comparison upper bound on $t\in[1/3,2/3]$ in $[-0.049480368641,-0.040946758100]$, with endpoints rounded outward here, and certifies that it is below $-1/25$. Read the explicit tail and rational exponential/logarithm bounds. The constant witness lies in the logarithmic domain and has smooth interior approximants there. The finite Schur comparison proof was also checked; no unconstrained continuum limit is inferred.

**First-prime stabilization and failed remainder.** For the unit linear input on $I_L$, integrate the product on its overlap to get $r_f(t)=1-3t/L+2(t/L)^3$, $0\le t\le L$. One exponential channel contributes

\[
I_a(L)={6\over La^2}-{24\over L^3a^4}
+e^{-aL}\left({6\over La^2}+{24\over L^2a^3}+{24\over L^3a^4}\right).
\]

This follows by integrating $2e^{-at}(1-r_f(t))$ on $(0,L)$ and $2e^{-at}$ on $(L,\infty)$. The odd pole square is retained. At $L=1$, add $-2c[1-3d+2d^3]$, $d=\log2,c=d/\sqrt2$, and compute the forced cap debit $c[1-(2d-1)^3]$. Reading the mass-tail estimates and replaying the rational check gives gamma $<-0.12$, full form $>0.26$, and debited remainder $<-0.58$. These are assertions on this input, not all-input positivity.

**Whole-line restriction.** Rechecked the proof at its precise topology. A full positive norm identity on all compact tests first implies RH by the criterion. The explicit formula then samples $\widehat f$ at real zero ordinates. For an isolated ordinate $\gamma_0$, let $f_N=N^{-1}e^{i\gamma_0x}\phi(x/N)$, $\widehat\phi(0)=1$. Its $L^2$ norm tends to zero, while the sampling vectors converge to the nonzero $\gamma_0$ coordinate: rapid Fourier decay and $N_\zeta(T)=O(T\log T)$ give a summable majorant. Consequently $Q[f_N-f_M]\to0$ but $Q[f_N]\not\to0$, contradicting closability. The contradiction concerns growing supports; it does not forbid the fixed-$L$ constructions in this package. No individual zero value is needed for any computation.

**Later status.** The round-4 even mean-zero estimate and scalar Schur reduction were read and their algebra checked; their checkers replayed. They are reported as prior restricted results, not new accomplishments. The current investigation does not depend on the unresolved even scalar being positive.

## Fresh checks and limitations

[results/prior-replay/RUN_RECORD.json](results/prior-replay/RUN_RECORD.json) records successful replay of rounds 1–3, the optimized-Python rejection control, and both round-4 programs. Temporary copies were used and historical diagnostic hashes were checked unchanged. Passing a checker does not validate an omitted analytic reduction; the reductions above were separately inspected.

[results/model-diagnostics.json](results/model-diagnostics.json) records the new channel, cohomology, actual logarithmic-delay, coherent-deformation, and failure-control diagnostics. At quadrature orders 64 and 128 the gamma channel polarization errors are below $4\times10^{-14}$. Actual-log delay identity errors are below $2\times10^{-15}$. The deformed tower's first-variation finite-difference discrepancies are below $3\times10^{-10}$; the residual Fourier check is compared with its explicit finite-mass tail bound, not with zero truncation error. These are floating-point observations, not interval-certified theorems.

No target matrix was diagonalized, no zeta zeros were input, and no large sweep was performed. Eigenvalue computations in the small checker are controls on independently defined finite toy Hamiltonians and isolated prime matrices only. Formal proofs of the new infinite-dimensional domain statements and kernel identities would benefit from specialist review.
