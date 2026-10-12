# Theta transformation and uniformity review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Parallel
model checks are internal scrutiny, not independent specialist validation
or formal verification.

## Result and mathematical boundary

The October 5 theta transformation and its moving-prime uniformity pass
this scoped internal audit, assuming the stated classical cubic
reciprocity and theta automorphy/coefficient theorems. The comparison
reaches the source's complete Appendix A.2 argument. It does not merely
reuse the earlier conclusion about the September 30 manuscript.

No substantive defect was found in the inspected transformation. Two
compressed parts need explicit explanation: the choice of representatives
avoiding zero entries in residue symbols, and the strip-growth argument
used to move the Mellin contour. Both admit the derivations recorded here
without adding a cancellation estimate or a new uniformity hypothesis.

The cusp formulas were checked directly against Dunn–Radziwiłł v3. The
original Patterson paper was not independently read because the attempted
publisher and repository routes failed. The underlying theta theorem and
global cubic reciprocity therefore remain mathematical imports. This
audit does not validate the entire quasi-RH argument or establish a new
zero-free region.

The detailed derivations are:

- [Cusp construction, multipliers, and uniformity](../notes/THETA_CUSP_AND_UNIFORMITY_AUDIT_20261012.md).
- [Mellin normalization, continuation, and kernel bounds](../notes/THETA_MELLIN_AND_KERNEL_AUDIT_20261012.md).
- [Primary coefficient and automorphy comparison](../notes/THETA_PRIMARY_SOURCE_COMPARISON_20261012.md).

## Exact versions and correspondence

Both manuscript versions were read at repository commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`:

- [October 5 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
  SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
- [September 30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
  SHA-256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.

The pinned September 30 PDF was also fetched and hashed. Its hash is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`,
exactly the artifact hash recorded by the earlier audit. The TeX and PDF
are published at the same revision; no claim of a byte-identical PDF
rebuild is made. The [version and replay record](../numerics/theta_version_crosswalk_record_20261012.json)
stores the immutable URLs, hashes, sizes, and scope. All third-party
source files remain outside the repository.

The mathematical dictionary is `q_a=N(a)`, `mu=ell`, and `V=V_*`.
September's `c_F` is the fixed reduced denominator corresponding to
October's `c_0`; October's separate `c_F(h)` notation is a Fourier
scalar. The three conjugated cusp sequences are ordered
`(F_1,F_19,F_10)=(0,-,+)`. September's
`tau_(p,j)^-` equals October's `chi_p(-1)^j*gamma_j(p)`, whereas
`tau_(p,j)^+=gamma_j(p)`. These identifications were checked in the
formulas; the two papers' source texts are not asserted identical.

| Proof component | September 30 physical lines | October 5 physical lines | Comparison and scope |
| --- | --- | --- | --- |
| Imported theta and cusp coefficients | 1889–2001 | 1649–1720, 1761–1779, 3087–3145 | Same three matrices and coefficients after reversing and conjugating Fourier frequency |
| Fixed mask and finite Fourier expansion | 2002–2087 | 2905–3025 | Every fixed frequency is retained, including nonunits; zero-exponent local characters retain their zeros |
| Reduced cusp, multiplier, fixed residues | 2089–2223 | 3028–3218 | Same fixed modulus and three ramified cases; October compresses the nondegenerate representative choice |
| Active and inactive local transforms | 2225–2262 | 3220–3281 | Same exponent change, exceptional Ramanujan term, and inactive scalar |
| Mellin normalization and contour | 2280–2407 | 3284–3438 | Same angular phases, scalar, gamma quotient, and squared cusp-norm scale; contour reasoning expanded in the new note |
| Moving-row uniformity | 2185–2223, 2253–2262; statement 1829–1852 | 3439–3451; statement 1841–1853 | A fixed ray partition determines coefficient and additive-character choices; moving phases remain bounded exterior scalars |
| Transformed-kernel bounds | 2409–2434 | 3453–3478 | Same pole-free shifts and Mellin seminorms; compact support gives a concrete finite derivative order |

September's additional marked-prime phase formulas, annular separation
estimates, and global induction are not consequences of this comparison
and are not newly validated here.

## The two clarifications

October 5 chooses a reduced cusp fraction `a/c` and CRT solution
`delta'`, then writes cubic residue symbols of the resulting entries.
The text does not repeat September 30's instruction to avoid the finite
set of choices where such an entry is zero. That instruction is at
September lines 2122–2127.

For completeness, replace the cusp by
`a/c + lambda^2*M^2*z`, an allowed theta period, to arrange `a!=0`.
Then replace `delta'` by `delta'+M*c*t`. This preserves the required
CRT congruences and changes `b_g=(a*delta'-1)/c` to `b_g+a*M*t`.
Choosing `t` outside finitely many values avoids the zero entries used
in the three multiplier calculations. The changes preserve the fixed
residues, additive phase modulo `lambda^3*c_0`, and selected cusp.
The [cusp note](../notes/THETA_CUSP_AND_UNIFORMITY_AUDIT_20261012.md)
checks those claims. This is an explicit completion of a routine choice,
not a discovered need for a new arithmetic estimate.

October's Phragmén–Lindelöf paragraph also compresses an analytic step.
For each fixed twist, endpoint decay makes the differentiated theta
Mellin transform entire. Division by gamma factors gives a crude
exponential bound on a fixed strip; the direct and dual series give
polynomial bounds on its edges. Dividing by a sufficiently large power
of `B+s` and multiplying by `exp(epsilon*s^2)` permits the maximum
principle on expanding rectangles. Sending `epsilon` to zero yields
the required polynomial strip bound. After Mellin inversion, individual
kernel contours are shifted and their rapidly decaying values are then
summed. A conditionally convergent dual series is not interchanged with
the zero-line integral. The [Mellin note](../notes/THETA_MELLIN_AND_KERNEL_AUDIT_20261012.md)
provides the convergence majorants.

## Uniformity that survives the transformation

The fixed modulus is `M=lambda^12*L^4`, with `L` depending only on
the fixed ray data and excluded set. It is chosen before the moving
primes. For a residual squarefree row `k_0`, all its local exponents
are 1 and hence active. Writing
`r=k_0*product_(p in A_fix) p`, a fixed class of `k_0 mod M^2`
fixes the required class of `r`. Consequently the cusp coefficient
sequence, fixed additive character, and fixed denominator component
are independent of the moving row within that class.

The surviving moving-prime dependence is explicit: the local factors
`B_(p,j)`, the active denominator `c=c_0*r`, the bounded exterior scalar,
and the number of active-subset terms. In particular, the possibly large
`j=4` Ramanujan factor is not included in the bound for that scalar.
Its later cost is the reindexing already recorded in the first review.

The independently derived archimedean calculation gives
\[
C=-\frac{i}{81}\times\text{the stated bounded phase and Fourier factors},
\qquad
V_*^\sharp\!\left(\frac{N(\ell)X}{N(c)^2}\right).
\]
For decay exponent `A>0` and Euler derivative order `j`, a sufficient
input order is `J=ceil(4A)+j+4`. The kernel constant depends on those
orders and the fixed support interval, not the moving primes.
Continuation constants may depend on the entire fixed twist because
they establish an exact identity; they are not subsequently quoted as
uniform bounds. This distinction supplies the uniformity required by
the completed-family estimate.

## Finite verification and next decision

The unchanged earlier checker was replayed after the formula and
version comparison. All **69,881 exact assertions** passed, and its JSON
result agrees with the historical record. These include 4,860 cusp
constructions, 5,328 local reflection cases, and 24,300 additive CRT
checks. The suite also contains primitive-Poisson checks; the total is
not a count of new theta obligations. It does not evaluate the global
cubic multiplier or prove theta automorphy. Those distinctions and the
separate source-hash verification are in the
[replay record](../numerics/theta_version_crosswalk_record_20261012.json).

The next bounded source target is now the **full initial Poisson
reduction and its arithmetic conversion identities**: source
`lem:arithmetic`, Appendix A.1, and `prop:poisson-reduction` in Section 4.
That audit should carry the original Möbius family, diagonal and shared
column factors, masks, and smooth norms into the precise initial dual
ranges. It must verify that the fixed ray group and loss choices are
compatible with the canonical estimate, including short or empty
boundary ranges. The full quadratic-sieve theorem and the original
theta proofs remain imports rather than independently re-proved results.

There is no reason from this scoped audit to halt the selected source
chain, and no basis yet to promote its final zero-free conclusion. The
two completed audits narrow the remaining task to identifiable source
steps.
