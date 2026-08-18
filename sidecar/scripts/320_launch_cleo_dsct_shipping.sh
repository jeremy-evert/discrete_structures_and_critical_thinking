#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="/mnt/brandy_nvme/jevert/git/discrete_structures_and_critical_thinking"
PROMPT="sidecar/prompts/320_continue_dsct_production_shipping_hold_week1_redesign.md"
LOCK="/tmp/dsct-cleocontrol-320.lock"

# This launcher is a human-to-Foreman rail. It may launch Cleo exactly once.
# A launched Cleo or worker must never invoke this launcher again.
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

# File executable-bit changes are not pedagogical/source changes and must not
# become a Mammal-RAM launch tax. Always invoke this launcher with `bash`.
git -c core.fileMode=false fetch origin main

CURRENT_BRANCH="$(git branch --show-current)"
if [[ "$CURRENT_BRANCH" != "main" ]]; then
  echo "STOP: expected canonical DSCT branch main, found $CURRENT_BRANCH." >&2
  exit 66
fi

# Pull current main while ignoring local executable-bit noise.
git -c core.fileMode=false pull --ff-only origin main

CURRENT_SHA="$(git rev-parse HEAD)"
ORIGIN_SHA="$(git rev-parse origin/main)"
if [[ "$CURRENT_SHA" != "$ORIGIN_SHA" ]]; then
  echo "STOP: local main ($CURRENT_SHA) is not origin/main ($ORIGIN_SHA) after pull." >&2
  exit 67
fi

if [[ ! -f "$PROMPT" ]]; then
  echo "STOP: governing prompt not found: $PROMPT" >&2
  exit 68
fi

# Meaningful tracked changes remain a hard stop. File-mode-only noise is ignored.
TRACKED_DIRT="$(git -c core.fileMode=false status --porcelain --untracked-files=no)"
if [[ -n "$TRACKED_DIRT" ]]; then
  echo "STOP: canonical DSCT checkout has tracked content changes. No Cleo launched." >&2
  printf '%s\n' "$TRACKED_DIRT" >&2
  exit 69
fi

# Untracked human notes/prompts are preserved rather than forcing Jeremy to
# stash/move/delete them. Only known non-course-source namespaces are tolerated.
mapfile -t UNTRACKED_PATHS < <(git status --porcelain --untracked-files=all | awk '$1 == "??" {sub(/^\?\? /, ""); print}')
PROTECTED_DIRT=""
for path in "${UNTRACKED_PATHS[@]:-}"; do
  [[ -z "$path" ]] && continue
  case "$path" in
    prompts/*|sidecar/raw/*|sidecar/scratch/*)
      PROTECTED_DIRT+="- $path"$'\n'
      ;;
    *)
      echo "STOP: untracked path may affect DSCT source and is not in a protected scratch/prompt namespace: $path" >&2
      echo "No files were changed or removed. Classify this path before launching Cleo." >&2
      exit 70
      ;;
  esac
done

printf '\n==> Launching fresh DSCT Cleo\n'
printf 'Repository: %s\n' "$ROOT"
printf 'Main SHA:   %s\n' "$CURRENT_SHA"
printf 'Work order: %s\n' "$PROMPT"
printf 'Canvas:     production course 74035 (writes only under Prompt 320 authority)\n'
printf 'Reserved:   Week 1 narrative/presentation lane belongs to Jeremy + Chaz\n'
printf 'Recursion:  launcher re-entry blocked\n'
printf 'File mode:  ignored; launcher is intentionally invoked with bash\n'
if [[ -n "$PROTECTED_DIRT" ]]; then
  printf 'Protected pre-existing untracked paths:\n%s' "$PROTECTED_DIRT"
else
  printf 'Protected pre-existing untracked paths: none\n'
fi
printf '\n'

read -r -d '' CLEO_ORDER <<EOF || true
You are Cleo, the Foreman for jeremy-evert/discrete_structures_and_critical_thinking.

You have ALREADY been launched by sidecar/scripts/320_launch_cleo_dsct_shipping.sh from canonical main at $CURRENT_SHA. Do NOT invoke this launcher again. Do NOT invoke another Foreman launcher. Do not recursively launch yourself.

Read sidecar/prompts/320_continue_dsct_production_shipping_hold_week1_redesign.md from the current checkout and execute it as the governing work order.

Your lane is DSCT production shipping. Jeremy + Chaz own the Week 1 narrative/presentation redesign in semester_kickoff_week and the reserved Week 1 paths named by Prompt 320. Do not edit that lane.

The launcher observed the following pre-existing untracked human-worktree paths. PRESERVE them. Do not edit, stage, commit, delete, move, clean, or use them as authority unless Prompt 320 independently names them:
${PROTECTED_DIRT:-none}
Start from current Git truth and read-only live truth for SWOSU Canvas course 74035. Keep production single-writer. Use bounded Golems for bounded work. If the Week 2 WAF seam does not fall in a bounded unit, name the yellow and move to other genuinely source-ready DSCT work. Do not fabricate lessons to make Canvas look full.

Jeremy is teaching. Manage the workers and evidence yourself. Escalate only the boundaries named in Prompt 320.

When the shift reaches a natural stopping point, leave durable DSCT-side evidence of what actually shipped, what remains yellow, and the exact next bounded unit.

Clipboard up. Take the con.
EOF

DSCT_CLEO_320_LAUNCHED=1 exec claude "$CLEO_ORDER"
