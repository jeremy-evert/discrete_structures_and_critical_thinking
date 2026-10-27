#!/usr/bin/env bash
# Runs pytest at every student-ref-step-NN tag in a throwaway clone; prints one line per tag
# and exits non-zero if any RED tag passes or any GREEN tag fails.
# Usage: ladder_check.sh [repo-path-or-url]   (default: the repo this script lives in)
set -uo pipefail
src="${1:-$(git -C "$(dirname "$0")" rev-parse --show-toplevel)}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
git clone -q "$src" "$tmp/clone"
git -C "$tmp/clone" fetch -q --tags "$src" 2>/dev/null || true
bad=0
for tag in $(git -C "$tmp/clone" tag -l 'student-ref-step-*' | sort); do
  git -C "$tmp/clone" checkout -q --detach "$tag"
  msg="$(git -C "$tmp/clone" log -1 --format=%s "$tag")"
  want="${msg#*: }"; want="${want%% *}"            # RED or GREEN
  out="$(cd "$tmp/clone/week-11/tdd-walkthrough/student/instructor-only/reference" && python3 -I -m pytest -q -p no:cacheprovider 2>&1)"
  code=$?
  summary="$(printf '%s\n' "$out" | tail -1)"
  if [ "$want" = RED ] && [ $code -ne 0 ]; then verdict=ok
  elif [ "$want" = GREEN ] && [ $code -eq 0 ]; then verdict=ok
  else verdict=MISMATCH; bad=1; fi
  printf '%s | want %-5s | %s | %s\n' "$tag" "$want" "$summary" "$verdict"
done
exit $bad
