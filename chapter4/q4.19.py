"""
Write a block of code that does the following. Assuming that words is a
list of strings, generate a new list shortWords that includes all of the original strings
with length 3 or less.
"""

words = ["hi", "world", "this", "is", "a", "javascript", "of", "the", "html", "css", "system"]
shortWords = []

for word in words:
    if len(word) <= 3:
        shortWords.append(word)

print(shortWords)