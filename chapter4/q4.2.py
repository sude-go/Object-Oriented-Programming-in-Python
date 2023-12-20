"""
Given the string original create a new string dramatic that
has two consecutive copies of each letter from the original string.
"""

given_string = input("Enter a string: ")
dramatic = ""
for char in given_string:
    dramatic += char * 2
print(dramatic)
