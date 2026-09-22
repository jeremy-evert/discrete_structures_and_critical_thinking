#!/usr/bin/env bash
set -Eeuo pipefail

# DSCT Week 6 Hanna launcher.
#
# Normal use:
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh go
#
# If Hanna stops at an ordinary bounded-authority gate and Jeremy wants her
# to continue inside the already-authorized mission:
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh go-baby-go
#
# Other cockpit-free controls:
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh telemetry
  bash week-06/scripts/11_hanna_parallelism_showdown.sh status
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh tail
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh follow
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh resume "message"
#   bash week-06/scripts/11_hanna_parallelism_showdown.sh stop

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
WEEK_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd -P)"
DSCT_ROOT="$(cd -- "${WEEK_DIR}/.." && pwd -P)"
WORK_FARM_ROOT="$(dirname -- "${DSCT_ROOT}")"

FOREMAN_ROOT="${FOREMAN_ROOT:-${WORK_FARM_ROOT}/foreman_interface}"
SESSION="${HANNA_SESSION:-dsct-week06-parallelism}"
MISSION="jobs/tasks/dsct_week06_parallelism_showdown.md"
PROJECT_MISSION="${WEEK_DIR}/instructor/HANNA_PARALLELISM_SHOWDOWN.md"
WRAPPER="${FOREMAN_ROOT}/scripts/hanna_fire_and_forget.sh"

MODEL="${HANNA_MODEL:-gpt-5.6-terra}"
EFFORT="${HANNA_EFFORT:-high}"

fail() {
    printf 'GO BABY GO STOP: %s\n' "$*" >&2
    exit 1
}

repo_clean() {
    [[ -z "$(git -C "$1" status --porcelain 2>/dev/null)" ]]
}

refresh_foreman_if_safe() {
    if ! git -C "${FOREMAN_ROOT}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        fail "foreman_interface is not a Git checkout: ${FOREMAN_ROOT}"
    fi

    if repo_clean "${FOREMAN_ROOT}"; then
        printf 'Refreshing foreman_interface with a safe fast-forward pull...\n'
        git -C "${FOREMAN_ROOT}" pull --ff-only
    else
        printf 'foreman_interface has local changes; preserving them and skipping pull.\n'
    fi
}

ensure_local_dispatch() {
    local dispatch="${FOREMAN_ROOT}/${MISSION}"

    [[ -f "${PROJECT_MISSION}" ]] || \
        fail "project mission missing: ${PROJECT_MISSION}"

    if [[ -f "${dispatch}" ]]; then
        return 0
    fi

    # The project-local Week 6 mission is the authority. If foreman_interface
    # cannot be fast-forwarded because it contains unrelated local work, create
    # a local-only dispatch copy instead of making Jeremy stash/commit/relay.
    # Do not overwrite an existing dispatch and do not stage/commit this copy.
    mkdir -p -- "$(dirname -- "${dispatch}")"
    cp -- "${PROJECT_MISSION}" "${dispatch}"

    printf 'Created local-only Hanna dispatch from the authoritative Week 6 mission:\n'
    printf '  %s\n' "${dispatch}"
    printf 'Existing foreman_interface work was left untouched.\n'
}

require_launch_files() {
    [[ -f "${PROJECT_MISSION}" ]] || \
        fail "project mission missing: ${PROJECT_MISSION}"

    [[ -f "${WRAPPER}" ]] || \
        fail "Hanna fire-and-forget wrapper missing: ${WRAPPER}"

    ensure_local_dispatch

    [[ -f "${FOREMAN_ROOT}/${MISSION}" ]] || \
        fail "could not create Hanna dispatch: ${FOREMAN_ROOT}/${MISSION}"
}

wrapper() {
    bash "${WRAPPER}" "$@"
}

ensure_telemetry_tools() {
    local missing=()

    command -v htop >/dev/null 2>&1 || missing+=("htop")
    command -v nvtop >/dev/null 2>&1 || missing+=("nvtop")

    if (( ${#missing[@]} == 0 )); then
        printf 'Telemetry tools ready: htop + nvtop\n'
        return 0
    fi

    printf 'Telemetry tools missing: %s\n' "${missing[*]}"

    if command -v apt-get >/dev/null 2>&1 && command -v sudo >/dev/null 2>&1; then
        printf 'Installing missing classroom telemetry tools with apt...\n'
        if sudo apt-get update && sudo apt-get install -y "${missing[@]}"; then
            printf 'Telemetry tools installed.\n'
        else
            printf 'WARNING: telemetry install failed; benchmark launch will continue.\n' >&2
        fi
    else
        printf 'No supported automatic apt/sudo path; benchmark launch will continue.\n'
    fi
}

show_telemetry_cockpit() {
    printf '\n============================================================\n'
    printf 'OPTIONAL LIVE TELEMETRY\n'
    printf '============================================================\n'

    if command -v htop >/dev/null 2>&1; then
        printf 'CPU/RAM:  htop\n'
    else
        printf 'CPU/RAM:  top   (press 1 for per-core view where supported)\n'
    fi

    if command -v nvtop >/dev/null 2>&1; then
        printf 'GPU:      nvtop\n'
    elif command -v nvidia-smi >/dev/null 2>&1; then
        printf 'GPU:      watch -n 0.5 nvidia-smi\n'
        printf 'GPU alt:  nvidia-smi dmon -s pucm\n'
    else
        printf 'GPU:      no nvtop or nvidia-smi detected on this host\n'
    fi

    printf 'HANNA:    bash week-06/scripts/11_hanna_parallelism_showdown.sh follow\n'
    printf '============================================================\n'
    printf 'Open those in separate terminals if you want the full cockpit.\n\n'
}

show_banner() {
    cat <<EOF

============================================================
DSCT WEEK 6 — HANNA PARALLELISM SHOWDOWN
============================================================
DSCT repo:       ${DSCT_ROOT}
Project mission: ${PROJECT_MISSION}
Foreman repo:    ${FOREMAN_ROOT}
Session:         ${SESSION}
Model:           ${MODEL}
Effort:          ${EFFORT}
============================================================

EOF
}

action="${1:-go}"

case "${action}" in
    go)
        show_banner
        [[ -d "${FOREMAN_ROOT}" ]] || \
            fail "foreman_interface checkout not found at ${FOREMAN_ROOT}"

        refresh_foreman_if_safe
        require_launch_files
        ensure_telemetry_tools

        if command -v tmux >/dev/null 2>&1 &&
           tmux has-session -t "=${SESSION}" 2>/dev/null; then
            printf 'Hanna session already exists. Showing status instead of starting a duplicate.\n\n'
            wrapper status "${SESSION}"
            exit 0
        fi

        printf 'Launching Hanna detached. Jeremy does not need to stay attached.\n\n'

        HANNA_MODEL="${MODEL}" \
        HANNA_EFFORT="${EFFORT}" \
            wrapper start "${MISSION}" "${SESSION}"

        printf '\nGO BABY GO.\n'
        printf 'Use this only when you want a quick look:\n'
        printf '  bash %q status\n' "$0"
        show_telemetry_cockpit
        ;;

    telemetry)
        ensure_telemetry_tools
        show_telemetry_cockpit
        ;;

    status)
        require_launch_files
        wrapper status "${SESSION}"
        ;;

    tail)
        require_launch_files
        wrapper tail "${SESSION}"
        ;;

    follow)
        require_launch_files
        wrapper follow "${SESSION}"
        ;;

    resume)
        shift
        [[ $# -gt 0 ]] || fail 'resume requires a message'
        require_launch_files
        wrapper resume "${SESSION}" "$*"
        ;;

    go-baby-go)
        require_launch_files
        wrapper resume "${SESSION}" \
            "Go baby go. Jeremy confirms you should continue autonomously inside the authority already granted by the DSCT Week 6 mission. Re-inspect current truth, perform ordinary repairs/tests/commits/pushes without asking again, and continue until COMPLETE. This does not authorize scope expansion, secrets, destructive system changes, driver changes, purchases, or bypassing a genuine credential/physical-action gate."
        ;;

    stop)
        require_launch_files
        wrapper stop "${SESSION}"
        ;;

    *)
        cat >&2 <<EOF
Usage:
  bash week-06/scripts/11_hanna_parallelism_showdown.sh go
  bash week-06/scripts/11_hanna_parallelism_showdown.sh status
  bash week-06/scripts/11_hanna_parallelism_showdown.sh tail
  bash week-06/scripts/11_hanna_parallelism_showdown.sh follow
  bash week-06/scripts/11_hanna_parallelism_showdown.sh resume "message"
  bash week-06/scripts/11_hanna_parallelism_showdown.sh go-baby-go
  bash week-06/scripts/11_hanna_parallelism_showdown.sh stop
EOF
        exit 64
        ;;
esac
