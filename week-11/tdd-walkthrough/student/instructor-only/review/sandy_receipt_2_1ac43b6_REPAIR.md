review_id: sandy-20261027-1ac43b6
role: Sandy the Skeptic (Sol, adversarial review)
input_refs:
  - HEAD: 1ac43b62b71760cfd2b02c33a107d85c0b4ff05b
  - prior receipt: sandy-20261027-d3a4e8b
  - week-11/tdd-walkthrough/student/
  - week-11/instructor/thursday-run-of-show.md
  - assignments/pair-reasoning-report.md
  - week-11/README.md
  - origin/anna/dsct-tdd-relations-20261027:week-11/tdd-walkthrough/STEPS.md
bounded_scope: Read-only re-review of the student workbook package, facilitator contract, starter, reference ladder, and stated repair commit.

attacks_or_checks_attempted:
  - Verified all three prior repairs in source and FACILITATOR.pdf.
  - Ran demo and starter checks.
  - Attempted ladder_check.sh and normal pytest.
  - Ran reference pytest with capture disabled.
  - Inspected all 19 tag subjects and tag diffs.
  - Rechecked workbook/glossary answer leaks, step mappings, contracts, Python compatibility, and sensitive-data/Canvas scans.
  - Parsed all reference Python files with Python AST.

commands_or_test_refs:
  - `bash instructor-only/ladder_check.sh` — blocked at `mktemp`
  - `bash instructor-only/check_demos.sh` — pass
  - `bash instructor-only/check_starter.sh` — pass
  - `python3 -I -m pytest -s -q -p no:cacheprovider instructor-only/reference` — 37 passed
  - `python3 -I -m pytest -s -q -p no:cacheprovider starter` — no tests ran, exit 5
  - `git tag --list 'student-ref-step-*'` — 19 tags found
  - `bash -n instructor-only/ladder_check.sh` — pass
  - Python AST parse of reference — pass
  - `pdftotext` checks of FACILITATOR.pdf and GLOSSARY.pdf

findings:
  - rank: 1
    severity: repair
    finding: The student glossary leaks the exact transitivity witness and states it inaccurately.
    reproduction: `GLOSSARY.md:31` and `GLOSSARY.pdf` give `200 s, 204 s, 208 s with a gap of 5`. WORKBOOK.md:356–395 says “YOU invent the witness,” “Do not ask Claude,” and explicitly says to avoid 204. The adjacent gaps are 4 and 4, not 5; only the end-to-end gap is 8.
    impact: This directly undermines the claim that the student authors the witness and contradicts the workbook instruction.
  - rank: 2
    severity: observation
    finding: The facilitator explicitly exposes unresolved Thursday-contract choices rather than silently hiding them.
    reproduction: FACILITATOR.md:13–16 and :67–78 call out the code-default/paper-path choice and the conflict between the README’s individual report and the retired assignment.
    impact: No new silent contract change found, but instructor action remains required.

verdict: REPAIR

reproduction_limits:
  - `ladder_check.sh` could not create `/tmp/tmp.*`: read-only filesystem; it exited 2 at `mktemp`.
  - Normal pytest capture could not create temporary files. Capture-disabled pytest ran successfully.
  - No clean-clone 19-tag execution was possible in this environment.
  - The worktree now contains an untracked `week-11/tdd-walkthrough/student/REPORT.md`; I did not modify it.

next_action: Remove or neutralize the exact witness and correct the “gap of 5” glossary wording in both Markdown and PDF, then rerun the ladder in a writable environment.