#!/usr/bin/env bash
set -euo pipefail

# Fast, non-destructive Week 6 archive integrity check. This does not run
# classroom benchmarks, mutate Git history, or require optional tools.

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
WEEK_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd -P)"
REPO_ROOT="$(cd -- "${WEEK_DIR}/.." && pwd -P)"
if [[ -n "${DSCT_GIT_BIN:-}" ]]; then
    GIT_BIN="${DSCT_GIT_BIN}"
elif [[ -x /usr/bin/git ]]; then
    GIT_BIN=/usr/bin/git
else
    GIT_BIN=git
fi

failures=0
require_file() {
    if [[ -s "$1" ]]; then
        printf 'OK   file %s\n' "${1#"${REPO_ROOT}/"}"
    else
        printf 'FAIL missing/empty %s\n' "${1#"${REPO_ROOT}/"}"
        failures=$((failures + 1))
    fi
}

printf '%s\n' 'Week 6 archive validation (read-only checks)'
printf '%s\n' '--- Git status ---'
"${GIT_BIN}" -C "${REPO_ROOT}" status --short --branch -- week-06

printf '%s\n' '--- required archive files ---'
required=(
    "${WEEK_DIR}/NEXT_SEMESTER_START_HERE.md"
    "${WEEK_DIR}/instructor/FALL_2026_ARCHIVE_MANIFEST.md"
    "${WEEK_DIR}/instructor/week06_algorithms_growth_backdrop.tex"
    "${WEEK_DIR}/scripts/13_archive_validation.sh"
    "${WEEK_DIR}/sidecar/hanna_semester_closeout/STATUS.md"
    "${WEEK_DIR}/sidecar/hanna_semester_closeout/AUTHORSHIP.md"
    "${WEEK_DIR}/sidecar/hanna_semester_closeout/WORKER_INDEX.md"
    "${WEEK_DIR}/sidecar/hanna_semester_closeout/SUMMARY.md"
    "${WEEK_DIR}/sidecar/archive/fall-2026/stuff.md"
    "${WEEK_DIR}/results/parallel_sort_results.csv"
    "${WEEK_DIR}/results/parallel_sort_hardware.txt"
)
for path in "${required[@]}"; do require_file "${path}"; done

printf '%s\n' '--- Python syntax ---'
mapfile -t python_files < <(find "${WEEK_DIR}/scripts" -maxdepth 1 -type f -name '*.py' -print | sort)
if ((${#python_files[@]})); then
    python3 -m py_compile "${python_files[@]}"
    printf 'OK   %d Python scripts compile\n' "${#python_files[@]}"
else
    printf 'FAIL no Python scripts found\n'
    failures=$((failures + 1))
fi

printf '%s\n' '--- Bash syntax ---'
mapfile -t shell_files < <(find "${WEEK_DIR}/scripts" -maxdepth 1 -type f -name '*.sh' -print | sort)
for path in "${shell_files[@]}"; do bash -n "${path}"; done
printf 'OK   %d Bash scripts parse\n' "${#shell_files[@]}"

printf '%s\n' '--- HTML presence ---'
html_count=0
while IFS= read -r -d '' path; do
    require_file "${path}"
    html_count=$((html_count + 1))
done < <(find "${WEEK_DIR}/websites" -maxdepth 1 -type f -name '*.html' -print0 | sort -z)
printf 'OK   inspected %d HTML files\n' "${html_count}"

printf '%s\n' '--- optional tool availability ---'
for tool in htop g++ nvcc nvidia-smi latexmk pdflatex; do
    if command -v "${tool}" >/dev/null 2>&1; then
        printf 'FOUND %-10s %s\n' "${tool}" "$(command -v "${tool}")"
    else
        printf 'MISS  %-10s (optional; no archive failure)\n' "${tool}"
    fi
done

printf '%s\n' '--- source hygiene ---'
conflicts="$(mktemp)"
trap 'rm -f -- "${conflicts}"' EXIT
if rg -n '^(<<<<<<< .*$|=======$|>>>>>>> .*$)' "${WEEK_DIR}" --glob '!*.html' --glob '!*.csv' --glob '!*.txt' >"${conflicts}"; then
    cat "${conflicts}"
    printf 'FAIL conflict markers found\n'
    failures=$((failures + 1))
else
    printf 'OK   no merge-conflict markers in text source\n'
fi

printf '%s\n' 'Start next semester at:' "${WEEK_DIR}/NEXT_SEMESTER_START_HERE.md"
if ((failures)); then
    printf 'ARCHIVE VALIDATION FAILED: %d genuine failure(s)\n' "${failures}" >&2
    exit 1
fi
printf '%s\n' 'ARCHIVE VALIDATION PASSED'
