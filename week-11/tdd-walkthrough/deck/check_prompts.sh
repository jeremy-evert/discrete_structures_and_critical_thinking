#!/usr/bin/env bash
# Exit 0 only if every PROMPT box on the slides equals the text in the real prompt file.
# Usage: check_prompts.sh [PROMPTS_DIR]   (default ../prompts)
set -euo pipefail
cd "$(dirname "$0")"
src="${1:-../prompts}"
fail=0; used=0
while read -r nn ab; do
  used=$((used+1))
  f=$(ls "$src"/${nn}_*.md 2>/dev/null | head -1 || true)
  if [ -z "$f" ]; then echo "MISSING prompt file for $nn"; fail=1; continue; fi
  expect=$(awk -v tag="\`\`\`prompt-$ab" '$0==tag{p=1;next} p&&/^```/{p=0} p' "$f")
  got=$(cat "prompts_txt/${nn}_${ab}.txt" 2>/dev/null || echo "__missing__")
  if [ "$expect" != "$got" ]; then echo "DIFF slide prompt $nn $ab vs $f"; fail=1; fi
done < <(python3 gen_index.py --list-prompts)
python3 gen_index.py --check || fail=1
python3 check_glossary.py || fail=1
echo "prompt boxes checked: $used"
exit $fail
