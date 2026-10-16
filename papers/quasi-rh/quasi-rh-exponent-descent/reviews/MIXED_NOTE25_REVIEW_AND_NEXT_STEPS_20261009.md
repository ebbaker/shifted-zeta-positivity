# Review of Note 25 and recommended next steps

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Three parallel
same-model audits supported this review. They are internal checks, not
independent specialist review or formal verification.

## Verdict

[Note 25](../mixed_character_families/notes/25_SQUAREPART_REMOVAL_AND_SMOOTH_OBSTRUCTION_20261009.md)
is mathematically consistent within its stated imported hypotheses. No
required correction to its squarepart removal or principal Mellin obstruction
was found. It controls a further sector, while correctly leaving the selected
mixed fourth theorem open. The smooth obstruction is a substantial diagnostic:
it rules out the unrestricted uncentered principal-compatible enlargement,
including its small-common-factor residual. It does not refute the selected
nonprincipal high-conductor target.

The most useful next route is a **quantified centered comparison for the
original inverse**, followed by a new signed centered moment estimate. The
source inputs and existing operational enclosures already leave enough
comparison room. The accompanying [feasibility note](../mixed_character_families/notes/26_CENTERED_COMPARISON_FEASIBILITY_20261009.md)
states the calculation, exact loss budget, and remaining theorem. This is
more specific than requesting another unrestricted smooth estimate.

## What was checked

The target, Notes 19 and 21–24, relevant earlier diagonal tests, the stable
manuscript, existing review, original checker and retained record were read.
The working tree already contained substantial uncommitted research; this
review preserves it and adds separate review/feasibility/audit files only.
The reviewed checkout HEAD was `348cb46dd12ec32eebcf14c4ef0317a400d01409`;
HEAD alone does not identify these uncommitted files.

| Claim in Note 25 | Assessment |
| --- | --- |
| Lines 21–63: \(c_Z(g^2h)=\mu_F(h)d_{Z/q_g}(h)\), exact caps, positive counting | Correct. The common factor belongs to the two truncated inverse factors. The capped divisor count need not be multiplicative. |
| Lines 65–102: selected square and complete Cauchy removal | Correct. Square saving is 1/125; full cross saving is at least 79927/20000000; combined removal retains 7979/2000000. |
| Lines 106–141: legal sixth-order sieve | Correct under imported native transfer. Its best endpoint misses this target by at least 5423/52500, even with the optimistic baseline slot envelope. |
| Lines 173–230: principal Mellin argument | Correct. The distinct zeta arguments force an affine chain of zeros tending to the isolated pole at one under a hypothetical subcritical bound. Profile numerator zeros cannot evade the necessary cancellation condition. |
| Lines 234–278: prime-sixth row transfer | Correct within the stated principal-compatible class. Uniform deletion is smaller than the obstruction, and arbitrarily large exceptional scales suffice. This is not an all-scale lower bound. |
| Lines 298–323: sixth-power-free projector and crude cutoff | Correct for the displayed unrestricted identity. It does not yet represent the full selected/high-conductor target. |

The sixth-order formula and power-free scope were checked against
[de Faveri, Theorem 1.1](https://arxiv.org/html/2610.04045v1).
The classical zeta/Dirichlet facts were checked against
[DLMF 25.10](https://dlmf.nist.gov/25.10) and
[DLMF 25.15](https://dlmf.nist.gov/25.15); a parallel audit checked
[Pollack–Troupe, Theorem 2.1](https://www.pollack-math.net/irreddiv-bams.pdf)
for fixed-ray prime counting. These checks verify statements and scope,
not their deep proofs or the native transfer. No third-party PDF was saved.

The 5423/52500 deficit is the gap in one particular sieve upper estimate.
It is not the gap between the existing selected envelope and its desired
bound, which is 1/700 plus retained source costs. Another useful count
or exact identity is not automatically a new correlation saving.

## A real verification weakness, with a separate regression check

The original checker replayed successfully and reproduced its retained
record byte-for-byte. Its 725,761 assertions should nevertheless be read
through coverage, rather than their total. With prime norms 7, 13 and 19
and cap \(Z=20\), each truncated squarefree inverse factor is a unit or
one prime. Its high-squarepart tuples have \(h=1\): they never exercise a
nontrivial common factor together with a nontrivial signed squarefree core.
About 98.45% of the assertions concern elementary projector/mask identities.
Its rational ledger also omits the section 2 sieve deficit.

The separate [review checker](../numerics/check_note25_review.py) and
[record](../numerics/note25_review_record_20261009.json) address those gaps
without changing the original files. They pass 742 exact assertions and
reproduce their record on a second run. Coverage includes 67 annular tuples,
18 with nontrivial \(g,h\), and two with both reduced inverse factors
nonunits. The explicit case is
\[
 (a,b,g,h,l)=(91,133,7,247,1),\qquad g^2hl=12103.
\]
Both inverse caps are 140. Here \(d_{20}(247)=2\), whereas
\(d_{20}(13)d_{20}(19)=4\), so the nonmultiplicative cap interaction is
actually exercised. The audit also tests selected complete-cross identities,
physical zeros, section 1 minima, section 2's piecewise sieve comparison,
and the new centered-comparison arithmetic. Its rows and profile values are
synthetic. It proves no analytic moment, Mellin obstruction, native transfer,
or derivative-uniform estimate.

## Recommended research sequence

### 1 Use the original-inverse centered comparison as the next interface

Take the same original plain profile at
\(Y_1=U^{1/4}\), \(Y_2=U^{2m-1/4}\), so \(Y_1Y_2=N^2\), and form
\[
 \Delta_u=M_uQ_J(u)[S_u(N)^2-S_u(Y_1)S_u(Y_2)].
\]
The imported marked inverse second moment applies directly to every whole
subset \(J\), with ample capacity room; no division by omitted slots is
needed. Combining it with the original all-length plain bounds gives a
complete selected comparison saving
\[
 \delta_c=\frac d2(r+2m-3/2)-(15-12m+6r)e_{\rm src}.
\]
The existing certified operational lower enclosures imply, for
\(e_{\rm src}\le1/1200000\),
\[
 \delta_c\ge0.0024516612>1/700,
 \qquad \delta_c-1/700\ge0.0010230897714\ldots.
\]
This conclusion holds on the actual operational region. Its coarse-box
infimum has no positive saving. Charge all separately fixed profile, mass
and height power losses before spending this reserve; the source/witness
application budgets remain separate.

Center the original \(M\) first. A marked second mass for \(M_\dagger\)
has not been supplied. Proving the centered original target recovers the
original target, then the residual target through Notes 24–25's controlled
differences. The accompanying feasibility note proves this conditional
comparison; it does not prove the centered mixed moment.

### 2 Verify auxiliary-row cancellation, then attack the signed centered norm

The next bounded analytic task is a uniform estimate for the centered plain
difference on admitted principal/fixed-ray auxiliary rows, including every
deletion mask, original twist, derivative profile and height allowance.
Equal-product centering cancels their leading response, but its error and
all other newly admitted conductor sectors must still be bounded before
using a full smooth enlargement.

Then prove the centered mixed norm with saving 1/700, preserving the
complete signed coprimality kernel of Note 21 and the actual inverse/slot
coefficients. Note 18 already shows that this centering does not repair
the separately positive coefficient-diagonal bound. A useful initial
experiment or subcase should test a specified signed block or response
tail, with its precise route to the full target stated in advance.

### 3 Keep a conductor-preserving mask route as the alternative

If the centered smooth comparison adds an unaffordable auxiliary sector,
return to the selected small-\(g\) correlation. A signed-mask interface must
carry the actual selected-bin predicate as \(1_{\mathcal C_+}(q^6v)\),
in addition to the radial envelope and the sixth-free Möbius mask.
In a fixed presentation the primitive conductor is unchanged by a sixth
power, although physical zeros change. Its high-conductor gate therefore
remains literal on \(v\).

There is a useful refinement to the unrestricted cutoff discussion:
\(Q_{\psi_v}\ll q_v\) and \(q_q^6q_v\ll U\) imply the exact support bound
\[
 q_q\ll U^{(1-2m+1/1000)/6}\le U^{67/2000},
\]
up to fixed constants. A full cutoff on this **conductor-restricted support**
has zero tail. Unlike absolute summation of (17) without that gate, absolute
mask terms retaining it do not reintroduce principal inducing characters.
Thus Note 25's unrestricted crude-tail failure must not be promoted to a
failure theorem for every conductor-preserving mask interface.

This shorter exact mask range is a potentially useful first lemma, but it
does not create a signed saving: already the \(q=1\) term retains a
nonradial conductor predicate and the selected-bin dependency. The source
radial Poisson formula cannot simply absorb those predicates. A comparison
or a new constrained aggregate estimate remains necessary.

## What should remain secondary

Keep modest cutoff optimization and additional algebraic sector removals
secondary to a quantitative signed estimate. Do not combine the inverse-pair
gcd selector of Note 14 with the truncated-factor gcd of Note 25 without
an exact tuple identity. Retain the genuine whole-slot/source/witness and
height quantifiers when translating any new theorem to the detector.
No stronger zero-free boundary or RH consequence follows from this review.

## Provenance and validation scope

| Reviewed artifact | SHA-256 |
| --- | --- |
| Note 25 | `5fce092262a9733f2fd6fe3c5d37a9281ad8e9f9edd6128ea73b6e04aa209dd2` |
| Stable manuscript | `76c95befc29059809197137cc8e5a83dfeef69307064a4e71bfa4c7a13f006c5` |
| Original squarepart checker | `88086a0ac402de588587d6d46553dac3206a2880940e7a61f468d70f15c10e14` |
| Original squarepart record | `d502669c675a2a0755210d94738a83c4a570bad7fc109d77a882f0f8a110eeff` |
| Separate review checker | `a49707df8a1cac49b5edecdad1d4df67d7f1c290e5152ce3210dce2e65220531` |
| Separate review record | `5eb8293dd763397d13c3d394f511b20e35655c1e99a5dc3d89a1952b8337afdb` |

The original manuscript was not edited or recompiled in this review; its
prior compilation claim was not rerun. All new files are small and conform
to the repository's LARGE_FILES policy. No commit, tag, exported PDF or
draft snapshot was created. No new manuscript milestone requires a
DRAFT_HISTOR entry. The detailed research calculation is saved in the
linked feasibility note rather than in a draft manuscript.
