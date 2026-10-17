# Claude review of the active lifted-theta directions, with new directions

**Chat routing update, 17 October 2026.** [Review investigation directions (current history 2)](../chat-histories/0002_2026-10-13T17-10-52Z_review-investigation-directions.json). These unique registrations were moved to their affiliated folders at Edward Baker's request. Use the destination registry for refreshes and new affiliated chats; this routing supersedes older formal-replay filing instructions below. Historical numbers in the narrative describe the earlier capture. [Relocation and renumbering receipt](../../formal_replay_crosswalk/CHAT_HISTORY_RELOCATION_20261017.json). Prepared for Edward Baker with substantial LLM assistance, `gpt-6.1-sol`, reasoning effort **ultra**.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

This is the Claude review requested in the [active-folder overview](../../active/README.md).
It is an internal cross-model assessment and research proposal, not
independent specialist validation. It establishes no collision exclusion,
zero-free region or RH implication. Exact identities are marked as such;
numerical statements come from the [checker](../numerics/check_active_directions_review_claude_20261013.py)
and its [record](../numerics/ACTIVE_DIRECTIONS_REVIEW_CHECKS_CLAUDE_20261013.json).

**Read for this review.** The [broad lifted-symmetry search](../LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md)
and its seed records; the seventeen initial programs in [active](../../active/README.md);
the [GPT-6-astra review](ACTIVE_DIRECTIONS_REVIEW_CODEX_20261013.md), its
[angular seeds](../../active/02_angular_jacobi_gluing/notes/ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md)
and the new [project 17](../../inactive/17_spacetime_collision_degree/notes/INITIAL_RESEARCH_PROGRAM_20261013.md);
the [13 October planning conversation](../../chat-histories/0002_2026-10-13T12-54-02Z_review-newman-certificate-audit.json)
and the [GPT-6-astra conversation](../chat-histories/0002_2026-10-13T17-10-52Z_review-investigation-directions.json);
upstream [Heat Note 14](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md),
[Heat Note 25](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md)
and project-17 Notes [4](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md),
[5](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md),
[7](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md),
[8](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md)
(appendix) and [21](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md);
and the earlier Claude assessments of the heat lane: the
[11 October brainstorm](../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md),
its [cross-assessment](../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md)
and the [project-17 external review](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md).

## Verdict

1. **The GPT-6-astra allocation is sound, and I endorse it with the changes
   below.** The sixteen cards are hypotheses to screen. Angular gluing (02),
   cutoff reflection (01) and the paired-kernel question are where a bounded
   calculation can still teach something; 03 and 06 are destinations; 04, 10,
   11, 14 and 16 should not run as separate projects.

2. **Selection is solved; transfer is the problem.** Among positive, even,
   super-exponentially decaying sources, the theta source is already singled
   out by two exact symmetries: the reflection \(u\mapsto-u\) (the functional
   equation) and the integral lattice law (the angular period and quasi-period
   at the same scale; equivalently, integer Dirichlet frequencies with equal
   coefficients). In the scalar picture this is Hamburger's theorem; in the
   angular picture it is GPT-6-astra's elliptic rigidity. A newly found
   symmetry cannot make the source more unique. It is useful only if it
   survives the Newman deformation as a relation that carries a sign. That is
   the test applied to every direction below.

3. **A sharper control family (§1.3).** Perturbing the Euler factor of
   \(\zeta\) at one prime \(p\), symmetrically about \(s=\tfrac12\), gives
   positive even sources that have exactly the real zeros of \(\xi\) at
   \(t=0\), are modular for a congruence subgroup, keep every Euler factor at
   \(q\ne p\) and every Hecke/Heisenberg relation on the characteristic torus,
   and still have \(\Lambda>0\); under RH, \(\Lambda\to0\) as \(p\to\infty\).
   Only the Euler factor at \(p\), or the level-one lattice law that implies
   it, distinguishes them from theta. Since each has \(\Lambda>0\), any proof
   of \(\Lambda\le0\) must use the Euler factor at every prime. An identity
   that also holds for these sources cannot exclude collisions.

4. **Card 09's first deliverable already exists, and its meaning is
   automorphic (§3).** The complete two-coset formula is the divisor-pair
   identity of project-17 [Note 8, eq. (10)](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md).
   Read correctly, it is the Fourier–Whittaker expansion of the
   **non-holomorphic Eisenstein series on the imaginary-axis geodesic**. In
   this rank-two lift your intuition holds in a precise sense: the full
   modular group acts on the *shape* of the lattice \(\mathbb Z^2\),
   transverse to the physical direction, and the physical height becomes the
   spectral parameter of an automorphic eigenfunction. The Newman weight
   reaches the shape only through an explicit geodesic weight
   \(e^{(t/8)(\log y)^2}\) (§3.3). I derived and verified
   the resulting exact formula for the first Laguerre expression of \(\xi\).
   I recommend this as a new first-group direction A, absorbing 09 and
   giving 06 its structured form.

5. **For 02, the lattice law is the right lever, and it commutes with the
   Newman weight (§4).** Both theta-selecting symmetries commute with
   multiplication by \(e^{tu^2}\) at fixed scale. Every defect comes from the
   physical insertion \((\partial_u^2-1)/16\) acting across a scale-dependent
   lattice. The Lagarias–Li two-variable Hecke operators are dilations and do
   not separate the Euler-factor controls. The planned period transport will
   most likely return the identity "all Dirichlet coefficients equal one" in a
   Gamma-convolution form. It is worth one calculation with a stop rule.

6. **For 01, start from the exact identity that already exists (§5).** The
   complete interior/exterior relation is Riemann's integral behind the
   Riemann–Siegel formula, whose remainder is of Mordell type with exact
   modular transformation laws. The logarithmic inversion \(v\mapsto P/v\) is
   its stationary-phase shadow.

7. **Project 17 is correct, and is real-zero counting in topological form
   (§7).** It deserves one cost benchmark and no expansion until a concrete
   boundary homotopy is proposed.

## 1. Screening principles for a lifted symmetry

### 1.1 What earlier rounds settled

These facts are in the linked reviews and are not re-derived here.

- **Shape control.** The kernel \(q_{T,b}\) of the 11 October brainstorm is
  positive, even and super-exponentially decaying, has zero density of the
  theta order, and has de Bruijn–Newman constant exactly \(T\). An argument
  using only properties it shares cannot exclude collisions. (The
  cross-assessment correctly narrows this: it rules out exactly the
  arguments using its properties.)
- **Laguerre identity.** \(H_x^2-HH_{xx}=H^2\sum_\rho(x-\rho)^{-2}\). The two
  stationary signs (S0)/(S1) hold automatically at every all-real time; on
  \((0,\infty)\times\mathbb R\) together they are equivalent to RH; and
  \(\mathscr L_0(H_0)\ge0\) on all of \(\mathbb R\) is Csordas's open
  problem. Cards 04, 06, 10, 11 and 13 all target these quadratic forms in
  different charts.
- **Certificate equivalence.** The anchored adjoint certificate of card 03
  exists on a cell exactly when the scalar first-jet test passes there. 03
  can transmit an independent relation; it cannot create one.
- **Chord targets.** \(D=-\beta^2A''-2\beta xA'-(x^2+2\beta)A\) is a
  differential operator on the readout, so the chord/score targets of 04 and
  11 carry no theta data.
- **Real-axis perturbations** (GPT-6-astra). Positive even sources arbitrarily
  close to theta in relative supremum norm can have a joint zero at any
  prescribed \((T,X)\) with \(X\) large.

The overbroad "fact (D)" of the 10–11 October reviews was corrected in the
cross-assessment and is not used here.

### 1.2 Selection versus transfer

Hamburger's theorem (Math. Z. 1921; Titchmarsh, *The Theory of the Riemann
Zeta-Function*, §2.13): a Dirichlet series over the integers with the
functional equation and gamma factor of \(\zeta\), and mild growth, is a
constant multiple of \(\zeta\). In the source variable this reads as follows.
With \(\varphi(u)=(2\pi^2e^{9u}-3\pi e^{5u})e^{-\pi e^{4u}}\),
\[
\Phi(u)=\sum_{n\ge1}n^{-1/2}\varphi\!\left(u+\tfrac12\log n\right)
\quad\text{for every real }u,
\]
and the functional equation is the statement that this sum of non-even
translates is even. (The raw series is even to rounding where cancellation
permits; record B5.) GPT-6-astra's rigidity is the angular form: the
quasi-period forces adjacent coefficients to agree.

There is also a chart obstruction. In the balanced chart \(F(u,z)\), Jacobi
inversion is the fixed map \((u,z)\mapsto(-u,-iz)\), but the lattice periods
depend on \(u\). In the unbalanced chart \(\Theta(r,y)\), the real period is
the fixed shift \(y\mapsto y+1\), but inversion is
\((r,y)\mapsto(r^{-1},-iy/r)\). No chart makes both symmetries independent of
the scale, because the Jacobi group acts on scale and angle jointly. Any
relation using both is therefore nonlocal in the physical variable after the
Newman–Fourier transform. This is why "S-only" constructions (the leading
inversion of 01, and 04, 05, 06, 10, 11, 16) cannot be load-bearing by
themselves, and why the arithmetic-lattice cards (02, 07, 15, with 03 as
receiver) can be.

### 1.3 A new arithmetic control: Euler-factor perturbations

For a prime \(p\), \(0<c\) and \(a=\tfrac12\log p\), set
\[
\Phi_{c,p}(u)=\Phi(u)+\tfrac c2\bigl[\Phi(u+a)+\Phi(u-a)\bigr].
\]

1. It is positive, even and super-exponentially decaying, since \(\Phi>0\)
   (Pólya).
2. Its time-zero transform is \(H_0(x)\,(1+c\cos ax)\). For \(0<c<1\) the
   multiplier lies in \([1-c,1+c]\) on the real line, so **the real zeros at
   \(t=0\) are exactly those of \(H_0\)**, unconditionally.
3. In the variable \(s=\tfrac12+\tfrac{ix}2\) the same transform is
   \(\tfrac18\xi(s)\cdot\tfrac c2p^{s-1/2}Q_p(p^{-s})\) with
   \(Q_p(X)=1+(2\sqrt p/c)X+pX^2\). This is the completion, with conductor
   factor \((p/\sqrt\pi)^s\), of the Dirichlet series \(\zeta(s)Q_p(p^{-s})\),
   whose coefficients are
   \(a_n=1+(2\sqrt p/c)\mathbf 1_{p\mid n}+p\,\mathbf 1_{p^2\mid n}\): \(\zeta\)
   with its Euler factor at \(p\) multiplied by a Fricke-symmetric quadratic.
   It is an imprimitive degree-one member of the extended Selberg class with
   conductor \(p^2\) and positive coefficients. Dobner's theorem
   ([arXiv:2005.05142](https://arxiv.org/abs/2005.05142)) gives
   \(\Lambda\ge0\) throughout that class, with the same \(e^{tu^2}\)
   normalization.
4. The roots of \(Q_p\) have moduli \((1\pm\sqrt{1-c^2})/(c\sqrt p)\ne p^{-1/2}\),
   so there are zeros on \(\Re s=\tfrac12\pm\operatorname{arccosh}(1/c)/\log p\),
   that is at \(|\Im x|=\delta:=2\operatorname{arccosh}(1/c)/\log p\).
   Hence \(\Lambda_{c,p}>0\) unconditionally, and under RH
   \(\Lambda_{c,p}\le\delta^2/2\) by de Bruijn's strip theorem.
5. On the theta side it is
   \(\theta(r)+\tfrac c2[p^{1/2}\theta(p^2r)+p^{-1/2}\theta(r/p^2)]\), up to
   zero modes: completely monotone in internal time, reflection symmetric,
   modular for a congruence subgroup with cusp width \(2p^2\). Its angular
   extensions with scale-independent coefficients fail the Jacobi lattice
   law at the theta scale: the three dilates have quasi-periods
   \(i\lambda r\), \(\lambda\in\{1,p^{\pm2}\}\), with different multipliers,
   and the balanced-chart extension also loses the real period. (A
   scale-dependent prefactor \(C(r)\) would make any positive scalar source
   quasi-periodic, so the lattice law must be stated, as in §1.2, for
   Dirichlet-type extensions.)
6. In the Lagarias–Li coordinates of §4 it satisfies every Hecke and
   Heisenberg relation at fixed \(s\), because it differs from theta by a
   scalar function of \(s\).

| \(p\) | \(c\) | \(\delta=\lvert\Im x\rvert\) of off-line zeros | offset of \(\Re s\) | \(\delta^2/2\) (bound under RH) |
| --- | --- | --- | --- | --- |
| 2 | 0.5 | 3.800 | 1.900 | 7.22 |
| 101 | 0.5 | 0.571 | 0.285 | 0.163 |
| \(10^6\) | 0.9 | 0.0676 | 0.0338 | 0.0023 |
| \(10^6\) | 0.99 | 0.0206 | 0.0103 | 0.00021 |

With \(c=1\) the multiplier is \(2\cos^2(ax/2)\), giving exact double zeros at
\(t=0\); with \(c>1\) the extra zeros are real and simple. The family reaches
\(\Lambda=0\) at \(c=1\): under RH, \(\Lambda_{c,p}=0\) for every \(c\ge1\),
using Dobner's \(\Lambda\ge0\). This makes it a tunable arithmetic test.

**Consequence.** For the RH target the conclusion is rigorous. Every
\(\Phi_{c,p}\) with \(0<c<1\) has \(\Lambda_{c,p}>0\). An argument for
\(\Lambda\le0\) must therefore use, at every prime \(p\), something these
sources lack: the Euler factor at \(p\), or the level-one lattice law that
implies it. For an intermediate target \(\Lambda\le t_0\) one needs lower
bounds \(\Lambda_{c,p}>t_0\), and only the upper bound \(\delta^2/2\) is
proved. The multiplier alone is instructive. Under backward heat,
\(1+c\cos ax\) evolves to \(1+ce^{ta^2}\cos ax\), whose zeros become real
exactly at \(t=\log(1/c)/a^2=4\log(1/c)/(\log p)^2\). The verification pass
tracked the zeros of the full product numerically and found \(\Lambda_{c,p}\)
close to this value: \(\Lambda_{0.5,2}\approx5.04\) against 5.77, and
\(\Lambda_{0.5,101}\approx0.1298\) against 0.1302. This is numerical
evidence, not a bound. If it holds, a proof of \(\Lambda\le t_0\) must see
the Euler factors at least up to
\(\exp\bigl(2\sqrt{\log(1/c)/t_0}\bigr)\) for perturbations of strength \(c\).
Since \(\Lambda_{c,p}\) grows without bound as \(c\to0\), plausibly it must
see them at every prime.

The finite arithmetic lifts at Newman time \(t\) retain primes up to
\(e^{\kappa/(2t)}\), so they are compatible with this requirement; analytic
lifts that see only reflection, positivity and kernel shape are not. **Every
new identity should report its behaviour on three controls**: the shape
kernel \(q_{T,b}\), the real-axis perturbations of GPT-6-astra, and
\(\Phi_{c,p}\).

### 1.4 One shared lemma: Newman conjugation of dilations

With \((\tau_af)(u)=f(u+a)\) and \(N_t[f]\,(x)=\tfrac12\int e^{tu^2+ixu}f(u)\,du\),
\[
\boxed{N_t[\tau_af]\,(x)=e^{ta^2}e^{-iax}\,N_t[f]\,(x+2ita).}
\]
Proof: \(e^{tu^2}f(u+a)=e^{ta^2}\bigl[e^{tw^2}e^{-2taw}f(w)\bigr]_{w=u+a}\),
and multiplication by \(e^{cu}\) shifts the transform by \(x\mapsto x-ic\).
Exact check A1. Every dilation symmetry passes through the Newman deformation
by this rule: divisor transport (Heat Note 25, eq. (9); card 07), the mixed
heat coefficients (card 15), the Lagarias–Li operators (§4), Hecke
correspondences on the Eisenstein side (§3), and the \(z-4i\) shift of
card 02 (multiplication by \(e^{4u}\)). I suggest citing it once rather than
re-deriving it in each folder.

## 2. The seventeen active directions

| Direction | GPT-6-astra | This review | Reason and change |
| --- | --- | --- | --- |
| 01 Complete cutoff reflection | First group | First group, re-anchored | Start from Riemann's exact integral and Polymath's exact formula (39) (§5). Test any signed remainder on \(\Phi_{c,p}\). |
| 02 Angular Jacobi gluing | First group | First group, narrowed | The lattice law commutes with the Newman weight; defects come only from the insertion. Expect a coefficient identity; stop if no sign accompanies it (§4). |
| 03 Anchored source observability | Destination | Destination only | Certificate equivalence: it transmits a relation from A, 01 or 02. |
| 04 Chord nonlocal closure | Demote | Merge into 06 and A | The chord target is a differential operator on the readout. |
| 05 Metaplectic atlas | Tool | Tool on demand | Build only the chart a chosen identity needs. |
| 06 Paired kernel factorization | Destination | Destination; RH-strength as stated | Take its structured form from A (§3). Both kernel signs remain necessary. |
| 07 Divisor product transport | Cap | Cap; merge with 02 and 15 | Divisor transport is the dilation/Hecke structure; §1.4 covers its Newman defect. |
| 08 Cusp unit-sector saving | Separate track | Separate track, unchanged | Not a lift. Keep the earlier remark that the short-row mean square does the work. |
| 09 Rank-two addition | First group | Absorbed into A | Note 8, eq. (10), is the complete two-coset formula; its meaning is the Eisenstein expansion (§3). |
| 10 Gaussian–Hermite correlations | Tool | Chart of 06; no separate work | The same quadratic forms in Hermite coordinates. |
| 11 Stein/SUSY correlations | One operator test | Chart of 06; close as a project | Weighted integration by parts; no closure mechanism named. |
| 12 Canonical boundary reflection | Long term | Bridge to the main repository | Suzuki's shifted systems against Newman's Gaussian law of shifts (§6). |
| 13 Stability, Jensen, Lee–Yang | Long term | Reading only | RH-strength preparation theorem missing. |
| 14 Theta Volterra integrability | Demote | Close | The Volterra flow holds for every even measure under \(e^{tu^2}\). |
| 15 Adelic/automorphic | Framework | Merge with 02 and 07 | Common-exponent compatibility is the lattice/Hecke law; same control test. |
| 16 Radial sine geometry | Secondary | Close | Radial positivity is Bochner positive-definiteness of \(H_t(\lvert z\rvert)\); generic. |
| 17 Spacetime collision degree | Benchmark | Benchmark only | Correct; equivalent to zero counting (§7). |
| **A Rank-two automorphic lift** | — | **New, first group** | §3. |

## 3. Direction A: the rank-two automorphic lift

### 3.1 The identity

Write \(\xi_c(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) and \(G(T)=\xi_c(\tfrac12+iT)\),
which is real and even. The completed Eisenstein series
\(E^*(z,w)=\xi_c(2w)E(z,w)\) has the expansion
\[
E^*(z,w)=\xi_c(2w)y^w+\xi_c(2w-1)y^{1-w}
+4\sqrt y\sum_{n\ge1}n^{w-1/2}\sigma_{1-2w}(n)K_{w-1/2}(2\pi ny)\cos2\pi nx .
\]
On the unitary line \(w=\tfrac12+iT\) the coefficients are the multiplicative
Hecke eigenvalues \(\lambda_T(n)=\sum_{ab=n}(a/b)^{iT}\), and along the
imaginary axis the cusp part is
\[
K_T(y)=4\sqrt y\sum_{n\ge1}\lambda_T(n)K_{iT}(2\pi ny).
\]

The derivation has four steps.

1. In the pair source \(\Phi(u_1)\Phi(u_2)\), put \(u_{1,2}=s\pm r\) (volume
   and shape). The Mellin transform in the volume of \(\theta(Va)\theta(V/a)-1\)
   is the Epstein zeta function of the rectangular lattice of shape
   \(\tau=i/a\), that is \(2E^*(\tau,w)\).
2. Hecke's integral, renormalized in Zagier's sense, gives
   \(\mathrm{RN}\!\int_0^\infty E^*(iy,\tfrac12+iT)y^{s-1/2}dy/y=\xi_c(s+iT)\xi_c(s-iT)\).
3. Fold at \(y=1\) using \(E^*(i/y)=E^*(iy)\), and evaluate the four
   constant-term powers. This gives the exact identity
   \[
   \xi_c(s+iT)\xi_c(s-iT)=\int_1^\infty K_T(y)\,(y^{s-1/2}+y^{1/2-s})\frac{dy}y
   -\xi_c(1+2iT)\Bigl[\tfrac1{s+iT}+\tfrac1{1+iT-s}\Bigr]
   -\xi_c(2iT)\Bigl[\tfrac1{s-iT}+\tfrac1{1-iT-s}\Bigr].
   \tag{A.1}
   \]
4. Evaluate at \(s=\tfrac12\) and take two \(s\)-derivatives there (checks A3,
   A4):
   \[
   G(T)^2=2\int_1^\infty K_T(y)\frac{dy}y-4\,\Re\frac{\xi_c(1+2iT)}{\tfrac12+iT},
   \tag{A.2}
   \]
   \[
   \boxed{G'(T)^2-G(T)G''(T)=\int_1^\infty K_T(y)\,(\log y)^2\frac{dy}y
   -4\,\Re\frac{\xi_c(1+2iT)}{(\tfrac12+iT)^3}.}
   \tag{A.3}
   \]

Since \(H_0(2T)=-(T^2+\tfrac14)G(T)/16\), the Laguerre product rule (check A2)
gives the program's first Laguerre expression:
\[
1024\,\mathscr L_0(H_0;2T)=(T^2+\tfrac14)^2\,(G'^2-GG'')+(2T^2-\tfrac12)\,G^2 .
\tag{A.4}
\]

These are exact identities. The record verifies (A.2)–(A.3) at
\(T=0.5,2,4,6,10\) and at the first zero \(T=14.1347\dots\), and (A.4) against
direct theta integrals at the last five of these heights. Agreement is at
least \(10^{-11}\) relative, and \(1.2\cdot10^{-9}\) relative to the
cancelling pieces in \(G^2\) at the zero. Independent mpmath replays, not
retained, agree at twelve printed digits at \(T=2,6,10,14.13\). The
verification pass rederived (A.1) and confirmed (A.1)–(A.4) at 45 digits at
\(T=8\) and at the second zero \(T=21.0220\dots\).

| \(x=2T\) | \(\mathscr L_0(H_0;x)\) | Cusp share | Constant-term share |
| --- | --- | --- | --- |
| 4 | \(3.78\cdot10^{-5}\) | 0.16 | 0.84 |
| 8 | \(2.29\cdot10^{-5}\) | 0.54 | 0.46 |
| 12 | \(9.83\cdot10^{-6}\) | 0.87 | 0.13 |
| 20 | \(5.98\cdot10^{-7}\) | 1.009 | \(-0.009\) |
| 28.269 (first zero) | \(7.47\cdot10^{-9}\) | 1.002 | \(-0.002\) |

At a zero of \(\zeta(\tfrac12+iT)\), (A.2) says that the cusp period equals
the constant-term period. At the first zero both are \(9.08\cdot10^{-11}\).

### 3.2 What this lift makes visible

- **The modular group acts transversely.** In rank one, \(S\) and \(T\) act on
  the scale \(u\), the same variable as the Newman weight and the physical
  transform; hence the chart obstruction of §1.2. In rank two the full
  \(\mathrm{SL}_2(\mathbb Z)\) acts on the lattice shape \(\tau\), while the
  physical height is Fourier-dual to the volume.
- **The physical height is a spectral parameter.**
  \(\Delta E^*=w(1-w)E^*\) with \(w=\tfrac12+ix/2\).
- **The Euler product is visible termwise.** \(K_T\) is a sum over
  multiplicative Hecke eigenvalues \(\lambda_T(n)\).
- **Reflection is folding at the CM point \(i\).** Every physical moment is a
  moment about the point fixed by \(S\).
- **Familiar heuristics acquire a location.** Pólya's \(n=1\) approximation
  reappears as the first Whittaker mode. The controls \(\Phi_{c,p}\) become
  combinations of moments about the Hecke-translated points
  \(ip^{\pm1},ip^{\pm2}\) as well as \(i\); the Hecke relation at \(p\) is
  exactly what separates them.

### 3.3 Newman time in the rank-two lift

Write \(e^{t(u_1^2+u_2^2)}=e^{2ts^2}e^{2tr^2}\) and
\(e^{2ts^2}=\mathbb E\,e^{Vs}\) with \(V\sim N(0,4t)\). Then
\[
\mathscr L_0(H_t;x)=\mathbb E_V\bigl[\mathcal J_t(2x-iV)\bigr],
\]
where \(\mathcal J_t\) is the same pair transform with shape weight
\(e^{2tr^2}r^2\). In Eisenstein language this has two parts.

- **A Gaussian average of the spectral parameter**,
  \(w=\tfrac12+ix/2+V/4\) with \(V/4\sim N(0,t/4)\). It commutes with
  \(\mathrm{SL}_2(\mathbb Z)\) and acts termwise in the Whittaker index; it
  averages the Hecke eigenvalues \(\lambda_{w+V/4}(n)\) rather than
  preserving them.
- **An explicit geodesic weight** \(e^{(t/8)(\log y)^2}\), symmetric under
  \(S\) and breaking \(T\).

The insertion \((\partial^2-1)/16\) adds explicit polynomial factors. Thus in
rank two the \(T\)-symmetry destroyed by the Newman weight in rank one is
**exact on the automorphic integrand**; the Newman flow breaks it only through
a known test function on the geodesic. This is my precise answer to the
question of whether a hidden symmetry shows itself more clearly in the lift.

One caution: at \(t>0\) the constant terms acquire log-normal growth along
the geodesic, so they must be combined with the rank-one pieces before the
geodesic integral is taken. The cusp part decays and needs no such care.

### 3.4 Limits, first tasks and stop rule

**What it does not do.** (A.1)–(A.4) are exact rewritings. On stationary sets
the sign question becomes positivity of geodesic moments of the cusp part,
which carries essentially all of \(\mathscr L_0\) at the heights where zeros
lie. The constant-term part matters only at low height. Even there,
Lagarias–Suzuki-type Hermite–Biehler arguments apply only up to one
exceptional imaginary pair: the constant-term piece of (A.2) vanishes at
\(T\approx\pm4.958i\), and that of (A.3) at \(T\approx\pm7.357i\) (found by
the verification pass).

**First bounded tasks.**

1. **A1.** Derive the \(t>0\) formula with all insertions and verify it at
   \((t,x)=(0.05,8)\) and \((0.05,28.27)\) against direct pair integrals.
2. **A2.** Write the Hecke correspondence at \(p=2\) as an exact identity
   between moments along the geodesic \(0\to\infty\) and along \(\infty\to1/2\),
   with dilated weights. This is the Euler factor at 2 inside the lift.
3. **A3.** Run the control test: express the \(\Phi_{c,p}\) moments through
   A2 and identify the single term where \(\lambda_T(p)\) enters.
4. **A4.** Calibrate the expected cancellation in the cusp moment against the
   literature on Eisenstein series restricted to this geodesic
   ([Young, arXiv:1306.1554](https://arxiv.org/abs/1306.1554), which proves
   the QUE analogue there).

**Stop rule.** If the stationary targets reduce, after A1–A3, to positivity of
a cusp moment with no positive-definite structure (no expression as
\(\langle f,f\rangle\), no positive Selberg-type transform, no
Hermite–Biehler pair), close A with an identity note.

**Literature anchors.** Hecke periods and their renormalization (D. Zagier,
"The Rankin–Selberg method for automorphic functions which are not of rapid
decay", 1981). [Lagarias–Suzuki](https://arxiv.org/abs/math/0412039) prove
that integrals of \(E(z,s)\) against certain non-negative measures have all
zeros on the critical line, including truncation integrals and Weng's rank-two
zeta function. Their mechanism is Hermite–Biehler dominance of the constant
term; the geodesic moments above keep every Fourier mode and lie outside it.

## 4. Sharpening 02: lattice law, Lerch–Heisenberg structure, and what to expect

**The lattice law commutes with the Newman weight.** In the angular field,
the period and quasi-period at a fixed scale are relations in the angle at
fixed \(u\), and Jacobi inversion maps \(u\mapsto-u\). Multiplication by the
even weight \(e^{tu^2}\) preserves all three exactly. Every defect in the physical field comes from the insertion
\((\partial_u^2-1)/16\) acting across a \(u\)-dependent lattice (balanced
chart) or a \(u\)-dependent inversion (unbalanced chart). This is the precise
form of the "moving-period connection terms" in GPT-6-astra's plan.

**Lagarias–Li supply the representation theory, but not the separation.**
With \(\zeta(s,a,c)=\sum_{n\ge0}e^{2\pi ina}(n+c)^{-s}\), the two-variable
Hecke operators \(T_mf(a,c)=m^{-1}\sum_{k<m}f((a+k)/m,mc)\)
([Lagarias–Li, arXiv:1511.08116](https://arxiv.org/abs/1511.08116)) give
\(T_m\zeta=m^{-s}\zeta\). The Lerch operator
\(D_L=(2\pi i)^{-1}\partial_a\partial_c+c\,\partial_c\) gives
\(D_L\zeta=-s\zeta\). These are direct computations in this normalization.
On the theta function with characteristics,
\(\Theta(r;a,c)=\sum_{n\in\mathbb Z}e^{2\pi ina}e^{-\pi(n+c)^2r}\), one finds
\[
T_m\Theta(r;a,c)=\Theta(m^2r;a,c):
\]
the Hecke operators are exactly the dilations \(u\mapsto u+\tfrac12\log m\).
By §1.4, the Newman-deformed completed Lerch function
\(F_t=e^{(t/4)\partial_s^2}\Lambda\) satisfies
\[
T_mF_t(s)=m^{-s}e^{(t/4)\log^2m}\,F_t\!\left(s-\tfrac t2\log m\right),
\qquad
\Bigl(D_L+s+\tfrac t2\partial_s\Bigr)F_t=0,
\]
and keeps the Lerch functional equation exactly. These are clean deformed
symmetries. However, \(\Phi_{c,p}\) satisfies all of them, because it differs
from theta by a scalar function of \(s\). The structure that separates them is
the quasi-period at the theta scale, which couples angle to scale and is not
diagonal in \(s\). Lagarias's Heisenberg-group paper
([arXiv:1511.08157](https://arxiv.org/abs/1511.08157)) gives the natural
operator setting. Its Theorem 1.1 shows that Lerch \(L\)-functions on the
critical line form a complete family of generalized eigenfunctions, with pure
continuous spectrum, of the skew-adjoint operator
\(\Delta_L=D_L+\tfrac12 I\).

**What to expect.** Transporting the quasi-period through the insertion
should give a relation between adjacent angular Fourier modes. After the
\(u\)-transform it is a Gamma-function convolution in \(x\), that is, the
statement that all Dirichlet coefficients equal one. It will be exact and will
pass the shape and Euler-factor screens, but it is linear. A sign needs a
second ingredient in the same relation: reflection, or a positive structure.

**Stop rule.** Carry out the transport, which is a short calculation. Then
test whether combining it with inversion yields a nonlocal relation with a
definite sign on one stationary cell. If it does not, record the obstruction
and stop. Checked by hand for this review: \(F(u,z)=F(-u,-iz)\), the
coefficient \([z^2]K_t=\tfrac{i\pi}2(2tH_x-xH)\), and the quasi-period defect
formula of the angular seeds note.

## 5. Re-anchoring 01: the exact interior/exterior identity

Riemann's integral representation, the starting point of the Riemann–Siegel
formula, writes \(\zeta(s)\) as two contour integrals of
\(x^{-s}e^{\pm i\pi x^2}/(e^{i\pi x}-e^{-i\pi x})\) and its reflected partner.
Their residues at the integers produce the two finite Dirichlet sums on either
side of the cutoff, and their saddle points produce the Riemann–Siegel
corrections. The kernels are of Mordell type. Mordell integrals obey exact
transformation laws under the Jacobi group
([Zwegers, arXiv:0807.4834](https://arxiv.org/abs/0807.4834), Prop. 1.2), and
[O'Sullivan (arXiv:1811.01130)](https://arxiv.org/abs/1811.01130) shows that
Mordell integrals govern the Riemann–Siegel asymptotics off the critical line.
This is the "complete reflection across the cutoff, with all boundary
payments" that card 01 asks for. The inversion \(v\mapsto P/v\) with
\(P=T/2\pi\) is its leading stationary-phase shadow.

For \(H_t\) the exact counterpart is Polymath's exact formula
([arXiv:1904.12438](https://arxiv.org/abs/1904.12438), §4, eq. (39)): finite
sums \(r_{t,n}\) plus the heat-evolved Riemann–Siegel remainder
\(R_{t,N}\), with reflections. Their \(A+B-C\) formula (the effective
Riemann–Siegel approximation of their Theorem 1.3, with its \(C_t\)
refinement) approximates it with explicit errors, and the project's corrected interface
(project-17 Notes 20–22) sharpens the approximation. **First task:** on one
cell, write the exact remainder \(R_{t,N}\) (leading term \(C_t\)) and its
reflected partner in Mordell form with the Newman defect of §1.4, and compare
the signed paired remainder with the current absolute envelope. **Stop** if
the exact transformation reproduces only the \(A\leftrightarrow B\) symmetry
already used. O'Sullivan's generalization, with partial sums of unequal
lengths \(\alpha\beta=t/2\pi\) and Mordell integrals in the asymptotics, is
the natural template for moving the cutoff.

## 6. Wild cards, labelled as such

**W1. A horocyclic-to-geodesic family.** In the folded form of (A.2),
replace the point mass at \(\Re z=0\) by a circle heat kernel
\(\rho_\varepsilon\) in \(\Re z\). As \(\varepsilon\to\infty\) only the
constant term survives, giving \(-4\Re[\xi_c(1+2iT)/(\tfrac12+iT)]\). This
endpoint does **not** satisfy RH: with \(w=\tfrac12+iT\), the function
\(\xi_c(2w)/w-\xi_c(2w-1)/(w-1)\) has a real zero at \(w\approx5.45763\),
that is zeros at \(T\approx\pm4.95763i\). Numerically, all its other zeros
with \(0.05<T<40\) are real. This is the analogue of the Lagarias–Suzuki
exceptional real zeros. As \(\varepsilon\to0\) the family tends to \(G^2\),
and small-\(\varepsilon\) splitting of the double zeros of \(G^2\) is
governed by the sign of an explicit Whittaker sum at each zero. It remains a
natural homotopy for project 17, but neither endpoint argument nor any
monotonicity keeps its zeros on the line.

**W2. Newman as a Gaussian law of shifts (card 12).** Exactly,
\(H_t(x)=\tfrac18\,\mathbb E\,\xi(\tfrac12+V+\tfrac{ix}2)\) with
\(V\sim N(0,t/2)\). Suzuki's canonical systems and the Hermite–Biehler
property of \(\xi(\tfrac12+\omega-iz)\) use the two-point law \(\pm\omega\);
the latter holds unconditionally for \(\omega\ge\tfrac12\). This connects the
present portfolio to the shifted-positivity program in the main repository.
De Bruijn's strip theorem is the quantitative bridge, and I see no gain beyond
it without a new monotonicity in \(\omega\).

## 7. Project 17: spacetime collision degree

The checker replays on the author's machine: windings
\(-1,-1,-2,-2,-3,-3,-4,-4,-5\) for multiplicities 2–10, winding 0 for the
non-heat control, and the recorded source hash. The local index
\(-\lfloor m/2\rfloor\) follows from Hermite splitting, and the proof is
correct. The note itself identifies the content: with no side collisions,
the winding equals \(-(Z(t_+)-Z(t_-))/2\) plus side flux. It is therefore
Sturm–Angenent zero-number monotonicity in topological form, and it inherits
the information content of real-zero counting.

Its value is economic. A boundary enclosure may be cheaper than interior jets,
and that is worth one benchmark on a rectangle already certified by the zero
atlas. The homotopy idea is sound in principle, since winding is invariant
under deformations through heat solutions with a nonvanishing boundary pair.
The natural families (\(\Phi_{c,p}\) in \(c\); W1 in \(\varepsilon\)) need that
nonvanishing along the whole path, which is the same information. Benchmark
only.

## 8. Suggested allocation

1. **A1–A3** (rank-two lift): one session. Identities first, then the
   control test.
2. **02**: the lattice transport plus the \(\Phi_{c,p}\) test; one session with
   the stop rule of §4.
3. **01**: the exact Riemann–Siegel/Polymath remainder \(R_{t,N}\) on one
   cell, as a comparison only.
4. **17** benchmark and **08** arithmetic probe: independent and optional.
5. **Close or merge:** 04 into 06/A; 10 and 11 as charts of 06; 14 and 16
   closed; 07 and 15 merged into 02. Keep 05 as a tool, 03 and 06 as
   destinations, and 12 and 13 as reading and bridges.
6. **For every new identity, report its behaviour on the three controls of
   §1.3.** An identity that also holds for \(\Phi_{c,p}\) cannot exclude
   collisions.

## 9. Checks, replays and sources

- **New checker**, [check_active_directions_review_claude_20261013.py](../numerics/check_active_directions_review_claude_20261013.py),
  standard library only, with its [record](../numerics/ACTIVE_DIRECTIONS_REVIEW_CHECKS_CLAUDE_20261013.json).
  Part A has 27 exact rational assertions: the dilation lemma A1, the
  Laguerre product rule A2, the pair second-derivative identity A3 and the
  folded pole terms A4. Part B is a double-precision quadrature replay:
  \(\xi_c(\tfrac12)\) against the literature value; \(G(\gamma_1)\approx0\);
  the normalization \(E^*(iy)=E^*(i/y)\); (A.2)–(A.3) at six heights and
  (A.4) at five; evenness of the raw theta series where cancellation permits;
  and the \(\Phi_{c,p}\) table. Part B is evidence, not a certificate.
- **Replays.** The lifted-seed checker (192 assertions) and the project-17
  degree checker both pass on the author's machine. The record above
  regenerates byte-for-byte under `python3 -I`.
- **Independent verification pass.** A separate Claude Opus 5.5 subagent
  (mpmath at 30–50 digits; scripts not retained) re-derived (A.1) and
  confirmed it at \(T=8\) and at the second zero, together with the dilation
  lemma, the Lerch relations and their deformed forms, the variance
  bookkeeping of §3.3 (to \(2\cdot10^{-13}\) at \(t=0.1\), \(x=10\)), W2, the
  Hermite–Biehler claim and the source series. It also estimated
  \(\Lambda_{c,p}\). It found the errors corrected in this version: a
  reversed inequality in §1.3, the status of Polymath's \(A+B-C\), the W1
  endpoint, and the adjointness of Lagarias's operator. I re-read Polymath's
  eq. (39) and Lagarias's Theorem 1.1 to confirm the last two corrections.
- **External sources consulted.** Lagarias–Li
  ([1511.08116](https://arxiv.org/abs/1511.08116)), Lagarias
  ([1511.08157](https://arxiv.org/abs/1511.08157)), Lagarias–Suzuki
  ([math/0412039](https://arxiv.org/abs/math/0412039)), Young
  ([1306.1554](https://arxiv.org/abs/1306.1554)), Dobner
  ([2005.05142](https://arxiv.org/abs/2005.05142)), O'Sullivan
  ([1811.01130](https://arxiv.org/abs/1811.01130)), Zwegers
  ([0807.4834](https://arxiv.org/abs/0807.4834)), and Hamburger via
  Titchmarsh §2.13. Abstract-level readings are used only for the statements
  attributed to them.
