user_input = input("Enter a string: ")
words = []

while user_input not in words:
    words.append(user_input)
    print(words)
    user_input = input("Enter a string: ")
print("You already entered", user_input)
