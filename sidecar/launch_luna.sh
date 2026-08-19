#!/usr/bin/env bash
set -Eeuo pipefail

DSCT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
FOREMAN_INTERFACE_DIR="${FOREMAN_INTERFACE_DIR:-$DSCT_ROOT/../foreman_interface}"
COURSE_FOUNDRY_DIR="${COURSE_FOUNDRY_DIR:-$DSCT_ROOT/../course_foundry}"
CANVAS_ENV="${CANVAS_ENV:-$HOME/.config/canvas/canvas.env}"
MODE="${1:-preflight}"
LOCK="/tmp/dsct-luna-321.lock"

fail() {
  echo "LUNA LAUNCH STOP: $*" >&2
  exit 1
}

require_repo() {
  local path="$1" label="$2"
  [[ -d "$path" ]] || fail "$label directory not found: $path"
  git -C "$path" rev-parse --is-inside-work-tree >/dev/null 2>&1 \
    || fail "$label is not a Git worktree: $path"
  git -C "$path" remote get-url origin >/dev/null 2>&1 \
    || fail "$label has no origin remote: $path"
}

if [[ "${DSCT_LUNA_321_LAUNCHED:-0}" == "1" ]]; then
  fail "this launcher is already inside a Luna shift; recursive launch refused"
fi

case "$MODE" in
  preflight)
    JOB_PROMPT="$DSCT_ROOT/sidecar/jobs/321_dsct_preflight_to_green_to_write.md"
    ;;
  production)
    JOB_PROMPT="$DSCT_ROOT/sidecar/jobs/321_dsct_production_closeout.md"
    ;;
  *)
    fail "usage: bash sidecar/launch_luna.sh [production]"
    ;;
esac

command -v git >/dev/null 2>&1 || fail "git is not available on PATH"
command -v codex >/dev/null 2>&1 || fail "codex is not available on PATH"
command -v flock >/dev/null 2>&1 || fail "flock is not available on PATH"

require_repo "$DSCT_ROOT" "discrete_structures_and_critical_thinking"
require_repo "$FOREMAN_INTERFACE_DIR" "foreman_interface"
require_repo "$COURSE_FOUNDRY_DIR" "course_foundry"

ORIGIN_URL="$(git -C "$DSCT_ROOT" remote get-url origin 2>/dev/null || true)"
[[ "$ORIGIN_URL" =~ github\.com[:/]jeremy-evert/discrete_structures_and_critical_thinking(\.git)?$ ]] \
  || fail "DSCT origin is not jeremy-evert/discrete_structures_and_critical_thinking: $ORIGIN_URL"

for required in \
  "$JOB_PROMPT" \
  "$DSCT_ROOT/sidecar/LUNA_BURN.md" \
  "$FOREMAN_INTERFACE_DIR/FOREMAN.md" \
  "$FOREMAN_INTERFACE_DIR/contracts/owner_foreman.md" \
  "$FOREMAN_INTERFACE_DIR/contracts/foreman_worker.md" \
  "$FOREMAN_INTERFACE_DIR/spells/dispatch.md" \
  "$FOREMAN_INTERFACE_DIR/spells/golem.md"
do
  [[ -r "$required" ]] || fail "required file is missing or unreadable: $required"
done

[[ -r "$CANVAS_ENV" ]] || fail "Canvas environment file is missing or unreadable: $CANVAS_ENV"

exec 9>"$LOCK"
if ! flock -n 9; then
  fail "another DSCT Luna launcher currently owns $LOCK; do not start a second DSCT Foreman"
fi

CURRENT_BRANCH="$(git -C "$DSCT_ROOT" branch --show-current)"
[[ "$CURRENT_BRANCH" == "main" ]] \
  || fail "expected canonical DSCT branch main, found $CURRENT_BRANCH"

# Refuse tracked content dirt before launch. Untracked notes are preserved and
# left for Luna to classify rather than silently deleted.
TRACKED_DIRT="$(git -C "$DSCT_ROOT" -c core.fileMode=false status --porcelain --untracked-files=no)"
[[ -z "$TRACKED_DIRT" ]] || {
  echo "$TRACKED_DIRT" >&2
  fail "canonical DSCT main has tracked content changes; preserve/resolve them before launch"
}

# Fetch only. Do not mutate the launch script's own checkout while it is running.
git -C "$DSCT_ROOT" -c core.fileMode=false fetch -q origin main \
  || fail "could not fetch DSCT origin/main"

CURRENT_SHA="$(git -C "$DSCT_ROOT" rev-parse HEAD)"
ORIGIN_SHA="$(git -C "$DSCT_ROOT" rev-parse origin/main)"
[[ "$CURRENT_SHA" == "$ORIGIN_SHA" ]] \
  || fail "local DSCT main ($CURRENT_SHA) is not canonical origin/main ($ORIGIN_SHA). Run: git pull --ff-only origin main"

# Do not clean or normalize Course Foundry. Only refuse interrupted Git control
# operations. Luna's job requires isolated exact-SHA execution for shared tooling.
CF_GIT_DIR="$(git -C "$COURSE_FOUNDRY_DIR" rev-parse --git-dir)"
case "$CF_GIT_DIR" in
  /*) ;;
  *) CF_GIT_DIR="$COURSE_FOUNDRY_DIR/$CF_GIT_DIR" ;;
esac
[[ ! -e "$CF_GIT_DIR/MERGE_HEAD" ]] || fail "unfinished merge in shared Course Foundry checkout"
[[ ! -d "$CF_GIT_DIR/rebase-merge" && ! -d "$CF_GIT_DIR/rebase-apply" ]] \
  || fail "unfinished rebase in shared Course Foundry checkout"

LAUNCH_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

if [[ "$MODE" == "production" ]]; then
  PREFLIGHT_REL="sidecar/reports/321_luna_preflight_to_green_to_write.md"
  PREFLIGHT_TEXT="$(git -C "$DSCT_ROOT" show "origin/main:$PREFLIGHT_REL" 2>/dev/null || true)"
  [[ -n "$PREFLIGHT_TEXT" ]] \
    || fail "production requires canonical preflight report on origin/main: $PREFLIGHT_REL"
  printf '%s\n' "$PREFLIGHT_TEXT" | grep -Fxq '**Verdict:** `GREEN TO WRITE`' \
    || fail "canonical preflight verdict is not GREEN TO WRITE"

  AUTHORITY_TEXT=$(cat <<EOF
PRODUCTION AUTHORIZATION:
- Jeremy intentionally invoked bash sidecar/launch_luna.sh production at $LAUNCH_UTC.
- This is fresh authorization ONLY for the bounded DSCT production reconcile described in $JOB_PROMPT after every freshness gate passes.
- It is not authority for another Canvas course, cross-list/topology changes, unexplained destructive cleanup, or a materially changed plan.
- Record this launcher timestamp and authorization provenance in the production report.
EOF
)
else
  AUTHORITY_TEXT=$(cat <<EOF
PRODUCTION AUTHORIZATION:
- NOT GRANTED in this launch.
- SWOSU production Canvas is READ ONLY for the entire shift.
- Git/source/tooling work is authorized by the job.
- Non-production/Savnac reconciliation is allowed only when the job's own bounded safety conditions are satisfied.
EOF
)
fi

UNTRACKED="$(git -C "$DSCT_ROOT" status --porcelain --untracked-files=all | awk '$1 == "??" {sub(/^\?\? /, ""); print}' || true)"

STARTUP_PROMPT=$(cat <<EOF
You are Luna, the fresh OpenAI Codex Foreman for exactly one Discrete Structures & Critical Thinking job.

This is a NEW shift. Do not resume or inherit an older conversation. Do not select work from JTT.

WORKING DIRECTORY:
$DSCT_ROOT

CANONICAL FOREMAN CONTRACTS — READ THESE FIRST:
1. $FOREMAN_INTERFACE_DIR/contracts/owner_foreman.md
2. $FOREMAN_INTERFACE_DIR/FOREMAN.md
3. $FOREMAN_INTERFACE_DIR/contracts/foreman_worker.md

WHEN YOU DISPATCH BOUNDED WORKERS, ALSO READ:
4. $FOREMAN_INTERFACE_DIR/spells/dispatch.md
5. $FOREMAN_INTERFACE_DIR/spells/golem.md

YOUR ONE JOB:
$JOB_PROMPT

$AUTHORITY_TEXT

Read the job in full and execute it autonomously.

Operating boundaries:
- DSCT is the owning worksite and center of gravity.
- Do not take CS1, Computer Architecture, CS2, or JTT work.
- Preserve unexplained local/shared-worktree dirt. Isolate work rather than cleaning someone else's state.
- The shared Course Foundry checkout may contain active runtime state. Do not reset, stash, clean, or normalize it. Use isolated exact-SHA worktrees/clones for deployment-defining work.
- You may dispatch bounded workers yourself. Jeremy is not your message bus.
- Inspect worker receipts yourself, repair/retry bounded failures, and promote accepted DSCT work/evidence yourself when allowed by the governing contract.
- Do not confuse historical Prompt 320/Report 319 with current truth. Verify Git and live state.
- Keep moving until the job's DONE condition or a genuine stop condition.

Pre-existing untracked DSCT paths observed at launch, preserved for your classification:
${UNTRACKED:-none}

Begin now.
EOF
)

export DSCT_LUNA_321_LAUNCHED=1
export DSCT_LUNA_ROOT="$DSCT_ROOT"
export DSCT_LUNA_JOB="$JOB_PROMPT"
export DSCT_LUNA_FOREMAN_INTERFACE="$FOREMAN_INTERFACE_DIR"
export DSCT_LUNA_COURSE_FOUNDRY="$COURSE_FOUNDRY_DIR"
export DSCT_LUNA_CANVAS_ENV="$CANVAS_ENV"
export DSCT_LUNA_MODE="$MODE"

CODEX_ARGS=()
if codex --help 2>&1 | grep -q -- '--model'; then
  CODEX_ARGS+=(--model gpt-5.6-luna)
fi

echo ">>> Launching fresh Luna for DSCT: $MODE"
echo ">>> Job: $JOB_PROMPT"
echo ">>> Worksite: $DSCT_ROOT"
echo ">>> DSCT main: $CURRENT_SHA"
echo ">>> Launch UTC: $LAUNCH_UTC"
if [[ "$MODE" == "production" ]]; then
  echo ">>> SWOSU production authority: BOUNDED WRITE AUTHORIZED, subject to freshness gates"
else
  echo ">>> SWOSU production authority: READ ONLY"
fi

# No resume/continue flag is used. Every invocation is a fresh Luna shift.
exec codex "${CODEX_ARGS[@]}" "$STARTUP_PROMPT"
