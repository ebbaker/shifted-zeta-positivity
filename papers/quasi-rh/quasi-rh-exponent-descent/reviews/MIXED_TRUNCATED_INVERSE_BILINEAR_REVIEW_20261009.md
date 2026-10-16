# Review of the truncated inverse bilinear removal

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex). Reasoning effort: inherited configuration, not
exposed; the exact serving variant is not inferred. Same-model internal
audit, not independent specialist validation or formal verification.

Reviewed [mixed note 22](../mixed_character_families/notes/22_TRUNCATED_INVERSE_BILINEAR_REMOVAL_20261009.md). Re-read printed pp. 56–59 of the
[30 September primary manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
in memory. The SHA-256 again matches
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
No source PDF or long extraction is saved. The deep source estimates,
their bin/presentation hypotheses, and the selected plain-fourth/slot
mass are imported assumptions; this review does not establish them.

**Assessment:** the exact decomposition, controlled-sector exponent,
complete cross-term removal, literal buffer arithmetic, and equivalence
at the stated target exponent are correct under those imported hypotheses.
No algebraic repair is required. The surviving large-cofactor theorem
remains unproved.

## Exact identities and physical coefficients

With B_Z=mu 1_(Nn<=Z) and R=mu-B_Z, the support of R*R*1 is strictly
above Z^2. On the boundary Nn=Z^2 it is still zero. Expanding gives
B_Z*B_Z*1=mu-2R+R*R*1, hence (7), including the unit ideal.
The original annulus has Nn<=CD=Z^2 and, eventually, Nn>=cD>Z;
thus its 2B_Z contribution is exactly zero.

The regrouping (8) is an exact finite rearrangement. Each product t l
uses the same original profile A0(Nt Nl/D), and multiplicativity of
the zero-extended character gives psi(t l)=psi(t)psi(l), also when
a factor is a nonunit. No division by a character value, physical-zero
deletion, squarefree restriction on t or l, or coprimality restriction
on the two factors inside c_Z is allowed or used.

The two factors of c_Z are individually squarefree but can share a prime.
In the short sector T<=Z, every divisor is below Z, so c_Z=mu*mu there,
with local values -2,1,0 at valuations 1,2,>=3. The full coefficients
c_Z beyond Z must retain both original cutoff conditions; they are
not multiplicative in general.

## Imported all-length profile estimate

The source hypotheses apply to the same native presentation for every
length in a fixed bounded nonnegative interval and to a uniformly smooth
untwisted profile family on a fixed annulus. Here the original profile
is unchanged, and x=r-log_U Nt lies in [3/5,73/100] throughout the
controlled sector. Thus its length variation is within source 8.2.
No cofactor-dependent character, puncture or coefficient sequence is
inserted into the plain response.

Source 8.1's reflected estimate and the explicit calculation on p. 58
give
|S(U^x)| <= U^(a-1/2+12e) U^((1/2-a-6e)x)
times the permitted height factor and additional small losses.
Squaring gives exactly d(1-x)+(24-12x)e in (4). This estimate keeps
the original deleted Euler factors and requires the retained nonprincipal
rows. Any bounded principal physical rows excluded by the detector need
their original separate treatment.

A pure norm twist is placed in the L-argument, while late-order tail
derivatives apply to the untwisted transform. At each cofactor length,
the same source cumulative T1/2 frequency allocation applies; there is
no newly assigned budget per cofactor. The source also requires
(1+T1)^AA<=U^(epsilon/10), with finite AA fixed before the external
tail order. Therefore “arbitrarily small additional loss” in (3)–(4)
must mean each requested loss for which these source conditions hold.
If a positive tau in T1=Z^tau has already been fixed, its height factor
cannot silently be absorbed into every smaller epsilon. The revised note
now explicitly states this cumulative allowance and quantifier-order
caveat after (4), and requires any fixed extra power cost to be added
to the removal exponent after (16). This clarification is resolved.

The selected fourth/slot mass in (3) remains a conditional imported
input with its original source allowance, whole-slot hypotheses and
witness/profile height budgets. The decomposition never changes the
original V or its plain S. Its new plain responses P have varying
lengths only. This audit does not manufacture a fourth estimate or
replace the operational slot certificate by a numerical slot sample.

## Normalization and controlled-sector exponent

The normalizer is precisely
D^(-1/2)P(D/Nt)=(Nt)^(-1/2)S(D/Nt).
Using the reflected bound, a term has absolute weight
U^[d(1-r)/2+(12-6r)e] (Nt)^[(d-1)/2+6e] |c_Z(t)|.
The divisor bound and ideal partial summation in (11), followed by
(Nt)^(6e)<=T^(6e), give (12) exactly:
d(1-r)+(1+d)alpha+(24-12r+12alpha)e.

For alpha=1/10 the unbuffered saving is
lambda_I=d(2r-1)-(1+d)/10. Its derivatives are
2r-1-1/10>0 with respect to d and 2d>0 with respect to r on the
closed comparison box. The minimum is therefore at d=9/25,r=7/10
and is exactly 1/125. The closed upper r endpoint causes no issue.

## Complete interaction and correlated buffer

Since M_L=M-M_I, the weighted identity preceding (14) is exact, with
the original positive V. Weighted Cauchy bounds all cross terms by
2 sqrt(F F_I)+F_I; no bound on F_L is needed for this removal.

The cross-term buffer must be averaged before maximizing the lengths.
Its value is
(12r+24-12r+12alpha)e/2=(12+6alpha)e=63e/5.
This verifies (15). The minimum unbuffered cross saving is 1/250.
At e<=1/1200000,
delta_e>=7979/2000000, and its reserve over 1/700 is
35853/14000000. The separate F_I term has greater saving:
its worst saving is 1/125-(84/5)e; at the maximal e the difference
from delta_e is 7993/2000000>0. The older unbuffered reserve over
1/540 is 29/13500. These values were recomputed with exact fractions.

The chosen e also has to satisfy the source's e0 and witness/height
budgets. The note correctly keeps its literal value visible rather than
absorbing it into every additional epsilon.

## Equivalent surviving target and gcd masks

The error in (16) is strictly smaller than the 1/700 target. Thus
F<=F_L+|F-F_L| and F_L<=F+|F-F_L| prove the claimed equivalence of
the target estimates in both directions, under the existing envelope
used to prove (16). No circular assumption of the new target occurs.

Expanding F_L gives (19) with precisely D^(-1), and the row kernel is
the Gram kernel of
psi_u(t)P_u(D/Nt) in the weighted row Hilbert space. Its positivity
is valid before contraction against c_Z(t)conjugate(c_Z(t')).
That fact does not make every pairwise term nonnegative.

If t=g a,t'=g b with g=(t,t'), then only (a,b)=1 is forced;
g can still meet a or b. The coefficients remain
c_Z(g a)conjugate(c_Z(g b)), the row factor is |psi_u(g)|^2,
and the plain lengths are D/(Ng Na),D/(Ng Nb).
The literal two-factor cuts inside each c_Z, the product lower cutoff
Nt>T, the original total annulus and every zero remain necessary.
These are not the squarefree inverse-pair gcd weights of notes 14–15.

The positivity of the original selected F supports this new alternative
reduction with unchanged selected weights. It does not transfer the old
near-gcd or ratio masks through the regrouping, and it does not authorize
enlarging the old selected signed R_near. The note states those limits
correctly. Source-all-length bounds are used only in the controlled
short sector; the surviving short plain quotients have no bound asserted
here.

## Validation limits

This review checked the identities directly and the numerical budgets
with exact rational arithmetic. I did not re-run the separate finite
checker in this audit. Its finite algebra is separate from the imported
analytic inputs, ideal asymptotics, native selected-bin realization and
the unproved large-cofactor correlation. No new mixed-moment theorem
is established.
