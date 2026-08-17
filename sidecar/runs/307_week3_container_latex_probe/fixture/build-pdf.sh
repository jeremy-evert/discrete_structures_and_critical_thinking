#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  printf 'usage: %s path/to/source.tex\n' "$0" >&2
  exit 64
fi

source_tex=$1
if [[ ! -f "$source_tex" ]]; then
  printf 'source not found: %s\n' "$source_tex" >&2
  exit 66
fi

source_dir=$(cd "$(dirname "$source_tex")" && pwd)
source_name=$(basename "$source_tex")
pdflatex -interaction=nonstopmode -halt-on-error -output-directory "$source_dir" "$source_name"
printf 'PDF: %s/%s\n' "$source_dir" "${source_name%.tex}.pdf"
