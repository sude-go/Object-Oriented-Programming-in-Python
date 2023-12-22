"""
if k is not divisible by a prime factor, it cannot be divisible by any other factors
"""


def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True


def take_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [num for num in range(2, n + 1) if is_prime[num]]
    return primes


num = int(input("Enter the number: "))

primes = take_primes(num)
print(f"Prime numbers less than or equal to {num}: {primes}")
