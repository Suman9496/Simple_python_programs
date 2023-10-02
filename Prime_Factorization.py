def prime_factorization(number):


    prime_factors = []
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            prime_factors.append(i)
            number //= i
    if number > 1:
        prime_factors.append(number)
    return prime_factors


# Example usage:

print(prime_factorization(100))


