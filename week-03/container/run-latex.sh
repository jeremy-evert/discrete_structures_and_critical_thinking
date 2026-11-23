#!/usr/bin/env bash
# DSCT Week 3 pinned-container LaTeX runner.
#
# Usage:
#   ./run-latex.sh path/to/source.tex
#
# What this wrapper hides (safely, per Prompt 316's contract):
#   - the exact latexmk engine flags;
#   - the container runtime invocation syntax (podman run with --mount);
#   - the working-directory/output-directory plumbing inside the container.
#
# What this wrapper always shows the student (per Prompt 316's contract):
#   - which image is being used, and whether it is pinned;
#   - which host directory is mounted, and at what container path;
#   - where the output PDF is expected to land;
#   - whether the run succeeded or failed, and where to look on failure.
#
# Pinning: the default image reference below is the course-supplied pinned
# reference (see IMAGE_CONTRACT.md). Set DSCT_WEEK3_IMAGE to override for
# local testing only; the banner always reports which reference was actually
# used so a student or grader can tell if they drifted off the pinned path.
set -u

DEFAULT_IMAGE_REF="ghcr.io/jeremy-evert/dsct-week3-latex@sha256:e7987919298c909f1a7f52247b8a7b54395cbde2400e2d6f3e8c5078425e2fca"
IMAGE_REF="${DSCT_WEEK3_IMAGE:-$DEFAULT_IMAGE_REF}"
RUNTIME="${DSCT_WEEK3_RUNTIME:-podman}"

fail() {
    echo "RESULT: FAIL"
    echo "REASON: $1"
    exit "${2:-1}"
}

if [ "$#" -ne 1 ]; then
    fail "usage: $0 path/to/source.tex" 64
fi

src_arg="$1"

if [ ! -f "$src_arg" ]; then
    fail "source not found: $src_arg (checked relative to $(pwd))" 66
fi

src_dir="$(cd "$(dirname "$src_arg")" && pwd)"
src_name="$(basename "$src_arg")"
pdf_name="${src_name%.tex}.pdf"

echo "IMAGE: $IMAGE_REF"
echo "RUNTIME: $RUNTIME"
echo "HOST_SOURCE_DIR: $src_dir"
echo "CONTAINER_WORK_DIR: /work"
echo "SOURCE: $src_name"
echo "EXPECTED_PDF: $src_dir/$pdf_name"

"$RUNTIME" run --rm \
    --pull=never \
    --userns=keep-id \
    --mount "type=bind,source=${src_dir},target=/work,relabel=private" \
    --workdir /work \
    "$IMAGE_REF" \
    latexmk -pdf -interaction=nonstopmode -halt-on-error "$src_name"
status=$?

if [ "$status" -ne 0 ]; then
    case "$status" in
        125|127)
            fail "container/runtime invocation error (exit $status) before compilation started -- check the IMAGE/RUNTIME lines above, not the LaTeX source" "$status"
            ;;
        *)
            fail "latexmk exited $status; inspect ${src_dir}/${src_name%.tex}.log for the LaTeX error" "$status"
            ;;
    esac
fi

if [ ! -f "${src_dir}/${pdf_name}" ]; then
    fail "latexmk reported success but ${pdf_name} was not found at ${src_dir}" 65
fi

echo "RESULT: PASS"
echo "PDF: ${src_dir}/${pdf_name}"
exit 0
