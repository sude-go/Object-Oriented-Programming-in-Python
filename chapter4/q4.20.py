"""
result will be:
0 is divisible by 9
3 is divisible by 3
6 is divisible by 3
9 is divisible by 9
12 is divisible by 3
15 is divisible by 3
18 is divisible by 9
"""

for x in range(20):
    if x % 9 == 0:
        print(x, 'is divisible by 9')
    elif x % 3 == 0:
        print(x, 'is divisible by 3')
