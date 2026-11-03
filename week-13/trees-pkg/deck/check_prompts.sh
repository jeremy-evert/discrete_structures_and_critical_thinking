#!/usr/bin/env bash
# Verify canonical prompts, rendered prompt listings, generated traces, the index,
# glossary coverage, and the unchanged Decision Gate.
set -euo pipefail
cd "$(dirname "$0")"
src="${1:-../prompts}"
fail=0
used=0
expected='01 a
01 b
02 a
02 b
03 a
03 b
04 a
04 b
05 a
05 b
06 a
06 b
07 a'
actual=$(python3 gen_index.py --list-prompts)
if [ "$actual" != "$expected" ]; then
  echo "prompt references differ from the seven source files"
  printf '%s\n' "$actual"
  fail=1
fi
while read -r nn ab; do
  [ -n "$nn" ] || continue
  used=$((used + 1))
  f=$(ls "$src"/${nn}_*.md 2>/dev/null | head -1 || true)
  if [ -z "$f" ]; then
    echo "MISSING prompt file for $nn"
    fail=1
    continue
  fi
  expect=$(awk -v tag="\`\`\`prompt-$ab" '$0==tag{p=1;next} p&&/^```/{p=0} p' "$f")
  got=$(cat "prompts_txt/${nn}_${ab}.txt" 2>/dev/null || echo "__missing__")
  if [ "$expect" != "$got" ]; then
    echo "DIFF slide prompt $nn $ab vs $f"
    fail=1
  fi
done < <(printf '%s\n' "$actual")

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
python3 extract_prompts.py "$src" "$tmp/prompts_txt" || fail=1
python3 render_verbatim.py "$tmp/prompts_txt" "$tmp/verbatim_txt" "$PWD/gate_text.txt" || fail=1
if ! diff -ru -- "$tmp/prompts_txt" prompts_txt; then
  echo "prompts_txt is not the deterministic extraction of prompts/"
  fail=1
fi
if ! diff -ru -- "$tmp/verbatim_txt" verbatim_txt; then
  echo "verbatim_txt is not the deterministic rendered transform of prompts/"
  fail=1
fi
python3 gen_index.py --check || fail=1
python3 make_traces.py --check || fail=1
python3 check_glossary.py || fail=1
cmp -s gate_text.txt ../../student/decision-gate.md || { echo "gate_text.txt differs from student/decision-gate.md"; fail=1; }
grep -q '\\TraceProjectPre' part3.tex || { echo "part3.tex is not using generated project traces"; fail=1; }
grep -q '\\TraceDecisionBFS' part4.tex || { echo "part4.tex is not using generated decision traces"; fail=1; }
python3 check_layout.py trees_slides.pdf trees_notes.pdf || fail=1
echo "prompt boxes checked: $used"
exit "$fail"
