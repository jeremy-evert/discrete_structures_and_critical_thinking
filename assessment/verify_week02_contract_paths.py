#!/usr/bin/env python3
"""Acceptance check for Prompt 305: DSCT Week 2 assessment contract path reconciliation.

Falsifiable check (per prompts/305_week2_assessment_contract_reconciliation.md):
every file path referenced by the ported YAML contract (submission_path,
recurring_method.source.path, course_extension repository/path, plus the
source_assignment path and every assessment/week-02-approved-materials.yaml
entry for good measure) must resolve to a real file at the commit this work
lands on.

`submission_path` is a special case: it names the file a student will
*create and submit* (`local-ai-readiness.md`), so it cannot pre-exist as a
repo file before any student has done the assignment. For that one field the
check instead asserts it is a bare filename (no path traversal) and that the
exact filename is referenced by the contract's own `source_assignment`
document, so the value is not an orphaned/invented string.

All other paths are checked for real existence on disk:
- paths whose `repository` is this repo (discrete_structures_and_critical_thinking)
  are checked relative to this repo's root.
- paths whose `repository` is a different course repo (local_ai_lab_setup,
  windows_classroom, ...) are checked relative to a sibling checkout at
  ../<repository> next to this repo's root, which is how this machine's
  course repos are laid out.

Run: python3 assessment/verify_week02_contract_paths.py
Exits 0 and prints PASS lines on success; exits 1 and prints FAIL lines
(without raising) on any unresolved path.
"""
import sys
from pathlib import Path

import yaml

REPO_NAME = "discrete_structures_and_critical_thinking"
REPO_ROOT = Path(__file__).resolve().parent.parent
SIBLINGS_ROOT = REPO_ROOT.parent

CONTRACT_PATH = REPO_ROOT / "assessment" / "week-02-readiness-assessment-contract.yaml"
MATERIALS_PATH = REPO_ROOT / "assessment" / "week-02-approved-materials.yaml"

failures = []
passes = []


def resolve_repo_path(repository: str, rel_path: str) -> Path:
    if repository == REPO_NAME:
        return REPO_ROOT / rel_path
    return SIBLINGS_ROOT / repository / rel_path


def check(label: str, path: Path):
    if path.is_file():
        passes.append(f"PASS: {label} -> {path}")
    else:
        failures.append(f"FAIL: {label} -> {path} (does not exist)")


def main():
    contract = yaml.safe_load(CONTRACT_PATH.read_text())
    materials = yaml.safe_load(MATERIALS_PATH.read_text())

    assignment = contract["assignment"]

    # submission_path: special-cased, see module docstring.
    submission_path = assignment["submission_path"]
    if "/" in submission_path or ".." in submission_path:
        failures.append(
            f"FAIL: assignment.submission_path is not a bare filename -> {submission_path}"
        )
    else:
        source_assignment = assignment["source_assignment"]
        source_doc = resolve_repo_path(
            source_assignment["repository"], source_assignment["path"]
        )
        if source_doc.is_file() and submission_path in source_doc.read_text():
            passes.append(
                f"PASS: assignment.submission_path '{submission_path}' is a bare "
                f"filename referenced by {source_doc}"
            )
        else:
            failures.append(
                f"FAIL: assignment.submission_path '{submission_path}' not found "
                f"referenced in {source_doc}"
            )

    check(
        "assignment.source_assignment.path",
        resolve_repo_path(
            assignment["source_assignment"]["repository"],
            assignment["source_assignment"]["path"],
        ),
    )
    check(
        "assignment.course_extension.path",
        resolve_repo_path(
            assignment["course_extension"]["repository"],
            assignment["course_extension"]["path"],
        ),
    )
    check(
        "assignment.recurring_method.source.path",
        resolve_repo_path(
            assignment["recurring_method"]["source"]["repository"],
            assignment["recurring_method"]["source"]["path"],
        ),
    )

    for entry in materials["entries"]:
        check(
            f"approved-materials[{entry['citation_id']}].path",
            resolve_repo_path(entry["repository"], entry["path"]),
        )

    for line in passes:
        print(line)
    for line in failures:
        print(line)

    print(f"\n{len(passes)} passed, {len(failures)} failed")
    if failures:
        sys.exit(1)
    print("ALL PATHS RESOLVED.")


if __name__ == "__main__":
    main()
