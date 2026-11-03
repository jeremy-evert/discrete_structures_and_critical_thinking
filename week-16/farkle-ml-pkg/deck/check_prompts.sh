#!/usr/bin/env bash
# Exit 0 only when every prompt box equals its prompt Markdown block.
set -euo pipefail
cd "$(dirname "$0")"

src="${1:-../prompts}"
fail=0
used=0
expected_names=(
  01_claim_and_rule.md
  02_initial_sample_audit.md
  03_bundle_stability_check.md
  04_repair_an_overclaim.md
)

for name in "${expected_names[@]}"; do
  if [ ! -f "$src/$name" ]; then
    echo "MISSING required prompt file: $name"
    fail=1
  fi
done

while read -r number label; do
  used=$((used + 1))
  prompt_file=$(ls "$src"/${number}_*.md 2>/dev/null | head -1 || true)
  if [ -z "$prompt_file" ]; then
    echo "MISSING prompt file for $number"
    fail=1
    continue
  fi
  expected=$(awk -v tag="\`\`\`prompt-$label" '$0==tag{p=1;next} p&&/^```/{p=0} p' "$prompt_file")
  actual=$(cat "prompts_txt/${number}_${label}.txt" 2>/dev/null || echo "__missing__")
  if [ "$expected" != "$actual" ]; then
    echo "DIFF slide prompt $number $label vs $prompt_file"
    fail=1
  fi
done < <(python3 gen_index.py --list-prompts)

python3 gen_index.py --check || fail=1
python3 scripts/make_numbers.py --check || fail=1
echo "prompt boxes checked: $used"
exit "$fail"
