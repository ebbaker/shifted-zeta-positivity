PYTHON ?= python3
LATEXMK ?= latexmk
RUN_DIR ?= /tmp/topological-susy-bulk-replay

.PHONY: pdf numerics verify

pdf:
	mkdir -p validation/build
	LC_ALL=C LANG=C $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error -outdir=validation/build manuscript.tex

numerics:
	$(PYTHON) numerics/replay.py --output-dir "$(RUN_DIR)"

verify:
	$(PYTHON) validation/check_package.py
