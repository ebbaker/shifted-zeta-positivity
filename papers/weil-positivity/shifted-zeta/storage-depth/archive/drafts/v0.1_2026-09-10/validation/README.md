# Package validation

The absolute spatial sign, direct relative sign at theta=.9, positive-shift
corollary, arithmetic partition check, and numerical cross-checks were replayed
through the supported entry point while preparing this package. Logs and
RUN_RECORD files are included. The relative replay reproduced its historical
small record byte-for-byte, so its replay folder contains the log and run
record rather than a duplicate mathematical record.

All 75 historical small files and all three external archives were verified.
Six archive-integrity tests passed; all Python files compile. Archive ignore
rules were checked in a temporary Git repository. No user repository was staged
or committed.

The 17-page PDF was compiled and visually checked; it has no unresolved
references or overfull boxes. PACKAGE_CHECKS.json records the exact scope.

These checks reuse the saved spatial matrices and inherited analytic bounds.
They are not an independent full matrix reconstruction or a normalization audit.
