# Integrated manuscript snapshot — 13 September 2026

This is the 48-page manuscript integrating all investigation results through note 19, saved after compilation and visual review.

- [PDF](manuscript.pdf)
- [TeX entry point](manuscript.tex) and complete sources in sections/
- [References](references.tex)
- [Build record](BUILD_RECORD.json)
- [Stored-byte hashes](SNAPSHOT.json)

To rebuild, copy this snapshot to a separate working directory and run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
```

The rebuilt PDF is written under build/. All manuscript inputs are included here. No external numerical data or shared background file is required. PDF metadata may differ between compilations; the snapshot hashes identify the preserved bytes. Keep this dated snapshot unchanged when the live manuscript evolves.

The physical chiral-equation identification is conditional, the finite arithmetic matrix sign is unresolved, and the manuscript claims no all-support Weil positivity or RH proof.
