# Numerical evidence

20 November 2026. For Edward Baker with OpenAI Codex assistance, recorded gpt-6.2-astra/max.

[Certificate 01](01_BACKWARD_GAP_999_1000_20261120.json) gives outward intervals for the first complete gap, the signed log-gap drift on \([999,1000]\), and two endpoint comparisons. The [program](certify_backward_gap.py) uses Python 3 and python-flint 0.9.0. From this folder run

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 certify_backward_gap.py
~~~

It prints the JSON to standard output. The upper-anchor evaluator and saved root brackets are loaded from the Jacobi sibling and checked against their recorded SHA-256 identities. The time tilt and the matched comparison use anchor polynomial moments through order 28; complete quadrature of the endpoint field serves as a separate value check. Mathematical details, time orientation and tail payments are in the [finite section](../manuscript/finite.tex). [Opening packet](../research-progress/handoffs/AGC_EZ_E01_E02_REQUEST_R1_20261120.md) · [Inherited one-time certificate](../../01_jacobi_integer_hierarchy/numerics/08_LARGE_TIME_LOOP_RESUMMATION_20261120.json)

**Signed mean correction, 20 November 2026.** Prepared for Edward Baker with OpenAI Codex assistance, gpt-6.2-astra/ultra lead and gpt-6.2-sol/ultra execution and replay. From this directory with python-flint 0.9.0, each command prints one small certificate.

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 certify_ez_signed_path.py
PYTHONDONTWRITEBYTECODE=1 python3 certify_ez_join.py
~~~

The [first receipt](03_SIGNED_PATH_999_1000_20261120.json) compares the signed transport and the all-28-moment direct endpoint on [999,1000]. The [joined receipt](04_JOINED_PATH_984_1000_20261120.json) tests the same cancellation on the longer connected path from 1000 to 984, reusing the first receipt. [Derivation](../notes/02_EZ_SIGNED_DIVIDED_DIFFERENCE_20261120.md) · [Separate replay with hashes](../reviews/02_EZ_ANALYTICAL_SCOPE_AND_REPLAY_20261120.md) · [Analytical limit of this chart](../notes/04_EZ_HALF_LINE_PHASE_OBSTRUCTION_20261120.md).

The current [production record 06](06_INTEGRATED_MANUSCRIPT_BUILD_20261120.json) identifies the integrated analytical manuscript, its source hashes and the checked PDF. [Record 05](05_ZERO_LOCATIONS_MANUSCRIPT_BUILD_20261120.json) identifies the preceding revision, and record 02 the opening draft. The finite computations in the manuscript retain their original records.
