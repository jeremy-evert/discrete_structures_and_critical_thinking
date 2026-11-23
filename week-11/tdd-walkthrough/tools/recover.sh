#!/usr/bin/env bash
# Recovery move: overwrite ./merger and ./tests with the reference versions from a ladder tag.
# Run from your live working folder.  Usage: tools/recover.sh NN   (e.g. 07 -> tdd-step-07)
# Set LADDER_REPO to the DSCT clone (default: ~/git/discrete_structures_and_critical_thinking).
set -euo pipefail
n="${1:?usage: recover.sh NN}"
repo="${LADDER_REPO:-$HOME/git/discrete_structures_and_critical_thinking}"
rm -rf ./merger ./tests
git -C "$repo" archive "tdd-step-$n" week-11/tdd-walkthrough/merger week-11/tdd-walkthrough/tests | tar -x --strip-components=2
[ -f pytest.ini ] || printf '[pytest]\npythonpath = .\ntestpaths = tests\n' > pytest.ini
echo "restored merger/ and tests/ to tdd-step-$n"; python3 -m pytest -q 2>&1 | tail -1
