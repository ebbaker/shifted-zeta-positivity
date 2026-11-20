# Numerical evidence

20 November 2026. For Edward Baker with OpenAI Codex assistance, recorded gpt-6.2-astra/max.

[Certificate 01](01_BACKWARD_GAP_999_1000_20261120.json) gives outward intervals for the first complete gap, the signed log-gap drift on \([999,1000]\), and two endpoint comparisons. The [program](certify_backward_gap.py) uses Python 3 and python-flint 0.9.0. From this folder run

~~~sh
PYTHONDONTWRITEBYTECODE=1 python3 certify_backward_gap.py
~~~

It prints the JSON to standard output. The upper-anchor evaluator and saved root brackets are loaded from the Jacobi sibling and checked against their recorded SHA-256 identities. The time tilt and the matched comparison use anchor polynomial moments through order 28; complete quadrature of the endpoint field serves as a separate value check. Mathematical details, time orientation and tail payments are in the [finite section](../manuscript/finite.tex). [Opening packet](../research-progress/handoffs/AGC_EZ_E01_E02_REQUEST_R1_20261120.md) · [Inherited one-time certificate](../../01_jacobi_integer_hierarchy/numerics/08_LARGE_TIME_LOOP_RESUMMATION_20261120.json)
