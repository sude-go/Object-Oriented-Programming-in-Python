n = int(input('Enter a number: '))
base = int(input('Enter a base number: '))

if base < 2 or base > 9:
    raise ValueError("Base must be between 2 and 9 inclusive.")

result = " "

while n > 0:
    q = n // base
    r = n % base
    result = str(r) + result
    n = q
print(result)
