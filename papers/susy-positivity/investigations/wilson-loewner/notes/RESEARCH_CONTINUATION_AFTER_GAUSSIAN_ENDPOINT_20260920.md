# Continuation after the Gaussian endpoint-response obstruction

20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: unavailable; not exposed in this session.
Status: internal research handoff; specialist review remains outstanding.

## Result to carry forward

The [new calculation](GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md)
tests a flavor-neutral Gaussian pairing interaction on the two canonical
lowest scalar modes, followed by a single charged endpoint. This coupling
is specified by a stable Hamiltonian before making the arithmetic comparison.
It is a spatially nonlocal boundary preparation with a positive ordinary
Hilbert norm; a local supersymmetric boundary realization is not established.

Its actual unit-norm response is

\[
G_g(u)=(1-q)^2\frac{e^{-u/2}}{(1-qe^{-u})^2},\quad
q=\tanh^2\eta,\quad \tanh(2\eta)=2g,\quad |g|<1/2.
\]

Thus it excites all protected flavor-one composites at energies \(k+1/2\)
with weights \((1-q)^2(k+1)q^k\). The elementary endpoint's Bose factor
is essential. Even after an extra, comparison-only projection to even
\(k\geq2\), no coupling and common normalization gives unit weights:
successive equal-weight tests require both \(q^2=3/5\) and \(q^2=5/7\).

Every finite-norm member is regular at \(u=0\). In the gap-closing limit
the normalized response vanishes at fixed positive \(u\); the nonzero
unnormalized boundary distribution has a \(u^{-2}\) singularity. The target
\(C_{\rm omit}=e^{-5u/2}/(1-e^{-2u})\) has a \(u^{-1}\) singularity.
The heat regulator and the precise convergence sense are given in the note.

This is a scoped obstruction to the specified Gaussian endpoint. It does
not prove that no protected observable can ever work, or that arbitrary
Gaussian constructions with extra spectator species and different endpoints
have the same weights. Those would be new physical proposals, not repairs
one may silently make to this one.

## Recommended next decision

Do not expand this failed test into an interacting Wilson calculation.
Seek specialist scrutiny of the fixed-representative/Hodge distinction and
the physical interpretation of the proposed boundary operations before
promoting these research notes into the manuscript.

A new localization proposal should proceed only when its action or boundary
condition independently fixes the observable, symmetry selection and
ordinary-adjoint matrix elements. Replacing the endpoint by a function of
occupation number chosen to cancel \(\sqrt{k+1}\), or adding the parity
filter merely because arithmetic needs it, is an inverse fit. A favorable
counting character remains insufficient. If no independently justified
physical input is available, record that limit and keep the direct
arithmetic continuation as the next bounded task.

## Independent arithmetic continuation

Read
[RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md](../../critical-path/notes/RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md)
before doing that task. The all-input EMA anchor remains internally certified
and awaits specialist review. At \(L=1/2,h=1/20,\omega=10^{-3}\), the scalar
bound has \(55<\|Y\|/\delta<72\), with \(\delta=0.000049998\).
The finite cumulative quotient near 0.802 is not an all-input upper bound.

The queued calculation is an energy-weighted bound for cumulative coupling
with both omitted input spaces controlled. Keep the output-side reflection,
the nonzero metric cross blocks unless using an energy-orthogonal split,
the signed pole states, the complete beta history and the fixed local
coefficient. Endpoint memory must cross the join. Do not turn an
instantaneous form lower bound into an operator exponential through the
nonnormal flow. Auxiliary smoothing loss and averaging variance are not
arithmetic positivity.

## Copyable next-session prompt

Continue in /Users/ebbaker/Documents/shifted-zeta-positivity using the current
checkout, preserving all uncommitted work, the version-0.5 manuscript pair
and every dated snapshot. Read applicable AGENTS.md instructions and
LARGE_FILES.md first.

Read wilson-loewner/notes/GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md
and its source audit in reviews/review_codex_endpoint_sources_20260920.md,
under papers/susy-positivity/investigations. The neutral Gaussian mode
interface can excite infinitely many protected composites, but a single
charged endpoint fixes weights proportional to (k+1)q^k. It fails the
omitted-channel test even after granting an additional parity/ground-state
projection. Its unnormalized singular limit has a double pole. This is an
internal result, not a specialist review or a universal physical no-go.

Unless a new independent physical action/observable is supplied, continue
the separate bounded arithmetic task described in
critical-path/notes/RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md.
At L=1/2, h=1/20, omega=10^-3, derive an energy-weighted all-input upper
bound for normalized cumulative coupling, retaining endpoint memory and
controlling both omitted input spaces. The finite quotient near 0.802 is
diagnostic only, and the scalar sufficient estimate fails. If the proposed
energy metrics still do not close the estimate, quantify the obstruction
and identify the uncontrolled block. Do not replace the task with a
certificate only on the enlarged interval.

If instead a concrete new physical candidate is supplied, compute its actual
ordinary-adjoint response before comparing arithmetic. Specify locality,
boundary conditions, charge and projection scope, normalization and any
singular regulator. Do not flatten weights or choose a generating function
to fit the target. Keep the signed arithmetic pole and fixed local finite
part separate from positive correlators. Request missing source material
before relying on it.

Write a new dated note and reproducible small records in the designated
folders. Preserve historical conclusions as dated; identify actual model
and only an exposed effort setting. Distinguish analytical arguments,
finite diagnostics, certificates and unresolved physical assumptions.
