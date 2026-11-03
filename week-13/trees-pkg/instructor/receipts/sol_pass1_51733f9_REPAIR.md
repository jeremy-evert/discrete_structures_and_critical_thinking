# Sol receipt — Sandy

- `review_id`: `sol-dsct-w13-trees-51733f9-20261103`
- `role`: Sol / adversarial review
- `input_refs`: package at commit `51733f9`; contract; Terra plan §2; `lunaA.md`, `lunaB.md`, `lunaB2.md`, `lunaC.md`; Luna outputs.
- `bounded_scope`: `week-13/trees-pkg/`; no Canvas, network, commits, or tracked-file edits.
- `terminal_state`: `COMPLETE`
- `verdict`: `REPAIR`

## Attacks and results

1. Fresh clone and tests:

```text
git clone --branch ivy/dsct-w13-trees-20261103 <worktree> /tmp/.../fresh
cd week-13/trees-pkg/code && python3 -m pytest -q
```

Result: `8 passed, 1 xfailed`.

Mutations in disposable copies all failed as required:

- swapped child order: 2 failures
- changed BFS queue pop to stack pop: 2 failures
- removed `requirements -> tests`: 3 failures, including strict-xfail XPASS

2. Slide traces:

```text
pdftotext -layout deck/trees_slides.pdf /tmp/slides.txt
```

All six independent traces matched:

- project preorder
- project postorder
- project breadth-first
- decision-tree preorder
- decision-tree postorder
- decision-tree breadth-first

Content claims also checked directly: six tree edges, dropped `requirements -> tests`, and project last in postorder are correct.

3. Deck checks/builds:

```text
./check_prompts.sh
./build.sh
./build.sh
```

Result: both PDFs had 48 pages; zero overfull/error and missing-character lines. `check_prompts.sh` exited 0 but reported `glossary check deferred`.

4. Prompt-integrity mutation:

- Altered `deck/verbatim_txt/01_a.txt`: `check_prompts.sh` incorrectly exited 0.
- Altered `deck/traces.tex`: `check_prompts.sh` correctly exited 1.

The slide macro uses `verbatim_txt` (`deck/preamble.tex:17`), while the checker compares `prompts_txt` only. Four prompt copies visibly substitute curly quotes with TeX quote pairs. Students can paste a usable prompt from the slide, but not byte-identical source text; Canvas `prompts.md` is byte-exact.

5. Manifest validator:

Baseline exited 0. These disposable mutations all exited 1:

- instructor path: forbidden path
- one-byte prompt-page change: byte mismatch
- removed source: missing source
- duplicate title: duplicate titles

No notes PDF, instructor guide, report, or `code/` path is reachable from the manifest.

6. Student/package checks:

- decision gate byte comparison: success
- fleet-host matches: 0
- secret literal matches: 0
- instructor/code links: 0
- answer-key trace leakage: 0
- notes-only phrase found in notes PDF, absent from slides PDF
- `pdftotext -bbox`: 0 boundary violations in both PDFs

The required AI failure mode appears in prompt 05.

## Findings

### HIGH — required `REPORT.md` is missing

The contract requires `instructor/REPORT.md` with commands, results, judgment calls, tip SHA, unfinished work, and terminal state ([contract](</mnt/nora/git/worktrees/fi-dsct-coverage/docs/DSCT_WEEK_PACKAGE_CONTRACT.md:52>)). The package contains only `INSTRUCTOR_GUIDE.md`.

Repair: add the required report with real verification evidence.

### HIGH — slide prompt drift is not detected

`check_prompts.sh` validates `prompts_txt`, but the deck renders `verbatim_txt`. A deliberate edit to the actual slide prompt passed validation.

Repair: make the checker validate the rendered prompt source, or render directly from canonical prompt bytes with a checked, deterministic TeX transformation.

### MEDIUM — glossary validation checks the wrong path

`check_glossary.py:6` resolves `week-13/student/glossary.md`, not `week-13/trees-pkg/student/glossary.md`. Removing a required glossary term still produced exit 0 with “glossary check deferred.”

Repair: point the checker at the package glossary and fail when it is missing or incomplete.

### MEDIUM — peer-visibility instruction is absent

Student pages contain no instruction that graded work is visible to peers or that reading peer work is part of the assignment, contrary to the course rule ([COURSE_DESIGN_RULES.md](</mnt/nora/git/jeremy_task_tracking/COURSE_DESIGN_RULES.md:104>)).

Repair: add the required peer-visibility wording to the student submission instructions, preserving the canonical Decision Gate byte-equality rule.

The core algorithms, traces, content claims, manifest validation, student safety checks, notes isolation, and layout checks survived.