


def count_primes(num):
    count = 0
    for i in range(2, num + 1):
        if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)):
            count += 1
    return count


num = 40
prime_count = count_primes(num)

print("The number of prime numbers in the range from zero to given num is:", prime_count)
