"""Week 6: Recursive Fibonacci full trace.

Purpose
-------
Make the *work* of naive recursive Fibonacci visible.

By default this script traces fib(0) through fib(5). For each run it prints
every algorithm-level operation we deliberately count:

    CALL        enter fib(n)
    COMPARE     evaluate n <= 1
    SUBTRACT    compute n - 1 or n - 2
    ASSIGN      store a returned recursive result
    ADD         combine the two recursive results
    RETURN      return from fib(n)

Important:
This is a teaching model of algorithmic work, not a count of Python bytecode,
CPU instructions, print statements, or tracing overhead. That distinction is
useful when we begin talking about Big O: we choose meaningful operations,
then study how the count grows as n grows.
"""

MAX_N = 5


def trace_fibonacci(start_n):
    """Trace one complete recursive Fibonacci calculation."""

    counters = {
        "calls": 0,
        "comparisons": 0,
        "subtractions": 0,
        "assignments": 0,
        "additions": 0,
        "returns": 0,
        "max_depth": 0,
    }

    event_number = 0

    def show(depth, operation, detail):
        """Print one numbered trace event."""
        nonlocal event_number
        event_number += 1
        indent = "    " * depth
        print(f"{event_number:03d} | depth {depth:<2} | {indent}{operation:<10} {detail}")

    def fib(n, depth=0):
        """Naive recursive Fibonacci, instrumented one operation at a time."""

        counters["calls"] += 1
        counters["max_depth"] = max(counters["max_depth"], depth)
        show(depth, "CALL", f"fib({n})")

        counters["comparisons"] += 1
        is_base_case = n <= 1
        show(depth, "COMPARE", f"{n} <= 1 -> {is_base_case}")

        if is_base_case:
            counters["returns"] += 1
            show(depth, "RETURN", f"fib({n}) -> {n}  [base case]")
            return n

        counters["subtractions"] += 1
        left_input = n - 1
        show(depth, "SUBTRACT", f"{n} - 1 -> {left_input}")

        left_result = fib(left_input, depth + 1)

        counters["assignments"] += 1
        show(depth, "ASSIGN", f"left_result = {left_result}")

        counters["subtractions"] += 1
        right_input = n - 2
        show(depth, "SUBTRACT", f"{n} - 2 -> {right_input}")

        right_result = fib(right_input, depth + 1)

        counters["assignments"] += 1
        show(depth, "ASSIGN", f"right_result = {right_result}")

        counters["additions"] += 1
        result = left_result + right_result
        show(depth, "ADD", f"{left_result} + {right_result} -> {result}")

        counters["returns"] += 1
        show(depth, "RETURN", f"fib({n}) -> {result}")
        return result

    print()
    print("=" * 86)
    print(f"FULL RECURSIVE TRACE: fib({start_n})")
    print("=" * 86)

    answer = fib(start_n)

    counted_operations = (
        counters["calls"]
        + counters["comparisons"]
        + counters["subtractions"]
        + counters["assignments"]
        + counters["additions"]
        + counters["returns"]
    )

    print()
    print("-" * 86)
    print(f"RESULT: fib({start_n}) = {answer}")
    print("-" * 86)
    print(f"Function calls : {counters['calls']}")
    print(f"Comparisons    : {counters['comparisons']}")
    print(f"Subtractions   : {counters['subtractions']}")
    print(f"Assignments    : {counters['assignments']}")
    print(f"Additions      : {counters['additions']}")
    print(f"Returns        : {counters['returns']}")
    print(f"Max call depth : {counters['max_depth']}")
    print(f"TOTAL COUNTED  : {counted_operations}")

    return {
        "n": start_n,
        "answer": answer,
        **counters,
        "counted_operations": counted_operations,
    }


def print_growth_summary(results):
    """Put fib(0)..fib(5) side by side so growth is easy to discuss."""

    print()
    print("=" * 86)
    print("GROWTH SUMMARY")
    print("=" * 86)
    print(
        f"{'n':>3} | {'fib(n)':>6} | {'calls':>6} | {'compares':>8} | "
        f"{'arith':>6} | {'assign':>6} | {'returns':>7} | {'total':>6}"
    )
    print("-" * 86)

    for row in results:
        arithmetic = row["subtractions"] + row["additions"]
        print(
            f"{row['n']:>3} | "
            f"{row['answer']:>6} | "
            f"{row['calls']:>6} | "
            f"{row['comparisons']:>8} | "
            f"{arithmetic:>6} | "
            f"{row['assignments']:>6} | "
            f"{row['returns']:>7} | "
            f"{row['counted_operations']:>6}"
        )

    print()
    print("DISCUSSION QUESTIONS")
    print("1. Which fib(n) calls are repeated?")
    print("2. What happens to the number of calls when n increases by just 1?")
    print("3. Are we doing new useful work, or repeating work we already did?")
    print("4. If fib(5) already needs this many calls, what do you predict for fib(10)?")
    print()
    print(
        "Big-O teaser: the important story is not the exact operation total. "
        "It is how quickly the amount of work grows."
    )


def main():
    print("NAIVE RECURSIVE FIBONACCI: WATCH THE WORK GROW")
    print()
    print(
        "We will trace fib(0) through fib(5). "
        "Indentation shows recursive call depth."
    )

    results = []

    for n in range(MAX_N + 1):
        results.append(trace_fibonacci(n))

    print_growth_summary(results)


if __name__ == "__main__":
    main()
