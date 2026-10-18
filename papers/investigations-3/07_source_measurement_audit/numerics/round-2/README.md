# Round 2 bounded verification

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance; **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. These are
same-model routine checks, not a cross-model or specialist assessment.

| Code / record | Purpose and bound |
| --- | --- |
| [certify_gap_alignment.py](certify_gap_alignment.py) / [GAP_ALIGNMENT_CERTIFICATE.json](GAP_ALIGNMENT_CERTIFICATE.json) | Two fixed endpoints and one midpoint near \(44.1060084240846\), \(t=1/4\), unanchored normalized \(N=6\), original recurrence design; interval existence, top eigendirection, positive coefficients and frozen nonzero curvature. 448 bits, 120 seconds, 512 MiB |
| [no_real_tail_certificate.py](no_real_tail_certificate.py) / [NO_REAL_TAIL_CERTIFICATE.json](NO_REAL_TAIL_CERTIFICATE.json) | Recomputes the round-one fixed directional budget and verifies uniform tail domination at only the declared sufficient heights 264/269. No physical integrals. 320 bits, 180 seconds, 512 MiB |
| [check_two_replays.py](check_two_replays.py) / [REPLAY_HYGIENE_CHECKS_CODEX_20261017.json](REPLAY_HYGIENE_CHECKS_CODEX_20261017.json) | Compares two unchanged fixed-case replays with the historical mathematical data, retaining stored-byte provenance separately |
| [test_replay_record_hygiene.py](test_replay_record_hygiene.py) | Checks invariance to timing/provenance, sensitivity to enclosure/precision/content-reference changes, self-hash exclusion, nonfinite-data rejection and Linux/macOS RSS units |

The gap certificate extends round one's scaled Acb method to the second
derivative and a local Taylor enclosure. It does not certify the adjacent
theta-zero gap or a unique \(N=6\) root. The tail certificate proves
sufficient no-real-zero heights for the specified fixed perturbed sources,
not a first-loss height or a bound for \(\eta\) at 140. The one-direction
gap theorem in [Note 02](../../notes/round-2/02_ONE_DIRECTION_GAP_COLLISIONS_AND_TAIL_BUDGET_CODEX_20261017.md)
is analytic; it does not depend on sampling more high zero gaps.

The replay runner in [round one](../round-1/README.md) now emits both stored
record hashes and canonical mathematical-content hashes, using
[replay_record_hygiene.py](../round-1/replay_record_hygiene.py). The explicit
projection retains enclosures, witnesses, precision, scope and mathematical
hash references; it omits listed execution/environment fields and stored
file/code provenance. All five retained records agree with their historical
mathematical contents in both runs. Their stored bytes can differ because
timings and dependent stored-file hashes change. No historical certificate
is replaced. This is tested serialized identity, not mathematical validity
or arithmetic portability.

Requires Python with python-flint; the replay also requires mpmath.
Choose output directories outside the repository:

~~~sh
python3 certify_gap_alignment.py --output /tmp/GAP_ALIGNMENT_CERTIFICATE.json
python3 no_real_tail_certificate.py --output /tmp/NO_REAL_TAIL_CERTIFICATE.json
python3 -m unittest discover -s . -p 'test_replay_record_hygiene.py'
~~~

To repeat the content comparison, run ../round-1/run_replay.py twice
under the unchanged round-one contract, using two different external
output folders and the same original-record argument. Then run:

~~~sh
python3 check_two_replays.py --code-dir ../round-1 \
  --historical-dir ../round-1 --first-run /tmp/replay-a \
  --second-run /tmp/replay-b --output /tmp/REPLAY_HYGIENE_CHECKS.json
~~~

The supporting fixed replays took about 29 seconds each and less than
34 MiB peak child memory on macOS. The code explicitly converts Linux's
KiB and macOS's byte ru_maxrss values to bytes. No new height grid or
support sweep was run. Stored and canonical hashes identify their own
objects; arithmetic checks remain necessary. Follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md); all retained files are
small, and full floating regeneration outputs remain outside the checkout.
