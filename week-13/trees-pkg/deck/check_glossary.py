#!/usr/bin/env python3
"""Small guard for the student glossary when the neighboring slice exists."""
from pathlib import Path
import sys

target = Path(__file__).resolve().parents[2] / "student" / "glossary.md"
if not target.exists():
    print("glossary check deferred: week-13/student/glossary.md is not present")
    raise SystemExit(0)
text = target.read_text(encoding="utf-8").lower()
terms = (
    "graph", "vertex", "directed edge", "dependency", "tree", "containment",
    "traversal", "preorder", "postorder", "breadth-first", "decision tree",
    "edge label", "assert",
)
missing = [term for term in terms if term not in text]
if missing:
    print("glossary missing terms:", ", ".join(missing))
    raise SystemExit(1)
print(f"glossary terms present: {len(terms)}")
