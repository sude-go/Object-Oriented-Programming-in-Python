"""
An integer k ≥ 2 is a prime number if it is not evenly divisible by any
numbers in range(2,k). Build a list of all prime numbers less than or equal to a
value n entered by a user. For each 2 ≤ k ≤ n, test its primality by looping over
range(2,k) looking for a factor of k.
"""


def is_prime(k):
    if k < 2:
        return False
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True


def take_primes(n):
    primes = []
    for k in range(2, n + 1):
        if is_prime(k):
            primes.append(k)
    return f"{primes}"


num = int(input("Enter the number: "))
print(is_prime(num))
print(take_primes(num))
