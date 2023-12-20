"""
factorial
"""

# Get the number
k = int(input("Enter a number: "))

# Calculate the factorial
factorial = 1
for i in range(k):
    factorial *= (k - i)

print(factorial)
