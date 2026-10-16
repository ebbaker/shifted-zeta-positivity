.PHONY: pdf verify
pdf:
	latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/storage_depth.tex

verify:
	python3 numerics/replay.py verify
