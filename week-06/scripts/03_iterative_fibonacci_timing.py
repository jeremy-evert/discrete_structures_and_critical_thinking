"""Week 6: Iterative Fibonacci timing race.

Run the same targets as the recursive 60-second race, but use iteration.
"""

import time


TARGETS = [1, 5, 10, 20, 30, 40, 50]


def fibonacci_iterative(n):
    """Return fib(n) by repeatedly updating the previous two values."""
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def main():
    print("ITERATIVE FIBONACCI: SAME TARGETS")
    print("=" * 68)
    print(f"Targets: {TARGETS}")
    print()

    overall_start = time.perf_counter()

    for n in TARGETS:
        start = time.perf_counter()
        answer = fibonacci_iterative(n)
        elapsed = time.perf_counter() - start

        print(
            f"fib({n:>2}) = {answer:<12} "
            f"time = {elapsed:12.9f} seconds"
        )

    total_elapsed = time.perf_counter() - overall_start

    print()
    print("=" * 68)
    print(f"COMPLETED TARGETS: {len(TARGETS)} of {len(TARGETS)}")
    print(f"TOTAL ELAPSED:     {total_elapsed:.9f} seconds")
    print()
    print("STUDENT QUESTION:")
    print("Same answers. What changed about the amount of repeated work?")


if __name__ == "__main__":
    main()
