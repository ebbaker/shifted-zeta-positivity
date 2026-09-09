# Verification protocol — items C1 and C2

**For:** *Archimedean first-slab positivity for shifted zeta canonical systems*, preprint v1.0 (5 Sept 2026)
**Covers:** C1 (normalization chain against Suzuki) and C2 (originality search)
**Estimated time:** C1 ≈ 3 hours, C2 ≈ 2–3 hours, both spread over as many sittings as you like
**Prepared:** 6 September 2026. Written for the author; usable verbatim by any checker ("your paper" = the preprint).

---

## 0. What this protocol is for, and what it cannot do

The manuscript has been through two adversarial referee rounds, a clean-room
reimplementation of the certificate, and two independent numerical
recomputations. That apparatus is strong against **implementation error** —
a mistyped constant, a quadrature bug, a wrong pivot. It is structurally blind
to **premise error**, because every round shares the premises.

There are exactly two premises it cannot test:

| | Item | Failure mode | Consequence if wrong |
|---|---|---|---|
| **C1** | The normalization chain against Suzuki [1] | Both checks were automated readings of the PDF. Two LLM extractions agreeing is not independence — they share failure modes. | A factor or shift moves the `log 2` threshold. Theorem A becomes a true statement about the wrong operator. |
| **C2** | Originality of Prop. 4.2 and the energy identity | A model's sense of "this is novel" is close to worthless. | The result is correct but known. Costs credibility, not correctness. |

Note what C1's failure mode is *not*. If the normalization is wrong, the
certificate is still a valid certificate, the Arb arithmetic is still sound,
and Theorem B is still true of the form it actually certifies. What breaks is
the claim that this form is the first slab of **Suzuki's** system, and with it
every sentence in §1.1, §2 and §9.3 that gives the result its significance.
That is why this is the highest-value hour available.

### The independence rule

**Do not let this document, the preprint, or any model tell you what Suzuki's
paper says.** Everything below is phrased as *"your paper claims X — go find
out what [1] actually says."* Where a step asks you to read [1], write down
what you find **before** looking at the corresponding claim in the preprint.
If you read the claim first, you will find it, because that is what reading
works like. The whole value of this exercise is that it is the one check in
the project performed by a mind that has not already been shown the answer.

Keep a single file — `verification/first-slab/C1_human_check_<date>.md` —
with one entry per item: what you looked at, what you found, verdict
(`confirms` / `contradicts` / `cannot tell`). "Cannot tell" is a real and
useful verdict; record it rather than resolving it by inference.

---

## Part 1 — What you can settle without opening Suzuki (≈ 1 hour)

Most of the normalization chain is not actually a convention question. It
follows from `ξ = Γ_∞ · ζ` and nothing else. Do this part first: it is faster,
it needs no external source, and it will tell you which of the remaining
items are genuinely at risk.

### 1.1 The master factorization

From the definitions printed in your own Appendix A, with `s = ½ − iz`:

```
Θ_ω(z) = ξ(s−ω)/ξ(s+ω)
       = [Γ_∞(s−ω)/Γ_∞(s+ω)] · [ζ(s−ω)/ζ(s+ω)]
```

The first bracket is `K_ω(p)` at `s = p + ½` — your eq. (3.3). The second is
the Dirichlet series `Σ c_ω(n) n^{−s}` — your eq. (2.1).

**Do this:** derive the display above from scratch on paper. Then confirm,
independently, that

```
Σ_{n≥1} c_ω(n) n^{−w} = ζ(w−ω)/ζ(w+ω),   c_ω(n) = n^ω Σ_{d|n} μ(d) d^{−2ω}
```

by Euler product or Dirichlet convolution. This is a five-line computation.

**What it buys you.** If both check out, then the *split* of `Θ_ω` into a
gamma factor and an arithmetic factor is forced, not conventional. The
definition of `Γ_∞`, the coefficients `c_ω(n)`, and the identification of
`K_ω` as the archimedean factor of `Θ_ω` then follow from one unambiguous
fact rather than from Suzuki on trust. What this does *not* settle is that
Suzuki's `g_ω` is the function whose Mellin transform is that gamma ratio,
or how `g_ω` assembles into `h_ω` — those are constructions, not
consequences, and they are exactly where Part 2 concentrates.

**Useful precision while you do this:** a *constant* multiplicative
discrepancy in `Γ_∞` cancels in the ratio `Γ_∞(s−ω)/Γ_∞(s+ω)` and is harmless.
An **s-dependent** one does not — `π^{−s/2}` versus `π^{−s}`, or `Γ(s/2)`
versus `Γ(s)`, or a missing `s(s−1)`. So when you check the definition, check
the shape, and don't waste time on the leading ½.

### 1.2 Internal checks that look like verification but are not

Two things already in the record will *not* catch a normalization error, and
it is worth knowing that before you feel reassured by them:

- The Laplace transform of the explicit impulse (3.6) against `K_ω` (3.3),
  agreeing to `1.5e−17`. This checks (3.6) against (3.3). If (3.3) is the
  wrong transfer function, both are wrong together and the agreement is
  perfect.
- The clean-room audit. It reimplements the mathematics *as stated in the
  manuscript*. It never opens Suzuki.

Neither is a criticism of those checks — they do their job. They just do a
different job than this one.

### 1.3 Record before proceeding

Write down, in your own words and without looking at §2 of the preprint, what
you now believe about: `Γ_∞`, `c_ω(n)`, `K_ω(p)`, and the domain on which the
Mellin identity holds. Then compare to the preprint. Any mismatch here is
found *before* you have been anchored by [1].

---

## Part 2 — The four items that genuinely need Suzuki's PDF (≈ 90 minutes)

After Part 1, the surface that actually depends on Suzuki's conventions is
small. It is these four. Each is a place where a different-but-reasonable
convention would change the geometry of the window and therefore the position
of the first prime layer.

For each: **open [1], find the displayed equation, transcribe it verbatim into
your notes, then and only then compare.**

### N1 — The support of `g_ω`

- **Your paper claims:** Suzuki constructs an explicit archimedean function
  `g_ω` supported in `(0,1)`.
- **Where to look:** [1, §2], around eq. (2.3); the construction is in §3.1.
- **Why it matters:** the support of `g_ω` is what makes
  `κ_ω(t) = e^{−t/2} g_ω(e^{−t}) 1_{t>0}` causal. If the support were `(0,c)`
  for some `c ≠ 1`, every layer offset shifts and the threshold is no longer
  `log 2`.
- **Transcribe:** the exact interval, and whether it is open/closed.

### N2 — The form of the arithmetic kernel `h_ω`

- **Your paper claims:** [1, eq. (2.3)] reads
  `h_ω(x) = (1/x) Σ_{n≤x} c_ω(n) g_ω(n/x)` for `x > 1`, with `h_ω = 0` on `(0,1)`.
- **Where to look:** [1, eq. (2.3)].
- **Why it matters:** this is *the* load-bearing convention. The prefactor
  (`1/x` vs `1/√x`), the argument (`g_ω(n/x)` vs `g_ω(x/n)`), and the
  summation range (`n ≤ x`) each independently determine where the `n = 2`
  layer lands. This single equation is the origin of `log 2`.
- **Transcribe:** the whole display, character by character, including the
  range of validity.

### N3 — The Hankel operator

- **Your paper claims:** [1, eq. (2.5)] is `(𝖧_ω f)(x) = ∫_0^∞ h_ω(xy) f(y) dy`.
- **Where to look:** [1, eq. (2.5)].
- **Why it matters:** `h_ω(xy)` is multiplicative and becomes `k_ω(x+y)`
  under `x → e^x`. A kernel `h_ω(x+y)`, or a measure `dy/y` instead of `dy`,
  would change the coordinate change and the `L²` space.
- **Transcribe:** the kernel argument and the measure.

### N4 — The compression window

- **Your paper claims:** [1, eq. (2.6)] defines
  `𝖧_{ω,a} = P_a 𝖧_ω P_a` on `L²((0,a), dx)`, and — this part is *your*
  inference, not a quotation — that since `h_ω(xy) = 0` for `xy < 1`, the
  compression effectively acts on `(1/a, a)`, which in logarithmic coordinates
  is the centered interval of total length `L = 2 log a`.
- **Where to look:** [1, eqs. (2.5)–(2.6)].
- **Why it matters:** this is the step that produces the factor 2 in
  `L = 2 log a`. It is the one item in this list that your manuscript
  *derives* rather than cites, so it needs checking as mathematics, not just
  as a quotation. Confirm the projection `P_a` is onto `(0,a)` and not onto
  `(1,a)` or `(a,∞)`, and then redo the "effectively `(1/a,a)`" step yourself.
- **Transcribe:** the definition of `P_a`, then your own re-derivation.

---

## Part 3 — Re-derive the threshold blind (≈ 30 minutes)

This is the payoff step and the one that would actually catch a compound
error. Having transcribed N1–N4, and *without rereading §2.1 of the preprint*:

1. Write `k_ω(t) = e^{t/2} h_ω(e^t)` and substitute your transcribed N2.
   Derive the layer formula. You should get a sum over `n` of delayed copies
   of a single impulse, with delays `log n` and weights `c_ω(n)/√n`.
2. Write down the sum-coordinate range. For the centered interval
   `I_L = (−L/2, L/2)` and a kernel evaluated at `x + y`, that range is
   `(−L, L)`.
3. Ask: for which `L` does the `n = 2` term contribute a set of positive
   measure to the quadratic form? Your answer should be a threshold, and you
   should be able to say why the boundary case is measure-zero rather than
   merely small.
4. Separately, from N4, express `L` in terms of Suzuki's `a`.

**Then** compare with (2.5), the sentence following it, and §2.2. If your
threshold is `log 2` and your correspondence is `L = 2 log a`, C1 is
confirmed and you can close it. If either differs, stop and do not touch
anything else in the project until it is resolved — everything downstream
inherits it.

A useful sanity anchor once you're done: your §5.3 cross-check against Zhu
[5] says the conventions relate by `L = 2 L_Z`, so the classical prime-free
cutoff `2L_Z ≤ log 2` should land on your `L ≤ log 2`. Two independent
conventions agreeing on the same threshold is meaningful corroboration —
but only *after* you have derived yours, not as a substitute for deriving it.

---

## Part 4 — The three citation checks (≈ 20 minutes, do while you have the PDF open)

These are the C3 items and they cost almost nothing once [1] is open. They
carry the significance claims rather than the mathematics, so an error here
weakens the framing rather than the theorem.

| | Your paper's claim | Check |
|---|---|---|
| **P1** | [1, Prop. 1.2]: for `ω₀ > 0`, `ζ(s) ≠ 0` for `Re s > ½+ω₀` ⟺ `Θ_ω` meromorphic inner for **every** `ω > ω₀` | The quantifier. "Every `ω > ω₀`" versus "some `ω`" is the whole content of §1.1's rewrite. |
| **P2** | [1, Thm. 2.2] innerness ⟺ Hankel mapping property; [1, Lemma 4.1] innerness ⟹ isometry on `L²((0,∞),dx)` | That both are stated as your §1.1 uses them, and on which space. |
| **P3** | [1, Lemma 4.4]: for `ω > ½` and every `a > 1`, `‖𝖧_{ω,a}‖ < 1`, via the support Lemma 4.3 | The hypotheses. §9.3 rests entirely on this, and it was rewritten once already when the earlier "unreproduced Paley–Wiener argument" reading turned out to be wrong. |

---

## Part 5 — C2: the originality search (≈ 2–3 hours)

Two objects need searching. Be precise about what you are searching *for*:
not "has anyone worked on Weil positivity" (thousands have) but "has this
specific identity appeared".

### Target A — the off-center kernel identity (Prop. 4.2)

```
a_ω(p) − a_0(p) = ∫_0^∞ e^{−pt} · 2(cosh(ωt) − 1) R(t) dt
R(t) = e^{t/2} − e^{−5t/2}/(1 − e^{−2t})
```
equivalently the kernel `c_ω(x,y) = (cosh(ω|x−y|) − 1) R(|x−y|)`.

The distinctive, searchable features are: the profile `R`; the fact that the
difference of two log-derivatives of completed-gamma factors at symmetrically
shifted points has **no diagonal singularity** (the `−1/(2t)` in `R` is killed
by the `O(t²)` of `cosh(ωt) − 1`); and the cancellation of the pole at
`p = ½ − ω`.

### Target B — the shift-radial energy identity (Theorem C)

```
I − V*_ω V_ω = 2 ∫_0^ω V*_s Q_s V_s ds
```

**The real risk here is not number theory.** This is a dissipation/storage
identity: the derivative of a contraction defect with respect to a parameter,
expressed as an accumulated positive quadratic form. That is the operator
analogue of a Lyapunov or Riccati differential equation, and structurally it
is close to standard material in dissipative-systems and passivity theory
(Kalman–Yakubovich–Popov, Kreĭn–Melik-Adamyan, Redheffer star-product
literature). The likely finding is not "someone did this for zeta" but "this
is a known identity in systems theory wearing different clothes." That would
not diminish the result — your §12.3 already gestures at the passive-network
framing — but it changes what you should claim is new, and it is far better
to find it yourself than to have it pointed out.

### Where to search

1. **arXiv full-text search** (`arxiv.org` → Full-text search, not just
   title/abstract) for the distinctive strings: `"cosh"` together with
   `"screw function"`; `"shifted scattering"`; `"off-center"` with `"Weil"`;
   `"storage"` with `"Hankel"` and `"zeta"`.
2. **The neighbourhood you already cite**, read for these two objects
   specifically rather than for general relevance: Suzuki [2] (2206.03682)
   and [3] (2606.09096), Connes–Consani [4], Zhu [5], Kim et al. [12],
   Groskin [13], Burnol [6], Lagarias [7]. Note [3] is Suzuki's own
   *Weil's quadratic form via the screw function* — that is the single most
   likely place for Target A to already exist.
3. **zbMATH Open** (free, no subscription needed) and Google Scholar
   forward-citation search on [1] and on Connes–Consani. Anything citing [1]
   is by definition in your neighbourhood, and the list is short enough to
   read titles exhaustively.
4. **Systems-theory side for Target B:** search on "dissipation inequality
   Volterra operator", "storage function contraction defect",
   "Riccati operator differential equation defect".
5. **Ask.** The MathOverflow question in the appendix is the cheapest
   high-quality answer available for Target A. And one email to Suzuki
   settles Target A, Target B and all of C1/P1–P3 at once, which is worth
   weighing against the three hours above.

### Recording

For each target, record: searches run (exact query strings), what you found,
and a one-line verdict — `no prior art found` / `prior art: <citation>` /
`related but distinct: <citation>`. Then update the preprint's §13(c) to say
the search was performed, by whom, and when. An originality search that
happened but isn't recorded is worth nothing to a reader.

---

## Appendix — MathOverflow question, draft

Post under tags: `reference-request`, `nt.number-theory`,
`special-functions`, `ca.classical-analysis-and-odes`.

Two notes before posting. First, MO expects you to have searched already —
do Part 5 steps 1–3 first, so the "what I've checked" paragraph is true.
Second, do not mention RH, the preprint's program, or language-model
assistance in the question body. The question is a reference request about a
gamma-function identity and should stand or fall as one; the preprint link
carries the disclosure for anyone who follows it.

---

**Title:**
Is this closed-form difference of shifted log-derivatives of the completed gamma factor known?

**Body:**

Let

$$\Gamma_\infty(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)$$

be the archimedean factor of the completed Riemann zeta function, so that
$\xi = \Gamma_\infty \zeta$. For $\omega \ge 0$ put
$\ell(p) = \log \Gamma_\infty(\tfrac12 + p)$ and

$$a_\omega(p) \;=\; \ell'(p-\omega) + \ell'(p+\omega),$$

which is the logarithmic shift-derivative of the ratio
$K_\omega(p) = \Gamma_\infty(\tfrac12+p-\omega)/\Gamma_\infty(\tfrac12+p+\omega)$,
in the sense that $\partial_\omega K_\omega = -a_\omega K_\omega$.

Using the integral representation
$\psi(z) = -\gamma + \int_0^\infty \frac{e^{-u} - e^{-zu}}{1-e^{-u}}\,du$
and forming the difference before separating the individually divergent
summands, one obtains, for $\operatorname{Re} p$ large,

$$a_\omega(p) - a_0(p) \;=\; \int_0^\infty e^{-pt}\,2\bigl(\cosh(\omega t) - 1\bigr) R(t)\,dt,
\qquad R(t) = e^{t/2} - \frac{e^{-5t/2}}{1-e^{-2t}}.$$

What makes this more than bookkeeping is that the resulting convolution
kernel is **bounded**: $R(t) = -\tfrac{1}{2t} + O(1)$ as $t \downarrow 0$,
but $\cosh(\omega t) - 1 = O(t^2)$, so the product is $O(t)$ and the diagonal
singularity cancels. So the associated convolution kernel
$(\cosh(\omega|x-y|)-1)R(|x-y|)$ is $O(|x-y|)$ at the diagonal, and the
symmetric shift of this gamma-type multiplier acts as a bounded — in fact
Hilbert–Schmidt — perturbation of the centre, uniformly for
$0 \le \omega \le \tfrac12$.

**Questions.**

1. Does this identity, or the profile $R$, appear anywhere in the literature
   on the archimedean Weil form, completed-gamma canonical systems, or screw
   functions?

2. Is there a general principle behind the cancellation — some class of
   multipliers for which a symmetric shift is a bounded perturbation of the
   centre — or is this particular to $\Gamma_\infty$?

I have checked Suzuki (arXiv:1204.1827, arXiv:2206.03682, arXiv:2606.09096),
Connes–Consani (arXiv:2006.13771), Burnol (arXiv:math/0509619) and Lagarias
(*Acta Arith.* 89 (1999)) without finding it, but this is not my area and I
would not necessarily recognise it in a different notation.

*Context, in case it is useful: the identity is used in a preprint of mine
on positivity for a family of shifted canonical systems
[link to Zenodo version DOI]. The question here is only whether the identity
itself is known.*

---

## Summary checklist

- [ ] **1.1** Derive `Θ_ω = (gamma ratio) × (Dirichlet series)` from `ξ = Γ_∞ ζ`
- [ ] **1.1** Verify `Σ c_ω(n) n^{−w} = ζ(w−ω)/ζ(w+ω)` independently
- [ ] **1.3** Record beliefs before opening the preprint's §2
- [ ] **N1** Support of `g_ω` — transcribe from [1]
- [ ] **N2** Form of `h_ω` — transcribe [1, eq. (2.3)] verbatim
- [ ] **N3** Hankel kernel and measure — transcribe [1, eq. (2.5)]
- [ ] **N4** Compression window — transcribe [1, eq. (2.6)], then re-derive `L = 2 log a`
- [ ] **Part 3** Re-derive the layer formula and the threshold blind
- [ ] **Part 3** Compare against §2.1–2.2; resolve any mismatch before anything else
- [ ] **P1–P3** Confirm the three [1] citations
- [ ] **C2-A** Search for the off-center kernel identity
- [ ] **C2-B** Search for the energy identity, including the systems-theory literature
- [ ] Post the MathOverflow question
- [ ] Update §13 and `verification/first-slab/` with dated results
