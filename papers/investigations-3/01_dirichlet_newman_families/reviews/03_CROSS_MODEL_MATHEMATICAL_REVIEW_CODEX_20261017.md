# Review of the Dirichlet Newman comparison and conductor bounds

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: **OpenAI gpt-6-astra (Codex), recorded reasoning effort max**.
**Review type: internal cross-model LLM review.** The principal arguments
were written with gpt-6.1-sol, and the initial contract with Claude Opus
5.5. Earlier reviews were available to this reviewer. This is not
independent specialist human review.

## Disposition

**No substantive mathematical defect was found in the current comparison
theorem or its two Dirichlet consequences.** The manuscript and its
supporting notes supply an applicable proof of

\[
\Lambda_\chi\le 27/100\quad(q\ge10^{12}),\qquad
0\le\Lambda_\chi=O((\log q)^{-4/7})\longrightarrow0,
\]

uniformly over primitive characters in the stated normalization. The
confinement hypothesis H12 is bypassed, rather than established for the
original character flow. The exact scalar certificate passed replay.
These conclusions are suitable for continued research use at the
**proved in manuscript and notes, internally reviewed** level; specialist
review and a full priority audit remain outstanding.

The revisions requested below concern the contradictory opening status,
one broken link, and the treatment of the current numerical benchmark.
There are also recommendations for making the proof package easier to
circulate and recording a closely related public discussion. None requires
withdrawing the two displayed results. The earlier zero-loss planning
tables retain their original unproved premises.

The review follows the [result summaries](../../../../result-summaries/README.md)
and [patterns to avoid](../../../../avoid/README.md), particularly
[the Dirichlet continuation](../../../../result-summaries/08_character_channels_ccm_and_detector.md),
[heat-flow results](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and [classification](../../../../avoid/01_restating_the_target.md),
[control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [current status reporting](../../../../avoid/19_status_files_that_lag_the_findings.md).
The target is a quantitative positive-time milestone, not a GRH-equivalent
criterion.

## Scope and source identity

The principal objects checked were [the manuscript](../manuscript/main.tex),
[round 2](../notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md),
and [round 3](../notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md).
The audit also checked the normalization and paired-zero calculation from
[round 1](../notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md),
the scalar program, all four numerical replays, the earlier reviews, and
the current guides. It does not re-audit the quasi-RH preprints behind
round 1's historical conditional baseline, or the analytic certificate
chain in the sibling investigation.

Repository HEAD at review: `238190ac9edd94f238aa2913af3c178e26909356`.
The following hashes identify the actual reviewed bytes; the
[replay record](../numerics/REVIEW_03_REPLAY_CODEX_20261017.json) contains
the complete checked manifest and execution results.

| Artifact | SHA-256 |
| --- | --- |
| Manuscript source | `a820f8103f9720fedce6ade79cf447354fddfdd1143ee58c6f09a8500411dce2` |
| Manuscript PDF | `73739071597d6b53a041492fe8b97cd9c7d53de3c28f0375224c79c37d9fc2ba` |
| Round 1 | `33a0652a114f87c316f2b6e61342e643bd735d08626e27f199aa7e4d6a29ce1a` |
| Round 2 | `fd4c176b48a5a6766e302190f7bebb14183a462ed67d2ca915b8dc972652302a` |
| Round 3 | `c1fdd827e3f1e344f1e4f8bcdd9435767602a24017982fe14a28a4953c245886` |
| Exact scalar program | `0b7d513728d6c20ae380bb9b3ea9bc01a8c8963be1d9efd5aab970a4535b4cf9` |
| Exact scalar record | `ff6e250a2340bdc88e00c6c2a9043257d50076c44231d7d0b7fd633de4030837` |

All entries in the existing manuscript build record match the files on
disk. This checks artifact identity; this review does not claim a new
PDF compilation or visual-layout audit.

## Mathematical assessment

### Normalization and the initial arithmetic floor

The Mellin substitution in the displayed theta kernel gives
\(H_{0,\chi}(z)=\xi_\chi((1+iz)/2)\), including the factor
\(4\alpha_\chi(\pi/q)^{\mathfrak a/2}\). The phase condition gives the
Hermitian functional equation and a real entire function, without
requiring an even function for a complex character. The compatible
conjugate-character phases give the stated reflection relation.

The sign and character in the manuscript's initial logarithmic-derivative
identity (source lines 261–267) are correct:

\[
-\Im\frac{H'_{0,\chi}}{H_{0,\chi}}(x+ip)
=\frac12\Re\frac{\xi_\chi'}{\xi_\chi}
\left(\frac{1+p+ix}{2}\right).
\]

This is reflection to the right half-plane for the same character.
The lower bound for the real part of the digamma function and
\(|L'/L(s,\chi)|\le-\zeta'/\zeta(\Re s)\) then give exactly the
stated floor. At height three, even parity gives the smaller input, so
one lower bound covers both parities and both real height directions.
The correction to the character orientation in round 1's separate open
Lemma A is present in round 2; that lemma is not used in the current
manuscript proof.

[Dobner, Theorems 1–3 and Section 2](https://arxiv.org/html/2005.05142v2)
was checked for the existence and nonnegativity of the constant and the
Hermitian Fourier strip theorem. Its rotated variable agrees with
\(s=(1+iz)/2\). Thus the lower bound used in the conductor limit applies
to complex as well as real primitive characters.

### The positive-time floor

Round 2, Section 2, supplies the regularization missing from the first
contract. Imaginary canonical compensators cancel in conjugate pairs;
their absolute summability follows from the bounded imaginary parts and
\(\sum|\rho|^{-2}<\infty\). A zero at the origin is included separately.
No divergent unregularized sum of real reciprocals is needed.

With \(U=u-iS\), \(d=p-1\), the estimates

\[
|u_x|\le S/d,\qquad |S_{xx}|\le2S/d^2,
\qquad S_t+2uS_x=-S_{xx}-2Su_x
\]

give the claimed Riccati comparison. The characteristic argument is
global: a uniformly zero-free anchor and Jensen's formula give real
drift \(O((1+|x|)\log(2+|x|))\) for the Dirichlet flow. The reciprocal
of this growth bound has divergent integral, excluding finite-time
escape in both directions. Fixed approximants have exponential type and
an even simpler bound. Onto characteristics justify uniformity over the
whole real line.

At \(p=3\), the solution is precisely
\(m_C(t)=Ce^{-t/2}/[1+2C(1-e^{-t/2})]\). It has a substantial loss;
the proof does not quietly reuse the initial constant at positive time.

### The compact comparison

The paired-zero algebra is correct, including the half weight for real
zeros and the subtraction of the moving zero's own conjugate pair.
The numerator

\[
D^2+(A+B-6r)D+(A-r)(B-r)
\]

is nonnegative for \(D\ge0\), \(0\le r\le A\), \(B\ge5A\).
It yields

\[
Q'\le-2-\frac{4Q}{p}S+\frac{8Q}{p^2-Q}.
\]

At \(p=3\), \(Q\le1\), this gives the manuscript's linear differential
inequality. The integrating factor is \(e^{-t}D_C(t)^{4/3}\), since
\(D_C'/D_C=m_C\). Both the factor \(4/3\) and the constant term \(-2\)
are needed and have been retained. The pair calculation agrees with
[Hakimoglu-Brown, Section 4](https://arxiv.org/html/2610.12803v1);
no other part of that preprint's conditional certificate is needed here.

The upward perturbation of both the initial height and the differential
equation gives a uniform initial time gap. Once confinement is available,
the first contact is attained in a compact set. Backward Hermite splitting
at a multiple nonreal zero supplies an earlier zero higher by order
\(\sqrt{v}\), contradicting contact with the smooth barrier. This handles
multiple zeros without a simplicity hypothesis. At the zero-height
endpoint, strip contraction from earlier times and Hurwitz give reality;
one need not differentiate a highest zero at the instant it becomes real.

### The sine tail removes the missing hypothesis

Round 3 addresses the actual obstacle in passing from finite products to
the original function. Polynomial truncations alone have no positive
global Poisson floor. For the proposed approximants, the two-region
estimate is valid: omitted true zeros cost
\(16(p+1)\sum_{|\rho|>R}|\rho|^{-2}=o(1)\) on \(|x|\le R/2\), while
outside this region deleting the central sine lattice costs at most
\(8p/(hR)+16p/R^2\). The strict input \(C_1<C\) absorbs the central
loss; the fixed lattice frequency supplies the exterior floor.

The strip import is appropriate. In
[Cardon, Definition 1.4 and Theorem 1.5](https://arxiv.org/html/1401.0237v2),
take \(\phi(z)=e^{-tz^2}\), \(\alpha^2=2t\), and the input quadratic
factor equal to zero. Each real genus-one approximant belongs to the
required class. The theorem gives the strip
\(\sqrt{\max(1-2t,0)}\). This use does not depend on the approximant
being the Fourier transform of an integrable kernel.

For fixed \(R\), the representation
\(e^{b_Rz}r_R(z)\sin(\kappa z)\) gives the stated heat asymptotic. The
imaginary Gaussian translation keeps the real part large and avoids
every finite rational pole. The estimate for the rational quotient
also covers negative degree and the unbounded Gaussian variable.
After integration its error is uniform in bounded time intervals and
the fixed zero strip. Rouché disks contain one zero each; reality forces
that zero to be real. The complement is zero-free. Hence confinement is
proved for each fixed approximant, including uniformly down to time zero.

The final limiting step has the necessary extra control. For every
fixed \(1<\sigma<2\), the canonical truncations have a common bound
\(\exp(A(1+|z|)^\sigma)\), and the added lattice tail is bounded by
\(e^{\kappa|z|}\). Gaussian domination therefore gives heat convergence
uniformly on spatial compact sets and bounded time intervals. The
real-Gaussian inverse, justified by the same domination and the angular
mean identity, excludes an identically zero limit. Hurwitz can then be
applied in each half-plane.

There is no need for a confinement radius uniform in \(R\). For strict
\(J_C(T)>1/2\), choose \(C_1<C\) first and then a sufficiently large
\(R\). For equality with \(T<1/2\), use slightly later times and heat
continuity; \(T=1/2\) is already covered by strip contraction. These
quantifiers close the earlier H12 gap.

### Explicit and asymptotic consequences

The scalar program's decisions all use rational arithmetic. Its logarithm
series remainder, alternating exponential bounds, cube-root bisection,
and outward decimal conversion have the correct directions. The
von Mangoldt tail is legitimately bounded by
\((\log1000+1)/1000\), and the harmonic-sum upper bound for Euler's
constant is also in the required direction. Together they prove

\[
C_{q,\mathfrak a}(3)>1221/200>6,
\quad
0.502464325582617834\le J_6(27/100)
\le0.502464325582617835.
\]

The positive margin is enough for the strict version of the approximation
argument. No conductor sweep or numerical approximation to a Dirichlet
zero is needed for this implication.

The elementary bound for \(J_C\) also gives exactly the displayed
\(B(C)\). Its leading power is \(C^{-4/7}\); since
\(C_{q,\mathfrak a}(3)=\tfrac14\log q+O(1)\) uniformly in parity, the
claimed exponent follows. Dobner's nonnegativity gives convergence to
zero. This limit concerns different characters as conductor grows and
does not establish zero-time GRH for any fixed character.

## Numerical replay

Question: do the four existing programs reproduce their recorded
arithmetic on their original domains? The workloads, grids, cutoffs, and
precision were unchanged; each program was run once with
`python3 -I -B`, with output kept outside the repository for comparison.
The stopping condition was completion of these four fixed workloads,
without extending a sweep. Runtime: Python 3.10.0, macOS 27.0.1, arm64.

| Program | Replay result | Evidential scope |
| --- | --- | --- |
| Character normalization | Numerically consistent; 256 scalar leaves differ from the stored output. Worst transform discrepancy is \(3.6648607808\times10^{-9}\); largest quoted LMFDB zero discrepancy is \(2.87769807983\times10^{-13}\) | Floating normalization diagnostic |
| Family benchmark | Byte-identical | Historical planning arithmetic |
| Comparison-loss diagnostic | Byte-identical | Historical planning arithmetic with its stated premises |
| Exact scalar certificate | Byte-identical; every assertion passes | Finite rational inequalities used in the current theorem |

The normalization replay hash is
`6be33b5e7947673715ddacbe14a2fb9e57620f20ab1f35109381f68810a7ed9a`,
the same local replay already reported in review 01. Its floating
differences do not invalidate the quoted normalization accuracy.
Reproducibility of the other programs does not promote the planning
tables to bounds. The exact certificate's historical conditional wording
is accurately explained by the current numerical README: the analytic
consumer is supplied by round 3.

## Controls and literature

The periodic control in round 2 remains a useful test of the distinction
between the comparison and confinement. It also has a non-even version:

\[
F(z)=e^{bz}(\cos z-\cosh(9/10)),\qquad
F_t(z)=e^{bz-b^2t}
\left[e^t\cos(z-2bt)-\cosh(9/10)\right],
\]

for any nonzero real \(b\). Its initial zeros lie at heights
\(\pm9/10\); the real exponential changes only the horizontal drift.
At \(T=27/100\), nonreal zeros persist because

\[
e^T<\frac{100}{73}<\frac{281}{200}<\cosh(9/10).
\]

The actual height-three floor is
\(\tfrac12[\tanh(21/20)+\tanh(39/20)]<1\).
For any admissible floor \(C\le1\),
\(J_C(T)\le T(1+T)^2=435483/10^6<1/2\).
Thus the theorem rejects the false 0.27 conclusion even on a non-even
control satisfying its generic strip and heat premises. The same example
prevents inferring H12 from those premises alone.

The Euler-factor, weighted-square, reflected, smooth, and
primitive-compatible controls in the repository do not acquire the
primitive-character completion and coefficient hypotheses used to prove
the conductor-dependent floor. Applying the general theorem to them
would require checking its initial strip and their actual global floor.
The review makes no blanket claim that these controls fail the generic
comparison or that it supplies a zero-time positivity mechanism.

The Ki–Kim–Lee correction is supported by the original article's
[Section 6, Example 1, pp. 303–304, in the available transcription](https://paperzz.com/doc/6928362/on-the-de-bruijn%E2%80%93newman-constant).
For real primitive characters their extension includes a strict
improvement on the strip bound. Their complex-character example uses
coefficients \(\Re(\omega\chi(n))\), giving a self-dual combination,
not the individual non-even family used here. Keep this distinction and
the present absence of a priority claim.

A bounded search also found the directly relevant
[MathOverflow question on the conductor limit](https://mathoverflow.net/questions/515667/do-de-bruijn-newman-constants-of-dirichlet-l-functions-tend-to-0-as-the-cond),
displayed as posted October 1 and edited October 2, accessed for this
review on 17 October 2026. It proposes the stronger rate
\(\log\log q/\log q\), but explicitly leaves positive-time counting
and confinement unwritten. This is a provenance lead, not a proved bound
or validation of the present proof. No identification of its author with
the repository author is assumed.

## Corrections and recommendations

**1. Replace the contradictory current status in the investigation
README.** Lines 6–30 still describe a pending Codex audit, open inputs
for the original Target A, and a gate awaiting that audit. The following
paragraph announces the completed comparison, and review 01 already
exists. Make the opening paragraph explicitly historical, and lead with
the current result and its review level. At line 9, replace the nonexistent
`notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md`
with the existing `notes/round-1/` path. This was the only broken local
link found in the seven current guides checked.

**2. Update the numerical benchmark for continuation.** The sibling
[round-two continuation in investigation 03](../../03_effective_outer_remainders/notes/round-2/README.md)
now records \(\Lambda_\chi\le43/200=0.215\) for the same primitive
\(q\ge10^{12}\) range, using a stronger uniform positive-time floor and
a restarted version of this approximation mechanism. Its stated status
is proved in-note from named imports, with Arb/exact certificates and
internal same-model checks; see its
[review 02](../../03_effective_outer_remainders/reviews/02_UNIFORM_FLOOR_AND_RESTARTED_COMPARISON_REVIEW_CODEX_20261017.md).
That separate proof chain was not re-audited here. Nevertheless the
current proposal in this folder's review 02 to seek an improvement over
0.27 needs this context. Retain 0.27 as the simpler certified application
of the general theorem, and compare new finite bounds with the sibling
0.215 claim at its stated review level. The general comparison and the
conductor-aspect exponent remain distinct contributions.

**3. Make the proof dependencies portable before external circulation.**
The repository package contains the needed arguments, but the manuscript
delegates complete-characteristic estimates and parts of the compact
comparison to Markdown notes through relative links. Include those notes
in a versioned supplementary package, or move the necessary lemmas into
an appendix. In particular, state the compact comparison once with its
growth, strip, nonzeroness, and confinement hypotheses before invoking it
for the rational-sine approximants. This is an exposition recommendation,
not a newly missing analytic premise.

**4. Add the public conductor-limit discussion to the provenance ledger.**
Record its incomplete status and the different rate, alongside the
Ki–Kim–Lee correction. It does not justify a priority claim, and its
unproved uniform-counting step should not be imported as a theorem.

The useful next review target is the stronger sibling floor and its
intermediate-strip restart. Further research in this folder should target
a sharper general comparison or a better conductor exponent. A separate
proof of H12 for the original non-even flow may be useful, but is no
longer an acceptance condition for the two results reviewed here.
