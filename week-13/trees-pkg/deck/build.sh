#!/usr/bin/env bash
# Build slides and a separate instructor-only speaker-notes PDF with cached Tectonic.
set -euo pipefail
cd "$(dirname "$0")"

python3 extract_prompts.py
python3 make_traces.py
python3 gen_index.py
python3 render_verbatim.py

rm -f trees_slides.pdf trees_notes.pdf trees.pdf trees_notes.tex
tectonic --only-cached --reruns 1 --keep-logs trees.tex >/dev/null 2>&1
mv trees.pdf trees_slides.pdf

sed 's/^\\begin{document}/\\setbeameroption{show only notes}\\setbeamertemplate{note page}{\\par\\vspace{6pt}{\\fontsize{15}{19}\\selectfont\\insertnote}}\n\\begin{document}/' trees.tex > trees_notes.tex
tectonic --only-cached --reruns 1 --keep-logs trees_notes.tex >/dev/null 2>&1

echo "overfull\/error lines: slides=$(grep -cE 'Overfull|^!' trees.log || true) notes=$(grep -cE 'Overfull|^!' trees_notes.log || true)"
echo "missing-character lines: slides=$(grep -c 'Missing character' trees.log || true) notes=$(grep -c 'Missing character' trees_notes.log || true)"
printf 'page counts: slides='; pdfinfo trees_slides.pdf | awk '/^Pages:/{print $2}'
printf 'page counts: notes='; pdfinfo trees_notes.pdf | awk '/^Pages:/{print $2}'
rm -f trees_notes.tex trees.aux trees.fls trees.nav trees.out trees.snm trees.toc trees.xdv trees_notes.aux trees_notes.fls trees_notes.nav trees_notes.out trees_notes.snm trees_notes.toc trees_notes.xdv
ls -1 trees_slides.pdf trees_notes.pdf
