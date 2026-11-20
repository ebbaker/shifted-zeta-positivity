# AGC-JH-E05 return r3 — assessment of the physical-time slab

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded reviewer dispatch **gpt-6.2-sol /
ultra**. Serving metadata are unavailable. The separate internal
review shares the recorded dispatch and mathematical inputs of the E08
implementers. [Frozen assessment request](AGC_JH_E05_REQUEST_R3_20261119.md),
[assessment](../../reviews/04_AGC_JH_SLAB_ASSESSMENT_20261119.md).

**Accepted within scope.** The fixed degree-24 chart at center 36 and
radius 9 is certified throughout \(0\le t\le10^{-4}\). The signed
correction is enclosed by \([-4.958280826,-4.956734690]\,10^{-8}\).
The matched direct mean-value calculation gives the narrower enclosure
\([-4.957996104,-4.957019318]\,10^{-8}\), contained in the signed
one. Both intervals are outward rounded. The paid target squared
half-gap exceeds \(47.43458098488\). The unsigned allowance
contains zero correction. The window and endpoint enclosures
support a finite canonical head-error measurement. The correction
increases from the left endpoint to the right endpoint by
\([4.0556183,4.0558878]\,10^{-12}\), using the saved E07 left endpoint.
Monotonicity inside the interval and weighted forcing remain open.
[Primary enclosure](../../numerics/06_AGC_JH_E08_SLAB_CERTIFICATE_20261119.json).

The audit traced the normalized heat coefficients, true Volterra
head, complex-time Gram and Schur estimates, complete joint tails,
common annulus and root tubes, signed residue orientation and
center payment, and the exact direct displacement formula. At a
target double the algebraic control retains a negative correction
but fails the separated-root, nonzero-slope and positive absolute-gap
premises. The review found no blocking issue.

One replay to a temporary destination accepted at \(K=10\), 768 bits,
144 source terms, 192 head terms and 512 sectors per boundary
circle. CPython 3.10.0, python-flint 0.9.0, FLINT 3.6.0, one thread
and 9.806 seconds were recorded. Every invariant matched the primary
record. An exact-rational check on the serialized endpoints
reconstructed the log allowance, sign and direct arithmetic, both
time-variation intervals and E07 compatibility.

| Reviewed or replayed item | SHA-256 |
| --- | --- |
| E05 r3 request | `4809e39d4f333463cfd2c07638a7bad42fd6bd721c535d484e46b1018d85e462` |
| E08 r1 request | `fa8b897bb986e663b6055e11ae5aa02d6afc7c2ccf54825b9b84b9b47b201e4f` |
| E08 primary certificate | `2197c811918435dc3ee8787a4c9f03b4f03aab67efddecff650dba58cec5758d` |
| E05 temporary E08 replay | `01f885642f5ef234cf4db3927e1b4cef1821948cdb0188f605e070f8ab05388e` |
| E08 driver | `2a2fa13c7c694f4e8aedee2bcba325850e1c72e3cdb5f2e80515517494fccf96` |
| E08 chart | `21ac715192bc565d57c658f372a32952b979d084ace6a7fd6c61f8a1e84619d9` |
| E08 head | `aeecc5fc3dc801c8a651b803b73eb12548e60cddb6654bd997ad4329d7b9bf31` |
| E08 source | `776b13f8cf71de6e9eecfe2d07cb8b9653374aaac40ff925f210a36ecb4305ef` |
| E07 anchor | `ff76aeb4ae3c08ce62d9e4d5c92ef06e11ee91b99c1da5c532a8d215b86b8956` |
| HDC count | `966540b5221b7b5f6cd4d73672728bee1fc26045efdb69c38bde4e9a813239dc` |
