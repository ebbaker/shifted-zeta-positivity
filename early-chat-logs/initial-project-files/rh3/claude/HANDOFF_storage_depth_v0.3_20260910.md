# Handoff — storage-depth v0.3 session (10–11 September 2026)

## State of the repository (`~/Documents/shifted-zeta-positivity`, branch `critical_path`, HEAD `89cc928`)

All changes are **staged, not committed** (40 index entries; `git status` shows them). Teddy commits.

* `papers/storage-depth/` is now **v0.3**: `manuscript/storage_depth.tex` + `.pdf` (20 pp.), rewritten as a paper (intro with main theorems, framework, spatial continuation + direct-floor lemma, finite certification, first step, second step with diagnosis, all-depth discussion with dimension estimate and Fourier-side observation, records; generator/cumulative-storage material moved to Appendix A). New `README.md`, `STATUS.md`, `ARCHIVES.md`, `CLAIMS.json` (R14–R17), `BUILD_RECORD.json`, `SHA256SUMS.txt` (verified on the device).
* v0.2 moved with `git mv` to `archive/drafts/v0.2_2026-09-10/` (tex, spatial_recursion.tex, pdf, and its six package files). `archive/drafts/README.md` describes v0.1 and v0.2. The review in `archive/reviews/` got an erratum paragraph (display-radius remark; confirmation of findings).
* New code: `numerics/recursion/stream_io.py` (streaming dual-hash loader), `replay_floor.py` (archive-based replays with three-figure bisection, `--oracle-tail-floor` diagnostic), `rayleigh_upper.py`; `numerics/fourier_side/{export_head,zero_sum_check,zero_sensitivity}.py`.
* New records: `numerics/records/floor-bisection-{first,second}-2048.json`, `rayleigh-upper-{first,second}-2048.json`, `oracle-second-{0.5,0.55,0.65}.json`; `numerics/fourier_side/{zero_sum_check_K400,zero_sensitivity_K20,zeta_zeros_400}.json`.
* Repository indices updated: root `README.md`, `papers/README.md`, `MANIFEST.md`, `CHANGELOG.md`, `.github/workflows/build-latex.yml` (storage_depth, 20 pages).
* Sibling archive unchanged; my review folder there (`shifted-zeta-positivity-archive/storage-depth/reviews/2026-09-10_review-of-v0.2_claude/`) still holds the diagnostic scripts and RESULTS.md (the erratum was added only to the repo copy of the review).

## Certified numbers (working normalization; all through the repository code path, 2048-bit re-evaluation of the 6144-bit archives)

* First step `L_q`: absolute floor **2.99e-29** (3.00e-29 fails); relative test `M_0.9 >= 2.90e-29`, `M_0.8 >= 2.67e-29`; `theta = 0.78` (0.76 fails); `mu = 1.13e-7` (1.14e-7 fails); ball Rayleigh upper bound **3.29e-29** (quotient 3.28379e-29). Shift interval `omega <= 9e-16`, `||V|| <= exp(-1.4e-29 omega)`.
* Second step `L_2`: `mu = 5.01e-8` (5.02e-8 fails); upper bound **1.89e-30**; absolute/residual not certified. Hypothetical floors (diagnostic only): 0.5 fails, 0.55 passes both tests, 0.65 gives theta 0.8 and largest absolute floor 1.64e-30.
* Fourier side (diagnostic): zero sums for f_0 reach 76/83/86/92% of lambda_0 at K = 100/150/200/400 zeros; f_0(0) = f_0(L_q) = 1.8e-14, join jump 1e-15; |F_0(gamma_k)| ~ 1e-28..1e-18 for k <= 13; displacing zero k off the line contradicts the certificate at delta* = 1e-12 (k=1) ... 0.1 (k=17, height 70). Interpretation in the paper §7.5: the certificate sees zeros only below height ~70; milestones L = 2,3 carry no information about zeros.

## Done on 11 September (after the session reset)

* **Second step certified (R18).** First step rebuilt with 96 slab modes (41 min, floor 1.109), then `256+96+96` built (85 min, three-interval floor 0.768 as projected). Certified: `1.69e-30 <= lambda_min(Q_{0,L_2}) <= 1.89e-30`, `M_0.9 >= 1.65e-30`, `theta = 0.8`, `mu = 5.25e-8`, shift `omega <= 2e-16` (`C_{L_2} < 17.4886`). Paper (now 21 pp.), Theorem 1.2, Section 6.4, STATUS, CLAIMS, ARCHIVES, README, indices all updated and staged on the device (54 index entries).
* **Two large archives could not be transferred** (bridge limit 20 MB/file): `closure_256_96.matrices.json.gz` (266 MB) and `output/second-quarter-96/central_matrices.json.gz` (633 MB). Their hashes, small records and regeneration commands are in ARCHIVES.md / README.md (R18 block); REGENERATE.md notes were placed in the sibling archive folders. A local rebuild gets a new gzip hash; use the record your own build writes and compare content hashes (`numerics/tools/describe_archive.py`).
* **Builder-source hash caveat:** the new archives record the hashes of every `*.py` in `numerics/recursion/` at build time; editing any of them (including `replay_floor.py`) will make `stream_io.load_record` reject the R18 archive. `build_step.py` / `build_from_seed.py` were left byte-identical; the parameterized variants are `build_step_seed.py` / `build_from_seed_v2.py`; helpers live in `numerics/tools/`.
* **Fourier side:** K = 2000 run recorded (97.8% of lambda_0 at height 2515, 1/T tail extrapolating to 100%).
* Untracked folder `Claude outputs/` at the repo root is not mine; check before committing.

## Still open

* Regenerate the two R18 archives locally and confirm content hashes; the two-interval (re-globalized) second step; half/whole-step builds to `log 8` (needs a slab-length parameter in a copy of the first-step builder); rigorous Fourier-side check; independent reconstruction; normalization audit.
* Depth strategy: see `NOTE_depth_strategy_20260911.md`.

## Environment notes

* Cloud container: python-flint 0.9.0 + mpmath 1.4.1 installed; the four matrix archives were staged to `/mnt/user-data/uploads/.../numerics-archives/` (STORAGE_DEPTH_ARCHIVES). The container is ephemeral.
* Teddy's Linux VM: python-flint 0.9.0 installed by pip for the review; 3 GB RAM, so use `stream_io`-based tools there; each device shell call is limited to 3 minutes.

## Suggested next conversation

Strategy for increasing depth (Teddy's request): weigh (a) the 96-slab second step and the recursion invariant (merge vs grow), (b) the dimension barrier near L = 3, (c) the Fourier-side finding that fixed-horizon certificates at L <= 3 cannot say anything new about zeros, and hence where analytic effort should go (the all-depth premises, not the numerics).
