# Changelog

## 2026-09-18 — wilson-lines: reflection networks (Claude Fable 5.1)

- New note `papers/susy-positivity/investigations/wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md`:
  the positive pairing of the endpoint kernel constructed as a through-the-defect
  reflection network; the within-defect reflection shown to glue only the
  alternating tower. Conditional on OS positivity of the interface.
- New check `numerics/check_reflection_networks.py` (1196 cases) with record;
  not yet registered in `validation/endpoint_matter.py`.
- Continuation `notes/CONTINUATION_20260918_CLAUDE_SESSION2.md`; indexes updated.
  Manuscript unchanged at 0.8.

All notable changes to the released contents of this repository. Dates are the
dates of the underlying work; the repository itself was created in September 2026.

## [Unreleased]

- Reorganized SUSY positivity as a program with shared background and overview;
  moved its v0.2 manuscript, checks, and historical support into
  `papers/susy-positivity/attempts/positive-factorizations/`. See the
  [move and verification record](papers/susy-positivity/archive/REORGANIZATION_20260912.md).

### 2026-09-18 — SUSY positivity: close the Loewner investigation, open fractional dimension

- Close `papers/susy-positivity/investigations/loewner/`. It was opened to test
  one proposal — that a Loewner-type conformal evolution could construct the
  shifted Weil family's deformation paths — and the proposal is answered in the
  negative on all three factors of the transfer: the comb (far-field transport is
  a pure delay), the rational correction (forced by unimodularity, no arithmetic
  in its residues), and the archimedean factor (three independent obstructions).
  The folder keeps its name, which records the question it tested, as the sibling
  folders' names do; a closing header at the head of its README says what is
  closed and where the work continues.
- Its durable output is the decomposition with its dictionary — including the
  identification of the archimedean factor as the horocycle integral
  `int_{R^d} |t+i|^{-(p+b)} dt` in dimension `d = 2 omega` — and a registered,
  standard-library assembly of the compressed transfer that computes its norm,
  defect and Cayley coordinate at any horizon. Manuscript *The Markov part of the
  shifted Weil transfer* reaches working draft 0.3 (33 pages) with two registered
  check programmes, 53 and 43 cases, replayed with it.
- Open `papers/susy-positivity/investigations/fractional-dimension/` from it, with
  an opening note, one check programme (72 cases) and no manuscript. Its first
  result: the comb's weights are the Jordan totient, `ct_n = J_d(n)/n^((d+1)/2)`,
  which at integer `d` counts the primitive vectors in `(Z/nZ)^d`, so every factor
  of the Markov part is `d`-dimensional as a formula and `d = 1` is the modular
  surface. Its question is whether `d` is a dimension or a parameter.
- Fractional dimension, first two results, closing its dictionary on a single
  object. (i) **The dimension is `2 omega`, not `omega`.** `tau = log|t+i|` is a
  Busemann function on the horocycle and not a distance: the hyperbolic distance
  is `d_H = 2 arcsinh(t/2)`, and `tau ~ r^2/2` is a square, so a measure with
  local exponent `r^(2om-1) dr` has local exponent `tau^(om-1) dtau` and the two
  normalized limits differ by exactly `2^(1-om)`. In the true half-distance
  `u = d_H/2`, Lebesgue on `R^(2om)` is the radial measure of complex hyperbolic
  space of complex dimension `omega` and real dimension `2 omega` — Jacobi
  parameters `(om-1, 0)` with `rho = om > 0`, the only reading that accounts for
  every factor of the kernel — and the comb, having no radial coordinate, fixes
  `d = 2 omega` independently. (ii) **The Blaschke factor is a volume term:**
  `Res_{p=b} Kt_om = |S^d| / (2 zeta(d+1))`, the sphere of `R^(d+1)` times the
  primitive density in `Z^(d+1)`, which is the volume term of a lattice of
  **rank `d+1`** whose cusp integrates over a `d`-dimensional horocycle; at
  `d = 1` it is `6/pi = 2/vol(PSL(2,Z)\H)`, the classical Eisenstein residue.
  The question sharpens accordingly: a dimension can be continued, but a rank is
  a cardinality, so — is there anything of which `J_d` and `zeta(d+1)` are the
  invariants when `d` is not an integer? Note
  *Which coordinate carries the dimension, and the correction as a volume term*,
  with two further standard-library check programmes (56 and 27 cases; 155 cases
  in the investigation). No value of zeta is computed except at real arguments
  above 1, by a convergent series.
- Fractional dimension, the rank question answered. (i) **The object at integer
  `d` is a lattice of rank `d+1`, at every integer and not only at `d = 1`.** For
  a covolume-one lattice `L` in `R^m` the primitive Epstein zeta
  `E*_L(s) = sum_{v primitive} |v|^(-2s)` satisfies
  `xi(2s) E*_L(s) = xi(m-2s) E*_{L*}(m/2-s)` — Poisson summation plus the
  factorization `Z_L = zeta(2s) E*_L` — so the reflection ratio is independent of
  the lattice and is an invariant of the **rank alone**. Under the dictionary that
  ratio is exactly the Markov part, so for every integer `d >= 1` the shifted Weil
  transfer is the scattering matrix of the space of unimodular lattices of rank
  `d+1`; and the transfer's own reflection `p -> -p` IS the Epstein functional
  equation `s -> m/2 - s`, which is why it is all-pass on `Re p = 0`. This
  strengthens the previous position, which held `d = 1` to be the only realized
  point. (ii) **The family's cap `omega <= 1/2` is a rank cap.** `xi` has poles at
  0 and 1, so the numerator has a second pole at `p = omega - 1/2`, in the closed
  left half-plane exactly when `m = 2 omega + 1 <= 2`; in the lattice variable it
  sits where zeta has its own pole. The family therefore occupies the first gap
  `m` in `(1,2]` of the rank sequence, with the modular surface — and RH — at its
  right endpoint. (iii) **Inside that gap the lattice does not exist.** The point
  count of `Z^m` has a unique interpolation, the q-coefficients of `theta^m`,
  which are polynomials in `m`; with `m = d+1`, `r_{d+1}(3) = (4/3)(d^3 - d)` is
  strictly negative for every `d` in `(0,1)` and vanishes only at the endpoints,
  so `theta(it)^(d+1)` is not completely monotone anywhere strictly inside the
  family — no positive measure, hence no point set. What continues is the whole of
  the cusp data (`J_d > 0`, `1/zeta(d+1)` in `(0,1)`, the horocycle integral, the
  unimodularity on the critical line); what fails is the interior. At fractional
  `d` the object is a scattering matrix without a space. Note *The rank is
  realized at every integer, and the lattice does not continue*, with a fourth
  standard-library check programme (327 cases; 482 in the investigation) built on
  Riemann's theta method in dimension `m`, cross-checked against direct lattice
  summation. zeta is evaluated at real arguments only, including negative ones; no
  value off the real axis is computed and no zero is located.
- Fractional dimension, the wall crossed and the criterion weighed. (i) **The
  Markov decomposition survives past the rank-two wall and needs no repair.**
  `R_om = B_b . (p+a)/(p-a)` at every `omega`, and `(p+a)/(p-a) = B_c` with
  `c = omega - 1/2` is a genuine Blaschke factor of the right half-plane exactly
  when `omega >= 1/2`, so past the wall `R_om = B_b B_c` is **inner**, where inside
  the range it is a ratio `B_b/B_a` with a right-half-plane pole. The parent's
  proof that `Khat_om` is completely monotone does fail there — the kernel of
  `(p+a)/(p-a)` is `delta_0 + 2a e^(at)` with `2a < 0` — but the statement does
  not: regrouping the Gamma factors,
  `Khat^Gamma_om = pi^om Gamma(z+c)/Gamma(z+om) . Gamma(z+1)/Gamma(z+c+1)` with
  `z = (p+a)/2`, exhibits it as a product of two Gamma ratios of parameter gap
  `1/2` and `c`, both completely monotone exactly when `omega >= 1/2`. So
  `Khat_om` is completely monotone for **every** `omega > 0`; the parent's
  proposition was uncapped and only its proof was. The two cancelled poles have
  different origins — `p = b` is the comb's pole, `p = c` the **archimedean**
  factor's — so past the wall the correction removes one pole from each half of the
  transfer. (ii) **The inherited assembly needed no second Blaschke factor at
  all**, because it is built from the partial fractions of `R_om`, which are the
  same algebra at every `omega`; the only change was a removable `0/0` in the k = 0
  Jacobi recurrence coefficient, which bites at `omega = 1` and nowhere else. With
  that one line changed the assembly's own Laplace certificate passes at
  `omega = 1, 3/2, 2` to `3e-13`. (iii) **But the experiment it unlocks cannot
  fail.** For every `omega >= 1/2` no zero satisfies `|Re rho - 1/2| > omega`,
  because `0 <= Re rho <= 1`; so by the parent's own dichotomy `V_om` is unitary and
  every `V_{om,L}` is a contraction **unconditionally** — on the strength of the Euler
  product alone for `omega > 1/2`, with the classical zero-free region needed only at
  the single boundary point `omega = 1/2`. The contraction criterion is vacuous on `[1/2, inf)` and has
  arithmetic content on exactly `(0, 1/2)`, where it is equivalent to the zero-free
  strip of half-width `omega`. (iv) **That is the same interval on which the lattice
  fails to exist:** `omega` in `(0,1/2)` is `d` in `(0,1)` is `m` in `(1,2)`, the
  open gap on which `r_{d+1}(3) < 0`. Same interval, same endpoints, both switching
  on the sign of `a = (1-d)/2` — the criterion has arithmetic content precisely
  where the lattice does not exist. (v) **Correcting the previous entry:** the
  modular surface is at the right endpoint of the gap but RH is not. The criterion
  is emptiest at `omega = 1/2` and sharpest as `omega -> 0`; the Euler product is
  its value at rank two and RH is its derivative at rank one, where
  `E*_Z = 2`, `Kt_0 = 1`, `V_0 = I` and the first-order law makes the localized Weil
  form its `d/d omega`. Note *Past the wall the decomposition survives and the
  criterion does not*, with a fifth standard-library check programme (266 cases;
  748 in the investigation), an extended copy of the parent's registered assembly.
  zeta is evaluated at real arguments `u >= 1.2` only, in one group, by
  Euler–Maclaurin; no value off the real axis is computed and no zero is located.
- Fractional dimension, the split explained and the question answered. (i) **The
  two positivity statements are not one statement.** The interpolated point count
  fails on `(2,3)` as well as on `(1,2)`, while the contraction criterion has
  arithmetic content only on `(1,2)`; and at `m = 3` the point count is completely
  monotone and the transfer's rational factor is not. No equivalence between them
  can hold, and the coincidence of intervals recorded in the previous entry is the
  first gap and nothing more — forced by both of the criterion's endpoints sitting
  at the two smallest ranks, `m = 1` where the transfer degenerates to the identity
  and `m = 2` where `a` changes sign. (ii) **The point count's failure is
  Lagrange's four-square theorem, seen through a binomial series.** Writing
  `theta^m = sum_j binom(m,j) (theta-1)^j`, on the gap `(k, k+1)` one has
  `sign binom(m,j) = (-1)^max(0, j-k-1)`, so `r_m(n) > 0` for free when `n <= k+1`,
  and the first coefficient that can be FORCED negative sits at `N_k`, the least
  integer needing `k+2` POSITIVE squares: `N_0 = 2`, `N_1 = 3`, `N_2 = 7`, and no
  `N_k` at all for `k >= 3`, because Lagrange gives `s(n) <= 4` for every `n`. The
  third note's Lagrange threshold at `m = 4`, recorded there as an observation from
  a scan, is exactly that and is now a theorem. (iii) **The transfer has exactly one
  positivity threshold in `m`, and it is at `m = 2`.** Every factor of the Markov
  part has a positive kernel at every real `omega > 0`; the only `omega`-dependent
  positivity anywhere in the decomposition is `(p+a)/(p-a)`. Its only other feature
  at an integer — the archimedean exponent `omega - 1 = (m-3)/2` vanishing at
  `m = 3` — is a REGULARITY threshold and not a positivity one, and it points the
  wrong way, since at `m = 3` the point count regains positivity. (iv) **What
  explains the split is where the rank sits.** In the transfer it enters every
  positive object as an EXPONENT — `(2 sinh tau)^(om-1)` in the archimedean kernel,
  `(1-e^-t)^(beta-alpha-1)` in each Beta density, `p^-d` in each Euler factor of the
  comb — where positivity is a LOCAL inequality, at one `tau` or at one prime, that
  continuation in the parameter cannot break. In the point count it enters as a
  BINOMIAL INDEX, where positivity is a global cancellation and continuation breaks
  it at once. So the transfer's positivity was never inherited from a lattice, and
  the lattice's failure leaves no trace in it; item 3 of the third note's plan, as
  posed — a factorization of the transfer exhibiting which factor loses positivity
  at fractional `d` — has no solution, because no factor loses positivity anywhere.
  (v) With that, **the investigation's own question is answered: `d` is a
  parameter**, with no remaining sense in which it is a dimension away from the
  integers. Note *The trade is not the explanation*, with a sixth standard-library
  check programme (774 cases; 1522 in the investigation), exact rational arithmetic
  throughout the theta side. No value of zeta is computed anywhere in it. The
  material is manuscript-shaped; no manuscript has been started.
- Fractional dimension gets its manuscript. *A scattering matrix without a space:
  the shifted Weil transfer as an invariant of the rank, the interval on which its
  criterion has content, and why the lattice's failure leaves no trace in it*,
  working draft 0.1, 21 pages, drafted for Edward Baker by Claude Opus 5. It
  consolidates the investigation's five research notes with every proposition
  proved in place and the inherited ones listed in its Section 2.3: the transfer
  as the primitive-Epstein scattering matrix of the rank-`d+1` lattices at every
  integer `d`; the wall at `m = 2` as the zero of `a = (2-m)/2`, where the
  archimedean pole crosses into the right half-plane, `R_om` turns from a ratio of
  Blaschke factors into an inner product, and the poles of `K_om` leave the closed
  right half-plane; complete monotonicity surviving that crossing by two groupings
  of the Gamma factors exchanged there; the criterion vacuous for `omega >= 1/2` on
  the Euler product alone, so its arithmetic content sits on exactly `m` in
  `(1,2)`, with the Euler product its value at rank two and RH its derivative at
  rank one; the point count's failure identified as Lagrange's four-square theorem
  read through a binomial series; and the two failures shown not to be one fact,
  separated by whether the rank enters as an exponent or as a binomial index. All
  six check programmes are registered in the investigation's new
  `validation/drafts.py` and replayed with the manuscript at 1522 cases,
  byte-identical. Snapshot `drafts/2026-09-18-v01`; build guide `BUILD.md`;
  provenance and the use of language models in the manuscript's Appendix B. No
  value of zeta is computed off the real axis anywhere in the package.
- No investigation folder was renamed and no preserved snapshot was rewritten.

### 2026-09-11 — group papers by research program

- Move psi-omega-margin, omega-string, defect-depth, first-slab-positivity,
  weil-depth, and storage-depth under `papers/shifted-zeta/`, with a project
  README explaining their relationships and reading order.
- Move rh-detector under `papers/misc/`; add a collection README and keep
  `papers/susy-positivity/` in place as a separate project.
- Replace the storage-depth-specific navigation with the shared project
  overview, treating all six papers as parts of the same program.
- Update current navigation, build paths, citation metadata, verification
  paths, and the repository checker for the grouped layout. Refresh current
  Weil-depth and storage-depth documentation hashes.
- Preserve manuscript sources and PDFs, numerical code and records, archived
  snapshots, SUSY background notes, and external data locations. Historical
  path references are explained in `papers/README.md`. No manuscript version
  or release is created.

### 2026-09-11 — storage-depth writing project closeout

- Merge `critical_path` into `main` with its five research commits preserved;
  no large numerical data enters the main tree or history.
- Update current README navigation, manuscript counts, the paper layout,
  repository metadata and the code/verification indexes for storage-depth v0.3.
- Standardize current archive documentation on `szp-archive`, locally
  `/Users/Shared/szp-archive`; keep historical draft snapshots unchanged.
- Move the existing lessons-learned note to `notes/`, retaining the author's
  pending wording change. Supersymmetric briefs are for a separate project.
- Record build, checksum, size and archive checks in
  `papers/storage-depth/CLOSEOUT.md`; refresh the current package manifests.
- Correct the dependency appendix to distinguish the failed 32-mode tests
  from the successful 96-mode R18 result; rebuild the 21-page PDF after
  minor typesetting fixes. No numerical constant or record changes.
- Document the author-accepted absence of the two regenerable R18 matrices
  and the intentionally omitted large Claude Fourier-analysis outputs.
- Keep the paper at working-draft v0.3. Independent normalization review,
  mathematical review and formal verification remain open; no release or DOI
  is created by this closeout.

### 2026-09-10 / 11 — storage-depth paper (branch `critical_path`): v0.1, v0.2, review, v0.3

- **New working draft `papers/storage-depth/`** — *Residual-controlled depth
  extension of finite-horizon Weil positivity: a spatial continuation past log 7
  for the shifted-zeta transfer* (v0.3, 21 pp.). Continues `weil-depth/` past
  `log 7` by splitting the interval at `log 7`, continuing old inputs onto a
  quarter slab of length `log(8/7)/4` by a Galerkin map, and certifying the
  graph-transformed Schur tests against the infinite polynomial complements.
  Certified in Arb ball arithmetic (working normalization):
  `2.99e-29 ≤ λ_min(Q_{0,L_q}) ≤ 3.29e-29` at `L_q = (3/4) log 14`, residual
  factor `R*F^{-1}R ≤ 0.78 H_J`, comparison `H_J ≥ 1.13e-7 A`, small-shift
  contraction for `ω ≤ 9e-16`; at `L_2 = log(56)/2` the 32-mode-slab build
  certifies only `H_{J_2} ≥ 5.01e-8 A_2` and the upper bound `1.89e-30` (its
  failed floor and residual tests diagnosed as an artifact of the three-interval
  complement floor), and the 96-mode-slab build of 11 Sept then certifies
  `1.69e-30 ≤ λ_min(Q_{0,L_2}) ≤ 1.89e-30`, residual factor `0.8`,
  `H_{J_2} ≥ 5.25e-8 A_2` and contraction for `ω ≤ 2e-16` (record R18). A direct-floor lemma
  (`M_θ ≥ m ⇒ Q ≥ m/τ²`) replaces the scalar comparison in the conditional
  all-depth scheme; a dimension estimate places the method's horizon near
  `L = 3`; a Fourier-side computation shows the near-null vector is tuned to
  vanish at the low zeros and that the certificate constrains zeros only below
  height about 70.
- Provenance: v0.1 and v0.2 drafted on 10 Sept by OpenAI models (five research
  packets, then a consolidated record); v0.2 reviewed by Claude with an
  independent re-implementation of the validators (`archive/reviews/`), which
  found the floors understated by four orders of magnitude and diagnosed the
  second step; v0.3 rewritten by Claude as a paper with the numbers re-derived
  through the repository's code path (records R14–R18: archive-based bisection
  replays, ball Rayleigh upper bounds, hypothetical-floor diagnostics,
  Fourier-side zero sums, the 96-mode-slab rebuild). Earlier drafts preserved under `archive/drafts/`.
- New tools under `numerics/recursion/`: `stream_io.py` (streaming dual-hash
  loader that runs in a few GB of memory), `replay_floor.py` (archive-based
  replays with bisection), `rayleigh_upper.py`; `numerics/fourier_side/` for the
  zero-sum diagnostic; `build_step_seed.py`, `build_from_seed_v2.py` and
  `numerics/tools/` for the 96-mode rebuild. Six matrix archives (about 1.6 GB, two of
  them built in a cloud container and to be regenerated locally) live outside git under
  `shifted-zeta-positivity-archive/storage-depth/numerics-archives/`.
- Root README, `papers/README.md` and `MANIFEST.md` describe the seventh
  manuscript. No human review; not released.

### 2026-09-09 / 10 — finite-horizon Weil paper (branch `finite-horizon-weil`); large-file convention

- **New working draft `papers/weil-depth/`** — *Finite-horizon Weil coercivity and
  shifted-zeta contraction: two-sided certificates for the finite-window Weil form
  through total horizon log 7* (22 pp.). Computer-assisted two-sided enclosures of
  `λ_min(Q_{0,L})` at `L = log 2, …, log 6, 9/5, log 7` in Arb ball arithmetic
  (analytic infinite-tail bound, full-output parity Grams, Schur test with an
  explicit profile remainder; ball Rayleigh upper bounds), reproduced by an
  independent implementation and checked against the Fourier-side form; each
  floor converted to a small-shift contraction of the transfer. Finite-depth
  statements only. Three machine-assisted review rounds on 9–10 Sept (v0.1 → v0.2
  Codex; v0.2 → v0.3 Claude with independent recomputation; v0.3 → v0.4 ChatGPT),
  each archived with the draft it reviewed under `archive/`. v0.4 changes are
  presentation and scope only: directed rounding in the certificate table,
  decay and horizon-ceiling claims restated as observations and resource
  projections, one denominator bound in the Laplace-line lemma corrected,
  classical hypotheses (Yoshida, Connes–Consani) cited as printed. No human
  review; not released.
- **Large-file convention.** New `LARGE_FILES.md`: committed files stay below
  about 1 MB; regenerable derived data are kept outside git in a sibling
  `shifted-zeta-positivity-archive/<slug>/numerics-archives/` folder, bound to
  the tree by file and content hashes in the small certificate records,
  described by a tracked `ARCHIVES.md` per paper, and located by scripts through
  an environment variable; pre-commit size check; repair procedure; what a
  release archives. Git LFS and shared drives rejected (LFS objects are absent
  from the tarball Zenodo archives). Root `.gitignore` excludes
  `numerics-archives/`. First instance: `papers/weil-depth/ARCHIVES.md` (about
  122 MB of ball matrices). The branch's early history still references those
  blobs; it is to be squash-merged into `main`, whose history has none.
- Root README, `papers/README.md` and `MANIFEST.md` describe the sixth manuscript
  and its layout; `build-latex.yml` builds the seventh PDF
  (`papers/weil-depth/manuscript/finite_horizon_weil.tex`, 22 pages).

### 2026-09-09 — external repository review applied (commit `50cb4d2` reviewed)

Changes from an independent repository-and-reproducibility review of the first
commit, applied after checking each finding; none touches the mathematics or
marks a pending human check complete.

- **Citation metadata.** `papers/first-slab-positivity/CITATION.cff` used
  `type: generic`, which the CFF 1.2.0 schema does not allow at top level
  (only `software`/`dataset`); both CFF files now validate. Each is a
  `software` record for the folder's sources with a `preferred-citation` of
  type `unpublished` identifying the preprint (that is what GitHub's "Cite this
  repository" and CFF tooling read). Root CFF license is MIT (it describes
  code); the papers stay CC BY 4.0 under `LICENSE`. New `tools/check_citations.py`
  validates both files against the official schema; `environment/requirements_metadata.txt`
  pins its dependencies.
- **No example DOIs.** `10.5281/zenodo.NNNNNNN`-style placeholders removed
  from every citation block; until a release exists the blocks give a
  commit-based form, and the DOI forms use ⟨…⟩ placeholders. README, paper
  README and `papers/README.md` now say plainly that no tag or DOI exists yet
  and that repository version (`0.2.0`) and manuscript version (`1.0`) are
  separate identifiers.
- **Honest description of the tree.** Root README tagline and `.zenodo.json`
  no longer imply the Arb certificate bundle is in the repository; `notes/`
  is described as an index for a planned migration (only the index and
  redaction checklist are present); "released as a preprint" → "available as
  a preprint". "No error survives in the main proof chain" (VERIFICATION_STATUS,
  CHECKLIST) → "no unresolved error was identified in those internal reviews;
  the independent human checks remain pending".
- **License notice** links the specific CC BY 4.0 deed and legal code and
  states that the two licenses apply by material type, not as a choice;
  "dual license" wording replaced everywhere. Copyright line unchanged.
- **Stable numerical diagnostics.** New
  `verification/first-slab/scripts/verify_stable_volterra_20260909.py`
  replaces the A4 section of the 5 Sept script, whose sampled singular kernel
  and unbounded float Laplace integral were numerically unreliable and whose
  printed failures never became a nonzero exit status. The new script uses
  integrated piecewise-constant Galerkin sections with Gauss–Jacobi treatment
  of the t^(ω−1) endpoint, checks the reflection algebra, 48/96-node and
  16/32-cell consistency and four high-precision Laplace-transfer identities
  (16 checks; exit 1 on failure). Re-run here: 16/16 pass under CPython 3.12
  with the pinned `mpmath==1.4.1`, `numpy==2.4.4`, `scipy==1.17.1`; an
  injected 0.001 error produces 4 FAILs and exit 1. Diagnostics only — not an
  interval certificate and not a bound on the infinite-dimensional operator.
- **CI.** `.github/workflows/check-first-slab.yml` runs the diagnostics and the
  CFF schema check. `RELEASING.md` now says what `build-latex` does and does
  not establish (compilation and page count, not PDF/source identity), that
  JSON parsing is not Zenodo metadata validation, and where each DOI goes.
- **Certificate code recovered, not integrated.** The Investigation 7/12/13/14
  generators, audit, diagnostics, result CSVs and verifiers were recovered and
  packaged as a review candidate outside the repository; its CSV hashes match
  the 5 Sept 2026 full-regeneration record and its stored-table verifiers pass.
  All three computations were then regenerated here in a fresh pinned
  environment (CPython 3.12.3, python-flint 0.9.0, numpy 2.3.5, scipy 1.17.0,
  mpmath 1.4.1; ~4 min total) and produced byte-identical tables —
  `verification/first-slab/CERTIFICATE_RERUN_20260909.md`, noted at D4 in the
  checklist and VERIFICATION_STATUS. The code stays out of the tree until
  D1–D5 are done (`code/README.md`, `MANIFEST.md` updated to say so).
- Contact e-mail in `code/certificates/first-slab/README.md` corrected to the
  personal address.

### 2026-09-08 / 09 — working drafts committed

- The four companion manuscripts are now in the tree as clearly labelled
  working drafts, each with `README.md`, `STATUS.md` and reproduction code:
  `papers/psi-omega-margin/` (full 21 pp. + concise 9 pp., scripts `c1`–`c8`,
  two supplementary notes), `papers/omega-string/` (v5, 13 pp., figure script,
  two verification scripts; Kasahara 1975 source-verified), `papers/defect-depth/`
  (v1, 15 pp., Ihara laboratory code), `papers/rh-detector/` (10 pp., scripts and
  zero caches; numerics re-verified). None is released; no DOI covers them.
- Folder slugs fixed to the actual names (`psi-omega-margin`, `omega-string`,
  `defect-depth`, `rh-detector`) throughout the READMEs, STATUS files, notes
  index and manifest; `rh-detector` marked as a separate thread that predates
  the Suzuki program.
- Author blocks filled in Papers 1 and 2 (Edward B. Baker III); contact email
  changed to the author's personal address in the preprint and all metadata;
  ORCID `0000-0001-5459-9993` added to `CITATION.cff` and `.zenodo.json`; no
  institutional affiliation in any paper (README carries the one mention).
- README: background section expanded (2015 origins; slice-regular,
  Yang–Mills and Chern–Simons phases; the turn to Suzuki's screw functions).
- `verification/first-slab/PROTOCOL_C1_C2.md` (6 Sept): step-by-step protocol
  for the two premise checks — normalization chain against Suzuki [1] and the
  originality search — written so the checker is not anchored by the preprint.
- `code/README.md` now points to the per-paper `code/` folders; the CI workflow
  builds all six PDFs.

- Single-repository plan adopted: releases archive the whole tree; each
  released paper is additionally deposited as its own Zenodo record linked by
  related identifiers (`README.md`, `RELEASING.md`, root `.zenodo.json`).
- `blueprint/first-slab/statements.md`: 30-statement inventory of the preprint
  with dependency graph, proof status, human-check status and formalization
  feasibility; machine-readable twin `statements/ledger.yaml`.
- `notes/REDACTION_CHECKLIST.md` and preface for the research log.
- Formalization section in `CONTRIBUTING.md`, `formalization` issue template,
  suggested labels.
- Program repository scaffold: papers/, verification/, notes/, code/, references/.
- Status files for the four unreleased manuscripts.
- Public verification checklist for the first-slab preprint, keyed to v1.0 numbering.

## [first-slab-positivity v1.0] — 2026-09-05

First deposited preprint: *Archimedean first-slab positivity for shifted zeta
canonical systems: an off-center Weil generator and a radial energy identity*.
Relative to the working draft of 3 September:

- Lemma 7.1 (block-Schur coercivity) and Remark 7.2 added; Theorem B now states
  the coercivity constant `c_* = 6.1159e−4` on `D_log` (the certified margin
  `6.11635e−4` is `~4e−8` above the exact block-Schur constant).
- §1.1 and abstract pinned to Suzuki's exact statements (Prop. 1.2, Thm. 2.2,
  Lemma 4.1 of arXiv:1204.1827); single-shift "equivalence" removed.
- §9.3 rewritten: strict finite-section contractivity for `ω > ½` is Suzuki's
  Lemma 4.4; Theorem A positioned as the complementary `0 < ω ≤ ½` result.
- Missing case-split line inserted in Lemma 6.1 (`a ≥ L/2 > t₀`).
- Private author-verification notice replaced by public §13 *Verification status*
  and Appendix C ledger row for `ω > ½`.
- Repository metadata: README, CITATION.cff, .zenodo.json, LICENSE (CC BY 4.0),
  VERIFICATION_STATUS.md.

### Earlier internal history (not released)

- 2026-09-03 — second referee round: all ten round-1 items resolved and
  re-verified (`verification/first-slab/reviews/REVIEW_round2_verdict_20260903.md`).
- 2026-08-31 — first referee round on the working draft
  (`REVIEW_round1_20260831.md`): endpoint lemma, sharp kernel bound (margin
  doubled), positivity horizon, Prop. 4.1 proof rewrite, §8 gaps.
- 2026-08-29 — defect-depth draft v1; Ihara laboratory rounds 1–5.
- 2026-08-28 — shifted zeta string paper frozen at v5 pending human review.
- 2026-08-27 — psi_omega_margin paper: next steps folded in (21 pp.).
- 2026-08-26 — geometry/physics routes closed (ROUND9); Suzuki screw-function
  program found (ROUND12) — pivot to the psi_omega_margin thread.
- 2026-08-24/25 — instanton-size brief; certified off-axis detector; pencil corollary.
