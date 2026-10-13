# Brainstorm numerics

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork. Internal checks, not independent
mathematical validation.

## Checks for the review of the Codex priority response

Programme: [check_priority_response_review_20261012.py](check_priority_response_review_20261012.py).
It uses only the standard library, is deterministic, and writes a JSON
record. Record:
[PRIORITY_RESPONSE_REVIEW_CHECKS_20261012.json](PRIORITY_RESPONSE_REVIEW_CHECKS_20261012.json).
Consumer: the
[review](../reviews/REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md).

| Check | Input (pinned) | Result in the record |
| --- | --- | --- |
| A | Gomila barrier transcript, `a74738de`, SHA-256 `2d010f70…05f4` | 883 prisms, all PASS; `min_mesh = spatial + time + eps + margin` to `1.3·10⁻¹⁹`; `spatial = 2D_z/mesh`; time allowance equal to margin in 882 prisms; worst joint majorant factor `1.497` and `D_z`-only factor `1.988`, both at prism 882; `D_t`-only factor `2` |
| B | Gomila tail Arb log, SHA-256 `bd189e50…6a66` | `D = P + TR + OV + M_max·AB = 0.99972`; `1 − D = 2.79·10⁻⁴`; `1 − (D − OV) = 0.0395` |
| C | Gomila `E_max` Arb log, SHA-256 `995651e4…b244` | `L_690988 / E_max = 3.39` |
| D | Liu closure manifest at `7d10420d` (upstream `adc7f124`), SHA-256 `b34b902e…043f`; openai/math modules at `fd4aeeb2` | 2,925 of 2,925 git blobs identical; Hecke solution module in the closure, zeta/Dirichlet wrapper module not |
| E | openai/math comparator, scope, toolchain and manifest files at both revisions | byte-identical |
| F | this repository's [certified row record](../../newman_certificate_audit/numerics/CERTIFIED_ROW_REPLAY_RECORD_20261012.json) | `1 − g_N − S_N = 1.40·10⁻⁶`; relative room in `S_N` with `E_max` is `1.07·10⁻⁶` |

## Replay

The inputs are third-party files. They stay outside this repository, under
the [large-file policy](../../../../LARGE_FILES.md). The programme can fetch
them by pinned commit URL. About 2,950 files are fetched, mostly small Lean
sources.

```sh
python3 check_priority_response_review_20261012.py \
  --inputs /path/outside/repo/inputs --fetch \
  --row-record ../../newman_certificate_audit/numerics/CERTIFIED_ROW_REPLAY_RECORD_20261012.json \
  --output PRIORITY_RESPONSE_REVIEW_CHECKS_20261012.json
```

If Python's certificate store rejects the HTTPS fetch, set `SSL_CERT_FILE`.
Alternatively, download the files with `curl` into this layout:

- `gomila/<package path>`
- `liu/upstream/closure_manifest.json`
- `openai-math-fd4aeeb2/lean/<path>`
- `openai-math-adc7f124/lean/<path>`

The programme refuses to run if a pinned input hash differs.

## Lifted theta symmetry seeds

13 October 2026. Prepared for Edward Baker with substantial LLM assistance
by GPT-6.1-sol (`gpt-6.1-sol`), Codex, reasoning effort **ultra**.
Internal checks, not independent mathematical validation.

The [broad lifted-symmetry brainstorm](../LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md)
is accompanied by:

- [Exact finite checker](check_lifted_symmetry_seeds_20261013.py), using only
  the Python standard library and rational arithmetic.
- [Retained execution record](LIFTED_SYMMETRY_SEED_CHECK_RECORD_20261013.json):
  192 passing assertions for fixed/moving reflection, truncated commutators,
  passive charts, and two generic collision/observation controls.
- [Source and scope record](LIFTED_THETA_SYMMETRY_SEARCH_RECORD_CODEX_20261013.json):
  source hashes, primary-reference access levels, and the distinction
  between checked seeds and proposed genuine-theta applications.

From this directory, replay without replacing the retained record:

```sh
python3 check_lifted_symmetry_seeds_20261013.py --output /tmp/lifted-symmetry-check.json
```

The finite checks do not test a genuine-theta stationary sign or prove
nonvanishing. The brainstorm's analytic Stein, Volterra, squeeze and weak
boundary dictionaries have direct derivations; they are not additional
claims of computational certification. All retained files are small and
no third-party PDFs or large generated data were added.
