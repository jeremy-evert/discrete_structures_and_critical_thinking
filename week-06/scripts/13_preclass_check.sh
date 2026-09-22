#!/usr/bin/env bash
# Fast, read-only Week 6 presentation readiness check.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEEK_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_DIR="$(cd "${WEEK_DIR}/.." && pwd)"
required=(
  README.md instructor/PRESENTATION_RUNBOOK.md instructor/week06_algorithms_growth_backdrop.tex
  scripts/00_recursive_fibonacci_simple.py scripts/01_recursive_fibonacci_trace.py
  scripts/02_recursive_fibonacci_60_second_race.py scripts/03_iterative_fibonacci_timing.py
  scripts/04_bubble_sort_timing.py scripts/07_parallel_sort_cpu.cpp scripts/07_parallel_sort_cpu.py
  scripts/08_parallel_sort_gpu.cu scripts/09_build_parallelism_webpage.py
  scripts/10_run_parallelism_showdown.sh scripts/12_collect_gpu_parallelism_showdown.sh
  websites/02_big_o_growth.html websites/03_fibonacci_recursive_vs_iterative.html
  websites/04_bubble_sort_quadratic_growth.html websites/04b_bubble_sort_measured.html
  websites/05_bubble_vs_merge_growth.html websites/06_live_sorting_runtime_race.html
  websites/07_parallelism_plot_twist.html results/parallel_sort_results.csv results/parallel_sort_hardware.txt
)
failures=0
fail() { printf 'BLOCKER: %s\n' "$*" >&2; failures=$((failures + 1)); }
have() { command -v "$1" >/dev/null 2>&1; }

printf 'DSCT Week 6 pre-class check\nRepository: %s\n\n' "${REPO_DIR}"
printf 'Git status (read-only):\n'
git -C "${REPO_DIR}" status --short --branch || fail 'could not read Git status'
printf '\nRequired files:\n'
for relative in "${required[@]}"; do
  if [[ -s "${WEEK_DIR}/${relative}" ]]; then printf '  OK  %s\n' "${relative}"; else fail "missing or empty week-06/${relative}"; fi
done

printf '\nPython syntax:\n'
if have python3 && python3 -m py_compile "${SCRIPT_DIR}"/*.py; then printf '  OK  all Week 6 Python scripts compile\n'; else fail 'Python syntax check failed or python3 is unavailable'; fi
printf '\nBash syntax:\n'
for script in "${SCRIPT_DIR}"/*.sh; do
  if bash -n "${script}"; then printf '  OK  %s\n' "${script##*/}"; else fail "Bash syntax failed: ${script##*/}"; fi
done

printf '\nLocal HTML dependency check:\n'
if python3 - "${WEEK_DIR}/websites" <<'PY'
import re
import sys
from pathlib import Path
bad = []
for page in sorted(Path(sys.argv[1]).glob("*.html")):
    text = page.read_text(encoding="utf-8")
    if not text.strip():
        bad.append(f"{page.name}: empty")
    if re.search(r"<(?:script|link)\b[^>]*(?:src|href)=[\"']https?://", text, re.I):
        bad.append(f"{page.name}: external script or stylesheet dependency")
if bad:
    print("\n".join(bad), file=sys.stderr)
    raise SystemExit(1)
print("  OK  pages are non-empty and have no external script/stylesheet dependency")
PY
then :; else fail 'a classroom HTML page needs an external asset or is empty'; fi

printf '\nTool availability (informational):\n'
for tool in htop g++ nvcc nvidia-smi latexmk pdflatex; do
  if have "${tool}"; then printf '  AVAILABLE  %s (%s)\n' "${tool}" "$(command -v "${tool}")"; else printf '  unavailable %s\n' "${tool}"; fi
done
if have latexmk || have pdflatex; then printf '  LaTeX source can be compiled with an installed engine.\n'; else printf '  LaTeX source is present; no local engine is installed, so no PDF is expected.\n'; fi
printf '\nRecommended first page on WSL:\n  explorer.exe "$(wslpath -w "%s")"\n' "${WEEK_DIR}/websites/02_big_o_growth.html"
printf 'Recommended first code command:\n  python3 week-06/scripts/00_recursive_fibonacci_simple.py\n'
if (( failures > 0 )); then printf '\nPRE-CLASS CHECK: BLOCKED (%d class-blocking failure(s))\n' "${failures}" >&2; exit 1; fi
printf '\nPRE-CLASS CHECK: PASS\n'
