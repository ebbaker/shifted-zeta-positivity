# Selected inverse distribution: a cubic frame target and an absolute-value obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model calculations and review are not independent specialist validation.

**Result.** Reversing the positive plain frame gives a legal smooth
column kernel while preserving the exceptional-row selector. Conditional
on the imported global family theorem and its quantitative growth lemma,
this kernel has a uniform nonprincipal bound `N^(-1/8+epsilon)`. It is
too weak for absolute Schur, and even hypothetical square-root cancellation
would not make that method reach the target. An exact cubic-character
frame explains this loss without appealing to the earlier abstract
marginal-amplitude model.

A third matrix trace gives a more specific sufficient target: a signed
cyclic correlation over three pairwise inequivalent primitive row
characters. The actual sixth-power-free family has uniformly bounded
primitive-character fibers. The existing inputs therefore control
every triple in which a primitive character repeats, with a fixed
exponent margin on the buffered application region.
No bound for the remaining cyclic correlation, new zero-free boundary,
or RH implication is proved.

This continues
[MIXED_CONDUCTOR_REFINEMENT_20261008.md](MIXED_CONDUCTOR_REFINEMENT_20261008.md).
Use its operational `(d,x,r,m)` region, `s`, `ell=10^-6`, actual
polynomials, and derivative-profile requirements. The original
[amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex)
and its [energy note](../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md)
remain the source of the analytic assumptions.

## 1. The actual weighted plain frame

At fixed common separating parameters let

    w_u = 1_(u in C+) |M_r(u) Q_I(u)|^2,
    A = sum_u w_u,  W = max_u w_u,
    N=U^m,
    T_(u,k)=N^(-1/2) psi_u(k) B(Nk/N).

Columns are all ideals in the original fixed plain annulus; original
fixed zeros may be retained as zero columns. Let `L_N` be their count,
so `L_N << N` with the allowed fixed-support constants. Take the column
vector `1` on that support. Then `T1=S_m` exactly. Define

    G = diag(sqrt(w)) T T* diag(sqrt(w)),
    K(u,v) = N^-1 sum_k |B(Nk/N)|^2 psi_u(k) conjugate(psi_v(k)). (1)

All entries use the actual coefficients and fixed profile; `G` is positive
semidefinite. The mixed energy obeys

    E_(C+) = ||diag(sqrt(w)) T1||^2
      <= L_N ||G|| <= L_N [Tr(G^3)]^(1/3).                (2)

Zeros of `w` can be removed when dividing by `sqrt(w)` below; their
contribution is identically zero. No weight on a surviving row has been
changed. In particular the Möbius and physical-prime coefficients remain
inside their actual positive weight, and every original prime annulus,
whole slot, cutoff and exclusion remains in place.

With a common ray presentation `psi_u(k)=nu(k)chi_k(u)^s_chi`, the
fixed ray phase cancels in (1), leaving `|nu(k)|^2`. Its zeros do not
cancel. The row-product character has an inducing primitive finite-order
Hecke character `vartheta_(u,v)`; write its conductor norm as `Q_(u,v)`.
Let `R_(u,v)` contain the radical of every original forbidden prime
for either factor, including the fixed presentation's zeros. Exactly,

    psi_u(k) conjugate(psi_v(k))
      = vartheta_(u,v)(k) 1_((k,R_(u,v))=1).              (3)

One can omit from `R` primes whose zeros are already supplied by the
primitive character, but retaining them is harmless and avoids mistakes.
If the phase becomes principal, all canceled-ramification zeros are still
in the mask. The conductor `Q_(u,v)` is a **row-ratio** conductor; it
is neither the physical row conductor nor either column-ratio conductor
of the previous residual.

The primitive conductor divides the product of the original row
conductors, hence `Q_(u,v)<<U^2`. The deletion radical has polynomial
norm in `U` from the two physical rows and fixed arithmetic data. Keep
this exponent fixed before choosing the arbitrary small analytic loss.

This transposition is legitimate because the inner sum in (1) is a
complete smooth ideal sum. The sharp selected-row indicator remains
outside it. However, imposing the **column-pair** high-conductor
restriction from `T_joint` directly on this matrix would generally
destroy its positive Gram form. We apply (2) to the full positive energy;
the previously established small-sector reduction then transfers any
successful energy bound to the original signed residual. No identity
with a silently unfiltered `T_joint` is asserted.

## 2. A legal conditional entrywise estimate

The source PDF consulted locally has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
In the [September 30 source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
**Lemma 4.9, page 22**, explicitly gives, for each fixed `b>=beta_*`
and positive `v`, quantitative bounds for both `L` and its reciprocal
on `Re s>=b+v`, of arbitrarily small power in the primitive conductor
and height. **Lemma 4.10, page 23**, bounds a deleted Euler product
by an arbitrarily small power of its polynomial-size radical on any
fixed positive half-plane. Both lemmas and the source's global
`beta_*<=7/8` are imported analytic assumptions here. A bare statement
about zero locations is not substituted for those growth estimates.

Mellin inversion of `|B|^2` and (3), for nonprincipal `vartheta_(u,v)`,
give an integral of

    N^(s-1) Mellin(|B|^2)(s) L(s,vartheta_(u,v))
       product_(p|R_(u,v)) (1-vartheta_(u,v)(p) Np^(-s)). (4)

Move the line to `Re s=7/8+v`. There is no principal pole. The
source's stated primitive growth and deleted-factor bounds, together
with the Mellin decay of the smooth annular profile, give

    |K(u,v)| <<_epsilon U^epsilon N^(-1/8) H^A
       whenever vartheta_(u,v) is nonprincipal.          (5)

Here choose the contour displacement and the source conductor/radical
losses small enough to fit the requested final `epsilon`; `m` lies in
a fixed bounded interval. The possible conductor `U^2`, instead of
`U`, merely changes that allocation. The height in the Mellin integral
is integrated against a sufficiently high fixed number of profile
derivatives. The argument is required for every derivative profile
used in the source's positive-norm Sobolev procedure. For a fixed
profile-specific amplitude envelope this uniformity is an additional
obligation; the universal physical-profile envelopes avoid that issue.

For a principal row ratio, the masked ideal count instead has its
possible main term. The elementary bound `|K(u,v)|<<H^A` always holds;
one must not apply (5). Source Lemma 18.3 evaluates such fixed-ray
masked smooth sums. The separate bounded-fiber argument below uses
the source's exact local reciprocity, not that smooth-sum estimate.

Thus (5) is an actual conditional selector-preserving **dual-kernel**
estimate. Its weakness, rather than a missing selector in its proof,
is the obstruction for the first operator argument.

## 3. Why absolute Schur does not suffice

Define the maximum weighted primitive-character fiber mass

    P = sup_u sum_(v: vartheta_(u,v) principal) w_v.       (6)

**Bounded-fiber lemma for the actual physical family.** Assume the rows
are nonzero sixth-power-free elements, as in the source application,
and keep the common fixed ray presentation and orientation. Then

    #{v: psi_v^*=psi_u^*} <= 6^(|S|+1),
    P <= 6^(|S|+1) W.                                  (6a)

If all physical rows are coprime to `S`, the constant can be replaced
by six. These are upper bounds; the fixed ray and unit data can reduce
the actual fiber further. An abstract row family without sixth-power-
freeness is not covered by (6a).

Proof: source equation (4.8), page 16, writes the numerator row
character as a product of its exact good-prime factors
`chi_p(k)^(v_p(u))` and a finite-ray factor ramified only in the fixed
set `S`. The latter retains the unit, fixed-prime valuation and good-ray
data. Consequently the local factor of the quotient for `u,v` at
`p notin S` has exponent

    s_chi [v_p(u)-v_p(v)] modulo six.

The prime character has exact order six. Equality of the inducing
primitive characters therefore forces this exponent to be zero.
Fixed-ray factors cannot cancel ramification at a good prime. As each
valuation lies in `{0,...,5}`, the valuations of `u,v` are equal outside
`S`. This argument uses the actual exponent, not just the order of
each individual local character: exponents one and five have the same
order but give different characters.

Equivalently, factor the integral element `uv^5=w a^6` with `w`
sixth-power-free and its unit retained. On ideals coprime to `Suv`,
the quotient is exactly `chi_k(w)^s_chi`. It induces the principal
character when `psi_u^*=psi_v^*`. The local statement of source
Section 8.1, page 56, then forces `w` to be supported on `S`, giving
the same valuation conclusion. Equality on the common coprime ideal
group determines the inducing primitive character; this argument
does not replace either imprimitive zero extension.

With the good ideal part fixed, each prime in `S` has at most six
valuation choices. An ideal in the Eisenstein ring has at most six
element generators, its units. This proves the first inequality in
(6a), and summing the actual weights proves the second. Both the
exact reciprocity formula and its local ramification consequence are
used within the imported source's arithmetic convention. No moving
good prime is absorbed into the fixed ray data.

All masks in (1)--(3) remain present. In particular, two rows with
the same inducing character need not have identical masked kernels.
The lemma counts the rows; it does not equate their imprimitive
presentations on primes deleted from only one of them.

Weighted Schur with test vector `sqrt(w_u)` gives

    ||G|| <= sup_u sum_v w_v |K(u,v)|
      << U^epsilon H^A [P+A N^(-1/8)].

Consequently (2) would give only

    E_(C+) << U^epsilon H^A [N P+A N^(7/8)].             (7)

By (6a) the principal term is now bounded by `N W` up to a fixed
arithmetic constant and allowed profile costs. This term is harmless
on the application region. The nonprincipal term in (7) is still
far from the mixed target.

Suppose optimistically that every nonprincipal entry were bounded by
`U^epsilon N^(-1/2)` instead. The same argument still yields

    E_(C+) << U^epsilon H^A [N P+A N^(1/2)].             (8)

Use the available selected inverse mass `A<<U^(1-mu)` from the previous
note, with the universal envelope

    g=d(r+z),  W<<U^(g+epsilon)H^A,
    mu=max(0,1-R*-ell-g).

The nonprincipal term in (8) exceeds the target exponent `1+dm-s`
by

    (1/2-d)m+s-mu.                                     (9)

For the near-saturated legal choice
`z=(1-r)/2-rho`, `0<rho<=ell`, one has `mu<=eta+2ell` throughout
the buffered region. This follows from equation (20) of the previous
note, `a_r>-(39/14)ell`, and `d<=21/50`; the decrement `rho` adds
at most `d ell` to that equation. Since `m>2/5` and `s>=0`, (9) is
at least

    (1/2-21/50)(2/5)-(eta+2ell)
      =15899/500000 =0.031798.                          (10)

This is a deficit in the **available absolute-Schur exponent**, not a
lower bound for the actual arithmetic energy. Special weighted
distribution of exceptionally small kernels could improve absolute
Schur, but generic square-root control by itself does not.

## 4. Exact cubic-character obstruction to discarding phases

Here is a separate finite-character theorem showing that this loss is
real for the specified method, even for an ideally conditioned frame.
It is not an Eisenstein/Möbius counterexample.

Let `q=3^n`, let `chi` be a nontrivial additive character of `F_q`,
and choose `B>=2` distinct nonzero elements `b` of `F_q`. Columns are
the `q` points `(y,y^2)` of the quadratic graph. Rows are the distinct
characters of `F_q^2` indexed by `(a,b)`, with every `a in F_q` and
the chosen `b`'s. Their normalized entries are

    T_((a,b),y)=q^(-1/2) chi(a y+b y^2).                 (11)

These are cubic character phases, hence also sixth roots of unity;
there are no nonunit masks in this unit-group example. For each fixed
`b` the `q` rows are an orthonormal basis. Thus

    T*T=B I_q,  ||TT*||=B,  Tr((TT*)^3)=q B^3.           (12)

For different `b,b'`, completing the square gives a quadratic Gauss
sum and

    |(TT*)_((a,b),(a',b'))|=q^(-1/2).

An elementary proof of the Gauss magnitude squares its modulus,
sets `h=y-z`, and uses additive orthogonality in `z`; only `h=0`
survives, giving exactly `q`. Within one basis the off-diagonal entries
are zero. Therefore the entrywise modulus matrix has constant row sum
and exact operator norm

    || |TT*| || = 1+(B-1)sqrt(q).                        (13)

For uniform row weight `w`, its signed norm is `wB=A/q`, whereas its
unsigned norm is `w[1+(B-1)sqrt(q)]`, of size `A/sqrt(q)` when `B`
is bounded below by two and grows. Absolute Schur loses a factor
comparable to `sqrt(q)` even though the signed frame is exactly tight.
All principal row-ratio fibers are singletons, so this example isolates
the nonprincipal loss.

The actual column vector `1` also causes no large values here:
because the chosen `b` are nonzero, every normalized row sum has
squared modulus one. Its weighted energy is exactly `A`.
Thus a small true energy and the failure of the entrywise-modulus
bound occur simultaneously.

For clarity about cubic cancellation, the all-identical and exactly-two-
equal row contributions to the trace in (12) total `qB(3B-2)`.
The signed pairwise-distinct contribution is

    qB(B-1)(B-2),

whereas the sum of its individual term moduli is

    q^(3/2) B(B-1)(B-2).                               (14)

Thus even the cubic expansion loses a factor `sqrt(q)` if its cyclic
phases are discarded. This is a specified obstruction to an absolute
operator/trace proof, not to retaining the signs.

The abstract scales can match those forgotten by the Schur reduction:
put `q=N=U^m` along a sequence and choose
`B` of order `U^(R*+ell-m)`. The buffered region has
`m<R*+ell<2m`, so such choices exist with `B<=q-1` at large scales.
Set total mass `A=U^(1-mu)` and uniform weight `w=A/(qB)`.
Its exponent is at most `g`, exactly as permitted by the mass and
pointwise inverse bounds. This does not realize the actual Möbius
coefficient or physical annulus; it shows why a method that has
forgotten those structures cannot infer the missing phase cancellation
from the surviving mass, count and square-root bounds alone.

## 5. A cubic target with controlled repeated-character sectors

The sufficient trace exponent from (2) is

    h_3=3[1-(1-d)m-s],
    Tr(G^3) << U^(h_3+epsilon)H^A.                      (15)

A perfectly tight weighted frame would have trace about `A^3/N^2`.
If that stronger estimate held, (2) would give `E<<A N^(1/3)`.
The reason to use a cube is `d>1/3`: the target (15) permits a factor

    U^((3d-1)m+3mu-3s)

above the ideal tight-frame trace. Throughout the buffered region this
exponent is at least

    (3(9/25)-1)(2/5)-3(eta+2ell)
      =15697/500000 =0.031394.                          (16)

Requiring perfect tightness would therefore ask for unnecessarily much.
A second trace/Hilbert--Schmidt bound instead leads back to the square-root
loss in (8).

There is also an exact rank check. Write `Z=Tr G`; since `rank G<=L_N`,
the nonnegative eigenvalues satisfy, for every integer `k>=2`,

    Tr(G^k) >= Z^k/L_N^(k-1).

If `Z` has the same exponent `1-mu` as the available inverse mass,
compatibility of a `k`th-trace sufficient target with this lower bound
requires

    (kd-1)m+k(mu-s) >= 0.                              (16a)

The finite frame above has `Z=A` exactly. In its near-saturated regime
the quadratic target violates (16a), whereas the cubic target has the
positive reserve in (16). For the actual masked frame, `Z` is the
diagonally weighted mass `sum_u w_u K(u,u)`; no lower bound `Z~A` is
assumed for arbitrary derivative profiles. The rank statement is
unconditional with `Z`, and the exponent interpretation is explicitly
conditional on the stated trace size. This explains the choice of
three without assuming nonexistent diagonal lower bounds.

Expand the actual trace, with the fixed profile and every mask intact:

    Tr(G^3)=sum_(u,v,h in C+) w_u w_v w_h K(u,v)K(v,h)K(h,u).

Partition the selected rows into classes `c` according to their
inducing primitive character. Write `A_c=sum_(u in c) w_u`, so
`sum_c A_c=A` and `max_c A_c=P`. Let `G_cd` be the corresponding
matrix blocks. The exact decomposition is

    Tr(G^3)=D_char+R_char+C_neq,                         (17)
    D_char=sum_c Tr(G_cc^3),
    R_char=3 sum_(c!=d) Tr(G_cc G_cd G_dc),

where `C_neq` contains precisely those triples whose three inducing
primitive characters are pairwise different. Such rows are necessarily
physically distinct. Reversal makes `C_neq` real, but its summands
need not be positive. The first two block sums are nonnegative:
`G_cc` is positive semidefinite, as is `G_cd G_dc`, so their product
has nonnegative trace.

When all three characters agree, the crude masked kernel bound gives
an absolute majorant `sum_c A_c^3 <= A P^2`. When precisely two agree,
each cyclic product has two nonprincipal cross-class kernels. Applying
(5) to them gives the absolute majorant
`3 N^(-1/4) sum_(c!=d) A_c^2 A_d <=3 A^2 P N^(-1/4)`.
Together with (6a), these prove

    D_char << U^epsilon H^A A P^2 <<_S U^epsilon H^A A W^2,
    R_char << U^epsilon H^A A^2 P N^(-1/4)
           <<_S U^epsilon H^A A^2 W N^(-1/4).           (18)

Thus the bounds cover all repeated **characters**, including different
physical rows in the same fiber. They use no equality of their
masked kernels. No selected row or zero mask is dropped from the
original signed expansion.

Both terms are already below (15) on the buffered application region.
For `D_char`, even the coarse original rectangle gives a margin
`154297/500000>3/10`. For `R_char`, discarding the useful `2mu`
improvement leaves the margin

    h_3-(2+g-m/4)
       >=1-d(1+r)/2-(11/4-3d)m-3s.                     (19)

To bound (19) continuously, replace `r,m,s` by the valid upper bounds

    r<=r_new+(eta+ell)/[d(1-x)],
    m<=m_new+ell/(dB_x),
    s<=eta+2ell.

The coefficient `11/4-3d` is positive. Exact rational interval
evaluation on 1,024 closed cells covering the full `(d,x)` rectangle
proves the resulting lower bound is at least

    147/12500 =0.01176.                                (20)

All small analytic losses and the fixed polynomial height cost can be
assigned inside this margin in the prescribed order. This is a genuine
controlled part of the actual cubic trace, not an assumed kernel
orthogonality or an endpoint numerical sample.

The new remaining sufficient arithmetic statement is therefore

    Re C_neq << U^(h_3+epsilon)H^A,                     (21)

uniformly in the buffered region and required profile/height families.
Every surviving cycle has three pairwise inequivalent inducing
primitive characters. The principal-fiber obligation is resolved
for the actual sixth-power-free family by (6a).

Equation (21) is stronger than the original fixed-coefficient mixed
energy target because (2) bounds an operator. It is not claimed
equivalent to that target or already implied by the source moments.
The useful progress is the legal transposition, bounded actual fibers,
controlled repeated-character sectors, and the explicit signed cyclic kernel to which further
arithmetic analysis can be directed. An inequality only for its
individual term moduli would miss the phenomenon in (14).

## 6. Reproduction and next step

Run

```sh
python3 papers/quasi-rh-exponent-descent/numerics/check_selected_inverse_distribution.py
```

The [script](../numerics/check_selected_inverse_distribution.py) reuses
the exact rational interval class in the previous cutoff script and
checks all quadratic Gauss sums over `F_3`, `F_9`, and `F_27` with
integer arithmetic in `Z[omega]`. Exact local sextic phase tests
also distinguish equal orders from equal characters and retain the
zero mask when a phase cancels. These tests do not prove reciprocity;
that input is explicitly attributed above. The script verifies the continuous
repeated-character margin and the exponent budgets above. Its small
[record](../numerics/selected_inverse_distribution_certificate_20261008.json)
contains no large matrices and proves no asymptotic arithmetic moment.

The next useful attempt should estimate the weighted **cyclic** product
in (21), retaining its phase, or exploit the weaker actual column vector
instead of seeking a full operator estimate. A conductor decomposition
must control the distribution of the actual `w_u` among row-ratio
characters and masks. Merely improving an entrywise bound to generic
square-root size cannot close the displayed absolute-Schur budget.
No uniform family-moment theorem for the cycle has been supplied here.
