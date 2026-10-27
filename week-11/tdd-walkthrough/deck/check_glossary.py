#!/usr/bin/env python3
"""Fail if a jargon term used on the slides is not defined on a Glossary slide."""
import re, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
gl = re.search(r"(\\begin\{frame\}\{Glossary 1.*)", (here / "part0.tex").read_text(), re.S).group(1).lower()
gl = gl.replace("\\textbf{", "").replace("\\_", "_")
watch = ["unit test", "pytest", "assert", "red", "green", "fixture", "stub", "partition", "bin", "boundary", "witness",
         "counterexample", "relation", "ordered pair", "reflexive", "symmetric", "antisymmetric", "transitive",
         "equivalence relation", "partial order", "property test", "canonical key", "union-find", "edit distance",
         "digraph", "matrix", "normalize", "leaf", "dependency", "cycle", "test-driven development", "property"]
body = ""
for p in ["part1", "part2", "part3", "part4"]:
    body += (here / f"{p}.tex").read_text().lower()
bad = [w for w in watch if re.search(r"(?<![a-z])" + re.escape(w), body) and w not in gl]
if bad:
    print("terms used but missing from glossary:", bad); sys.exit(1)
print("glossary complete for", len(watch), "watched terms")
