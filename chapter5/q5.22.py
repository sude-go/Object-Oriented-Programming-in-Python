def factorial(k):
    if k < 0:
        return "Factorial is undefined for negative numbers."
    result = 1
    for i in range(k):
        result *= (k - i)
    return result


num = int(input("Enter a non-negative integer (k): "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")
