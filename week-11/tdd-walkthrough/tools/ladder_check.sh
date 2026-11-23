#!/usr/bin/env bash
# Runs pytest at every tdd-step-NN tag in a throwaway clone and prints one line per tag.
# Usage: tools/ladder_check.sh [repo-path-or-url]   (default: the repo this script lives in)
set -uo pipefail
src="${1:-$(git -C "$(dirname "$0")" rev-parse --show-toplevel)}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
git clone -q "$src" "$tmp/clone"
git -C "$tmp/clone" fetch -q --tags "$src" 2>/dev/null || true
for tag in $(git -C "$tmp/clone" tag -l 'tdd-step-*' | sort); do
  git -C "$tmp/clone" checkout -q --detach "$tag"
  summary="$(cd "$tmp/clone/week-11/tdd-walkthrough" && python3 -m pytest -q -p no:cacheprovider 2>&1 | tail -1)"
  msg="$(git -C "$tmp/clone" log -1 --format=%s "$tag")"
  printf '%s | %s | %s\n' "$tag" "$summary" "${msg#*: }"
done
