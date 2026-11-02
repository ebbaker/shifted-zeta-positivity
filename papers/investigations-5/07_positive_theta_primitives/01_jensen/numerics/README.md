# Jensen exact algebra and small execution records

1 November 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), reasoning effort ultra**.

## Replay after folder numbering

J-E07, 1 November 2026; prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / xhigh**. Original calculation programs and JSON evidence retain their exact bytes and historical paths. Run them through [replay_frozen.py](replay_frozen.py), which checks current files, reverses only recorded navigation edits into a temporary tree, verifies original hashes, then executes the unchanged program. Every original integrity assertion stays active. The [path manifest](J_E07_REPLAY_PATHS_20261101.json) records the original and current versions; changed inputs fail closed.

```sh
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py --verify-only
```

The commands below use that adapter. Historical chat text and JSON provenance intentionally retain their original paths. The [organization return](../notes/17_NUMBERED_RESEARCH_FOLDERS_20261101.md) records verification. Existing mathematical results are unchanged.

- [j_e01_audit.py](j_e01_audit.py): standard-library rational algebra for
  J-E01 r1, generating only Q0–Q8, retaining the complete mixed curvature
  numerator and proving the endpoint sign by polynomial translation.
- [J_E01_R1_EXACT_RECORD_20261101.json](J_E01_R1_EXACT_RECORD_20261101.json):
  full signed polynomial coefficients, input/code hashes, exact checks,
  finite limits and bounded disposition.

From the repository root:

```sh
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e01_audit > /tmp/J_E01_R1_REPLAY.json
cmp /tmp/J_E01_R1_REPLAY.json papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/J_E01_R1_EXACT_RECORD_20261101.json
```

The [derivation and analytic tail justification](../notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md)
carry the proof. The code records exact algebra; it performs no theta
evaluation grid, coefficient campaign or optional numerical acquisition.
Input hashes refer to the frozen mathematical sources, not the later
progress/navigation edits.

## J-E01 r2: signed averaging

- [j_e01_r2_audit.py](j_e01_r2_audit.py): hash-checked reuse of immutable
  r1 routines, Q0–Q10, origin quotient series and mixed J numerator,
  P0–P7 tail cancellation, Gaussian relation and pair-lattice identity.
- [J_E01_R2_EXACT_RECORD_20261101.json](J_E01_R2_EXACT_RECORD_20261101.json):
  all exact coefficients and signs, input/code hashes and finite limits.

```sh
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e01_r2_audit > /tmp/J_E01_R2_REPLAY.json
cmp /tmp/J_E01_R2_REPLAY.json papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/J_E01_R2_EXACT_RECORD_20261101.json
```

The [r2 return](../notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md)
contains the conditional proof and differentiated remainder. Both limiting
tests pass; global R'>0 and K>=0 remain unproved. No optional numerical
theta acquisition, source grid, theta-minor or quadrature calculation is
performed. r1 files remain unchanged. Prepared for Edward Baker with
substantial LLM assistance, gpt-6.1-sol / ultra, 1 November 2026.

## J-E02 r1: compact certificate and exact algebra

- [j_e02_certificate.py](j_e02_certificate.py) and [interval record](J_E02_R1_INTERVAL_RECORD_20261101.json): full-source origin coefficients and 126 direct-normalized Taylor/Bernstein cells, including all error payments and exact dyadic lower bounds.
- [j_e02_algebra_audit.py](j_e02_algebra_audit.py) and [algebra record](J_E02_R1_ALGEBRA_RECORD_20261101.json): joint numerator identities, r2 equivalence, Gaussian equality and generic even-source cancellations.
- [Replay validation](J_E02_R1_REPLAY_VALIDATION_20261101.json): artifact/cover checks, conservative margins, installed replay and actual arithmetic times.

The certificate uses python-flint 0.9.0 / FLINT 3.6.0 (Arb), starts at
128 bits and permits the frozen 256-bit refinement. The retained run passed
all 127 leaves at 128 bits with no refinement or subdivision. Setup a
separate environment if the dependency is not already available:

```sh
python3 -m venv /tmp/j-e02-replay-env
/tmp/j-e02-replay-env/bin/pip install python-flint==0.9.0
/tmp/j-e02-replay-env/bin/python papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e02_certificate --record /tmp/J_E02_R1_REPLAY.json
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e02_algebra_audit > /tmp/J_E02_R1_ALGEBRA_REPLAY.json
```

Run from the repository root. The installed replay was identical in all
non-timing fields with the recorded versions. Timing fields differ on
rerun; arithmetic on actual balls, rather than a matching hash alone,
decides the signs. The whole leaf cover and source/origin coefficient
balls fit in the small record; no bulky coefficient archive is required.

The [return](../notes/11_J_E02_R1_GLOBAL_SIGN_CERTIFICATE_RETURN_20261101.md)
contains the audited analytical tail, joins and scoped consequence. The
global fixed-order claim awaits J-E03 assessment. Prepared for Edward
Baker with substantial LLM assistance, gpt-6.1-sol / ultra, 1 November 2026.

## J-E03 assessment evidence

- [j_e03_assessment_check.py](j_e03_assessment_check.py) and [assessment record](J_E03_ASSESSMENT_RECORD_20261101.json): exact input/record hashes, dyadic endpoint consistency, rational cell cover and margins, plus one unchanged fixed-certificate replay comparison.
- [j_e03_firstmode_check.py](j_e03_firstmode_check.py) and [first-mode record](J_E03_FIRSTMODE_RECORD_20261101.json): fresh standard-library integer-polynomial verification of the P0–P7 first-mode rational formulas. No numerical evaluations.

After generating a replay with the unchanged E02 program:

```sh
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e03_assessment_check --replay /tmp/J_E02_R1_REPLAY.json
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/numerics/replay_frozen.py j_e03_firstmode_check
```

The assessment's sole compact replay took 4.305158625 seconds and matched
every non-timing field. No certificate code, mathematical input, case or
allowance was changed. Analytical acceptance and the review relationship
are in [Review01](../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md);
the record checker does not itself assess the analytic proof. Prepared
for Edward Baker with substantial LLM assistance, gpt-6.1-sol / ultra,
1 November 2026.

## Parallel-branch support, 1 November 2026

- [J-B05 finite tail checker](../02_signed_averaging/numerics/j_b05_tail_check.py) and [exact record](../02_signed_averaging/numerics/J_B05_TAIL_CHECK_20261101.json): integer recurrence only through P7, supporting the analytical h4 obstruction; no source samples or scan.
- [J-B09 version/check record](J_B09_PARALLEL_REVIEW_RECORD_20261101.json): original input hashes, final return hashes and coordinator verification. It identifies versions, not mathematical truth.

Prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra / ultra; [Review02](../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) states the internal assessment scope.
