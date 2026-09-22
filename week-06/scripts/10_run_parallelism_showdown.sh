#!/usr/bin/env bash
set -euo pipefail

# Week 6 parallelism showdown.
#
# One command:
#   bash week-06/scripts/10_run_parallelism_showdown.sh
#
# Produces:
#   week-06/results/parallel_sort_results.csv
#   week-06/results/parallel_sort_hardware.txt
#   week-06/websites/07_parallelism_plot_twist.html
#
# Optional:
#   DSCT_THREADS=8 bash week-06/scripts/10_run_parallelism_showdown.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEEK_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
RESULT_DIR="${WEEK_DIR}/results"
WEB_DIR="${WEEK_DIR}/websites"

CSV="${RESULT_DIR}/parallel_sort_results.csv"
META="${RESULT_DIR}/parallel_sort_hardware.txt"
HTML="${WEB_DIR}/07_parallelism_plot_twist.html"

CPU_SRC="${SCRIPT_DIR}/07_parallel_sort_cpu.cpp"
CPU_FALLBACK="${SCRIPT_DIR}/07_parallel_sort_cpu.py"
GPU_SRC="${SCRIPT_DIR}/08_parallel_sort_gpu.cu"
GENERATOR="${SCRIPT_DIR}/09_build_parallelism_webpage.py"

CPU_BIN="/tmp/dsct_week06_parallel_sort_cpu"
GPU_BIN="/tmp/dsct_week06_parallel_sort_gpu"

mkdir -p "${RESULT_DIR}" "${WEB_DIR}"

if ! command -v python3 >/dev/null 2>&1; then
    echo "ERROR: python3 is required to build the classroom webpage."
    exit 1
fi

LOGICAL_THREADS="$(nproc 2>/dev/null || echo 2)"

if [[ -n "${DSCT_THREADS:-}" ]]; then
    THREADS="${DSCT_THREADS}"
else
    THREADS="${LOGICAL_THREADS}"
fi

CPU_MODEL="$(
    lscpu 2>/dev/null |
    awk -F: '/Model name/ {sub(/^[[:space:]]+/, "", $2); print $2; exit}'
)"

if [[ -z "${CPU_MODEL}" ]]; then
    CPU_MODEL="Unknown CPU"
fi

cat > "${META}" <<EOF
cpu_model=${CPU_MODEL}
cpu_logical_threads=${LOGICAL_THREADS}
parallel_workers=${THREADS}
EOF

echo
echo "============================================================"
echo "WEEK 6 PARALLELISM SHOWDOWN"
echo "============================================================"
echo "CPU: ${CPU_MODEL}"
echo "Logical processors: ${LOGICAL_THREADS}"
echo "Parallel workers for this run: ${THREADS}"
echo

if command -v g++ >/dev/null 2>&1; then
    echo "[1/4] Compiling CPU benchmark..."
    g++ -O3 -std=c++17 -fopenmp "${CPU_SRC}" -o "${CPU_BIN}"
    echo "cpu_parallel_implementation=GNU libstdc++ parallel multiway mergesort via OpenMP" >> "${META}"
    echo "[2/4] Running sequential CPU vs parallel CPU..."
    "${CPU_BIN}" --output "${CSV}" --threads "${THREADS}" --repeats 3
else
    echo "[1/4] No C++ compiler found; using Python multiprocessing."
    echo "cpu_parallel_implementation=Python multiprocessing chunk sort plus merge" >> "${META}"
    echo "[2/4] Running sequential CPU vs multiprocess CPU..."
    python3 "${CPU_FALLBACK}" --output "${CSV}" --threads "${THREADS}" --repeats 3
fi

GPU_RAN=0

if command -v nvcc >/dev/null 2>&1 &&
   command -v nvidia-smi >/dev/null 2>&1 &&
   nvidia-smi -L >/dev/null 2>&1; then

    echo
    echo "[3/4] CUDA detected. Compiling and running GPU benchmark..."
    nvcc -O3 -std=c++17 "${GPU_SRC}" -o "${GPU_BIN}"

    printf 'gpu_access=available\n' >> "${META}"

    "${GPU_BIN}" \
        --output "${CSV}" \
        --metadata "${META}" \
        --repeats 3

    GPU_RAN=1
else
    echo
    echo "[3/4] No accessible CUDA toolchain/device; skipping GPU timing. CPU results are valid."
    echo "gpu_access=unavailable_on_this_run" >> "${META}"
fi

echo
echo "[4/4] Building self-contained classroom webpage..."
python3 "${GENERATOR}" \
    --csv "${CSV}" \
    --metadata "${META}" \
    --output "${HTML}"

echo
echo "============================================================"
echo "READY FOR CLASS"
echo "============================================================"
echo "Results: ${CSV}"
echo "Hardware: ${META}"
echo "Website: ${HTML}"
echo

if (( GPU_RAN == 1 )); then
    echo "GPU data is included."
else
    echo "GPU data is not included from this run."
    echo "To collect real GPU data outside this sandbox:"
    echo "  bash week-06/scripts/12_collect_gpu_parallelism_showdown.sh"
fi

echo
echo "Open it with:"
echo "  xdg-open \"${HTML}\""
echo
