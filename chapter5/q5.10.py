import math


def approximate_pi_with_accuracy(accuracy):
    result = 0
    sign = 1
    approximation = 0
    iteration = 0

    while abs(approximation - math.pi) > accuracy:
        term = 1 / (2 * iteration + 1)
        result += sign * term
        sign *= -1
        approximation = 4 * result
        iteration += 1

    return approximation, iteration


desired_accuracy = 1e-6
approximation, iterations = approximate_pi_with_accuracy(desired_accuracy)

print(f"Approximation of π with accuracy within {desired_accuracy}: {approximation}")
print(f"Number of iterations: {iterations}")
