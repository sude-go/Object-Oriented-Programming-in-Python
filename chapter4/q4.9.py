"""
Write a program that prints an n-level staircase made of text
"""

n = int(input("Enter the number of steps: "))
text = input("Enter the text: ")
for i in range(n):
    print(" " * (n - i - 1) + text * (i + 1))
