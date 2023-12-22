def to_decimal(string, base):
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36 inclusive.")

    value = 0

    for i in string:
        digit = int(i, base=base)
        value = value * base + digit
    return value


try:
    input_string = input("Enter a string representing a number: ")
    input_base = int(input("Enter the base of the number: "))

    result = to_decimal(input_string, input_base)
    print(f"The decimal value of '{input_string}' in base {input_base} is: {result}")

except ValueError as ve:
    print(ve)
