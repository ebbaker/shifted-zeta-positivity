# Computations and small records

19 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Actual lead model/effort unavailable in canonical public-history metadata.

[Setup check](01_AGC_JH_SETUP_CHECK_20261119.json) records documentation, source-integrity and link checks only. No mathematical computation or numerical campaign was executed during setup. Future code and small execution records require a fixed E packet; large reproducible data and third-party PDFs follow [LARGE_FILES](../../../../../LARGE_FILES.md) and stay outside Git.

[Policy update check02](02_AGC_JH_POLICY_UPDATE_CHECK_20261119.json)
records the later Astra/ultra and Sol 6.2/ultra guidance revision.
The original setup check is an unchanged historical file-version record.


First research milestone, 19 November 2026: [Exact check record03](03_AGC_JH_EXACT_CHECKS_20261119.json) and [program](check_agc_jh_interface_20261119.py) cover fixed algebra controls; [integration record04](04_AGC_JH_MILESTONE_RECORD_20261119.json) records file checks and provenance.

[E07 certificate](05_AGC_JH_E07_CERTIFICATE_20261119.json) contains the canonical time-zero input, bounds and root intervals. Run [certify_e07.py](certify_e07.py) with python-flint 0.9.0; it imports [the source and head evaluator](e07_fields.py) and [the count and collar evaluator](e07_chart.py). Its default output is JSON on standard output.

[E08 certificate](06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json) records certified physical-time enclosures, all 15 primary gates, the E07 anchor and the endpoint change. Run [certify_e08.py](certify_e08.py) with python-flint 0.9.0. Its [source](e08_source.py), [moving head](e08_head.py) and [collar and root routines](e08_chart.py) share the E07 time-zero conventions.

[Build record07](07_AGC_JH_MANUSCRIPT_BUILD_20261120.json) identifies the 20 November 2026 manuscript reading copy, editable sources and PDF checks.
