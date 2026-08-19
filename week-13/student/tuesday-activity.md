# Tuesday activity — Can this hierarchy support the claim?

Work individually first. Your instructor will provide the diagram below or an
equivalent local scenario.

```text
                         Start
                       /       \
                 eligible?     not eligible
                 /      \
             yes         no
             /             \
        needs aid?       explain rule
          /    \
        yes     no
       /         \
   aid route   standard route
```

The original intake notes also say that some students on the aid route need a
language-access review before the route is usable. That relationship is not
shown in the tree.

## 1. Sources

Identify the supplied diagram and intake note as your sources. Do not claim
facts about a real admissions, benefits, or student system from this example.

## 2. Rules / assumptions

Define `root`, `internal node`, `leaf`, and one traversal. State what each
decision question means and whether every person is assumed to receive exactly
one answer at each split.

## 3. Work

1. Label every root-to-leaf route with its decision outcomes.
2. Write the preorder and breadth-first visit order for the diagram.
3. Trace the route for a person who is eligible and needs aid.
4. Add the language-access review as either a new node or an explicit
   limitation. Explain why you made that choice.

## 4. Check your answer

Use a second traversal or a partner's trace to check one route. Then answer:
does the displayed tree justify the claim “everyone routed to aid can use the
aid route immediately”? Give the missing relationship or condition that bears
on your answer.

## 5. One-sentence summary

Write one sentence that states what the tree can establish and what it cannot.

## AI Fluency check

If an AI tool offers a tree or traversal, treat it as a proposal. Compare its
nodes and edges against the supplied information. A clean diagram is not
evidence that it preserved all relevant relationships. Record one specific
thing you checked; if you did not use AI, state the check you would require
before trusting an AI-generated hierarchy.
