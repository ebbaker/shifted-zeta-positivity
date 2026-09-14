TEXBUILD ?= /tmp/storage-depth-tex
.PHONY: all
all:
	mkdir -p "$(TEXBUILD)"
	cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$(TEXBUILD)" storage_depth.tex
	cp "$(TEXBUILD)/storage_depth.pdf" manuscript/storage_depth.pdf
