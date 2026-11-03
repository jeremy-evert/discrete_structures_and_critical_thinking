# Luna receipt — slices 4 and 5

Date: 2026-11-03  
Worktree: `<worktree>`
Branch: `ivy/dsct-w16-farkle-ml-20261103`  
Base HEAD preserved: `3a633af12742bf238a2f3af365d3916c97a19de0`

## Commands run and exact results

The sandbox command wrapper printed `Failed to create stream fd: Operation not permitted` three times before several processes. Those wrapper diagnostics did not change the command exit status; the command output and statuses below are the package results.

### Manifest validator

Command, from `week-16/farkle-ml-pkg/`:

```text
python3 canvas/validate_manifest.py
```

Output:

```text
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
glossary coverage: OK (47 checked terms; terms present in handout checked)
forbidden-string scan: clean (16 student-facing markdown files)
VALIDATION OK
```

Exit: `0`.

### Instructor code tests

Command, from `week-16/farkle-ml-pkg/code/`:

```text
pytest
```

Output:

```text
.....                                                                    [100%]
5 passed in 0.01s
```

Exit: `0`.

The first test attempt exposed only a binary-floating-point exact-equality assertion for +20/+60 percentage points; the implementation was normalized to ten decimal places and the test was rerun successfully. No intentionally red test remains.

### Fresh-copy test

Command:

```text
tmpdir=$(mktemp -d /tmp/farkle-ml-code-test.XXXXXX); cp -a week-16/farkle-ml-pkg/code "$tmpdir/code"; cd "$tmpdir/code"; echo "fresh copy: $tmpdir/code"; pytest
```

Output:

```text
fresh copy: /tmp/farkle-ml-code-test.vxnWt2/code
.....                                                                    [100%]
5 passed in 0.01s
```

Exit: `0`. The copied directory remains available at that temporary path as the clean-clone-like test artifact.

### Prompt/deck consistency check

Command, from `week-16/farkle-ml-pkg/deck/`:

```text
./check_prompts.sh
```

Output:

```text
index consistent: 13 rows, 16 content slides
numbers consistent: CSV-derived macros and tables match
prompt boxes checked: 4
```

Exit: `0`.

### Evidence-reader CLI

Command, from `week-16/farkle-ml-pkg/code/`:

```text
python3 evidence_summary.py fixtures/quick_v1_results.csv
```

The command returned exit `0` and reported:

```text
"max_difference_pp": 60.0
"min_difference_pp": -40.0
"range_pp": 100.0
"sign_flip_detected": true
```

Its three rows reported ordering signs `-1`, `1`, and `1`, with recomputed win rates `0.3/0.7`, `0.6/0.4`, and `0.8/0.2`.

### Scope and byte checks

Command:

```text
set -e
cmp week-16/farkle-ml-pkg/student/thursday_activity.md week-16/farkle-ml-pkg/canvas/thursday_activity.md
cmp week-16/farkle-ml-pkg/student/recap_outline.md week-16/farkle-ml-pkg/canvas/recap_outline.md
cmp week-16/farkle-ml-pkg/student/glossary.md week-16/farkle-ml-pkg/canvas/glossary.md
cmp week-16/fallback/quick_v1_results.csv week-16/farkle-ml-pkg/code/fixtures/quick_v1_results.csv
python3 -m json.tool week-16/farkle-ml-pkg/canvas/manifest.json >/dev/null
python3 -m py_compile week-16/farkle-ml-pkg/code/evidence_summary.py week-16/farkle-ml-pkg/code/test_evidence_summary.py
test ! -e week-16/farkle-ml-pkg/student/decision-gate.md
```

Output: no output; exit `0`.

The recap count check also returned:

```text
recap bullets: Tuesday=5 Thursday=5
```

`git diff --check` returned no output and exit `0`.

## Files created

Student-facing:

- `student/thursday_activity.md`
- `student/recap_outline.md`

Canvas copies and manifest support:

- `.gitignore` — ignored the generated `code/.pytest_cache/` directory.
- `canvas/thursday_activity.md`
- `canvas/recap_outline.md`
- `canvas/manifest.json` — added the two Thursday pages.
- `canvas/validate_manifest.py` — added required-page and byte-copy checks.
- `student/glossary.md` and `canvas/glossary.md` — added `Threshold` and `Deterministic` entries; the copies match.

Instructor-only:

- `instructor/INSTRUCTOR_GUIDE.md`
- `instructor/RUN_OF_SHOW.md`
- `instructor/LUNA_RECEIPT_4_5.md`

Code and tests:

- `code/evidence_summary.py`
- `code/test_evidence_summary.py`
- `code/pytest.ini`
- `code/README.md`
- `code/fixtures/quick_v1_results.csv` — byte-identical copy of the fallback CSV.

## Not done / boundaries respected

- No `git add`, commit, fetch, push, merge, or branch/worktree deletion was performed; the work remains an uncommitted work artifact on the coordinator branch at the preserved base HEAD.
- No Canvas contact, upload, or deployment was performed.
- No PDF rebuild was performed because no deck source changed. The existing Tectonic build path is documented in `INSTRUCTOR_GUIDE.md`.
- No `instructor/REPORT.md` was written; the coordinator owns that report.
- No `student/decision-gate.md` was written or copied.
- No vendor files, root README, original assignment receipt, deck sources, or prompt sources were modified.
- No live Farkle runner, GPU, cloud service, paid service, or student data was used. The code tests and evidence summary use only the synthetic fallback fixture.
