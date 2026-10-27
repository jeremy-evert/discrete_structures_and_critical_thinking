#!/usr/bin/env bash
# The starter folder must equal the reference solution as it stood before the student writes anything of their own
# (tag student-ref-step-05: tests/fixtures.py only changes at Step 07, when students add their own tracks).
set -u
root="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
base=week-11/tdd-walkthrough/student; bad=0
for f in $(cd "$root/$base/starter" && find . -type f ! -name .gitkeep | sort); do
  f="${f#./}"
  if git -C "$root" show "student-ref-step-05:$base/instructor-only/reference/$f" 2>/dev/null | diff -q -I '^#' - "$root/$base/starter/$f" >/dev/null; then echo "starter/$f | same as reference | ok"
  else echo "starter/$f | DIFFERS"; bad=1; fi
done
exit $bad
