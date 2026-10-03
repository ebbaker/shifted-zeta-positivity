# Next session handoff for all-window Sonin comparisons

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. This is a continuation brief. Established statements below have internal same-model audits, not independent specialist refereeing; proposed global strategies are identified separately.

## Task for the next session

Place the next certified comparison into a plausible all-window proof strategy. First audit how the length-one certificate scales and identify the estimate that would have to hold for arbitrarily large windows. Then carry out one bounded extension, provisionally to L=6/5, only after that context and its cost/error budget are explicit. The deliverable is a supported next comparison or a precise obstruction in the method, together with the remaining all-window theorem obligation. Do not substitute an unbounded numerical sweep for that obligation.

The current session did not run a comparison beyond L=1. It produced the [all-window strategy note](ALL_WINDOW_STRATEGY_20261003.md), including an exact continuous-prime centering identity, potential relative-energy estimates, and limits of continuation.

## Repository and preservation

- Local repository: `/Users/ebbaker/Documents/shifted-zeta-positivity`.
- Investigation: `papers/investigations/sonin-critical-boundary`.
- Baseline HEAD inspected: `c943006b5003dad7ac48afc7689e7273f30c267a`.
- The newer resonance notes, relative-comparison notes, two numerical packages, and audits are currently uncommitted; the investigation README is modified. The baseline commit alone does not contain them. Use the existing working tree, inspect its status first, and preserve its untracked files. Do not reset or replace it with a clean checkout of the baseline.
- The ChatGPT project mirror is `/Users/ebbaker/.codex/.chatgpt-projects/g-p-6a90684bbcb881918a5a1f5740bfbc65`. Everything under its `sources/` is read-only synced reference material.
- Follow repository `LARGE_FILES.md`: keep source code and small records, regenerate matrices outside Git, and do not add third-party PDFs. New derivations go in `notes/`, numerics in `numerics/`, audits in `reviews/`. Include model and effort metadata honestly; if unavailable, say so.
- The manuscript has not been revised for the resonance obstruction or the new local comparison. Its SHA-256 is `f48309c50261d01b46023c6255c10ad8e784f8f92329c1357b91e11f9e293fc8`. Do not create draft snapshot folders; use the existing concise draft-history convention for future commit milestones.

## Read first

1. [Completed local outcome](REVISED_B_LOCAL_OUTCOME_20261003.md).
2. [All-window strategies](ALL_WINDOW_STRATEGY_20261003.md), especially the quantifiers, centering identity, and scaling barriers.
3. [Local arithmetic coercivity proof](LOCAL_COERCIVITY_LOW_BAND_20261003.md).
4. [Closed source form and relative comparison](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md).
5. [Certificate README](../numerics/local_weil_gap_20261003/README.md), [generator](../numerics/local_weil_gap_20261003/certify_local_weil_gap.py), and [audit](../reviews/REVISED_B_CERTIFICATE_REVIEW_20261003.md).
6. [Finite Euler identity](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md) for conventions, actual transported metric, and signs. Its historical rank-one proposal is superseded by the [translated resonance obstruction](FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md).

Use the investigation README as the full index. Older continuation files contain retired proposals and should not be treated as the current plan.

## Conventions and established status

Use Fourier transform Fhat(t)=integral F(x)e^(-itx)dx and inverse measure dt/(2pi). On I_L=(-L/2,L/2), the source class is smooth, compactly supported, complex-valued F satisfying

\[
\int F=\int e^{x/2}F=\int e^{-x/2}F=0.
\]

Equivalently F=(-d²/dx²+1/4)h with compact smooth h of the same support and integral h=0. The three conditions stay fixed as L grows. Both parity sectors and complex polarization must remain.

For a finite prime set capturing all active primes, the audited identity is

\[
Q[F]=B_{S,1/2}[F]-K_{S,1/2}[F],\qquad
B_{S,1/2}[F]=\|C_F\Pi_S\|_{\mathrm{HS}}^2\ge0,
\]

with the independent correction

\[
K[F]=2\Re\operatorname{Tr}\bigl(C(I-C^2)^{-1}T X\bigr),
\quad X=P a_e(D)\chi.
\]

The exact inverse compressed metric is essential in the transported projection. A compression of C² is not the square of the compressed C. No separately divergent half-line traces may be introduced.

The translated two-packet argument produces positive K on prepared mean-zero sources at L=1 and proves infinite positive index in both parities. Thus K<=0 and domination by finitely many moment penalties are false. This does not refute K<=B. For normalized narrow packets, K is asymptotic to a positive constant times their width while Q grows logarithmically; see [packet scale](TWO_PACKET_WEIL_SCALE_20261003.md).

The completed first-window result is

\[
Q[F]\ge\frac9{100}\|F\|_2^2,\qquad
|K[F]|\le772\|F\|_2^2,
\quad
Q[F]\ge\frac9{77209}B[F]\ge\frac{B[F]}{9000}.
\]

It covers the entire stated source class at L=1, not just a finite test family. The relative comparison follows from the arithmetic lower bound and the independent correction norm bound. The revised term B_new=B/9000 has nonnegative remainder (8999/9000)B-K. The unweighted positive-part domination B>=K_plus remains unproved.

The bound for K uses the exact source factorization

\[
X_F=P C_F^*1_{I_L}C_F\chi,
\quad \|X_F\|_1\le\frac L2\|F\|_2^2,
\quad |K[F]|\le\frac{Lc}{\sqrt g}\|F\|_2^2.
\]

At L=1, g=(17-12sqrt(2))*57/10^6 and c=sqrt(1-g) give c/sqrt(g)<772. The inherited archimedean gap was freshly replayed. The closed-source note proves fixed-window positivity of B and compactness of its relative correction in the one-prime setting. Extension of the compactness proof to multiple primes needs explicit justification.

## Certificate and reproduction

The successful low-band certificate uses lambda=1, T=46, 46,000 midpoint cells and 40 Legendre coordinates. It projects out the full analytic moment functions before truncating. Arb/Acb LDL proves the finite matrix below 0.9 I. Full-source truncation plus integration error is below 0.008253, leaving the conservative Q gap 0.09.

Generator SHA-256: `d4285411922142e366be60ac0ca103cc4ba4a654c551e34e3b43fa2096d17b38`.
Both `certificate_192.json` and `certificate_256.json` bind this exact source; `replay_check.json` and `inherited_gap_replay.json` record the checks. Hash matching identifies input versions, while the outward inequalities establish the claims.

The certificate needs Python and python-flint; the recorded runtime is Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0. From the certificate folder:

```sh
python3 -B certify_local_weil_gap.py --bits 192 --output /tmp/local-weil-gap-replay.json
```

In the originating environment, python-flint was available to system Python through `PYTHONPATH=/private/tmp/sonin-moment-python-deps`; that temporary path is not a portable dependency guarantee. Discover available runtimes in a fresh environment rather than assuming it survives. The NumPy/SciPy pilot used a separate Python 3.12 runtime. Do not mix incompatible extension builds.

The [source-space pilot](../numerics/revised_B_source_pilot_20261003/README.md) contains floating B_d/Q matrices summarized by small records, with unresolved state truncation and quadrature errors. It does not certify B>=K_plus and is not an input to the successful certificate. A finite state trace is compact as a source form, not necessarily finite rank; it cannot alone dominate a positive multiple of the identity on the entire source space.

## The global question to settle before extending

Write down the intended all-window theorem explicitly. It is enough to prove Q>=0 on an unbounded sequence of nested windows. The constants delta_L or theta_L may decay; no common positive L2 gap is required. A proof for finitely many windows is not a proof for that sequence. Adaptive steps must be shown to reach arbitrarily large L rather than accumulating at a finite endpoint.

The present absolute-amplitude frequency cutoff scales badly. Let C_L=2 sum_(p^m<e^L) log(p)p^(-m/2). Its sufficient cutoff requires gamma(T)>lambda+C_L. C_L grows on the scale e^(L/2), while gamma grows only logarithmically. More precision cannot repair this structural cost or the information lost by discarding the positive part of q_L-lambda.

The strategy note gives an exact alternative organization. Define W_cont=integral e^(|u|/2)kappa_F(u)du. Pole neutrality gives W_cont=-J, where J=integral |Fhat(t)|²/(t²+1/4)dt/(2pi). Therefore Q=Gamma+J-E with E=W-W_cont. This isolates signed prime-density error before absolute estimates. It is a candidate for a new bound, not an established positivity mechanism; Gamma+J itself has a negative low-frequency part.

Do not carry one-prime isolated-resonance arguments into {2,3} unchanged. Ratios of smooth frequencies give dense candidate resonance locations. Fixed-set kernel L2 summability may replace isolated-singularity analysis, but its constants must be tracked. The arithmetic certificate and the source nuclear bound can be used without assuming this additional compactness theorem.

## Bounded next-session work

1. Replay the existing certificate once and verify its bindings. Preserve it as an immutable baseline; develop a separately parameterized extension.
2. Derive the general-L moment projection, complete active-prime-power multiplier, Legendre tail, and integration remainder. For normalized plane waves on the fixed reference interval the low-band operator has factor L, derivative bound L/sqrt(12), and plane argument LT/2. Account for all changes under dilation.
3. Write a cost preflight and a proposed analytic continuation or relative-energy estimate. Include the cutoff, rank, integration cells, estimated work, and independent error margins. Select a finite resource budget; stop expansion when the preflight exceeds it rather than silently starting a large sweep.
4. Use L=6/5 as the provisional next anchor. Its active prime powers are 2 and 3; 4 is still inactive. When comparing B and K over [1,6/5], use the fixed set S_star={2,3}. Recalibrate the inherited bound for that representation; Q on old sources is unchanged by adding the inactive place, but B and K are not individually unchanged.
5. Compare the raw low-band bound with a cancellation-preserving alternative on the same source space. If the capped multiplier fails, evaluate the worst test direction against the actual Q and quantify the positive energy that was discarded. Classify arithmetic, approximation, and cost failures separately.
6. Attempt an outward full-space certificate only if the chosen method has a plausible margin and acceptable cost. Deliver one result or a specific obstruction, an audit, and a statement of what all-window estimate the experiment supports. Do not infer B>=K_plus, generic place monotonicity, or RH from a finite pass.

## Recommended working environment

Use Codex with the existing local repository for the next execution session. The work requires reading the actual files, editing a certificate generator, running outward arithmetic, checking hashes and maintaining small research artifacts. This matches the repository execution workflow described in the [official Codex documentation](https://learn.chatgpt.com/docs/codex/cli). This is a recommendation based on workflow, not a claim that the Codex interface guarantees stronger mathematical reasoning.

ChatGPT is useful for a fresh conceptual or literature review of the strategy and proof, especially when given this handoff and the referenced notes. Official documentation describes [ChatGPT projects](https://learn.chatgpt.com/docs/projects) as supporting separate research, drafting and review chats. Ensure the reviewer receives the actual new files; the local uncommitted notes are not automatically implied by a repository URL. A different interface does not guarantee a different underlying model or specialist-level independent verification.

Suggested opening request for the new session:

> Continue the sonin-critical-boundary investigation from NEXT_SESSION_ALL_WINDOW_HANDOFF_20261003.md in the existing local checkout. First audit the all-window strategy and the scaling of the completed L=1 certificate. Then carry out the bounded next-session work in that note, preserving the current certificate and source class. Treat a larger-window certificate as a test of the proposed global mechanism, and report the precise remaining theorem obligation.
