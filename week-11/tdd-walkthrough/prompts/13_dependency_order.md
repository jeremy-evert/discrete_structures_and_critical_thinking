# 13 — Partial order: what depends on what, and which to test first

**Why:** "depends on" is a partial order. Test the functions nothing else needs first. The tool reads our own code to draw the graph.
**Slide:** Part 3, "Piece 7: depends-on order" (then the digraph slide). **Principle:** partial-order test ordering.
**Recovery:** red = `tools/recover.sh 16`; green = `tools/recover.sh 17`.

```prompt-a
Test first. Stub merger/deps.py: build_graph(*modules) and leaves_first(graph), both raising
NotImplementedError. build_graph maps each top-level function name in the given modules to the
set of OTHER top-level functions (from those modules) it calls by plain name.
Write tests/test_dependencies.py for modules merger.names, merger.records, merger.pipeline:
(1) graph["merge_duplicates"] == {"group_records","merge_group"}, graph["group_records"] ==
{"duplicate_key"}, graph["duplicate_key"] == {"canonical_key"}, graph["canonical_key"] ==
{"_split"}, graph["_split"] == set(); (2) leaves_first(graph) lists every function after
everything it depends on, and its first item depends on nothing; (3) the transitive closure of
"depends on" has no function depending on itself and is antisymmetric and transitive (helpers).
Run pytest, show it red, stop.
```

```prompt-b
Implement build_graph with the ast module (parse the source with inspect.getsource; look at
ast.Call nodes whose func is a Name) and leaves_first with a depth-first walk that visits
dependencies first. Do not edit the tests. Run pytest: all green. Then print the graph and the
leaves_first order, one function per line. Stop.
```

**What you should see (green):** graph lines as in the test; order starts `_split`, `canonical_key`, `duplicate_key` and every function appears after the ones it calls (so `merge_duplicates` comes after `group_records` and `merge_group`). The order is not unique; do not expect it to end on `merge_duplicates`.

**Predict first (30 seconds, ask the room before running):** Which function should be tested first, and which last?
**Expected answer:** First a function that needs nothing (_split). merge_duplicates only after the functions it calls.
**Common mistake / drift:** Claude hardcodes the graph. Say: "read the real source with ast".
