# Review of the WZW branch: what it established, what closes it, and where the viable paths are

**Reviewer: Claude Fable 5.1 (Anthropic, model `claude-fable-5-1`).** 24 September 2026, for Edward Baker.

**Review status.** Independent review by a different model from the one that produced the branch (all branch files are attributed to GPT-6 / Codex). Not a specialist human review. Each claim below is labelled *verified* (re-derived or replayed here), *reading* (taken from a cited file), or *assessment* (my judgement).

**Artifacts reviewed**, at repository commit `8b221419` (2026-09-23 23:17 −0400):

- `WZW/manuscript.tex` and all active sections (17 pages, *Thermal arithmetic orbit weights and the shifted-zeta equation*), the seven orphaned WZW section fragments in `WZW/sections/`, `WZW/README.md`, `WZW/DRAFT_HISTOR.md`, `WZW/BUILD_RECORD.json`.
- All eleven notes in `WZW/notes/` and all ten reviews in `WZW/reviews/`.
- The three parent notes that carry the WZW-proper work: `CHERN_SIMONS_WZW_AND_NATURAL_LOEWNER_EVOLUTION_20260922.md`, `SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md`, `ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md`; the synthesis `LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md`; the head of the `N4SYM` proposal.
- For context: `loewner/notes/MARKOV_PART_AND_REALIZATIONS_20260917.md`, `loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md`, `wilson-lines/notes/THE_QUARTER_SHIFT_SURVEY_20260917.md`, `wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md`, `fractional-dimension/README.md`, `LARGE_FILES.md`.

**Replays run here.** `numerics/check_wzw_loewner_pilot.py`: 72/72 pass. `WZW/numerics/check_boundary_readout.py`: 60/60 pass. (Both need NumPy and nothing else beyond the standard library.) A new standard-library programme accompanies this review (Section 6): 40 cases, 24 exact, all pass; it re-derives the pilot's finite algebra in exact arithmetic over $\mathbb Q(\sqrt3)$ and checks every identity this review asserts.

---

## 0. Summary

1. **The WZW-proper work is correct, careful and reproducible.** The proposal (22 Sep), the SU(2)$_2$ pilot (22 Sep) and the bounded collar test (23 Sep) do what they say. I re-derived the pilot's generator, its square reduction, both matrices (19) and (21), the Cardy-state growth rate $0.436388\ldots$ and the KZ blocks independently; all agree (Section 2.1).

2. **The branch's exclusions are narrower than what the repository already proves.** Four results from sibling investigations are not cited anywhere in `WZW/` or the three parent WZW notes, and each bears directly on the program: the far-field pure-delay theorem (Loewner chains cannot make the comb), the horocycle-dimension quantization (scattering-matrix realizations cannot move the offset off an integer), the quarter-shift survey (H$_3^+$, the cigar, Liouville, FZZT, ZZ and the Schwarzian wall all fail the archimedean graded invariants), and the even-tower decomposition $n_\gamma=\tfrac12(G_s+G_o)$. Taken together they say something the branch never quite says: **neither factor of $K_\omega$ makes use of the non-abelian data that motivated the Chern–Simons/WZW setting** (Section 2.3–2.4).

3. **Two corrections to the collar test's framing.** (i) A reflected readout is self-adjoint, so it cannot be the *transfer* $V_{\omega,L}$ — correct — but the *Weil form* $Q_{\omega,L}=\operatorname{Re}\langle g,G_{\omega,L}g\rangle$ is self-adjoint by construction, is what Weil positivity actually needs, and is the natural target of a Gram or reflection construction; the theorem is not an obstruction to that. (ii) The premise "matching the level spacing forces $\lambda=2$" excluded the one SU(2)$_2$ primary with unit two-point weights, the $h=\tfrac12$ triplet, which is a free Majorana fermion; at cylinder scale $\lambda=1$ the sum over its two spin structures is *exactly* $2n_\gamma$ — weights, gap and $1/u$ collision order (verified, Section 2.2). Both corrections sharpen the negative conclusion: what SU(2)$_2$ can supply for the archimedean sector is free-field content.

4. **Most of what now lives in `WZW/` is a different program** (Bost–Connes thermal weights, finite-place interfaces, thermal loads, Brownian bridge, modular Hodge scattering, fractional cusp). Its central identity is the Jordan totient $J_{2\omega}(n)$ of the fractional-dimension investigation (18 Sep, Prop. 1.2), read through a KMS state; the fractional-dimension folder is not cited. The genuine gain — a *positive* meaning for $J_d$ at the non-integer $d$ where that investigation proved no lattice exists — should be stated as such, and so should its limits (Section 3). The elementary exclusions check out.

5. **Provenance and organization** (Section 4): the reviewed 15-page WZW manuscript was overwritten in place with no `drafts/` snapshot, against the repository's own practice; seven section fragments are orphaned; the folder name no longer describes its content; the numerical programmes depend on NumPy/mpmath and none is registered in a validation script.

6. **Recommendation** (Section 5): close the WZW branch formally, as `loewner` was closed; give the thermal program its own approach-named folder; direct arithmetic effort at the continuation note's avenues 1–2 with two sharpenings — the *spectrum-condition* criterion for any construction aimed at the transfer, and Connes–Consani's archimedean-place positivity as the proven base case for the prime-free window. Do not pursue non-compact WZW reflection amplitudes, deformations of modular scattering that stay inside the scattering class, further thermal loop fitting, or larger level.

---

## 1. What the branch contains

| Piece | Where | Model | What it is | Status of its claims |
|---|---|---|---|---|
| Proposal: CS/WZW as the natural Loewner setting | parent `notes/CHERN_SIMONS_WZW…_20260922` | GPT-6 | literature-grounded pilot design | reading; sound |
| SU(2)$_2$ deterministic pilot | parent `notes/SU2_LEVEL2…_20260922`, 72 checks | GPT-6 | exact blocks, closed generator, two pairings, HS initial operator | **verified** (Section 2.1) |
| Arithmetic source as generalized Loewner flow | parent `notes/ARITHMETIC_SOURCE…_20260922`, 60 checks | GPT-6 | $m_\eta$ positive-real iff no zero right of $\tfrac12+\eta$; safe flows; $\|V_\omega\|\le e^{bL}$ | reading; correct where I checked |
| Original WZW manuscript (15 pp.) | *overwritten*; sections `02_boundary`…`08_outlook` orphaned | GPT-6 | synthesis of the two above | not recoverable from HEAD |
| Bounded collar readout test | `WZW/notes/BOUNDED_ARITHMETIC_READOUT…`, 60 checks | GPT-6 | self-adjoint-causal theorem; primary weights $(3/8)_n/n!$ | **verified**; framing corrected (2.2) |
| Research avenues | `WZW/notes/RESEARCH_AVENUES…` | GPT-6 | four options, 2-state storage control | reading; sound |
| Independent-source search; Brownian; modular Hodge; fractional cusp | four notes, 51+65+80 checks | GPT-6 | scoped negative tests; $\omega=\tfrac12$ Hodge benchmark | reading; not re-derived here |
| Bost–Connes orbit weights; finite-place interface; thermal boundary | three notes, 87+144+203 checks | GPT-6 | $c_n=n^{(\beta-1)/2}\varphi_\beta(P_n)$; two interface exclusions; front rigidity | spot-checked (Section 3) |
| Current manuscript (17 pp.) | `WZW/manuscript.tex` | GPT-6 | the thermal program; WZW is §7, one paragraph | reading |
| Continuation and lessons | `WZW/notes/CONTINUATION_AFTER_THERMAL…`, parent `LESSONS_FROM_WZW…` | GPT-6 | five avenues; N4SYM handoff | assessment in Section 5 |

The WZW question proper occupies three notes and one paragraph of the live manuscript. Everything else under the folder name is the arithmetic program that grew out of the WZW failures.

---

## 2. The WZW-proper results

### 2.1 The pilot — verified

The pilot's algebra is exact and I re-derived it independently, in exact arithmetic over $\mathbb Q(\sqrt3)$ where the statement is exact (programme groups A1–A8, A16) and to $10^{-12}$ where it is not (A9–A15):

- the spin identities $D+C+B=-\tfrac32 I$, $D^2=\tfrac34I-D$, $C^2=\tfrac34I-C$, $DC+CD=B$ (eq. 7, 17);
- the Ward/KZ generator (16) reduces to $\dot M=-\nu(2Q^2+\dot uQ)M$ (eq. 1) for arbitrary rational $(a,b,\dot u)$ — the reduction is an identity, not a coincidence of the tested geometry;
- $G$ at $(a,b)=(1,2)$ equals (19) for $\dot u=0$ and (21) for $\dot u=4$; $\det Q=-\tfrac34(1/a-1/b)^2$;
- the blocks (10)–(11) satisfy the KZ system (8) (residual $2.6\times10^{-12}$ with a sixth-order stencil) and have the stated Frobenius leading terms;
- $M_0$ matches (13) to $6\times10^{-15}$; the Cardy-selected state's initial norm derivative at $\dot u=4$ is $0.436388495438834$ (to $2\times10^{-16}$) and positive; at $\dot u=0$ it is negative; $\langle e_0,2Ge_0\rangle=\tfrac9{16}$ exactly.

*Assessment.* The pilot establishes exactly what it claims: a nonconstant finite BCFT observable under deterministic Loewner transport, with the tensor pairing and the Chern–Simons gluing pairing correctly distinguished, a genuine counterexample to all-driver contraction in the tensor pairing, and a Hilbert–Schmidt (hence non-identity) initial operator for the raw smeared kernel. Two remarks the pilot does not make:

- Identity (18), $\|M_T\|^2+4\nu\int_0^T\|QM\|^2\,dt=\|M_0\|^2$, is a cumulative-storage identity of precisely the shape the continuation note's avenue 1 asks for — in dimension two, with the KZ connection contracted with the Loewner velocity field as the storage density. The two-state oscillator control in `RESEARCH_AVENUES` §1 is its cousin. Neither has an input waveform, which is the whole difficulty.
- The module-level version of the pilot's evolution is the Bauer–Bernard operator $-2L_{-2}-\dot uL_{-1}$ acting on the boundary module in the tip-centred frame; the pilot's (1) is its finite shadow through Sugawara. Since $L_{-2}$ raises the level, that operator is not a contraction on the module in the module's own inner product. The pilot's constant-driver contraction is a property of the evaluated, conformally weighted tensor pairing, as the pilot itself warns in §6. Anyone resuming "sewing with descendants" should start from this fact rather than from (18).

### 2.2 The collar test — theorem verified; framing corrected

**The theorem is airtight** (reading; proof checked): if $T$ is bounded, self-adjoint and causal on scalar $L^2(0,L)$, then $P_aT(I-P_a)=0$ and its adjoint give $[T,P_a]=0$ for all $a$, so $T$ is multiplication by an $L^\infty$ function; a compact such $T$ is zero. Hence $J^*S_sJ$ is never causal and never equals $V_{\omega,L}$. The finite shadow is programme case C7.

**Correction (i): the transfer is the wrong target for a reflected readout; the form is the right one.** The shifted Weil criterion is positivity of the quadratic form $Q_{\omega,L}(g)=\operatorname{Re}\langle g,G_{\omega,L}g\rangle$ on the window, equivalently contractivity of $V_{\omega,L}$ (the dichotomy). The form is a *self-adjoint* object: its kernel is the even extension $2\cosh(\omega(x-y))\,g^+(|x-y|)$ plus the contact and the prime atoms (Wilson-lines Theorem 3.1). A reflected Euclidean pairing $\langle f,J^*S_sJf\rangle$ *is* a form, and self-adjointness is exactly what it should have. So the theorem excludes reflected constructions of $V$ and says nothing against reflected constructions of $Q$ — which is what a Gram construction would prove positive. The obstacles to a collar-type form are the kernel comparisons in the note's §4–5 (tower weights, contact, pole term, atoms), not §3. This matters for Section 5: constructions aimed at the *form* may use reflection positivity; constructions aimed at the *transfer* need something else (the spectrum condition, Section 5.B1). The collar note conflates the two targets, and the lessons note inherits the conflation ("reflection positivity should help construct accumulated storage").

**Correction (ii): the unit-weight primary is the fermion, and the gap is fixed by the second spin structure.** The note's §4.2 sets $\lambda=2$ to match the archimedean spacing $2$, obtains weights $(3/8)_n/n!$ and collision order $u^{-3/8}$ for the $h=\tfrac3{16}$ spin field, notes that the $h=\tfrac12$ field has "unit binomial weights" but "gap 1 rather than 1/2", and moves on. The following is verified (programme B1–B10):

- $(2h)_n/n!=1$ for all $n$ **iff** $2h=1$ (B1, B4). In SU(2)$_2$ that is the spin-1 primary, $h=\tfrac12$, which in the three-Majorana description is the fermion triplet $\psi^a$.
- At cylinder scale $\lambda=1$ its two-point function is $G_s(u)=1/(2\sinh(u/2))=\sum_{n\ge0}e^{-(n+\frac12)u}$: offset $\tfrac12$, spacing $1$ (B6). The other spin structure gives $G_o(u)=1/(2\cosh(u/2))=\sum(-1)^ne^{-(n+\frac12)u}$ (B8). Their sum is
  $$G_s+G_o=2\sum_{n\ge0}e^{-(2n+\frac12)u}=2n_\gamma(u)$$
  to $10^{-15}$ (B5): offset $\tfrac12$, spacing $2$, unit weights, and $2n_\gamma(u)\,u\to1$ — the $1/u$ collision the form requires (B9). The $\lambda=2$ single tower is $1/\sinh u=2\sum e^{-(2n+1)u}$, offset $1$ (B7): that is the note's "gap 1", and it is an artefact of the premise.

This is the same identity as the wilson-lines even-tower decomposition $n_\gamma=\tfrac12(G_s+G_o)$ (18 Sep), seen from the SU(2)$_2$ side: the D3–D5 same-ray/opposite-ray kernels are the fermion's two spin structures. It is also consistent with the note's own Beta formula: the Laplace susceptibility $\lambda^{2h-1}B(p/\lambda+h,1-2h)$ diverges logarithmically at $h=\tfrac12$, which is the $1/u$ singularity that becomes the contact term.

*Assessment.* Correction (ii) is not a rescue. It says that the one place SU(2)$_2$ matches the archimedean sector exactly is its *free-fermion* subsector — the non-abelian current algebra, the Cardy labels and the Chern–Simons gluing play no role in it. The pilot's $h=\tfrac3{16}$ field is the fermion's twist field; that is why its weights are $(3/8)_n/n!$. Record the dictionary once and stop.

### 2.3 Four results elsewhere in the repository that the branch does not cite

None of these appears in `WZW/`, in the three parent WZW notes, or in the lessons note. Each is a *reading* of a sibling note; each is checked to be as stated.

(a) **Far-field transport is a pure delay** — `loewner/notes/MARKOV_PART_AND_REALIZATIONS_20260917.md`, Proposition 2.1, and the lemma in `wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md` §3.2 (rotation-averaged composition operators on analytic functions are pure dilations). Consequence: no Loewner chain, deterministic or stochastic, produces the prime comb; the comb is the Hecke/Bost–Connes operator $\sum\tilde c_n\mu_n$ (same note, §2). The WZW proposal's hope that "the arithmetic comparison follows the construction" was therefore already known to fail for the comb before the pilot was written.

(b) **Scattering-matrix realizations quantize the offset** — `loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md` §3.2: the offset of a cusp scattering matrix is the dimension of the horocycle it integrates over, hence an integer; the shifted transfer's offset is $2\omega$. This bears directly on the current manuscript's avenue 3 ("global deformations of modular scattering") and on the fractional-cusp test: any deformation that stays within the class of automorphic scattering matrices cannot move $2\omega$ off $1$. The first test of a proposed deformation is not the front exponent but whether it has left that class.

(c) **The quarter-shift survey** — `wilson-lines/notes/THE_QUARTER_SHIFT_SURVEY_20260917.md` item 4: bulk Liouville, FZZT, ZZ, H$_3^+$, the Schwarzian/JT wall, the SL(2,$\mathbb R$)/U(1) cigar and the full-line inverted oscillator all fail the dictionary-free graded invariants $I_{2m}$ of the archimedean factor, most already at $I_2$; the sole survivor is the half-line inverted oscillator (Bhaduri–Khare–Law) and its $c=1$ matrix-model realization. So the obvious "non-compact WZW reflection amplitude" continuation of the WZW program — the level-dependent Gamma ratios of H$_3^+$ and the cigar — was surveyed and excluded six days before the WZW folder opened. It should not be reopened.

(d) **The even tower** — `wilson-lines/notes/REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md`: $n_\gamma=\tfrac12(G_s+G_o)$, $G_o$ regular with positive transform, the $1/(2u)$ singularity carried by $G_s$. This is correction (ii) above, already in the repository.

### 2.4 The structural conclusion

*Assessment.* Put (a)–(d) together with the pilot and the collar test and the picture is complete enough to close the branch:

- **Conformal transport is composition plus local Jacobians.** A Loewner map acts on a boundary field's position by $g_t$ and multiplies by $g_t'(x)^h$. Composition operators are never convolutions except for translations and dilations (source note §7.2, "multiplication is not composition"); Jacobians are multiplication operators in position space. So a single transported field can never produce a nonlocal Volterra kernel.
- **Nonlocality comes only from the OPE, whose singularities sit at coincident points.** The pilot's four-point kernel $M_t(x,y)$ is nonlocal, but its only singularities are the powers $|x-y|^{-2h}$ at $x=y$; in the logarithmic coordinate that is $u=0$. Boundary correlators are analytic away from coincidence (locality). Atoms at $u=\log n$ would be singularities at $x/y=n$, which no correlator on a smooth domain has.
- **Atoms at $u=\log n$ need the domain to be identified under integer dilations.** The modular surface has exactly that — the lattice, $SL(2,\mathbb Z)$ — which is why the $\omega=\tfrac12$ Hodge benchmark works; and once the domain is an arithmetic quotient the offset is a horocycle dimension, which is (b). So the one mechanism that produces the comb is the one that freezes the shift.
- **The archimedean sector needs no non-abelian data.** It is the parity-projected free-fermion tower (2.2), equivalently the even sector of a harmonic oscillator, equivalently the half-line inverted oscillator's phase (c). Nothing in SU(2)$_k$ beyond its free-field content is used.

Hence the Chern–Simons/WZW structure — Wilson-line endpoints as conformal-block labels, gluing, fusion — does no work on either factor of $K_\omega$. The pilot is a good piece of finite BCFT and the collar theorem is a good operator lemma; neither points at a continuation *in this setting*.

Two further ideas were considered while writing this and are recorded so they are not re-invented: the Galois action on WZW modular data (Coste–Gannon) and on Bost–Connes KMS states — but the BC symmetry lives on the *extremal* states at $\beta>1$, while the manuscript's range $\beta=2\omega\le1$ is the unique-KMS phase where that action is trivial; and Eisenstein series on affine Kac–Moody groups (Garland; Braverman–Kazhdan–Patnaik), the one place where level-$k$ affine algebras and zeta constant terms genuinely meet — but by the (affine) Gindikin–Karpelevich structure each factor is $\zeta(\langle\lambda,\alpha\rangle)/\zeta(\langle\lambda,\alpha\rangle+1)$, a unit shift per root, so (b) applies factor by factor. (Both *assessment*, not checked in detail.)

---

## 3. The thermal / interface program housed in `WZW/`

### 3.1 The coefficient identity is the Jordan totient read through a KMS state

The manuscript's central identity $c_n(\omega)=n^{(\beta-1)/2}\varphi_\beta(P_n)$, $\varphi_\beta(P_n)=\prod_{\ell\mid n}(1-\ell^{-\beta})$, $\beta=2\omega$, is (verified, C1–C4)
$$c_n(\omega)=\frac{J_{2\omega}(n)}{n^{\omega+1/2}},\qquad J_d(n)=n^d\prod_{\ell\mid n}(1-\ell^{-d}),$$
which is Proposition 1.2 of the fractional-dimension opening note (18 Sep): "the comb's weights are the Jordan totient, $\tilde c_n=J_d(n)/n^{(d+1)/2}$", with $d=2\omega$. The manuscript states the integer-$d$ counting interpretation (§3.1) but does not cite the investigation that found it, nor the loewner note (17 Sep, §2) that first named the comb a Bost–Connes operator. Both should be cited; the priority inside the project is theirs.

What the KMS reading adds is real and should be stated plainly: the fractional-dimension investigation proved that for $d\in(0,1)$ there is no lattice — $\theta(it)^{d+1}$ is not completely monotone, $r_{d+1}(3)<0$ — so "count primitive vectors in $(\mathbb Z/n)^d$" has no object. The Bost–Connes system replaces the nonexistent count by the *probability* of primitiveness under a positive equilibrium state, which exists for every $\beta\in(0,1]$. That is a genuine reinterpretation of $J_d$ at non-integer $d$.

Its limits are equally sharp, and the manuscript states most of them; two are worth adding:

- $0<\beta\le1$ is the *high-temperature, unique-KMS* phase of the BC system. Its arithmetic content — the $\mathrm{Gal}(\mathbb Q^{ab}/\mathbb Q)$ action on extremal KMS states — is confined to $\beta>1$, i.e. $\omega>\tfrac12$, exactly the vacuous range of the criterion. The range that matters is the range where BC has no symmetry to offer.
- BC has no archimedean place. The manuscript's completion $A_\omega$ is adjoined by hand, and the finite-Euler completion pole (§5.4) is the precise price: deleting primes while keeping the full archimedean factor leaves the pole that $1/\zeta(s_+)$ would have cancelled. This is not a defect of the test; it is a statement that any BC-based realization must be *adelic* from the start, which is where Connes' later work lives (Section 3.3).

### 3.2 The exclusions

The bare-Euler-train exclusion, the product-vacuum obstruction, the fixed-bounded-readout limitation, the finite-Euler pole and the front-rigidity proposition are elementary and correct as far as I checked (the proofs are two to five lines each; the $S-K$ algebra and the $\lambda C/(2p)$ correction are right). Two remarks:

- The bare Euler train (§4.3) is a straw man the manuscript itself immediately qualifies; it should not be listed among the results.
- Across *every* test in this folder — Loewner, collar, Brownian, modular, fractional, thermal loops, thermal loads — the invariant of failure is the same: **nothing derives $\log n$ as a delay.** A thermal energy label, a Loewner capacity, a diffusion clock and a first-passage time are each *one* parameter; the comb is a *multiplicative convolution* over $\mathbb N^\times$. This is (a) of Section 2.3 restated, and it is the sentence the manuscript's §7 should contain.

### 3.3 Literature the folder should connect to

The independent-source search (23 Sep) says "adelic scaling and semilocal Fourier theory remain the strongest arithmetic-geometric explanation of prime delays" and then does not pursue it. But the repository already has the references: `PROGRAM_OVERVIEW.md` cites Connes–Consani, *Weil positivity and trace formula, the archimedean place* (arXiv:2006.13771), and `brainstorm/ASSESSMENT.md` cites *Quasi-inner functions and local factors* (2008.10974) and Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators* (2310.18423), with their theorem numbers. The first proves positivity of the archimedean contribution to the Weil form for test functions of small enough logarithmic support — the prime-free window; the exact support range is in the paper — through the Sonin space and a scaling Hamiltonian (reading from memory of the paper, not re-checked here). That is the *proven base case* of the continuation note's avenue 1, and the semilocal papers are the framework for adjoining the place $2$. The WZW manuscript's §4.2 mentions "the canonical Sonin embeddings studied elsewhere in the project" without a link; avenue 1 should be phrased against these results, not next to them. (Suzuki is cited correctly throughout, with the $\omega>1$ range kept distinct from unconditional innerness at $\omega\ge\tfrac12$.)

---

## 4. Provenance and organization

These are observations against the repository's own stated conventions, not against the branch's mathematics.

1. **The reviewed WZW manuscript no longer exists.** `BUILD_RECORD.json` records an "earlier delivery": *Boundary WZW evolution and the arithmetic Loewner source*, 15 pages, PDF sha256 `904bb620…`, "superseded in place; no dated snapshot created". `DRAFT_HISTOR.md` calls it an "initial uncommitted working-tree version". So the manuscript that `review_codex_manuscript_20260923.md` audited was never committed and was overwritten before the folder was committed. The parent investigation snapshots every version under `drafts/2026-09-*-v0*`; `WZW/` has no `drafts/` at all and its `DRAFT_HISTOR.md` instructs "do not create dated manuscript snapshots". That instruction contradicts the practice of every other investigation in `papers/susy-positivity/`. The seven orphaned sections (`02_boundary` … `08_outlook`) survive; the original scope section and validation appendix do not. A compile test here (live `preamble.tex` and `references.tex`, the seven fragments, no scope section) produces 12 pages; seven citation keys the fragments use were dropped from `references.tex` in the pivot (`ABI`, `ABM`, `BCDM`, `BPPZ`, `Cardy`, `Lagarias`, `LagariasCorrection`), and nothing else is missing. Reconstruction is a short task.

2. **The folder name and its content have diverged.** By the naming decision of 18 Sep (`fractional-dimension` opened rather than renaming `loewner`), investigation folders are named for the *approach tested*. `WZW/` now carries a Bost–Connes manuscript, and the parent README's first paragraph points to `N4SYM`. Nobody looking for the thermal program will look under `WZW`, and nobody looking for the WZW result will expect to find it as one paragraph of a thermal manuscript.

3. **Numerics.** All seven `WZW/numerics/check_*.py` programmes and the two parent WZW programmes require NumPy and/or mpmath; none is standard-library; none is registered in a `validation/drafts.py` or `endpoint_matter.py`-style script, so `check --replay` in the parent does not exercise them. Records are present and hashed, which is good; the replay instructions work (I ran two). Per the repository's convention, either register them or state the exemption in `numerics/README.md`.

4. **Attribution and review.** Every file is attributed to GPT-6 (Codex) with the effort setting recorded as "not exposed"; the acknowledgement appendix is present in the manuscript. All ten reviews are same-assistant audits and say so. This review is the first cross-model review of the branch.

5. **Sizes.** No file in `WZW/` approaches the 1 MB convention (largest is `manuscript.pdf`); `LARGE_FILES.md` is respected.

---

## 5. Viable paths forward, ranked

### A. Close the WZW branch (one bounded session) — recommended first

Deliverables, following the `loewner` closure as the template:

1. A closing note in `WZW/notes/` stating the four uncited results (2.3), the two corrections (2.2), and the structural conclusion (2.4), with the fermion dictionary recorded once and cross-linked to the even-tower note.
2. A closing header at the top of `WZW/README.md` and a sentence in `wilson-loewner/README.md`, as `loewner/README.md` has.
3. Reconstruct the WZW manuscript from the seven orphaned sections plus a short scope section that records the closure and a validation appendix, restore the seven dropped bibliography entries, and snapshot it under `WZW/drafts/2026-09-24-v01/`. The fragments compile (Section 4, item 1); this repairs the provenance gap. Retire the "no dated snapshots" line from `DRAFT_HISTOR.md`.
4. Register the check programme accompanying this review (standard library, Section 6) and either register the existing NumPy/mpmath programmes or record the exemption.
5. Move the thermal program's manuscript, notes, numerics and reviews to a new approach-named folder (`investigations/thermal-orbit-weights/` or similar), leaving pointers in `WZW/`; historical paths inside notes stay as they are, per the naming decision's provenance rule.

Decision criterion: after this session, a reader arriving at `WZW/` learns in one screen what was tested, why it closed, and where the continuing arithmetic work lives.

### B. The arithmetic effort: avenues 1–2 of the continuation note, sharpened

The continuation note's ranking (cumulative storage on $\log2<L<\log3$; explicit canonical systems) is right. Three sharpenings:

**B1. The spectrum-condition criterion** (*assessment*). Any construction aimed at the *transfer* must derive causality — innerness — from something. In quantum field theory that something is the spectrum condition: positive energy plus locality make Wightman functions boundary values of functions analytic in the forward tube, and make S-matrices and retarded responses analytic in the physical half-plane. That is the only mechanism by which a physical realization *would* prove RH rather than assume it. So a candidate for $V_{\omega,L}$ should present $K_\omega$ as the boundary value of a positive-energy object — a reflection amplitude, a retarded response — and the first question to ask of it is "which positive operator supplies the analyticity?" Euclidean Gram and reflection pairings cannot play this role: they are self-adjoint and yield forms. Conversely, constructions aimed at the *form* may use reflection positivity and should be judged on the kernel comparison, not on causality. The collar note conflated the two targets; future notes should name their target in the first paragraph.

**B2. State avenue 1 against its proven base case.** For the prime-free window the positivity of the archimedean Weil form is a theorem (Connes–Consani, 2006.13771), with the Sonin space as the positive Hilbert structure and an explicit remainder. Avenue 1 is then: extend from the place $\{\infty\}$ to the semilocal place set $\{\infty,2\}$ on $\log2<L<\log3$, with the semilocal framework of 2008.10974 / 2310.18423 as the comparison. The decision criterion stays as written (a derived non-negative storage expression, or an explicit obstruction term).

**B3. Avenue 2 as stated.** Suzuki's explicit construction at $\omega>1$; the extension problem into $(0,\tfrac12)$ is the deliverable, with the innerness assumption kept out of the construction. No change.

### C. Not recommended, with the reason on record

1. *Non-compact WZW reflection amplitudes* (H$_3^+$, SL(2,$\mathbb R$)/U(1), Liouville, FZZT, ZZ, Schwarzian): excluded by the quarter-shift survey's graded invariants (2.3c).
2. *Global deformations of modular scattering* that remain automorphic scattering matrices: excluded by the horocycle-dimension quantization (2.3b). A deformation is admissible only if it leaves that class — for instance by changing the domain's identifications rather than its metric — and its first test is the offset, not the front exponent.
3. *Further regular finite-place parallel loads*: the front-rigidity proposition is decisive for finite spectral mass; infinite spectral mass is an escape from the hypothesis, not evidence.
4. *Larger level, more blocks, coefficient fitting*: the pilot and collar note already say so; Section 2.4 says why.
5. *Affine Kac–Moody Eisenstein series* as a "WZW meets zeta" locus: unit shifts per root; (2.3b) applies factor by factor (*assessment*, Section 2.4).

### D. Optional, small and arithmetic-neutral

The avenues note's item 4 — whether the completing-square scalar $\exp[-\tfrac\nu8\int\dot u^2]$ is a sewing anomaly. The observed equality with $\exp[-cI_T/24]$ holds only at $k=2$ (verified, C5–C6: $\nu/4=c/24$ with $\nu=1/(k+2)$, $c=3k/(k+2)$ iff $k=2$). A perturbative test about a constant driver is a day's work and would settle whether it is a coincidence. Its outcome would not touch the arithmetic; it belongs in a closing note, not on the critical path.

### E. Outside this review's brief

The `N4SYM` proposal and the YM hierarchy are the parent program's business. One transferable point from this review: its exclusion-transfer table (lessons note §8) is sound, and criterion B1 applies there too — the displacement-operator sector supplies a *retarded* response, which is the right kind of object for the transfer, and the proposal correctly separates Euclidean shape derivatives from it.

---

## 6. Checks accompanying this review

**Programme:** `check_wzw_program_review.py` (standard library only; sha256 `77ae7b0da9363d2c85a59df0be9490941e4df8a8bcf1bb3fde9daa538c6434dd`). **Record:** `wzw-program-review-20260924.json`. **Cases:** 40, of which 24 exact (rational or $\mathbb Q(\sqrt3)$) and 16 floating; all pass.

| Group | Cases | What is checked |
|---|---|---|
| A | 22 | Pilot: spin identities (7),(17); Ward/KZ reduction to (1) at five rational geometries; (19),(21); $\det Q$; KZ blocks (10)–(11) and Frobenius terms; $M_0$ (13); growth $0.436388\ldots$ at $\dot u=4$, decay at $\dot u=0$; $\langle e_0,2Ge_0\rangle=9/16$ |
| B | 10 | $(2h)_n/n!=1\iff 2h=1$; collar weights $3/8,33/128,209/1024$; $G_s+G_o=2n_\gamma$; scale-1 vs scale-2 fermion towers; $(-1)^n$ alternation of $G_o$; $1/u$ collision; regularity of $G_o$ |
| C | 7 | $c_n(\omega)=J_{2\omega}(n)/n^{\omega+1/2}$; $\omega=\tfrac12$ gives $\varphi(n)/n$ exactly; multiplicativity; integer-$d$ counting; $k=2$ anomaly coincidence unique; causal + self-adjoint finite matrix is diagonal |
| D | 1 | $q_\omega(u)\sim A_\omega u^{\omega-1}$, $A_\omega=(2\pi)^\omega/\Gamma(\omega)$ |

Replay:

```sh
python3 -B check_wzw_program_review.py --output /tmp/wzw-program-review-replay.json
```

Suggested locations: programme in `WZW/numerics/`, record in `WZW/numerics/records/`, this file in `WZW/reviews/`. Suggested index lines are given in the accompanying message.

**What these checks are not.** Finite identities and floating diagnostics supporting the statements of this review. They certify nothing about positivity, realizations, or zeros, and they do not replace specialist review of either the pilot's BCFT input or the thermal program's KMS input.
