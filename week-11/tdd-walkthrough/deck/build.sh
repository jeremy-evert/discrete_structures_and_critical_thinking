#!/usr/bin/env bash
# Builds slides (no notes) and a separate speaker-notes PDF from the same .tex.
set -euo pipefail
cd "$(dirname "$0")"
n=tdd_walkthrough
[ -d prompts_txt ] || python3 extract_prompts.py
python3 gen_index.py
pdflatex -interaction=nonstopmode "$n.tex" >/dev/null; pdflatex -interaction=nonstopmode "$n.tex" >/dev/null
sed 's/^\\begin{document}/\\setbeameroption{show only notes}\\setbeamertemplate{note page}{\\insertslideintonotes{0.22}\\par\\vspace{6pt}{\\fontsize{15}{19}\\selectfont\\insertnote}}\n\\begin{document}/' "$n.tex" > "${n}_notes.tex"
pdflatex -interaction=nonstopmode "${n}_notes.tex" >/dev/null; pdflatex -interaction=nonstopmode "${n}_notes.tex" >/dev/null
echo "overfull/error lines: slides=$(grep -cE 'Overfull|^!' $n.log) notes=$(grep -cE 'Overfull|^!' ${n}_notes.log)"
rm -f "${n}_notes.tex" *.aux *.log *.nav *.out *.snm *.toc
ls -1 *.pdf
