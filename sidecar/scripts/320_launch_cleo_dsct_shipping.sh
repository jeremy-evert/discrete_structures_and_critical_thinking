#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="/mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking"
PROMPT="sidecar/prompts/320_continue_dsct_production_shipping_hold_week1_redesign.md"
LOCK="/tmp/dsct-cleocontrol-320.lock"

# If Cleo (or one of her workers) somehow tries to invoke the launcher again,
# refuse rather than recursively spawning another Foreman.
if [[ "${DSCT_CLEO_320_LAUNCHED:-0}" == "1" ]]; then
  echo "STOP: Prompt 320 Cleo is already launched. Do not invoke this launcher recursively." >&2
  exit 64
fi

cd "$ROOT"

# One Foreman seat for this production campaign. A second launch stops safely.
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "STOP: another Prompt 320 Cleo launcher currently owns $LOCK" >&2
  echo "Do not start a second DSCT production Foreman." >&2
  exit 65
fi

# Safe canonical-seat checks. The human one-liner also performs checkout/pull,
# but repeat the verification here so direct script invocation is safe too.
git checkout main
git pull --ff-only

if [[ ! -f "$PROMPT" ]]; then
  echo "STOP: governing prompt not found: $PROMPT" >&2
  exit 66
fi

CURRENT_BRANCH="$(git branch --show-current)"
CURRENT_SHA="$(git rev-parse HEAD)"
ORIGIN_SHA="$(git rev-parse origin/main)"

if [[ "$CURRENT_BRANCH" != "main" ]]; then
  echo "STOP: expected main, found $CURRENT_BRANCH" >&2
  exit 67
fi

if [[ "$CURRENT_SHA" != "$ORIGIN_SHA" ]]; then
  echo "STOP: local main ($CURRENT_SHA) is not origin/main ($ORIGIN_SHA) after pull." >&2
  exit 68
fi

# Do not silently launch a production Foreman on top of local edits.
if [[ -n "$(git status --porcelain)" ]]; then
  echo "STOP: canonical DSCT checkout is dirty. No Cleo launched." >&2
  git status --short --branch >&2
  exit 69
fi

printf '\n==> Launching fresh DSCT Cleo\n'
printf 'Repository: %s\n' "$ROOT"
printf 'Main SHA:   %s\n' "$CURRENT_SHA"
printf 'Work order: %s\n' "$PROMPT"
printf 'Canvas:     production course 74035 (writes only under Prompt 320 authority)\n'
printf 'Reserved:   Week 1 narrative/presentation lane belongs to Jeremy + Chaz\n'
printf 'Recursion:  launcher re-entry blocked\n\n'

read -r -d '' CLEO_ORDER <<'EOF' || true
You are Cleo, the Foreman for jeremy-evert/discrete_structures_and_critical_thinking.

You have ALREADY been launched by sidecar/scripts/320_launch_cleo_dsct_shipping.sh from a clean, synchronized canonical main checkout. Do NOT invoke this launcher again. Do NOT invoke another Foreman launcher. Do not recursively launch yourself.

Read sidecar/prompts/320_continue_dsct_production_shipping_hold_week1_redesign.md from the current checkout and execute it as the governing work order.

Your lane is DSCT production shipping. Jeremy + Chaz own the Week 1 narrative/presentation redesign in semester_kickoff_week and the reserved Week 1 paths named by Prompt 320. Do not edit that lane.

Start from current Git truth and read-only live truth for SWOSU Canvas course 74035. Keep production single-writer. Use bounded Golems for bounded work. If the Week 2 WAF seam does not fall in a bounded unit, name the yellow and move to other genuinely source-ready DSCT work. Do not fabricate lessons to make Canvas look full.

Jeremy is teaching. Manage the workers and evidence yourself. Escalate only the boundaries named in Prompt 320.

When the shift reaches a natural stopping point, leave durable DSCT-side evidence of what actually shipped, what remains yellow, and the exact next bounded unit.

Clipboard up. Take the con.
EOF

DSCT_CLEO_320_LAUNCHED=1 exec claude "$CLEO_ORDER"
