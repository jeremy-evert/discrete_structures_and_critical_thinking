#!/usr/bin/env bash
# Builds the slides PDF. (No speaker notes: Jeremy does not use them.)
set -euo pipefail
cd "$(dirname "$0")"
n=week13_tue_boolean_binary
pdflatex -interaction=nonstopmode "$n.tex" >/dev/null; pdflatex -interaction=nonstopmode "$n.tex" >/dev/null
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb
ls -1 "$n.pdf"
