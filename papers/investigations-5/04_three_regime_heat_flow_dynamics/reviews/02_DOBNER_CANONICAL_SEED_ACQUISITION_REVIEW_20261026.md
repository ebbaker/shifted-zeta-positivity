# Dobner canonical seed acquisition: internal assessment

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Disposition:** no blocking mathematical defect found in the final
[small-time note][small] and [direct-lattice note][lattice] at their stated
analytical scopes. Review included the producing assistant, a separate
read-only same-model researcher on small-time seeds, another on direct
seeds and a separate read-only same-model reviewer of both final notes.
This is internal same-model review, not independent specialist validation.

The [result index][results], [avoid index][avoid], [control cluster][controls],
[same-model warning][same], [status rule][status], [scope rule][scope] and
[quantitative-gain rule][gain] apply. The user narrowed this chat to the
Dobner continuation; no response-branch research was performed here.

## Checks of the small-time theorem

| Obligation | Checked result |
| --- | --- |
| Uniform full-series growth | Factoring n^{-2} and completing the square proves S4 with constant2, for the whole series and all real x. |
| Nonzero logarithmic third derivative | The positive coefficients at s=8 give mu1<=1/96, mu2<=mu3/log2 and mu3>3/16384. The third cumulant is >45/262144>2^{-13}; no unproved sign or zero assumption is used. |
| Explicit seed radius | The positive-harmonic Fourier coefficient gives the factor12 in S7. R=2^{17}/tau makes its upper bound <=13/2^{17}<2^{-13}, so the zero-free disk premise is contradicted. The argument handles a possible boundary zero without assuming a logarithm there. |
| Number of zeros | Jensen at outer radius8R bounds all zeros through5R by N0, using Z_tau(8)>=1. Avoiding outer zero radii and passing to the limit is valid. |
| Zero-free factor | Blaschke division removes all zeros within a chosen L_out in[4R,5R]. Boundary modulus1, maximum modulus and Harnack factor7 give log|g|>=-6M on3R. |
| Complete finite-grid wall | The monic polynomial of radial zero moduli is augmented to degreeN0. Its exact finite difference gives max on the N0+1 grid points >=(2e)^{-N0}; each Blaschke factor costs at most the displayed8 denominator. This proves delta=exp[-6M-N0log(16e)] on at least one entire candidate circle. It does not identify its index computationally. |
| Infinite coefficient tail | The separate Q cutoff pays both the partial-square threshold and exp[-tau log^2 Q/8]<delta/12. The finite prime-factor sum is bounded by (log Q/log2)W. |
| Explicit recurrence degree | T=64(m+1)/theta^2, k=ceil(T log T) pays the exact B8 inequality, using T>=128 and 5T log T<=T^2. Note02's positive Fourier polynomial then gives its complete interval bound. |
| Published approximation | Theorem4 and equation35 were rechecked for fixed C=1. Their constants depend on this fixed C and the completed function, not secretly on tau in(0,1]. The growing real seed strip is paid by Y>=B_*^4. No constant has been numerically instantiated. |
| Transport and radius direction | Both errors are <delta/3; the gamma factor is nonzero above the paid onset. The map precedes canonical rotation, with the correct factor2 and sign. The result is an upper bound from a constructed nonreal zero, with |Im z|>=2d. |
| Final uniformity | M,N0,E=O(tau^{-3}); log Q, log(1/theta), log k=O(tau^{-3}); log L_rec<=exp(O(tau^{-3})). The complete map and field gates retain the bound exp exp(C_d tau^{-3}). |

During analysis a weaker radial-avoidance grid would have paid an extra
log N0 in the floor and log(2/tau) in the final exponent. The final note
uses the proved finite-difference estimate instead. No discarded formula
is left as a competing current claim.

The seed data are **analytical**: a specified finite family has a proved
good member, with count between1 andN0 and a complete floor. They are
not an interval-selected circle, a computed exact count or a numerical
certificate. Those distinctions do not obstruct the existence upper bound.

## Checks of the direct seed lattice and interpretation

For tau>=32, the n=1,2 terms equal 1-exp[-(log2)zeta] on the stated
disks. Its Taylor wall exceeds1/4; the complete n>=3 majorant is <1/8.
The proof of its n=3 payment uses a finite positive Taylor lower bound
for exp(16/5); the rest is paid by the full integral tail. Thus every disk
has exactly one simple seed zero and floor>1/8, with W<21/8. The field
constants126K_C and48K_C and exact map gate4pi exp[4(1+d)/tau] follow.
The first lattice disk above Y fits below Y+1+2pi/log2, deleting the
almost-period/recurrence term. Map injectivity also preserves simplicity.
All constants are uniform only on the declared fixed interval[32,C].

The divergence of this particular absolute two-term tail as tau->0 is
correctly scoped to that payment. Note03 supplies a different small-time
method. The gap1<tau<32 is explicitly left in the seed-parameterized
opening budget, rather than described as covered.

The new source-derived small-time upper envelope is compatible with all
three regimes. It does not prove RH, simplicity, a positive-threshold
contradiction, a lower escape rate, a fixed-transverse-strip overlap or an
optimal cost. Negative-time existence was known; the recorded gain is the
quantitative seed/count/wall acquisition and resulting uniformity.

## Register disposition and next work

TRD-03 remains **Partial** for usable numerical constants and sharper
seed/recurrence costs. Its analytical seed-input and uniform small-time
budget subtask is complete. TRD-04 becomes **Partial** because an actual
source-derived upper envelope is now proved; lower escape, practical
onsets and first-witness information remain open. TRD-07/08 remain Open.
The response tasks retain their previous statuses and owners.

The next bounded Dobner return should acquire a narrower small-time seed
strip with a complete count and floor, or instantiate K_1,y_0(1) on a
declared family. Compare the full recurrence cost before improving a field
allowance already dominated by it. No research numerical execution,
new PDF, manuscript snapshot, Git commit or scheduled model work occurred.

[small]: ../notes/03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md
[lattice]: ../notes/04_DIRECT_DOBNER_SEED_LATTICE_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[same]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[status]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[gain]: ../../../../avoid/20_volume_without_a_gain.md
