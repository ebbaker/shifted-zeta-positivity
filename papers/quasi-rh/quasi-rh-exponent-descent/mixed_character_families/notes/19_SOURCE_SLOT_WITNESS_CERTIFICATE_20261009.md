# Physical slots, witness losses, and the source order of choices

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model derivation and source
inspection are internal validation, not independent specialist review or
formal proof verification.

The existing source permits a theorem-level construction that meets the
mixed program's whole-slot length and lower-gain requirements. No concrete
application manifest containing the actual slot system, buffered constants,
and loss assignments was found locally. These are different conclusions:
absence of such a manifest is not an obstruction to the source's quantified
existence argument. The new mixed arithmetic estimate remains open.

## 1. What was inspected

The repository was read without modification. Searches covered the
amplification and exponent-descent manuscripts, their notes, reviews,
numerics and JSON records, and then the entire repository `papers/` tree
and the synced project `sources/` tree for slot-system, original-ID,
provenance, and simultaneous-witness records. In particular I inspected:

- Mixed notes 9, 13, 14 and 15, and the mixed manuscript.
- The amplification source-transfer note `SELECTOR_PRESERVING_SUBCASES_20261008.md`,
  `MOMENT_STRUCTURAL_AUDIT_20261008.md`, the amplitude-profile and joint-witness
  notes, and the amplification manuscript.
- The operational optimizer and its stored synthetic-slot record.

The [primary source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
was fetched and read in memory; no PDF was saved. It has 199 pages and
SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
I inspected PDF pages 56–60, 153–154, 179, 181–186 and 194–197. This checks
the source statements and their quantifiers, not their deep analytic proofs.

## 2. The source already supplies a fixed physical construction

Keep two exponent bases separate:

\[
 U=Z^{d_{\rm base}},\qquad d=2a-1,
 \qquad L=\ell_{\rm geom}/d_{\rm base}.
\]

Here `d_base` measures the physical row norm, `d` is the mixed note's
zero-bin parameter, `ell_geom` is the total physical prime length at base
`Z`, and `L` is its length at row base `U`. The operational scalar constant
`ell=10^-6` is a third, distinct quantity.

Source Proposition 20.3, pages 195–197, constructs a fixed even slot count
`K`, equal physical widths `ell_i=ell_geom/K`, and windows

\[
 I_i=\left(1+\frac{2i-1}{2K+1},\,
             1+\frac{2i}{2K+1}\right)\subset(1,2),
 \qquad 1\le i\le K.
 \tag{1}
\]

Any nonnegative, nonzero smooth `W_i` compactly supported in `I_i` is
allowed. These original windows have gaps and are disjoint before all
ray, excluded-prime and physical row masks. Their common scale is
`P_i=Z^(ell_geom/K)`. The source makes the moment mesh and rounding budget
choices before fixing `K`; narrow windows can change the eventual fixed
seminorms, height orders and thresholds, but cannot invalidate the mesh
by their slot count. The fixed exclusions eventually leave the windows.

Source pages 181–183 identify the physical factors with the smooth full
prime-annulus form. In a fixed presentation, their coefficients are the
finite character expansion of `nu(p) 1_(p in the fixed ray class)`, with
members in the fixed group `Theta`. The coefficient list and selected
indices are independent of the varying row after the presentation,
physical parameters and amplitude bin have been fixed. Conjugating an
entire product handles the opposite common orientation and retains every
zero. Arbitrarily deleting primes from an annulus is not authorized by
this construction.

The moderate physical range in the audited source has `d_base>=1/2` and
provides `L>1/5` by a fixed amount. The proposed mixed application must
retain that dynamic range or provide its own supply proof. In this range

\[
 z_i=\ell_i/d_{\rm base}\le 2\ell_{\rm geom}/K.
 \tag{2}
\]

Thus the original system can be chosen with any prescribed fixed positive
upper bound on `max z_i`, as well as the source moment mesh. This is a
choice of the original system before application; existing slots cannot
be split later to repair a deficit.

## 3. A conditional uniform whole-slot certificate

The following is an explicit *construction interface*, not an assertion
that a particular saved physical vector has already been instantiated.
Assume the existing imported moment/detector package, the retained supply
`L>1/5`, and the mixed operational ranges

\[
 9/25\le d\le21/50,\quad49/100\le x\le1/2,
 \quad7/10\le r<73/100,\quad2/5<m<207/500.
\]

For the marked plain fourth input use **fixed `kappa=3/4`**, conditional
on the imported global family bound `beta_*<=7/8`. This is permitted by
Lemma 18.1. The source's original Part II choice
`kappa=3/4+2 Delta` would have the different capacity
`(1-2m)/(6 kappa)` and cannot silently be assigned the `9/2` denominator.

Choose the original even `K` so that

\[
 h:=\max_i z_i\le \ell/4=1/4000000,
 \qquad h\le\eta_{\rm moment},
 \tag{3}
\]

with strict room if the source mesh requires it. A sufficient symbolic
choice is an even integer greater than
`max(2 ell_geom/eta_moment, 8 ell_geom/ell)`, in the physical range of
(2). All profiles and windows then remain fixed. This possibly very large
finite `K` is allowed by the source's count-independent mesh assertion;
its constants and final height orders need not be practical numerical
constants.

The complete source construction also takes the maximum over its other
fixed rounding allowance `b_round` and its `1/185` separation/supply
bound: require `2 ell_geom/K` strictly below those values as well.
At `ell_geom=1/6`, the width condition alone has minimum even integer
`K=1,333,334`. This is a width-only benchmark, not an instantiated source
slot count: the unevaluated moment mesh or `b_round` may require a larger
one, and a different chosen geometry changes the benchmark.

On a fixed amplitude bin source Section 19.1 gives numbers `g_i` with
`0<=g_i<=d/2`, weighted mean `q=dx`, and, for every selected positive
slot, the exact lower bound `|Q_i|>=P_i^(g_i)`. Zero-amplitude and error
slots are retained when computing the total weighted mean, and need no
lower bound. Set

\[
 \nu_I=\ell/2,
 \qquad c_I=(1-r)/2-\nu_I.
 \tag{4}
\]

Order the original positive slots by decreasing `g_i`, using a fixed ID
order to break ties, and take the whole prefix immediately before it
crosses `c_I`. The total positive supply is sufficient: if `L_+` is its
total length, then

\[
 qL\le(d/2)L_+,\quad
 L_+\ge2xL>49/250=0.196,
 \qquad c_I<3/20=0.15.
 \tag{5}
\]

Consequently a crossing slot exists, and the chosen total `z_I` obeys

\[
 c_I-h\le z_I\le c_I,
 \qquad \ell/2\le t_I=(1-r)/2-z_I\le3\ell/4.
 \tag{6}
\]

Its first strict inverse margin is `1-r-2z_I=2t_I>=ell`. The second is
`3-2r-8z_I=2r-1+8t_I>=2/5`, before the positive buffer contribution.
Fixed annular constants create only eventual `O_K(1/log U)` length
adjustments, absorbed at the eventual threshold as in source page 195.

There is no lower-gain shortfall for this prefix relative to the actual
mean. The weighted average of an initial decreasing segment is at least
the weighted average of the entire list, so

\[
 G_I=\sum_{i\in I}g_i z_i\ge qz_I=dx z_I,
 \qquad\Delta_G=dx z_I-G_I\le0.
 \tag{7}
\]

This uses the source amplitude-bin lower bounds, not a synthetic flat
vector. Rounding is already paid by `t_I`; it must not be charged a
second time as a purported gain loss. The subset is fixed within the
amplitude/presentation subdivision, not chosen afresh on each row.

For the fourth subset choose a whole prefix of this existing `I` just
below

\[
 c_m-\nu_4,\qquad c_m=2(1-2m)/9,
 \qquad\nu_4=1/2000.
 \tag{8}
\]

There is ample supply because `z_I>=0.135-3 ell/4`, whereas `c_m<2/45`.
Every slot has width at most `h`, so

\[
 0<h_J=c_m-z_J\le1/2000+1/4000000<1/1000,
 \quad2m+(9/2)z_J\le1-9/4000.
 \tag{9}
\]

No original prime support or coefficient is changed. The original source
mesh, coefficient class, high-conductor/nonexceptional family requirement,
derivative profiles and common frequency budget still have to be retained.
With these hypotheses (6) and (9) meet Note 9's uniform arithmetic
conditions; they do not prove a new inverse-weighted fourth theorem.

## 4. The remaining detector budget can be allocated existentially

Note 9's actual count/witness test is

\[
 2dx t_I+2\Delta_G+\Lambda\le\ell.
 \tag{10}
\]

From (6), (7), and `dx<=21/100`, the geometric part is at most

\[
 2dx t_I\le(63/200)\ell.
\]

It is therefore sufficient to choose the total remaining application
loss **strictly** below

\[
 \boxed{\Lambda<(137/200)\ell
              =137/200000000=0.000000685.}
 \tag{11}
\]

Here `Lambda` must include the actual combined upper-moment and lower-
witness losses, parameter/buffer allowances, finite subdivisions, and the
height and profile costs allocated to this count implication. Assigning a
number to (11) without accounting for those losses would not certify it.

The source provides an existence procedure for arbitrarily small requested
losses: Proposition 8.3 gives a simultaneous inverse/plain product spike
for every retained row above the floor, with one common presentation and
height; source Section 19.2 fixes finitely many presentations, logarithmically
many dyadic pairs, and applies its Sobolev calculus to the remaining
rowwise parameters. This does not give a witness on every arbitrary
preselected exact tuple `(r,m)`, or one common chosen height across different
detector cutoffs. The actual selected tuples must enter the coverage proof.

The mixed program's local shortened inverse reduction separately needs
its literal contour cost recorded. From primary page 58 its squared
exponent is `d+rho`, with `rho=12e` before other small powers. Thus

\[
 \rho\le1/100000\quad\Longleftarrow\quad
 0<e\le1/1200000.
 \tag{12}
\]

This satisfies Notes 14–15's stated allowance, but it **does not by itself**
certify (11). The chosen `e` may need to be much smaller to meet the actual
detector and envelope costs. One must also require `e<e_0` for every
retained Lemma 8.2 invocation and the source's other fixed real inequalities.
The value of `e_0` is existential in the source and no evaluated value was
found locally.

Prime envelopes also have a literal fixed-buffer cost. Source Lemma 19.1
has a uniform `O(e)` in its prime exponent; after choosing amplitude width
`vartheta` it supplies the exact upper bound
`|Q_i|<=P_i^(g_i+vartheta)<=P_i^(d/2+vartheta)`. Hence an instantiated
certificate must either record

\[
 \Gamma_i=(d+2\vartheta)z_i
\]

or explicitly allocate the difference from `d z_i` in its remaining loss
calculation. A fixed positive `vartheta` is not an arbitrary small power
for every subsequently requested epsilon. The positive-bin lower bound
used in (7) has no `vartheta` loss. Source pages 195–196 allow reducing
`e`, `vartheta`, and the other moment/detector powers after the fixed
slot system has been chosen, within the pretarget real ordering.

## 5. The same original mesh lowers the required common fourth saving

The conservative choice (8) leaves a large fourth-capacity margin. The
already chosen original mesh also permits a finer fourth decrement,
without changing the original system:
\[
 \nu_4=\ell/2,\qquad 0<h_J\le3\ell/4,
 \qquad 1-2m-(9/2)z_J\ge9\ell/4=9/4000000.       \tag{13}
\]
This is still a fixed positive strict margin. It may require smaller
preliminary losses and a finer source moment mesh in the original choice
of \(K\); it does not permit subdividing an existing slot in an application.

Note 9's continuous bound, together with its monotonic extension to
\(t_I\ge\ell/2\), now gives
\[
 \chi_J\le
 \frac{43774520332379}{30789918900000000}
 +\frac{21}{50}\frac{3\ell}{4}
 =\frac{17513687662733}{12315967560000000}
 =0.001422030999790405\ldots<\frac1{700}.             \tag{14}
\]
The uniform spare saving is
\[
 \delta_\chi=\frac1{700}-
 \frac{17513687662733}{12315967560000000}
 =\frac{563861960869}{86211772920000000}
 =0.000006540428781023\ldots .                       \tag{15}
\]
All fixed upper-envelope, buffer, profile and count perturbations of this
fourth criterion must fit strictly inside \(\delta_\chi\), separately from
the witness allowance (11). Those source losses can be requested small
in the prescribed order; their existence is conditional on the imported
analytic package. The baseline convention \(\Gamma_i=dz_i\) must not be
used to discard a fixed positive amplitude-width cost.

Consequently, for this finer *original* source system, the weaker new
arithmetic theorem
\[
 \boxed{F_J\ll_\varepsilon
 U^{1+dr-1/700+\varepsilon}H^b}                       \tag{16}
\]
is sufficient for the operational direct-energy implication. The previous
\(1/540\) target allowed much coarser fourth subsets and remains a valid
stronger sufficient target. No saving in (16) is proved here: the result
reduces the saving that a new correlation theorem needs to supply.

The old high-gcd and small-core removals are still affordable, because
their target exponent is now larger. For example the unbuffered high-gcd
reserve becomes \(d/125-1/700\ge127/87500\), and the old half-power
reserve increases by \(1/540-1/700=2/4725\). All literal fixed-buffer
costs remain as in notes 14–15. The contour and diagonal tests in
[note 17](17_NATIVE_COPRIME_AND_RESPONSE_TEST_20261009.md) and
[note 18](18_NATIVE_ANNULAR_DIAGONAL_TEST_20261009.md) apply with this
new \(\chi\) as well. In particular the unchanged diagonal-majorant gap
is still greater than \(103/500+1/700=363/1750\).

The [small exact checker](../../numerics/check_mixed_marked_bridge.py)
records the rational prefix, margin and refined-saving bounds. Its
arithmetic checks do not certify the source existence statements or the
new selected moment.

## 6. A certificate interface that can be checked

An application record should contain the following fields. The existing
operational optimizer checks rational width and envelope arithmetic;
it does not verify the analytic or provenance fields merely by echoing
them.

| Record | Required content | Availability now |
| --- | --- | --- |
| Source package | Primary SHA and exact lemma references; imported analytic status | Present in notes and independently matched in this read |
| Geometry and bases | Fixed `ell_geom`, moderate `d_base` range, `L>1/5` supply proof, `U=Z^d_base` | General constructions and symbolic margins present; must identify the geometry used in the final application |
| Original slots | Fixed even `K`, stable IDs, `ell_i`, intervals, exact `W_i`, seminorm family, scales `P_i`, disjointness | Source gives (1) and existence; no actual instantiation manifest found |
| Arithmetic presentation | Fixed `S`, ray group `Theta`, common native orientation, finite expansion coefficients, physical zero rules | Source transfer formulas present; final target-dependent arithmetic instance must be specified |
| Buffered bin | Actual `i,a`, `d=2a-1`, presentation label, actual dynamic-domain inclusion and high-conductor cut | Symbolic definitions and imported detector coverage present; no actual row population record needed for the quantified theorem |
| Amplitude class | Fixed physical parameters, `vartheta`, bin vector `g_i`, `q=dx`, lower and upper inequalities | Source guarantees the finite subdivision; no saved application vector found |
| Whole subsets | Stable IDs for `I` and `J`, sorted-prefix rule, `z_I,z_J`, capacities, `t_I,h_J`, `G_I`, `Gamma_I,Gamma_J` | Conditional rules (3)–(9) suffice existentially; existing 512-slot record is explicitly synthetic |
| Simultaneous witness | Source Prop. 8.3 quantifier, common character/height, permitted actual inverse/plain profiles, finite dyadic/presentation cover, loss costs | Source theorem and exact profile recipe present; no instantiated aggregate loss certificate found |
| Real-loss allocation | Actual `e`, `rho=12e`, all `e_0` comparisons, amplitude/upper-envelope costs, named terms of `Lambda`, strict (11) | Symbolic allowance present; numerical choices and evaluated constants absent |
| Height allocation | Fixed internal orders, cumulative frequency matrix/shares, target-dependent `A_ht`, allowed `tau`, later external tail order and threshold | Source formula exists; no evaluated application orders or height ceiling found |
| Fourth input | Fixed `kappa=3/4`, family `beta_*<=7/8`, nonexceptional row condition, source mesh and original profile classes | Explicit conditional import, not independently proved |
| New arithmetic theorem | Derivative/profile/height-uniform bound for the actual selected fourth correlation | Still open; neither the construction nor a finite native test supplies it |

The absent instantiated fields can be resolved by a theorem-level choice
of the source's constants and a proof of uniformity. They need not be
measurements of a conjectural selected zero population. Conversely, a
numerical slot vector without its analytic source provenance would not
replace this certificate.

## 7. The order that preserves the source quantifiers

1. Fix the intended real ranges, physical geometry, positive application
   reserves, moment losses, capacity decrements and requested original mesh.
   Invoke the source's slot-count-independent moment mesh.
2. Fix one original even `K`, its intervals and smooth profiles, with (3).
   These precede the target and the large scale. Establish the supply and
   prefix arguments as uniform rules on each later amplitude subdivision.
3. Choose the fixed amplitude and bin widths and real buffer `e` small
   enough for (11), (12), each `e_0`, and the literal upper-envelope costs.
   Retain the original frequency allowances; finer binning only creates
   another fixed finite subdivision.
4. Fix the target-dependent arithmetic data and final fixed exclusions.
   Determine the finite internal profile, moment and Sobolev orders. This
   produces a finite `A_ht` and a minimum positive detector allowance
   `epsilon_ht`.
5. As in source pages 186 and 197, choose
   `0<tau<=min(d_base,min/100, d_base,min epsilon_ht/[20(A_ht+1)])`.
   Then `T1=Z^tau` satisfies every retained finite-height condition at a
   sufficiently large threshold. Each L-argument uses one common allotted
   frequency budget, not a renewed budget at each shift.
6. Only after `tau` is fixed choose the external tail orders. Their
   enlargement changes external seminorm constants and the threshold,
   and must not change an internal height order or the already fixed mesh.

The original source uses this order to prove its own global boundary.
Its positive Part II margin depending on `Delta=beta_*-7/8` cannot be
quoted after changing the contradiction; the mixed application uses its
own fixed reserves and the permitted fixed `kappa=3/4` moment input.
The later full family-boundary reuse, low estimate and contour audit are
separate obligations.

## 8. Conclusion

There is a source-compatible conditional construction of whole `I,J`
with the required capacities and no positive lower-gain shortfall relative
to the actual mean. It leaves a strictly positive, explicit detector-loss
budget, and it can be fixed before application. The repository currently
records the abstract optimizer, source existence statements and synthetic
checks, rather than one completely instantiated analytic application.
That distinction should be stated without claiming that the source lacks
the existence mechanism. The outstanding arithmetic theorem, actual
uniform loss bookkeeping and program-wide bin/boundary coverage remain.
With the finer fourth choice (13), the common sufficient new saving is
\(1/700\). The next arithmetic proof should retain the full signed
coprimality combination through its transformed bilinear kernel, or prove
the weighted response-tail criterion, with the original selected rows.
The separately positive marked-diagonal approach has the native
coefficient obstruction in note 18. A theorem only for \(g=1\) would
still need extension to the aggregate \(Ng<cU^{1/125}\) before the
direct selected-energy implication closes.
