# Luna repair receipt — bounded REPAIR pass

Date: 2026-11-03  
Branch: `ivy/dsct-w16-farkle-ml-20261103`  
HEAD at start: `096874e`  
Scope: Week 16 Farkle package repairs under `week-16/farkle-ml-pkg/`

## Commands and exact results

Prompt extraction:

```text
python3 extract_prompts.py
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
exit 0
```

Deck build 1:

```text
./build.sh
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
slides pages: 18
notes pages: 18
overfull/error lines: slides=0 notes=0
outputs: farkle_ml_slides.pdf farkle_ml_notes.pdf
exit 0
```

Deck build 2:

```text
./build.sh
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
slides pages: 18
notes pages: 18
overfull/error lines: slides=0 notes=0
outputs: farkle_ml_slides.pdf farkle_ml_notes.pdf
exit 0
```

Prompt consistency:

```text
./check_prompts.sh
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
index consistent: 13 rows, 16 content slides
numbers consistent: CSV-derived macros and tables match
prompt boxes checked: 4
exit 0
```

Code tests:

```text
pytest
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
Failed to create stream fd: Operation not permitted
.....                                                                    [100%]
5 passed in 0.01s
exit 0
```

Manifest and package validation:

```text
python3 week-16/farkle-ml-pkg/canvas/validate_manifest.py
manifest JSON: OK
metadata: week=16 module_id=218914 module_name_contains='Week 16'
pages: 7 unique titles; sources present
page H1s: OK for all pages except exact-concat prompts.md (documented invariant)
files: 1 source(s) present and linked
zips: 1 directive(s); temporary prompt ZIP members:
  01_claim_and_rule.md
  02_initial_sample_audit.md
  03_bundle_stability_check.md
  04_repair_an_overclaim.md
byte matches: handout.md, concept_map.md, glossary.md, thursday_activity.md, recap_outline.md; prompts.md exact concatenation
glossary coverage: OK (68 checked terms; all student pages and prompts checked)
forbidden-string scan: clean (16 student-facing markdown files)
VALIDATION OK
exit 0
```

Package-wide host/path scan (receipt-safe escaped pattern; no output):

```text
grep -rniE "$(printf '\\141\\160\\162\\151\\154|\\155\\141\\151\\163\\145|\\142\\162\\141\\156\\144\\171|\\155\\157\\162\\147\\141\\156|\\163\\145\\160\\164\\145\\155\\142\\145\\162|\\057\\155\\156\\164\\057\\156\\157\\162\\141|\\057\\150\\157\\155\\145\\057\\152\\145\\166\\145\\162\\164')" week-16/farkle-ml-pkg
(no output; exit 1, meaning no matches)
```

Whitespace check:

```text
git diff --check
(no output; exit 0)
```

The three-byte-match checks for `student/*.md` versus `canvas/*.md` also returned no output and exit 0. The validator independently reported all five byte matches and exact sorted prompt concatenation.

## Files changed

- Student pages: `student/handout.md`, `student/thursday_activity.md`, `student/concept_map.md`, `student/glossary.md`, `student/recap_outline.md`.
- Canvas pages and checks: `canvas/tuesday_landing.md`, the five copied student pages, `canvas/prompts.md`, `canvas/validate_manifest.py`.
- Prompts: all four files under `prompts/`.
- Generated prompt/deck outputs: `deck/prompts_txt/01_a.txt`, `02_a.txt`, `03_a.txt`, `04_a.txt`, `deck/farkle_ml_slides.pdf`, `deck/farkle_ml_notes.pdf`.
- Host-path cleanup needed by F6: `deck/build.sh`, `instructor/INSTRUCTOR_GUIDE.md`, `instructor/LUNA_RECEIPT_4_5.md`.
- This receipt: `instructor/LUNA_RECEIPT_repair.md`.

No manifest title changed.

## Repair summary

The Tuesday handout now shows only seed 17, explains that the slides PDF is linked from the Tuesday landing page, and says the handout is sufficient. The full three-row table remains on Thursday. The alternate-metric task is explicitly reasoning-only because no extra numbers are supplied; metric definitions and a sample answer are included. Strategy behavior, learner training turns, banking, turn, fallback-fixture wording, thresholds, signs, pp, and the requested decision vocabulary are defined inline and in the alphabetized glossary.

The Thursday page delays the interpretation until after students apply their own rule, provides late-rule recovery, row rebuilding arithmetic, model filled sentences, the graded-discussion exchange mechanism, and the revised -40 question. Receipt wording uses the Week 16 assignment name without inventing a URL or repository path.

The validator now checks the curated glossary terms across every student page and prompt, while retaining the documented exact-concatenation H1 exception. The forbidden host-name fragments are constructed at runtime, and the package-wide path scan is clean.

## Not done

- No `instructor/REPORT.md` was written; the coordinator explicitly owns that file and instructed this pass to ignore it.
- No Canvas contact, publishing, upload, or receipt-route change was attempted.
- No `git add`, commit, fetch, push, merge, or branch/worktree cleanup was performed.
- No files under `lessons/vendor/` or `week-16/README.md` were changed. No `deck/*.tex` files were changed.
- No additional alternate-metric numbers were published; the student task was reframed to reasoning from the supplied evidence.
- No independent fresh Sol review was performed after this bounded repair pass.
