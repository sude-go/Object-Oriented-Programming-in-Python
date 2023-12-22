def dramatic(original):
    result = ""
    for char in original:
        result += char * 2
    return result


given_string = input("Enter a string: ")
result_string = dramatic(given_string)
print(result_string)
