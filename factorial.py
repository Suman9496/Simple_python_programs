def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    print("The factorial of 5 is:", factorial(5))


main()
