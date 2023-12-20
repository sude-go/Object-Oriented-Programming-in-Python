def convert_to_decimal(num_str, base):
    decimal_value = 0
    num_str = num_str[::-1]

    for i, symbol in enumerate(num_str):
        if symbol.isdigit():
            value = int(symbol)
        else:
            value = 10 + ord(symbol.upper()) - ord('A')

        decimal_value += value * (base ** i)

    return decimal_value


hexadecimal_value = input("Enter the hexadecimal value: ")
base = int(input("Enter the base (up to 36): "))

if 2 <= base <= 36:
    decimal_result = convert_to_decimal(hexadecimal_value, base)
    print(f"The decimal equivalent of {hexadecimal_value} in base {base} is: {decimal_result}")
else:
    print("Invalid base. Please enter a base between 2 and 36.")
