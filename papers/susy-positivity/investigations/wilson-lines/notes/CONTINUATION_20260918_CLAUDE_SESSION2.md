# Continuation: reflection networks, next session

18 September 2026. Prepared by Claude Fable 5.1 (Anthropic), model
`claude-fable-5-1`, for Edward Baker, at the end of a session cut short by the
usage limit. Supersedes the "next calculation" section of
[CONTINUATION_20260918_CLAUDE.md](CONTINUATION_20260918_CLAUDE.md); everything
else in that note (repository state, claims requiring care, reproduction) still
stands. The manuscript remains **0.8, unchanged**; nothing was integrated into it.

## What this session did

Read, in order: the Codex handoff, both endpoint notes, the 17 September review,
Loewner Section 4, the manuscript's conventions and generator sections, the
investigation and notes indexes, the check programme and continuation registry,
and the source paper arXiv:1102.4948 in full (Sections 3.1--3.2 and Appendices
B--C are what matter). Verified `validation/endpoint_matter.py check --replay`
(154 cases) and `validation/drafts.py check` (identity, 9 snapshots) on this
runtime.

Then did the head item of the handoff --- **construct the positive pairing** ---
and wrote it up in
[REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md](REFLECTION_NETWORKS_AND_THE_EVEN_TOWER_20260918.md)
with a standard-library check programme,
[`numerics/check_reflection_networks.py`](../numerics/check_reflection_networks.py)
(1196 cases, deterministic, record
[`reflection-networks-checks.json`](../numerics/records/reflection-networks-checks.json)).

## The results, in one paragraph

The archimedean kernel splits by reflection type: $n_\gamma=G_o+G_-$, and
$\tfrac12(G_s+G_o)$. The reflection *within* the defect ($x_1\to-x_1$), with the
origin as common reference, glues only the opposite-ray half and yields the
**alternating** tower $1/(2\cosh(u/2))$; its pairing path has a backtracking
cusp at the origin and its two halves share no bulk supercharge. The reflection
*through* the defect ($x_3\to-x_3$) fixes every defect point; with kets
$\Phi_r=W_{\rm up}[0\leftarrow r]q(r)$ along the semicircle of diameter $[0,r]$
and the even combination $\Phi_+(r)=\Phi_r+\Phi_{-r}$, the pairing
$\langle\Theta_3\Phi_+(r_1)\,\Phi_+(r_2)\rangle$ is a gauge-invariant open Wilson
line through the origin, smooth there, whose free kernel is **exactly**
$n_\gamma$ (the even image average survives), and which is a Gram kernel
**conditional on** Osterwalder--Schrader positivity of the interface theory under
$\Theta_3$. All kets $\Phi_{\pm r}$, for every $r$, are annihilated by one bulk
special supercharge ($\epsilon_s=0$, $J\epsilon_c=-\epsilon_c$), which removes,
for this network, the obstruction the transport note found for pairwise
semicircles. Reading the source's Appendix B, $X^H_3$ is $\Theta_3$-odd, so the
reflected bra carries $-X^H_3$ and the full pairing path is not BPS under a single
charge --- as a norm should not be. Nothing about primes, contact or poles follows.

## Next calculations, in order

1. **Audit the OS-positivity hypothesis.** Parities of every defect field under
   $x_3\to-x_3$ from DeWolfe--Freedman--Ooguri (hep-th/0111135), including the
   fermionic and auxiliary terms of the defect action (68) of the source; whether
   a bulk Wilson line piercing the defect needs a local coupling at the piercing
   point. Until this is done, the positivity of the network is a hypothesis.
2. **Defect endpoint conditions for the kets** $\Phi_{\pm r}$ under the common
   charge, against (81)--(84) of the source. Both kets point *into* the origin,
   so their endpoint polarizations should coincide; confirm, and record which
   $q_m$ sits at the outer ends.
3. **First interaction correction of the network kernel in one local scheme.**
   Reuse the source's (31), (42), (57) for the pieces they cover; compute the new
   cross-arc exchange between the upper and lower semicircles (the constant
   $\frac12$ of (31) does not hold across two different circles) and the
   piercing term; then test the weight through the matter note's (3.5).
4. **Stokes difference** between the pairwise semicircle $\mathcal O(-r_2,r_1)$
   and the network path at $O(g^2)$.
5. **Registration.** `check_reflection_networks.py` is *not yet* in
   `validation/endpoint_matter.py`'s `CHECKS`/`FILES`; add it and the two new
   notes there, run `python3 validation/endpoint_matter.py record --replay`
   (this refreshes `ENDPOINT_MATTER_RECORD.json`; update its `model` field to
   name both models), and update `numerics/README.md`, `notes/README.md`, the
   investigation README's "What is open" list and `CHANGELOG.md`. I ran out of
   session before doing this; the programme itself is verified deterministic and
   its record matches a fresh run.

## What not to redo

- Do not test the pairwise semicircles for a common supercharge again; the
  transport note's negative is correct for them and the network note explains
  which gluing evades it.
- Do not try to glue the opposite-ray half within the defect; Section 4 of the
  network note shows it produces the alternating tower with a cusp.
- Do not read the network's free kernel as a result about the transfer: the
  positivity of $n_\gamma$ was never in doubt; the placement inside a
  gauge-invariant Gram pairing was the open item, and that is all that changed.

## Reproduction

```sh
python3 numerics/check_reflection_networks.py   # 1196 cases
python3 validation/endpoint_matter.py check --replay   # 154 cases, unchanged
python3 validation/drafts.py check
```

The project folder connected to this session also contains a scan of
H. Yoshida, *On Hermitian forms attached to zeta functions* (1992), which treats
positivity of the Weil form on $C_c^\infty([-a,a])$ and its deformation in $a$;
it is third-party material and must not be committed, but it bears directly on
the frame-bound and critical-path notes and is worth a reading pass.
