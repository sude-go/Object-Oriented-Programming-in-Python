"""
u = int(input('Enter first number: '))
v = int(input('Enter second number: '))
smallest = min(u, v)
gcd = 1

for d in range(2, smallest + 1):
    if u % d == 0 and v % d == 0:
        gcd = gcd * d
        u = u / d
        v = v / d
print('The gcd is', gcd)

Algorithm fails :
u = 36
v = 48
result = 6 -> should be 12
to fix it:
 - Replaced the division (/) with integer division (//) to update u and v.
 - Changed the condition in the loop to a while loop, ensuring that the loop continues
 as long as both u and v are divisible by d.
"""

u = int(input('Enter first number: '))
v = int(input('Enter second number: '))
smallest = min(u, v)
gcd = 1

for d in range(2, smallest + 1):
    while u % d == 0 and v % d == 0:
        gcd = gcd * d
        u = u // d
        v = v // d

print('The gcd is', gcd)
