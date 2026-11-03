# Sol receipt — Sandy, second pass

- `review_id`: `sol-dsct-w13-trees-24161b1-20261103`
- `role`: Sol / adversarial review
- `input_refs`: package at commit `24161b1`; `DSCT_WEEK_PACKAGE_CONTRACT.md`; Terra plan §2; `lunaA.md`, `lunaB.md`, `lunaB2.md`, `lunaC.md`, `lunaR.md`; `lunaA_out.md`, `lunaB2_out.md`, `lunaC_out.md`; prior `sol_out.md`
- `bounded_scope`: `week-13/trees-pkg/`; no Canvas, network, commits, or persistent tracked-file edits
- `terminal_state`: `COMPLETE`
- `verdict`: **REPAIR**

## Attacks and real results

1. Fresh clone and pytest

```text
git clone --branch ivy/dsct-w13-trees-20261103 <worktree> $TMPDIR/fresh
cd week-13/trees-pkg/code && python3 -m pytest -q
```

Result: `8 passed, 1 xfailed`.

2. Required code mutations

- Swap child order: exit `1`, 2 failures.
- Change BFS queue pop to stack pop: exit `1`, 2 failures.
- Remove `("requirements", "tests")`: exit `1`, 3 failures, including strict-XFAIL XPASS.

3. Independent slide traces

```text
pdftotext -layout deck/trees_slides.pdf /tmp/slides.txt
```

Independently derived traces all matched:

- project preorder
- project postorder
- project breadth-first
- decision-tree preorder
- decision-tree postorder
- decision-tree breadth-first

Content checks passed: seven graph edges, six tree edges, dropped `requirements -> tests`, and project last in postorder.

4. Deck checker mutations

```text
sed -i '1s/^/[MUTATED] /' deck/verbatim_txt/01_a.txt
./check_prompts.sh
```

Result: exit `1`.

```text
sed -i 's/project, plan, build/project, build, plan/' deck/traces.tex
./check_prompts.sh
```

Result: exit `1`.

Baseline `./check_prompts.sh`: exit `0`; 13 prompt blocks, 39 glossary terms, generated traces and layout valid.

5. Cached builds

```text
./build.sh
./build.sh
```

Both builds: slides `48` pages, notes `48` pages; overfull/error `0`; missing-character `0`.

6. Prompt identity

- `prompts_txt` and `verbatim_txt` are deterministically checked.
- 9/13 rendered prompt files are byte-equal.
- 4/13 differ only by TeX-safe curly-quote substitutions; prompts remain pasteable from slides.
- `canvas/prompts.md` is byte-exact with all source prompt files: `7926` bytes.

7. Manifest mutations

Baseline:

```text
python3 canvas/validate_manifest.py --write
python3 canvas/validate_manifest.py
```

Result: exit `0`; 9 pages, 1 file, 1 ZIP.

Each mutation exited `1`:

- instructor path added
- one byte appended to `canvas/prompts.md`
- `student/concept_map.md` removed
- duplicate manifest title

Manifest exposes no notes PDF, instructor guide, report, or `code/` path.

8. Student/content checks

- Decision Gate byte comparison: pass.
- Fleet names/secrets/instructor/code links: no matches.
- No exact answer traces leaked into student pages.
- AI failure mode appears in prompt 05.
- F1–F8 repairs are present and consistent.
- Notes-only phrases are absent from `trees_slides.pdf`.
- `pdftotext -bbox`: slides and notes each had zero boundary violations.
- Final Git status is clean; branch remains `ivy/dsct-w13-trees-20261103`.

## Findings

### HIGH — REPORT.md does not satisfy the required tip-SHA/terminal evidence

[REPORT.md:3](</mnt/nora/git/worktrees/dsct-w13-trees/week-13/trees-pkg/instructor/REPORT.md:3>) says:

> “Tip SHA: the commit that adds this file; read `git log -1`…”

It does not record the actual tip SHA `24161b1`, and it still says “COMPLETE pending Sol re-pass receipt.” The contract explicitly requires a report containing the tip SHA and terminal state.

Repair: update `REPORT.md` with `Tip SHA: 24161b1`, record this second-pass review as `REPAIR`, and rerun the package checks after that documentation-only change.

## Reproduction limits

No Canvas or network state was inspected. The build temporarily rewrote the two tracked PDFs; their exact HEAD blobs were restored, and the worktree is clean. No independent subagent review was claimed.

## Next action

Repair the report metadata/evidence, then perform the required fresh Sol pass.