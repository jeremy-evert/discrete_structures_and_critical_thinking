# Prompt 05 — Find the missing transition

Why: a model validator can expose what the state machine forgot to represent.

Slide reference: Week 14 Tuesday, the model-limit check.

```prompt-a
Write a validator for a finite-state machine whose declared states are Locked and Open and whose input alphabet is valid and timeout. The intentionally incomplete transition table contains (Locked, valid) -> Open, (Locked, timeout) -> Locked, and (Open, valid) -> Open. List every missing (state, input) pair in deterministic order. The validator must identify exactly (Open, timeout) as the missing transition needed by the badge trace. Do not assume an implicit self-loop counts as a declared transition. Explain in one sentence what this validator can establish and what it cannot establish about a real access system.
```

Expected observable result: the missing-transition list names exactly
`("Open", "timeout")`; an implicit self-loop is not accepted as a declaration.

Predict first: which state/input pair is absent from the incomplete model?

Likely AI drift: it may fill the gap automatically, report only a count, or
claim the model proves real authorization.

Recovery: enumerate the Cartesian product of declared states and inputs, then
compare it with the explicit transition keys.
