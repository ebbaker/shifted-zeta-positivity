# Next session after the signed two-prime comparison

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and configured reasoning effort not
exposed. Internal separate-agent same-model audits are complete; these
are not independent specialist reviews.

## Current result

The bounded work in [the previous handoff](NEXT_SESSION_ALL_WINDOW_HANDOFF_20261003.md)
is complete. On the original three-moment complex source class at L=6/5,

    Q[F] >= (3/2000)||F||²,
    |K_{2,3}[F]| <= 3458||F||²,
    Q[F] >= (3/6916003) B_{2,3}[F].

These are full-source bounds, not finite-family tests. They cover smaller
windows by inclusion with the same prime representation {2,3}. The previous
L=1 result for {2} remains separate and unchanged. The full signed
certificate passed at 192 and 256 bits, and the first-window certificate
was replayed once with all mathematical fields matching.

Read:

1. [Outcome and remaining obligation](ALL_WINDOW_EXTENSION_OUTCOME_20261003.md).
2. [Scaling and relative compactness audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md).
3. [Certificate package](../numerics/all_window_extension_20261003/README.md) and
   [implementation review](../reviews/ALL_WINDOW_EXTENSION_CERTIFICATE_REVIEW_20261003.md).
4. [Preflight](ALL_WINDOW_EXTENSION_PREFLIGHT_20261003.md) for the fixed budget
   and rejected capped comparison.

## Two changes in the available method

**Signed frequency compression.** The positive-part bound failed already
at L=6/5. Its worst directions have positive actual-Q diagnostics; the
failure is explained by discarded positive energy. Retaining signed
`lambda-q_L` on a certified frequency band fixes this bounded comparison.
The smooth integrand also permits an O(h²) midpoint error bound. The
successful parameters are lambda 1/2, T 100, rank 100, nodes 30000, with
matrix cap 249/500 and error cap 1/2000. Total actual error bound is below
0.000320680. The two actual primes are 2 and 3; 4 is inactive.

**Relative compactness for any finite set.** The two-prime unweighted
correction kernel need not be proved Hilbert–Schmidt. K is bounded on the
source space, while the positive closed source operator B has compact
resolvent and a positive fixed-window gap. Hence B^(-1/2) is compact and
H=B^(-1/2)KB^(-1/2) is compact for every fixed finite S,L. The audit
supplies the domain, smooth neutral core, positivity and compactness
arguments. It gives no uniform or effective gap as S,L grow.

## What should be pursued next

Use this result to pursue a quantitative all-window mechanism, rather
than automatically raising L. The exact target remains positivity on an
unbounded sequence of nested windows with the same three constraints.
Constants may decay; no common positive L2 gap is needed.

A focused next analytic task is an effective relative spectral split.
If an actual B-spectral complement lies above Lambda and B>=beta I,

    ||H11|| <= k/Lambda,
    ||H01|| <= k/sqrt(beta Lambda).

These now hold for every finite prime set without a kernel-compactness
lemma. The missing work is to certify the spectral split and finite block,
control mixed terms relative to its margin, and replace transport-based
constants when too pessimistic. With `H11<=vartheta I< I`, the sufficient
comparison is `I-H00-H01 H10/(1-vartheta)>=0`. Dropping mixed terms is invalid.

The alternative arithmetic task is a theorem controlling the signed
compressed band plus its complete complement for unbounded L. The current
cutoff still requires gamma(T)>lambda+C_L, with C_L on the scale e^(L/2);
preserving positive energy has **not** removed this cost barrier. The
exact centering identity Q=Gamma+J-E and finite-window null multiplier
in §5 of the scaling audit remain useful reorganizations, but no useful
signed prime-discrepancy bound has been established. A continuation
algorithm must prove its successful window steps cannot accumulate.

Choose one bounded test only after its analytic purpose and cost/error
preflight are written. The existing script deliberately rejects L>6/5;
preserve this package and develop any further experiment separately.
Do not infer RH, B>=K_plus, or place monotonicity from the new comparison.

## Reproduction and preservation

Repository: `/Users/ebbaker/Documents/shifted-zeta-positivity`.
HEAD remains `c943006b5003dad7ac48afc7689e7273f30c267a`; existing and new
research notes/packages are uncommitted. Inspect status and preserve the
working tree. No clean checkout/reset, commit, push, or manuscript revision
was performed in this continuation.

New certificate generator SHA-256:
`6334c0a3cbda39458e30c4abf1a339b5a642424b421a034b83f9615eabfca4c2`.
The two precision records bind this source; replay_check.json verifies
strict caps and scalar enclosure overlap. Hashes establish input identity,
while outward comparisons establish the mathematical claims.

The old generator hash remains
`d4285411922142e366be60ac0ca103cc4ba4a654c551e34e3b43fa2096d17b38`.
The manuscript hash remains
`f48309c50261d01b46023c6255c10ad8e784f8f92329c1357b91e11f9e293fc8`.
The inherited prolate record and generator binding were checked; the
earlier outward archimedean gap was reused, not rerun this session.

Certificate runtime discovered here: Python 3.10.0 with python-flint 0.9.0,
FLINT 3.6.0, using PYTHONPATH=/private/tmp/sonin-moment-python-deps. The
temporary path is not a durable dependency guarantee. Floating diagnostics
used separate Python 3.12.14 with NumPy 2.5.3/SciPy 1.17.1. Follow LARGE_FILES.md:
source and small records belong in Git, regenerated matrices do not.
No large derived arrays were saved. The ChatGPT synced reference mirror
remains read-only. No draft snapshot directory was created.
