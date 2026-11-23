#!/usr/bin/env python3
"""Falsifiable DSCT source-completion check for Fall 2026."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(path: str):
    if not (ROOT / path).is_file():
        ERRORS.append(f"missing local source: {path}")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    for week in range(1, 18):
        if week == 3:
            required = [
                "week-03/student/container-latex-skill-ladder.md",
                "week-03/instructor/container-latex-instructor-notes.md",
            ]
        elif week == 16:
            required = [
                "week-16/README.md",
                "week-16/student/farkle-evidence-lab.md",
                "week-16/instructor/guide.md",
            ]
        elif week == 15:
            required = ["week-15/README.md", "week-15/instructor/asynchronous-buffer-note.md"]
        elif week == 17:
            required = [
                "week-17/README.md",
                "week-17/instructor/final-reflection-run-of-show.md",
                "assignments/week-17-final-individual-reflection.md",
                "assignments/week-17-final-individual-reflection-rubric.md",
            ]
        elif week in (13, 14):
            required = [
                f"week-{week:02d}/README.md",
                f"week-{week:02d}/student/tuesday-activity.md",
                f"week-{week:02d}/instructor/guide.md",
            ]
        else:
            required = [
                f"week-{week:02d}/README.md",
                f"week-{week:02d}/student/tuesday-activity.md",
                f"week-{week:02d}/instructor/tuesday-run-of-show.md",
            ]
        for path in required:
            require(path)

    formal = {
        4: ("Show & Tell", "ordinary Decision Gate"),
        5: ("Pair Reasoning", "ordinary Decision Gate"),
        6: ("Show & Tell", "ordinary Decision Gate"),
        7: ("Pair Reasoning", "Checkpoint 1"),
        8: ("Show & Tell", "ordinary Decision Gate"),
        9: ("Tuesday-only", "Decision Gate"),
        10: ("Show & Tell", "ordinary Decision Gate"),
        11: ("Pair Reasoning", "Checkpoint 2"),
        12: ("Show & Tell", "ordinary Decision Gate"),
        13: ("Pair Reasoning", "ordinary Decision Gate"),
        14: ("Show & Tell", "Checkpoint 3"),
    }
    for week, (mode, evidence) in formal.items():
        body = "\n".join(
            p.read_text(encoding="utf-8")
            for p in (ROOT / f"week-{week:02d}").rglob("*.md")
        )
        if mode not in body:
            ERRORS.append(f"Week {week}: missing cadence marker {mode!r}")
        if evidence == "ordinary Decision Gate":
            if "Decision Gate" not in body:
                ERRORS.append(f"Week {week}: missing ordinary Decision Gate evidence path")
        elif evidence not in body:
            ERRORS.append(f"Week {week}: missing evidence marker {evidence!r}")
        if re.search(r"SOURCE_PENDING|CONTRACTED_NOT_AUTHORED|TODO|TBD|FIXME|\[INSERT", body, re.I):
            ERRORS.append(f"Week {week}: unresolved source placeholder/status token")

    week9 = text("week-09/README.md")
    if (ROOT / "week-09/instructor/thursday-run-of-show.md").exists():
        ERRORS.append("Week 9 must not have a Thursday run-of-show")
    if "Oct 15" not in week9 and "October 15" not in week9:
        ERRORS.append("Week 9 must name the October 15 Fall Break")

    week15 = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "week-15").rglob("*.md"))
    if re.search(r"(?m)^\s*(?:Required|Submit|Due date|Class meeting|Formal topic)\s*:", week15, re.I):
        ERRORS.append("Week 15 invents a prohibited topic, obligation, due date, or meeting")

    week16 = text("week-16/README.md")
    if "Farkle" not in week16 or "Machine Learning" not in week16:
        ERRORS.append("Week 16 Farkle + ML package is not visible")
    if "Decision Gate" in week16 and "not" not in week16:
        ERRORS.append("Week 16 may be duplicating a Decision Gate")

    week17 = text("week-17/README.md")
    if "5%" not in week17 or "reflection" not in week17.lower():
        ERRORS.append("Week 17 final 5% reflection is not visible")
    if re.search(r"(?m)^\s*(?:Comprehensive exam|Programming exam|Reasoning Defense)\s*:", week17, re.I):
        ERRORS.append("Week 17 introduces a prohibited exam/final")

    weights = [int(n) for n in re.findall(r"\|\s*(\d+)%\s*\|", text("docs/grading-model.md"))]
    if sum(weights) != 100:
        ERRORS.append(f"grading weights sum to {sum(weights)}, expected 100")
    spine = text("planning/fall-2026-spine.md")
    if not all(re.search(rf"\|\s*{week}\s*\|.*Checkpoint", spine) for week in (7, 11, 14)):
        ERRORS.append("checkpoint weeks are not visible in the spine")
    for week in (7, 11, 14):
        body = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / f"week-{week:02d}").rglob("*.md"))
        if "Checkpoint" not in body or "ordinary Decision Gate" not in body:
            ERRORS.append(f"Week {week}: checkpoint replacement language is incomplete")

    # Local markdown references in newly authored week packages must resolve.
    for path in [p for week in list(range(4, 15)) + [15, 17] for p in (ROOT / f"week-{week:02d}").rglob("*.md")]:
        for ref in re.findall(r"\]\(([^)#]+)", path.read_text(encoding="utf-8")):
            if ref.startswith(("http://", "https://", "mailto:")):
                continue
            target = (path.parent / ref).resolve()
            if not target.is_file():
                ERRORS.append(f"broken local reference: {path.relative_to(ROOT)} -> {ref}")

    if ERRORS:
        print("FAIL")
        print("\n".join(f"- {error}" for error in ERRORS))
        return 1
    print("PASS: Fall 2026 DSCT source package contract satisfied")
    print("PASS: intentional Weeks 1–17 source states, formal cadence, special weeks, weights, and local links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
