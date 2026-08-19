#!/usr/bin/env python3
"""Fast structural validation for the authored Fall 2026 Weeks 7–9 package."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "week-07": ["README.md", "student/tuesday-activity.md", "student/odyssey-checkpoint-1.md", "instructor/tuesday-run-of-show.md", "instructor/thursday-run-of-show.md"],
    "week-08": ["README.md", "student/tuesday-activity.md", "student/decision-gate.md", "instructor/tuesday-run-of-show.md", "instructor/thursday-run-of-show.md"],
    "week-09": ["README.md", "student/tuesday-activity.md", "student/decision-gate.md", "instructor/tuesday-run-of-show.md"],
}


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def main():
    errors = []
    for week, files in REQUIRED.items():
        for file in files:
            if not (ROOT / week / file).is_file():
                errors.append(f"missing {week}/{file}")
    if (ROOT / "week-09" / "instructor" / "thursday-run-of-show.md").exists():
        errors.append("Week 9 must not contain a Thursday run-of-show")
    week7 = read("week-07/README.md")
    if "Checkpoint 1" not in week7 or "separate ordinary Decision Gate" not in week7:
        errors.append("Week 7 must state that Checkpoint 1 replaces the Decision Gate")
    week8 = read("week-08/README.md")
    if "Show & Tell" not in week8 or "Decision Gate" not in week8:
        errors.append("Week 8 must retain Show & Tell and an ordinary Decision Gate")
    week9 = read("week-09/README.md") + read("week-09/instructor/tuesday-run-of-show.md")
    if "Fall Break" not in week9 or "no class" not in week9:
        errors.append("Week 9 must state the Fall Break/no-class exception")
    authored = "\n".join(read(f"{week}/{file}") for week, files in REQUIRED.items() for file in files)
    for token in ("SOURCE_PENDING", "TODO", "TBD", "{{"):
        if token in authored:
            errors.append(f"unresolved placeholder token: {token}")
    if errors:
        print("FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PASS: Weeks 7–9 package contract satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
