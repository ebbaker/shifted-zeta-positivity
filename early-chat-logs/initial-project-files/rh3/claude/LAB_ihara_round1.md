# LAB — Ihara laboratory, round 1: the finite chain built, the Siegel anatomy realized, both ω-flow indices decided

**2026-08-29.** Executes §3.4 of `NOTE_variation_axes.md` (the memo's Ihara-laboratory avenue,
queued first there). Everything below is computed and verified this session at 60–200 digits;
scripts in §9. For finite (q+1)-regular graphs the entire chain of the ζ programme —
Ψ_ω → Herglotz response → spectral measure → Kreĭn string — is **finite and exact**, and the
graph RH-analogue (Ramanujan) is realized as string admissibility. The main yields: the finite
Siegel anatomy (three inequivalent criteria, separated on actual graphs), both ω-flow indices
computed with crossings pinned at ω = δ (memo item 6 decided), the UV/IR localization of
violations and of covering-space topology in the bulk, and the universality of the early bulk
toward the universal-cover (Kesten–McKay) string.

## 0. Findings at a glance

| # | finding | where |
|---|---|---|
| F1 | Ramanujan ⟺ q_X Stieltjes ⟺ positive beaded string; 20+ graphs, no exceptions; CF round-trips ≤ 1e−160 | §3 |
| F2 | per-vertex bulk → universal-cover (KM) string; early (UV) beads universal, far (IR) end carries the gap | §4 |
| F3 | finite Siegel anatomy: exc+ (λ>2√q) invisible to Ψ at every shift and to Pick, visible to support; exc− (λ<−2√q) visible to all three | §5 |
| F4 | Siegel shielding realized: synthetic shield restores Ψ ≥ 0 over a violating configuration; natural shielding delay on prism C17 | §5 |
| F5 | ω-flow: κ_Pick(ω) drops at ω = δ_N, support-leak dies at ω = δ_P; both = zero counting exactly (memo item 6: repackaging confirmed, but the two indices separate the violation types) | §6 |
| F6 | covers: BD(K4)=Q3 and BD(Petersen)=Desargues exact; UV bead preserved base→cover; the twisted (topological) spectrum lands at the IR end with the heaviest beads | §7 |
| F7 | ceiling: for regular graphs everything factors through the spectrum — cospectral graphs share a bulk; beyond-spectrum topology needs irregular graphs or edge data (round 2) | §8 |
| F8 | violation-position law: exc− anomalies at bead 3–4 (UV section) in all four specimens regardless of size (2N = 20…80); exc+ anomalies at bead 9–10 in all four specimens; depth ≈ size-independent — mechanism open | §5.3 |

## 1. Setup and conventions

Graph X finite, connected, simple, (q+1)-regular (all data below: cubic, q = 2). Ihara zeta via
Bass: `ζ_X(u)^{-1} = (1−u²)^{|E|−|V|} det(I − Au + qu²)`; the exponent is −χ(X). Nontrivial
eigenvalues: all λ except q+1 (and −(q+1) when bipartite). Each nontrivial λ (mult m) is
encoded by θ with `λ = 2√q cos θ` (ordinates in units of log q):

| class | condition | θ | ζ-analogue |
|---|---|---|---|
| tempered | \|λ\| ≤ 2√q | τ ∈ [0,π] | on-line zero pair |
| exc+ | λ > 2√q | iδ, δ = acosh(λ/2√q) | **real zero pair ½±δ (Siegel type)** |
| exc− | λ < −2√q | π − iδ | offset pair at height π |

**Truncation choice (flagged).** The s-plane zeta is periodic (period 2π in these units); only
the principal zeros are kept. The dropped 2πℤ towers are the graph's "gamma factor"; the
periodic-tower variant (infinite string with explicit UV tower) is a round-2 item. Each
eigenvalue deposits total weight 2m on atoms t = γ²: tempered 2m at τ² > 0; exc+ 2m at −δ² < 0;
exc− m at each of (π∓iδ)² (conjugate pair).

Response `q_X(z) = Σ w_j/(t_j − z)`. Shifted family
`h_ω(w) = Σ pairs [1/(ω+w−iγ) + 1/(ω+w+iγ)]`, `q_ω(z) = h_ω(√(−z))/√(−z)` (exc−: half-weight
over γ and γ̄, keeping analyticity and reality). Screw function, pair ρ = ½ ± iγ:
`T(t) = Σ_± (e^{bt}−1−bt)/b²`, `b = ±iγ − ω` — checked against both anchors: ω=0 real γ gives
`2(1−cos γt)/γ²`; a real pair gives growth `e^{(δ−ω)t}/(δ−ω)²` (the shielding term of
PROGRESS §2, matched numerically to 5 digits at t = 40).

**String convention** (fixed by the 1-mass case, round-trip verified): first mass at the
measuring end x = 0, Dirichlet wall at the far end;
`q(z) = 1/(−z m₁ + 1/(l₁ + 1/(−z m₂ + …)))`; `q(0) = total length` (the Kasahara `ℓ = h(0)`
anchor of ROUND19). Inversion by exact polynomial Stieltjes CF at dps 80–200.

## 2. Machinery validation

| check | result |
|---|---|
| Bass identity `det(I−Au+qu²) = u^n p_A((1+qu²)/u)`, random complex u | ≤ 1e−40 |
| K4 closed form `ζ^{-1} = (1−u²)²(1−u)(1−2u)(1+u+2u²)³` [Terras] | 4e−41 |
| exact charpoly (Faddeev–LeVerrier over ℤ) + Yun square-free + mp roots | exact mults |
| CF round-trip (atoms → P/Q → string → q), incl. 39-atom graphs | ≤ 1e−160 |
| 1-mass string by hand: m = 1/w, l = w/t; q(0) = Σ lengths | exact |
| q_ω at ω=0 ≡ atom form, all three violation kinds | ≤ 1e−60 |
| Ψ series vs closed tempered form; synthetic real-pair growth rate e^{δ−ω} | 0.0; 5 digits |

## 3. Census (cubic): Ramanujan ⟺ string admissibility

20 graphs: K4, K3,3, Q3, crown(4), Petersen, Heawood, Desargues, prisms C3–C17, Möbius ladders,
dumbbells (two K4−e blobs joined by a ladder of k rungs), random cubics n = 12–40. **Every
Ramanujan member yields an all-positive CF (Stieltjes string); every non-Ramanujan member
yields CF anomalies** — no exceptions. (This is a theorem — support ⊂ (0, π²] ⟺ Stieltjes — the
census confirms the pipeline computes it.) Sample values, `L = q(0)`:

| graph | n | b₁ | Ram | L | string (m,l,…) |
|---|---|---|---|---|---|
| K4 | 4 | 3 | yes | 1.6072 | [0.1667, 1.6072] |
| Petersen | 10 | 6 | yes | 8.2776 | [0.0556, 5.488, 0.1448, 2.790] |
| Heawood | 14 | 8 | yes | 13.678 | [0.0417, 8.754, 0.1157, 4.924] |
| prism C9 | 18 | 10 | **NO** (exc− δ=0.1895) | — | anomalies §5 |
| dumbbell+4 | 16 | 9 | **NO** (exc+ δ=0.0988) | — | anomalies §5 |

Structure: first mass exactly `m₁ = 1/Σw = 1/(2(n−1))` (bipartite: 1/(2(n−2))); masses increase
and gaps shrink along the string — light UV beads at the measuring end, heavy IR beads at the
far end (Möbius(4): last mass 30.0 after m₁ = 0.071). The lowest-τ atom (spectral gap)
contributes 30–83% of the total length across the census: **the string length is dominated by
the spectral gap; the gap lives at the far (IR) end.** A long-bridge dumbbell drives τ_min down
(dumbbell+2: 23.6/31.9 of L from the gap atom) until at k = 4 rungs the gap eigenvalue crosses
2√2 and the graph leaves the Ramanujan class — the string "detects" the impending violation by
its diverging IR end.

## 4. Universality: the early bulk is the universal cover's

Per-vertex limit: Kesten–McKay measure pushed to t = τ², total mass 2;
`ℓ∞ = Q∞(0) = 3.802299…` (per-vertex limit length). Per-vertex strings (q → q/n: masses ×n,
lengths /n), first beads, against the K=12 Gauss discretization of the KM measure:

| | m̃₁ | l̃₁ | m̃₂ | l̃₂ | L/n |
|---|---|---|---|---|---|
| KM (tree) | 0.5 | 0.667 | 0.815 | 0.462 | 3.802 |
| K4 (n=4) | 0.667 | 0.402 | — | — | 0.40 |
| Petersen (10) | 0.556 | 0.549 | 1.448 | 0.279 | 0.83 |
| rand24 | 0.522 | 0.618 | 1.020 | 0.363 | 2.09 |
| rand40 | 0.513 | 0.627 | 0.855 | 0.375 | 1.93 |

`m̃₁ = n/(2(n−1)) → ½` exactly; deeper beads converge more slowly (bead k is a functional of the
first ~2k moments of the empirical τ²-distribution, so convergence is at the
Benjamini–Schramm/empirical-spectral rate, and depth costs moments). Stieltjes-transform
distance |q/n − Q∞| at z = −1 falls 0.42 → 0.052 from n = 4 to n = 40. The far end never
converges — it carries the gap (§3). **The locality/globality split is realized as position
along the string: UV = local = universal (tree), IR = global (gap, topology §7).** Caveat: the
K-point KM discretization truncates the IR tail (K=12 length 2.70 vs ℓ∞ = 3.80) — the tree
string's own IR needs the closed form (round 2).

## 5. Violation anatomy: the finite Siegel structure

Specimens: dumbbell+4 (pure exc+, δ=0.0988), prism C9 (pure exc−, δ=0.1895, mult 2), prism C17
(both: δ_P=0.1605, δ_N=0.3106), rand40 seed 4 (a random cubic that happens to violate: one exc−,
δ=0.1822), Petersen (control).

### 5.1 Three detectors, two violation types

| detector | exc+ (real zeros) | exc− (height-π zeros) | control |
|---|---|---|---|
| Ψ ≥ 0 (screw positivity) | **BLIND**: min Ψ = +0.006 on (0,40]; stays ≥ +0.017 at ω = 0.05, 0.2, 0.4 | visible: C9 first dip t=25.8, min −385 | ≥ 0 |
| Pick κ (Nevanlinna) | **BLIND**: κ = 0 | κ = 1–2 | 0 |
| support (Stieltjes/string) | **detects**: atom at t = −δ² < 0 | detects: conjugate complex atoms | clean |

So the three criteria are strictly ordered in sensitivity — screw positivity ⊂ Nevanlinna ⊂
Stieltjes — and the gaps between them are exactly the two violation types. This refines
PROGRESS §2's Siegel-blindness: for ζ-like systems with no real zeros the three coincide;
here all three inequivalences are realized by explicit graphs. A random cubic at n = 40 already
realizes the exc− type (rand40 s4) — violations are not exotic.

### 5.2 Shielding (Fejér extremals are graph-realizable)

Synthetic (labelled): C9's violating configuration plus an artificial real pair at
δ_P = δ_N + 0.15 has min Ψ = **+0.0072** on (0,40] — the real-zero term lifts the oscillation
above the axis, exactly Prop. 9.5(iii) / NOTE_oneside §5. Natural: prism C17's own exc+
(δ_P = 0.16 < δ_N = 0.31) cannot shield forever but **delays** the first dip to t = 39.9
(vs 25.8 for C9, though C17's δ_N is larger).

### 5.3 Where the violation lands in the bulk (F8)

CF anomaly positions (index / 2N), all verified at dps 160 with exact round-trips:

| graph | type | anomaly indices / 2N |
|---|---|---|
| prism C9 | exc− | 6,7 / 20 |
| prism C11 | exc− | 5,6 / 24 |
| rand40(s4) | exc− | 7,8 / **80** |
| prism C17 | both | 5,6 / 36 **and** 19 / 36 |
| dumbbell+4 | exc+ | 17 / 26 |
| dumbbell+6 | both | 7,8 / 36 and 17 / 36 |
| dumbbell+8 | both | 6,7 / 44 and 17 / 44 |

Pattern: **exc− anomalies (atoms near t ≈ π², the top of the spectrum) land at bead 3–4 — the
UV section; exc+ anomalies (atom below 0) land at bead 9–10 — the IR section**; mixed graphs
show both sites simultaneously. The depth is strikingly size-independent (bead 3–4 whether
2N = 20 or 80). Mechanism open: CF depth should measure how many moments are needed before the
anomalous atom is felt; making that precise is a round-2 item.

## 6. The ω-flow indices (memo item 6, decided in finite form)

Two independent indices, computed on ω-grids with pole-tracking test points:

**κ_Pick(ω)** (counts exc− above the shift): prism C9: κ = 1–2 for ω < δ_N, **exactly 0 from
ω = 0.192**; crossing pinned in (0.187, 0.192) against predicted δ_N = 0.18954. Prism C17:
drop pinned in (0.305, 0.316) against δ_N = 0.31058. (Below the crossing the measured κ
fluctuates 1↔2 for the mult-2 eigenvalue — resolution of the second negative square depends on
test-point placement; the crossing location is sharp.)

**Support-leak index** (counts exc+ above the shift): |Im q_ω| at the predicted pole
z = −(δ_P−ω)²: dumbbell+4: 2.0·10⁸ (= w/ε) for ω < δ_P, collapsing to ≤ 0.7 immediately above;
crossing pinned in (0.097, 0.101) against δ_P = 0.098773. C17: leak dies in (0.15, 0.25)
against δ_P = 0.16052. κ_Pick stays 0 throughout for pure exc+ — real zeros never make negative
squares, at any shift.

**Verdict on memo item 6:** the index is an exact repackaging of zero counting — the crossings
are at ω = δ and nothing else happens — confirming the memo's own suspicion and
NOTE_variation_axes §2.2's relabelling verdict. What the repackaging does add: the two indices
are *type-separating* (Pick sees only height-π violations, support sees only real-zero
violations), which the raw zero count does not do, and which is exactly the finite image of the
Siegel split.

## 7. Covers: topology lands at the IR end

Exact (integer charpoly equality): BD(K4) = Q3, BD(Petersen) = Desargues. Atom provenance in
the cover: base atoms keep their τ; the twisted part contributes the mirrored τ → π−τ atoms.
Per-vertex strings:

| | beads (m̃, l̃, …) | L/n |
|---|---|---|
| Petersen | 0.556, 0.549, 1.448, 0.279 | 0.828 |
| Desargues = BD(Pet) | 0.556, 0.640, 1.264, 0.381, 3.26, 0.118, **14.12**, 0.058 | 1.196 |

The UV bead is **identical** (m̃₁ = 5/9 both — the cover has the same local structure), the
early beads deform slightly, and the twisted spectrum supplies the IR-most atoms: the cover's
smallest-τ atom (τ = π/4, from twisted λ = +2) produces the far-end mass 14.12. Same pattern
for K4 → Q3 (far-end mass 3.49 from twisted λ = ±1). **Covering-space topology is readable in
the bulk by position: it lives at the far (IR) end**, consistent with §4's locality split —
what the cover changes is global, so it cannot touch the UV beads. Strings do not factor under
σ_cover = σ_base + σ_twisted (the string map is nonlinear); position is the readable structure.

## 8. Ceiling and round-2 queue

**Ceiling (F7).** For regular graphs, ζ_X and everything built here factor through the
spectrum: cospectral graphs have identical bulks. So round 1's "topology detection" statements
are statements about *where spectral information localizes in the bulk* (gap → IR end, twisted
spectrum → IR end, local structure → UV end) — which is the memo's question answered at the
level regular graphs permit. Genuinely beyond-spectrum topology needs:

1. **Irregular graphs** (Bass with Q ≠ qI: the zeta is no longer spectrum-determined) — do
   cospectral-but-different graphs get different bulks?
2. **Magnetic/character twists** (cyclic covers with flux = Artin L-functions of graphs; the
   Kurasov mechanism finitely; conductor experiment of PROGRESS §2 in finite form).
3. **Periodic-tower variant**: keep the 2πℤ towers (graph gamma factor) — infinite string with
   explicit UV tower; test the Kasahara UV-law analogue (bulk UV coefficient vs −χ, the §3.3
   candidate theorem of NOTE_variation_axes, testable here first).
4. **Prime side**: the geodesic explicit formula for Ψ_X — close the full chain
   primes ⟷ zeros ⟷ bulk finitely.
5. **CF-depth mechanism** for the violation-position law (F8); **closed form for the tree
   string** (the tree's Green function is algebraic; the τ² change of variable is not — what
   survives?); the finite margin/order-parameter analogue (slope of Ψ_ω vs the graph
   (ξ′/ξ)(½+ω)).

## 9. Reproduction

All scripts in the session workspace (copies in `claude/lab_ihara_core.py` and
`claude/lab_ihara_experiments.py`): `lab_core.py` (graphs; exact charpoly via
Faddeev–LeVerrier over ℤ + Yun square-free + mp roots; atoms/γ data; q, h_ω, q_ω, Ψ; Stieltjes
CF and evaluation; Pick; Bass check) · `v1_validate.py` (§2) · `e2_census.py` (§3) ·
`e3_universality.py` (§4; KM Gauss string via Stieltjes procedure on a 500-pt Legendre grid) ·
`e4_e5.py`, `e5_fix.py` (§5–6) · `e6_covers.py` (§5.3, §7). mpmath + numpy only; dps 60–200
(CF synthesis needs ≥ 160 at 2N ≈ 80). Known-answer anchors: Terras' K4 zeta; Petersen
spectrum {3, 1⁵, −2⁴}; BD identities; ℓ = q(0).
