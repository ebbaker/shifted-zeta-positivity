# RGD-E02 r2 — first next-order verification from existing data

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual **gpt-6.1-sol (Codex), effort ultra**,
research chat0003, thread `01a1a77f-2607-7832-9902-29399c58b442`, turn
`01a1a7ac-1448-7770-b86d-3264bc4b53e2`.

**Disposition: E02 r2 complete; all frozen checks pass, first attempt.**
Under [Packet08][packet], the existing accepted acquisition verifies
[Note05][lemma]'s premises and complete analytical closure at **(r,k)=(4,1)**:
\[
\boxed{\mathcal R_{4,1}/q^*_{4,1}<1/15,\qquad
Q_{4,1}\ge L_{4,1}>\frac7{3000}(c_1^*)^8
>\frac7{3000^9}>3\cdot10^{-31}.}
\]
This is exact rational verification plus a checked analytical norm theorem,
inheriting the accepted Arb/FLINT input enclosures. **No new integration,
floating feasibility calculation, source mode, moment, index scan or
precision selection was performed.** The simple final number is a weak
rational consequence, not a measured determinant or remainder value.

The [checker][code] uses the Python standard library only; the
[49,060-byte exact record][record] preserves its input dyadics, derived
rational intervals, polynomials, every checked inequality and hashes.
All recorded checks pass. Execution used **Python 3.10.0**, took
**0.023964500 seconds**, and performed **zero integrand evaluations**.
Only one of the two permitted runs was used; no correction or cap occurred.
The old E02 r1 acquisition and every frozen input remain unchanged.

## 1. What was assessed and reused

Note05 is Astra/max's conditional analytical return. The coordinator and
one fresh read-only Sol/ultra contributor checked its norm argument,
Hessenberg recurrence, endpoint signs, finite closure and scoped growth
claim. This is a **different-model internal check of that analytical
argument**, with shared acquisition/source premises. The coordinator
wrote and ran the new checker; implementation checks are author checks,
not specialist-independent review. The [assessment/author-check note][review]
records that relationship. The new application is not retroactively
covered by E04 r2's assessment of the old r=3 pilot.

The trusted input is the single existing 384-bit acquisition accepted in
[E04 r2 Review03][priorreview]. Only its compact moment balls j=0,...,5
and six E/B pairs are used. Short `display` strings are never mathematical
inputs. The old checker was neither imported nor rerun. New arithmetic
uses exact integer powers and Fraction operations on serialized dyadics.

The source is still complete canonical theta at physical time zero,
b=1/16 exactly, U=2, and the full unit-square source/spatial payment E+B.
The compact reference is unchanged; it is not replaced by a full first
mode or a Gaussian. No PF property of the positive atomic reference is
assumed, and no desired canonical D5 sign supplies a reference margin.

## 2. Fixed input-box verification

For saved X_j=[l_j,u_j], the checker constructs
C0=[1/16-u0,1/16-l0] and
Cj=[l_(j-1)-u_j,u_(j-1)-l_j], j=1,...,5.
Every lower endpoint is positive, and lower(C1)>1/3000. Its reading is
about 3.589284178466e-4. Normalized ratio enclosures use the prescribed
positive endpoint orientations; exact inclusion holds in all four boxes:

| j | Approximate reading of t_j, not an enclosure endpoint | Required exact rational box |
| --- | --- | --- |
| 2 | 4.652039934289E-1 | [93/200, 233/500] |
| 3 | 1.357560422245E-1 | [27/200, 137/1000] |
| 4 | 2.818186831125E-2 | [7/250, 29/1000] |
| 5 | 4.465684872336E-3 | [1/250, 1/200] |

The displayed readings are rounded aids only; the exact lower and upper
fractions are in the record. They use lower(C0)^(j-1)*lower(Cj)/upper(C1)^j
and the corresponding upper expression. No endpoint was loosened.

For each j, saved E and B have strictly positive lower endpoints. The
checker adds upper(E)+upper(B) **exactly**, then rounds upward to the
fixed absolute dyadic grid 2^-384, verifying containment. Nonzero B is
paid even though it is vastly smaller than the working grid. The resulting
entry-relative upper allowances satisfy the required epsilon=1/40000:

| j | Approximate reading of the exact relative upper allowance |
| --- | --- |
| 0 | 1.423934251493E-7 |
| 1 | 2.466226601680E-5 |
| 2 | 3.781535701583E-6 |
| 3 | 9.243386908155E-7 |
| 4 | 3.176136657802E-7 |
| 5 | 1.429748170496E-7 |

The largest occurs at j=1, about 2.466226601680e-5, below 2.5e-5. At j=0
the expression is Tbar0/lower(C0); at j>=1 it is
(Tbar_(j-1)+Tbar_j)/lower(Cj). These are upper allowances for the full
source/spatial error, not measured actual coefficient errors. The
accepted acquisition uncertainty is already included in every endpoint.

## 3. Analytical norm proof and exact algebra

For the weighted coefficient norm ||H||_T=sum|h_alpha|T^alpha,
coefficient convolution proves submultiplicativity. Expand each collected
homogeneous degree-n determinant monomial around its positive reference
coefficients. Since every linear coefficient perturbation has norm at
most epsilon*c_j*, all **nonconstant** terms together are bounded by
\[
B_{n,1}\le[(1+\epsilon)^n-1]H_{n,1}(c^*).
\]
The binomial factor includes all degrees 1,...,n; it is not a first-order
Taylor estimate. Negative-index entries vanish identically and need no
relative bound. The exact c0 boundary remains in every term.

The checker independently compares the recurrence-derived Dn,1,
n=2,...,5, with permutation expansion in formal c0,...,c5. It verifies
homogeneity and normalizes each monomial to (c1*)^n f_n(t2,...,t5).
The resulting four f_n are exactly Note05 (11); their collected absolute
coefficients give precisely S_n in (13). The new degree-eight identity
\[
D_{4,1}^2-D_{4,0}D_{4,2}=D_{5,1}D_{3,1}
\]
passes formal permutation checking, including negative-index zeros and
the entire c0 boundary. Its collected c polynomial has 15 terms. That
finite identity is normalization evidence, not a sign argument.

Put d_n=Dn,1(c*) and Delta_n=Dn,1(C(z))-d_n. Subtracting the constant
from the **same combined polynomial** through the product identity gives
\[
P_{4,1}(z)-q^*_{4,1}=d_5\Delta_3+d_3\Delta_5+\Delta_5\Delta_3.
\]
All three pieces are retained. Submultiplicativity bounds its exact
coefficient norm by |d5|B3+|d3|B5+B5B3. This pays all translated degrees
through eight, including the nonlinear product remainder. It does not
replace the target with a separately bounded original neighboring product,
a sampled sign, or an unrelated simpler test. No large translated array
is needed because the norm theorem pays those degrees symbolically.

## 4. Exact finite margin/error closure

Derivative signs on the entire coarse rational box are verified exactly.
In particular, partial_t2 f5<=-1.474<0 and partial_t3 f5>=2.068>0;
f4 has the displayed negative/positive signs as well. Endpoint evaluations
and strict convenient bounds are:

| n | Exact endpoint interval (terminating decimals are rational) | Strict f_n bounds | Strict S_n upper bound |
| --- | --- | --- | --- |
| 2 | [0.534, 0.535] | 1/2 < f2 < 3/5 | 3/2 |
| 3 | [0.203, 0.207] | 1/5 < f3 < 1/4 | 21/10 |
| 4 | [0.060156, 0.067225] | 3/50 < f4 < 7/100 | 3 |
| 5 | [0.012648, 0.021265] | 1/80 < f5 < 1/40 | 21/5 |

Thus reference f5 and f3 are positive on the full box without importing
canonical PF44 positivity or assuming the reference is PF. Exact binomial
checks give h_n=(1+epsilon)^n-1<(n+1)/40000 for n=2,...,5. Higher terms
are included: their binomial coefficient sum is at most 26 and
26*epsilon^2<epsilon. The resulting b_n=B_n/(c1*)^n strict upper bounds
are 9/80000, 21/100000, 3/8000, 63/100000.

The checker verifies both matched analytical sums, including their
product-remainder terms:
\[
\frac{149067}{640000000}<\frac1{4000},\qquad
\frac{1628823}{10^{10}}<\frac1{6000}.
\]
With reference floors 3/100 and 1/400, these give the unchanged relative
ceilings <1/120 at r=3 and <1/15 at r=4. They are conservative analytical
budgets on the same mechanism. Their factor-eight comparison is **not
measured growth of the exact error**.

At the requested new case, q*4,1>(c1*)^8/400 and
R4,1<(c1*)^8/6000. Consequently
\[
L_{4,1}>\left(\frac1{400}-\frac1{6000}\right)(c1^*)^8
=\frac7{3000}(c1^*)^8>\frac7{3000^9}>
\frac3{10^{31}}.
\]
The intermediate rational floor is about 3.556368439770e-31; it is a
proved lower consequence, not an optimized endpoint. Note01's complete
moment payment and the same joint norm argument give actual Q4,1>=L4,1.
The inherited **actual-source D3,1>0** then implies
D5,1>3e-31/D3,1. No numerical D3 or relative eta was acquired, and no
canonical D5 sign entered the argument.

## 5. Scoped limitation and continuation

Note05 (19)–(20) is also checked analytically. For j>=2 and u in [0,2],
u^2/[(2j)(2j-1)]<=1/3, so 0<c_j*<=a_(j-1). The compact support then
gives c_j*<=a0*4^(j-1)/(2j-2)!. With positive a=16*pi-1,
K=exp(-4*pi)/[8*(1-exp(-5*pi))], the entry-relative upper allowance is
at least
\[
\frac{K}{a a_0}\frac{(2j-2)!}{(4a^2)^{j-1}}\longrightarrow\infty.
\]
Its successive factor ratio is (2j)(2j-1)/(4a^2). This excludes a fixed
uniformly small entry-relative epsilon for all moment indices with this
compact reference and original E vector. It does **not** show that the
exact joint R/q fails or that a canonical determinant is negative. No
infinite sequence of new data was computed to establish this analytic
limitation.

Read the [result index][results], [theta cluster][theta],
[control screen][controls] and [avoid index][avoid], especially
[joint estimates][a12], [scope][a07], [bounded numerics][a10] and
[shared review][a05]. The polynomial norm lemma is generic; canonical
application uses the complete unit-square source and its paid input box.
Weighted-square and Euler-factor controls change those inputs; reflected
and smooth positive-primitive controls lack the literal square expansion.
No uncalculated control-box failure is asserted, and positive-time
collisions do not refute this time-zero finite-order bound.

The first next-order application is now closed, but k=2,3,4, the k=5
pure-volume triple, all large k and full order induction remain outside
the result. Known finite-order positivity already covers order five;
no new positivity range or RH conclusion is claimed. Full B03 remains
gated on reference margins/conditioning and a useful domain-dependent
error comparison, rather than the false uniform entry-relative premise.

**Next: [E] RGD-E04 r3 — Sol**, assess this fixed new application and
Note05's lemma under the [continuation/model-change packet][next]. No new
integration or new index is part of that assessment. The later conceptual
question is how to control the original joint payment against a justified
margin as r,k vary; that remains unresolved, not silently selected here.

## Versions and reproducibility

Exact record SHA-256: `9ddc5881df258c3dbdfe611bf0c620c74cbd1292e0628d0e00dbca30a4e06e9a`.
New checker SHA-256: `934f0ad3ab8321de6751508ef24d70a87d19b6ca848ebf9be9addce610fb6b34`.
All frozen inputs matched before the sole run:

| Input | SHA-256 |
| --- | --- |
| notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md | `93ac9495bf685a4464ca7751ae89b7218364f635b522aa80dbc4f554f6007a2b` |
| numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json | `6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298` |
| numerics/rgd_e02_two_case_certificate.py | `b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4` |
| reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md | `4c1d9e07f620e49f6d2fcaad538f176549316e19e8f11d9010cc52f4856b3807` |
| notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md | `556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847` |
| research-progress/handoffs/08_RGD_E02_R2_EXISTING_DATA_NEXT_ORDER_AND_MODEL_CHANGE_20261104.md | `c58c87ce3af0b4ca67c320b883929bdc6dc4b366d11f21dace57b683024d3d6c` |

Use the saved exact record for review. To regenerate later under an
explicitly requested review/replay scope, run the installed standard-
library checker with --output pointing to a **fresh** temporary filename.
It refuses to overwrite a record. No replay is requested by this return.
No manuscript snapshot, large array, PDF, parent/sibling artifact or global
index was changed; preexisting working-tree changes are not attributed
to this execution.

[packet]: ../research-progress/handoffs/08_RGD_E02_R2_EXISTING_DATA_NEXT_ORDER_AND_MODEL_CHANGE_20261104.md
[lemma]: 05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md
[priorreview]: ../reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md
[record]: ../numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json
[code]: ../numerics/rgd_e02_r2_next_order_existing_data_check.py
[review]: ../reviews/04_RGD_E02_R2_ANALYTICAL_ASSESSMENT_AND_AUTHOR_CHECKS_20261104.md
[next]: ../research-progress/handoffs/09_RGD_E04_R3_NEXT_ORDER_ASSESSMENT_AND_MODEL_CHANGE_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
