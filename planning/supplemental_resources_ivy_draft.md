# DSCT — supplemental resources draft (Ivy)

**Bite:** `foreman_interface/jobs/tasks/dsct_supplemental_resources_ivy.md`,
assigned by Flo at Jeremy's direct request, 2026-09-17. Trigger: an
unsolicited email from João Sarubbi (CEFET-MG) sharing his Discrete Math
YouTube collection, now DSCT's first Resources module entry (Canvas module
`219452`). This is the follow-on: don't stop at one lucky email.

**No Canvas contact was made to produce this list.** Every entry below is a
candidate for Anna to review and decide on — post, skip, or look closer —
before anything goes near DSCT course `74035`, module `219452`.

**How to read the verification tags:**
- **VERIFIED** — I (or the research pass I ran) actually opened the URL via
  WebFetch and confirmed it's real, on-topic, free, and not behind a
  login/paywall.
- **SEARCH-CONFIRMED** — the title/URL showed up consistently across
  independent search results (so it's very likely real and correctly
  described), but the page itself wasn't independently opened and read —
  usually because it's a YouTube/JS-heavy page that returns only boilerplate
  to a fetch tool. Anna should personally click these before trusting the
  content description, not just the existence.
- **GAP, honestly reported** — for a few topics I could not find a strong
  second resource (especially the "explains it differently" interactive
  kind) and am saying so rather than padding the list with a weak or
  unverified link.

The Bazett full-course playlist recurs across several weeks — it's one
durable series covering many topics well, not a sign I ran out of ideas.

---

## Week 1 — Reasoning Odyssey (intro, mindset)

1. **Introduction to Critical Thinking** (Khan Academy / Wi-Phi, Geoff Pynn)
   — https://www.khanacademy.org/partner-content/wi-phi/wiphi-critical-thinking/wiphi-fundamentals/v/intro-to-critical-thinking
   — *Video.* Short intro to what critical thinking is and what counts as
   an argument — general mindset framing, not discrete-math-specific, which
   fits Week 1's "intro/mindset" role rather than a topic week.
   **SEARCH-CONFIRMED** (WebFetch only returned the page shell — JS-rendered
   page — so the content itself wasn't independently read).

**Coverage note:** thin on purpose — Week 1 is explicitly a mindset/intro
week, not a technical topic, and I didn't force a second resource just to
hit a quota.

---

## Week 4 — Logic, Claims & Proof

1. **Discrete Math — Full Course** (Dr. Trefor Bazett, YouTube playlist) —
   https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS
   — *Video series.* Dedicated units on propositions, logical operators,
   truth tables, quantifiers, and proof techniques (direct, contrapositive,
   contradiction, induction) — a full alternate walkthrough of exactly
   Week 4's material, from a well-established free channel.
   **VERIFIED** (title and topic list confirmed via WebFetch; the fetch was
   truncated before it showed the channel name explicitly, but the playlist
   content itself was read).

**Coverage note:** one strong series is doing the work here; I didn't find
a second free, durable, differently-formatted resource (e.g., an
interactive proof-checker) I could verify — a proof-checker tool exists in
some closed/paywalled forms but nothing free/durable turned up. Worth Anna
flagging to Jeremy as a "look for later" rather than something I invented.

---

## Week 5 — Sets, Functions & Sequences

1. **Discrete Math — Full Course** (Bazett playlist, same link as Week 4)
   — dedicated units on sets, functions, and relations exist inside the
   same series; reuse the link, point students to the specific units rather
   than duplicating the whole-series entry.

**GAP, honestly reported:** I did not find a second, differently-formatted
resource (an interactive set/function-mapping visualizer would be the ideal
"explains it differently" fit here) that I could verify as free and
durable. This week is genuinely thin in my research pass — flag to Anna
rather than padding it.

---

## Week 6 — Algorithms, Correctness & Growth

1. **Big-O Notation Visualizer** —
   https://basicfreetools.com/big-o-notation-visualizer/
   — *Interactive tool.* Drag an input-size slider and compare O(1) through
   O(n!) curves side by side with operation counts and estimated real-world
   timing — a numeric/graphical way to build Big-O intuition that a lecture
   can't easily replicate live.
   **VERIFIED** (WebFetch confirmed: free, no sign-up, runs client-side).
2. **Big O Analysis** (GeeksforGeeks) —
   https://www.geeksforgeeks.org/dsa/analysis-algorithms-big-o-analysis/
   — *Article.* Standard reference-style explainer on Big-O with worked
   examples; useful as a plain-text companion to the visualizer above.
   **SEARCH-CONFIRMED only** — seen in search results, not independently
   fetched/read. Anna should personally check it (GeeksforGeeks articles
   are usually solid but occasionally have ad-heavy or stale pages).

---

## Week 7 — Integer Properties & Cryptography

1. **Fun With Modular Arithmetic** (BetterExplained) —
   https://betterexplained.com/articles/fun-with-modular-arithmetic/
   — *Article.* Explains modular arithmetic via the "clock math" analogy
   and connects it directly to cryptography and hash tables — a genuinely
   different intuition-first angle than a formal congruence-class
   definition.
   **VERIFIED** (WebFetch confirmed: free, no login).
2. **RSA Visual** (CrypTool) —
   https://legacy.cryptool.org/en/cto/rsa-visual
   — *Interactive tool.* Runs entirely client-side (no login); lets
   students step through RSA key generation, encryption, and decryption
   with two different geometric visualizations of modular exponentiation —
   strong fit for the "simple crypto" part of this week.
   **VERIFIED** (WebFetch confirmed: free, client-side, no login).
3. **RSA Algorithm in Cryptography** (GeeksforGeeks) —
   https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/
   — *Article.* Covers the underlying math (totient function, encryption/
   decryption formulas) with a worked numeric example — a text companion to
   the interactive tool above.
   **VERIFIED** (WebFetch confirmed: free, no paywall).

---

## Week 8 — Induction, Recursion & Recurrences

1. **Recursion Tree Visualizer** — https://recursion.vercel.app/
   — *Interactive tool.* Animates recursive calls (e.g., Fibonacci) as an
   expanding call tree, step by step — a genuinely different visual angle
   on recursion than a chalkboard proof, and a natural bridge into "where
   is the logical bridge" induction questions.
   **VERIFIED** (WebFetch confirmed: free, no login).
2. **CS Unplugged — Activities** — https://classic.csunplugged.org/activities/
   — *Hands-on/article resource, non-digital.* Free, open/CC-licensed.
   **Caveat, stated honestly:** I could not confirm a standalone
   induction/recursion-named activity on the site during this pass — the
   closest matches are the sorting/searching and "divide and conquer"
   activities, which are adjacent but not a precise topic match. Anna
   should treat this as "look closer before posting," not a confirmed fit.
   **VERIFIED the site itself** (free, real, CC-licensed) but **not
   verified as topic-precise** for induction/recursion specifically.

---

## Week 9 — Counting & Combinatorial Reasoning

1. **The Pigeonhole Principle: Theorem, Statement & Examples**
   (GeeksforGeeks) —
   https://www.geeksforgeeks.org/engineering-mathematics/discrete-mathematics-the-pigeonhole-principle/
   — *Article.* Covers basic and generalized pigeonhole with worked
   examples and practice problems.
   **VERIFIED** (WebFetch confirmed: free, no login).

**GAP, honestly reported:** I specifically searched for an interactive
pigeonhole/combinatorics visualizer (the highest-value format for this
topic per the "explains it differently" goal) and did not find one worth
recommending. Flag to Anna/Jeremy as a real open gap rather than a resource
I'm pretending exists.

---

## Week 10 — Probability, Uncertainty & Evidence

1. **Bayes' theorem, the geometry of changing beliefs** (3Blue1Brown) —
   lesson page https://www.3blue1brown.com/lessons/bayes-theorem (video:
   https://www.youtube.com/watch?v=HZGCoVF3YvM)
   — *Video.* Addresses the base-rate fallacy directly through the
   "librarian vs. farmer" thought experiment and an area-diagram visual
   method — an unusually strong match for Week 10's own critical-thinking
   question ("how do base rates... fool us?").
   **VERIFIED the official 3blue1brown.com lesson page** (free, official,
   on-topic). **The YouTube URL itself returned only footer boilerplate on
   fetch** — treat the video's existence/content as corroborated via the
   official lesson page and search results, not independently opened on
   YouTube directly.

**GAP, honestly reported:** I looked specifically for a free interactive
probability/Monte-Carlo simulator aimed at base-rate or independence
fallacies and did not find a durable one worth recommending. Real gap, not
filled with a weak substitute.

---

## Week 11 — Relations, Equivalence, Partial Orders, Matrices & Digraphs

1. **Equivalence Relations!** (Dr. Trefor Bazett) —
   https://www.youtube.com/watch?v=7YDx3oWQQHI
   — *Video* (~17 min). Dedicated walkthrough of equivalence relations,
   same trusted series as Weeks 4-5.
   **SEARCH-CONFIRMED only** — title and runtime corroborated across
   sources, not independently opened.
2. **Hasse Diagrams** (GeeksforGeeks) —
   https://www.geeksforgeeks.org/engineering-mathematics/discrete-mathematics-hasse-diagrams/
   — *Article.* Covers poset construction, maximal/minimal elements, and
   Hasse diagram rules — directly supports the partial-order half of this
   week.
   **VERIFIED** (WebFetch confirmed: free, no login).

**GAP, honestly reported:** I looked for a dedicated interactive Hasse-
diagram/poset-builder tool (the ideal "different format" fit here) and
didn't find a durable free one — most results were R packages requiring
programming, not a student-facing tool. Real gap.

---

## Week 12 — Graphs & Network Reasoning

1. **VisuAlgo — Graph Traversal (DFS/BFS)** —
   https://visualgo.net/en/dfsbfs
   — *Interactive tool.* Build or select a graph and step through DFS/BFS,
   topological sort, bipartite checking, bridges/cut-vertices, and strongly
   connected components — one of the best-known free discrete-math
   visualization sites, core use is login-free.
   **VERIFIED** (WebFetch confirmed).
2. **VisuAlgo — Single-Source Shortest Paths** —
   https://visualgo.net/en/sssp
   — *Interactive tool* (same site). Visualizes BFS/Dijkstra/Bellman-Ford
   for shortest-path reasoning — good fit for "are we solving the graph
   correctly" Week 12 framing.
   **VERIFIED via the site's category-page fetch**, same session as #1.
3. **Graph Theory** (Sarada Herke, YouTube playlist) —
   https://www.youtube.com/playlist?list=PLoJC20gNfC2gmT_5WgwYwGMvgCjYVsIQg
   — *Video series.* Search results indicate dedicated Euler-trail and
   Hamiltonian-graph videos specifically, which matches Week 12's
   "Euler/Hamilton as appropriate" line directly.
   **SEARCH-CONFIRMED only** — not independently opened; Anna should
   confirm the Euler/Hamilton videos are actually in this playlist before
   posting.

---

## Week 13 — Trees, Search & Decision Structures

1. **VisuAlgo — Binary Search Tree / AVL** and **Minimum Spanning Tree
   (Prim/Kruskal)** — both under https://visualgo.net/en
   — *Interactive tools* (same site as Week 12). Tree traversal, BST/AVL
   visualizations, and MST/spanning-tree visualizations with both Prim's
   and Kruskal's algorithms — direct fit for "rooted trees, traversal,
   spanning/decision trees."
   **VERIFIED** (WebFetch confirmed via the site's category page: free,
   no login required for core use).

**Coverage note:** VisuAlgo alone covers Weeks 12-13 well since it's one
consistently strong, free, no-login site — not a sign I stopped looking,
just a genuinely dominant resource for this material.

---

## Week 14 — Boolean Algebra, Circuits & Finite-State Machines

1. **Karnaugh Map Solver** — https://karnaughmapsolver.com/
   — *Interactive tool.* Simplifies Boolean expressions via K-map, truth
   table, expression, or minterm input, shows step-by-step grouping, and
   auto-generates a circuit diagram — directly useful for the "equivalence
   under every assignment" / simplification half of Week 14.
   **VERIFIED** (WebFetch confirmed: free, no login).
2. **Automaton Simulator** — https://automatonsimulator.com/
   — *Interactive tool.* Build and run DFAs/NFAs/PDAs visually, test
   string acceptance, share a built automaton via URL — strong, precise
   fit for the finite-state-machine half of Week 14.
   **VERIFIED** (WebFetch confirmed: free, no login).
3. **Making Logic Gates from Transistors** (Ben Eater, YouTube) —
   search results place this on Ben Eater's channel (eater.net), ~13 min,
   builds NAND/XOR/inverter from real transistors.
   **SEARCH-CONFIRMED only** — not independently opened; verify the exact
   URL before posting (I did not want to guess a video ID I hadn't
   confirmed).
4. VisuAlgo's DFS/BFS module (linked under Week 12) also includes a
   **2-SAT satisfiability checker**, confirmed in the same WebFetch pass as
   Week 12's entries — directly relevant to the SAT portion of this week;
   worth cross-linking rather than a new entry.

---

## Summary for Anna

- **Post-ready (VERIFIED, on-topic, free, no login):** Week 4 Bazett
  playlist; Week 6 Big-O Visualizer; Week 7 all three (BetterExplained,
  CrypTool RSA Visual, GeeksforGeeks RSA); Week 8 Recursion Tree Visualizer;
  Week 9 GeeksforGeeks pigeonhole; Week 10 3Blue1Brown Bayes lesson page;
  Week 11 Hasse Diagrams article; Week 12 both VisuAlgo entries; Week 13
  VisuAlgo BST/AVL/MST; Week 14 Karnaugh Map Solver and Automaton Simulator.
- **Needs a closer look before posting (SEARCH-CONFIRMED only, or a
  verified-but-imprecise match):** Week 1 Khan Academy video; Week 6
  GeeksforGeeks Big-O article; Week 8 CS Unplugged (real site, imprecise
  topic match); Week 11 Bazett equivalence-relations video; Week 12 Sarada
  Herke playlist; Week 14 Ben Eater video (URL not confirmed).
- **Real, honestly-reported gaps — no resource found, not filled with a
  weak substitute:** Week 5 second resource (interactive set/function
  tool); Week 9 interactive pigeonhole/combinatorics tool; Week 10
  interactive probability/base-rate simulator; Week 11 interactive
  Hasse-diagram builder.

IVY BITE dsct-supplemental-resources READY FOR ANNA
