#!/usr/bin/env bash
# Build the student deck and a separate speaker-notes PDF with Tectonic.
set -euo pipefail
cd "$(dirname "$0")"
name=boolean_fsm_slides
python3 extract_prompts.py ../prompts
python3 gen_index.py

tectonic --only-cached --keep-logs --keep-intermediates --reruns 1 "${name}.tex"
sed 's/^\\begin{document}/\\setbeameroption{show only notes}\\setbeamertemplate{note page}{\\insertslideintonotes{0.22}\\par\\vspace{6pt}{\\fontsize{15}{19}\\selectfont\\insertnote}}\n\\begin{document}/' \
  "${name}.tex" > "${name}_notes.tex"
tectonic --only-cached --keep-logs --keep-intermediates --reruns 1 "${name}_notes.tex"
mv "${name}_notes.pdf" "boolean_fsm_notes.pdf"

slides_errors=$(grep -cE 'Overfull|^!' "${name}.log" || true)
notes_errors=$(grep -cE 'Overfull|^!' "${name}_notes.log" || true)
slides_pages=$(pdfinfo "${name}.pdf" | awk '/^Pages:/ {print $2}')
notes_pages=$(pdfinfo boolean_fsm_notes.pdf | awk '/^Pages:/ {print $2}')
echo "page counts: slides=${slides_pages} notes=${notes_pages}"
echo "overfull/error lines: slides=${slides_errors} notes=${notes_errors}"
test "$slides_errors" -eq 0
test "$notes_errors" -eq 0

rm -f "${name}_notes.tex" *.aux *.log *.nav *.out *.snm *.toc *.fls *.fdb_latexmk *.synctex.gz
echo "built: ${name}.pdf boolean_fsm_notes.pdf"
