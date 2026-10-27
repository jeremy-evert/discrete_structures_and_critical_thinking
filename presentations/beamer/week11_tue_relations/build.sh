#!/usr/bin/env bash
# Builds slides (no notes) and a separate speaker-notes PDF from the same .tex.
set -euo pipefail
cd "$(dirname "$0")"
n=week11_tue_relations
pdflatex -interaction=nonstopmode "$n.tex" >/dev/null; pdflatex -interaction=nonstopmode "$n.tex" >/dev/null
sed 's/^\\begin{document}/\\setbeameroption{show only notes}\\setbeamertemplate{note page}{\\insertslideintonotes{0.22}\\par\\vspace{6pt}{\\fontsize{15}{19}\\selectfont\\insertnote}}\n\\begin{document}/' "$n.tex" > "${n}_notes.tex"
pdflatex -interaction=nonstopmode "${n}_notes.tex" >/dev/null; pdflatex -interaction=nonstopmode "${n}_notes.tex" >/dev/null
rm -f "${n}_notes.tex" *.aux *.log *.nav *.out *.snm *.toc *.vrb
ls -1 *.pdf
