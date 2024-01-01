def decimal_to_base(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36 inclusive.")

    result = " "

    while num > 0:
        r = num % base
        if r < 10:
            result = str(r) + result
        else:
            result = chr(ord('A') + r - 10) + result
        q = num // base
        num = q
    return result


num = int(input("Enter a number: "))
base = int(input("Enter a base: "))
result = decimal_to_base(num, base)
print(result)
