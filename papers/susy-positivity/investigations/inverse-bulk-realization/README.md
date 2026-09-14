# Inverse bulk realization of the localized Weil form

14 September 2026. Continuation after the canonical semilocal pairing
comparison and the user's clarification of the research objective.

The objective is to construct an independently positive bulk system and
fit its complete boundary pairing to the localized Weil form. The present
task is exact model selection and matching. Estimating successively more
complicated errors in a fixed positive completion is not the continuation
strategy.

The paper's scope is a forward conditional reduction: a constructively
credible field theory, together with an exact boundary matching theorem,
would imply RH. A Yang–Mills-to-RH mapping is a proposed case to investigate.
The speculative reverse RH-to-Yang–Mills direction is outside this paper.

[Latest calculation: gauge transfer and the first-prime boundary test](GAUGE_TRANSFER_TEST.md)
compares Wilson-loop winding with transfer evolution, constructs a positive
disk model for the gamma masses and prime returns, and computes two
explicit preparations. One fails by a cusp at the prime delay; a coherent
repair removes it but leaves the independent contact problem. These are
scoped model tests, with no full Weil matching identity.

[Analysis](ANALYSIS.md) contains:

- a scoped obstruction to exact constant subtraction by finitely many
  rational feedback channels built from one positive reference operator;
- an exact positive-action refinement of the gamma tower into integer
  branches, using the classical digamma multiplication formula;
- a proposed common-field junction construction, with explicit first-prime,
  repeated-prime and two-prime matching requirements.

The obstruction has a written algebraic proof. The gamma refinement is an
exact reindexing of a known positive tower, not a claim of novelty for the
multiplication formula. No junction satisfying the full Weil identity has
yet been constructed, and positivity at arbitrary support remains open.

The [exact checks](check_matching.py) verify the finite algebra underlying
the refinement, its composition, and the elementary feedback identity.
The [record](checks.json) is not an analytical proof certificate.

Run from this folder:

    python3 check_matching.py
    python3 check_gauge_transfer.py

Related material:

- [Shared framework](../../PROGRAM_OVERVIEW.md)
- [Ground-state investigation](../arithmetic-ground-state-geometry/README.md)
- [Prime return channels](../arithmetic-ground-state-geometry/notes/16_PRIME_RETURN_CHANNELS.md)
- [Collective feedback](../arithmetic-ground-state-geometry/notes/17_COLLECTIVE_FEEDBACK_AND_COMPACT_DEFECT.md)
- [Earlier brainstorm assessment and revised priority](../../brainstorm/ASSESSMENT.md)
- [Finite-response novelty assessment](../../manuscripts/finite-response-weil-positivity/EVALUATION.md)
