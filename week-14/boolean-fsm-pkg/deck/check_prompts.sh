#!/usr/bin/env bash
# Check every displayed prompt box against its numbered source prompt block.
set -euo pipefail
cd "$(dirname "$0")"
src="${1:-../prompts}"
fail=0
used=0
while read -r number label; do
  used=$((used + 1))
  prompt_file=$(ls "$src"/${number}_*.md 2>/dev/null | head -1 || true)
  if [[ -z "$prompt_file" ]]; then
    echo "MISSING prompt file for ${number}"
    fail=1
    continue
  fi
  expected=$(awk -v tag="\`\`\`prompt-${label}" '$0 == tag { inside=1; next } inside && /^```/ { inside=0 } inside' "$prompt_file")
  actual=$(cat "prompts_txt/${number}_${label}.txt" 2>/dev/null || echo "__missing__")
  if [[ "$expected" != "$actual" ]]; then
    echo "DIFF slide prompt ${number}${label} vs ${prompt_file}"
    fail=1
  fi
done < <(python3 gen_index.py --list-prompts)
python3 gen_index.py --check || fail=1
echo "prompt boxes checked: ${used}"
exit "$fail"
