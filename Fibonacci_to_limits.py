def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Get the number of Fibonacci numbers from the user
n = int(input("Enter the number of Fibonacci numbers to print: "))

# Print the Fibonacci sequence up to the specified number
for i in range(n):
    print(fibonacci(i))

