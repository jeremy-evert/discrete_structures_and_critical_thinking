def factorial_doll(size, level=0):
    print("  " * level + f"Opening doll {size}")

    if size == 1:
        print("  " * level + "Tiny doll found!")
        return 1

    result = size * factorial_doll(size - 1, level + 1)

    print("  " * level + f"Closing doll {size}")
    print("  " * level + f"{size}! = {result}")

    return result


n = int(input("Starting doll size: "))

if n < 1:
    print("Please enter a positive number.")
else:
    answer = factorial_doll(n)
    print(f"\nFinal Answer: {n}! = {answer}")