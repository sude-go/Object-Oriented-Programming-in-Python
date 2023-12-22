def from_decimal(value, base):
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36 inclusive.")

    if value == 0:
        return "0"

    result = ""
    while value > 0:
        remainder = value % base
        result = str(int(remainder)) + result
        value //= base

    return result


input_value = int(input("Enter an integer value: "))
input_base = int(input("Enter the base to convert to (2 to 36): "))

result = from_decimal(input_value, input_base)
print(f"The representation of {input_value} in base {input_base} is: {result}")
