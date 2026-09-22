"""Week 6: the simplest recursive Fibonacci example."""

def fibonacci(n):
    # STUDENT LEARNING: Recursion needs a stopping point.
    if n <= 1:
        return n

    # STUDENT LEARNING: The function solves a problem by calling itself
    # on two smaller versions of the same problem.
    return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(4):
    print(f"fib({n}) = {fibonacci(n)}")
