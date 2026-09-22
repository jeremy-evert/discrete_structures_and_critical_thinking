#!/usr/bin/env bash
set -euo pipefail

# Run this from Jeremy's ordinary WSL terminal, outside the Hanna sandbox, after
# the CPU benchmark has created week-06/results/parallel_sort_results.csv.
# It preserves CPU rows, replaces only prior GPU rows, adds real CUDA/Thrust
# timings, and regenerates the self-contained classroom webpage.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEEK_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
RESULT_DIR="${WEEK_DIR}/results"
CSV="${RESULT_DIR}/parallel_sort_results.csv"
META="${RESULT_DIR}/parallel_sort_hardware.txt"
GPU_SRC="${SCRIPT_DIR}/08_parallel_sort_gpu.cu"
GENERATOR="${SCRIPT_DIR}/09_build_parallelism_webpage.py"
HTML="${WEEK_DIR}/websites/07_parallelism_plot_twist.html"
GPU_BIN="/tmp/dsct_week06_parallel_sort_gpu"

fail() {
    echo "ERROR: $*" >&2
    exit 1
}

[[ -f "${CSV}" ]] || fail "CPU results missing; run bash week-06/scripts/10_run_parallelism_showdown.sh first."
[[ -f "${META}" ]] || fail "CPU metadata missing; run the CPU benchmark first."
command -v nvcc >/dev/null 2>&1 || fail "nvcc is unavailable in this shell."
command -v nvidia-smi >/dev/null 2>&1 || fail "nvidia-smi is unavailable in this shell."
nvidia-smi -L >/dev/null 2>&1 || fail "NVIDIA device access is unavailable in this shell."

header="$(head -n 1 "${CSV}")"
[[ "${header}" == "backend,n,workers,median_ms,timed_sorts" ]] || \
    fail "Unexpected CSV schema: ${header}"

tmp_csv="$(mktemp "${RESULT_DIR}/parallel_sort_results.XXXXXX")"
tmp_meta="$(mktemp "${RESULT_DIR}/parallel_sort_hardware.XXXXXX")"
cleanup() { rm -f -- "${tmp_csv}" "${tmp_meta}"; }
trap cleanup EXIT

# Keep the canonical header and every non-GPU row. This makes the helper safe to
# rerun: prior GPU records cannot accumulate or contaminate the chart.
echo "Compiling CUDA/Thrust GPU benchmark..."
nvcc -O3 -std=c++17 "${GPU_SRC}" -o "${GPU_BIN}"

awk -F, 'NR == 1 || $1 !~ /^gpu_/' "${CSV}" > "${tmp_csv}"
awk -F= '$1 !~ /^gpu_/' "${META}" > "${tmp_meta}"
printf 'gpu_access=available_from_host_wsl\n' >> "${tmp_meta}"

echo "Collecting real GPU sort-only and end-to-end medians..."
"${GPU_BIN}" --output "${tmp_csv}" --metadata "${tmp_meta}" --repeats 3

mv -- "${tmp_csv}" "${CSV}"
mv -- "${tmp_meta}" "${META}"

echo "Regenerating classroom webpage..."
python3 "${GENERATOR}" --csv "${CSV}" --metadata "${META}" --output "${HTML}"

echo "GPU timings added safely: ${CSV}"
echo "Open: ${HTML}"
