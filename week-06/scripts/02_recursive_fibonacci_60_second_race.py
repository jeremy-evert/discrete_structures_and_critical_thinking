"""Week 6: Naive recursive Fibonacci 60-second race.

Try the same Fibonacci targets in order and see how far naive recursion
can get before the class has waited 60 seconds total.
"""

import multiprocessing as mp
import time


TARGETS = [1, 5, 10, 20, 30, 40, 50]
TIME_LIMIT_SECONDS = 60


def fibonacci_recursive(n):
    """Return fib(n) using the intentionally naive recursive algorithm."""
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def worker(n, output_queue):
    """Run one Fibonacci calculation in a child process."""
    answer = fibonacci_recursive(n)
    output_queue.put(answer)


def main():
    print("NAIVE RECURSIVE FIBONACCI: 60-SECOND RACE")
    print("=" * 68)
    print(f"Targets: {TARGETS}")
    print(f"Total time budget: {TIME_LIMIT_SECONDS} seconds")
    print()
    print("We will try each target in order.")
    print("If the 60-second classroom budget expires, we stop.")
    print()

    overall_start = time.perf_counter()
    completed = 0

    for n in TARGETS:
        elapsed_total = time.perf_counter() - overall_start
        remaining = TIME_LIMIT_SECONDS - elapsed_total

        if remaining <= 0:
            print(f"fib({n:>2}) -> NOT STARTED: 60-second budget already used")
            break

        output_queue = mp.Queue()
        process = mp.Process(target=worker, args=(n, output_queue))

        start = time.perf_counter()
        process.start()
        process.join(timeout=remaining)
        elapsed = time.perf_counter() - start

        if process.is_alive():
            process.terminate()
            process.join()
            print(
                f"fib({n:>2}) -> NOT FINISHED after {elapsed:8.4f} seconds "
                f"(60-second total budget reached)"
            )
            break

        if process.exitcode != 0 or output_queue.empty():
            print(f"fib({n:>2}) -> ERROR")
            break

        answer = output_queue.get()
        completed += 1
        print(
            f"fib({n:>2}) = {answer:<12} "
            f"time = {elapsed:10.6f} seconds"
        )

    total_elapsed = time.perf_counter() - overall_start

    print()
    print("=" * 68)
    print(f"COMPLETED TARGETS: {completed} of {len(TARGETS)}")
    print(f"TOTAL ELAPSED:     {total_elapsed:.3f} seconds")

    if completed < len(TARGETS):
        next_target = TARGETS[completed]
        print(f"FIRST TARGET NOT COMPLETED: fib({next_target})")

    print()
    print("STUDENT QUESTION:")
    print("The code is correct. So what is going wrong as n grows?")


if __name__ == "__main__":
    # spawn is explicit so this behaves predictably across Windows/WSL/macOS.
    mp.set_start_method("spawn")
    main()
