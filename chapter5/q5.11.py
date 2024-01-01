"""
You can check whether one string is contained as a substring of another
using the built-in syntax 'era' in 'average'. Implement such a test on your
own. Do not use any behaviors of the string class other than the fact that strings are
a sequence of characters.
"""


def is_substring(sub, main):
    sub_len = len(sub)
    main_len = len(main)

    for i in range(main_len - sub_len + 1):
        if all(main[i + j] == sub[j] for j in range(sub_len)):
            return True
    return False


# Example usage:
main_string = str(input("Enter a string: "))
substring = str(input("Enter a substring: "))

result = is_substring(substring, main_string)

if result:
    print(f"'{substring}' is a substring of '{main_string}'.")
else:
    print(f"'{substring}' is not a substring of '{main_string}'.")
