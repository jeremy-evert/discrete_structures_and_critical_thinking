# Luna receipt — Tuesday deck + prompts

Date: 2026-11-03  
Worktree: `ivy/dsct-w16-farkle-ml-20261103`  
Scope: approved slice 1 only, under `week-16/farkle-ml-pkg/`

## Commands run and exact results

The supplied plan path existed but was empty (`0` bytes). I followed the
explicit coordinator decisions in the request, the package contract, and the
source materials.

Python syntax check:

```text
python3 -m py_compile week-16/farkle-ml-pkg/deck/extract_prompts.py week-16/farkle-ml-pkg/deck/gen_index.py week-16/farkle-ml-pkg/deck/scripts/make_numbers.py
```

No output; exit `0`.

CSV-derived number generation:

```text
week-16/farkle-ml-pkg/deck/scripts/make_numbers.py
wrote numbers.tex and 2 CSV-derived tables
```

Prompt extraction/index generation:

```text
cd week-16/farkle-ml-pkg/deck && python3 extract_prompts.py && python3 gen_index.py && python3 gen_index.py --list-prompts
wrote index_rows.tex: 13 rows over 2 frames; content slides 16
01 a
02 a
03 a
04 a
```

Initial diagnostic build, before tightening prompt-slide layout:

```text
week-16/farkle-ml-pkg/deck/build.sh
slides pages: 18
notes pages: 18
overfull/error lines: slides=4 notes=4
outputs: farkle_ml_slides.pdf farkle_ml_notes.pdf
```

The four overfull vertical boxes were fixed with prompt-slide shrink settings.

Final build 1:

```text
week-16/farkle-ml-pkg/deck/build.sh
slides pages: 18
notes pages: 18
overfull/error lines: slides=0 notes=0
outputs: farkle_ml_slides.pdf farkle_ml_notes.pdf
```

Final build 2 plus prompt check:

```text
week-16/farkle-ml-pkg/deck/build.sh
slides pages: 18
notes pages: 18
overfull/error lines: slides=0 notes=0
outputs: farkle_ml_slides.pdf farkle_ml_notes.pdf
week-16/farkle-ml-pkg/deck/check_prompts.sh
index consistent: 13 rows, 16 content slides
numbers consistent: CSV-derived macros and tables match
prompt boxes checked: 4
```

PDF metadata and retained-log checks:

```text
pdfinfo week-16/farkle-ml-pkg/deck/farkle_ml_slides.pdf | rg '^(Pages|Page size):'
Pages:           18
Page size:       453.54 x 255.12 pts
pdfinfo week-16/farkle-ml-pkg/deck/farkle_ml_notes.pdf | rg '^(Pages|Page size):'
Pages:           18
Page size:       453.54 x 255.12 pts

week-16/farkle-ml-pkg/deck/farkle_ml.log: 0
week-16/farkle-ml-pkg/deck/farkle_ml_notes.log: 0
```

Raster spot-check:

```text
pdftoppm -png -r 110 -f 1 -l 1 -singlefile .../farkle_ml_slides.pdf .../.raster/slide-01
pdftoppm -png -r 110 -f 7 -l 7 -singlefile .../farkle_ml_slides.pdf .../.raster/slide-07
pdftoppm -png -r 110 -f 12 -l 12 -singlefile .../farkle_ml_slides.pdf .../.raster/slide-12
pdftoppm -png -r 110 -f 17 -l 17 -singlefile .../farkle_ml_slides.pdf .../.raster/slide-17
```

The four inspected pages showed no obvious overlap or cropped content. Raster
files are ignored build/inspection intermediates under `deck/.raster/`.

## Files created

- `deck/build.sh`, `check_prompts.sh`, `extract_prompts.py`, `gen_index.py`
- `deck/preamble.tex`, `farkle_ml.tex`, `part0.tex` through `part3.tex`
- `deck/scripts/make_numbers.py`
- CSV-derived `deck/numbers.tex`, `table_initial.tex`, and `table_bundle.tex`
- Generated `deck/index_rows.tex` and `deck/prompts_txt/` pipeline files
- `deck/farkle_ml_slides.pdf` and `deck/farkle_ml_notes.pdf`
- `deck/JUDGMENT_CALLS.md`
- `prompts/01_claim_and_rule.md`
- `prompts/02_initial_sample_audit.md`
- `prompts/03_bundle_stability_check.md`
- `prompts/04_repair_an_overclaim.md`
- Package/deck `.gitignore` rules for generated intermediates

All quoted evidence values come from `week-16/fallback/quick_v1_results.csv`
through `deck/scripts/make_numbers.py`; no numeric result was hand-entered in
the slides.

## Not done by design

- No `git add`, commit, push, fetch, or merge; the coordinator owns Git state.
- No Canvas access or publishing.
- No changes to `vendor/`, the receipt outside this deck receipt, README,
  Decision Gate text, or any path outside `week-16/farkle-ml-pkg/`.
- No student data, real host names, secrets, handout, Canvas manifest, code,
  Thursday page, or full-week package work.
- No `pytest` run: this approved slice contains no reference-code slice.

Status: verified Tuesday deck and prompt subset complete; coordinator review and
commit remain pending.
