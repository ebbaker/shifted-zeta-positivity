# Continuation after the first manuscript

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

The investigation is now assembled as working manuscript 0.1,
*Wilson lines on Loewner-generated contours: defect supersymmetry,
reflection, and endpoint positivity*. Start with the
[paper](../manuscript.pdf), [editable source](../manuscript.tex),
[build guide](../BUILD.md), and [dated drafts index](../drafts/README.md).
The paper is self contained and includes the relevant literature, the
arithmetic target, the free angular and auxiliary Gaussian background,
and the three calculations already in the notes. The earlier notes and
handoffs are preserved as dated research history.

This assembly does not add a new interacting calculation. The next research
step is still the [third continuation](CONTINUATION_20260919_SESSION3.md):
compute the complete first interaction-order response of the ordinary-time
reflected endpoint network. Begin at a positive bulge height; include the
endpoint-to-line gauge and H-derivative vertices, endpoint self-energy and
the relevant defect and reference-junction counterterms in one consistent
scheme. The computed coefficient `3/2 - 2 log 2` belongs only to the direct
Feynman-gauge Gaussian bulk exchange. Do not substitute it for the full
answer or assume the full height expansion is analytic at zero.

Before a substantial extension, an independent review should check the
physical charge conventions, the reference color sector and the endpoint
annihilator argument. No such independent review is claimed for version 0.1.
The first manuscript includes same-agent source and visual checks, alongside
the 268 finite diagnostics; that is a different level of verification.

The main unresolved distinction remains: the ordinary same-charge scalar
pairing vanishes, whereas the physical adjoint gives a positive free kernel
with different branch charges. A common bulk supercharge does not protect
that norm. Neither pairing realizes the full arithmetic transfer. The
manuscript's final section states the exact identities and all-interval
control that would be needed to reach the Weil positivity criterion.

Use `python3 validation/drafts.py check --replay` for the portable manuscript
and saved snapshot. Use `python3 validation/check_package.py check --replay`
in the live investigation for the wider research inventory and inherited
inputs. A hash record is not a proof certificate. Bump the manuscript version
and create a new snapshot after substantive changes; never rewrite the
dated version 0.1 archive.
