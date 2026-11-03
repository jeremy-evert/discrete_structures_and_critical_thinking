#!/usr/bin/env python3
"""Fail if the package glossary is missing a required plain-language term."""
from pathlib import Path
import re

target = Path(__file__).resolve().parents[1] / "student" / "glossary.md"
if not target.exists():
    print(f"glossary missing: {target}")
    raise SystemExit(1)

terms = (
    "graph", "vertex", "directed edge", "dependency", "tree", "containment",
    "traversal", "preorder", "postorder", "breadth-first", "decision tree",
    "edge label", "assert", "connected", "cycle", "descendant", "recursion",
    "recursively", "depth-first", "binary tree", "inorder", "trace", "audit",
    "conversion", "model", "claim", "test", "pytest", "set", "branch", "split",
    "route", "search", "language-access review", "discriminating evidence",
    "bounded conclusion", "network", "edge case", "counterexample",
)
entries = {
    match.group(1).strip().lower()
    for match in re.finditer(r"^\|\s*\*\*(.+?)\*\*\s*\|", target.read_text(encoding="utf-8"), re.M)
}
missing = [term for term in terms if term not in entries]
if missing:
    print("glossary missing terms:", ", ".join(missing))
    raise SystemExit(1)
print(f"glossary terms present: {len(terms)}")
