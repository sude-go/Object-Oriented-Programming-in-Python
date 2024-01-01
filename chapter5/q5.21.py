"""
n
∑ k^2
k=1
"""


def sum_of_squares(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2
    return result


n = int(input("Enter a positive integer (n): "))
result = sum_of_squares(n)
print(f"The sum of the squares of the first {n} positive integers is: {result}")
