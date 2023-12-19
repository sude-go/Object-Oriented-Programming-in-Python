"""
The precise value of the mathematical constant π is equal to the following
infinite series:
π = 4 ·((1/1) − (1/3) + (1/5) − (1/7) + · · ·)
Although we cannot compute the entire infinite series, we get an approximation to
the value by computing the beginning of such a sequence. Write a program that
approximates π by computing the first n terms, for some n.
"""


def approximate_pi(n):
    result = 0
    sign = 1

    for i in range(1, 2 * n, 2):
        term = 1 / i
        result += sign * term
        sign *= -1

    result *= 4

    return result


n_terms = 1000
approximation = approximate_pi(n_terms)

print(f"Approximation of π using {n_terms} terms: {approximation}")
