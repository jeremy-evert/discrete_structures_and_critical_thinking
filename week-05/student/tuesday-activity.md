# Tuesday activity — What did the mapping hide?

An advising system records a student's completed courses as a **set**. It
uses a function `next(S)` that maps a set of completed courses `S` to one
recommended next course.

1. State a plausible domain and codomain for `next`. Be specific about what a
   valid input and output are.
2. Explain why two students with the same completed-course set might still
   need different advice. Name a distinction the set representation omits.
3. Let `eligible(S)` return `true` when `S` contains the prerequisites for a
   course. Trace `eligible(S)` for one concrete set you choose.
4. Suppose a second function `notify` maps `true` to “send registration
   message” and `false` to “show prerequisite explanation.” Trace
   `(notify ∘ eligible)(S)`.
5. Write a sequence of three semester snapshots for one student and state one
   rule that produces the next snapshot.

Use Sources, Rules/Assumptions, Work, Check, and One-Sentence Summary. For
your check, change one course in the set and confirm whether your rule and
composition still make sense.

## AI fluency prompt

If AI proposes a mapping, write down its domain and codomain before using it.
Then test an input at the boundary (an empty set, a completed set with a
missing prerequisite, or another valid edge case). A plausible diagram is not
evidence that the mapping preserved the intended distinction.
