#!/usr/bin/env bash
# Build slides and a separate speaker-notes PDF with Tectonic.
set -euo pipefail
cd "$(dirname "$0")"

n=farkle_ml
tectonic_bin="/home/jevert/.local/bin/tectonic"

python3 scripts/make_numbers.py >/dev/null
python3 extract_prompts.py >/dev/null
python3 gen_index.py >/dev/null

"$tectonic_bin" --keep-logs --keep-intermediates "$n.tex" > "${n}_slides.tectonic.log" 2>&1
mv -f "${n}.pdf" "${n}_slides.pdf"

sed 's/^\\begin{document}/\\setbeameroption{show only notes}\\setbeamertemplate{note page}{\\insertslideintonotes{0.22}\\par\\vspace{6pt}{\\fontsize{15}{19}\\selectfont\\insertnote}}\n\\begin{document}/' "$n.tex" > "${n}_notes.tex"
"$tectonic_bin" --keep-logs --keep-intermediates "${n}_notes.tex" > "${n}_notes.tectonic.log" 2>&1

slide_log_count=$(grep -cE 'Overfull|^!' "${n}.log" || true)
notes_log_count=$(grep -cE 'Overfull|^!' "${n}_notes.log" || true)
slide_pages=$(pdfinfo "${n}_slides.pdf" | awk '/^Pages:/{print $2}')
notes_pages=$(pdfinfo "${n}_notes.pdf" | awk '/^Pages:/{print $2}')

echo "slides pages: ${slide_pages}"
echo "notes pages: ${notes_pages}"
echo "overfull/error lines: slides=${slide_log_count} notes=${notes_log_count}"
echo "outputs: ${n}_slides.pdf ${n}_notes.pdf"
