#!/usr/bin/env bash
# Runs the reference demos for Steps 01-03 and diffs against the recorded expected output.
set -u
here="$(cd "$(dirname "$0")" && pwd)"; bad=0
for f in "$here"/reference/demos/step0*.py; do
  n="$(basename "$f" .py)"
  if python3 -I "$f" | diff -q - "$here/reference/demos/expected/$n.txt" >/dev/null; then echo "$n | output matches expected | ok"
  else echo "$n | MISMATCH"; bad=1; fi
done
exit $bad
