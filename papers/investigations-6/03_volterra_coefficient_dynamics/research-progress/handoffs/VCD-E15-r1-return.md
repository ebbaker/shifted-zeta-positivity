# VCD-E15 r1 — shared-memory comparison return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note.** [Note 13][note] executes [E15 r1][request]
and [decision08][decision]. The four pinned hashes matched. The note
SHA-256 is `a0cf6bb5b2a70b0440c3e44471b92ad3d4be8166aee5246bfa1a3b52016d114f`.
One analytical proof and correction pass checked the endpoint signs,
the midpoint rescaling, the leading boundary propagation, and the
fixed-disk estimate. The proposed identity, coefficient, and bound
hold as written.

1. Iteration of the integrated equation on complex straight segments
   gives the unique entire fundamental matrix \(T_k\) and vector
   \(y_k=T_k e_0\) for arbitrary scalar entire \(k\). The two-height
   expression satisfies \((\partial_t-\partial_s)H_k=0\) with
   \(H_k(t,0)=f_k(t)\). Hence its midpoint readout is exactly
   \(f_k(z)\), the same model evaluated at full height. The omitted
   term uses kernel arguments out to \(z\). Setting \(k=0\) gives bare
   quadrature, with zero memory.
2. Ordered convolution gives
   \[
    f_k-f_\ell=-\beta_N(e_0^{\mathsf T}T_k e)*
       (k-\ell)*(e^{\mathsf T}T_\ell e_0).
   \]
   This transports the combined signed error before any norm bound.
3. The tridiagonal prefix fixes the first derivative of each boundary
   transfer at order \(N-1\). If \(q\) is the first derivative order
   of \(k-\ell\) with a nonzero value at zero, the scalar first differs
   at order \(2N+q\), with coefficient
   \((-1)^N(\prod_{j=1}^N\beta_j)(k-\ell)^{(q)}(0)/(2N+q)!\).
   For even normalized kernels a finite \(q\) is even and at least
   two. A flat entire difference gives identical responses.
4. With \(M,\epsilon,L\) as in the request, the fixed-disk absolute
   estimate is \(\|T_k(z)\|,\|T_\ell(z)\|\le e^{L|z|}\) and
   \(|f_k(z)-f_\ell(z)|\le \beta_N\epsilon |z|^2 e^{L|z|}/2\).
   Its constants depend on the fixed prefix and disk, and E04's
   moving-tail obstruction still applies.

At the exact theta \(k_N\), the common scalar is \(F_\lambda\).
E06 keeps its exact canonical \(b\) correction. The generic
comparison uses \(A,\beta_N,k,\ell\). Zero transfer still needs a
justified canonical kernel error, a modeled margin or contour
estimate, and degree or terminal control. The note records the
catalog screen and the distinct E07/E10 source classes. The equality
concerns a single kernel shared by both terms at a fixed prefix. Improved
kernels and distinct joint models remain outside that comparison.

[request]: VCD-E15-r1.md
[decision]: ../../brainstorm/notes/08_VCD_B04_SHARED_MEMORY_COMPARISON_DECISION_20261116.md
[note]: ../../notes/13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
