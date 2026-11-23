# Tuesday activity — A positive result is not a probability of truth

A clinic screens for a condition present in 1% of a population. Sensitivity is
90%; specificity is 95%. Consider 10,000 screened people. Define `C` as “has
the condition” and `+` as “tests positive.”

## Sources and rules

Use only the stated rates. State what sensitivity and specificity mean; assume
they apply to this population. Name one reason that assumption could be unsafe.

## Work

1. Build counts for `C/+`, `C/-`, `not C/+`, and `not C/-`.
2. Calculate `P(C | +)`.
3. An AI answer claims a positive is correct 90% of the time because the test
   is 90% sensitive. Identify the conditional probability it confused.

## Check and summary

Check that cells total 10,000 and the positive column is your denominator.
Change prevalence to 20%, predict the effect on `P(C | +)`, then calculate.
Write one bounded sentence reporting the 1% result and base-rate boundary.
Keep this trace for the Decision Gate.
