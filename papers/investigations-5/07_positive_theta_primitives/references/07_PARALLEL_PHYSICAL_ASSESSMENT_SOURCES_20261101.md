# Sources checked for the six physical assessments

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; coordinator **gpt-6-astra / ultra**. Selected passages only; no novelty survey or full-paper assessment.

## Tao2010GaussianEnsembles

Terence Tao, *254A, Notes 6: Gaussian ensembles*, online lecture notes, 23 February 2010. [Primary source](https://terrytao.wordpress.com/2010/02/23/254a-notes-6-gaussian-ensembles/), Section 1, equation (1), inspected by MC03 and the coordinator on 1 November 2026. The ordered GUE eigenvalue density has a Gaussian factor and a squared Vandermonde, with denominator `(2π)^(n/2) 1! ... (n−1)!`. For three ordered coordinates its integral is `2(2π)^(3/2)`.

This identifies the physical name and checks the normalization of the local model in [MC03 Return01](../01_jensen/01_mellin_curvature/03_connected_mellin_response/notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md). The theta local limit and the needed Gaussian moments are derived in that return. No signed-theta universality theorem, global moment convergence, effective threshold or response inequality is imported. This is an online reference; no artificial PDF was made. The existing four physical-source records retain their original inspection limits.

## ChabaudMarkhamGrosshans2020

Ulysse Chabaud, Damian Markham and Frédéric Grosshans, *Stellar representation of non-Gaussian quantum states*, Physical Review Letters 124, 063605 (2020), DOI [10.1103/PhysRevLett.124.063605](https://doi.org/10.1103/PhysRevLett.124.063605). Read [arXiv:1907.11009v3](https://arxiv.org/pdf/1907.11009v3), submitted 17 April 2020 (PDF dateline 20 April 2020). MC05 and the coordinator inspected p.2 Definition 1 and equations (1)-(3), fixing the factorial convention and conjugation in the Husimi function, and p.3's unitary squeezing generator.

[MC05 Return01](../01_jensen/01_mellin_curvature/05_schur_toda_structure/notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md) constructs its actual theta state and proves its normalizability separately. The source supplies representation conventions, not theta zero alignment or a Mellin estimate. Finite-rank factorization and state-engineering theorems are not imported for theta. The proposed `a²` source deformation is not unitary squeezing. A public reading copy is archived outside Git with [receipt](PDF_RECEIPTS_PARALLEL_PHYSICS_20261101.json); the hash identifies the file, not the validity of its mathematics.

## Witten1982Morse

Edward Witten, *Supersymmetry and Morse Theory*, Journal of Differential Geometry 17 (1982), 661–692, DOI [10.4310/jdg/1214437492](https://doi.org/10.4310/jdg/1214437492). [IAS primary PDF](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf). MC06 inspected indexed primary passages around pp.664 and 677; coordinator web open returned a 32-page PDF with no readable text. This is background inspection, not a full reading or imported localization theorem. Retrieval status is recorded in the [receipt](PDF_RECEIPTS_PARALLEL_PHYSICS_20261101.json).

[MC06 Return01](../01_jensen/01_mellin_curvature/06_topological_field_theory/notes/01_PROTECTED_OBSERVABLE_FEASIBILITY_RETURN_20261101.md) explicitly constructs the circle de Rham complex and proves the relevant spectral cancellation, degree-fugacity identity and commutator obstruction. The result applies to that model and its specified Q-closed insertions; it does not exclude topological or cohomological approaches generally.
