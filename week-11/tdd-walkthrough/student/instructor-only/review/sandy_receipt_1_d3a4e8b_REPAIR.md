review_id: sandy-20261027-d3a4e8b
role: Sandy the Skeptic (Sol, adversarial review)
input_refs:
  - HEAD: d3a4e8bd59349ce97684e797e6740342a94c7ff7
  - week-11/tdd-walkthrough/student/
  - week-11/instructor/thursday-run-of-show.md
  - assignments/pair-reasoning-report.md
  - week-11/README.md
  - origin/anna/dsct-tdd-relations-20261027:week-11/tdd-walkthrough/STEPS.md
bounded_scope: Read-only review of the stated Thursday student workbook package and instructor reference ladder.

attacks_or_checks_attempted:
  - Ran all three instructor-only check scripts.
  - Inspected all 19 reference tags and commit subjects.
  - Reviewed workbook, glossary, facilitator page, starter, contracts, and Tuesday mapping.
  - Scanned for answer leaks, student data, Canvas integration, and Python-version hazards.
  - Inspected reference implementation and tests.

commands_or_test_refs:
  - `bash instructor-only/ladder_check.sh`
  - `bash instructor-only/check_demos.sh`
  - `bash instructor-only/check_starter.sh`
  - `git tag --list 'student-ref-step-*'`
  - `python3 -I -m pytest -q -p no:cacheprovider` on reference and starter
  - `pdftotext` spot checks of generated PDFs
  - `rg` scans for sensitive data and Canvas references

findings:
  - rank: 1
    severity: repair
    finding: FACILITATOR submission instructions use stale step numbers.
    reproduction: `week-11/tdd-walkthrough/student/FACILITATOR.md:67` says “red-at-Step-6 and green-at-Step-7”; the workbook correctly defines red at Step 07 and green at Step 08 (`WORKBOOK.md:391,645`). The same stale wording is present in `FACILITATOR.pdf`.
    impact: A facilitator or pair could collect the wrong evidence and contradict the workbook’s central transitivity sequence.
  - rank: 2
    severity: repair
    finding: The facilitator’s timing-change explanation is internally inaccurate.
    reproduction: `FACILITATOR.md:14` says the original 1:12–1:25 model-limit block shrinks to 3 minutes, but the replacement schedule uses 1:40–1:45, which is 5 minutes and is not the same clock position.
    impact: The existing Thursday contract is explicitly discussed, but the timing mapping is misleading.
  - rank: 3
    severity: repair
    finding: `ladder_check.sh` can report success after clone/setup failure.
    reproduction: In this read-only environment, `mktemp` and `git clone` failed; the script still exited 0 because `bad` remains 0 and no post-clone validation exists.
    impact: A failed clean-clone verification can be mistaken for a passing ladder check. Add explicit failure handling for `mktemp`, clone, checkout, and empty tag discovery.
  - rank: 4
    severity: observation
    finding: The workbook reveals several expected answers.
    reproduction: `WORKBOOK.md:180` gives the Step 02 property pattern, `:211` gives all Step 03 verdicts, and `:150` gives Step 01 output shape.
    impact: These are substantial scaffolds, but the exact Step 07 transitivity witness is not supplied; students still author the three lengths. I found no instructor reference code embedded in WORKBOOK or GLOSSARY.
  - rank: 5
    severity: clear
    finding: No real student data or Canvas workflow was found.
    reproduction: Student-facing materials state made-up data; the scan found no names, emails, recordings, or Canvas API/content. “Canvas?” appears only as a planning note in an instructor dry-run log.

verdict: REPAIR

reproduction_limits:
  - The clean-clone ladder could not execute because the filesystem is read-only and denies `/tmp` and `/clone`.
  - Direct pytest execution was likewise blocked by Python temporary-file creation.
  - Static inspection confirms all 19 tags and their RED/GREEN subjects, but does not substitute for a successful clean-clone run.

next_action: Correct the FACILITATOR.md/PDF Step 06/07 evidence wording and timing note, harden ladder_check.sh failure handling, then rerun all three checks in a writable clean-clone environment.