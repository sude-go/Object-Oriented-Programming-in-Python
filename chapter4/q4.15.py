base = int(input("Enter the base: "))
string = input("Enter the string: ")


def convert(string, base):
    value = 0
    for i in range(len(string)):
        value += int(string[i]) * base ** (len(string) - i - 1)
    return value


print("The value is: ", convert(string, base))
